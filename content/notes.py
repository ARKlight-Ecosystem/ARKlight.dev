"""Five more short essays, in the same spirit as content/concepts.py:
not a port of anything in reference/svelte-v2.16.1/ (that checkout has
no site of its own -- see docs/SVELTE-REFERENCE.md), but organized
around five more concerns a compiler-era project like that one faces,
looked at from ARKlight's side only. Where concepts.py covers parsing,
compilation, rendering and state, this module covers styling,
preprocessing, debugging, distribution and build tooling.
"""

_NAV = [
    ("Styling model", "No component-scoped stylesheet pass, because no component boundary survives into the output.", "/docs/notes/styling-model"),
    ("Preprocessing", "No pipeline stage for a second authoring language, because the entry file is already plain Python.", "/docs/notes/preprocessing"),
    ("Sourcemaps and debugging", "Nothing transformed to map back to, so --debug prints a real Python traceback instead.", "/docs/notes/sourcemaps-and-debugging"),
    ("Custom elements", "No compile target for exporting a component as a reusable element outside its own build.", "/docs/notes/custom-elements"),
    ("Build tooling", "One CLI invocation instead of a bundler configuration, with sbom.txt standing in for build stats.", "/docs/notes/build-tooling"),
]


def _series_cards(current):
    return [(t, d, h) for (t, d, h) in _NAV if h != current]


