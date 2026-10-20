# markdown-island

A real, buildable ARKlight site. `../../md-theme-demo/` describes
itself as turning `content/index.md` into a page with
`# include <markdown.ARKlight>` and `Site(markdown_theme=...)`.
Neither exists in the ARKlight version this repository is pinned to
(v0.70.1): `arklight build md-theme-demo/site.py` fails at preamble
resolution, and `arklight search Markdown` finds nothing. See
`/examples/markdown-authoring` on the main site for the full story,
checked against a real build rather than assumed.

This project reproduces the same content by hand, as an actual
`Page(...)` tree, with its own palette -- deliberately unrelated to
`theme.py`'s Material You crimson -- so visiting it reads as leaving
the main site entirely. A `Link` at the bottom goes back.

## Build it on its own

```
ARKLIGHT_ACCEPT_LICENSE=1 arklight build site.py -o ARK
```

## Build it as part of the main site

`make build` (in the repository root) builds this project too, via
the `island` target, and nests its output under the main build's own
output directory at `ARK/examples/markdown-authoring/live/` -- its own
`index.html`, `styles.css` and `arklight.js`, never mixed with the
main site's. `/examples/markdown-authoring` links to it with an
absolute URL (`site_config.SITE_URL` + the nested path), since it
isn't a route `pages/manifest.py` registers and a root-relative link
to it would fail this site's own internal-link check.
