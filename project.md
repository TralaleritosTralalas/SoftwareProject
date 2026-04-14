# CodeBundle: SoftwareProject
Generated: 2026-04-14T08:28:44.803Z
Root: /home/toni/Documentos/GitHub/SoftwareProject
Files: 49

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
│  │  └─ generate_qc_report.js
│  └─ workflows
│     ├─ deploy.yml
│     ├─ histogram.yml
│     ├─ pareto.yml
│     ├─ quality-control-aggregator.yml
│     ├─ runchart.yml
│     └─ test.yml
├─ .gitignore
├─ app
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ services.py
│  ├─ static
│  │  ├─ css
│  │  │  └─ main.css
│  │  └─ js
│  │     └─ tailwind.config.js
│  ├─ templates
│  │  ├─ base
│  │  │  └─ base.html
│  │  ├─ components
│  │  │  ├─ card_movies.html
│  │  │  ├─ card_series.html
│  │  │  ├─ footer.html
│  │  │  └─ navbar.html
│  │  └─ pages
│  │     ├─ catalog.html
│  │     ├─ content_view.html
│  │     ├─ home.html
│  │     ├─ main.html
│  │     └─ search.html
│  ├─ tests.py
│  ├─ urls.py
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
├─ proyecto.md
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

- `.dockerignore` (369 bytes)
- `.github/ISSUE_TEMPLATE/config.yml` (27 bytes)
- `.github/ISSUE_TEMPLATE/issue_template.md` (674 bytes)
- `.github/quality_control_data.json` (1434 bytes)
- `.github/scripts/generate_qc_report.js` (5936 bytes)
- `.github/workflows/deploy.yml` (874 bytes)
- `.github/workflows/histogram.yml` (943 bytes)
- `.github/workflows/pareto.yml` (986 bytes)
- `.github/workflows/quality-control-aggregator.yml` (3826 bytes)
- `.github/workflows/runchart.yml` (1258 bytes)
- `.github/workflows/test.yml` (766 bytes)
- `.gitignore` (48 bytes)
- `app/__init__.py` (0 bytes)
- `app/admin.py` (63 bytes)
- `app/apps.py` (81 bytes)
- `app/migrations/__init__.py` (0 bytes)
- `app/models.py` (57 bytes)
- `app/services.py` (6386 bytes)
- `app/static/css/main.css` (1053 bytes)
- `app/static/js/tailwind.config.js` (713 bytes)
- `app/templates/base/base.html` (1321 bytes)
- `app/templates/components/card_movies.html` (2493 bytes)
- `app/templates/components/card_series.html` (2505 bytes)
- `app/templates/components/footer.html` (616 bytes)
- `app/templates/components/navbar.html` (3966 bytes)
- `app/templates/pages/catalog.html` (662 bytes)
- `app/templates/pages/content_view.html` (37633 bytes)
- `app/templates/pages/home.html` (17517 bytes)
- `app/templates/pages/main.html` (27320 bytes)
- `app/templates/pages/search.html` (9187 bytes)
- `app/tests.py` (60 bytes)
- `app/urls.py` (455 bytes)
- `app/views.py` (1474 bytes)
- `docker-compose.yml` (938 bytes)
- `Dockerfile` (390 bytes)
- `entrypoint.sh` (173 bytes)
- `IshikawaTools/chart.py` (4069 bytes)
- `IshikawaTools/histogram.py` (5451 bytes)
- `IshikawaTools/runchart.py` (4479 bytes)
- `manage.py` (671 bytes)
- `meeting_files/to_do_list.md` (407 bytes)
- `proyecto.md` (146754 bytes)
- `pyproject.toml` (311 bytes)
- `SoftwareProject/__init__.py` (0 bytes)
- `SoftwareProject/asgi.py` (407 bytes)
- `SoftwareProject/settings.py` (3317 bytes)
- `SoftwareProject/urls.py` (815 bytes)
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
*.sqlite3

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
media/

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

# Register your models here.

```
<!-- END_FILE -->

---
<!-- FILE: app/apps.py -->
## app/apps.py

```py
from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'

```
<!-- END_FILE -->

---
<!-- FILE: app/migrations/__init__.py -->
## app/migrations/__init__.py

```py


```
<!-- END_FILE -->

---
<!-- FILE: app/models.py -->
## app/models.py

```py
from django.db import models

# Create your models here.

```
<!-- END_FILE -->

---
<!-- FILE: app/services.py -->
## app/services.py

```py
import requests
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


def get_all_movies():  # obtener todas las peliculas de todas las "plataformas"

    movies_dict = {} #diccionario para saber el contenido

    for url, key, platform_name in PLATFORMS:
        
        # mapa de generos x plataforma
        genre_map = {}

        genres = get_genre(url, key)
        for g in genres:
            genre_map[g["id"]] = g["name"]

        movies = get_local_movies(url, key)
        for movie in movies:
            identifier = f"{movie.get('title')}_{movie.get('year')}".lower().strip() #identificador del contenido
            
            if identifier not in movies_dict: #el contenido no esta 
                movie["genre_name"] = genre_map.get(movie.get('genre_id'), "Unknown") #agarramos su genero
                movie["platforms"] = [platform_name]# lista de plataformas 
                movie.pop("platform_name", None) 
                movies_dict[identifier] = movie #guardamos en el diccionario
            else:
                if platform_name not in movies_dict[identifier]["platforms"]:
                    movies_dict[identifier]["platforms"].append(platform_name)
    return list(movies_dict.values())


def get_all_series():  # obtener todas las peliculas de todas las "plataformas"
    series_dict = {}

    for url, key, platform_name in PLATFORMS:
        genre_map = {}
        genres = get_genre(url, key)
        for g in genres:
            genre_map[g["id"]] = g["name"]

        series = get_local_series(url, key)

        for serie in series:
            identifier = f"{serie.get('title')}_{serie.get('start_year', '')}".lower().strip()

            if identifier not in series_dict:
                serie["genre_name"] = genre_map.get(serie.get("genre_id"), "Unknown")
                serie["platforms"] = [platform_name]
                serie.pop("platform_name", None)
                series_dict[identifier] = serie
            else:
                if platform_name not in series_dict[identifier]["platforms"]:
                    series_dict[identifier]["platforms"].append(platform_name)
    
    return list(series_dict.values())


def search_content(query): #buscar peli o serie segun titulo
    results_dict = {}

    for url, key, platform_name in PLATFORMS:

        genre_map = {}
        genres = get_genre(url, key)
        for g in genres:
            genre_map[g["id"]] = g["name"]

        # Buscar en movies
        try:
            response = requests.get(
                f"{url}/movies",
                headers={"X-API-KEY": key},
                params={"title": query},  # la API ya filtra por title con LIKE
                timeout=5
            )
            response.raise_for_status()
            for movie in response.json():
                movie["content_type"] = "movie"
                movie.setdefault("start_year", None)
                identifier = f"movie_{movie.get('title', '').lower().strip()}_{movie.get('year', '')}"
                if identifier not in results_dict:
                    movie["platforms"] = [platform_name]
                    movie["genre_name"] = genre_map.get(movie.get("genre_id"), "Unknown")
                    results_dict[identifier] = movie
                else:
                    if platform_name not in results_dict[identifier]["platforms"]:
                        results_dict[identifier]["platforms"].append(platform_name)
        except requests.exceptions.RequestException:
            pass  # plataforma no disponible, se ignora

        # Buscar en series
        try:
            response = requests.get(
                f"{url}/series",
                headers={"X-API-KEY": key},
                params={"title": query},
                timeout=5
            )
            response.raise_for_status()
            for serie in response.json():
                serie["content_type"] = "series"
                identifier = f"series_{serie.get('title', '').lower().strip()}_{serie.get('start_year', '')}"
                if identifier not in results_dict:
                    serie["platforms"] = [platform_name]
                    serie["genre_name"] = genre_map.get(serie.get("genre_id"), "Unknown")
                    results_dict[identifier] = serie
                else:
                    if platform_name not in results_dict[identifier]["platforms"]:
                        results_dict[identifier]["platforms"].append(platform_name)
        except requests.exceptions.RequestException:
            pass

    return list(results_dict.values())

```
<!-- END_FILE -->

---
<!-- FILE: app/static/css/main.css -->
## app/static/css/main.css

```css
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
                "background-light": "#f5f6f8",
                "background-dark": "#101622",
                "surface-dark": "#182234",
                "surface-light": "#ffffff",
                "border-dark": "#222f49",
                "border-light": "#e2e8f0",
            },
            fontFamily: {
                "display": ["Spline Sans", "sans-serif"]
            },
            borderRadius: {
                "DEFAULT": "0.25rem", 
                "lg": "0.5rem", 
                "xl": "0.75rem", 
                "full": "9999px"
            },
        },
    },
}

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
</head>
<body class="bg-background-dark dark:bg-background-dark text-slate-900 dark:text-slate-100 font-display min-h-screen flex flex-col overflow-x-hidden antialiased">

    {% include "components/navbar.html" %}

    <main class="flex-1 w-full max-w-7xl mx-auto px-6 py-8">
        {% block content %}{% endblock %}
    </main>

    {% include "components/footer.html" %}

</body>
</html>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/components/card_movies.html -->
## app/templates/components/card_movies.html

```html
{% for movie in movies %}
        <div class="group flex flex-col gap-3 transition-all duration-500 hover:scale-105">

            <div class="aspect-[2/3] rounded-xl overflow-hidden relative cinematic-shadow hover-electric">

                <!-- Image -->
                <img
                    src="https://via.placeholder.com/300x450?text=No+Image"
                    class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
                />

                <!-- Gradient -->
                <div class="absolute inset-0 bg-gradient-to-t from-[#101622] via-transparent to-transparent opacity-80"></div>

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
                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-all duration-300 flex flex-col justify-end p-4">
                    <button class="bg-primary text-white text-xs font-bold py-2 rounded-lg tracking-wide hover:bg-primary/80">
                        Watch now
                    </button>
                </div>

            </div>

            <!-- Info -->
            <div class="px-1">
                <h3 class="font-bold text-sm truncate group-hover:text-primary transition-colors">
                    {{ movie.title }}
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
            </div>

        </div>
        {% endfor %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/components/card_series.html -->
## app/templates/components/card_series.html

```html
{% for serie in series %}
        <div class="group flex flex-col gap-3 transition-all duration-500 hover:scale-105">

            <div class="aspect-[2/3] rounded-xl overflow-hidden relative cinematic-shadow hover-electric">

                <!-- Image -->
                <img
                    src="https://via.placeholder.com/300x450?text=No+Image"
                    class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
                />

                <!-- Gradient -->
                <div class="absolute inset-0 bg-gradient-to-t from-[#101622] via-transparent to-transparent opacity-80"></div>

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
                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-all duration-300 flex flex-col justify-end p-4">
                    <button class="bg-primary text-white text-xs font-bold py-2 rounded-lg tracking-wide hover:bg-primary/80">
                        Watch now
                    </button>
                </div>

            </div>

            <!-- Info -->
            <div class="px-1">
                <h3 class="font-bold text-sm truncate group-hover:text-primary transition-colors">
                    {{ serie.title }}
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
            </div>

        </div>
        {% endfor %}

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/components/footer.html -->
## app/templates/components/footer.html

```html
<footer class="border-t border-border-light dark:border-border-dark mt-auto py-8">
    <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-4">
        <p class="text-slate-500 dark:text-slate-400 text-sm">© 2023 StreamSync Inc. All rights reserved.</p>
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
<!-- FILE: app/templates/components/navbar.html -->
## app/templates/components/navbar.html

```html
<!-- Top Navigation -->
<header class="sticky top-0 z-50 w-full border-b border-solid border-border-light dark:border-border-dark bg-surface-light/80 dark:bg-background-dark/80 backdrop-blur-md px-6 py-4">
  <div class="max-w-7xl mx-auto flex items-center justify-between">
    
    <!-- Left Section (Logo + Nav) -->
    <div class="flex items-center gap-8">
      
      <!-- Logo -->
      <a href="{% url 'app:main' %}" class="flex items-center gap-3 text-primary">
        <div class="size-8 rounded-lg bg-primary/20 flex items-center justify-center">
          <span class="material-symbols-outlined text-primary text-2xl">play_circle</span>
        </div>
        <h2 class="text-slate-900 dark:text-white text-xl font-bold tracking-tight">
          StreamSync
        </h2>
      </a>

      <!-- Navigation Links -->
      <nav class="hidden md:flex items-center gap-6 text-sm font-medium">
        <a href="{% url 'app:catalog' %}" class="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors">
          Discover
        </a>
        <a href="{% url 'app:movies' %}" class="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors">
          Movies
        </a>
        <a href="{% url 'app:series' %}" class="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors">
          TV Shows
        </a>
        <a href="#" class="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors">
          My List
        </a>
      </nav>

    </div>

  <!-- Search Bar -->
  <div class="hidden md:flex flex-1 max-w-xl mx-8">
    <form action="{% url 'app:search' %}" method="GET" class="relative w-full group">
      
      <!-- Icono izquierda -->
      <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 dark:text-slate-500">
        <span class="material-symbols-outlined text-[20px]">search</span>
      </div>

      <!-- Input -->
      <input 
        type="text"
        name="q"
        value="{{ request.GET.q }}"
        placeholder="Search movies, shows, or platforms..."
        class="block w-full rounded-xl border-none bg-slate-100 dark:bg-[#1e293b] py-2.5 pl-10 pr-3 text-sm placeholder-slate-400 dark:placeholder-slate-500 text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all shadow-sm"
      />

      <!-- Shortcut derecha -->
      <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
        <span class="text-xs text-slate-400 dark:text-slate-500 border border-slate-200 dark:border-slate-700 rounded px-1.5 py-0.5">⌘K</span>
      </div>

    </form>
  </div>

    <!-- User Actions -->
    <div class="flex items-center gap-4">
      <button class="relative p-2 rounded-full hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors text-slate-600 dark:text-slate-400">
        <span class="material-symbols-outlined">notifications</span>
        <span class="absolute top-2 right-2 size-2 bg-red-500 rounded-full border-2 border-surface-light dark:border-background-dark"></span>
      </button>
      <div class="h-8 w-[1px] bg-border-light dark:bg-border-dark mx-1"></div>
      <button class="flex items-center gap-3 rounded-full pl-1 pr-1 py-1 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">
        <div class="size-9 rounded-full bg-cover bg-center border border-slate-200 dark:border-slate-700" 
          style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuDDIAQ90IxsinjXM6PKvOAaLRDc7SY_R-7MVZ7vKDplBK7950nw55ZsHlVjzpNJ8O2lOn4dzlyKwejQm-g1R1zTQ-yZAJh8gKj7DDUaFAjgMlw4f_G4wKHpDUU5KvzD1qk71kCOaHNW-DXrAhGOeBQGxvzYQeMW70BVbPqVRfxLbQuAyoV2zIfQjweJuxtG5gg4Nr-3nsr2ETbHgYaZBmzIGdzCM9pS9q1rVq1DLjeAigarT-PPxUa7ZeXqXbs6yqL6JUmGOnKS_X36");'>
        </div>
      </button>
    </div>

  </div>
</header>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/catalog.html -->
## app/templates/pages/catalog.html

```html
{% extends "base/base.html" %}

{% block title %}StreamSync – Catalog{% endblock %}

{% block content %}
<!-- Movies -->
<section class="mb-14">
    <h2 class="text-xl font-bold tracking-tight mb-6">MOVIES</h2>

    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">

        {% include "components/card_movies.html" %}

    </div>
</section>

<!-- Series -->
<section class="mb-14">
    <h2 class="text-xl font-bold tracking-tight mb-6">SERIES</h2>

    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">

        {% include "components/card_series.html" %}

    </div>
</section>
{% endblock %}


```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/content_view.html -->
## app/templates/pages/content_view.html

