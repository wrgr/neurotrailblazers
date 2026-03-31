# Bibliometric Connectomics Pipeline

A principled, reproducible pipeline that maps the EM connectomics literature using
OpenAlex citation data. It constructs three independent paper corpora, builds four
graph representations, computes centrality metrics, detects communities, generates
a prerequisite-ordered reading list, and produces structured OCAR study cards for
the top 200 papers.

**Key statistics (current run):**
- 7,925 papers in merged corpus
- 94,223 directed citation edges
- 35,947 author nodes, 514,301 co-authorship edges
- 30 Louvain communities
- Top-500 reading list (noise-filtered)
- 200 OCAR cards (full + plain-language versions)

---

## Quick Start

### Automatic Pipeline (requires OpenAlex access)

```bash
cd scripts/bibliometrics

# Install dependencies
pip install -r requirements.txt

# Run the full pipeline (steps 1–7)
bash run_pipeline.sh

# Resume from a specific step
bash run_pipeline.sh --from 3

# Generate OCAR cards for top 200 (requires ANTHROPIC_API_KEY or run via Claude agents)
export ANTHROPIC_API_KEY=sk-ant-...
python 08_generate_ocar.py

# Extended analysis: k-cores, degree distributions, expert gaps
python 09_graph_analysis.py

# Strategic audit report (now includes domain labels)
python 11_strategic_audit.py
```

### QA/QC Workflow (no OpenAlex needed; uses cached data)

```bash
# Step 1: Detect duplicates (requires human review)
python 12_dedup_review.py
# → Edit output/duplicate_review.tsv and output/author_dedup_review.tsv

# Step 2: Apply accepted merges
python 12_apply_duplicate_merges.py

# Step 3: Analyze review citations (uses cached data)
python 13_review_citations.py

# Step 4: Compile inclusion decisions
python 13_inclusion_decisions.py

# Step 5: Final orchestration and metadata
python 14_update_corpus_and_rerank.py

# Output: inclusion_metadata.json (inclusion source & criteria for each paper)
```

See `streamlined_plan.md` for detailed QA/QC workflow documentation.

---

## Pipeline Architecture

| Step | Script | Input | Output | Description |
|------|--------|-------|--------|-------------|
| 1 | `01_harvest.py` | OpenAlex API | `corpus_{a,b,c}.json`, `corpus_merged.json` | Build three independent corpora, merge |
| 2 | `02_build_graphs.py` | `corpus_merged.json` | `graphs/*.json` | Build citation, co-citation, coupling, co-authorship graphs |
| 3 | `03_compute_metrics.py` | graphs, corpus | `paper_rankings.json`, `author_rankings.json`, `communities.json` | Centrality, PageRank, community detection, composite scores |
| 4 | `04_validate.py` | rankings, expert data | `validation_report.json` | Expert recall, corpus triangulation |
| 5 | `05_html_report.py` | rankings, communities | `field_map.html` | Interactive D3 visualization |
| 6 | `06_reading_list.py` | rankings, communities | `reading_list.json`, `reading_list.md` | Prerequisite-ordered reading list |
| 7 | `07_evolution_graph.py` | corpus, communities | `evolution_graph.html` | Timeline of field evolution |
| 8 | `08_generate_ocar.py` | `reading_list.json` | `ocar_entries.{json,yaml}` | OCAR study cards via Claude |
| 9 | `09_graph_analysis.py` | graphs, rankings | `reading_list_enriched.json`, `*_gaps.json` | K-cores, degree distributions, expert gap analysis |
| 10 | `10_apply_merges.py` | corpus, rankings | `author_merge_map.json` | Apply verified author name merges |
| 11 | `11_strategic_audit.py` | all outputs | `strategic_audit.{json,md}` | Flag papers needing human review |
| 12 | `12_dedup_review.py` | corpus, graphs | `duplicate_review.{tsv,md}`, `author_dedup_review.tsv` | Multi-signal duplicate + author dedup detection |
| 12b | `12_apply_duplicate_merges.py` | dedup TSV (with decisions), corpus, graphs | `corpus_deduplicated.json`, `duplicate_merge_log.json` | Apply human-approved duplicate merges |
| 13 | `13_review_citations.py` | reading_list, graph (cached) | `review_citations.json`, `review_cited_candidates.json` | Analyze review paper citations |
| 13b | `13_inclusion_decisions.py` | review_cited, expert_gaps, duplicates | `inclusion_decisions.json` | Compile inclusion candidates with criteria |
| 14 | `14_update_corpus_and_rerank.py` | all decision files | `inclusion_metadata.json`, `domain_labels.json` | Orchestrate all QA/QC phases, final stats |
| + | `classify_domain.py` | graphs | `domain_labels.json` | Multi-signal domain classification (journal + concepts + keywords) |

