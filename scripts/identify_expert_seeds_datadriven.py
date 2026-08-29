#!/usr/bin/env python3
"""
Data-driven expert seed discovery using three complementary methods.

Methods:
1. Most papers in top-500: Authors publishing high-impact work
2. Last-author signal: Researchers with multiple top-100 papers (PI role)
3. Co-authorship network: Betweenness centrality (bridge researchers)

Output: Ranked list of expert seed researchers for corpus expansion via OpenAlex
"""

import json
from collections import defaultdict
from pathlib import Path
import networkx as nx

class DataDrivenExpertFinder:
    def __init__(self, output_dir="scripts/bibliometrics/output"):
        self.output_dir = Path(output_dir)
        self.rankings = self._load_rankings()
        self.experts = {
            'method1': {},  # Most papers in top-500
            'method2': {},  # Last-author in top-100
            'method3': {}   # Co-authorship betweenness
        }

    def _load_rankings(self):
        """Load paper rankings."""
        path = self.output_dir / 'paper_rankings_all.json'
        with open(path) as f:
            return json.load(f)

    def method1_top500_authors(self):
        """Find authors with most papers in top-500 ranked papers."""
        print("\n[METHOD 1] Authors with most papers in top-500...")

        top500 = [p for p in self.rankings if p.get('rank', 99999) <= 500]

        author_counts = defaultdict(int)
        author_ranks = defaultdict(list)

        for paper in top500:
            rank = paper.get('rank', 99999)
            authors = paper.get('authors', [])

            if not authors:
                continue

            for author in authors:
                # Handle both string and dict formats
                if isinstance(author, dict):
                    name = author.get('name', 'Unknown')
                else:
                    name = author  # It's already a string

                if name and name != 'Unknown':
                    author_counts[name] += 1
                    author_ranks[name].append(rank)

        # Sort by paper count, then by average rank
        for name, count in sorted(author_counts.items(), key=lambda x: (-x[1], sum(author_ranks[x[0]]))):
            avg_rank = sum(author_ranks[name]) / len(author_ranks[name])
            self.experts['method1'][name] = {
                'papers_in_top500': count,
                'avg_rank': avg_rank,
                'top_rank': min(author_ranks[name])
            }

        return self.experts['method1']

    def method2_last_author_signal(self):
        """Find last-author (PI) researchers with multiple top-100 papers."""
        print("\n[METHOD 2] Last-author (PI) signal in top-100...")

        top100 = [p for p in self.rankings if p.get('rank', 99999) <= 100]

        last_author_counts = defaultdict(int)
        last_author_ranks = defaultdict(list)

        for paper in top100:
            rank = paper.get('rank', 99999)
            authors = paper.get('authors', [])

            if not authors or len(authors) == 0:
                continue

            # Last author (corresponding/PI)
            last_author = authors[-1]
            if isinstance(last_author, dict):
                name = last_author.get('name', 'Unknown')
            else:
                name = last_author

            if name and name != 'Unknown':
                last_author_counts[name] += 1
                last_author_ranks[name].append(rank)

        # Filter for researchers with ≥2 last-author positions in top-100
        for name, count in sorted(last_author_counts.items(), key=lambda x: (-x[1], sum(last_author_ranks[x[0]]))):
            if count >= 2:  # PI signal: multiple lead papers
                avg_rank = sum(last_author_ranks[name]) / len(last_author_ranks[name])
                self.experts['method2'][name] = {
                    'last_author_top100': count,
                    'avg_rank': avg_rank,
                    'top_rank': min(last_author_ranks[name])
                }

        return self.experts['method2']

    def method3_coauthorship_betweenness(self):
        """Build co-authorship network and find bridge researchers."""
        print("\n[METHOD 3] Co-authorship network betweenness...")

        # Build co-authorship graph
        G = nx.Graph()

        for paper in self.rankings[:1500]:  # Use top-1500 for co-authorship graph
            authors = paper.get('authors', [])

            if not authors or len(authors) < 2:
                continue

            # Convert all to strings
            author_names = []
            for author in authors:
                if isinstance(author, dict):
                    name = author.get('name', 'Unknown')
                else:
                    name = author
                if name and name != 'Unknown':
                    author_names.append(name)

            # Add edges for all author pairs
            if len(author_names) >= 2:
                for i, a1 in enumerate(author_names):
                    for a2 in author_names[i+1:]:
                        if G.has_edge(a1, a2):
                            G[a1][a2]['weight'] += 1
                        else:
                            G.add_edge(a1, a2, weight=1)

        # Compute betweenness centrality
        print(f"  Co-authorship network: {G.number_of_nodes()} authors, {G.number_of_edges()} edges")

        betweenness = nx.betweenness_centrality(G, weight='weight')

        # Sort by betweenness
        for name, centrality in sorted(betweenness.items(), key=lambda x: -x[1])[:50]:
            neighbors = len(list(G.neighbors(name)))
            total_coauthors = sum(1 for _ in G.neighbors(name))

            self.experts['method3'][name] = {
                'betweenness_centrality': centrality,
                'direct_collaborators': neighbors,
                'degree': G.degree(name)
            }

        return self.experts['method3']

    def generate_combined_ranking(self):
        """Combine three methods into unified expert ranking."""
        print("\n[COMBINING] Synthesizing three methods...")

        combined = {}

        # Score from Method 1 (0-50 points: papers in top-500)
        for name, data in self.experts['method1'].items():
            if name not in combined:
                combined[name] = {'scores': {}, 'metadata': {}}
            combined[name]['scores']['method1'] = data['papers_in_top500']
            combined[name]['metadata']['method1'] = data

        # Score from Method 2 (0-50 points: last-author in top-100)
        for name, data in self.experts['method2'].items():
            if name not in combined:
                combined[name] = {'scores': {}, 'metadata': {}}
            combined[name]['scores']['method2'] = data['last_author_top100'] * 25  # weight up
            combined[name]['metadata']['method2'] = data

        # Score from Method 3 (0-50 points: betweenness centrality)
        betweenness_scores = list(self.experts['method3'].values())
        if betweenness_scores:
            max_bet = max(s['betweenness_centrality'] for s in betweenness_scores)
            for name, data in self.experts['method3'].items():
                if name not in combined:
                    combined[name] = {'scores': {}, 'metadata': {}}
                # Normalize to 0-50
                combined[name]['scores']['method3'] = (data['betweenness_centrality'] / max_bet) * 50
                combined[name]['metadata']['method3'] = data

        # Compute combined score
        results = []
        for name, scores_data in combined.items():
            scores = scores_data['scores']

            # Average of available scores
            avg_score = sum(scores.values()) / len(scores) if scores else 0

            results.append({
                'name': name,
                'combined_score': avg_score,
                'methods_present': list(scores.keys()),
                'method1_score': scores.get('method1', 0),
                'method2_score': scores.get('method2', 0),
                'method3_score': scores.get('method3', 0),
                'metadata': scores_data['metadata']
            })

        # Sort by combined score
        results.sort(key=lambda x: -x['combined_score'])

        return results

    def generate_report(self, combined_ranking):
        """Generate human-readable report."""
        lines = []

        lines.append("# Data-Driven Expert Seed Discovery Report\n")
        lines.append(f"**Generated:** 2026-04-01\n")

        # Method 1
        lines.append("\n## Method 1: Most Papers in Top-500\n")
        lines.append(f"**Count:** {len(self.experts['method1'])} authors\n")
        if self.experts['method1']:
            lines.append("**Top 10:**\n")
            for name, data in list(self.experts['method1'].items())[:10]:
                lines.append(f"- {name}: {data['papers_in_top500']} papers (avg rank: {data['avg_rank']:.0f})")

        # Method 2
        lines.append(f"\n## Method 2: Last-Author Signal (Top-100, ≥2 papers)\n")
        lines.append(f"**Count:** {len(self.experts['method2'])} PI-level researchers\n")
        if self.experts['method2']:
            lines.append("**All (sorted by papers):**\n")
            for name, data in list(self.experts['method2'].items())[:15]:
                lines.append(f"- {name}: {data['last_author_top100']} top-100 papers (avg rank: {data['avg_rank']:.0f})")

        # Method 3
        lines.append(f"\n## Method 3: Co-authorship Network Betweenness\n")
        lines.append(f"**Count:** {len(self.experts['method3'])} bridge researchers\n")
        if self.experts['method3']:
            lines.append("**Top 10:**\n")
            for name, data in list(self.experts['method3'].items())[:10]:
                lines.append(f"- {name}: centrality={data['betweenness_centrality']:.4f}, degree={data['degree']}")

        # Combined ranking
        lines.append(f"\n## Combined Ranking (All Methods)\n")
        lines.append(f"**Total Unique Experts:** {len(combined_ranking)}\n")
        lines.append("\n**Top 30:**\n")

        for i, expert in enumerate(combined_ranking[:30], 1):
            methods = ', '.join(expert['methods_present'])
            lines.append(f"\n{i}. **{expert['name']}** (Score: {expert['combined_score']:.1f})")
            lines.append(f"   - Methods: {methods}")
            lines.append(f"   - M1: {expert['method1_score']:.0f} | M2: {expert['method2_score']:.0f} | M3: {expert['method3_score']:.0f}")

        return "\n".join(lines)

    def save_results(self, combined_ranking):
        """Save expert seeds."""
        # JSON file
        experts_file = self.output_dir / 'expert_seeds_datadriven.json'
        with open(experts_file, 'w') as f:
            json.dump({
                'metadata': {
                    'timestamp': '2026-04-01',
                    'purpose': 'Data-driven expert seed discovery for corpus expansion',
                    'methods': 3,
                    'unique_experts': len(combined_ranking)
                },
                'experts': combined_ranking
            }, f, indent=2)
        print(f"✓ Saved: {experts_file}")

        # Report
        report = self.generate_report(combined_ranking)
        report_file = self.output_dir / 'expert_seeds_discovery_report.md'
        with open(report_file, 'w') as f:
            f.write(report)
        print(f"✓ Saved: {report_file}")

    def run(self):
        """Execute all methods."""
        print("=" * 80)
        print("DATA-DRIVEN EXPERT SEED DISCOVERY")
        print("=" * 80)

        # Run three methods
        m1 = self.method1_top500_authors()
        m2 = self.method2_last_author_signal()
        m3 = self.method3_coauthorship_betweenness()

        print(f"\n✓ Method 1: {len(m1)} authors")
        print(f"✓ Method 2: {len(m2)} PI-level researchers")
        print(f"✓ Method 3: {len(m3)} bridge researchers")

        # Combine
        combined = self.generate_combined_ranking()

        # Save
        self.save_results(combined)

        # Summary
        print("\n" + "=" * 80)
        print("EXPERT SEED RANKING SUMMARY")
        print("=" * 80)

        top_experts = combined[:10]
        for i, expert in enumerate(top_experts, 1):
            print(f"\n{i}. {expert['name']}")
            print(f"   Score: {expert['combined_score']:.1f}")
            print(f"   Present in: {', '.join(expert['methods_present'])}")

if __name__ == '__main__':
    finder = DataDrivenExpertFinder()
    finder.run()
