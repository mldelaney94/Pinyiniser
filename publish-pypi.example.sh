#!/usr/bin/env bash
set -euo pipefail

# Personal publish helper (gitignored). Configure once, then run:
#   ./publish-pypi.sh

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

export TWINE_USERNAME=__token__
export TWINE_PASSWORD='pypi-YOUR_TOKEN_HERE'

if [[ -z "${TWINE_USERNAME:-}" || -z "${TWINE_PASSWORD:-}" ]]; then
  echo "Set TWINE_USERNAME and TWINE_PASSWORD in this script before publishing." >&2
  exit 1
fi

VERSION="$(grep '^version = ' setup.cfg | cut -d' ' -f3)"
echo "Publishing pinyiniser ${VERSION} to PyPI..."

if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi

.venv/bin/pip install -q --upgrade pip build twine
rm -rf dist build
.venv/bin/python -m build
.venv/bin/twine check dist/*
.venv/bin/twine upload dist/*

echo "Published pinyiniser ${VERSION} to https://pypi.org/project/pinyiniser/"
