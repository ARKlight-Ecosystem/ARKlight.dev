---
title: Markdown, themed
description: One markdown-authored ARKlight page, built twice to compare the light and dark markdown_theme presets.
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
- This bullet list is `ark-md-list` / `ark-md-item`.

### A numbered list

1. Fenced code blocks become `ark-md-pre` / `ark-md-code-block`.
2. Blockquotes become `ark-md-blockquote`.
3. A pipe table becomes `ark-md-table`.

### A code block

```python
# include <stdlib.ARKlight>
# include <markdown.ARKlight>

site = Site(markdown_theme="dark")
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

That rule above is `ark-md-hr`. This page was built twice from the
same markdown file and the same `site.py` -- only the `markdown_theme`
value changed between builds.
