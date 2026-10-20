"""Material You (Material Design 3) theme for the ARKlight site, now
with a real dark mode.

Plain Python (no ARKlight vocabulary) except for the `ScriptExtension`
subclass at the bottom, imported by `scripts/gen_site.py` and applied
to the one `Site()` instance there -- same reason `site_config.py`
stays plain Python: build scripts need to read it too.

Color roles follow the Material 3 naming convention
(`--md-<role>` / `--md-on-<role>`, see m3.material.io/styles/color/roles)
seeded from a crimson tone that matches the official ARKlight mark
(`assets/ARKlight-logo.png`) rather than Material's stock baseline
purple. Shape and elevation follow Material 3's own scale
(m3.material.io/styles/shape, .../elevation).

Dark mode is a second seed-derived role set (`DARK_ROLES`), not an
inverted light theme -- surfaces go near-black rather than dark-grey,
`primary` lightens instead of darkening (Material's own rule for
legible color-on-dark text), and the result leans into the logo's own
black/crimson/silver palette instead of fighting it. Every rule this
file registers through `site.style_selector(...)`/`site.style(...)`
points at a `var(--md-*)`/`--ark-*` custom property rather than a
baked-in hex value (see `_var`), so swapping those sixteen-odd
properties at `html.theme-dark` is enough to re-skin the entire site --
nav, cards, buttons, code blocks, forms, focus rings -- with no
per-component dark-mode branching.
"""

from arklight.backend.script_extension import ScriptExtension

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
    # v2: the old #FFF8F7 "surface" read as plain white at a glance --
    # a warmer, slightly deeper blush-grey keeps the same light,
    # airy feel but actually reads as a designed color, not a
    # default. surface-container-lowest stays near-white so cards
    # still pop a visible step above the page behind them.
    "surface": "#F7E8E6",
    "surface-dim": "#E7D6D7",
    "surface-bright": "#F7E8E6",
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

