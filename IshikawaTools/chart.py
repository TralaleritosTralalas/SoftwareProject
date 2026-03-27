import os
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
from decouple import config

# ── Configuración ──────────────────────────────────────────────────────────────
REPO = "TralaleritosTralalas/SoftwareProject"
TOKEN = config("HISTOGRAM_TOKEN")
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