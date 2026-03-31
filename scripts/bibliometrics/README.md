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
| D: k-core inversions (k≥30, rank 201–500) | 34 | Structurally central graph theory papers ranked lower than expected |

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
   Re-runs with an intact cache are fully deterministic.

2. **Louvain is non-deterministic** beyond `seed=42`. Community assignments may
   shift if the graph structure changes between runs. Refer to communities by their
   top-concept labels, not by ID numbers.

3. **Betweenness approximation** (k=500) introduces ~5% error vs. exact computation.
   Exact betweenness on the 35,947-node co-authorship graph is computationally
   infeasible; k=500 is the right tradeoff.

4. **Abstract coverage**: ~72% of corpus papers have `abstract_inverted_index` in
   OpenAlex. The remaining 28% fall back to title + concepts for OCAR generation.

5. **Author identity**: OpenAlex disambiguation is imperfect. The 17 merge groups in
   `10_apply_merges.py` are manually verified. Run `11_strategic_audit.py` and inspect
   `author_merge_suggestions.json` to find new candidates.

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
