# Uses .RECIPEPREFIX so recipes are indented with ">" instead of tabs.
.RECIPEPREFIX = >
PY  ?= python3
OUT ?= ARK

.PHONY: help site1 site2 check status pitstop release dev1 dev2 serve clean _license

help:
> @echo "make pitstop   release build of the 15-page pitstop site (phase 1)"
> @echo "make release   release build of the full 36-page site (phase 2)"
> @echo "make dev1      build phase 1, no release gate"
> @echo "make dev2      build phase 2 incl. DRAFT pages, no release gate"
> @echo "make check     structure checks over the manifest and content"
> @echo "make status    regenerate docs/CONTENT-STATUS.md"
> @echo "make serve     serve $(OUT)/ locally with extensionless URLs"
> @echo "make clean     remove $(OUT)/"
> @echo
> @echo "Needs: pip install arklight; SITE_URL=https://your-domain for release builds;"
> @echo "ARKLIGHT_ACCEPT_LICENSE=1 once you have read ARKlight's LICENSE."

site1:
> $(PY) scripts/gen_site.py 1

site2:
> $(PY) scripts/gen_site.py 2

check:
> $(PY) scripts/check_content.py

status:
> $(PY) scripts/status.py

_license:
> @test -n "$$ARKLIGHT_ACCEPT_LICENSE" || { echo "Set ARKLIGHT_ACCEPT_LICENSE=1 after reading ARKlight's LICENSE (non-interactive runs need it)."; exit 1; }

pitstop: _license
> $(PY) scripts/check_content.py --release --phase 1
> $(PY) scripts/gen_site.py 1
> rm -rf $(OUT)
> arklight build site.py -o $(OUT) --no-open
> $(PY) scripts/postbuild.py $(OUT)

release: _license
> $(PY) scripts/check_content.py --release --phase 2
> $(PY) scripts/gen_site.py 2
> rm -rf $(OUT)
> arklight build site.py -o $(OUT) --no-open
> $(PY) scripts/postbuild.py $(OUT)

dev1: _license
> $(PY) scripts/gen_site.py 1
> rm -rf $(OUT)
> arklight build site.py -o $(OUT) --no-open
> $(PY) scripts/postbuild.py $(OUT)

dev2: _license
> $(PY) scripts/gen_site.py 2
> rm -rf $(OUT)
> arklight build site.py -o $(OUT) --no-open
> $(PY) scripts/postbuild.py $(OUT)

serve:
> $(PY) scripts/serve.py $(OUT) 8000

clean:
> rm -rf $(OUT)
