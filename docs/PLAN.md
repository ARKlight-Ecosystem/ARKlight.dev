# Plan: 36 pages in two stops

## Why this shape

The model is the Svelte 2 website: a home page that shows the idea in one screen,
a hands-on tutorial, a reference, an examples gallery, and a blog. Svelte's site
also had an in-browser REPL; ARKlight has no Python in the browser, so there is
none here. Each example instead shows source next to what it builds.

> Provenance: the structure above is from memory of how `v2.svelte.dev` was laid out.
> The Svelte v2.16.1 checkout in `reference/` contains the compiler, not the site
> (see `SVELTE-REFERENCE.md`), so I could not copy the structure from source.

## Inventory

| Section | Pages | Phase 1 | Phase 2 |
|---|---|---|---|
| Home | `/` | 1 | |
| Start | `/getting-started`, `/why` | 2 | |
| Tutorial | index + 8 lessons | index, lesson 1 | lessons 2-8 |
| Reference | index + 9 | index, components, actions, cli, gotchas | derive, predicates, config, experimental, platform-apis |
| Examples | index + 5 | index, hello-site | counter, todo-list, multi-page-docs, landing-page |
| Compare | 2 | | eleventy, astro |
| Project | 5 | changelog, license | roadmap, blog, introducing-arklight |
| System | `/404` | 1 | |
| **Total** | **36** | **15** | **21** |

## Phase 1 (pitstop): 15 pages

Enough to be a credible site on day one: pitch, install, one lesson, the core
reference, one example, license and changelog. It is deliberately the smallest set that
answers "what is it, how do I start, what are the rules, what are the limits".

## Phase 2 (final): the remaining 21

Order of work I would suggest, highest search value first:

1. Reference pages (derive, predicates, config, experimental, platform-apis). These
   already have generated lists of every entry; they need prose and one example each.
2. Tutorial lessons 2-8. Each should be one small, buildable `site.py`.
3. Examples. Build and test each one before publishing it.
4. `/blog/introducing-arklight` and `/roadmap`. These need the author's voice and decisions.
5. Compare pages last, and only after fact-checking the other tools' current docs.

## Why the draft gate exists

A "coming soon" page costs SEO and trust. Drafts render with a banner for
preview, but `make pitstop` and `make release` refuse to build while any page in
that phase is still a draft.
