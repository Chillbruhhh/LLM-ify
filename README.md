# LLM-ify

LLM-ify generates `llms.txt` and `llms-full.txt` plus full markdown/text captures for single pages or entire websites, so your LLM has clean, readable context.

## What is llms.txt?

`llms.txt` is a standardized format for making website content more accessible to Large Language Models (LLMs). It provides:

- `llms.txt`: A concise index of all pages with titles and descriptions
- `llms-full.txt`: Complete content of all pages for comprehensive access

## Features

- Crawl4AI-based crawling (open-source, local)
- Smart URL discovery:
  - Sitemap discovery via sitemap.xml
  - Link crawling for scoped paths (for example `/docs/api/`)
  - Auto mode (default): try sitemap first, then merge with link crawling for scoped URLs
- Path-scoped crawling: target a section like `example.com/docs/`
- Content scraping: extract markdown from each page
- AI summaries: OpenAI `gpt-4.1-nano` generates concise titles and descriptions
- Parallel processing: Crawl4AI runs multiple URLs concurrently (configurable)
- Configurable limits: max URLs and concurrency caps
- Flexible output: generate both files or `llms.txt` only
- Single-page mode for one-off page captures
- Interactive terminal UI for guided runs

## Prerequisites

- Python 3.7+
- OpenAI API key ([Get one here](https://platform.openai.com))
- Crawl4AI setup (see installation)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Chillbruhhh/LLM-ify.git
cd LLM-ify
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the setup command:

```bash
crawl4ai-setup
```

This installs browser dependencies needed for Crawl4AI.

4. Set up your OpenAI API key:

   Option A: Using .env file (recommended)

   ```bash
   cp .env.example .env
   # Edit .env and configure:
   # - Add OPENAI_API_KEY (required)
   ```

   Option B: Using environment variables

   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   ```

   Option C: Using command line arguments
   (See usage examples below)

## URL Discovery Methods

When using Crawl4AI, you can choose how to discover URLs:

### Auto Discovery (Default)

Automatically tries the best method - starts with sitemap, merges in link crawling for scoped URLs:

```bash
python generate-llmstxt.py https://example.com/docs/
# Uses auto discovery by default
```

When to use: always. This is the default and works well for most cases.
Note: seed URLs are deduped using a normalized form that drops query strings/fragments, collapses `/index.html` to `/`, and prefers `.md` when both `.md` and `.html` exist. Scraped pages are also deduped by content hash after scraping, and output is sorted by path for stability.

### Sitemap Discovery

Fast discovery using the website's sitemap.xml:

```bash
python generate-llmstxt.py https://example.com --discovery-method sitemap
```

When to use:
- When crawling entire domains
- When the site has a comprehensive sitemap
- Not ideal for specific subdirectories (e.g., `/docs/api/`)

### Link Crawling Discovery

Crawls pages and extracts links, perfect for specific paths:

```bash
# Crawl a specific section of a website
python generate-llmstxt.py https://learn.microsoft.com/en-us/graph/ --discovery-method crawl

# Control crawl depth (how many link levels to follow)
python generate-llmstxt.py https://example.com/docs/ --discovery-method crawl --crawl-depth 2
```

When to use:
- When targeting specific subdirectories (`/docs/`, `/api/`, `/blog/`)
- When sitemap includes URLs you don't want (other languages, sections)
- For sites without sitemaps

Crawl depth options:
- `--crawl-depth 1`: Only the base page (fast, minimal URLs)
- `--crawl-depth 2`: Base page + pages it links to (default, balanced)
- `--crawl-depth 3`: Go deeper (slower, comprehensive)

### Real-World Examples

```bash
# Crawl only Microsoft Graph API docs (not all of learn.microsoft.com)
python generate-llmstxt.py https://learn.microsoft.com/en-us/graph/ \
  --discovery-method crawl \
  --crawl-depth 2 \
  --max-urls 50

# Crawl specific documentation section
python generate-llmstxt.py https://docs.example.com/api/v2/ \
  --discovery-method crawl \
  --max-urls 100

# Let auto mode decide (recommended)
python generate-llmstxt.py https://example.com/docs/ \
  --max-urls 50
```

## Usage

### Basic Usage

Generate llms.txt and llms-full.txt for a website:

```bash
python generate-llmstxt.py https://example.com
```

### With Options

```bash
# Limit to 50 URLs
python generate-llmstxt.py https://example.com --max-urls 50

# Control parallel crawling
python generate-llmstxt.py https://example.com --max-concurrent 20

# Fast crawling with high concurrency
python generate-llmstxt.py https://example.com --max-urls 100 --max-concurrent 15

# Save to specific directory
python generate-llmstxt.py https://example.com --output-dir ./output

# Only generate llms.txt (skip full text)
python generate-llmstxt.py https://example.com --no-full-text

# Enable verbose logging
python generate-llmstxt.py https://example.com --verbose

# Specify API key via command line
python generate-llmstxt.py https://example.com --openai-api-key "sk-..."
```

### Interactive Mode

```bash
python generate-llmstxt.py --interactive
```

The interactive UI uses a curses-based full-screen panel with collapsible crawl/seeding sections. Use Tab/Shift+Tab to cycle discovery mode. On Windows, install `windows-curses` if you see a curses import error.

### Single Page

```bash
python generate-llmstxt.py https://example.com/docs/getting-started --single-page
```

This writes the page content into `txt-output/<page-title>.txt` and `md-output/<page-title>.md`, with the filename derived from the first markdown heading when available.

### Command Line Options

General options:
- `url` (required): The website URL to process
- `--max-urls`: Maximum number of URLs to process (default: no limit)
- `--output-dir`: Base directory to save output files (default: collected-texts)
- `--openai-api-key`: OpenAI API key (required, defaults to .env or OPENAI_API_KEY env var)
- `--no-full-text`: Only generate llms.txt, skip llms-full.txt
- `--verbose`: Enable verbose logging for debugging
- `--single-page`: Scrape only the provided URL and save it as a standalone file
- `--llms-list-all-urls`: Include all discovered URLs in llms.txt even if content duplicates are removed
- `--interactive`: Launch the guided terminal UI

Crawl4AI URL discovery options:
- `--discovery-method`: How to discover URLs: 'auto' (default), 'sitemap', or 'crawl'
  - `auto`: Try sitemap first, merge with link crawling for scoped URLs
  - `sitemap`: Use website's sitemap.xml
  - `crawl`: Crawl pages and extract links
- `--crawl-depth`: Maximum link depth for 'crawl' method (default: 2)
- `--max-concurrent`: Maximum concurrent crawlers for crawl4ai (default: 10 or from MAX_CONCURRENT_CRAWLERS env var)

Crawl4AI advanced seeding options:
- `--seed-source`: Seeding source: 'sitemap', 'cc', or 'sitemap+cc' (default: sitemap+cc)
- `--seed-query`: BM25 query to score and filter seed URLs
- `--seed-scoring-method`: Override scoring method used by Crawl4AI when seeding
- `--seed-score-threshold`: Minimum relevance score for seed URLs
- `--seed-live-check`: Verify URLs are live before crawling
- `--seed-no-live-check`: Disable live URL verification
- `--seed-head`: Enable <head> extraction during seeding
- `--seed-no-head`: Disable <head> extraction during seeding
- `--seed-filter-nonsense`: Keep Crawl4AI nonsense URL filtering (default)
- `--seed-allow-nonsense`: Disable nonsense URL filtering
- `--seed-include-pattern`: Glob pattern to retain matching seed URLs (repeatable)
- `--seed-exclude-pattern`: Glob pattern to drop seed URLs (repeatable)

## Output Format

### llms.txt

```
# https://example.com llms.txt

- [Page Title](https://example.com/page1): Brief description of the page content here
- [Another Page](https://example.com/page2): Another concise description of page content
```

### llms-full.txt

```
# https://example.com llms-full.txt

<|llm-ify-page-1-lllmstxt|>
## Page Title
Full markdown content of the page...

<|llm-ify-page-2-lllmstxt|>
## Another Page
Full markdown content of another page...
```

## How It Works

### With Crawl4AI
1. URL discovery (auto mode by default):
   - Sitemap: uses Crawl4AI's `AsyncUrlSeeder`
   - Link crawling: uses `AsyncWebCrawler`
   - Auto: sitemap first, merge with link crawling for scoped URLs
2. Seeding controls (optional): use `SEED_*` env vars or CLI flags to score/filter seeds, apply include/exclude patterns, or check URL liveness.
3. Parallel processing: uses `asyncio.gather()` with a semaphore (default: 10 concurrent crawlers)
4. Content extraction: uses `AsyncWebCrawler` to extract markdown content
5. AI summarization: `gpt-4.1-nano` generates:
   - A 3-4 word title
   - A 9-10 word description
6. File generation: writes `llms.txt`, `llms-full.txt`, and `seeds.json` when available

## Error Handling

- Failed URL scrapes are logged and skipped
- If no URLs are found, the script exits with an error
- API errors are logged with details for debugging

## Performance Considerations

### Crawl4AI (Parallel Processing)
- Concurrent crawling: default 10 simultaneous browser instances (configurable via `--max-concurrent`)
- Recommended settings:
  - Small sites (< 50 pages): `--max-concurrent 5`
  - Medium sites (50-200 pages): `--max-concurrent 10` (default)
  - Large sites (200+ pages): `--max-concurrent 15-20`
- System resources: each browser instance uses ~100-200MB RAM
- Speed: processes multiple URLs in parallel vs one at a time

## Examples

### Small Website

```bash
python generate-llmstxt.py https://small-blog.com --max-urls 20
```

### Specific Documentation Section

```bash
# Crawl only the Graph API docs from Microsoft Learn
python generate-llmstxt.py https://learn.microsoft.com/en-us/graph/ \
  --discovery-method crawl \
  --crawl-depth 2 \
  --max-urls 50 \
  --verbose

# Crawl specific API documentation
python generate-llmstxt.py https://docs.stripe.com/api/ \
  --max-urls 100
```

### Large Website with Limited Scope

```bash
python generate-llmstxt.py https://docs.example.com --max-urls 100 --verbose
```

### Quick Index Only

```bash
python generate-llmstxt.py https://example.com --no-full-text --max-urls 50
```

### Fast Crawling with High Concurrency

```bash
# Crawl multiple pages simultaneously
python generate-llmstxt.py https://example.com/docs/ \
  --max-concurrent 20 \
  --max-urls 200
```

## Configuration Priority

The script checks for configuration in this order:

API keys:
1. Command line argument (`--openai-api-key`)
2. `.env` file in the current directory
3. Environment variable (`OPENAI_API_KEY`)

## Troubleshooting

### No API Keys Found

Ensure you've either:

- Created a `.env` file with your API keys (copy from `env.example`)
- Set environment variables: `OPENAI_API_KEY`
- Or pass it via command line arguments

### Memory Issues

For very large websites:

- Use `--max-urls` to limit the number of pages
- Process in smaller batches
- Use `--no-full-text` to skip full content generation

## Output Filenames

Output files are written under `collected-texts/crawl4ai-<domain>/` by default and split into `txt-output` and `md-output` folders. Example:

```
collected-texts/crawl4ai-docs.example.com/txt-output/llms.txt
collected-texts/crawl4ai-docs.example.com/txt-output/llms-full.txt
collected-texts/crawl4ai-docs.example.com/md-output/llms.md
collected-texts/crawl4ai-docs.example.com/md-output/llms-full.md
collected-texts/crawl4ai-docs.example.com/seeds.json
```

## License

MIT License - see LICENSE file for details