```html
<!DOCTYPE html>
<html class="dark" lang="en">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>StreamSync - Content Detail</title>
  <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
  <link href="https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
  <script>
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          colors: {
            "primary": "#256af4",
            "background-light": "#f5f6f8",
            "background-dark": "#101622",
            "surface-dark": "#1a2333",
          },
          fontFamily: {
            "display": ["Spline Sans", "sans-serif"]
          },
          borderRadius: {
            "DEFAULT": "0.25rem",
            "lg": "0.5rem",
            "xl": "0.75rem",
            "full": "9999px"
          },
        },
      },
    }
  </script>
  <style>
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #101622; }
    ::-webkit-scrollbar-thumb { background: #222f49; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #314368; }
    .glass-panel {
      background: rgba(26, 35, 51, 0.6);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.05);
    }
  </style>
</head>
<body class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100 font-display min-h-screen flex flex-col overflow-x-hidden">

  <!-- Top Navigation -->
  <header class="sticky top-0 z-50 flex items-center justify-between whitespace-nowrap border-b border-solid border-slate-200 dark:border-[#222f49] bg-background-light/90 dark:bg-[#101623]/90 backdrop-blur-md px-10 py-3">
    <div class="flex items-center gap-8">
      <div class="flex items-center gap-4 text-slate-900 dark:text-white">
        <div class="size-8 text-primary">
          <span class="material-symbols-outlined !text-4xl">play_circle</span>
        </div>
        <h2 class="text-slate-900 dark:text-white text-lg font-bold leading-tight tracking-[-0.015em]">StreamSync</h2>
      </div>
      <div class="hidden md:flex items-center gap-9">
        <a class="text-slate-600 dark:text-white hover:text-primary dark:hover:text-primary transition-colors text-sm font-medium leading-normal" href="#">Movies</a>
        <a class="text-slate-600 dark:text-white hover:text-primary dark:hover:text-primary transition-colors text-sm font-medium leading-normal" href="#">Series</a>
        <a class="text-slate-600 dark:text-white hover:text-primary dark:hover:text-primary transition-colors text-sm font-medium leading-normal" href="#">My List</a>
      </div>
    </div>
    <div class="flex flex-1 justify-end gap-6">
      <label class="hidden sm:flex flex-col min-w-40 !h-10 max-w-64">
        <div class="flex w-full flex-1 items-stretch rounded-lg h-full">
          <div class="text-slate-400 dark:text-[#90a4cb] flex border-none bg-slate-200 dark:bg-[#222f49] items-center justify-center pl-4 rounded-l-lg border-r-0">
            <span class="material-symbols-outlined text-xl">search</span>
          </div>
          <input
            class="form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-slate-900 dark:text-white focus:outline-0 focus:ring-0 border-none bg-slate-200 dark:bg-[#222f49] focus:border-none h-full placeholder:text-slate-400 dark:placeholder:text-[#90a4cb] px-4 rounded-l-none border-l-0 pl-2 text-base font-normal leading-normal"
            placeholder="Search titles..."
            value=""
          />
        </div>
      </label>
      <div class="flex items-center gap-4">
        <button class="flex items-center justify-center rounded-full size-10 bg-slate-200 dark:bg-[#222f49] text-slate-600 dark:text-white hover:bg-slate-300 dark:hover:bg-[#314368] transition-colors">
          <span class="material-symbols-outlined">notifications</span>
        </button>
        <div class="size-10 rounded-full bg-gradient-to-tr from-primary to-purple-500 overflow-hidden border-2 border-white dark:border-[#222f49]">
          <img
            alt="User Avatar"
            class="w-full h-full object-cover"
            src="https://lh3.googleusercontent.com/aida-public/AB6AXuD_N7fMliLsTQjdWP4RrFz7rqJ2kqy-ogoVRqzh6oq4yzZ_fBvb3TZzzrAd4cTs3eDuicZQhuXPaWd06OK3Gk5IKF2m5oiXykz-Ek4aQU261qL0KACAzvpSKc5wnUgNMl8_UFDZ-3jjSXbTQiLeFTzanML4FPQmJG0415Vpr5ObIIw-v2R2ymM2jdX_mSCiGpyYBSseJAxl080ThUo6e9NoruSIowApMzYfrU0ksmGu5BPMYw11TGYHBHQi-IN01sClae7k7nXzoe0T"
          />
        </div>
      </div>
    </div>
  </header>

  <main class="flex-grow">

    <!-- Hero Section -->
    <div
      class="relative w-full h-[60vh] min-h-[500px] bg-cover bg-center bg-no-repeat"
      data-alt="Dark moody cinematic sci-fi scene with red lighting"
      style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuDIW9lvG0NM2LwiYLiHL359dc0EkYYmbp_6eAWWWXShXQSJO-N8trRVqz7aP7pNRelXwLl06drautO-xgd9TgDSDC4YNtnaFNw5AFz2tsDQAco3hEjisR0Go8J-FHRdu3lyiv-EDSGEVmzFG9UxJYI8lvZ2gI9-dwPo2rcgcPw5SozWDgDKva4yGdJEJ8HuIWiNfQsr7I42zvEP3y0KZih1fVWk70pST3K5PXGJ-tRBbql3rYHOZucHzGA2jR3emCHwAjNb2u6RNFOF");'
    >
      <!-- Gradient Overlays -->
      <div class="absolute inset-0 bg-gradient-to-t from-background-light via-background-light/40 to-transparent dark:from-background-dark dark:via-background-dark/60 dark:to-transparent"></div>
      <div class="absolute inset-0 bg-gradient-to-r from-background-light/90 via-transparent to-transparent dark:from-background-dark/95 dark:via-background-dark/30 dark:to-transparent"></div>

      <div class="relative h-full container mx-auto px-6 lg:px-12 flex items-end pb-12">
        <div class="flex flex-col gap-6 max-w-3xl">

          <!-- Badges -->
          <div class="flex flex-wrap items-center gap-3">
            <span class="px-2 py-1 bg-red-600 text-white text-xs font-bold uppercase tracking-wider rounded">Netflix</span>
            <span class="px-2 py-1 bg-white/10 backdrop-blur-md border border-white/20 text-white text-xs font-medium rounded">4K Ultra HD</span>
            <span class="px-2 py-1 bg-white/10 backdrop-blur-md border border-white/20 text-white text-xs font-medium rounded">Dolby Atmos</span>
          </div>

          <!-- Title -->
          <h1 class="text-5xl md:text-7xl font-bold text-slate-900 dark:text-white leading-tight drop-shadow-lg">Stranger Things</h1>

          <!-- Metadata Row -->
          <div class="flex items-center gap-4 text-slate-700 dark:text-slate-300 text-sm md:text-base font-medium">
            <span>2016</span>
            <span class="w-1 h-1 rounded-full bg-current opacity-50"></span>
            <span>TV-14</span>
            <span class="w-1 h-1 rounded-full bg-current opacity-50"></span>
            <span>4 Seasons</span>
            <span class="w-1 h-1 rounded-full bg-current opacity-50"></span>
            <span>Sci-Fi, Horror, Drama</span>
          </div>

          <!-- Rating -->
          <div class="flex items-center gap-3">
            <div class="flex text-yellow-400">
              <span class="material-symbols-outlined !text-2xl fill-current">star</span>
              <span class="material-symbols-outlined !text-2xl fill-current">star</span>
              <span class="material-symbols-outlined !text-2xl fill-current">star</span>
              <span class="material-symbols-outlined !text-2xl fill-current">star</span>
              <span class="material-symbols-outlined !text-2xl">star_half</span>
            </div>
            <span class="text-2xl font-bold text-slate-900 dark:text-white">4.8</span>
            <span class="text-slate-600 dark:text-slate-400 text-sm">(12k reviews)</span>
          </div>

          <!-- Description -->
          <p class="text-slate-800 dark:text-slate-200 text-lg leading-relaxed line-clamp-3 max-w-2xl drop-shadow-sm">
            When a young boy disappears, his mother, a police chief and his friends must confront terrifying supernatural forces in order to get him back. A love letter to the '80s classics that captivated a generation.
          </p>

          <!-- Actions -->
          <div class="flex flex-wrap gap-4 mt-4">
            <button class="flex items-center gap-2 bg-primary hover:bg-blue-600 text-white px-8 py-3 rounded-lg font-bold text-lg shadow-lg shadow-primary/30 transition-all hover:scale-105">
              <span class="material-symbols-outlined">play_arrow</span>
              Watch on Netflix
            </button>
            <button class="flex items-center gap-2 glass-panel hover:bg-white/10 text-white px-6 py-3 rounded-lg font-medium transition-all">
              <span class="material-symbols-outlined">add</span>
              Add to Watchlist
            </button>
            <button class="flex items-center justify-center glass-panel hover:bg-white/10 text-white size-12 rounded-lg font-medium transition-all" title="Mark as Watched">
              <span class="material-symbols-outlined">check</span>
            </button>
            <button class="flex items-center justify-center glass-panel hover:bg-white/10 text-white size-12 rounded-lg font-medium transition-all" title="Share">
              <span class="material-symbols-outlined">share</span>
            </button>
          </div>

        </div>
      </div>
    </div>

    <!-- Content Body -->
    <div class="container mx-auto px-6 lg:px-12 py-12">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-12">

        <!-- Left Column: Episodes & Details -->
        <div class="lg:col-span-2 space-y-12">

          <!-- Episode Tracker -->
          <section>
            <div class="flex items-center justify-between mb-6">
              <h3 class="text-2xl font-bold text-slate-900 dark:text-white">Episodes</h3>
              <div class="relative">
                <select class="bg-slate-200 dark:bg-surface-dark text-slate-900 dark:text-white border-none rounded-lg py-2 pl-4 pr-10 focus:ring-1 focus:ring-primary cursor-pointer appearance-none font-medium">
                  <option>Season 4</option>
                  <option>Season 3</option>
                  <option>Season 2</option>
                  <option>Season 1</option>
                </select>
                <span class="material-symbols-outlined absolute right-2 top-2.5 pointer-events-none text-slate-500">expand_more</span>
              </div>
            </div>

            <div class="space-y-4">

              <!-- Episode 1 -->
              <div class="group flex flex-col sm:flex-row gap-4 p-4 rounded-xl bg-slate-100 dark:bg-surface-dark hover:bg-slate-200 dark:hover:bg-[#222f49] transition-colors cursor-pointer border border-transparent dark:border-white/5">
                <div class="relative sm:w-48 h-28 flex-shrink-0 rounded-lg overflow-hidden bg-slate-300 dark:bg-black">
                  <img
                    alt="Abstract dark scene representing a TV episode thumbnail"
                    class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuACgWBOiwg84r-mfJe-Q3i7YEI7m7QUvkPYC-7qbkOnSpD3ed7ugM170yxULykkyV0Ll-fKUrlzWEhHIMQA7x6TvIJ1nVTPxb9LdtxDo5zJWOlZjLVIenyTFg4NFFWv_BpcmKUMqVwkXfgIW9vZ1Al2o-Yc-uDe8Z2om5xgj4paJqpxvZh3aLiMVhhYE9eF7K2dUfdT5Z3r4KePyv725oTzgP89zYAmjtkJfe_cqJdwLtdOU8i3c3AMr0Q3xoJvxZie-dY3qXK_yrsr"
                  />
                  <div class="absolute inset-0 flex items-center justify-center bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity">
                    <span class="material-symbols-outlined text-white !text-4xl">play_circle</span>
                  </div>
                  <div class="absolute bottom-2 right-2 px-1.5 py-0.5 bg-black/80 text-white text-xs rounded font-medium">1h 18m</div>
                </div>
                <div class="flex flex-col flex-1 justify-center">
                  <div class="flex justify-between items-start">
                    <h4 class="text-lg font-bold text-slate-900 dark:text-white group-hover:text-primary transition-colors">
                      1. Chapter One: The Hellfire Club
                    </h4>
                    <div class="hidden sm:block">
                      <button class="text-slate-400 hover:text-primary transition-colors">
                        <span class="material-symbols-outlined">download</span>
                      </button>
                    </div>
                  </div>
                  <p class="text-slate-600 dark:text-slate-400 text-sm mt-2 line-clamp-2">
                    Hawkins High stands on the precipice of change as the gang navigates high school, a new D&amp;D club, and a horrifying new threat.
                  </p>
                  <div class="mt-3 w-full bg-slate-300 dark:bg-slate-700 h-1 rounded-full overflow-hidden">
                    <div class="bg-primary h-full rounded-full" style="width: 100%"></div>
                  </div>
                  <span class="text-xs text-primary mt-1 font-medium">Watched</span>
                </div>
              </div>

              <!-- Episode 2 -->
              <div class="group flex flex-col sm:flex-row gap-4 p-4 rounded-xl bg-slate-100 dark:bg-surface-dark hover:bg-slate-200 dark:hover:bg-[#222f49] transition-colors cursor-pointer border border-transparent dark:border-white/5">
                <div class="relative sm:w-48 h-28 flex-shrink-0 rounded-lg overflow-hidden bg-slate-300 dark:bg-black">
                  <img
                    alt="Dark moody forest scene thumbnail"
                    class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuDdCgZV9zBVlK7IcicFbuGunuEU3xbvk_7Ru9MuwPCZT5W8b4HZQrYqF6NCbG_DiGDyPtttcNFRgHGnWHTCGFcTckTiay8s2I5DibLD791e49KxOY0SMPsZgT63KI0wkARtXLEpasCRQi9Mityuv7tMXy1ywbZMnkIJh37GCh3wqbDDuW0xAzdxLPou5_XFBSEl-zkYwyFYMAe6QStSnGoR857fcWR6Lef_gw4R6WYVv0ian9YMQKLzehV6nyjF5sRyTixPPLopS0XN"
                  />
                  <div class="absolute inset-0 flex items-center justify-center bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity">
                    <span class="material-symbols-outlined text-white !text-4xl">play_circle</span>
                  </div>
                  <div class="absolute bottom-2 right-2 px-1.5 py-0.5 bg-black/80 text-white text-xs rounded font-medium">1h 15m</div>
                </div>
                <div class="flex flex-col flex-1 justify-center">
                  <div class="flex justify-between items-start">
                    <h4 class="text-lg font-bold text-slate-900 dark:text-white group-hover:text-primary transition-colors">
                      2. Chapter Two: Vecna's Curse
                    </h4>
                  </div>
                  <p class="text-slate-600 dark:text-slate-400 text-sm mt-2 line-clamp-2">
                    A plane crash brings unexpected visitors to Russia. Mike flies to California. A death in Hawkins sparks fear and confusion.
                  </p>
                  <div class="mt-3 w-full bg-slate-300 dark:bg-slate-700 h-1 rounded-full overflow-hidden">
                    <div class="bg-primary h-full rounded-full" style="width: 45%"></div>
                  </div>
                  <span class="text-xs text-slate-500 dark:text-slate-400 mt-1 font-medium">34m remaining</span>
                </div>
              </div>

              <!-- Episode 3 -->
              <div class="group flex flex-col sm:flex-row gap-4 p-4 rounded-xl bg-transparent hover:bg-slate-100 dark:hover:bg-[#222f49] transition-colors cursor-pointer border border-slate-200 dark:border-white/10">
                <div class="relative sm:w-48 h-28 flex-shrink-0 rounded-lg overflow-hidden bg-slate-300 dark:bg-black">
                  <img
                    alt="Red abstract pattern thumbnail"
                    class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500 grayscale opacity-70 group-hover:grayscale-0 group-hover:opacity-100"
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuCg3DOzDxQZsFKaj400NDGVGaI0XFR_WhgjeaK_1kARJllxk2eqXsBZPNqH9BaT09T8yUSF8G9_1vCr9UhvfTdM8pMZOr-G8czIBLPHu_FDuNa19RHWaX0YoOkboCNRDtVhkhDS76J7Wvj8HboAGl3m1fn433-qJlSItRj_66zYgWLMn43GOTYOBHcSB8qHLHHkh4bv5kmqFEqHTLNMq-VbCKgSWYHdx4zipRc7Viua3-4wbMrj_ml3nnus7XrSzra1Fj-XByFn8hNx"
                  />
                  <div class="absolute inset-0 flex items-center justify-center bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity">
                    <span class="material-symbols-outlined text-white !text-4xl">play_circle</span>
                  </div>
                  <div class="absolute bottom-2 right-2 px-1.5 py-0.5 bg-black/80 text-white text-xs rounded font-medium">1h 03m</div>
                </div>
                <div class="flex flex-col flex-1 justify-center">
                  <div class="flex justify-between items-start">
                    <h4 class="text-lg font-bold text-slate-900 dark:text-white group-hover:text-primary transition-colors">
                      3. Chapter Three: The Monster and the Superhero
                    </h4>
                  </div>
                  <p class="text-slate-600 dark:text-slate-400 text-sm mt-2 line-clamp-2">
                    Murray and Joyce fly to Alaska, and El faces serious consequences. Robin and Nancy investigate Hawkins' demons.
                  </p>
                </div>
              </div>

            </div>
          </section>

          <!-- Cast & Crew -->
          <section>
            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-6">Cast</h3>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-6">

              <!-- Cast Member 1 -->
              <div class="flex flex-col items-center text-center gap-3 group cursor-pointer">
                <div class="size-24 rounded-full overflow-hidden border-2 border-transparent group-hover:border-primary transition-colors">
                  <img
                    alt="Actor headshot"
                    class="w-full h-full object-cover"
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuAZ5Mw8naiJ4WCPPyUeYRRHeyBHA5uASmRclhkvSR4qAnHgyMzWKpirSnBWUeTEphupr8bG_sb0fpJHnuDMcVHf1TKTZ-Wq8CzbQScf5ci1j6fFDsNZ-dFoJh06ZJXun2Kl-AbXEu5XZC3Xg9-rWgyys2nX8ZtzvoItkBfaAtxx0T5rtTaP8GJoSKqiofMQPQMsywahYStuyoFgAb99UZg0ka36Zr8tLnYbH3NBQ3dbDBT_AYqKr80ZELtk9aQ5gxLKunAssYgmZ-7b"
                  />
                </div>
                <div>
                  <h5 class="text-slate-900 dark:text-white font-bold text-sm">Millie B. Brown</h5>
                  <p class="text-slate-500 dark:text-slate-400 text-xs">Eleven</p>
                </div>
              </div>

              <!-- Cast Member 2 -->
              <div class="flex flex-col items-center text-center gap-3 group cursor-pointer">
                <div class="size-24 rounded-full overflow-hidden border-2 border-transparent group-hover:border-primary transition-colors">
                  <img
                    alt="Actor headshot"
                    class="w-full h-full object-cover"
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuBVm4F2-8ONAwAN8l4tfqqPUmqhQog8HhP9veZ5iGSGvkvHYA3VeX6HpZDa13mUz0j2-07L3ZUq4ySKZZTnv4dHDy0OxWY0TOLGJpZIPxtURe2RLx9edCFIEosjN-CkkrZ8Rj_5MXy7ngRxPzevhrXtmqKT3W-qzrlm99HQ-1K68zzJ10Gxr1YyedIYDIVn_Jhu8sOS4nA2qQvW87reBeal3Ft8oiBMidxgSXjRTpn7tACcR8uZQg_DCAqIlaiRGX3_7OGK6i0oJz7J"
                  />
                </div>
                <div>
                  <h5 class="text-slate-900 dark:text-white font-bold text-sm">Finn Wolfhard</h5>
                  <p class="text-slate-500 dark:text-slate-400 text-xs">Mike Wheeler</p>
                </div>
              </div>

              <!-- Cast Member 3 -->
              <div class="flex flex-col items-center text-center gap-3 group cursor-pointer">
                <div class="size-24 rounded-full overflow-hidden border-2 border-transparent group-hover:border-primary transition-colors">
                  <img
                    alt="Actor headshot"
                    class="w-full h-full object-cover"
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuC-p1qM1Hq7NZzDtDhuwVgOynZznpe8fS7XMkdl9C94xIy4uny6pPyTJkJdfgypvn9FCiznQW6TaVp5f2fomTSfBUrn3931ghMHEzI-k15JnhCr22RMUgXN_Bm7Isr_9SsukojG-GbXbXiqJp8JWJVhnWnDAUZgga6yFqOiRYDicXr-D4K0wHo03bcK5_VItZU0cnrxozRaBnY6heDOw2tvWG-ix11tMSfZaHvrlESMncJUhhnXro5tci3EIVwux4zq1OvnSHO75shJ"
                  />
                </div>
                <div>
                  <h5 class="text-slate-900 dark:text-white font-bold text-sm">Winona Ryder</h5>
                  <p class="text-slate-500 dark:text-slate-400 text-xs">Joyce Byers</p>
                </div>
              </div>

              <!-- Cast Member 4 -->
              <div class="flex flex-col items-center text-center gap-3 group cursor-pointer">
                <div class="size-24 rounded-full overflow-hidden border-2 border-transparent group-hover:border-primary transition-colors">
                  <img
                    alt="Actor headshot"
                    class="w-full h-full object-cover"
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuCe9kZkdYIkwNT9lJFmrqnN3OGrBq6RK-hpJEkzvP-yLGGXfBlNfYJruf0eIwmq_BUjRDP50HetJL_Yi-C7T4EzpHXxetiD8fJ_yES-xh7GAyt3i4eqoIJd-7xSSqOrJIIOzQofV1ZHn_3xYbrh8ZSyJIHuuAI5rRrW3Ws2LFp5pE38Cy7az-y9znn_lz1DUM3974Oqoqn3AQ8nSscvdrciU3mjdtCBY6AxHYYfXl0ZbXHBYHPA0E8RWJ5waTrQo7Fo5WJQlqgTGBsO"
                  />
                </div>
                <div>
                  <h5 class="text-slate-900 dark:text-white font-bold text-sm">David Harbour</h5>
                  <p class="text-slate-500 dark:text-slate-400 text-xs">Jim Hopper</p>
                </div>
              </div>

              <!-- Cast Member 5 -->
              <div class="flex flex-col items-center text-center gap-3 group cursor-pointer">
                <div class="size-24 rounded-full overflow-hidden border-2 border-transparent group-hover:border-primary transition-colors">
                  <img
                    alt="Actor headshot"
                    class="w-full h-full object-cover"
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuCNYu7d-cWtjHOVqN8yYQroWfeCpS8McMYx9rFLGcfh41Zs3vGFDTtftxiJIVFoX4SpLkvv3kEK7aRqWMtUROQRN9jGyVNKGLXQ6JcFn2aS7o4zoZgDxqi9EPTavDafLQn9akFLqjs9IqMfzBOWayWtPOxfTgiYzSYxwoWoF9apJm3IrTRR86-yT_fPG6raqI0V4d0nwgPStuny3XkxzUNjozO3N_Dhy2jFV4PtkCQSo3XulRjaqMgLtU2RCzpJit53qeGAI6-4VN1n"
                  />
                </div>
                <div>
                  <h5 class="text-slate-900 dark:text-white font-bold text-sm">Gaten M.</h5>
                  <p class="text-slate-500 dark:text-slate-400 text-xs">Dustin Henderson</p>
                </div>
              </div>

            </div>
          </section>

        </div>

        <!-- Right Column: Sidebar Stats & Similar -->
        <div class="space-y-8">

          <!-- Rating Breakdown -->
          <div class="p-6 rounded-xl bg-slate-100 dark:bg-surface-dark border border-slate-200 dark:border-white/5">
            <h4 class="text-lg font-bold text-slate-900 dark:text-white mb-4">Audience Rating</h4>
            <div class="grid grid-cols-[20px_1fr_40px] items-center gap-y-3">
              <p class="text-slate-900 dark:text-white text-sm font-medium">5</p>
              <div class="flex h-2 flex-1 overflow-hidden rounded-full bg-slate-200 dark:bg-[#314368]">
                <div class="rounded-full bg-primary" style="width: 80%;"></div>
              </div>
              <p class="text-slate-500 dark:text-[#90a4cb] text-sm text-right">80%</p>

              <p class="text-slate-900 dark:text-white text-sm font-medium">4</p>
              <div class="flex h-2 flex-1 overflow-hidden rounded-full bg-slate-200 dark:bg-[#314368]">
                <div class="rounded-full bg-primary" style="width: 12%;"></div>
              </div>
              <p class="text-slate-500 dark:text-[#90a4cb] text-sm text-right">12%</p>

              <p class="text-slate-900 dark:text-white text-sm font-medium">3</p>
              <div class="flex h-2 flex-1 overflow-hidden rounded-full bg-slate-200 dark:bg-[#314368]">
                <div class="rounded-full bg-primary" style="width: 5%;"></div>
              </div>
              <p class="text-slate-500 dark:text-[#90a4cb] text-sm text-right">5%</p>

              <p class="text-slate-900 dark:text-white text-sm font-medium">2</p>
              <div class="flex h-2 flex-1 overflow-hidden rounded-full bg-slate-200 dark:bg-[#314368]">
                <div class="rounded-full bg-primary" style="width: 2%;"></div>
              </div>
              <p class="text-slate-500 dark:text-[#90a4cb] text-sm text-right">2%</p>

              <p class="text-slate-900 dark:text-white text-sm font-medium">1</p>
              <div class="flex h-2 flex-1 overflow-hidden rounded-full bg-slate-200 dark:bg-[#314368]">
                <div class="rounded-full bg-primary" style="width: 1%;"></div>
              </div>
              <p class="text-slate-500 dark:text-[#90a4cb] text-sm text-right">1%</p>
            </div>
            <button class="w-full mt-6 py-2 rounded-lg border border-slate-300 dark:border-slate-600 text-slate-900 dark:text-white hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors text-sm font-medium">
              Write a Review
            </button>
          </div>

          <!-- Where to Watch -->
          <div class="p-6 rounded-xl bg-slate-100 dark:bg-surface-dark border border-slate-200 dark:border-white/5">
            <h4 class="text-lg font-bold text-slate-900 dark:text-white mb-4">Available On</h4>
            <div class="space-y-3">
              <a class="flex items-center justify-between p-3 rounded-lg bg-white dark:bg-[#101622] hover:bg-gray-50 dark:hover:bg-[#1a2333] border border-slate-200 dark:border-slate-800 transition-colors" href="#">
                <div class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded bg-red-600 flex items-center justify-center text-white font-bold text-xs">N</div>
                  <span class="text-slate-900 dark:text-white font-medium">Netflix</span>
                </div>
                <span class="text-xs text-slate-500 dark:text-slate-400">4K HDR</span>
              </a>
              <a class="flex items-center justify-between p-3 rounded-lg bg-white dark:bg-[#101622] hover:bg-gray-50 dark:hover:bg-[#1a2333] border border-slate-200 dark:border-slate-800 transition-colors" href="#">
                <div class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded bg-blue-500 flex items-center justify-center text-white font-bold text-xs">P</div>
                  <span class="text-slate-900 dark:text-white font-medium">Prime Video</span>
                </div>
                <span class="text-xs text-slate-500 dark:text-slate-400">Buy/Rent</span>
              </a>
            </div>
          </div>

          <!-- Information -->
          <div>
            <h4 class="text-lg font-bold text-slate-900 dark:text-white mb-4">Information</h4>
            <div class="space-y-3 text-sm">
              <div class="flex justify-between border-b border-slate-200 dark:border-slate-800 pb-2">
                <span class="text-slate-500 dark:text-slate-400">Original Title</span>
                <span class="text-slate-900 dark:text-white font-medium">Stranger Things</span>
              </div>
              <div class="flex justify-between border-b border-slate-200 dark:border-slate-800 pb-2">
                <span class="text-slate-500 dark:text-slate-400">Status</span>
                <span class="text-slate-900 dark:text-white font-medium">Returning Series</span>
              </div>
              <div class="flex justify-between border-b border-slate-200 dark:border-slate-800 pb-2">
                <span class="text-slate-500 dark:text-slate-400">Network</span>
                <span class="text-slate-900 dark:text-white font-medium">Netflix</span>
              </div>
              <div class="flex justify-between border-b border-slate-200 dark:border-slate-800 pb-2">
                <span class="text-slate-500 dark:text-slate-400">Language</span>
                <span class="text-slate-900 dark:text-white font-medium">English</span>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- Similar Content Row -->
      <div class="mt-16 pb-12">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-2xl font-bold text-slate-900 dark:text-white">You Might Also Like</h3>
          <div class="flex gap-2">
            <button class="p-2 rounded-full border border-slate-200 dark:border-slate-700 hover:bg-slate-200 dark:hover:bg-slate-800 text-slate-900 dark:text-white transition-colors">
              <span class="material-symbols-outlined">chevron_left</span>
            </button>
            <button class="p-2 rounded-full border border-slate-200 dark:border-slate-700 hover:bg-slate-200 dark:hover:bg-slate-800 text-slate-900 dark:text-white transition-colors">
              <span class="material-symbols-outlined">chevron_right</span>
            </button>
          </div>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-6">

          <!-- Card 1 -->
          <div class="group relative cursor-pointer">
            <div class="aspect-[2/3] rounded-lg overflow-hidden relative">
              <img
                alt="Dark movie poster with silhouettes"
                class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-110"
                src="https://lh3.googleusercontent.com/aida-public/AB6AXuBYm3NWVfq7leHvo_U8i3lzO-A6ifTaVDvwfSzmVdvvawCVVZbZD3rKH3TvxiBFZ225YOJbTHXFLyRpe0xmrH4dDzo_n2EIDRPCJXIrrvUeyUCwgGjskgvimmFG494vJ6q_2SJMsZvkDq3PT5Wt_4RJEp-GrJfMgXdh7ItSIPw23NyIQSBif6t_SnzLwIHOWIajEnFXgwreuKdyGpGVVg1K2fjZOi28TZBV-9FtGMdbRMFt9nZ9uzn2q1DSz3UOl7XPbDbU_zG8qa4O"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
                <button class="w-full py-2 bg-primary text-white rounded font-bold text-sm">View Details</button>
              </div>
              <div class="absolute top-2 left-2 px-2 py-1 bg-black/60 backdrop-blur-sm rounded text-[10px] text-white font-bold uppercase">98% Match</div>
            </div>
            <h4 class="mt-2 text-slate-900 dark:text-white font-bold truncate">Dark</h4>
            <div class="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
              <span>2017</span>
              <span class="flex items-center gap-1">
                <span class="material-symbols-outlined !text-xs text-yellow-400 fill-current">star</span>
                8.8
              </span>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="group relative cursor-pointer">
            <div class="aspect-[2/3] rounded-lg overflow-hidden relative">
              <img
                alt="Abstract sci-fi poster"
                class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-110"
                src="https://lh3.googleusercontent.com/aida-public/AB6AXuCI4PwAM4b8ap4cC0vn-qKbHSF-KWPujlpV2qGuAGcp67LOneDL1dzbCwT2cqBQLJKBGRGMDGg4-nmRId5pqa22Wd9qjz7FfWmO-7MrNZpcShOZR4Lb11d855d3ibhjp0dDMs2rSGkpahHOKItEjeiuj5DuhodEh1og9n2OxbgY4YIB7tTl-uDWxjy3HMMVKfZkaNVVFnpCB87IUAj4TJBtdHpViE6D30u68BblycCIRKB5CmImcccIsZf5HOSljHwzl-c1_uFFNXPI"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
                <button class="w-full py-2 bg-primary text-white rounded font-bold text-sm">View Details</button>
              </div>
            </div>
            <h4 class="mt-2 text-slate-900 dark:text-white font-bold truncate">Black Mirror</h4>
            <div class="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
              <span>2011</span>
              <span class="flex items-center gap-1">
                <span class="material-symbols-outlined !text-xs text-yellow-400 fill-current">star</span>
                8.7
              </span>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="group relative cursor-pointer">
            <div class="aspect-[2/3] rounded-lg overflow-hidden relative">
              <img
                alt="Mysterious forest poster"
                class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-110"
                src="https://lh3.googleusercontent.com/aida-public/AB6AXuDzpxOui7rvRL92p6gsD80-W8b8OyRyofSUyopXU5Tis3w7gzG5muw37lEJ4Fa-grWVrkXTHqjFj0CfJ9LYIL9meyreCUyGuX-ZiJmYdgtrBbxLgOdplyi5ORzf10fiDlaqRnI-GWu3qDoUGb3uTrOr5GDw6Pu8OZDlHlu3LLCY-T6fHM8tmIIW0_s2GrqPf-xCGCsNWbHW4PJh2V4s5krZpPbhc9t-oVj8t8_i87kco7Ic-c-_iO0uNh_cAlTLgjUR-tJrK6c1T0UZ"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
                <button class="w-full py-2 bg-primary text-white rounded font-bold text-sm">View Details</button>
              </div>
            </div>
            <h4 class="mt-2 text-slate-900 dark:text-white font-bold truncate">Twin Peaks</h4>
            <div class="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
              <span>1990</span>
              <span class="flex items-center gap-1">
                <span class="material-symbols-outlined !text-xs text-yellow-400 fill-current">star</span>
                8.8
              </span>
            </div>
          </div>

          <!-- Card 4 -->
          <div class="group relative cursor-pointer">
            <div class="aspect-[2/3] rounded-lg overflow-hidden relative">
              <img
                alt="Futuristic city poster"
                class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-110"
                src="https://lh3.googleusercontent.com/aida-public/AB6AXuDAzKPgWoN5SVZnbbB5llv8Hry6Zt87squMlQ2jBsiBuCNFTHJac-dFgbJ6K2Vaq1vw20GfcvF8-mTWuw1gG4GAA82G0hM1AYnH3fBbW7D_U5-eRMwdVwNJpxjtDP1Ec6vPLV4zVlnHol6vDRkG1yrVnc4og5iqENkurbepblm9prKzBVRCm0qV6zkjOLvDUSgV8lP_UD3_Il3_KTGzM9Emx3U5UEvFrVE9qNMGAU29dsN_u-SqfMz_BIsjbYnUIWeFr8-2oc5FbQqS"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
                <button class="w-full py-2 bg-primary text-white rounded font-bold text-sm">View Details</button>
              </div>
            </div>
            <h4 class="mt-2 text-slate-900 dark:text-white font-bold truncate">Altered Carbon</h4>
            <div class="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
              <span>2018</span>
              <span class="flex items-center gap-1">
                <span class="material-symbols-outlined !text-xs text-yellow-400 fill-current">star</span>
                7.9
              </span>
            </div>
          </div>

          <!-- Card 5 -->
          <div class="group relative cursor-pointer hidden lg:block">
            <div class="aspect-[2/3] rounded-lg overflow-hidden relative">
              <img
                alt="Eerie book cover style poster"
                class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-110"
                src="https://lh3.googleusercontent.com/aida-public/AB6AXuBYO89MMHHrywzQIoQaIs1Pf6Fwu23d8CO4wZwkipGwtV_VQc8aRs6ze43hH5292L_HqFOIX8st9wiB46r9zETit7l1ddCxagmWnDMK0-9z5Wh2gCM6zTGfhG2x0-Kfwt83UZ9EytjelG5nwTqQ6VBReusGXQ4paHRlUgP9miJdfjAnMtwSRFPjwfvGM2CejTzJ65sgaeXykjZEGKHu5aD2wAkYAyejp44S4BtJkwJJ0ZeaNAhdou1kgZ1Np0WjxMZcUhFbyghJx42n"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
                <button class="w-full py-2 bg-primary text-white rounded font-bold text-sm">View Details</button>
              </div>
            </div>
            <h4 class="mt-2 text-slate-900 dark:text-white font-bold truncate">Locke &amp; Key</h4>
            <div class="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
              <span>2020</span>
              <span class="flex items-center gap-1">
                <span class="material-symbols-outlined !text-xs text-yellow-400 fill-current">star</span>
                7.3
              </span>
            </div>
          </div>

        </div>
      </div>
    </div>

  </main>

</body>
</html>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/pages/home.html -->
## app/templates/pages/home.html

```html
<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>StreamSync - Premium Streaming Aggregator</title>
<!-- Fonts -->
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<!-- Icons -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
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
<a class="text-slate-600 dark:text-slate-400 hover:text-primary dark:hover:text-primary transition-colors text-sm font-medium" href="#">Features</a>
<a class="text-slate-600 dark:text-slate-400 hover:text-primary dark:hover:text-primary transition-colors text-sm font-medium" href="#">Pricing</a>
<a class="text-slate-600 dark:text-slate-400 hover:text-primary dark:hover:text-primary transition-colors text-sm font-medium" href="#">About Us</a>
</div>
<div class="flex gap-3">
<button class="h-10 px-5 rounded-lg text-slate-900 dark:text-white text-sm font-bold border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all">
                                    Log In
                                </button>
