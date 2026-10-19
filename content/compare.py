from ._util import draft

PAGES = {
    "/compare/eleventy": draft(
        "ARKlight vs Eleventy",
        "How ARKlight compares with Eleventy for building static sites: authoring language, templates, reactivity, and when to pick each.",
        "Two static-site tools with different centres of gravity.",
        [
            ("Summary table", "Authoring language, templating, client-side reactivity, ecosystem size, learning curve."),
            ("Where ARKlight fits better", "Python teams, built-in reactive state without a JS toolchain."),
            ("Where Eleventy fits better", "Content-heavy sites, Markdown pipelines, a large plugin ecosystem."),
            ("An honest verdict", "Do not overclaim. Verify every Eleventy claim against its current docs before publishing."),
        ],
        "Eleventy's own docs (must be checked at writing time; do not write from memory)",
    ),
    "/compare/astro": draft(
        "ARKlight vs Astro",
        "How ARKlight compares with Astro: component model, JavaScript shipped to the browser, authoring language, and when to pick each.",
        "Different answers to 'how much JavaScript ships?'",
        [
            ("Summary table", "Authoring language, components, shipped JS, integrations, ecosystem."),
            ("Where ARKlight fits better", "Python authors, a closed vocabulary with build-time validation."),
            ("Where Astro fits better", "Framework components, content collections, large ecosystem."),
            ("An honest verdict", "Verify every Astro claim against its current docs before publishing."),
        ],
        "Astro's own docs (must be checked at writing time; do not write from memory)",
    ),
}
