# Connectomics Bibliometric Analysis Pipeline

## Context

We have 150 seed papers (with DOIs) from 55 experts in `_data/expert_seed_papers/`, plus 102 papers in `_data/journal_papers.yml`. The goal is to build a principled, bias-aware bibliometric pipeline that maps the **EM connectomics** field — identifying the most important papers and people via citation graph analysis.

The key methodological concern is **seed bias**: starting from hand-picked experts risks over-representing their citation neighborhoods. The solution is to go **fully data-driven first** — start from a minimal, inarguable seed set, let OpenAlex discover the field organically, then use the existing 55-expert / 150-paper list as a **validation set** to measure coverage.

**Scope**: Nanoscale / synaptic-resolution connectomics — any technique that resolves individual synapses or maps connectivity at cellular resolution. This includes:
- **Volume EM**: SEM, TEM, FIB-SEM, SBEM, multibeam SEM, ATUM/GridTape, serial section
- **Barcoding / molecular**: MAPseq, BARseq, BRICseq (connectivity mapping without imaging)
- **Expansion microscopy**: ExM for nanoscale optical connectomics
- **X-ray**: micro-CT, nano-CT, synchrotron nanotomography
- **Array tomography**: correlative light/EM
- **Graph theory / network analysis**: when applied to synaptic-resolution connectomes

**Excluded**: Macro-connectomics (dMRI tractography, fMRI functional connectivity, resting-state) UNLESS it bridges to nanoscale work (e.g., Sporns graph theory applied to both scales). This is deliberate — the MRI and nanoscale communities are largely separate citation networks.

## Methodological Grounding

This pipeline implements established bibliometric methods with citations:

| Method | Citation | What it justifies |
|--------|----------|-------------------|
| Citation chasing / snowball sampling | Greenhalgh & Peacock, BMJ 2005; Hinde & Spackman, PharmacoEconomics 2015 | Corpus expansion via forward/backward citations |
| Multi-graph bibliometric mapping | Van Eck & Waltman 2014 (VOSviewer); Boyack & Klavans, JASIST 2010 | Citation + co-citation + coupling graphs |
| PageRank for scientific impact | Chen et al., J. Informetrics 2007 | Graph-based paper importance |
| Data triangulation | Marzi et al., Int J Mgmt Reviews 2025; Denzin 1978 | Multiple independent corpora for convergence |
| OpenAlex as data source | Priem et al. 2022; validated in Scientometrics 2025 | Free, comprehensive bibliometric database |

**Prior work**: Two bibliometric analyses of connectomics exist (Frontiers Neurosci 2022, Neurosci Res 2022) but both focus on MRI/fMRI connectomics and use Web of Science. Neither covers EM connectomics specifically. Our pipeline fills this gap.

**Note on OpenAlex Concepts**: OpenAlex is deprecating Concepts in favor of Topics. The concept ID `C2776102887` should be verified at runtime. The pipeline should fall back to title/keyword search if concept queries fail.

## Approach: Data-Driven Discovery + Expert Validation

### Philosophy
1. **Discover first, validate second** — don't bake expert opinions into the input
2. **Auto-seed from OpenAlex** — only human input is search terms definitional to EM connectomics
3. **Three independent entry points** — data triangulation (Marzi et al. 2025) across citation, keyword, and dataset paths
4. **Expert list as ground truth** — compare what the data finds vs. what experts curated
5. **Nanoscale filtering** — exclude pure dMRI/fMRI macro-connectomics; include graph theory bridges and all synaptic-resolution techniques

### File Structure

```
scripts/
  bibliometrics/
    01_harvest.py              # All three corpus paths + adaptive expansion
    02_build_graphs.py         # Construct citation, co-citation, co-authorship graphs
    03_compute_metrics.py      # PageRank, betweenness, community detection
    04_validate.py             # Compare data-driven results vs expert-curated list
    05_html_report.py          # Standalone D3 interactive visualization
    cache/                     # API response cache (gitignored)
    output/                    # Results JSON + summary reports
    config.py                  # API settings, thresholds, keyword lists, minimal seeds
    openalex_client.py         # Rate-limited OpenAlex API wrapper with caching
```

### Step 1: Harvest (`01_harvest.py`)
Three parallel corpus construction paths, all fully data-driven.

