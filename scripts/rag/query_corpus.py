#!/usr/bin/env python3
"""
Interactive Research Q&A & Literature Synthesis Engine for Connectomics.
Queries the local RAG SQLite index using hybrid section-aware scoring,
returns grounded academic excerpts with full citations and license terms,
and generates structured synthesis prompts for Gemini, Claude, and ChatGPT.
"""

import argparse
import json
import math
import os
import re
import sqlite3
import sys
from pathlib import Path
from typing import Dict, Any, List, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
DB_PATH = PROJECT_ROOT / "data" / "rag_index" / "connectomics_rag.sqlite"


def tokenize(text: str) -> List[str]:
    return [w.lower() for w in re.findall(r'\b[a-zA-Z0-9_\-\.]{3,}\b', text) if len(w) > 2]


def search_rag(query_str: str, top_k: int = 5, section_filter: str = None) -> List[Dict[str, Any]]:
    if not DB_PATH.exists():
        print(f"Error: Database {DB_PATH} not found. Please run build_vector_index.py first.")
        return []

    tokens = tokenize(query_str)
    if not tokens:
        return []

    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()

    # Build SQL keyword match query
    conditions = []
    params = []
    for tok in tokens[:8]:
        conditions.append("c.text_content LIKE ?")
        params.append(f"%{tok}%")

    sec_clause = ""
    if section_filter:
        sec_clause = "AND c.section = ?"
        params.append(section_filter)

    sql = f"""
        SELECT 
            c.chunk_id, c.doi, c.section, c.text_content,
            d.title, d.authors, d.year, d.journal, d.dimension, d.organism, d.tier,
            d.license_type, d.redistribution_permitted, d.storage_location,
            d.segmentation_approaches, d.imaging_modalities, d.validation_metrics
        FROM chunks c
        JOIN documents d ON c.doi = d.doi
        WHERE ({" OR ".join(conditions)}) {sec_clause}
        LIMIT 200
    """

    rows = c.execute(sql, params).fetchall()
    conn.close()

    # Rank rows by token overlap frequency & tier bonus
    scored_results = []
    for r in rows:
        text = r[3].lower()
        score = 0
        for tok in tokens:
            count = text.count(tok)
            if count > 0:
                score += 1.0 + math.log(1 + count)

        # Boost core flagship & landmark papers
        tier = r[10] or 2000
        if tier == 500:
            score *= 1.3
        elif tier == 1000:
            score *= 1.15

        scored_results.append((score, {
            "chunk_id": r[0],
            "doi": r[1],
            "section": r[2],
            "text": r[3],
            "title": r[4],
            "authors": r[5],
            "year": r[6],
            "journal": r[7],
            "dimension": r[8],
            "organism": json.loads(r[9]) if r[9] else [],
            "tier": r[10],
            "license_type": r[11],
            "redistribution_permitted": bool(r[12]),
            "storage_location": r[13],
            "segmentation_approaches": json.loads(r[14]) if r[14] else [],
            "imaging_modalities": json.loads(r[15]) if r[15] else [],
            "validation_metrics": json.loads(r[16]) if r[16] else []
        }))

    scored_results.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in scored_results[:top_k]]


def format_cli_output(results: List[Dict[str, Any]], query: str, compare_seg: bool = False):
    print("=" * 80)
    print(f"CONNECTOMICS RAG QUERY RESULTS: \"{query}\"")
    print("=" * 80)

    if not results:
        print("No matching literature excerpts found in the local index.")
        return

    for i, res in enumerate(results, 1):
        redist_str = "✅ Open (CC-BY)" if res["redistribution_permitted"] else "🔒 Private / Research Index"
        seg_str = ", ".join(res.get("segmentation_approaches", [])) or "General"
        mod_str = ", ".join(res.get("imaging_modalities", [])) or "Volume EM"

        print(f"\n[{i}] {res['title']} ({res['year']})")
        print(f"    Authors: {res['authors']} | Journal: {res['journal']}")
        print(f"    DOI: {res['doi']} | Section: {res['section'].upper()} | Rights: {redist_str}")
        print(f"    🔬 Segmentation Approach: {seg_str} | Modality: {mod_str}")
        print(f"    Excerpt:")
        snippet = res["text"].strip().replace("\n", " ")
        if len(snippet) > 320:
            snippet = snippet[:315] + "..."
        print(f"    \"{snippet}\"")
        print("-" * 80)

    if compare_seg:
        print("\n" + "=" * 80)
        print("🔬 SEGMENTATION METHODOLOGY DIVERSITY AUDIT")
        print("=" * 80)
        for res in results:
            print(f"• {res['title']} ({res['year']}):")
            print(f"   - Algorithms: {', '.join(res.get('segmentation_approaches', []))}")
            print(f"   - Imaging:    {', '.join(res.get('imaging_modalities', []))}")
            print(f"   - Metrics:    {', '.join(res.get('validation_metrics', [])) or 'Standard Visual QC'}")
        print("=" * 80)


def main():
    parser = argparse.ArgumentParser(description="Query Connectomics RAG Corpus")
    parser.add_argument("--query", "-q", type=str, required=True, help="Research question or topic to search")
    parser.add_argument("--top-k", "-k", type=int, default=5, help="Number of top excerpts to return")
    parser.add_argument("--section", "-s", type=str, choices=["abstract", "methods_protocol", "results_findings", "discussion_horizons", "opportunity_intro"],
                        help="Filter by specific academic section")
    parser.add_argument("--compare-segmentation", action="store_true", help="Print structured segmentation diversity comparison across retrieved papers")
    args = parser.parse_args()

    results = search_rag(args.query, top_k=args.top_k, section_filter=args.section)
    format_cli_output(results, args.query, compare_seg=args.compare_segmentation)


if __name__ == "__main__":
    main()
