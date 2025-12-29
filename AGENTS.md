# Repository Guidelines

## Project Structure & Module Organization

- `src/llmify/`: Primary package (CLI entry points and `generate_llmstxt.py` core logic).
- `src/generate-llmstxt.py`: Script entry for direct CLI usage.
- `main.py`: Terminal UI launcher.
- `scripts/`: Quickstart helpers (`quickstart.ps1`, `quickstart.sh`) for venv + setup.
- `collected-texts/`: Generated output (domain-scoped crawl folders).
- `Public/assets/`: Static assets (project image).
- `dist/`: Build artifacts (wheel/tarball); treat as generated.

## Build, Test, and Development Commands

- `python -m venv venv` and `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux): create/activate venv.
- `pip install -r requirements.txt`: install runtime dependencies for local development.
- `crawl4ai-setup`: install Crawl4AI browser dependencies.
- `python main.py`: launch the TUI for interactive runs.
- `python src/generate-llmstxt.py https://example.com --discovery-method auto`: run the direct generator.
- `scripts\quickstart.ps1` or `./scripts/quickstart.sh`: one-shot setup + TUI launch.

## Coding Style & Naming Conventions

- Python with 4-space indentation; follow existing patterns in `src/llmify/`.
- Use `snake_case` for modules/functions, `PascalCase` for classes.
- Keep CLI flags kebab/long-form (see `--discovery-method`, `--max-urls`).
- Avoid committing generated outputs or secrets; use `.env` (see `.env.example`).

## Testing Guidelines

- No automated test suite is present. Use manual smoke checks:
  - TUI: `python main.py`
  - CLI: `python src/generate-llmstxt.py https://example.com --max-urls 5`
- If adding tests, place them under `tests/` and keep names `test_*.py`.

## Commit & Pull Request Guidelines

- Commit history uses short, plain summaries (e.g., “updated readme”, “added pypi install”).
- Prefer concise, lowercase subject lines without prefixes.
- PRs should include: purpose, key changes, how to run/verify, and any config changes.
- Include screenshots for TUI/UX changes when relevant.

## Security & Configuration Tips

- API keys are read from `--openai-api-key`, `.env`, or environment variables.
- Never commit `.env`; update `.env.example` if you introduce new settings.