---

## Step 1 — Data Collection

### Three Independent Corpora

The pipeline uses **data triangulation** across three independent collection strategies,
following the methodology of Marzi et al. (2025). Agreement across corpora signals
robust, field-central papers; corpus-unique papers may be emerging or niche.

#### Corpus A: Auto-Seed + Citation Expansion

1. **Seed phase** — 19 OpenAlex queries (`config.AUTO_SEED_QUERIES`):
   - 1 concept-filter query (OpenAlex concept ID for "connectomics")
   - 18 title-keyword queries covering: connectomics, FIB-SEM, SBEM, serial-section TEM,
     expansion microscopy, MAPseq/BARseq, array tomography, flood-filling networks,
     synapse detection, graph theory

2. **Citation expansion** — up to 2 hops from seeds:
   - A discovered paper is retained if cited/referenced by **≥ 2 seed papers**
   - Each paper yields at most 200 forward-citation neighbors (`EXPANSION_MAX_CITED_BY = 200`)
   - Expansion stops when marginal gain < 5% new papers per hop, or corpus reaches 5,000 papers

3. **Macro-connectomics filter** — papers matching dMRI/fMRI terms (`diffusion mri`,
   `fmri`, `resting state`, `tractography`, `bold`, etc.) are removed *unless* they also
   contain a nanoscale indicator (`electron microscopy`, `synapse`, `connectome`, etc.)

#### Corpus B: Keyword Search

14 full-text keyword queries against OpenAlex:
- Filters: `publication_year > 1985`, `cited_by_count > 5`, max 200 results per query
- Queries cover: `"connectome" OR "connectomics"`, `"serial section electron microscopy" neuron`,
  `"FlyWire" OR "hemibrain" OR "MICrONS" OR "H01"`, `"MAPseq OR BARseq connectivity"`, etc.

#### Corpus C: Dataset-Anchored

16 landmark papers are hardcoded as anchors (DOIs in `config.py`), including FlyWire
(Dorkenwald 2024), Hemibrain v1.2 (Scheffer 2020), FAFB (Zheng 2018), H01 human cortex
(Shapson-Coe 2024), MICrONS, larval Drosophila (Winding 2023), C. elegans (Witvliet 2021),
flood-filling networks (Januszewski 2018), CATMAID, webKnossos, CAVE, neuPrint, BossDB,
Kasthuri cortex (2015), White C. elegans (1986), SBEM (Denk & Horstmann 2004).

For each anchor: the paper itself + up to 500 papers citing it (`DATASET_MAX_CITERS = 500`).

#### Merge

All three corpora deduplicated by `openalex_id`. Each paper carries provenance tag
`{"a": bool, "b": bool, "c": bool}`.

---

## Step 2 — Graph Construction

### Citation Graph (Directed)
- A → B if paper A lists B in `referenced_works` and both are in corpus
- **7,925 nodes, 94,223 edges**
- Used for PageRank, HITS, betweenness, k-core decomposition

### Co-Citation Graph (Undirected, Weighted)
- Edge (A, B) if ≥ 2 corpus papers cite both A and B together
- Edge weight = co-citation count; minimum weight threshold: 2

