"""Helpers shared by content modules (plain Python)."""


def draft(title, description, lead, outline, source_notes=None):
    """A draft outline page: real title/description/headings, each
    heading followed by a one-line statement of what the section must
    cover. Marked draft=True, so release builds refuse to ship it until
    the text is written (see docs/CONTENT-STATUS.md)."""
    blocks = []
    for heading, intent in outline:
        blocks.append(("h2", heading))
        blocks.append(("p", intent))
    if source_notes:
        blocks.append(("note", "Sources to draw from: " + source_notes))
    return {
        "title": title,
        "description": description,
        "lead": lead,
        "blocks": blocks,
        "draft": True,
    }
