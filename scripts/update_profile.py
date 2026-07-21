from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

README_PATH = Path("README.md")
PROJECTS_START = "<!-- PROJECTS:START -->"
PROJECTS_END = "<!-- PROJECTS:END -->"
UPDATE_START = "<!-- LAST_UPDATE:START -->"
UPDATE_END = "<!-- LAST_UPDATE:END -->"
MAX_PROJECTS = 4


def api_get(url: str, token: str) -> object:
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "profile-readme-updater",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API returned HTTP {exc.code}: {details}") from exc
    except URLError as exc:
        raise RuntimeError(f"Could not connect to GitHub API: {exc.reason}") from exc


def escape_table(value: object, fallback: str = "No description provided") -> str:
    if value is None or value == "":
        return fallback
    return str(value).replace("|", r"\|").replace("\n", " ").strip()


def replace_section(text: str, start: str, end: str, content: str) -> str:
    pattern = re.compile(rf"{re.escape(start)}.*?{re.escape(end)}", re.DOTALL)
    if not pattern.search(text):
        raise RuntimeError(f"Markers {start!r} and {end!r} were not found")
    replacement = f"{start}\n{content.rstrip()}\n{end}"
    return pattern.sub(lambda _: replacement, text, count=1)


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN")
    username = os.environ.get("PROFILE_USERNAME")
    if not token or not username:
        print("GITHUB_TOKEN and PROFILE_USERNAME are required.", file=sys.stderr)
        return 1

    encoded_username = quote(username, safe="")
    repos = api_get(
        f"https://api.github.com/users/{encoded_username}/repos?per_page=100&type=owner&sort=updated",
        token,
    )
    if not isinstance(repos, list):
        print("Unexpected response from GitHub API.", file=sys.stderr)
        return 1

    usable = [
        repo for repo in repos
        if isinstance(repo, dict)
        and not repo.get("fork", False)
        and not repo.get("archived", False)
        and str(repo.get("name", "")).lower() != username.lower()
    ]
    usable.sort(
        key=lambda repo: (int(repo.get("stargazers_count", 0)), repo.get("pushed_at") or ""),
        reverse=True,
    )

    rows = ["| Project | Description | Main language |", "|---|---|---|"]
    for repo in usable[:MAX_PROJECTS]:
        name = escape_table(repo.get("name"), "repository")
        url = str(repo.get("html_url") or f"https://github.com/{username}/{name}")
        description = escape_table(repo.get("description"))
        language = escape_table(repo.get("language"), "Other")
        rows.append(f"| [**{name}**]({url}) | {description} | `{language}` |")
    if len(rows) == 2:
        rows.append("| No public projects yet | Add your first public repository | `—` |")

    readme = README_PATH.read_text(encoding="utf-8")
    readme = replace_section(readme, PROJECTS_START, PROJECTS_END, "\n".join(rows))
    updated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    readme = replace_section(readme, UPDATE_START, UPDATE_END, f"_Last project list update: {updated_at}._")
    README_PATH.write_text(readme, encoding="utf-8")
    print(f"Updated {README_PATH} with {len(rows) - 2} repositories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
