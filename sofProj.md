# CodeBundle: SoftwareProject
Generated: 2026-05-17T16:46:41.922Z
Root: /Users/natjs/Github/SoftwareProject
Files: 96

## How to apply changes
- Return changes as **unified diffs** per file whenever possible.
- Files are delimited with `<!-- FILE: ... -->` markers.

## Project tree
```
├─ .dockerignore
├─ .github
│  ├─ ISSUE_TEMPLATE
│  │  ├─ config.yml
│  │  └─ issue_template.md
│  ├─ quality_control_data.json
│  ├─ scripts
│  │  ├─ .release-please-manifest.json
│  │  ├─ CyclomaticMetricGP.py
│  │  ├─ depth_conditional_nesting_GP.py
│  │  ├─ fog_comments_indexGP.py
│  │  ├─ generate_qc_report.js
│  │  ├─ generate-integrity-report.js
│  │  ├─ len_identifiersGP.py
│  │  ├─ release-please-config.json
│  │  ├─ render-integrity-html.js
│  │  └─ route-auth-audit.js
│  └─ workflows
│     ├─ deploy.yml
│     ├─ histogram.yml
│     ├─ pareto.yml
│     ├─ quality-control-aggregator.yml
│     ├─ quality-metrics.yml
│     ├─ realease-please.yml
│     ├─ runchart.yml
│     └─ test.yml
├─ .gitignore
├─ .gitmodules
├─ accounts
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ app
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ __init__.py
│  │  └─ 0001_initial.py
│  ├─ models.py
│  ├─ services.py
│  ├─ static
│  │  ├─ css
│  │  │  ├─ auth-signup.css
│  │  │  └─ main.css
│  │  └─ js
│  │     ├─ auth-signup.js
│  │     ├─ content.js
│  │     ├─ genres.js
│  │     ├─ navbar.js
│  │     └─ tailwind.config.js
│  ├─ tech_admin.py
│  ├─ templates
│  │  ├─ admin
│  │  │  ├─ tech_add_user.html
│  │  │  ├─ tech_edit_user.html
│  │  │  └─ tech.html
│  │  ├─ base
│  │  │  ├─ base.html
│  │  │  └─ initial.html
│  │  ├─ components
│  │  │  ├─ card_movies.html
│  │  │  ├─ card_series.html
│  │  │  ├─ footer.html
│  │  │  ├─ navbar-init.html
│  │  │  ├─ navbar.html
│  │  │  ├─ platforms_filter.html
│  │  │  └─ stat_card.html
│  │  ├─ pages
│  │  │  ├─ catalog.html
│  │  │  ├─ content_view.html
│  │  │  ├─ direction_dashboard.html
│  │  │  ├─ home.html
│  │  │  ├─ main.html
│  │  │  ├─ movies.html
│  │  │  ├─ personal_library.html
│  │  │  ├─ search.html
│  │  │  ├─ series.html
│  │  │  └─ user_settings.html
│  │  └─ registration
│  │     ├─ login.html
│  │     ├─ onboarding_complete.html
│  │     ├─ onboarding_genres.html
│  │     ├─ onboarding.html
│  │     ├─ privacy_policy.html
│  │     ├─ singup.html
│  │     └─ terms_of_service.html
│  ├─ tests.py
│  ├─ urls.py
│  ├─ utils.py
│  └─ views.py
├─ docker-compose.yml
├─ Dockerfile
├─ entrypoint.sh
├─ IshikawaTools
│  ├─ chart.py
│  ├─ histogram.py
│  └─ runchart.py
├─ manage.py
├─ meeting_files
│  └─ to_do_list.md
├─ pyproject.toml
├─ SoftwareProject
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
└─ uv.lock
```

## Files list

- `.dockerignore` (352 bytes)
- `.github/ISSUE_TEMPLATE/config.yml` (27 bytes)
- `.github/ISSUE_TEMPLATE/issue_template.md` (674 bytes)
- `.github/quality_control_data.json` (1434 bytes)
- `.github/scripts/.release-please-manifest.json` (18 bytes)
- `.github/scripts/CyclomaticMetricGP.py` (7013 bytes)
- `.github/scripts/depth_conditional_nesting_GP.py` (5643 bytes)
- `.github/scripts/fog_comments_indexGP.py` (3097 bytes)
- `.github/scripts/generate_qc_report.js` (5936 bytes)
- `.github/scripts/generate-integrity-report.js` (10405 bytes)
- `.github/scripts/len_identifiersGP.py` (2879 bytes)
- `.github/scripts/release-please-config.json` (204 bytes)
- `.github/scripts/render-integrity-html.js` (16156 bytes)
- `.github/scripts/route-auth-audit.js` (5104 bytes)
- `.github/workflows/deploy.yml` (874 bytes)
- `.github/workflows/histogram.yml` (945 bytes)
- `.github/workflows/pareto.yml` (988 bytes)
- `.github/workflows/quality-control-aggregator.yml` (3826 bytes)
- `.github/workflows/quality-metrics.yml` (38123 bytes)
- `.github/workflows/realease-please.yml` (465 bytes)
- `.github/workflows/runchart.yml` (1259 bytes)
- `.github/workflows/test.yml` (766 bytes)
- `.gitignore` (62 bytes)
- `.gitmodules` (119 bytes)
- `accounts/__init__.py` (0 bytes)
- `accounts/admin.py` (63 bytes)
- `accounts/apps.py` (91 bytes)
- `accounts/forms.py` (4167 bytes)
- `accounts/migrations/__init__.py` (0 bytes)
- `accounts/models.py` (57 bytes)
- `accounts/tests.py` (60 bytes)
- `accounts/urls.py` (311 bytes)
- `accounts/views.py` (571 bytes)
- `app/__init__.py` (0 bytes)
- `app/admin.py` (2087 bytes)
- `app/apps.py` (139 bytes)
- `app/migrations/__init__.py` (0 bytes)
- `app/migrations/0001_initial.py` (12276 bytes)
- `app/models.py` (6735 bytes)
- `app/services.py` (14159 bytes)
- `app/static/css/auth-signup.css` (2118 bytes)
- `app/static/css/main.css` (4129 bytes)
- `app/static/js/auth-signup.js` (3664 bytes)
- `app/static/js/content.js` (4150 bytes)
- `app/static/js/genres.js` (1763 bytes)
- `app/static/js/navbar.js` (901 bytes)
- `app/static/js/tailwind.config.js` (829 bytes)
- `app/tech_admin.py` (2881 bytes)
- `app/templates/admin/tech_add_user.html` (5635 bytes)
- `app/templates/admin/tech_edit_user.html` (6457 bytes)
- `app/templates/admin/tech.html` (14123 bytes)
- `app/templates/base/base.html` (1408 bytes)
- `app/templates/base/initial.html` (1401 bytes)
- `app/templates/components/card_movies.html` (3232 bytes)
- `app/templates/components/card_series.html` (3231 bytes)
- `app/templates/components/footer.html` (619 bytes)
- `app/templates/components/navbar-init.html` (584 bytes)
- `app/templates/components/navbar.html` (5687 bytes)
- `app/templates/components/platforms_filter.html` (1824 bytes)
- `app/templates/components/stat_card.html` (378 bytes)
- `app/templates/pages/catalog.html` (746 bytes)
- `app/templates/pages/content_view.html` (9449 bytes)
- `app/templates/pages/direction_dashboard.html` (17419 bytes)
- `app/templates/pages/home.html` (19757 bytes)
- `app/templates/pages/main.html` (19355 bytes)
- `app/templates/pages/movies.html` (443 bytes)
- `app/templates/pages/personal_library.html` (9217 bytes)
- `app/templates/pages/search.html` (4701 bytes)
- `app/templates/pages/series.html` (440 bytes)
- `app/templates/pages/user_settings.html` (31560 bytes)
- `app/templates/registration/login.html` (3765 bytes)
- `app/templates/registration/onboarding_complete.html` (1079 bytes)
- `app/templates/registration/onboarding_genres.html` (6253 bytes)
- `app/templates/registration/onboarding.html` (7856 bytes)
- `app/templates/registration/privacy_policy.html` (3589 bytes)
- `app/templates/registration/singup.html` (7477 bytes)
- `app/templates/registration/terms_of_service.html` (2941 bytes)
- `app/tests.py` (60 bytes)
- `app/urls.py` (1377 bytes)
- `app/utils.py` (3282 bytes)
- `app/views.py` (26146 bytes)
- `docker-compose.yml` (860 bytes)
- `Dockerfile` (455 bytes)
- `entrypoint.sh` (173 bytes)
- `IshikawaTools/chart.py` (4069 bytes)
- `IshikawaTools/histogram.py` (5451 bytes)
- `IshikawaTools/runchart.py` (4479 bytes)
- `manage.py` (671 bytes)
- `meeting_files/to_do_list.md` (407 bytes)
- `pyproject.toml` (311 bytes)
- `SoftwareProject/__init__.py` (0 bytes)
- `SoftwareProject/asgi.py` (407 bytes)
- `SoftwareProject/settings.py` (3631 bytes)
- `SoftwareProject/urls.py` (1009 bytes)
- `SoftwareProject/wsgi.py` (407 bytes)
- `uv.lock` (68257 bytes)

---
<!-- FILE: .dockerignore -->
## .dockerignore

```
# Byte-compiled / Python caches
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environments
.venv/
venv/
.env

# Logs
*.log

# Git
.git
.gitignore

# Docker
Dockerfile
.dockerignore

# Node / frontend (si tens)
node_modules/
dist/

# Static / media build folders (si es re-generen en collectstatic)
staticfiles/

# IDE / editor configs
.vscode/
.idea/
*.swp

```
<!-- END_FILE -->

---
<!-- FILE: .github/ISSUE_TEMPLATE/config.yml -->
## .github/ISSUE_TEMPLATE/config.yml

```yaml
blank_issues_enabled: false

```
<!-- END_FILE -->

---
<!-- FILE: .github/ISSUE_TEMPLATE/issue_template.md -->
## .github/ISSUE_TEMPLATE/issue_template.md

```md
---
name: User Story
about: Capture a user story with acceptance criteria and planning details
title: "[User Story] "
labels: ["user-story"]
assignees: []
---

## Story
As a **[type of user/persona]**,  
I want **[goal/action]**,  
so that **[benefit/value]**.

## Context
- **Problem:** [What problem are we solving?]
- **Current behavior:** [How does it work today?]
- **Expected behavior:** [How should it work?]

## Scope
- **In scope:** [What is included in this story]
- **Out of scope:** [What is not included]

## Estimation & Planning
- **Priority:** [Low / Medium / High / Critical]
- **Story Points:** [1, 2, 3, 5, 8, 13]
- **Sprint/Milestone:** [e.g., Sprint 12]

```
<!-- END_FILE -->

---
<!-- FILE: .github/quality_control_data.json -->
## .github/quality_control_data.json

```json
{
  "document_type": "Check Sheet",
  "purpose": "Quality Control - Defect/Event Tracking",
  "title": "Check Sheet or Checklist",
  "schema": {
    "columns": [
      "Defect/Event occurrence",
      "Mon",
      "Tue",
      "Wed",
      "Thu",
      "Fri",
      "TOTAL"
    ],
    "data_format": "Tally marks represented as integers for logic",
    "total_calculation": "Sum of daily occurrences"
  },
  "records": [
    {
      "occurrence": "Test error",
      "daily_counts": {
        "Mon": 0,
        "Tue": 0,
        "Wed": 0,
        "Thu": 2,
        "Fri": 0
      },
      "total": 2
    },
    {
      "occurrence": "Security vulnerability",
      "daily_counts": {
        "Mon": 0,
        "Tue": 0,
        "Wed": 0,
        "Thu": 2,
        "Fri": 0
      },
      "total": 2
    },
    {
      "occurrence": "Code smells/Bugs",
      "daily_counts": {
        "Mon": 0,
        "Tue": 0,
        "Wed": 0,
        "Thu": 0,
        "Fri": 0
      },
      "total": 0
    },
    {
      "occurrence": "Other/Miscellaneous",
      "daily_counts": {
        "Mon": 0,
        "Tue": 0,
        "Wed": 0,
        "Thu": 0,
        "Fri": 0
      },
      "total": 0
    }
  ],
  "summary": {
    "grand_total": 4,
    "days_tracked": 5
  },
  "issues_tracking": {
    "open_bugs": 0,
    "open_features": 0,
    "open_docs": 0,
    "open_ux": 0,
    "open_infra": 0,
    "open_testing": 0,
    "total_open": 0
  }
}

```
<!-- END_FILE -->

---
<!-- FILE: .github/scripts/.release-please-manifest.json -->
## .github/scripts/.release-please-manifest.json

```json
{
  ".": "1.0.0"
}

```
<!-- END_FILE -->

---
<!-- FILE: .github/scripts/CyclomaticMetricGP.py -->
## .github/scripts/CyclomaticMetricGP.py

```py
import os
import re
import sys
import ast
import json

# ── JavaScript / TypeScript support ──────────────────────────────────────────
JS_EXTENSIONS = {'.js', '.ts', '.mjs', '.tsx', '.jsx', '.cjs'}

# Regex patterns that each add 1 to cyclomatic complexity in JS/TS
_JS_DECISION_PATTERNS = [
    re.compile(r'\bif\s*\('),
    re.compile(r'\belse\s+if\s*\('),
    re.compile(r'\bfor\s*\('),
    re.compile(r'\bwhile\s*\('),
    re.compile(r'\bdo\s*\{'),
    re.compile(r'\bcase\b'),
    re.compile(r'\bcatch\s*\('),
    re.compile(r'&&'),
    re.compile(r'\|\|'),
    re.compile(r'\?(?![?.:])'),   # ternary — excludes ?. and ??
]


def _strip_js_noise(source: str) -> str:
    """Remove JS/TS comments and string literals to avoid false positives."""
    source = re.sub(r'//[^\n]*', '', source)
    source = re.sub(r'/\*.*?\*/', '', source, flags=re.DOTALL)
    source = re.sub(r'`[^`\\]*(?:\\.[^`\\]*)*`', '``', source, flags=re.DOTALL)
    source = re.sub(r'"(?:[^"\\]|\\.)*"', '""', source)
    source = re.sub(r"'(?:[^'\\]|\\.)*'", "''", source)
    return source


# Matches function-like declarations in JS/TS (named functions, arrow fns, method shorthands)
_JS_FN_PATTERN = re.compile(
    r'\bfunction\s*\w*\s*\('     # function foo( or function(
    r'|(?<!=)=>\s*[{(]'            # => { or => ( (arrow function body)
    r'|\basync\s+\w+\s*\('        # async method shorthand
    r'|(?:^|[{,;\n])\s*\w+\s*\([^)]*\)\s*\{',  # method shorthand: foo(args) {
    re.MULTILINE
)


def calcular_js(codigo_fuente: str) -> int:
    """Return average cyclomatic complexity per function (JS/TS).

    Divides the file-level branch count by the number of function declarations
    so that the threshold is meaningful on a per-function basis, not per-file.
    """
    source = _strip_js_noise(codigo_fuente)
    total = 1
    for pattern in _JS_DECISION_PATTERNS:
        total += len(pattern.findall(source))
    fn_count = max(len(_JS_FN_PATTERN.findall(source)), 1)
    # Ceiling integer division
    return (total + fn_count - 1) // fn_count
# ─────────────────────────────────────────────────────────────────────────────

class AnalizadorComplejidad(ast.NodeVisitor):
    def __init__(self):
        self.complejidad = 1
        self.fn_count = 0

    def visit_FunctionDef(self, node):
        self.fn_count += 1
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.fn_count += 1
        self.generic_visit(node)

    def visit_If(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.complejidad += len(node.values) - 1
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_match_case(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_ListComp(self, node):
        self.complejidad += 1
        self.generic_visit(node)
        
    def visit_DictComp(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_SetComp(self, node):
        self.complejidad += 1
        self.generic_visit(node)

    def visit_GeneratorExp(self, node):
        self.complejidad += 1
        self.generic_visit(node)

def calcular(codigo_fuente: str, extension: str = '.py') -> int:
    """Dispatch to the correct complexity calculator based on file extension."""
    if extension in JS_EXTENSIONS:
        return calcular_js(codigo_fuente)
    # Python AST path
    try:
        arbol = ast.parse(codigo_fuente)
    except SyntaxError:
        return 0

    visitante = AnalizadorComplejidad()
    visitante.visit(arbol)
    fn_count = max(visitante.fn_count, 1)
    # Ceiling integer division — average CC per function
    return (visitante.complejidad + fn_count - 1) // fn_count

DIRECTORIOS_IGNORADOS = {'venv', 'env', '.venv', 'migrations', '__pycache__', '.git', 'tests',
                         'node_modules', 'dist', 'build', '.next', 'coverage'}
ARCHIVOS_IGNORADOS = {'manage.py', 'settings.py', 'wsgi.py', 'asgi.py'}
EXTENSIONES_VALIDAS = {'.py'} | JS_EXTENSIONS


def es_archivo_valido(ruta):
    nombre = os.path.basename(ruta)
    ext = os.path.splitext(nombre)[1]

    if nombre in ARCHIVOS_IGNORADOS:
        return False
    if ext not in EXTENSIONES_VALIDAS:
        return False

    partes_ruta = ruta.split(os.sep)
    for ignorado in DIRECTORIOS_IGNORADOS:
        if ignorado in partes_ruta:
            return False

    return True

def analizar_archivos(rutas_archivos: list, limite_complejidad: int = 20):
    resultados_array = []
    archivos_procesados = 0
    archivos_fallidos = 0
    
    for ruta in rutas_archivos:
        if not os.path.exists(ruta):
            continue 
            
        if not es_archivo_valido(ruta):
            continue
            
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()

        ext = os.path.splitext(ruta)[1]
        complejidad = calcular(contenido, ext)
        archivos_procesados += 1
        
        # Asignar el status_code que solicitaste
        if complejidad > limite_complejidad:
            status_code = "DANGER"
            archivos_fallidos += 1
        elif complejidad >= limite_complejidad - 5:
            status_code = "WARN"
        else:
            status_code = "OK"
            
        resultados_array.append({
            "file": ruta,
            "complexity": complejidad,
            "status_code": status_code
        })
    
    # Construcción del diccionario final con la estructura requerida
    salida_json = {
        "analysis_type": "Cyclomatic Complexity",
        "threshold": limite_complejidad,
        "summary": {
            "total_files": archivos_procesados,
            "failed_files": archivos_fallidos
        },
        "results": resultados_array
    }
    
    # Imprimir el JSON formateado con indentación
    print(json.dumps(salida_json, indent=4))
    sys.exit(0)

if __name__ == "__main__":
    archivos_a_analizar = sys.argv[1:]
    limite = 20
    
    if not archivos_a_analizar:
        # Estructura vacía consistente si no hay archivos
        salida_vacia = {
            "analysis_type": "Cyclomatic Complexity",
            "threshold": limite,
            "summary": {
                "total_files": 0,
                "failed_files": 0
            },
            "results": []
        }
        print(json.dumps(salida_vacia, indent=4))
        sys.exit(0)
        
    analizar_archivos(archivos_a_analizar, limite)

```
<!-- END_FILE -->

---
<!-- FILE: .github/scripts/depth_conditional_nesting_GP.py -->
## .github/scripts/depth_conditional_nesting_GP.py

```py
import ast
import re
import sys
import json
from pathlib import Path
from typing import Dict, Optional, List, Any

CRITICAL_THRESHOLD = 7
WARNING_THRESHOLD = 3

# ── JavaScript / TypeScript support ──────────────────────────────────────────
JS_EXTENSIONS = {'.js', '.ts', '.mjs', '.tsx', '.jsx', '.cjs'}
JS_CONTROL_RE = re.compile(r'\b(if|else\s+if|for|while|switch|do)\b')


def _strip_js_noise(source: str) -> str:
    """Remove JS/TS comments and string literals to avoid false positives."""
    source = re.sub(r'//[^\n]*', '', source)
    source = re.sub(r'/\*.*?\*/', '', source, flags=re.DOTALL)
    source = re.sub(r'`[^`\\]*(?:\\.[^`\\]*)*`', '``', source, flags=re.DOTALL)
    source = re.sub(r'"(?:[^"\\]|\\.)*"', '""', source)
    source = re.sub(r"'(?:[^'\\]|\\.)*'", "''", source)
    return source


def get_metrics_js(filepath: Path) -> Optional[Dict[str, Any]]:
    """Brace-tracking nesting depth estimator for JavaScript / TypeScript."""
    try:
        content = filepath.read_text(encoding="utf-8").strip()
        if not content:
            return None
    except OSError as e:
        print(f"Error reading {filepath}: {e}")
        return None

    content = _strip_js_noise(content)
    depths: List[int] = []
    brace_depth = 0

    for line in content.split('\n'):
        has_control = bool(JS_CONTROL_RE.search(line))
        for ch in line:
            if ch == '{':
                brace_depth += 1
                if has_control:
                    depths.append(brace_depth)
                    has_control = False  # record once per statement
            elif ch == '}':
                brace_depth = max(0, brace_depth - 1)
        # braceless single-line if/for (no `{` on this line)
        if has_control and '{' not in line:
            depths.append(brace_depth + 1)

    if not depths:
        return {"avg": 0.0, "max": 0, "status_code": "\u2705 OK"}

    max_d = max(depths)
    avg_d = round(sum(depths) / len(depths), 1)
    return {"avg": avg_d, "max": max_d, "status_code": get_status_code(max_d)}
# ─────────────────────────────────────────────────────────────────────────────


class NestingVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.depths: List[int] = []
        self.current_depth: int = 0

    def visit_If(self, node: ast.If) -> None:
        self.current_depth += 1
        self.depths.append(self.current_depth)

        for item in node.body:
            self.visit(item)

        if len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
            self.current_depth -= 1
            self.visit(node.orelse[0])
            self.current_depth += 1
        else:
            for item in node.orelse:
                self.visit(item)

        self.current_depth -= 1


def get_status_code(max_depth: int) -> str:
    if max_depth > CRITICAL_THRESHOLD:
        return "❌ CRITICAL"
    if max_depth >= WARNING_THRESHOLD:
        return "🚨 WARNING"
    return "✅ OK"


def get_metrics(filepath: Path) -> Optional[Dict[str, Any]]:
    try:
        content = filepath.read_text(encoding="utf-8").strip()
        if not content:
            return None
        tree = ast.parse(content)
    except (SyntaxError, OSError) as e:
        print(f"Error processing {filepath}: {e}")
        return None

    visitor = NestingVisitor()
    visitor.visit(tree)

    if not visitor.depths:
        return {"avg": 0.0, "max": 0, "status_code": "✅ OK"}

    max_d = max(visitor.depths)
    avg_d = round(sum(visitor.depths) / len(visitor.depths), 1)

    return {
        "avg": avg_d,
        "max": max_d,
        "status_code": get_status_code(max_d)
    }


def main() -> None:
    all_args = sys.argv[1:]
    py_files = [Path(f) for f in all_args if f.endswith('.py')]
    js_files = [Path(f) for f in all_args
                if Path(f).suffix in JS_EXTENSIONS]
    files_to_analyze = py_files + js_files

    if not files_to_analyze:
        print("No Python or JavaScript/TypeScript files to analyze.")
        sys.exit(0)

    all_results: List[Dict[str, Any]] = []
    failed_count = 0

    for filepath in files_to_analyze:
        if not filepath.exists():
            continue

        if filepath.suffix in JS_EXTENSIONS:
            metrics = get_metrics_js(filepath)
        else:
            metrics = get_metrics(filepath)

        if metrics:
            all_results.append({
                "file": str(filepath),
                "avg_depth": metrics["avg"],
                "max_depth": metrics["max"],
                "status_code": metrics["status_code"]
            })
            if metrics["max"] > CRITICAL_THRESHOLD:
                failed_count += 1

    json_data = {
        "analysis_type": "Depth of Conditional Nesting",
        "threshold": CRITICAL_THRESHOLD,
        "summary": {
            "total_files": len(all_results),
            "failed_files": failed_count
        },
        "results": all_results
    }

    output_file = Path("nesting_metrics.json")
    output_file.write_text(json.dumps(json_data, indent=4, ensure_ascii=False), encoding="utf-8")

    print(f"Analysis report saved to {output_file}")

    if failed_count > 0:
        print(f"FAIL: {failed_count} files exceed the nesting threshold.")
        sys.exit(1)
    else:
        print("SUCCESS: All files are within the nesting threshold.")
        sys.exit(0)


if __name__ == "__main__":
    main()

```
<!-- END_FILE -->

---
<!-- FILE: .github/scripts/fog_comments_indexGP.py -->
## .github/scripts/fog_comments_indexGP.py

```py
import re
import os
import sys
import json
import textstat
from pathlib import Path

SUPPORTED_EXTENSIONS = {'.py', '.js', '.ts', '.cpp', '.java', '.html'}

def extract_comments(file_path):
    extension = os.path.splitext(file_path)[1]

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            code = f.read()
    except:
        return []

    if extension == '.py':
        pattern = r'#.*?$|""".*?"""|\'\'\'.*?\'\'\''
        flags = re.DOTALL | re.MULTILINE
    elif extension in ['.js', '.ts', '.cpp', '.java']:
        pattern = r'//.*?$|/\*.*?\*/'
        flags = re.DOTALL | re.MULTILINE
    elif extension == '.html':
        pattern = r'<!--.*?-->'
        flags = re.DOTALL
    else:
        return []

    comments = re.findall(pattern, code, flags)

    clean_comments = []
    for c in comments:
        c = re.sub(r'#|//|/\*|\*/|"""|\'\'\'|<!--|-->', '', c)
        c = re.sub(r'\s+', ' ', c).strip()

        # ignorar comentarios muy cortos
        if len(c.split()) >= 8:
            clean_comments.append(c)

    return clean_comments


def compute_fog(comments):
    scores = []

    for c in comments:
        try:
            score = textstat.gunning_fog(c)
            scores.append(score)
        except:
            continue

    if not scores:
        return None, None

    avg = sum(scores) / len(scores)
    return avg, max(scores)


def classify(score):
    if score is None:
        return "NO DATA"
    elif score < 12:
        return "OK"
    elif score <= 22:
        return "MODERATE"
    else:
        return "COMPLEX"


def scan(target_path):
    path = Path(target_path)

    files = (
        [path] if path.is_file()
        else [f for f in path.rglob('*') if f.suffix in SUPPORTED_EXTENSIONS]
    )

    results = []
    failed = 0

    for file in files:
        comments = extract_comments(file)
        avg, max_score = compute_fog(comments)

        status = classify(avg)
        if status.startswith("COMPLEX"):
            failed += 1

        results.append({
            "file": str(file),
            "avg_fog": round(avg, 1) if avg else None,
            "max_fog": round(max_score, 1) if max_score else None,
            "status_code": status
        })

    return results, len(files), failed


def print_json(results, total, failed):
    output = {
        "analysis_type": "Comment Readability (Fog Index)",
        "threshold": 22,
        "summary": {
            "total_files": total,
            "failed_files": failed
        },
        "results": results
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fog.py <file_or_directory>")
        sys.exit(1)

    results, total, failed = scan(sys.argv[1])

    if not results:
        print(json.dumps({
            "analysis_type": "Comment Readability (Fog Index)",
            "threshold": 22,
            "summary": {"total_files": 0, "failed_files": 0},
            "results": []
        }, indent=2))
        sys.exit(0)

    print_json(results, total, failed)

```
<!-- END_FILE -->

---
<!-- FILE: .github/scripts/generate_qc_report.js -->
## .github/scripts/generate_qc_report.js

```js
// .github/scripts/generate_qc_report.js

const fs = require('fs');
const path = require('path');

module.exports = async ({ github, context, core }) => {
  const jsonPath = path.join(process.env.GITHUB_WORKSPACE, '.github', 'quality_control_data.json');

  // 1. Ler o arquivo atual
  let qcData;
  try {
    const rawData = fs.readFileSync(jsonPath, 'utf8');
    qcData = JSON.parse(rawData);
  } catch (error) {
    core.setFailed(`Erro ao ler o arquivo JSON: ${error.message}`);
    return;
  }

  // 2. Determinar o dia da semana atual em UTC
  const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  const today = days[new Date().getUTCDay()];

  // Se for fim de semana, logamos e paramos (ou agrupamos em Sexta, depende da regra)
  if (today === 'Sat' || today === 'Sun') {
    core.info('Final de semana. Nenhuma métrica diária de QC coletada no Check Sheet para Sat/Sun.');
    return;
  }

  // Obter as variáveis de falhas passadas pelo Workflow
  // Elas vêm do steps context no arquivo yml
  const testErrorsCount = parseInt(process.env.TEST_ERRORS || '0', 10);
  const securityIssuesCount = parseInt(process.env.SECURITY_ISSUES || '0', 10);
  const codeSmellsCount = parseInt(process.env.CODE_SMELLS || '0', 10);

  core.info(`Coletado hoje (${today}): Testes: ${testErrorsCount}, Segurança: ${securityIssuesCount}, Code Smells: ${codeSmellsCount}`);

  // 3. Atualizar as contagens diárias (Sobrescrever para refletir o estado atual do dia)
  qcData.records.forEach(record => {
    switch (record.occurrence) {
      case 'Test error':
        record.daily_counts[today] = testErrorsCount;
        break;
      case 'Security vulnerability':
        record.daily_counts[today] = securityIssuesCount;
        break;
      case 'Code smells/Bugs':
        record.daily_counts[today] = codeSmellsCount;
        break;
      default:
        // Other/Misc não mapeado automaticamente para este trigger
        break;
    }

    // Recalcular o Total por linha
    record.total = Object.values(record.daily_counts).reduce((sum, val) => sum + val, 0);
  });

  // Recalcular o Grand Total
  qcData.summary.grand_total = qcData.records.reduce((sum, record) => sum + record.total, 0);

  // --- Rastreamento Automático de Issues e Labels ---
  try {
    core.info('Buscando issues abertas no repositório...');

    // Buscar todas as issues abertas (o GitHub API retorna PRs como issues também, filtraremos depois se necessário)
    const { data: openIssues } = await github.rest.issues.listForRepo({
      owner: context.repo.owner,
      repo: context.repo.repo,
      state: 'open',
      per_page: 100
    });

    // Apenas issues reais (não Pull Requests)
    const realIssues = openIssues.filter(issue => !issue.pull_request);

    let bugCount = 0;
    let featureCount = 0;
    let docsCount = 0;
    let uxCount = 0;
    let infraCount = 0;
    let testingCount = 0;

    realIssues.forEach(issue => {
      const labels = issue.labels.map(l => l.name.toLowerCase());

      if (labels.some(l => l === 'bug' || l === 'fix')) bugCount++;
      if (labels.some(l => l === 'feature' || l === 'new-feature' || l === 'enhancement')) featureCount++;
      if (labels.some(l => l === 'documentation' || l === 'docs')) docsCount++;
      if (labels.some(l => ['ui/ux', 'accessibility', 'card-sorting', 'heuristic', 'user-test'].includes(l))) uxCount++;
      if (labels.some(l => ['chore', 'refactor', 'ci/cd', 'ci', 'build', 'performance', 'style'].includes(l))) infraCount++;
      if (labels.some(l => l === 'testing' || l === 'tests')) testingCount++;
    });

    // Atualizar no schema do JSON
    qcData.issues_tracking = {
      open_bugs: bugCount,
      open_features: featureCount,
      open_docs: docsCount,
      open_ux: uxCount,
      open_infra: infraCount,
      open_testing: testingCount,
      total_open: realIssues.length
    };

    core.info(`Issues trackeadas: ${realIssues.length} total, Bugs: ${bugCount}, Features: ${featureCount}, UX: ${uxCount}`);

  } catch (error) {
    core.warning(`Erro ao buscar e contabilizar issues: ${error.message}`);
  }
  // ----------------------------------------------------

  // 4. Salvar o arquivo JSON atualizado
  fs.writeFileSync(jsonPath, JSON.stringify(qcData, null, 2));
  core.info('Arquivo quality_control_data.json atualizado com sucesso.');

  // 5. Gerar o Markdown para o Job Summary
  let mdSummary = `# 🛡️ Quality Control Daily Report (${new Date().toISOString().split('T')[0]})\n\n`;
  mdSummary += `### 📊 Weekly Cumulative Defects (Check Sheet)\n\n`;
  mdSummary += `| Defect/Event occurrence | Mon | Tue | Wed | Thu | Fri | TOTAL |\n`;
  mdSummary += `| :--- | :---: | :---: | :---: | :---: | :---: | :---: |\n`;

  qcData.records.forEach(r => {
    mdSummary += `| ${r.occurrence} | ${r.daily_counts.Mon} | ${r.daily_counts.Tue} | ${r.daily_counts.Wed} | ${r.daily_counts.Thu} | ${r.daily_counts.Fri} | **${r.total}** |\n`;
  });

  mdSummary += `| **GRAND TOTAL** | | | | | | **${qcData.summary.grand_total}** |\n\n`;

  if (qcData.issues_tracking) {
    mdSummary += `### 🐛 Active Issues Analysis (by Labels)\n\n`;
    mdSummary += `| Category | Bug 🐛 | Feature ✨ | UX/UI 🎨 | Infra 🛠️ | Testing 🧪 | Docs 📝 | **Total (Open)** |\n`;
    mdSummary += `| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n`;
    mdSummary += `| Count | ${qcData.issues_tracking.open_bugs} | ${qcData.issues_tracking.open_features} | ${qcData.issues_tracking.open_ux} | ${qcData.issues_tracking.open_infra} | ${qcData.issues_tracking.open_testing} | ${qcData.issues_tracking.open_docs} | **${qcData.issues_tracking.total_open}** |\n\n`;
  }

  mdSummary += `--- \n`;
  mdSummary += `*💡 This report aggregates results from all active pipelines for today. Values represent the current state of failures.*`;

  // Escrever no Github Step Summary
  await core.summary.addRaw(mdSummary).write();
};

```
<!-- END_FILE -->

---
<!-- FILE: .github/scripts/generate-integrity-report.js -->
## .github/scripts/generate-integrity-report.js

```js
'use strict'

/**
 * generate-integrity-report.js
 *
 * Reads captured log files from each security job AND quality metric JSON files
 * produced by the unified Quality & Security Pipeline, then writes a single
 * consolidated JSON report.
 *
 * Backward-compatible: when QUALITY_ARTIFACT_PREFIX is not set the script
 * behaves exactly as before (reads from integrity-job1/2/3, writes to
 * integrity-report/security-report.json).
 *
 * Environment variables (set by quality-metrics.yml):
 *   QUALITY_ARTIFACT_PREFIX  — artifact directory prefix, e.g. "quality-job"
 *                              When present, security logs are read from
 *                              <prefix>5/, <prefix>6/, <prefix>7/ and quality
 *                              JSONs from <prefix>1/ … <prefix>4/.
 *   REPORT_OUTPUT_DIR        — directory for the output JSON
 *                              (default: "integrity-report")
 *
 * Output file:  <REPORT_OUTPUT_DIR>/report.json
 *               (legacy path: integrity-report/security-report.json)
 *
 * JSON schema (v2 — unified pipeline):
 * {
 *   schema_version, pipeline, metadata: { repository, ref, sha, run_id, generated_at },
 *   languages_targeted: [...],
 *   summary: { overall, jobs: { <job-id>: "pass|fail|skipped" } },
 *   quality: { complexity, nesting, identifier_length, fog_index },
 *   security: { access_control, route_auth, static_scan },
 *   // legacy flat fields kept for render-integrity-html.js compatibility:
 *   overall: { status, total_errors, total_warnings, total_notices },
 *   jobs: [{ id, name, status, errors, warnings, notices, findings }]
 * }
 */

const fs = require('fs')
const path = require('path')

// ─── Path resolution ─────────────────────────────────────────────────────────

const PREFIX = process.env.QUALITY_ARTIFACT_PREFIX || null  // e.g. "quality-job"
const OUTPUT_DIR = process.env.REPORT_OUTPUT_DIR || 'integrity-report'

// When running inside the unified pipeline the security logs live in
// quality-job5/, quality-job6/, quality-job7/.
// When running from the legacy integrity-GP.yml they live in integrity-job1/2/3.
const securityJobDir = (n) =>
  PREFIX ? path.join(`${PREFIX}${n}`) : path.join(`integrity-job${n - 4}`)

// ─── Security job definitions ────────────────────────────────────────────────

const SECURITY_JOBS = [
  {
    id: 'access-control',
    name: 'Access Control Audit',
    file: path.join(securityJobDir(5), 'access-control.log'),
  },
  {
    id: 'route-auth',
    name: 'Route Authorization Audit',
    file: path.join(securityJobDir(6), 'route-auth.log'),
  },
  {
    id: 'static-scan',
    name: 'Static Security Analysis',
    file: path.join(securityJobDir(7), 'static-scan.log'),
  },
]

// ─── Helpers ────────────────────────────────────────────────────────────────

function readLog(filePath) {
  try {
    return fs.readFileSync(filePath, 'utf8')
  } catch {
    return null
  }
}

function readJson(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'))
  } catch {
    return null
  }
}

/**
 * Parses a job log file for GitHub Actions annotations.
 * Handles both ::error:: and ::error file=foo.js::message forms.
 */
function parseLog(content) {
  if (!content) {
    return { findings: [], status: 'unknown', errors: 0, warnings: 0, notices: 0 }
  }

  const findings = []

  for (const line of content.split('\n')) {
    const fileMatch = line.match(/::(?:error|warning)[^:]*file=([^:,]+)[^:]*::(.+)/)
    const errorMatch = line.match(/::error[^:]*::(.+)/)
    const warningMatch = line.match(/::warning[^:]*::(.+)/)
    const noticeMatch = line.match(/::notice[^:]*::(.+)/)

    if (errorMatch) {
      findings.push({
        level: 'error',
        message: errorMatch[1].trim(),
        file: fileMatch ? fileMatch[1].trim() : null,
      })
    } else if (warningMatch) {
      findings.push({
        level: 'warning',
        message: warningMatch[1].trim(),
        file: fileMatch ? fileMatch[1].trim() : null,
      })
    } else if (noticeMatch) {
      findings.push({
        level: 'notice',
        message: noticeMatch[1].trim(),
        file: null,
      })
    }
  }

  const errors = findings.filter((f) => f.level === 'error').length
  const warnings = findings.filter((f) => f.level === 'warning').length
  const notices = findings.filter((f) => f.level === 'notice').length

  const hasFail = errors > 0 || content.includes('❌')
  const status = hasFail ? 'fail' : warnings > 0 ? 'warn' : 'pass'

  return { findings, status, errors, warnings, notices }
}

/**
 * Derives a "pass | fail | skipped" status from a quality metric JSON.
 * A missing / unreadable file is treated as "skipped".
 */
function qualityStatus(json) {
  if (!json) return 'skipped'
  if (json.skipped) return 'skipped'
  return json.summary && json.summary.failed_files > 0 ? 'fail' : 'pass'
}

// ─── Read quality metric JSONs (only available in unified pipeline) ──────────

const qualityData = PREFIX
  ? {
      complexity:        readJson(path.join(`${PREFIX}1`, 'complexity-results.json')),
      nesting:           readJson(path.join(`${PREFIX}2`, 'nesting_metrics.json')),
      identifier_length: readJson(path.join(`${PREFIX}3`, 'identifier_report.json')),
      fog_index:         readJson(path.join(`${PREFIX}4`, 'fog-results.json')),
    }
  : null

// ─── Main ────────────────────────────────────────────────────────────────────

const securityResults = SECURITY_JOBS.map((job) => {
  const content = readLog(job.file)
  const { findings, status, errors, warnings, notices } = parseLog(content)
  return { id: job.id, name: job.name, status, errors, warnings, notices, findings }
})

const totalErrors   = securityResults.reduce((s, r) => s + r.errors, 0)
const totalWarnings = securityResults.reduce((s, r) => s + r.warnings, 0)
const totalNotices  = securityResults.reduce((s, r) => s + r.notices, 0)

const securityOverall = securityResults.some((r) => r.status === 'fail')
  ? 'fail'
  : securityResults.some((r) => r.status === 'warn' || r.status === 'unknown')
    ? 'warn'
    : 'pass'

// Overall status includes quality failures when running in unified pipeline
const qualityOverall = qualityData
  ? Object.values(qualityData).some((d) => qualityStatus(d) === 'fail') ? 'fail' : 'pass'
  : 'pass'

const overallStatus =
  securityOverall === 'fail' || qualityOverall === 'fail'
    ? 'fail'
    : securityOverall === 'warn'
      ? 'warn'
      : 'pass'

// ─── Build report ────────────────────────────────────────────────────────────

const jobsSummary = {
  'access-control-audit': securityResults.find((r) => r.id === 'access-control')?.status ?? 'skipped',
  'route-auth-audit':     securityResults.find((r) => r.id === 'route-auth')?.status     ?? 'skipped',
  'static-security-scan': securityResults.find((r) => r.id === 'static-scan')?.status    ?? 'skipped',
}

if (qualityData) {
  jobsSummary['cyclomatic-complexity'] = qualityStatus(qualityData.complexity)
  jobsSummary['nesting-depth']         = qualityStatus(qualityData.nesting)
  jobsSummary['identifier-length']     = qualityStatus(qualityData.identifier_length)
  jobsSummary['fog-index-metrics']     = qualityStatus(qualityData.fog_index)
}

const report = {
  schema_version: '2.0',
  pipeline: PREFIX ? 'quality-and-security' : 'integrity',
  metadata: {
    repository:   process.env.GITHUB_REPOSITORY || '',
    ref:          process.env.GITHUB_REF_NAME   || '',
    sha:          process.env.GITHUB_SHA        || '',
    run_id:       process.env.GITHUB_RUN_ID     || '',
    generated_at: new Date().toISOString(),
  },
  languages_targeted: ['python', 'javascript', 'typescript', 'java', 'csharp'],
  summary: {
    overall: overallStatus,
    jobs: jobsSummary,
  },
  // Quality metric data (null when running from legacy integrity-GP.yml)
  quality: qualityData
    ? {
        complexity:        qualityData.complexity        ?? null,
        nesting:           qualityData.nesting           ?? null,
        identifier_length: qualityData.identifier_length ?? null,
        fog_index:         qualityData.fog_index         ?? null,
      }
    : null,
  // Security audit data
  security: {
    access_control: securityResults.find((r) => r.id === 'access-control') ?? null,
    route_auth:     securityResults.find((r) => r.id === 'route-auth')     ?? null,
    static_scan:    securityResults.find((r) => r.id === 'static-scan')    ?? null,
  },
  // ── Legacy flat fields kept for render-integrity-html.js compatibility ──
  overall: {
    status:          overallStatus,
    total_errors:    totalErrors,
    total_warnings:  totalWarnings,
    total_notices:   totalNotices,
  },
  jobs: securityResults,
}

// ─── Write output ────────────────────────────────────────────────────────────

fs.mkdirSync(OUTPUT_DIR, { recursive: true })

// Unified pipeline writes report.json; legacy path is security-report.json
const outFileName = PREFIX ? 'report.json' : 'security-report.json'
const outFile = path.join(OUTPUT_DIR, outFileName)
fs.writeFileSync(outFile, JSON.stringify(report, null, 2), 'utf8')

console.log(`✅ Report generated: ${outFile}`)
console.log(`   Pipeline : ${report.pipeline}`)
console.log(`   Status   : ${overallStatus.toUpperCase()}`)
console.log(`   Errors   : ${totalErrors}`)
console.log(`   Warnings : ${totalWarnings}`)
console.log(`   Notices  : ${totalNotices}`)

if (qualityData) {
  console.log('   Quality  :',
    Object.entries(jobsSummary)
      .filter(([k]) => !['access-control-audit','route-auth-audit','static-security-scan'].includes(k))
      .map(([k, v]) => `${k}=${v}`)
      .join(', ')
  )
}

```
<!-- END_FILE -->

---
<!-- FILE: .github/scripts/len_identifiersGP.py -->
## .github/scripts/len_identifiersGP.py

```py
import re
import sys
import json

# Python reserved words
PY_KEYWORDS = {
    'if', 'else', 'for', 'while', 'return', 'class',
    'def', 'import', 'from', 'as', 'with', 'try', 'except',
    'break', 'continue', 'pass', 'finally', 'raise', 'in',
    'and', 'or', 'not', 'is', 'lambda', 'yield'
}

# JavaScript / TypeScript reserved words
JS_KEYWORDS = {
    'if', 'else', 'for', 'while', 'do', 'return', 'class', 'function',
    'import', 'export', 'from', 'as', 'with', 'try', 'catch', 'finally',
    'throw', 'break', 'continue', 'new', 'delete', 'typeof', 'instanceof',
    'in', 'of', 'let', 'const', 'var', 'this', 'super', 'null', 'undefined',
    'true', 'false', 'void', 'switch', 'case', 'default', 'debugger',
    # TypeScript extras
    'interface', 'type', 'enum', 'namespace', 'declare', 'abstract',
    'implements', 'extends', 'readonly', 'public', 'private', 'protected',
    'static', 'async', 'await', 'yield', 'get', 'set', 'keyof', 'typeof',
    'never', 'unknown', 'any', 'string', 'number', 'boolean', 'object',
    'symbol', 'bigint',
}

# Combined set used for all languages
KEYWORDS = PY_KEYWORDS | JS_KEYWORDS

JS_EXTENSIONS = {'.js', '.ts', '.mjs', '.tsx', '.jsx', '.cjs'}
ACCEPTED_EXTENSIONS = {'.py'} | JS_EXTENSIONS

IDENTIFIER = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
THRESHOLD = 6

def extract_identifiers(code):
    return re.findall(IDENTIFIER, code)

def filter_identifiers(ids):
    return [i for i in ids if i not in KEYWORDS]

def average_length(ids):
    if not ids:
        return 0
    return sum(len(i) for i in ids) / len(ids)

def analyze_file(path):
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    identifiers = filter_identifiers(extract_identifiers(code))
    avg = average_length(identifiers)

    return {
        "file": path,
        "avg_length": round(avg, 2),
        "status_code": "OK!" if avg >= THRESHOLD else "⚠️ IMPROVE NAMING"
    }

def main(paths):
    results = []

    for path in paths:
        from pathlib import Path as _Path
        if _Path(path).suffix not in ACCEPTED_EXTENSIONS:
            print(f"Skipping {path} — unsupported extension")
            continue
        print(f"Analyzing {path}")
        results.append(analyze_file(path))

    # Create JSON
    report = {
        "analysis_type": "Identifier Length",
        "threshold": THRESHOLD,
        "summary": {
            "total_files": len(results),
            "failed_files": sum(1 for r in results if r["status_code"] != "OK!")
        },
        "results": results
    }

    with open("identifier_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    print("JSON report generated: identifier_report.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python identifier_length.py <file1> <file2> ...")
        sys.exit(1)

    main(sys.argv[1:])

```
<!-- END_FILE -->

---
<!-- FILE: .github/scripts/release-please-config.json -->
## .github/scripts/release-please-config.json

```json
{
  "packages": {
    ".": {
      "release-type": "python",
      "package-name": "softwareproject",
      "changelog-path": "../../CHANGELOG.md",
      "version-file": "../../pyproject.toml"
    }
  }
}

```
<!-- END_FILE -->

---
<!-- FILE: .github/scripts/render-integrity-html.js -->
## .github/scripts/render-integrity-html.js

```js
'use strict'

/**
 * render-integrity-html.js
 *
 * Reads a security/quality report JSON and generates a self-contained HTML
 * visualisation. Path resolution is environment-variable-driven so both the
 * legacy integrity-GP.yml workflow and the unified quality-metrics.yml can
 * share this script without modification.
 *
 * Environment variables:
 *   REPORT_INPUT_DIR   — directory containing the input JSON
 *                        (default: "integrity-security-report")
 *   REPORT_OUTPUT_DIR  — directory to write the HTML file into
 *                        (default: "integrity-html-report")
 *
 * Input  : <REPORT_INPUT_DIR>/report.json
 *          (legacy fallback: <REPORT_INPUT_DIR>/security-report.json)
 * Output : <REPORT_OUTPUT_DIR>/report.html
 *          (legacy fallback: <REPORT_OUTPUT_DIR>/security-report.html)
 */

const fs = require('fs')
const path = require('path')

// ─── Path resolution ─────────────────────────────────────────────────────────

const INPUT_DIR  = process.env.REPORT_INPUT_DIR  || 'integrity-security-report'
const OUTPUT_DIR = process.env.REPORT_OUTPUT_DIR || 'integrity-html-report'

// Unified pipeline uses report.json; legacy pipeline used security-report.json
function resolveInputPath() {
  const primary = path.join(INPUT_DIR, 'report.json')
  const legacy  = path.join(INPUT_DIR, 'security-report.json')
  if (fs.existsSync(primary)) return primary
  if (fs.existsSync(legacy))  return legacy
  return primary  // will fail with a clear error below
}

const jsonPath  = resolveInputPath()
const htmlFile  = fs.existsSync(path.join(INPUT_DIR, 'report.json'))
  ? 'report.html'
  : 'security-report.html'

// ─── Load JSON ───────────────────────────────────────────────────────────────

let report
try {
  report = JSON.parse(fs.readFileSync(jsonPath, 'utf8'))
} catch (err) {
  console.error(`❌ Could not read ${jsonPath}: ${err.message}`)
  process.exit(1)
}

// ─── Helpers ─────────────────────────────────────────────────────────────────

function esc(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;')
}

const STATUS_STYLE = {
  pass:    { label: '✅ PASS',                 color: '#16a34a', bg: '#dcfce7' },
  warn:    { label: '⚠️ WARN',                 color: '#d97706', bg: '#fef3c7' },
  fail:    { label: '❌ FAIL',                 color: '#dc2626', bg: '#fee2e2' },
  unknown: { label: '❓ N/A',                  color: '#6b7280', bg: '#f3f4f6' },
}

const LEVEL_STYLE = {
  error:   { label: 'ERROR', color: '#dc2626', bg: '#fee2e2' },
  warning: { label: 'WARN',  color: '#d97706', bg: '#fef3c7' },
  notice:  { label: 'INFO',  color: '#2563eb', bg: '#eff6ff' },
}

function badge(status) {
  const s = STATUS_STYLE[status] || STATUS_STYLE.unknown
  return `<span style="background:${s.bg};color:${s.color};border:1px solid ${s.color};
    padding:3px 12px;border-radius:20px;font-weight:700;font-size:12px;white-space:nowrap">${s.label}</span>`
}

function chip(level) {
  const s = LEVEL_STYLE[level] || { label: level.toUpperCase(), color: '#6b7280', bg: '#f3f4f6' }
  return `<span style="background:${s.bg};color:${s.color};padding:2px 7px;border-radius:6px;
    font-size:11px;font-weight:700;letter-spacing:.3px;white-space:nowrap">${s.label}</span>`
}

function stat(value, label, color, bg) {
  return `<div style="background:${bg};border-radius:10px;padding:14px 18px;text-align:center;min-width:80px">
    <div style="font-size:28px;font-weight:800;color:${color};line-height:1">${value}</div>
    <div style="font-size:11px;color:#64748b;margin-top:4px;text-transform:uppercase;letter-spacing:.5px">${label}</div>
  </div>`
}

// ─── Security job section ─────────────────────────────────────────────────────

const JOB_ICONS = {
  'access-control': '🛡️',
  'route-auth':     '🔑',
  'static-scan':    '🔍',
}

function buildJobSection(job) {
  const icon = JOB_ICONS[job.id] || '📋'

  const findingsHtml = job.findings.length === 0
    ? `<p style="color:#64748b;font-style:italic;margin:0;font-size:14px">No security annotations found.</p>`
    : job.findings.map((f) => `
      <div style="display:flex;gap:10px;align-items:flex-start;padding:10px 0;border-bottom:1px solid #f1f5f9">
        <div style="flex-shrink:0;padding-top:1px">${chip(f.level)}</div>
        <div>
          <div style="font-family:ui-monospace,monospace;font-size:13px;color:#1e293b;word-break:break-word">${esc(f.message)}</div>
          ${f.file ? `<div style="font-size:11px;color:#94a3b8;margin-top:3px">📄 ${esc(f.file)}</div>` : ''}
        </div>
      </div>`).join('')

  return `
  <div style="background:#fff;border:1px solid #e2e8f0;border-radius:14px;padding:24px;margin-bottom:20px">
    <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:20px">
      <h2 style="margin:0;font-size:17px;color:#0f172a">${icon} ${esc(job.name)}</h2>
      ${badge(job.status)}
    </div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-bottom:20px">
      ${stat(job.errors,   'Errors',   '#dc2626', '#fee2e2')}
      ${stat(job.warnings, 'Warnings', '#d97706', '#fef3c7')}
      ${stat(job.notices,  'Notices',  '#2563eb', '#eff6ff')}
    </div>
    <div>${findingsHtml}</div>
  </div>`
}

// ─── Quality metric section ───────────────────────────────────────────────────

const QUALITY_META = {
  complexity:        { icon: '📊', name: 'Cyclomatic Complexity', metric: 'complexity',        unit: 'CC avg/fn', decimals: 0 },
  nesting:           { icon: '🌲', name: 'Nesting Depth',         metric: 'max_nesting_depth', unit: 'max depth', decimals: 0 },
  identifier_length: { icon: '🏷️', name: 'Identifier Length',     metric: 'avg_length',        unit: 'avg chars', decimals: 2 },
  fog_index:         { icon: '📖', name: 'Fog Index',             metric: 'fog_score',         unit: 'score',     decimals: 1 },
}

function qualityJobStatus(data) {
  if (!data || data.skipped) return 'unknown'
  return (data.summary && data.summary.failed_files > 0) ? 'fail' : 'pass'
}

function buildQualitySection(key, data) {
  const qm = QUALITY_META[key]
  if (!qm) return ''
  const status = qualityJobStatus(data)

  if (!data || data.skipped) {
    return `
  <div style="background:#fff;border:1px solid #e2e8f0;border-radius:14px;padding:24px;margin-bottom:20px">
    <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px">
      <h2 style="margin:0;font-size:17px;color:#0f172a">${qm.icon} ${esc(qm.name)}</h2>
      ${badge('unknown')}
    </div>
    <p style="color:#64748b;font-style:italic;margin:16px 0 0;font-size:14px">Skipped — no files analysed.</p>
  </div>`
  }

  const results = data.results || []
  const totalFiles = (data.summary && data.summary.total_files != null) ? data.summary.total_files : results.length
  const violations = results.filter((r) => r.status_code !== 'OK' && r.status_code !== 'OK!')
  const passed = totalFiles - violations.length

  const findingsHtml = violations.length === 0
    ? `<p style="color:#64748b;font-style:italic;margin:0;font-size:14px">All ${totalFiles} file(s) passed — no violations found.</p>`
    : violations.map((r) => {
        const val = r[qm.metric]
        const display = typeof val === 'number' ? val.toFixed(qm.decimals) : (val ?? '?')
        const lvl = (r.status_code === 'DANGER' || r.status_code === '⚠️ IMPROVE NAMING') ? 'error' : 'warning'
        return `
      <div style="display:flex;gap:10px;align-items:flex-start;padding:10px 0;border-bottom:1px solid #f1f5f9">
        <div style="flex-shrink:0;padding-top:1px">${chip(lvl)}</div>
        <div>
          <div style="font-family:ui-monospace,monospace;font-size:13px;color:#1e293b;word-break:break-word">
            ${esc(qm.metric)} = ${esc(display)} ${esc(qm.unit)} &nbsp;·&nbsp; threshold: ${esc(String(data.threshold))}
          </div>
          <div style="font-size:11px;color:#94a3b8;margin-top:3px">📄 ${esc(r.file)}</div>
        </div>
      </div>`
      }).join('')

  return `
  <div style="background:#fff;border:1px solid #e2e8f0;border-radius:14px;padding:24px;margin-bottom:20px">
    <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:20px">
      <h2 style="margin:0;font-size:17px;color:#0f172a">${qm.icon} ${esc(qm.name)}</h2>
      ${badge(status)}
    </div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-bottom:20px">
      ${stat(totalFiles,       'Files Analysed', '#2563eb', '#eff6ff')}
      ${stat(data.threshold,   'Threshold',      '#6b7280', '#f3f4f6')}
      ${stat(violations.length,'Violations',     violations.length > 0 ? '#dc2626' : '#16a34a', violations.length > 0 ? '#fee2e2' : '#dcfce7')}
      ${stat(passed,           'Passed',         '#16a34a', '#dcfce7')}
    </div>
    <div>${findingsHtml}</div>
  </div>`
}

// ─── Assemble HTML ───────────────────────────────────────────────────────────

const { metadata: meta, overall, jobs, quality } = report

const QUALITY_ORDER = ['complexity', 'nesting', 'identifier_length', 'fog_index']

const os = STATUS_STYLE[overall.status] || STATUS_STYLE.unknown
const overallLabel = {
  pass:    '✅ ALL CHECKS PASSED',
  warn:    '⚠️ WARNINGS DETECTED',
  fail:    '❌ ISSUES FOUND',
  unknown: '❓ INCOMPLETE',
}[overall.status] || '❓ INCOMPLETE'

const runUrl = meta.repository && meta.run_id
  ? `https://github.com/${esc(meta.repository)}/actions/runs/${esc(meta.run_id)}`
  : null

// Quality rows in the summary table (shown only when quality data is present)
const qualitySummaryRows = quality
  ? QUALITY_ORDER.map((key) => {
      const qm = QUALITY_META[key]
      const data = quality[key]
      const status = qualityJobStatus(data)
      const violations = data ? (data.results || []).filter((r) => r.status_code !== 'OK' && r.status_code !== 'OK!').length : 0
      return `
  <tr>
    <td style="padding:12px 16px"><strong>${qm.icon} ${esc(qm.name)}</strong></td>
    <td style="padding:12px 16px">${badge(status)}</td>
    <td style="padding:12px 16px;text-align:center;font-weight:700;color:${violations > 0 ? '#dc2626' : '#64748b'}">${violations}</td>
    <td style="padding:12px 16px;text-align:center;color:#94a3b8">—</td>
    <td style="padding:12px 16px;text-align:center;color:#94a3b8">—</td>
  </tr>`
    }).join('')
  : ''

// Security rows in the summary table
const securitySummaryRows = jobs.map((j) => `
  <tr>
    <td style="padding:12px 16px"><strong>${JOB_ICONS[j.id] || '📋'} ${esc(j.name)}</strong></td>
    <td style="padding:12px 16px">${badge(j.status)}</td>
    <td style="padding:12px 16px;text-align:center;font-weight:700;color:${j.errors   > 0 ? '#dc2626' : '#64748b'}">${j.errors}</td>
    <td style="padding:12px 16px;text-align:center;font-weight:700;color:${j.warnings > 0 ? '#d97706' : '#64748b'}">${j.warnings}</td>
    <td style="padding:12px 16px;text-align:center;color:#64748b">${j.notices}</td>
  </tr>`).join('')

const summaryRows = qualitySummaryRows + securitySummaryRows

// Quality sections HTML
const qualitySectionsHtml = quality
  ? QUALITY_ORDER.map((key) => buildQualitySection(key, quality[key])).join('')
  : ''

const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Quality &amp; Security Report — ${esc(meta.repository)}</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #f8fafc; color: #334155; margin: 0; padding: 24px 16px; line-height: 1.5;
    }
    table { width: 100%; border-collapse: collapse; }
    th {
      background: #f1f5f9; text-align: left; padding: 10px 16px;
      font-size: 12px; color: #64748b; font-weight: 600;
      text-transform: uppercase; letter-spacing: .5px; border-bottom: 1px solid #e2e8f0;
    }
    td { border-bottom: 1px solid #f1f5f9; font-size: 14px; vertical-align: middle; }
    tr:last-child td { border-bottom: none; }
  </style>
</head>
<body>
  <div style="max-width:960px;margin:0 auto">

    <!-- Header -->
    <div style="background:#fff;border:1px solid #e2e8f0;border-radius:14px;padding:28px;margin-bottom:20px">
      <div style="display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:16px">
        <div>
          <h1 style="margin:0 0 6px;font-size:22px;color:#0f172a">🔐 Quality &amp; Security Report</h1>
          <p style="margin:0;color:#64748b;font-size:13px">
            ${esc(meta.repository)}${meta.ref ? ` · ${esc(meta.ref)}` : ''}${meta.sha ? ` · <code>${esc(meta.sha.slice(0, 7))}</code>` : ''}
          </p>
          <p style="margin:4px 0 0;color:#94a3b8;font-size:12px">
            Generated: ${esc(meta.generated_at)}
            ${runUrl ? ` · <a href="${runUrl}" style="color:#94a3b8">Run #${esc(meta.run_id)}</a>` : ''}
          </p>
        </div>
        <div style="background:${os.bg};border:1px solid ${os.color};border-radius:12px;padding:16px 24px;text-align:center">
          <div style="font-size:15px;font-weight:800;color:${os.color}">${overallLabel}</div>
          <div style="font-size:12px;color:#64748b;margin-top:6px">
            ${overall.total_errors} error(s) · ${overall.total_warnings} warning(s) · ${overall.total_notices} notice(s)
          </div>
        </div>
      </div>
    </div>

    <!-- Pipeline Summary (all 7 jobs) -->
    <div style="background:#fff;border:1px solid #e2e8f0;border-radius:14px;margin-bottom:20px;overflow:hidden">
      <div style="padding:18px 20px 14px;border-bottom:1px solid #e2e8f0">
        <h2 style="margin:0;font-size:15px;color:#0f172a">Pipeline Summary</h2>
      </div>
      <table>
        <thead>
          <tr>
            <th>Job</th><th>Status</th>
            <th style="text-align:center">Violations / Errors</th>
            <th style="text-align:center">Warnings</th>
            <th style="text-align:center">Notices</th>
          </tr>
        </thead>
        <tbody>${summaryRows}</tbody>
      </table>
    </div>

    ${quality ? `
    <!-- Quality Metrics -->
    <h2 style="font-size:15px;color:#0f172a;margin:0 0 14px">📐 Quality Metrics</h2>
    ${qualitySectionsHtml}
    ` : ''}

    <!-- Security Audits -->
    <h2 style="font-size:15px;color:#0f172a;margin:0 0 14px">🔒 Security Audits</h2>
    ${jobs.map(buildJobSection).join('')}

    <p style="text-align:center;color:#94a3b8;font-size:11px;margin-top:24px">
      Quality &amp; Security Pipeline · ${esc(meta.generated_at)}
    </p>
  </div>
</body>
</html>`

// ─── Write output ─────────────────────────────────────────────────────────────

fs.mkdirSync(OUTPUT_DIR, { recursive: true })
const outFile = path.join(OUTPUT_DIR, htmlFile)
fs.writeFileSync(outFile, html, 'utf8')

console.log(`✅ HTML report generated: ${outFile}`)
console.log(`   Status   : ${overall.status.toUpperCase()}`)
console.log(`   Errors   : ${overall.total_errors}`)
console.log(`   Warnings : ${overall.total_warnings}`)
console.log(`   Notices  : ${overall.total_notices}`)

```
<!-- END_FILE -->

---
<!-- FILE: .github/scripts/route-auth-audit.js -->
## .github/scripts/route-auth-audit.js

```js
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
const path = require('path') // Añadido aquí para uso global

// Routes defined here are intentionally public — skip them
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

// Route files that are expected to define protected routes
const PROTECTED_MODULES = [
  'src/router/modules/admin.js',
  'src/router/modules/superAdmin.js',
]

// Discover UX-module routers dynamically
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

  // Extract each route block heuristically by finding `path:` declarations
  const pathMatches = [...content.matchAll(/path:\s*['"`]([^'"`]+)['"`]/g)]

  for (const match of pathMatches) {
    const routePath = match[1]

    if (PUBLIC_PATHS.has(routePath)) continue
    // Skip dynamic token segments (e.g. testview/:id/:token?)
    if (routePath.includes(':token')) continue

    // Inspect surrounding context (~400 chars) for authorization metadata
    const contextStart = Math.max(0, match.index - 50)
    const contextEnd = Math.min(content.length, match.index + 400)
    const context = content.slice(contextStart, contextEnd)

    const hasAuthorizeMeta = context.includes('authorize')
    const hasMetaBlock = context.includes('meta:')

    if (!hasAuthorizeMeta && !hasMetaBlock) {
      if (isProtectedModule) {
        // Protected modules should always declare authorize
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

```
<!-- END_FILE -->

---
<!-- FILE: .github/workflows/deploy.yml -->
## .github/workflows/deploy.yml

```yaml
name: CD Deploy to Render

on:
  pull_request:
    branches:
      - main
    types:
      - closed

jobs:
  deploy:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Docker
        uses: docker/setup-buildx-action@v3

      - name: Login to DockerHub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build Docker image
        run: |
          docker build -t marcpujolnavajo/softwareproject-web:latest .

      - name: Push Docker image
        run: |
          docker push marcpujolnavajo/softwareproject-web:latest

      - name: Trigger Render deploy
        run: |
          curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}

```
<!-- END_FILE -->

---
<!-- FILE: .github/workflows/histogram.yml -->
## .github/workflows/histogram.yml

```yaml


name: Histogram Action

on:
  schedule:
    - cron: "0 6 * * 1"   # every monday at 6:00
  workflow_dispatch:

jobs:
  generate-graph:
    runs-on: ubuntu-latest

    permissions:
      issues: read
      contents: read

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests matplotlib python-decouple

      - name: Run issues histogram script
        working-directory: ./IshikawaTools
        env:
          HISTOGRAM_TOKEN: ${{ secrets.HISTOGRAM_TOKEN }}
        run: python histogram.py

      - name: Upload histogram artifact
        uses: actions/upload-artifact@v4
        with:
          name: issues-histogram-graph
          path: IshikawaTools/issues_histogram.png

```
<!-- END_FILE -->

---
<!-- FILE: .github/workflows/pareto.yml -->
## .github/workflows/pareto.yml

```yaml

name: Pareto Diagram Action


on:
  schedule:
    - cron: "0 3 * * 1"   # every monday at 3:00
  workflow_dispatch:

permissions: 
  issues: read
  contents: read

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.12]

    steps:
    - name: Checkout repo
      uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pandas matplotlib python-decouple requests

    - name: Generate Pareto chart
      working-directory: ./IshikawaTools
      env:
        HISTOGRAM_TOKEN: ${{ secrets.HISTOGRAM_TOKEN }}
      run: python chart.py

    - name: Upload chart
      uses: actions/upload-artifact@v4
      with:
        name: pareto-chart
        path: IshikawaTools/pareto_report.png

```
<!-- END_FILE -->

---
<!-- FILE: .github/workflows/quality-control-aggregator.yml -->
## .github/workflows/quality-control-aggregator.yml

```yaml
name: Quality Control Aggregator

on:
  workflow_run:
    workflows: ["CD Deploy to Render", "Django CI"]
    types:
      - completed
  schedule:
    # Roda as 23:00 de Seg a Sex (UTC)
    - cron: '0 23 * * 1-5'
  workflow_dispatch:

permissions:
  contents: write
  actions: read
  issues: read

jobs:
  aggregate-quality-control:
    runs-on: ubuntu-latest
    env:
      FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          # Token customizado caso precise commitar por cima de protecoes de branch. Senão usar padrao.
          # token: ${{ secrets.PAT_TOKEN }}
          fetch-depth: 1

      - name: Fetch Pipeline Results
        id: fetch_results
        uses: actions/github-script@v7
        with:
          script: |
            let testFails = 0, secFails = 0, codeFails = 0;
            const todayStart = new Date();
            todayStart.setUTCHours(0, 0, 0, 0);
            
            core.info(`Scanning workflows for runs since: ${todayStart.toISOString()}`);

            try {
              // 1. Busca as pipelines/workflows do repositório automaticamente
              const { data } = await github.rest.actions.listRepoWorkflows({
                owner: context.repo.owner,
                repo: context.repo.repo,
              });
              
              const activeWorkflows = data.workflows.filter(w => w.state === 'active');
              core.info(`✅ Encontradas ${activeWorkflows.length} pipelines ativas no repositório.`);

              for (const workflow of activeWorkflows) {
                // Pular o próprio aggregator para evitar loop ou ruído
                if (workflow.name === 'Quality Control Aggregator' || workflow.name === 'PR/Commit Checks Summary') continue;

                const { data: { workflow_runs } } = await github.rest.actions.listWorkflowRuns({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  workflow_id: workflow.id,
                  per_page: 20
                });

                const failedToday = workflow_runs.filter(run => 
                  run.conclusion === 'failure' && 
                  new Date(run.created_at) >= todayStart
                );

                if (failedToday.length > 0) {
                  core.info(`- ❌ Workflow '${workflow.name}' teve ${failedToday.length} falhas hoje.`);
                  const nameLower = workflow.name.toLowerCase();
                  
                  if (nameLower.includes('django')) testFails += failedToday.length;
                  else if (nameLower.includes('gitguardian') || nameLower.includes('security')) secFails += failedToday.length;
                  else if (nameLower.includes('deploy') || nameLower.includes('code issue')) codeFails += failedToday.length;
                } else {
                   core.info(`- ✅ Workflow '${workflow.name}' sem falhas registradas hoje.`);
                }
              }
            } catch (error) {
              core.warning(`Erro ao buscar pipelines: ${error.message}`);
            }
            
            core.exportVariable('TEST_ERRORS', testFails);
            core.exportVariable('SECURITY_ISSUES', secFails);
            core.exportVariable('CODE_SMELLS', codeFails);

      - name: Execute QC Aggregator Script
        uses: actions/github-script@v7
        with:
          script: |
            const script = require('./.github/scripts/generate_qc_report.js');
            await script({github, context, core});

      - name: Commit Updated Check Sheet
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore(qc): Update Daily Quality Control Check Sheet"
          file_pattern: .github/quality_control_data.json

```
<!-- END_FILE -->

---
<!-- FILE: .github/workflows/quality-metrics.yml -->
## .github/workflows/quality-metrics.yml

```yaml
# ┌─────────────────────────────────────────────────────────────────────────────┐
# │                     Unified Quality & Security Pipeline                      │
# │                                                                              │
# │  Consolidates 6 former workflows into a single dependency-ordered graph:    │
# │                                                                              │
# │  TIER 1 (parallel) ─── Quality Metrics                                      │
# │    job1 · cyclomatic-complexity   (Python + JS/TS)                          │
# │    job2 · nesting-depth           (Python + JS/TS)                          │
# │    job3 · identifier-length       (Python + JS/TS)                          │
# │    job4 · fog-index-metrics       (Python, JS/TS, Java, HTML)               │
# │                                                                              │
# │  TIER 2 (parallel, after TIER 1) ─── Security Audits                       │
# │    job5 · access-control-audit    (multi-stack bash grep)                   │
# │    job6 · route-auth-audit        (Vue Router + Python routes)              │
# │    job7 · static-security-scan    (Semgrep OWASP / auth bypass)             │
# │                                                                              │
# │  TIER 3 (always, after TIER 2) ─── Report                                  │
# │    job8 · generate-report         (JSON + HTML consolidated artifact)       │
# │                                                                              │
# │  Replaces: ComplexiCheckGP.yml, conditional-nestingGP.yml,                  │
# │            identifier_lengthGP.yml, metrics-Gp.yml,                         │
# │            integrity-GP.yml, Metrics-html-reportGP.yml                      │
# └─────────────────────────────────────────────────────────────────────────────┘

name: Quality & Security Pipeline

on:
  pull_request:
    types: [opened, synchronize, reopened]
  push:
  schedule:
    - cron: '0 3 * * 1'   # Weekly integrity sweep — Monday 03:00 UTC
  workflow_dispatch:

permissions:
  contents: read

# ═══════════════════════════════════════════════════════════════════════════════
# TIER 1 — Quality Metric Jobs  (run in parallel)
# ═══════════════════════════════════════════════════════════════════════════════

jobs:

  # ─────────────────────────────────────────────────────────────────────────────
  # JOB 1 · Cyclomatic Complexity
  # Source: ComplexiCheckGP.yml
  # Script: CyclomaticMetricGP.py  (Python AST + JS/TS regex)
  # Gate  : fail if any file exceeds complexity threshold (default 15)
  # ─────────────────────────────────────────────────────────────────────────────
  cyclomatic-complexity:
    name: "📊 Cyclomatic Complexity"
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Resolve target files
        id: target
        run: |
          EXT_PATTERN='\.(py|js|ts|jsx|tsx|mjs|cjs)$'
          EVENT="${{ github.event_name }}"
          BEFORE="${{ github.event.before }}"

          if [[ "$EVENT" == "schedule" || "$EVENT" == "workflow_dispatch" ]]; then
            FILES=$(find . src/ functions/src/ weight_function/ -type f 2>/dev/null \
              | grep -E "$EXT_PATTERN" \
              | grep -v node_modules | grep -v /dist/ \
              | sort | tr '\n' ' ' || true)

          elif [[ "$EVENT" == "pull_request" ]]; then
            FILES=$(git diff --name-only --diff-filter=AM \
              "origin/${{ github.base_ref }}" HEAD 2>/dev/null \
              | grep -E "$EXT_PATTERN" | tr '\n' ' ' || true)

          else
            # push — fall back to full scan when branch is new (zeroed before SHA)
            if [[ "$BEFORE" =~ ^0+$ ]]; then
              FILES=$(find . src/ functions/src/ -type f 2>/dev/null \
                | grep -E "$EXT_PATTERN" | grep -v node_modules | sort | tr '\n' ' ' || true)
            else
              FILES=$(git diff --name-only --diff-filter=AM \
                "$BEFORE" "${{ github.sha }}" 2>/dev/null \
                | grep -E "$EXT_PATTERN" | tr '\n' ' ' || true)
            fi
          fi

          # Fallback — if diff produced no code files, full-scan src/
          if [[ -z "${FILES// /}" ]]; then
            FILES=$(find . src/ functions/src/ weight_function/ -type f 2>/dev/null \
              | grep -E "$EXT_PATTERN" \
              | grep -v node_modules | grep -v /dist/ \
              | sort | tr '\n' ' ' || true)
          fi

          FOUND=$([ -n "${FILES// /}" ] && echo 'true' || echo 'false')
          echo "files=$FILES"      >> "$GITHUB_OUTPUT"
          echo "found=$FOUND"      >> "$GITHUB_OUTPUT"

      - name: Run complexity analysis
        run: |
          mkdir -p quality-job1
          if [[ "${{ steps.target.outputs.found }}" == "true" ]]; then
            python .github/scripts/CyclomaticMetricGP.py \
              ${{ steps.target.outputs.files }} \
              > quality-job1/complexity-results.json
          else
            echo '{"analysis_type":"Cyclomatic Complexity","threshold":15,"summary":{"total_files":0,"failed_files":0},"results":[],"skipped":true}' \
              > quality-job1/complexity-results.json
            echo "::notice::No supported files changed — complexity check skipped"
          fi
          cat quality-job1/complexity-results.json

      - name: Gate — fail if threshold exceeded
        run: |
          python3 - <<'PYEOF'
          import json, sys
          with open("quality-job1/complexity-results.json") as f:
              d = json.load(f)
          failed = d["summary"]["failed_files"]
          if failed > 0:
              print(f"::error::Cyclomatic complexity: {failed} file(s) exceed threshold {d['threshold']}")
              sys.exit(1)
          print(f"✅ Cyclomatic complexity OK — {d['summary']['total_files']} file(s) analysed")
          PYEOF

      - name: Upload artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: quality-job1
          path: quality-job1/complexity-results.json
          retention-days: 30
          if-no-files-found: warn

  # ─────────────────────────────────────────────────────────────────────────────
  # JOB 2 · Nesting Depth
  # Source: conditional-nestingGP.yml
  # Script: depth_conditional_nesting_GP.py  (Python AST + brace-tracking)
  # Gate  : script exits 1 when any file exceeds CRITICAL_THRESHOLD (5)
  # ─────────────────────────────────────────────────────────────────────────────
  nesting-depth:
    name: "🌲 Nesting Depth"
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Detect changed files
        id: changed-files
        uses: tj-actions/changed-files@v46
        with:
          files: |
            **/*.py
            **/*.js
            **/*.ts
            **/*.jsx
            **/*.tsx
            **/*.mjs
            **/*.cjs

      - name: Resolve target files (scheduled / manual full scan)
        id: all-files
        if: github.event_name == 'schedule' || github.event_name == 'workflow_dispatch'
        run: |
          FILES=$(find . src/ functions/src/ weight_function/ -type f 2>/dev/null \
            | grep -E '\.(py|js|ts|jsx|tsx|mjs|cjs)$' \
            | grep -v node_modules | grep -v /dist/ | sort | tr '\n' ' ' || true)
          echo "files=$FILES" >> "$GITHUB_OUTPUT"

      - name: Run nesting depth analysis
        run: |
          # Prefer full-scan list for schedule/dispatch; fall back to changed-files
          FILES="${{ steps.all-files.outputs.files }}${{ steps.changed-files.outputs.all_changed_files }}"
          # Fallback — if diff produced no code files, full-scan src/
          if [[ -z "${FILES// /}" ]]; then
            FILES=$(find . src/ functions/src/ weight_function/ -type f 2>/dev/null \
              | grep -E '\.(py|js|ts|jsx|tsx|mjs|cjs)$' \
              | grep -v node_modules | grep -v /dist/ | sort | tr '\n' ' ' || true)
          fi
          if [[ -n "${FILES// /}" ]]; then
            python .github/scripts/depth_conditional_nesting_GP.py $FILES
          else
            echo '{"analysis_type":"Depth of Conditional Nesting","threshold":5,"summary":{"total_files":0,"failed_files":0},"results":[]}' \
              > nesting_metrics.json
            echo "::notice::No supported files changed — nesting depth check skipped"
          fi

      - name: Stage artifact
        if: always()
        run: mkdir -p quality-job2 && mv nesting_metrics.json quality-job2/ 2>/dev/null || true

      - name: Upload artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: quality-job2
          path: quality-job2/nesting_metrics.json
          retention-days: 30
          if-no-files-found: warn

  # ─────────────────────────────────────────────────────────────────────────────
  # JOB 3 · Identifier Length
  # Source: identifier_lengthGP.yml
  # Script: len_identifiersGP.py  (Python + JS/TS keyword-aware regex)
  # Gate  : fail if any file has average identifier length < 10
  # ─────────────────────────────────────────────────────────────────────────────
  identifier-length:
    name: "🏷️ Identifier Length"
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Detect changed files
        id: changed-files
        uses: tj-actions/changed-files@v46
        with:
          files: |
            **/*.py
            **/*.js
            **/*.ts
            **/*.jsx
            **/*.tsx
            **/*.mjs
            **/*.cjs

      - name: Resolve target files (scheduled / manual full scan)
        id: all-files
        if: github.event_name == 'schedule' || github.event_name == 'workflow_dispatch'
        run: |
          FILES=$(find . src/ functions/src/ weight_function/ -type f 2>/dev/null \
            | grep -E '\.(py|js|ts|jsx|tsx|mjs|cjs)$' \
            | grep -v node_modules | grep -v /dist/ | sort | tr '\n' ' ' || true)
          echo "files=$FILES" >> "$GITHUB_OUTPUT"

      - name: Run identifier length analysis
        run: |
          FILES="${{ steps.all-files.outputs.files }}${{ steps.changed-files.outputs.all_changed_files }}"
          # Exclude tooling scripts — quality gates target application code only
          FILTERED=$(echo "$FILES" | tr ' ' '\n' | grep -v '^\.github' | tr '\n' ' ')
          # No fallback: identifier-length gates newly-changed code only.
          # A full-scan fails on legacy files that predate this threshold.
          if [[ -n "${FILTERED// /}" ]]; then
            python .github/scripts/len_identifiersGP.py $FILTERED
          else
            echo '{"analysis_type":"Identifier Length","threshold":6,"summary":{"total_files":0,"failed_files":0},"results":[]}' \
              > identifier_report.json
            echo "::notice::No supported files changed — identifier length check skipped"
          fi

      - name: Gate — fail if threshold exceeded
        run: |
          python3 - <<'PYEOF'
          import json, sys
          with open("identifier_report.json") as f:
              d = json.load(f)
          failed = d["summary"]["failed_files"]
          if failed > 0:
              for r in d.get("results", []):
                  if r.get("status_code") != "OK!":
                      print(f"::error file={r['file']}::Average identifier length {r['avg_length']:.1f} is below threshold {d['threshold']}")
              sys.exit(1)
          print(f"✅ Identifier length OK — {d['summary']['total_files']} file(s) analysed")
          PYEOF

      - name: Stage artifact
        if: always()
        run: mkdir -p quality-job3 && mv identifier_report.json quality-job3/ 2>/dev/null || true

      - name: Upload artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: quality-job3
          path: quality-job3/identifier_report.json
          retention-days: 30
          if-no-files-found: warn

  # ─────────────────────────────────────────────────────────────────────────────
  # JOB 4 · Fog Index (Comment Readability)
  # Source: metrics-Gp.yml
  # Script: fog_comments_indexGP.py  (Gunning Fog via textstat)
  # Scope : always full-tree scan (readability is a project-wide concern)
  # Gate  : fail if any file has average fog score > 17
  # ─────────────────────────────────────────────────────────────────────────────
  fog-index-metrics:
    name: "📖 Fog Index"
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install textstat
        run: pip install textstat --quiet

      - name: Run fog index analysis
        run: |
          mkdir -p quality-job4
          python .github/scripts/fog_comments_indexGP.py . \
            > quality-job4/fog-results.json
          cat quality-job4/fog-results.json

      - name: Gate — fail if threshold exceeded
        run: |
          python3 - <<'PYEOF'
          import json, sys
          with open("quality-job4/fog-results.json") as f:
              d = json.load(f)
          failed = d["summary"]["failed_files"]
          if failed > 0:
              for r in d.get("results", []):
                  if r.get("status_code") == "COMPLEX":
                      avg = r.get("avg_fog") or "N/A"
                      print(f"::error file={r['file']}::Fog index {avg} exceeds threshold {d['threshold']}")
              sys.exit(1)
          print(f"✅ Fog index OK — {d['summary']['total_files']} file(s) analysed")
          PYEOF

      - name: Upload artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: quality-job4
          path: quality-job4/fog-results.json
          retention-days: 30
          if-no-files-found: warn

# ═══════════════════════════════════════════════════════════════════════════════
# TIER 2 — Security Audit Jobs  (parallel, start after all TIER 1 jobs finish)
# ═══════════════════════════════════════════════════════════════════════════════

  # ─────────────────────────────────────────────────────────────────────────────
  # JOB 5 · Access Control Audit
  # Source: integrity-GP.yml — Job 1
  # Covers: Express/Fastify, Django/Flask, Spring Boot, SQL, Docker/K8s, REST
  # ─────────────────────────────────────────────────────────────────────────────
  access-control-audit:
    name: "🛡️ Access Control Audit"
    runs-on: ubuntu-latest
    needs: [cyclomatic-complexity, nesting-depth, identifier-length, fog-index-metrics]
    if: always()

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Audit Access Controls
        run: |
          mkdir -p quality-job5
          exec > >(tee -a quality-job5/access-control.log) 2>&1
          echo "=== Access Control Audit ==="
          DETECTED=0
          FAIL=0

          # ── Express / Fastify (Node.js) ──────────────────
          if find . -name "*.js" -o -name "*.ts" | grep -v node_modules | xargs grep -lE "express\(\)|fastify\(\)" 2>/dev/null | grep -q .; then
            echo "--- Detected: Express/Fastify ---"
            DETECTED=1

            if grep -rEn 'origin\s*:\s*['"'"'"]?\*['"'"'"]?' --include="*.js" --include="*.ts" . 2>/dev/null | grep -v node_modules | grep -v "//"; then
              echo "::error::Express/Fastify — CORS allows all origins (*). Restrict to known domains."
              FAIL=1
            fi

            UNPROTECTED=$(grep -rEn "app\.(get|post|put|delete|patch)\s*\(" --include="*.js" --include="*.ts" . 2>/dev/null \
              | grep -v node_modules | grep -v "//" \
              | grep -vE "auth|middleware|verify|protect|guard|token|jwt|session")
            if [ -n "$UNPROTECTED" ]; then
              COUNT=$(echo "$UNPROTECTED" | wc -l | tr -d ' ')
              echo "::warning::Express/Fastify — $COUNT route(s) found with no recognizable auth middleware:"
              echo "$UNPROTECTED"
            fi
          fi

          # ── Django / Flask (Python) ──────────────────────
          if find . -name "*.py" | grep -v node_modules | xargs grep -lE "from django|from flask|import flask" 2>/dev/null | grep -q .; then
            echo "--- Detected: Django/Flask ---"
            DETECTED=1

            PROTECTED=$(grep -rEn "@login_required|@permission_required|@jwt_required|LoginRequiredMixin" --include="*.py" . 2>/dev/null)
            if [ -z "$PROTECTED" ]; then
              echo "::error::Django/Flask — No @login_required or @permission_required decorators found. Views may be publicly accessible."
              FAIL=1
            else
              echo "✅ Django/Flask — auth decorators detected"
            fi
          fi

          # ── Spring Boot (Java) ───────────────────────────
          if find . -name "*.java" 2>/dev/null | grep -q .; then
            echo "--- Detected: Spring Boot (Java) ---"
            DETECTED=1

            if ! grep -rEn "@PreAuthorize|SecurityFilterChain|WebSecurityConfigurerAdapter|antMatchers" --include="*.java" . 2>/dev/null | grep -q .; then
              echo "::error::Spring Boot — No security configuration found (@PreAuthorize / SecurityFilterChain). Routes may be unprotected."
              FAIL=1
            else
              echo "✅ Spring Boot — security configuration detected"
            fi

            if grep -rEn "\.permitAll\(\)" --include="*.java" . 2>/dev/null | grep -v "//"; then
              echo "::warning::Spring Boot — .permitAll() detected. Verify this is only for intended public endpoints."
            fi
          fi

          # ── PostgreSQL / MySQL ───────────────────────────
          if find . \( -name "*.sql" -o -name "*.pgsql" \) 2>/dev/null | grep -q .; then
            echo "--- Detected: SQL schema files ---"
            DETECTED=1

            if grep -rEin "GRANT ALL.*TO PUBLIC|GRANT ALL PRIVILEGES.*TO PUBLIC" --include="*.sql" --include="*.pgsql" . 2>/dev/null; then
              echo "::error::Database — GRANT ALL TO PUBLIC detected. This exposes all tables to unauthenticated users."
              FAIL=1
            fi

            if grep -rEin "GRANT.*TO\s+''" --include="*.sql" --include="*.pgsql" . 2>/dev/null; then
              echo "::error::Database — GRANT to empty user detected. This may expose data to anonymous connections."
              FAIL=1
            fi

            if [ "$FAIL" -eq 0 ]; then
              echo "✅ SQL schema — no public grant issues detected"
            fi
          fi

          # ── Docker / Kubernetes ──────────────────────────
          if find . \( -name "Dockerfile*" -o -name "docker-compose*.yml" -o -name "deployment.yaml" -o -name "*.k8s.yml" \) -not -path "*/node_modules/*" 2>/dev/null | grep -q .; then
            echo "--- Detected: Docker/Kubernetes ---"
            DETECTED=1

            if grep -rEn "['\"]?(3306|5432|27017|6379|9200|2375):[0-9]+['\"]?" --include="*.yml" --include="*.yaml" . 2>/dev/null | grep -v node_modules; then
              echo "::warning::Docker — Sensitive port(s) (DB/cache/Docker daemon) mapped to host. Restrict to internal networks."
            fi

            for df in $(find . -name "Dockerfile*" -not -path "*/node_modules/*" 2>/dev/null); do
              if grep -q "^FROM" "$df"; then
                if ! grep -qE "^USER[[:space:]]+" "$df"; then
                  echo "::warning file=$df::Dockerfile has no USER directive — container may run as root."
                elif grep -qE "^USER[[:space:]]+root" "$df"; then
                  echo "::warning file=$df::Dockerfile sets USER root explicitly — containers should not run as root."
                fi
              fi
            done
          fi

          # ── REST API / Generic ───────────────────────────
          if find . \( -name "*.js" -o -name "*.ts" -o -name "*.py" -o -name "*.java" \) -not -path "*/node_modules/*" 2>/dev/null | grep -q .; then
            echo "--- Running generic REST API checks ---"
            DETECTED=1

            if grep -rEn "jwt\.sign\(|jwt\.verify\(" --include="*.js" --include="*.ts" . 2>/dev/null \
              | grep -v node_modules | grep -v "//" \
              | grep -vE "process\.env|config\.|secrets\."; then
              echo "::warning::REST API — JWT call found with possible hardcoded secret. Use environment variables."
            fi

            if grep -rEn "Access-Control-Allow-Origin:\s*\*" --include="*.js" --include="*.ts" --include="*.py" --include="*.java" . 2>/dev/null \
              | grep -v node_modules | grep -v "//"; then
              echo "::error::REST API — Access-Control-Allow-Origin: * found in source code. Restrict CORS to known origins."
              FAIL=1
            fi
          fi

          # ── Final result ─────────────────────────────────
          echo ""
          if [ "$DETECTED" -eq 0 ]; then
            echo "::error::Access Control Audit — No recognizable technology stack detected."
            exit 1
          fi

          if [ "$FAIL" -eq 1 ]; then
            echo "❌ Access Control Audit failed — critical issues found above"
            exit 1
          fi

          echo "✅ Access Control Audit passed"

      - name: Upload artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: quality-job5
          path: quality-job5/access-control.log
          retention-days: 30
          if-no-files-found: warn

  # ─────────────────────────────────────────────────────────────────────────────
  # JOB 6 · Route Authorization Audit
  # Source: integrity-GP.yml — Job 2
  # Checks: Vue Router beforeEach guard + route meta + Python route decorators
  # ─────────────────────────────────────────────────────────────────────────────
  route-auth-audit:
    name: "🔑 Route Authorization Audit"
    runs-on: ubuntu-latest
    needs: [cyclomatic-complexity, nesting-depth, identifier-length, fog-index-metrics]
    if: always()

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 'lts/*'

      - name: Verify Router Guard Integrity
        run: |
          mkdir -p quality-job6
          exec > >(tee -a quality-job6/route-auth.log) 2>&1
          echo "=== Router Guard Integrity Check ==="
          FAIL=0

          ROUTER="src/app/router/index.js"
          
          if [ -f "$ROUTER" ]; then
            if ! grep -q "router\.beforeEach" "$ROUTER"; then
              echo "::error file=$ROUTER::router.beforeEach guard not found — all routes may be unprotected"
              FAIL=1
            fi

            if ! grep -q "authorize" "$ROUTER"; then
              echo "::error file=$ROUTER::No authorization enforcement found in router guard"
              FAIL=1
            fi

            if ! grep -qE "Auth\.user|autoSignIn|currentUser" "$ROUTER"; then
              echo "::error file=$ROUTER::Router guard does not appear to verify authentication state"
              FAIL=1
            fi

            if ! grep -q "signin" "$ROUTER"; then
              echo "::warning file=$ROUTER::Router guard may not redirect unauthenticated users to /signin"
            fi

            if [ "$FAIL" -eq 0 ]; then
              echo "✅ Router guard integrity verified"
            else
              exit 1
            fi
          else
            echo "::notice::Vue Router not found — skipping frontend router guard check (Django project)"
            echo "N/A: File $ROUTER not found." >> quality-job6/route-auth.log
          fi

      - name: Audit Route Definitions for Missing Auth Metadata
        run: |
          set -o pipefail
          node .github/scripts/route-auth-audit.js 2>&1 | tee -a quality-job6/route-auth.log

      - name: Upload artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: quality-job6
          path: quality-job6/route-auth.log
          retention-days: 30
          if-no-files-found: warn

  # ─────────────────────────────────────────────────────────────────────────────
  # JOB 7 · Static Security Scan (OWASP / Semgrep)
  # Source: integrity-GP.yml — Job 3
  # Scans : JS, TS, Vue, Python, Java  +  C# via p/csharp
  # ─────────────────────────────────────────────────────────────────────────────
  static-security-scan:
    name: "🔍 Static Security Scan (OWASP)"
    runs-on: ubuntu-latest
    needs: [cyclomatic-complexity, nesting-depth, identifier-length, fog-index-metrics]
    if: always()

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Install Semgrep
        run: pip install semgrep --quiet

      - name: Run OWASP Top 10 Scan
        run: |
          mkdir -p quality-job7
          exec > >(tee -a quality-job7/static-scan.log) 2>&1
          semgrep \
            --config=p/owasp-top-ten \
            --config=p/javascript \
            --exclude=node_modules \
            --exclude=dist \
            --exclude=tests \
            --include="*.js" \
            --include="*.vue" \
            --error \
            src/ functions/src/
        continue-on-error: true

      - name: Run C# security scan (Semgrep p/csharp)
        run: |
          exec >> quality-job7/static-scan.log 2>&1
          if find . -name "*.cs" -not -path "*/node_modules/*" 2>/dev/null | grep -q .; then
            echo "--- C# files detected — running p/csharp ruleset ---"
            semgrep \
              --config=p/csharp \
              --exclude=node_modules \
              --include="*.cs" \
              --error \
              . || true
          else
            echo "::notice::No .cs files found — C# scan skipped"
          fi

      - name: Scan for Auth Bypass Patterns
        run: |
          exec >> quality-job7/static-scan.log 2>&1
          echo "=== Auth Bypass Pattern Scan ==="
          FAIL=0

          if find . \( -name "*.js" -o -name "*.ts" -o -name "*.vue" -o -name "*.py" -o -name "*.java" \) \
            -not -path "*/node_modules/*" -not -path "*/dist/*" 2>/dev/null | grep -q .; then
            DETECTED=1
          else
            DETECTED=0
          fi

          # Unconditional frontend router guard bypass
          if grep -rEn "next\(true\)|beforeEach.*return true|navigate\(.*\{.*replace.*\}\)" \
            --include="*.js" --include="*.ts" --include="*.vue" . 2>/dev/null \
            | grep -v node_modules | grep -v "//"; then
            echo "::warning::Possible unconditional navigation guard bypass detected"
          fi

          # Hardcoded passwords / tokens
          if grep -rEn "password\s*[=:]\s*['\"][^'\"]{4,}['\"]" \
            --include="*.js" --include="*.ts" --include="*.vue" --include="*.py" --include="*.java" \
            . 2>/dev/null \
            | grep -v node_modules \
            | grep -v "//" \
            | grep -vE "[[:space:]]:[a-zA-Z][a-zA-Z0-9_-]*=" \
            | grep -q .; then
            grep -rEn "password\s*[=:]\s*['\"][^'\"]{4,}['\"]" \
              --include="*.js" --include="*.ts" --include="*.vue" --include="*.py" --include="*.java" \
              . 2>/dev/null \
              | grep -v node_modules | grep -v "//" \
              | grep -vE "[[:space:]]:[a-zA-Z][a-zA-Z0-9_-]*="
            echo "::error::Hardcoded password value detected in source code"
            FAIL=1
          fi

          # eval() / exec() usage
          if grep -rEn "\beval\(|\bexec\(" \
            --include="*.js" --include="*.ts" --include="*.vue" --include="*.py" \
            . 2>/dev/null | grep -v node_modules | grep -v "//"; then
            echo "::warning::eval()/exec() usage detected — review for potential code injection risk"
          fi

          # Disabled SSL/TLS certificate verification
          if grep -rEn "rejectUnauthorized\s*:\s*false|verify\s*=\s*False|ssl_verify\s*=\s*false" \
            --include="*.js" --include="*.ts" --include="*.py" --include="*.java" \
            . 2>/dev/null | grep -v node_modules | grep -v "//"; then
            echo "::error::SSL/TLS certificate verification disabled — man-in-the-middle attack risk"
            FAIL=1
          fi

          # Sensitive tokens in URL query strings
          if grep -rEn "[?&](token|api_key|apikey|access_token|secret)=" \
            --include="*.js" --include="*.ts" --include="*.vue" --include="*.py" \
            . 2>/dev/null | grep -v node_modules | grep -v "//"; then
            echo "::warning::Sensitive token/key passed in URL query string — use Authorization header instead."
          fi

          # ── Final result ─────────────────────────────────
          echo ""
          if [ "$DETECTED" -eq 0 ]; then
            echo "::error::Auth Bypass Scan — No source files matched. Cannot confirm scan was effective."
            exit 1
          fi

          if [ "$FAIL" -eq 1 ]; then
            exit 1
          fi

          echo "✅ Auth bypass pattern scan passed"

      - name: Upload artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: quality-job7
          path: quality-job7/static-scan.log
          retention-days: 30
          if-no-files-found: warn

# ═══════════════════════════════════════════════════════════════════════════════
# TIER 3 — Report Generation  (always runs, even if upstream jobs failed)
# ═══════════════════════════════════════════════════════════════════════════════

  # ─────────────────────────────────────────────────────────────────────────────
  # JOB 8 · Generate Consolidated Report
  # Source: integrity-GP.yml — Job 4  +  Metrics-html-reportGP.yml (merged)
  # Output: quality-security-report/report.json  +  report.html
  # ─────────────────────────────────────────────────────────────────────────────
  generate-report:
    name: "📋 Generate Consolidated Report"
    runs-on: ubuntu-latest
    needs:
      - cyclomatic-complexity
      - nesting-depth
      - identifier-length
      - fog-index-metrics
      - access-control-audit
      - route-auth-audit
      - static-security-scan
    if: always()

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 'lts/*'

      # Download all seven job artifacts (continue-on-error: true so a missing
      # artifact from a skipped or failed job does not block the report)
      - name: Download quality-job1 (cyclomatic complexity)
        uses: actions/download-artifact@v4
        with:
          name: quality-job1
          path: quality-job1/
        continue-on-error: true

      - name: Download quality-job2 (nesting depth)
        uses: actions/download-artifact@v4
        with:
          name: quality-job2
          path: quality-job2/
        continue-on-error: true

      - name: Download quality-job3 (identifier length)
        uses: actions/download-artifact@v4
        with:
          name: quality-job3
          path: quality-job3/
        continue-on-error: true

      - name: Download quality-job4 (fog index)
        uses: actions/download-artifact@v4
        with:
          name: quality-job4
          path: quality-job4/
        continue-on-error: true

      - name: Download quality-job5 (access control)
        uses: actions/download-artifact@v4
        with:
          name: quality-job5
          path: quality-job5/
        continue-on-error: true

      - name: Download quality-job6 (route auth)
        uses: actions/download-artifact@v4
        with:
          name: quality-job6
          path: quality-job6/
        continue-on-error: true

      - name: Download quality-job7 (static scan)
        uses: actions/download-artifact@v4
        with:
          name: quality-job7
          path: quality-job7/
        continue-on-error: true

      - name: Generate JSON report
        env:
          GITHUB_REPOSITORY: ${{ github.repository }}
          GITHUB_REF_NAME:   ${{ github.ref_name }}
          GITHUB_SHA:        ${{ github.sha }}
          GITHUB_RUN_ID:     ${{ github.run_id }}
          # Tell the script to use the new artifact paths and output directory
          QUALITY_ARTIFACT_PREFIX: quality-job
          REPORT_OUTPUT_DIR:       quality-security-report
        run: node .github/scripts/generate-integrity-report.js

      - name: Render HTML report
        env:
          GITHUB_REPOSITORY: ${{ github.repository }}
          GITHUB_REF_NAME:   ${{ github.ref_name }}
          GITHUB_SHA:        ${{ github.sha }}
          GITHUB_RUN_ID:     ${{ github.run_id }}
          # Tell the renderer where to find the JSON and where to write HTML
          REPORT_INPUT_DIR:  quality-security-report
          REPORT_OUTPUT_DIR: quality-security-report
        run: node .github/scripts/render-integrity-html.js

      - name: Upload consolidated report
        uses: actions/upload-artifact@v4
        with:
          name: quality-security-report
          path: quality-security-report/
          retention-days: 30
          if-no-files-found: error

```
<!-- END_FILE -->

---
<!-- FILE: .github/workflows/realease-please.yml -->
## .github/workflows/realease-please.yml

```yaml
name: release-please

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: write
  issues: write
  pull-requests: write

jobs:
  release-please:
    runs-on: ubuntu-latest
    steps:
      - uses: googleapis/release-please-action@v4
        with:
          token: ${{ secrets.MY_RELEASE_TOKEN }}
          config-file: .github/scripts/release-please-config.json
          manifest-file: .github/scripts/.release-please-manifest.json

```
<!-- END_FILE -->

---
<!-- FILE: .github/workflows/runchart.yml -->
## .github/workflows/runchart.yml

```yaml

name: Run Chart Action

on:  
  schedule:
    - cron: "0 3 * * 1"   # every monday at 3:00
  workflow_dispatch:
  #push:
  #  branches: master

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      # Give the default GITHUB_TOKEN write permission to commit and push the
      # added or changed files to the repository.
      contents: write
      issues: read

    steps:
      - name: Checkout repo
        uses: actions/checkout@v5
        with:
          ref: ${{ github.head_ref }}
          # Value already defaults to true, but `persist-credentials` is required to push new commits to the repository.
          persist-credentials: true

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install matplotlib>=3.7.3 python-decouple requests

      - name: Run script
        working-directory: ./IshikawaTools
        env:
          HISTOGRAM_TOKEN: ${{ secrets.HISTOGRAM_TOKEN }}
        run: python runchart.py

      - name: Upload chart
        uses: actions/upload-artifact@v4
        with:
          name: runchart
          path: IshikawaTools/issue_runchart.png

```
<!-- END_FILE -->

---
<!-- FILE: .github/workflows/test.yml -->
## .github/workflows/test.yml

```yaml
name: CI Django Test

on:
  push:
    branches:
      - '**'
  pull_request:
    branches:
      - '**'

jobs:
  build:

    runs-on: ubuntu-latest

    env:
      API_KEY_LOCAL_1: ${{ secrets.API_KEY_LOCAL_1 }}
      API_KEY_LOCAL_2: ${{ secrets.API_KEY_LOCAL_2 }}
      API_KEY_LOCAL_3: ${{ secrets.API_KEY_LOCAL_3 }}

    strategy:
      max-parallel: 4
      matrix:
        python-version: ["3.14"]

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install uv
      run: pip install uv
    - name: Install dependencies
      run: uv sync
    - name: Run Tests
      run: uv run python manage.py test

```
<!-- END_FILE -->

---
<!-- FILE: .gitignore -->
## .gitignore

```
.venv
.env
__pycache__/
*.pyc
staticfiles/
.idea
codebundle.md

```
<!-- END_FILE -->

---
<!-- FILE: .gitmodules -->
## .gitmodules

```
[submodule "Models-de-proc-s-26"]
	path = Models-de-proc-s-26
	url = https://github.com/xemyst/Models-de-proc-s-26.git

```
<!-- END_FILE -->

---
<!-- FILE: accounts/__init__.py -->
## accounts/__init__.py

```py


```
<!-- END_FILE -->

---
<!-- FILE: accounts/admin.py -->
## accounts/admin.py

```py
from django.contrib import admin

# Register your models here.

```
<!-- END_FILE -->

---
<!-- FILE: accounts/apps.py -->
## accounts/apps.py

```py
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

```
<!-- END_FILE -->

---
<!-- FILE: accounts/forms.py -->
## accounts/forms.py

```py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator

from app.models import User


username_validator = UnicodeUsernameValidator()


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label='First Name',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'First Name',
            'autocomplete': 'given-name'
        })
    )
    last_name = forms.CharField(
        label='Last Name',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Last Name',
            'autocomplete': 'family-name'
        })
    )
    email = forms.EmailField(
        label='Email Address',
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'email@example.com',
            'autocomplete': 'email'
        })
    )
    username = forms.CharField(
        label='Username',
        required=True,
        max_length=150,
        validators=[username_validator],
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Username',
            'autocomplete': 'username'
        })
    )
    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Password',
            'autocomplete': 'new-password'
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirm Password',
            'autocomplete': 'new-password'
        })
    )
    terms_of_service = forms.BooleanField(
        label='I accept the Terms of Service',
        required=True,
        error_messages={'required': 'You must accept the Terms of Service to create an account.'},
        widget=forms.CheckboxInput(attrs={
            'class': 'form-checkbox'
        })
    )
    privacy_policy = forms.BooleanField(
        label='I accept the Privacy Policy',
        required=True,
        error_messages={'required': 'You must accept the Privacy Policy to create an account.'},
        widget=forms.CheckboxInput(attrs={
            'class': 'form-checkbox'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'terms_of_service', 'privacy_policy')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = password_validation.password_validators_help_text_html()

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('The two password fields didn\'t match.', code='password_mismatch')

        password_validation.validate_password(password2, self.instance)

        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('An account with this email already exists.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('A user with that username already exists.')
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        if commit:
            user.save()

        return user

```
<!-- END_FILE -->

---
<!-- FILE: accounts/migrations/__init__.py -->
## accounts/migrations/__init__.py

```py


```
<!-- END_FILE -->

---
<!-- FILE: accounts/models.py -->
## accounts/models.py

```py
from django.db import models

# Create your models here.

```
<!-- END_FILE -->

---
<!-- FILE: accounts/tests.py -->
## accounts/tests.py

```py
from django.test import TestCase

# Create your tests here.

```
<!-- END_FILE -->

---
<!-- FILE: accounts/urls.py -->
## accounts/urls.py

```py
from django.urls import path
from .views import SignUpView, terms_of_service, privacy_policy

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("terms-of-service/", terms_of_service, name="terms_of_service"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
]

```
<!-- END_FILE -->

---
<!-- FILE: accounts/views.py -->
## accounts/views.py

```py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("app:onboarding")
    template_name = "registration/singup.html"


def terms_of_service(request):
    return render(request, "registration/terms_of_service.html")


def privacy_policy(request):
    return render(request, "registration/privacy_policy.html")

```
<!-- END_FILE -->

---
<!-- FILE: app/__init__.py -->
## app/__init__.py

```py


```
<!-- END_FILE -->

---
<!-- FILE: app/admin.py -->
## app/admin.py

```py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'country', 'age', 'is_staff')
    list_filter = ('role', 'country', 'is_staff')
    fieldsets = (
        ('User information', {'fields': ('username', 'password')}),
        ('Personal user information', {'fields': ('first_name', 'last_name', 'email')}),
        ('Extra information', {'fields': ('role', 'birth_date', 'country', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates related info', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'genre', 'rating', 'duration_minutes')
    search_fields = ('title', 'synopsis')
    list_filter = ('year', 'genre', 'age_rating')


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_year', 'end_year', 'total_seasons', 'rating')
    list_filter = ('start_year', 'genre')


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('platform', 'content', 'state')
    list_filter = ('platform', 'state')


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'birth_date')


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('platform', 'week', 'total_favorites', 'total_clicks')
    readonly_fields = ('total_favorites', 'total_clicks')


@admin.register(VisualizationProgress)
class VisualizationProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'last_minute', 'completed')
    list_filter = ('completed',)


admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(AgeRating)
admin.site.register(Language)
admin.site.register(Platform)
admin.site.register(Notification)
admin.site.register(Favorite)
admin.site.register(Watchlist)

```
<!-- END_FILE -->

---
<!-- FILE: app/apps.py -->
## app/apps.py

```py
from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'app'
    default_auto_field = 'django.db.models.BigAutoField'

```
<!-- END_FILE -->

---
<!-- FILE: app/migrations/__init__.py -->
## app/migrations/__init__.py

```py


```
<!-- END_FILE -->

---
<!-- FILE: app/migrations/0001_initial.py -->
## app/migrations/0001_initial.py

```py
# Generated by Django 6.0.2 on 2026-05-06 23:31

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('minimum_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AudiovisualContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('synopsis', models.TextField()),
                ('rating', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('age_rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.agerating')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('iso_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('iso_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('audiovisualcontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.audiovisualcontent')),
                ('year', models.IntegerField()),
                ('release_date', models.DateField()),
                ('duration_minutes', models.IntegerField()),
            ],
            bases=('app.audiovisualcontent',),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('audiovisualcontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.audiovisualcontent')),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField(blank=True, null=True)),
                ('total_seasons', models.IntegerField()),
            ],
            bases=('app.audiovisualcontent',),
        ),
        migrations.AddField(
            model_name='audiovisualcontent',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.country'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('non-binary', 'Non-binary'), ('other', 'Other')], max_length=20, null=True)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profiles/', verbose_name='Foto de Perfil')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Biografía')),
                ('onboarding_completed', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_roles', to='auth.group', verbose_name='Rol de Usuario')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.country', verbose_name='País')),
                ('favorite_genres', models.ManyToManyField(blank=True, related_name='users', to='app.genre')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.country')),
            ],
        ),
        migrations.AddField(
            model_name='audiovisualcontent',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.director'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.audiovisualcontent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='audiovisualcontent',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.genre'),
        ),
        migrations.AddField(
            model_name='audiovisualcontent',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.language'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('seen', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=100)),
                ('url_api', models.URLField()),
                ('p_manager', models.ForeignKey(limit_choices_to={'role': 'manager'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable'), ('coming_soon', 'Coming Soon')], default='available', max_length=20)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.audiovisualcontent')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.platform')),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_favorites', models.IntegerField(default=0)),
                ('total_clicks', models.IntegerField(default=0)),
                ('week', models.DateField()),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.platform')),
            ],
        ),
        migrations.CreateModel(
            name='VisualizationProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_minute', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.audiovisualcontent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.audiovisualcontent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

```
<!-- END_FILE -->

---
<!-- FILE: app/models.py -->
## app/models.py

```py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from datetime import date

class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('non-binary', 'Non-binary'),
        ('other', 'Other'),
    ]

    role = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Rol de Usuario",
        related_name='user_roles'
    )
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Nacimiento")
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="País")
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True, verbose_name="Foto de Perfil")
    bio = models.TextField(null=True, blank=True, verbose_name="Biografía")
    onboarding_completed = models.BooleanField(default=False)
    favorite_genres = models.ManyToManyField('Genre', blank=True, related_name='users')

    def __str__(self):
        return f"{self.username} - {self.role.name if self.role else 'Sin Rol'}"

    def save(self, *args, **kwargs):
        if self.role and self.role.name.lower() == 'technical':
            new_staff_status = True
        else:
            new_staff_status = False

        if self.is_staff != new_staff_status and not self.is_superuser:
            self.is_staff = new_staff_status
            self.save(update_fields=['is_staff'])

        super().save(*args, **kwargs)

    @property
    def age(self):
        if not self.birth_date:
            return None

        today = date.today()

        return today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))


class Country(models.Model):
    name = models.CharField(max_length=100)
    iso_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AgeRating(models.Model):
    description = models.CharField(max_length=100)
    minimum_age = models.IntegerField()

    def __str__(self):
        return f"+{self.minimum_age} - {self.description}"


class Language(models.Model):
    name = models.CharField(max_length=100)
    iso_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class AudiovisualContent(models.Model):
    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    rating = models.FloatField(default=0.0)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    age_rating = models.ForeignKey(AgeRating, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Movie(AudiovisualContent):
    year = models.IntegerField()
    release_date = models.DateField()
    duration_minutes = models.IntegerField()


class Series(AudiovisualContent):
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    total_seasons = models.IntegerField()


class Platform(models.Model):
    platform_name = models.CharField(max_length=100)
    url_api = models.URLField()
    p_manager = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'manager'})

    def __str__(self):
        return self.platform_name


class Catalog(models.Model):
    STATE_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('coming_soon', 'Coming Soon'),
    ]
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    content = models.ForeignKey(AudiovisualContent, on_delete=models.CASCADE)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='available')

    def __str__(self):
        return f"{self.platform.platform_name} - {self.content.title}"


class Statistics(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    total_favorites = models.IntegerField(default=0)
    total_clicks = models.IntegerField(default=0)
    week = models.DateField()

    def __str__(self):
        return f"Stats for {self.platform} - Week: {self.week}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f"To: {self.user.username} - Seen: {self.seen}"


class VisualizationProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(AudiovisualContent, on_delete=models.CASCADE)
    last_minute = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} watching {self.content.title} (Min: {self.last_minute})"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(AudiovisualContent, on_delete=models.CASCADE)


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(AudiovisualContent, on_delete=models.CASCADE)

# SIGNALS
@receiver(post_save, sender=User)
def sync_user_groups(sender, instance, **kwargs):
    if instance.role:
        instance.groups.clear()
        instance.groups.add(instance.role)

@receiver(m2m_changed, sender=User.groups.through)
def sync_profile_role_from_group(sender, instance, action, pk_set, **kwargs):
    if action == "post_add" or action == "post_remove":
        first_group = instance.groups.first()
        User.objects.filter(id=instance.id).update(role=first_group)

```
<!-- END_FILE -->

---
<!-- FILE: app/services.py -->
## app/services.py

```py
import requests
from django.urls import reverse
from decouple import config

# URL DE LAS MOVIES-API EN LOCAL
url_local_1 = "http://127.0.0.1:8080" #API LOCAL 1
url_local_2 = "http://127.0.0.1:8081" #API LOCAL 2
url_local_3 = "http://127.0.0.1:8082" #API LOCAL 3
     
# API KEYS DE LAS MOVIES-API EN LOCAL
api_key_local_1 = config("API_KEY_LOCAL_1")
api_key_local_2 = config("API_KEY_LOCAL_2")
api_key_local_3 = config("API_KEY_LOCAL_3")

#PLATAFORMAS
PLATFORMS = [
    (url_local_1, api_key_local_1, "Platform 1"),
    (url_local_2, api_key_local_2, "Platform 2"),
    (url_local_3, api_key_local_3, "Platform 3"),
]


def get_local_movies(url, api_key): #de una "plataforma" obtengo sus peliculas
    try:
        response = requests.get(
            f"{url}/movies", 
            headers={"X-API-KEY": api_key},
            timeout=5
        )
        response.raise_for_status() 
        print(response.status_code, response.text)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return []

def get_local_series(url, api_key): #de una "plataforma" obtengo sus series
    try:
        response = requests.get(
            f"{url}/series", 
            headers={"X-API-KEY": api_key},
            timeout=5
        )
        response.raise_for_status() 
        print(response.status_code, response.text)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return []

def get_genre(url, api_key):
    try:
        response = requests.get(
            f"{url}/genres", 
            headers={"X-API-KEY": api_key}, 
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return []
    
def get_directors(url, api_key):
    try:
        response = requests.get(
            f"{url}/directors", 
            headers={"X-API-KEY": api_key}, 
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return []

def get_all_platforms():
    """Retorna los nombres de las plataformas configuradas."""
    return [p[2] for p in PLATFORMS]

def get_all_genres_from_api():
    """Obtiene géneros únicos consultando todas las APIs configuradas."""
    all_genres = set()
    for url, key, _ in PLATFORMS:
        genres = get_genre(url, key)
        for g in genres:
            all_genres.add(g["name"])
    return sorted(list(all_genres))

def get_all_movies(platform_filter= None):  # obtener todas las peliculas de todas las "plataformas"

    movies_dict = {} #diccionario para saber el contenido

    for url, key, platform_name in PLATFORMS:
        if platform_filter and platform_name != platform_filter:
            continue
        
        # mapa de generos x plataforma
        genre_map = {}
        director_map = {}

        genres = get_genre(url, key)
        for g in genres:
            genre_map[g["id"]] = g["name"]

        directors = get_directors(url, key)
        for d in directors:
            director_map[d["id"]] = {
                "name": d.get("name", "Unknown Director"),
                "nationality": d.get("country", {}).get("name") if isinstance(d.get("country"), dict) else "Unknown"
            }

        movies = get_local_movies(url, key)
        for movie in movies:
            identifier = f"{movie.get('title')}_{movie.get('year')}".lower().strip() #identificador del contenido
            
            if identifier not in movies_dict:
                # Género y descripción
                movie["genre_name"] = genre_map.get(movie.get('genre_id'), "Unknown")
                dir_info = director_map.get(movie.get("director_id"), {})
                movie["director"] = dir_info.get("name", "Unknown Director")
                movie["director_nationality"] = dir_info.get("nationality", "Unknown")

                # Otros datos
                movie["age_rating"] = movie.get("age_rating", {}).get("title", "NR")
                movie["duration_minutes"] = movie.get("duration_minutes", "—")
                movie['unique_id'] = identifier

                movie["platforms"] = [platform_name]
                movie.pop("platform_name", None)
                movies_dict[identifier] = movie
                
            else:
                if platform_name not in movies_dict[identifier]["platforms"]:
                    movies_dict[identifier]["platforms"].append(platform_name)
    return list(movies_dict.values())


def get_all_series(platform_filter = None):  # obtener todas las peliculas de todas las "plataformas"
    series_dict = {}

    for url, key, platform_name in PLATFORMS:
        if platform_filter and platform_name != platform_filter:
            continue
        genre_map = {}
        genres = get_genre(url, key)
        for g in genres:
            genre_map[g["id"]] = g["name"]

        series = get_local_series(url, key)

        for serie in series:
            identifier = f"{serie.get('title')}_{serie.get('start_year', '')}".lower().strip()

            if identifier not in series_dict:
                serie["genre_name"] = serie.get("genre", {}).get("name") or genre_map.get(serie.get("genre_id"), "Unknown")
                serie["synopsis"] = serie.get("synopsis", "No synopsis available.")

                director_data = serie.get("director", {})
                serie["director"] = director_data.get("name", "Unknown Director")

                serie["director_nationality"] = director_data.get("country", {}).get("name", "Unknown")
                serie["genre_description"] = serie.get("genre", {}).get("description", "")
                serie["age_rating"] = serie.get("age_rating", {}).get("title", "NR")
                serie['unique_id'] = identifier

                serie["platforms"] = [platform_name]
                serie.pop("platform_name", None)
                series_dict[identifier] = serie
            else:
                if platform_name not in series_dict[identifier]["platforms"]:
                    series_dict[identifier]["platforms"].append(platform_name)
    
    return list(series_dict.values())


def get_movies_by_genres(genre_names, min_total=5):
    all_movies = get_all_movies()
    
    result = {}
    used_movies = []
    
    # Primero: intentar 3+ de cada género
    for genre_name in genre_names:
        genre_movies = [
            m for m in all_movies 
            if m.get('genre_name', '').lower() == genre_name.lower()
        ]
        genre_movies.sort(key=lambda x: x.get('rating', 0), reverse=True)
        
        # Tomar hasta 3 películas de este género
        selected = []
        for m in genre_movies:
            if m not in used_movies:
                selected.append(m)
                used_movies.append(m)
                if len(selected) >= 3:
                    break
        
        result[genre_name] = selected
    
    # Contar total actual
    current_total = sum(len(movies) for movies in result.values())
    
    # Si no llega a min_total, completar con otros géneros
    if current_total < min_total:
        remaining = min_total - current_total
        # Recolectar movies adicionales de otros géneros
        extra_movies = []
        for m in all_movies:
            if m not in used_movies and len(extra_movies) < remaining:
                extra_movies.append(m)
        
        # Distribuir los extras entre los géneros
        genre_list = list(result.keys())
        idx = 0
        for m in extra_movies:
            while len(result[genre_list[idx]]) >= 5 and idx < len(genre_list) - 1:
                idx += 1
            if idx < len(genre_list):
                m_copy = m.copy()
                m_copy['unique_id'] = f"{m.get('title', '').lower().replace(' ', '-')}_{m.get('year', '')}"
                result[genre_list[idx]].append(m_copy)
    
    # Asignar unique_id a cada movie que no lo tenga
    for genre_name, movies in result.items():
        for m in movies:
            if 'unique_id' not in m:
                m['unique_id'] = f"{m.get('title', '').lower().replace(' ', '-')}_{m.get('year', '')}"
    
    return result


def get_series_by_genres(genre_names, min_total=5):
    all_series = get_all_series()
    
    result = {}
    used_series = []
    
    # Primero: intentar 3+ de cada género
    for genre_name in genre_names:
        genre_series = [
            s for s in all_series 
            if s.get('genre_name', '').lower() == genre_name.lower()
        ]
        genre_series.sort(key=lambda x: x.get('rating', 0), reverse=True)
        
        # Tomar hasta 3 series de este género
        selected = []
        for s in genre_series:
            if s not in used_series:
                selected.append(s)
                used_series.append(s)
                if len(selected) >= 3:
                    break
        
        result[genre_name] = selected
    
    # Contar total actual
    current_total = sum(len(series_list) for series_list in result.values())
    
    # Si no llega a min_total, completar con otros géneros
    if current_total < min_total:
        remaining = min_total - current_total
        # Recolectar series adicionales de otros géneros
        extra_series = []
        for s in all_series:
            if s not in used_series and len(extra_series) < remaining:
                extra_series.append(s)
        
        # Distribuir los extras entre los géneros
        genre_list = list(result.keys())
        idx = 0
        for s in extra_series:
            while len(result[genre_list[idx]]) >= 5 and idx < len(genre_list) - 1:
                idx += 1
            if idx < len(genre_list):
                s_copy = s.copy()
                s_copy['unique_id'] = f"{s.get('title', '').lower().replace(' ', '-')}_{s.get('start_year', '')}"
                result[genre_list[idx]].append(s_copy)
    
    # Asignar unique_id a cada serie que no lo tenga
    for genre_name, series_list in result.items():
        for s in series_list:
            if 'unique_id' not in s:
                s['unique_id'] = f"{s.get('title', '').lower().replace(' ', '-')}_{s.get('start_year', '')}"
    
    return result


def get_trending(limit=10):
    """
    Obtiene las películas y series mejor valoradas (Top Rated).
    Combina movies y series, ordena por rating descendente.
    """
    all_movies = get_all_movies()
    all_series = get_all_series()
    
    all_content = []
    
    for m in all_movies:
        m['content_type'] = 'movie'
        m['unique_id'] = f"{m.get('title', '').lower().replace(' ', '-')}_{m.get('year', '')}"
        all_content.append(m)
    
    for s in all_series:
        s['content_type'] = 'series'
        s['unique_id'] = f"{s.get('title', '').lower().replace(' ', '-')}_{s.get('start_year', '')}"
        all_content.append(s)
    
    all_content.sort(key=lambda x: x.get('rating', 0), reverse=True)
    
    return all_content[:limit]


def search_content(query, platform=None, genre=None, sort_rating=None, sort_year=None):
    results_dict = {}

    for url, key, platform_name in PLATFORMS:
        if platform and platform_name != platform:
            continue

        genre_map = {g["id"]: g["name"] for g in get_genre(url, key)}

        # --- Búsqueda en Películas ---
        try:
            res = requests.get(f"{url}/movies", headers={"X-API-KEY": key}, params={"title": query}, timeout=5)
            if res.status_code == 200:
                for movie in res.json():
                    movie_genre = genre_map.get(movie.get("genre_id"), "Unknown")
                    if genre and genre.lower() not in movie_genre.lower():
                        continue
                    
                    clean_title = movie.get('title', '').lower().strip()
                    year = movie.get('year', '')
                    identifier = f"{clean_title}_{year}" 
                    
                    if identifier not in results_dict:
                        movie["content_type"] = "movie"
                        movie["genre_name"] = movie_genre
                        movie["platforms"] = [platform_name]
                        movie["unique_id"] = identifier  
                        results_dict[identifier] = movie
                    else:
                        if platform_name not in results_dict[identifier]["platforms"]:
                            results_dict[identifier]["platforms"].append(platform_name)
        except:
            pass

        # --- Búsqueda en Series ---
        try:
            res = requests.get(f"{url}/series", headers={"X-API-KEY": key}, params={"title": query}, timeout=5)
            if res.status_code == 200:
                for serie in res.json():
                    serie_genre = genre_map.get(serie.get("genre_id"), "Unknown")
                    if genre and genre.lower() not in serie_genre.lower():
                        continue
                    
                    # CAMBIO AQUÍ: Eliminamos el prefijo 'series_'
                    clean_title = serie.get('title', '').lower().strip()
                    year = serie.get('start_year', '')
                    identifier = f"{clean_title}_{year}"
                    
                    if identifier not in results_dict:
                        serie["content_type"] = "series"
                        serie["genre_name"] = serie_genre
                        serie["platforms"] = [platform_name]
                        serie["unique_id"] = identifier
                        results_dict[identifier] = serie
                    else:
                        if platform_name not in results_dict[identifier]["platforms"]:
                            results_dict[identifier]["platforms"].append(platform_name)
        except:
            pass

    # ... (resto de la lógica de ordenación y retorno)
    return list(results_dict.values())

```
<!-- END_FILE -->

---
<!-- FILE: app/static/css/auth-signup.css -->
## app/static/css/auth-signup.css

```css
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px) scale(0.98);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.animate-fade-in-up {
    animation: fadeInUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

input, .form-input {
    width: 100%;
    border-radius: 0.75rem;
    border: 1px solid #e2e8f0;
    background-color: #f8fafc;
    padding: 0.625rem 1rem;
    font-size: 0.875rem;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.dark input, .dark .form-input {
    background-color: #1e293b;
    border-color: #334155;
    color: white;
}

input:focus, .form-input:focus {
    outline: none;
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
}

input.error, .form-input.error {
    border-color: #ef4444;
}

input.error:focus, .form-input.error:focus {
    box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.15);
}

input.valid-field, .form-input.valid-field {
    border-color: #22c55e;
}

input.valid-field:focus {
    box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.15);
}

.form-checkbox {
    width: 18px;
    height: 18px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
    cursor: pointer;
    accent-color: #3b82f6;
    transition: all 0.2s;
}

.dark .form-checkbox {
    background-color: #1e293b;
    border-color: #334155;
}

.form-checkbox:checked {
    background-color: #256af4;
    border-color: #256af4;
    box-shadow: 0 0 8px rgba(37, 106, 244, 0.4);
}

.error-message {
    color: #ef4444;
    animation: shake 0.4s ease;
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-4px); }
    75% { transform: translateX(4px); }
}

.valid-input {
    border-color: #22c55e;
}

.valid-input:focus {
    border-color: #22c55e;
    ring-color: #22c55e;
}

#submit-btn:not(:disabled) {
    background: linear-gradient(135deg, #256af4 0%, #1d4ed8 100%);
}

#submit-btn:not(:disabled):hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(37, 106, 244, 0.35);
}

#submit-btn:not(:disabled):active {
    transform: translateY(0);
}

```
<!-- END_FILE -->

---
<!-- FILE: app/static/css/main.css -->
## app/static/css/main.css

```css
:root {
    --primary: #256af4;
    --background: #101622;
    --surface-container: #1d2a44;
    --surface-container-low: #182234;
    --on-background: #f8fafc;
    --on-surface-variant: #94a3b8;
    --on-surface: #f1f5f9;
}

/* Hide scrollbar for horizontal scroll areas */
.no-scrollbar::-webkit-scrollbar {
    display: none;
}
.no-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
}

.cinematic-shadow {
    box-shadow: 
        0 10px 30px rgba(0,0,0,0.6), 
        0 0 25px rgba(37,106,244,0.25);
}
.hover-electric:hover { box-shadow: 0 0 25px rgba(37, 106, 244, 0.6); }

.card-enter {
    animation: cardIn 0.4s ease both;
}

@keyframes cardIn {
    from { opacity: 0; transform: translateY(16px) scale(0.97); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
}

.unavailable-card {
    opacity: 0.55;
    filter: grayscale(1);
    transition: filter 0.3s, opacity 0.3s;
}

.unavailable-card:hover {
    opacity: 1;
    filter: grayscale(0);
}

    /* Platform badge colors */
.badge-p1 { background-color: #E50914; }
.badge-p2 { background-color: #0073E6; }
.badge-p3 { background-color: #5822b4; }

.cinematic-shadow { box-shadow: 0 0 20px rgba(37, 106, 244, 0.2); }
.hover-electric:hover { box-shadow: 0 0 25px rgba(37, 106, 244, 0.6); }
.material-symbols-outlined {
    font-variation-settings: 'FILL' 0, 'wght' 400;
}
.glass-panel {
    background: rgba(30, 41, 59, 0.4);
    backdrop-filter: blur(12px);
}


    .bg-background { background-color: var(--background); }
    .text-primary { color: var(--primary); }
    .bg-primary { background-color: var(--primary); }
    .text-on-background { color: var(--on-background); }
    .text-on-surface-variant { color: var(--on-surface-variant); }
    .bg-surface-container { background-color: var(--surface-container); }

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(15px) scale(0.95);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.genre-animate {
    opacity: 0;
    animation: fadeInUp 0.4s ease forwards;
}

.genre-card:active {
    transform: scale(0.98);
}

.genre-card input:checked + div {
    animation: pulseSelect 0.3s ease;
}

@keyframes pulseSelect {
    0% { transform: scale(1); }
    50% { transform: scale(1.02); }
    100% { transform: scale(1); }
}

#count {
    transition: transform 0.15s ease, color 0.3s ease;
}

#selection-counter {
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

#continue-btn {
    position: relative;
    overflow: hidden;
}

#continue-btn::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, transparent 100%);
    opacity: 0;
    transition: opacity 0.3s;
}

#continue-btn:hover::before {
    opacity: 1;
}

@keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .field-animate {
        opacity: 0;
        animation: slideInUp 0.5s ease forwards;
    }

    .btn-continue {
        position: relative;
        overflow: hidden;
    }

    .btn-continue::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, transparent 100%);
        opacity: 0;
        transition: opacity 0.3s;
    }

    .btn-continue:hover::before {
        opacity: 1;
    }

    .btn-continue:active {
        transform: scale(0.98);
    }

.genre-card.is-selected .card-inner {
    border-color: #256af4;
    box-shadow: 0 0 25px rgba(37, 106, 244, 0.5);
}

.genre-card.is-selected .card-img {
    filter: grayscale(0);
    transform: scale(1.1);
}

.genre-card.is-selected .card-check {
    opacity: 1;
    transform: scale(1);
}

.no-scrollbar::-webkit-scrollbar {
    display: none;
}
.no-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
}

.horizontal-scroll {
    overflow-x: auto;
    overflow-y: visible;
    white-space: nowrap;
    -webkit-overflow-scrolling: touch;
}

```
<!-- END_FILE -->

---
<!-- FILE: app/static/js/auth-signup.js -->
## app/static/js/auth-signup.js

```js
document.addEventListener('DOMContentLoaded', function() {
    const password1 = document.getElementById('id_password1');
    const password2 = document.getElementById('id_password2');
    const submitBtn = document.getElementById('submit-btn');

    const lengthCheck = document.getElementById('length-check');
    const commonCheck = document.getElementById('common-check');
    const numberCheck = document.getElementById('number-check');
    const password2Match = document.getElementById('password2-match');
    const matchIcon = document.getElementById('match-icon');
    const matchText = document.getElementById('match-text');

    const commonPasswords = [
        'password', '12345678', '123456789', 'qwerty', 'abc123', 'password1',
        '1234567', 'password123', 'welcome', 'hello', 'admin', 'letmein',
        'sunshine', 'princess', 'football', 'monkey', 'dragon'
    ];

    function validatePassword1() {
        const pwd = password1.value;
        let valid = true;

        if (pwd.length >= 8) {
            lengthCheck.textContent = '✓';
            lengthCheck.className = 'text-green-500';
        } else {
            lengthCheck.textContent = '○';
            lengthCheck.className = 'text-slate-400';
            valid = false;
        }

        if (!commonPasswords.includes(pwd.toLowerCase())) {
            commonCheck.textContent = '✓';
            commonCheck.className = 'text-green-500';
        } else {
            commonCheck.textContent = '○';
            commonCheck.className = 'text-slate-400';
            valid = false;
        }

        if (!/^\d+$/.test(pwd)) {
            numberCheck.textContent = '✓';
            numberCheck.className = 'text-green-500';
        } else {
            numberCheck.textContent = '○';
            numberCheck.className = 'text-slate-400';
            valid = false;
        }

        return valid;
    }

    function validatePassword2() {
        const pwd1 = password1.value;
        const pwd2 = password2.value;

        password2Match.classList.remove('hidden');

        if (pwd2.length === 0) {
            password2Match.classList.add('hidden');
            return false;
        }

        if (pwd1 === pwd2) {
            matchIcon.textContent = '✓';
            matchText.textContent = 'Passwords match';
            matchIcon.className = 'text-green-500';
            matchText.className = 'text-green-500';
            return true;
        } else {
            matchIcon.textContent = '✗';
            matchText.textContent = 'Passwords do not match';
            matchIcon.className = 'text-red-500';
            matchText.className = 'text-red-500';
            return false;
        }
    }

    function updateSubmitButton() {
        const pwd1Valid = validatePassword1();
        const pwd2Valid = validatePassword2();
        const termsChecked = document.getElementById('id_terms_of_service').checked;
        const privacyChecked = document.getElementById('id_privacy_policy').checked;

        if (pwd1Valid && pwd2Valid && termsChecked && privacyChecked) {
            submitBtn.disabled = false;
        } else {
            submitBtn.disabled = true;
        }
    }

    password1.addEventListener('input', function() {
        validatePassword1();
        validatePassword2();
        updateSubmitButton();
    });

    password2.addEventListener('input', function() {
        validatePassword2();
        updateSubmitButton();
    });

    document.getElementById('id_terms_of_service').addEventListener('change', updateSubmitButton);
    document.getElementById('id_privacy_policy').addEventListener('change', updateSubmitButton);
});

```
<!-- END_FILE -->

---
<!-- FILE: app/static/js/content.js -->
## app/static/js/content.js

```js

document.addEventListener('DOMContentLoaded', function() {
  const contentId = window.CONTENT_DATA.id;
  const contentType = window.CONTENT_DATA.type;
  const userStatus = window.CONTENT_DATA.userStatus;
  
  // Inicializar estado del dropdown
  const statusLabels = {
    'not_seen': 'Not Seen',
    'watching': 'Watching',
    'completed': 'Completed'
  };
  const statusIcons = {
    'not_seen': 'visibility_off',
    'watching': 'play_circle',
    'completed': 'check_circle'
  };
  
  // Actualizar texto del status según el estado del usuario
  const statusText = document.getElementById('status-text');
  const statusIcon = document.getElementById('status-icon');
  if (statusText && userStatus) {
    statusText.textContent = statusLabels[userStatus] || 'Not Seen';
    statusIcon.textContent = statusIcons[userStatus] || 'visibility_off';
  }
  
  // Toggle dropdown de Status
  const statusBtn = document.getElementById('status-btn');
  const statusDropdown = document.getElementById('status-dropdown');
  
  if (statusBtn && statusDropdown) {
    statusBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      statusDropdown.classList.toggle('hidden');
    });
    
    // Cerrar dropdown al hacer click fuera
    document.addEventListener('click', function(e) {
      if (!statusBtn.contains(e.target) && !statusDropdown.contains(e.target)) {
        statusDropdown.classList.add('hidden');
      }
    });
    
    // Manejar cambio de estado
    const statusOptions = statusDropdown.querySelectorAll('button[data-status]');
    statusOptions.forEach(btn => {
      btn.addEventListener('click', function(e) {
        const status = this.dataset.status;
        updateStatus(status);
        statusDropdown.classList.add('hidden');
      });
    });
  }
  
  // Toggle Favorites
  const favoriteBtn = document.getElementById('favorite-btn');
  if (favoriteBtn) {
    favoriteBtn.addEventListener('click', function() {
      toggleFavorite();
    });
  }
  
  // Función para actualizar estado
  function updateStatus(status) {
    fetch(`/content/${contentType}/${contentId}/update-status/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify({ status: status })
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        const statusText = document.getElementById('status-text');
        const statusIcon = document.getElementById('status-icon');
        
        statusText.textContent = statusLabels[status] || 'Not Seen';
        statusIcon.textContent = statusIcons[status] || 'visibility_off';
      }
    })
    .catch(error => console.error('Error:', error));
  }
  
  // Función para toggle favorite
  function toggleFavorite() {
    fetch(`/content/${contentType}/${contentId}/toggle-favorite/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      }
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        const favoriteIcon = document.getElementById('favorite-icon');
        const favoriteText = document.getElementById('favorite-text');
        
        if (data.is_favorite) {
          favoriteIcon.textContent = 'favorite';
          favoriteText.textContent = 'Remove from Favorites';
        } else {
          favoriteIcon.textContent = 'favorite_border';
          favoriteText.textContent = 'Add to Favorites';
        }
      }
    })
    .catch(error => console.error('Error:', error));
  }
  
  // Función para obtener CSRF token
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});

```
<!-- END_FILE -->

---
<!-- FILE: app/static/js/genres.js -->
## app/static/js/genres.js

```js
document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('.genre-checkbox');
    const countDisplay = document.getElementById('count');
    const continueBtn = document.getElementById('continue-btn');
    const counterWrapper = document.getElementById('selection-counter');

    function updateCounter() {
        const selected = document.querySelectorAll('.genre-checkbox:checked').length;
        const prevCount = parseInt(countDisplay.textContent) || 0;
        countDisplay.textContent = selected;

        if (selected >= 3) {
            continueBtn.disabled = false;
            countDisplay.classList.remove('text-white');
            countDisplay.classList.add('text-green-400');
            counterWrapper.classList.add('border-green-500/50', 'shadow-[0_0_15px_rgba(34,197,94,0.2)]');
        } else {
            continueBtn.disabled = true;
            countDisplay.classList.add('text-white');
            countDisplay.classList.remove('text-green-400');
            counterWrapper.classList.remove('border-green-500/50', 'shadow-[0_0_15px_rgba(34,197,94,0.2)]');
        }

        if (selected !== prevCount) {
            countDisplay.style.transform = 'scale(1.3)';
            setTimeout(() => { countDisplay.style.transform = 'scale(1)'; }, 150);
        }
    }

    checkboxes.forEach(cb => {
        cb.addEventListener('change', function () {
            const label = this.closest('.genre-card');
            label.classList.toggle('is-selected', this.checked);
            updateCounter();
        });
    });

    
    checkboxes.forEach(cb => {
        if (cb.checked) {
            cb.closest('.genre-card').classList.add('is-selected');
        }
    });

    updateCounter();
});

```
<!-- END_FILE -->

---
<!-- FILE: app/static/js/navbar.js -->
## app/static/js/navbar.js

```js
document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // User dropdown toggle
    const userMenuBtn = document.getElementById('user-menu-button');
    const userDropdown = document.getElementById('user-dropdown');

    if (userMenuBtn && userDropdown) {
        userMenuBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            userDropdown.classList.toggle('hidden');
        });

        // Cerrar al hacer click fuera
        document.addEventListener('click', () => {
            userDropdown.classList.add('hidden');
        });
    }
});

```
<!-- END_FILE -->

---
<!-- FILE: app/static/js/tailwind.config.js -->
## app/static/js/tailwind.config.js

```js
tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
            colors: {
                "primary": "#256af4",
                "background": "#101622",
                "background-light": "#f5f6f8",
                "background-dark": "#101622",
                "surface-dark": "#182234",
                "surface-light": "#ffffff",
                "border-dark": "#222f49",
                "border-light": "#e2e8f0",
                "surface-container-low": "#182234",
                "outline-variant": "#222f49",
                "on-surface-variant": "#94a3b8",
            },
            fontFamily: {
                "display": ["Spline Sans", "sans-serif"]
            },
            borderRadius: {
                "lg": "0.5rem", 
                "xl": "0.75rem", 
            },
        },
    },
}

```
<!-- END_FILE -->

---
<!-- FILE: app/tech_admin.py -->
## app/tech_admin.py

```py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.admin import AdminSite
from . import views
from django.urls import path

class TechUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'get_role', 'is_staff')
    list_filter = ('role', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)
    list_per_page = 10

    def get_role(self, obj):
        return obj.role
    get_role.short_description = 'Rol'

class TechAdminSite(AdminSite):
    site_header = "StreamSync Tech"
    index_template = 'admin/tech.html'
    change_form_template = 'admin/tech_change_form.html'
    add_form_template = 'admin/tech_add_form.html'

    def has_permission(self, request):
        if not request.user.is_authenticated or not request.user.is_active:
            return False
        
        if request.user.is_superuser:
            return True

        try:
            custom_user = User.objects.select_related('role').get(pk=request.user.pk)
            if custom_user.role:
                return custom_user.role.name.lower() == 'technical'
        except User.DoesNotExist:
            return False
        
        return False
                
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('auth/user/add/', self.admin_view(views.tech_add_user_view), name='auth_user_add'),
            path('auth/user/<int:user_id>/change/', self.admin_view(views.tech_edit_user_view), name='auth_user_change'),
            path('auth/user/<int:user_id>/delete/', self.admin_view(views.tech_delete_user), name='auth_user_delete'),
        ]
        return custom_urls + urls
    
    def index(self, request, extra_context=None):
        from django.contrib.auth.models import Group
        
        users = User.objects.all().select_related('role')

        query = request.GET.get('q')
        if query:
            users = users.filter(username__icontains=query) | users.filter(email__icontains=query)

        role_filter = request.GET.get('role')
        if role_filter:
            users = users.filter(role_id=role_filter)

        status_filter = request.GET.get('status')

        if status_filter == 'active':
            users = users.filter(is_active=True)
        elif status_filter == 'inactive':
            users = users.filter(is_active=False)

        extra_context = extra_context or {}
        extra_context['tech_users'] = users.order_by('-date_joined')[:10]
        extra_context['groups'] = Group.objects.all()
        
        extra_context['current_role'] = role_filter
        extra_context['current_status'] = status_filter
        
        return super().index(request, extra_context)

tech_admin_site = TechAdminSite(name='tech_admin')
tech_admin_site.register(User, TechUserAdmin)

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/admin/tech_add_user.html -->
## app/templates/admin/tech_add_user.html

```html
{% extends "base/base.html" %}

{% block content %}
<div class="min-h-screen bg-background-dark p-4 md:p-8 text-white">
    <div class="max-w-4xl mx-auto">
        <a href="{% url 'tech_admin:index' %}" class="flex items-center gap-2 text-slate-500 hover:text-primary transition-colors mb-6 text-sm font-bold">
            <span class="material-symbols-outlined">arrow_back</span> BACK TO DASHBOARD
        </a>

        <div class="bg-surface-dark border border-white/10 rounded-3xl shadow-2xl overflow-hidden">
            <div class="bg-primary/10 p-8 border-b border-white/5">
                <h2 class="text-3xl font-black tracking-tight text-white">CREATE <span class="text-primary">NEW ACCOUNT</span></h2>
                <p class="text-slate-400 text-sm mt-1">Configure user credentials and profile settings simultaneously.</p>
            </div>

            <form method="POST" enctype="multipart/form-data" class="p-8 space-y-8">
                {% csrf_token %}
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="md:col-span-2"><h3 class="text-primary font-bold text-xs uppercase tracking-[0.2em]">Personal Information</h3></div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">First Name</label>
                        <input type="text" name="first_name" class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none transition-all">
                    </div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Last Name</label>
                        <input type="text" name="last_name" class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none transition-all">
                    </div>
                    <div class="md:col-span-2">
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Email Address</label>
                        <input type="email" name="email" required class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none transition-all">
                    </div>
                </div>

                <hr class="border-white/5">

                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="md:col-span-3"><h3 class="text-primary font-bold text-xs uppercase tracking-[0.2em]">System Credentials</h3></div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Username</label>
                        <input type="text" name="username" required class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none transition-all">
                    </div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Password</label>
                        <input type="password" name="password" required class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none transition-all">
                    </div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Repeat Password</label>
                        <input type="password" name="password_again" required class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none transition-all">
                    </div>
                </div>

                <hr class="border-white/5">

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="md:col-span-2"><h3 class="text-primary font-bold text-xs uppercase tracking-[0.2em]">Profile Configuration</h3></div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Assigned Role</label>
                        <select name="role" class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none appearance-none">
                            {% for g in groups %}
                            <option value="{{ g.id }}">{{ g.name|upper }}</option>
                            {% endfor %}
                        </select>
                    </div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Profile Picture</label>
                        <input type="file" name="profile_image" accept="image/*" 
                               class="w-full text-xs text-slate-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-bold file:bg-primary file:text-white hover:file:bg-primary/80 transition-all">
                    </div>
                </div>

                <div class="pt-6 flex flex-col md:flex-row gap-4">
                    <button type="submit" class="flex-1 bg-primary text-white py-4 rounded-2xl font-black uppercase tracking-widest hover:brightness-110 transition-all shadow-lg shadow-primary/20">
                        CREATE SYSTEM USER
                    </button>
                    <a href="{% url 'tech_admin:index' %}" class="flex-1 bg-white/5 text-center py-4 rounded-2xl font-black uppercase tracking-widest hover:bg-white/10 transition-all">
                        CANCEL
                    </a>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/admin/tech_edit_user.html -->
## app/templates/admin/tech_edit_user.html

```html
{% extends "base/base.html" %}

{% block content %}
<div class="min-h-screen bg-background-dark p-4 md:p-8 text-white">
    <div class="max-w-4xl mx-auto">
        <a href="{% url 'tech_admin:index' %}" class="flex items-center gap-2 text-slate-500 hover:text-primary transition-colors mb-6 text-sm font-bold">
            <span class="material-symbols-outlined">arrow_back</span> VOLVER AL DASHBOARD
        </a>

        <div class="bg-surface-dark border border-white/10 rounded-3xl shadow-2xl overflow-hidden">
            <div class="bg-primary/10 p-8 border-b border-white/5 flex justify-between items-center">
                <div>
                    <h2 class="text-3xl font-black tracking-tight text-white">EDITAR <span class="text-primary">USUARIO</span></h2>
                    <p class="text-slate-400 text-sm mt-1">Modificando la cuenta de <b>{{ user_to_edit.username }}</b></p>
                </div>
                <div class="size-16 rounded-2xl border-2 border-primary/30 overflow-hidden bg-slate-800">
                    <img src="{{ user_to_edit.image.url }}" class="w-full h-full object-cover">
                </div>
            </div>

            <form method="POST" enctype="multipart/form-data" class="p-8 space-y-8">
                {% csrf_token %}
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="md:col-span-2"><h3 class="text-primary font-bold text-xs uppercase tracking-[0.2em]">Información Personal</h3></div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Nombre</label>
                        <input type="text" name="first_name" value="{{ user_to_edit.first_name }}" class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none transition-all">
                    </div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Apellidos</label>
                        <input type="text" name="last_name" value="{{ user_to_edit.last_name }}" class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none transition-all">
                    </div>
                    <div class="md:col-span-2">
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Email</label>
                        <input type="email" name="email" value="{{ user_to_edit.email }}" required class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none transition-all">
                    </div>
                </div>

                <hr class="border-white/5">

                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="md:col-span-3">
                        <h3 class="text-primary font-bold text-xs uppercase tracking-[0.2em]">Credenciales del Sistema</h3>
                        <p class="text-[10px] text-slate-500 mt-1 italic italic">Deja la contraseña en blanco si no deseas cambiarla.</p>
                    </div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Username</label>
                        <input type="text" name="username" value="{{ user_to_edit.username }}" required class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none transition-all">
                    </div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Nueva Contraseña</label>
                        <input type="password" name="password" placeholder="••••••••" class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none transition-all">
                    </div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Repetir Contraseña</label>
                        <input type="password" name="password_again" placeholder="••••••••" class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none transition-all">
                    </div>
                </div>

                <hr class="border-white/5">

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="md:col-span-2"><h3 class="text-primary font-bold text-xs uppercase tracking-[0.2em]">Configuración de Perfil</h3></div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Rol Asignado</label>
                        <select name="role" class="w-full bg-white/5 border border-white/10 rounded-xl p-3 focus:border-primary outline-none appearance-none">
                            {% for g in groups %}
                            <option value="{{ g.id }}" {% if user_to_edit.role.id == g.id %}selected{% endif %}>
                                {{ g.name|upper }}
                            </option>
                            {% endfor %}
                        </select>
                    </div>
                    <div>
                        <label class="block text-[10px] font-black text-slate-500 mb-2 uppercase">Cambiar Imagen</label>
                        <input type="file" name="profile_image" accept="image/*" 
                               class="w-full text-xs text-slate-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-bold file:bg-primary file:text-white hover:file:bg-primary/80 transition-all">
                    </div>
                </div>

                <div class="pt-6 flex flex-col md:flex-row gap-4">
                    <button type="submit" class="flex-1 bg-primary text-white py-4 rounded-2xl font-black uppercase tracking-widest hover:brightness-110 transition-all shadow-lg shadow-primary/20">
                        GUARDAR CAMBIOS
                    </button>
                    <a href="{% url 'tech_admin:index' %}" class="flex-1 bg-white/5 text-center py-4 rounded-2xl font-black uppercase tracking-widest hover:bg-white/10 transition-all">
                        CANCELAR
                    </a>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/admin/tech.html -->
## app/templates/admin/tech.html

```html
{% extends "base/base.html" %}

{% block content %}
<div class="min-h-screen p-4 md:p-6 animate-in fade-in duration-700">
    
    <div class="flex flex-col lg:flex-row justify-between items-start lg:items-end mb-12 gap-6">
        <div class="space-y-1">
            <div class="flex items-center gap-2 mb-1">
                <span class="size-2 bg-primary rounded-full animate-pulse"></span>
                <span class="text-[10px] font-black tracking-[0.3em] text-primary uppercase">System Administration</span>
            </div>
            <h1 class="text-4xl md:text-5xl font-black tracking-tighter text-white">
                TECH <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-blue-400">DASHBOARD</span>
            </h1>
            <p class="text-slate-400 text-sm font-medium">Monitoring system integrity & access control.</p>
        </div>
        
        <form action="." method="GET" class="relative w-full lg:w-[450px] group">
            <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-slate-500 group-focus-within:text-primary transition-colors">search</span>
            <input type="text" name="q" value="{{ request.GET.q }}" placeholder="Search users by name or email..." 
                   class="w-full bg-surface-dark/50 border border-white/10 rounded-2xl py-4 pl-12 pr-4 focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary transition-all text-sm backdrop-blur-md shadow-xl">
        </form>
    </div>

    <div class="flex flex-wrap items-center gap-4 mb-8 bg-white/[0.02] p-4 rounded-2xl border border-white/5">
        <div class="flex items-center gap-2 border-r border-white/10 pr-4">
            <span class="material-symbols-outlined text-slate-500 text-sm">filter_list</span>
            <span class="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Filters</span>
        </div>
        
        <form id="filterForm" method="GET" class="flex flex-wrap gap-3 flex-1 items-center">
            {% if request.GET.q %}
                <input type="hidden" name="q" value="{{ request.GET.q }}">
            {% endif %}

            <div class="relative">
                <select name="role" onchange="this.form.submit()" 
                        class="appearance-none bg-surface-dark border border-white/10 rounded-xl px-4 py-2 pr-10 text-xs text-slate-300 focus:border-primary outline-none cursor-pointer hover:bg-white/5 transition-all">
                    <option value="">All Roles</option>
                    {% for g in groups %}
                        <option value="{{ g.id }}" {% if current_role == g.id|stringformat:"s" %}selected{% endif %}>
                            {{ g.name|upper }}
                        </option>
                    {% endfor %}
                </select>
                <span class="material-symbols-outlined absolute right-2 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none text-sm">expand_more</span>
            </div>

            <div class="relative">
                <select name="status" onchange="this.form.submit()" 
                        class="appearance-none bg-surface-dark border border-white/10 rounded-xl px-4 py-2 pr-10 text-xs text-slate-300 focus:border-primary outline-none cursor-pointer hover:bg-white/5 transition-all">
                    <option value="">All Status</option>
                    <option value="active" {% if current_status == 'active' %}selected{% endif %}>ACTIVE</option>
                    <option value="inactive" {% if current_status == 'inactive' %}selected{% endif %}>INACTIVE</option>
                </select>
                <span class="material-symbols-outlined absolute right-2 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none text-sm">expand_more</span>
            </div>

            {% if current_role or current_status or request.GET.q %}
                <a href="." class="px-4 py-2 rounded-xl bg-red-500/10 text-red-500 text-[10px] font-bold hover:bg-red-500 hover:text-white transition-all flex items-center gap-2">
                    <span class="material-symbols-outlined text-sm">filter_alt_off</span> RESET
                </a>
            {% endif %}
        </form>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-4 gap-8">
        
        <div class="lg:col-span-3 space-y-6">
            <div class="bg-surface-dark rounded-3xl border border-white/10 overflow-hidden shadow-2xl backdrop-blur-sm">
                <div class="p-6 border-b border-white/5 flex justify-between items-center bg-white/[0.01]">
                    <div class="flex items-center gap-3">
                        <div class="size-10 rounded-xl bg-primary/20 flex items-center justify-center">
                            <span class="material-symbols-outlined text-primary">groups</span>
                        </div>
                        <h3 class="font-bold text-lg tracking-tight">Database Entities</h3>
                    </div>
                    <a href="{% url 'tech_admin:auth_user_add' %}" class="bg-primary hover:bg-primary/80 text-black px-5 py-2.5 rounded-xl font-black text-xs transition-all shadow-lg shadow-primary/20 flex items-center gap-2">
                        <span class="material-symbols-outlined text-sm">person_add</span> ADD USER
                    </a>
                </div>
                
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-sm border-separate border-spacing-0">
                        <thead class="bg-white/[0.03] text-slate-500 uppercase text-[10px] font-black tracking-widest">
                            <tr>
                                <th class="px-6 py-5">User Identity</th>
                                <th class="px-6 py-5">Privileges</th>
                                <th class="px-6 py-5">Status</th>
                                <th class="px-6 py-5 text-right">Operational Actions</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-white/5">
                            {% for u in tech_users %}
                            <tr class="hover:bg-primary/[0.03] transition-colors group">
                                <td class="px-6 py-5 flex items-center gap-4">
                                    <div class="relative">
                                        <div class="size-12 rounded-2xl bg-gradient-to-br from-slate-700 to-slate-900 p-[1px] group-hover:scale-110 transition-transform duration-300">
                                            <img src="{{ u.image.url }}" class="w-full h-full object-cover rounded-2xl" alt="">
                                        </div>
                                        {% if u.is_active %}
                                            <span class="absolute -bottom-1 -right-1 size-3 bg-green-500 border-2 border-surface-dark rounded-full"></span>
                                        {% endif %}
                                    </div>
                                    <div>
                                        <p class="font-bold text-slate-100 group-hover:text-primary transition-colors">{{ u.username }}</p>
                                        <p class="text-[11px] text-slate-500 font-medium">{{ u.email }}</p>
                                    </div>
                                </td>
                                <td class="px-6 py-5">
                                    {% if u.role %}
                                        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-[10px] font-black bg-slate-800 text-slate-300 border border-white/10 group-hover:border-primary/30 transition-colors">
                                            {{ u.role.name|upper }}
                                        </span>
                                    {% else %}
                                        <span class="text-slate-600 text-[10px] font-medium tracking-tighter">UNASSIGNED</span>
                                    {% endif %}
                                </td>
                                <td class="px-6 py-5">
                                    {% if u.is_active %}
                                        <div class="flex items-center gap-2 text-green-500 font-black text-[10px] uppercase">
                                            <span class="size-1.5 rounded-full bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.6)]"></span>
                                            Operational
                                        </div>
                                    {% else %}
                                        <div class="flex items-center gap-2 text-slate-500 font-black text-[10px] uppercase">
                                            <span class="size-1.5 rounded-full bg-slate-600"></span>
                                            Locked
                                        </div>
                                    {% endif %}
                                </td>
                                <td class="px-6 py-5 text-right">
                                    <div class="flex justify-end gap-2">
                                        <a href="{% url 'tech_admin:auth_user_change' u.id %}" 
                                           class="p-2 rounded-lg bg-white/5 text-slate-400 hover:text-primary hover:bg-primary/10 transition-all"
                                           title="Edit User">
                                            <span class="material-symbols-outlined text-lg">edit_square</span>
                                        </a>

                                        <form action="{% url 'tech_admin:auth_user_delete' u.id %}" method="POST" 
                                              onsubmit="return confirm('Confirm deletion of {{ u.username }}?');"
                                              class="inline">
                                            {% csrf_token %}
                                            <button type="submit" class="p-2 rounded-lg bg-white/5 text-slate-400 hover:text-red-500 hover:bg-red-500/10 transition-all" title="Delete User">
                                                <span class="material-symbols-outlined text-lg">delete</span>
                                            </button>
                                        </form>
                                    </div>
                                </td>
                            </tr>
                            {% empty %}
                            <tr>
                                <td colspan="4" class="px-6 py-20 text-center">
                                    <span class="material-symbols-outlined text-4xl text-slate-700 mb-2">database_off</span>
                                    <p class="text-slate-500 italic text-sm">No records match your current parameters.</p>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="space-y-6">
            <h4 class="text-[10px] font-black text-slate-500 uppercase tracking-[0.3em] pl-2">System Modules</h4>
            <div class="grid grid-cols-1 gap-3">
                {% for app in app_list %}
                    {% for model in app.models %}
                    {% if model.object_name != "User" %}
                    <a href="{{ model.admin_url }}" 
                       class="group relative flex items-center justify-between p-4 bg-surface-dark/40 border border-white/5 rounded-2xl hover:border-primary/40 hover:bg-surface-dark transition-all duration-300 overflow-hidden">
                        
                        <div class="absolute -right-4 -bottom-4 size-20 bg-primary/5 rounded-full blur-2xl group-hover:bg-primary/10 transition-all"></div>
                        
                        <div class="flex items-center gap-4 relative z-10">
                            <div class="size-11 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center group-hover:scale-110 group-hover:bg-primary/10 group-hover:border-primary/20 transition-all duration-300">
                                <span class="material-symbols-outlined text-slate-400 group-hover:text-primary">
                                    {% if model.object_name == "Movie" %}movie
                                    {% elif model.object_name == "User" %}account_circle
                                    {% else %}analytics{% endif %}
                                </span>
                            </div>
                            <div class="flex flex-col">
                                <span class="font-bold text-sm text-slate-200 group-hover:text-white">{{ model.name }}</span>
                                <span class="text-[9px] text-slate-500 font-bold uppercase tracking-tighter">Manage data entries</span>
                            </div>
                        </div>
                        <span class="material-symbols-outlined text-slate-700 group-hover:text-primary transition-all translate-x-0 group-hover:translate-x-1">chevron_right</span>
                    </a>
                    {% endif %}
                    {% endfor %}
                {% endfor %}
            </div>

            <div class="p-5 rounded-3xl bg-gradient-to-br from-primary/10 to-transparent border border-primary/20 mt-8">
                <h5 class="text-xs font-black text-primary uppercase mb-2">System Integrity</h5>
                <p class="text-[11px] text-slate-400 leading-relaxed mb-4">All services are currently operational. Database latency is within normal parameters (12ms).</p>
                <div class="w-full bg-white/5 h-1.5 rounded-full overflow-hidden">
                    <div class="bg-primary h-full w-[98%] shadow-[0_0_8px_#your-primary-color]"></div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/base/base.html -->
## app/templates/base/base.html

```html
{% load static %}
<!DOCTYPE html>
<html class="dark" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    
    <title>{% block title %}StreamSync{% endblock %}</title>

    <!-- Fonts -->
    <link href="https://fonts.googleapis.com" rel="preconnect"/>
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
    <link href="https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>

    <!-- DESPUÉS (correcto) -->
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <script src="{% static 'js/tailwind.config.js' %}"></script>
        
    <link rel="stylesheet" href="{% static 'css/main.css' %}"/>
    {% block extra_styles %}{% endblock %}
</head>
<body class="bg-background-dark dark:bg-background-dark text-slate-900 dark:text-slate-100 font-display min-h-screen flex flex-col overflow-x-hidden antialiased">

    {% include "components/navbar.html" %}

    <main class="flex-1 w-full max-w-7xl mx-auto px-6 py-8">
        {% block content %}{% endblock %}
    </main>

    {% include "components/footer.html" %}

    {% block extra_scripts %}{% endblock %}
</body>
</html>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/base/initial.html -->
## app/templates/base/initial.html

```html
{% load static %}
<!DOCTYPE html>
<html class="dark" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>

    <title>{% block title %}StreamSync{% endblock %}</title>

    <!-- Fonts -->
    <link href="https://fonts.googleapis.com" rel="preconnect"/>
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
    <link href="https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>

    <!-- DESPUÉS (correcto) -->
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <script src="{% static 'js/tailwind.config.js' %}"></script>

    <link rel="stylesheet" href="{% static 'css/main.css' %}"/>
    {% block extra_styles %}{% endblock %}
</head>
<body class="bg-background-dark dark:bg-background-dark text-slate-900 dark:text-slate-100 font-display min-h-screen flex flex-col overflow-x-hidden antialiased">

     {% include "components/navbar-init.html" %}
    <main class="flex-1 w-full max-w-7xl mx-auto px-6 py-8">
        {% block content %}{% endblock %}
    </main>

    {% include "components/footer.html" %}

    {% block extra_scripts %}{% endblock %}
</body>
</html>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/components/card_movies.html -->
## app/templates/components/card_movies.html

```html
<!-- Movies -->
<section class="mb-14">
    

    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">
        {% for movie in movies %}
        <div class="group flex flex-col gap-3 transition-all duration-500 hover:scale-105">

            <div class="aspect-[2/3] rounded-xl overflow-hidden relative cinematic-shadow hover-electric">

                <!-- Image -->
                <img src="{{'https://via.placeholder.com/300x450?text=No+Image'}}"
                    class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" />

                <!-- Gradient -->
                <div class="absolute inset-0 bg-gradient-to-t from-[#101622] via-transparent to-transparent opacity-80">
                </div>

                <!-- Year -->
                <div class="absolute top-3 left-3">
                    <span class="bg-black/60 backdrop-blur-sm text-white text-[10px] px-2 py-0.5 rounded">
                        {{ movie.year }}
                    </span>
                </div>

                <!-- Platforms -->
                <div class="absolute top-3 right-3 flex flex-col gap-1.5 items-end">
                    {% for platform in movie.platforms %}
                    <span class="bg-primary text-white text-[10px] px-2 py-0.5 rounded shadow">
                        {{ platform }}
                    </span>
                    {% endfor %}
                </div>

                <!-- Hover -->
                <div
                    class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-all duration-300 flex flex-col justify-end p-4">
                    <a href="{% url 'app:content_detail' 'movie' movie.unique_id %}" 
                        class="bg-primary text-white text-center text-xs font-bold py-2 rounded-lg tracking-wide hover:bg-primary/80 block">
                        Watch now
                    </a>
                </div>

            </div>

            <!-- Info -->
            <div class="px-1">
                <h3 class="font-bold text-sm truncate group-hover:text-primary transition-colors">
                    <a href="{% url 'app:content_detail' 'movie' movie.unique_id %}">{{ movie.title }}</a>
                </h3>
                <div class="flex items-center gap-2 mt-1">
                    <span class="text-xs text-slate-400">
                        {{ movie.year|default:"—" }}
                    </span>

                    <span class="w-1 h-1 bg-slate-500/40 rounded-full"></span>

                    <span class="text-xs text-slate-400 truncate">
                        {{ movie.genre_name|default:"Unknown" }}
                    </span>
                </div>
                
                {% if movie.rating %}
                <div class="flex items-center gap-1 mt-1">
                    <span class="material-symbols-outlined text-amber-400 text-sm"
                        style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="text-xs text-on-surface-variant">{{ movie.rating }}</span>
                </div>
                {% endif %}
            </div>

        </div>
        {% endfor %}
    </div>
</section>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/components/card_series.html -->
## app/templates/components/card_series.html

```html
<!-- Series -->
<section class="mb-14">
    

    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">
        {% for serie in series %}
        <div class="group flex flex-col gap-3 transition-all duration-500 hover:scale-105">

            <div class="aspect-[2/3] rounded-xl overflow-hidden relative cinematic-shadow hover-electric">

                <!-- Image -->
                <img  src="{{'https://via.placeholder.com/300x450?text=No+Image'}}"
                    class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" />

                <!-- Gradient -->
                <div class="absolute inset-0 bg-gradient-to-t from-[#101622] via-transparent to-transparent opacity-80">
                </div>

                <!-- Year -->
                <div class="absolute top-3 left-3">
                    <span class="bg-black/60 backdrop-blur-sm text-white text-[10px] px-2 py-0.5 rounded">
                        {{ serie.start_year }}
                    </span>
                </div>

                <!-- Platforms -->
                <div class="absolute top-3 right-3 flex flex-col gap-1.5 items-end">
                    {% for platform in serie.platforms %}
                    <span class="bg-primary text-white text-[10px] px-2 py-0.5 rounded shadow">
                        {{ platform }}
                    </span>
                    {% endfor %}
                </div>

                <!-- Hover -->
                <div
                    class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-all duration-300 flex flex-col justify-end p-4">
                    <a href="{% url 'app:content_detail' 'series' serie.unique_id %}"
                        class="bg-primary text-white text-center text-xs font-bold py-2 rounded-lg tracking-wide hover:bg-primary/80 block">
                        Watch now
                    </a>
                </div>

            </div>

            <!-- Info -->
            <div class="px-1">
                <h3 class="font-bold text-sm truncate group-hover:text-primary transition-colors">
                    <a href="{% url 'app:content_detail' 'series' serie.unique_id %}">{{ serie.title }}</a>
                </h3>

                <div class="flex items-center gap-2 mt-1">
                    <span class="text-xs text-slate-400">
                        {{ serie.start_year|default:"—" }}
                    </span>

                    <span class="w-1 h-1 bg-slate-500/40 rounded-full"></span>

                    <span class="text-xs text-slate-400 truncate">
                        {{ serie.genre_name|default:"Unknown" }}
                    </span>
                </div>

                {% if serie.rating %}
                <div class="flex items-center gap-1 mt-1">
                    <span class="material-symbols-outlined text-amber-400 text-sm"
                        style="font-variation-settings: 'FILL' 1;">star</span>
                    <span class="text-xs text-on-surface-variant">{{ serie.rating }}</span>
                </div>
                {% endif %}
            </div>

        </div>
        {% endfor %}
    </div>
</section>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/components/footer.html -->
## app/templates/components/footer.html

```html
<footer class="border-t border-border-light dark:border-border-dark mt-auto py-8">
    <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-4">
        <p class="text-slate-500 dark:text-slate-400 text-sm">&copy 2026 StreamSync Inc. All rights reserved.</p>
        <div class="flex gap-6 text-sm text-slate-500 dark:text-slate-400">
            <a class="hover:text-primary" href="#">Privacy Policy</a>
            <a class="hover:text-primary" href="#">Terms of Service</a>
            <a class="hover:text-primary" href="#">Help Center</a>
        </div>
    </div>
</footer>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/components/navbar-init.html -->
## app/templates/components/navbar-init.html

```html
<header class="sticky top-0 z-50 w-full border-b border-solid border-border-light dark:border-border-dark bg-surface-light/80 dark:bg-background-dark/80 backdrop-blur-md px-6 py-4">

    <a href="{% url 'app:home' %}" class="flex items-center gap-3 text-primary">
      <div class="size-8 rounded-lg bg-primary/20 flex items-center justify-center">
        <span class="material-symbols-outlined text-primary text-2xl">play_circle</span>
      </div>
      <h2 class="text-slate-900 dark:text-white text-xl font-bold tracking-tight">
        StreamSync
      </h2>
    </a>

</header>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/components/navbar.html -->
## app/templates/components/navbar.html

```html
<header class="sticky top-0 z-50 w-full border-b border-solid border-border-light dark:border-border-dark bg-surface-light/80 dark:bg-background-dark/80 backdrop-blur-md px-6 py-4">
  <div class="max-w-7xl mx-auto flex items-center justify-between">

    <div class="flex items-center gap-8">

      <a href="{% url 'app:main' %}" class="flex items-center gap-3 text-primary">
        <div class="size-8 rounded-lg bg-primary/20 flex items-center justify-center">
          <span class="material-symbols-outlined text-primary text-2xl">play_circle</span>
        </div>
        <h2 class="text-slate-900 dark:text-white text-xl font-bold tracking-tight">
          StreamSync
        </h2>
      </a>

      <nav class="hidden md:flex items-center gap-6 text-sm font-medium">
        <a href="{% url 'app:catalog' %}" class="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors">
          Full Catalog
        </a>
        <a href="{% url 'app:movies' %}" class="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors">
          Movies
        </a>
        <a href="{% url 'app:series' %}" class="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors">
          Series
        </a>
        <a href="#" class="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors">
          My List
        </a>
      </nav>

    </div>

    <div class="hidden md:flex flex-1 max-w-xl mx-8">
      <form action="{% url 'app:search' %}" method="GET" class="relative w-full group">

        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 dark:text-slate-500">
          <span class="material-symbols-outlined text-[20px]">search</span>
        </div>

        <input
          type="text"
          name="q"
          value="{{ request.GET.q }}"
          placeholder="Search movies, shows, or platforms..."
          class="block w-full rounded-xl border-none bg-slate-100 dark:bg-[#1e293b] py-2.5 pl-10 pr-3 text-sm placeholder-slate-400 dark:placeholder-slate-500 text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all shadow-sm"
        />

        <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
          <span class="text-xs text-slate-400 dark:text-slate-500 border border-slate-200 dark:border-slate-700 rounded px-1.5 py-0.5">⌘K</span>
        </div>

      </form>
    </div>

    <div class="flex items-center gap-4">
  {% if user.is_authenticated %}
    <button class="relative p-2 rounded-full hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors text-slate-600 dark:text-slate-400">
      <span class="material-symbols-outlined">notifications</span>
      <span class="absolute top-2 right-2 size-2 rounded-full border-2 border-surface-light dark:border-background-dark bg-primary"></span>
    </button>

    <div class="h-8 w-[1px] bg-border-light dark:bg-border-dark mx-1"></div>

    <div class="relative" id="user-menu-wrapper">
      <button id="user-menu-button" class="flex items-center gap-2 rounded-full p-1 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors focus:outline-none">
        <div class="size-9 rounded-full bg-cover bg-center border border-slate-200 dark:border-slate-700"
          style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuDDIAQ90IxsinjXM6PKvOAaLRDc7SY_R-7MVZ7vKDplBK7950nw55ZsHlVjzpNJ8O2lOn4dzlyKwejQm-g1R1zTQ-yZAJh8gKj7DDUaFAjgMlw4f_G4wKHpDUU5KvzD1qk71kCOaHNW-DXrAhGOeBQGxvzYQeMW70BVbPqVRfxLbQuAyoV2zIfQjweJuxtG5gg4Nr-3nsr2ETbHgYaZBmzIGdzCM9pS9q1rVq1DLjeAigarT-PPxUa7ZeXqXbs6yqL6JUmGOnKS_X36");'>
        </div>
        <span class="material-symbols-outlined text-slate-400 text-sm">expand_more</span>
      </button>

      <div id="user-dropdown" class="hidden absolute right-0 mt-2 w-52 origin-top-right rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xl z-[60] overflow-hidden">
        <div class="p-2 flex flex-col gap-1">
          
          <a href="{% url 'app:personal_library' %}" class="flex items-center gap-3 px-3 py-2.5 text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-xl transition-colors">
            <span class="material-symbols-outlined text-primary">video_library</span>
            Personal Library
          </a>

          <a href="{% url 'app:user_settings' %}" class="flex items-center gap-3 px-3 py-2.5 text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-xl transition-colors">
            <span class="material-symbols-outlined text-slate-400">settings</span>
            Settings
          </a>

          <div class="h-[1px] bg-slate-100 dark:bg-slate-800 my-1"></div>

          <form action="{% url 'logout' %}" method="post" class="w-full">
            {% csrf_token %}
            <button type="submit" class="flex w-full items-center gap-3 px-3 py-2.5 text-sm text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-xl transition-colors">
              <span class="material-symbols-outlined">logout</span>
              Sign Out
            </button>
          </form>

        </div>
      </div>
    </div>
  {% else %}
    <a href="{% url 'login' %}" class="text-sm font-bold text-primary px-4 py-2 rounded-xl hover:bg-primary/10 transition-colors">
      Sign In
    </a>
  {% endif %}
</div>


</header>
{% block extra_scripts %} 
    {% load static %}
    <script src="{% static 'js/navbar.js' %}"></script>
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/components/platforms_filter.html -->
## app/templates/components/platforms_filter.html

```html
<div class="flex flex-wrap items-center gap-3 p-2 bg-surface-dark rounded-xl border border-white/5">
    <span class="text-xs font-bold text-slate-500 uppercase ml-2">Filtrar por:</span>
    
    <select name="platform" onchange="this.form.submit()"
        class="bg-background-dark border-slate-700 rounded-lg text-sm text-white focus:ring-primary">
        <option value="">All Platforms</option>
        {% for p in platforms %}
        <option value="{{ p }}" {% if selected_platform == p %}selected{% endif %}>{{ p }}</option>
        {% endfor %}
    </select>

    <select name="genre" onchange="this.form.submit()"
        class="bg-background-dark border-slate-700 rounded-lg text-sm text-white focus:ring-primary">
        <option value="">All Genres</option>
        {% for g in genres %}
        <option value="{{ g }}" {% if selected_genre == g %}selected{% endif %}>{{ g }}</option>
        {% endfor %}
    </select>

    <select name="sort_rating" onchange="this.form.submit()"
        class="bg-background-dark border-slate-700 rounded-lg text-sm text-white focus:ring-primary">
        <option value="">Rating (Sin orden)</option>
        <option value="desc" {% if sort_rating == "desc" %}selected{% endif %}>Rating: Highest to Lowest</option>
        <option value="asc" {% if sort_rating == "asc" %}selected{% endif %}>Rating: Lowest to Highest</option>
    </select>

    <select name="sort_year" onchange="this.form.submit()"
        class="bg-background-dark border-slate-700 rounded-lg text-sm text-white focus:ring-primary">
        <option value="">Año (Sin orden)</option>
        <option value="desc" {% if sort_year == "desc" %}selected{% endif %}>Year: Most recent</option>
        <option value="asc" {% if sort_year == "asc" %}selected{% endif %}>Year: Oldest</option>
    </select>
</div>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/components/stat_card.html -->
## app/templates/components/stat_card.html

```html
<div class="rounded-2xl border border-white/5 bg-surface-dark p-5">
  <div class="flex items-center justify-between">
    
    <p class="text-sm text-text-secondary">
      {{ title }}
    </p>

    <span class="material-symbols-outlined {{ icon_color }}">
      {{ icon }}
    </span>

  </div>

  <h2 class="text-3xl font-black text-white mt-4">
    {{ value }}
  </h2>
</div>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/catalog.html -->
## app/templates/pages/catalog.html

```html
{% extends "base/base.html" %}

{% block title %}StreamSync – Catalog{% endblock %}

{% block content %}

<div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-10 gap-4">
        <h1 class="text-3xl md:text-4xl font-bold tracking-tight">Full Catalog</h1>
        <form method="GET" action="{% url 'app:catalog' %}" class="flex flex-wrap gap-4 mb-8 p-4">
                {% include "components/platforms_filter.html" with selected_platform=selected_platform %}
        </form>
</div>

<h1 class="text-3xl font-bold">Movies</h1>
{% include "components/card_movies.html" with movies=movies %}

<h1 class="text-3xl font-bold">Series</h1>
{% include "components/card_series.html" with series=series %}


{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/content_view.html -->
## app/templates/pages/content_view.html

```html
{% extends "base/base.html" %}

{% block content %}
<!-- Content Canvas -->
<main class="relative min-h-screen">

  <!-- Detail Content -->
  <div class="relative z-10 pt-64 px-8 md:px-24 pb-24 max-w-7xl mx-auto">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
      <!-- Main Info Col -->
      <div class="lg:col-span-8 space-y-12">
        <section>
          <h1 class="text-6xl md:text-8xl font-black tracking-tighter text-on-surface mb-6 leading-none">
            {{ content.title }}
          </h1>
          <!-- Metadata Row -->
          <div class="flex flex-wrap items-center gap-6 text-[#90a4cb] font-medium tracking-wide">

            <span class="flex items-center gap-2">
              <span class="material-symbols-outlined text-primary text-lg">calendar_today</span>
              {{ content.year}}
            </span>
            <span class="flex items-center gap-2 border-l border-white/10 pl-6">
              <span class="material-symbols-outlined text-primary text-lg">event</span>
              {{ content.release_date}}
            </span>
            <span class="flex items-center gap-2 border-l border-white/10 pl-6">
              <span class="material-symbols-outlined text-primary text-lg">schedule</span>
              {{ content.duration_minutes }} min
            </span>
            <span class="flex items-center gap-2 border-l border-white/10 pl-6">
              <span
                class="px-2 py-0.5 rounded-lg border border-primary text-primary text-xs font-bold uppercase tracking-widest">
                <span class="material-symbols-outlined text-amber-400 text-sm"
                  style="font-variation-settings: 'FILL' 1;">star </span>
                {{ content.rating }}
              </span>
            </span>
            <span class="flex items-center gap-2 border-l border-white/10 pl-6">
              <span
                class="px-2 py-0.5 rounded-lg border border-primary text-primary text-xs font-bold uppercase tracking-widest">
                {{ content.age_rating|default:"NR" }}
              </span>
            </span>
            <span class="flex items-center gap-2 border-l border-white/10 pl-6 text-on-surface">
              <span class="material-symbols-outlined text-primary text-lg">movie</span>
              {{ content.genre_name|default:"Unknown Genre" }}
            </span>
            {% if content.start_year %}
            <span class="flex items-center gap-2 border-l border-white/10 pl-6 text-on-surface">
              TV Series
            </span>
            {% else %}
            <span class="flex items-center gap-2 border-l border-white/10 pl-6 text-on-surface">
              Movie
            </span>
            {% endif %}
          </div>
        </section>
        <!-- CTA Buttons -->
        <div class="flex flex-wrap gap-4 pt-4">
          {% for platform in content.platforms %}
          <button
            class="bg-[#256af4] hover:bg-blue-500 text-white px-10 py-4 rounded-xl font-bold flex items-center gap-3 shadow-lg shadow-primary/30 active:scale-95 transition-all">
            <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">play_arrow</span>

            {{ platform }}

          </button>
          {% endfor %}
        </div>
        <!-- Synopsis Section -->
        <section class="space-y-4 pt-8">
          <h2 class="text-xl font-bold tracking-tight text-white uppercase tracking-[0.2em] text-primary">Synopsis</h2>
          <p class="text-lg text-[#90a4cb] leading-relaxed max-w-3xl">
            {{ content.synopsis }}
          </p>
        </section>
      </div>
      <!-- Secondary Info Col -->
      <div class="lg:col-span-4 flex flex-col gap-8">
        <!-- Director Card -->
        <div class="glass-panel border border-white/5 p-8 rounded-2xl">
          <h3 class="text-xs font-bold text-[#90a4cb] uppercase tracking-widest mb-6">Directed By</h3>
          <div class="flex items-center gap-5">
            <div class="w-16 h-16 rounded-full overflow-hidden border-2 border-primary/20">
              <img alt="Director Profile" class="w-full h-full object-cover"
                data-alt="Professional headshot of a film director with graying hair in a dark turtleneck against a moody blue background"
                src="https://lh3.googleusercontent.com/aida-public/AB6AXuAjnvAPY6qgA6yHuXKHrqtvsy2emspZ-UM482wOZLhf7904tFkORqIHEMtb8SqXCkucBSuxFv7otqPbkVCQe3DbEI9ynd5Ci8JGX1CyKsyRszYkOzxnP3buEB39QxiczkWHTbD7zBPkghxebW9WyTfSQdOO57OfBnwMDg7l6yhti7h61rfym8V4-BW0qYh7_gSYGzAaGhPu-LMBLIO7GmFPPIIHkkaaJiZFesTqAERm0d-r3C9VYmeVoE4aqZKoahCv0lF-HROr3FNY" />
            </div>
            <div>
              <p class="text-xl font-bold text-white leading-tight">
                {{ content.director|default:"Unknown Director" }}
              </p>
              <p class="text-[#90a4cb] text-sm flex items-center gap-1.5 mt-1">
                <span class="material-symbols-outlined text-xs">public</span>
                {{ content.director_nationality|default:"Unknown Nationality" }}
              </p>
            </div>
          </div>
        </div>
        <!-- Genre Spotlight -->
        <div class="bg-surface-container-high/40 p-8 rounded-2xl border border-white/5">
          <h3 class="text-xs font-bold text-[#90a4cb] uppercase tracking-widest mb-4"></h3>
          <p class="text-on-surface leading-relaxed text-sm">
            {{ content.genre_description|default:"No genre description available." }}
          </p>
        </div>
        <button
          class="flex items-center gap-3 px-6 py-3 rounded-xl font-semibold transition-all border border-blue-500/30 bg-blue-500/10 hover:bg-blue-500/20 text-blue-400 active:scale-95">
          <span class="material-symbols-outlined text-blue-400">bookmark_add</span>
          Add to Watchlist
        </button>

        <button id="favorite-btn"
          class="flex items-center gap-3 px-6 py-3 rounded-xl font-semibold transition-all border border-pink-500/30 bg-pink-500/10 hover:bg-pink-500/20 text-pink-400 hover:text-pink-300 active:scale-95">
          <span class="material-symbols-outlined text-pink-400" id="favorite-icon">{% if is_favorite %}favorite{% else %}favorite_border{% endif %}</span>
          <span id="favorite-text">{% if is_favorite %}Remove from Favorites{% else %}Add to Favorites{% endif %}</span>
        </button>

        <div class="relative">
          <button id="status-btn" type="button"
            class="w-full flex items-center justify-between gap-3 px-6 py-3 rounded-xl font-semibold transition-all border border-purple-500/30 bg-purple-500/10 text-purple-400 active:scale-95">
            <span class="material-symbols-outlined text-purple-400" id="status-icon">visibility_off</span>
            <span id="status-text">Not Seen</span>
            <span class="material-symbols-outlined text-purple-400">expand_more</span>
          </button>
          <div id="status-dropdown" class="hidden absolute top-full left-0 w-full mt-2 bg-surface-dark border border-white/10 rounded-xl overflow-hidden z-50 shadow-xl">
            <button type="button" class="w-full px-6 py-3 text-left hover:bg-white/10 text-slate-300 flex items-center gap-3 transition-colors" data-status="not_seen">
              <span class="material-symbols-outlined text-sm">visibility_off</span>
              Not Seen
            </button>
            <button type="button" class="w-full px-6 py-3 text-left hover:bg-white/10 text-slate-300 flex items-center gap-3 transition-colors" data-status="watching">
              <span class="material-symbols-outlined text-sm">play_circle</span>
              Watching
            </button>
            <button type="button" class="w-full px-6 py-3 text-left hover:bg-white/10 text-slate-300 flex items-center gap-3 transition-colors" data-status="completed">
              <span class="material-symbols-outlined text-sm">check_circle</span>
              Completed
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</main>
<!-- BottomNavBar (Shared Component - Mobile Only) -->
<nav
  class="md:hidden fixed bottom-0 w-full z-50 bg-[#1a2333]/60 backdrop-blur-md flex justify-around items-center py-4 px-6 border-t border-white/5">
  <button class="flex flex-col items-center gap-1 text-[#256af4] font-bold">
    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">home</span>
    <span class="text-[10px]">Home</span>
  </button>
  <button class="flex flex-col items-center gap-1 text-[#90a4cb]">
    <span class="material-symbols-outlined">explore</span>
    <span class="text-[10px]">Discovery</span>
  </button>
  <button class="flex flex-col items-center gap-1 text-[#90a4cb]">
    <span class="material-symbols-outlined">bookmark</span>
    <span class="text-[10px]">Watchlist</span>
  </button>
  <button class="flex flex-col items-center gap-1 text-[#90a4cb]">
    <span class="material-symbols-outlined">settings</span>
    <span class="text-[10px]">Settings</span>
  </button>
</nav>
{% endblock %}

{% block extra_scripts %} 
    {% load static %}
    <script>
      window.CONTENT_DATA = {
        id: '{{ content.unique_id|default:content.id }}',
        type: '{{ content.content_type|default:"movie" }}',
        userStatus: '{{ user_status|default:"not_seen" }}'
      };
    </script>
    <script src="{% static 'js/content.js' %}"></script>
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/direction_dashboard.html -->
## app/templates/pages/direction_dashboard.html

```html
{% extends "base/base.html" %}

{% block content %}
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <div class="flex min-h-screen font-display text-slate-100 bg-transparent">

        <aside class="w-80 flex flex-col justify-center sticky top-0 h-screen bg-transparent px-6">
            <form id="filter-form" method="GET"
                  class="bg-[#0f172a] border border-slate-800/60 p-8 rounded-[3.5rem] flex flex-col gap-5 shadow-[0_0_50px_rgba(0,0,0,0.8)]">

                <div class="text-center mb-2">
                    <h2 class="text-xl font-bold text-white flex items-center justify-center gap-2">
                        <span class="material-symbols-outlined text-primary">tune</span> Filters
                    </h2>
                    <p class="text-[9px] text-slate-500 uppercase tracking-widest mt-1">Control Panel</p>
                </div>

                <div class="space-y-2">
                    <div class="flex flex-col mb-1">
                        <label class="text-[11px] font-black text-primary uppercase tracking-tight">Time
                            Analytics</label>
                        <span class="text-[9px] text-slate-500 leading-none">Predefined reporting periods</span>
                    </div>

                    <div class="grid grid-cols-3 gap-2 bg-slate-950/60 p-1 rounded-2xl border border-slate-800/50">
                        <button type="button" onclick="setQuickRange('24h')"
                                class="py-2 rounded-xl text-[9px] font-bold transition-all {% if filters.range == '24h' %}bg-primary text-white shadow-lg{% else %}text-slate-500 hover:text-slate-300{% endif %}">
                            24H
                        </button>
                        <button type="button" onclick="setQuickRange('7d')"
                                class="py-2 rounded-xl text-[9px] font-bold transition-all {% if filters.range == '7d' %}bg-primary text-white shadow-lg{% else %}text-slate-500 hover:text-slate-300{% endif %}">
                            7D
                        </button>
                        <button type="button" onclick="setQuickRange('30d')"
                                class="py-2 rounded-xl text-[9px] font-bold transition-all {% if filters.range == '30d' %}bg-primary text-white shadow-lg{% else %}text-slate-500 hover:text-slate-300{% endif %}">
                            30D
                        </button>
                    </div>

                    <div class="grid grid-cols-2 gap-2 bg-slate-950/60 p-1.5 rounded-2xl border border-slate-800/50">
                        <button type="button" onclick="setQuickRange('90d')"
                                class="py-2 rounded-xl text-[9px] font-bold transition-all {% if filters.range == '90d' %}bg-primary text-white shadow-lg{% else %}text-slate-500 hover:text-slate-300{% endif %}">
                            QUARTER
                        </button>
                        <button type="button" onclick="setQuickRange('ytd')"
                                class="py-2 rounded-xl text-[9px] font-bold transition-all {% if filters.range == 'ytd' %}bg-primary text-white shadow-lg{% else %}text-slate-500 hover:text-slate-300{% endif %}">
                            YTD
                        </button>
                    </div>

                    <input type="hidden" name="range" id="range-input" value="{{ filters.range }}">
                </div>

                <div class="space-y-3">
                    <div class="flex flex-col mb-1">
                        <label class="text-[11px] font-black text-primary uppercase tracking-tight">Custom Range</label>
                        <span class="text-[9px] text-slate-500 leading-none">Specific calendar selection</span>
                    </div>
                    <div class="relative">
                        <input type="date" name="start_date" id="start_date" value="{{ filters.start_date }}"
                               onfocus="clearQuickRange()"
                               class="w-full bg-slate-950/40 border border-slate-800 text-[11px] text-slate-300 rounded-2xl px-4 py-3 outline-none focus:border-primary appearance-none">
                        <span class="text-[8px] text-slate-500 absolute -top-2 left-4 bg-[#0f172a] px-2 border border-slate-800 rounded-full font-bold uppercase">From</span>
                    </div>
                    <div class="relative">
                        <input type="date" name="end_date" id="end_date" value="{{ filters.end_date }}"
                               onfocus="clearQuickRange()"
                               class="w-full bg-slate-950/40 border border-slate-800 text-[11px] text-slate-300 rounded-2xl px-4 py-3 outline-none focus:border-primary appearance-none">
                        <span class="text-[8px] text-slate-500 absolute -top-2 left-4 bg-[#0f172a] px-2 border border-slate-800 rounded-full font-bold uppercase">To</span>
                    </div>
                    <button type="submit"
                            class="w-full py-3 bg-slate-800 hover:bg-primary text-white rounded-2xl text-[10px] font-black transition-all flex items-center justify-center gap-2">
                        UPDATE SEARCH <span class="material-symbols-outlined text-base">calendar_month</span>
                    </button>
                </div>

                <div class="space-y-3 pt-3 border-t border-slate-800/50">
                    <div class="flex flex-col mb-1">
                        <label class="text-[11px] font-black text-primary uppercase tracking-tight">Segmentation</label>
                        <span class="text-[9px] text-slate-500 leading-none">Categorical filters</span>
                    </div>

                    <select name="platform" onchange="this.form.submit()"
                            class="w-full bg-slate-950/40 border border-slate-800 text-xs font-bold text-slate-300 rounded-2xl px-4 py-3 appearance-none focus:border-primary outline-none cursor-pointer">
                        <option value="all">All Platforms</option>
                        {% for p in platforms %}
                            <option value="{{ p.id }}"
                                    {% if filters.platform|stringformat:"s" == p.id|stringformat:"s" %}selected{% endif %}>{{ p.platform_name }}</option>
                        {% endfor %}
                    </select>

                    <select name="country" onchange="this.form.submit()"
                            class="w-full bg-slate-950/40 border border-slate-800 text-xs font-bold text-slate-300 rounded-2xl px-4 py-3 appearance-none focus:border-primary outline-none cursor-pointer">
                        <option value="all">All Countries</option>
                        {% for c in countries %}
                            <option value="{{ c.id }}"
                                    {% if filters.country|stringformat:"s" == c.id|stringformat:"s" %}selected{% endif %}>{{ c.name }}</option>
                        {% endfor %}
                    </select>

                    <select name="genre" onchange="this.form.submit()"
                            class="w-full bg-slate-950/40 border border-slate-800 text-xs font-bold text-slate-300 rounded-2xl px-4 py-3 appearance-none focus:border-primary outline-none cursor-pointer">
                        <option value="all">All Genres</option>
                        {% for g in genres %}
                            <option value="{{ g.id }}"
                                    {% if filters.genre|stringformat:"s" == g.id|stringformat:"s" %}selected{% endif %}>{{ g.name }}</option>
                        {% endfor %}
                    </select>
                </div>
            </form>
        </aside>

        <main class="flex-1 p-8 lg:p-12 max-w-[1300px]">
            <header class="mb-10 flex justify-between items-start">
                <div>
                    <h1 class="text-4xl font-black text-white tracking-tight mb-2">Direction Dashboard</h1>
                    <p class="text-slate-400 text-sm">Strategic performance analysis and interaction growth trends.</p>
                </div>

                <a href="?{{ request.GET.urlencode }}&export=csv"
                   class="flex items-center gap-3 bg-[#2563eb] hover:bg-[#1d4ed8] text-white px-8 py-3.5 rounded-2xl font-black text-[11px] tracking-widest transition-all active:scale-95 uppercase">
                    <span class="material-symbols-outlined text-lg">download</span> EXPORT CSV
                </a>
            </header>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <div class="bg-slate-900/40 border border-slate-800/50 p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <p class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-2">Total
                            Engagement</p>
                        <h3 class="text-3xl font-black text-white flex items-baseline gap-2 flex-wrap">
                            {{ total_clicks }}
                            <span class="text-[11px] font-black text-slate-600 uppercase tracking-widest">Clicks</span>
                        </h3>
                    </div>
                </div>

                <div class="bg-slate-900/40 border border-slate-800/50 p-8 rounded-3xl flex flex-col justify-between">
                    <div>
                        <p class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-2">Interest
                            Score</p>
                        <h3 class="text-3xl font-black text-white flex items-baseline gap-2 flex-wrap">
                            {{ total_favorites }}
                            <span class="text-[11px] font-black text-slate-600 uppercase tracking-widest">Favs</span>
                        </h3>
                    </div>
                </div>

                <div class="bg-slate-900/40 border border-slate-800/50 p-8 rounded-3xl flex flex-col justify-between min-w-0">
                    <div>
                        <p class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-2">Dominant
                            Entity</p>
                        <h3 class="text-2xl font-black text-primary uppercase leading-tight"
                            title="{{ top_platform.platform__platform_name|default:'--' }}">
                            <div class="truncate">
                                {{ top_platform.platform__platform_name|default:"--" }}
                            </div>
                            <span class="text-[10px] font-black text-slate-600 uppercase tracking-widest block mt-1">Platform</span>
                        </h3>
                    </div>
                </div>
            </div>

            <section class="bg-slate-900/30 border border-slate-800/50 rounded-3xl p-8 mb-8 shadow-2xl">
                <h3 class="font-bold text-white mb-8 flex items-center gap-2">
                    <span class="material-symbols-outlined text-primary">analytics</span> Periodic Engagement Trend
                </h3>

                <div class="h-80 w-full relative flex items-center justify-center">
                    {% if chart_labels == '["No Data"]' or chart_labels == '[]' %}
                        <div class="text-center">
                            <span class="material-symbols-outlined text-slate-700 text-6xl mb-2">Query_stats</span>
                            <p class="text-slate-500 font-bold tracking-widest text-[10px] uppercase">No analytics data
                                 found for this period</p>
                        </div>
                    {% else %}
                        <canvas id="trendChart"></canvas>
                    {% endif %}
                </div>
            </section>

            <section class="bg-slate-900/30 border border-slate-800/50 rounded-3xl overflow-hidden shadow-2xl">
                <div class="p-8 pb-4 font-bold text-white flex items-center gap-2 border-b border-slate-800/50">
                    <span class="material-symbols-outlined text-primary">military_tech</span> Top Content Performance
                </div>
                <div class="px-8 pb-8 pt-4 overflow-x-auto">
                    <table class="w-full text-left table-auto">
                        <thead class="text-[10px] font-bold text-slate-500 uppercase tracking-wider">
                        <tr>
                            <th class="py-4 px-4">Title & Director</th>
                            <th class="py-4 px-4 text-center">Genre</th>
                            <th class="py-4 px-4 text-center">Country</th>
                            <th class="py-4 px-4 text-right">Interactions (Favs)</th>
                        </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/40">
                        {% for content in trending_content %}
                            <tr class="group hover:bg-slate-800/30 transition-all border-none">
                                <td class="py-5 px-4">
                                    <div class="font-bold text-slate-200 group-hover:text-primary transition-colors">{{ content.title }}</div>
                                    <div class="text-[10px] text-slate-600 font-bold uppercase tracking-widest">
                                        Dir. {{ content.director.name }}</div>
                                </td>
                                <td class="py-5 px-4 text-center">
                                    <span class="bg-slate-800 px-3 py-1 rounded-full text-[9px] text-slate-300 border border-slate-700 font-black uppercase">{{ content.genre.name }}</span>
                                </td>
                                <td class="py-5 px-4 text-center text-[11px] text-slate-400 font-medium uppercase">{{ content.country.name }}</td>
                                <td class="py-5 px-4 text-right font-mono font-black text-primary text-lg">{{ content.fav_count }}</td>
                            </tr>
                        {% empty %}
                            <tr>
                                <td colspan="4" class="py-16 text-center">
                                    <p class="text-slate-600 italic text-sm">No content matches the selected
                                        filters.</p>
                                </td>
                            </tr>
                        {% endfor %}
                        </tbody>
                    </table>
                </div>
            </section>
        </main>
    </div>

    <script>
        // Form handling
        function setQuickRange(v) {
            document.getElementById('range-input').value = v;
            document.getElementById('start_date').value = '';
            document.getElementById('end_date').value = '';
            document.getElementById('filter-form').submit();
        }

        function clearQuickRange() {
            document.getElementById('range-input').value = '';
        }

        // Chart.js initialization
        document.addEventListener('DOMContentLoaded', function () {
            const chartElement = document.getElementById('trendChart');

            if (chartElement) {
                const ctx = chartElement.getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: JSON.parse('{{ chart_labels|safe }}'),
                        datasets: [{
                            data: JSON.parse('{{ chart_values|safe }}'),
                            borderColor: '#3b82f6',
                            backgroundColor: 'rgba(59, 130, 246, 0.05)',
                            borderWidth: 3,
                            fill: true,
                            tension: 0.4,
                            pointRadius: 4,
                            pointBackgroundColor: '#3b82f6',
                            pointHoverRadius: 6
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {display: false},
                            tooltip: {
                                backgroundColor: '#0f172a',
                                titleFont: {size: 10},
                                bodyFont: {size: 12, weight: 'bold'},
                                padding: 12,
                                borderColor: '#1e293b',
                                borderWidth: 1
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                grid: {color: 'rgba(255,255,255,0.05)'},
                                ticks: {color: '#64748b', font: {size: 10}}
                            },
                            x: {
                                grid: {display: false},
                                ticks: {color: '#64748b', font: {size: 10}}
                            }
                        }
                    }
                });
            }
        });
    </script>
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/home.html -->
## app/templates/pages/home.html

```html
<!DOCTYPE html>

<html class="dark" lang="en">

<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>StreamSync - Premium Streaming Aggregator</title>
    <!-- Fonts -->
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect" />
    <link href="https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&amp;display=swap"
        rel="stylesheet" />
    <!-- Icons -->
    <link
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap"
        rel="stylesheet" />
    <link
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap"
        rel="stylesheet" />
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <!-- Tailwind Config -->
    <script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        "primary": "#256af4",
                        "background-light": "#f5f6f8",
                        "background-dark": "#101622",
                    },
                    fontFamily: {
                        "display": ["Spline Sans", "sans-serif"]
                    },
                    borderRadius: {
                        "DEFAULT": "0.25rem",
                        "lg": "0.5rem",
                        "xl": "0.75rem",
                        "2xl": "1rem",
                        "full": "9999px"
                    },
                },
            },
        }
    </script>
    <style>
        /* Custom Glassmorphism Utilities */
        .glass-card {
            background: rgba(24, 34, 52, 0.4);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .glass-btn {
            background: rgba(37, 106, 244, 0.2);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(37, 106, 244, 0.4);
        }
    </style>
</head>
<body class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100 font-display min-h-screen overflow-x-hidden selection:bg-primary selection:text-white">
<div class="relative flex h-auto min-h-screen w-full flex-col overflow-x-hidden">
<div class="layout-container flex h-full grow flex-col">
<!-- Navbar -->
<div class="w-full flex justify-center sticky top-0 z-50 bg-background-light/80 dark:bg-background-dark/80 backdrop-blur-md border-b border-slate-200 dark:border-slate-800">
<div class="w-full max-w-[1280px] px-6 py-4">
<header class="flex items-center justify-between whitespace-nowrap">
<div class="flex items-center gap-3 text-slate-900 dark:text-white group cursor-pointer">
<div class="size-8 rounded bg-gradient-to-tr from-primary to-blue-400 flex items-center justify-center text-white shadow-lg shadow-primary/20">
<span class="material-symbols-outlined text-xl">play_arrow</span>
</div>
<h2 class="text-lg font-bold leading-tight tracking-tight">StreamSync</h2>
</div>
<div class="hidden md:flex flex-1 justify-end gap-8 items-center">
<div class="flex items-center gap-8">
</div>
<div class="flex gap-3">
    <a href="/accounts/login">
        <button class="h-10 px-5 rounded-lg text-slate-900 dark:text-white text-sm font-bold border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all" >
            Log In
        </button>
    </a>
    <a href="/accounts/signup">
        <button class="h-10 px-5 rounded-lg bg-primary text-white text-sm font-bold hover:bg-blue-600 shadow-lg shadow-primary/25 transition-all" >
            Sign Up
        </button>
    </a>
</div>
</div>
<div class="md:hidden text-slate-900 dark:text-white cursor-pointer">
<span class="material-symbols-outlined">menu</span>
</div>
</header>
</div>
</div>
<div class="flex flex-1 justify-center w-full">
<div class="flex flex-col w-full max-w-[1280px]">
<!-- Hero Section -->
<div class="w-full p-4 md:p-6 lg:p-8">
<div class="relative w-full rounded-2xl overflow-hidden min-h-[600px] flex flex-col items-center justify-center text-center p-8 md:p-16 isolate group" data-alt="Cinematic abstract dark background with blurred lights suggesting a movie theater or streaming interface" style="background-image: linear-gradient(rgba(16, 22, 34, 0.7), rgba(16, 22, 34, 0.9)), url('https://lh3.googleusercontent.com/aida-public/AB6AXuB-Bj8k031UvDGluEh-Ip27Av30W7cX8wGrhKzpVgW1q_gj9WIjRXrw9m3uWt_Qot3ryseaq0Ef6KN2R1HM2QymJQ-CeRIBWH-5HY8h-f-o0XLCH07S9foil70ZfWM30jRReMJs7ictepzGIoYQedcDY8Tvle0kwVOViD_BYSRft3OesavfhBOQyfC2ASI-mN65x9FrpQp5F81FwJUUd3UpSV_9IyRvPOuHv0NngMQphqzqFZZZ6Dl1Kwi7h-BbFeExtAMiRYC-PVdl'); background-size: cover; background-position: center;">
<!-- Hero Content -->
<div class="relative z-10 flex flex-col gap-6 max-w-4xl mx-auto">
<div class="inline-flex items-center justify-center gap-2 px-3 py-1 rounded-full bg-white/10 backdrop-blur-sm border border-white/10 w-fit mx-auto">
<span class="w-2 h-2 rounded-full bg-primary animate-pulse"></span>
<span class="text-xs font-medium text-white tracking-wide uppercase">The Future of Streaming</span>
</div>
<h1 class="text-white text-5xl md:text-7xl font-black leading-[1.1] tracking-tight drop-shadow-2xl">
                                    All your streaming platforms in <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-blue-300">one place</span>
</h1>
<h2 class="text-slate-300 text-lg md:text-xl font-normal leading-relaxed max-w-2xl mx-auto">
                                    Experience entertainment management reimagined. StreamSync unifies Netflix, Hulu, HBO, and more into a single, seamless cinematic interface.
                                </h2>
                                <div class="flex flex-col sm:flex-row gap-4 justify-center mt-6">

                                </div>
                            </div>
                            <!-- Decorative blur -->
                            <div
                                class="absolute -bottom-1/2 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-primary/20 rounded-full blur-[120px] -z-10 pointer-events-none">
                            </div>
                        </div>
                    </div>
                    <!-- Stats Section -->
                    <div class="px-6 py-10 w-full">
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                            <div
                                class="glass-card p-6 rounded-xl flex flex-col items-center justify-center text-center gap-2 hover:border-primary/30 transition-colors">
                                <p class="text-primary text-4xl font-bold tracking-tighter">50+</p>
                                <p class="text-slate-400 font-medium text-sm uppercase tracking-wider">Services
                                    Integrated</p>
                            </div>
                            <div
                                class="glass-card p-6 rounded-xl flex flex-col items-center justify-center text-center gap-2 hover:border-primary/30 transition-colors">
                                <p class="text-primary text-4xl font-bold tracking-tighter">1M+</p>
                                <p class="text-slate-400 font-medium text-sm uppercase tracking-wider">Movies Indexed
                                </p>
                            </div>
                            <div
                                class="glass-card p-6 rounded-xl flex flex-col items-center justify-center text-center gap-2 hover:border-primary/30 transition-colors">
                                <p class="text-primary text-4xl font-bold tracking-tighter">500k+</p>
                                <p class="text-slate-400 font-medium text-sm uppercase tracking-wider">Active Users</p>
                            </div>
                        </div>
                    </div>
                    <!-- Features Section -->
                    <div class="flex flex-col gap-12 px-6 py-16 w-full">
                        <div
                            class="flex flex-col md:flex-row justify-between items-end gap-6 border-b border-slate-800 pb-8">
                            <div class="flex flex-col gap-3 max-w-2xl">
                                <h3 class="text-primary font-bold text-sm tracking-widest uppercase">Premium Tools</h3>
                                <h2
                                    class="text-slate-900 dark:text-white text-3xl md:text-5xl font-bold tracking-tight">
                                    Unlock your full viewing potential
                                </h2>
                                <p class="text-slate-600 dark:text-slate-400 text-lg">Powerful features designed to save
                                    you time and help you discover your next obsession.</p>
                            </div>
                            <button
                                class="hidden md:flex items-center gap-2 text-primary font-bold hover:text-blue-400 transition-colors">
                                Explore all features
                                <span class="material-symbols-outlined text-sm">arrow_forward</span>
                            </button>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                            <!-- Feature 1 -->
                            <div
                                class="glass-card p-6 rounded-2xl flex flex-col gap-4 group hover:-translate-y-1 transition-transform duration-300">
                                <div
                                    class="size-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
                                    <span class="material-symbols-outlined text-3xl">search</span>
                                </div>
                                <div>
                                    <h3 class="text-slate-900 dark:text-white text-lg font-bold mb-2">Unified Search
                                    </h3>
                                    <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                        Stop jumping between tabs. Search across Netflix, Hulu, HBO, and Disney+
                                        instantly from one bar.
                                    </p>
                                </div>
                            </div>
                            <!-- Feature 2 -->
                            <div
                                class="glass-card p-6 rounded-2xl flex flex-col gap-4 group hover:-translate-y-1 transition-transform duration-300">
                                <div
                                    class="size-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
                                    <span class="material-symbols-outlined text-3xl">checklist</span>
                                </div>
                                <div>
                                    <h3 class="text-slate-900 dark:text-white text-lg font-bold mb-2">Series Tracking
                                    </h3>
                                    <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                        Never forget which episode you're on. Keep track of every season and episode
                                        automatically.
                                    </p>
                                </div>
                            </div>
                            <!-- Feature 3 -->
                            <div
                                class="glass-card p-6 rounded-2xl flex flex-col gap-4 group hover:-translate-y-1 transition-transform duration-300">
                                <div
                                    class="size-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
                                    <span class="material-symbols-outlined text-3xl">auto_awesome</span>
                                </div>
                                <div>
                                    <h3 class="text-slate-900 dark:text-white text-lg font-bold mb-2">Smart Recs</h3>
                                    <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                        AI-driven suggestions that understand your unique taste better than any single
                                        platform algorithm.
                                    </p>
                                </div>
                            </div>
                            <!-- Feature 4 -->
                            <div
                                class="glass-card p-6 rounded-2xl flex flex-col gap-4 group hover:-translate-y-1 transition-transform duration-300">
                                <div
                                    class="size-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
                                    <span class="material-symbols-outlined text-3xl">notifications_active</span>
                                </div>
                                <div>
                                    <h3 class="text-slate-900 dark:text-white text-lg font-bold mb-2">Availability
                                        Alerts</h3>
                                    <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                        Get notified the second a movie on your watchlist becomes available on your
                                        subscribed services.
                                    </p>
                                </div>
                            </div>
                        </div>
                        <button
                            class="md:hidden w-full h-12 rounded-lg border border-slate-700 text-slate-300 font-bold hover:bg-slate-800 transition-all flex items-center justify-center gap-2">
                            Explore all features
                            <span class="material-symbols-outlined text-sm">arrow_forward</span>
                        </button>
                    </div>

                    <!-- Footer -->
                    <footer class="w-full border-t border-slate-200 dark:border-slate-800 py-10 px-6">
                        <div class="flex flex-col md:flex-row justify-between items-center gap-6">
                            <div class="flex items-center gap-2 text-slate-900 dark:text-white">
                                <div class="size-6 rounded bg-primary flex items-center justify-center text-white">
                                    <span class="material-symbols-outlined text-sm">play_arrow</span>
                                </div>
                                <span class="font-bold">StreamSync</span>
                            </div>
                            <div class="flex flex-wrap justify-center gap-8">
                                <a class="text-sm text-slate-500 hover:text-primary transition-colors" href="#">Privacy
                                    Policy</a>
                                <a class="text-sm text-slate-500 hover:text-primary transition-colors" href="#">Terms of
                                    Service</a>
                                <a class="text-sm text-slate-500 hover:text-primary transition-colors" href="#">Help
                                    Center</a>
                                <a class="text-sm text-slate-500 hover:text-primary transition-colors"
                                    href="#">Contact</a>
                            </div>
                            <div class="flex gap-4">
                                <a class="text-slate-400 hover:text-white transition-colors" href="#">
                                    <svg aria-hidden="true" class="h-5 w-5" fill="currentColor" viewbox="0 0 24 24">
                                        <path clip-rule="evenodd"
                                            d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"
                                            fill-rule="evenodd"></path>
                                    </svg>
                                </a>
                                <a class="text-slate-400 hover:text-white transition-colors" href="#">
                                    <svg aria-hidden="true" class="h-5 w-5" fill="currentColor" viewbox="0 0 24 24">
                                        <path
                                            d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84">
                                        </path>
                                    </svg>
                                </a>
                                <a class="text-slate-400 hover:text-white transition-colors" href="#">
                                    <svg aria-hidden="true" class="h-5 w-5" fill="currentColor" viewbox="0 0 24 24">
                                        <path clip-rule="evenodd"
                                            d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 016.588 3.32c.636-.247 1.363-.416 2.427-.465C10.051 2.013 10.406 2 12.315 2zm-4.755 8.461c-1.57 0-2.841 1.272-2.841 2.841 0 1.57 1.271 2.841 2.841 2.841 1.57 0 2.841-1.271 2.841-2.841 0-1.57-1.272-2.841-2.841-2.841zm6.617-3.26c-.724 0-1.312.588-1.312 1.312 0 .724.588 1.312 1.312 1.312.724 0 1.312-.588 1.312-1.312 0-.724-.588-1.312-1.312-1.312zm-4.305 6.1c1.514 0 2.744 1.23 2.744 2.744 0 1.514-1.23 2.744-2.744 2.744-1.514 0-2.744-1.23-2.744-2.744 0-1.514 1.23-2.744 2.744-2.744z"
                                            fill-rule="evenodd"></path>
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </footer>
                </div>
            </div>
        </div>
    </div>
</body>

</html>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/main.html -->
## app/templates/pages/main.html

```html
{% extends "base/base.html" %}

{% block title %}StreamSync Dashboard{% endblock %}

{% block content %}

<!-- Hero / Continue Watching Section -->
<section class="mb-12">
    <div class="flex items-center justify-between mb-6">
        <h2 class="text-2xl font-bold text-slate-900 dark:text-white tracking-tight">Continue Watching</h2>
        {% if has_watch_history %}
        <div class="flex gap-2">
            <button class="size-8 flex items-center justify-center rounded-full bg-slate-200 dark:bg-surface-dark hover:bg-primary hover:text-white dark:hover:bg-primary dark:hover:text-white transition-colors">
                <span class="material-symbols-outlined text-sm">chevron_left</span>
            </button>
            <button class="size-8 flex items-center justify-center rounded-full bg-slate-200 dark:bg-surface-dark hover:bg-primary hover:text-white dark:hover:bg-primary dark:hover:text-white transition-colors">
                <span class="material-symbols-outlined text-sm">chevron_right</span>
            </button>
        </div>
        {% endif %}
    </div>

    {% if has_watch_history %}
    <div class="flex gap-6 overflow-x-auto no-scrollbar pb-4 snap-x snap-mandatory">
        {% for progress in watch_progress %}
        <div class="min-w-[85%] md:min-w-[600px] snap-center relative group rounded-2xl overflow-hidden shadow-lg bg-surface-dark">
           <div 
                class="aspect-video w-full bg-cover bg-center transition-transform duration-700 group-hover:scale-105"
                data-alt="{{ progress.content.title }}"
                style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuB8gmG2z7Mt5ql8YqZIB9UncRckA9dVvEIypPTYJsz2Uv9uJVEmJuHGUjuplevC6kQTz3FZzFlEAaRT9aniSjkCyMNhQbqQ7Q5FYKLdRRJUi2ZN0EbI4CLDSqdZIxEQCBpQmWb_ILr-kpkgNZtKr5wSUUG3IOYiCW3mHglRN_SBbZla-bx_uf9DCYKKAiAPt5mATMcehA79Ae5rVymhTnO3jP6k088Sy1Em0RKbuTNTgAClz82PDIx-JXPQV6lEwIbjOCX3-q4uSij-");
            '>    
<div class="absolute inset-0 bg-gradient-to-t from-background-dark via-background-dark/50 to-transparent opacity-90"></div>
            </div>
            <div class="absolute bottom-0 left-0 w-full p-6 md:p-8">
                <div class="flex items-center gap-3 mb-2">
                    <span class="bg-primary text-white text-[10px] font-bold px-2 py-0.5 rounded tracking-wider uppercase">{{ progress.content.genre_name|default:"Movie" }}</span>
                    <span class="text-slate-300 text-sm font-medium">{{ progress.last_minute }}m • {{ progress.content.duration_minutes|default:90 }}m left</span>
                </div>
                <h3 class="text-3xl font-bold text-white mb-2 leading-tight">{{ progress.content.title }}</h3>
                <p class="text-slate-300 text-sm line-clamp-2 mb-4 max-w-lg">{{ progress.content.synopsis|default:"No description available." }}</p>
                <div class="flex items-center gap-4">
                    <button class="flex items-center gap-2 bg-primary hover:bg-primary/90 text-white px-6 py-2.5 rounded-lg font-semibold transition-all">
                        <span class="material-symbols-outlined fill text-[20px]">play_arrow</span>
                        <span>Resume</span>
                    </button>
                    <button class="flex items-center justify-center size-10 rounded-lg bg-white/10 hover:bg-white/20 backdrop-blur-sm text-white transition-colors">
                        <span class="material-symbols-outlined text-[20px]">add</span>
                    </button>
                </div>
                {% widthratio progress.last_minute progress.content.duration_minutes 100 as percentage %}
                <div class="absolute bottom-0 left-0 w-full h-1 bg-white/10">
                    <div class="h-full bg-primary w-[{{ percentage }}%] shadow-[0_0_10px_rgba(37,106,244,0.5)]"></div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
    {% else %}
    <div class="flex flex-col items-center justify-center py-16 bg-slate-100 dark:bg-surface-dark rounded-2xl">
        <span class="material-symbols-outlined text-6xl text-slate-400 mb-4">movie_filter</span>
        <h3 class="text-xl font-semibold text-slate-700 dark:text-slate-300 mb-2">Oops, you're not watching anything yet</h3>
        <p class="text-slate-500 dark:text-slate-400 mb-6">Take a look at our catalog!</p>
        <a href="{% url 'app:catalog' %}" class="bg-primary hover:bg-primary/90 text-white px-6 py-2.5 rounded-lg font-semibold transition-all">
            Browse Catalog
        </a>
    </div>
    {% endif %}
</section>


<!-- Series Recommended for You -->
{% if recommended_series_by_genre %}
<section class="mb-12">
    <h2 class="text-xl font-bold text-slate-900 dark:text-white tracking-tight mb-6">Series Recommended for You</h2>
        <div class="relative w-full">
        <div class="flex gap-6 overflow-x-auto overflow-y-visible pb-4" 
                style="scrollbar-width: thin; 
                        overflow-x: scroll; 
                        overflow-y: visible;
                        -webkit-overflow-scrolling: touch;
                        white-space: nowrap;">
        {% for genre_name, series_list in recommended_series_by_genre.items %}
            {% for serie in series_list %}
            <div class="min-w-[200px] md:min-w-[240px] flex-shrink-0 group">
                <div class="aspect-[2/3] rounded-xl overflow-hidden relative shadow-md bg-surface-dark">
                    <img 
                        alt="{{ serie.title }}"
                        class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
                        src="https://via.placeholder.com/300x450?text=No+Image"
                    />
                    <div class="absolute top-2 right-2">
                        <span class="bg-primary text-white text-[10px] px-2 py-0.5 rounded shadow">{{ serie.platforms.0|default:"Series" }}</span>
                    </div>
                    <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
                        <a href="{% url 'app:content_detail' 'series' serie.unique_id %}" class="bg-primary text-white text-center text-xs font-bold py-2 rounded-lg hover:bg-primary/80 block">
                            Watch now
                        </a>
                    </div>
                </div>
                <div class="mt-3 px-1">
                    <h4 class="font-semibold text-slate-900 dark:text-white text-sm truncate group-hover:text-primary transition-colors">
                        <a href="{% url 'app:content_detail' 'series' serie.unique_id %}">{{ serie.title }}</a>
                    </h4>
                    <div class="flex items-center gap-2 mt-1">
                        <span class="text-xs text-slate-400">{{ serie.start_year|default:"—" }}</span>
                        <span class="w-1 h-1 bg-slate-500/40 rounded-full"></span>
                        <span class="text-xs text-slate-400 truncate">{{ serie.genre_name|default:"Unknown" }}</span>
                    </div>
                    {% if serie.rating %}
                    <div class="flex items-center gap-1 mt-1">
                        <span class="material-symbols-outlined text-amber-400 text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                        <span class="text-xs text-on-surface-variant">{{ serie.rating }}</span>
                    </div>
                    {% endif %}
                </div>
            </div>
            {% endfor %}
        {% endfor %}
    </div>
</section>
{% endif %}

<!-- Movies Recommended for You -->
{% if recommended_by_genre %}
<section class="mb-12 w-full">
    <h2 class="text-xl font-bold text-slate-900 dark:text-white tracking-tight mb-6">Movies Recommended for You</h2>
    
    <!-- Contenedor del scroll horizontal -->
    <div class="relative w-full">
        <div class="flex gap-6 overflow-x-auto overflow-y-visible pb-4" 
                style="scrollbar-width: thin; 
                        overflow-x: scroll; 
                        overflow-y: visible;
                        -webkit-overflow-scrolling: touch;
                        white-space: nowrap;">
                        
            {% for genre_name, movies_list in recommended_by_genre.items %}
                {% for movie in movies_list %}
                <div class="flex-shrink-0 w-[200px] md:w-[240px] group">
                    <div class="aspect-[2/3] rounded-xl overflow-hidden relative shadow-md bg-surface-dark">
                        <img 
                            alt="{{ movie.title }}" 
                            class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
                            src="{{'https://via.placeholder.com/300x450?text=No+Image'}}"
                            src='https://via.placeholder.com/300x450?text=No+Image'
                        />
                        
                        <div class="absolute top-2 right-2">
                            <span class="bg-primary text-white text-[10px] px-2 py-0.5 rounded shadow">
                                {{ movie.platforms.0|default:"Movie" }}
                            </span>
                        </div>
                        
                        <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
                            <a href="{% url 'app:content_detail' 'movie' movie.unique_id %}" 
                               class="bg-primary text-white text-center text-xs font-bold py-2 rounded-lg hover:bg-primary/80 block">
                                Watch now
                            </a>
                        </div>
                    </div>
                    
                    <div class="mt-3 px-1">
                        <h4 class="font-semibold text-slate-900 dark:text-white text-sm truncate group-hover:text-primary transition-colors">
                            <a href="{% url 'app:content_detail' 'movie' movie.unique_id %}">{{ movie.title }}</a>
                        </h4>
                        <div class="flex items-center gap-2 mt-1">
                            <span class="text-xs text-slate-400">{{ movie.year|default:"—" }}</span>
                            <span class="w-1 h-1 bg-slate-500/40 rounded-full"></span>
                            <span class="text-xs text-slate-400 truncate">{{ movie.genre_name|default:"Unknown" }}</span>
                        </div>
                        {% if movie.rating %}
                        <div class="flex items-center gap-1 mt-1">
                            <span class="material-symbols-outlined text-amber-400 text-sm" 
                                  style="font-variation-settings: 'FILL' 1;">star</span>
                            <span class="text-xs text-slate-400">{{ movie.rating }}</span>
                        </div>
                        {% endif %}
                    </div>
                </div>
                {% endfor %}
            {% endfor %}
        </div>
    </div>
</section>
{% endif %}

{% if not recommended_by_genre and not recommended_series_by_genre %}
<section class="mb-12">
    <h2 class="text-xl font-bold text-slate-900 dark:text-white tracking-tight mb-6">Recommended for You</h2>
    <div class="flex flex-col items-center justify-center py-12 bg-slate-100 dark:bg-surface-dark rounded-2xl">
        <span class="material-symbols-outlined text-5xl text-slate-400 mb-4">genre</span>
        <p class="text-slate-500 dark:text-slate-400">Complete your profile to get personalized recommendations</p>
        <a href="{% url 'app:onboarding_genres' %}" class="mt-4 bg-primary hover:bg-primary/90 text-white px-6 py-2.5 rounded-lg font-semibold transition-all">
            Select Genres
        </a>
    </div>
</section>
{% endif %}
<!-- Trending Now -->
{% if trending %}
<section class="mb-12">
    <div class="flex items-center justify-between mb-6">
        <h2 class="text-xl font-bold text-slate-900 dark:text-white tracking-tight">Trending Now</h2>
    </div>
    <div class="flex gap-4 overflow-x-auto no-scrollbar pb-4">
        {% for item in trending %}
        <div class="min-w-[200px] md:min-w-[240px] relative group cursor-pointer">
            <a href="{% url 'app:content_detail' item.content_type item.unique_id %}">
                <div class="aspect-video rounded-lg overflow-hidden relative shadow-sm bg-surface-dark">
                    {% if item.poster_url %}
                    <img alt="{{ item.title }}" class="w-full h-full object-cover transition-all duration-300 group-hover:scale-110 group-hover:brightness-50" src="{{ item.poster_url }}"/>
                    {% elif item.image_url %}
                    <img alt="{{ item.title }}" class="w-full h-full object-cover transition-all duration-300 group-hover:scale-110 group-hover:brightness-50" src="{{ item.image_url }}"/>
                    {% else %}
                    <div class="w-full h-full bg-gradient-to-br from-slate-700 to-slate-800 flex items-center justify-center">
                        <span class="material-symbols-outlined text-4xl text-slate-500">movie</span>
                    </div>
                    {% endif %}
                    <span class="absolute top-2 left-2 {% if forloop.counter == 1 %}bg-primary{% else %}bg-slate-700/80{% endif %} text-white text-[10px] font-bold px-1.5 py-0.5 rounded z-10">#{{ forloop.counter }}</span>
                    <span class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity z-20">
                        <span class="material-symbols-outlined text-white text-4xl drop-shadow-lg">play_circle</span>
                    </span>
                </div>
            </a>
            <div class="mt-2">
                <h4 class="text-slate-900 dark:text-white font-medium text-sm truncate">{{ item.title }}</h4>
                <p class="text-xs text-slate-500 dark:text-slate-400">{{ item.platforms.0|default:"Streaming" }} • {{ item.genre_name|default:"Movie" }}</p>
            </div>
        </div>
        {% endfor %}
    </div>
</section>
{% endif %}
<!-- New Releases (List Layout) -->
<section>
<div class="flex items-center justify-between mb-6">
<h2 class="text-xl font-bold text-slate-900 dark:text-white tracking-tight">New Releases</h2>
<a class="text-primary text-sm font-semibold hover:underline" href="#">View All</a>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
<!-- New Release Item 1 -->
<div class="flex gap-4 p-3 rounded-xl hover:bg-slate-100 dark:hover:bg-surface-dark transition-colors group cursor-pointer">
<div class="w-24 aspect-[2/3] rounded-lg overflow-hidden shrink-0 shadow-sm relative">
<img alt="Fantasy movie poster" class="w-full h-full object-cover" data-alt="Fantasy movie poster with mystical elements" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDO-VEkvvtIsG9LCguTWi-iqw4xpTSWspaKyHtdRz8_mNAgE9EeTpeXrMgCxwk48QrkGkdyx2CSaJOL0w3wBifG4fTKLzwnKm7NuAvlG7x0UG0eLcRqqPDjekhbD67LpI--LoJVGSofVWCJBYe8tFpTUjYaJPqSgIGwI4s9WJODh62cZz-uaXZiT4vj38BbKxvjdFR_GC15HywmtHVlVp7BZFa_UvoxMVl2byoX5g90Ot0IbJtaEk7pju5OS30IUrozviLLVc5MX-EM"/>
</div>
<div class="flex flex-col justify-center flex-1 min-w-0">
<div class="flex justify-between items-start mb-1">
<h4 class="text-slate-900 dark:text-white font-semibold truncate pr-2">The Witcher</h4>
<span class="text-xs text-slate-500 dark:text-slate-400 whitespace-nowrap">Today</span>
</div>
<p class="text-xs text-slate-500 dark:text-slate-400 mb-2">Season 3 • Episode 1</p>
<div class="flex items-center gap-2">
<span class="bg-[#E50914]/20 text-[#E50914] text-[10px] font-bold px-2 py-0.5 rounded border border-[#E50914]/20 uppercase">Netflix</span>
<span class="text-xs text-slate-400">• Fantasy</span>
</div>
</div>
<div class="flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
<span class="material-symbols-outlined text-primary text-3xl">play_circle</span>
</div>
</div>
<!-- New Release Item 2 -->
<div class="flex gap-4 p-3 rounded-xl hover:bg-slate-100 dark:hover:bg-surface-dark transition-colors group cursor-pointer">
<div class="w-24 aspect-[2/3] rounded-lg overflow-hidden shrink-0 shadow-sm relative">
<img alt="Sci-fi movie poster" class="w-full h-full object-cover" data-alt="Minimalist sci-fi movie poster" src="https://lh3.googleusercontent.com/aida-public/AB6AXuC0XQMaIvARlSTgtKRzpz_dtqEMbMP7lqbdv_HOrlaZTwAS5Z1xiEDfahbx31kfA3kzBviQfWFjEMn86vJbOPUbTwlfn3uOii2ZSt5-9TZ-wKyodP0Vt8tN4nvduvvJvP9C2jHfHy5TxB2RKb1GZNFt-5XoejKXPUiGt3IxMF2tXEKbe0bBWCb7Iyh--dYaO9bsl-EQI50jmO7cx5OmgOhAKytKSYaPqUXL1V3VEeGXBgOybrAUUT6iXGgPYa9QBIjqK9ivmu1kD1w4"/>
</div>
<div class="flex flex-col justify-center flex-1 min-w-0">
<div class="flex justify-between items-start mb-1">
<h4 class="text-slate-900 dark:text-white font-semibold truncate pr-2">Black Mirror</h4>
<span class="text-xs text-slate-500 dark:text-slate-400 whitespace-nowrap">Yesterday</span>
</div>
<p class="text-xs text-slate-500 dark:text-slate-400 mb-2">Season 6 • Full Release</p>
<div class="flex items-center gap-2">
<span class="bg-[#E50914]/20 text-[#E50914] text-[10px] font-bold px-2 py-0.5 rounded border border-[#E50914]/20 uppercase">Netflix</span>
<span class="text-xs text-slate-400">• Sci-Fi Anthology</span>
</div>
</div>
<div class="flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
<span class="material-symbols-outlined text-primary text-3xl">play_circle</span>
</div>
</div>
<!-- New Release Item 3 -->
<div class="flex gap-4 p-3 rounded-xl hover:bg-slate-100 dark:hover:bg-surface-dark transition-colors group cursor-pointer">
<div class="w-24 aspect-[2/3] rounded-lg overflow-hidden shrink-0 shadow-sm relative">
<img alt="Sports drama poster" class="w-full h-full object-cover" data-alt="Sports drama movie poster" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDTzWJDYjhPAXQj5iDWC4DMoDu6pqgFnhdInF8SMqZ3AhjLTnTyieIGnDoyhfyb5UZHBSNz9y-In5uL4zidA3KzeleVaLad98NPPG2oBtjOyY-QXTISOofEX0yrtRuETFQyr5y-ky1tSwsWxSLtJmfejslBk50r4RdSpHJ9_JDSF6IVtCk6eeD10NDPgpcXRTAl_I5DxwIXa2SL0jY22WSinjWFjQq7zcQ1qbWoQ4ABfBgWA3kL_QYWQ0SdvmqoTxu-DmlbzR94xB3b"/>
</div>
<div class="flex flex-col justify-center flex-1 min-w-0">
<div class="flex justify-between items-start mb-1">
<h4 class="text-slate-900 dark:text-white font-semibold truncate pr-2">Ted Lasso</h4>
<span class="text-xs text-slate-500 dark:text-slate-400 whitespace-nowrap">2 days ago</span>
</div>
<p class="text-xs text-slate-500 dark:text-slate-400 mb-2">Season 3 • Finale</p>
<div class="flex items-center gap-2">
<span class="bg-slate-200 dark:bg-white/20 text-slate-700 dark:text-white text-[10px] font-bold px-2 py-0.5 rounded border border-slate-300 dark:border-white/20 uppercase">Apple TV+</span>
<span class="text-xs text-slate-400">• Comedy</span>
</div>
</div>
<div class="flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
<span class="material-symbols-outlined text-primary text-3xl">play_circle</span>
</div>
</div>
</div>
</section>
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/movies.html -->
## app/templates/pages/movies.html

```html
{% extends "base/base.html" %}

{% block content %}

<div class="flex justify-between items-center mb-8">
    <h1 class="text-3xl font-bold">Movies</h1>
    <form method="GET" action="{% url 'app:movies' %}" class="flex flex-wrap gap-4 mb-8 p-4">
        {% include "components/platforms_filter.html" with selected_platform=selected_platform %}
    </form>
</div>

{% include "components/card_movies.html" with movies=movies %}

{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/personal_library.html -->
## app/templates/pages/personal_library.html

```html
{% extends "base/base.html" %}

{% block title %}Library · StreamSync{% endblock %}

{% block content %}

<main class="flex-1 px-4 lg:px-8 py-8">
  <div class="max-w-7xl mx-auto flex flex-col gap-10">

    <!-- HEADER -->
    <section class="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-6">
      <div class="space-y-3">
        <div class="flex items-center gap-3">
          <div class="size-12 rounded-2xl bg-primary/10 flex items-center justify-center text-primary">
            <span class="material-symbols-outlined text-[28px]">
              movie
            </span>
          </div>

          <div>
            <h1 class="text-4xl font-black tracking-tight text-white">
              Your Library
            </h1>

            <p class="text-text-secondary text-sm mt-1">
              Track what you're watching and organize your favorite titles.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- STATS -->
    <section class="grid grid-cols-2 lg:grid-cols-4 gap-4">

    {% with title="Continue Watching" value=watching_count icon="play_circle" icon_color="text-blue-400" %}
      {% include "components/stat_card.html" %}
    {% endwith %}

    {% with title="Completed" value=completed_count icon="check_circle" icon_color="text-emerald-400" %}
      {% include "components/stat_card.html" %}
    {% endwith %}

    {% with title="Favorites" value=favorites_count icon="favorite" icon_color="text-red-400 fill-current" %}
      {% include "components/stat_card.html" %}
    {% endwith %}

    {% with title="Lists" value="5" icon="stacks" icon_color="text-primary" %}
      {% include "components/stat_card.html" %}
    {% endwith %}

    </section>

    <!-- CONTINUE WATCHING -->
    <section class="flex flex-col gap-5">

      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-2xl font-bold text-white tracking-tight">
            Continue Watching
          </h2>

          <p class="text-sm text-text-secondary mt-1">
            Pick up where you left off.
          </p>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-5">

        <!-- CARD -->
        <div
          class="group rounded-3xl overflow-hidden bg-surface-dark border border-white/5 hover:border-primary/30 transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl hover:shadow-black/30"
        >

          <div class="flex">

            <div class="w-32 shrink-0 relative">

              <img
                src="https://lh3.googleusercontent.com/aida-public/AB6AXuAk67r9IkPtCHUUaj0QbHO_zhM9htuV23McSZwI-V6P4bP_DR86Pib2yH0e5OxmSCzyDpbbPE5s_lOB15ZkeaWL0Dund2MEra6wEJJPpAhEXCqz4bq2Wqmi4LibyGwgPSWvJ87q-K_l8MK_RabraXK1Rew3ColsIaSa3UfdkBHnVJ6Frhl-4sXuwX_uRMYZkbIoYyfjEzC3OaS3xsT_0MR8gWGZlTcJo8RrBxWnLB2BA2E646JDkbt_T6X6koQs57BDPTX_QLdCz1CK"
                class="w-full h-full object-cover"
              >

              <div class="absolute top-3 left-3">
                <span class="px-2 py-1 rounded-lg bg-blue-500/90 backdrop-blur-md text-white text-xs font-bold">
                  Watching
                </span>
              </div>

            </div>

            <div class="flex-1 p-5 flex flex-col justify-between">

              <div>

                <div class="flex items-start justify-between gap-3">

                  <div>
                    <h3 class="text-white font-bold text-xl leading-tight">
                      Succession
                    </h3>

                    <p class="text-sm text-text-secondary mt-1">
                      S4 · Episode 3
                    </p>
                  </div>

                  <button
                    class="size-9 rounded-xl bg-surface-highlight hover:bg-primary transition-colors text-white flex items-center justify-center"
                  >
                    <span class="material-symbols-outlined text-[18px]">
                      check
                    </span>
                  </button>

                </div>

              </div>

              <div class="space-y-3">

                <div class="w-full h-2 rounded-full bg-surface-highlight overflow-hidden">
                  <div class="w-2/3 h-full bg-primary rounded-full"></div>
                </div>

                <div class="flex items-center justify-between">
                  <span class="text-xs text-text-secondary">
                    67% completed
                  </span>

                  <span class="text-xs text-text-secondary">
                    In Favorites
                  </span>
                </div>

              </div>

            </div>

          </div>

        </div>

      </div>

    </section>

    <!-- FAVORITES -->
    <section class="flex flex-col gap-5">

      <div class="flex items-center justify-between">

        <div class="flex items-center gap-3">

          <div
            class="size-11 rounded-2xl bg-red-500/10 text-red-400 flex items-center justify-center"
          >
            <span class="material-symbols-outlined fill-current">
              favorite
            </span>
          </div>

          <div>
            <h2 class="text-2xl font-bold text-white tracking-tight">
              Favorites
            </h2>

            <p class="text-sm text-text-secondary mt-1">
              Your all-time favorite titles.
            </p>
          </div>

        </div>

      </div>

      <div
        class="rounded-3xl border border-red-500/20 bg-gradient-to-br from-red-500/10 to-transparent p-6"
      >

        {% if favorite_movies %}
          {% include "components/card_movies.html" with movies=favorite_movies %}
        {% endif %}

        {% if favorite_series %}
          {% include "components/card_series.html" with series=favorite_series %}
        {% endif %}

        {% if not favorite_movies and not favorite_series %}
          <p class="text-text-secondary text-center py-8">No favorites yet. Start adding your favorite titles!</p>
        {% endif %}

      </div>

    </section>

    <!-- CUSTOM LISTS -->
    <section class="flex flex-col gap-5">

      <div class="flex items-center justify-between">

        <div>
          <h2 class="text-2xl font-bold text-white tracking-tight">
            Your Lists
          </h2>

          <p class="text-sm text-text-secondary mt-1">
            Personal collections created by you.
          </p>
        </div>

        <button
          class="h-10 px-4 rounded-xl border border-white/10 bg-surface-dark hover:bg-surface-highlight text-white text-sm font-semibold transition-all"
        >
          New List
        </button>

      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">

        <!-- LIST CARD -->
        <div
          class="group rounded-3xl bg-surface-dark border border-white/5 hover:border-primary/30 transition-all duration-300 p-5 flex flex-col gap-5 hover:-translate-y-1"
        >

          <div class="flex items-center justify-between">

            <div class="flex items-center gap-3">

              <div
                class="size-12 rounded-2xl bg-primary/10 text-primary flex items-center justify-center"
              >
                <span class="material-symbols-outlined">
                  stacks
                </span>
              </div>

              <div>
                <h3 class="text-white font-bold">
                  Weekend Binge
                </h3>

                <p class="text-xs text-text-secondary mt-1">
                  8 titles
                </p>
              </div>

            </div>

            <span class="material-symbols-outlined text-text-secondary">
              chevron_right
            </span>

          </div>

          <div class="flex -space-x-4">

            <div class="size-20 rounded-xl overflow-hidden border-2 border-surface-dark">
              <img
                src="https://lh3.googleusercontent.com/aida-public/AB6AXuDW5XoUJIvkRuZ2SukHriq6IfI0bDKHMu3EGRtlHS7-5W1gdCfjNxThLWbLzxEHoJKj8sBCc_rlVjR2DxFGUfKW40rTAl-5JLHYAyVCK3KUXDaEHUNiuMJRZnVjVF7UQP-iKGJn4WMuYBEXGClpWXBKD5zyIs1t1gdgYjcvpDuznVmsdpL427OmCFVM8fCLEwo_tnIwzQdTBGhfVC9dyflDVfa_hKBauna9Gzo0Zudq5Kc5IiG0Oi8mlrAKyK4-MyVmDptABtLOoZ36"
                class="w-full h-full object-cover"
              >
            </div>

            <div class="size-20 rounded-xl overflow-hidden border-2 border-surface-dark">
              <img
                src="https://lh3.googleusercontent.com/aida-public/AB6AXuAk67r9IkPtCHUUaj0QbHO_zhM9htuV23McSZwI-V6P4bP_DR86Pib2yH0e5OxmSCzyDpbbPE5s_lOB15ZkeaWL0Dund2MEra6wEJJPpAhEXCqz4bq2Wqmi4LibyGwgPSWvJ87q-K_l8MK_RabraXK1Rew3ColsIaSa3UfdkBHnVJ6Frhl-4sXuwX_uRMYZkbIoYyfjEzC3OaS3xsT_0MR8gWGZlTcJo8RrBxWnLB2BA2E646JDkbt_T6X6koQs57BDPTX_QLdCz1CK"
                class="w-full h-full object-cover"
              >
            </div>

            <div
              class="size-20 rounded-xl border-2 border-surface-dark bg-surface-highlight flex items-center justify-center text-white font-bold text-sm"
            >
              +6
            </div>

          </div>

        </div>

      </div>

    </section>

    

  </div>
</main>

{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/search.html -->
## app/templates/pages/search.html

```html
{% extends "base/base.html" %}
{% load static %}

{% block title %}Search — StreamSync{% endblock %}

{% block content %}

<!-- ── Search Header ─────────────────────────────────────────────────────── -->
<header class="mb-10 mt-2">
    {% if query %}
        <p class="text-on-surface-variant text-xs uppercase tracking-widest font-bold mb-2">Search Results for</p>
        <h1 class="text-3xl md:text-4xl font-bold tracking-tight mb-2">"{{ query }}"</h1>
        {% if result_count %}
            <p class="text-on-surface-variant text-sm">
                {{ result_count }} result{{ result_count|pluralize }} found across your connected platforms.
            </p>
        {% endif %}
    {% else %}
        <h1 class="text-3xl md:text-4xl font-bold tracking-tight mb-2">Search</h1>
        <p class="text-on-surface-variant text-sm">Type in the search bar to find movies and TV shows.</p>
    {% endif %}
</header>

<!-- ── Filter Bar ────────────────────────────────────────────────────────── -->
<form method="GET" action="{% url 'app:search' %}" class="flex flex-wrap gap-4 mb-8 p-4 bg-surface-dark rounded-xl border border-white/5">
    
    <input type="hidden" name="q" value="{{ query }}">
    
    {% include "components/platforms_filter.html" with selected_platform=selected_platform selected_genre=selected_genre %}

    <button type="submit" class="bg-primary px-4 py-2 rounded-lg text-sm font-bold text-white hover:bg-blue-600 transition-colors">
        Aplicar Filtros
    </button>
</form>

<!-- ── Results Grid ─────────────────────────────────────────────────────── -->
{% if query %}
    {% if movies or series %}
        {% if movies %}
            {% include "components/card_movies.html" with movies=movies %}
        {% endif %}

        {% if series %}
            {% include "components/card_series.html" with series=series %}
        {% endif %}
    {% else %}
        <!-- No results -->
        <div class="text-center py-16">
            <div class="inline-flex items-center justify-center w-20 h-20 rounded-full bg-surface-dark mb-6">
                <span class="material-symbols-outlined text-slate-500 text-4xl">search_off</span>
            </div>
            <h2 class="text-2xl font-bold mb-2">No results for "{{ query }}"</h2>
            <p class="text-slate-400 text-sm mb-2">Try another search term or check the spelling.</p>
        </div>

        {% if suggestions %}
            <div class="mt-8">
                <div class="flex items-center gap-3 mb-6">
                    <div class="h-px flex-1 bg-slate-800"></div>
                    <p class="text-slate-500 text-xs uppercase tracking-widest font-bold px-2">You might like</p>
                    <div class="h-px flex-1 bg-slate-800"></div>
                </div>
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-6 max-w-2xl mx-auto">
                    {% for item in suggestions %}
                        <div class="group relative flex flex-col gap-3 transition-all duration-500 hover:scale-105">
                            <div class="aspect-[2/3] rounded-xl overflow-hidden bg-surface-dark relative cinematic-shadow">
                                <div class="w-full h-full flex items-center justify-center">
                                    <span class="material-symbols-outlined text-slate-700 text-6xl">
                                        {% if item.content_type == "series" %}live_tv{% else %}movie{% endif %}
                                    </span>
                                </div>
                                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
                                    <button class="bg-primary text-white text-xs font-bold py-2 rounded-lg">Watch now</button>
                                </div>
                            </div>
                            <div class="px-1">
                                <h3 class="font-bold text-sm truncate">{{ item.title }}</h3>
                                <p class="text-xs text-slate-500">{{ item.year|default:item.start_year }}</p>
                            </div>
                        </div>
                    {% endfor %}
                </div>
            </div>
        {% endif %}
    {% endif %}
{% endif %}

{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/series.html -->
## app/templates/pages/series.html

```html
{% extends "base/base.html" %}
{% block content %}

<div class="flex justify-between items-center mb-8">
    <h1 class="text-3xl font-bold">Series</h1>
    <form method="GET" action="{% url 'app:series' %}" class="flex flex-wrap gap-4 mb-8 p-4">
        {% include "components/platforms_filter.html" with selected_platform=selected_platform %}
    </form>
</div>
{% include "components/card_series.html" with series=series %}
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/user_settings.html -->
## app/templates/pages/user_settings.html

```html
{% extends "base/base.html" %}

{% block title %}StreamSync Dashboard{% endblock %}

{% block content %}

<main class="flex-1 flex flex-col">

    <!-- HERO -->
    <section class="relative w-full h-[320px] overflow-hidden rounded-3xl group">

        <div class="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105"
             style='background-image:url("https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?q=80&w=2069&auto=format&fit=crop")'>
        </div>

        <div class="absolute inset-0 bg-gradient-to-t from-background-dark via-background-dark/40"></div>

        <!-- COVER EDIT -->
        <button class="absolute top-5 right-5 p-3 bg-black/40 backdrop-blur-md rounded-2xl text-white opacity-0 group-hover:opacity-100 transition-all hover:scale-105">
            <span class="material-symbols-outlined">edit_square</span>
        </button>

        <div class="relative max-w-7xl mx-auto px-6 h-full flex items-end pb-12">

            <div class="flex flex-col md:flex-row items-end gap-6">

                <!-- PROFILE -->
                <div class="relative group/avatar">

                    <img
                        class="w-32 h-32 md:w-40 md:h-40 rounded-3xl border-4 border-background-dark object-cover shadow-2xl"
                        src="{% if user.profile_picture %}{{ user.profile_picture.url }}{% else %}https://randomuser.me/api/portraits/men/32.jpg{% endif %}"
                        id="profile-preview"/>

                    <label
                        for="avatar-upload"
                        class="absolute inset-0 flex items-center justify-center bg-black/60 rounded-3xl opacity-0 group-hover/avatar:opacity-100 transition-all cursor-pointer">

                        <span class="material-symbols-outlined text-white text-3xl">
                            add_a_photo
                        </span>

                        <input
                            type="file"
                            id="avatar-upload"
                            class="hidden"
                            accept="image/*"
                            onchange="previewImage(event)">
                    </label>

                </div>

                <!-- INFO -->
                <div class="mb-2">

                    <h2 class="text-4xl font-bold text-white">
                        {{ user.first_name }} {{ user.last_name }}
                    </h2>

                    <p class="text-on-surface-variant flex items-center gap-2 mt-2">
                        <span class="size-2 bg-green-500 rounded-full"></span>
                        @{{ user.username }}
                    </p>

                </div>

            </div>

        </div>

    </section>

    <!-- CONTENT -->
    <section class="max-w-7xl mx-auto px-6 py-12 w-full">

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">

            <!-- LEFT -->
            <div class="lg:col-span-8 space-y-6">

                <!-- ACCOUNT SETTINGS -->
                <form method="POST" enctype="multipart/form-data" class="block">
                    {% csrf_token %}

                    {% if errors %}
                    <div class="mb-6 p-4 bg-red-500/20 border border-red-500 rounded-2xl">
                        {% for error in errors %}
                        <p class="text-red-400 text-sm">{{ error }}</p>
                        {% endfor %}
                    </div>
                    {% endif %}

                    {% if success %}
                    <div class="mb-6 p-4 bg-green-500/20 border border-green-500 rounded-2xl">
                        <p class="text-green-400 text-sm">{{ success }}</p>
                    </div>
                    {% endif %}

                    <div class="bg-surface-container-low rounded-3xl border border-outline-variant overflow-hidden shadow-xl">

                        <!-- HEADER -->
                        <div class="flex items-center justify-between px-8 py-6 border-b border-outline-variant">

                            <div>
                                <h3 class="text-2xl font-bold">
                                    Account Settings
                                </h3>

                                <p class="text-sm text-on-surface-variant mt-1">
                                    Manage your profile information and preferences.
                                </p>
                            </div>

                            <!-- EDIT BTN -->
                            <button
                                type="button"
                                id="edit-profile-btn"
                                onclick="toggleEditProfile()"
                                class="flex items-center gap-2 px-5 py-3 rounded-2xl bg-background-dark border border-outline-variant hover:border-primary hover:bg-surface-container-high transition-all group">

                                <span class="material-symbols-outlined text-[20px] group-hover:text-primary transition-colors">
                                    edit
                                </span>

                                <span class="font-medium">
                                    Edit Profile
                                </span>

                            </button>

                        </div>

                        <!-- BODY -->
                        <div class="p-8">

                            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">

                                <!-- FIRST NAME -->
                                <div class="space-y-2">

                                    <label class="text-sm text-on-surface-variant">
                                        First Name
                                    </label>

                                    <input
                                        disabled
                                        type="text"
                                        name="first_name"
                                        class="profile-field w-full p-4 rounded-2xl bg-background-dark/60 border border-outline-variant text-on-surface-variant cursor-not-allowed transition-all"
                                        value="{{ user.first_name|default:'' }}"/>

                                </div>

                                <!-- LAST NAME -->
                                <div class="space-y-2">

                                    <label class="text-sm text-on-surface-variant">
                                        Last Name
                                    </label>

                                    <input
                                        disabled
                                        type="text"
                                        name="last_name"
                                        class="profile-field w-full p-4 rounded-2xl bg-background-dark/60 border border-outline-variant text-on-surface-variant cursor-not-allowed transition-all"
                                        value="{{ user.last_name|default:'' }}"/>

                                </div>

                                <!-- USERNAME -->
                                <div class="space-y-2">

                                    <label class="text-sm text-on-surface-variant">
                                        Username
                                    </label>

                                    <input
                                        disabled
                                        type="text"
                                        name="username"
                                        class="profile-field w-full p-4 rounded-2xl bg-background-dark/60 border border-outline-variant text-on-surface-variant cursor-not-allowed transition-all"
                                        value="{{ user.username }}"/>

                                </div>

                                <!-- COUNTRY -->
                                <div class="space-y-2">

                                    <label class="text-sm text-on-surface-variant">
                                        Country
                                    </label>

                                    <select
                                        disabled
                                        name="country"
                                        class="profile-field w-full p-4 rounded-2xl bg-background-dark/60 border border-outline-variant text-on-surface-variant cursor-not-allowed appearance-none transition-all">

                                    {% for country in countries %}
                                    <option value="{{ country.id }}" {% if user.country_id == country.id %}selected{% endif %}>
                                        {{ country.name }}
                                    </option>
                                    {% endfor %}

                                </select>

                            </div>

                            <!-- GENDER -->
                            <div class="space-y-2 md:col-span-2">

                                <label class="text-sm text-on-surface-variant">
                                    Gender
                                </label>

                                <input type="hidden" name="gender" id="selected-gender" value="{{ user.gender|default:'' }}">

                                <div class="grid grid-cols-2 md:grid-cols-4 gap-3">

                                    <button type="button" onclick="selectGender('male')" class="gender-btn p-3 rounded-2xl {% if user.gender == 'male' %}bg-primary text-white{% else %}bg-background-dark border border-outline-variant text-on-surface-variant opacity-70{% endif %} font-medium cursor-not-allowed transition-all">
                                        Male
                                    </button>

                                    <button type="button" onclick="selectGender('female')" class="gender-btn p-3 rounded-2xl {% if user.gender == 'female' %}bg-primary text-white{% else %}bg-background-dark border border-outline-variant text-on-surface-variant opacity-70{% endif %} font-medium cursor-not-allowed transition-all">
                                        Female
                                    </button>

                                    <button type="button" onclick="selectGender('non-binary')" class="gender-btn p-3 rounded-2xl {% if user.gender == 'non-binary' %}bg-primary text-white{% else %}bg-background-dark border border-outline-variant text-on-surface-variant opacity-70{% endif %} font-medium cursor-not-allowed transition-all">
                                        Non-binary
                                    </button>

                                    <button type="button" onclick="selectGender('other')" class="gender-btn p-3 rounded-2xl {% if user.gender == 'other' %}bg-primary text-white{% else %}bg-background-dark border border-outline-variant text-on-surface-variant opacity-70{% endif %} font-medium cursor-not-allowed transition-all">
                                        Other
                                    </button>

                                </div>

                            </div>

                        </div>

                        <!-- BIO -->
                        <div class="space-y-2 mb-8">

                            <label class="text-sm text-on-surface-variant">
                                Bio
                            </label>

                            <textarea
                                rows="4"
                                disabled
                                name="bio"
                                class="profile-field w-full p-4 rounded-2xl bg-background-dark/60 border border-outline-variant text-on-surface-variant cursor-not-allowed resize-none transition-all"
                            >{{ user.bio|default:'' }}</textarea>

                        </div>

                        <!-- ACTIONS -->
                        <div
                            id="profile-actions"
                            class="hidden opacity-0 translate-y-3 flex justify-end gap-4 transition-all duration-300">

                            <button
                                type="button"
                                onclick="cancelProfileEdit()"
                                class="px-6 py-3 text-on-surface-variant hover:text-white transition-colors">

                                Cancel

                            </button>

                            <button
                                type="submit"
                                class="px-8 py-3 bg-primary hover:bg-blue-600 text-white rounded-2xl font-bold shadow-lg shadow-primary/20 transition-all">

                                Save Changes

                            </button>

                        </div>

                    </div>

                    </div>

                </form>

                <!-- SECURITY -->
                <form method="POST" class="block">
                    {% csrf_token %}

                    {% if password_errors %}
                    <div class="mb-6 p-4 bg-red-500/20 border border-red-500 rounded-2xl">
                        {% for error in password_errors %}
                        <p class="text-red-400 text-sm">{{ error }}</p>
                        {% endfor %}
                    </div>
                    {% endif %}

                    {% if password_success %}
                    <div class="mb-6 p-4 bg-green-500/20 border border-green-500 rounded-2xl">
                        <p class="text-green-400 text-sm">{{ password_success }}</p>
                    </div>
                    {% endif %}

                    <div class="bg-surface-container-low rounded-3xl border border-outline-variant overflow-hidden shadow-xl">

                        <!-- HEADER -->
                        <div class="flex items-center justify-between px-8 py-6 border-b border-outline-variant">

                            <div>

                                <h3 class="text-2xl font-bold">
                                    Security
                                </h3>

                                <p class="text-sm text-on-surface-variant mt-1">
                                    Manage your password and security preferences.
                                </p>

                            </div>

                            <!-- SECURITY BTN -->
                            <button
                                type="button"
                                onclick="toggleSecurityEdit()"
                                class="flex items-center gap-2 px-5 py-3 rounded-2xl bg-background-dark border border-outline-variant hover:border-primary hover:bg-surface-container-high transition-all group">

                                <span class="material-symbols-outlined text-[20px] group-hover:text-primary transition-colors">
                                    lock_reset
                                </span>

                                <span class="font-medium">
                                    Change Password
                                </span>

                            </button>

                        </div>

                        <!-- BODY -->
                        <div class="p-8 space-y-5">

                            <!-- CURRENT -->
                            <div class="space-y-2">

                                <label class="text-sm text-on-surface-variant">
                                    Current Password
                                </label>

                                <input
                                    disabled
                                    type="password"
                                    name="current_password"
                                    placeholder="••••••••••••"
                                    class="security-field w-full p-4 rounded-2xl bg-background-dark/60 border border-outline-variant text-on-surface-variant cursor-not-allowed transition-all"/>

                            </div>

                            <!-- NEW -->
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

                                <div class="space-y-2">

                                    <label class="text-sm text-on-surface-variant">
                                        New Password
                                    </label>

                                    <input
                                        disabled
                                        type="password"
                                        name="new_password"
                                        placeholder="Enter new password"
                                        class="security-field w-full p-4 rounded-2xl bg-background-dark/60 border border-outline-variant text-on-surface-variant cursor-not-allowed transition-all"/>

                                </div>

                                <div class="space-y-2">

                                    <label class="text-sm text-on-surface-variant">
                                        Confirm Password
                                    </label>

                                    <input
                                        disabled
                                        type="password"
                                        name="confirm_password"
                                        placeholder="Confirm new password"
                                        class="security-field w-full p-4 rounded-2xl bg-background-dark/60 border border-outline-variant text-on-surface-variant cursor-not-allowed transition-all"/>

                                    <div id="password-match" class="text-[11px] text-on-surface-variant mt-2 hidden">
                                        <span id="match-icon"></span> <span id="match-text"></span>
                                    </div>

                                </div>

                            </div>

                            <!-- PASSWORD FEEDBACK -->
                            <div id="password-feedback" class="space-y-1 mt-2">
                                <p class="text-[11px] text-on-surface-variant">
                                    <span id="length-check">○</span> At least 8 characters
                                </p>
                                <p class="text-[11px] text-on-surface-variant">
                                    <span id="common-check">○</span> Not a commonly used password
                                </p>
                                <p class="text-[11px] text-on-surface-variant">
                                    <span id="number-check">○</span> Not entirely numeric
                                </p>
                            </div>

                            <!-- ACTIONS -->
                            <div
                                id="security-actions"
                                class="hidden opacity-0 translate-y-3 flex items-center justify-between pt-2 transition-all duration-300">

                                <a
                                    href="#"
                                    class="text-sm text-primary hover:underline">

                                    Forgot your password?

                                </a>

                                <button
                                    type="submit"
                                    name="action"
                                    value="change_password"
                                    class="px-8 py-3 bg-white text-black rounded-2xl font-bold hover:bg-slate-200 transition-all">

                                    Update Password

                                </button>

                            </div>

                        </div>

                    </div>

                </form>

            </div>

            <!-- RIGHT -->
            <div class="lg:col-span-4 space-y-6">

                <!-- ACTIVITY -->
                <div class="bg-surface-container-low p-6 rounded-3xl border border-outline-variant shadow-xl">

                    <h4 class="font-bold mb-5 flex items-center gap-2">

                        <span class="material-symbols-outlined text-primary">
                            analytics
                        </span>

                        Your Activity

                    </h4>

                    <div class="grid grid-cols-2 gap-4">

                        <div class="p-5 bg-background-dark rounded-2xl border border-outline-variant text-center">

                            <p class="text-3xl font-bold">
                                142
                            </p>

                            <p class="text-[10px] uppercase tracking-wider text-on-surface-variant mt-1">
                                Watched
                            </p>

                        </div>

                        <div class="p-5 bg-background-dark rounded-2xl border border-outline-variant text-center">

                            <p class="text-3xl font-bold">
                                24
                            </p>

                            <p class="text-[10px] uppercase tracking-wider text-on-surface-variant mt-1">
                                Reviews
                            </p>

                        </div>

                    </div>

                </div>

                <!-- DELETE ACCOUNT -->
                <div class="bg-surface-container-low p-6 rounded-3xl border border-outline-variant shadow-xl">

                    <h4 class="font-bold mb-5 flex items-center gap-2 text-red-500">

                        <span class="material-symbols-outlined text-red-500">
                            delete_forever
                        </span>

                        Danger Zone

                    </h4>

                    <p class="text-sm text-on-surface-variant mb-5">
                        Once you delete your account, there is no going back. Please be certain.
                    </p>

                    <button type="button" onclick="showDeleteModal()"
                            class="w-full px-6 py-3 bg-red-600 hover:bg-red-700 text-white rounded-2xl font-bold transition-all flex items-center justify-center gap-2">
                        <span class="material-symbols-outlined text-[20px]">delete</span>
                        Delete Account
                    </button>

                </div>

                <!-- DELETE MODAL -->
                <div id="deleteModal" class="fixed inset-0 z-50 flex items-center justify-center hidden">

                    <div class="fixed inset-0 bg-black/60 backdrop-blur-sm" onclick="closeDeleteModal()"></div>

                    <div class="relative bg-surface-container-low p-8 rounded-3xl border border-outline-variant shadow-2xl max-w-md w-full mx-4 opacity-0 scale-95 transition-all duration-200">

                        <div class="text-center mb-6">
                            <span class="material-symbols-outlined text-6xl text-red-500">delete_forever</span>
                        </div>

                        <h3 class="text-2xl font-bold text-center mb-2">Delete Account</h3>

                        <p class="text-sm text-on-surface-variant text-center mb-8">
                            Are you sure you want to delete your account? This action cannot be undone.
                            All your data will be permanently removed.
                        </p>

                        <form method="POST" action="{% url 'app:delete_account' %}">
                            {% csrf_token %}
                            <div class="flex gap-4">
                                <button type="button" onclick="closeDeleteModal()"
                                        class="flex-1 px-6 py-3 rounded-2xl border border-outline-variant text-on-surface-variant hover:text-white transition-all font-medium">
                                    Cancel
                                </button>
                                <button type="submit"
                                        class="flex-1 px-6 py-3 bg-red-600 hover:bg-red-700 text-white rounded-2xl font-bold transition-all">
                                    Yes, delete my account
                                </button>
                            </div>
                        </form>

                    </div>

                </div>

            </div>

        </div>

    </section>

</main>

<script>

function previewImage(event) {

    const reader = new FileReader();

    reader.onload = function() {

        const output = document.getElementById('profile-preview');
        output.src = reader.result;
    };

    reader.readAsDataURL(event.target.files[0]);
}

let isEditing = false;

function toggleEditProfile() {
    isEditing = !isEditing;

    const fields = document.querySelectorAll('.profile-field');
    const actions = document.getElementById('profile-actions');
    const genderBtns = document.querySelectorAll('.gender-btn');
    const editBtn = document.getElementById('edit-profile-btn');

    fields.forEach(field => {
        field.disabled = !field.disabled;

        if (!field.disabled) {
            field.classList.remove(
                'cursor-not-allowed',
                'bg-background-dark/60',
                'opacity-70'
            );
            field.classList.add(
                'focus:ring-2',
                'focus:ring-primary/50',
                'bg-background-dark'
            );
        } else {
            field.classList.add(
                'cursor-not-allowed',
                'bg-background-dark/60'
            );
        }
    });

    genderBtns.forEach(btn => {
        if (isEditing) {
            btn.classList.remove('cursor-not-allowed', 'opacity-70');
            btn.classList.add('hover:scale-105', 'hover:border-primary');
        } else {
            btn.classList.add('cursor-not-allowed', 'opacity-70');
            btn.classList.remove('hover:scale-105', 'hover:border-primary');
        }
    });

    editBtn.querySelector('span:last-child').textContent = isEditing ? 'Cancel' : 'Edit Profile';

    actions.classList.toggle('hidden');

    setTimeout(() => {
        actions.classList.toggle('opacity-0');
        actions.classList.toggle('translate-y-3');
    }, 10);
}

function selectGender(gender) {
    if (!isEditing) return;

    document.getElementById('selected-gender').value = gender;

    document.querySelectorAll('.gender-btn').forEach(btn => {
        btn.classList.remove('bg-primary', 'text-white');
        btn.classList.add('bg-background-dark', 'border', 'border-outline-variant', 'text-on-surface-variant', 'opacity-70');
    });

    event.target.classList.remove('bg-background-dark', 'border', 'border-outline-variant', 'text-on-surface-variant', 'opacity-70');
    event.target.classList.add('bg-primary', 'text-white');
}

function toggleSecurityEdit() {

    const fields = document.querySelectorAll('.security-field');
    const actions = document.getElementById('security-actions');

    fields.forEach(field => {

        field.disabled = !field.disabled;

        if (!field.disabled) {

            field.classList.remove(
                'cursor-not-allowed',
                'bg-background-dark/60'
            );

            field.classList.add(
                'focus:ring-2',
                'focus:ring-primary/50',
                'bg-background-dark'
            );

        } else {

            field.classList.add(
                'cursor-not-allowed',
                'bg-background-dark/60'
            );
        }
    });

    actions.classList.toggle('hidden');

    setTimeout(() => {

        actions.classList.toggle('opacity-0');
        actions.classList.toggle('translate-y-3');

    }, 10);
}

function cancelProfileEdit() {
    if (isEditing) {
        location.reload();
    }
}

const commonPasswords = [
    'password', '12345678', '123456789', 'qwerty', 'abc123', 'password1',
    '1234567', 'password123', 'welcome', 'hello', 'admin', 'letmein',
    'sunshine', 'princess', 'football', 'monkey', 'dragon'
];

function validateNewPassword() {
    const newPassword = document.querySelector('input[name="new_password"]');
    if (!newPassword) return;

    const pwd = newPassword.value;
    const lengthCheck = document.getElementById('length-check');
    const commonCheck = document.getElementById('common-check');
    const numberCheck = document.getElementById('number-check');

    if (pwd.length >= 8) {
        lengthCheck.textContent = '✓';
        lengthCheck.className = 'text-green-500';
    } else {
        lengthCheck.textContent = '○';
        lengthCheck.className = 'text-on-surface-variant';
    }

    if (!commonPasswords.includes(pwd.toLowerCase())) {
        commonCheck.textContent = '✓';
        commonCheck.className = 'text-green-500';
    } else {
        commonCheck.textContent = '○';
        commonCheck.className = 'text-on-surface-variant';
    }

    if (!/^\d+$/.test(pwd)) {
        numberCheck.textContent = '✓';
        numberCheck.className = 'text-green-500';
    } else {
        numberCheck.textContent = '○';
        numberCheck.className = 'text-on-surface-variant';
    }
}

function validateConfirmPassword() {
    const newPassword = document.querySelector('input[name="new_password"]');
    const confirmPassword = document.querySelector('input[name="confirm_password"]');
    if (!newPassword || !confirmPassword) return;

    const pwd1 = newPassword.value;
    const pwd2 = confirmPassword.value;
    const matchDiv = document.getElementById('password-match');
    const matchIcon = document.getElementById('match-icon');
    const matchText = document.getElementById('match-text');

    if (pwd2.length === 0) {
        matchDiv.classList.add('hidden');
        return;
    }

    matchDiv.classList.remove('hidden');

    if (pwd1 === pwd2 && pwd1.length > 0) {
        matchIcon.textContent = '✓';
        matchText.textContent = 'Passwords match';
        matchIcon.className = 'text-green-500';
        matchText.className = 'text-green-500';
    } else {
        matchIcon.textContent = '✗';
        matchText.textContent = 'Passwords do not match';
        matchIcon.className = 'text-red-500';
        matchText.className = 'text-red-500';
    }
}

document.querySelectorAll('.security-field').forEach(field => {
    field.addEventListener('input', function() {
        if (this.name === 'new_password') {
            validateNewPassword();
        } else if (this.name === 'confirm_password') {
            validateConfirmPassword();
        }
    });
});

function showDeleteModal() {
    const modal = document.getElementById('deleteModal');
    modal.classList.remove('hidden');
    setTimeout(() => {
        modal.querySelector('div.relative').classList.remove('opacity-0', 'scale-95');
        modal.querySelector('div.relative').classList.add('opacity-100', 'scale-100');
    }, 10);
}

function closeDeleteModal() {
    const card = document.querySelector('#deleteModal div.relative');
    card.classList.remove('opacity-100', 'scale-100');
    card.classList.add('opacity-0', 'scale-95');
    setTimeout(() => document.getElementById('deleteModal').classList.add('hidden'), 200);
}

</script>

{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/registration/login.html -->
## app/templates/registration/login.html

```html
{% extends "base/initial.html" %}

{% block content %}
<style>
    .glass-panel {
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        background: rgba(16, 22, 35, 0.6);
    }
</style>

<div class="bg-background-light dark:bg-background-dark font-display text-slate-900 dark:text-slate-100 min-h-screen flex flex-col">
    <div class="relative min-h-screen w-full flex items-center justify-center cinematic-bg overflow-hidden">

        <div class="z-10 w-full max-w-[540px] px-8 py-12">
            <div class="flex flex-col items-center mb-10">
                <div class="flex items-center gap-4 mb-4">
                    <h1 class="text-4xl font-bold tracking-tight">Login to StreamSync</h1> </div>
                <p class="text-slate-400 text-center text-lg">Enter your credentials to continue</p>
            </div>

            <div class="glass-panel rounded-2xl p-10 shadow-2xl"> {% if form.errors %}
                <div class="mb-6 flex items-center gap-3 bg-red-500/10 border border-red-500/20 p-4 rounded-lg text-red-400 text-base">
                    <span class="material-symbols-outlined text-xl">error</span>
                    <span>Invalid username or password.</span>
                </div>
                {% endif %}

                <form method="post" class="space-y-6"> {% csrf_token %}

                    <div>
                        <label class="block text-base font-medium text-slate-300 mb-2" for="id_username">Username or Email</label>
                        <input name="username" id="id_username" required
                               class="w-full bg-slate-900/50 border border-slate-700 rounded-lg h-14 px-5 text-lg text-slate-100 focus:ring-2 focus:ring-primary focus:border-transparent transition-all placeholder:text-slate-600"
                               placeholder="name@example.com" type="text" />
                    </div>

                    <div>
                        <div class="flex justify-between items-center mb-2">
                            <label class="text-base font-medium text-slate-300" for="id_password">Password</label>
                            <a class="text-sm text-primary hover:underline font-medium" href="#">Forgot password?</a>
                        </div>
                        <div class="relative">
                            <input name="password" id="id_password" required
                                   class="w-full bg-slate-900/50 border border-slate-700 rounded-lg h-14 px-5 pr-12 text-lg text-slate-100 focus:ring-2 focus:ring-primary focus:border-transparent transition-all placeholder:text-slate-600"
                                   placeholder="Enter your password" type="password" />
                        </div>
                    </div>

                    <div class="pt-2">
                        <button class="w-full bg-primary hover:bg-primary/90 text-white font-bold py-4 px-6 rounded-lg shadow-lg shadow-primary/20 transition-all flex items-center justify-center gap-3 group text-xl" type="submit">
                            Sign In
                            <span class="material-symbols-outlined text-2xl transition-transform">arrow_forward</span>
                        </button>
                    </div>
                </form>

                <div class="mt-10 pt-8 border-t border-slate-800/50 flex flex-col items-center gap-5">
                    <p class="text-base text-slate-400">
                        Don't have an account?
                        <a class="text-primary font-semibold hover:text-blue-400 ml-1" href="{% url 'signup' %}">Register here</a>
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/registration/onboarding_complete.html -->
## app/templates/registration/onboarding_complete.html

```html
{% extends "base/initial.html" %} {% block content %}
<div class="flex items-center justify-center min-h-[calc(100vh-80px)] bg-slate-50 dark:bg-background-dark px-4 py-8">
    <div class="max-w-lg w-full text-center">
        <div class="w-20 h-20 bg-green-100 dark:bg-green-900/30 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-10 h-10 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
            </svg>
        </div>
        
        <h2 class="text-3xl font-bold text-slate-900 dark:text-white mb-4">You're All Set!</h2>
        <p class="text-slate-500 dark:text-slate-400 mb-8">Your profile has been created successfully. Time to start watching!</p>
        
        <a href="{% url 'app:main' %}" class="inline-block bg-primary hover:bg-primary/90 text-white font-bold py-3 px-8 rounded-xl transition-all shadow-lg shadow-primary/20">
            Go to Main
        </a>
    </div>
</div>
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/registration/onboarding_genres.html -->
## app/templates/registration/onboarding_genres.html

```html
{% extends "base/initial.html" %}
{% block content %}
<div class="bg-background dark:bg-background-dark min-h-screen selection:bg-primary/30 font-display relative overflow-hidden">

    <div class="fixed inset-0 z-0">
        <div class="absolute inset-0 bg-gradient-to-br from-surface-dark via-background-dark to-background-dark"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-background-dark via-background-dark/60 to-transparent"></div>
    </div>

    <main class="relative z-10 flex min-h-[calc(100vh-80px)] flex-col items-center justify-start p-6 md:p-12">

        <header class="w-full max-w-4xl mb-12 text-center">
            <div class="flex items-center justify-center mb-8">
                <span class="text-3xl font-extrabold tracking-tighter text-primary">StreamSync</span>
            </div>


        <section class="mb-8 text-center md:text-left">
            <h1 class="text-3xl md:text-4xl font-bold tracking-tight mb-3 text-white">Personalize Your Experience</h1>
            <p class="text-slate-400 text-base max-w-2xl leading-relaxed">
                Select at least 3 genres you love. We'll use this to create a personalized feed just for you.
            </p>
        </section>

            <div class="relative w-full">
                <div class="w-full h-2 bg-surface-dark/50 rounded-full overflow-hidden backdrop-blur-sm">
                    <div class="progress-bar h-full bg-gradient-to-r from-primary to-blue-400 rounded-full shadow-[0_0_15px_rgba(37,106,244,0.5)] transition-all duration-1000 ease-out" style="width: 100%"></div>
                </div>
                <div class="flex justify-between mt-3">
                    <div class="flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-primary shadow-[0_0_8px_rgba(37,106,244,0.8)]"></span>
                        <span class="text-xs font-medium text-primary">Profile</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-primary shadow-[0_0_8px_rgba(37,106,244,0.8)]"></span>
                        <span class="text-xs font-medium text-primary">Genres</span>
                    </div>
                </div>
            </div>
        
    <section class="pt-4 pb-48 px-6 max-w-7xl mx-auto">
        {% if error %}
        <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-4 text-red-400 mb-6">
            {{ error }}
        </div>
        {% endif %}

        <form method="post" id="genre-form">
            {% csrf_token %}

            <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-4">
                {% for genre in genres %}
                <label class="genre-card relative group block cursor-pointer overflow-hidden rounded-xl aspect-square transition-all duration-300 hover:scale-[1.02] genre-animate">
                    <input type="checkbox" name="genres" value="{{ genre.id }}" class="genre-checkbox sr-only"/>

                    <div class="card-inner absolute inset-0 bg-surface-dark rounded-xl border-2 border-border-dark transition-all duration-300 overflow-hidden group-hover:border-slate-500">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent z-10"></div>
                        <img src="https://source.unsplash.com/400x400/?{{ genre.name }},movie&w=800"
                            alt="{{ genre.name }}"
                            class="card-img w-full h-full object-cover grayscale group-hover:grayscale-0 group-hover:scale-110 transition-all duration-500"
                            onerror="this.src='https://placehold.co/400x400/1e293b/f1f5f9?text={{ genre.name|slugify }}'"/>

                        <div class="absolute bottom-4 left-4 z-20">
                            <span class="text-lg font-bold text-white drop-shadow-md">{{ genre.name }}</span>
                        </div>

                        <div class="card-check absolute top-4 right-4 z-20 opacity-0 scale-50 transition-all duration-300">
                            <span class="material-symbols-outlined text-primary bg-black/60 backdrop-blur-sm rounded-full p-1.5 shadow-lg" style="font-variation-settings: 'FILL' 1;">check_circle</span>
                        </div>
                    </div>
                </label>
                {% endfor %}
            </div>
        </form>
    </section>

    <footer class="fixed bottom-0 left-0 w-full p-6 z-50 flex flex-col md:flex-row gap-4 justify-between items-center bg-gradient-to-t from-background-dark via-background-dark/95 to-transparent border-t border-border-dark/30">
        <div class="hidden md:block">
            <span class="text-slate-400 text-sm">Select at least 3 genres</span>
        </div>

        <div class="flex items-center gap-4 w-full md:w-auto">
            <div id="selection-counter" class="flex items-center gap-2 bg-surface-dark/80 backdrop-blur-xl px-5 py-2.5 rounded-full border border-border-dark transition-all duration-300">
                <span id="count" class="text-sm font-bold text-white min-w-[1.5rem] text-center">0</span>
                <span class="text-sm text-slate-400">selected</span>
            </div>

            <button type="submit" form="genre-form" id="continue-btn"
                    class="flex-1 md:flex-none px-10 py-3.5 rounded-xl bg-gradient-to-r from-primary to-blue-500 text-white font-bold text-base shadow-lg shadow-primary/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all flex items-center justify-center gap-2 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:scale-100 group">
                <span class="transition-all">Continue</span>
                <span class="material-symbols-outlined transition-transform group-hover:translate-x-1">arrow_forward</span>
            </button>
        </div>

        <div class="md:hidden">
            <span class="text-slate-400 font-medium text-sm">Select at least 3 genres</span>
        </div>
    </footer>
    </header>
    </main>
</div>


{% endblock %}

{% block extra_scripts %} 
    {% load static %}
    <script src="{% static 'js/genres.js' %}"></script>
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/registration/onboarding.html -->
## app/templates/registration/onboarding.html

```html
{% extends "base/initial.html" %}
{% block content %}
<div class="bg-background dark:bg-background-dark min-h-screen selection:bg-primary/30 font-display relative overflow-hidden">

    <div class="fixed inset-0 z-0">
        <div class="absolute inset-0 bg-gradient-to-br from-surface-dark via-background-dark to-background-dark"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-background-dark via-background-dark/60 to-transparent"></div>
    </div>

    <main class="relative z-10 flex min-h-[calc(100vh-80px)] flex-col items-center justify-center p-6 md:p-12">

        <header class="w-full max-w-4xl mb-12 text-center">
            <div class="flex items-center justify-center mb-8">
                <span class="text-3xl font-extrabold tracking-tighter text-primary">StreamSync</span>
            </div>

            <div class="flex justify-between items-end mb-4 px-1">
                <h1 class="text-3xl font-bold text-white leading-tight">Complete Your Profile</h1>
                <span class="text-sm font-medium text-slate-400 mb-1">Step 1 of 2</span>
            </div>

            <div class="relative w-full">
                <div class="w-full h-2 bg-surface-dark/50 rounded-full overflow-hidden backdrop-blur-sm">
                    <div class="progress-bar h-full bg-gradient-to-r from-primary to-blue-400 rounded-full shadow-[0_0_15px_rgba(37,106,244,0.5)] transition-all duration-1000 ease-out" style="width: 50%"></div>
                </div>
                <div class="flex justify-between mt-3">
                    <div class="flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-primary shadow-[0_0_8px_rgba(37,106,244,0.8)]"></span>
                        <span class="text-xs font-medium text-primary">Profile</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-slate-600"></span>
                        <span class="text-xs font-medium text-slate-500">Genres</span>
                    </div>
                </div>
            </div>
        </header>

        <form method="post" class="w-full max-w-4xl space-y-8" novalidate>
            {% csrf_token %}

            {% if errors %}
            <div class="bg-red-500/10 border border-red-500/30 rounded-lg p-4 text-red-400">
                <ul class="list-disc list-inside space-y-1">
                    {% for error in errors %}
                    <li>{{ error }}</li>
                    {% endfor %}
                </ul>
            </div>
            {% endif %}

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="field-animate bg-surface-dark/50 backdrop-blur-sm p-6 rounded-xl border border-border-dark flex flex-col group hover:border-primary/50 transition-all duration-300 hover:shadow-lg hover:shadow-primary/10" style="animation-delay: 0.1s">
                    <label class="block text-xs font-bold text-slate-400 uppercase tracking-[0.2em] mb-4">
                        Date of Birth <span class="text-red-400">*</span>
                    </label>
                    <div class="relative mt-auto">
                        <input type="date" name="birth_date" id="id_birth_date" required
                               class="w-full bg-surface-dark border border-border-dark text-white rounded-lg py-3 px-4 focus:ring-2 focus:ring-primary/50 cursor-pointer transition-all duration-300 [color-scheme:dark] hover:border-slate-500 focus:border-primary focus:shadow-[0_0_0_3px_rgba(37,106,244,0.15)]">
                    </div>
                </div>

                <div class="field-animate bg-surface-dark/50 backdrop-blur-sm p-6 rounded-xl border border-border-dark flex flex-col group hover:border-primary/50 transition-all duration-300 hover:shadow-lg hover:shadow-primary/10" style="animation-delay: 0.2s">
                    <label class="block text-xs font-bold text-slate-400 uppercase tracking-[0.2em] mb-4">
                        Country <span class="text-red-400">*</span>
                    </label>
                    <div class="relative mt-auto group">
                        <select name="country" id="id_country" required
                                class="w-full bg-surface-dark border border-border-dark text-white rounded-lg py-3 px-4 appearance-none focus:ring-2 focus:ring-primary/50 cursor-pointer transition-all duration-300 hover:border-slate-500 focus:border-primary focus:shadow-[0_0_0_3px_rgba(37,106,244,0.15)]">
                            <option value="" class="bg-surface-dark">Select country</option>
                            {% for country in countries %}
                            <option value="{{ country.id }}" class="bg-surface-dark">{{ country.name }}</option>
                            {% endfor %}
                        </select>
                        <span class="material-symbols-outlined absolute right-3 top-3 pointer-events-none text-slate-400 group-hover:text-slate-300 transition-colors">
                            expand_more
                        </span>
                    </div>
                </div>

                <div class="field-animate bg-surface-dark/50 backdrop-blur-sm p-6 rounded-xl border border-border-dark flex flex-col group hover:border-primary/50 transition-all duration-300 hover:shadow-lg hover:shadow-primary/10" style="animation-delay: 0.3s">
                    <label class="block text-xs font-bold text-slate-400 uppercase tracking-[0.2em] mb-4">
                        Gender
                    </label>
                    <div class="relative mt-auto group">
                        <select name="gender" id="id_gender"
                                class="w-full bg-surface-dark border border-border-dark text-white rounded-lg py-3 px-4 appearance-none focus:ring-2 focus:ring-primary/50 cursor-pointer transition-all duration-300 hover:border-slate-500 focus:border-primary focus:shadow-[0_0_0_3px_rgba(37,106,244,0.15)]">
                            <option value="" class="bg-surface-dark">Select gender</option>
                            <option value="male" class="bg-surface-dark">Male</option>
                            <option value="female" class="bg-surface-dark">Female</option>
                            <option value="non-binary" class="bg-surface-dark">Non-binary</option>
                            <option value="other" class="bg-surface-dark">Other / Prefer not to say</option>
                        </select>
                        <span class="material-symbols-outlined absolute right-3 top-3 pointer-events-none text-slate-400 group-hover:text-slate-300 transition-colors">
                            expand_more
                        </span>
                    </div>
                </div>
            </div>

            <footer class="w-full pt-6 flex justify-end gap-6">
                <button type="submit"
                        class="flex-1 md:flex-none px-10 py-3.5 rounded-xl bg-gradient-to-r from-primary to-blue-500 text-white font-bold text-base shadow-lg shadow-primary/20 hover:brightness-110 hover:scale-[1.02] active:scale-[0.98] transition-all flex items-center justify-center gap-2 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:scale-100 group">
                <span class="transition-all">Continue</span>
                    <span class="material-symbols-outlined transition-transform group-hover:translate-x-1">arrow_forward</span>
                </button>
            </footer>
        </form>

        <div class="fixed bottom-10 left-10 pointer-events-none opacity-[0.03] select-none hidden lg:block">
            <span class="text-[12rem] font-black leading-none tracking-tighter uppercase">Profile</span>
        </div>
    </main>
</div>


{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/registration/privacy_policy.html -->
## app/templates/registration/privacy_policy.html

```html
{% extends "base/initial.html" %} {% block content %}
<div class="min-h-[calc(100vh-80px)] bg-slate-50 dark:bg-background-dark px-4 py-8">
    <div class="max-w-3xl mx-auto bg-white dark:bg-[#1e293b] p-8 rounded-2xl shadow-xl border border-slate-200 dark:border-slate-800">
        
        <h1 class="text-3xl font-bold text-slate-900 dark:text-white mb-6">Privacy Policy</h1>
        
        <div class="prose dark:prose-invert max-w-none">
            <p class="text-slate-600 dark:text-slate-400">
                At StreamSync, we take your privacy seriously. This Privacy Policy explains how we collect, use, and protect your information.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">1. Information We Collect</h2>
            <p class="text-slate-600 dark:text-slate-400">
                We collect information you provide when creating an account, including your name, email address, and other profile information.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">2. How We Use Your Information</h2>
            <p class="text-slate-600 dark:text-slate-400">
                We use your information to provide and improve our services, communicate with you, and personalize your experience.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">3. Data Protection</h2>
            <p class="text-slate-600 dark:text-slate-400">
                We implement appropriate security measures to protect your personal information against unauthorized access, alteration, or disclosure.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">4. Third-Party Services</h2>
            <p class="text-slate-600 dark:text-slate-400">
                We may share information with third-party service providers who assist us in operating our service, under strict confidentiality obligations.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">5. Cookies</h2>
            <p class="text-slate-600 dark:text-slate-400">
                We use cookies to enhance your user experience. You can control cookies through your browser settings.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">6. Your Rights</h2>
            <p class="text-slate-600 dark:text-slate-400">
                You have the right to access, correct, or delete your personal information. Contact us to exercise these rights.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">7. Changes to Policy</h2>
            <p class="text-slate-600 dark:text-slate-400">
                We may update this policy periodically. We will notify you of any material changes.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">8. Contact</h2>
            <p class="text-slate-600 dark:text-slate-400">
                If you have questions about this Privacy Policy, please contact us.
            </p>
        </div>
        
        <div class="mt-8 text-center">
            <a href="{% url 'signup' %}" class="inline-block bg-primary hover:bg-primary/90 text-white font-bold py-3 px-8 rounded-xl transition-all">
                Back to
            </a>
        </div>
    </div>
</div>
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/registration/singup.html -->
## app/templates/registration/singup.html

```html
{% extends "base/initial.html" %}
{% load static %}
{% block extra_styles %}<link rel="stylesheet" href="{% static 'css/auth-signup.css' %}">{% endblock %}
{% block content %}
<div class="flex items-center justify-center min-h-[calc(100vh-80px)] bg-slate-50 dark:bg-background-dark px-4 py-8">
    <div class="max-w-lg w-full bg-white dark:bg-[#1e293b] p-8 rounded-2xl shadow-xl border border-slate-200 dark:border-slate-800 animate-fade-in-up">

        <div class="text-center mb-8">
            <h2 class="text-3xl font-bold text-slate-900 dark:text-white">Create Account</h2>
            <p class="text-slate-500 dark:text-slate-400 mt-2">Join StreamSync to start watching</p>
        </div>

        <form method="post" class="space-y-5" id="signup-form" novalidate>
            {% csrf_token %}

            <div class="grid grid-cols-2 gap-4">
                <div class="flex flex-col gap-1">
                    <label class="text-sm font-medium text-slate-700 dark:text-slate-300 ml-1">
                        First Name
                    </label>
                    <div class="relative">
                        {{ form.first_name }}
                    </div>
                    {% for error in form.first_name.errors %}
                        <p class="text-xs text-red-500 ml-1 error-message">{{ error }}</p>
                    {% endfor %}
                </div>

                <div class="flex flex-col gap-1">
                    <label class="text-sm font-medium text-slate-700 dark:text-slate-300 ml-1">
                        Last Name
                    </label>
                    <div class="relative">
                        {{ form.last_name }}
                    </div>
                    {% for error in form.last_name.errors %}
                        <p class="text-xs text-red-500 ml-1 error-message">{{ error }}</p>
                    {% endfor %}
                </div>
            </div>

            <div class="flex flex-col gap-1">
                <label class="text-sm font-medium text-slate-700 dark:text-slate-300 ml-1">
                    Username
                </label>
                <div class="relative">
                    {{ form.username }}
                </div>
                <p class="text-[11px] text-slate-400 ml-1 leading-tight">Required. 150 characters or fewer.</p>
                {% for error in form.username.errors %}
                    <p class="text-xs text-red-500 ml-1 error-message">{{ error }}</p>
                {% endfor %}
            </div>

            <div class="flex flex-col gap-1">
                <label class="text-sm font-medium text-slate-700 dark:text-slate-300 ml-1">
                    Email Address
                </label>
                <div class="relative">
                    {{ form.email }}
                </div>
                {% for error in form.email.errors %}
                    <p class="text-xs text-red-500 ml-1 error-message">{{ error }}</p>
                {% endfor %}
            </div>

            <div class="flex flex-col gap-1">
                <label class="text-sm font-medium text-slate-700 dark:text-slate-300 ml-1">
                    Password
                </label>
                <div class="relative">
                    {{ form.password1 }}
                </div>
                <div id="password1-feedback" class="space-y-1 mt-1">
                    <p class="text-[11px] text-slate-400">
                        <span id="length-check">○</span> At least 8 characters
                    </p>
                    <p class="text-[11px] text-slate-400">
                        <span id="common-check">○</span> Not a commonly used password
                    </p>
                    <p class="text-[11px] text-slate-400">
                        <span id="number-check">○</span> Not entirely numeric
                    </p>
                </div>
                {% for error in form.password1.errors %}
                    <p class="text-xs text-red-500 ml-1 error-message">{{ error }}</p>
                {% endfor %}
            </div>

            <div class="flex flex-col gap-1">
                <label class="text-sm font-medium text-slate-700 dark:text-slate-300 ml-1">
                    Confirm Password
                </label>
                <div class="relative">
                    {{ form.password2 }}
                </div>
                <p id="password2-match" class="text-[11px] text-slate-400 mt-1 hidden">
                    <span id="match-icon"></span> <span id="match-text"></span>
                </p>
                {% for error in form.password2.errors %}
                    <p class="text-xs text-red-500 ml-1 error-message">{{ error }}</p>
                {% endfor %}
            </div>

            <div class="space-y-3 pt-2">
                <div class="flex items-start gap-3">
                    <div class="flex items-center h-5">
                        {{ form.terms_of_service }}
                    </div>
                    <div class="text-sm">
                        <label for="id_terms_of_service" class="text-slate-700 dark:text-slate-300">
                            I agree to the
                            <a href="{% url 'terms_of_service' %}" target="_blank" class="text-primary hover:underline">Terms of Service</a>
                        </label>
                        {% for error in form.terms_of_service.errors %}
                            <p class="text-xs text-red-500 error-message">{{ error }}</p>
                        {% endfor %}
                    </div>
                </div>

                <div class="flex items-start gap-3">
                    <div class="flex items-center h-5">
                        {{ form.privacy_policy }}
                    </div>
                    <div class="text-sm">
                        <label for="id_privacy_policy" class="text-slate-700 dark:text-slate-300">
                            I agree to the
                            <a href="{% url 'privacy_policy' %}" target="_blank" class="text-primary hover:underline">Privacy Policy</a>
                        </label>
                        {% for error in form.privacy_policy.errors %}
                            <p class="text-xs text-red-500 error-message">{{ error }}</p>
                        {% endfor %}
                    </div>
                </div>
            </div>

            <button type="submit" id="submit-btn" class="w-full bg-primary hover:bg-primary/90 text-white font-bold py-3 rounded-xl transition-all shadow-lg shadow-primary/20 mt-4 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100 group relative overflow-hidden" disabled>
                <span class="relative z-10 flex items-center justify-center gap-2">
                    <span class="btn-text">Create Account</span>
                </span>
                <div class="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
            </button>
        </form>

        <div class="mt-6 text-center">
            <p class="text-sm text-slate-500">
                Already have an account?
                <a href="{% url 'login' %}" class="text-primary font-semibold hover:underline">Log in</a>
            </p>
        </div>
    </div>
</div>

{% block extra_scripts %}<script src="{% static 'js/auth-signup.js' %}"></script>{% endblock %}
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/registration/terms_of_service.html -->
## app/templates/registration/terms_of_service.html

```html
{% extends "base/initial.html" %} {% block content %}
<div class="min-h-[calc(100vh-80px)] bg-slate-50 dark:bg-background-dark px-4 py-8">
    <div class="max-w-3xl mx-auto bg-white dark:bg-[#1e293b] p-8 rounded-2xl shadow-xl border border-slate-200 dark:border-slate-800">
        
        <h1 class="text-3xl font-bold text-slate-900 dark:text-white mb-6">Terms of Service</h1>
        
        <div class="prose dark:prose-invert max-w-none">
            <p class="text-slate-600 dark:text-slate-400">
                Welcome to StreamSync. By accessing and using our service, you agree to be bound by these Terms of Service.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">1. Acceptance of Terms</h2>
            <p class="text-slate-600 dark:text-slate-400">
                By creating an account or accessing StreamSync, you acknowledge that you have read, understood, and agree to be bound by these terms.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">2. Use of Service</h2>
            <p class="text-slate-600 dark:text-slate-400">
                You agree to use StreamSync only for lawful purposes and in accordance with these Terms of Service.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">3. Account Responsibilities</h2>
            <p class="text-slate-600 dark:text-slate-400">
                You are responsible for maintaining the confidentiality of your account credentials and for all activities that occur under your account.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">4. Privacy</h2>
            <p class="text-slate-600 dark:text-slate-400">
                Your privacy is important to us. Please review our Privacy Policy to understand how we collect and use your information.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">5. Changes to Terms</h2>
            <p class="text-slate-600 dark:text-slate-400">
                We reserve the right to modify these terms at any time. Continued use of the service constitutes acceptance of any changes.
            </p>
            
            <h2 class="text-xl font-semibold text-slate-900 dark:text-white mt-6 mb-3">6. Contact</h2>
            <p class="text-slate-600 dark:text-slate-400">
                If you have any questions about these Terms of Service, please contact us.
            </p>
        </div>
        
        <div class="mt-8 text-center">
            <a href="{% url 'signup' %}" class="inline-block bg-primary hover:bg-primary/90 text-white font-bold py-3 px-8 rounded-xl transition-all">
                Back to Sign Up
            </a>
        </div>
    </div>
</div>
{% endblock %}

```
<!-- END_FILE -->

---
<!-- FILE: app/tests.py -->
## app/tests.py

```py
from django.test import TestCase

# Create your tests here.

```
<!-- END_FILE -->

---
<!-- FILE: app/urls.py -->
## app/urls.py

```py
from django.urls import path
from . import views, admin
app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('catalog/', views.catalog, name='catalog'),
    path('movies/', views.movies, name='movies'),
    path('series/', views.series, name='series'),
    path('search/', views.search, name='search'),
    path('redirect/',views.login_redirect, name='login_redirect'),
    path('content/<str:ctype>/<str:cid>/', views.content_detail, name='content_detail'),
    path('content/<str:ctype>/<str:cid>/update-status/', views.update_status, name='update_status'),
    path('content/<str:ctype>/<str:cid>/toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('personal_library/',views.personal_library, name='personal_library'),
    path('user_settings/',views.user_settings, name='user_settings'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('onboarding/genres/', views.onboarding_genres, name='onboarding_genres'),
    path('onboarding-complete/', views.onboarding_complete, name='onboarding_complete'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('dashboard/direction/', views.direction_dashboard, name='direction_dashboard'),
    path('content/<str:ctype>/<int:cid>/', views.content_detail, name='content_detail'),
]

```
<!-- END_FILE -->

---
<!-- FILE: app/utils.py -->
## app/utils.py

```py
import csv
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse
from .models import Statistics, AudiovisualContent


class DashboardService:
    @staticmethod
    def apply_filters(params):
        stats_qs = Statistics.objects.all()
        content_qs = AudiovisualContent.objects.all()
        today = timezone.now().date()

        range_val = params.get('range')
        start_date = params.get('start_date')
        end_date = params.get('end_date')

        if range_val:
            if range_val == '24h':
                stats_qs = stats_qs.filter(week=today)
            elif range_val == '7d':
                stats_qs = stats_qs.filter(week__gte=today - timedelta(days=7))
            elif range_val == '30d':
                stats_qs = stats_qs.filter(week__gte=today - timedelta(days=30))
            elif range_val == '90d':
                stats_qs = stats_qs.filter(week__gte=today - timedelta(days=90))
            elif range_val == 'ytd':
                stats_qs = stats_qs.filter(week__year=today.year)
        elif start_date and end_date:
            stats_qs = stats_qs.filter(week__range=[start_date, end_date])

        genre_id = params.get('genre')
        if genre_id and genre_id != 'all':
            content_qs = content_qs.filter(genre_id=genre_id)
            stats_qs = stats_qs.filter(platform__catalog__content__genre_id=genre_id).distinct()

        platform_id = params.get('platform')
        if platform_id and platform_id != 'all':
            stats_qs = stats_qs.filter(platform_id=platform_id)
            content_qs = content_qs.filter(catalog__platform_id=platform_id).distinct()

        country_id = params.get('country')
        if country_id and country_id != 'all':
            content_qs = content_qs.filter(country_id=country_id)
            stats_qs = stats_qs.filter(platform__catalog__content__country_id=country_id).distinct()

        return stats_qs, content_qs

    @staticmethod
    def get_csv_response(trending_content, totals, top_p):
        response = HttpResponse(content_type='text/csv')
        today = timezone.now()
        response['Content-Disposition'] = f'attachment; filename="Strategic_Report_{today.date()}.csv"'

        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response, delimiter=';')

        writer.writerow(['STRATEGIC PERFORMANCE REPORT'])
        writer.writerow(['Report Date', today.strftime('%Y-%m-%d %H:%M')])
        writer.writerow(['Total Clicks', totals['clicks']])
        writer.writerow(['Total Favorites', totals['favs']])
        writer.writerow(['Top Performing Platform', top_p['platform__platform_name'] if top_p else 'N/A'])
        writer.writerow([])

        writer.writerow(['TOP 10 CONTENT PERFORMANCE DETAILS'])
        writer.writerow(['RANK', 'TITLE', 'DIRECTOR', 'GENRE', 'COUNTRY', 'INTERACTIONS (FAVS)'])

        for i, item in enumerate(trending_content, 1):
            writer.writerow([
                i,
                item.title,
                item.director.name if item.director else 'N/A',
                item.genre.name if item.genre else 'N/A',
                item.country.name if item.country else 'N/A',
                item.fav_count
            ])

        return response

```
<!-- END_FILE -->

---
<!-- FILE: app/views.py -->
## app/views.py

```py
from django.contrib.auth.forms import UserCreationForm
from .services import get_all_movies, get_all_series, search_content, get_movies_by_genres, get_series_by_genres, get_trending, get_all_platforms, get_all_genres_from_api, search_content
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash, logout
from .models import VisualizationProgress
from django.utils.text import slugify
from app.models import Country
from app.models import User, Country
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Count
from django.core.exceptions import PermissionDenied
from .models import *
from .utils import DashboardService
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import VisualizationProgress, Movie, Series
import json
    
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

@login_required
def user_settings(request):


    countries = Country.objects.all()

    if request.method == 'POST':
        user = request.user

        if request.POST.get('action') == 'change_password':
            current_password = request.POST.get('current_password', '').strip()
            new_password = request.POST.get('new_password', '').strip()
            confirm_password = request.POST.get('confirm_password', '').strip()

            password_errors = []

            if not current_password:
                password_errors.append('Current password is required')
            elif not user.check_password(current_password):
                password_errors.append('Current password is incorrect')

            if not new_password:
                password_errors.append('New password is required')
            elif len(new_password) < 8:
                password_errors.append('New password must be at least 8 characters')

            if new_password != confirm_password:
                password_errors.append('New password and confirm password do not match')

            if password_errors:
                return render(request, 'pages/user_settings.html', {
                    'user': user,
                    'countries': countries,
                    'password_errors': password_errors
                })

            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)

            return render(request, 'pages/user_settings.html', {
                'user': user,
                'countries': countries,
                'password_success': 'Password changed successfully!'
            })

        username = request.POST.get('username', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        bio = request.POST.get('bio', '').strip()
        gender = request.POST.get('gender')
        country_id = request.POST.get('country')

        errors = []

        if not username:
            errors.append('Username is required')
        elif username != user.username and User.objects.filter(username=username).exclude(pk=user.pk).exists():
            errors.append('Username already exists')

        if not first_name:
            errors.append('First name is required')

        if not last_name:
            errors.append('Last name is required')

        if errors:
            return render(request, 'pages/user_settings.html', {
                'user': user,
                'countries': countries,
                'errors': errors
            })

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.bio = bio
        user.gender = gender if gender else None

        if country_id:
            user.country_id = country_id
        else:
            user.country_id = None

        if request.FILES.get('profile_picture'):
            user.profile_picture = request.FILES['profile_picture']

        user.save()

        return render(request, 'pages/user_settings.html', {
            'user': user,
            'countries': countries,
            'success': 'Profile updated successfully!'
        })

    return render(request, 'pages/user_settings.html', {
        'user': request.user,
        'countries': countries
    })

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()

    return redirect('app:home')

def catalog(request):
    # Obtener parámetros de filtro
    selected_platform = request.GET.get('platform')
    selected_genre = request.GET.get('genre')
    sort_rating = request.GET.get('sort_rating')
    sort_year = request.GET.get('sort_year')

    # Obtener datos base
    movies = get_all_movies(platform_filter=selected_platform)
    series = get_all_series(platform_filter=selected_platform)
    
    # Filtrar por género localmente si se seleccionó uno
    if selected_genre:
        movies = [m for m in movies if m.get('genre_name') == selected_genre]
        series = [s for s in series if s.get('genre_name') == selected_genre]

    # Lógica de ordenamiento
    def apply_sort(data, key_rating, key_year):
        if sort_rating:
            data.sort(key=lambda x: x.get(key_rating, 0), reverse=(sort_rating == 'desc'))
        if sort_year:
            data.sort(key=lambda x: x.get(key_year, 0), reverse=(sort_year == 'desc'))
        return data

    movies = apply_sort(movies, 'rating', 'year')
    series = apply_sort(series, 'rating', 'start_year')

    context = {
        'movies': movies,
        'series': series,
        'platforms': get_all_platforms(),
        'genres': get_all_genres_from_api(),
        'selected_platform': selected_platform,
        'selected_genre': selected_genre,
        'sort_rating': sort_rating,
        'sort_year': sort_year,
    }
    return render(request, 'pages/catalog.html', context)

def movies(request):
    selected_platform = request.GET.get('platform')
    selected_genre = request.GET.get('genre')
    sort_rating = request.GET.get('sort_rating')
    sort_year = request.GET.get('sort_year')

    movies_list = get_all_movies(platform_filter=selected_platform)
    
    # Filtrado por género
    if selected_genre:
        movies_list = [m for m in movies_list if m.get('genre_name') == selected_genre]

    # Ordenamiento
    if sort_rating:
        movies_list.sort(key=lambda x: x.get('rating', 0), reverse=(sort_rating == 'desc'))
    if sort_year:
        movies_list.sort(key=lambda x: x.get('year', 0), reverse=(sort_year == 'desc'))

    context = {
        'movies': movies_list,
        'platforms': get_all_platforms(), # <--- Añadir esto
        'genres': get_all_genres_from_api(), # <--- Añadir esto
        'selected_platform': selected_platform,
        'selected_genre': selected_genre,
        'sort_rating': sort_rating,
        'sort_year': sort_year,
    }
    return render(request, 'pages/movies.html', context)

def series(request):
    selected_platform = request.GET.get('platform')
    selected_genre = request.GET.get('genre')
    sort_rating = request.GET.get('sort_rating')
    sort_year = request.GET.get('sort_year')

    series_list = get_all_series(platform_filter=selected_platform)
    
    # Filtrado por género
    if selected_genre:
        series_list = [s for s in series_list if s.get('genre_name') == selected_genre]

    # Ordenamiento
    if sort_rating:
        series_list.sort(key=lambda x: x.get('rating', 0), reverse=(sort_rating == 'desc'))
    if sort_year:
        series_list.sort(key=lambda x: x.get('start_year', 0), reverse=(sort_year == 'desc'))

    context = {
        'series': series_list,
        'platforms': get_all_platforms(), 
        'genres': get_all_genres_from_api(), 
        'selected_platform': selected_platform,
        'selected_genre': selected_genre,
        'sort_rating': sort_rating,
        'sort_year': sort_year,
    }
    return render(request, 'pages/series.html', context)

def search(request):
    query = request.GET.get('q', '').strip()
    p = request.GET.get('platform')
    g = request.GET.get('genre')
    sr = request.GET.get('sort_rating')
    sy = request.GET.get('sort_year')
    
    results = []
    if query:
        # Ahora el servicio devuelve objetos con el campo 'detail_url' ya calculado
        results = search_content(query, platform=p, genre=g, sort_rating=sr, sort_year=sy)

    context = {
        'query': query,
        'movies': [i for i in results if i['content_type'] == 'movie'],
        'series': [i for i in results if i['content_type'] == 'series'],
        'result_count': len(results),
        'platforms': get_all_platforms(),
        'genres': get_all_genres_from_api(),
        'selected_platform': p,
        'selected_genre': g,
    }
    return render(request, 'pages/search.html', context)

def register(request):
    return render(request, 'streamsync_register.html',{
        'form': UserCreationForm
    })

def login(request):
    return render(request, 'login.html')


def content_detail(request, ctype, cid):
    from django.http import JsonResponse
    from .models import VisualizationProgress, Favorite, Watchlist
    
    if ctype == 'series':
        data = get_all_series()
    else:
        data = get_all_movies()
    
    content = next((item for item in data if slugify(f"{item.get('title', '').replace(' ', '-')}_{item.get('year', item.get('start_year', ''))}") == slugify(str(cid))), None)
    
    if content:
        content['content_type'] = ctype
        
        # Obtener estado del usuario si está autenticado
        user_status = 'not_seen'
        is_favorite = False
        is_in_watchlist = False
        
        if request.user.is_authenticated:
            # Buscar el contenido en la base de datos local
            from app.models import AudiovisualContent, Movie, Series
            try:
                if ctype == 'series':
                    local_content = Series.objects.filter(title=content.get('title')).first()
                else:
                    local_content = Movie.objects.filter(title=content.get('title')).first()
                
                if local_content:
                    # Verificar VisualizationProgress
                    vp = VisualizationProgress.objects.filter(user=request.user, content=local_content).first()
                    if vp:
                        if vp.completed:
                            user_status = 'completed'
                        elif vp.last_minute > 0:
                            user_status = 'watching'
                    
                    # Verificar Favorite
                    is_favorite = Favorite.objects.filter(user=request.user, content=local_content).exists()
                    
                    # Verificar Watchlist
                    is_in_watchlist = Watchlist.objects.filter(user=request.user, content=local_content).exists()
            except Exception:
                pass
        
        return render(request, 'pages/content_view.html', {
            'content': content,
            'user_status': user_status,
            'is_favorite': is_favorite,
            'is_in_watchlist': is_in_watchlist
        })
    else:
        return render(request, 'pages/home.html', status=404)


def _safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def _safe_float(value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def _resolve_content(ctype, cid):
    """Find API content dict and local ORM object from ctype/cid."""
    from datetime import date

    data = get_all_series() if ctype == 'series' else get_all_movies()
    api_content = next(
        (item for item in data 
         if slugify(f"{item.get('title', '').replace(' ', '-')}_{item.get('year', item.get('start_year', ''))}") 
            == slugify(str(cid))),
        None
    )
    if not api_content:
        return None, None

    model_class = Series if ctype == 'series' else Movie
    local_content = model_class.objects.filter(title=api_content['title']).first()
    if local_content:
        return api_content, local_content

    defaults = {
        'synopsis': api_content.get('synopsis')  or 'No synopsis available.',
        'rating': _safe_float(api_content.get('rating')),
    }
    if ctype == 'series':
        defaults.update({
            'start_year': _safe_int(api_content.get('start_year')),
            'end_year': _safe_int(api_content.get('end_year')) if api_content.get('end_year') else None,
            'total_seasons': _safe_int(api_content.get('total_seasons')),
        })
    else:
        release_date_str = api_content.get('release_date')
        try:
            release_date = date.fromisoformat(release_date_str) if release_date_str else date.today()
        except (ValueError, TypeError):
            release_date = date.today()
        defaults.update({
            'year': _safe_int(api_content.get('year')),
            'release_date': release_date,
            'duration_minutes': _safe_int(api_content.get('duration_minutes')),
        })

    local_content = model_class.objects.create(title=api_content['title'], **defaults)
    return api_content, local_content


@login_required
def update_status(request, ctype, cid):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            status = data.get('status', 'not_seen')

            _, local_content = _resolve_content(ctype, cid)
            if not local_content:
                return JsonResponse({'success': False, 'error': 'Content not found'})

            vp, created = VisualizationProgress.objects.get_or_create(
                user=request.user,
                content=local_content
            )

            if status == 'completed':
                vp.completed = True
            elif status == 'watching':
                vp.completed = False
                vp.last_minute = vp.last_minute if vp.last_minute > 0 else 1
            else:
                vp.completed = False
                vp.last_minute = 0

            vp.save()
            return JsonResponse({'success': True, 'status': status})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid method'})


@login_required
def toggle_favorite(request, ctype, cid):
    if request.method == 'POST':
        try:
            _, local_content = _resolve_content(ctype, cid)
            if not local_content:
                return JsonResponse({'success': False, 'error': 'Content not found'})

            favorite = Favorite.objects.filter(user=request.user, content=local_content).first()
            if favorite:
                favorite.delete()
                return JsonResponse({'success': True, 'is_favorite': False})
            else:
                Favorite.objects.create(user=request.user, content=local_content)
                return JsonResponse({'success': True, 'is_favorite': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid method'})
    
@login_required
def personal_library(request):
    from app.models import Movie, Series
    
    # Favoritos del usuario
    favorites = Favorite.objects.filter(user=request.user).select_related('content', 'content__genre')
    favorites_count = favorites.count()
    
    # Separar movies y series
    favorite_movies = []
    favorite_series = []
    
    for fav in favorites:
        content = fav.content
        item = {
            'title': content.title,
            'rating': content.rating,
            'genre_name': content.genre.name if content.genre else 'Unknown',
            'platforms': []
        }
        
        if isinstance(content, Series):
            item['start_year'] = content.start_year
            item['unique_id'] = f"{content.title.lower().replace(' ', '-')}_{content.start_year}"
            favorite_series.append(item)
        elif isinstance(content, Movie):
            item['year'] = content.year
            item['unique_id'] = f"{content.title.lower().replace(' ', '-')}_{content.year}"
            favorite_movies.append(item)
    
    # Continue Watching: tiene progreso pero no completado (last_minute > 0)
    watching_count = VisualizationProgress.objects.filter(
        user=request.user,
        completed=False
    ).exclude(last_minute=0).count()
    
    # Completed: marcados como completados
    completed_count = VisualizationProgress.objects.filter(
        user=request.user,
        completed=True
    ).count()
    
    return render(request, 'pages/personal_library.html', {
        'favorites_count': favorites_count,
        'watching_count': watching_count,
        'completed_count': completed_count,
        'favorite_movies': favorite_movies,
        'favorite_series': favorite_series
    })


@login_required
def main(request):
    user = request.user
    
    favorite_genres = list(user.favorite_genres.values_list('name', flat=True))
    
    recommended_by_genre = {}
    recommended_series_by_genre = {}
    if favorite_genres:
        recommended_by_genre = get_movies_by_genres(favorite_genres, min_total=5)
        recommended_series_by_genre = get_series_by_genres(favorite_genres, min_total=5)
    
    trending = get_trending(limit=4)
    
    watch_progress = VisualizationProgress.objects.filter(user=user, completed=False).select_related('content')
    has_watch_history = watch_progress.exists()
    
    return render(request, 'pages/main.html', {
        'recommended_by_genre': recommended_by_genre,
        'recommended_series_by_genre': recommended_series_by_genre,
        'trending': trending,
        'has_watch_history': has_watch_history,
        'watch_progress': watch_progress
    })

@login_required
def login_redirect(request):
    user = request.user

    if not user.onboarding_completed:
        return redirect('app:onboarding')

    if user.is_superuser or user.groups.filter(name='director').exists():
        return redirect('app:direction_dashboard')

    elif user.groups.filter(name='technical').exists():
        return redirect('tech_admin:index')
    
    elif user.groups.filter(name='plataform').exists():
        return redirect('app:series')  # provisional redirect

    else:
        return redirect('app:main')


@login_required
def onboarding(request):
    from app.models import Country
    
    if request.user.onboarding_completed:
        return redirect('app:main')
    
    if request.method == 'POST':
        birth_date = request.POST.get('birth_date')
        country_id = request.POST.get('country')
        gender = request.POST.get('gender')
        errors = []
        
        if not birth_date:
            errors.append('Date of birth is required')
        if not country_id:
            errors.append('Country is required')
        
        if errors:
            countries = Country.objects.all()
            return render(request, 'registration/onboarding.html', {
                'countries': countries,
                'errors': errors
            })
        
        user = request.user
        user.birth_date = birth_date
        user.country_id = country_id
        user.gender = gender if gender else None
        user.onboarding_completed = True
        user.save()
        
        return redirect('app:onboarding_genres')
    
    countries = Country.objects.all()
    return render(request, 'registration/onboarding.html', {
        'countries': countries
    })


@login_required
def onboarding_genres(request):
    from app.models import Genre
    
    if not request.user.onboarding_completed:
        return redirect('app:onboarding')
    
    if request.method == 'POST':
        selected_genres = request.POST.getlist('genres')
        
        if len(selected_genres) < 3:
            genres = Genre.objects.all()
            return render(request, 'registration/onboarding_genres.html', {
                'genres': genres,
                'error': f'Select at least 3 genres (you selected {len(selected_genres)})'
            })
        
        user = request.user
        user.favorite_genres.clear()
        for genre_id in selected_genres:
            try:
                genre = Genre.objects.get(id=genre_id)
                user.favorite_genres.add(genre)
            except Genre.DoesNotExist:
                pass
        
        return redirect('app:onboarding_complete')
    
    genres = Genre.objects.all()
    return render(request, 'registration/onboarding_genres.html', {
        'genres': genres
    })


@login_required
def onboarding_complete(request):
    if not request.user.onboarding_completed:
        return redirect('app:onboarding')
    return render(request, 'registration/onboarding_complete.html')
def tech_add_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password_again')

        role_id = request.POST.get('role')
        profile_img = request.FILES.get('profile_image')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect(request.path)

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
password=***REDACTED***
                first_name=first_name,
                last_name=last_name
            )

            if role_id:
                user.role = Group.objects.get(id=role_id)

            if profile_img:
                user.profile_picture = profile_img

            user.save()

            messages.success(request, f"User {username} created successfully!")
            return redirect('tech_admin:index')

        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect(request.path)

    groups = Group.objects.all()
    return render(request, 'admin/tech_add_user.html', {'groups': groups})

def tech_edit_user_view(request, user_id):
    user_to_edit = get_object_or_404(User, id=user_id)
    groups = Group.objects.all()

    if request.method == 'POST':
        user_to_edit.username = request.POST.get('username')
        user_to_edit.first_name = request.POST.get('first_name')
        user_to_edit.last_name = request.POST.get('last_name')
        user_to_edit.email = request.POST.get('email')

        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password_again')
        if pass1:
            if pass1 == pass2:
                user_to_edit.set_password(pass1)
            else:
                messages.error(request, "Las contraseñas no coinciden.")
                return redirect(request.path)

        role_id = request.POST.get('role')
        profile_img = request.FILES.get('profile_image')

        if role_id:
            user_to_edit.role = Group.objects.get(id=role_id)

        if profile_img:
            user_to_edit.profile_picture = profile_img

        try:
            user_to_edit.save()
            messages.success(request, f"Usuario {user_to_edit.username} actualizado correctamente.")
            return redirect('tech_admin:index')
        except Exception as e:
            messages.error(request, f"Error al guardar: {e}")

    return render(request, 'admin/tech_edit_user.html', {
        'user_to_edit': user_to_edit,
        'groups': groups
    })

def tech_delete_user(request, user_id):
    if request.user.id == user_id:
        messages.error(request, "No puedes borrar tu propia cuenta desde aquí.")
        return redirect('tech_admin:index')

    user_to_delete = get_object_or_404(User, id=user_id)
    username = user_to_delete.username

    if request.method == 'POST':
        user_to_delete.delete()
        messages.success(request, f"Usuario {username} eliminado permanentemente.")

    return redirect('tech_admin:index')

@login_required
def direction_dashboard(request):
    if not (request.user.groups.filter(name='director').exists() or request.user.is_superuser):
        raise PermissionDenied

    stats_qs, content_qs = DashboardService.apply_filters(request.GET)

    metrics = stats_qs.aggregate(sc=Sum('total_clicks'), sf=Sum('total_favorites'))
    totals = {'clicks': metrics['sc'] or 0, 'favs': metrics['sf'] or 0}

    top_p = stats_qs.values('platform__platform_name').annotate(c=Sum('total_clicks')).order_by('-c').first()

    trending = content_qs.annotate(
        fav_count=Count('favorite')
    ).select_related('genre', 'country', 'director').order_by('-fav_count')[:10]

    if request.GET.get('export') == 'csv':
        return DashboardService.get_csv_response(trending, totals, top_p)

    chart_qs = stats_qs.values('week').annotate(c=Sum('total_clicks')).order_by('week')

    if chart_qs.exists():
        labels = [d['week'].strftime('%d %b') for d in chart_qs]
        values = [d['c'] for d in chart_qs]
    else:
        labels, values = ["No Data"], [0]

    return render(request, 'pages/direction_dashboard.html', {
        'total_clicks': f"{totals['clicks']:,}".replace(",", "."),
        'total_favorites': f"{totals['favs']:,}".replace(",", "."),
        'top_platform': top_p,
        'trending_content': trending,
        'platforms': Platform.objects.all(),
        'countries': Country.objects.all(),
        'genres': Genre.objects.all(),
        'chart_labels': json.dumps(labels),
        'chart_values': json.dumps(values),
        'filters': request.GET
    })

```
<!-- END_FILE -->

---
<!-- FILE: docker-compose.yml -->
## docker-compose.yml

```yaml
# Docker Compose file -- defines how to run the project's containers

services:
  # The Django web application
  web:
    # Build the image using the Dockerfile in the current directory (./Dockerfile)
    build: .

    environment:
      SECRET_KEY: ${SECRET_KEY}
      DEBUG: ${DEBUG}
      ALLOWED_HOSTS: ${ALLOWED_HOSTS}
      API_KEY_LOCAL_1: ${API_KEY_LOCAL_1}
      API_KEY_LOCAL_2: ${API_KEY_LOCAL_2}
      API_KEY_LOCAL_3: ${API_KEY_LOCAL_3}

    # Map port 8000 on your machine to port 8000 in the container
    # Access the app at http://localhost:8000
    ports:
      - "8000:8000"

    # Mount the current directory into /app in the container
    # This means code changes on your machine are reflected instantly (live reload)
    volumes:
      - .:/app  # "." = your project folder, "/app" = where it goes inside the container
      - /app/.venv

```
<!-- END_FILE -->

---
<!-- FILE: Dockerfile -->
## Dockerfile

```
# Use Python 3.13 as base image
FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files first (better Docker cache)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy project
COPY . .

# Execution permits to entrypoint.sh
RUN chmod +x entrypoint.sh

# Expose port
EXPOSE 8000

# Start server
CMD ["./entrypoint.sh"]

```
<!-- END_FILE -->

---
<!-- FILE: entrypoint.sh -->
## entrypoint.sh

```sh
#!/bin/sh
set -e

uv run python manage.py migrate

uv run python manage.py collectstatic --noinput

exec uv run gunicorn SoftwareProject.wsgi:application --bind 0.0.0.0:8000

```
<!-- END_FILE -->

---
<!-- FILE: IshikawaTools/chart.py -->
## IshikawaTools/chart.py

```py
import os
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
from decouple import config

# ── Configuración ──────────────────────────────────────────────────────────────
REPO = "TralaleritosTralalas/SoftwareProject"
TOKEN=***REDACTED***
OWNER, REPO_NAME = REPO.split("/")

INPUT_FILE = "IshikawaTools/issues.json"
OUTPUT_FILE = "pareto_report.png"

headers = {
    "X-GitHub-Api-Version": "2022-11-28",
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}

# ── Crear fichero si no existe ─────────────────────────────────────────────────
def ensure_issues_file(path: str):
    if os.path.exists(path):
        return

    print("issues.json no encontrado, descargando desde GitHub…")

    issues, page = [], 1
    while True:
        resp = requests.get(
            f"https://api.github.com/repos/{OWNER}/{REPO_NAME}/issues",
            headers=headers,
            params={"state": "all", "per_page": 100, "page": page},
        )
        resp.raise_for_status()
        batch = resp.json()

        if not batch:
            break

        issues.extend(i for i in batch if "pull_request" not in i)
        page += 1

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(issues, f, indent=2)

    print(f"issues.json creado con {len(issues)} issues")

# ── Carga ──────────────────────────────────────────────────────────────────────
def load_issues(path: str):
    with open(path, "r") as f:
        return json.load(f)

# ── Procesado ──────────────────────────────────────────────────────────────────
def build_dataframe(issues):
    all_labels = []

    for issue in issues:
        if issue["labels"]:
            for label in issue["labels"]:
                all_labels.append(label["name"])
        else:
            all_labels.append("Unlabeled")

    df = pd.Series(all_labels).value_counts().to_frame(name="frecuencia")
    df.index.name = "etiqueta"

    df["porcentaje"] = (df["frecuencia"] / df["frecuencia"].sum()) * 100
    df["acumulado"] = df["porcentaje"].cumsum()

    return df

# ── Gráfica ────────────────────────────────────────────────────────────────────
def plot_pareto(df):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.bar(df.index, df["frecuencia"], color="steelblue")
    ax1.set_ylabel("Cantidad de Issues", fontweight="bold")
    ax1.set_xlabel("Etiquetas", fontweight="bold")
    plt.xticks(rotation=45, ha="right")

    ax2 = ax1.twinx()
    ax2.plot(df.index, df["acumulado"], color="red", marker="D", ms=5)
    ax2.axhline(80, color="orange", linestyle="--", alpha=0.5)
    ax2.set_ylabel("Porcentaje Acumulado (%)", fontweight="bold")
    ax2.set_ylim(0, 110)

    plt.title("Diagrama de Pareto: Análisis de Etiquetas en Issues")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE)
    print(f"Gráfica guardada como {OUTPUT_FILE}")

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    ensure_issues_file(INPUT_FILE)

    print("Leyendo issues desde fichero…")
    issues = load_issues(INPUT_FILE)

    df = build_dataframe(issues)
    plot_pareto(df)

if __name__ == "__main__":
    main()

```
<!-- END_FILE -->

---
<!-- FILE: IshikawaTools/histogram.py -->
## IshikawaTools/histogram.py

```py
import calendar
import os
import json
import requests
from decouple import config
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# ── Configuración ──────────────────────────────────────────────────────────────
REPO = "TralaleritosTralalas/SoftwareProject"
TOKEN=***REDACTED***
OWNER, REPO_NAME = REPO.split("/")

INPUT_FILE = "IshikawaTools/issues.json"
OUTPUT_FILE = "issues_histogram.png"

headers = {
    "X-GitHub-Api-Version": "2022-11-28",
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}

# ── Crear fichero si no existe ─────────────────────────────────────────────────
def ensure_issues_file(path: str):
    if os.path.exists(path):
        return

    print("issues.json no encontrado, descargando desde GitHub…")

    issues, page = [], 1
    while True:
        resp = requests.get(
            f"https://api.github.com/repos/{OWNER}/{REPO_NAME}/issues",
            headers=headers,
            params={"state": "all", "per_page": 100, "page": page},
        )
        resp.raise_for_status()
        batch = resp.json()

        if not batch:
            break

        issues.extend(i for i in batch if "pull_request" not in i)
        page += 1

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(issues, f, indent=2)

    print(f"issues.json creado con {len(issues)} issues")

# ── Carga de datos──────────────────────────────────────────────────────────────
def load_issues(path: str):
    with open(path, "r") as f:
        return json.load(f)

# ── Parseo de fechas ───────────────────────────────────────────────────────────
def parse_dates(issues: list[dict]) -> list[tuple[datetime, datetime | None]]:
    result = []
    for issue in issues:
        created = datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        closed = (
            datetime.strptime(issue["closed_at"], "%Y-%m-%dT%H:%M:%SZ")
            if issue.get("closed_at")
            else None
        )
        result.append((created, closed))
    return result

# ── Semanas del mes con rango real (lun–dom) ───────────────────────────────────
def build_weeks(year: int, month: int) -> list[tuple[str, datetime, datetime]]:
    cal   = calendar.monthcalendar(year, month)
    weeks = []
    for i, week in enumerate(cal):
        days = [d for d in week if d != 0]
        if not days:
            continue
        start = datetime(year, month, days[0])
        end = datetime(year, month, days[-1], 23, 59, 59)
        weeks.append((f"Sem {i+1}\n({days[0]}-{days[-1]})", start, end))
    return weeks

# ── Conteo de issues abiertas en cada semana ───────────────────────────────────
def count_open_per_week(
    issue_dates: list[tuple[datetime, datetime | None]],
    weeks: list[tuple[str, datetime, datetime]],
) -> list[int]:
    counts = []
    for _, start, end in weeks:
        open_count = sum(
            1
            for created, closed in issue_dates
            if start <= created <= end and (closed is None)
        )
        counts.append(open_count)
    return counts

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    ensure_issues_file(INPUT_FILE)

    print("Leyendo issues desde fichero…")
    issues = load_issues(INPUT_FILE)
    issue_dates = parse_dates(issues)

    weeks = []
    weeks.extend(build_weeks(2026, 3))
    weeks.extend(build_weeks(2026, 4))
    weeks.extend(build_weeks(2026, 5))

    sprint_end_date = datetime(2026, 5, 5)
    weeks = [(l, s, e) for (l, s, e) in weeks if s <= sprint_end_date]

    counts = count_open_per_week(issue_dates, weeks)

    labels = [
        f"{datetime(start.year, start.month, 1).strftime('%b')} {label}"
        for label, start, _ in weeks
    ]

    fig, ax = plt.subplots(figsize=(14, 6))
    bars = ax.bar(labels, counts, color="#4C72B0", edgecolor="white")

    for bar, count in zip(bars, counts):
        if count > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.1,
                str(count),
                ha="center",
                va="bottom",
                fontweight="bold",
            )

    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel("Semanas del mes")
    ax.set_ylabel("Número de issues abiertas")
    ax.set_title("Issues abiertas por semana activas a día de hoy")
    ax.spines[["top", "right"]].set_visible(False)

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE)
    print(f"Gráfica guardada como {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

```
<!-- END_FILE -->

---
<!-- FILE: IshikawaTools/runchart.py -->
## IshikawaTools/runchart.py

```py
import os
import json
import requests
from decouple import config
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# ── Configuración ──────────────────────────────────────────────────────────────
REPO = "TralaleritosTralalas/SoftwareProject"
TOKEN=***REDACTED***
OWNER, REPO_NAME = REPO.split("/")

INPUT_FILE = "IshikawaTools/issues.json"
OUTPUT_FILE = "issue_runchart.png"

headers = {
    "X-GitHub-Api-Version": "2022-11-28",
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}

# ── Crear fichero si no existe ─────────────────────────────────────────────────
def ensure_issues_file(path: str):
    if os.path.exists(path):
        return

    print("issues.json no encontrado, descargando desde GitHub…")

    issues, page = [], 1
    while True:
        resp = requests.get(
            f"https://api.github.com/repos/{OWNER}/{REPO_NAME}/issues",
            headers=headers,
            params={"state": "all", "per_page": 100, "page": page},
        )
        resp.raise_for_status()
        batch = resp.json()

        if not batch:
            break

        issues.extend(i for i in batch if "pull_request" not in i)
        page += 1

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(issues, f, indent=2)

    print(f"issues.json creado con {len(issues)} issues")

# ── Carga ──────────────────────────────────────────────────────────────────────
def load_issues(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# ── Procesado ──────────────────────────────────────────────────────────────────
def compute_weekly_counts(issues):
    dates = []

    for issue in issues:
        dt_str = issue["created_at"].replace("Z", "+00:00")
        dates.append(datetime.fromisoformat(dt_str))

    min_date = min(dates)
    max_date = max(dates)

    start_week = min_date - timedelta(days=min_date.weekday())
    start_week = start_week.replace(hour=0, minute=0, second=0, microsecond=0)

    weekly_counts = {}
    current_week = start_week

    while current_week <= max_date + timedelta(days=7):
        week_label = current_week.strftime("%Y-W%W")
        weekly_counts[week_label] = 0
        current_week += timedelta(days=7)

    for dt in dates:
        week_label = dt.strftime("%Y-W%W")
        if week_label in weekly_counts:
            weekly_counts[week_label] += 1

    return weekly_counts

# ── Gráfica ────────────────────────────────────────────────────────────────────
def plot_runchart(weekly_counts):
    x_labels = list(weekly_counts.keys())
    y_values = list(weekly_counts.values())

    plt.figure(figsize=(12, 6))
    plt.plot(
        x_labels,
        y_values,
        marker="o",
        linestyle="-",
        color="#8957e5",
        linewidth=2,
    )

    plt.title("Issues Created Per Week", fontsize=16, fontweight="bold")
    plt.xlabel("Week (Year-Week Number)", fontsize=12)
    plt.ylabel("Number of New Issues", fontsize=12)

    plt.xticks(rotation=45, ha="right")

    max_issues = max(y_values) if y_values else 0
    plt.yticks(range(0, max_issues + 2))

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()

    plt.savefig(OUTPUT_FILE)
    print(f"Gráfica guardada como {OUTPUT_FILE}")

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    ensure_issues_file(INPUT_FILE)

    print("Leyendo issues desde fichero…")
    issues = load_issues(INPUT_FILE)

    weekly_counts = compute_weekly_counts(issues)
    plot_runchart(weekly_counts)

if __name__ == "__main__":
    main()

```
<!-- END_FILE -->

---
<!-- FILE: manage.py -->
## manage.py

```py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SoftwareProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

```
<!-- END_FILE -->

---
<!-- FILE: meeting_files/to_do_list.md -->
## meeting_files/to_do_list.md

```md
# QUALITAT TO DO

## High Priority
- Implement the CD pipelines from the other groups
- Interview with Marc
- Use Conventional Commits in the issues (DONE)
- Move Priority / Points / Sprint to tags and remove them from the Issues (DONE)

## Low Priority
- Write the issues in English (DONE)
- Rename the `.yml` files
- Add the date to the presentation

> **Note:** Update the presentation at every meeting.

```
<!-- END_FILE -->

---
<!-- FILE: pyproject.toml -->
## pyproject.toml

```toml
[project]
name = "softwareproject"
version = "1.0.0"
description = "Add your description here"
requires-python = ">=3.14"
dependencies = [
    "django>=6.0.2",
    "gunicorn>=25.1.0",
    "matplotlib>=3.10.8",
    "pandas>=3.0.1",
    "python-decouple>=3.8",
    "requests>=2.32.5",
    "whitenoise>=6.12.0",
]

```
<!-- END_FILE -->

---
<!-- FILE: SoftwareProject/__init__.py -->
## SoftwareProject/__init__.py

```py


```
<!-- END_FILE -->

---
<!-- FILE: SoftwareProject/asgi.py -->
## SoftwareProject/asgi.py

```py
"""
ASGI config for SoftwareProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SoftwareProject.settings')

application = get_asgi_application()

```
<!-- END_FILE -->

---
<!-- FILE: SoftwareProject/settings.py -->
## SoftwareProject/settings.py

```py
"""
Django settings for SoftwareProject project

Generated by 'django-admin startproject' using Django 6.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/6.0/ref/settings/
"""

from pathlib import Path
from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='unsafe-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)


ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="localhost,127.0.0.1,0.0.0.0",
    cast=Csv()
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'app.apps.MyAppConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SoftwareProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [BASE_DIR / "app" / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SoftwareProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [BASE_DIR / 'app' / 'static']

LOGIN_REDIRECT_URL = "/redirect/"
LOGOUT_REDIRECT_URL = "app:home"

# Custom user model

AUTH_USER_MODEL = 'app.User'

# Configuration for static files, such as CSS, JS and images
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

```
<!-- END_FILE -->

---
<!-- FILE: SoftwareProject/urls.py -->
## SoftwareProject/urls.py

```py
"""
URL configuration for SoftwareProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.tech_admin import tech_admin_site 
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include("app.urls")),
    path('tech/', tech_admin_site.urls),
]

```
<!-- END_FILE -->

---
<!-- FILE: SoftwareProject/wsgi.py -->
## SoftwareProject/wsgi.py

```py
"""
WSGI config for SoftwareProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SoftwareProject.settings')

application = get_wsgi_application()

```
<!-- END_FILE -->

---
<!-- FILE: uv.lock -->
## uv.lock

```
version = 1
revision = 3
requires-python = ">=3.14"
resolution-markers = [
    "sys_platform == 'win32'",
    "sys_platform == 'emscripten'",
    "sys_platform != 'emscripten' and sys_platform != 'win32'",
]

[[package]]
name = "asgiref"
version = "3.11.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/63/40/f03da1264ae8f7cfdbf9146542e5e7e8100a4c66ab48e791df9a03d3f6c0/asgiref-3.11.1.tar.gz", hash = "sha256:5f184dc43b7e763efe848065441eac62229c9f7b0475f41f80e207a114eda4ce", size = 38550, upload-time = "2026-02-03T13:30:14.33Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5c/0a/a72d10ed65068e115044937873362e6e32fab1b7dce0046aeb224682c989/asgiref-3.11.1-py3-none-any.whl", hash = "sha256:e8667a091e69529631969fd45dc268fa79b99c92c5fcdda727757e52146ec133", size = 24345, upload-time = "2026-02-03T13:30:13.039Z" },
]

[[package]]
name = "certifi"
version = "2026.2.25"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/af/2d/7bf41579a8986e348fa033a31cdd0e4121114f6bce2457e8876010b092dd/certifi-2026.2.25.tar.gz", hash = "sha256:e887ab5cee78ea814d3472169153c2d12cd43b14bd03329a39a9c6e2e80bfba7", size = 155029, upload-time = "2026-02-25T02:54:17.342Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/3c/c17fb3ca2d9c3acff52e30b309f538586f9f5b9c9cf454f3845fc9af4881/certifi-2026.2.25-py3-none-any.whl", hash = "sha256:027692e4402ad994f1c42e52a4997a9763c646b73e4096e4d5d6db8af1d6f0fa", size = 153684, upload-time = "2026-02-25T02:54:15.766Z" },
]

[[package]]
name = "charset-normalizer"
version = "3.4.5"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1d/35/02daf95b9cd686320bb622eb148792655c9412dbb9b67abb5694e5910a24/charset_normalizer-3.4.5.tar.gz", hash = "sha256:95adae7b6c42a6c5b5b559b1a99149f090a57128155daeea91732c8d970d8644", size = 134804, upload-time = "2026-03-06T06:03:19.46Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/43/be/0f0fd9bb4a7fa4fb5067fb7d9ac693d4e928d306f80a0d02bde43a7c4aee/charset_normalizer-3.4.5-cp314-cp314-macosx_10_15_universal2.whl", hash = "sha256:8197abe5ca1ffb7d91e78360f915eef5addff270f8a71c1fc5be24a56f3e4873", size = 280232, upload-time = "2026-03-06T06:02:01.508Z" },
    { url = "https://files.pythonhosted.org/packages/28/02/983b5445e4bef49cd8c9da73a8e029f0825f39b74a06d201bfaa2e55142a/charset_normalizer-3.4.5-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a2aecdb364b8a1802afdc7f9327d55dad5366bc97d8502d0f5854e50712dbc5f", size = 189688, upload-time = "2026-03-06T06:02:02.857Z" },
    { url = "https://files.pythonhosted.org/packages/d0/88/152745c5166437687028027dc080e2daed6fe11cfa95a22f4602591c42db/charset_normalizer-3.4.5-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:a66aa5022bf81ab4b1bebfb009db4fd68e0c6d4307a1ce5ef6a26e5878dfc9e4", size = 206833, upload-time = "2026-03-06T06:02:05.127Z" },
    { url = "https://files.pythonhosted.org/packages/cb/0f/ebc15c8b02af2f19be9678d6eed115feeeccc45ce1f4b098d986c13e8769/charset_normalizer-3.4.5-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:d77f97e515688bd615c1d1f795d540f32542d514242067adcb8ef532504cb9ee", size = 202879, upload-time = "2026-03-06T06:02:06.446Z" },
    { url = "https://files.pythonhosted.org/packages/38/9c/71336bff6934418dc8d1e8a1644176ac9088068bc571da612767619c97b3/charset_normalizer-3.4.5-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01a1ed54b953303ca7e310fafe0fe347aab348bd81834a0bcd602eb538f89d66", size = 195764, upload-time = "2026-03-06T06:02:08.763Z" },
    { url = "https://files.pythonhosted.org/packages/b7/95/ce92fde4f98615661871bc282a856cf9b8a15f686ba0af012984660d480b/charset_normalizer-3.4.5-cp314-cp314-manylinux_2_31_armv7l.whl", hash = "sha256:b2d37d78297b39a9eb9eb92c0f6df98c706467282055419df141389b23f93362", size = 183728, upload-time = "2026-03-06T06:02:10.137Z" },
    { url = "https://files.pythonhosted.org/packages/1c/e7/f5b4588d94e747ce45ae680f0f242bc2d98dbd4eccfab73e6160b6893893/charset_normalizer-3.4.5-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e71bbb595973622b817c042bd943c3f3667e9c9983ce3d205f973f486fec98a7", size = 192937, upload-time = "2026-03-06T06:02:11.663Z" },
    { url = "https://files.pythonhosted.org/packages/f9/29/9d94ed6b929bf9f48bf6ede6e7474576499f07c4c5e878fb186083622716/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:4cd966c2559f501c6fd69294d082c2934c8dd4719deb32c22961a5ac6db0df1d", size = 192040, upload-time = "2026-03-06T06:02:13.489Z" },
    { url = "https://files.pythonhosted.org/packages/15/d2/1a093a1cf827957f9445f2fe7298bcc16f8fc5e05c1ed2ad1af0b239035e/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:d5e52d127045d6ae01a1e821acfad2f3a1866c54d0e837828538fabe8d9d1bd6", size = 184107, upload-time = "2026-03-06T06:02:14.83Z" },
    { url = "https://files.pythonhosted.org/packages/0f/7d/82068ce16bd36135df7b97f6333c5d808b94e01d4599a682e2337ed5fd14/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:30a2b1a48478c3428d047ed9690d57c23038dac838a87ad624c85c0a78ebeb39", size = 208310, upload-time = "2026-03-06T06:02:16.165Z" },
    { url = "https://files.pythonhosted.org/packages/84/4e/4dfb52307bb6af4a5c9e73e482d171b81d36f522b21ccd28a49656baa680/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:d8ed79b8f6372ca4254955005830fd61c1ccdd8c0fac6603e2c145c61dd95db6", size = 192918, upload-time = "2026-03-06T06:02:18.144Z" },
    { url = "https://files.pythonhosted.org/packages/08/a4/159ff7da662cf7201502ca89980b8f06acf3e887b278956646a8aeb178ab/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:c5af897b45fa606b12464ccbe0014bbf8c09191e0a66aab6aa9d5cf6e77e0c94", size = 204615, upload-time = "2026-03-06T06:02:19.821Z" },
    { url = "https://files.pythonhosted.org/packages/d6/62/0dd6172203cb6b429ffffc9935001fde42e5250d57f07b0c28c6046deb6b/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:1088345bcc93c58d8d8f3d783eca4a6e7a7752bbff26c3eee7e73c597c191c2e", size = 197784, upload-time = "2026-03-06T06:02:21.86Z" },
    { url = "https://files.pythonhosted.org/packages/c7/5e/1aab5cb737039b9c59e63627dc8bbc0d02562a14f831cc450e5f91d84ce1/charset_normalizer-3.4.5-cp314-cp314-win32.whl", hash = "sha256:ee57b926940ba00bca7ba7041e665cc956e55ef482f851b9b65acb20d867e7a2", size = 133009, upload-time = "2026-03-06T06:02:23.289Z" },
    { url = "https://files.pythonhosted.org/packages/40/65/e7c6c77d7aaa4c0d7974f2e403e17f0ed2cb0fc135f77d686b916bf1eead/charset_normalizer-3.4.5-cp314-cp314-win_amd64.whl", hash = "sha256:4481e6da1830c8a1cc0b746b47f603b653dadb690bcd851d039ffaefe70533aa", size = 143511, upload-time = "2026-03-06T06:02:26.195Z" },
    { url = "https://files.pythonhosted.org/packages/ba/91/52b0841c71f152f563b8e072896c14e3d83b195c188b338d3cc2e582d1d4/charset_normalizer-3.4.5-cp314-cp314-win_arm64.whl", hash = "sha256:97ab7787092eb9b50fb47fa04f24c75b768a606af1bcba1957f07f128a7219e4", size = 133775, upload-time = "2026-03-06T06:02:27.473Z" },
    { url = "https://files.pythonhosted.org/packages/c5/60/3a621758945513adfd4db86827a5bafcc615f913dbd0b4c2ed64a65731be/charset_normalizer-3.4.5-py3-none-any.whl", hash = "sha256:9db5e3fcdcee89a78c04dffb3fe33c79f77bd741a624946db2591c81b2fc85b0", size = 55455, upload-time = "2026-03-06T06:03:17.827Z" },
]

[[package]]
name = "contourpy"
version = "1.3.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "numpy" },
]
sdist = { url = "https://files.pythonhosted.org/packages/58/01/1253e6698a07380cd31a736d248a3f2a50a7c88779a1813da27503cadc2a/contourpy-1.3.3.tar.gz", hash = "sha256:083e12155b210502d0bca491432bb04d56dc3432f95a979b429f2848c3dbe880", size = 13466174, upload-time = "2025-07-26T12:03:12.549Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/72/8b/4546f3ab60f78c514ffb7d01a0bd743f90de36f0019d1be84d0a708a580a/contourpy-1.3.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:fde6c716d51c04b1c25d0b90364d0be954624a0ee9d60e23e850e8d48353d07a", size = 292189, upload-time = "2025-07-26T12:02:16.095Z" },
    { url = "https://files.pythonhosted.org/packages/fd/e1/3542a9cb596cadd76fcef413f19c79216e002623158befe6daa03dbfa88c/contourpy-1.3.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:cbedb772ed74ff5be440fa8eee9bd49f64f6e3fc09436d9c7d8f1c287b121d77", size = 273251, upload-time = "2025-07-26T12:02:17.524Z" },
    { url = "https://files.pythonhosted.org/packages/b1/71/f93e1e9471d189f79d0ce2497007731c1e6bf9ef6d1d61b911430c3db4e5/contourpy-1.3.3-cp314-cp314-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:22e9b1bd7a9b1d652cd77388465dc358dafcd2e217d35552424aa4f996f524f5", size = 335810, upload-time = "2025-07-26T12:02:18.9Z" },
    { url = "https://files.pythonhosted.org/packages/91/f9/e35f4c1c93f9275d4e38681a80506b5510e9327350c51f8d4a5a724d178c/contourpy-1.3.3-cp314-cp314-manylinux_2_26_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:a22738912262aa3e254e4f3cb079a95a67132fc5a063890e224393596902f5a4", size = 382871, upload-time = "2025-07-26T12:02:20.418Z" },
    { url = "https://files.pythonhosted.org/packages/b5/71/47b512f936f66a0a900d81c396a7e60d73419868fba959c61efed7a8ab46/contourpy-1.3.3-cp314-cp314-manylinux_2_26_s390x.manylinux_2_28_s390x.whl", hash = "sha256:afe5a512f31ee6bd7d0dda52ec9864c984ca3d66664444f2d72e0dc4eb832e36", size = 386264, upload-time = "2025-07-26T12:02:21.916Z" },
    { url = "https://files.pythonhosted.org/packages/04/5f/9ff93450ba96b09c7c2b3f81c94de31c89f92292f1380261bd7195bea4ea/contourpy-1.3.3-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f64836de09927cba6f79dcd00fdd7d5329f3fccc633468507079c829ca4db4e3", size = 363819, upload-time = "2025-07-26T12:02:23.759Z" },
    { url = "https://files.pythonhosted.org/packages/3e/a6/0b185d4cc480ee494945cde102cb0149ae830b5fa17bf855b95f2e70ad13/contourpy-1.3.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:1fd43c3be4c8e5fd6e4f2baeae35ae18176cf2e5cced681cca908addf1cdd53b", size = 1333650, upload-time = "2025-07-26T12:02:26.181Z" },
    { url = "https://files.pythonhosted.org/packages/43/d7/afdc95580ca56f30fbcd3060250f66cedbde69b4547028863abd8aa3b47e/contourpy-1.3.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:6afc576f7b33cf00996e5c1102dc2a8f7cc89e39c0b55df93a0b78c1bd992b36", size = 1404833, upload-time = "2025-07-26T12:02:28.782Z" },
    { url = "https://files.pythonhosted.org/packages/e2/e2/366af18a6d386f41132a48f033cbd2102e9b0cf6345d35ff0826cd984566/contourpy-1.3.3-cp314-cp314-win32.whl", hash = "sha256:66c8a43a4f7b8df8b71ee1840e4211a3c8d93b214b213f590e18a1beca458f7d", size = 189692, upload-time = "2025-07-26T12:02:30.128Z" },
    { url = "https://files.pythonhosted.org/packages/7d/c2/57f54b03d0f22d4044b8afb9ca0e184f8b1afd57b4f735c2fa70883dc601/contourpy-1.3.3-cp314-cp314-win_amd64.whl", hash = "sha256:cf9022ef053f2694e31d630feaacb21ea24224be1c3ad0520b13d844274614fd", size = 232424, upload-time = "2025-07-26T12:02:31.395Z" },
    { url = "https://files.pythonhosted.org/packages/18/79/a9416650df9b525737ab521aa181ccc42d56016d2123ddcb7b58e926a42c/contourpy-1.3.3-cp314-cp314-win_arm64.whl", hash = "sha256:95b181891b4c71de4bb404c6621e7e2390745f887f2a026b2d99e92c17892339", size = 198300, upload-time = "2025-07-26T12:02:32.956Z" },
    { url = "https://files.pythonhosted.org/packages/1f/42/38c159a7d0f2b7b9c04c64ab317042bb6952b713ba875c1681529a2932fe/contourpy-1.3.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:33c82d0138c0a062380332c861387650c82e4cf1747aaa6938b9b6516762e772", size = 306769, upload-time = "2025-07-26T12:02:34.2Z" },
    { url = "https://files.pythonhosted.org/packages/c3/6c/26a8205f24bca10974e77460de68d3d7c63e282e23782f1239f226fcae6f/contourpy-1.3.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:ea37e7b45949df430fe649e5de8351c423430046a2af20b1c1961cae3afcda77", size = 287892, upload-time = "2025-07-26T12:02:35.807Z" },
    { url = "https://files.pythonhosted.org/packages/66/06/8a475c8ab718ebfd7925661747dbb3c3ee9c82ac834ccb3570be49d129f4/contourpy-1.3.3-cp314-cp314t-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d304906ecc71672e9c89e87c4675dc5c2645e1f4269a5063b99b0bb29f232d13", size = 326748, upload-time = "2025-07-26T12:02:37.193Z" },
    { url = "https://files.pythonhosted.org/packages/b4/a3/c5ca9f010a44c223f098fccd8b158bb1cb287378a31ac141f04730dc49be/contourpy-1.3.3-cp314-cp314t-manylinux_2_26_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:ca658cd1a680a5c9ea96dc61cdbae1e85c8f25849843aa799dfd3cb370ad4fbe", size = 375554, upload-time = "2025-07-26T12:02:38.894Z" },
    { url = "https://files.pythonhosted.org/packages/80/5b/68bd33ae63fac658a4145088c1e894405e07584a316738710b636c6d0333/contourpy-1.3.3-cp314-cp314t-manylinux_2_26_s390x.manylinux_2_28_s390x.whl", hash = "sha256:ab2fd90904c503739a75b7c8c5c01160130ba67944a7b77bbf36ef8054576e7f", size = 388118, upload-time = "2025-07-26T12:02:40.642Z" },
    { url = "https://files.pythonhosted.org/packages/40/52/4c285a6435940ae25d7410a6c36bda5145839bc3f0beb20c707cda18b9d2/contourpy-1.3.3-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b7301b89040075c30e5768810bc96a8e8d78085b47d8be6e4c3f5a0b4ed478a0", size = 352555, upload-time = "2025-07-26T12:02:42.25Z" },
    { url = "https://files.pythonhosted.org/packages/24/ee/3e81e1dd174f5c7fefe50e85d0892de05ca4e26ef1c9a59c2a57e43b865a/contourpy-1.3.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:2a2a8b627d5cc6b7c41a4beff6c5ad5eb848c88255fda4a8745f7e901b32d8e4", size = 1322295, upload-time = "2025-07-26T12:02:44.668Z" },
    { url = "https://files.pythonhosted.org/packages/3c/b2/6d913d4d04e14379de429057cd169e5e00f6c2af3bb13e1710bcbdb5da12/contourpy-1.3.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:fd6ec6be509c787f1caf6b247f0b1ca598bef13f4ddeaa126b7658215529ba0f", size = 1391027, upload-time = "2025-07-26T12:02:47.09Z" },
    { url = "https://files.pythonhosted.org/packages/93/8a/68a4ec5c55a2971213d29a9374913f7e9f18581945a7a31d1a39b5d2dfe5/contourpy-1.3.3-cp314-cp314t-win32.whl", hash = "sha256:e74a9a0f5e3fff48fb5a7f2fd2b9b70a3fe014a67522f79b7cca4c0c7e43c9ae", size = 202428, upload-time = "2025-07-26T12:02:48.691Z" },
    { url = "https://files.pythonhosted.org/packages/fa/96/fd9f641ffedc4fa3ace923af73b9d07e869496c9cc7a459103e6e978992f/contourpy-1.3.3-cp314-cp314t-win_amd64.whl", hash = "sha256:13b68d6a62db8eafaebb8039218921399baf6e47bf85006fd8529f2a08ef33fc", size = 250331, upload-time = "2025-07-26T12:02:50.137Z" },
    { url = "https://files.pythonhosted.org/packages/ae/8c/469afb6465b853afff216f9528ffda78a915ff880ed58813ba4faf4ba0b6/contourpy-1.3.3-cp314-cp314t-win_arm64.whl", hash = "sha256:b7448cb5a725bb1e35ce88771b86fba35ef418952474492cf7c764059933ff8b", size = 203831, upload-time = "2025-07-26T12:02:51.449Z" },
]

[[package]]
name = "cycler"
version = "0.12.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a9/95/a3dbbb5028f35eafb79008e7522a75244477d2838f38cbb722248dabc2a8/cycler-0.12.1.tar.gz", hash = "sha256:88bb128f02ba341da8ef447245a9e138fae777f6a23943da4540077d3601eb1c", size = 7615, upload-time = "2023-10-07T05:32:18.335Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e7/05/c19819d5e3d95294a6f5947fb9b9629efb316b96de511b418c53d245aae6/cycler-0.12.1-py3-none-any.whl", hash = "sha256:85cef7cff222d8644161529808465972e51340599459b8ac3ccbac5a854e0d30", size = 8321, upload-time = "2023-10-07T05:32:16.783Z" },
]

[[package]]
name = "django"
version = "6.0.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "asgiref" },
    { name = "sqlparse" },
    { name = "tzdata", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/26/3e/a1c4207c5dea4697b7a3387e26584919ba987d8f9320f59dc0b5c557a4eb/django-6.0.2.tar.gz", hash = "sha256:3046a53b0e40d4b676c3b774c73411d7184ae2745fe8ce5e45c0f33d3ddb71a7", size = 10886874, upload-time = "2026-02-03T13:50:31.596Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/96/ba/a6e2992bc5b8c688249c00ea48cb1b7a9bc09839328c81dc603671460928/django-6.0.2-py3-none-any.whl", hash = "sha256:610dd3b13d15ec3f1e1d257caedd751db8033c5ad8ea0e2d1219a8acf446ecc6", size = 8339381, upload-time = "2026-02-03T13:50:15.501Z" },
]

[[package]]
name = "fonttools"
version = "4.62.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/5a/96/686339e0fda8142b7ebed39af53f4a5694602a729662f42a6209e3be91d0/fonttools-4.62.0.tar.gz", hash = "sha256:0dc477c12b8076b4eb9af2e440421b0433ffa9e1dcb39e0640a6c94665ed1098", size = 3579521, upload-time = "2026-03-09T16:50:06.217Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1a/64/61f69298aa6e7c363dcf00dd6371a654676900abe27d1effd1a74b43e5d0/fonttools-4.62.0-cp314-cp314-macosx_10_15_universal2.whl", hash = "sha256:4fa5a9c716e2f75ef34b5a5c2ca0ee4848d795daa7e6792bf30fd4abf8993449", size = 2864222, upload-time = "2026-03-09T16:49:28.285Z" },
    { url = "https://files.pythonhosted.org/packages/c6/57/6b08756fe4455336b1fe160ab3c11fccc90768ccb6ee03fb0b45851aace4/fonttools-4.62.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:625f5cbeb0b8f4e42343eaeb4bc2786718ddd84760a2f5e55fdd3db049047c00", size = 2410674, upload-time = "2026-03-09T16:49:30.504Z" },
    { url = "https://files.pythonhosted.org/packages/6f/86/db65b63bb1b824b63e602e9be21b18741ddc99bcf5a7850f9181159ae107/fonttools-4.62.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6247e58b96b982709cd569a91a2ba935d406dccf17b6aa615afaed37ac3856aa", size = 4999387, upload-time = "2026-03-09T16:49:32.593Z" },
    { url = "https://files.pythonhosted.org/packages/86/c8/c6669e42d2f4efd60d38a3252cebbb28851f968890efb2b9b15f9d1092b0/fonttools-4.62.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:840632ea9c1eab7b7f01c369e408c0721c287dfd7500ab937398430689852fd1", size = 4912506, upload-time = "2026-03-09T16:49:34.927Z" },
    { url = "https://files.pythonhosted.org/packages/2e/49/0ae552aa098edd0ec548413fbf818f52ceb70535016215094a5ce9bf8f70/fonttools-4.62.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:28a9ea2a7467a816d1bec22658b0cce4443ac60abac3e293bdee78beb74588f3", size = 4951202, upload-time = "2026-03-09T16:49:37.1Z" },
    { url = "https://files.pythonhosted.org/packages/71/65/ae38fc8a4cea6f162d74cf11f58e9aeef1baa7d0e3d1376dabd336c129e5/fonttools-4.62.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:5ae611294f768d413949fd12693a8cba0e6332fbc1e07aba60121be35eac68d0", size = 5060758, upload-time = "2026-03-09T16:49:39.464Z" },
    { url = "https://files.pythonhosted.org/packages/db/3d/bb797496f35c60544cd5af71ffa5aad62df14ef7286908d204cb5c5096fe/fonttools-4.62.0-cp314-cp314-win32.whl", hash = "sha256:273acb61f316d07570a80ed5ff0a14a23700eedbec0ad968b949abaa4d3f6bb5", size = 2283496, upload-time = "2026-03-09T16:49:42.448Z" },
    { url = "https://files.pythonhosted.org/packages/2e/9f/91081ffe5881253177c175749cce5841f5ec6e931f5d52f4a817207b7429/fonttools-4.62.0-cp314-cp314-win_amd64.whl", hash = "sha256:a5f974006d14f735c6c878fc4b117ad031dc93638ddcc450ca69f8fd64d5e104", size = 2335426, upload-time = "2026-03-09T16:49:44.228Z" },
    { url = "https://files.pythonhosted.org/packages/f8/65/f47f9b3db1ec156a1f222f1089ba076b2cc9ee1d024a8b0a60c54258517e/fonttools-4.62.0-cp314-cp314t-macosx_10_15_universal2.whl", hash = "sha256:0361a7d41d86937f1f752717c19f719d0fde064d3011038f9f19bdf5fc2f5c95", size = 2947079, upload-time = "2026-03-09T16:49:46.471Z" },
    { url = "https://files.pythonhosted.org/packages/52/73/bc62e5058a0c22cf02b1e0169ef0c3ca6c3247216d719f95bead3c05a991/fonttools-4.62.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:d4108c12773b3c97aa592311557c405d5b4fc03db2b969ed928fcf68e7b3c887", size = 2448802, upload-time = "2026-03-09T16:49:48.328Z" },
    { url = "https://files.pythonhosted.org/packages/2b/df/bfaa0e845884935355670e6e68f137185ab87295f8bc838db575e4a66064/fonttools-4.62.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b448075f32708e8fb377fe7687f769a5f51a027172c591ba9a58693631b077a8", size = 5137378, upload-time = "2026-03-09T16:49:50.223Z" },
    { url = "https://files.pythonhosted.org/packages/32/32/04f616979a18b48b52e634988b93d847b6346260faf85ecccaf7e2e9057f/fonttools-4.62.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:e5f1fa8cc9f1a56a3e33ee6b954d6d9235e6b9d11eb7a6c9dfe2c2f829dc24db", size = 4920714, upload-time = "2026-03-09T16:49:53.172Z" },
    { url = "https://files.pythonhosted.org/packages/3b/2e/274e16689c1dfee5c68302cd7c444213cfddd23cf4620374419625037ec6/fonttools-4.62.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:f8c8ea812f82db1e884b9cdb663080453e28f0f9a1f5027a5adb59c4cc8d38d1", size = 5016012, upload-time = "2026-03-09T16:49:55.762Z" },
    { url = "https://files.pythonhosted.org/packages/7f/0c/b08117270626e7117ac2f89d732fdd4386ec37d2ab3a944462d29e6f89a1/fonttools-4.62.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:03c6068adfdc67c565d217e92386b1cdd951abd4240d65180cec62fa74ba31b2", size = 5042766, upload-time = "2026-03-09T16:49:57.726Z" },
    { url = "https://files.pythonhosted.org/packages/11/83/a48b73e54efa272ee65315a6331b30a9b3a98733310bc11402606809c50e/fonttools-4.62.0-cp314-cp314t-win32.whl", hash = "sha256:d28d5baacb0017d384df14722a63abe6e0230d8ce642b1615a27d78ffe3bc983", size = 2347785, upload-time = "2026-03-09T16:49:59.698Z" },
    { url = "https://files.pythonhosted.org/packages/f8/27/c67eab6dc3525bdc39586511b1b3d7161e972dacc0f17476dbaf932e708b/fonttools-4.62.0-cp314-cp314t-win_amd64.whl", hash = "sha256:3f9e20c4618f1e04190c802acae6dc337cb6db9fa61e492fd97cd5c5a9ff6d07", size = 2413914, upload-time = "2026-03-09T16:50:02.251Z" },
    { url = "https://files.pythonhosted.org/packages/9c/57/c2487c281dde03abb2dec244fd67059b8d118bd30a653cbf69e94084cb23/fonttools-4.62.0-py3-none-any.whl", hash = "sha256:75064f19a10c50c74b336aa5ebe7b1f89fd0fb5255807bfd4b0c6317098f4af3", size = 1152427, upload-time = "2026-03-09T16:50:04.074Z" },
]

[[package]]
name = "gunicorn"
version = "25.1.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "packaging" },
]
sdist = { url = "https://files.pythonhosted.org/packages/66/13/ef67f59f6a7896fdc2c1d62b5665c5219d6b0a9a1784938eb9a28e55e128/gunicorn-25.1.0.tar.gz", hash = "sha256:1426611d959fa77e7de89f8c0f32eed6aa03ee735f98c01efba3e281b1c47616", size = 594377, upload-time = "2026-02-13T11:09:58.989Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/da/73/4ad5b1f6a2e21cf1e85afdaad2b7b1a933985e2f5d679147a1953aaa192c/gunicorn-25.1.0-py3-none-any.whl", hash = "sha256:d0b1236ccf27f72cfe14bce7caadf467186f19e865094ca84221424e839b8b8b", size = 197067, upload-time = "2026-02-13T11:09:57.146Z" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "kiwisolver"
version = "1.5.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d0/67/9c61eccb13f0bdca9307614e782fec49ffdde0f7a2314935d489fa93cd9c/kiwisolver-1.5.0.tar.gz", hash = "sha256:d4193f3d9dc3f6f79aaed0e5637f45d98850ebf01f7ca20e69457f3e8946b66a", size = 103482, upload-time = "2026-03-09T13:15:53.382Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e4/d7/060f45052f2a01ad5762c8fdecd6d7a752b43400dc29ff75cd47225a40fd/kiwisolver-1.5.0-cp314-cp314-macosx_10_15_universal2.whl", hash = "sha256:8df31fe574b8b3993cc61764f40941111b25c2d9fea13d3ce24a49907cd2d615", size = 123231, upload-time = "2026-03-09T13:14:41.323Z" },
    { url = "https://files.pythonhosted.org/packages/c2/a7/78da680eadd06ff35edef6ef68a1ad273bad3e2a0936c9a885103230aece/kiwisolver-1.5.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:1d49a49ac4cbfb7c1375301cd1ec90169dfeae55ff84710d782260ce77a75a02", size = 66489, upload-time = "2026-03-09T13:14:42.534Z" },
    { url = "https://files.pythonhosted.org/packages/49/b2/97980f3ad4fae37dd7fe31626e2bf75fbf8bdf5d303950ec1fab39a12da8/kiwisolver-1.5.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:0cbe94b69b819209a62cb27bdfa5dc2a8977d8de2f89dfd97ba4f53ed3af754e", size = 64063, upload-time = "2026-03-09T13:14:44.759Z" },
    { url = "https://files.pythonhosted.org/packages/e7/f9/b06c934a6aa8bc91f566bd2a214fd04c30506c2d9e2b6b171953216a65b6/kiwisolver-1.5.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:80aa065ffd378ff784822a6d7c3212f2d5f5e9c3589614b5c228b311fd3063ac", size = 1475913, upload-time = "2026-03-09T13:14:46.247Z" },
    { url = "https://files.pythonhosted.org/packages/6b/f0/f768ae564a710135630672981231320bc403cf9152b5596ec5289de0f106/kiwisolver-1.5.0-cp314-cp314-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4e7f886f47ab881692f278ae901039a234e4025a68e6dfab514263a0b1c4ae05", size = 1282782, upload-time = "2026-03-09T13:14:48.458Z" },
    { url = "https://files.pythonhosted.org/packages/e2/9f/1de7aad00697325f05238a5f2eafbd487fb637cc27a558b5367a5f37fb7f/kiwisolver-1.5.0-cp314-cp314-manylinux_2_24_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:5060731cc3ed12ca3a8b57acd4aeca5bbc2f49216dd0bec1650a1acd89486bcd", size = 1300815, upload-time = "2026-03-09T13:14:50.721Z" },
    { url = "https://files.pythonhosted.org/packages/5a/c2/297f25141d2e468e0ce7f7a7b92e0cf8918143a0cbd3422c1ad627e85a06/kiwisolver-1.5.0-cp314-cp314-manylinux_2_24_s390x.manylinux_2_28_s390x.whl", hash = "sha256:7a4aa69609f40fce3cbc3f87b2061f042eee32f94b8f11db707b66a26461591a", size = 1347925, upload-time = "2026-03-09T13:14:52.304Z" },
    { url = "https://files.pythonhosted.org/packages/b9/d3/f4c73a02eb41520c47610207b21afa8cdd18fdbf64ffd94674ae21c4812d/kiwisolver-1.5.0-cp314-cp314-manylinux_2_39_riscv64.whl", hash = "sha256:d168fda2dbff7b9b5f38e693182d792a938c31db4dac3a80a4888de603c99554", size = 991322, upload-time = "2026-03-09T13:14:54.637Z" },
    { url = "https://files.pythonhosted.org/packages/7b/46/d3f2efef7732fcda98d22bf4ad5d3d71d545167a852ca710a494f4c15343/kiwisolver-1.5.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:413b820229730d358efd838ecbab79902fe97094565fdc80ddb6b0a18c18a581", size = 2232857, upload-time = "2026-03-09T13:14:56.471Z" },
    { url = "https://files.pythonhosted.org/packages/3f/ec/2d9756bf2b6d26ae4349b8d3662fb3993f16d80c1f971c179ce862b9dbae/kiwisolver-1.5.0-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:5124d1ea754509b09e53738ec185584cc609aae4a3b510aaf4ed6aa047ef9303", size = 2329376, upload-time = "2026-03-09T13:14:58.072Z" },
    { url = "https://files.pythonhosted.org/packages/8f/9f/876a0a0f2260f1bde92e002b3019a5fabc35e0939c7d945e0fa66185eb20/kiwisolver-1.5.0-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:e4415a8db000bf49a6dd1c478bf70062eaacff0f462b92b0ba68791a905861f9", size = 1982549, upload-time = "2026-03-09T13:14:59.668Z" },
    { url = "https://files.pythonhosted.org/packages/6c/4f/ba3624dfac23a64d54ac4179832860cb537c1b0af06024936e82ca4154a0/kiwisolver-1.5.0-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:d618fd27420381a4f6044faa71f46d8bfd911bd077c555f7138ed88729bfbe79", size = 2494680, upload-time = "2026-03-09T13:15:01.364Z" },
    { url = "https://files.pythonhosted.org/packages/39/b7/97716b190ab98911b20d10bf92eca469121ec483b8ce0edd314f51bc85af/kiwisolver-1.5.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:5092eb5b1172947f57d6ea7d89b2f29650414e4293c47707eb499ec07a0ac796", size = 2297905, upload-time = "2026-03-09T13:15:03.925Z" },
    { url = "https://files.pythonhosted.org/packages/a3/36/4e551e8aa55c9188bca9abb5096805edbf7431072b76e2298e34fd3a3008/kiwisolver-1.5.0-cp314-cp314-win_amd64.whl", hash = "sha256:d76e2d8c75051d58177e762164d2e9ab92886534e3a12e795f103524f221dd8e", size = 75086, upload-time = "2026-03-09T13:15:07.775Z" },
    { url = "https://files.pythonhosted.org/packages/70/15/9b90f7df0e31a003c71649cf66ef61c3c1b862f48c81007fa2383c8bd8d7/kiwisolver-1.5.0-cp314-cp314-win_arm64.whl", hash = "sha256:fa6248cd194edff41d7ea9425ced8ca3a6f838bfb295f6f1d6e6bb694a8518df", size = 66577, upload-time = "2026-03-09T13:15:09.139Z" },
    { url = "https://files.pythonhosted.org/packages/17/01/7dc8c5443ff42b38e72731643ed7cf1ed9bf01691ae5cdca98501999ed83/kiwisolver-1.5.0-cp314-cp314t-macosx_10_15_universal2.whl", hash = "sha256:d1ffeb80b5676463d7a7d56acbe8e37a20ce725570e09549fe738e02ca6b7e1e", size = 125794, upload-time = "2026-03-09T13:15:10.525Z" },
    { url = "https://files.pythonhosted.org/packages/46/8a/b4ebe46ebaac6a303417fab10c2e165c557ddaff558f9699d302b256bc53/kiwisolver-1.5.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:bc4d8e252f532ab46a1de9349e2d27b91fce46736a9eedaa37beaca66f574ed4", size = 67646, upload-time = "2026-03-09T13:15:12.016Z" },
    { url = "https://files.pythonhosted.org/packages/60/35/10a844afc5f19d6f567359bf4789e26661755a2f36200d5d1ed8ad0126e5/kiwisolver-1.5.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:6783e069732715ad0c3ce96dbf21dbc2235ab0593f2baf6338101f70371f4028", size = 65511, upload-time = "2026-03-09T13:15:13.311Z" },
    { url = "https://files.pythonhosted.org/packages/f8/8a/685b297052dd041dcebce8e8787b58923b6e78acc6115a0dc9189011c44b/kiwisolver-1.5.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:e7c4c09a490dc4d4a7f8cbee56c606a320f9dc28cf92a7157a39d1ce7676a657", size = 1584858, upload-time = "2026-03-09T13:15:15.103Z" },
    { url = "https://files.pythonhosted.org/packages/9e/80/04865e3d4638ac5bddec28908916df4a3075b8c6cc101786a96803188b96/kiwisolver-1.5.0-cp314-cp314t-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:2a075bd7bd19c70cf67c8badfa36cf7c5d8de3c9ddb8420c51e10d9c50e94920", size = 1392539, upload-time = "2026-03-09T13:15:16.661Z" },
    { url = "https://files.pythonhosted.org/packages/ba/01/77a19cacc0893fa13fafa46d1bba06fb4dc2360b3292baf4b56d8e067b24/kiwisolver-1.5.0-cp314-cp314t-manylinux_2_24_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:bdd3e53429ff02aa319ba59dfe4ceeec345bf46cf180ec2cf6fd5b942e7975e9", size = 1405310, upload-time = "2026-03-09T13:15:18.229Z" },
    { url = "https://files.pythonhosted.org/packages/53/39/bcaf5d0cca50e604cfa9b4e3ae1d64b50ca1ae5b754122396084599ef903/kiwisolver-1.5.0-cp314-cp314t-manylinux_2_24_s390x.manylinux_2_28_s390x.whl", hash = "sha256:3cdcb35dc9d807259c981a85531048ede628eabcffb3239adf3d17463518992d", size = 1456244, upload-time = "2026-03-09T13:15:20.444Z" },
    { url = "https://files.pythonhosted.org/packages/d0/7a/72c187abc6975f6978c3e39b7cf67aeb8b3c0a8f9790aa7fd412855e9e1f/kiwisolver-1.5.0-cp314-cp314t-manylinux_2_39_riscv64.whl", hash = "sha256:70d593af6a6ca332d1df73d519fddb5148edb15cd90d5f0155e3746a6d4fcc65", size = 1073154, upload-time = "2026-03-09T13:15:22.039Z" },
    { url = "https://files.pythonhosted.org/packages/c7/ca/cf5b25783ebbd59143b4371ed0c8428a278abe68d6d0104b01865b1bbd0f/kiwisolver-1.5.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:377815a8616074cabbf3f53354e1d040c35815a134e01d7614b7692e4bf8acfa", size = 2334377, upload-time = "2026-03-09T13:15:23.741Z" },
    { url = "https://files.pythonhosted.org/packages/4a/e5/b1f492adc516796e88751282276745340e2a72dcd0d36cf7173e0daf3210/kiwisolver-1.5.0-cp314-cp314t-musllinux_1_2_ppc64le.whl", hash = "sha256:0255a027391d52944eae1dbb5d4cc5903f57092f3674e8e544cdd2622826b3f0", size = 2425288, upload-time = "2026-03-09T13:15:25.789Z" },
    { url = "https://files.pythonhosted.org/packages/e6/e5/9b21fbe91a61b8f409d74a26498706e97a48008bfcd1864373d32a6ba31c/kiwisolver-1.5.0-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:012b1eb16e28718fa782b5e61dc6f2da1f0792ca73bd05d54de6cb9561665fc9", size = 2063158, upload-time = "2026-03-09T13:15:27.63Z" },
    { url = "https://files.pythonhosted.org/packages/b1/02/83f47986138310f95ea95531f851b2a62227c11cbc3e690ae1374fe49f0f/kiwisolver-1.5.0-cp314-cp314t-musllinux_1_2_s390x.whl", hash = "sha256:0e3aafb33aed7479377e5e9a82e9d4bf87063741fc99fc7ae48b0f16e32bdd6f", size = 2597260, upload-time = "2026-03-09T13:15:29.421Z" },
    { url = "https://files.pythonhosted.org/packages/07/18/43a5f24608d8c313dd189cf838c8e68d75b115567c6279de7796197cfb6a/kiwisolver-1.5.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:e7a116ae737f0000343218c4edf5bd45893bfeaff0993c0b215d7124c9f77646", size = 2394403, upload-time = "2026-03-09T13:15:31.517Z" },
    { url = "https://files.pythonhosted.org/packages/3b/b5/98222136d839b8afabcaa943b09bd05888c2d36355b7e448550211d1fca4/kiwisolver-1.5.0-cp314-cp314t-win_amd64.whl", hash = "sha256:1dd9b0b119a350976a6d781e7278ec7aca0b201e1a9e2d23d9804afecb6ca681", size = 79687, upload-time = "2026-03-09T13:15:33.204Z" },
    { url = "https://files.pythonhosted.org/packages/99/a2/ca7dc962848040befed12732dff6acae7fb3c4f6fc4272b3f6c9a30b8713/kiwisolver-1.5.0-cp314-cp314t-win_arm64.whl", hash = "sha256:58f812017cd2985c21fbffb4864d59174d4903dd66fa23815e74bbc7a0e2dd57", size = 70032, upload-time = "2026-03-09T13:15:34.411Z" },
]

[[package]]
name = "matplotlib"
version = "3.10.8"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "contourpy" },
    { name = "cycler" },
    { name = "fonttools" },
    { name = "kiwisolver" },
    { name = "numpy" },
    { name = "packaging" },
    { name = "pillow" },
    { name = "pyparsing" },
    { name = "python-dateutil" },
]
sdist = { url = "https://files.pythonhosted.org/packages/8a/76/d3c6e3a13fe484ebe7718d14e269c9569c4eb0020a968a327acb3b9a8fe6/matplotlib-3.10.8.tar.gz", hash = "sha256:2299372c19d56bcd35cf05a2738308758d32b9eaed2371898d8f5bd33f084aa3", size = 34806269, upload-time = "2025-12-10T22:56:51.155Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/3c/43/9c0ff7a2f11615e516c3b058e1e6e8f9614ddeca53faca06da267c48345d/matplotlib-3.10.8-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:b53285e65d4fa4c86399979e956235deb900be5baa7fc1218ea67fbfaeaadd6f", size = 8262481, upload-time = "2025-12-10T22:56:10.885Z" },
    { url = "https://files.pythonhosted.org/packages/6f/ca/e8ae28649fcdf039fda5ef554b40a95f50592a3c47e6f7270c9561c12b07/matplotlib-3.10.8-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:32f8dce744be5569bebe789e46727946041199030db8aeb2954d26013a0eb26b", size = 8151473, upload-time = "2025-12-10T22:56:12.377Z" },
    { url = "https://files.pythonhosted.org/packages/f1/6f/009d129ae70b75e88cbe7e503a12a4c0670e08ed748a902c2568909e9eb5/matplotlib-3.10.8-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4cf267add95b1c88300d96ca837833d4112756045364f5c734a2276038dae27d", size = 9553896, upload-time = "2025-12-10T22:56:14.432Z" },
    { url = "https://files.pythonhosted.org/packages/f5/26/4221a741eb97967bc1fd5e4c52b9aa5a91b2f4ec05b59f6def4d820f9df9/matplotlib-3.10.8-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:2cf5bd12cecf46908f286d7838b2abc6c91cda506c0445b8223a7c19a00df008", size = 9824193, upload-time = "2025-12-10T22:56:16.29Z" },
    { url = "https://files.pythonhosted.org/packages/1f/f3/3abf75f38605772cf48a9daf5821cd4f563472f38b4b828c6fba6fa6d06e/matplotlib-3.10.8-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:41703cc95688f2516b480f7f339d8851a6035f18e100ee6a32bc0b8536a12a9c", size = 9615444, upload-time = "2025-12-10T22:56:18.155Z" },
    { url = "https://files.pythonhosted.org/packages/93/a5/de89ac80f10b8dc615807ee1133cd99ac74082581196d4d9590bea10690d/matplotlib-3.10.8-cp314-cp314-win_amd64.whl", hash = "sha256:83d282364ea9f3e52363da262ce32a09dfe241e4080dcedda3c0db059d3c1f11", size = 8272719, upload-time = "2025-12-10T22:56:20.366Z" },
    { url = "https://files.pythonhosted.org/packages/69/ce/b006495c19ccc0a137b48083168a37bd056392dee02f87dba0472f2797fe/matplotlib-3.10.8-cp314-cp314-win_arm64.whl", hash = "sha256:2c1998e92cd5999e295a731bcb2911c75f597d937341f3030cc24ef2733d78a8", size = 8144205, upload-time = "2025-12-10T22:56:22.239Z" },
    { url = "https://files.pythonhosted.org/packages/68/d9/b31116a3a855bd313c6fcdb7226926d59b041f26061c6c5b1be66a08c826/matplotlib-3.10.8-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:b5a2b97dbdc7d4f353ebf343744f1d1f1cca8aa8bfddb4262fcf4306c3761d50", size = 8305785, upload-time = "2025-12-10T22:56:24.218Z" },
    { url = "https://files.pythonhosted.org/packages/1e/90/6effe8103f0272685767ba5f094f453784057072f49b393e3ea178fe70a5/matplotlib-3.10.8-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:3f5c3e4da343bba819f0234186b9004faba952cc420fbc522dc4e103c1985908", size = 8198361, upload-time = "2025-12-10T22:56:26.787Z" },
    { url = "https://files.pythonhosted.org/packages/d7/65/a73188711bea603615fc0baecca1061429ac16940e2385433cc778a9d8e7/matplotlib-3.10.8-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5f62550b9a30afde8c1c3ae450e5eb547d579dd69b25c2fc7a1c67f934c1717a", size = 9561357, upload-time = "2025-12-10T22:56:28.953Z" },
    { url = "https://files.pythonhosted.org/packages/f4/3d/b5c5d5d5be8ce63292567f0e2c43dde9953d3ed86ac2de0a72e93c8f07a1/matplotlib-3.10.8-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:495672de149445ec1b772ff2c9ede9b769e3cb4f0d0aa7fa730d7f59e2d4e1c1", size = 9823610, upload-time = "2025-12-10T22:56:31.455Z" },
    { url = "https://files.pythonhosted.org/packages/4d/4b/e7beb6bbd49f6bae727a12b270a2654d13c397576d25bd6786e47033300f/matplotlib-3.10.8-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:595ba4d8fe983b88f0eec8c26a241e16d6376fe1979086232f481f8f3f67494c", size = 9614011, upload-time = "2025-12-10T22:56:33.85Z" },
    { url = "https://files.pythonhosted.org/packages/7c/e6/76f2813d31f032e65f6f797e3f2f6e4aab95b65015924b1c51370395c28a/matplotlib-3.10.8-cp314-cp314t-win_amd64.whl", hash = "sha256:25d380fe8b1dc32cf8f0b1b448470a77afb195438bafdf1d858bfb876f3edf7b", size = 8362801, upload-time = "2025-12-10T22:56:36.107Z" },
    { url = "https://files.pythonhosted.org/packages/5d/49/d651878698a0b67f23aa28e17f45a6d6dd3d3f933fa29087fa4ce5947b5a/matplotlib-3.10.8-cp314-cp314t-win_arm64.whl", hash = "sha256:113bb52413ea508ce954a02c10ffd0d565f9c3bc7f2eddc27dfe1731e71c7b5f", size = 8192560, upload-time = "2025-12-10T22:56:38.008Z" },
]

[[package]]
name = "numpy"
version = "2.4.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/10/8b/c265f4823726ab832de836cdd184d0986dcf94480f81e8739692a7ac7af2/numpy-2.4.3.tar.gz", hash = "sha256:483a201202b73495f00dbc83796c6ae63137a9bdade074f7648b3e32613412dd", size = 20727743, upload-time = "2026-03-09T07:58:53.426Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/70/ae/3936f79adebf8caf81bd7a599b90a561334a658be4dcc7b6329ebf4ee8de/numpy-2.4.3-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:5884ce5c7acfae1e4e1b6fde43797d10aa506074d25b531b4f54bde33c0c31d4", size = 16664563, upload-time = "2026-03-09T07:57:43.817Z" },
    { url = "https://files.pythonhosted.org/packages/9b/62/760f2b55866b496bb1fa7da2a6db076bef908110e568b02fcfc1422e2a3a/numpy-2.4.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:297837823f5bc572c5f9379b0c9f3a3365f08492cbdc33bcc3af174372ebb168", size = 14702161, upload-time = "2026-03-09T07:57:46.169Z" },
    { url = "https://files.pythonhosted.org/packages/32/af/a7a39464e2c0a21526fb4fb76e346fb172ebc92f6d1c7a07c2c139cc17b1/numpy-2.4.3-cp314-cp314-macosx_14_0_arm64.whl", hash = "sha256:a111698b4a3f8dcbe54c64a7708f049355abd603e619013c346553c1fd4ca90b", size = 5208738, upload-time = "2026-03-09T07:57:48.506Z" },
    { url = "https://files.pythonhosted.org/packages/29/8c/2a0cf86a59558fa078d83805589c2de490f29ed4fb336c14313a161d358a/numpy-2.4.3-cp314-cp314-macosx_14_0_x86_64.whl", hash = "sha256:4bd4741a6a676770e0e97fe9ab2e51de01183df3dcbcec591d26d331a40de950", size = 6543618, upload-time = "2026-03-09T07:57:50.591Z" },
    { url = "https://files.pythonhosted.org/packages/aa/b8/612ce010c0728b1c363fa4ea3aa4c22fe1c5da1de008486f8c2f5cb92fae/numpy-2.4.3-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:54f29b877279d51e210e0c80709ee14ccbbad647810e8f3d375561c45ef613dd", size = 15680676, upload-time = "2026-03-09T07:57:52.34Z" },
    { url = "https://files.pythonhosted.org/packages/a9/7e/4f120ecc54ba26ddf3dc348eeb9eb063f421de65c05fc961941798feea18/numpy-2.4.3-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:679f2a834bae9020f81534671c56fd0cc76dd7e5182f57131478e23d0dc59e24", size = 16613492, upload-time = "2026-03-09T07:57:54.91Z" },
    { url = "https://files.pythonhosted.org/packages/2c/86/1b6020db73be330c4b45d5c6ee4295d59cfeef0e3ea323959d053e5a6909/numpy-2.4.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:d84f0f881cb2225c2dfd7f78a10a5645d487a496c6668d6cc39f0f114164f3d0", size = 17031789, upload-time = "2026-03-09T07:57:57.641Z" },
    { url = "https://files.pythonhosted.org/packages/07/3a/3b90463bf41ebc21d1b7e06079f03070334374208c0f9a1f05e4ae8455e7/numpy-2.4.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:d213c7e6e8d211888cc359bab7199670a00f5b82c0978b9d1c75baf1eddbeac0", size = 18339941, upload-time = "2026-03-09T07:58:00.577Z" },
    { url = "https://files.pythonhosted.org/packages/a8/74/6d736c4cd962259fd8bae9be27363eb4883a2f9069763747347544c2a487/numpy-2.4.3-cp314-cp314-win32.whl", hash = "sha256:52077feedeff7c76ed7c9f1a0428558e50825347b7545bbb8523da2cd55c547a", size = 6007503, upload-time = "2026-03-09T07:58:03.331Z" },
    { url = "https://files.pythonhosted.org/packages/48/39/c56ef87af669364356bb011922ef0734fc49dad51964568634c72a009488/numpy-2.4.3-cp314-cp314-win_amd64.whl", hash = "sha256:0448e7f9caefb34b4b7dd2b77f21e8906e5d6f0365ad525f9f4f530b13df2afc", size = 12444915, upload-time = "2026-03-09T07:58:06.353Z" },
    { url = "https://files.pythonhosted.org/packages/9d/1f/ab8528e38d295fd349310807496fabb7cf9fe2e1f70b97bc20a483ea9d4a/numpy-2.4.3-cp314-cp314-win_arm64.whl", hash = "sha256:b44fd60341c4d9783039598efadd03617fa28d041fc37d22b62d08f2027fa0e7", size = 10494875, upload-time = "2026-03-09T07:58:08.734Z" },
    { url = "https://files.pythonhosted.org/packages/e6/ef/b7c35e4d5ef141b836658ab21a66d1a573e15b335b1d111d31f26c8ef80f/numpy-2.4.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:0a195f4216be9305a73c0e91c9b026a35f2161237cf1c6de9b681637772ea657", size = 14822225, upload-time = "2026-03-09T07:58:11.034Z" },
    { url = "https://files.pythonhosted.org/packages/cd/8d/7730fa9278cf6648639946cc816e7cc89f0d891602584697923375f801ed/numpy-2.4.3-cp314-cp314t-macosx_14_0_arm64.whl", hash = "sha256:cd32fbacb9fd1bf041bf8e89e4576b6f00b895f06d00914820ae06a616bdfef7", size = 5328769, upload-time = "2026-03-09T07:58:13.67Z" },
    { url = "https://files.pythonhosted.org/packages/47/01/d2a137317c958b074d338807c1b6a383406cdf8b8e53b075d804cc3d211d/numpy-2.4.3-cp314-cp314t-macosx_14_0_x86_64.whl", hash = "sha256:2e03c05abaee1f672e9d67bc858f300b5ccba1c21397211e8d77d98350972093", size = 6649461, upload-time = "2026-03-09T07:58:15.912Z" },
    { url = "https://files.pythonhosted.org/packages/5c/34/812ce12bc0f00272a4b0ec0d713cd237cb390666eb6206323d1cc9cedbb2/numpy-2.4.3-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7d1ce23cce91fcea443320a9d0ece9b9305d4368875bab09538f7a5b4131938a", size = 15725809, upload-time = "2026-03-09T07:58:17.787Z" },
    { url = "https://files.pythonhosted.org/packages/25/c0/2aed473a4823e905e765fee3dc2cbf504bd3e68ccb1150fbdabd5c39f527/numpy-2.4.3-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c59020932feb24ed49ffd03704fbab89f22aa9c0d4b180ff45542fe8918f5611", size = 16655242, upload-time = "2026-03-09T07:58:20.476Z" },
    { url = "https://files.pythonhosted.org/packages/f2/c8/7e052b2fc87aa0e86de23f20e2c42bd261c624748aa8efd2c78f7bb8d8c6/numpy-2.4.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:9684823a78a6cd6ad7511fc5e25b07947d1d5b5e2812c93fe99d7d4195130720", size = 17080660, upload-time = "2026-03-09T07:58:23.067Z" },
    { url = "https://files.pythonhosted.org/packages/f3/3d/0876746044db2adcb11549f214d104f2e1be00f07a67edbb4e2812094847/numpy-2.4.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:0200b25c687033316fb39f0ff4e3e690e8957a2c3c8d22499891ec58c37a3eb5", size = 18380384, upload-time = "2026-03-09T07:58:25.839Z" },
    { url = "https://files.pythonhosted.org/packages/07/12/8160bea39da3335737b10308df4f484235fd297f556745f13092aa039d3b/numpy-2.4.3-cp314-cp314t-win32.whl", hash = "sha256:5e10da9e93247e554bb1d22f8edc51847ddd7dde52d85ce31024c1b4312bfba0", size = 6154547, upload-time = "2026-03-09T07:58:28.289Z" },
    { url = "https://files.pythonhosted.org/packages/42/f3/76534f61f80d74cc9cdf2e570d3d4eeb92c2280a27c39b0aaf471eda7b48/numpy-2.4.3-cp314-cp314t-win_amd64.whl", hash = "sha256:45f003dbdffb997a03da2d1d0cb41fbd24a87507fb41605c0420a3db5bd4667b", size = 12633645, upload-time = "2026-03-09T07:58:30.384Z" },
    { url = "https://files.pythonhosted.org/packages/1f/b6/7c0d4334c15983cec7f92a69e8ce9b1e6f31857e5ee3a413ac424e6bd63d/numpy-2.4.3-cp314-cp314t-win_arm64.whl", hash = "sha256:4d382735cecd7bcf090172489a525cd7d4087bc331f7df9f60ddc9a296cf208e", size = 10565454, upload-time = "2026-03-09T07:58:33.031Z" },
]

[[package]]
name = "packaging"
version = "26.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/65/ee/299d360cdc32edc7d2cf530f3accf79c4fca01e96ffc950d8a52213bd8e4/packaging-26.0.tar.gz", hash = "sha256:00243ae351a257117b6a241061796684b084ed1c516a08c48a3f7e147a9d80b4", size = 143416, upload-time = "2026-01-21T20:50:39.064Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b7/b9/c538f279a4e237a006a2c98387d081e9eb060d203d8ed34467cc0f0b9b53/packaging-26.0-py3-none-any.whl", hash = "sha256:b36f1fef9334a5588b4166f8bcd26a14e521f2b55e6b9de3aaa80d3ff7a37529", size = 74366, upload-time = "2026-01-21T20:50:37.788Z" },
]

[[package]]
name = "pandas"
version = "3.0.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "numpy" },
    { name = "python-dateutil" },
    { name = "tzdata", marker = "sys_platform == 'emscripten' or sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/2e/0c/b28ed414f080ee0ad153f848586d61d1878f91689950f037f976ce15f6c8/pandas-3.0.1.tar.gz", hash = "sha256:4186a699674af418f655dbd420ed87f50d56b4cd6603784279d9eef6627823c8", size = 4641901, upload-time = "2026-02-17T22:20:16.434Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/bb/8b/4bb774a998b97e6c2fd62a9e6cfdaae133b636fd1c468f92afb4ae9a447a/pandas-3.0.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:99d0f92ed92d3083d140bf6b97774f9f13863924cf3f52a70711f4e7588f9d0a", size = 10322465, upload-time = "2026-02-17T22:19:36.803Z" },
    { url = "https://files.pythonhosted.org/packages/72/3a/5b39b51c64159f470f1ca3b1c2a87da290657ca022f7cd11442606f607d1/pandas-3.0.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:3b66857e983208654294bb6477b8a63dee26b37bdd0eb34d010556e91261784f", size = 9910632, upload-time = "2026-02-17T22:19:39.001Z" },
    { url = "https://files.pythonhosted.org/packages/4e/f7/b449ffb3f68c11da12fc06fbf6d2fa3a41c41e17d0284d23a79e1c13a7e4/pandas-3.0.1-cp314-cp314-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:56cf59638bf24dc9bdf2154c81e248b3289f9a09a6d04e63608c159022352749", size = 10440535, upload-time = "2026-02-17T22:19:41.157Z" },
    { url = "https://files.pythonhosted.org/packages/55/77/6ea82043db22cb0f2bbfe7198da3544000ddaadb12d26be36e19b03a2dc5/pandas-3.0.1-cp314-cp314-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c1a9f55e0f46951874b863d1f3906dcb57df2d9be5c5847ba4dfb55b2c815249", size = 10893940, upload-time = "2026-02-17T22:19:43.493Z" },
    { url = "https://files.pythonhosted.org/packages/03/30/f1b502a72468c89412c1b882a08f6eed8a4ee9dc033f35f65d0663df6081/pandas-3.0.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:1849f0bba9c8a2fb0f691d492b834cc8dadf617e29015c66e989448d58d011ee", size = 11442711, upload-time = "2026-02-17T22:19:46.074Z" },
    { url = "https://files.pythonhosted.org/packages/0d/f0/ebb6ddd8fc049e98cabac5c2924d14d1dda26a20adb70d41ea2e428d3ec4/pandas-3.0.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:c3d288439e11b5325b02ae6e9cc83e6805a62c40c5a6220bea9beb899c073b1c", size = 11963918, upload-time = "2026-02-17T22:19:48.838Z" },
    { url = "https://files.pythonhosted.org/packages/09/f8/8ce132104074f977f907442790eaae24e27bce3b3b454e82faa3237ff098/pandas-3.0.1-cp314-cp314-win_amd64.whl", hash = "sha256:93325b0fe372d192965f4cca88d97667f49557398bbf94abdda3bf1b591dbe66", size = 9862099, upload-time = "2026-02-17T22:19:51.081Z" },
    { url = "https://files.pythonhosted.org/packages/e6/b7/6af9aac41ef2456b768ef0ae60acf8abcebb450a52043d030a65b4b7c9bd/pandas-3.0.1-cp314-cp314-win_arm64.whl", hash = "sha256:97ca08674e3287c7148f4858b01136f8bdfe7202ad25ad04fec602dd1d29d132", size = 9185333, upload-time = "2026-02-17T22:19:53.266Z" },
    { url = "https://files.pythonhosted.org/packages/66/fc/848bb6710bc6061cb0c5badd65b92ff75c81302e0e31e496d00029fe4953/pandas-3.0.1-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:58eeb1b2e0fb322befcf2bbc9ba0af41e616abadb3d3414a6bc7167f6cbfce32", size = 10772664, upload-time = "2026-02-17T22:19:55.806Z" },
    { url = "https://files.pythonhosted.org/packages/69/5c/866a9bbd0f79263b4b0db6ec1a341be13a1473323f05c122388e0f15b21d/pandas-3.0.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:cd9af1276b5ca9e298bd79a26bda32fa9cc87ed095b2a9a60978d2ca058eaf87", size = 10421286, upload-time = "2026-02-17T22:19:58.091Z" },
    { url = "https://files.pythonhosted.org/packages/51/a4/2058fb84fb1cfbfb2d4a6d485e1940bb4ad5716e539d779852494479c580/pandas-3.0.1-cp314-cp314t-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:94f87a04984d6b63788327cd9f79dda62b7f9043909d2440ceccf709249ca988", size = 10342050, upload-time = "2026-02-17T22:20:01.376Z" },
    { url = "https://files.pythonhosted.org/packages/22/1b/674e89996cc4be74db3c4eb09240c4bb549865c9c3f5d9b086ff8fcfbf00/pandas-3.0.1-cp314-cp314t-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:85fe4c4df62e1e20f9db6ebfb88c844b092c22cd5324bdcf94bfa2fc1b391221", size = 10740055, upload-time = "2026-02-17T22:20:04.328Z" },
    { url = "https://files.pythonhosted.org/packages/d0/f8/e954b750764298c22fa4614376531fe63c521ef517e7059a51f062b87dca/pandas-3.0.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:331ca75a2f8672c365ae25c0b29e46f5ac0c6551fdace8eec4cd65e4fac271ff", size = 11357632, upload-time = "2026-02-17T22:20:06.647Z" },
    { url = "https://files.pythonhosted.org/packages/6d/02/c6e04b694ffd68568297abd03588b6d30295265176a5c01b7459d3bc35a3/pandas-3.0.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:15860b1fdb1973fffade772fdb931ccf9b2f400a3f5665aef94a00445d7d8dd5", size = 11810974, upload-time = "2026-02-17T22:20:08.946Z" },
    { url = "https://files.pythonhosted.org/packages/89/41/d7dfb63d2407f12055215070c42fc6ac41b66e90a2946cdc5e759058398b/pandas-3.0.1-cp314-cp314t-win_amd64.whl", hash = "sha256:44f1364411d5670efa692b146c748f4ed013df91ee91e9bec5677fb1fd58b937", size = 10884622, upload-time = "2026-02-17T22:20:11.711Z" },
    { url = "https://files.pythonhosted.org/packages/68/b0/34937815889fa982613775e4b97fddd13250f11012d769949c5465af2150/pandas-3.0.1-cp314-cp314t-win_arm64.whl", hash = "sha256:108dd1790337a494aa80e38def654ca3f0968cf4f362c85f44c15e471667102d", size = 9452085, upload-time = "2026-02-17T22:20:14.331Z" },
]

[[package]]
name = "pillow"
version = "12.1.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1f/42/5c74462b4fd957fcd7b13b04fb3205ff8349236ea74c7c375766d6c82288/pillow-12.1.1.tar.gz", hash = "sha256:9ad8fa5937ab05218e2b6a4cff30295ad35afd2f83ac592e68c0d871bb0fdbc4", size = 46980264, upload-time = "2026-02-11T04:23:07.146Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/03/d0/bebb3ffbf31c5a8e97241476c4cf8b9828954693ce6744b4a2326af3e16b/pillow-12.1.1-cp314-cp314-ios_13_0_arm64_iphoneos.whl", hash = "sha256:417423db963cb4be8bac3fc1204fe61610f6abeed1580a7a2cbb2fbda20f12af", size = 4062652, upload-time = "2026-02-11T04:21:53.19Z" },
    { url = "https://files.pythonhosted.org/packages/2d/c0/0e16fb0addda4851445c28f8350d8c512f09de27bbb0d6d0bbf8b6709605/pillow-12.1.1-cp314-cp314-ios_13_0_arm64_iphonesimulator.whl", hash = "sha256:b957b71c6b2387610f556a7eb0828afbe40b4a98036fc0d2acfa5a44a0c2036f", size = 4138823, upload-time = "2026-02-11T04:22:03.088Z" },
    { url = "https://files.pythonhosted.org/packages/6b/fb/6170ec655d6f6bb6630a013dd7cf7bc218423d7b5fa9071bf63dc32175ae/pillow-12.1.1-cp314-cp314-ios_13_0_x86_64_iphonesimulator.whl", hash = "sha256:097690ba1f2efdeb165a20469d59d8bb03c55fb6621eb2041a060ae8ea3e9642", size = 3601143, upload-time = "2026-02-11T04:22:04.909Z" },
    { url = "https://files.pythonhosted.org/packages/59/04/dc5c3f297510ba9a6837cbb318b87dd2b8f73eb41a43cc63767f65cb599c/pillow-12.1.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:2815a87ab27848db0321fb78c7f0b2c8649dee134b7f2b80c6a45c6831d75ccd", size = 5266254, upload-time = "2026-02-11T04:22:07.656Z" },
    { url = "https://files.pythonhosted.org/packages/05/30/5db1236b0d6313f03ebf97f5e17cda9ca060f524b2fcc875149a8360b21c/pillow-12.1.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:f7ed2c6543bad5a7d5530eb9e78c53132f93dfa44a28492db88b41cdab885202", size = 4657499, upload-time = "2026-02-11T04:22:09.613Z" },
    { url = "https://files.pythonhosted.org/packages/6f/18/008d2ca0eb612e81968e8be0bbae5051efba24d52debf930126d7eaacbba/pillow-12.1.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:652a2c9ccfb556235b2b501a3a7cf3742148cd22e04b5625c5fe057ea3e3191f", size = 6232137, upload-time = "2026-02-11T04:22:11.434Z" },
    { url = "https://files.pythonhosted.org/packages/70/f1/f14d5b8eeb4b2cd62b9f9f847eb6605f103df89ef619ac68f92f748614ea/pillow-12.1.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:d6e4571eedf43af33d0fc233a382a76e849badbccdf1ac438841308652a08e1f", size = 8042721, upload-time = "2026-02-11T04:22:13.321Z" },
    { url = "https://files.pythonhosted.org/packages/5a/d6/17824509146e4babbdabf04d8171491fa9d776f7061ff6e727522df9bd03/pillow-12.1.1-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b574c51cf7d5d62e9be37ba446224b59a2da26dc4c1bb2ecbe936a4fb1a7cb7f", size = 6347798, upload-time = "2026-02-11T04:22:15.449Z" },
    { url = "https://files.pythonhosted.org/packages/d1/ee/c85a38a9ab92037a75615aba572c85ea51e605265036e00c5b67dfafbfe2/pillow-12.1.1-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a37691702ed687799de29a518d63d4682d9016932db66d4e90c345831b02fb4e", size = 7039315, upload-time = "2026-02-11T04:22:17.24Z" },
    { url = "https://files.pythonhosted.org/packages/ec/f3/bc8ccc6e08a148290d7523bde4d9a0d6c981db34631390dc6e6ec34cacf6/pillow-12.1.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:f95c00d5d6700b2b890479664a06e754974848afaae5e21beb4d83c106923fd0", size = 6462360, upload-time = "2026-02-11T04:22:19.111Z" },
    { url = "https://files.pythonhosted.org/packages/f6/ab/69a42656adb1d0665ab051eec58a41f169ad295cf81ad45406963105408f/pillow-12.1.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:559b38da23606e68681337ad74622c4dbba02254fc9cb4488a305dd5975c7eeb", size = 7165438, upload-time = "2026-02-11T04:22:21.041Z" },
    { url = "https://files.pythonhosted.org/packages/02/46/81f7aa8941873f0f01d4b55cc543b0a3d03ec2ee30d617a0448bf6bd6dec/pillow-12.1.1-cp314-cp314-win32.whl", hash = "sha256:03edcc34d688572014ff223c125a3f77fb08091e4607e7745002fc214070b35f", size = 6431503, upload-time = "2026-02-11T04:22:22.833Z" },
    { url = "https://files.pythonhosted.org/packages/40/72/4c245f7d1044b67affc7f134a09ea619d4895333d35322b775b928180044/pillow-12.1.1-cp314-cp314-win_amd64.whl", hash = "sha256:50480dcd74fa63b8e78235957d302d98d98d82ccbfac4c7e12108ba9ecbdba15", size = 7176748, upload-time = "2026-02-11T04:22:24.64Z" },
    { url = "https://files.pythonhosted.org/packages/e4/ad/8a87bdbe038c5c698736e3348af5c2194ffb872ea52f11894c95f9305435/pillow-12.1.1-cp314-cp314-win_arm64.whl", hash = "sha256:5cb1785d97b0c3d1d1a16bc1d710c4a0049daefc4935f3a8f31f827f4d3d2e7f", size = 2544314, upload-time = "2026-02-11T04:22:26.685Z" },
    { url = "https://files.pythonhosted.org/packages/6c/9d/efd18493f9de13b87ede7c47e69184b9e859e4427225ea962e32e56a49bc/pillow-12.1.1-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:1f90cff8aa76835cba5769f0b3121a22bd4eb9e6884cfe338216e557a9a548b8", size = 5268612, upload-time = "2026-02-11T04:22:29.884Z" },
    { url = "https://files.pythonhosted.org/packages/f8/f1/4f42eb2b388eb2ffc660dcb7f7b556c1015c53ebd5f7f754965ef997585b/pillow-12.1.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:1f1be78ce9466a7ee64bfda57bdba0f7cc499d9794d518b854816c41bf0aa4e9", size = 4660567, upload-time = "2026-02-11T04:22:31.799Z" },
    { url = "https://files.pythonhosted.org/packages/01/54/df6ef130fa43e4b82e32624a7b821a2be1c5653a5fdad8469687a7db4e00/pillow-12.1.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:42fc1f4677106188ad9a55562bbade416f8b55456f522430fadab3cef7cd4e60", size = 6269951, upload-time = "2026-02-11T04:22:33.921Z" },
    { url = "https://files.pythonhosted.org/packages/a9/48/618752d06cc44bb4aae8ce0cd4e6426871929ed7b46215638088270d9b34/pillow-12.1.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:98edb152429ab62a1818039744d8fbb3ccab98a7c29fc3d5fcef158f3f1f68b7", size = 8074769, upload-time = "2026-02-11T04:22:35.877Z" },
    { url = "https://files.pythonhosted.org/packages/c3/bd/f1d71eb39a72fa088d938655afba3e00b38018d052752f435838961127d8/pillow-12.1.1-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d470ab1178551dd17fdba0fef463359c41aaa613cdcd7ff8373f54be629f9f8f", size = 6381358, upload-time = "2026-02-11T04:22:37.698Z" },
    { url = "https://files.pythonhosted.org/packages/64/ef/c784e20b96674ed36a5af839305f55616f8b4f8aa8eeccf8531a6e312243/pillow-12.1.1-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:6408a7b064595afcab0a49393a413732a35788f2a5092fdc6266952ed67de586", size = 7068558, upload-time = "2026-02-11T04:22:39.597Z" },
    { url = "https://files.pythonhosted.org/packages/73/cb/8059688b74422ae61278202c4e1ad992e8a2e7375227be0a21c6b87ca8d5/pillow-12.1.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:5d8c41325b382c07799a3682c1c258469ea2ff97103c53717b7893862d0c98ce", size = 6493028, upload-time = "2026-02-11T04:22:42.73Z" },
    { url = "https://files.pythonhosted.org/packages/c6/da/e3c008ed7d2dd1f905b15949325934510b9d1931e5df999bb15972756818/pillow-12.1.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:c7697918b5be27424e9ce568193efd13d925c4481dd364e43f5dff72d33e10f8", size = 7191940, upload-time = "2026-02-11T04:22:44.543Z" },
    { url = "https://files.pythonhosted.org/packages/01/4a/9202e8d11714c1fc5951f2e1ef362f2d7fbc595e1f6717971d5dd750e969/pillow-12.1.1-cp314-cp314t-win32.whl", hash = "sha256:d2912fd8114fc5545aa3a4b5576512f64c55a03f3ebcca4c10194d593d43ea36", size = 6438736, upload-time = "2026-02-11T04:22:46.347Z" },
    { url = "https://files.pythonhosted.org/packages/f3/ca/cbce2327eb9885476b3957b2e82eb12c866a8b16ad77392864ad601022ce/pillow-12.1.1-cp314-cp314t-win_amd64.whl", hash = "sha256:4ceb838d4bd9dab43e06c363cab2eebf63846d6a4aeaea283bbdfd8f1a8ed58b", size = 7182894, upload-time = "2026-02-11T04:22:48.114Z" },
    { url = "https://files.pythonhosted.org/packages/ec/d2/de599c95ba0a973b94410477f8bf0b6f0b5e67360eb89bcb1ad365258beb/pillow-12.1.1-cp314-cp314t-win_arm64.whl", hash = "sha256:7b03048319bfc6170e93bd60728a1af51d3dd7704935feb228c4d4faab35d334", size = 2546446, upload-time = "2026-02-11T04:22:50.342Z" },
]

[[package]]
name = "pyparsing"
version = "3.3.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f3/91/9c6ee907786a473bf81c5f53cf703ba0957b23ab84c264080fb5a450416f/pyparsing-3.3.2.tar.gz", hash = "sha256:c777f4d763f140633dcb6d8a3eda953bf7a214dc4eff598413c070bcdc117cbc", size = 6851574, upload-time = "2026-01-21T03:57:59.36Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/10/bd/c038d7cc38edc1aa5bf91ab8068b63d4308c66c4c8bb3cbba7dfbc049f9c/pyparsing-3.3.2-py3-none-any.whl", hash = "sha256:850ba148bd908d7e2411587e247a1e4f0327839c40e2e5e6d05a007ecc69911d", size = 122781, upload-time = "2026-01-21T03:57:55.912Z" },
]

[[package]]
name = "python-dateutil"
version = "2.9.0.post0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "six" },
]
sdist = { url = "https://files.pythonhosted.org/packages/66/c0/0c8b6ad9f17a802ee498c46e004a0eb49bc148f2fd230864601a86dcf6db/python-dateutil-2.9.0.post0.tar.gz", hash = "sha256:37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3", size = 342432, upload-time = "2024-03-01T18:36:20.211Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ec/57/56b9bcc3c9c6a792fcbaf139543cee77261f3651ca9da0c93f5c1221264b/python_dateutil-2.9.0.post0-py2.py3-none-any.whl", hash = "sha256:a8b2bc7bffae282281c8140a97d3aa9c14da0b136dfe83f850eea9a5f7470427", size = 229892, upload-time = "2024-03-01T18:36:18.57Z" },
]

[[package]]
name = "python-decouple"
version = "3.8"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/e1/97/373dcd5844ec0ea5893e13c39a2c67e7537987ad8de3842fe078db4582fa/python-decouple-3.8.tar.gz", hash = "sha256:ba6e2657d4f376ecc46f77a3a615e058d93ba5e465c01bbe57289bfb7cce680f", size = 9612, upload-time = "2023-03-01T19:38:38.143Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a2/d4/9193206c4563ec771faf2ccf54815ca7918529fe81f6adb22ee6d0e06622/python_decouple-3.8-py3-none-any.whl", hash = "sha256:d0d45340815b25f4de59c974b855bb38d03151d81b037d9e3f463b0c9f8cbd66", size = 9947, upload-time = "2023-03-01T19:38:36.015Z" },
]

[[package]]
name = "requests"
version = "2.32.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "charset-normalizer" },
    { name = "idna" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c9/74/b3ff8e6c8446842c3f5c837e9c3dfcfe2018ea6ecef224c710c85ef728f4/requests-2.32.5.tar.gz", hash = "sha256:dbba0bac56e100853db0ea71b82b4dfd5fe2bf6d3754a8893c3af500cec7d7cf", size = 134517, upload-time = "2025-08-18T20:46:02.573Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1e/db/4254e3eabe8020b458f1a747140d32277ec7a271daf1d235b70dc0b4e6e3/requests-2.32.5-py3-none-any.whl", hash = "sha256:2462f94637a34fd532264295e186976db0f5d453d1cdd31473c85a6a161affb6", size = 64738, upload-time = "2025-08-18T20:46:00.542Z" },
]

[[package]]
name = "six"
version = "1.17.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/94/e7/b2c673351809dca68a0e064b6af791aa332cf192da575fd474ed7d6f16a2/six-1.17.0.tar.gz", hash = "sha256:ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81", size = 34031, upload-time = "2024-12-04T17:35:28.174Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b7/ce/149a00dd41f10bc29e5921b496af8b574d8413afcd5e30dfa0ed46c2cc5e/six-1.17.0-py2.py3-none-any.whl", hash = "sha256:4721f391ed90541fddacab5acf947aa0d3dc7d27b2e1e8eda2be8970586c3274", size = 11050, upload-time = "2024-12-04T17:35:26.475Z" },
]

[[package]]
name = "softwareproject"
version = "1.0.0"
source = { virtual = "." }
dependencies = [
    { name = "django" },
    { name = "gunicorn" },
    { name = "matplotlib" },
    { name = "pandas" },
    { name = "python-decouple" },
    { name = "requests" },
    { name = "whitenoise" },
]

[package.metadata]
requires-dist = [
    { name = "django", specifier = ">=6.0.2" },
    { name = "gunicorn", specifier = ">=25.1.0" },
    { name = "matplotlib", specifier = ">=3.10.8" },
    { name = "pandas", specifier = ">=3.0.1" },
    { name = "python-decouple", specifier = ">=3.8" },
    { name = "requests", specifier = ">=2.32.5" },
    { name = "whitenoise", specifier = ">=6.12.0" },
]

[[package]]
name = "sqlparse"
version = "0.5.5"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/90/76/437d71068094df0726366574cf3432a4ed754217b436eb7429415cf2d480/sqlparse-0.5.5.tar.gz", hash = "sha256:e20d4a9b0b8585fdf63b10d30066c7c94c5d7a7ec47c889a2d83a3caa93ff28e", size = 120815, upload-time = "2025-12-19T07:17:45.073Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/49/4b/359f28a903c13438ef59ebeee215fb25da53066db67b305c125f1c6d2a25/sqlparse-0.5.5-py3-none-any.whl", hash = "sha256:12a08b3bf3eec877c519589833aed092e2444e68240a3577e8e26148acc7b1ba", size = 46138, upload-time = "2025-12-19T07:17:46.573Z" },
]

[[package]]
name = "tzdata"
version = "2025.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/5e/a7/c202b344c5ca7daf398f3b8a477eeb205cf3b6f32e7ec3a6bac0629ca975/tzdata-2025.3.tar.gz", hash = "sha256:de39c2ca5dc7b0344f2eba86f49d614019d29f060fc4ebc8a417896a620b56a7", size = 196772, upload-time = "2025-12-13T17:45:35.667Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c7/b0/003792df09decd6849a5e39c28b513c06e84436a54440380862b5aeff25d/tzdata-2025.3-py2.py3-none-any.whl", hash = "sha256:06a47e5700f3081aab02b2e513160914ff0694bce9947d6b76ebd6bf57cfc5d1", size = 348521, upload-time = "2025-12-13T17:45:33.889Z" },
]

[[package]]
name = "urllib3"
version = "2.6.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c7/24/5f1b3bdffd70275f6661c76461e25f024d5a38a46f04aaca912426a2b1d3/urllib3-2.6.3.tar.gz", hash = "sha256:1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed", size = 435556, upload-time = "2026-01-07T16:24:43.925Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/39/08/aaaad47bc4e9dc8c725e68f9d04865dbcb2052843ff09c97b08904852d84/urllib3-2.6.3-py3-none-any.whl", hash = "sha256:bf272323e553dfb2e87d9bfd225ca7b0f467b919d7bbd355436d3fd37cb0acd4", size = 131584, upload-time = "2026-01-07T16:24:42.685Z" },
]

[[package]]
name = "whitenoise"
version = "6.12.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/cb/2a/55b3f3a4ec326cd077c1c3defeee656b9298372a69229134d930151acd01/whitenoise-6.12.0.tar.gz", hash = "sha256:f723ebb76a112e98816ff80fcea0a6c9b8ecde835f8ddda25df7a30a3c2db6ad", size = 26841, upload-time = "2026-02-27T00:05:42.028Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/db/eb/d5583a11486211f3ebd4b385545ae787f32363d453c19fffd81106c9c138/whitenoise-6.12.0-py3-none-any.whl", hash = "sha256:fc5e8c572e33ebf24795b47b6a7da8da3c00cff2349f5b04c02f28d0cc5a3cc2", size = 20302, upload-time = "2026-02-27T00:05:40.086Z" },
]

```
<!-- END_FILE -->


---
## Bundle notes
- Redaction: enabled (mask: `***REDACTED***`).
- No truncations.

