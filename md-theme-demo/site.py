# include <stdlib.ARKlight>
# include <markdown.ARKlight>

# A single page, content/index.md, with nothing to register by hand:
# the `# include <markdown.ARKlight>` above is what turns content/*.md
# into pages at all -- remove it and this project builds with no
# pages, since site.py registers none of its own either.
#
# MD_THEME picks which of the three built-in markdown_theme presets
# this build uses -- plain Python, read before Site() is constructed,
# the same way the ARKlight.dev site reads SITE_URL from the
# environment in site_config.py. Nothing here is ARKlight vocabulary;
# only the string passed to markdown_theme= is.
import os

MD_THEME = os.environ.get("MD_THEME", "dark")

site = Site(markdown_theme=MD_THEME)
