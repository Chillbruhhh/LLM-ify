# Changelog

All notable changes to this project are documented in this file.

## [0.1.5] - 2025-12-28

- Added `llmify setup` command plus setup warnings (with optional force env var).
- Added setup messaging in README prerequisites.
- TUI: removed redundant action bar, keep hotkeys line only.

## [0.1.4] - 2025-12-28

- Added per-page docs export into `docs/` with title-based filenames and collisions handled.
- Added `GLOSSARY.md` at the crawl root listing each doc file with title, URL, and description.
- Renamed crawl output folder prefix to `llmify-<domain>` and moved llms outputs into `llms-files/`.
- Removed `txt-output`/`md-output` directories from output layout.
- Added output scope control (all/docs/llms.txt/llms-full.txt/both) and LLMS format control (md/txt/both).
- Added automatic update check with a PyPI prompt.
- TUI tweaks: no auto-focus on boot; Enter focuses URL; hotkeys updated.
- Added Shift+Tab keycode fallback for Windows terminals.
- Added `INSTRUCTIONS.md`, `CONTRIBUTING.md`, and `CHANGELOG.md`, and linked them from `README.md`.
