# Authoring

## Add or edit a page

1. The route must be in `pages/manifest.py` (route, section, nav label).
2. Add or edit its dict in the matching `content/*.py` module.
3. `make build` to generate `site.py` and build it, then `make serve` to look at it.
4. `make check` to catch a missing field or a route/content mismatch before you build.

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

- **Internal links must point at a route in `pages/manifest.py`.** A typo is dropped
  silently to plain text rather than failing the build; `make check` won't catch it, so
  proofread links by eye.
- **Verify every claim about ARKlight** with `arklight search <Name>` or the compiler source.
  Reference tables here were checked that way; several first guesses were wrong
  (for example `Action.remove` is index-based).

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
