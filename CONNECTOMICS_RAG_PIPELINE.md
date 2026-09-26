# Connectomics RAG Pipeline: End-to-End Strategy

**Status:** Implemented end-to-end k-core filtering strategy for NeuroTrailblazers connectomics corpus.

## Overview

The connectomics RAG pipeline uses **principled, topology-based corpus selection** built on a complete bibliometric analysis pipeline. The strategy is three-tiered and based on **k-core decomposition**, a graph-theoretic measure of structural embeddedness.

```
┌─────────────────────────────────────────────────────────────────┐
│ OpenAlex Data Collection (3 independent corpora)               │
│ → 7,925 papers, 94,223 citation edges                          │
└──────────────────────┬──────────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────────┐
│ Graph Analysis: K-Core Decomposition                           │
│ → Maximum k-core: 32                                            │
│ → Natural inflection point at k=25                              │
└──────────────────────┬──────────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
    ┌────────┐   ┌──────────┐   ┌────────┐
    │TIER 1  │   │TIER 2    │   │TIER 3  │
    │k≥32    │   │k≥25 ⭐   │   │k≥20    │
    │213 pp  │   │1,064 pp  │   │2,074pp │
    └────────┘   └──────────┘   └────────┘
    Ultra-core   PRIMARY        Bridge +
    seminal      main analysis  emerging
    foundations
        │              │              │
        │              ▼              │
        │         ┌─────────────┐    │
        │         │ RAG Corpus  │    │
        │         │ 1,064 pp    │    │
        │         │ 794 PDFs    │    │
        │         │ (74%)       │    │
        │         └─────────────┘    │
        │                            │
        │         Journal Club   ────┘
        │         (k=20-24)
        │         236 candidates
```

## Three-Tier Strategy

### TIER 1: Ultra-Core (k ≥ 32) – Seminal Papers
- **Papers:** 213
- **% of corpus:** 2.7%
- **Use case:** Essential foundational work, landmark datasets
- **Characteristics:** Highest citation density, well-established methods
- **Risk:** Too narrow for broad field understanding

### TIER 2: EM Connectomics Core (k ≥ 25 + in-degree ≥ 2) ⭐ **PRIMARY**
- **Papers:** 959 (45% of full corpus)
- **% of corpus:** 12.1%
- **Use case:** **Main analysis corpus for RAG training**
- **PDF Coverage:** 730/959 (76%)
- **Criteria:**
  - K-core ≥ 25 (structurally embedded in dense subgraph)
  - In-degree ≥ 2 (cited by at least 2 other papers in corpus)
- **Characteristics:**
  - Natural inflection point in k-core cumulative distribution
  - Balances structural rigor with citation validation
  - Community-recognized as important (multiple internal citations)
  - Dense core papers only (excludes papers not yet validated internally)
- **Rationale:** K-core captures topology; in-degree≥2 adds empirical validation that papers are recognized by other corpus papers. The CDF shows steep rise at k≥25 (213→548→939→1,064 as k goes from 32→27→26→25), but we require multiple internal citations to filter to high-confidence core only.

### Emerging Watch List (k ≥ 25 + Top 500 + 2024+ + in-degree < 2) 🚀
- **Papers:** 22
- **Use case:** Track cutting-edge work not yet validated by multiple citations
- **Criteria:**
  - K-core ≥ 25 (structurally important)
  - Ranked in top 500 (high composite score)
  - Published 2024 or later (cutting-edge)
  - In-degree < 2 (not yet widely cited within corpus)
- **Characteristics:**
  - Emerging techniques and applications
  - Rapid adoption (being cited heavily)
  - Rising authors/labs in connectomics
- **Monitoring:** Quarterly check for promotion to PRIMARY if in-degree≥2

### TIER 3: Core + Bridge (k ≥ 20) – Reference
- **Papers:** 2,074 (83% of full corpus)
- **% of corpus:** 26.2%
- **Use case:** Reference set for external citation resolution
- **Characteristics:**
  - All papers in k≥25 PLUS bridge papers from k=20–24 zone
  - Includes emerging work (in-degree < 2) and specialized subfields
- **Risk:** Less validation signal; includes peripheral work

## Implementation: Refined K-Core + Citation Validation

### PRIMARY Corpus Selection
**For RAG Training:** Use `corpus_primary_validated.json`

**Criteria:**
- K-core ≥ 25 (structurally embedded)
- In-degree ≥ 2 (cited by ≥2 papers in corpus)

**Output:**
- 959 papers with full metadata
- PDF availability indicators (76% with direct links)
- Composite ranking scores, k-core values, in-degree counts
- Community-validated core literature only

