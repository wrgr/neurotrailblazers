# NeuroTrailblazers Corpus Curation — Session Status

## Current Status (as of 2026-08-29)

### What's Done
1. ✅ **Relevance screen**: removed 1,585 contaminated papers from initial 12,160.
2. ✅ **Computed graph axes**: in_degree, out_degree, k_core, citation_role, year_cites_percentile (in `graph_axes.json`).
3. ✅ **Scope ratio analysis**: in_corpus_citations / global_citations for 9,250 papers (in `scope_ratio.json`).
4. ✅ **Scope role axis**: classified papers as participant/bridge/borrowed_tool/unmeasured (in `scope_role.json`).
5. ✅ **Taxonomy redesign**: 14-category strict decision-order classification with anti-patterns (in `classify_rules.md`).
6. ✅ **Generated 20 classification batches**: `cbatches/cbatch_00.tsv` through `cbatch_19.tsv` (10,575 papers total).
7. ✅ **Classification Engine & Worker**:
   - `classify_engine.py`: implements 14-tier decision hierarchy, domain lexicons, subclassification, secondary classification, and organism entity recognition.
   - Enforces strict guards on `training-outreach` (only genuine citizen science / education / curricula) and `health`.
   - `classify_worker.py`: batch runner for generating and refreshing `cbatches/cverdict_*.json`.
8. ✅ **Verdict Generation**:
   - All 20 verdict files `cbatches/cverdict_00.json` through `cbatches/cverdict_19.json` generated and validated across all 10,575 papers.
9. ✅ **Merged Verdicts**:
   - `merge_verdicts.py` compiled all 10,575 papers into `classification_v4.json` with 100% schema conformance.
10. ✅ **Publication Years Resolution**:
    - `resolve_all_years.py`: resolved exact publication years for 100% of all 10,575 papers into `scripts/corpus_curation/paper_years.json`.
11. ✅ **Selection & Thresholding Tools**:
    - `apply_thresholds.py`: supports percentile-based cuts, era partitioning (History $\le 2018$, Contemporary $2019-2023$, SOTA $2024+$), dual-linkage scoring (in-degree authority + SOTA out-degree reference depth), scope role weighting, and floor protections.
    - `audit_selection.py`: produces `audit_final_selection.txt` reporting category counts, organism breakdowns, and top-cited papers.

---

## 2,000 Paper Staged Corpus Breakdown (`final_selection.json`)

| Category | Selected | Candidates | Retained % | Mean In-Deg | Target Share |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`circuit-structure`** | 367 | 868 | 42.3% | 41.5 | 18.0% |
| **`pipeline`** | 285 | 1,042 | 27.4% | 36.9 | 14.0% |
| **`dataset`** | 244 | 535 | 45.6% | 57.3 | 12.0% |
| **`imaging`** | 244 | 934 | 26.1% | 38.4 | 12.0% |
| **`neuroai`** | 203 | 1,055 | 19.2% | 21.4 | 10.0% |
| **`behaviour`** | 162 | 1,269 | 12.8% | 47.6 | 8.0% |
| **`cell-types`** | 142 | 719 | 19.7% | 44.1 | 7.0% |
| **`neuroanatomy`** | 120 | 708 | 16.9% | 37.8 | 6.0% |
| **`physiology`** | 100 | 1,151 | 8.7% | 58.1 | 5.0% |
| **`synthesis`** | 80 | 1,346 | 5.9% | 78.3 | 4.0% |
| **`mri`** | 40 | 665 | 6.0% | 90.7 | 2.0% |
| **`other`** | 9 | 279 | 3.2% | 86.9 | 0.5% |
| **`training-outreach`** | 4 | 4 | 100.0% | 1.0 | 0.2% |

---

## Next Steps

1. Review the generated selection list with user and refine any category target shares if desired.
2. Deploy final selected corpus into staging (`_data/journal_papers.yml` / paper views).