### Bibliographic Coupling Graph (Undirected, Weighted)
- Edge (A, B) if A and B share ≥ 2 references
- Edge weight = shared reference count
- Output (~194 MB) is gitignored

### Co-Authorship Graph (Undirected, Weighted)
- Nodes: authors (by OpenAlex author ID)
- Edge (A, B) for every pair of co-authors on a corpus paper
- Edge weight = number of jointly authored papers
- **35,947 nodes, 514,301 edges** (~72 MB; gitignored)

All graphs saved as D3 node-link JSON (`networkx.readwrite.json_graph.node_link_data`).

---

## Step 3 — Metrics & Rankings

### Paper Role Classification

```
if "review" or "survey" in title        → review
elif dataset keyword count ≥ 2          → dataset
elif biology_score > methods_score      → biology
else                                    → methods
```

### Domain Classification (Multi-Signal)

Applied to all 7,925 papers to identify research area:

| Layer | Coverage | Signal | Priority |
|-------|----------|--------|----------|
| **Journal name** | 97% | Map to domain (eLife → em_connectomics, NeuroImage → mri, etc.) | Strongest |
| **OpenAlex concepts** | 30% | Named entities like "Drosophila", "connectomics", "scale-free networks" | Tie-breaker |
| **Title keywords** | 100% | Pattern matching on title + abstract | Fallback |

**Output domain labels:**
- `em_connectomics` — 28% (2,227 papers) — electron microscopy connectomics
- `neuroscience` — 18% (1,464 papers) — general neuroscience (not connectomics-specific)
- `mri_connectomics` — 6% (465 papers) — macro-scale (dMRI, fMRI, structural)
- `methods_ml` — 4% (323 papers) — computer vision, machine learning, tools
- `network_science` — 2% (167 papers) — graph theory, complex networks
- `off_topic` — 5% (377 papers) — cancer statistics, geophysics, pharmacology, etc. (noise)
- `unknown` — 37% (2,902 papers) — big-tent journals (Nature/Science/bioRxiv) with generic titles

**Why multi-signal?** Title-keyword matching alone is brittle. Journal name is fast and reliable.
Concepts add precision. Together they achieve ~95% accuracy on labeled samples.

### Graph Centrality (Citation Graph)

| Metric | Function | Parameters | Interpretation |
|--------|----------|------------|----------------|
| PageRank | `nx.pagerank()` | α = 0.85 | Global structural importance |
| HITS hubs | `nx.hits()` | max_iter=200 | Reviews/surveys (cite many important works) |
| HITS authorities | `nx.hits()` | max_iter=200 | Landmark results (cited by important works) |
| Betweenness | `nx.betweenness_centrality()` | k=500 for n>2,000 | Bridge papers between clusters |
| In-degree | `citation_graph.in_degree()` | — | Within-corpus citation count |
| Recent PageRank | `nx.pagerank()` on 2020+ subgraph | α=0.85 | Current relevance |

The **k=500 betweenness approximation** samples 500 random source nodes for
shortest-path computation when the graph exceeds 2,000 nodes. This reduces runtime
from hours to seconds with ~5% error vs. exact computation.

### Author Centrality (Co-Authorship Graph)

| Metric | Notes |
|--------|-------|
| Weighted degree | Sum of co-authorship edge weights |
| Betweenness | k=500 approximation (graph has 35,947 nodes) |
| Eigenvector centrality | max_iter=500; set to 0 on convergence failure |

### Community Detection

**Louvain modularity optimization** (`nx.community.louvain_communities`):
- Random seed: **42** (reproducibility)
- Applied to undirected citation graph
- Minimum community size: 3 members
- **30 communities** found
- 3 are pure noise (geology, mass spectrometry, autophagy) — filtered in reading list step

### Composite Scores

**Paper:**
```
score = 0.35 × (pagerank / max_pr)
      + 0.25 × (total_citations / max_cites)
      + 0.20 × (betweenness / max_betw)
      + 0.20 × (recent_pagerank / max_recent_pr)
```

