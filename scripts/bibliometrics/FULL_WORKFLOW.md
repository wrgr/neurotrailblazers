# Full End-to-End Connectomics Bibliography Workflow

## Overview

This document describes the **complete workflow** from raw OpenAlex data to final reading list, visualizations, and OCAR study cards.

**Total time:** ~2–4 hours (steps 1–11) + 2–4 hours (QA/QC phases 12–14)

---

## Part A: Automated Corpus Collection & Ranking (2–4 hours, requires OpenAlex)

### Steps 1–11: Core Pipeline

| Step | Script | Time | Input | Output | Purpose |
|------|--------|------|-------|--------|---------|
| 1 | `01_harvest.py` | 45 min | OpenAlex API | `corpus_a/b/c.json`, `corpus_merged.json` | Collect papers via 3 independent strategies + merge |
| 2 | `02_build_graphs.py` | 30 min | `corpus_merged.json` | `graphs/citation_graph.json` + 3 others | Build directed citation graph + co-citation, coupling, co-authorship |
| 3 | `03_compute_metrics.py` | 20 min | graphs, corpus | `paper_rankings.json`, `author_rankings.json`, `communities.json` | PageRank, betweenness, community detection, composite scores |
| 4 | `04_validate.py` | 5 min | rankings, expert data | `validation_report.json` | Cross-check against expert seed papers (66 researchers) |
| 5 | `05_html_report.py` | 10 min | rankings, communities | `field_map.html` | Interactive D3 citation network visualization (top 500 papers) |
| 5b | `06b_kcore_visualization.py` | 5 min | graphs, enriched list | `kcore_map.html` | K-core shells visualization (network position, 6 colored shells) |
| 6 | `06_reading_list.py` | 5 min | rankings, communities | `reading_list.json`, `.md` | Top-500 papers, topologically sorted |
| 7 | `07_evolution_graph.py` | 10 min | corpus, communities | `evolution_graph.html` | Timeline of field evolution 2000–2025 |
| 8 | `08_generate_ocar.py` | 90 min | `reading_list.json` | `ocar_entries.json/.yaml` | OCAR study cards (via Claude API) for top 200 |
| 9 | `09_graph_analysis.py` | 15 min | graphs, rankings | `reading_list_enriched.json`, `*_gaps.json` | K-core analysis, expert gaps, high in-degree omissions |
| 10 | `10_apply_merges.py` | 5 min | corpus, merges | Updated rankings, author changes | Apply known author name merges (17 groups) |
| 11 | `11_strategic_audit.py` | 5 min | all outputs | `strategic_audit.json`, `.md` | Flag papers needing human review (5 lenses) |

### Run Automated Pipeline

```bash
cd scripts/bibliometrics

# Full pipeline (steps 1–11)
bash run_pipeline.sh

# Or resume from specific step
bash run_pipeline.sh --from 3  # Skip corpus collection, start at graphs

# Generate k-core visualization (run after step 9)
python 06b_kcore_visualization.py

# Generate OCAR cards (requires API key, run after step 6)
export ANTHROPIC_API_KEY=sk-ant-...
python 08_generate_ocar.py
```

### Outputs After Step 11

**Ranked Papers & Rankings:**
- `reading_list.json` (500 papers) — top-ranked, topologically sorted
- `paper_rankings.json` (2,000 papers) — full ranking with metrics
- `author_rankings.json` (1,000 authors) — ranked by composite score

**Visualizations (top 500 papers only):**
- `field_map.html` — D3 force-directed citation network, colored by community (5 MB)
- `kcore_map.html` — K-core shells, colored by network position (3 MB)
- `evolution_graph.html` — Timeline of field evolution 2000–2025 (2 MB)

**Study Materials:**
- `ocar_entries.json` / `.yaml` — 200 OCAR cards (Opportunity/Challenge/Action/Resolution)

**Analysis & Audit:**
- `reading_list_enriched.json` — top-500 with in/out degrees, k-core
- `strategic_audit.json`, `.md` — papers flagged for human review (5 categories)
- `expert_list_gaps.json` — expert-nominated papers not recovered
- `high_indegree_omissions.json` — highly-cited papers ranked below 500
- `communities.json` — 30 Louvain communities with members, top authors

---

## Part B: Quality Assurance & Corpus Enhancement (2–4 hours, no OpenAlex needed)

### Steps 12–14: QA/QC Workflow

Applies transparent decision criteria to accept/reject duplicates, author merges, and inclusion candidates.

#### Step 12: Detect Duplicates & Author Variants

```bash
# Generate TSV files for human review
python 12_dedup_review.py
# → Output: duplicate_review.tsv (1,425 pairs), author_dedup_review.tsv (980 pairs)
```

