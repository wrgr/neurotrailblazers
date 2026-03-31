# Final Recomputation & Visualization Regeneration

## Current Status

✅ **Phase Complete: Enrichment & Validation**
- Seed list (200 papers) verified: 185/200 in corpus (92.5%)
- Missing papers identified & flagged: 15 papers (pending verification)
- Author merging applied: 17 expert name merges (35,797 → 35,641 authors)
- Paper roles refined: 10 granular categories with data-driven thresholds
- Key experts identified: Career arcs extracted for top 50 researchers

📊 **Corpus Ready for Final Recomputation**
- Size: 7,503 papers (with author merges)
- Authors: 35,641 (after merging)
- Citation edges: 85,589 (directed)
- Co-authorship edges: 511,670 (undirected)

---

## Final Recomputation Pass: Tasks

### 1. **Recompute All Metrics** (on full corpus)
- [ ] PageRank (citation network, all 7,503 papers)
- [ ] HITS hub/authority scores
- [ ] Betweenness centrality
- [ ] K-core decomposition
- [ ] Community detection (Louvain)
- [ ] Composite scores (updated formula)

**Output:** `paper_rankings_all_final.json` (with fresh metrics)

### 2. **Recompute Author Rankings**
- [ ] Paper count (using merged author names)
- [ ] Co-author network metrics
- [ ] PageRank on co-authorship network
- [ ] Specialization scores
- [ ] Career timeline statistics

**Output:** `author_rankings_final.json` (35,641 authors)

### 3. **Regenerate Visualizations**
- [ ] **field_map_full.html** — Citation network (7,503 nodes, 85K edges)
  - Force-directed layout with zoom/pan
  - Ranked list (all papers, sortable)
  - Toggle citation/co-authorship networks
  
- [ ] **coauthor_map_full.html** — Co-authorship network (35,641 nodes)
  - Force-directed layout
  - Ranked author list
  
- [ ] **career_arcs_plot.html** — Interactive visualization (NEW)
  - Timeline: publications per year × expert
  - Color by paper role/importance
  - Hover: citation impact trajectory
  
- [ ] **journal_club_threshold_*.html** (4 versions)
  - Refresh with updated metrics
  - Threshold 10, 15, 20, 30
  
- [ ] **kcore_map.html** — K-core shells
  - Updated k-values and coloring
  
- [ ] **evolution_graph_full.html** — Field timeline
  - Verify data freshness

- [ ] **index.html** — Dashboard (updated)
  - Link to all visualizations
  - Updated statistics

### 4. **Journal Club Refresh** (all thresholds)
- [ ] Compute new importance scores
- [ ] Apply thresholds: 0.10, 0.15, 0.20, 0.30
- [ ] Assign tier labels (Platinum/Gold/Silver/Bronze)
- [ ] Calculate in-degree/out-degree metrics
- [ ] Generate markdown + JSON for each threshold

**Output:** 4 sets of files (threshold_10, 15, 20, 30)

### 5. **Comprehensive Documentation Update**
- [ ] BIBLIOGRAPHY_ANALYSIS_DOCS.md
  - Verify corpus size: 7,503 papers
  - Verify author count: 35,641 (after merges)
  - Update metrics explanations
  - Document career arc visualization
  
- [ ] METHODOLOGY_AND_PIPELINE.md (NEW)
  - Document full pipeline flow
  - Explain metric computations
  - Discuss thresholds and choices
  - Flag limitations & biases
  - Prepare for critical review

---

## Quality Assurance Checklist

Before considering this "ready for review":

- [ ] Verify all 7,503 papers have metrics
- [ ] Check author merges applied correctly (Gray-Roncal, Jefferis, etc.)
- [ ] Spot-check: top 10 papers ranked correctly
- [ ] Spot-check: Lichtman papers present and ranked appropriately
- [ ] Journal club at threshold 0.20 has ~22 papers ✓
- [ ] Visualizations load without errors
- [ ] Dashboard links all work
- [ ] Career arcs show expected trajectories
- [ ] Seed list (200 papers) confirms 185/200 in corpus

---

## Execution Plan

**Recommended sequence:**
1. Re-run PageRank/HITS/betweenness (can parallelize)
2. Re-run k-core decomposition
3. Re-detect communities
4. Recompute author rankings (depends on corpus)
5. Regenerate ALL visualizations in parallel
6. Update documentation
7. QA spot checks
8. Lock for methodology review

**Estimated scope:** 6-8 discrete computational tasks, some parallelizable

---

## For Future: Methodology Review

Once this recomputation is complete and verified, separate work session to:

1. **Critical review of thresholds**
   - In-degree/out-degree cutoffs (10 for each direction — too strict? too loose?)
   - Composite score formula (80% PageRank + 20% k-core — still optimal?)
   - Journal club thresholds (0.10, 0.15, 0.20, 0.30 — right choices?)

2. **Methods paper weighting**
   - Current: out-degree ≥37 (top 5%)
   - Consider: boost formula for infrastructure papers?
   - Consider: temporal dynamics (older methods vs. newer)?

3. **Community detection robustness**
   - Louvain algorithm choices (randomness, resolution)
   - Alternative: other clustering methods?
   - Validation: compare to hand-labeled communities

4. **Author merging completeness**
   - Are there other Gray-Roncal-like merges we missed?
   - Automated name similarity scoring?

5. **Graph properties**
   - Citation network: power-law? small-world?
   - Co-authorship: assortative? community structure?

---

## Next Session: "Methodology Review & Refinement"

Once locked and verified, can tackle:
- Refined composite scoring
- Dynamic importance (temporal decay)
- Cross-validation against external rankings
- Potential precomputed indices for faster querying

---

**Ready to execute final recomputation pass?**
