# Bibliometric Connectomics Pipeline

> Legacy bibliography pipeline execution has moved to `connectome-kb`; this repo now consumes synced visualization assets.


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

```bash
cd ../connectome-kb

# Install dependencies
pip install -r requirements.txt

# Run the full pipeline (steps 1–7)
bash run_pipeline.sh

# Resume from a specific step
bash run_pipeline.sh --from 3

# Generate OCAR cards for top 200 (requires ANTHROPIC_API_KEY or run via agents)
export ANTHROPIC_API_KEY=sk-ant-...
python 08_generate_ocar.py

# Extended analysis: k-cores, degree distributions, expert gaps
python 09_graph_analysis.py

# Apply author name merges
python 10_apply_merges.py

# Strategic audit report
python 11_strategic_audit.py
```

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

---

## Step 1 — Data Collection

### Three Independent Corpora

The pipeline uses **data triangulation** across three independent collection strategies,
following the methodology of Marzi et al. (2025). Agreement across corpora signals
robust, field-central papers; corpus-unique papers may be emerging or niche.

#### Corpus A: Auto-Seed + Citation Expansion

1. **Seed phase**: 19 OpenAlex queries (see `config.AUTO_SEED_QUERIES`):
   - 1 concept-filter query (OpenAlex concept ID for "connectomics")
   - 18 title-keyword queries covering: connectomics, FIB-SEM, SBEM, serial-section TEM,
     expansion microscopy, MAPseq/BARseq, array tomography, flood-filling networks,
     synapse detection, graph theory

2. **Citation expansion**: Up to 2 hops from seeds.
   - A discovered paper is retained if cited/referenced by **≥ 2 seed papers** (seed_connections threshold)
   - Each paper can yield at most 200 forward-citation neighbors (`EXPANSION_MAX_CITED_BY = 200`)
   - Expansion stops when marginal gain < 5% new papers per hop, or corpus reaches 5,000 papers

3. **Macro-connectomics filter**: Papers matching dMRI/fMRI terms
   (`diffusion mri`, `fmri`, `resting state`, `tractography`, `bold`, etc.) are removed
   *unless* they also contain a nanoscale indicator (`electron microscopy`, `synapse`,
   `connectome`, `barcod`, etc.).

#### Corpus B: Keyword Search

14 full-text keyword queries against OpenAlex with filters:
- `publication_year > 1985`
- `cited_by_count > 5`
- Max 200 results per query

Queries cover: `"connectome" OR "connectomics"`, `"serial section electron microscopy" neuron`,
`"FlyWire" OR "hemibrain" OR "MICrONS" OR "H01"`, `"MAPseq OR BARseq connectivity"`, etc.

#### Corpus C: Dataset-Anchored

16 landmark dataset/tool papers are hardcoded as anchors (DOIs in `config.py`):

| Anchor | Paper |
|--------|-------|
| FlyWire | Dorkenwald et al. 2024 |
| Hemibrain v1.2 | Scheffer et al. 2020 |
| FAFB | Zheng et al. 2018 |
| H01 human cortex | Shapson-Coe et al. 2024 |
| MICrONS mm³ | MICrONS Consortium 2021 |
| Larval Drosophila | Winding et al. 2023 |
| C. elegans connectome | Witvliet et al. 2021 |
| Flood-filling nets | Januszewski et al. 2018 |
| CATMAID | Saalfeld et al. 2009 |
| webKnossos | Boergens et al. 2017 |
| CAVE | Dorkenwald et al. 2023 |
| neuPrint | Clements et al. 2020 |
| BossDB | Hider et al. 2022 |
| Kasthuri cortex | Kasthuri et al. 2015 |
| White C. elegans | White et al. 1986 |
| SBEM | Denk & Horstmann 2004 |

For each anchor: fetch the paper itself + up to 500 papers that cite it
(`DATASET_MAX_CITERS = 500`).

#### Merge

All three corpora are deduplicated by `openalex_id`. Each paper carries a
provenance tag `{"a": bool, "b": bool, "c": bool}`. Papers in all three
corpora are considered field-central.

---

## Step 2 — Graph Construction

Four graphs are built from `corpus_merged.json`:

### Citation Graph (Directed)
- **Nodes**: one per paper
- **Edges**: A → B if paper A lists B in its `referenced_works` AND both A and B are in the corpus
- **7,925 nodes, 94,223 edges**
- Used for PageRank, HITS, betweenness, k-core