**Time:** 5 min (no network calls, uses cached data)

**What it does:**
- 5-signal duplicate detection (title, DOI, citations, authors, mutual non-citation)
- 5-signal author name dedup (name similarity, co-authors, citation neighborhoods)
- Scores ranked by confidence

**User action needed:** Fill in `decision` column of TSV (ACCEPT/REJECT/NULL)

#### Step 12b: Auto-Review High-Confidence Decisions

```bash
# Automatically accept high-confidence decisions (>= 0.80)
# Only flag ambiguous cases (0.50–0.79) for human review
python 12_auto_review.py --confidence-level high

# Or specify custom threshold
python 12_auto_review.py --auto-threshold 0.80
```

**Time:** 1 min

**What it does:**
- Reads TSV outputs from step 12
- Automatically ACCEPT decisions >= threshold (0.70–0.85)
- REJECT decisions < 0.40
- FLAG ambiguous decisions (0.40–threshold) for manual TSV review
- Logs all decisions with confidence scores

**Output:**
- `duplicate_auto_decisions.json` — papers to merge
- `author_auto_decisions.json` — author pairs to consolidate
- `duplicate_review_flagged.tsv` — only ambiguous cases (human review)
- `author_review_flagged.tsv` — only ambiguous cases (human review)

#### Step 12c: Apply Accepted Merges

```bash
# Apply all AUTO_ACCEPT decisions + any user-marked ACCEPT in TSV
python 12_apply_duplicate_merges.py
# → Output: corpus_deduplicated.json, updated graphs
```

**Time:** 2 min

**What it does:**
- Consolidates duplicate papers to canonical version (published > preprint)
- Merges author name variants
- Transfers citation edges
- Updates corpus and graph

#### Step 13: Analyze Review Citations

```bash
# Fetch citations from 6 major reviews (cache-first)
python 13_review_citations.py
# → Output: review_citations.json, review_cited_candidates.json
```

**Time:** 1 min (if cached) or 10 min (if fetching from OpenAlex)

**What it does:**
- Analyzes citations in landmark review papers
- Identifies papers cited by reviews but outside top-500
- Categorizes as: promote, add, or flag

**Cache strategy:** Checks `cache/review_citations_*.json` before API calls

#### Step 14: Compile Inclusion Decisions

```bash
# Synthesize all inclusion candidates with criteria
python 13_inclusion_decisions.py
# → Output: inclusion_decisions.json
```

**Time:** 1 min

**What it does:**
- Compiles: papers to promote from tail, missing expert papers, review-cited candidates
- Documents inclusion criteria for each
- Recommends which to add to corpus

#### Step 14b: Orchestrate Final Update & Rerank

```bash
# Apply all decisions and generate metadata
python 14_update_corpus_and_rerank.py

# For full metric recomputation (if changes made):
python 14_update_corpus_and_rerank.py --full-rebuild
```

**Time:** 
- Without rebuild: 2 min
- With rebuild: 30 min (re-runs metrics computation)

**What it does:**
- Applies all duplicate merges
- Applies all author merges
- Classifies domains (journal + concepts + keywords)
- Analyzes review citations
- Generates `inclusion_metadata.json` (provenance for each paper)

**Output:**
- `inclusion_metadata.json` — each paper tagged with source + inclusion criteria
- `domain_labels.json` — domain classification (em_connectomics, mri, network_science, etc.)
- `auto_review_log.json` — decision log with confidence scores

---

## Part C: Final Outputs & Artifacts

### Graph Strategy

**Primary graph:** ~500 papers (top-ranked from reading list)
- This is the **main visualization** and **basis for statistics**
- Bounded size makes it useful for interpretation and teaching
- Can expand to ~550 if manual review adds important papers

**Secondary (analysis) graph:** 7,925 papers
- Used for computing PageRank, k-cores, metrics
- Used to identify gaps and anomalies
- Not visualized (too large); reduced to 500 for viz

**Journal club subset:** Top 200 papers
- Receive detailed OCAR cards (Opportunity/Challenge/Action/Resolution)
- Get full expert review and discussion prompts
- Used for structured learning in journal club

**Visualization outputs:**
1. `field_map.html` — Force-directed citation graph (top 500 papers)
2. `kcore_map.html` — K-core shells (color-coded by network position)
3. `evolution_graph.html` — Temporal evolution (2000–2025)

### After All Steps: Reading List with Full Provenance

**Core Artifacts:**

