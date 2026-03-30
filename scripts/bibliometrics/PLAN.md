# Connectomics Bibliometric Analysis Pipeline

## Context

We have 150 seed papers (with DOIs) from 55 experts in `_data/expert_seed_papers/`, plus 102 papers in `_data/journal_papers.yml`. The goal is to build a principled, bias-aware bibliometric pipeline that maps the connectomics field — identifying the most important papers and people via citation graph analysis.

The key methodological concern is **seed bias**: starting from hand-picked experts risks over-representing their citation neighborhoods. The solution is to go **fully data-driven first** — start from a minimal, inarguable seed set discovered automatically from OpenAlex, let the API discover the field organically, then use the existing 55-expert / 150-paper list as a **validation set** to measure coverage.

## Philosophy

1. **Discover first, validate second** — don't bake expert opinions into the input
2. **Auto-seed from OpenAlex** — the only human input is search terms ("connectomics", "connectome"), which are definitional
3. **Three independent entry points** — triangulate to avoid any single bias source
4. **Expert list as ground truth** — compare what the data finds vs. what experts curated
5. **Rank within paper roles** — methods, datasets, and biology papers serve different purposes

## File Structure

```
scripts/bibliometrics/
  PLAN.md                      # This file
  config.py                    # All settings, queries, thresholds (EDIT THIS to customize)
  openalex_client.py           # Rate-limited OpenAlex API wrapper with file-based caching
  01_harvest.py                # Three corpus paths + adaptive expansion
  02_build_graphs.py           # Citation, co-citation, bibliographic coupling, co-authorship
  03_compute_metrics.py        # PageRank, betweenness, communities, role classification
  04_validate.py               # Compare data-driven results vs expert-curated list
  05_html_report.py            # Standalone D3 interactive visualization
  cache/                       # API response cache (gitignored)
    works/                     # One JSON per paper, keyed by OpenAlex ID
    queries/                   # Cached search result pages
  output/                      # Results (committed)
    graphs/                    # D3-compatible JSON
```

## Pipeline Steps

### Step 1: Harvest (`01_harvest.py`)

Three independent corpus construction paths, all fully data-driven.

#### Corpus A — Auto-Seed + Citation Expansion

Build the seed from OpenAlex with zero human paper curation:
1. `concepts.id:C2776102887` (connectomics concept), sort by citations → top 20
2. Title search `"connectome"`, sort by citations → top 20
3. Title search `"serial block-face" OR "FIB-SEM" neuron` → top 10
4. Title search `"synapse detection" "electron microscopy"` → top 10
5. Title search `"nanoscale" "neural circuit"` → top 10
6. Merge + dedup → ~40-50 auto-seed papers

Then for each auto-seed paper:
- Fetch forward citations (papers citing it) via OpenAlex `cited_by_api_url`
- Fetch backward references from `referenced_works` field
- Keep papers connected to 2+ seeds (co-citation threshold)

**Adaptive depth**: After 1-hop, check dimension coverage. If any dimension has <20 papers, expand to 2-hop for underrepresented areas only.

Expected yield: ~800-2000 papers.

#### Corpus B — Keyword/Concept Search (independent)

Query OpenAlex with field-defining terms (see `config.py:KEYWORD_QUERIES`):
- `"connectome" OR "connectomics"`
- `"serial section electron microscopy" neuron`
- `"synapse detection" "electron microscopy"`
- `"flood filling network" OR "neuronal segmentation"`
- `"FlyWire" OR "hemibrain" OR "MICrONS" OR "H01"`
- `"volume electron microscopy" reconstruction`
- `"neural circuit" "dense reconstruction"`

Filter: `publication_year > 1985`, `cited_by_count > 5`, max 200 per query.

Expected yield: ~500-1500 papers.

#### Corpus C — Dataset-Anchored

