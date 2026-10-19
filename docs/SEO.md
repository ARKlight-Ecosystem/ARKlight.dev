# SEO

## Implemented (checked in the generated HTML)

| Item | How |
|---|---|
| Unique `<title>` per page | `"<Page title> - ARKlight"`; the home page has its own title |
| Meta description per page | `Page(description=...)`; `check_content.py` warns outside 70-200 chars |
| One `<h1>` per page | verified on the home, reference and tutorial pages |
| Canonical URL | `Page(links=[{"rel": "canonical", ...}])`, absolute, from `SITE_URL` |
| Open Graph | `og_title`, `og_description`, `og_image` (absolute URL) |
| Twitter card | `Page(meta={"twitter:card": "summary_large_image"})` |
| Favicon | `assets/favicon.svg` |
| `/404` | `noindex`, no canonical, builds to `404.html` |
| Semantic landmarks | `header`, `main`, `article`, `nav`, `footer` |
| `sitemap.xml`, `robots.txt` | `scripts/postbuild.py`; sitemap has **no `lastmod`** on purpose (a build-date stamp on every URL is inaccurate, and engines learn to ignore inaccurate lastmod) |
| `lang="en"` | `Site(lang="en")` |
| Content works without JS | output is static HTML |

## Not implemented

- **`og:url` / `og:type`.** ARKlight's `og_*` props cover title, description and image only, and `meta={...}` emits `name=` attributes, not `property=`. The canonical link carries the URL.
- **Structured data (JSON-LD).** I did not find a supported way to emit it. Unverified, not ruled out.
- **Analytics.** ARKlight sets `script-src 'self'` by default; a third-party script needs `Site(trusted_script_origins=[...])` and a deliberate decision.
- **Per-page social images.** One shared `og-image.png`, currently a placeholder.

## Verify after you put this somewhere

1. **Canonical vs `.html`.** ARKlight writes `docs/cli.html` and links to `.html` files, but the canonical tags say `/docs/cli`. This is fine on a host that serves extensionless URLs. `make serve` mimics that behavior locally. If the host serves only one form, make sure the other redirects to it.
2. `/anything-missing` returns **HTTP 404** with the 404 page.
3. Submit `sitemap.xml` in Search Console; confirm the 14 non-404 URLs are discovered.
4. Check a page in a social-card preview tool to confirm the OG image loads.
5. Look at the site in a real browser on a phone. The layout was **not** visually verified.

## Off-site (matters more than any tag at first)

A new domain takes months to rank. The links that count early: the ARKlight GitHub README,
the PyPI project page, and a launch post. Comparison pages ("ARKlight vs Eleventy/Astro")
are where new tools usually get found, but only if the claims in them are accurate.