#### Corpus A — Auto-Seed + Citation Expansion

Build the seed from OpenAlex (zero human paper curation):

**Core connectomics** (field-defining terms):
1. `concepts.id:C2776102887` (connectomics concept) → top 20
2. Title: `"connectome" AND ("synapse" OR "nanoscale" OR "reconstruction")` → top 20
3. Title: `"connectomics"` → top 20

**Volume EM** (the dominant technique family):
4. Title: `"serial block-face" OR "SBF-SEM" OR "SBEM"` → top 10
5. Title: `"FIB-SEM" OR "focused ion beam" brain` → top 10
6. Title: `"serial section" AND ("TEM" OR "electron microscopy") neuron` → top 10
7. Title: `"volume electron microscopy" reconstruction` → top 10
8. Title: `"multi-beam SEM" OR "multibeam" brain` → top 5
9. Title: `"ATUM" OR "GridTape" OR "automated tape-collecting"` → top 5

**Non-EM nanoscale techniques**:
10. Title: `"MAPseq" OR "BARseq" OR "barcoding" connectivity brain` → top 10
11. Title: `"expansion microscopy" synapse OR connectom` → top 5
12. Title: `"X-ray" AND ("nanotomography" OR "nano-CT" OR "micro-CT") neuron` → top 5
13. Title: `"array tomography" synapse OR neuron` → top 5

**Segmentation & reconstruction**:
14. Title: `"synapse detection" OR "neuron segmentation"` → top 10
15. Title: `"flood-filling network" OR "dense reconstruction" neural` → top 10

**Graph theory / network analysis** (bridges both scales):
16. Title: `"connectome" "graph theory" OR "network analysis"` → top 10

Merge + dedup → ~80-120 auto-seed papers.

**Macro-connectomics exclusion filter**: After merging, remove papers where title/abstract contains `"diffusion MRI" OR "dMRI" OR "fMRI" OR "resting state" OR "tractography" OR "BOLD" OR "functional connectivity"` UNLESS they also contain nanoscale indicators: `"electron microscopy" OR "synapse" OR "nanoscale" OR "connectome" AND "graph"`.

For each auto-seed paper: fetch forward citations + backward references. 1-hop expansion.
Keep papers connected to 2+ seeds (co-citation threshold).
**Adaptive**: after 1-hop, check technique coverage; expand to 2-hop only for underrepresented technique families.
Expected yield: ~800-2000 papers.

#### Corpus B — Keyword/Concept Search (independent of seeds)

Broader nanoscale connectomics vocabulary, organized by technique:

**Core field terms**:
- `"connectome" OR "connectomics"` (post-filter for nanoscale)
- `"neural circuit" "dense reconstruction"`
- `"connectome" "graph theory" OR "network analysis"`

**Volume EM**:
- `"serial section electron microscopy" neuron`
- `"volume electron microscopy" reconstruction`
- `"serial block-face SEM" OR "FIB-SEM" brain`
- `"multi-beam SEM" OR "multibeam SEM" neuron`
- `"ATUM" OR "GridTape" electron microscopy`

**Non-EM nanoscale**:
- `"MAPseq" OR "BARseq" connectivity`
- `"expansion microscopy" synapse`
- `"array tomography" synapse OR neuron`
- `"X-ray nanotomography" OR "nano-CT" neuron`

**Segmentation & tools**:
- `"synapse detection" "electron microscopy"`
- `"flood filling network" OR "neuronal segmentation"`

**Dataset names**:
- `"FlyWire" OR "hemibrain" OR "MICrONS" OR "H01"`

Filter: `publication_year > 1985`, `cited_by_count > 5`, max 200 per query.
Post-filter: same macro-connectomics exclusion as Corpus A.
Expected yield: ~500-1500 papers.

#### Corpus C — Dataset-Anchored (papers citing landmark EM datasets)

Verified DOIs for major EM connectome releases:

| Dataset | DOI | Modality |
|---------|-----|----------|
| FlyWire whole-brain | 10.1038/s41586-024-07558-y | FIB-SEM/ssTEM |
| Hemibrain v1.2 | 10.7554/eLife.57443 | FIB-SEM |
| FAFB (Zheng 2018) | 10.1016/j.cell.2018.06.019 | ssTEM (TEMCA2) |
| Larval Drosophila (Winding) | 10.1126/science.add9330 | ssTEM |
| MICrONS | 10.1101/2023.03.29.534851 | sSEM |
| H01 human cortex | 10.1126/science.adk4858 | multibeam SEM |
| Kasthuri 2015 | 10.1038/nature12346 | ATUM-SEM |
| Bock 2011 | 10.1038/nature10011 | ssTEM |
| Briggman retina | 10.1038/nn.2868 | SBEM |
| C. elegans developmental (Witvliet) | 10.1038/s41586-021-03778-8 | ssTEM |
| Cook C. elegans 2019 | 10.1016/j.cell.2019.05.026 | ssTEM |
| MANC (Takemura) | *verify DOI* | GridTape-TEM |
| FANC (Phelps) | *verify DOI* | GridTape-TEM |
| Optic lobe (Nern) | 10.1101/2024.04.16.589741 | FIB-SEM |

Also anchor on key **tool/infrastructure papers**:

| Tool | DOI | Role |
|------|-----|------|
| CATMAID | 10.1093/bioinformatics/btp266 | Annotation |
| webKnossos | 10.1038/nmeth.4331 | Annotation |
| CAVE | 10.1038/s41592-024-02426-z | Versioning |
| neuPrint | 10.1101/2020.01.16.909465 | Analysis DB |
| BossDB | 10.3389/fninf.2022.828787 | Storage |
| Flood-filling networks | 10.1038/s41592-018-0049-4 | Segmentation |

Fetch all papers citing these (capped at 500 per anchor).
Expected yield: ~500-1000 papers.

#### Merge

Union of A ∪ B ∪ C. Each paper tagged with provenance: `{corpus_a, corpus_b, corpus_c}`.

#### Caching & Incremental Re-runs
- All API responses cached to `cache/works/{openalex_id}.json` — one file per paper
- Search result pages cached to `cache/queries/{query_hash}.json`
- On re-run: skip already-cached works, only fetch new ones
- Changing `config.py` seed queries or adding manual DOIs → re-run picks up the delta
- Manual override: `config.py` has `EXTRA_SEED_DOIS` list for injecting specific papers
- `cache/` is gitignored; `output/` is committed

**Rate limiting**: 10 req/sec with `mailto` param for polite pool. Exponential backoff on 429s.

### Step 3: Build Graphs (`03_build_graphs.py`)
From the merged corpus (A ∪ B ∪ C), construct:

1. **Citation graph** (directed) — paper A → paper B if A cites B
2. **Co-citation graph** (undirected, weighted) — edge weight = number of corpus papers citing both A and B
3. **Bibliographic coupling graph** (undirected, weighted) — edge weight = number of shared references between A and B
4. **Co-authorship graph** (undirected, weighted) — author nodes, edge weight = number of co-authored papers

Store as networkx graphs, serialize to JSON (node-link format for D3 compatibility).

### Step 4: Compute Metrics (`04_compute_metrics.py`)

**Paper role classification** (auto-detected from OpenAlex metadata):
- **Methods** — introduces a technique/tool (high concept overlap with "algorithm", "segmentation", "software")
- **Dataset** — releases a connectome or dataset (has `data_url`, or title matches dataset patterns)
- **Biology** — reports a scientific finding (concepts overlap with "neuron", "synapse", "circuit")
- **Review** — survey/review paper (OpenAlex `type` = "review", or high HITS hub score)

Rankings are computed **both globally and within each role**, so a high-impact biology paper isn't drowned out by a heavily-cited methods paper.

**Paper metrics (two tiers):**

*Tier 0 — Pure citation baseline (no graph analysis needed):*
| Metric | Source | Meaning |
|--------|--------|---------|
| Total citations | OpenAlex `cited_by_count` | Raw impact |
| Citations/year | OpenAlex | Recency-normalized impact |

This produces a standalone "most cited connectomics papers" ranking — purely data-driven, reproducible by anyone. Output separately as `output/citation_baseline.json`.

*Tier 1 — Graph-derived metrics:*
| Metric | Graph | Meaning |
|--------|-------|---------|
| PageRank | Citation | Structural importance |
| HITS authority | Citation | Landmark results |
| HITS hub | Citation | Good reviews/surveys |
| Betweenness | Citation | Bridge papers |
| Co-citation strength | Co-citation | Intellectual pairing |
| Recent PageRank | Citation (2020+ subgraph) | Emerging importance |

