#!/usr/bin/env bash
set -euo pipefail

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Running Crawl4AI setup..."
crawl4ai-setup

echo "Done. Launching TUI..."
python main.py
