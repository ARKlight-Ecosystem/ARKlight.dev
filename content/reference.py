import json
import os

_GEN = json.load(open(os.path.join(os.path.dirname(__file__), "generated_reference.json")))
V = _GEN["arklight_version"]


def _codes(names):
    return ", ".join(f"`{n}`" for n in names)


PAGES = {
    "/docs": {
        "title": "Reference",
        "description": "ARKlight reference: components, actions, derivations, predicates, the CLI, configuration, experimental APIs and common build gotchas.",
        "lead": "Everything the compiler knows, in one place.",
        "blocks": [
            ("p", f"Written against ARKlight v{V}. For the exact contract of any entry, ask the compiler: `arklight search <Name>`. It prints the live schema with typo-tolerant suggestions."),
            ("cards", [
                ("Components", "The built-in component vocabulary and how props and children work.", "/docs/components"),
                ("Actions", "State-changing actions and the built-in click behaviors.", "/docs/actions"),
                ("CLI", "build, pack, unpack, pwa, deploy, new, search, live-streaming.", "/docs/cli"),
                ("Gotchas", "The four mistakes that cost the most build cycles, and the error table.", "/docs/gotchas"),
            ]),
        ],
    },
    "/docs/components": {
        "title": "Components",
        "description": "The ARKlight component vocabulary: layout, text, links, buttons, lists, tables and more, with the rules for props and children.",
        "lead": f"{len(_GEN['components'])} built-in components in v{V}.",
        "blocks": [
            ("h2", "How components work"),
            ("list", [
                "Positional arguments are children. Keyword arguments are props.",
                "Some components accept text only as children (for example Heading, Text, Item, Link and Code). Put a Code inside a Container, not inside an Item.",
                "Components you register with @component take keyword props only.",
            ]),
            ("h2", "The ones you will use first"),
            ("table", ["Component", "Notes"], [
                ["Site", "One per project. Takes site-wide options such as lang, max_width, bg and font_family."],
                ["Page", "One per route. Props include title, description, favicon, og_title, og_description, og_image, meta and links."],
                ["Container, Section, Article, Main, Header, Footer, Nav", "Layout and semantic wrappers; accept any children."],
                ["Heading", "Text child; the level prop sets the heading level (as in Heading(\"About\", level=2))."],
                ["Text, Strong, Em, Code", "Text-only children."],
                ["Link", "Requires href. Unresolved internal links halt the build."],
                ["Button", "on_click takes an Action, or a behavior name such as 'toggle'."],
                ["Image", "Requires src, which must exist under assets/."],
                ["Pre", "Wrap a Code inside for code blocks."],
                ["List, Item", "Item children are text only."],
                ["Table, TableHead, TableBody, TableRow, TableHeaderCell, TableCell", "Table building blocks."],
                ["Details, Summary", "A native disclosure widget."],
            ]),
            ("h2", "SEO props on Page"),
            ("p", "Page supports description, og_title, og_description, og_image and favicon. The meta prop is a dict of name to content, and links is a list of attribute dicts, each rendered as one link tag. That is how this site adds canonical URLs."),
            ("h2", f"Every component in v{V} (generated from the compiler)"),
            ("p", _codes(_GEN["components"])),
            ("note", "Props and child rules change between versions. Run `arklight search <Name>` for the authoritative contract."),
        ],
    },
    "/docs/actions": {
        "title": "Actions",
        "description": "ARKlight actions change page state in response to events: increment, decrement, set, reset, append, remove, toggle_bool and geolocate, plus the built-in click behaviors.",
        "lead": "What a click can do.",
        "blocks": [
            ("h2", "Actions"),
            ("p", "Pass an action to a component's `on_click`. The first argument is the name of a State."),
            ("code", "Button(\"Increment\", on_click=Action.increment(\"count\", 1))"),
            ("table", ["Action", "Notes"], [
                ["Action.increment", "Adds a delta (default 1) to a numeric state."],
                ["Action.decrement", "Subtracts a delta (default 1) from a numeric state."],
                ["Action.set", "Takes a value. A Bind(...) value is read from state when the action runs."],
                ["Action.reset", "Puts a state back to the initial value it was declared with. Needs no argument."],
                ["Action.append", "Takes a value. A Bind(...) value is read from state when the action runs."],
                ["Action.remove", "Removes the item at a given index from list-valued state (index-based, not value-based)."],
                ["Action.toggle_bool", "No arguments beyond the state name."],
                ["Action.geolocate", "Asks the browser for the visitor's location and stores a {lat, lng} object in state once they answer the permission prompt."],
            ]),
            ("p", "These are the actions present in v" + V + ". Run `arklight search Action.<name>` for each one's exact arguments."),
            ("h2", "Click behaviors"),
            ("p", "For disclosures and scrolling you don't need an action at all. Behaviors are validated against a fixed vocabulary at build time: " + _codes(_GEN["behaviors"]) + "."),
            ("code", "Button(\n    \"Show details\",\n    on_click=\"toggle\",\n    behavior_target=\"#more-details\",\n    toggle_class=\"hidden\",\n)"),
            ("p", "`toggle` flips a class on the target. Start the target with `class_name=\"hidden\"` and the button reveals it."),
        ],
    },
    "/docs/cli": {
        "title": "CLI",
        "description": "The arklight command-line reference: build, pack, unpack, pwa, deploy, new, search and live-streaming, with the most useful flags.",
        "lead": "One command, eight subcommands.",
        "blocks": [
            ("table", ["Command", "What it does"], [
                ["arklight build", "Compile a site file to static HTML and CSS."],
                ["arklight pack", "Pack a build directory into a single .ark bundle (sealed by default)."],
                ["arklight unpack", "Extract a .ark bundle's archive half back into a build directory."],
                ["arklight pwa", "Turn a build directory into an installable PWA (manifest and service worker)."],
                ["arklight deploy", "Build, then deploy with the hosting provider's own CLI (Cloudflare Workers via Wrangler)."],
                ["arklight new", "Scaffold a new project from a built-in template."],
                ["arklight search", "Look up a component's schema by name, with typo-tolerant suggestions."],
                ["arklight live-streaming", "Dev-only: auto-rebuild and browser auto-reload on file change."],
            ]),
            ("h2", "build"),
            ("code", "arklight build site.py -o ARK --no-open"),
            ("table", ["Flag", "Meaning"], [
                ["-o, --output", "Output directory (default: ARK)."],
                ["--open / --no-open", "Open the built site in your browser (default is to open)."],
                ["-v, --verbose", "Print each compiler pipeline stage."],
                ["--debug", "Like --verbose, plus the full traceback on failure."],
                ["--narrate", "Like --verbose, narrated in sentences by Rei, the compiler narrator."],
                ["--max-width, --bg, --font-family, --lang, --button-text", "Override site-wide options without editing the site file."],
                ["--emit-arklight", "Emit a binary IR snapshot that a later build can start from."],
            ]),
            ("h2", "Non-interactive use"),
            ("p", "In CI or scripts, set `ARKLIGHT_ACCEPT_LICENSE=1`, or `arklight` refuses to run. See the [license summary](/license)."),
            ("h2", "Looking things up"),
            ("code", "arklight search Picture\narklight search Action.increment"),
            ("p", "Prints required props, child rules, and arguments straight from the installed compiler."),
        ],
    },
    "/docs/gotchas": {
        "title": "Gotchas",
        "description": "The ARKlight build errors that cost the most time, with causes and fixes: missing include, route decorators, State placement, and a quick error table.",
        "lead": "Almost every one traces back to a single fact.",
        "blocks": [
            ("note", "ARKlight parses your entry file as an AST and never runs it to discover routes. It looks for specific syntax shapes, not runtime behavior."),
            ("h2", "1. The include line is mandatory"),
            ("p", "Every file using the built-in vocabulary must begin with `# include <stdlib.ARKlight>`. Without it you get `name 'Site' is not defined`. Each imported project module needs its own include line too."),
            ("h2", "2. Routes need the literal decorator"),
            ("code", "@site.page(\"/\")\ndef home():\n    ..."),
            ("p", "`site.page(\"/\")(home)` is valid Python but is silently ignored. The build fails with `No pages registered on 'site'`."),
            ("h2", "3. Decorators belong in the entry file"),
            ("p", "Discovery scans only the file you pass to `arklight build`. A decorator inside an imported module is invisible. Keep every `@site.page` in the entry file and import helpers for everything else."),
            ("h2", "4. State is a child of Page"),
            ("code", "# Wrong: State is never attached to the page\nState(\"count\", 0)\nreturn Page(Text(Bind(\"count\")))\n\n# Right\nreturn Page(\n    State(\"count\", 0),\n    Text(Bind(\"count\")),\n)"),
            ("h2", "Error table"),
            ("table", ["Error", "Likely cause"], [
                ["name 'X' is not defined (a component name)", "Missing the include line."],
                ["No pages registered on 'site'", "Decorator used as a call, or placed in an imported module."],
                ["state isn't declared on this page", "State(...) called as a bare statement instead of a Page child."],
                ["PreambleCollisionError", "Two includes bind the same name differently, or your code rebinds a preamble name."],
                ["BracketIndentationError", "A continuation line inside brackets is not indented further than its opener, or nesting is deeper than 8 levels."],
                ["ComponentError on a component call", "A registered component takes keyword props only."],
                ["Build halts on an unresolved link or asset", "A Link to a route that does not exist, or a src or favicon not under assets/."],
                ["Item can only contain text", "A Code or other component placed inside an Item."],
            ]),
            ("p", "For anything else, run `arklight build --debug` to see the full traceback."),
        ],
    },
}
