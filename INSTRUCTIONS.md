# Repository Agent Instructions

These instructions are intended to be copied into agent-specific files
(for example `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`) so automated assistants
know how to navigate scraped documentation in this repository.

## How to Navigate Scraped Docs

1. Start with the glossary:
   - Read `collected-texts/llmify-<domain>/GLOSSARY.md` first.
   - Use it to map topics/functions to the exact markdown files in `docs/`.
2. Open only the relevant doc file(s):
   - Each page is stored as a standalone markdown file under
     `collected-texts/llmify-<domain>/docs/`.
3. Use llms outputs for summaries or cross-checks:
   - `collected-texts/llmify-<domain>/llms-files/llms.md`
   - `collected-texts/llmify-<domain>/llms-files/llms-full.md`
4. Prefer minimal context:
   - Don’t load every doc file at once.
   - Select a small set of relevant docs based on the glossary first.

## Expected Output Structure

- `GLOSSARY.md`: overview of all doc files, titles, URLs, and short descriptions.
- `docs/`: one markdown file per page (title-based filename).
- `llms-files/`: llms index/full corpus in markdown or text depending on settings.
