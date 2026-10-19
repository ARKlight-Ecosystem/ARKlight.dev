from ._util import draft

PAGES = {
    "/tutorial": {
        "title": "Tutorial",
        "description": "A hands-on ARKlight tutorial: pages and routes, components, state, bindings, actions, conditionals, styling, and packaging a build.",
        "lead": "Eight short lessons. Each one builds something you can run.",
        "blocks": [
            ("p", "Each lesson is a small, complete `site.py`. Build it with `arklight build site.py` and open the result. If a build fails, check the [gotchas](/docs/gotchas) before anything else."),
            ("cards", [
                ("1. Pages and routes", "Site, Page, and the @site.page decorator.", "/tutorial/pages-and-routes"),
                ("2. Components", "Reusable pieces, with keyword-only props.", "/tutorial/components"),
                ("3. State", "Declare reactive values on a page.", "/tutorial/state"),
                ("4. Bindings", "Show state and bind it to inputs.", "/tutorial/bindings"),
                ("5. Actions", "Change state in response to clicks.", "/tutorial/actions"),
                ("6. Conditionals and lists", "Show, hide and repeat.", "/tutorial/conditionals-and-lists"),
                ("7. Styling and layout", "Classes, selectors and container-based layout.", "/tutorial/styling-and-layout"),
                ("8. Build and pack", "Build, pack to .ark, PWA, deploy.", "/tutorial/build-and-pack"),
            ]),
        ],
    },
    "/tutorial/pages-and-routes": {
        "title": "Pages and routes",
        "description": "Lesson 1: how an ARKlight site is structured. The mandatory include line, Site(), and the @site.page decorator, including the rules that make routes discoverable.",
        "lead": "Every ARKlight site is a Site plus one decorated function per page.",
        "blocks": [
            ("h2", "The shape of a site"),
            ("code", "# include <stdlib.ARKlight>\n\nsite = Site()\n\n@site.page(\"/\")\ndef home():\n    return Page(\n        Heading(\"Home\"),\n        Text(\"Welcome.\"),\n        title=\"Home\",\n    )\n\n@site.page(\"/about\")\ndef about():\n    return Page(\n        Heading(\"About\"),\n        Link(\"Back home\", href=\"/\"),\n        title=\"About\",\n    )"),
            ("p", "Positional arguments to any component are its children. Keyword arguments are props, such as `title=` on `Page`."),
            ("h2", "Why the include line matters"),
            ("p", "`# include <stdlib.ARKlight>` looks like a comment to Python, but to ARKlight it is a compiler directive that brings the built-in vocabulary into scope. Leave it out and you get `name 'Site' is not defined`, with no hint that a directive is missing. Every file ARKlight loads needs its own include line."),
            ("h2", "How routes are found"),
            ("p", "ARKlight parses your entry file as an AST to find routes, and does not run it to discover them. That means it looks for specific syntax shapes. Use the literal decorator form `@site.page(\"/path\")`, in the file you pass to `arklight build`."),
            ("note", "Calling `site.page(\"/\")(home)` is valid Python, but ARKlight silently ignores it and fails with `No pages registered on 'site'`. See [gotchas](/docs/gotchas)."),
            ("h2", "Where each route becomes a file"),
            ("p", "`/` builds to `index.html`. Other routes build to their own HTML files. A `/404` route builds to `404.html`, which static hosts such as GitHub Pages serve for missing pages."),
            ("h2", "Try it"),
            ("list", [
                "Add a third page and link to it from the other two.",
                "Move the page bodies into helper functions in another module, keeping every `@site.page` in the entry file.",
            ]),
            ("p", "Next: [components](/tutorial/components)."),
        ],
    },
    "/tutorial/components": draft(
        "Components",
        "Lesson 2: building reusable ARKlight components with @component, keyword-only props, and what they compile to.",
        "Reusable pieces that disappear at build time.",
        [
            ("Plain functions first", "Show that a nav bar can be an ordinary Python function returning a Container (as in the hello_site example)."),
            ("The @component decorator", "Register a render function with props={...}; props are keyword-only, so Stat(label='x') works and Stat('x') raises ComponentError."),
            ("Compile-time expansion", "Explain that components expand during compilation and are validated as part of the resulting tree."),
            ("Try it", "Build a NavBar(active='home') component and use it on two pages."),
        ],
        "docs/Foundational/USER-DEFINED-COMPONENTS.md in the ARKlight repo",
    ),
    "/tutorial/state": draft(
        "State",
        "Lesson 3: declaring reactive state on an ARKlight page with State and Computed, and the rule that they must be children of Page.",
        "Reactive values that belong to a page.",
        [
            ("Declaring state", "State('count', 0) as a positional child of Page(...), never a bare statement."),
            ("The mistake everyone makes", "Reproduce the 'state isn't declared on this page' error and explain why: discovery walks the returned Page tree."),
            ("Derived values", "Computed and Derive.* with a small worked example."),
        ],
        "SKILL gotcha 4 and docs/Foundational/AUTHORING-GUIDE.md",
    ),
    "/tutorial/bindings": draft(
        "Bindings",
        "Lesson 4: showing state with Bind and wiring inputs with Bind.model in ARKlight.",
        "Connect state to what the reader sees and types.",
        [
            ("Showing a value", "Bind('name') as a child displays a scalar state value."),
            ("Two-way input binding", "Bind.model(...) is specifically for inputs; bind_value= usage; debounced and throttled variants."),
            ("Binding classes", "bind_class=Bind.when(...) for state-driven styling."),
        ],
        "docs/Implementation/JS-VOCABULARY-ADDENDUM-v0.070.md",
    ),
    "/tutorial/actions": draft(
        "Actions",
        "Lesson 5: changing ARKlight state from clicks with Action.increment, set, append, toggle_bool and friends, plus the built-in click behaviors.",
        "Everything a click can do without hand-written JavaScript.",
        [
            ("Actions that change state", "Walk through increment, decrement, set, reset, toggle_bool, append, remove."),
            ("Click behaviors", "on_click='toggle' and 'scroll-to' with behavior_target='#id' for disclosures and smooth scrolling."),
            ("Reading state in an action", "Bind(...) arguments are read from state when the action runs."),
        ],
        "arklight search Action.* output",
    ),
    "/tutorial/conditionals-and-lists": draft(
        "Conditionals and lists",
        "Lesson 6: Show with Predicate conditions and Repeat/RepeatItem for list-valued state in ARKlight.",
        "Show things conditionally and repeat them from state.",
        [
            ("Show and Predicate", "Show(Predicate.*(...)) with equals, gt, lt, one_of, is_empty."),
            ("Lists in state", "Repeat/RepeatItem is only for list-valued state; append and remove actions."),
            ("Worked example", "A small todo list (shared with /examples/todo-list)."),
        ],
    ),
    "/tutorial/styling-and-layout": draft(
        "Styling and layout",
        "Lesson 7: styling an ARKlight site with class_name, site.style, style_selector and container-width layout utilities, no media queries.",
        "Layout that responds to its container, not the viewport.",
        [
            ("Classes and style dicts", "class_name=, style={...}, site.style(name, {...}) takes a dict, never a CSS string."),
            ("Selectors", "site.style_selector for hover states, combinators and pseudo-classes."),
            ("Container-based layout", ".stack .cluster .switcher .grid .sidebar .center .reel and the Site(...) override kwargs."),
            ("Media queries", "Explain why css-media-queries is a deliberate experimental tradeoff."),
        ],
        "SKILL 'Authoring patterns' and docs/Foundational/CONFIGURABILITY.md",
    ),
    "/tutorial/build-and-pack": draft(
        "Build and pack",
        "Lesson 8: building, packing to a sealed .ark bundle, making a PWA, and deploying an ARKlight site.",
        "From a folder of HTML to something you can ship.",
        [
            ("Build", "arklight build site.py -o ARK --no-open and what the output folder contains."),
            ("Pack", "arklight pack ARK -o mysite.ark and unpack."),
            ("PWA", "arklight pwa for manifest and service worker."),
            ("Deploy", "arklight deploy cloudflare via Wrangler; see docs/Foundational/DEPLOYMENT-CLI.md."),
        ],
        "docs/Foundational/CLI-REFERENCE.md and DEPLOYMENT-CLI.md",
    ),
}
