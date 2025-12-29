# Contributing to LLM-ify

Thanks for helping improve LLM-ify! This guide explains the workflow and expectations for contributions.

## Getting Started

1. Fork and clone the repo.
2. Create and activate a virtual environment:
   - Windows: `python -m venv venv` then `venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv venv` then `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run setup: `crawl4ai-setup`

## Development Workflow

- Run the TUI: `python main.py`
- Direct CLI: `python src/generate-llmstxt.py https://example.com --max-urls 5`
- Output is written under `collected-texts/llmify-<domain>/`.

## Coding Style

- Python, 4-space indentation.
- Follow existing naming: `snake_case` for functions/modules, `PascalCase` for classes.
- Keep CLI flags long-form and consistent (e.g., `--discovery-method`, `--llms-output`).

## Testing

There is no automated test suite yet. Please run at least one manual check:

- TUI smoke test: `python main.py`
- CLI smoke test: `python src/generate-llmstxt.py https://example.com --max-urls 3`

If you add a test suite, place files under `tests/` and name them `test_*.py`.

## Pull Requests

- Keep changes focused and explain the “why.”
- Include steps to verify (commands and expected output).
- Add screenshots for any TUI/UX changes.
- Avoid committing generated output (`collected-texts/`) or secrets (`.env`).

## Versioning

- Update the version in `pyproject.toml` and `src/llmify/__init__.py` when releasing.
- Add release notes to `CHANGELOG.md`.
- Rebuild artifacts with `python -m build` before publishing.
