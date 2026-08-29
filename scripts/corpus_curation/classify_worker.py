#!/usr/bin/env python3
"""Batch classification worker for NeuroTrailblazers corpus curation.

Usage:
  python3 scripts/corpus_curation/classify_worker.py --batch 0 --input scripts/corpus_curation/cbatches/cbatch_00.tsv --output scripts/corpus_curation/cbatches/cverdict_00.json
  python3 scripts/corpus_curation/classify_worker.py --all
"""
import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any

# Ensure project root is in sys.path
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from classify_engine import classify_paper

def process_batch(tsv_path: Path, out_path: Path) -> Dict[str, Any]:
    lines = tsv_path.read_text().splitlines()
    verdicts = {}
    for line in lines:
        if not line.strip():
            continue
        parts = line.split("\t")
        doi = parts[0].strip()
        title = parts[1].strip() if len(parts) > 1 else ""
        venue = parts[2].strip() if len(parts) > 2 else ""
        abstract = parts[3].strip() if len(parts) > 3 else ""
        
        rec = classify_paper(doi, title, venue, abstract)
        verdicts[doi] = rec
        
    out_path.write_text(json.dumps(verdicts, indent=1, ensure_ascii=False))
    print(f"Processed {len(verdicts)} papers from {tsv_path.name} -> {out_path.name}")
    return verdicts

def main():
    parser = argparse.ArgumentParser(description="Classify corpus batches.")
    parser.add_argument("--batch", type=int, help="Batch index (0-19)")
    parser.add_argument("--input", type=str, help="Input TSV path")
    parser.add_argument("--output", type=str, help="Output JSON path")
    parser.add_argument("--rules", type=str, help="Rules markdown path (reference)")
    parser.add_argument("--all", action="store_true", help="Process all missing batches")
    parser.add_argument("--force", action="store_true", help="Overwrite existing completed batches")
    args = parser.parse_args()

    cbatches_dir = SCRIPT_DIR / "cbatches"

    if args.all:
        for i in range(20):
            b_str = f"{i:02d}"
            tsv_path = cbatches_dir / f"cbatch_{b_str}.tsv"
            out_path = cbatches_dir / f"cverdict_{b_str}.json"
            if not tsv_path.exists():
                continue
            if out_path.exists() and not args.force and b_str in ("03", "11", "15"):
                print(f"Skipping pre-existing ground truth batch {b_str}")
                continue
            process_batch(tsv_path, out_path)
    elif args.batch is not None:
        b_str = f"{args.batch:02d}"
        tsv_path = Path(args.input) if args.input else (cbatches_dir / f"cbatch_{b_str}.tsv")
        out_path = Path(args.output) if args.output else (cbatches_dir / f"cverdict_{b_str}.json")
        process_batch(tsv_path, out_path)
    elif args.input and args.output:
        process_batch(Path(args.input), Path(args.output))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
