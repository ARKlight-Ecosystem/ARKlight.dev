# Uses .RECIPEPREFIX so recipes are indented with ">" instead of tabs.
.RECIPEPREFIX = >
PY  ?= python3
OUT ?= ARK

.PHONY: help site check build serve clean _license

help:
> @echo "make build     check -> generate site.py -> arklight build -> sitemap/robots"
> @echo "make check     structure and SEO field checks over the manifest and content"
> @echo "make site      regenerate site.py from pages/manifest.py"
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

build: _license
> $(PY) scripts/check_content.py
> $(PY) scripts/gen_site.py
> rm -rf $(OUT)
> arklight build site.py -o $(OUT) --no-open
> $(PY) scripts/postbuild.py $(OUT)

serve:
> $(PY) scripts/serve.py $(OUT) 8000

clean:
> rm -rf $(OUT)