<button class="h-10 px-5 rounded-lg bg-primary text-white text-sm font-bold hover:bg-blue-600 shadow-lg shadow-primary/25 transition-all">
                                    Sign Up
                                </button>
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
<button class="h-12 px-8 rounded-xl bg-primary hover:bg-blue-600 text-white text-base font-bold tracking-wide shadow-xl shadow-primary/30 transition-all transform hover:scale-105">
                                        Start Free Trial
                                    </button>
<button class="glass-btn h-12 px-8 rounded-xl text-white text-base font-bold tracking-wide hover:bg-white/10 transition-all flex items-center justify-center gap-2 group/btn">
<span class="material-symbols-outlined text-xl group-hover/btn:translate-x-1 transition-transform">play_circle</span>
                                        Watch Demo
                                    </button>
</div>
</div>
<!-- Decorative blur -->
<div class="absolute -bottom-1/2 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-primary/20 rounded-full blur-[120px] -z-10 pointer-events-none"></div>
</div>
</div>
<!-- Stats Section -->
<div class="px-6 py-10 w-full">
<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
<div class="glass-card p-6 rounded-xl flex flex-col items-center justify-center text-center gap-2 hover:border-primary/30 transition-colors">
<p class="text-primary text-4xl font-bold tracking-tighter">50+</p>
<p class="text-slate-400 font-medium text-sm uppercase tracking-wider">Services Integrated</p>
</div>
<div class="glass-card p-6 rounded-xl flex flex-col items-center justify-center text-center gap-2 hover:border-primary/30 transition-colors">
<p class="text-primary text-4xl font-bold tracking-tighter">1M+</p>
<p class="text-slate-400 font-medium text-sm uppercase tracking-wider">Movies Indexed</p>
</div>
<div class="glass-card p-6 rounded-xl flex flex-col items-center justify-center text-center gap-2 hover:border-primary/30 transition-colors">
<p class="text-primary text-4xl font-bold tracking-tighter">500k+</p>
<p class="text-slate-400 font-medium text-sm uppercase tracking-wider">Active Users</p>
</div>
</div>
</div>
<!-- Features Section -->
<div class="flex flex-col gap-12 px-6 py-16 w-full">
<div class="flex flex-col md:flex-row justify-between items-end gap-6 border-b border-slate-800 pb-8">
<div class="flex flex-col gap-3 max-w-2xl">
<h3 class="text-primary font-bold text-sm tracking-widest uppercase">Premium Tools</h3>
<h2 class="text-slate-900 dark:text-white text-3xl md:text-5xl font-bold tracking-tight">
                                    Unlock your full viewing potential
                                </h2>
