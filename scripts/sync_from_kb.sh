#!/bin/bash
# Sync connectome-kb website outputs into neurotrailblazers assets.
# Run from the neurotrailblazers repo root.
#
# Usage:
#   bash scripts/sync_from_kb.sh
#   KB_OUTPUTS_PATH=/custom/path bash scripts/sync_from_kb.sh

set -e

KB_DIR="${KB_OUTPUTS_PATH:-../connectome-kb/outputs/website}"
NT_ASSETS="assets/analysis"

if [ ! -d "$KB_DIR" ]; then
    echo "Error: KB outputs not found at $KB_DIR"
    echo "Run the connectome-kb pipeline first, or set KB_OUTPUTS_PATH."
    exit 1
fi

mkdir -p "$NT_ASSETS/graphs"

cp "$KB_DIR/graphs/citation_graph.json" "$NT_ASSETS/graphs/"
cp "$KB_DIR/graphs/cocitation_graph.json" "$NT_ASSETS/graphs/"
cp "$KB_DIR/graphs/coupling_graph.json" "$NT_ASSETS/graphs/"
cp "$KB_DIR/graphs/coauthorship_graph.json" "$NT_ASSETS/graphs/"

cp "$KB_DIR/paper_rankings.json" "$NT_ASSETS/"
cp "$KB_DIR/author_rankings.json" "$NT_ASSETS/"
cp "$KB_DIR/communities.json" "$NT_ASSETS/"
cp "$KB_DIR/lineage_data.json" "$NT_ASSETS/"

echo "Synced KB outputs from $KB_DIR → $NT_ASSETS"
echo "  $(ls "$NT_ASSETS/graphs/" | wc -l) graph files"
echo "  $(ls "$NT_ASSETS"/*.json | wc -l) ranking/metadata files"
