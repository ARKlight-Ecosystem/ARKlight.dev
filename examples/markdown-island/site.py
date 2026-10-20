# include <stdlib.ARKlight>
#
# This is the real, buildable counterpart to ../../md-theme-demo/, which
# describes itself (README.md, site.py's own comments) as using
# `# include <markdown.ARKlight>` and `Site(markdown_theme=...)` to turn
# content/index.md into a page with no Page(...) tree of its own. Neither
# exists in the ARKlight version this project is pinned to (confirmed with
# `arklight search Markdown` -- "No component named 'Markdown' found" -- and
# with a real `arklight build` of md-theme-demo/, which fails at preamble
# resolution naming only `<stdlib.ARKlight>` and `<acc.<dotted.module.path>>`
# as recognized include forms). See /examples/markdown-authoring on the main
# site for the full story.
#
# This file reproduces md-theme-demo/content/index.md's content by hand,
# component by component, as a genuinely standalone ARKlight site -- its
# own Site(), its own palette, its own stylesheet and arklight.js runtime,
# no shared header/footer/sidebar with arklight-dev. Built on its own and
# nested into the main site's output directory (see ../../Makefile), it
# reads as a deliberately separate "island" page: open it and you've left
# arklight-dev's own look entirely, with one Link back at the bottom.

LIVE_SITE = "https://arklight.arklight-compiler.workers.dev"

site = Site(
    name="markdown-island",
    lang="en",
    max_width="42rem",
    bg="#FBF6EC",
    font_family='"Source Serif 4", Georgia, "Times New Roman", serif',
    button_text="#FBF6EC",
)

# A reading-themed palette, deliberately unrelated to arklight-dev's
# Material You crimson (theme.py) -- the point of an island page is that
# it doesn't look like the site around it.
site.style("island-ink", {"color": "#2B2420"})
site.style("island-muted", {"color": "#6B5E52", "font-style": "italic"})
site.style("island-card", {
    "background": "#F3EAD9",
    "border": "1px solid #D8C7A8",
    "border-radius": "0.25rem",
    "padding": "1.25rem 1.5rem",
    "margin": "1.5rem 0",
})
site.style("island-pre", {
    "background": "#2B2420",
    "color": "#F3EAD9",
    "border-radius": "0.25rem",
    "padding": "1rem",
    "overflow-x": "auto",
})
site.style("island-rule", {
    "border": "none",
    "border-top": "1px solid #D8C7A8",
    "margin": "2rem 0",
})
site.style("island-back", {
    "display": "inline-block",
    "margin-top": "2rem",
    "font-family": '"Source Serif 4", Georgia, serif',
})


@site.page("/")
def home():
    return Page(
        Article(
            Heading("Markdown, themed", level=1),
            Container(
                "md-theme-demo/content/index.md describes itself as "
                "living in one file, turned into a page by an include "
                "directive and a markdown_theme preset -- neither of "
                "which this compiler build recognizes. Everything below "
                "is that same content instead, built the way ARKlight "
                "actually authors a page: as a ",
                Code("Page(...)"),
                " tree, by hand.",
                class_name="island-ink",
            ),
            Heading("What it can hold", level=2),
            Container(
                "A paragraph can carry ", Em("italic"), ", ",
                Strong("bold"), ", and ", Code("inline code"), ", plus a ",
                Link("link back to the ARKlight repository",
                     href="https://github.com/ARKlight-Ecosystem/ARKlight"),
                ".",
            ),
            Heading("A short list", level=3),
            List(
                Item("Headings here are plain Heading(level=...) calls, not generated ark-md-h1..h6 classes."),
                Item("Paragraphs are plain Text(...)."),
                Item("This bullet list is a real List of Item -- the same components the main site's own render.py uses."),
            ),
            Heading("A numbered list", level=3),
            OrderedList(
                Item("Fenced code blocks below are a real Pre(Code(...)), styled with the island-pre class."),
                Item("Blockquotes are a real Blockquote component, not a styled note card standing in for one."),
                Item("The table further down is a real Table/TableHead/TableBody tree."),
            ),
            Heading("A code block", level=3),
            Pre(
                Code(
                    "# include <stdlib.ARKlight>\n\n"
                    "site = Site(bg=\"#FBF6EC\")\n\n"
                    "@site.page(\"/\")\n"
                    "def home():\n"
                    "    return Page(Heading(\"Markdown, themed\"))"
                ),
                class_name="island-pre",
            ),
            Heading("A blockquote", level=3),
            Blockquote(
                Text(
                    "Markdown-as-content was meant to be opt-in, and not a "
                    "second syntax for Page(...) -- a page that needs "
                    "State, Bind, or a custom component still goes through "
                    "a @site.page(...)-decorated function. That line "
                    "turned out to be true for a reason its own author "
                    "probably didn't intend: there was no second syntax "
                    "to opt into at all."
                ),
                class_name="island-card",
            ),
            Heading("A table", level=3),
            Container(
                Table(
                    TableHead(
                        TableRow(
                            TableHeaderCell("Preset"),
                            TableHeaderCell("What md-theme-demo claimed"),
                        ),
                    ),
                    TableBody(
                        TableRow(TableCell("Light"), TableCell(Code("markdown_theme=\"light\""))),
                        TableRow(TableCell("Dark"), TableCell(Code("markdown_theme=\"dark\""))),
                        TableRow(TableCell("Reading"), TableCell(Code("markdown_theme=\"reading\""))),
                    ),
                ),
                class_name="table-scroll",
            ),
            Container(class_name="island-rule"),
            Text(
                "This island was built from examples/markdown-island/site.py, "
                "on its own, with its own Site(...), stylesheet and "
                "arklight.js -- then copied into the main build's output "
                "directory as a nested page (see the Makefile). Nothing "
                "about its look is shared with the rest of arklight-dev.",
                class_name="island-muted",
            ),
            Link(
                "\u2190 Back to arklight-dev",
                href=LIVE_SITE + "/examples/markdown-authoring",
                class_name="island-back",
            ),
        ),
        title="Markdown, themed (the real build)",
        description="The md-theme-demo content, hand-rebuilt as a real, buildable ARKlight page and deliberately styled as its own separate island.",
    )
