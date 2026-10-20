"""Five short essays contrasting ARKlight's model with a conventional
compile-to-JS framework. Not a tutorial on Svelte and not a port of
anything in reference/svelte-v2.16.1/ -- that checkout has no site of
its own (see docs/SVELTE-REFERENCE.md); these pages are organized
around the same handful of concerns any such compiler faces (parsing,
compilation, server rendering and hydration, client state, and a
fixture-driven test suite), looked at from ARKlight's side only.
"""

_NAV = [
    ("Parsing", "ARKlight reads syntax shapes, never runtime behavior.", "/docs/concepts/parsing"),
    ("Compilation", "One pass, a closed vocabulary, no plugin pipeline.", "/docs/concepts/compilation"),
    ("Rendering model", "Static HTML/CSS/JS out; no hydration step at all.", "/docs/concepts/rendering-model"),
    ("State model", "State lives on the page, not in an importable store.", "/docs/concepts/state-model"),
    ("Fixture-driven docs", "Every example here is a file that actually builds.", "/docs/concepts/fixture-driven-docs"),
]


def _series_cards(current):
    return [(t, d, h) for (t, d, h) in _NAV if h != current]


PAGES = {
    "/docs/concepts/parsing": {
        "title": "Parsing",
        "description": "Why ARKlight reads your entry file as an AST and never executes it to discover routes, and what that trades away and buys back.",
        "lead": "Five short essays, part 1 of 5.",
        "blocks": [
            ("p", "A compile-to-JS framework typically has to parse a custom file format -- Svelte's `.svelte` single-file components are their own small language, with a parser, a validator and an AST all of its own before any JavaScript is generated."),
            ("p", "ARKlight's entry file is plain Python. It still has a parser, but that parser is `ast.parse` from the standard library, pointed only at the entry file's own source, before any of your code runs. It looks for specific *syntax shapes* -- `Site()`, `@site.page(\"/...\")` -- not for what your code does when called."),
            ("note", "This is the single fact that explains the two most common build failures: `site.page(\"/\")(home)` is valid Python that does the same thing as the decorator at runtime, but the static scan never executes anything, so it never sees it. And a `@site.page(...)` decorator inside an *imported* module is invisible to a scan that only reads the entry file."),
            ("h2", "What this buys back"),
            ("list", [
                "No risk of an entry file with a route registered by a conditional, a loop, or a function call the compiler would have to actually run to find.",
                "A build fails at the same, predictable moment every time, rather than depending on what a dynamic script decided to do this run.",
                "`arklight search <Name>` can describe the whole component vocabulary up front, because the vocabulary isn't extensible at parse time the way a template language's custom directives can be.",
            ]),
            ("p", "The cost is symmetry: the entry file is the one place route decorators are allowed to live. See [gotchas](/docs/gotchas) for the exact error each mistake produces."),
            ("cards", _series_cards("/docs/concepts/parsing")),
        ],
    },
    "/docs/concepts/compilation": {
        "title": "Compilation",
        "description": "ARKlight's one-pass build from Python source to static output, and why there is no plugin pipeline to configure.",
        "lead": "Five short essays, part 2 of 5.",
        "blocks": [
            ("p", "A framework compiler of the Svelte v2 era is usually built as a pipeline: parse, then one or more preprocess stages, then compile, with hooks a project can slot into at nearly every stage."),
            ("p", "`arklight build site.py -o ARK` is closer to a single pass: read the entry file, resolve the closed `Site()` / `Page(...)` / component vocabulary against its own schema, and write plain HTML, CSS and one shared JS runtime file. There is no preprocess hook, because there is no second language to preprocess -- the input is already plain Python, and the output vocabulary is fixed."),
            ("h2", "Where configuration still exists"),
            ("list", [
                "`arklight.config.py` controls build-time settings such as the narrow `overdrive` escape hatch for a path a server supplies at runtime.",
                "Seven registered experimental features (`arklight search` and [experimental APIs](/docs/experimental)) are the only sanctioned way to step outside the default, intrinsic-layout-only output -- each one gated and warned about at build time, not silently available.",
                "`arklight pack` is a separate, later step (bundle a built site into one `.ark` file) rather than a compiler plugin.",
            ]),
            ("p", "The practical effect: there's very little to configure wrong. Most build failures trace back to the entry file's syntax shape (see [parsing](/docs/concepts/parsing)), not to a misconfigured pipeline stage."),
            ("cards", _series_cards("/docs/concepts/compilation")),
        ],
    },
    "/docs/concepts/rendering-model": {
        "title": "Rendering model",
        "description": "ARKlight ships plain static HTML with no server-side rendering mode and no client-side hydration step to reconcile.",
        "lead": "Five short essays, part 3 of 5.",
        "blocks": [
            ("p", "Server-side rendering and the hydration step that reconciles it against a client-rendered tree are a substantial part of what a framework compiler like Svelte's has to get right -- rendering the same component twice, once on a server and once in a browser, and making sure the two agree closely enough that the browser can take over without a visible flash or a mismatch error."),
            ("p", "ARKlight has neither mode, by design. `arklight build` always produces the same static HTML, once, with no server-rendered variant to keep in sync and nothing to hydrate afterward. The shipped `arklight.js` runtime attaches behavior -- `Bind`, `Action.*`, `Show`, `Repeat` -- to markup that already exists, rather than re-rendering it."),
            ("table", ["Concern", "A hydrating framework", "ARKlight"], [
                ["Initial HTML", "Rendered server-side or at build time", "Rendered once, at build time, always"],
                ["Client takeover", "Hydration reconciles server and client trees", "Runtime attaches behavior to existing markup"],
                ["Mismatch risk", "A real failure mode (hydration warnings)", "Not applicable -- there is only one render"],
            ]),
            ("note", "This is also why ARKlight has no large-SPA-style persistent cross-navigation app state and no general `fetch`/HTTP primitive: those live naturally in a client-rendering model, not a static-output one. The [Provider](/docs/experimental) escape hatch is the sanctioned way to talk to a real backend when a site needs one."),
            ("cards", _series_cards("/docs/concepts/rendering-model")),
        ],
    },
    "/docs/concepts/state-model": {
        "title": "State model",
        "description": "Why ARKlight keeps reactive state as a declared child of the page instead of an importable store module.",
        "lead": "Five short essays, part 4 of 5.",
        "blocks": [
            ("p", "Svelte v2 shipped `store.js`: an importable, framework-level store object that components anywhere in a tree could subscribe to, independent of where on the page it was created."),
            ("p", "ARKlight's `State(\"count\", 0)` works differently: it has to appear as a declared child of the `Page(...)` it belongs to (or, for a user-defined `@component`, instance-scoped to one call of that component) before anything else on the page can `Bind(...)` to it, act on it with `Action.*(...)`, or gate on it with `Show(Predicate.*(...))`."),
            ("list", [
                "`State(...)` called as a bare statement instead of a `Page(...)` child produces `\"<state> isn't declared on this page\"` at build time -- a build-time check a free-floating store object can't offer in the same way.",
                "Component-scoped state is genuinely instance-scoped: two calls to the same `@component` on one page never share one value, with no extra wiring needed to keep them apart.",
                "There is no cross-page store: state doesn't persist across a navigation, which follows directly from there being no large-SPA-style persistent app state at all (see [rendering model](/docs/concepts/rendering-model)).",
            ]),
            ("p", "The trade-off is explicit: a store you can import from anywhere is more flexible, but also harder for a static analyzer to reason about than state that must be declared where it's used. Walked through hands-on in [state and actions](/tutorial/state-and-actions)."),
            ("cards", _series_cards("/docs/concepts/state-model")),
        ],
    },
    "/docs/concepts/fixture-driven-docs": {
        "title": "Fixture-driven docs",
        "description": "Why every example on this site is a complete, buildable file rather than a prose description of one, borrowed from fixture-driven test suites.",
        "lead": "Five short essays, part 5 of 5.",
        "blocks": [
            ("p", "A compiler test suite of the Svelte v2 era is commonly fixture-driven: one directory per case, holding real input and the expected output side by side, so a suite doubles as a library of concrete, runnable examples rather than only a pass/fail signal."),
            ("p", "This site borrows that shape for documentation rather than tests. [Hello site](/examples/hello-site), [Counter](/examples/counter) and [Todo list](/examples/todo-list) are each a complete `site.py` that actually builds with `arklight build site.py` -- not a trimmed snippet assembled for prose."),
            ("list", [
                "A claim about the component vocabulary is checked against `arklight search <Name>` before it's written down here, the same way a fixture's expected output is checked against a real compiler run rather than typed from memory.",
                "`scripts/check_content.py` catches a route with no matching content, or content for a route the manifest doesn't declare -- a smaller, site-specific echo of a fixture suite catching an input with no expected output beside it.",
                "Keeping examples buildable means they drift much less: a prose description of a counter can quietly go stale; a `site.py` that's actually built stops building the moment it does.",
            ]),
            ("p", "Full component, action and CLI vocabulary: [reference overview](/docs). Worked examples end to end: [tutorial](/tutorial)."),
            ("cards", _series_cards("/docs/concepts/fixture-driven-docs")),
        ],
    },
}
