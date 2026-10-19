"""The page manifest: the single source of truth for every route.

Everything else derives from this list: scripts/gen_site.py writes the
@site.page(...) routes into site.py, scripts/postbuild.py writes
sitemap.xml, and components/render.py builds the section sidebars.

Plain Python only -- no ARKlight vocabulary here.
"""

# (route, section, nav label)
_ROWS = [
    ("/",                              "home",     "Home"),
    ("/getting-started",               "start",    "Getting started"),
    ("/why",                           "start",    "Why ARKlight"),

    ("/tutorial",                      "tutorial", "Tutorial overview"),
    ("/tutorial/pages-and-routes",     "tutorial", "1. Pages and routes"),

    ("/docs",                          "docs",     "Reference overview"),
    ("/docs/components",               "docs",     "Components"),
    ("/docs/actions",                  "docs",     "Actions"),
    ("/docs/cli",                      "docs",     "CLI"),
    ("/docs/gotchas",                  "docs",     "Gotchas"),

    ("/examples",                      "examples", "Examples overview"),
    ("/examples/hello-site",           "examples", "Hello site"),

    ("/changelog",                     "project",  "Changelog"),
    ("/license",                       "project",  "License"),

    ("/404",                           "system",   "Not found"),
]

PAGES = [
    {"route": r, "section": s, "label": l} for (r, s, l) in _ROWS
]

# Top-bar navigation (section landing pages).
TOP_NAV = [
    ("Getting started", "/getting-started"),
    ("Tutorial", "/tutorial"),
    ("Reference", "/docs"),
    ("Examples", "/examples"),
    ("Why", "/why"),
    ("Changelog", "/changelog"),
]

SECTION_TITLES = {
    "tutorial": "Tutorial",
    "docs": "Reference",
    "examples": "Examples",
    "project": "Project",
    "start": "Start here",
}


def by_route():
    return {p["route"]: p for p in PAGES}


def siblings(section):
    return [p for p in PAGES if p["section"] == section]
