#!/usr/bin/env python3
"""Merge verdicts from all 20 batches into classification_v4.json.

Validates schema, checks completeness across all 10,575 papers, and reports
category and organism distribution metrics.
"""
import glob
import json
import sys
from collections import Counter
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CBATCHES_DIR = SCRIPT_DIR / "cbatches"
OUTPUT_FILE = SCRIPT_DIR / "classification_v4.json"

def main():
    verdict_files = sorted(CBATCHES_DIR.glob("cverdict_*.json"))
    if len(verdict_files) != 20:
        print(f"Error: expected 20 verdict files, found {len(verdict_files)}", file=sys.stderr)
        sys.exit(1)

    merged = {}
    total_tsv_dois = []
    
    # Read expected DOIs from TSVs
    for tsv_file in sorted(CBATCHES_DIR.glob("cbatch_*.tsv")):
        for line in tsv_file.read_text().splitlines():
            if line.strip():
                doi = line.split("\t")[0].strip()
                total_tsv_dois.append(doi)

    print(f"Total DOIs expected from 20 batch TSVs: {len(total_tsv_dois)}")

    # Merge verdict files
    for vf in verdict_files:
        data = json.loads(vf.read_text())
        for doi, rec in data.items():
            if doi in merged:
                print(f"Warning: Duplicate DOI {doi} found across verdict files!", file=sys.stderr)
            # Schema validation
            assert "classification" in rec, f"Missing classification for {doi} in {vf.name}"
            assert "subclassification" in rec, f"Missing subclassification for {doi} in {vf.name}"
            assert "secondary_classifications" in rec, f"Missing secondary_classifications for {doi} in {vf.name}"
            assert "organism" in rec, f"Missing organism for {doi} in {vf.name}"
            merged[doi] = rec

    print(f"Total merged records: {len(merged)}")
    missing = set(total_tsv_dois) - set(merged.keys())
    extra = set(merged.keys()) - set(total_tsv_dois)
    if missing:
        print(f"Error: {len(missing)} DOIs missing from merged verdicts: {list(missing)[:5]}", file=sys.stderr)
        sys.exit(1)
    if extra:
        print(f"Error: {len(extra)} unexpected DOIs in merged verdicts: {list(extra)[:5]}", file=sys.stderr)
        sys.exit(1)

    OUTPUT_FILE.write_text(json.dumps(merged, indent=1, ensure_ascii=False))
    print(f"Successfully wrote {len(merged)} records to {OUTPUT_FILE} ({OUTPUT_FILE.stat().st_size / 1024 / 1024:.2f} MB)")

    # Print summary metrics
    cat_counts = Counter(r["classification"] for r in merged.values())
    print("\n--- Final Classification Breakdown ---")
    for cat, count in cat_counts.most_common():
        pct = count / len(merged) * 100
        print(f"  {cat:22s}: {count:5d} ({pct:4.1f}%)")

    org_counts = Counter()
    for r in merged.values():
        for o in r.get("organism", []):
            org_counts[o] += 1
    print("\n--- Organism Breakdown ---")
    for org, count in org_counts.most_common():
        pct = count / len(merged) * 100
        print(f"  {org:22s}: {count:5d} ({pct:4.1f}%)")

if __name__ == "__main__":
    main()
