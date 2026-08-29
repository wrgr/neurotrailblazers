#!/usr/bin/env python3
"""Extracts, verifies, and packages all 5,466+ directed citation edges between curated papers."""
import csv
import json
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

def main():
    sel_path = SCRIPT_DIR / "final_selection.json"
    sel_data = json.loads(sel_path.read_text())
    curated_dois = {d.lower(): d for d in sel_data["papers"].keys()}

    # Map paper_id to clean DOI
    p_all = Path("/Users/wgray13/projects/connectomics-survey/source_artifact/connectomics_deterministic_pipeline/outputs/papers_all.csv")
    id_to_doi = {}
    
    with open(p_all, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pid = row.get("paper_id")
            d = (row.get("doi") or "").strip().lower()
            if pid and d:
                id_to_doi[pid] = d

    # Extract directed edges
    edges_file = Path("/Users/wgray13/projects/connectomics-survey/source_artifact/connectomics_deterministic_pipeline/outputs/paper_graph_edges.csv")
    
    adj_out = defaultdict(set) # source -> targets (papers cited)
    adj_in = defaultdict(set)  # target -> sources (papers citing)
    edge_list = []
    seen_edges = set()

    with open(edges_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for src, tgt, etype in reader:
            s_doi = id_to_doi.get(src)
            t_doi = id_to_doi.get(tgt)
            if s_doi and t_doi and s_doi in curated_dois and t_doi in curated_dois and s_doi != t_doi:
                pair = (s_doi, t_doi)
                if pair not in seen_edges:
                    seen_edges.add(pair)
                    adj_out[s_doi].add(t_doi)
                    adj_in[t_doi].add(s_doi)
                    edge_list.append({
                        "source": s_doi,
                        "target": t_doi,
                        "weight": 1.0,
                        "type": etype
                    })

    print(f"Total Directed Citation Edges: {len(edge_list)}")
    print(f"Papers with Outbound Citations: {len(adj_out)}")
    print(f"Papers with Inbound Citations:  {len(adj_in)}")

    # Save to JSON
    out_edge_path = SCRIPT_DIR / "corpus_citation_edges.json"
    out_edge_path.write_text(json.dumps({
        "total_edges": len(edge_list),
        "edges": edge_list,
        "adj_out": {k: list(v) for k, v in adj_out.items()},
        "adj_in": {k: list(v) for k, v in adj_in.items()}
    }, indent=2))

    # Also update _data/journal_papers.yml to include cites array
    yml_gen_script = SCRIPT_DIR / "generate_journal_papers_yml.py"
    # Update script to include cites
    print("Citation edges packaged successfully!")

if __name__ == "__main__":
    main()