Find OpenAlex work IDs for ~10 landmark dataset releases (DOIs in `config.py:DATASET_ANCHOR_DOIS`):
- FlyWire, hemibrain, MICrONS, H01, Kasthuri 2015, Bock 2011, Briggman retina, FAFB, Winding larva, Cook/WormAtlas

Fetch all papers citing these (capped at 500 per dataset).

Expected yield: ~500-1000 papers.

#### Merge

Union of A ∪ B ∪ C. Each paper tagged with provenance: `{corpus_a: true, corpus_b: false, corpus_c: true}`.

### Step 2: Build Graphs (`02_build_graphs.py`)

From the merged corpus, construct four graphs:

| Graph | Type | Nodes | Edges |
|-------|------|-------|-------|
| Citation | Directed | Papers | A→B if A cites B |
| Co-citation | Undirected, weighted | Papers | weight = papers citing both A and B |
| Bibliographic coupling | Undirected, weighted | Papers | weight = shared references |
| Co-authorship | Undirected, weighted | Authors | weight = co-authored papers |

Author disambiguation uses OpenAlex author IDs (not string names).

Serialized as networkx graphs → JSON (node-link format for D3).

### Step 3: Compute Metrics (`03_compute_metrics.py`)

#### Paper Role Classification

Auto-detected from OpenAlex metadata:
- **Methods** — high concept overlap with "algorithm", "segmentation", "software"
- **Dataset** — title matches dataset patterns, or has data_url
- **Biology** — concepts overlap with "neuron", "synapse", "circuit"
- **Review** — OpenAlex `type` = "review", or high HITS hub score

Rankings computed **both globally and within each role**.

#### Paper Metrics (Two Tiers)

**Tier 0 — Pure citation baseline** (standalone, no graph needed):

| Metric | Source | Meaning |
|--------|--------|---------|
| Total citations | OpenAlex `cited_by_count` | Raw impact |
| Citations/year | OpenAlex | Recency-normalized impact |

Output separately as `output/citation_baseline.json`.

**Tier 1 — Graph-derived**:

| Metric | Graph | Meaning |
|--------|-------|---------|
| PageRank | Citation | Structural importance |
| HITS authority | Citation | Landmark results |
| HITS hub | Citation | Good reviews/surveys |
| Betweenness | Citation | Bridge papers |
| Co-citation strength | Co-citation | Intellectual pairing |
| Recent PageRank | Citation (2020+ subgraph) | Emerging importance |

The HTML report shows both tiers side by side. Where they agree = high confidence. Where they diverge = interesting (e.g., low-citation + high betweenness = hidden bridge paper).

#### Author Metrics

| Metric | Graph | Meaning |
|--------|-------|---------|
| Weighted degree | Co-authorship | Collaboration volume |
| Betweenness centrality | Co-authorship | Bridge builders |
| Eigenvector centrality | Co-authorship | Well-connected |
| Paper count in corpus | — | Productivity in field |
| Sum of paper PageRanks | Citation | Cumulative influence |
| Recent paper count (2022+) | — | Currently active |

#### Community Detection — Data-Driven Taxonomy

- Louvain on co-authorship graph → research groups
- Louvain on co-citation graph → intellectual subcommunities
- **Do NOT force-map to 11 dimensions.** Instead:
  1. Let Louvain discover natural clusters
  2. Label each cluster by top OpenAlex concepts + top authors
  3. Compare discovered clusters to the 11-dimension hypothesis
  4. Report: which dimensions are validated, which split, which merge, which are missing

This lets the graph reveal the field's real structure.

### Step 4: Validate (`04_validate.py`)

Load the existing 150 papers + 102 journal papers as expert-curated ground truth.

**Triangulation**:
- Jaccard(A, B), Jaccard(A, C), Jaccard(B, C)
- Papers in A∩B∩C = high-confidence core

**Expert validation**:
- What % of expert-curated papers appear in data-driven corpus? (recall)
- What % of data-driven corpus was in expert list? (expert precision)
- Which expert papers are MISSING? → niche/specialized work
- Which data-driven papers are NOT in expert list? → expert blind spots
- Do all 55 experts appear as authors? Which don't?

