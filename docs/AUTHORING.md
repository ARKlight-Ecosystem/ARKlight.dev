# Authoring

## Add or finish a page

1. The route must be in `pages/manifest.py` (route, section, phase, nav label).
2. Add or edit its dict in the matching `content/*.py` module.
3. Run `make dev2` (or `dev1`) and open it with `make serve`.
4. When the text is real, **remove `draft=True`** (or stop using the `draft(...)` helper).
5. `make status` to refresh `docs/CONTENT-STATUS.md`.

## A page dict

```python
{
    "title": "Components",                 # becomes <title> and the h1
    "description": "70-200 chars...",      # meta description + og:description
    "lead": "One muted sentence under the h1.",
    "blocks": [ ... ],
}
```

`scripts/check_content.py` warns when a description is outside 70-200 characters.

## Blocks

| Block | Renders |
|---|---|
| `("h2", text)`, `("h3", text)` | headings |
| `("p", text)` | paragraph; supports `` `code` `` and `[label](/route)` |
| `("code", source)` | code block |
| `("list", [text, ...])` | bullet list (plain text only: `Item` accepts text children only) |
| `("note", text)` | bordered card |
| `("table", [headers], [[cells]...])` | table (plain text cells) |
| `("cards", [(title, text, href), ...])` | grid of cards |

## Rules that will bite you

- **Internal links must point at a built route.** In a phase-1 build, links to phase-2
  pages are dropped automatically (the label stays as text). Typos fail the build.
- **Verify every claim about ARKlight** with `arklight search <Name>` or the compiler source.
  Reference tables here were checked that way; several first guesses were wrong
  (for example `Action.remove` is index-based).
- Don't write comparison pages from memory. Check the other tool's current docs.

## Regenerating the reference data

```python
import json
from arklight.ir import schema
from arklight import api
data = {
    "components": sorted(schema.SCHEMA),
    "actions": sorted(m for m in dir(api.Action) if not m.startswith("_")),
    "derive": sorted(m for m in dir(api.Derive) if not m.startswith("_")),
    "predicates": sorted(m for m in dir(api.Predicate) if not m.startswith("_")),
    "platform_apis": sorted(m for m in dir(api.PlatformAPI) if not m.startswith("_")),
    "behaviors": sorted(schema.KNOWN_BEHAVIORS),
    "arklight_version": "0.70.1",   # update
}
json.dump(data, open("content/generated_reference.json", "w"), indent=1)
```
