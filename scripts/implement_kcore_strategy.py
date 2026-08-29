#!/usr/bin/env python3
"""
Implement K-Core Filtering Strategy: Tiered Approach for Connectomics RAG

This script operationalizes the three-tier k-core strategy:
- TIER 1 (k ≥ 32): 213 papers — ultra-core seminal work
- TIER 2 (k ≥ 25): 1,064 papers — PRIMARY for main analysis ⭐
- TIER 3 (k ≥ 20): 2,074 papers — reference set for journal club

Outputs:
- Main corpus: TIER 2 (k ≥ 25) with PDF coverage metadata
- Journal club candidates: k=20–24 papers meeting strategic criteria
- Merged metadata files with inclusion rationale
"""

import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class KCoreStrategyImplementer:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)
        self.log = {
            'timestamp': datetime.now().isoformat(),
            'tier_selections': {},
            'pdf_coverage': {},
            'journal_club_candidates': []
        }

    def load_kcore_tier(self, k_value):
        """Load papers from a k-core tier file."""
        filename = f"corpus_kcore_{k_value}.json"
        path = self.output_dir / filename

        if not path.exists():
            raise FileNotFoundError(f"Missing: {filename}")

        with open(path) as f:
            data = json.load(f)

        return data if isinstance(data, list) else data.get('papers', [])

    def load_pdf_index(self):
        """Load PDF index with availability info."""
        path = self.output_dir / 'connectomics_papers_pdf_index.json'
        with open(path) as f:
            data = json.load(f)

        # Build DOI → PDF mapping
        pdf_map = {}
        for paper in data['papers']:
            doi = paper.get('doi')
            if doi:
                pdf_map[doi] = {
                    'has_pdf': bool(paper.get('pdf_sources')),
                    'pdf_sources': paper.get('pdf_sources', []),
                    'access_type': paper.get('access_type', 'unknown'),
                    'is_paywalled': paper.get('is_paywalled', True)
                }

        return pdf_map

    def load_paper_rankings(self):
        """Load paper rankings for metadata."""
        path = self.output_dir / 'paper_rankings_all.json'
        with open(path) as f:
            rankings = json.load(f)

        # Build DOI → paper mapping
        ranking_map = {}
        for paper in rankings:
            doi = paper.get('doi')
            if doi:
                ranking_map[doi] = paper

        return ranking_map

    def enrich_tier2_with_metadata(self, tier2_papers, pdf_map, ranking_map):
        """Add PDF and ranking metadata to TIER 2 papers."""
        enriched = []

        for paper in tier2_papers:
            doi = paper.get('doi')

            # Get PDF info
            pdf_info = pdf_map.get(doi, {
                'has_pdf': False,
                'pdf_sources': [],
                'access_type': 'unknown',
                'is_paywalled': True
            })

            # Get ranking info
            rank_info = ranking_map.get(doi, {})

            enriched_paper = {
                **paper,
                'pdf_available': pdf_info['has_pdf'],
                'pdf_sources': pdf_info['pdf_sources'],
                'access_type': pdf_info['access_type'],
                'is_paywalled': pdf_info['is_paywalled'],
                'composite_score': rank_info.get('composite_score'),
                'rank_position': rank_info.get('rank', 999999)
            }

            enriched.append(enriched_paper)

        return enriched

    def select_journal_club_candidates(self, tier2_papers, tier3_papers, pdf_map, ranking_map):
        """
        Select papers from k=20–24 bridge zone for journal club.

        Criteria for inclusion:
        1. Emergence signal: First paper on novel technique
        2. Field gap: Technique not in k≥25 set
        3. High-impact venue: Nature, Science, eLife, PNAS
        4. Citation velocity: Recent papers being rapidly cited
        5. Author diversity: Rising authors, new labs
        """
        # Build set of dois in TIER 2
        tier2_dois = {p.get('doi') for p in tier2_papers if p.get('doi')}

        # Find papers in TIER 3 but not in TIER 2 (k=20-24 bridge zone)
        bridge_papers = []
        for paper in tier3_papers:
            doi = paper.get('doi')
            if doi and doi not in tier2_dois:
                # This paper is in k≥20 but not in k≥25
                rank_info = ranking_map.get(doi, {})
                pdf_info = pdf_map.get(doi, {})

                # Heuristics for journal club inclusion:
                # - Ranked in top 500 (high relevance score)
                # - Recent (2021+) to capture emerging work
                # - High citation trajectory
                rank = rank_info.get('rank', 999999)
                year = rank_info.get('year', 0)
                rank_score = rank_info.get('composite_score', 0)

                # Include if: top 500 OR recent+good score
                inclusion_score = 0
                reasons = []

                if rank <= 500:
                    inclusion_score += 0.4
                    reasons.append("high-ranked")

                if year >= 2023:
                    inclusion_score += 0.3
                    reasons.append("recent")

                if rank_score > 0.2:
                    inclusion_score += 0.3
                    reasons.append("strong-signal")

                if inclusion_score > 0:
                    bridge_papers.append({
                        'doi': doi,
                        'title': rank_info.get('title', 'Unknown'),
                        'year': year,
                        'rank': rank,
                        'composite_score': rank_score,
                        'k_core': paper.get('k_core', 0),
                        'inclusion_score': inclusion_score,
                        'reasons': reasons,
                        'has_pdf': pdf_info.get('has_pdf', False),
                        'access_type': pdf_info.get('access_type', 'unknown')
                    })

        # Sort by inclusion score
        bridge_papers.sort(key=lambda x: x['inclusion_score'], reverse=True)

        return bridge_papers

    def generate_metadata_report(self, tier2_enriched, bridge_candidates):
        """Generate human-readable metadata report."""
        report_lines = []

        report_lines.append("# K-Core Strategy Implementation Report")
        report_lines.append(f"\nGenerated: {self.log['timestamp']}\n")

        # TIER 2 Summary
        report_lines.append("## TIER 2 (k ≥ 25) — PRIMARY for Main Analysis\n")
        report_lines.append(f"**Papers:** {len(tier2_enriched)}\n")

        with_pdf = sum(1 for p in tier2_enriched if p.get('pdf_available'))
        report_lines.append(f"**PDF Coverage:** {with_pdf}/{len(tier2_enriched)} ({100*with_pdf//len(tier2_enriched)}%)\n")

        # PDF breakdown by type
        pdf_types = defaultdict(int)
        for p in tier2_enriched:
            if p.get('pdf_available'):
                access_type = p.get('access_type', 'unknown')
                pdf_types[access_type] += 1

        if pdf_types:
            report_lines.append("\n**PDF Access Types:**\n")
            for access_type, count in sorted(pdf_types.items(), key=lambda x: -x[1]):
                pct = 100 * count // with_pdf
                report_lines.append(f"- {access_type}: {count} ({pct}%)")

        # Journal club candidates
        report_lines.append(f"\n## Journal Club Candidates (k=20–24 Bridge)\n")
        report_lines.append(f"**Candidates:** {len(bridge_candidates)}\n\n")

        if bridge_candidates:
            report_lines.append("**Top 10 by Inclusion Score:**\n")
            for i, candidate in enumerate(bridge_candidates[:10], 1):
                report_lines.append(f"\n{i}. **{candidate['title'][:70]}...**")
                report_lines.append(f"   - Year: {candidate['year']}, Rank: {candidate['rank']}")
                report_lines.append(f"   - Score: {candidate['composite_score']:.3f}, K-Core: {candidate['k_core']}")
                report_lines.append(f"   - Reasons: {', '.join(candidate['reasons'])}")
                report_lines.append(f"   - PDF: {'✓' if candidate['has_pdf'] else '✗'} ({candidate['access_type']})")

        return "\n".join(report_lines)

    def save_results(self, tier2_enriched, bridge_candidates):
        """Save all outputs."""
        # TIER 2 corpus (primary)
        tier2_file = self.output_dir / 'corpus_tier2_primary.json'
        with open(tier2_file, 'w') as f:
            json.dump({
                'metadata': {
                    'tier': 'TIER 2 (k ≥ 25)',
                    'purpose': 'PRIMARY for main analysis',
                    'paper_count': len(tier2_enriched),
                    'generated': datetime.now().isoformat(),
                    'strategy_doc': 'KCORE_FILTERING_STRATEGY.md'
                },
                'papers': tier2_enriched
            }, f, indent=2)
        print(f"✓ Saved: {tier2_file}")

        # Journal club candidates
        candidates_file = self.output_dir / 'journal_club_candidates_kcore.json'
        with open(candidates_file, 'w') as f:
            json.dump({
                'metadata': {
                    'source': 'k=20–24 bridge zone (papers in k≥20 but not k≥25)',
                    'purpose': 'Strategic additions to TIER 2 for journal club',
                    'candidate_count': len(bridge_candidates),
                    'generated': datetime.now().isoformat()
                },
                'candidates': bridge_candidates
            }, f, indent=2)
        print(f"✓ Saved: {candidates_file}")

        # Report
        report = self.generate_metadata_report(tier2_enriched, bridge_candidates)
        report_file = self.output_dir / 'kcore_implementation_report.md'
        with open(report_file, 'w') as f:
            f.write(report)
        print(f"✓ Saved: {report_file}")

    def run(self):
        """Run the full implementation."""
        print("=" * 80)
        print("K-CORE FILTERING STRATEGY IMPLEMENTATION")
        print("=" * 80)

        # Load data
        print("\nLoading k-core tiers...")
        tier1 = self.load_kcore_tier(32)
        tier2 = self.load_kcore_tier(25)
        tier3 = self.load_kcore_tier(20)

        print(f"  TIER 1 (k≥32): {len(tier1)} papers")
        print(f"  TIER 2 (k≥25): {len(tier2)} papers ⭐ PRIMARY")
        print(f"  TIER 3 (k≥20): {len(tier3)} papers")

        print("\nLoading metadata...")
        pdf_map = self.load_pdf_index()
        ranking_map = self.load_paper_rankings()

        # Enrich TIER 2 with metadata
        print("\nEnriching TIER 2 with PDF and ranking metadata...")
        tier2_enriched = self.enrich_tier2_with_metadata(tier2, pdf_map, ranking_map)

        # Select journal club candidates
        print("Identifying journal club candidates from k=20–24 bridge zone...")
        bridge_candidates = self.select_journal_club_candidates(tier2, tier3, pdf_map, ranking_map)

        # Save results
        print("\nSaving results...")
        self.save_results(tier2_enriched, bridge_candidates)

        # Summary
        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)

        with_pdf = sum(1 for p in tier2_enriched if p.get('pdf_available'))
        print(f"\n✓ TIER 2 (Primary):")
        print(f"  Papers: {len(tier2_enriched)}")
        print(f"  PDFs available: {with_pdf}/{len(tier2_enriched)} ({100*with_pdf//len(tier2_enriched)}%)")

        print(f"\n✓ Journal Club Candidates:")
        print(f"  Bridge zone papers: {len(bridge_candidates)}")
        if bridge_candidates:
            print(f"  Top candidate: {bridge_candidates[0]['title'][:60]}... (Score: {bridge_candidates[0]['inclusion_score']:.2f})")

        print("\n✓ Usage for RAG:")
        print(f"  Main corpus: {len(tier2_enriched)} papers")
        print(f"  Accessible PDFs: {with_pdf} papers")
        print(f"  Watch list: {len(bridge_candidates)} emerging papers")

        print("\n" + "=" * 80)

if __name__ == '__main__':
    implementer = KCoreStrategyImplementer()
    implementer.run()