**Author:**
```
score = 0.35 × (total_pagerank / max)
      + 0.25 × (betweenness / max)
      + 0.20 × (weighted_degree / max)
      + 0.20 × (recent_paper_count / max_paper_count)
```

Top **2,000 papers** and **1,000 authors** saved to rankings files.

---

## Step 6 — Reading List

### Filtering

Only papers from **noise communities** (geology, seismology, mass spectrometry,
autophagy, chromatography) are excluded. Methods papers, MRI/fMRI, general CV,
and graph theory are retained — all are legitimate signal in a connectomics
education context. Of 2,000 ranked papers: 33 removed, 1,967 pass.

### Selection

Top **500 by composite score** from survivors.

### Topological Sort (Kahn's BFS)

Papers are reordered so prerequisites appear before the papers that cite them:

```
1. Build citation subgraph restricted to the 500 selected papers
2. Compute in-degree within this subgraph for each paper
3. Queue: papers with in-degree 0, sorted by (year, role_priority)
   role_priority = {review:0, methods:1, dataset:2, biology:3}
4. Pop lowest-priority paper → emit → decrement successors' in-degrees
5. Papers reaching in-degree 0 join the queue
6. Remaining papers (cycles) appended sorted by year
```

### Reading Phases

| Phase | Label | Criteria |
|-------|-------|----------|
| 0 | Orientation | role = review |
| 1 | Foundations | year < 2010 |
| 2 | Core Methods | methods/biology, 2010–2020 |
| 3 | Landmark Datasets | role = dataset, any year |
| 4 | Frontiers | year ≥ 2021 |

Current: 88 orientation · 173 foundations · 176 core methods · 4 datasets · 59 frontiers.

---

## Step 8 — OCAR Study Cards

**OCAR** = Opportunity / Challenge / Action / Resolution (+ future_work)

Each card also includes:
- `plain_language_summary` — 2–3 sentences for a general audience, with analogy if helpful
- `summaries.beginner / .intermediate / .advanced` — tiered by background
- `discussion_prompts` — 3 journal-club questions specific to the paper
- `dimension` — one of: `connectomics | image-acquisition | segmentation | proofreading | graph-analysis | neuroanatomy | cell-types | infrastructure | neuroai | methods-general | review`
- `tags` — up to 6, format `category:term` (e.g. `imaging:fib-sem`, `species:drosophila`)

Generated for the **top 200 papers by composite score**. Per-paper results cached to
`output/ocar_cache/{openalex_id}.json` — generation is fully resumable.

Output `ocar_entries.yaml` matches `_data/journal_papers.yml` schema and can be
appended directly.

**To run**: `export ANTHROPIC_API_KEY=sk-ant-... && python 08_generate_ocar.py`
Alternatively, generate via Claude Code agents (no separate API key needed).

---

## Step 9 — Extended Graph Analysis

### K-Core Decomposition

Applied to the undirected citation graph (self-loops removed). A node's **core number**
is the highest k such that it remains in a subgraph where every node has degree ≥ k.
High core number = deeply embedded in the network's dense nucleus.

- Maximum k in current run: **32**
- Inner core (k ≥ 28): **402 papers**
- k=32 shell is dominated by the fMRI/MRI connectomics community (tight cross-citation cluster)
- EM connectomics papers occupy k=28–31

### Degree Distribution

In-degree (cited within corpus) and out-degree (references within corpus) annotated
on all reading-list papers. Papers with in-degree ≥ 30 outside the top 500 are flagged
as potential omissions (`high_indegree_omissions.json`).

---

## Step 10 — Author Name Merges

OpenAlex assigns separate author IDs when a name appears differently across papers
(hyphenation variants, initials vs. full name, unicode dashes). This inflates author
counts and suppresses composite scores for affected researchers.

### Confirmed Merges (17 groups)

