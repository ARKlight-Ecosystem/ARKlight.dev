#!/usr/bin/env python3
"""Post-build step: write sitemap.xml and robots.txt (and CNAME) into
the build output. ARKlight does not generate these itself.

Usage: python scripts/postbuild.py [OUTPUT_DIR]   (default: ARK)
Env:   SITE_URL (required for a meaningful sitemap), CNAME_HOST (optional)
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from pages.manifest import PAGES  # noqa: E402
from site_config import SITE_URL  # noqa: E402


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "ARK"
    if not os.path.isdir(out):
        sys.exit(f"output directory {out!r} not found; run the build first")

    urls = []
    for route in (p["route"] for p in PAGES):
        if route == "/404":
            continue
        loc = SITE_URL + ("/" if route == "/" else route)
        # No <lastmod>: stamping every URL with the build date is
        # inaccurate, and search engines learn to ignore inaccurate lastmod.
        urls.append(f"  <url><loc>{loc}</loc></url>")
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    with open(os.path.join(out, "sitemap.xml"), "w") as f:
        f.write(sitemap)

    with open(os.path.join(out, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")

    host = os.environ.get("CNAME_HOST")
    if host:
        with open(os.path.join(out, "CNAME"), "w") as f:
            f.write(host + "\n")

    print(f"wrote sitemap.xml ({len(urls)} urls), robots.txt" + (", CNAME" if host else ""))


if __name__ == "__main__":
    main()