### Co-Citation Graph (Undirected, Weighted)
- Edge (A, B) exists if ≥ 2 corpus papers cite both A and B simultaneously
- Edge weight = number of corpus papers co-citing the pair
- Minimum weight threshold: 2

### Bibliographic Coupling Graph (Undirected, Weighted)
- Edge (A, B) exists if A and B share ≥ 2 references
- Edge weight = number of shared references
- **Warning**: O(n²) construction; the output file (~194 MB) is gitignored

### Co-Authorship Graph (Undirected, Weighted)
- **Nodes**: authors (by OpenAlex author ID)
- **Edges**: all pairs of authors who co-authored ≥ 1 paper in corpus
- Edge weight = number of jointly authored papers
- **35,947 nodes, 514,301 edges** (~72 MB; gitignored)

All graphs saved as D3 node-link JSON (`networkx.readwrite.json_graph.node_link_data`).

---

## Step 3 — Metrics & Rankings

### Paper Role Classification

Each paper is classified as `review | dataset | methods | biology` using keyword scoring:

```
if "review" or "survey" in title → review
elif dataset keyword count ≥ 2   → dataset
elif biology_score > methods_score → biology
else                               → methods
```

### Graph Centrality (Citation Graph)

| Metric | Function | Parameters | Interpretation |
|--------|----------|------------|----------------|
| PageRank | `nx.pagerank()` | α = 0.85 | Global structural importance |
| HITS hubs | `nx.hits()` | max_iter=200 | Papers citing many important works (reviews/surveys) |
| HITS authorities | `nx.hits()` | max_iter=200 | Papers cited by important works (landmark results) |
| Betweenness | `nx.betweenness_centrality()` | k=500 for n>2000 | Bridge papers between clusters |
| In-degree | `citation_graph.in_degree()` | — | Within-corpus citation count |
| Recent PageRank | `nx.pagerank()` on 2020+ subgraph | α=0.85 | Current relevance |

The k=500 approximation for betweenness (used when graph has >2,000 nodes) samples
500 random source nodes for shortest-path computation, introducing ~5% error vs exact
but reducing runtime from hours to seconds.

### Author Centrality (Co-Authorship Graph)

| Metric | Notes |
|--------|-------|
| Weighted degree | Sum of co-authorship edge weights |
| Betweenness | k=500 approximation (graph has 35,947 nodes) |
| Eigenvector centrality | max_iter=500; set to 0 on convergence failure |

### Community Detection

**Algorithm**: Louvain modularity optimization (`nx.community.louvain_communities`)
- Random seed: **42** (reproducibility)
- Applied to undirected citation graph
- Minimum community size: 3 members
- **30 communities** found in current run
- 3 communities are pure noise (geology, mass spectrometry, autophagy) — filtered in reading list

### Composite Scores

**Paper composite score:**
```
score = 0.35 × (pagerank / max_pr)
      + 0.25 × (total_citations / max_cites)
      + 0.20 × (betweenness / max_betw)
      + 0.20 × (recent_pagerank / max_recent_pr)
```

**Author composite score:**
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
autophagy, chromatography) are removed. Methods papers, MRI/fMRI papers, general
computer vision papers, and graph theory papers are retained — they are legitimate
signal in a connectomics education context.

Of 2,000 ranked papers: **33 removed** (noise communities), **1,967 pass**.

### Selection

Top **500 by composite score** from the survivors.

### Topological Sort

Papers are reordered using **Kahn's BFS algorithm** so that within the reading list,
every paper appears after the papers it cites (prerequisites first).

```
1. Build citation subgraph restricted to the 500 selected papers
2. Compute in-degree for each paper within this subgraph
3. Initialize queue: papers with in-degree 0, sorted by (year, role_priority)
   where role_priority = {review:0, methods:1, dataset:2, biology:3}
4. Pop lowest-priority paper, emit it, decrement successors' in-degrees
5. Papers entering in-degree 0 are added to queue
6. Cycle-breaking: remaining papers appended sorted by year
```

### Reading Phases

| Phase | Label | Criteria |
|-------|-------|----------|
| 0 | Orientation | role = review |
| 1 | Foundations | year < 2010 |
| 2 | Core Methods | methods/biology, 2010–2020 |
| 3 | Landmark Datasets | role = dataset, any year |
| 4 | Frontiers | year ≥ 2021 |

