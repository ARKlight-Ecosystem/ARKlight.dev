"""Material You (Material Design 3) theme for the ARKlight site.

Plain Python (no ARKlight vocabulary), imported by `scripts/gen_site.py`
and applied to the one `Site()` instance there -- same reason
`site_config.py` stays plain Python: build scripts need to read it too.

Color roles follow the Material 3 naming convention
(`--md-<role>` / `--md-on-<role>`, see m3.material.io/styles/color/roles)
seeded from a crimson tone that matches the official ARKlight mark
(`assets/ARKlight-logo.png`) rather than Material's stock baseline
purple. Shape and elevation follow Material 3's own scale
(m3.material.io/styles/shape, .../elevation). None of this is
ARKlight's doing -- `Site()` only exposes `bg`, `font_family` and
`button_text` as constructor kwargs (see `arklight.api.Site.__init__`);
every other `--ark-*` custom property is reachable only by redeclaring
`:root` through `site.style_selector(":root", {...})`, which is what
`apply_theme()` below does, each override pointing at one of the
`--md-*` roles so there is exactly one place (ROLES) that defines what
"ARKlight's brand color" means.
"""

# Material 3 color roles, light scheme, seeded from a crimson matching
# the logo's accent rather than Material's stock baseline purple
# (#6750A4). Hand-derived following the M3 role system (surface tones
# warm-tinted toward the seed, on-* pairs meeting the system's 3:1+
# minimum contrast) rather than run through the Material Theme
# Builder -- there is no network path to Figma/Android tooling from
# this build.
ROLES = {
    "primary": "#9A2340",
    "on-primary": "#FFFFFF",
    "primary-container": "#FFD9DF",
    "on-primary-container": "#40001A",
    "secondary": "#74565C",
    "on-secondary": "#FFFFFF",
    "secondary-container": "#FFD9DF",
    "on-secondary-container": "#2B151A",
    "tertiary": "#7C5635",
    "on-tertiary": "#FFFFFF",
    "tertiary-container": "#FFDCBF",
    "on-tertiary-container": "#2E1500",
    "surface": "#FFF8F7",
    "surface-dim": "#E7D6D7",
    "surface-bright": "#FFF8F7",
    "surface-container-lowest": "#FFFFFF",
    "surface-container-low": "#FFF1EF",
    "surface-container": "#FBEAEA",
    "surface-container-high": "#F5E4E4",
    "surface-container-highest": "#EFDEDE",
    "on-surface": "#22191A",
    "on-surface-variant": "#534347",
    "outline": "#857377",
    "outline-variant": "#D8C2C5",
    "error": "#BA1A1A",
    "on-error": "#FFFFFF",
    "error-container": "#FFDAD6",
    "on-error-container": "#410002",
}

# Material 3's shape scale (m3.material.io/styles/shape/overview):
# named corner-radius steps, small components to pill-shaped ones.
SHAPE = {
    "xs": "4px",
    "sm": "8px",
    "md": "12px",
    "lg": "16px",
    "xl": "28px",
    "full": "999px",
}

# Material 3 elevation levels 1-3 (m3.material.io/styles/elevation),
# expressed as the key-light + ambient-light shadow pair the spec
# defines, rather than a single flat drop shadow.
ELEVATION = {
    1: "0 1px 2px rgba(0,0,0,.30), 0 1px 3px 1px rgba(0,0,0,.15)",
    2: "0 1px 2px rgba(0,0,0,.30), 0 2px 6px 2px rgba(0,0,0,.15)",
    3: "0 1px 3px rgba(0,0,0,.30), 0 4px 8px 3px rgba(0,0,0,.15)",
}

# Material's own type ramp leads with Roboto; Google Sans is Google
# internal/not on Google Fonts, so Roboto is the honest choice here,
# not a placeholder. `components/render.py` loads it from Google Fonts
# in <head>; this stack is the fallback chain for before that request
# resolves (or when it's blocked) down to the system default.
FONT_FAMILY = '"Roboto", "Segoe UI", system-ui, -apple-system, sans-serif'

GOOGLE_FONTS_HREF = (
    "https://fonts.googleapis.com/css2?"
    "family=Roboto:wght@400;500;700&family=Roboto+Mono:wght@400;500&display=swap"
)


def _role(name):
    return ROLES[name]