1. **`reading_list_final.json`** — 500-paper list (±50 for manual additions) with:
   - Title, authors, year, journal
   - Composite score (PageRank + citations + betweenness + recent)
   - Rank (1–500)
   - Inclusion source: "corpus_a", "promoted_from_tail", "review_cited", "expert_gap", "dedup_merge"
   - Inclusion criteria: why this paper is in the list
   - Domain: em_connectomics, mri_connectomics, neuroscience, etc.
   - Phase: 0 (orientation) through 4 (frontiers)

2. **Interactive Visualizations:**
   - `field_map.html` — Force-directed citation network of top 500 papers, color by community (5 MB)
   - `kcore_map.html` — K-core shells (new): nodes color-coded by network position
     - Red (k≥30): Inner core, highest centrality
     - Orange (k=25–29): EM connectomics zone, structurally central
     - Green (k=20–24): Bridge papers
     - Purple/Gray: Peripheral papers
   - `evolution_graph.html` — Temporal evolution of research (streamgraph, 2000–2025)

3. **Study Materials:**
   - `ocar_entries.json` — 200 papers with OCAR cards (Opportunity/Challenge/Action/Resolution/Future Work)
   - `ocar_entries.yaml` — Same, ready to append to `_data/journal_papers.yml`
   - Each card includes: beginner/intermediate/advanced summaries, discussion prompts, key figures

4. **Quality Assurance:**
   - `strategic_audit.md` — Papers flagged for human review (5 lenses), with domain labels
   - `duplicate_merge_log.json` — What was consolidated + impact on rankings
   - `author_merge_log.json` — Author name variants merged
   - `inclusion_metadata.json` — Full provenance for each paper