<p class="text-slate-600 dark:text-slate-400 text-lg">Powerful features designed to save you time and help you discover your next obsession.</p>
</div>
<button class="hidden md:flex items-center gap-2 text-primary font-bold hover:text-blue-400 transition-colors">
                                Explore all features
                                <span class="material-symbols-outlined text-sm">arrow_forward</span>
</button>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
<!-- Feature 1 -->
<div class="glass-card p-6 rounded-2xl flex flex-col gap-4 group hover:-translate-y-1 transition-transform duration-300">
<div class="size-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
<span class="material-symbols-outlined text-3xl">search</span>
</div>
<div>
<h3 class="text-slate-900 dark:text-white text-lg font-bold mb-2">Unified Search</h3>
<p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                        Stop jumping between tabs. Search across Netflix, Hulu, HBO, and Disney+ instantly from one bar.
                                    </p>
</div>
</div>
<!-- Feature 2 -->
<div class="glass-card p-6 rounded-2xl flex flex-col gap-4 group hover:-translate-y-1 transition-transform duration-300">
<div class="size-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
<span class="material-symbols-outlined text-3xl">checklist</span>
</div>
<div>
<h3 class="text-slate-900 dark:text-white text-lg font-bold mb-2">Series Tracking</h3>
<p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                        Never forget which episode you're on. Keep track of every season and episode automatically.
                                    </p>
</div>
</div>
<!-- Feature 3 -->
<div class="glass-card p-6 rounded-2xl flex flex-col gap-4 group hover:-translate-y-1 transition-transform duration-300">
<div class="size-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
<span class="material-symbols-outlined text-3xl">auto_awesome</span>
</div>
<div>
<h3 class="text-slate-900 dark:text-white text-lg font-bold mb-2">Smart Recs</h3>
<p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                        AI-driven suggestions that understand your unique taste better than any single platform algorithm.
                                    </p>
</div>
</div>
<!-- Feature 4 -->
<div class="glass-card p-6 rounded-2xl flex flex-col gap-4 group hover:-translate-y-1 transition-transform duration-300">
<div class="size-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
<span class="material-symbols-outlined text-3xl">notifications_active</span>
</div>
<div>
<h3 class="text-slate-900 dark:text-white text-lg font-bold mb-2">Availability Alerts</h3>
<p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                        Get notified the second a movie on your watchlist becomes available on your subscribed services.
                                    </p>
</div>
</div>
</div>
<button class="md:hidden w-full h-12 rounded-lg border border-slate-700 text-slate-300 font-bold hover:bg-slate-800 transition-all flex items-center justify-center gap-2">
                            Explore all features
                            <span class="material-symbols-outlined text-sm">arrow_forward</span>
</button>
</div>
<!-- CTA Section -->
<div class="w-full px-6 py-16 md:py-24">
<div class="relative w-full rounded-3xl overflow-hidden bg-slate-900 border border-slate-800 p-8 md:p-16 flex flex-col md:flex-row items-center justify-between gap-10">
<!-- Background gradient for CTA -->
<div class="absolute top-0 right-0 w-1/2 h-full bg-gradient-to-l from-primary/10 to-transparent pointer-events-none"></div>
<div class="flex flex-col gap-4 z-10 max-w-xl">
<h2 class="text-3xl md:text-4xl font-black text-white leading-tight">
                                    Ready to sync your stream?
                                </h2>
<p class="text-slate-400 text-lg">
                                    Join thousands of users simplifying their entertainment life today. Cancel anytime.
                                </p>
</div>
<div class="w-full max-w-md z-10">
<form class="flex flex-col sm:flex-row gap-3">
<input class="flex-1 h-12 rounded-lg bg-slate-800 border-slate-700 text-white placeholder:text-slate-500 focus:ring-2 focus:ring-primary focus:border-transparent px-4 outline-none transition-all" placeholder="Enter your email address" type="email"/>
<button class="h-12 px-6 rounded-lg bg-primary hover:bg-blue-600 text-white font-bold whitespace-nowrap shadow-lg shadow-primary/20 transition-all" type="submit">
                                        Get Started
                                    </button>