The HTML report will show both side by side — where they agree is high confidence; where they diverge is interesting (e.g., a low-citation paper with high betweenness is a hidden bridge).

**Author metrics:**
| Metric | Graph | Meaning |
|--------|-------|---------|
| Weighted degree | Co-authorship | Collaboration volume |
| Betweenness centrality | Co-authorship | Bridge builders |
| Eigenvector centrality | Co-authorship | Well-connected |
| Paper count in corpus | — | Productivity in field |
| Sum of paper PageRanks | Citation | Cumulative influence |
| Recent paper count (2022+) | — | Currently active |

**Community detection — data-driven taxonomy:**
- Louvain on co-authorship graph → research groups
- Louvain on co-citation graph → intellectual subcommunities
- **Do NOT force-map to 11 dimensions**. Instead:
  1. Let Louvain discover natural clusters
  2. Label each cluster by top OpenAlex concepts + top authors
  3. Compare discovered clusters to the 11-dimension hypothesis
  4. Report: which dimensions are validated, which split, which merge, which are missing
- This lets the graph tell us the field's real structure rather than confirming our priors

**Output:** `output/paper_rankings.json`, `output/author_rankings.json`, `output/communities.json`

### Step 4: Validate Against Expert List (`04_validate.py`)
Load the existing 150 papers from `_data/expert_seed_papers/` and 102 from `_data/journal_papers.yml` as the **expert-curated ground truth**.

**Triangulation metrics:**
- Jaccard(A, B), Jaccard(A, C), Jaccard(B, C), Jaccard(A∩B, C)
- Papers in A∩B∩C = high-confidence core

**Expert validation:**
- What % of expert-curated papers appear in the data-driven corpus? (recall)
- What % of data-driven corpus was in the expert list? (precision of expert curation)
- Which expert-curated papers are MISSING from data-driven? → potential niche/specialized work
- Which data-driven papers are NOT in expert list? → potential blind spots in expert curation
- Do all 55 experts appear as authors in the discovered corpus? Which don't?

**Data-driven taxonomy vs 11 dimensions:**
- Report Louvain clusters with auto-generated labels
- Cross-tab: which clusters map to which of the 11 dimensions?
- Which dimensions have no matching cluster? Which clusters have no matching dimension?

**Output:** `output/validation_report.json` + `output/validation_report.md`

## Key Design Decisions

1. **Nanoscale scope** — covers all synaptic-resolution techniques (EM, barcoding, ExM, X-ray) but excludes macro-connectomics (dMRI/fMRI). Existing bibliometrics (Frontiers 2022, Neurosci Res 2022) covered MRI; we fill the nanoscale gap.
2. **Comprehensive technique coverage** — queries span volume EM (SEM, TEM, FIB-SEM, SBEM, multibeam, ATUM, GridTape), barcoding (MAPseq, BARseq), expansion microscopy, array tomography, and X-ray nanotomography. Missing any technique family would create blind spots.
3. **OpenAlex as primary source** — free, no API key, validated for bibliometrics (Scientometrics 2025). Note: OpenAlex Concepts are being deprecated → Topics. Pipeline should handle both.
4. **Adaptive depth** — 1-hop default; expand to 2-hop only where technique coverage is thin (target: every technique family represented with 5+ papers)
5. **Three corpora (data triangulation)** — core anti-bias mechanism per Marzi et al. 2025 and Denzin 1978
6. **Expert list as validation, not input** — stronger epistemically than baking expert opinion into seeds
7. **JSON cache** — resumable, inspectable, no database dependency
8. **networkx** — installed, sufficient for graphs up to ~5000 nodes

## Dependencies
- `requests` (installed)
- `networkx` (installed)
- Python 3.11 (available)
- No additional packages needed (stdlib json, collections, pathlib, time)

## Changes Needed in Code (from expert review)

