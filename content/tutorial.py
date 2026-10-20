PAGES = {
    "/tutorial": {
        "title": "Tutorial",
        "description": "A hands-on ARKlight tutorial: pages, routes, Site, Page, and the @site.page decorator.",
        "lead": "A short lesson. It builds something you can run.",
        "blocks": [
            ("p", "The lesson is a small, complete `site.py`. Build it with `arklight build site.py` and open the result. If a build fails, check the [gotchas](/docs/gotchas) before anything else."),
            ("cards", [
                ("1. Pages and routes", "Site, Page, and the @site.page decorator.", "/tutorial/pages-and-routes"),
                ("2. State and actions", "A click counter: State, Bind, and Action.*, no hand-written JS.", "/tutorial/state-and-actions"),
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
            ("p", "Next: the [reference](/docs) covers every component and action in the vocabulary."),
        ],
    },
    "/tutorial/state-and-actions": {
        "title": "State and actions",
        "description": "Lesson 2: a click counter built from State, Bind and Action.*, with no JavaScript written by hand anywhere in the file.",
        "lead": "State lives on the page. Bind displays it. Action.* changes it.",
        "blocks": [
            ("h2", "Declare the state"),
            ("p", "`State(\"count\", 0)` is a child of `Page(...)`, not a bare statement -- that's what makes it declared on the page. It takes a name and a starting value."),
            ("code", "# include <stdlib.ARKlight>\n\nsite = Site()\n\n@site.page(\"/\")\ndef home():\n    return Page(\n        State(\"count\", 0),\n        Heading(\"Counter\"),\n        Text(Bind(\"count\")),\n        Button(\"Increment\", on_click=Action.increment(\"count\")),\n        Button(\"Decrement\", on_click=Action.decrement(\"count\")),\n        Button(\"Reset\", on_click=Action.set(\"count\", value=0)),\n        title=\"Counter\",\n    )"),
            ("note", "`State(...)` called as a bare statement before the `return`, instead of passed as a child of `Page(...)`, fails with \"references state that isn't declared on this page\" the moment anything tries to `Bind` it. See [gotchas](/docs/gotchas)."),
            ("h2", "Display it"),
            ("p", "`Bind(\"count\")` as a direct child of `Text(...)` renders the live value. It's for a single scalar value; a list-valued state uses `Repeat` instead."),
            ("h2", "Change it"),
            ("list", [
                "`Action.increment(\"count\")` and `Action.decrement(\"count\")` each take an optional `delta`, 1 by default.",
                "`Action.set(\"count\", value=0)` sets it outright -- useful for a reset button.",
                "Every `Action.*` call is built-in and validated at build time against a closed vocabulary. There's no arbitrary JS here.",
            ]),
            ("h2", "Try it"),
            ("list", [
                "Change the increment button's delta to 5 and see the build re-validate it.",
                "Add a squared value next to the counter: `Computed(\"squared\", deps=(\"count\",), derive=Derive.multiply(\"count\", \"count\"))`, then `Bind(\"squared\")`.",
            ]),
            ("p", "See it live in [examples](/examples/counter), or move on to the [reference](/docs) for the full `State`/`Action`/`Derive` vocabulary."),
        ],
    },
}