PAGES = {
    "/docs/notes/styling-model": {
        "title": "Styling model",
        "description": "Why ARKlight has no component-scoped CSS compiler pass, and leans on site-wide styling and a closed set of layout utility classes instead.",
        "lead": "Five more short essays, part 1 of 5.",
        "blocks": [
            ("p", "Svelte's compiler gives every component its own scoped stylesheet: a `<style>` block in a `.svelte` file is rewritten with a generated attribute selector so its rules can't leak into another component. `reference/svelte-v2.16.1/test/css` is full of fixtures pinning down exactly how that rewriting behaves."),
            ("p", "ARKlight has no per-component stylesheet to scope in the first place, because an `@component` compiles away rather than surviving into the output -- by the time a build finishes there's no component boundary left for a selector to leak across. Site-wide styling instead goes through `Site.style(...)` / `Site.style_selector(...)`, plus the built-in `.stack`/`.cluster`/`.switcher`/`.grid`/`.sidebar` utility classes from [styling and layout](/tutorial/styling-and-layout)."),
            ("note", "This site's own `theme.py` is the concrete example: one Material You palette applied with `site.style_selector(...)` calls, not a stylesheet attached to any one page or component."),
            ("h2", "What this trades away"),
            ("list", [
                "No per-component CSS-Modules-style isolation -- a class name collision is a real possibility the utility classes and `style_selector` specificity have to avoid by convention, not by a compiler-generated attribute.",
                "No component-local `<style>` block at all: `@component` props configure markup and behavior, never styling rules of their own.",
                "Anything keyed to viewport size still has to go through the gated `css-media-queries` experimental feature, the same as everywhere else in ARKlight -- see [experimental APIs](/docs/experimental).",
            ]),
            ("p", "The payoff: one generated stylesheet per build, with no risk of a scoping attribute mismatch between a server-rendered and a hydrated tree -- the same absence of a hydration step covered in [rendering model](/docs/concepts/rendering-model)."),
            ("cards", _series_cards("/docs/notes/styling-model")),
        ],
    },
    "/docs/notes/preprocessing": {
        "title": "Preprocessing",
        "description": "Why ARKlight has no preprocess hook for TypeScript, SCSS or any other input language, and what a one-stage compiler trades away by skipping it.",
        "lead": "Five more short essays, part 2 of 5.",
        "blocks": [
            ("p", "`reference/svelte-v2.16.1/src/preprocess` is a dedicated pipeline stage: a `.svelte` file can be rewritten by one or more preprocessors -- TypeScript, SCSS, PostCSS, and the like -- before the real compiler ever sees it, each registered as a plugin a project configures in its own build tool."),
            ("p", "ARKlight has nothing in this position. [Compilation](/docs/concepts/compilation) already covers the one-pass build; the preprocessing-specific point is narrower -- there's no earlier stage where a second language could be rewritten into Python, because the entry file is already plain Python and the component vocabulary is closed and versioned with the compiler itself, not pluggable per project."),
            ("h2", "Where a project-specific rewrite still happens"),
            ("list", [
                "`arklight.config.py` is read as plain Python before `Site()` is constructed, but that's ordinary Python control flow -- a project reading its own environment variables, say -- not a registered preprocessor stage.",
                "The seven registered experimental features ([experimental APIs](/docs/experimental)) are the only place ARKlight steps outside its default closed vocabulary, and none of them is a general preprocessing hook.",
                "`--emit-arklight` writes a binary IR snapshot a later build can start from, which is closer to a build cache than to preprocessing a second language.",
            ]),
            ("p", "The practical effect mirrors parsing and compilation: fewer moving parts to configure, at the cost of no project-level escape hatch for a second authoring language. See [gotchas](/docs/gotchas) for what actually goes wrong at the one stage ARKlight does have -- including an unrecognized `# include` directive, covered in [sourcemaps and debugging](/docs/notes/sourcemaps-and-debugging)."),
            ("cards", _series_cards("/docs/notes/preprocessing")),
        ],
    },
    "/docs/notes/sourcemaps-and-debugging": {
        "title": "Sourcemaps and debugging",
        "description": "ARKlight's single-pass build has nothing transformed to map back to, so --debug prints a real Python traceback instead of a generated-to-source sourcemap.",
        "lead": "Five more short essays, part 3 of 5.",
        "blocks": [
            ("p", "`reference/svelte-v2.16.1/test/sourcemaps` fixtures exist because Svelte's compiler genuinely transforms your source into different generated code, line by line -- a sourcemap is what lets a browser devtools panel point back at the `.svelte` file instead of the generated JS it's actually running."),
            ("p", "ARKlight never generates code from a transformed intermediate form the way a `.svelte` file is rewritten. `arklight build --verbose` prints each pipeline stage, and `--debug` adds the full Python traceback on failure -- a trace through the compiler's own source, not a map back into a different source language."),
            ("table", ["Concern", "Svelte v2", "ARKlight"], [
                ["What the compiler emits", "Generated JS, often with a sourcemap back to .svelte", "Static HTML/CSS plus one fixed arklight.js runtime"],
                ["Debugging a build failure", "Devtools via the sourcemap, or the bundler's own errors", "--debug for the full Python traceback; --narrate for prose via Rei"],
                ["What the trace points at", "Your component source, through the map", "The compiler's own source, since nothing of yours survives transformed"],
            ]),
            ("note", "A real example: this patch tried wiring a markdown-authoring companion project into this site using a `# include <markdown.ARKlight>` directive its own README describes. Building it against the ARKlight version installed for this patch fails at the preamble-resolution stage with a plain, specific message naming the two directive forms that do exist -- no sourcemap needed to find the problem. See [markdown authoring](/examples/markdown-authoring) for the full story."),
            ("p", "This is also why ARKlight ships `sbom.txt` with every build: not a sourcemap, but a manifest of what actually went into the output, for a different kind of after-the-fact accounting -- more in [build tooling](/docs/notes/build-tooling)."),
            ("p", "See [the CLI](/docs/cli) for the exact flags, and [gotchas](/docs/gotchas) for the error table most `--debug` sessions end up confirming."),
            ("cards", _series_cards("/docs/notes/sourcemaps-and-debugging")),
        ],
    },
    "/docs/notes/custom-elements": {
        "title": "Custom elements",
        "description": "Why ARKlight has no compile target that exports a component as a reusable custom element usable outside its own build.",
        "lead": "Five more short essays, part 4 of 5.",
        "blocks": [
            ("p", "`reference/svelte-v2.16.1/test/custom-elements` fixtures cover a real Svelte v2 compile target: a component can be built so it registers itself as a native custom element, usable in any page regardless of whether that page was built with Svelte at all."),
            ("p", "ARKlight has no equivalent target. An `@component` is validated and expanded entirely within one build of one site -- [state model](/docs/concepts/state-model) already covers how its state is scoped to that one call -- and nothing about it is designed to be registered as a standalone element another, unrelated page could import."),
            ("h2", "Why that's a fairly deliberate gap, not an oversight"),
            ("list", [
                "A custom element has to carry its own runtime wiring wherever it's dropped in; ARKlight's one shared `arklight.js` is built for the one site that declares it, not for distribution to pages it never built.",
                "None of the seven registered experimental features targets this either -- see [experimental APIs](/docs/experimental) for the full list.",
                "The closest ARKlight gets to sharing a component across projects is sharing the Python function that builds it, the same plain-function reuse `nav()` demonstrates in [hello site](/examples/hello-site).",
            ]),
            ("p", "If a project genuinely needs a widget usable outside any one ARKlight build, that's a case for hand-written JS behind `script-extension`, not for stretching `@component` past the one build it belongs to."),
            ("cards", _series_cards("/docs/notes/custom-elements")),
        ],
    },
    "/docs/notes/build-tooling": {
        "title": "Build tooling",
        "description": "Why a complete ARKlight build is one CLI invocation instead of a bundler configuration, and what sbom.txt stands in for.",
        "lead": "Five more short essays, part 5 of 5.",
        "blocks": [
            ("p", "`reference/svelte-v2.16.1/rollup.config.js`, `rollup.store.config.js` and `package.json` show what surrounded the v2 compiler itself: a bundler configuration, a separate build for `store.js`, and `src/Stats.ts` tracking compile-time statistics as its own module."),
            ("p", "`arklight build site.py -o ARK` is the entire pipeline in one command, with no bundler to configure around it -- there's nothing downstream to bundle, since the output is already the static HTML, CSS and one fixed JS runtime a browser serves directly. [CLI](/docs/cli) lists the handful of flags that exist instead of a config file: `-v/--verbose`, `--debug`, `--narrate`, and the small set of site-wide overrides."),
            ("h2", "Where build-time information still comes out"),
            ("list", [
                "`sbom.txt`, written with every build, is the closest thing to `Stats.ts`'s compile-time bookkeeping -- a manifest of what the build actually produced, touched on in [sourcemaps and debugging](/docs/notes/sourcemaps-and-debugging).",
                "`arklight.config.py` covers genuinely build-affecting settings -- CSP, the `live-streaming` host and port, Android/Desktop packaging -- without turning into a general-purpose plugin pipeline.",
                "`arklight pack` and `arklight deploy` are later, separate steps -- bundling into a `.ark` file and shipping to Cloudflare Workers via Wrangler -- not stages a single build config wires together.",
            ]),
            ("p", "The trade is the same one running through this whole series: fewer configuration surfaces, because there's a closed vocabulary and one pipeline rather than a bundler project can extend arbitrarily."),
            ("cards", _series_cards("/docs/notes/build-tooling")),
        ],
    },
}