</form>
<p class="mt-3 text-xs text-slate-500 text-center sm:text-left">No credit card required for 14-day trial.</p>
</div>
</div>
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
<a class="text-sm text-slate-500 hover:text-primary transition-colors" href="#">Privacy Policy</a>
<a class="text-sm text-slate-500 hover:text-primary transition-colors" href="#">Terms of Service</a>
<a class="text-sm text-slate-500 hover:text-primary transition-colors" href="#">Help Center</a>
<a class="text-sm text-slate-500 hover:text-primary transition-colors" href="#">Contact</a>
</div>
<div class="flex gap-4">
<a class="text-slate-400 hover:text-white transition-colors" href="#">
<svg aria-hidden="true" class="h-5 w-5" fill="currentColor" viewbox="0 0 24 24"><path clip-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" fill-rule="evenodd"></path></svg>
</a>
<a class="text-slate-400 hover:text-white transition-colors" href="#">
<svg aria-hidden="true" class="h-5 w-5" fill="currentColor" viewbox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"></path></svg>
</a>
<a class="text-slate-400 hover:text-white transition-colors" href="#">
<svg aria-hidden="true" class="h-5 w-5" fill="currentColor" viewbox="0 0 24 24"><path clip-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 016.588 3.32c.636-.247 1.363-.416 2.427-.465C10.051 2.013 10.406 2 12.315 2zm-4.755 8.461c-1.57 0-2.841 1.272-2.841 2.841 0 1.57 1.271 2.841 2.841 2.841 1.57 0 2.841-1.271 2.841-2.841 0-1.57-1.272-2.841-2.841-2.841zm6.617-3.26c-.724 0-1.312.588-1.312 1.312 0 .724.588 1.312 1.312 1.312.724 0 1.312-.588 1.312-1.312 0-.724-.588-1.312-1.312-1.312zm-4.305 6.1c1.514 0 2.744 1.23 2.744 2.744 0 1.514-1.23 2.744-2.744 2.744-1.514 0-2.744-1.23-2.744-2.744 0-1.514 1.23-2.744 2.744-2.744z" fill-rule="evenodd"></path></svg>
</a>
</div>
</div>
</footer>
</div>
</div>
</div>
</div>
</body></html>

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
        <div class="flex gap-2">
            <button class="size-8 flex items-center justify-center rounded-full bg-slate-200 dark:bg-surface-dark hover:bg-primary hover:text-white dark:hover:bg-primary dark:hover:text-white transition-colors">
                <span class="material-symbols-outlined text-sm">chevron_left</span>
            </button>
            <button class="size-8 flex items-center justify-center rounded-full bg-slate-200 dark:bg-surface-dark hover:bg-primary hover:text-white dark:hover:bg-primary dark:hover:text-white transition-colors">
                <span class="material-symbols-outlined text-sm">chevron_right</span>
            </button>
        </div>
    </div>

    <div class="flex gap-6 overflow-x-auto no-scrollbar pb-4 snap-x snap-mandatory">
        <!-- Card 1 (Hero-like) -->
        <div class="min-w-[85%] md:min-w-[600px] snap-center relative group rounded-2xl overflow-hidden shadow-lg bg-surface-dark">
            <div class="aspect-video w-full bg-cover bg-center transition-transform duration-700 group-hover:scale-105" data-alt="Stranger Things movie scene with dark atmosphere" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuB8gmG2z7Mt5ql8YqZIB9UncRckA9dVvEIypPTYJsz2Uv9uJVEmJuHGUjuplevC6kQTz3FZzFlEAaRT9aniSjkCyMNhQbqQ7Q5FYKLdRRJUi2ZN0EbI4CLDSqdZIxEQCBpQmWb_ILr-kpkgNZtKr5wSUUG3IOYiCW3mHglRN_SBbZla-bx_uf9DCYKKAiAPt5mATMcehA79Ae5rVymhTnO3jP6k088Sy1Em0RKbuTNTgAClz82PDIx-JXPQV6lEwIbjOCX3-q4uSij-");'>
                <div class="absolute inset-0 bg-gradient-to-t from-background-dark via-background-dark/50 to-transparent opacity-90"></div>
            </div>
            <div class="absolute bottom-0 left-0 w-full p-6 md:p-8">
                <div class="flex items-center gap-3 mb-2">
                    <span class="bg-[#E50914] text-white text-[10px] font-bold px-2 py-0.5 rounded tracking-wider uppercase">Netflix</span>
                    <span class="text-slate-300 text-sm font-medium">S4:E2 • 42m left</span>
                </div>
                <h3 class="text-3xl font-bold text-white mb-2 leading-tight">Stranger Things</h3>
                <p class="text-slate-300 text-sm line-clamp-2 mb-4 max-w-lg">Darkness returns to Hawkins just in time for spring break, triggering fresh terror, disturbing memories, and the threat of war.</p>
                <div class="flex items-center gap-4">
                    <button class="flex items-center gap-2 bg-primary hover:bg-primary/90 text-white px-6 py-2.5 rounded-lg font-semibold transition-all">
                        <span class="material-symbols-outlined fill text-[20px]">play_arrow</span>
                        <span>Resume</span>
                    </button>
                    <button class="flex items-center justify-center size-10 rounded-lg bg-white/10 hover:bg-white/20 backdrop-blur-sm text-white transition-colors">
                        <span class="material-symbols-outlined text-[20px]">add</span>
                    </button>
                </div>
                <!-- Progress Bar -->
                <div class="absolute bottom-0 left-0 w-full h-1 bg-white/10">
                    <div class="h-full bg-primary w-[65%] shadow-[0_0_10px_rgba(37,106,244,0.5)]"></div>
                </div>
            </div>
        </div>
        <!-- Card 2 -->
        <div class="min-w-[85%] md:min-w-[500px] snap-center relative group rounded-2xl overflow-hidden shadow-lg bg-surface-dark">
            <div class="aspect-video w-full bg-cover bg-center transition-transform duration-700 group-hover:scale-105" data-alt="Futuristic Mandalorian helmet scene" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuCI69Zh9Ozwzp9KiMas2WZXZ9W_Wbk7nDiBhhvMLvpxXOB6hNKjpwXfKzpQzLDA1y0VkQ6n9QQJqG4fFgW-fyT_g-JAPq_uPtgSGbpGYmglIQmfBKjXaFGqRa3PPuWCRseps-8w9DwZcLMr6zYZEfp6qyBons7O5-23N__vYJ6df-uJqL4OHwZh69eDt5OniUuRS3e2hOz1nC7gpu7i4mA3m90GaChk1nCtvk7aadDcgXr9efbYi6XP8LW4XzlAQEIRrhi2zb1XvqXo");'>
                <div class="absolute inset-0 bg-gradient-to-t from-background-dark via-transparent to-transparent opacity-90"></div>
            </div>
            <div class="absolute bottom-0 left-0 w-full p-6">
                <div class="flex items-center gap-3 mb-2">
                    <span class="bg-[#113CCF] text-white text-[10px] font-bold px-2 py-0.5 rounded tracking-wider uppercase">Disney+</span>
                    <span class="text-slate-300 text-sm font-medium">S3:E5 • 12m left</span>
                </div>
                <h3 class="text-2xl font-bold text-white mb-4">The Mandalorian</h3>
                <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full bg-primary w-[85%]"></div>
                </div>
            </div>
            <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity bg-black/40 backdrop-blur-[2px]">
                <button class="size-14 rounded-full bg-white/20 backdrop-blur-md flex items-center justify-center text-white hover:bg-primary hover:scale-110 transition-all">
                    <span class="material-symbols-outlined text-3xl ml-1">play_arrow</span>
                </button>
            </div>
        </div>
        <!-- Card 3 -->
        <div class="min-w-[85%] md:min-w-[500px] snap-center relative group rounded-2xl overflow-hidden shadow-lg bg-surface-dark">
            <div class="aspect-video w-full bg-cover bg-center transition-transform duration-700 group-hover:scale-105" data-alt="Dramatic scene from Succession" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuAjPYEHU1et45OP2HKulV7xIFnD3Rs_NNwEmi7XJgsI8mWfsOlmvZAof3PVFGse7oEMIC4f1M4x9V8osLb_vnTDS2laiNAaPqBuB9TvYNDNJSII7ON-LTem2LZYI5n_YksWeYsTJE5pbqJ1Ri8-0_zNcxRadvaHCyHE4prOlv-9BKtALciZ-EbHJvHVT0lWatXQV69Ynvg1vN45vmru2Rd2GCVzhHGM6uoLzqjCWjQpkiLodGkIzO-GFT1YxZ938LvpJQyIESj0b_Le");'>
                <div class="absolute inset-0 bg-gradient-to-t from-background-dark via-transparent to-transparent opacity-90"></div>
            </div>
            <div class="absolute bottom-0 left-0 w-full p-6">
                <div class="flex items-center gap-3 mb-2">
                    <span class="bg-purple-700 text-white text-[10px] font-bold px-2 py-0.5 rounded tracking-wider uppercase">HBO Max</span>
                    <span class="text-slate-300 text-sm font-medium">S2:E9 • 5m left</span>
                </div>
                <h3 class="text-2xl font-bold text-white mb-4">Succession</h3>
                <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full bg-primary w-[92%]"></div>
                </div>
            </div>
            <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity bg-black/40 backdrop-blur-[2px]">
                <button class="size-14 rounded-full bg-white/20 backdrop-blur-md flex items-center justify-center text-white hover:bg-primary hover:scale-110 transition-all">
                    <span class="material-symbols-outlined text-3xl ml-1">play_arrow</span>
                </button>
            </div>
        </div>
    </div>
</section>


<!-- Recommended For You -->
<section class="mb-12">
    <h2 class="text-xl font-bold text-slate-900 dark:text-white tracking-tight mb-6">Recommended for You</h2>
    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">
        <!-- Rec Card 1 -->
        <div class="group relative cursor-pointer">
            <div class="aspect-[2/3] rounded-xl overflow-hidden mb-3 relative shadow-md bg-surface-dark">
                <img alt="Cyberpunk city scene poster" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Movie poster showing a cyberpunk city scene" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCXcoUyMFOowo-ToYyh1hlfNn3wt3ZVkduwwVvtnrqhZwaZ6iPIORA9i0ucON6c1k3jy6IgAjnbr-Oj9LXK-lPtB5o7BV9Zx4DqD1czX9WWivLUt3xWX-f34mUfZdAqEAFEutUuczr9mYFQ02cWzf_rDtkWXKKSPm8f1c3mgws1xbJ9Y6Rte9gCSffefy01uSbCVic3xfdeuBBuFJrkXIaPF_6Jzjw0feICsgIqFHtJ4mF4QrKI1VB4sW5JVIRupygMPHgWxftWgT0s"/>
                <div class="absolute top-2 right-2">
                    <span class="bg-black/60 backdrop-blur-sm text-white text-[10px] font-bold px-1.5 py-0.5 rounded border border-white/10 uppercase">Hulu</span>
                </div>
                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
                    <div class="flex gap-2 mb-2">
                        <button class="flex-1 bg-primary text-white text-xs font-bold py-2 rounded hover:bg-primary/90">Play</button>
                        <button class="bg-white/20 text-white p-1.5 rounded hover:bg-white/30"><span class="material-symbols-outlined text-sm">add</span></button>
                    </div>
                </div>
            </div>
            <h3 class="font-semibold text-slate-900 dark:text-white text-sm truncate">Blade Runner 2049</h3>
            <div class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
                <span class="text-green-500 font-bold">98% Match</span>
                <span>•</span>
                <span>Sci-Fi</span>
            </div>
        </div>
        <!-- Rec Card 2 -->
        <div class="group relative cursor-pointer">
            <div class="aspect-[2/3] rounded-xl overflow-hidden mb-3 relative shadow-md bg-surface-dark">
                <img alt="Dramatic book cover style poster" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Book cover style poster with dark moody lighting" src="https://lh3.googleusercontent.com/aida-public/AB6AXuD-n5TtKaYDNO-1qqgU1VZbzRHGxrvF08Y7msqT5G7Iw_x28DUiSsn07bl2gHN-6e4mkOX-rXs517yV_hgQFIcxQvzuDGw3zpUXFlz-3RcVnSrlAWRHIYKDdZ9AiJMNdE2YEdHk2aaSBa3XJRRiJNDSAEr_VvqpEdaSLF3XCZkVRK03QBtWN9uBLDRNJOR-SZ6eV-s2KbOL6zSWmvOuJ4CKEDpIJvSoBOhe6XJE024Hs6uUBIGJQj75jlfnACA75kVavmy7AUEfGF2S"/>
                <div class="absolute top-2 right-2">
                    <span class="bg-black/60 backdrop-blur-sm text-white text-[10px] font-bold px-1.5 py-0.5 rounded border border-white/10 uppercase">Netflix</span>
                </div>
                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
                <div class="flex gap-2 mb-2">
                <button class="flex-1 bg-primary text-white text-xs font-bold py-2 rounded hover:bg-primary/90">Play</button>
                <button class="bg-white/20 text-white p-1.5 rounded hover:bg-white/30"><span class="material-symbols-outlined text-sm">add</span></button>
                </div>
                </div>
            </div>
            <h3 class="font-semibold text-slate-900 dark:text-white text-sm truncate">Dark</h3>
            <div class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
            <span class="text-green-500 font-bold">95% Match</span>
            <span>•</span>
            <span>Thriller</span>
            </div>
        </div>
        <!-- Rec Card 3 -->
        <div class="group relative cursor-pointer">
        <div class="aspect-[2/3] rounded-xl overflow-hidden mb-3 relative shadow-md bg-surface-dark">
        <img alt="Colorful abstract poster" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Abstract colorful poster representing animation" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCrhVD6lIvpLJRgz01KwlMvwnpyEAZD7SFgS9bKNMbcoSATPG4DJ6l_H_6aJSOMP9PwXq58boVwZPW1d5XjTYKSIcM02LcddVEot3v6CiV86TMLQITA7GBs28pZsG3lk8FLNzLH_AsThoVbh9ONxnFO3YxlVBp07SNcIV8XlJfA2cjYuvkroG4Q9i3CPy8jn8UFRV93u3jHMF8xzJcTnVsaosN2NLxkoYFCZhVUWV-DbJp9y8v3VSYLjeDEAVypdRxO8iSHvYcas-VQ"/>
        <div class="absolute top-2 right-2">
        <span class="bg-black/60 backdrop-blur-sm text-white text-[10px] font-bold px-1.5 py-0.5 rounded border border-white/10 uppercase">Disney+</span>
        </div>
        <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
        <div class="flex gap-2 mb-2">
        <button class="flex-1 bg-primary text-white text-xs font-bold py-2 rounded hover:bg-primary/90">Play</button>
        <button class="bg-white/20 text-white p-1.5 rounded hover:bg-white/30"><span class="material-symbols-outlined text-sm">add</span></button>
        </div>
        </div>
        </div>
        <h3 class="font-semibold text-slate-900 dark:text-white text-sm truncate">Spider-Man: Across the Spider-Verse</h3>
        <div class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
        <span class="text-green-500 font-bold">94% Match</span>
        <span>•</span>
        <span>Animation</span>
        </div>
        </div>
        <!-- Rec Card 4 -->
        <div class="group relative cursor-pointer">
        <div class="aspect-[2/3] rounded-xl overflow-hidden mb-3 relative shadow-md bg-surface-dark">
        <img alt="Vintage movie poster style" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Vintage style movie poster" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDMi_J2eqIkkcfGsoCjuqtdWFYX8U5BltvKa_Fi_oDoLsAfk1EjW0WlnxQ6OUCQZgXlL6CK1T5-I0bW07gc35m7LW_b7hmiI07E-CwRfGsrk5-0SXxZjO1N2pmOIKdNly0vtYfth_Gs9RIe8FstpzW7zHdl7El_C20BWvuJMoOf70SH2GbO5reqWhtb7uDBBLCCT92Zm97NAL8UHUH85jmiUSd2aJS61ErXq1LwhXlkBTue4xaFLY6Ot5GQ2MLWlrrOPqzMpDLNwaBk"/>
        <div class="absolute top-2 right-2">
        <span class="bg-black/60 backdrop-blur-sm text-white text-[10px] font-bold px-1.5 py-0.5 rounded border border-white/10 uppercase">Prime</span>
        </div>
        <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
        <div class="flex gap-2 mb-2">
        <button class="flex-1 bg-primary text-white text-xs font-bold py-2 rounded hover:bg-primary/90">Play</button>
        <button class="bg-white/20 text-white p-1.5 rounded hover:bg-white/30"><span class="material-symbols-outlined text-sm">add</span></button>
        </div>
        </div>
        </div>
        <h3 class="font-semibold text-slate-900 dark:text-white text-sm truncate">The Marvelous Mrs. Maisel</h3>
        <div class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
        <span class="text-green-500 font-bold">90% Match</span>
        <span>•</span>
        <span>Comedy</span>
        </div>
        </div>
        <!-- Rec Card 5 -->
        <div class="group relative cursor-pointer hidden xl:block">
        <div class="aspect-[2/3] rounded-xl overflow-hidden mb-3 relative shadow-md bg-surface-dark">
        <img alt="Space fantasy poster" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Fantasy space movie poster" src="https://lh3.googleusercontent.com/aida-public/AB6AXuA8dOQfA4BeHrjaO8AcVURII2bZnKCxwwJ4OlTa2m4yFOOBlm5xcBB0PWTTg3ix0PUEe-syk8eVa9emcp4q6iIx_PpFYAAZ9Ij0g3irKPuxKtHYcSD28-GlDawV3jdvfF5oDUG3D57Zg_K7Oi9KpsoZ7ePt8_eCQ6WxISZVP3_bumVbV9upj7A7mf8tL6Qa462R7JS4jasldX5RCw6lxqW69kVZ3bf0ENY1fx984GnUwlMlo60uY1N3nbhsCtijL-4zhrOanI7-fR4L"/>
        <div class="absolute top-2 right-2">
        <span class="bg-black/60 backdrop-blur-sm text-white text-[10px] font-bold px-1.5 py-0.5 rounded border border-white/10 uppercase">Apple TV+</span>
        </div>
        <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
        <div class="flex gap-2 mb-2">
        <button class="flex-1 bg-primary text-white text-xs font-bold py-2 rounded hover:bg-primary/90">Play</button>
        <button class="bg-white/20 text-white p-1.5 rounded hover:bg-white/30"><span class="material-symbols-outlined text-sm">add</span></button>
        </div>
        </div>
        </div>
        <h3 class="font-semibold text-slate-900 dark:text-white text-sm truncate">Foundation</h3>
        <div class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
        <span class="text-green-500 font-bold">88% Match</span>
        <span>•</span>
        <span>Sci-Fi</span>
        </div>
    </div>
    </div>