Current distribution: 88 orientation, 173 foundations, 176 core methods,
4 landmark datasets, 59 frontiers.

---

## Step 8 — OCAR Study Cards

**OCAR** = Opportunity / Challenge / Action / Resolution (+ future_work)

Each card also includes:
- `plain_language_summary` — 2–3 sentences for a general audience, with analogy
- `summaries.beginner` — undergrad with intro biology
- `summaries.intermediate` — grad student with neuroscience background
- `summaries.advanced` — researcher, with methodological caveats
- `discussion_prompts` — 3 journal-club questions specific to the paper
- `dimension` — one of: `connectomics | image-acquisition | segmentation | proofreading | graph-analysis | neuroanatomy | cell-types | infrastructure | neuroai | methods-general | review`
- `tags` — up to 6, format `category:term` (e.g. `imaging:fib-sem`, `species:drosophila`)

Generated for the **top 200 papers by composite score**. Individual paper results
cached to `output/ocar_cache/{openalex_id}.json` — the generation is fully resumable.

Output `ocar_entries.yaml` matches the schema of `_data/journal_papers.yml` and can
be appended directly.

**Note**: The script (`08_generate_ocar.py`) calls the Anthropic API directly and
requires `ANTHROPIC_API_KEY`. Alternatively, run via Claude Code agents (no API key
needed — used in the original pipeline run).

---

## Step 9 — Extended Graph Analysis

### K-Core Decomposition

Applied to the **undirected** citation graph (self-loops removed first).

The **k-core** of a graph is the maximal subgraph where every node has degree ≥ k.
A node's **core number** is the highest k-core it belongs to — a proxy for how
deeply embedded it is in the network's dense nucleus.

**Current results**:
- Maximum k: **32**
- Inner core (k ≥ 28): **402 papers**
- The k=32 shell is dominated by the fMRI/MRI connectomics community (tight cross-citation cluster)
- EM connectomics papers occupy k=28–31

### Degree Distribution

In-degree (citations within corpus) and out-degree (references within corpus) computed
for all reading-list papers. High-in-degree papers *outside* the top 500 flagged as
potential omissions (threshold: in-degree ≥ 30).

---

## Step 10 — Author Name Merges

OpenAlex assigns separate author IDs to the same person when their name appears
differently across papers (hyphenation, initials, unicode variants). This inflates
author counts and suppresses composite scores.

### Merge Strategy

Merges are accepted when at least one of the following holds:
1. **User-confirmed** (e.g. Gray Roncal)
2. **Multiple shared papers** as co-authors (same last + first initial + ≥2 shared)
3. **Unicode normalization**: en-dash (–) ↔ ASCII hyphen (-), trailing periods, etc.
4. **Abbreviation match**: "G Jefferis" clearly = "Gregory S.X.E. Jefferis" given shared papers

### Confirmed Merges (17 groups)

| Canonical Name | Aliases | Evidence |
|----------------|---------|----------|
| William Gray-Roncal | William Gray Roncal, William R. Gray Roncal, William R. Gray-Roncal, Will Gray-Roncal | User-confirmed; 5 OpenAlex IDs, 34 combined papers |
| Shin-ya Takemura | Satoko Takemura | 13 shared consortium papers |
| Alexander Shakeel Bates | Alexander S. Bates | 1 shared paper + full name present |
| Gregory S.X.E. Jefferis | G Jefferis, Gregory S. X. E. Jefferis, Gregory SXE Jefferis | Abbreviation + shared papers |
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

**Impact of Gray Roncal merge**: Unified from outside top-1,000 to **#47 by paper count**
(34 papers), **#205 by total citation sum** (1,886). His lower citation rank relative
to paper count reflects an infrastructure-heavy portfolio (BossDB, Open Connectome,
NeuVue, DotMotif) vs. the biology flagship papers that dominate the top-50 by citations.

---

## Step 11 — Strategic Audit

`11_strategic_audit.py` flags papers needing human review across five lenses:

