# Deploying to Cloudflare (git-connected, auto-deploy on push)

This repo has no `npm`/Node.js build step -- it's built with `arklight`, a
PyPI package, via plain `python3`. Cloudflare's build container ships
Python/pip preinstalled, so this works, but none of it is auto-detected:
every field below has to be set by hand when connecting the repo.

If you just want to deploy once without auto-deploy-on-push, skip all of
this and use Direct Upload (drag-and-drop the `ARK/` folder you get from
running `make build` locally) instead -- it needs none of this setup.
See `make help` for the local build commands this file's "Build command"
mirrors.

## 1. Connect the repo

Cloudflare dashboard -> Workers & Pages -> Create application -> Pages (or
Workers, depending on which unified flow your account shows) -> Connect to
Git -> this repo.

## 2. Build configuration

| Field | Value |
|---|---|
| Framework preset | None |
| Build command | see below |
| Build output directory | `ARK` (only shown in the classic Pages flow; the Workers Builds flow instead reads this from `wrangler.jsonc`'s `assets.directory`, already set to `./ARK` in this repo) |
| Deploy command | `npx wrangler deploy` (Workers Builds flow only) |
| Non-production branch / preview deploy command | `npx wrangler versions upload` (Workers Builds flow only) |

**Build command:**

```
pip install arklight==0.70.0 && ARKLIGHT_ACCEPT_LICENSE=1 python3 scripts/check_content.py && ARKLIGHT_ACCEPT_LICENSE=1 python3 scripts/gen_site.py && ARKLIGHT_ACCEPT_LICENSE=1 arklight build site.py -o ARK --no-open && python3 scripts/postbuild.py ARK
```

Mirrors the Makefile's `build` target (`check_content.py` ->
`gen_site.py` -> `arklight build` -> `postbuild.py`) using the
container's own `python3`/`pip` instead of a local venv. Pinned to
`arklight==0.70.0` -- the latest version actually published to PyPI as
of this writing (`site_config.py`'s `ARKLIGHT_VERSION` constant says
0.70.1, which is this repo's own in-development version, ahead of
what's on PyPI; confirmed PyPI's 0.70.0 wheel still ships the
`script_extension` module this site's dark-mode toggle needs, so this
is a safe pin, not a workaround). Bump it deliberately once a newer
release is actually out, rather than tracking latest automatically --
an unpinned `pip install arklight` means a new release can change this
site's build output without anyone deciding that should happen.

## 3. Environment variables

Set these in the project's **Settings -> Environment variables** (not
in the build command itself -- keeps secrets/config out of build logs
and out of this repo):

| Variable | Value | Why |
|---|---|---|
| `ARKLIGHT_ACCEPT_LICENSE` | `1` | Required non-interactively by both `check_content.py`'s and `gen_site.py`'s underlying `arklight` import path and the `arklight build` step itself -- see `Makefile`'s `_license` target. Already inlined per-command above too, since Cloudflare's variable injection timing relative to each `&&`-chained command isn't guaranteed by this doc's own testing -- belt and suspenders. |
| `SITE_URL` | `https://<your-project>.pages.dev` (or your custom domain, once attached) | `site_config.py` builds canonical tags, Open Graph URLs and `sitemap.xml` from this; with it unset, those all resolve to `https://CHANGE-ME.example` instead -- the build won't fail, but the deployed site's own metadata will be wrong until this is set. |
| `CNAME_HOST` | your custom domain, if any | Optional -- only needed if `postbuild.py` should write a `CNAME` file (a GitHub-Pages-style custom-domain marker that Cloudflare itself ignores; harmless either way, but there's no reason to set it unless something else in your toolchain reads it). |

## 4. First deploy

Save and deploy. Workers Builds flow: this runs the build command, then
`npx wrangler deploy`, which reads `wrangler.jsonc` in the repo root
(already committed -- `assets.directory: "./ARK"`, `not_found_handling:
"404-page"`) to know what to upload and how to serve it. No `main`
field in that file is deliberate: there's no server-side Worker script,
only static assets.

## 5. After every push

Auto-deploys: pushes to the production branch run the build + deploy
command above; pushes to other branches (if non-production branch
builds are enabled in the project's settings) run the build command
then the preview deploy command, producing a preview URL instead of
promoting to production.