# Dark scheme, same crimson seed, hand-derived to Material 3's own
# "dark theme" rules (surfaces go near-black and warm-tinted rather
# than neutral grey; `primary`/`secondary`/`tertiary` lighten so they
# stay legible as *text/icon* color on a dark surface, while the old
# light-scheme containers become the new dark containers). Landed on
# values close to the logo's own black-armor-plus-crimson-plus-silver
# palette rather than a generic "invert everything" dark mode.
DARK_ROLES = {
    "primary": "#FFB2C0",
    "on-primary": "#5E1130",
    "primary-container": "#7A1C34",
    "on-primary-container": "#FFD9DF",
    "secondary": "#E2BDC2",
    "on-secondary": "#412A2F",
    "secondary-container": "#5A3F44",
    "on-secondary-container": "#FFD9DF",
    "tertiary": "#EFBD92",
    "on-tertiary": "#49290A",
    "tertiary-container": "#5F3F1E",
    "on-tertiary-container": "#FFDCBF",
    "surface": "#15100F",
    "surface-dim": "#15100F",
    "surface-bright": "#3A3132",
    "surface-container-lowest": "#0F0A0A",
    "surface-container-low": "#1D1717",
    "surface-container": "#211B1B",
    "surface-container-high": "#2C2525",
    "surface-container-highest": "#372F30",
    "on-surface": "#EDE0DF",
    "on-surface-variant": "#D3C2C2",
    "outline": "#9C8C8C",
    "outline-variant": "#4E4344",
    "error": "#FFB4AB",
    "on-error": "#690005",
    "error-container": "#93000A",
    "on-error-container": "#FFDAD6",
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


def _role(name, roles=ROLES):
    return roles[name]


def _var(name):
    """A component-level rule should reference the role through its
    custom property, not its current literal value, so that a single
    `html.theme-dark` override (see `apply_theme`) re-skins every rule
    that uses it. Only the two places that actually *declare* the
    custom properties (`:root` and `html.theme-dark` themselves) use
    `_role(...)`'s literal hex instead."""
    return f"var(--md-{name})"


def _role_vars(roles):
    out = {f"--md-{name}": value for name, value in roles.items()}
    out.update({f"--md-shape-{k}": v for k, v in SHAPE.items()})
    out.update({f"--md-elevation-{k}": v for k, v in ELEVATION.items()})
    return out


def apply_theme(site):
    """Register the Material You theme -- light by default, with a
    `html.theme-dark` override -- on `site`.

    Call once, right after `Site(...)` is constructed and before any
    `@site.page` registration -- order doesn't matter to ARKlight's
    route discovery (that only scans for the decorator's literal
    syntax shape), but keeping it next to the `Site()` call makes the
    theme the first thing a reader sees about this site's look.
    """
    root_vars = _role_vars(ROLES)
    # Re-point ARKlight's own tokens at Material You roles, so every
    # built-in element (links, borders, the muted/accent utility
    # classes) picks up the theme with no per-component edits.
    root_vars.update({
        "--ark-bg": _role("surface"),
        "--ark-text": _role("on-surface"),
        "--ark-muted": _role("on-surface-variant"),
        "--ark-accent": _role("primary"),
        "--ark-accent-hover": "#7A1C34",  # primary, one step darker
        "--ark-border": _role("outline-variant"),
        "--ark-button-text": _role("on-primary"),
    })
    site.style_selector(":root", root_vars)

    # Dark scheme: redeclares the exact same custom-property set at a
    # higher-specificity selector on the same element (`:root` *is*
    # `<html>`), so it wins the cascade once `html` carries the
    # `theme-dark` class -- see `ThemeToggleScript` below for how that
    # class actually gets there. Because every rule below this point
    # reads colors through `_var(...)` rather than a literal, this one
    # block is the entire dark theme; nothing else needs a dark-mode
    # branch.
    dark_vars = _role_vars(DARK_ROLES)
    dark_vars.update({
        "--ark-bg": _role("surface", DARK_ROLES),
        "--ark-text": _role("on-surface", DARK_ROLES),
        "--ark-muted": _role("on-surface-variant", DARK_ROLES),
        "--ark-accent": _role("primary", DARK_ROLES),
        "--ark-accent-hover": "#FFD1DA",  # primary, one step lighter (hover brightens on dark)
        "--ark-border": _role("outline-variant", DARK_ROLES),
        "--ark-button-text": _role("on-primary", DARK_ROLES),
    })
    site.style_selector("html.theme-dark", dark_vars)

    # .nav: Material's top-app-bar tabs read as pill-shaped chips, not
    # an underlined link row.
    site.style_selector(".nav", {
        "border-bottom": "none",
        "background": _var("surface-container-low"),
        "border-radius": SHAPE["full"],
        "padding": "0.5rem 0.75rem",
        "gap": "0.25rem",
    }, allow_redefine=True)
    site.style_selector(".nav a", {
        "padding": "0.5rem 1rem",
        "border-radius": SHAPE["full"],
        "transition": "background 0.15s ease, color 0.15s ease",
        "&:hover": {
            "background": _var("surface-container-high"),
            "text-decoration": "none",
        },
        "&.is-active": {
            "background": _var("secondary-container"),
            "color": _var("on-secondary-container"),
        },
    })

    # .card: a Material "filled card" -- tonal surface instead of a
    # hairline border, elevation-1 at rest, elevation-2 on hover.
    site.style_selector(".card", {
        "border": "1px solid " + _var("outline-variant"),
        "background": _var("surface-container-low"),
        "border-radius": SHAPE["lg"],
        "box-shadow": "var(--md-elevation-1)",
        "transition": "box-shadow 0.2s ease, border-color 0.2s ease, background 0.2s ease",
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
        "transition": "box-shadow 0.15s ease, background 0.15s ease",
        "&:hover": {"box-shadow": "var(--md-elevation-2)"},
        "&:active": {"box-shadow": "none"},
    })

    # Code surfaces: tonal container instead of a flat border/accent
    # color, matching the rest of the "surface" family.
    site.style_selector("code", {
        "background": _var("surface-container-high"),
        "color": _var("on-surface-variant"),
        "border-radius": SHAPE["xs"],
    })
    site.style_selector("pre", {
        "background": _var("on-surface"),
        "color": _var("surface-container-lowest"),
        "border-radius": SHAPE["md"],
    })
    site.style_selector("pre code", {"background": "none", "color": "inherit"})

    # Details/dialog/fieldset/inputs: align corner radii to the shape
    # scale and borders to outline-variant instead of the plain
    # --ark-border gray.
    site.style_selector("details, dialog, fieldset", {
        "border-color": _var("outline-variant"),
        "border-radius": SHAPE["lg"],
    })
    site.style_selector("input, textarea, select", {
        "border-color": _var("outline"),
        "border-radius": SHAPE["sm"],
        "background": _var("surface-container-lowest"),
        "color": _var("on-surface"),
    })
    for tag in ("input", "textarea", "select"):
        site.style_selector(tag, {
            "&:focus": {"outline-color": _var("primary")},
        }, allow_redefine=True)
    site.style_selector("blockquote", {
        "border-left-color": _var("primary"),
        "background": _var("surface-container-low"),
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
                "outline": f"2px solid {_var('primary')}",
                "outline-offset": "2px",
            },
        }, allow_redefine=True)

    # ------------------------------------------------------------------
    # Header: logo mark + wordmark on the left, section nav in the
    # middle, theme toggle on the right -- a real top app bar instead
    # of a bare row of links floating on the page background.
    # ------------------------------------------------------------------
    site.style_selector(".site-header", {
        "justify-content": "space-between",
        "padding": "0.85rem 1.25rem",
        "margin": "-0.5rem -1.25rem 2rem",
        "background": _var("surface-container-low"),
        "border-radius": SHAPE["lg"],
        "border": "1px solid " + _var("outline-variant"),
    })
    site.style_selector(".site-header .nav", {
        "margin": "0",
        "padding": "0.35rem 0.5rem",
    }, allow_redefine=True)
    site.style_selector(".brand", {
        "display": "flex",
        "align-items": "center",
        "gap": "0.6rem",
    })
    site.style_selector(".brand-mark", {
        "width": "2.25rem",
        "height": "2.25rem",
        "border-radius": SHAPE["full"],
        "box-shadow": "var(--md-elevation-1)",
        "margin": "0",
    })
    site.style_selector(".brand-name", {
        "font-weight": "700",
        "font-size": "1.1rem",
        "color": _var("on-surface"),
    })
    site.style_selector(".brand-name:hover", {
        "color": _var("primary"),
        "text-decoration": "none",
    })

    # Theme toggle: an outlined pill, not a filled accent button, so
    # it reads as a utility control rather than the page's primary
    # call to action.
    site.style_selector(".theme-toggle", {
        "background": "transparent",
        "color": _var("on-surface"),
        "border": "1px solid " + _var("outline"),
        "box-shadow": "none",
        "padding": "0.5em 1.1em",
        "font-size": "0.9rem",
        "&:hover": {
            "background": _var("surface-container-high"),
            "box-shadow": "none",
        },
    }, allow_redefine=True)

    # ------------------------------------------------------------------
    # Hero: the one section most people see first. A flat card on the
    # page background reads as filler; a tonal gradient panel reads as
    # designed, and doubles as the clearest place to show the theme
    # actually changed when toggled.
    # ------------------------------------------------------------------
    site.style_selector(".hero", {
        "background": (
            f"linear-gradient(135deg, {_var('primary-container')} 0%, "
            f"{_var('surface-container-low')} 65%)"
        ),
        "border": "1px solid " + _var("outline-variant"),
        "border-radius": SHAPE["xl"],
        "padding": "clamp(1.75rem, 4vw, 3rem)",
        "margin-bottom": "2rem",
        "box-shadow": "var(--md-elevation-1)",
    })
    site.style_selector(".hero h1", {
        "color": _var("on-primary-container"),
    })
    site.style_selector(".hero pre", {
        "margin-bottom": "0",
    })

    # Footer: a quieter tonal strip, not plain body background,
    # consistent with the header treatment.
    site.style_selector("footer", {
        "margin-top": "3rem",
        "padding": "1.5rem 1.25rem",
        "background": _var("surface-container-low"),
        "border-radius": SHAPE["lg"],
        "border": "1px solid " + _var("outline-variant"),
    })
    site.style_selector("footer .nav", {
        "background": "transparent",
        "padding": "0",
        "border-radius": "0",
    }, allow_redefine=True)

    site.register_script_extension(ThemeToggleScript)