</section>
<!-- Trending Now (Horizontal Scroll) -->
<section class="mb-12">
<div class="flex items-center justify-between mb-6">
<h2 class="text-xl font-bold text-slate-900 dark:text-white tracking-tight">Trending Now</h2>
<a class="text-primary text-sm font-semibold hover:underline" href="#">View All</a>
</div>
<div class="flex gap-4 overflow-x-auto no-scrollbar pb-4">
<!-- Trend Card 1 -->
<div class="min-w-[200px] md:min-w-[240px] relative group cursor-pointer">
<div class="aspect-video rounded-lg overflow-hidden relative shadow-sm bg-surface-dark">
<img alt="Action movie car chase scene" class="w-full h-full object-cover transition-all duration-300 group-hover:scale-110 group-hover:brightness-50" data-alt="Action movie scene with a car chase" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAjiucoXa_4EXaEwEkLFPoXWhWCzhwNNUsFW__i4En-euL-oCC4g4gcjtbUOIH3vHTQsP4qVqZr9VPUXD2EZyhcbffUI87IwsNPxUAcR1802RTlR-uDajrGBN501MO9_E2OmjPxtA19Yvle5j3XDTzOuK6SDqasetxCYK_vqHYOAYkytUjiLRtOqGxZnU6NFuvgbXnqNDm6boe6WmswB6Lr7N0UKVKqiVyDKwYaVMXEsS5RUjcseeCd0_XApXIKapUhdbyI-VNkseK_"/>
<span class="absolute top-2 left-2 bg-primary text-white text-[10px] font-bold px-1.5 py-0.5 rounded z-10">#1</span>
<span class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity z-20">
<span class="material-symbols-outlined text-white text-4xl drop-shadow-lg">play_circle</span>
</span>
</div>
<div class="mt-2">
<h4 class="text-slate-900 dark:text-white font-medium text-sm truncate">Fast X</h4>
<p class="text-xs text-slate-500 dark:text-slate-400">Peacock • Action</p>
</div>
</div>
<!-- Trend Card 2 -->
<div class="min-w-[200px] md:min-w-[240px] relative group cursor-pointer">
<div class="aspect-video rounded-lg overflow-hidden relative shadow-sm bg-surface-dark">
<img alt="Horror movie dark hallway" class="w-full h-full object-cover transition-all duration-300 group-hover:scale-110 group-hover:brightness-50" data-alt="Spooky dark hallway scene from a horror movie" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAUPVUtBCcdKiv_sIK1XjJO-lC95zNMxnXmSV9VUJB91JITa2MGr5F2FplH1l24hh9W29RSAvTYywYNk70HG8D0Hfulq5d2UlLcsaRfWtYGmAas3LpWE51oqy4o8j3rMuE_2jIhYsQf7Nmsmo7yJLWgM6BgM-HUqy5ZqG9OM5Wp0_Q6g1WXOiufyt8V_beVMUalvtWBA2vC3jyH5ObscSj3DwltdxI_UEXXunlpZNBtQ3ZdsE758umPA0DjpQmc997Wfnk5UpRyvffw"/>
<span class="absolute top-2 left-2 bg-slate-700/80 text-white text-[10px] font-bold px-1.5 py-0.5 rounded z-10">#2</span>
<span class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity z-20">
<span class="material-symbols-outlined text-white text-4xl drop-shadow-lg">play_circle</span>
</span>
</div>
<div class="mt-2">
<h4 class="text-slate-900 dark:text-white font-medium text-sm truncate">Evil Dead Rise</h4>
<p class="text-xs text-slate-500 dark:text-slate-400">HBO Max • Horror</p>
</div>
</div>
<!-- Trend Card 3 -->
<div class="min-w-[200px] md:min-w-[240px] relative group cursor-pointer">
<div class="aspect-video rounded-lg overflow-hidden relative shadow-sm bg-surface-dark">
<img alt="Documentary nature scene" class="w-full h-full object-cover transition-all duration-300 group-hover:scale-110 group-hover:brightness-50" data-alt="Nature documentary scene with mountains" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAlEv6k67dPoKONbUbCtsKvTPasBwA6wwh8XweKzEQi2_J19qm7tJxbZQd212vlDAmoE66bXAN3A8d6DjKhA-DhRbv4JDwXlQr3HcYLr7rG-khNS4NZFNnCl-FB6dijNIOQBqkcnf6fKAaR8yHdqCJznHm_eVEJh9sQ01CocEwLkdyQBV4Je6vL5caSxkQGi_NOR0wFGpubdWhNCcw3X1dHSn2xbeERk0nj66nXGejh_9Y-6ZWaVMLsQ8M367ogE32cNQPAQa5iW3zs"/>
<span class="absolute top-2 left-2 bg-slate-700/80 text-white text-[10px] font-bold px-1.5 py-0.5 rounded z-10">#3</span>
<span class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity z-20">
<span class="material-symbols-outlined text-white text-4xl drop-shadow-lg">play_circle</span>
</span>
</div>
<div class="mt-2">
<h4 class="text-slate-900 dark:text-white font-medium text-sm truncate">Planet Earth III</h4>
<p class="text-xs text-slate-500 dark:text-slate-400">BBC • Documentary</p>
</div>
</div>
<!-- Trend Card 4 -->
<div class="min-w-[200px] md:min-w-[240px] relative group cursor-pointer">
<div class="aspect-video rounded-lg overflow-hidden relative shadow-sm bg-surface-dark">
<img alt="Comedy show stage" class="w-full h-full object-cover transition-all duration-300 group-hover:scale-110 group-hover:brightness-50" data-alt="Stage setup for a comedy special" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCOVuvOvAo1lMN2koKGmZQ-EDbqJW7_EWOW5k28ygvnO9gY4r5QETZTi5i_VY9cAXMCwdgr3gl6ReRBvuSVDQlZg0L6r3acniO8EI3E23r-P8BYkJdMv4dty96TL1GJNXqSwSO_YaNlEcG2575d-Ro0qsvQPPwP9Hj9BM3PKPOGT2t1iZeKRO1dXc2ic7Xgvo0agwW4qMOsNzBI39Sc35iWiEGKD3_XjebP1QSITXy-9URF134kAQyIUKHEslm7_wUqIh4ZywkkXvn3"/>
<span class="absolute top-2 left-2 bg-slate-700/80 text-white text-[10px] font-bold px-1.5 py-0.5 rounded z-10">#4</span>
<span class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity z-20">
<span class="material-symbols-outlined text-white text-4xl drop-shadow-lg">play_circle</span>
</span>
</div>
<div class="mt-2">
<h4 class="text-slate-900 dark:text-white font-medium text-sm truncate">John Mulaney: Baby J</h4>
<p class="text-xs text-slate-500 dark:text-slate-400">Netflix • Comedy</p>
</div>
</div>
</div>
</section>
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
        <p class="text-on-surface-variant text-xs uppercase tracking-widest font-bold mb-2">
            Search Results for
        </p>

        <h1 class="text-3xl md:text-4xl font-bold tracking-tight mb-2">
            "{{ query }}"
        </h1>

        {% if results %}
            <p class="text-on-surface-variant text-sm">
                {{ result_count }} result{{ result_count|pluralize }} found{{ result_count|pluralize }} across your connected platforms.
            </p>
        {% endif %}

    {% else %}
        <h1 class="text-3xl md:text-4xl font-bold tracking-tight mb-2">Search</h1>
        <p class="text-on-surface-variant text-sm">
            Type in the search bar to find movies and TV shows.
        </p>
    {% endif %}
</header>

<!-- ── Search bar ───────────────────────────────────────────────────────── -->
{% if not query %}
<div class="flex justify-center mb-16">
    <form action="{% url 'app:search' %}" method="GET" class="w-full max-w-lg">
        <div class="relative">
            <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-on-surface-variant text-xl">search</span>

            <input
                name="q"
                autofocus
                placeholder="Search movies, series, genres..."
                class="w-full rounded-2xl border border-outline bg-surface-container-low py-3.5 pl-12 pr-4 text-sm text-on-surface placeholder-on-surface-variant focus:outline-none focus:ring-2 focus:ring-primary/60 transition-all"
            />
        </div>
    </form>
</div>
{% endif %}

<!-- ── Results Grid ─────────────────────────────────────────────────────── -->
{% if results %}
<div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">

    {% for item in results %}
    <div class="group relative flex flex-col gap-3 transition-all duration-500 hover:scale-105 card-enter"
         style="animation-delay: {{ forloop.counter0 }}00ms">

        <div class="aspect-[2/3] rounded-xl overflow-hidden bg-surface-container relative cinematic-shadow hover-electric">

            <!-- Placeholder image -->
            <div class="w-full h-full bg-gradient-to-br from-surface-container-high to-surface-dim flex items-center justify-center">
                <span class="material-symbols-outlined text-on-surface-variant opacity-30 text-6xl">
                    {% if item.content_type == "series" %}live_tv{% else %}movie{% endif %}
                </span>
            </div>

            <!-- Gradient -->
            <div class="absolute inset-0 bg-gradient-to-t from-[#101622] via-transparent to-transparent opacity-80"></div>

            <!-- Platform badges -->
            <div class="absolute top-3 right-3 flex flex-col gap-1.5">
                {% for platform in item.platforms %}
                <span class="bg-primary text-white text-[10px] px-2 py-0.5 rounded shadow">
                    {{ platform }}
                </span>
                {% endfor %}
            </div>

            <!-- Hover overlay -->
            <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-4">
                <button class="bg-primary text-white text-xs font-bold py-2 rounded-lg tracking-wide hover:bg-primary/80 transition-colors">
                    Watch now
                </button>
            </div>

        </div>

        <!-- Info -->
        <div class="px-1">
            <h3 class="font-bold text-sm leading-tight group-hover:text-primary transition-colors truncate">
                {{ item.title }}
            </h3>

            <div class="flex items-center gap-2 mt-1">
                <span class="text-xs text-on-surface-variant">
                    {{ item.year|default:item.start_year|default:"—" }}
                </span>

                <span class="w-1 h-1 rounded-full bg-on-surface-variant/40"></span>

                <span class="text-xs text-on-surface-variant truncate">
                    {{ item.genre_name|default:"—" }}
                </span>
            </div>

            {% if item.rating %}
            <div class="flex items-center gap-1 mt-1">
                <span class="material-symbols-outlined text-amber-400 text-sm" style="font-variation-settings: 'FILL' 1;">star</span>
                <span class="text-xs text-on-surface-variant">{{ item.rating }}</span>
            </div>
            {% endif %}
        </div>

    </div>
    {% endfor %}

</div>

<!-- ── No results ───────────────────────────────────────────────────────── -->
{% elif query %}

<div class="text-center py-16">
    <div class="inline-flex items-center justify-center w-20 h-20 rounded-full bg-surface-container mb-6">
        <span class="material-symbols-outlined text-on-surface-variant text-4xl">search_off</span>
    </div>

    <h2 class="text-2xl font-bold mb-2">
        No results for "{{ query }}"
    </h2>

    <p class="text-on-surface-variant text-sm mb-2">
        Try another search term or check the spelling.
    </p>
</div>

{% if suggestions %}
<div class="mt-8">

    <div class="flex items-center gap-3 mb-6">
        <div class="h-px flex-1 bg-outline/40"></div>

        <p class="text-on-surface-variant text-xs uppercase tracking-widest font-bold px-2">
            You might like
        </p>

        <div class="h-px flex-1 bg-outline/40"></div>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-3 gap-6 max-w-2xl mx-auto">

        {% for item in suggestions %}
        <div class="group relative flex flex-col gap-3 transition-all duration-500 hover:scale-105 card-enter"
             style="animation-delay: {{ forloop.counter0 }}00ms">

            <div class="aspect-[2/3] rounded-xl overflow-hidden bg-surface-container relative cinematic-shadow hover-electric">

                <div class="w-full h-full bg-gradient-to-br from-surface-container-high to-surface-dim flex items-center justify-center">
                    <span class="material-symbols-outlined text-on-surface-variant opacity-30 text-6xl">
                        {% if item.content_type == "series" %}live_tv{% else %}movie{% endif %}
                    </span>
                </div>

                <div class="absolute inset-0 bg-gradient-to-t from-[#101622] via-transparent to-transparent opacity-80"></div>

                <!-- Platform badges -->
                <div class="absolute top-3 left-3 flex flex-col gap-1.5">
                    {% for platform in item.platforms %}
                        {% if platform == "Platform 1" %}
                            <div class="badge-p1 text-white px-2 py-0.5 rounded-sm text-[10px] font-bold uppercase shadow-lg shadow-black/50">{{ platform }}</div>
                        {% elif platform == "Platform 2" %}
                            <div class="badge-p2 text-white px-2 py-0.5 rounded-sm text-[10px] font-bold uppercase shadow-lg shadow-black/50">{{ platform }}</div>
                        {% else %}
                            <div class="badge-p3 text-white px-2 py-0.5 rounded-sm text-[10px] font-bold uppercase shadow-lg shadow-black/50">{{ platform }}</div>
                        {% endif %}
                    {% endfor %}
                </div>

                <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-4">
                    <button class="bg-primary text-white text-xs font-bold py-2 rounded-lg tracking-wide">
                        Watch now
                    </button>
                </div>

            </div>

            <div class="px-1">
                <h3 class="font-bold text-sm leading-tight group-hover:text-primary transition-colors truncate">
                    {{ item.title }}
                </h3>

                <div class="flex items-center gap-2 mt-1">
                    <span class="text-xs text-on-surface-variant">
                        {{ item.year|default:item.start_year|default:"—" }}
                    </span>

                    <span class="w-1 h-1 rounded-full bg-on-surface-variant/40"></span>

                    <span class="text-xs text-on-surface-variant truncate">
                        {{ item.genre_name|default:"—" }}
                    </span>
                </div>
            </div>

        </div>
        {% endfor %}

    </div>
</div>
{% endif %}

{% endif %}

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
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('main/', views.main, name='main'),
    path('movies/', views.movies, name='movies'),
    path('series/', views.series, name='series'),
    path('search/', views.search, name='search'),
    path('content/<int:content_id>/', views.content_detail, name='content_detail'),
]

```
<!-- END_FILE -->

---
<!-- FILE: app/views.py -->
## app/views.py

```py
from django.shortcuts import render
from .services import get_all_movies, get_all_series, search_content

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def catalog(request):
    movies = get_all_movies()
    series = get_all_series()
    return render(request, 'pages/catalog.html', {'movies': movies, 'series': series})

def series(request):
    series=get_all_series()
    return render(request, 'pages/series.html', {'series': series} )

def movies(request):
    movies = get_all_movies()
    return render(request, 'pages/movies.html', {'movies': movies})

