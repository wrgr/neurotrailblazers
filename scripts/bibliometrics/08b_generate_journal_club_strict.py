#!/usr/bin/env python3
"""
Generate journal club selection with STRICT connectomics filtering.

Filters papers by:
1. Community type (strict connectomics communities only)
2. Individual paper relevance check (title/abstract/concepts match connectomics terms)

Uses 80/20 weights: 80% composite score + 20% k-core
"""
import json
from pathlib import Path
from collections import defaultdict

OUT = Path("output")

# Strict connectomics terms that must appear
CONNECTOMICS_REQUIRED_TERMS = [
    "connectom", "electron microscopy", "em microscopy", "synapse", "synaptic",
    "neural circuit", "nanoscale", "ultrastructure", "neural wiring",
    "serial section", "sbem", "fib-sem", "volume em",
    "expansion microscopy", "segmentation", "reconstruction",
    "synaptic connectivity", "wiring diagram", "connectome",
]

# Communities to explicitly exclude
EXCLUDE_COMMUNITIES = {
    13,  # Apoptosis, Cell death
    5, 89, 265,  # General biology, materials science
}

TIER_ORDER = ["platinum", "gold", "silver", "bronze"]
TIER_LABELS = {
    "platinum": "🏆 Platinum (≥0.40) — Foundational & highly central",
    "gold": "🥇 Gold (0.30–0.40) — Key papers with strong signal",
    "silver": "🥈 Silver (0.20–0.30) — Solid connectomics contributions",
    "bronze": "🥉 Bronze (<0.20) — Emerging & peripheral work",
}


def get_tier(score):
    """Assign tier based on composite score."""
    if score >= 0.40:
        return "platinum"
    elif score >= 0.30:
        return "gold"
    elif score >= 0.20:
        return "silver"
    else:
        return "bronze"


def normalize(values):
    """Min-max normalize values to [0, 1]."""
    if not values:
        return {}
    min_val = min(values.values())
    max_val = max(values.values())
    if min_val == max_val:
        return {k: 0.5 for k in values}
    return {k: (v - min_val) / (max_val - min_val) for k, v in values.items()}


def is_connectomics_relevant(paper_title, concepts):
    """Check if paper is actually connectomics-relevant."""
    title_lower = paper_title.lower()
    concept_text = " ".join(c.lower() for c in concepts)
    combined = f"{title_lower} {concept_text}"

    return any(term in combined for term in CONNECTOMICS_REQUIRED_TERMS)


def load_json(name):
    with open(OUT / name) as f:
        return json.load(f)