**Example PRIMARY Corpus Paper:**
```json
{
  "title": "Connectome-constrained networks...",
  "doi": "10.1038/nature12346",
  "k_core": 25,
  "composite_score": 0.487,
  "in_degree_actual": 8,
  "pdf_available": true,
  "access_type": "direct",
  "rank_position": 42
}
```

### Emerging Watch List
**For Monitoring:** Use `emerging_papers_watch_list.json`

**Criteria:**
- K-core ≥ 25, Top 500 ranked, 2024+, In-degree < 2
- 22 papers identified as rising work
- 18/22 with direct PDF access (82%)

**Example Emerging Paper:**
```json
{
  "title": "Synaptic-resolution connectomics: towards large brains...",
  "year": 2025,
  "rank": 31,
  "composite_score": 0.246,
  "k_core": 25,
  "in_degree": 1,
  "importance_flags": ["top-50-ranked", "high-composite-score"],
  "pdf_available": false
}
```

### Journal Club Enhancement: Bridge Zone Selection
**Papers from k=20–24 not in TIER 2:**
- 236 candidates identified using heuristic inclusion scoring
- Selection criteria:
  1. **High ranking:** Papers ranked in top 500 by composite score
  2. **Recency:** Published 2021+ (emerging work signal)
  3. **Citation velocity:** Strong composite score despite lower k-core
  4. **Author diversity:** Rising authors, new labs entering connectomics

**Top Journal Club Candidates:**
1. "Neurons on tape: Automated Tape Collecting..." (2023, rank 377)
2. "Array tomography: trails to discovery..." (2024, rank 367)
3. "Current Progress in Expansion Microscopy..." (2023, rank 232)

## PDF Access Strategy

### Coverage by Access Type
**TIER 2 (k ≥ 25) Coverage:** 794/1,064 papers (74%)

**Paper Accessibility:**
- **Direct Links:** 5,837 papers (77% of full corpus)
  - PubMed Central: ~3,439 papers
  - Preprints (bioRxiv): ~2,398 papers
  - Publisher direct access: Variable
- **Accessible URLs (potentially scrapeable):** 939 papers (12%)
- **Behind paywalls:** ~1,728 papers (23%)
  - Many have institutional access through university networks
  - Some available through preprint servers with institutional delay

### PDF Discovery Pipeline
```
scripts/find_pdfs_fast.py      → Heuristic scan (seconds)
scripts/check_unpaywall.py      → Unpaywall API check (8 workers)
scripts/check_pmc_availability.py → PMC availability check
scripts/check_doi_access.py     → DOI URL validation
```

## Pipeline Architecture

The end-to-end pipeline consists of three phases:

### Phase 1: Data Harvesting (Steps 1-2)
```bash
bash scripts/bibliometrics/run_pipeline.sh --from 1
```
- **Step 1:** Harvest from OpenAlex (3 independent corpora)
- **Step 2:** Build citation, co-citation, coupling, and co-authorship graphs
- **Output:** 7,925 papers, 94,223 citation edges

### Phase 2: Analysis & Metrics (Steps 3-7)
```bash
bash scripts/bibliometrics/run_pipeline.sh --from 3
```
- **Step 3:** Compute centrality metrics (PageRank, HITS, betweenness)
- **Step 4:** Validate corpus against expert data
- **Step 5:** Generate interactive visualizations
- **Step 6:** Create prerequisite-ordered reading list
- **Step 7:** Generate field evolution timeline

### Phase 3: K-Core Selection & Enhancement (Steps 9+)
```bash
bash scripts/bibliometrics/run_pipeline.sh --from 9
python3 scripts/implement_kcore_strategy.py
```
- **Step 9:** K-core decomposition and degree distribution analysis
- **Step 10-14:** QA/QC phases (dedup, author merges, strategic audit)
- **Custom:** Implement TIER 2 selection with PDF metadata

## Usage for RAG Pipeline

### Building RAG from PRIMARY Corpus
```python
import json

# Load PRIMARY validated corpus (K≥25 + in-degree≥2)
with open('scripts/bibliometrics/output/corpus_primary_validated.json') as f:
    corpus = json.load(f)

papers = corpus['papers']  # 959 papers

# Filter to papers with PDFs for embedding
papers_with_pdfs = [p for p in papers if p['pdf_available']]
# → 730 papers ready for PDF download and chunking

# Emerging watch list for monitoring
with open('scripts/bibliometrics/output/emerging_papers_watch_list.json') as f:
    watch = json.load(f)

emerging = watch['papers']  # 22 papers to monitor
```

### RAG Index Strategy
1. **Primary Core (959 papers):** Embed all validated papers in RAG index
2. **PDFs Available:** Download 730 papers, chunk, and embed
3. **Emerging Watch List (22 papers):** Monitor quarterly for promotion to primary
4. **Fallback References:** Use full corpus (7,925) for external citation resolution