| Canonical | Aliases | Evidence |
|-----------|---------|----------|
| William Gray-Roncal | William Gray Roncal, W.R. Gray Roncal, William R. Gray-Roncal, Will Gray-Roncal | User-confirmed; 5 OpenAlex IDs |
| Shin-ya Takemura | Satoko Takemura | 13 shared consortium papers |
| Alexander Shakeel Bates | Alexander S. Bates | 1 shared paper + full name present |
| Gregory S.X.E. Jefferis | G Jefferis, Gregory S. X. E. Jefferis | Abbreviation + shared papers |
| H. Sebastian Seung | H Sebastian Seung | Abbreviation |
| Olaf Sporns | O Sporns | Abbreviation |
| Moritz Helmstaedter | M Helmstaedter | Abbreviation |
| Davi D. Bock | D Bock | Abbreviation |
| Marta Costa | M Costa | Abbreviation |
| Casey M. Schneider-Mizell | Casey M Schneider-Mizell | Trailing period |
| Wei-Chung Allen Lee | Wei-Chung Lee, W.C.A. Lee | Abbreviation |
| C. Shan Xu | C Shan Xu, Shan Xu | Abbreviation |
| Thomas Müller-Reichert | Thomas Müller‐Reichert (en-dash) | Unicode normalization |
| Adam A. Atanas | Adam A Atanas | Trailing period |
| Mark W. Moyle | Mark W Moyle | Trailing period |
| Christopher J. Potter | Christopher J Potter | Trailing period |
| Chun-Chieh Lin | Chun‐Chieh Lin (en-dash) | Unicode normalization |

**Impact example — William Gray-Roncal**: Before merge, fragmented across 5 OpenAlex
IDs, effectively invisible in author rankings. After merge: **34 papers in corpus,
#47 by paper count, #205 by total citation sum** (1,886). His citation rank relative
to paper count reflects an infrastructure-heavy portfolio (BossDB, Open Connectome,
NeuVue, DotMotif) vs. the biology flagship papers that dominate the top-50.

### Finding New Merge Candidates

`author_merge_suggestions.json` (generated by the analysis) uses two signals:
1. **Jaccard similarity on paper sets** — same person should have overlapping paper sets
2. **Coauthor last-name overlap** — same person shares coauthors across name variants

Only pairs with shared papers > 0 OR (abbreviation match AND coauthor_sim > 0.4) are
reported. Always verify candidates before adding to the merge table.

---

## Step 11 — Strategic Audit

Five lenses for identifying papers outside the top 200 that warrant human review:

| Lens | Count | Description |
|------|-------|-------------|
| A1: Expert, in corpus, ranked below 500 | 20 | Promote candidates: connectome fingerprinting (2,967 ext. cites), NBS (2,779), connectome disorders (1,757) |
| A2: Expert, not in corpus | 28 | Require manual DOI seeding into `EXTRA_SEED_DOIS` + re-run |
| B: High in-degree, outside top 500 | 50 | Cited ≥30× within corpus; top neuro: en-bloc staining (171), zebrafish whole-brain EM (154), iterative ExM (137) |
| C1: High ext-cites / low composite | 197 | Large external citation count but weak corpus signal; mostly off-topic (cryo-EM, FieldTrip, WHO classification) |
| C2: Off-topic or unknown domain | 14 | Papers classified as `off_topic` or `unknown` with weak neuro signal; noise to filter |
| D: k-core inversions (k≥30, rank 201–500) | 34 | Structurally central graph theory papers ranked lower than expected |

---

## Steps 12–14 — Quality Assurance & Corpus Enhancement

These three orchestrated steps apply statistical criteria to accept/flag decisions and optionally
expand the corpus with high-confidence additions.

### Step 12 — Duplicate Detection & Merging

**Scripts:** `12_dedup_review.py`, `12_apply_duplicate_merges.py`

**Duplicate detection method:** 5-signal classifier:

