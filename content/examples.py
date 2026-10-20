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
                ("Counter", "A click counter built from State, Bind and Action.*, with a derived squared value.", "/examples/counter"),
                ("Todo list", "A growing list built from State, Repeat, Show and a bound input, no hand-written JS.", "/examples/todo-list"),
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
}
