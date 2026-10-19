#!/usr/bin/env python3
"""Sanity checks over the manifest and content.

  python scripts/check_content.py            # structure + SEO field checks
  python scripts/check_content.py --release   # also fail on the placeholder SITE_URL
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content import CONTENT  # noqa: E402
from pages.manifest import PAGES  # noqa: E402
from site_config import PLACEHOLDER_URL, SITE_URL  # noqa: E402

errors, warnings = [], []
routes = {p["route"] for p in PAGES}

for r in routes - set(CONTENT):
    errors.append(f"manifest route has no content: {r}")
for r in set(CONTENT) - routes:
    errors.append(f"content for a route not in the manifest: {r}")

for r, c in CONTENT.items():
    d = c.get("description", "")
    t = c.get("title", "")
    if not d:
        errors.append(f"{r}: missing description")
    elif not 70 <= len(d) <= 200:
        warnings.append(f"{r}: description is {len(d)} chars (aim for 70-200)")
    if not t:
        errors.append(f"{r}: missing title")
    elif len(t) > 70:
        warnings.append(f"{r}: title is {len(t)} chars")

if "--release" in sys.argv and SITE_URL == PLACEHOLDER_URL:
    errors.append("SITE_URL is still the placeholder; set SITE_URL=https://your-domain")

for w in warnings:
    print("warn: ", w)
for e in errors:
    print("ERROR:", e)
print(f"{len(CONTENT)} pages, {len(warnings)} warnings, {len(errors)} errors")
sys.exit(1 if errors else 0)
