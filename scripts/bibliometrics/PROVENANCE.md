# Provenance Record — NeuroTrailblazers Bibliometric Pipeline

**Snapshot date:** 2026-03-31  
**Data source:** OpenAlex API (https://api.openalex.org)  
**Contact header:** neurotrailblazers@example.com (polite pool, 9 req/s)  
**Pipeline version:** commit `8c3c14f` on branch `claude/bibliometric-connectomics-pipeline-f7ber`

---

## Corpus Statistics

| Metric | Value |
|--------|-------|
| Total papers (merged corpus) | 7,925 |
| Publication year range | 1909 – 2026 |
| Corpus A papers | ~2,400 (auto-seed + 2-hop expansion) |
| Corpus B papers | ~1,800 (keyword search) |
| Corpus C papers | ~4,500 (16 dataset anchors + citers) |
| Unique after deduplication | 7,925 |
| OpenAlex cache files | 17,441 |

## Graph Statistics

| Graph | Type | Nodes | Edges | File size |
|-------|------|-------|-------|-----------|
| Citation graph | Directed | 7,925 | 94,223 | 13 MB |
| Co-citation graph | Undirected, weighted | — | — | 26 MB |
| Bibliographic coupling | Undirected, weighted | — | — | 194 MB |
| Co-authorship graph | Undirected, weighted | 35,947 | 514,301 | 73 MB |

## Analysis Outputs

| Output | Count/Size |
|--------|-----------|
| Paper rankings (composite score) | Top 2,000 |
| Author rankings (composite score) | Top 1,000 |
| Louvain communities | 30 |
| Reading list (noise-filtered, topo-sorted) | 500 papers |
| OCAR study cards | 200 papers (top 200 by composite score) |
| OCAR cache entries | 322 |
| Author merge groups | 17 confirmed |

---

## File Checksums (MD5)

| File | MD5 | Size |
|------|-----|------|
| `output/provenance_20260331.tar.gz` | `301dceb31cfbedab552b5fb3db423732` | 38 MB |
| `cache_snapshot_20260331.tar.gz` | `4572bf6c33708bcd317d1175a9bc874c` | 74 MB |
| `output/graphs/citation_graph.json` | `ab84f5fac309386a33e7a590e0008c42` | 13 MB |

### Verify checksums
```bash
md5sum output/provenance_20260331.tar.gz cache_snapshot_20260331.tar.gz output/graphs/citation_graph.json
```

---

## Archive Contents

### `output/provenance_20260331.tar.gz` (38 MB)
All pipeline outputs frozen at snapshot date:
```
output/graphs/citation_graph.json        — directed citation graph
output/graphs/coauthorship_graph.json    — author co-authorship graph
output/graphs/cocitation_graph.json      — paper co-citation graph
output/graphs/coupling_graph.json        — bibliographic coupling graph
output/corpus_a.json                     — Corpus A (auto-seed)
output/corpus_b.json                     — Corpus B (keyword search)
output/corpus_c.json                     — Corpus C (dataset-anchored)
output/corpus_merged.json                — deduplicated merged corpus
output/paper_rankings.json               — top 2,000 by composite score
output/author_rankings.json              — top 1,000 by composite score
output/communities.json                  — 30 Louvain communities
output/citation_baseline.json            — top 200 by raw citation count
output/reading_list.json                 — 500-paper reading list
output/reading_list_enriched.json        — + in_degree, out_degree, core_number
output/ocar_entries.json                 — 200 OCAR cards (JSON)
output/ocar_entries.yaml                 — 200 OCAR cards (YAML schema)
output/strategic_audit.json              — 329 flagged papers across 5 lenses
output/validation_report.json            — expert recall, corpus triangulation
output/author_merge_map.json             — 17 confirmed author merge groups
output/expert_list_gaps.json             — 48 expert papers not in top-500
output/high_indegree_omissions.json      — 100 high-indegree omissions
```

### `cache_snapshot_20260331.tar.gz` (74 MB)
17,441 OpenAlex API response files (`cache/works/W*.json`).  
Enables fully deterministic re-runs of all pipeline steps without API calls.  
Extract to `scripts/bibliometrics/cache/` before running.

---

## Reproducing the Analysis

### From cache (deterministic, no API calls)
```bash
git clone <repo>
cd scripts/bibliometrics

# Restore cache snapshot
tar -xzf cache_snapshot_20260331.tar.gz

# Restore full outputs
tar -xzf output/provenance_20260331.tar.gz

# Or re-run pipeline from scratch using cached API responses
pip install -r requirements.txt
bash run_pipeline.sh
```

### From scratch (requires internet, results may differ as OpenAlex updates)
```bash
pip install -r requirements.txt
bash run_pipeline.sh
python 09_graph_analysis.py
python 10_apply_merges.py
python 11_strategic_audit.py

# OCAR generation (top 200)
export ANTHROPIC_API_KEY=sk-ant-...
python 08_generate_ocar.py
```

---

## Key Algorithmic Parameters

| Parameter | Value | Location |
|-----------|-------|----------|
| OpenAlex request rate | 9 req/s | `config.py` |
| Citation expansion hops | 2 | `config.py` |
| Min seed connections | 2 | `config.py` |
| Marginal gain threshold | 5% | `config.py` |
| Max corpus size | 5,000 | `config.py` |
| PageRank damping (α) | 0.85 | `03_compute_metrics.py` |
| Betweenness k-approximation | 500 | `03_compute_metrics.py` |
| Louvain random seed | 42 | `03_compute_metrics.py` |
| Composite score weights | 0.35 PR + 0.25 cites + 0.20 betw + 0.20 recent PR | `03_compute_metrics.py` |
| Reading list size | 500 | `06_reading_list.py` |
| OCAR model | claude-sonnet-4-6 | `08_generate_ocar.py` |
| K-core inner threshold | k ≥ 0.9 × k_max (k ≥ 28) | `09_graph_analysis.py` |

## Reproducibility Caveats

1. **OpenAlex data drifts daily.** Citation counts, author disambiguation, and
   concept assignments change as OpenAlex ingests new records. Use the cache
   snapshot for exact reproduction.

2. **Louvain is non-deterministic** beyond `seed=42`. If graph structure changes
   (different corpus), community IDs and labels may shift. Refer to communities
   by top-concept labels, not integer IDs.

3. **Betweenness approximation** (k=500) introduces ~5% error vs. exact computation.
   Exact betweenness on the 35,947-node co-authorship graph is infeasible at runtime.

4. **Author name disambiguation** is imperfect in OpenAlex. The 17 merge groups
   in `author_merge_map.json` were manually verified. Additional fragmentation
   almost certainly exists for authors with non-ASCII names or frequent name changes.

5. **OCAR generation** is non-deterministic (language model sampling). The
   `output/ocar_cache/` directory preserves the exact generated entries.
   Re-running `08_generate_ocar.py` against the same papers will produce
   semantically similar but textually different output.

6. **Abstract coverage**: ~72% of corpus papers have abstracts in OpenAlex
   (`abstract_inverted_index`). The remaining 28% were generated from title +
   OpenAlex concepts only.