def apply_theme(site):
    """Register the Material You theme on `site`.

    Call once, right after `Site(...)` is constructed and before any
    `@site.page` registration -- order doesn't matter to ARKlight's
    route discovery (that only scans for the decorator's literal
    syntax shape), but keeping it next to the `Site()` call makes the
    theme the first thing a reader sees about this site's look.
    """
    root_vars = {f"--md-{name}": value for name, value in ROLES.items()}
    root_vars.update({f"--md-shape-{k}": v for k, v in SHAPE.items()})
    root_vars.update({f"--md-elevation-{k}": v for k, v in ELEVATION.items()})
    # Re-point ARKlight's own tokens at Material You roles, so every
    # built-in element (links, borders, the muted/accent utility
    # classes) picks up the theme with no per-component edits.
    root_vars.update({
        "--ark-text": _role("on-surface"),
        "--ark-muted": _role("on-surface-variant"),
        "--ark-accent": _role("primary"),
        "--ark-accent-hover": "#7A1C34",  # primary, one step darker
        "--ark-border": _role("outline-variant"),
    })
    site.style_selector(":root", root_vars)

    # .nav: Material's top-app-bar tabs read as pill-shaped chips, not
    # an underlined link row.
    site.style_selector(".nav", {
        "border-bottom": "none",
        "background": _role("surface-container-low"),
        "border-radius": SHAPE["full"],
        "padding": "0.5rem 0.75rem",
        "gap": "0.25rem",
    }, allow_redefine=True)
    site.style_selector(".nav a", {
        "padding": "0.5rem 1rem",
        "border-radius": SHAPE["full"],
        "transition": "background 0.15s ease, color 0.15s ease",
        "&:hover": {
            "background": _role("surface-container-high"),
            "text-decoration": "none",
        },
        "&.is-active": {
            "background": _role("secondary-container"),
            "color": _role("on-secondary-container"),
        },
    })

    # .card: a Material "filled card" -- tonal surface instead of a
    # hairline border, elevation-1 at rest, elevation-2 on hover.
    site.style_selector(".card", {
        "border": "1px solid " + _role("outline-variant"),
        "background": _role("surface-container-low"),
        "border-radius": SHAPE["lg"],
        "box-shadow": "var(--md-elevation-1)",
        "transition": "box-shadow 0.2s ease, border-color 0.2s ease",
        "&:hover": {
            "box-shadow": "var(--md-elevation-2)",
            "border-color": "transparent",
        },
    }, allow_redefine=True)

    # Filled button: Material's default button shape is the full pill,
    # not an 8px rounded rectangle.
    site.style_selector("button", {
        "border-radius": SHAPE["full"],
        "font-weight": "500",
        "padding": "0.7em 1.6em",
        "box-shadow": "var(--md-elevation-1)",
        "&:hover": {"box-shadow": "var(--md-elevation-2)"},
        "&:active": {"box-shadow": "none"},
    })

    # Code surfaces: tonal container instead of a flat border/accent
    # color, matching the rest of the "surface" family.
    site.style_selector("code", {
        "background": _role("surface-container-high"),
        "color": _role("on-surface-variant"),
        "border-radius": SHAPE["xs"],
    })
    site.style_selector("pre", {
        "background": _role("on-surface"),
        "color": _role("surface-container-lowest"),
        "border-radius": SHAPE["md"],
    })
    site.style_selector("pre code", {"background": "none", "color": "inherit"})

    # Details/dialog/fieldset/inputs: align corner radii to the shape
    # scale and borders to outline-variant instead of the plain
    # --ark-border gray.
    site.style_selector("details, dialog, fieldset", {
        "border-color": _role("outline-variant"),
        "border-radius": SHAPE["lg"],
    })
    site.style_selector("input, textarea, select", {
        "border-color": _role("outline"),
        "border-radius": SHAPE["sm"],
        "background": _role("surface-container-lowest"),
    })
    for tag in ("input", "textarea", "select"):
        site.style_selector(tag, {
            "&:focus": {"outline-color": _role("primary")},
        }, allow_redefine=True)
    site.style_selector("blockquote", {
        "border-left-color": _role("primary"),
        "background": _role("surface-container-low"),
        "border-radius": "0 " + SHAPE["sm"] + " " + SHAPE["sm"] + " 0",
        "padding": "0.6em 0 0.6em 1.25em",
    })

    # Focus ring: Material's visible-focus indicator (2px solid,
    # offset) on the two interactive elements most of this site's
    # content uses. Registered per-tag: style_selector's `&`-nesting
    # only resolves against a single base selector, not a grouped list.
    for tag in ("a", "button"):
        site.style_selector(tag, {
            "&:focus-visible": {
                "outline": f"2px solid {_role('primary')}",
                "outline-offset": "2px",
            },
        }, allow_redefine=True)
