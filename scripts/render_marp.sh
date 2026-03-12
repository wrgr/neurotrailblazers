#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC_DIR="$ROOT_DIR/course/decks/marp"
OUT_DIR="$ROOT_DIR/course/decks/marp/out"

MARP_BIN=""
if command -v marp >/dev/null 2>&1; then
  MARP_BIN="$(command -v marp)"
elif [ -x "$ROOT_DIR/node_modules/.bin/marp" ]; then
  MARP_BIN="$ROOT_DIR/node_modules/.bin/marp"
elif [ -x "$ROOT_DIR/../node_modules/.bin/marp" ]; then
  MARP_BIN="$ROOT_DIR/../node_modules/.bin/marp"
else
  echo "Error: marp CLI is not installed or not on PATH."
  echo "Install globally: npm install -g @marp-team/marp-cli"
  echo "Or local (workspace): npm install --no-save @marp-team/marp-cli"
  exit 1
fi

mkdir -p "$OUT_DIR"

count=0
while IFS= read -r -d '' file; do
  base="$(basename "$file" .marp.md)"
  rel_dir="$(dirname "${file#$SRC_DIR/}")"
  target_dir="$OUT_DIR/$rel_dir"
  mkdir -p "$target_dir"
  "$MARP_BIN" "$file" --html --allow-local-files --output "$target_dir/$base.html" </dev/null
  count=$((count + 1))
  echo "Rendered: $target_dir/$base.html"
done < <(find "$SRC_DIR" -type f -name '*.marp.md' -print0)

echo "Done. Rendered $count slide decks to $OUT_DIR"
