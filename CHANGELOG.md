# Changelog

All notable changes to this project are documented in this file.

## [0.1.4] - 2025-12-28

- Added per-page docs export into `docs/` with title-based filenames and collisions handled.
- Added `GLOSSARY.md` at the crawl root listing each doc file with title, URL, and description.
- Renamed crawl output folder prefix to `llmify-<domain>`.
- Added scope control (all/docs/llms.txt/llms-full.txt/both) with Shift+Tab and UI display.
- Added LLMS output format control (md/txt/both), defaulting to markdown.
- Moved llms outputs into `llms-files/` and removed `txt-output`/`md-output`.
- TUI tweaks: no auto-focus on boot; Enter focuses URL; hotkeys updated.
- Added Shift+Tab keycode fallback for Windows terminals.
- Added automatic update check with a PyPI prompt.
- Added `INSTRUCTIONS.md` and `CONTRIBUTING.md`, and linked them from `README.md`.
