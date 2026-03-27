import os
import json
import requests
from decouple import config
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# ── Configuración ──────────────────────────────────────────────────────────────
REPO = "TralaleritosTralalas/SoftwareProject"
TOKEN = config("HISTOGRAM_TOKEN")
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