SOURCE = '''# include <stdlib.ARKlight>

site = Site()

@site.page("/")
def home():
    return Page(
        Heading("ARKlight"),
        State("count", 0),
        Text(Bind("count")),
        Button("Increment", on_click=Action.increment("count", 1)),
        title="Demo",
    )'''

PAGES = {
    "/": {
        "kind": "home",
        "title": "ARKlight: build websites with Python, ship plain HTML",
        "h1": "ARKlight",
        "description": "ARKlight is a Python-first static-site compiler. Write pages as Python, get plain HTML, CSS and a tiny fixed JS runtime. The browser never runs Python.",
        "lead": "A Python-first compiler for websites. Write pages as ordinary Python; ship plain HTML, CSS and a small fixed JavaScript runtime. The browser never runs Python.",
        "install": "pip install arklight\narklight build site.py",
        "source": SOURCE,
        "ships": [
            ("p", "A static folder you can serve from anything: `index.html`, a stylesheet, one fixed `arklight.js` runtime, and an `sbom.txt`."),
            ("p", "The button above is wired to live reactive state, with no JavaScript written by hand."),
            ("p", "Python needs to be 3.10 or newer, and only at build time."),
        ],
        "blocks": [
            ("h2", "What you get"),
            ("cards", [
                ("Python in, static out", "Describe pages as Python function calls. ARKlight validates them against a closed vocabulary, then compiles them to HTML, CSS and a fixed JS runtime.", "/why"),
                ("Compiler first, runtime last", "Routing, validation, dependency resolution and CSS happen at build time. The browser runtime only handles what needs a browser: input, local storage, viewport, reactive state, URL state.", "/why"),
                ("A closed vocabulary", "The compiler knows every component and behavior that can exist. No arbitrary JavaScript expressions are evaluated at runtime.", "/docs/components"),
                ("Components that compile away", "User-defined components expand during compilation, so the abstraction does not survive into the generated site.", "/docs/components"),
                ("Package it your way", "Pack a build into a single sealed `.ark` bundle, make it a PWA, or deploy it to Cloudflare Workers with `arklight deploy`.", "/docs/cli"),
                ("Diagnostics with a voice", "Rei, the compiler narrator, can narrate a build in plain sentences with `--narrate`.", "/docs/cli"),
            ]),
            ("h2", "Start here"),
            ("p", "New to ARKlight? Go to [Getting started](/getting-started), then work through the [tutorial](/tutorial). Already building something? The [reference](/docs) and the [gotchas](/docs/gotchas) will save you a few build cycles."),
        ],
    },
}
