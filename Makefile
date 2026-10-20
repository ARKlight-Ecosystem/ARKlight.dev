# Uses .RECIPEPREFIX so recipes are indented with ">" instead of tabs.
.RECIPEPREFIX = >
PY  ?= python3
OUT ?= ARK

.PHONY: help site check build island serve clean _license

ISLAND_OUT := $(OUT)/examples/markdown-authoring/live

help:
> @echo "make build     check -> generate site.py -> arklight build -> island -> sitemap/robots"
> @echo "make check     structure and SEO field checks over the manifest and content"
> @echo "make site      regenerate site.py from pages/manifest.py"
> @echo "make island    build examples/markdown-island/ on its own, nested under $(ISLAND_OUT)/"
> @echo "make serve     serve $(OUT)/ locally with extensionless URLs"
> @echo "make clean     remove $(OUT)/"
> @echo
> @echo "Needs: pip install arklight; SITE_URL=https://your-domain for the real site;"
> @echo "ARKLIGHT_ACCEPT_LICENSE=1 once you have read ARKlight's LICENSE."

site:
> $(PY) scripts/gen_site.py

check:
> $(PY) scripts/check_content.py

_license:
> @test -n "$$ARKLIGHT_ACCEPT_LICENSE" || { echo "Set ARKLIGHT_ACCEPT_LICENSE=1 after reading ARKlight's LICENSE (non-interactive runs need it)."; exit 1; }

# examples/markdown-island/ is its own ARKlight project -- own Site(),
# own stylesheet, own arklight.js, no shared header/footer/sidebar with
# the main site. Built on its own, then nested under the main build's
# output directory as a deliberately separate-looking page. Must run
# after the main `arklight build` (which recreates $(OUT) from scratch)
# and before postbuild.py (which only touches $(OUT)'s own root).
island: _license
> arklight build examples/markdown-island/site.py -o $(ISLAND_OUT) --no-open

build: _license
> $(PY) scripts/check_content.py
> $(PY) scripts/gen_site.py
> rm -rf $(OUT)
> arklight build site.py -o $(OUT) --no-open
> $(MAKE) island
> $(PY) scripts/postbuild.py $(OUT)

serve:
> $(PY) scripts/serve.py $(OUT) 8000

clean:
> rm -rf $(OUT)
