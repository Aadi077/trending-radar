"""Daily snapshot of the fastest-rising new GitHub repositories.

Queries the GitHub search API for repos created in the last 7 days,
ranked by stars, and writes a dated JSON + Markdown snapshot plus an
updated README.
"""

import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKEN = os.environ.get("GITHUB_TOKEN")
CATEGORIES = {
    "All languages": None,
    "Python": "Python",
    "TypeScript": "TypeScript",
    "Rust": "Rust",
    "Go": "Go",
}
TOP_N = 10


def search(language, since):
    q = f"created:>={since}"
    if language:
        q += f" language:{language}"
    params = urllib.parse.urlencode({"q": q, "sort": "stars", "order": "desc", "per_page": TOP_N})
    req = urllib.request.Request(f"https://api.github.com/search/repositories?{params}")
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        items = json.load(resp)["items"]
    return [
        {
            "name": r["full_name"],
            "url": r["html_url"],
            "description": (r["description"] or "").strip(),
            "language": r["language"],
            "stars": r["stargazers_count"],
            "created_at": r["created_at"],
        }
        for r in items
    ]


def md_table(repos):
    lines = ["| # | Repo | ⭐ | Description |", "|---|---|---|---|"]
    for i, r in enumerate(repos, 1):
        desc = r["description"].replace("|", "\\|").replace("\n", " ")
        if len(desc) > 100:
            desc = desc[:97] + "..."
        lines.append(f"| {i} | [{r['name']}]({r['url']}) | {r['stars']:,} | {desc} |")
    return "\n".join(lines)


def main():
    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")
    since = (now - timedelta(days=7)).strftime("%Y-%m-%d")

    snapshot = {"date": today, "window_start": since, "categories": {}}
    for label, lang in CATEGORIES.items():
        snapshot["categories"][label] = search(lang, since)

    out_dir = ROOT / "data" / now.strftime("%Y") / now.strftime("%m")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{today}.json").write_text(json.dumps(snapshot, indent=2) + "\n")

    body = "\n\n".join(f"### {label}\n\n{md_table(repos)}" for label, repos in snapshot["categories"].items())
    (out_dir / f"{today}.md").write_text(f"# Rising repos — {today}\n\nNew repos created since {since}, ranked by stars.\n\n{body}\n")

    days = sorted((ROOT / "data").rglob("*.json"))
    readme = (
        "# 📈 Trending Radar\n\n"
        "A daily archive of the fastest-rising **new** GitHub repositories "
        "(created in the last 7 days, ranked by stars), collected automatically by GitHub Actions.\n\n"
        f"**Last updated:** {today} · **Days archived:** {len(days)}\n\n"
        f"## Today's top new repos\n\n{md_table(snapshot['categories']['All languages'])}\n\n"
        f"More languages: [`data/{now:%Y/%m}/{today}.md`](data/{now:%Y/%m}/{today}.md)\n\n"
        "## How it works\n\n"
        "- [`scripts/snapshot.py`](scripts/snapshot.py) queries the GitHub search API (stdlib only, no dependencies).\n"
        "- [`.github/workflows/daily.yml`](.github/workflows/daily.yml) runs it every day and commits the results.\n"
        "- Raw JSON snapshots live in [`data/`](data) for anyone who wants to analyze trends over time.\n"
    )
    (ROOT / "README.md").write_text(readme)
    print(f"Wrote snapshot for {today} ({len(days)} days archived)")


if __name__ == "__main__":
    main()
