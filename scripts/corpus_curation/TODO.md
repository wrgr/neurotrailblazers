# NeuroTrailblazers Corpus Curation — Session Resumption Plan

## Current Status (as of 2026-08-29)

**Session ended due to token exhaustion after launching 20 parallel LLM classification workers.**

### What's Done
1. ✅ Relevance screen: removed 1,585 contaminated papers from initial 12,160
2. ✅ Computed graph axes: in_degree, out_degree, k_core, citation_role, year_cites_percentile (in `graph_axes.json`)
3. ✅ Scope ratio analysis: in_corpus_citations / global_citations for 9,250 papers with usable data (in `scope_ratio.json`)
4. ✅ Scope role axis: classified papers as participant/bridge/borrowed_tool/unmeasured (in `scope_role.json`)
5. ✅ Redesigned taxonomy: 14-category strict decision-order classification (spec in `classify_rules.md`)
6. ✅ Generated 20 classification batches: `cbatches/cbatch_00.tsv` through `cbatch_19.tsv` (20 × ~529 papers each)
7. ✅ Launched 20 parallel LLM workers to classify all batches using `classify_rules.md` decision order

### What's Incomplete
1. ❌ **BLOCKING: Classification verdicts** — Only 3 of 20 workers completed before hitting rate limits:
   - `cbatches/cverdict_03.json` ✅ complete
   - `cbatches/cverdict_11.json` ✅ complete
   - `cbatches/cverdict_15.json` ✅ complete
   - `cbatches/cverdict_00.json` through `cverdict_19.json` (except above) ❌ NEED TO RESTART

2. ❌ Merge classification verdicts from all 20 workers into unified `classification_v4.json`
3. ❌ Validate worker agreement on boundary cases (especially dataset vs pipeline, circuit-structure vs behaviour)
4. ❌ Apply per-category per-era thresholds using scope_role axis + share weights + floor protection
5. ❌ Generate final top-k selection lists per cell (categories × eras)
6. ❌ Audit resulting selection against graph metrics and citation ratios

---

## Rate Limit Status

### Claude API (Opus/Sonnet)
- **Session limit:** resets 2:20 AM UTC (likely reset by now)
- **Weekly limit:** resets Sep 1, 7 AM UTC
- **Status as of 2026-08-29:** Unknown if session limit has reset; need to check

### Semantic Scholar API
- **Status:** last used in classification workers; may have per-worker throttling

---

## Next Steps to Resume

### 1. **Restart Classification Workers (CRITICAL PATH)**
   - Check if session/weekly rate limits have reset
   - For each missing batch `N` in [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 17, 18, 19]:
     - Run `scripts/classify_worker.py --batch N --rules requery/classify_rules.md --input requery/cbatches/cbatch_N.tsv --output requery/cbatches/cverdict_N.json`
   - Each worker must produce JSON schema: `{<doi>: {"classification": "...", "subclassification": "...", "secondary_classifications": [...], "organism": [...]}, ...}`
   - **Consistency check:** Sample 10 papers from each worker's output and verify classification against `classify_rules.md` anti-examples
   - **Drop-rate measurement:** For each worker, compute classification distribution and compare to expected entropy — should be consistent across workers (within ±5%)

### 2. **Merge Verdicts**
   - Combine all 20 `cverdict_*.json` files into `classification_v4.json`
   - Schema: `{<doi>: {"classification": "...", ...}}`
   - Run consistency check on merged data (no doi should have conflicting classifications from different workers)

### 3. **Audit Boundary Cases**
   - Papers classified as `dataset` that rank high on in_degree: verify they release a dataset, not just analyze one
   - Papers classified as `circuit-structure` that rank high on in_degree: spot-check 20 by hand to confirm they measure connectivity
   - Papers classified as `behaviour` vs `circuit-structure`: ensure they don't conflate circuit analysis with behavioural phenotype analysis
   - Use abstracts in `requery/universe_meta.json` for ambiguous cases

