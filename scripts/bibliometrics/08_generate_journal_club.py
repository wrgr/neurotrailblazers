#!/usr/bin/env python3
"""
Generate journal club selection using Approach A with adjusted weights:
- 80% composite score (PageRank + HITS + betweenness)
- 20% k-core

Mark papers by multiple thresholds so they can be filtered and used as topics progress.
"""
import json
from pathlib import Path
from collections import defaultdict

OUT = Path("output")


def load_json(name):
    with open(OUT / name) as f:
        return json.load(f)


def normalize(values):
    """Min-max normalize values to [0, 1]."""
    if not values:
        return {}
    min_val = min(values.values())
    max_val = max(values.values())
    if min_val == max_val:
        return {k: 0.5 for k in values}
    return {k: (v - min_val) / (max_val - min_val) for k, v in values.items()}


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


def main():
    print("Loading data...")
    rankings = load_json("paper_rankings.json")
    kcore = load_json("kcore_tiers_annotated.json")
    communities = load_json("communities.json")
    corpus = load_json("corpus_merged.json")

    # Build lookup tables
    rankings_by_id = {r["openalex_id"]: r for r in rankings}
    corpus_by_id = {p["openalex_id"]: p for p in corpus}

    # Identify connectomics communities
    connectomics_communities = set()
    for c in communities:
        top_labels = [x["name"].lower() for x in c.get("top_concepts", [])[:3]]
        is_noise = any(x in " ".join(top_labels) for x in
                      ["geology", "seismology", "chromatography", "mass spectrometry"])
        if not is_noise:
            connectomics_communities.add(c["community_id"])

    print(f"Connectomics communities: {len(connectomics_communities)}")

    # Build data for all papers in connectomics communities
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

        if cid not in connectomics_communities:
            continue

        papers.append({
            "openalex_id": pid,
            "title": corpus_p.get("title", "Unknown"),
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

    print(f"Papers in connectomics communities: {len(papers)}")

    # Compute composite scores for papers without them
    for p in papers:
        pid = p["openalex_id"]
        if p["composite_score"] <= 0:
            if p["pagerank"] > 0 or p["hits_hub"] > 0:
                # Compute from components
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
    with open(OUT / "journal_club_final.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nSaved: journal_club_final.json ({len(results)} total papers)")

    # Group by tier for both markdown and summary
    by_tier = defaultdict(list)
    for p in results:
        by_tier[p["tier"]].append(p)

    # Generate markdown with tier markers
    def generate_markdown(results, by_tier):
        lines = [
            "# Journal Club Selection — EM Connectomics\n",
            "> **Methodology**: 80% × composite_score (PageRank + HITS + betweenness) + 20% × k-core\n",
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

            # Group by community within tier
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
    with open(OUT / "journal_club_final.md", "w") as f:
        f.write(md)

    print(f"Saved: journal_club_final.md")

    # Summary statistics
    print("\n" + "="*70)
    print("JOURNAL CLUB SELECTION SUMMARY (80/20 weights)")
    print("="*70)

    for tier in ["platinum", "gold", "silver", "bronze"]:
        papers_in_tier = by_tier[tier]
        if papers_in_tier:
            print(f"\n{tier.upper()}: {len(papers_in_tier)} papers")
            for p in papers_in_tier[:3]:
                print(f"  • {p['title'][:70]}... (y:{p['year']} k:{p['kcore']})")

    print(f"\n{'='*70}")
    print(f"TOTAL: {len(results)} papers (threshold ≥0.2 = {len([p for p in results if p['combined_score'] >= 0.2])}) ready for journal club")
    print(f"{'='*70}")

    # Show distribution
    print(f"\nDistribution by tier:")
    for tier in TIER_ORDER:
        count = len(by_tier[tier])
        pct = 100 * count / len(results) if results else 0
        print(f"  {tier:10s}: {count:3d} papers ({pct:5.1f}%)")


if __name__ == "__main__":
    main()
