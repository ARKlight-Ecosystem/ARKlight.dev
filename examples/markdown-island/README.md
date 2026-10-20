# markdown-island

A real, buildable ARKlight site. `../../md-theme-demo/` turns
`content/index.md` into a page with `# include <markdown.ARKlight>`
and `Site(markdown_theme=...)`. Neither exists on the ARKlight `main`
branch this repository's own site is otherwise pinned to (v0.70.1):
`arklight build md-theme-demo/site.py` fails there at preamble
resolution, and `arklight search Markdown` finds nothing. Both work
on the `alpha` branch -- confirmed with a real `arklight build` of
this project against `alpha` -- so this island now uses the real
directive directly instead of reproducing the content by hand. See
`/examples/markdown-authoring` on the main site for the fuller story.

This project's `content/index.md` uses the built-in `"reading"`
`markdown_theme` preset, the closest match to this island's old
bespoke cream/serif palette -- deliberately unrelated to `theme.py`'s
Material You crimson, so visiting it still reads as leaving the main
site entirely. `content/index.md` ends with its own Markdown link
back.

Building this project needs an `alpha`-branch ARKlight install
(`pip install -e .` from an `ARKlight` checkout on the `alpha`
branch); it fails against a `main`-branch install the same way
`md-theme-demo/` does.

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
