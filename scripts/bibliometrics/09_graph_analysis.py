#!/usr/bin/env python3
"""
Step 9: Extended graph analysis.

  1. K-core decomposition of citation graph
     — core number = how deeply embedded in the network
     — flag core number for every reading-list paper
     — print k-core shells and their prominent papers

  2. Degree distributions for reading-list papers
     — in-degree (cited by), out-degree (cites), total degree
     — flag papers with high in-degree not in top-500
     — flag original expert-curated papers excluded from top-500 with high cite count

  3. Author k-core / connectivity analysis
     — find Will Gray Roncal (and similar names) in full author list
     — report position, composite score, betweenness, degree

Usage:
  python 09_graph_analysis.py
"""
import json
import re
from collections import defaultdict
from pathlib import Path

import networkx as nx

from config import OUTPUT_DIR, CACHE_DIR

# ── Load helpers ──────────────────────────────────────────────────────

def load_json(fname):
    with open(OUTPUT_DIR / fname) as f:
        return json.load(f)

def load_graph(fname):
    path = OUTPUT_DIR / "graphs" / fname
    with open(path) as f:
        data = json.load(f)
    G = nx.DiGraph() if data.get("directed") else nx.Graph()
    for n in data["nodes"]:
        G.add_node(n["id"], **{k: v for k, v in n.items() if k != "id"})
    for e in data["edges"]:
        G.add_edge(e["source"], e["target"],
                   **{k: v for k, v in e.items() if k not in ("source", "target")})
    return G

def save_json(obj, fname):
    with open(OUTPUT_DIR / fname, "w") as f:
        json.dump(obj, f, indent=2)
    print(f"  Saved → output/{fname}")


# ── 1. K-core decomposition ───────────────────────────────────────────

