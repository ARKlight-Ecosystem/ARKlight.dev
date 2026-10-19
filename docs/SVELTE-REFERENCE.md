# The Svelte reference

`reference/svelte-v2.16.1/` is a **shallow clone** of `sveltejs/svelte` at tag `v2.16.1`
(commit `1e4ecf6`, 2019-02-08) with the `.git` directory removed. It is the last Svelte 2
release; Svelte 3.0.0 landed on 2019-04-21. About 14 MB, MIT licensed (see its `LICENSE`).

## What is in it

`src/` (compiler: `parse`, `compile`, `ssr`, `preprocess`, `shared`, ...), `test/`
(fixture-driven suites: `parser`, `runtime`, `css`, `hydration`, `server-side-rendering`,
`sourcemaps`, ...), `store.js`, `CHANGELOG.md`, rollup configs, `package.json`.

## What is NOT in it

**The v2 website source.** At this tag the repository has no `site/` folder; I did not find
the v2 docs site in it, and I did not track down where it lived. `site/` only shows up in
the repo during the Svelte 3 era. So this site's structure (home, tutorial, guide, examples,
blog) comes from my recollection of how `v2.svelte.dev` was laid out, not from copying source.
If you want the true site source, that is a separate search.

## What it is still good for

- A concrete picture of how a compiler-style project of that era organized `src/`, `test/` and a changelog.
- Fixture-driven tests (one directory per case) as a model for ARKlight's own docs examples.
- Reading how `v2` handled things that ARKlight also faces: server-side rendering, hydration, sourcemaps.

None of it is wired into the build. Nothing in the site depends on this directory,
so it can be deleted without effect.
