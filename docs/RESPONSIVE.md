# Responsive design notes

Mobile-first and mostly intrinsic (ARKlight's own model). All rules live in
`theme.py` (`_responsive_layer` plus edits to the component rules) and
`components/render.py` (class names / wrappers).

| Concern | Technique |
|---|---|
| Horizontal overflow | `min-width: 0` on flex/grid children (`.switcher`, `.grid`, `.sidebar`, `main`, `article`); `pre` and `.table-scroll` scroll inside their own box; inline `code` uses `overflow-wrap: anywhere` |
| Fluid type | `clamp()` with rem + vw for h1-h3 and code blocks (respects user font size) |
| Reading measure | `.prose` / `article > p, ul, ol` capped at 42rem; code, tables, card grids stay full width |
| Page frame | fluid gutters, `env(safe-area-inset-*)`, `min-height: 100dvh` |
| Header | `order` reflow: brand + toggle on row 1, nav on row 2; single row from 72rem (the only `media_query`, flagged experimental by ARKlight) |
| Section sidebar | flex-basis switch (`calc((17rem - 100%) * 999)`): chip row when it spans the page, vertical list beside the article. No breakpoint |
| Touch targets | nav, sidebar, brand and buttons are at least 2.75rem (44px) tall |
| Cards | `--ark-grid-min: min(16rem, 100%)` so a card can shrink below 16rem on tiny screens |
| Current page | `is-active` on top nav and sidebar links |

Gotchas found while building: `media_query` blocks are emitted *before*
`style_selector` rules, so base rules that share a class must use `:where()`;
`style_selector` rejects `*` selectors.

Verified in headless Chromium at 320/375/768/1280/1920px across all 14 routes
(no horizontal overflow, no tap target under 44px) and at 320px with 200% text.
