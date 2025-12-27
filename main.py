#!/usr/bin/env python3
"""Entry point that launches the TUI by default."""

import os
import runpy
import sys


def main() -> None:
    if "--interactive" not in sys.argv:
        sys.argv.insert(1, "--interactive")
    repo_root = os.path.dirname(__file__)
    src_path = os.path.join(repo_root, "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
    runpy.run_module("llmify.generate_llmstxt", run_name="__main__")


if __name__ == "__main__":
    main()
