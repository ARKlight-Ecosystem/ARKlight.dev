PAGES = {
    "/changelog": {
        "title": "Changelog",
        "description": "Recent ARKlight releases: v0.70.1 documentation patch and the v0.70.0 catch-up release with user-defined components, Provider SDK, Platform API IR and arklight deploy.",
        "lead": "A summary. The full history lives in the repository.",
        "blocks": [
            ("h2", "0.70.1: documentation patch"),
            ("p", "Docs-only; no behavior change. The README now points AI-assisted developers to the ARKlight Skills Collections, install instructions name `pip install arklight` and the license flag a source build needs, and preamble docs open with `# include <stdlib.ARKlight>`."),
            ("h2", "0.70.0: catch-up release"),
            ("p", "Main moved from 0.54.0 to the v0.070 milestone, with code, tests and docs together."),
            ("list", [
                "User-defined components with `@component` and clear build-time diagnostics.",
                "A ten-rung JS vocabulary ladder: new Derive and Predicate kinds, Action.geolocate, clipboard paste, matchMedia state, reveal and lazy, debounced and throttled binding, URL-state syncing, class binding.",
                "The Provider SDK for declaring external runtime services.",
                "Platform API IR, including PlatformAPI.db (IndexedDB, Web only on main).",
                "The preamble system and the Rei compiler narrator.",
                "Search and docs tooling, including arklight search --retrieve-doc.",
                "arklight deploy.",
            ]),
            ("p", "Read the complete, authoritative history in the [CHANGELOG on GitHub](https://github.com/ARKlight-Ecosystem/ARKlight/blob/main/CHANGELOG.md)."),
        ],
    },
    "/license": {
        "title": "License",
        "description": "A plain-language summary of ARKlight's license: GPLv3 plus attribution terms, what it covers, what it does not, and the acceptance step the CLI requires.",
        "lead": "A summary, not legal advice. The LICENSE file is authoritative.",
        "blocks": [
            ("h2", "The short version"),
            ("list", [
                "ARKlight is licensed under GPLv3 plus attribution terms.",
                "Those terms cover the compiler and its embedded runtime file.",
                "They do not cover your own site's source or the output you build with it.",
            ]),
            ("h2", "The acceptance step"),
            ("p", "The first `arklight` command asks you to accept the license terms. Scripted or CI contexts cannot answer, so `arklight` refuses to run there unless `ARKLIGHT_ACCEPT_LICENSE=1` is set. A source checkout installed with `pip install -e .` has a second build-time gate, passed as `--config-settings=yes-i-agree-to-arklight-license=1` or the same environment variable."),
            ("note", "Read `LICENSE` in the [repository](https://github.com/ARKlight-Ecosystem/ARKlight) before setting the flag in anything you plan to distribute."),
        ],
    },
    "/404": {
        "title": "Page not found",
        "description": "That page does not exist on the ARKlight site. Try the home page, getting started or the reference.",
        "lead": "That page is not here.",
        "blocks": [
            ("p", "Try the [home page](/), [getting started](/getting-started) or the [reference](/docs)."),
        ],
    },
}
