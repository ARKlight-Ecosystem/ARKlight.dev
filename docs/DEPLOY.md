# Deploying

Nothing here has been run against a real host. Treat each route as a starting point.

## Choose the domain first

`SITE_URL` has no default. Canonical tags, Open Graph image URLs and `sitemap.xml` all
need it, and `make pitstop` / `make release` fail until it is set.

## GitHub Pages (workflow included, untested)

`.github/workflows/deploy.yml` builds and deploys on push to `main`.

1. Settings > Pages > Source: **GitHub Actions**.
2. Repository variables: `SITE_URL`, `SITE_PHASE` (`1` or `2`, default `1`), optionally `CNAME_HOST`.
3. The workflow sets `ARKLIGHT_ACCEPT_LICENSE=1`. That means you accept ARKlight's license for the build, so read it first.

`SITE_PHASE=1` ships the pitstop. Flip it to `2` once the 21 drafts are written; until then
the workflow's check step fails the build, by design.

## Cloudflare (via `arklight deploy`)

`arklight deploy cloudflare` builds the site itself and then hands off to Wrangler. Per
`docs/Foundational/DEPLOYMENT-CLI.md` in the ARKlight repository, its form is:

```
arklight deploy [cloudflare] [entry] [-o OUTPUT_DIR] [--name NAME] [--skip-build] [--dry-run]
```

Because `deploy` runs its own build, a plain `arklight deploy` would produce an `ARK/`
**without** `sitemap.xml` and `robots.txt` (those come from `scripts/postbuild.py`). Build
with make first, then deploy the existing folder:

```bash
make pitstop        # or: make release   (builds and writes sitemap/robots)
arklight deploy cloudflare site.py -o ARK --skip-build --name your-worker-name --dry-run
```

Drop `--dry-run` when the printed command looks right. Not run by me; it needs Wrangler
and a Cloudflare account.

## Any static host

```bash
make pitstop        # or: make release
# upload ARK/
```

Make sure the host serves `404.html` for missing paths and resolves extensionless URLs
(see `SEO.md`).
