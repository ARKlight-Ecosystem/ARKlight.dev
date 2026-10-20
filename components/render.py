# include <stdlib.ARKlight>
"""Turns content dicts (content/*.py) into ARKlight Page(...) trees.

Every imported project module needs its own `# include` line (see
docs/AUTHORING.md); route decorators live only in site.py.

Content blocks (see docs/AUTHORING.md for the full list):
  ("h2", text) ("h3", text) ("p", text) ("code", source)
  ("list", [text, ...]) ("note", text) ("table", header, rows)
  ("cards", [(title, text, href), ...])
Inline markup inside text: `code` and [label](href).
"""

import re

from site_config import (
    APPLE_TOUCH_ICON, FAVICON, OG_IMAGE, SITE_NAME, SITE_URL, TAGLINE, REPO_URL, PYPI_URL,
)
from pages.manifest import PAGES, TOP_NAV, SECTION_TITLES, by_route
from content import CONTENT
from theme import GOOGLE_FONTS_HREF

_INLINE = re.compile(r"(`[^`]+`|\[[^\]]+\]\([^)]+\))")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

ROUTES = {p["route"] for p in PAGES}


def _is_internal(href):
    return href.startswith("/")


def _link_ok(href):
    """Internal links must resolve to a route in this build, or ARKlight
    halts on an unresolved link. Checked here too so a typo fails fast
    with a clear message instead of a raw compiler error."""
    if not _is_internal(href):
        return True
    path = href.split("#", 1)[0] or "/"
    return path in ROUTES


def plain(text):
    """Strip inline markup (for components that only accept text)."""
    text = _LINK.sub(lambda m: m.group(1), text)
    return text.replace("`", "")


def inline(text):
    parts = _INLINE.split(text)
    if len(parts) == 1:
        return Text(text)
    nodes = []
    for part in parts:
        if not part:
            continue
        if part.startswith("`") and part.endswith("`"):
            nodes.append(Code(part[1:-1]))
        else:
            m = _LINK.fullmatch(part)
            if m and _link_ok(m.group(2)):
                nodes.append(Link(m.group(1), href=m.group(2)))
            elif m:
                nodes.append(m.group(1))
            else:
                nodes.append(part)
    return Container(*nodes)


def block(b):
    kind = b[0]
    if kind == "h2":
        return Heading(b[1], level=2)
    if kind == "h3":
        return Heading(b[1], level=3)
    if kind == "p":
        return inline(b[1])
    if kind == "code":
        return Pre(Code(b[1]))
    if kind == "list":
        return List(*[Item(plain(i)) for i in b[1]])
    if kind == "note":
        return Container(inline(b[1]), class_name="card")
    if kind == "table":
        head = TableHead(TableRow(*[TableHeaderCell(plain(h)) for h in b[1]]))
        rows = TableBody(
            *[TableRow(*[TableCell(plain(c)) for c in row]) for row in b[2]]
        )
        return Table(head, rows)
    if kind == "cards":
        cards = []
        for title, text, href in b[1]:
            if not _link_ok(href):
                continue  # skip cards whose target route doesn't exist
            cards.append(Container(
                Heading(title, level=3), Text(text), Link("Open", href=href),
                class_name="card",
            ))
        return Container(*cards, class_name="grid")
    raise ValueError(f"unknown content block {kind!r}")


# --------------------------------------------------------------------
# Shell: header, footer, section sidebar, prev/next, SEO head
# --------------------------------------------------------------------

def _header():
    links = [Link(SITE_NAME, href="/")]
    for label, href in TOP_NAV:
        if href in ROUTES:
            links.append(Link(label, href=href))
    return Header(Container(*links, class_name="nav"))


