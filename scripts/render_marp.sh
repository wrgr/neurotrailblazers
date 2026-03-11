#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC_DIR="$ROOT_DIR/course/decks/marp"
OUT_DIR="$ROOT_DIR/course/decks/marp/out"

if ! command -v marp >/dev/null 2>&1; then
  echo "Error: marp CLI is not installed or not on PATH."
  echo "Install: npm install -g @marp-team/marp-cli"
  exit 1
fi

mkdir -p "$OUT_DIR"

count=0
for file in "$SRC_DIR"/*.marp.md; do
  [ -e "$file" ] || continue
  base="$(basename "$file" .marp.md)"
  marp "$file" --html --allow-local-files --output "$OUT_DIR/$base.html"
  count=$((count + 1))
  echo "Rendered: $OUT_DIR/$base.html"
done

echo "Done. Rendered $count slide decks to $OUT_DIR"