| Signal | Weight | Interpretation |
|--------|--------|-----------------|
| Title similarity (fuzzy Levenshtein) | 0.35 | Fast, high precision for exact duplicates |
| Citation neighborhood Jaccard | 0.25 | Do they cite/are-cited-by the same papers? |
| Author overlap | 0.15 | Shared authors; controls for name collisions |
| Mutual non-citation | 0.15 | Same year + unique refs = likely same paper |
| Preprint DOI pattern | 0.10 | arXiv/bioRxiv IDs suggest preprint version |

**Confidence tiers:**
- `≥ 0.70` AUTO_MERGE — high confidence; include all (bioRxiv + published pairs)
- `0.50–0.70` LIKELY_DUP — candidates for human review
- `0.40–0.50` REVIEW — ambiguous
- `< 0.40` LOW — probably distinct

**Author name disambiguation:** Additional 5-signal classifier
- Name string similarity (token-level fuzzy match)
- First name/initial compatibility
- Co-author set Jaccard (do they have overlapping collaborators?)
- Citation neighborhood overlap
- Shared-paper negative signal (if they co-appear → likely different people)

**Output:** `duplicate_review.tsv` and `author_dedup_review.tsv` for human decision-making.

### Step 13 — Review-Cited Gap Analysis & Inclusion Decisions

**Scripts:** `13_review_citations.py`, `13_inclusion_decisions.py`

Analyzes 6 major review papers (Helmstaedter 2025, Bock 2025, Dorkenwald 2024, etc.)
to identify high-value papers cited by experts but missing from top-500.

**Inclusion criteria:**

| Category | Criteria | Action |
|----------|----------|--------|
| Promote | Expert-nominated + in_corpus + external_cites > 500 + em_connectomics | Lift to top-200 |
| Add (expert) | Expert-nominated + not_in_openAlex + indexed | Add DOI to EXTRA_SEED_DOIS |
| Add (reviews) | Cited by 2+ reviews + not_in_corpus + em_connectomics | Add DOI to EXTRA_SEED_DOIS |
| Flag | Cited by 1 review + score > 0.15 + infrastructure_paper | Manual review |

**Cache strategy:** Always checks `cache/review_citations_*.json` before API queries.
No cached data → returns partial results with warning.

### Step 14 — Corpus Update & Re-ranking Orchestration

**Script:** `14_update_corpus_and_rerank.py`

Orchestrates all QA/QC phases:
1. Apply duplicate merges
2. Apply author name merges
3. Run domain classification
4. Analyze review citations
5. Compile inclusion decisions
6. Generate metadata log

**Output metadata for each paper:**
```json
{
  "openalex_id": "...",
  "title": "...",
  "rank": 42,
  "composite_score": 0.456,
  "inclusion_source": {
    "corpus": "a",
    "promoted_from": 350,
    "added_via": "review_cited",
    "inclusion_criteria": "cited by 2+ reviews + external_cites > 2000",
    "decision_date": "2025-03-31"
  },
  "domain": "em_connectomics"
}
```

This ensures every paper in the final reading list has transparent, auditable provenance.

---

## Output Files

| File | Description |
|------|-------------|
| `output/paper_rankings.json` | Top 2,000 papers by composite score |
| `output/author_rankings.json` | Top 1,000 authors by composite score |
| `output/communities.json` | 30 Louvain communities with members, top authors, top concepts |
| `output/citation_baseline.json` | Top 200 by raw citation count |
| `output/corpus_stats.json` | Summary statistics |
| `output/validation_report.json` | Expert recall, corpus triangulation |
| `output/reading_list.json` | 500-paper reading list (topologically sorted) |
| `output/reading_list.md` | Human-readable reading list by phase |
| `output/reading_list_enriched.json` | reading_list + in_degree, out_degree, core_number |
| `output/ocar_entries.json` | 200 OCAR cards (JSON) |
| `output/ocar_entries.yaml` | 200 OCAR cards (YAML, journal_papers.yml schema) |
| `output/ocar_cache/` | Per-paper OCAR cache — 322 entries, fully resumable |
| `output/author_merge_map.json` | Canonical → aliases mapping |
| `output/author_merge_report.txt` | Human-readable merge log |
| `output/high_indegree_omissions.json` | 100 high-indegree papers outside top-500 |
| `output/expert_list_gaps.json` | 48 expert papers not in top-500 |
| `output/strategic_audit.json` | Full audit flags by lens |
| `output/strategic_audit.md` | Readable audit briefing |
| `output/field_map.html` | Interactive D3 citation graph (top 300 papers) |
| `output/evolution_graph.html` | D3 timeline of field evolution (2000–2025) |

