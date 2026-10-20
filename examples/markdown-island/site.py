# include <stdlib.ARKlight>
# include <markdown.ARKlight>
#
# This is the real, buildable counterpart to ../../md-theme-demo/, which
# turns content/index.md into a page with no Page(...) tree of its own.
# On the ARKlight version this project was previously pinned to (main,
# v0.70.1), `# include <markdown.ARKlight>` failed at preamble resolution
# and `arklight search Markdown` found nothing -- see git history and
# /examples/markdown-authoring on the main site for that story. On
# `alpha`, confirmed with a real `arklight build` of this project, the
# directive and `Site(markdown_theme=...)` both work, so this island now
# uses them directly instead of reproducing the content by hand.
#
# `markdown_theme="reading"` is the built-in preset closest to this
# island's old bespoke cream/serif palette (see
# ../../md-theme-demo/README.md and arklight/backend/css/
# markdown_presets.py for the other two presets, "light" and "dark").
# The island still has no shared header/footer/sidebar with arklight-dev:
# content/index.md ends with its own Link back, in Markdown.

site = Site(
    name="markdown-island",
    lang="en",
    markdown_theme="reading",
)