### 4. **Apply Thresholds (Using Scope Role Axis)**
   - Do NOT use ratio-based cuts; use scope_role axis (participant/bridge/borrowed_tool/unmeasured)
   - For each of 14 classification × era combinations, apply share weights + floor protection:
     - Dataset: 90% share, floor 8 per era
     - Circuit-structure: 75% share, floor 6 per era
     - Pipeline: 70% share, floor 5 per era
     - Imaging: 65% share, floor 4 per era
     - Behaviour: 55% share, floor 3 per era
     - Cell-types: 60% share, floor 3 per era
     - NeuroAI: 55% share, floor 2 per era
     - Training-outreach: 70% share, floor 1 per era
     - Neuroanatomy: 50% share, floor 2 per era
     - Physiology: 40% share, floor 1 per era
     - Synthesis: 40% share, floor 2 per era
     - Other: 25% share, floor 0
     - MRI: 30% share, floor 1 per era
     - Health: 30% share, floor 1 per era
   - Eras: history (≤2018), contemporary (2019-2024), sota (2025+)
   - Selection metric: `year_cites_percentile` (rank within era cohort) + `citation_role` bias
   - Output: `final_selection.json` with selected DOIs + reason (share/floor/rank)

### 5. **Final Audit**
   - Compute selection statistics per cell (count, in_degree mean, citation_role distribution)
   - Compare to legacy corpus and `candidate_pool.json` coverage:
     - Should maintain ~90% of dataset papers
     - Should improve NeuroAI/health/behaviour coverage vs strict ratio cuts
   - Hand-sample 50 papers from underrepresented cells (health, training_outreach) and verify by title
   - Generate `audit_final_selection.txt` with:
     - Per-category/era counts and coverage statistics
     - Top-5 papers per category by in_degree
     - Bottom-5 papers per category (floor protection) with rationale

### 6. **Deploy to Corpus**
   - Once audit passes, swap `classification_v4.json` into `_data/journal_papers.yml`
   - Regenerate dependent files (`paper_views/*`, graph metadata)
   - Commit and push to main branch (or staging branch TBD)

---

## Key Files and Locations

### Scratchpad (ephemeral, work-in-progress):
- `/tmp/claude-0/-home-user-neurotrailblazers/7d6ef4bf-5672-5dcc-ab95-ea75d0c1e6b2/scratchpad/requery/`
  - `classify_rules.md` — taxonomy spec, decision order, anti-patterns
  - `cbatches/cbatch_*.tsv` — 20 input batches (DOI|title|venue|abstract)
  - `cbatches/cverdict_*.json` — classification verdicts (3/20 complete)
  - `classification_v3.json` — keyword-based classification (reference; workers will replace)
  - `graph_axes.json` — all 10,575 papers with citation metrics
  - `scope_ratio.json` — in_corpus/global citation ratios
  - `scope_role.json` — participant/bridge/borrowed_tool/unmeasured classification
  - `universe_meta.json` — DOI→{title, abstract, venue, year, ...}

### Repo (to be committed):
- `scripts/` — add `classify_worker.py`, `merge_verdicts.py`, `apply_thresholds.py`, `audit_selection.py`
- `_data/` — `classification_v4.json` (output), any intermediate reference files
- Documentation: `CORPUS_METHODOLOGY_PART_1B.md` (summarize what was done)

---

## Environment Notes

- **Model for classification workers:** Claude Haiku 4.5 (switched from Opus due to token exhaustion; Haiku has lower cost and should complete all batches without hitting weekly limits)
- **Classification window:** Aug 28, 22:00 UTC → Aug 29, after token reset
- **Testing hypothesis:** With Haiku + no parallel agent overhead, all 20 workers should complete in ~30-40 minutes

---

## Known Issues / Anti-Patterns (from prior session)

These were flagged as failures; confirm workers avoid them:

1. **White 1986 should NOT be in `other`** — it's a canonical `circuit-structure` paper (first *C. elegans* connectome)
2. **FAFB should NOT be in `imaging`** — it's a `dataset` paper (FlyEM's entire-brain Drosophila EM reconstruction)
3. **Hemibrain should NOT be in `pipeline`** — it's a `dataset` paper (Janelia's mushroom-body connectome)
4. **"Space-time wiring specificity..." should NOT be in `training-outreach`** — it's a `circuit-structure` paper about retinal wiring rules, not a training-data paper; "training" has a specific meaning in this taxonomy (pedagogical materials)
5. **"The Nervous System: Structure and Function in Disease"** (1973 textbook) should be dropped or marked as `other` — keyword classifier caught "disease" but it's a reference work, not a research paper

---

## Contact / Questions

If resuming this work:
- All classifications use `classify_rules.md` decision order (strict, deterministic)
- Anti-patterns are in that same file; verify workers read them
- For boundary cases, read abstract from `universe_meta.json` and apply decision order manually
- If workers diverge on a paper, log it and re-run that batch with higher verbosity

Good luck! — Claude (prior session, 2026-08-28)
