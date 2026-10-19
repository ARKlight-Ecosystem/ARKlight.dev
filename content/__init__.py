"""Aggregates every content module into CONTENT[route] -> dict.

Plain Python (no ARKlight vocabulary). Each module exposes PAGES, a
dict of route -> page dict. A page dict has: title, description, lead,
blocks.
"""
from . import home, start, tutorial, reference, examples, project

CONTENT = {}
for _m in (home, start, tutorial, reference, examples, project):
    for _route, _page in _m.PAGES.items():
        assert _route not in CONTENT, f"duplicate content for {_route}"
        CONTENT[_route] = _page
