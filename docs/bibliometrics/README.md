# Bibliometrics Pipeline — Technical Documentation

Complete documentation for the EM connectomics bibliometrics analysis pipeline.

## Files

1. **METHODOLOGY_AND_PIPELINE.md**
   - Pipeline overview and data flow
   - Metric computations (PageRank, HITS, betweenness, k-core, composite score)
   - Paper role classification (10 categories)
   - Author merging strategy (17 name merges)
   - Journal club selection philosophy
   - Visualization design rationale
   - Known limitations and biases
   - QA checklist
   - Future improvements
   - Data dictionary

2. **BIBLIOGRAPHY_ANALYSIS_DOCS.md**
   - Dataset overview (7,503 papers, 35,641 authors)
   - Quality assurance metrics
   - Visualization descriptions
   - Paper metrics explanation
   - Author rankings methodology

3. **SEMANTIC_RELEVANCE_FLAGGING.md**
   - Flags in top 100 papers potentially unrelated to EM connectomics
   - Identifies authors primarily focused on fMRI/functional connectivity
   - Recommendations for filtering/metadata
   - Core EM connectomics researchers highlighted

## Quick Reference

**Key Statistics:**
- Papers: 7,503 (with all metrics)
- Authors: 35,641 (after 17 name merges)
- Citation edges: 85,589
- Communities: 30 (Louvain detection)
- K-core range: 0–32

**Top 20 People:** See METHODOLOGY_AND_PIPELINE.md Section 10 (References)
**Top 20 Papers:** See METHODOLOGY_AND_PIPELINE.md Section 10 (References)
**Will Gray-Roncal:** Rank #65, 28 papers (merged from 4 name variants)

**Recommended Journal Club Threshold:** 20 (~22 papers, balanced scope)

---

For implementation details, see `/scripts/bibliometrics/` for all code.
