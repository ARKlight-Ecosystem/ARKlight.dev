"""The page manifest: the single source of truth for every route.

Everything else derives from this list: scripts/gen_site.py writes the
@site.page(...) routes into site.py, scripts/postbuild.py writes
sitemap.xml, and components/render.py builds the section sidebars.

phase 1 = the "pitstop" site (launch-quality, ~15 pages)
phase 2 = the full site (36 pages incl. 404)

Plain Python only -- no ARKlight vocabulary here.
"""

# (route, section, phase, nav label)
_ROWS = [
    ("/",                              "home",     1, "Home"),
    ("/getting-started",               "start",    1, "Getting started"),
    ("/why",                           "start",    1, "Why ARKlight"),

    ("/tutorial",                      "tutorial", 1, "Tutorial overview"),
    ("/tutorial/pages-and-routes",     "tutorial", 1, "1. Pages and routes"),
    ("/tutorial/components",           "tutorial", 2, "2. Components"),
    ("/tutorial/state",                "tutorial", 2, "3. State"),
    ("/tutorial/bindings",             "tutorial", 2, "4. Bindings"),
    ("/tutorial/actions",              "tutorial", 2, "5. Actions"),
    ("/tutorial/conditionals-and-lists", "tutorial", 2, "6. Conditionals and lists"),
    ("/tutorial/styling-and-layout",   "tutorial", 2, "7. Styling and layout"),
    ("/tutorial/build-and-pack",       "tutorial", 2, "8. Build and pack"),

    ("/docs",                          "docs",     1, "Reference overview"),
    ("/docs/components",               "docs",     1, "Components"),
    ("/docs/actions",                  "docs",     1, "Actions"),
    ("/docs/cli",                      "docs",     1, "CLI"),
    ("/docs/gotchas",                  "docs",     1, "Gotchas"),
    ("/docs/derive",                   "docs",     2, "Derive"),
    ("/docs/predicates",               "docs",     2, "Predicates"),
    ("/docs/config",                   "docs",     2, "Configuration"),
    ("/docs/experimental",             "docs",     2, "Experimental APIs"),
    ("/docs/platform-apis",            "docs",     2, "Platform APIs"),

    ("/examples",                      "examples", 1, "Examples overview"),
    ("/examples/hello-site",           "examples", 1, "Hello site"),
    ("/examples/counter",              "examples", 2, "Counter"),
    ("/examples/todo-list",            "examples", 2, "Todo list"),
    ("/examples/multi-page-docs",      "examples", 2, "Multi-page docs"),
    ("/examples/landing-page",         "examples", 2, "Landing page"),

    ("/compare/eleventy",              "compare",  2, "ARKlight vs Eleventy"),
    ("/compare/astro",                 "compare",  2, "ARKlight vs Astro"),

    ("/changelog",                     "project",  1, "Changelog"),
    ("/license",                       "project",  1, "License"),
    ("/roadmap",                       "project",  2, "Roadmap"),
    ("/blog",                          "project",  2, "Blog"),
    ("/blog/introducing-arklight",     "project",  2, "Introducing ARKlight"),

    ("/404",                           "system",   1, "Not found"),
]

PAGES = [
    {"route": r, "section": s, "phase": p, "label": l} for (r, s, p, l) in _ROWS
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
    "compare": "Compare",
    "project": "Project",
    "start": "Start here",
}


def pages_for_phase(phase):
    return [p for p in PAGES if p["phase"] <= phase]


def by_route():
    return {p["route"]: p for p in PAGES}


def siblings(section):
    return [p for p in PAGES if p["section"] == section]
