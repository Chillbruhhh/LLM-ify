#!/usr/bin/env python3
"""Entry point that launches the TUI by default."""

import os
import runpy
import sys


def main() -> None:
    script_path = os.path.join(os.path.dirname(__file__), "src", "generate-llmstxt.py")
    if "--interactive" not in sys.argv:
        sys.argv.insert(1, "--interactive")
    runpy.run_path(script_path, run_name="__main__")


if __name__ == "__main__":
    main()
