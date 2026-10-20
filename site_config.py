"""Site-wide settings. Plain Python (no ARKlight vocabulary), so the
build scripts can import it too.

SITE_URL has no real default on purpose: the production domain is the
owner's call. Canonical tags and sitemap.xml need an absolute URL, so
`make release` refuses to run while this is still the placeholder.
"""
import os

PLACEHOLDER_URL = "https://CHANGE-ME.example"
SITE_URL = os.environ.get("SITE_URL", PLACEHOLDER_URL).rstrip("/")
SITE_NAME = "ARKlight"
TAGLINE = "Build websites with Python. Ship plain HTML."
REPO_URL = "https://github.com/ARKlight-Ecosystem/ARKlight"
PYPI_URL = "https://pypi.org/project/arklight/"
ARKLIGHT_VERSION = "0.70.1"  # the compiler version this site was written against
OG_IMAGE = "/assets/og-image.png"  # 1200x630; the official ARKlight mark, see docs/SEO.md
FAVICON = "/assets/favicon.png"  # the official ARKlight mark, see docs/SEO.md
APPLE_TOUCH_ICON = "/assets/apple-touch-icon.png"  # 180x180, same mark