### `config.py` updates:
- Replace `AUTO_SEED_QUERIES` with expanded 16-query set (volume EM + barcoding + ExM + X-ray + segmentation + graph theory)
- Add `MACRO_EXCLUSION_TERMS = ["diffusion MRI", "dMRI", "fMRI", "resting state", "tractography", "BOLD", "functional connectivity"]`
- Add `NANOSCALE_KEEP_TERMS = ["electron microscopy", "synapse", "nanoscale", "connectome"]` (override exclusion if present)
- Replace `KEYWORD_QUERIES` with expanded 16-query set organized by technique family
- Add tool/infrastructure DOIs to `DATASET_ANCHOR_DOIS` (CATMAID, webKnossos, CAVE, neuPrint, BossDB, FFN)
- Add `TECHNIQUE_FAMILIES` dict for coverage checking: `{"volume_em": [...], "barcoding": [...], "exm": [...], "xray": [...], "array_tomography": [...]}`
- Add concept ID fallback (OpenAlex deprecating Concepts → Topics)

### `01_harvest.py` updates:
- Add `filter_macro_connectomics(papers)` function: removes papers matching `MACRO_EXCLUSION_TERMS` unless they also match `NANOSCALE_KEEP_TERMS`
- Apply filter after each corpus build and after final merge
- Log: "Filtered N macro-connectomics papers (dMRI/fMRI)"

### `04_validate.py` updates:
- Add technique family coverage check using `TECHNIQUE_FAMILIES` from config
- Report: papers per technique family (volume EM, barcoding, ExM, X-ray, AT)
- Flag if any technique family has <5 papers

## Verification
1. Run `01_harvest.py` → outputs `output/corpus_merged.json` with ~1000-3000 papers
2. Spot-check: Sporns 2005, Helmstaedter 2013, FlyWire 2024, FFN 2018, CAVE 2024 should all appear
3. **Macro filter check**: search corpus for "fMRI" / "diffusion MRI" — should be <5% of total
4. **Technique coverage check**: grep titles for SEM, TEM, FIB-SEM, SBEM, multibeam, ATUM, MAPseq/BARseq, expansion microscopy — all should have hits
5. `02_build_graphs.py` → 4 graph JSON files with reasonable node/edge counts
6. `03_compute_metrics.py` → Sporns has high PageRank; Seung, Lichtman, Helmstaedter rank high in author metrics
7. `04_validate.py` → Jaccard(A,B) > 0.3; all 55 experts mostly appear; validation_report.md is readable
8. `05_html_report.py` → `output/field_map.html` opens in browser with working visualization

## Expected Outputs
- `output/corpus_merged.json` — full merged corpus with provenance tags
- `output/citation_baseline.json` — pure citation-count ranking (no graph analysis)
- `output/paper_rankings.json` — top papers by composite score (global + per-role)
- `output/author_rankings.json` — top authors by composite score
- `output/communities.json` — detected subcommunities with auto-generated labels
- `output/graphs/citation_graph.json` — D3-compatible node-link JSON
- `output/graphs/coauthorship_graph.json` — D3-compatible
- `output/validation_report.json` — triangulation + expert comparison
- `output/validation_report.md` — human-readable version
- `output/corpus_stats.json` — paper counts, modality coverage, year distribution
- `output/field_map.html` — standalone interactive visualization

## Methodological References

Full citations for methods section:

1. Greenhalgh T, Peacock R. Effectiveness and efficiency of search methods in systematic reviews of complex evidence. *BMJ* 331:1064-1065, 2005. PMID:16230312
2. Hinde S, Spackman E. Bidirectional citation searching to completion. *PharmacoEconomics* 33(1):5-11, 2015. DOI:10.1007/s40273-014-0205-3
3. Van Eck NJ, Waltman L. Visualizing bibliometric networks. In *Measuring Scholarly Impact*, Springer, pp 285-320, 2014.
4. Boyack KW, Klavans R. Co-citation analysis, bibliographic coupling, and direct citation. *JASIST* 61(12):2389-2404, 2010.
5. Chen P, Xie H, Maslov S, Redner S. Finding scientific gems with Google's PageRank algorithm. *J Informetrics* 1(1):8-15, 2007. DOI:10.1016/j.joi.2006.06.001
6. Marzi G et al. Guidelines for bibliometric-systematic literature reviews. *Int J Mgmt Reviews* 27(1), 2025.
7. Priem J, Piwowar H, Orr R. OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts. arXiv:2205.01833, 2022.
8. [OpenAlex validation] Reference coverage analysis vs Web of Science and Scopus. *Scientometrics*, 2025. DOI:10.1007/s11192-025-05293-3
