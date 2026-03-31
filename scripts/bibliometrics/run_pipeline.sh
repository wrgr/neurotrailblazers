#!/usr/bin/env bash
# Connectomics Bibliometric Pipeline — full run
#
# Usage:
#   ./run_pipeline.sh           # Run all steps
#   ./run_pipeline.sh --from 3  # Resume from step 3
#   CORPUS=a ./run_pipeline.sh  # Harvest corpus A only then stop
#
# Outputs land in output/. Cache is in cache/ (gitignored, resumable).
# See PLAN.md for methodology and expected outputs.

set -euo pipefail
cd "$(dirname "$0")"

FROM_STEP="${1:-1}"
[[ "${1:-}" == "--from" ]] && FROM_STEP="${2:-1}"

log() { echo "[$(date '+%H:%M:%S')] $*"; }

# ── 0. Dependencies ───────────────────────────────────────────────────
if ! python3 -c "import networkx, requests" 2>/dev/null; then
    log "Installing dependencies..."
    pip3 install -r requirements.txt -q
fi
mkdir -p output output/graphs cache

# ── 1. Harvest ────────────────────────────────────────────────────────
if [[ "$FROM_STEP" -le 1 ]]; then
    log "Step 1/5: Harvesting papers from OpenAlex..."
    if [[ -n "${CORPUS:-}" ]]; then
        python3 01_harvest.py --corpus "$CORPUS"
    else
        python3 01_harvest.py
    fi
    log "  → output/corpus_merged.json"
fi

# ── 2. Build graphs ───────────────────────────────────────────────────
if [[ "$FROM_STEP" -le 2 ]]; then
    log "Step 2/5: Building citation, co-citation, coupling, co-authorship graphs..."
    python3 02_build_graphs.py
    log "  → output/graphs/*.json"
fi

# ── 3. Compute metrics ────────────────────────────────────────────────
if [[ "$FROM_STEP" -le 3 ]]; then
    log "Step 3/5: Computing PageRank, HITS, betweenness, community detection..."
    python3 03_compute_metrics.py
    log "  → output/paper_rankings.json, author_rankings.json, communities.json"
fi

# ── 4. Validate ───────────────────────────────────────────────────────
if [[ "$FROM_STEP" -le 4 ]]; then
    log "Step 4/5: Validating against expert-curated list..."
    python3 04_validate.py
    log "  → output/validation_report.md"
fi

# ── 5. HTML report ────────────────────────────────────────────────────
if [[ "$FROM_STEP" -le 5 ]]; then
    log "Step 5/5: Generating interactive field map..."
    python3 05_html_report.py
    log "  → output/field_map.html"
fi

log "Done. Open output/field_map.html in a browser to explore the field map."
