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
TOKEN = config("HISTOGRAM_TOKEN")
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