| Lens | Count | Description |
|------|-------|-------------|
| A1: Expert in-corpus, not in top-500 | 20 | Expert-curated papers ranked below 500; top candidates: connectome fingerprinting (2,967 cites), NBS (2,779), connectome disorders (1,757) |
| A2: Expert not in corpus | 28 | Papers not fetched by pipeline; require manual DOI seeding |
| B: High in-degree omissions | 50 | Cited ≥30 times within corpus but outside top-500; top neuro: en-bloc staining (indeg=171), zebrafish whole-brain EM (154), iterative ExM (137) |
| C1: High ext-cites / low composite | 197 | Large external citation count but weak corpus signal; many are off-topic (SARS-CoV-2 cryo-EM, FieldTrip, WHO classification) |
| D: k-core inversions | 34 | Papers in k≥30 inner core but ranked 201–500; graph theory foundations (Girvan-Newman, betweenness centrality, community detection) |

---

## Output Files

| File | Description | Size |
|------|-------------|------|
| `output/corpus_merged.json` | All papers with provenance tags | ~56 MB (gitignored) |
| `output/paper_rankings.json` | Top 2,000 papers by composite score | ~4 MB |
| `output/author_rankings.json` | Top 1,000 authors by composite score | ~500 KB |
| `output/communities.json` | 30 Louvain communities with members, top authors, top concepts | ~2 MB |
| `output/citation_baseline.json` | Top 200 by raw citation count | ~100 KB |
| `output/corpus_stats.json` | Summary statistics | ~10 KB |
| `output/validation_report.json` | Expert recall, corpus triangulation | ~50 KB |
| `output/reading_list.json` | 500-paper reading list (topologically sorted) | ~1.5 MB |
| `output/reading_list.md` | Human-readable reading list by phase | ~200 KB |
| `output/reading_list_enriched.json` | reading_list + in_degree, out_degree, core_number | ~1.6 MB |
| `output/ocar_entries.json` | 200 OCAR cards (JSON) | ~800 KB |
| `output/ocar_entries.yaml` | 200 OCAR cards (YAML, journal_papers.yml schema) | ~700 KB |
| `output/ocar_cache/` | Per-paper OCAR cache (322 entries) | ~1.2 MB |
| `output/author_merge_map.json` | Canonical → aliases mapping | ~5 KB |
| `output/author_merge_report.txt` | Human-readable merge log | ~5 KB |
| `output/high_indegree_omissions.json` | 100 high-indegree papers outside top-500 | ~50 KB |
| `output/expert_list_gaps.json` | 48 expert papers not in top-500 | ~20 KB |
| `output/strategic_audit.json` | Full audit flags by lens | ~200 KB |
| `output/strategic_audit.md` | Readable audit briefing | ~50 KB |
| `output/field_map.html` | Interactive D3 citation graph (top 300 papers) | ~500 KB |
| `output/evolution_graph.html` | D3 timeline of field evolution (2000–2025) | ~400 KB |

Large files gitignored: `corpus_merged.json`, `corpus_{a,b,c}.json`, all four raw graphs,
`cache/`. These are fully regenerable from `run_pipeline.sh`.

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
| `EXTRA_SEED_DOIS` | `[]` | Force-include specific papers |

---

## Reproducibility Notes

1. **OpenAlex data drifts**: Citation counts update daily. To freeze a snapshot, preserve
   the `cache/` directory. Re-runs with an intact cache are fully deterministic.

2. **Louvain non-determinism**: Community assignments can shift across runs even with
   `seed=42` if the graph structure changes. Community *labels* (derived from top concepts)
   are stable but community *IDs* may reassign. Always refer to communities by their
   top-concept labels, not IDs.

3. **Betweenness approximation**: The k=500 sample introduces ~5% error relative to exact
   betweenness. For a 7,925-node graph this is the right tradeoff — exact computation
   would take hours. Results are stable across re-runs given the fixed seed.

4. **Abstract coverage**: ~72% of corpus papers have an `abstract_inverted_index` in
   OpenAlex. The remaining 28% use title + concepts for OCAR generation.

5. **Author identity**: OpenAlex author disambiguation is imperfect. The 17 merge groups
   in `10_apply_merges.py` are manually verified. Run `11_strategic_audit.py` to find
   new candidates using Jaccard paper-overlap + co-author similarity.

---

## Dependencies

```
requests>=2.28       # OpenAlex API
networkx>=3.0        # Graph construction and analysis
numpy>=1.24          # Required by networkx PageRank backend
scipy>=1.10          # Required by networkx sparse solvers
anthropic>=0.40      # Step 8 only — OCAR generation via Claude API
```

Install: `pip install -r requirements.txt`

Python 3.10+ required.