def _footer():
    kids = []
    for label, href in (("License", "/license"), ("Changelog", "/changelog")):
        if href in ROUTES:
            kids.append(Link(label, href=href))
    kids.append(Link("GitHub", href=REPO_URL))
    kids.append(Link("PyPI", href=PYPI_URL))
    return Footer(
        Container(*kids, class_name="nav"),
        Text(
            "ARKlight is GPLv3 with attribution terms; sites you build are yours. "
            "Your browser is still running JavaScript. We just made Python responsible for getting it there.",
            class_name="muted",
        ),
    )


def _sidebar(section, route):
    pages = [p for p in PAGES if p["section"] == section and p["route"] in ROUTES]
    title = SECTION_TITLES.get(section, section.title())
    links = [Link(p["label"], href=p["route"]) for p in pages]
    return Nav(Heading(title, level=3), *[Container(l) for l in links])


def _prev_next(section, route):
    pages = [p for p in PAGES if p["section"] == section and p["route"] in ROUTES]
    routes = [p["route"] for p in pages]
    if route not in routes or section not in ("tutorial",):
        return None
    i = routes.index(route)
    kids = []
    if i > 0:
        kids.append(Link("Previous: " + pages[i - 1]["label"], href=pages[i - 1]["route"]))
    if i < len(pages) - 1:
        kids.append(Link("Next: " + pages[i + 1]["label"], href=pages[i + 1]["route"]))
    return Container(*kids, class_name="nav") if kids else None


def _head_props(route, c):
    title = c["title"]
    full_title = title if route == "/" else f"{title} - {SITE_NAME}"
    description = c["description"]
    url = SITE_URL + ("/" if route == "/" else route)
    props = dict(
        title=full_title,
        description=description,
        og_title=full_title,
        og_description=description,
        og_image=SITE_URL + OG_IMAGE,
        favicon=FAVICON,
    )
    meta = {"twitter:card": "summary_large_image"}
    # Material You's type ramp leads with Roboto (see theme.py); these
    # two tags are how it actually loads in the browser instead of
    # silently falling back to the font stack's next entry.
    links = [
        {"rel": "preconnect", "href": "https://fonts.googleapis.com"},
        {"rel": "preconnect", "href": "https://fonts.gstatic.com", "crossorigin": ""},
        {"rel": "stylesheet", "href": GOOGLE_FONTS_HREF},
        {"rel": "apple-touch-icon", "href": APPLE_TOUCH_ICON},
    ]
    if route == "/404":
        meta["robots"] = "noindex"
    else:
        links.append({"rel": "canonical", "href": url})
    props["meta"] = meta
    props["links"] = links  # ARKlight rejects an empty links=[], but this is never empty
    return props


def render(route):
    c = CONTENT[route]
    meta = by_route()[route]
    section = meta["section"]
    head = _head_props(route, c)

    if c.get("kind") == "home":
        return _render_home(route, c, head)

    body = [Heading(c["title"], level=1)]
    if c.get("lead"):
        body.append(Text(c["lead"], class_name="muted"))
    body.extend(block(b) for b in c["blocks"])
    pn = _prev_next(section, route)
    if pn is not None:
        body.append(pn)
    article = Article(*body)

    in_section = section in ("tutorial", "docs", "examples", "project", "start")
    siblings = [p for p in PAGES if p["section"] == section and p["route"] in ROUTES]
    if in_section and len(siblings) > 1:
        main = Main(Container(_sidebar(section, route), article, class_name="sidebar"))
    else:
        main = Main(article)
    return Page(_header(), main, _footer(), **head)


def _render_home(route, c, head):
    hero = Section(
        Heading(c.get("h1", c["title"]), level=1),
        Text(c["lead"], class_name="muted"),
        Pre(Code(c["install"])),
    )
    demo = Container(
        Container(Heading("You write", level=3), Pre(Code(c["source"]))),
        Container(Heading("You ship", level=3), *[block(b) for b in c["ships"]]),
        class_name="switcher",
    )
    body = [hero, demo]
    body.extend(block(b) for b in c["blocks"])
    return Page(_header(), Main(*body), _footer(), **head)