# ----------------------------------------------------------------------
# Dark-mode persistence. `toggle`, ARKlight's built-in click behavior
# (arklight/backend/js/behaviors/toggle.py), flips a class on an
# element but has no notion of *remembering* that choice across visits
# or of the OS-level `prefers-color-scheme` -- neither is expressible
# in the closed component/behavior vocabulary, so this is the
# `script-extension` escape hatch (see arklight/experimental.py,
# "script-extension"), used for exactly the gap it exists for: a few
# lines of hand-written JS, nothing structural.
# ----------------------------------------------------------------------

#include <expapilib.ARKlight>
class ThemeToggleScript(ScriptExtension):
    """Applies the visitor's last-chosen theme (or their OS
    preference, the first time) by toggling `.theme-dark` on
    `<html>`, and wires the `#theme-toggle` button to flip and
    remember that choice. `arklight.js` is loaded with `defer` (see
    arklight/backend/html/page_render.py) and ARKlight's CSP forbids
    inline `<script>` entirely (arklight/backend/html/csp.py), so this
    runs as soon as the deferred script executes -- after parsing, not
    before paint. In practice this only matters for a visitor who has
    explicitly chosen a theme that differs from their OS preference;
    everyone else never sees a flash because the CSS default already
    matches `prefers-color-scheme` the first time `apply()` runs.
    """

    script = """
    <script>
      (function () {
        var KEY = "ark-theme";
        var root = document.documentElement;

        function apply(theme) {
          root.classList.toggle("theme-dark", theme === "dark");
        }

        function storedTheme() {
          try {
            return localStorage.getItem(KEY);
          } catch (err) {
            return null;
          }
        }

        function preferredTheme() {
          var saved = storedTheme();
          if (saved === "dark" || saved === "light") return saved;
          return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
            ? "dark"
            : "light";
        }

        apply(preferredTheme());

        document.addEventListener("DOMContentLoaded", function () {
          var btn = document.getElementById("theme-toggle");
          if (!btn) return;

          function sync() {
            var dark = root.classList.contains("theme-dark");
            btn.setAttribute("aria-pressed", dark ? "true" : "false");
            btn.textContent = dark ? "Light mode" : "Dark mode";
          }

          btn.addEventListener("click", function () {
            var next = root.classList.contains("theme-dark") ? "light" : "dark";
            apply(next);
            try {
              localStorage.setItem(KEY, next);
            } catch (err) {
              /* private-browsing / storage disabled: theme still
                 applies for this page view, just doesn't persist. */
            }
            sync();
          });

          sync();
        });
      })();
    </script>
    """
