#!/usr/bin/env bash
# Render the Marp slide sources under course/decks/marp/.
#
#   ./scripts/render_marp.sh              # HTML only (the default; committed to the repo)
#   ./scripts/render_marp.sh --pptx       # PPTX only (not tracked; see below)
#   ./scripts/render_marp.sh --all        # both
#
# HTML is committed because it is text, it is what the site links to, and it is
# self-contained enough to present from directly.
#
# PPTX is NOT committed. Thirty-five exports came to 88 MB against a repo whose
# history was already 279 MB, and every content edit re-committed all of them.
# Run with --pptx locally when you need PowerPoint; the output is gitignored.
#
# Rendering also writes out/.render-manifest.json, recording the SHA-256 of each
# source at render time. scripts/check_deck_freshness.rb compares live sources
# against it in CI, so a source edited without a re-render fails the build.
# Content hashes rather than mtimes, because git does not preserve mtimes --
# which is exactly why 29 of 35 decks went stale without anything noticing.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC_DIR="$ROOT_DIR/course/decks/marp"
OUT_DIR="$SRC_DIR/out"

DO_HTML=1
DO_PPTX=0
case "${1:-}" in
  --pptx) DO_HTML=0; DO_PPTX=1 ;;
  --all)  DO_HTML=1; DO_PPTX=1 ;;
  --html|"") ;;
  *) echo "Usage: $0 [--html|--pptx|--all]" >&2; exit 2 ;;
esac

MARP_BIN=""
if command -v marp >/dev/null 2>&1; then
  MARP_BIN="$(command -v marp)"
elif [ -x "$ROOT_DIR/node_modules/.bin/marp" ]; then
  MARP_BIN="$ROOT_DIR/node_modules/.bin/marp"
elif [ -x "$ROOT_DIR/../node_modules/.bin/marp" ]; then
  MARP_BIN="$ROOT_DIR/../node_modules/.bin/marp"
else
  echo "Error: marp CLI is not installed or not on PATH."
  echo "Install locally (not saved to package.json): npm install --no-save @marp-team/marp-cli"
  echo "Or globally: npm install -g @marp-team/marp-cli"
  exit 1
fi

# PPTX export drives a headless browser. Marp finds Chrome via CHROME_PATH; the
# sandbox flags are required in containers and CI.
if [ "$DO_PPTX" -eq 1 ] && [ -z "${CHROME_PATH:-}" ]; then
  for candidate in \
    /opt/pw-browsers/chromium-*/chrome-linux/chrome \
    /usr/bin/chromium /usr/bin/chromium-browser /usr/bin/google-chrome; do
    if [ -x "$candidate" ]; then export CHROME_PATH="$candidate"; break; fi
  done
fi

mkdir -p "$OUT_DIR"

count=0
while IFS= read -r -d '' file; do
  base="$(basename "$file" .marp.md)"
  rel_dir="$(dirname "${file#"$SRC_DIR"/}")"
  target_dir="$OUT_DIR/$rel_dir"
  mkdir -p "$target_dir"

  if [ "$DO_HTML" -eq 1 ]; then
    "$MARP_BIN" "$file" --html --allow-local-files \
      --output "$target_dir/$base.html" </dev/null

    # Fix image paths for the extra out/ directory level.
    #
    # Deck sources live in course/decks/marp/ and reference images as
    # ../../../assets/... -- correct relative to the SOURCE. Marp copies those
    # paths into the HTML verbatim, but the HTML lands one level deeper, in
    # course/decks/marp/out/, where ../../../assets/ resolves to course/assets/
    # -- which does not exist. Every image in every rendered deck was therefore
    # broken, both as a local file and as served by the site at
    # /course/decks/marp/out/NN.html. Adding one ../ restores the intended
    # target in both contexts. Verified by loading a rendered deck in a browser:
    # 12 of 12 images broken before, 0 after.
    perl -pi -e 's{(src=")((?:\.\./)+)assets/}{$1../$2assets/}g' "$target_dir/$base.html"

    echo "Rendered: $target_dir/$base.html"
  fi

  if [ "$DO_PPTX" -eq 1 ]; then
    "$MARP_BIN" "$file" \
      --pptx \
      --allow-local-files \
      --browser-timeout 120 \
      --browser-arg=--no-sandbox \
      --browser-arg=--disable-setuid-sandbox \
      --output "$target_dir/$base.pptx" </dev/null
    echo "Rendered: $target_dir/$base.pptx"
  fi

  count=$((count + 1))
done < <(find "$SRC_DIR" -type f -name '*.marp.md' -print0 | sort -z)

# Only an HTML render refreshes the manifest: HTML is the committed artifact the
# freshness gate is about. A local --pptx run must not silently mark stale HTML
# as current.
if [ "$DO_HTML" -eq 1 ]; then
  python3 - "$SRC_DIR" "$OUT_DIR" <<'PY'
import hashlib, json, pathlib, sys

src_dir, out_dir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
sources = {}
for path in sorted(src_dir.rglob("*.marp.md")):
    sources[str(path.relative_to(src_dir))] = hashlib.sha256(path.read_bytes()).hexdigest()

manifest = out_dir / ".render-manifest.json"
manifest.write_text(
    json.dumps({"note": "SHA-256 of each Marp source at HTML render time. "
                        "Checked by scripts/check_deck_freshness.rb.",
                "sources": sources}, indent=2) + "\n",
    encoding="utf-8",
)
print(f"Wrote manifest: {manifest} ({len(sources)} sources)")
PY
fi

echo "Done. Processed $count slide decks in $OUT_DIR"
