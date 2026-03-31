#!/bin/bash
set -e

echo "Regenerating pipeline with clean corpus..."

# Use corpus_final.json instead of corpus_merged.json
cp output/corpus_final.json output/corpus_merged.json

echo "Step 1: Rebuild graphs with clean corpus..."
python3 02_build_graphs.py

echo "Step 2: Recompute metrics..."
python3 03_compute_metrics.py

echo "Step 3: Regenerate HTML report..."
python3 05_html_report.py --max-nodes 500

echo "Step 4: Regenerate k-core visualization..."
python3 06b_kcore_visualization.py

echo "Step 5: Regenerate reading list..."
python3 06_reading_list.py --top 500

echo "Step 6: Regenerate journal club selection..."
python3 08b_generate_journal_club_strict.py

echo "All downstream analysis regenerated!"
