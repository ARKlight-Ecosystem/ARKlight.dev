import os

from site_config import SITE_URL

_HERE = os.path.dirname(__file__)
_HELLO = open(os.path.join(_HERE, "_hello_site_excerpt.txt")).read().rstrip()
# The island build is a real, separately-built page nested at this path
# under the main site's own output (see the Makefile's `island` target,
# and examples/markdown-island/site.py). It isn't a route this site's
# own `pages/manifest.py` registers, so it has to be linked as an
# absolute URL -- render.py's internal-link check only resolves routes
# in ROUTES, and would silently drop a root-relative link to a path
# that isn't one of them.
_ISLAND_URL = SITE_URL + "/examples/markdown-authoring/live/"

PAGES = {
    "/examples": {
        "title": "Examples",
        "description": "A complete, buildable ARKlight example site: a shared nav bar, a styled card and a toggle behavior.",
        "lead": "A small, complete site you can copy and build.",
        "blocks": [
            ("p", "Every example is a single `site.py`. Build with `arklight build site.py`."),
            ("cards", [
                ("Hello site", "A shared nav bar, a styled card and a toggle behavior. Straight from the ARKlight repo.", "/examples/hello-site"),
                ("Counter", "A click counter built from State, Bind and Action.*, with a derived squared value.", "/examples/counter"),
                ("Todo list", "A growing list built from State, Repeat, Show and a bound input, no hand-written JS.", "/examples/todo-list"),
                ("Markdown authoring", "A companion project's Markdown page, and what happened when we actually tried to build it.", "/examples/markdown-authoring"),
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
    "/examples/counter": {
        "title": "Counter",
        "description": "A click counter: State, Bind, Action.increment/decrement/set, and a Computed derived value, with no hand-written JavaScript.",
        "lead": "The lesson from the tutorial, as a complete, buildable file.",
        "blocks": [
            ("code", "# include <stdlib.ARKlight>\n\nsite = Site()\n\n@site.page(\"/\")\ndef home():\n    return Page(\n        State(\"count\", 0),\n        Computed(\"squared\", deps=(\"count\",), derive=Derive.multiply(\"count\", \"count\")),\n        Heading(\"Counter\"),\n        Text(Bind(\"count\")),\n        Text(\"Squared: \", Bind(\"squared\")),\n        Button(\"Increment\", on_click=Action.increment(\"count\")),\n        Button(\"Decrement\", on_click=Action.decrement(\"count\")),\n        Button(\"Reset\", on_click=Action.set(\"count\", value=0)),\n        title=\"Counter\",\n    )"),
            ("h2", "What to notice"),
            ("list", [
                "`State(\"count\", 0)` is a child of `Page(...)`, which is what makes it declared on the page.",
                "`Computed` takes `deps=` (the state names it reads) and `derive=` (a closed-vocabulary `Derive.*` call) -- never a parsed or executed expression string.",
                "`Action.increment`/`Action.decrement` default to a delta of 1; `Action.set(..., value=0)` is the reset.",
                "Nothing here is hand-written JavaScript -- every behavior is validated against a fixed vocabulary at build time.",
            ]),
            ("p", "Walked through step by step in the [tutorial](/tutorial/state-and-actions)."),
        ],
    },
    "/examples/todo-list": {
        "title": "Todo list",
        "description": "A complete, buildable ARKlight todo list: State, Bind.model, Action.append/set/reset, Watch, Repeat and Show, with no hand-written JavaScript anywhere in the file.",
        "lead": "Every piece from the lists-and-conditionals lesson, assembled into one file.",
        "blocks": [
            ("code", "# include <stdlib.ARKlight>\n\nsite = Site()\n\n@site.page(\"/\")\ndef home():\n    return Page(\n        State(\"draft\", \"\"),\n        State(\"tasks\", []),\n        Heading(\"Tasks\"),\n        Text(\"Add a task, then clear the list whenever you're done.\", class_name=\"muted\"),\n        Container(\n            Input(bind_value=Bind.model(\"draft\")),\n            Button(\"Add\", on_click=Action.append(\"tasks\", Bind(\"draft\"))),\n            Button(\"Clear all\", on_click=Action.set(\"tasks\", value=[])),\n            class_name=\"cluster\",\n        ),\n        Watch(\"tasks\", then=Action.reset(\"draft\")),\n        Show(Predicate.is_empty(\"tasks\"), Text(\"No tasks yet.\", class_name=\"muted\")),\n        Container(\n            Repeat(\"tasks\", template=lambda: Text(RepeatItem.value())),\n            class_name=\"stack card\",\n        ),\n        title=\"Tasks\",\n    )"),
            ("h2", "What to notice"),
            ("list", [
                "`State(\"draft\", \"\")` and `State(\"tasks\", [])` are both children of `Page(...)`, which is what makes them declared on the page.",
                "`Bind(\"draft\")` as `Action.append`'s value argument reads whatever the input currently holds at the moment the button is clicked.",
                "`Watch(\"tasks\", then=Action.reset(\"draft\"))` fires whenever `tasks` changes, so the input empties itself right after a task is added.",
                "`Show(Predicate.is_empty(\"tasks\"), ...)` and `Repeat(\"tasks\", ...)` read the same list; nothing here is hand-written JavaScript -- every behavior is validated against a fixed vocabulary at build time.",
                "`.cluster`, `.stack` and `.card` are the built-in layout and style utility classes from [styling and layout](/tutorial/styling-and-layout); nothing here needed a stylesheet of its own.",
            ]),
            ("p", "Walked through step by step in [lists and conditionals](/tutorial/lists-and-conditionals)."),
        ],
    },
    "/examples/markdown-authoring": {
        "title": "Markdown authoring",
        "description": "A page written as Markdown in a companion project, reproduced here through this site's own content pipeline, plus what happened when we tried to build the original.",
        "lead": "What authoring a page as Markdown looks like, and what actually builds today.",
        "blocks": [
            ("p", "This repository also carries a small, separate scaffold project, `md-theme-demo/`, built around a `# include <markdown.ARKlight>` directive that, according to its own README and `site.py` comments, turns a folder of `.md` files into pages with no `@site.page(...)` or `Page(...)` tree at all."),
            ("note", "Building `md-theme-demo/` against the ARKlight version installed for this patch's `main` branch (v0.70.1) fails: `arklight build` rejects `# include <markdown.ARKlight>` at the preamble-resolution stage, naming the two directive forms that do exist there -- `<stdlib.ARKlight>` and `<acc.<dotted.module.path>>`. On the `alpha` branch it builds correctly -- confirmed with a real `arklight build` of `md-theme-demo/` and of `examples/markdown-island/`, both producing `# include <markdown.ARKlight>` output with the `reading` `markdown_theme` preset. Verify with `arklight search Markdown` or a real build against whichever branch you have installed before relying on it."),
            ("p", "The content is still worth carrying over, since it's a clean demonstration of the inline markup and block types this site already renders through `components/render.py`: inline code, links, lists, a table and a note card. What follows is that same content, carried by hand into this site's own `title`/`description`/`blocks` shape, since this site itself still targets `main` rather than `alpha`."),
            ("p", "There is also a real, buildable version: `examples/markdown-island/site.py` now uses the real `# include <markdown.ARKlight>` directive and `Site(markdown_theme=\"reading\")` directly -- content/index.md, not a hand-written Page(...) tree -- built against the `alpha` branch. It builds on its own and is nested into this site's own output at `/examples/markdown-authoring/live/` -- [open it](" + _ISLAND_URL + ") and use the link at the bottom to come back."),
            ("h2", "What it can hold"),
            ("p", "A paragraph can carry `inline code` and a [link back to the ARKlight repository](https://github.com/ARKlight-Ecosystem/ARKlight). The original Markdown version could also carry italics and bold; this site's own inline parser (`components/render.py`) only understands backtick code and `[label](href)` links, which is part of why the rest of this page is plain prose rather than a reproduction of that formatting."),
            ("h3", "A short list"),
            ("list", [
                "Headings would become `ark-md-h1` through `ark-md-h6` in the original markdown-theme build, each with a slugged id.",
                "Paragraphs would be `ark-md-p`.",
                "This bullet list would be `ark-md-list` / `ark-md-item` there; here it renders through this site's own List and Item components instead.",
            ]),
            ("h3", "A numbered list"),
            ("list", [
                "Fenced code blocks would become `ark-md-pre` / `ark-md-code-block`.",
                "Blockquotes would become `ark-md-blockquote`.",
                "A pipe table would become `ark-md-table`.",
            ]),
            ("h3", "A code block"),
            ("code", "# include <stdlib.ARKlight>\n# include <markdown.ARKlight>\n\nsite = Site(markdown_theme=\"dark\")"),
            ("h3", "A blockquote"),
            ("note", "Markdown-as-content was meant to be opt-in, and not a second syntax for `Page(...)` -- a page that needs `State`, `Bind`, or a custom component still goes through a `@site.page(...)`-decorated function."),
            ("h3", "A table"),
            ("table", ["Preset", "Site(markdown_theme=...)"], [
                ["Light", "\"light\""],
                ["Dark", "\"dark\""],
                ["Reading", "\"reading\""],
            ]),
            ("p", "See `md-theme-demo/` in this repository for the original files, and [gotchas](/docs/gotchas) and [sourcemaps and debugging](/docs/notes/sourcemaps-and-debugging) for more on how ARKlight reports an unrecognized include directive like this one."),
        ],
    },
}
