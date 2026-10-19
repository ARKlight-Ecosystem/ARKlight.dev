# Architecture

```
pages/manifest.py ──┐
content/*.py ───────┼─> scripts/gen_site.py ─> site.py + pages/active.py
site_config.py ─────┘                              │
                                                   v
                              components/render.py (called by every route)
                                                   │
                         arklight build site.py ───┘──> ARK/*.html
                                                   │
                         scripts/postbuild.py ─────┴──> sitemap.xml, robots.txt
```

## Why `site.py` is generated

ARKlight finds routes by reading the entry file's syntax; it never runs the file to
discover them. So each route needs a literal `@site.page("/x")` decorator **in the file
passed to `arklight build`**. Registering routes in a loop, or in an imported module, is
silently invisible and fails with `No pages registered on 'site'`.

Writing 36 decorators by hand would let them drift from the sitemap and the sidebar, so
`scripts/gen_site.py` writes them from the manifest. Everything else stays ordinary
imported Python.

## Phases are a build input

`gen_site.py 1` writes only the 15 phase-1 routes and records them in `pages/active.py`.
The renderer reads that list so that, in a phase-1 build:

- links to phase-2 pages become plain text (an unresolved internal link halts the build)
- cards for phase-2 pages are omitted
- sidebars list only pages that exist

## Rules the renderer works around

- Every imported module that uses the built-in vocabulary needs its own `# include <stdlib.ARKlight>` first line.
- `Item` accepts text only, so list items drop inline code and links.
- `Page(links=[])` is rejected; the prop is passed only when there is a canonical URL.
- `Container` can mix text and `Code`/`Link` nodes, so paragraphs with inline markup use it.

## Version coupling

This site targets ARKlight v0.70.1. `content/generated_reference.json` was dumped from
that version's schema (90 components, 8 actions, 76 derivations, 13 predicates, 3 platform
APIs, 5 behaviors). Regenerating it is a one-off Python snippet; see `docs/AUTHORING.md`.
