import requests
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

headers = {
    'X-GitHub-Api-Version': '2022-11-28',
    'Authorization': 'Bearer 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'
}

response = requests.get(
    'https://api.github.com/repos/TralaleritosTralalas/SoftwareProject/issues',
    headers=headers
)

issues = response.json()

issues_per_week = defaultdict(int)

for issue in issues:
    date = datetime.strptime(issue['created_at'], "%Y-%m-%dT%H:%M:%SZ")
    year, week, _ = date.isocalendar()
    issues_per_week[(year, week)] += 1

weeks = sorted(issues_per_week.keys())
counts = [issues_per_week[w] for w in weeks]
labels = [f"{w[0]}-W{w[1]}" for w in weeks]

plt.figure(figsize=(10,5))
plt.plot(labels, counts, marker='o')
plt.xticks(rotation=45)
plt.xlabel("Semana")
plt.ylabel("Issues abiertas")
plt.title("Issues abiertas por semana")
plt.tight_layout()

plt.show()