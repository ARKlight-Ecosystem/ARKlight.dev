---
title: Markdown, themed (the real build)
description: md-theme-demo/content/index.md, built for real with # include <markdown.ARKlight> and Site(markdown_theme="reading") on the alpha compiler.
---

# Markdown, themed

This whole page is **one file**: `content/index.md`. No
`@site.page(...)`, no `Page(...)` tree -- just
`# include <markdown.ARKlight>` in `site.py` and a markdown file next
to it. ARKlight's own markdown parser turns this into the tree below,
and the classed `ark-md-*` styling renders it without a line of CSS
written for this project.

## What it can hold

A paragraph can carry *italic*, **bold**, and `inline code`, plus a
[link back to the ARKlight repository](https://github.com/ARKlight-Ecosystem/ARKlight).

### A short list

- Headings become `ark-md-h1` through `ark-md-h6`, each with a slugged `id`.
- Paragraphs are `ark-md-p`.
- This bullet list is `ark-md-list` / `ark-md-item` -- the same markdown parser `md-theme-demo/` uses.

### A numbered list

1. Fenced code blocks become `ark-md-pre` / `ark-md-code-block`.
2. Blockquotes become `ark-md-blockquote`.
3. The table further down becomes `ark-md-table`.

### A code block

```python
# include <stdlib.ARKlight>
# include <markdown.ARKlight>

site = Site(markdown_theme="reading")
```

### A blockquote

> Markdown-as-content is opt-in, and it is not a second syntax for
> `Page(...)` -- a page that needs `State`, `Bind`, or a custom
> component still goes through a `@site.page(...)`-decorated function.

### A table

| Preset | `Site(markdown_theme=...)` |
| --- | --- |
| Light | `"light"` |
| Dark | `"dark"` |
| Reading | `"reading"` |

---

This island is built from `examples/markdown-island/`, on its own,
with its own `Site(...)` and the `reading` markdown theme -- then
nested into the main build's output directory (see the Makefile).
It no longer reproduces `md-theme-demo/content/index.md` by hand:
on the `alpha` branch (unlike the `main` branch this repository was
previously pinned to), `# include <markdown.ARKlight>` and
`Site(markdown_theme=...)` build correctly, so this page is that
real directive, not a stand-in for it.

[← Back to arklight-dev](https://arklight.arklight-compiler.workers.dev/examples/markdown-authoring)
