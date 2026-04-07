#!/usr/bin/env bash
# Sync connectome-kb website outputs into neurotrailblazers assets.
# Run from the neurotrailblazers repo root.
#
# Usage:
#   bash scripts/sync_from_kb.sh
#   KB_OUTPUTS_PATH=/custom/path bash scripts/sync_from_kb.sh
#   KB_REPO_DIR=~/projects/connectome-kb bash scripts/sync_from_kb.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

KB_REPO_DIR="${KB_REPO_DIR:-$NT_ROOT/../connectome-kb}"
KB_PUBLISH_SCRIPT="$KB_REPO_DIR/scripts/publish_website_bundle.sh"
KB_DIR="${KB_OUTPUTS_PATH:-$KB_REPO_DIR/outputs/website}"

NT_BIB_DIR="${NT_BIB_ASSETS:-$NT_ROOT/assets/bibliometrics}"
NT_ANALYSIS_DIR="${NT_ANALYSIS_ASSETS:-$NT_ROOT/assets/analysis}"

# Prefer connectome-kb's canonical publisher if present.
if [[ -x "$KB_PUBLISH_SCRIPT" ]]; then
    NT_REPO_DIR="$NT_ROOT" bash "$KB_PUBLISH_SCRIPT"
    exit 0
fi

required_files=(
  "graphs/citation_graph.json"
  "graphs/cocitation_graph.json"
  "graphs/coupling_graph.json"
  "graphs/coauthorship_graph.json"
  "paper_rankings.json"
  "author_rankings.json"
  "communities.json"
  "lineage_data.json"
  "corpus_canonical.json"
)

optional_files=(
  "strategic_audit.json"
  "strategic_audit.md"
)

if [[ ! -d "$KB_DIR" ]]; then
    echo "Error: KB outputs not found at $KB_DIR"
    echo "Run the connectome-kb pipeline first, or set KB_OUTPUTS_PATH."
    exit 1
fi

for rel in "${required_files[@]}"; do
    if [[ ! -f "$KB_DIR/$rel" ]]; then
        echo "Error: missing required file: $KB_DIR/$rel"
        exit 1
    fi
done

mkdir -p "$NT_BIB_DIR/graphs" "$NT_ANALYSIS_DIR/graphs"

for rel in "${required_files[@]}"; do
    mkdir -p "$(dirname "$NT_BIB_DIR/$rel")"
    cp "$KB_DIR/$rel" "$NT_BIB_DIR/$rel"

    # Compatibility mirror for existing /assets/analysis pages.
    mkdir -p "$(dirname "$NT_ANALYSIS_DIR/$rel")"
    cp "$KB_DIR/$rel" "$NT_ANALYSIS_DIR/$rel"
done

for rel in "${optional_files[@]}"; do
    if [[ ! -f "$KB_DIR/$rel" ]]; then
        continue
    fi
    mkdir -p "$(dirname "$NT_BIB_DIR/$rel")"
    cp "$KB_DIR/$rel" "$NT_BIB_DIR/$rel"
    mkdir -p "$(dirname "$NT_ANALYSIS_DIR/$rel")"
    cp "$KB_DIR/$rel" "$NT_ANALYSIS_DIR/$rel"
done

if [[ -f "$KB_DIR/manifest.json" ]]; then
    cp "$KB_DIR/manifest.json" "$NT_BIB_DIR/manifest.json"
    cp "$KB_DIR/manifest.json" "$NT_ANALYSIS_DIR/manifest.json"
fi

echo "Synced KB outputs from $KB_DIR"
echo "  canonical target: $NT_BIB_DIR"
echo "  compatibility mirror: $NT_ANALYSIS_DIR"
echo "  files: ${#required_files[@]} required artifacts + ${#optional_files[@]} optional (+ manifest if present)"