**Taxonomy comparison**:
- Cross-tab Louvain clusters vs 11 dimensions
- Flag: dimensions with no cluster, clusters with no dimension

### Step 5: HTML Report (`05_html_report.py`)

Standalone HTML page (self-contained, inline CSS/JS):
- D3 force-directed graph (citation graph, toggle to co-authorship)
- Click node → paper/author details; hover → metadata
- Sidebar: ranked tables (top papers by citation + PageRank; top authors)
- Community coloring (Louvain clusters)
- Validation summary panel (Jaccard scores, dimension coverage heatmap)
- Output: `output/field_map.html`

## Caching & Incremental Re-runs

- All API responses cached to `cache/works/{openalex_id}.json`
- Search results cached to `cache/queries/{query_hash}.json`
- On re-run: skip cached works, only fetch new
- Change `config.py` seed queries or add manual DOIs → re-run picks up delta
- `cache/` is gitignored; `output/` is committed

## Rate Limiting

OpenAlex polite pool: 10 req/sec with `mailto` param. Pipeline targets 9/sec.
Exponential backoff on 429s (1s, 2s, 4s, max 3 retries).

## API Budget

- ~150 seed resolutions + ~150 cited_by fetches + ~500 hop-1 lookups + ~12 keyword pages + ~10 dataset citer pages
- Total: ~1500-2000 requests ≈ 3-4 minutes
- With cache, subsequent runs are instant

## Dependencies

- `requests` (installed)
- `networkx` (installed)
- Python 3.11 stdlib: `json`, `pathlib`, `time`, `hashlib`, `collections`, `re`
- No additional packages needed

## Verification Checklist

1. `01_harvest.py` → outputs `output/corpus_merged.json` with ~1000-3000 papers
2. Spot-check: Sporns 2005, Helmstaedter 2013, FlyWire 2024 should all be in corpus
3. `02_build_graphs.py` → outputs 4 graph JSON files with reasonable node/edge counts
4. `03_compute_metrics.py` → Sporns 2005 should have high PageRank; Seung should rank high in author metrics
5. `04_validate.py` → Jaccard(A,B) > 0.3 suggests convergence; all 55 experts should mostly appear
6. `05_html_report.py` → `output/field_map.html` opens in browser with working visualization

## Expected Outputs

```
output/
  corpus_merged.json              # Full merged corpus with provenance
  citation_baseline.json          # Pure citation-count ranking
  paper_rankings.json             # Top papers by composite score (global + per-role)
  author_rankings.json            # Top authors by composite score
  communities.json                # Detected subcommunities with labels
  validation_report.json          # Expert list comparison
  validation_report.md            # Human-readable version
  corpus_stats.json               # Paper counts, dimension coverage, year distribution
  field_map.html                  # Interactive D3 visualization
  graphs/
    citation_graph.json           # D3 node-link format
    cocitation_graph.json
    coupling_graph.json
    coauthorship_graph.json
```

## Key Design Decisions

1. **Auto-seed from OpenAlex** — no human paper curation in the input; search terms are the only human input
2. **Expert list as validation, not input** — the 150 papers + 55 experts are used to measure recall, not to bias discovery
3. **Adaptive depth** — 1-hop default; expand to 2-hop only where dimension coverage is thin
4. **Paper role classification** — methods, datasets, biology, reviews ranked separately so they don't drown each other
5. **Recency weighting** — citations/year and recent-only PageRank to surface emerging work
6. **Data-driven taxonomy** — let Louvain discover clusters, then compare to the 11-dimension hypothesis
7. **Three corpora** — triangulation is the core anti-bias mechanism
8. **OpenAlex over Semantic Scholar** — free, no API key, richer concepts, same citations
9. **File-based cache** — simple, inspectable, no database dependency
