# md-theme-demo

An ARKlight site, scaffolded with `arklight new md-theme-demo --template markdown-simple`.

## Build it

```
arklight build site.py -o ARK
```

This writes `ARK/index.html`, `ARK/about.html`, `ARK/styles.css`, and
`ARK/arklight.js`, then opens `ARK/index.html` in your default browser
(pass `--no-open` to skip that).

## Next steps

- Edit the Markdown files under `content/` -- that's the whole site.
  Each one becomes a page; its route comes from its path
  (`content/guide.md` -> `/guide`, `content/index.md` -> `/`) unless
  its own front matter sets `route: /somewhere-else`.
- Front matter is optional. When present it's a `---`-delimited block
  at the top of the file setting `title`, `description`, `route`
  and/or `draft` (`true` excludes the page from the build entirely) --
  see `content/index.md`/`content/about.md` for the shape. An
  unrecognized key, or a block that opens but never closes, fails the
  build with a diagnostic naming the file and line.
- Standard Markdown is supported: headings, **bold**/*italic*, links,
  images, lists, fenced code blocks, blockquotes, tables, and `---`
  rules. A broken local link or image fails the build with the same
  diagnostic a Python-authored page would get -- never a silent dead
  link.
- Add an `assets/` folder next to `site.py` (images, fonts, favicons,
  ...) and `arklight build` copies it into the output directory
  automatically; reference them from Markdown with a relative path
  (`![logo](./logo.png)` or `![logo](assets/logo.png)`).
- Two Markdown files resolving to the same route, or a Markdown route
  that collides with a hand-written `@site.page(...)`, is a build
  error naming both sources -- never a silent "last one wins."
- Want to mix hand-written Python pages in with Markdown content?
  `arklight new <name> --template markdown-production` scaffolds a
  `components/` / `pages/` / `content/` layout that does both.
