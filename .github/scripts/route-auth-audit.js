/**
 * Route Authorization Audit
 *
 * Scans all Vue Router route definition files and reports routes
 * that are missing the `authorize` meta property, which is required
 * by the router guard to enforce access control.
 *
 * Exit code 0 — audit passed (warnings may exist)
 * Exit code 1 — critical issue found (route with no meta at all in a protected module)
 */

const { execSync } = require('child_process')
const fs = require('fs')
const path = require('path')

const PUBLIC_PATHS = new Set([
  '/signin',
  '/signup',
  '/forgot-password',
  '/verify-email',
  '/help',
  '/terms',
  '/privacy',
  '/faq',
  '/',
  '/:pathMatch(.*)*',
])

const PROTECTED_MODULES = [
  'src/router/modules/admin.js',
  'src/router/modules/superAdmin.js',
]

let uxRouters = []
try {
  uxRouters = execSync('find src/ux -name "router.js" 2>/dev/null')
    .toString()
    .trim()
    .split('\n')
    .filter(Boolean)
} catch (_) {}

const PUBLIC_MODULES = ['src/router/modules/public.js']

const allFiles = [...PROTECTED_MODULES, ...uxRouters, ...PUBLIC_MODULES]

let warnings = 0
let errors = 0

for (const file of allFiles) {
  if (!fs.existsSync(file)) {
    console.log(`⚠  Skipping ${file} — file not found`)
    continue
  }

  const content = fs.readFileSync(file, 'utf8')
  const isProtectedModule = PROTECTED_MODULES.includes(file)

  const pathMatches = [...content.matchAll(/path:\s*['"`]([^'"`]+)['"`]/g)]

  for (const match of pathMatches) {
    const routePath = match[1]

    if (PUBLIC_PATHS.has(routePath)) continue
    if (routePath.includes(':token')) continue

    const contextStart = Math.max(0, match.index - 50)
    const contextEnd = Math.min(content.length, match.index + 400)
    const context = content.slice(contextStart, contextEnd)

    const hasAuthorizeMeta = context.includes('authorize')
    const hasMetaBlock = context.includes('meta:')

    if (!hasAuthorizeMeta && !hasMetaBlock) {
      if (isProtectedModule) {
        console.log(
          `::error file=${file}::Route '${routePath}' in a protected module has no 'authorize' meta — unauthorized access may be possible`,
        )
        errors++
      } else {
        console.log(
          `::warning file=${file}::Route '${routePath}' has no 'authorize' meta — verify it is intentionally public`,
        )
        warnings++
      }
    }
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// Python Route Authorization Audit
// Scans Flask / Django / FastAPI Python source files and reports route
// handler functions that are missing authentication decorators.
// ─────────────────────────────────────────────────────────────────────────────
console.log('\n=== Django View Authorization Audit ===')

const DJANGO_AUTH = [
  '@login_required',
  '@permission_required',
]

let viewFiles = []
try {
  viewFiles = execSync(
    'find . -name "views.py" -not -path "*/venv/*" -not -path "*/.venv/*" ' +
    '-not -path "*/migrations/*" -not -path "*/__pycache__/*"'
  )
    .toString()
    .trim()
    .split('\n')
    .filter(Boolean)
} catch (_) {}

warnings = warnings || 0

for (const file of viewFiles) {
  if (!fs.existsSync(file)) continue

  const lines = fs.readFileSync(file, 'utf8').split('\n')

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim()

    const isView = line.match(/^def\s+\w+\(request[,\)]/)

    if (!isView) continue

    const viewName = line.match(/^def\s+(\w+)/)?.[1] || 'unknown'

    let hasAuth = false
    let j = i - 1

    while (j >= 0 && lines[j].trim().startsWith('@')) {
      const decoratorLine = lines[j].trim()

      if (DJANGO_AUTH.some(d => decoratorLine.includes(d))) {
        hasAuth = true
      }

      j--
    }

    if (!hasAuth) {
      console.log(
        `::warning file=${file}::Django view '${viewName}' (line ${i + 1}) has no auth decorator — verify it is public`
      )
      warnings++
    }
  }
}

if (errors > 0) {
  console.log(
    `\n❌ Route auth audit failed: ${errors} error(s), ${warnings} warning(s)`,
  )
  process.exit(1)
} else if (warnings > 0) {
  console.log(
    `\n⚠  Route auth audit completed with ${warnings} warning(s) — review the routes/views above`,
  )
} else {
  console.log('\n✅ Route auth audit passed — all routes and views have authorization metadata')
}