def search(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        results = search_content(query)
        return render(request, 'pages/search.html', {
            'query' : query,
            'results' : results
        })
    
def get_content_by_id(content_id):
    movies = get_all_movies()
    series = get_all_series()
    all_content = movies + series

    for content in all_content:
        if content['id'] == content_id:
            return content
    return None
        
def show_content_detail(request, content_id):   
    content = get_content_by_id(content_id)
    if content:
        return render(request, 'pages/content_detail.html', {'content': content})
    else:
        return render(request, 'pages/content_not_found.html', status=404)



def main(request):
    return render(request, 'pages/main.html')

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
      SECRET_KEY: django-insecure-e@p&465=fx5(a#@t7q!1*-3z@3@-&1ar-v29!zr1hvn+fj$8g$
      DEBUG: False
      ALLOWED_HOSTS: localhost,127.0.0.1,0.0.0.0

    # Map port 8000 on your machine to port 8000 in the container
    # Access the app at http://localhost:8000
    ports:
      - "8000:8000"

    # Mount the current directory into /app in the container
    # This means code changes on your machine are reflected instantly (live reload)
    volumes:
      - .:/app  # "." = your project folder, "/app" = where it goes inside the container

# Named volumes (folders managed by Docker that live outside the containers)
# They keep data even if you delete and recreate the containers
volumes:
  pgdata:

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
<!-- FILE: proyecto.md -->
## proyecto.md

```md
# CodeBundle: SoftwareProject
Generated: 2026-04-02T14:00:02.743Z
Root: /home/nat/GitHub/SoftwareProject
Files: 39

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
│  │  └─ generate_qc_report.js
│  └─ workflows
│     ├─ deploy.yml
│     ├─ histogram.yml
│     ├─ pareto.yml
│     ├─ quality-control-aggregator.yml
│     ├─ runchart.yml
│     └─ test.yml
├─ .gitignore
├─ app
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ services.py
│  ├─ templates
│  │  ├─ content_card.html
│  │  ├─ home.html
│  │  └─ user_home.html
│  ├─ tests.py
│  ├─ urls.py
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

- `.dockerignore` (369 bytes)
- `.github/ISSUE_TEMPLATE/config.yml` (27 bytes)
- `.github/ISSUE_TEMPLATE/issue_template.md` (674 bytes)
- `.github/quality_control_data.json` (1434 bytes)
- `.github/scripts/generate_qc_report.js` (5936 bytes)
- `.github/workflows/deploy.yml` (874 bytes)
- `.github/workflows/histogram.yml` (943 bytes)
- `.github/workflows/pareto.yml` (986 bytes)
- `.github/workflows/quality-control-aggregator.yml` (3826 bytes)
- `.github/workflows/runchart.yml` (1258 bytes)
- `.github/workflows/test.yml` (593 bytes)
- `.gitignore` (48 bytes)
- `app/__init__.py` (0 bytes)
- `app/admin.py` (63 bytes)
- `app/apps.py` (81 bytes)
- `app/migrations/__init__.py` (0 bytes)
- `app/models.py` (57 bytes)
- `app/services.py` (398 bytes)
- `app/templates/content_card.html` (1529 bytes)
- `app/templates/home.html` (17517 bytes)
- `app/templates/user_home.html` (13513 bytes)
- `app/tests.py` (60 bytes)
- `app/urls.py` (181 bytes)
- `app/views.py` (193 bytes)
- `docker-compose.yml` (938 bytes)
- `Dockerfile` (390 bytes)
- `entrypoint.sh` (173 bytes)
- `IshikawaTools/chart.py` (4069 bytes)
- `IshikawaTools/histogram.py` (5451 bytes)
- `IshikawaTools/runchart.py` (4479 bytes)
- `manage.py` (671 bytes)
- `meeting_files/to_do_list.md` (407 bytes)
- `pyproject.toml` (285 bytes)
- `SoftwareProject/__init__.py` (0 bytes)
- `SoftwareProject/asgi.py` (407 bytes)
- `SoftwareProject/settings.py` (3260 bytes)
- `SoftwareProject/urls.py` (815 bytes)
- `SoftwareProject/wsgi.py` (407 bytes)
- `uv.lock` (67473 bytes)

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
*.sqlite3

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
media/

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

# Register your models here.

```
<!-- END_FILE -->

---
<!-- FILE: app/apps.py -->
## app/apps.py

```py
from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'

```
<!-- END_FILE -->

---
<!-- FILE: app/migrations/__init__.py -->
## app/migrations/__init__.py

```py


```
<!-- END_FILE -->

---
<!-- FILE: app/models.py -->
## app/models.py

```py
from django.db import models

# Create your models here.

```
<!-- END_FILE -->

---
<!-- FILE: app/services.py -->
## app/services.py

```py
"""
import requests

def get_local_movies():
    url = "http://127.0.0.1:8080'''" # Tu API local
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Lanza error si hay fallos (404, 500, etc.)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error conectando a la API: {e}")
        return []
        """

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/content_card.html -->
## app/templates/content_card.html

```html
<!-- Recommended Card Component -->
<div class="group relative cursor-pointer">
    <div class="aspect-[2/3] rounded-xl overflow-hidden mb-3 relative shadow-md bg-surface-dark">
      
      <!-- Imagen -->
      <img 
        src="IMAGE_URL"
        alt="poster"
        class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
      />
  
      <!-- Plataforma -->
      <div class="absolute top-2 right-2">
        <span class="bg-black/60 backdrop-blur-sm text-white text-[10px] font-bold px-1.5 py-0.5 rounded border border-white/10 uppercase">
          PLATFORM
        </span>
      </div>
  
      <!-- Hover Overlay -->
      <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
        <div class="flex gap-2 mb-2">
          <button class="flex-1 bg-primary text-white text-xs font-bold py-2 rounded hover:bg-primary/90">
            Play
          </button>
          <button class="bg-white/20 text-white p-1.5 rounded hover:bg-white/30">
            <span class="material-symbols-outlined text-sm">add</span>
          </button>
        </div>
      </div>
  
    </div>
  
    <!-- Info -->
    <h3 class="font-semibold text-slate-900 dark:text-white text-sm truncate">
      TITLE
    </h3>
  
    <div class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
      <span class="text-green-500 font-bold">MATCH%</span>
      <span>•</span>
      <span>GENRE</span>
    </div>
  </div>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/home.html -->
## app/templates/home.html

```html
<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>StreamSync - Premium Streaming Aggregator</title>
<!-- Fonts -->
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<!-- Icons -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
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
<a class="text-slate-600 dark:text-slate-400 hover:text-primary dark:hover:text-primary transition-colors text-sm font-medium" href="#">Features</a>
<a class="text-slate-600 dark:text-slate-400 hover:text-primary dark:hover:text-primary transition-colors text-sm font-medium" href="#">Pricing</a>
<a class="text-slate-600 dark:text-slate-400 hover:text-primary dark:hover:text-primary transition-colors text-sm font-medium" href="#">About Us</a>
</div>
<div class="flex gap-3">
<button class="h-10 px-5 rounded-lg text-slate-900 dark:text-white text-sm font-bold border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all">
                                    Log In
                                </button>
<button class="h-10 px-5 rounded-lg bg-primary text-white text-sm font-bold hover:bg-blue-600 shadow-lg shadow-primary/25 transition-all">
                                    Sign Up
                                </button>
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
<button class="h-12 px-8 rounded-xl bg-primary hover:bg-blue-600 text-white text-base font-bold tracking-wide shadow-xl shadow-primary/30 transition-all transform hover:scale-105">
                                        Start Free Trial
                                    </button>
<button class="glass-btn h-12 px-8 rounded-xl text-white text-base font-bold tracking-wide hover:bg-white/10 transition-all flex items-center justify-center gap-2 group/btn">
<span class="material-symbols-outlined text-xl group-hover/btn:translate-x-1 transition-transform">play_circle</span>
                                        Watch Demo
                                    </button>
</div>
</div>
<!-- Decorative blur -->
<div class="absolute -bottom-1/2 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-primary/20 rounded-full blur-[120px] -z-10 pointer-events-none"></div>
</div>
</div>
<!-- Stats Section -->
<div class="px-6 py-10 w-full">
<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
<div class="glass-card p-6 rounded-xl flex flex-col items-center justify-center text-center gap-2 hover:border-primary/30 transition-colors">
<p class="text-primary text-4xl font-bold tracking-tighter">50+</p>
<p class="text-slate-400 font-medium text-sm uppercase tracking-wider">Services Integrated</p>
</div>
<div class="glass-card p-6 rounded-xl flex flex-col items-center justify-center text-center gap-2 hover:border-primary/30 transition-colors">
<p class="text-primary text-4xl font-bold tracking-tighter">1M+</p>
<p class="text-slate-400 font-medium text-sm uppercase tracking-wider">Movies Indexed</p>
</div>
<div class="glass-card p-6 rounded-xl flex flex-col items-center justify-center text-center gap-2 hover:border-primary/30 transition-colors">
<p class="text-primary text-4xl font-bold tracking-tighter">500k+</p>
<p class="text-slate-400 font-medium text-sm uppercase tracking-wider">Active Users</p>
</div>
</div>
</div>
<!-- Features Section -->
<div class="flex flex-col gap-12 px-6 py-16 w-full">
<div class="flex flex-col md:flex-row justify-between items-end gap-6 border-b border-slate-800 pb-8">
<div class="flex flex-col gap-3 max-w-2xl">
<h3 class="text-primary font-bold text-sm tracking-widest uppercase">Premium Tools</h3>
<h2 class="text-slate-900 dark:text-white text-3xl md:text-5xl font-bold tracking-tight">
                                    Unlock your full viewing potential
                                </h2>
<p class="text-slate-600 dark:text-slate-400 text-lg">Powerful features designed to save you time and help you discover your next obsession.</p>
</div>
<button class="hidden md:flex items-center gap-2 text-primary font-bold hover:text-blue-400 transition-colors">
                                Explore all features
                                <span class="material-symbols-outlined text-sm">arrow_forward</span>
</button>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
<!-- Feature 1 -->
<div class="glass-card p-6 rounded-2xl flex flex-col gap-4 group hover:-translate-y-1 transition-transform duration-300">
<div class="size-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
<span class="material-symbols-outlined text-3xl">search</span>
</div>
<div>
<h3 class="text-slate-900 dark:text-white text-lg font-bold mb-2">Unified Search</h3>
<p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                        Stop jumping between tabs. Search across Netflix, Hulu, HBO, and Disney+ instantly from one bar.
                                    </p>
</div>
</div>
<!-- Feature 2 -->
<div class="glass-card p-6 rounded-2xl flex flex-col gap-4 group hover:-translate-y-1 transition-transform duration-300">
<div class="size-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
<span class="material-symbols-outlined text-3xl">checklist</span>
</div>
<div>
<h3 class="text-slate-900 dark:text-white text-lg font-bold mb-2">Series Tracking</h3>
<p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                        Never forget which episode you're on. Keep track of every season and episode automatically.
                                    </p>
</div>
</div>
<!-- Feature 3 -->
<div class="glass-card p-6 rounded-2xl flex flex-col gap-4 group hover:-translate-y-1 transition-transform duration-300">
<div class="size-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
<span class="material-symbols-outlined text-3xl">auto_awesome</span>
</div>
<div>
<h3 class="text-slate-900 dark:text-white text-lg font-bold mb-2">Smart Recs</h3>
<p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                        AI-driven suggestions that understand your unique taste better than any single platform algorithm.
                                    </p>
</div>
</div>
<!-- Feature 4 -->
<div class="glass-card p-6 rounded-2xl flex flex-col gap-4 group hover:-translate-y-1 transition-transform duration-300">
<div class="size-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
<span class="material-symbols-outlined text-3xl">notifications_active</span>
</div>
<div>
<h3 class="text-slate-900 dark:text-white text-lg font-bold mb-2">Availability Alerts</h3>
<p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                        Get notified the second a movie on your watchlist becomes available on your subscribed services.
                                    </p>
</div>
</div>
</div>
<button class="md:hidden w-full h-12 rounded-lg border border-slate-700 text-slate-300 font-bold hover:bg-slate-800 transition-all flex items-center justify-center gap-2">
                            Explore all features
                            <span class="material-symbols-outlined text-sm">arrow_forward</span>
</button>
</div>
<!-- CTA Section -->
<div class="w-full px-6 py-16 md:py-24">
<div class="relative w-full rounded-3xl overflow-hidden bg-slate-900 border border-slate-800 p-8 md:p-16 flex flex-col md:flex-row items-center justify-between gap-10">
<!-- Background gradient for CTA -->
<div class="absolute top-0 right-0 w-1/2 h-full bg-gradient-to-l from-primary/10 to-transparent pointer-events-none"></div>
<div class="flex flex-col gap-4 z-10 max-w-xl">
<h2 class="text-3xl md:text-4xl font-black text-white leading-tight">
                                    Ready to sync your stream?
                                </h2>
<p class="text-slate-400 text-lg">
                                    Join thousands of users simplifying their entertainment life today. Cancel anytime.
                                </p>
</div>
<div class="w-full max-w-md z-10">
<form class="flex flex-col sm:flex-row gap-3">
<input class="flex-1 h-12 rounded-lg bg-slate-800 border-slate-700 text-white placeholder:text-slate-500 focus:ring-2 focus:ring-primary focus:border-transparent px-4 outline-none transition-all" placeholder="Enter your email address" type="email"/>
<button class="h-12 px-6 rounded-lg bg-primary hover:bg-blue-600 text-white font-bold whitespace-nowrap shadow-lg shadow-primary/20 transition-all" type="submit">
                                        Get Started
                                    </button>
</form>
<p class="mt-3 text-xs text-slate-500 text-center sm:text-left">No credit card required for 14-day trial.</p>
</div>
</div>
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
<a class="text-sm text-slate-500 hover:text-primary transition-colors" href="#">Privacy Policy</a>
<a class="text-sm text-slate-500 hover:text-primary transition-colors" href="#">Terms of Service</a>
<a class="text-sm text-slate-500 hover:text-primary transition-colors" href="#">Help Center</a>
<a class="text-sm text-slate-500 hover:text-primary transition-colors" href="#">Contact</a>
</div>
<div class="flex gap-4">
<a class="text-slate-400 hover:text-white transition-colors" href="#">
<svg aria-hidden="true" class="h-5 w-5" fill="currentColor" viewbox="0 0 24 24"><path clip-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" fill-rule="evenodd"></path></svg>
</a>
<a class="text-slate-400 hover:text-white transition-colors" href="#">
<svg aria-hidden="true" class="h-5 w-5" fill="currentColor" viewbox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"></path></svg>
</a>
<a class="text-slate-400 hover:text-white transition-colors" href="#">
<svg aria-hidden="true" class="h-5 w-5" fill="currentColor" viewbox="0 0 24 24"><path clip-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 016.588 3.32c.636-.247 1.363-.416 2.427-.465C10.051 2.013 10.406 2 12.315 2zm-4.755 8.461c-1.57 0-2.841 1.272-2.841 2.841 0 1.57 1.271 2.841 2.841 2.841 1.57 0 2.841-1.271 2.841-2.841 0-1.57-1.272-2.841-2.841-2.841zm6.617-3.26c-.724 0-1.312.588-1.312 1.312 0 .724.588 1.312 1.312 1.312.724 0 1.312-.588 1.312-1.312 0-.724-.588-1.312-1.312-1.312zm-4.305 6.1c1.514 0 2.744 1.23 2.744 2.744 0 1.514-1.23 2.744-2.744 2.744-1.514 0-2.744-1.23-2.744-2.744 0-1.514 1.23-2.744 2.744-2.744z" fill-rule="evenodd"></path></svg>
</a>
</div>
</div>
</footer>
</div>
</div>
</div>
</div>
</body></html>

```
<!-- END_FILE -->

---
<!-- FILE: app/templates/user_home.html -->
## app/templates/user_home.html

```html
<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>StreamSync Dashboard</title>
<!-- Google Fonts: Spline Sans -->
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Spline+Sans:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<!-- Material Symbols -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<!-- Theme Config -->
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        "primary": "#256af4",
                        "background-light": "#f5f6f8",
                        "background-dark": "#101622",
                        "surface-dark": "#182234",
                        "surface-light": "#ffffff",
                        "border-dark": "#222f49",
                        "border-light": "#e2e8f0",
                    },
                    fontFamily: {
                        "display": ["Spline Sans", "sans-serif"]
                    },
                    borderRadius: {"DEFAULT": "0.25rem", "lg": "0.5rem", "xl": "0.75rem", "full": "9999px"},
                },
            },
        }
    </script>
<style>
        /* Hide scrollbar for horizontal scroll areas */
        .no-scrollbar::-webkit-scrollbar {
            display: none;
        }
        .no-scrollbar {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }
    </style>
</head>

<body class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100 font-display min-h-screen flex flex-col overflow-x-hidden antialiased">
<!-- Top Navigation -->
<header class="sticky top-0 z-50 w-full border-b border-solid border-border-light dark:border-border-dark bg-surface-light/80 dark:bg-background-dark/80 backdrop-blur-md px-6 py-4">
<div class="max-w-7xl mx-auto flex items-center justify-between">
<!-- Logo Section -->
<div class="flex items-center gap-3 text-primary">
<div class="size-8 rounded-lg bg-primary/20 flex items-center justify-center">
<span class="material-symbols-outlined text-primary text-2xl">play_circle</span>
</div>
<h2 class="text-slate-900 dark:text-white text-xl font-bold tracking-tight">StreamSync</h2>
</div>
<!-- Search Bar -->
<div class="hidden md:flex flex-1 max-w-xl mx-8">
<div class="relative w-full group">
<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 dark:text-slate-500">
<span class="material-symbols-outlined text-[20px]">search</span>
</div>
<input class="block w-full rounded-xl border-none bg-slate-100 dark:bg-[#1e293b] py-2.5 pl-10 pr-3 text-sm placeholder-slate-400 dark:placeholder-slate-500 text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all shadow-sm" placeholder="Search movies, shows, or platforms..." type="text"/>
<div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
<span class="text-xs text-slate-400 dark:text-slate-500 border border-slate-200 dark:border-slate-700 rounded px-1.5 py-0.5">⌘K</span>
</div>
</div>
</div>
<!-- User Actions -->
<div class="flex items-center gap-4">
<button class="relative p-2 rounded-full hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors text-slate-600 dark:text-slate-400">
<span class="material-symbols-outlined">notifications</span>
<span class="absolute top-2 right-2 size-2 bg-red-500 rounded-full border-2 border-surface-light dark:border-background-dark"></span>
</button>
<div class="h-8 w-[1px] bg-border-light dark:bg-border-dark mx-1"></div>
<button class="flex items-center gap-3 rounded-full pl-1 pr-1 py-1 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">
<div class="size-9 rounded-full bg-cover bg-center border border-slate-200 dark:border-slate-700" data-alt="User profile picture" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuDDIAQ90IxsinjXM6PKvOAaLRDc7SY_R-7MVZ7vKDplBK7950nw55ZsHlVjzpNJ8O2lOn4dzlyKwejQm-g1R1zTQ-yZAJh8gKj7DDUaFAjgMlw4f_G4wKHpDUU5KvzD1qk71kCOaHNW-DXrAhGOeBQGxvzYQeMW70BVbPqVRfxLbQuAyoV2zIfQjweJuxtG5gg4Nr-3nsr2ETbHgYaZBmzIGdzCM9pS9q1rVq1DLjeAigarT-PPxUa7ZeXqXbs6yqL6JUmGOnKS_X36");'></div>
</button>
</div>
</div>
</header>


<!-- Recommended For You -->
<section class="mb-12">
<h2 class="text-xl font-bold text-slate-900 dark:text-white tracking-tight mb-6">Catalog</h2>
<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">
<!-- Rec Card 1 -->
<div class="group relative cursor-pointer">
<div class="aspect-[2/3] rounded-xl overflow-hidden mb-3 relative shadow-md bg-surface-dark">
<img alt="Cyberpunk city scene poster" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Movie poster showing a cyberpunk city scene" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCXcoUyMFOowo-ToYyh1hlfNn3wt3ZVkduwwVvtnrqhZwaZ6iPIORA9i0ucON6c1k3jy6IgAjnbr-Oj9LXK-lPtB5o7BV9Zx4DqD1czX9WWivLUt3xWX-f34mUfZdAqEAFEutUuczr9mYFQ02cWzf_rDtkWXKKSPm8f1c3mgws1xbJ9Y6Rte9gCSffefy01uSbCVic3xfdeuBBuFJrkXIaPF_6Jzjw0feICsgIqFHtJ4mF4QrKI1VB4sW5JVIRupygMPHgWxftWgT0s"/>
<div class="absolute top-2 right-2">
<span class="bg-black/60 backdrop-blur-sm text-white text-[10px] font-bold px-1.5 py-0.5 rounded border border-white/10 uppercase">Hulu</span>
</div>
<div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
<div class="flex gap-2 mb-2">
<button class="flex-1 bg-primary text-white text-xs font-bold py-2 rounded hover:bg-primary/90">Play</button>
<button class="bg-white/20 text-white p-1.5 rounded hover:bg-white/30"><span class="material-symbols-outlined text-sm">add</span></button>
</div>
</div>
</div>
<h3 class="font-semibold text-slate-900 dark:text-white text-sm truncate">Blade Runner 2049</h3>
<div class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
<span class="text-green-500 font-bold">98% Match</span>
<span>•</span>
<span>Sci-Fi</span>
</div>
</div>
<!-- Rec Card 2 -->
<div class="group relative cursor-pointer">
<div class="aspect-[2/3] rounded-xl overflow-hidden mb-3 relative shadow-md bg-surface-dark">
<img alt="Dramatic book cover style poster" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Book cover style poster with dark moody lighting" src="https://lh3.googleusercontent.com/aida-public/AB6AXuD-n5TtKaYDNO-1qqgU1VZbzRHGxrvF08Y7msqT5G7Iw_x28DUiSsn07bl2gHN-6e4mkOX-rXs517yV_hgQFIcxQvzuDGw3zpUXFlz-3RcVnSrlAWRHIYKDdZ9AiJMNdE2YEdHk2aaSBa3XJRRiJNDSAEr_VvqpEdaSLF3XCZkVRK03QBtWN9uBLDRNJOR-SZ6eV-s2KbOL6zSWmvOuJ4CKEDpIJvSoBOhe6XJE024Hs6uUBIGJQj75jlfnACA75kVavmy7AUEfGF2S"/>
<div class="absolute top-2 right-2">
<span class="bg-black/60 backdrop-blur-sm text-white text-[10px] font-bold px-1.5 py-0.5 rounded border border-white/10 uppercase">Netflix</span>
</div>
<div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
<div class="flex gap-2 mb-2">
<button class="flex-1 bg-primary text-white text-xs font-bold py-2 rounded hover:bg-primary/90">Play</button>
<button class="bg-white/20 text-white p-1.5 rounded hover:bg-white/30"><span class="material-symbols-outlined text-sm">add</span></button>
</div>
</div>
</div>
<h3 class="font-semibold text-slate-900 dark:text-white text-sm truncate">Dark</h3>
<div class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
<span class="text-green-500 font-bold">95% Match</span>
<span>•</span>
<span>Thriller</span>
</div>
</div>
<!-- Rec Card 3 -->
<div class="group relative cursor-pointer">
<div class="aspect-[2/3] rounded-xl overflow-hidden mb-3 relative shadow-md bg-surface-dark">
<img alt="Colorful abstract poster" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Abstract colorful poster representing animation" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCrhVD6lIvpLJRgz01KwlMvwnpyEAZD7SFgS9bKNMbcoSATPG4DJ6l_H_6aJSOMP9PwXq58boVwZPW1d5XjTYKSIcM02LcddVEot3v6CiV86TMLQITA7GBs28pZsG3lk8FLNzLH_AsThoVbh9ONxnFO3YxlVBp07SNcIV8XlJfA2cjYuvkroG4Q9i3CPy8jn8UFRV93u3jHMF8xzJcTnVsaosN2NLxkoYFCZhVUWV-DbJp9y8v3VSYLjeDEAVypdRxO8iSHvYcas-VQ"/>
<div class="absolute top-2 right-2">
<span class="bg-black/60 backdrop-blur-sm text-white text-[10px] font-bold px-1.5 py-0.5 rounded border border-white/10 uppercase">Disney+</span>
</div>
<div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
<div class="flex gap-2 mb-2">
<button class="flex-1 bg-primary text-white text-xs font-bold py-2 rounded hover:bg-primary/90">Play</button>
<button class="bg-white/20 text-white p-1.5 rounded hover:bg-white/30"><span class="material-symbols-outlined text-sm">add</span></button>
</div>
</div>
</div>
<h3 class="font-semibold text-slate-900 dark:text-white text-sm truncate">Spider-Man: Across the Spider-Verse</h3>
<div class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
<span class="text-green-500 font-bold">94% Match</span>
<span>•</span>
<span>Animation</span>
</div>
</div>
<!-- Rec Card 4 -->
<div class="group relative cursor-pointer">
<div class="aspect-[2/3] rounded-xl overflow-hidden mb-3 relative shadow-md bg-surface-dark">
<img alt="Vintage movie poster style" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Vintage style movie poster" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDMi_J2eqIkkcfGsoCjuqtdWFYX8U5BltvKa_Fi_oDoLsAfk1EjW0WlnxQ6OUCQZgXlL6CK1T5-I0bW07gc35m7LW_b7hmiI07E-CwRfGsrk5-0SXxZjO1N2pmOIKdNly0vtYfth_Gs9RIe8FstpzW7zHdl7El_C20BWvuJMoOf70SH2GbO5reqWhtb7uDBBLCCT92Zm97NAL8UHUH85jmiUSd2aJS61ErXq1LwhXlkBTue4xaFLY6Ot5GQ2MLWlrrOPqzMpDLNwaBk"/>
<div class="absolute top-2 right-2">
<span class="bg-black/60 backdrop-blur-sm text-white text-[10px] font-bold px-1.5 py-0.5 rounded border border-white/10 uppercase">Prime</span>
</div>
<div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
<div class="flex gap-2 mb-2">
<button class="flex-1 bg-primary text-white text-xs font-bold py-2 rounded hover:bg-primary/90">Play</button>
<button class="bg-white/20 text-white p-1.5 rounded hover:bg-white/30"><span class="material-symbols-outlined text-sm">add</span></button>
</div>
</div>
</div>
<h3 class="font-semibold text-slate-900 dark:text-white text-sm truncate">The Marvelous Mrs. Maisel</h3>
<div class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
<span class="text-green-500 font-bold">90% Match</span>
<span>•</span>
<span>Comedy</span>
</div>
</div>
<!-- Rec Card 5 -->
<div class="group relative cursor-pointer hidden xl:block">
<div class="aspect-[2/3] rounded-xl overflow-hidden mb-3 relative shadow-md bg-surface-dark">
<img alt="Space fantasy poster" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="Fantasy space movie poster" src="https://lh3.googleusercontent.com/aida-public/AB6AXuA8dOQfA4BeHrjaO8AcVURII2bZnKCxwwJ4OlTa2m4yFOOBlm5xcBB0PWTTg3ix0PUEe-syk8eVa9emcp4q6iIx_PpFYAAZ9Ij0g3irKPuxKtHYcSD28-GlDawV3jdvfF5oDUG3D57Zg_K7Oi9KpsoZ7ePt8_eCQ6WxISZVP3_bumVbV9upj7A7mf8tL6Qa462R7JS4jasldX5RCw6lxqW69kVZ3bf0ENY1fx984GnUwlMlo60uY1N3nbhsCtijL-4zhrOanI7-fR4L"/>
<div class="absolute top-2 right-2">
<span class="bg-black/60 backdrop-blur-sm text-white text-[10px] font-bold px-1.5 py-0.5 rounded border border-white/10 uppercase">Apple TV+</span>
</div>
<div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-end p-4">
<div class="flex gap-2 mb-2">
<button class="flex-1 bg-primary text-white text-xs font-bold py-2 rounded hover:bg-primary/90">Play</button>
<button class="bg-white/20 text-white p-1.5 rounded hover:bg-white/30"><span class="material-symbols-outlined text-sm">add</span></button>
</div>
</div>
</div>
<h3 class="font-semibold text-slate-900 dark:text-white text-sm truncate">Foundation</h3>
<div class="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
<span class="text-green-500 font-bold">88% Match</span>
<span>•</span>
<span>Sci-Fi</span>
</div>
</div>
</div>
</section>


<!-- Simple Footer -->
<footer class="border-t border-border-light dark:border-border-dark mt-auto py-8">
<div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-4">
<p class="text-slate-500 dark:text-slate-400 text-sm">© 2023 StreamSync Inc. All rights reserved.</p>
<div class="flex gap-6 text-sm text-slate-500 dark:text-slate-400">
<a class="hover:text-primary" href="#">Privacy Policy</a>
<a class="hover:text-primary" href="#">Terms of Service</a>
<a class="hover:text-primary" href="#">Help Center</a>
</div>
</div>
</footer>
</body></html>

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
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.user_home, name='user_home'),
]

```
<!-- END_FILE -->

---
<!-- FILE: app/views.py -->
## app/views.py

```py
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def user_home(request):
    return render(request, 'user_home.html')

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
      SECRET_KEY: django-insecure-e@p&465=fx5(a#@t7q!1*-3z@3@-&1ar-v29!zr1hvn+fj$8g$
      DEBUG: False
      ALLOWED_HOSTS: localhost,127.0.0.1,0.0.0.0

    # Map port 8000 on your machine to port 8000 in the container
    # Access the app at http://localhost:8000
    ports:
      - "8000:8000"

    # Mount the current directory into /app in the container
    # This means code changes on your machine are reflected instantly (live reload)
    volumes:
      - .:/app  # "." = your project folder, "/app" = where it goes inside the container

# Named volumes (folders managed by Docker that live outside the containers)
# They keep data even if you delete and recreate the containers
volumes:
  pgdata:

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
version = "0.1.0"
description = "Add your description here"
requires-python = ">=3.14"
dependencies = [
    "django>=6.0.2",
    "gunicorn>=25.1.0",
    "matplotlib>=3.10.8",
    "pandas>=3.0.1",
    "python-decouple>=3.8",
    "requests>=2.32.5",
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
DEBUG = config('DEBUG', default=False, cast=bool)


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
    'app.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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
        'DIRS': [BASE_DIR / 'templates']
        ,
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

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / "staticfiles"

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

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
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
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "django" },
    { name = "gunicorn" },
    { name = "matplotlib" },
    { name = "pandas" },
    { name = "python-decouple" },
    { name = "requests" },
]

[package.metadata]
requires-dist = [
    { name = "django", specifier = ">=6.0.2" },
    { name = "gunicorn", specifier = ">=25.1.0" },
    { name = "matplotlib", specifier = ">=3.10.8" },
    { name = "pandas", specifier = ">=3.0.1" },
    { name = "python-decouple", specifier = ">=3.8" },
    { name = "requests", specifier = ">=2.32.5" },
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

```
<!-- END_FILE -->


---
## Bundle notes
- Redaction: enabled (mask: `***REDACTED***`).
- No truncations.


```
<!-- END_FILE -->

---
<!-- FILE: pyproject.toml -->
## pyproject.toml

```toml
[project]
name = "softwareproject"
version = "0.1.0"
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
    'app.apps.AppConfig',
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
        'DIRS': [BASE_DIR / 'app' / 'templates']
        ,
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

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / "staticfiles"

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

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
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
version = "0.1.0"
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

