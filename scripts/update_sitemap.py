#!/usr/bin/env python3
"""
Updates <lastmod> dates in sitemap.xml for any .html files that changed
in the current push. Run from the repo root.

Usage: python3 scripts/update_sitemap.py file1.html file2.html ...
"""
import sys
import re
from datetime import datetime, timezone

SITE_BASE = "https://nebraska-rare.org"
SITEMAP_PATH = "sitemap.xml"


def html_path_to_loc(path: str) -> str:
    """Map a repo-relative html file path to its sitemap <loc> URL."""
    path = path.strip().lstrip("./")
    if path == "index.html":
        return f"{SITE_BASE}/"
    return f"{SITE_BASE}/{path}"


def main():
    changed_files = [f for f in sys.argv[1:] if f.endswith(".html")]
    if not changed_files:
        print("No changed .html files passed in. Nothing to do.")
        return

    with open(SITEMAP_PATH, "r", encoding="utf-8") as f:
        sitemap = f.read()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    updated_locs = []

    for html_file in changed_files:
        loc = html_path_to_loc(html_file)
        # Match the <url>...</url> block containing this exact <loc>, and
        # bump the <lastmod> inside that same block only.
        pattern = re.compile(
            r"(<url>\s*<loc>"
            + re.escape(loc)
            + r"</loc>\s*<lastmod>)\d{4}-\d{2}-\d{2}(</lastmod>)"
        )
        new_sitemap, count = pattern.subn(rf"\g<1>{today}\g<2>", sitemap)
        if count:
            sitemap = new_sitemap
            updated_locs.append(loc)
        else:
            print(f"No matching <url> entry found in sitemap.xml for: {loc} (skipped)")

    if updated_locs:
        with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
            f.write(sitemap)
        print("Updated lastmod for:")
        for loc in updated_locs:
            print(f"  - {loc} -> {today}")
    else:
        print("No sitemap entries matched changed files. Nothing to update.")


if __name__ == "__main__":
    main()