import os

_HERE = os.path.dirname(__file__)
_HELLO = open(os.path.join(_HERE, "_hello_site_excerpt.txt")).read().rstrip()

PAGES = {
    "/examples": {
        "title": "Examples",
        "description": "A complete, buildable ARKlight example site: a shared nav bar, a styled card and a toggle behavior.",
        "lead": "A small, complete site you can copy and build.",
        "blocks": [
            ("p", "Every example is a single `site.py`. Build with `arklight build site.py`."),
            ("cards", [
                ("Hello site", "A shared nav bar, a styled card and a toggle behavior. Straight from the ARKlight repo.", "/examples/hello-site"),
            ]),
        ],
    },
    "/examples/hello-site": {
        "title": "Hello site",
        "description": "The ARKlight hello_site example: a shared nav function, a styled card, and the built-in toggle behavior, with no hand-written JavaScript.",
        "lead": "The example that ships in the ARKlight repository (examples/hello_site/site.py), trimmed to its first page.",
        "blocks": [
            ("code", _HELLO),
            ("h2", "What to notice"),
            ("list", [
                "The first line is the include directive.",
                "`nav()` is a plain Python function. Reusable pieces are just function composition.",
                "The nav link for the current page is highlighted automatically by the shipped runtime.",
                "The Show details button uses the `toggle` behavior with `behavior_target`, so it needs no JavaScript of your own.",
            ]),
            ("p", "The full file also defines an /about page. Find it at `examples/hello_site/site.py` in the [ARKlight repository](https://github.com/ARKlight-Ecosystem/ARKlight/tree/main/examples/hello_site)."),
        ],
    },
}
