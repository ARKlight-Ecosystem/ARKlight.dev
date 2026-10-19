# Architecture

```
pages/manifest.py ──┐
content/*.py ───────┼─> scripts/gen_site.py ─> site.py
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

Writing 15 decorators by hand would let them drift from the sitemap and the sidebar, so
`scripts/gen_site.py` writes them from the manifest. Everything else stays ordinary
imported Python.

## Rules the renderer works around

- Every imported module that uses the built-in vocabulary needs its own `# include <stdlib.ARKlight>` first line.
- `Item` accepts text only, so list items drop inline code and links.
- `Page(links=[])` is rejected; the prop is passed only when there is a canonical URL.
- `Container` can mix text and `Code`/`Link` nodes, so paragraphs with inline markup use it.
- An internal link to a route that doesn't exist halts the build, so `components/render.py`
  checks every link against `pages/manifest.py` and drops the ones that don't resolve
  (the label stays as plain text) instead of letting the compiler fail opaquely.

## Version coupling

This site targets ARKlight v0.70.1. `content/generated_reference.json` was dumped from
that version's schema. Regenerating it is a one-off Python snippet; see `docs/AUTHORING.md`.
