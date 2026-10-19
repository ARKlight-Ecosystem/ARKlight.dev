PAGES = {
    "/tutorial": {
        "title": "Tutorial",
        "description": "A hands-on ARKlight tutorial: pages, routes, Site, Page, and the @site.page decorator.",
        "lead": "A short lesson. It builds something you can run.",
        "blocks": [
            ("p", "The lesson is a small, complete `site.py`. Build it with `arklight build site.py` and open the result. If a build fails, check the [gotchas](/docs/gotchas) before anything else."),
            ("cards", [
                ("1. Pages and routes", "Site, Page, and the @site.page decorator.", "/tutorial/pages-and-routes"),
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
}
