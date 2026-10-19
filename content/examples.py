import os

from ._util import draft

_HERE = os.path.dirname(__file__)
_HELLO = open(os.path.join(_HERE, "_hello_site_excerpt.txt")).read().rstrip()

PAGES = {
    "/examples": {
        "title": "Examples",
        "description": "Complete, buildable ARKlight example sites: hello site, counter, todo list, a multi-page docs site and a landing page.",
        "lead": "Small, complete sites you can copy and build.",
        "blocks": [
            ("p", "Every example is a single `site.py`. Build with `arklight build site.py`."),
            ("cards", [
                ("Hello site", "A shared nav bar, a styled card and a toggle behavior. Straight from the ARKlight repo.", "/examples/hello-site"),
                ("Counter", "State, Bind and Action.increment.", "/examples/counter"),
                ("Todo list", "Lists in state with append and remove.", "/examples/todo-list"),
                ("Multi-page docs", "The entry-file routing pattern with helpers in other modules.", "/examples/multi-page-docs"),
                ("Landing page", "Layout utilities and SEO props.", "/examples/landing-page"),
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
    "/examples/counter": draft(
        "Counter",
        "A minimal ARKlight counter: State, Bind and Action.increment/decrement/reset, built from one Python file.",
        "The smallest stateful site.",
        [
            ("The code", "Full site.py with State, Text(Bind), and three buttons."),
            ("What gets built", "Show the output folder and explain the fixed arklight.js runtime."),
        ],
    ),
    "/examples/todo-list": draft(
        "Todo list",
        "An ARKlight todo list using list-valued State, Action.append and remove, and Repeat/RepeatItem.",
        "Lists in state.",
        [
            ("The code", "Full site.py: input with Bind.model, Action.append, Repeat/RepeatItem, Action.remove."),
            ("Limits", "No persistence by default; mention PlatformAPI.db for local storage."),
        ],
    ),
    "/examples/multi-page-docs": draft(
        "Multi-page docs",
        "How to structure a multi-page ARKlight site: every route decorator in the entry file, content and components in imported modules.",
        "The pattern this very website uses.",
        [
            ("Layout of the project", "site.py, pages/, components/, content/, assets/."),
            ("The entry file", "Show @site.page functions that delegate to render helpers."),
            ("Generating routes", "Explain gen_site.py and why a generator is needed (decorators must be literal)."),
        ],
        "this repository's scripts/gen_site.py and docs/ARCHITECTURE.md",
    ),
    "/examples/landing-page": draft(
        "Landing page",
        "An ARKlight landing page using container-based layout utilities (switcher, grid) and Page SEO props: description, Open Graph and canonical link.",
        "Layout and SEO on one page.",
        [
            ("The code", "Hero, switcher, grid of cards, footer."),
            ("The head tags", "description, og_*, meta={...}, links=[{'rel':'canonical'}] and what HTML each produces."),
        ],
    ),
}