## Maintenance & Updates

### Quarterly Update Cycle
1. **Re-harvest:** Run step 1 to pull new papers
2. **Recompute:** Run step 2-3 to rebuild graphs
3. **Reselect:** Re-run k-core decomposition (step 9)
4. **Promote:** Move papers from journal club to TIER 2 if they reach k=25
5. **Regenerate:** Rebuild RAG indices with new papers

### Monitoring for Corpus Growth
**Example: Paper "Emerging connectomics technique" (2024)**
- Initial state: Ranked #450, composite_score=0.18, k-core=22 → Journal club
- 6 months later: k-core=25 (cited by 3+ papers) → **Promote to TIER 2**
- Update: `corpus_tier2_primary.json` and rebuild RAG index

## Comparison with Alternative Approaches

### Why K-Core Over Simple Degree Threshold?
**Alternative approach (not used):** Degree ≥ 5 + in-degree ≥ 2
- Results: 3,808 papers (too broad, reduced coherence)
- Issue: Doesn't account for structural embeddedness
- Problem: A paper citing many unconnected papers scores high despite poor integration

**K-Core advantage:**
- K-core value = degree within induced subgraph (papers citing/cited by other high-k papers)
- Natural inflection point at k=25 identified via CDF analysis
- Statistically principled: accounts for dense clustering
- Result: 1,064 papers (coherent, well-validated core)

### Why Not Just Top 500 Ranked Papers?
**Alternative approach (not used):** Select top-500 by composite score
- Results: Misses important papers outside top-500 (some have k≥25 but lower ranking score)
- Issue: Ranking weights (PageRank, HITS, betweenness) can favor breadth over depth
- Problem: Recent papers with fewer citations underrepresented

**K-Core advantage:**
- Topology-first: embeddedness indicates field integration
- Captures both central and emerging work
- Natural complement to ranking-based selection

## Files Generated

| File | Description |
|------|-------------|
| `corpus_primary_validated.json` | ⭐ PRIMARY corpus (959 papers, k≥25 + in-degree≥2, 76% PDF) |
| `emerging_papers_watch_list.json` | 🚀 Emerging papers to monitor (22 papers, k≥25 + top-500 + 2024+ + in-degree<2) |
| `corpus_refinement_report.md` | Detailed analysis of refinement decision |
| `corpus_tier2_primary.json` | TIER 2 unfiltered (1,064 papers, k≥25 only) |
| `journal_club_candidates_kcore.json` | Bridge zone candidates (236 papers from k=20-24) |
| `kcore_implementation_report.md` | Initial k-core analysis summary |
| `KCORE_FILTERING_STRATEGY.md` | Strategy document (theoretical foundation) |
| `corpus_kcore_20.json` | TIER 3 papers (k≥20, all 2,074) |
| `corpus_kcore_25.json` | TIER 2 papers (k≥25, all 1,064) |
| `corpus_kcore_32.json` | TIER 1 papers (k≥32, all 213) |

## Integration Checklist

- [x] K-core decomposition (generated by pipeline step 9)
- [x] In-degree calculation from citation graph
- [x] PRIMARY corpus refinement (K≥25 + in-degree≥2): 959 papers
- [x] Emerging watch list identification: 22 papers
- [x] PDF availability mapping (connectomics_papers_pdf_index.json)
- [x] Implementation report generation (corpus_refinement_report.md)
- [ ] Download PDFs for 730 PRIMARY papers with direct links
- [ ] Chunk and embed papers into RAG vector database
- [ ] Set up quarterly update monitoring
- [ ] Document promotion criteria (in-degree<2 → in-degree≥2)

## Next Steps for RAG Integration

1. **Download phase:** Use PDF links for 794 accessible papers
2. **Chunking phase:** Split papers into semantic chunks with citation context
3. **Embedding phase:** Embed chunks using connectomics-aware embeddings
4. **Indexing phase:** Build RAG index with TIER 2 papers
5. **Monitoring phase:** Track journal club candidates for quarterly promotion

## References

- **K-Core Theory:** Batagelj, V., & Zaversnik, M. (2003). "An O(m) Algorithm for Cores Decomposition of Networks"
- **Field-Specific Application:** See KCORE_FILTERING_STRATEGY.md for connectomics-specific rationale
- **Pipeline Details:** See scripts/bibliometrics/README.md for full pipeline documentation

---

**Generated:** 2026-04-01  
**Strategy:** K-Core + Citation Validation (Refined Tiered Approach)  
**PRIMARY Corpus:** K≥25 + In-degree≥2 with 959 papers and 76% PDF coverage (730 PDFs)  
**Emerging Watch List:** 22 papers (k≥25, top-500, 2024+, in-degree<2)  
**Implementation:** Scripts in `scripts/bibliometrics/output/`