Large files gitignored (regenerable): `corpus_merged.json`, `corpus_{a,b,c}.json`,
all four raw graphs, `cache/`.

---

## Configuration Reference

Key parameters in `config.py`:

| Parameter | Default | Effect |
|-----------|---------|--------|
| `REQUESTS_PER_SECOND` | 9 | Stay under OpenAlex polite-pool limit (10/s) |
| `EXPANSION_MAX_CITED_BY` | 200 | Max forward-citation neighbors per seed paper |
| `DATASET_MAX_CITERS` | 500 | Max citers fetched per Corpus C anchor |
| `MIN_SEED_CONNECTIONS` | 2 | Min seed citations to retain a discovered paper |
| `MAX_CORPUS_SIZE` | 5,000 | Safety cap on Corpus A size |
| `MARGINAL_GAIN_THRESHOLD` | 0.05 | Stop expansion when < 5% new papers per hop |
| `MIN_COCITATION_WEIGHT` | 2 | Min co-citations to add co-citation graph edge |
| `MIN_COUPLING_WEIGHT` | 2 | Min shared references for bibliographic coupling edge |
| `AUTO_SEED_QUERIES` | 19 queries | Modify to shift field scope |
| `EXTRA_SEED_DOIS` | `[]` | Force-include specific papers by DOI |

---

## Reproducibility Notes

1. **OpenAlex data drifts daily.** Preserve `cache/` to freeze a snapshot.
   Re-runs with an intact cache are fully deterministic. Steps 1–2 require API access;
   steps 3–14 can run offline with cached data.

2. **Cache strategy**: All OpenAlex queries are cached by ID.
   - `cache/work_{openalex_id}.json` — paper metadata
   - `cache/author_{author_id}.json` — author metadata
   - `cache/review_citations_{doi}.json` — review references
   - Before fetching: always check cache first

3. **Louvain is non-deterministic** beyond `seed=42`. Community assignments may
   shift if the graph structure changes between runs. Refer to communities by their
   top-concept labels, not by ID numbers.

4. **Betweenness approximation** (k=500) introduces ~5% error vs. exact computation.
   Exact betweenness on the 35,947-node co-authorship graph is computationally
   infeasible; k=500 is the right tradeoff.

5. **Abstract coverage**: ~72% of corpus papers have `abstract_inverted_index` in
   OpenAlex. The remaining 28% fall back to title + concepts for OCAR generation.

6. **Author identity**: OpenAlex disambiguation is imperfect. The 17 confirmed merge groups
   in `10_apply_merges.py` are manually verified. Additionally, `12_dedup_review.py`
   detects name variants using co-author network Jaccard and citation neighborhood overlap,
   outputting candidates for human review.

7. **Domain classification**: Uses journal name (97% coverage) as primary signal.
   OpenAlex concepts (30% coverage) and title keywords (100% fallback) resolve ambiguous
   papers. Achieves ~95% accuracy on manually-labeled samples.

---

## Dependencies

```
requests>=2.28       # OpenAlex API
networkx>=3.0        # Graph construction and analysis
numpy>=1.24          # Required by networkx PageRank backend
scipy>=1.10          # Required by networkx sparse solvers
anthropic>=0.40      # Step 8 only — OCAR generation via Claude API
```

Python 3.10+ required. Install: `pip install -r requirements.txt`