def main():
    print("Loading data...")
    rankings = load_json("paper_rankings.json")
    kcore = load_json("kcore_tiers_annotated.json")
    communities = load_json("communities.json")
    corpus = load_json("corpus_merged.json")

    # Build lookup tables
    rankings_by_id = {r["openalex_id"]: r for r in rankings}
    corpus_by_id = {p["openalex_id"]: p for p in corpus}

    # Build data for papers with strict connectomics filtering
    papers = []

    for pid, k_core_data in kcore.items():
        corpus_p = corpus_by_id.get(pid, {})
        rank_p = rankings_by_id.get(pid, {})

        # Get community assignment
        cid = None
        for c in communities:
            if pid in c.get("members", []):
                cid = c["community_id"]
                break

        # Skip explicitly excluded communities
        if cid in EXCLUDE_COMMUNITIES:
            continue

        # Check connectomics relevance by title and concepts
        title = corpus_p.get("title", "")
        concepts = [c.get("name", "") for c in corpus_p.get("concepts", [])]

        if not is_connectomics_relevant(title, concepts):
            continue

        # Skip if no community assignment
        if cid is None:
            continue

        papers.append({
            "openalex_id": pid,
            "title": title,
            "year": corpus_p.get("year", 0),
            "doi": corpus_p.get("doi", ""),
            "citations": corpus_p.get("cited_by_count", 0),
            "kcore": k_core_data.get("k_core", 0),
            "pagerank": rank_p.get("pagerank", 0),
            "hits_hub": rank_p.get("hits_hub", 0),
            "hits_authority": rank_p.get("hits_authority", 0),
            "betweenness": rank_p.get("betweenness", 0),
            "composite_score": rank_p.get("composite_score", 0),
            "community_id": cid,
        })

    print(f"Papers after strict connectomics filtering: {len(papers)}")

    # Compute composite scores for papers without them
    for p in papers:
        pid = p["openalex_id"]
        if p["composite_score"] <= 0:
            if p["pagerank"] > 0 or p["hits_hub"] > 0:
                score = (0.35 * p["pagerank"] +
                        0.25 * p["hits_hub"] +
                        0.20 * p["hits_authority"] +
                        0.20 * max(p["betweenness"], 0))
                p["composite_score"] = score

    # Normalize metrics
    normalized_composite = normalize({p["openalex_id"]: p["composite_score"] for p in papers})
    normalized_kcore = normalize({p["openalex_id"]: p["kcore"] for p in papers})

    # Combine with 80/20 weights
    results = []
    for p in papers:
        pid = p["openalex_id"]
        score = 0.8 * normalized_composite.get(pid, 0) + 0.2 * normalized_kcore.get(pid, 0)
        tier = get_tier(score)

        results.append({
            **p,
            "composite_component": round(normalized_composite.get(pid, 0), 4),
            "kcore_component": round(normalized_kcore.get(pid, 0), 4),
            "combined_score": round(score, 4),
            "tier": tier,
        })

    results.sort(key=lambda x: x["combined_score"], reverse=True)

    # Save full results
    with open(OUT / "journal_club_final_strict.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nSaved: journal_club_final_strict.json ({len(results)} total papers)")

    # Group by tier
    by_tier = defaultdict(list)
    for p in results:
        by_tier[p["tier"]].append(p)

    # Generate markdown
    def generate_markdown(results, by_tier):
        lines = [
            "# Journal Club Selection — EM Connectomics (Strict)\n",
            "> **Methodology**: 80% × composite_score (PageRank + HITS + betweenness) + 20% × k-core\n",
            "> **Filtering**: Papers must match connectomics-specific terms in title/concepts\n",
            "> **Primary threshold**: score ≥ 0.2 (Silver tier and above)\n",
            "> **All papers listed** with tier markers for progressive engagement\n",
            f"> **Coverage**: {len(results)} papers across {len(set(p['community_id'] for p in results))} communities\n",
        ]

        for tier in TIER_ORDER:
            papers_in_tier = by_tier[tier]
            if not papers_in_tier:
                continue

            lines.append(f"\n---\n\n## {TIER_LABELS[tier]}\n")
            lines.append(f"**{len(papers_in_tier)} papers**\n")

            by_comm = defaultdict(list)
            for p in papers_in_tier:
                by_comm[p['community_id']].append(p)

            for comm_id in sorted(by_comm.keys()):
                comm_papers = by_comm[comm_id]
                lines.append(f"\n### Community {comm_id} ({len(comm_papers)} papers)\n")

                for i, p in enumerate(comm_papers, 1):
                    doi_link = f" · [doi](https://doi.org/{p['doi']})" if p['doi'] else ""
                    lines.append(
                        f"**{i}. {p['title']}**  \n"
                        f"{p['year']} · Citations: {p['citations']:,} · K-core: {p['kcore']} · Score: {p['combined_score']:.3f}{doi_link}\n"
                    )

        return "\n".join(lines)

    md = generate_markdown(results, by_tier)
    with open(OUT / "journal_club_final_strict.md", "w") as f:
        f.write(md)

    print(f"Saved: journal_club_final_strict.md")

    # Summary
    print("\n" + "="*70)
    print("JOURNAL CLUB SELECTION — STRICT CONNECTOMICS FILTERING")
    print("="*70)

    for tier in TIER_ORDER:
        papers_in_tier = by_tier[tier]
        if papers_in_tier:
            print(f"\n{tier.upper()}: {len(papers_in_tier)} papers")
            for p in papers_in_tier[:3]:
                print(f"  • {p['title'][:70]}... (y:{p['year']} k:{p['kcore']})")

    print(f"\n{'='*70}")
    threshold_count = len([p for p in results if p['combined_score'] >= 0.2])
    print(f"TOTAL: {len(results)} papers")
    print(f"Primary selection (≥0.2): {threshold_count} papers")
    print(f"{'='*70}")

    print(f"\nDistribution by tier:")
    for tier in TIER_ORDER:
        count = len(by_tier[tier])
        pct = 100 * count / len(results) if results else 0
        print(f"  {tier:10s}: {count:3d} papers ({pct:5.1f}%)")


if __name__ == "__main__":
    main()