def kcore_analysis(citation_graph, reading_list, paper_rankings):
    """Decompose undirected version of citation graph into k-cores."""
    print("\n=== K-Core Decomposition ===")
    G_undir = citation_graph.to_undirected()
    G_undir.remove_edges_from(nx.selfloop_edges(G_undir))
    core_numbers = nx.core_number(G_undir)

    max_k = max(core_numbers.values())
    print(f"  Max k-core: {max_k}")
    print(f"  Nodes: {G_undir.number_of_nodes()}  Edges: {G_undir.number_of_edges()}")

    # Distribution of core numbers
    shell_counts = defaultdict(int)
    for k in core_numbers.values():
        shell_counts[k] += 1
    print("\n  Core shell distribution (k: count):")
    for k in sorted(shell_counts)[-15:]:
        bar = "#" * min(shell_counts[k] // 20, 50)
        print(f"    k={k:3}: {shell_counts[k]:5}  {bar}")

    # Annotate reading list with core numbers
    rl_lookup = {p["openalex_id"]: p for p in reading_list}
    for pid, k in core_numbers.items():
        if pid in rl_lookup:
            rl_lookup[pid]["core_number"] = k

    # Papers in the innermost 10% of cores
    top_k_threshold = int(max_k * 0.90)
    inner_core = [
        (pid, k) for pid, k in core_numbers.items()
        if k >= top_k_threshold
    ]
    inner_core.sort(key=lambda x: -x[1])
    print(f"\n  Inner core (k ≥ {top_k_threshold}): {len(inner_core)} papers")

    # Build lookup for titles
    pr_lookup = {p["openalex_id"]: p for p in paper_rankings}
    print(f"  Top 30 inner-core papers:")
    for pid, k in inner_core[:30]:
        p = pr_lookup.get(pid) or rl_lookup.get(pid, {})
        in_rl = "✓" if pid in rl_lookup else " "
        print(f"    [{in_rl}] k={k:3}  {p.get('title','?')[:70]}")

    return core_numbers, max_k, top_k_threshold


# ── 2. Degree distributions ───────────────────────────────────────────

def degree_analysis(citation_graph, reading_list, paper_rankings, corpus):
    """Compute in/out degree for all nodes; flag outliers."""
    print("\n=== Degree Distribution (Citation Graph) ===")

    in_deg  = dict(citation_graph.in_degree())
    out_deg = dict(citation_graph.out_degree())

    rl_ids = {p["openalex_id"] for p in reading_list}
    pr_lookup = {p["openalex_id"]: p for p in paper_rankings}
    corpus_lookup = {p["openalex_id"]: p for p in corpus}

    # Annotate reading list
    rl_enriched = []
    for p in reading_list:
        pid = p["openalex_id"]
        rl_enriched.append({
            **p,
            "in_degree":  in_deg.get(pid, 0),
            "out_degree": out_deg.get(pid, 0),
            "total_degree": in_deg.get(pid, 0) + out_deg.get(pid, 0),
        })

    # Sort by in_degree
    rl_by_indeg = sorted(rl_enriched, key=lambda x: -x["in_degree"])
    print(f"\n  Top 20 reading-list papers by in-degree (cited by others in corpus):")
    for p in rl_by_indeg[:20]:
        print(f"    in={p['in_degree']:4}  out={p['out_degree']:4}  "
              f"[{p['year']}] {p['title'][:65]}")

    # High-citation papers NOT in top-500
    print(f"\n  High in-degree papers NOT in reading list (potential omissions):")
    not_in_rl = [
        (pid, deg) for pid, deg in in_deg.items()
        if pid not in rl_ids and deg >= 30
    ]
    not_in_rl.sort(key=lambda x: -x[1])
    for pid, deg in not_in_rl[:30]:
        p = pr_lookup.get(pid) or corpus_lookup.get(pid, {})
        cite = p.get("cited_by_count") or p.get("total_citations", 0)
        print(f"    in={deg:4}  ext_cites={cite:6}  {p.get('title','?')[:65]}")

    return rl_enriched, not_in_rl


# ── 3. Expert list gap analysis ───────────────────────────────────────

def expert_gap_analysis(reading_list, paper_rankings, corpus):
    """Flag expert-curated papers excluded from top-500 with high external citations."""
    print("\n=== Expert-Curated Papers Not in Top-500 ===")

    # Load expert seeds
    expert_dois = set()
    # Seeds file
    seeds_path = Path(__file__).parent / "output" / "corpus_a.json"
    if seeds_path.exists():
        with open(seeds_path) as f:
            corpus_a = json.load(f)
        for p in corpus_a:
            if p.get("doi"):
                expert_dois.add(p["doi"].lower().strip())

    # journal_papers.yml
    jp_path = Path(__file__).parent.parent.parent / "_data" / "journal_papers.yml"
    def norm_doi(d):
        return (d or "").strip().lower().replace("https://doi.org/","").replace("http://doi.org/","")

    jp_dois = {}
    if jp_path.exists():
        current = {}
        with open(jp_path) as f:
            for line in f:
                line = line.rstrip()
                if line.strip().startswith("- id:"):
                    if current.get("doi"):
                        jp_dois[norm_doi(current["doi"])] = current.copy()
                    current = {"id": line.split(":",1)[1].strip()}
                elif line.strip().startswith("doi:"):
                    v = line.split(":",1)[1].strip().strip('"').strip("'")
                    if v and v != "null":
                        current["doi"] = v
                elif line.strip().startswith("title:"):
                    current["title"] = line.split(":",1)[1].strip().strip('"')
                elif line.strip().startswith("dimension:"):
                    current["dimension"] = line.split(":",1)[1].strip().strip('"')
            if current.get("doi"):
                jp_dois[norm_doi(current["doi"])] = current

    rl_dois = {norm_doi(p.get("doi","")) for p in reading_list}
    corpus_by_doi = {norm_doi(p.get("doi","")): p for p in corpus if p.get("doi")}

    missed = []
    for doi, meta in jp_dois.items():
        if doi not in rl_dois:
            cp = corpus_by_doi.get(doi, {})
            missed.append({
                "doi": doi,
                "title": meta.get("title", cp.get("title", "?")),
                "dimension": meta.get("dimension", "?"),
                "external_citations": cp.get("cited_by_count", 0),
                "in_corpus": bool(cp),
            })

    missed.sort(key=lambda x: -x["external_citations"])
    print(f"  {len(missed)} expert papers missing from top-500:")
    print(f"  {'Cites':>6}  {'Dim':<22}  Title")
    print(f"  {'-'*6}  {'-'*22}  {'-'*60}")
    for m in missed:
        corpus_flag = "" if m["in_corpus"] else " [NOT IN CORPUS]"
        print(f"  {m['external_citations']:6}  {m['dimension']:<22}  "
              f"{m['title'][:60]}{corpus_flag}")

    return missed


# ── 4. Author / Gray Roncal lookup ────────────────────────────────────

def author_analysis(author_rankings):
    """Find Will Gray Roncal and report key metrics."""
    print("\n=== Author Analysis ===")

    # Search for Gray Roncal and related names
    search_terms = ["roncal", "gray roncal", "william gray", "will gray"]
    print("  Searching for Will Gray Roncal...")
    found = []
    for i, a in enumerate(author_rankings):
        name_lower = a.get("name", "").lower()
        if any(t in name_lower for t in search_terms):
            found.append((i + 1, a))

    if found:
        for rank, a in found:
            print(f"\n  Found: {a['name']}")
            print(f"    Rank:             #{rank} of {len(author_rankings)}")
            print(f"    Composite score:  {a.get('composite_score', 0):.4f}")
            print(f"    Papers in corpus: {a.get('paper_count', 0)}")
            print(f"    PageRank sum:     {a.get('total_pagerank', 0):.6f}")
            print(f"    Betweenness:      {a.get('betweenness', 0):.6f}")
            print(f"    Weighted degree:  {a.get('weighted_degree', 0):.2f}")
    else:
        print("  Will Gray Roncal not found in author rankings.")
        print("  (May be outside ranked set or name variant)")
        # Try broader search in corpus
        print("\n  Top 50 authors for context:")
        for i, a in enumerate(author_rankings[:50]):
            print(f"    #{i+1:3}  {a['name']}")

    # Print full top-30 for reference
    print(f"\n  Top 30 authors by composite score:")
    for i, a in enumerate(author_rankings[:30]):
        marker = " ◄" if any(t in a.get("name","").lower() for t in search_terms) else ""
        print(f"    #{i+1:3}  {a['composite_score']:.4f}  "
              f"{a.get('paper_count',0):3}p  {a['name']}{marker}")

    return found


# ── Main ──────────────────────────────────────────────────────────────

def main():
    print("Loading data...")
    reading_list   = load_json("reading_list.json")
    paper_rankings = load_json("paper_rankings.json")
    author_rankings = load_json("author_rankings.json")
    corpus         = load_json("corpus_merged.json")

    print("Loading citation graph...")
    citation_graph = load_graph("citation_graph.json")
    print(f"  {citation_graph.number_of_nodes()} nodes, {citation_graph.number_of_edges()} edges")

    # 1. K-core
    core_numbers, max_k, top_k_threshold = kcore_analysis(
        citation_graph, reading_list, paper_rankings
    )

    # 2. Degree distributions
    rl_enriched, not_in_rl = degree_analysis(
        citation_graph, reading_list, paper_rankings, corpus
    )

    # 3. Expert gap
    missed_expert = expert_gap_analysis(reading_list, paper_rankings, corpus)

    # 4. Author lookup
    found_authors = author_analysis(author_rankings)

    # Save enriched reading list (adds in_degree, out_degree, core_number)
    for p in rl_enriched:
        pid = p["openalex_id"]
        p["core_number"] = core_numbers.get(pid, 0)
    save_json(rl_enriched, "reading_list_enriched.json")

    # Save high-indegree non-RL papers
    corpus_lookup = {p["openalex_id"]: p for p in corpus}
    pr_lookup = {p["openalex_id"]: p for p in paper_rankings}
    high_indeg_omissions = []
    for pid, deg in not_in_rl[:100]:
        p = pr_lookup.get(pid) or corpus_lookup.get(pid, {})
        high_indeg_omissions.append({
            "openalex_id": pid,
            "title": p.get("title", "?"),
            "year": p.get("year"),
            "journal": p.get("journal", "?"),
            "external_citations": p.get("cited_by_count") or p.get("total_citations", 0),
            "corpus_in_degree": deg,
            "composite_score": p.get("composite_score", 0),
        })
    save_json(high_indeg_omissions, "high_indegree_omissions.json")
    save_json(missed_expert, "expert_list_gaps.json")

    print("\n=== Done ===")
    print(f"  reading_list_enriched.json  — {len(rl_enriched)} papers with degree + core")
    print(f"  high_indegree_omissions.json — {len(high_indeg_omissions)} high-indeg papers outside top-500")
    print(f"  expert_list_gaps.json        — {len(missed_expert)} expert papers not recovered")


if __name__ == "__main__":
    main()