5. **Publishable Summary:**
   - `corpus_stats.json` — 7,925 papers, 94K edges, 30 communities, coverage by technique family
   - `validation_report.json` — Expert recall (% of 66 researchers' papers recovered)

---

## Workflow: No OpenAlex Access (After Initial Corpus Collection)

If OpenAlex becomes unavailable mid-workflow:

```bash
# Steps 1–2 are cached; steps 3+ use cached data only

# Step 3 onward: no API calls
python 03_compute_metrics.py      # Uses local graph
python 04_validate.py             # Uses local corpus
python 05_html_report.py          # Generates visualization
python 06_reading_list.py         # Creates reading list
python 07_evolution_graph.py      # Generates timeline
python 08_generate_ocar.py        # Generates OCAR (via Claude API, not OpenAlex)
python 09_graph_analysis.py       # K-core, gaps, etc.
python 10_apply_merges.py         # Author merges
python 11_strategic_audit.py      # Audit report

# QA/QC phases: no API calls (use cached review data)
python 12_dedup_review.py         # Generate TSV
python 12_auto_review.py          # Auto-accept high-confidence
python 12_apply_duplicate_merges.py # Apply merges
python 13_review_citations.py     # Uses cached citations
python 13_inclusion_decisions.py  # Synthesizes decisions
python 14_update_corpus_and_rerank.py # Final update
```

**Cache locations:**
- `cache/work_*.json` — paper metadata by OpenAlex ID
- `cache/author_*.json` — author metadata
- `cache/review_citations_*.json` — review references

All API queries check cache first. No Internet required after initial corpus collection.

---

## Quality Metrics: What We Check

### Part A (Automated):

1. **Expert recall:** % of papers from 66 researchers' seed lists recovered
2. **Corpus coverage:** Papers from each technique family represented
3. **Graph structure:** 7,925 nodes, 94K edges, 30 communities detected
4. **Ranking stability:** Top-10 papers stable across metric variations

### Part B (QA/QC):

1. **Duplicate precision:** % of AUTO_ACCEPT decisions that are true duplicates (target: ≥95%)
2. **Author merge precision:** % of name merges that are same person (target: ≥90%)
3. **Domain classification:** % em_connectomics labels correct (target: ≥85%)
4. **Off-topic filtering:** % papers marked off-topic are actually noise (target: ≥90%)
5. **Decision transparency:** Every paper has documented source + criteria

See `HEURISTICS_VALIDATION.md` for detailed validation strategy.

---

## Recommended Workflow for Production

### Session 1: Corpus Collection (2–4 hours)

```bash
# Steps 1–11 (requires OpenAlex)
bash run_pipeline.sh
export ANTHROPIC_API_KEY=sk-ant-...
python 08_generate_ocar.py
```

**Deliverables:**
- `reading_list.json` (top 500)
- `field_map.html`, `kcore_map.html`, `evolution_graph.html`
- `ocar_entries.yaml` (200 cards with detailed study materials)
- `strategic_audit.md` (papers flagged for review, with domain labels)

### Session 2: QA/QC & Corpus Enhancement (2–4 hours, no API)

```bash
# Step 12: Detect duplicates
python 12_dedup_review.py
# ← User reviews TSV (30–60 min)

# Step 12b: Auto-review
python 12_auto_review.py --confidence-level high

# Step 12c: Apply merges
python 12_apply_duplicate_merges.py

# Step 13–14: Final decisions & rerank
python 13_review_citations.py
python 13_inclusion_decisions.py
python 14_update_corpus_and_rerank.py --full-rebuild
```

**Deliverables:**
- Updated `reading_list_final.json` with domain labels and k-core positions
- `inclusion_metadata.json` (provenance for every paper)
- `field_map.html`, `kcore_map.html`, `evolution_graph.html` (updated rankings)

### Session 3: Publish Results

```bash
# Copy OCAR cards to website
cp output/ocar_entries.yaml ../../../_data/journal_papers.yml

# Update analysis page
cp output/field_map.html ../../../assets/analysis/
cp output/kcore_map.html ../../../assets/analysis/
cp output/evolution_graph.html ../../../assets/analysis/

# Commit and deploy
git add -A
git commit -m "Update bibliography with QA/QC improvements, final rankings"
git push
```

---

## Troubleshooting

### "OpenAlex API rate limit exceeded"
- Solution: Wait 60 seconds, rerun. Cache handles resumption. Max 9 requests/second.

### "duplicate_review.tsv not found"
- Run `python 12_dedup_review.py` first to generate it.

### "domain_labels.json missing"
- Run `python 14_update_corpus_and_rerank.py` which generates domain labels.

### "OCAR generation stalling"
- Normal: ~30 sec per paper, 200 papers = 100+ min. Check `output/ocar_cache/` for progress.
- Resume: rerun `python 08_generate_ocar.py` (fully resumable).

### "Rerank changed top-100 significantly"
- Check: Did you apply duplicate merges? Large consolidations shift PageRank.
- Expected: Top-20 typically stable; ranks 100–500 may shift 10–20 positions.

---

## Performance Notes

- **Corpus collection** (step 1): 45 min, ~2,500 API queries, needs throttling
- **Metrics** (step 3): 20 min on modern laptop, dominated by PageRank
- **QA/QC** (steps 12–14): 10 min total once TSV review complete
- **OCAR generation** (step 8): 100 min for 200 papers (Claude API, parallel safe)
- **Visualization** (steps 5, 7): 10–20 min, D3.js rendering
- **Reranking** (step 3 re-run): 20 min, only if corpus changed significantly

**Bottleneck:** OpenAlex corpus collection (45 min) and OCAR generation (100 min).

---

## Files Generated (65 total)

**In `output/`:**

- **Rankings:** `reading_list.json`, `paper_rankings.json`, `author_rankings.json`
- **Graphs:** `graphs/citation_graph.json`, `graphs/co_citation.json`, `graphs/coupling.json`, `graphs/coauthorship.json` (~500 MB total)
- **Visualizations:** `field_map.html` (~5 MB), `kcore_map.html` (~3 MB), `evolution_graph.html` (~2 MB)
- **Study cards:** `ocar_entries.json`, `ocar_entries.yaml` (+ `ocar_cache/` 322 papers)
- **Metadata:** `communities.json`, `corpus_stats.json`, `validation_report.json`
- **QA/QC:** `strategic_audit.json`, `duplicate_merge_log.json`, `inclusion_metadata.json`, etc.
- **TSV review files:** `duplicate_review.tsv`, `author_dedup_review.tsv` (human review)

**Total size:** ~800 MB (graphs gitignored; ~300 MB committed)

---

## Reproducibility & Git

- **Corpus is deterministic** if `cache/` is preserved
- **Louvain communities** may shift slightly (seed=42, but non-deterministic edge order)
- **Visualizations** regenerate identically if graphs unchanged
- **OCAR cards** cached; re-runs skip already-generated papers

**Recommended:** Commit `cache/` once, then never change. Re-runs will be identical.

---

## Next Steps Post-Publication

1. **Schedule:** Re-run quarterly (Q1, Q2, Q3, Q4) to catch new major papers
2. **Expert feedback:** Collect citations of papers not in top-500 via journal club discussions
3. **Domain expansion:** Consider adding macro-connectomics papers (dMRI/fMRI) if demand
4. **Tool integration:** Link OCAR cards to code/data repositories when available
5. **Community:** Publish reading list & encourage expert annotations

---

## Contact & Issues

- **Questions about pipeline:** See `README.md` (architecture) and `streamlined_plan.md` (QA/QC)
- **Heuristics concerns:** See `HEURISTICS_VALIDATION.md` (defense of multi-signal scoring)
- **Reproducibility:** Check `cache/` is committed; preserve between runs
