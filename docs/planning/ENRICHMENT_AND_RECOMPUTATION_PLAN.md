# Enrichment & Recomputation Plan

## Current State

✅ **Phase 1 Complete:**
- Author merging applied (17 expert name merges)
- Paper role categories refined (granular, lower thresholds)
- Key experts identified (top 50 researchers)
- Career arcs extracted (publication trajectories)
- Synthesis papers analyzed (references checked)

**Result:** All papers cited by synthesis experts already in corpus — no enrichment candidates needed (good news!)

---

## Phase 2: Seed List Comparison & Strategic Enrichment

### Step 1: Load User Seed List
- Load the original 200 hand-curated papers
- Compare against current corpus (7,503 papers)
- Identify missing papers from seed list

### Step 2: Cross-Reference with Key Experts
- Check which seed papers are authored by top 50 experts
- Check which seed papers are cited by synthesis experts
- Identify missing papers by key authors

### Step 3: Strategic Enrichment Decision
**Framework:** Confidence >0.5 threshold, with justification
- Papers cited by 2+ expert synthesis papers ✓ (already in corpus)
- Papers from seed list by key experts (TO BE ADDED)
- Papers with explicit domain expert notation (TO BE REVIEWED)

**Flag for manual review:**
- Decision: INCLUDE / EXCLUDE / MAYBE
- Confidence score: 0.0-1.0
- Reason: Why we flagged this paper

---

## Phase 3: Final Recomputation Pass

### After enrichment is approved, recompute everything:

1. **Paper Metrics** (all papers)
   - PageRank on citation graph (85,000+ edges)
   - HITS hub/authority
   - Betweenness centrality
   - K-core decomposition
   - Composite scores

2. **Author Rankings** (all 35,797 authors)
   - Productivity (paper count after merges)
   - Collaboration breadth (co-author count)
   - PageRank on co-authorship network
   - Updated with merged names

3. **Network Analysis**
   - Community detection (Louvain) — may change with new papers
   - Citation neighborhoods
   - Collaboration patterns

4. **Journal Club** (new selections)
   - Recompute on updated paper rankings
   - 4 thresholds: 0.10, 0.15, 0.20, 0.30
   - Re-evaluate role-weighted scores

5. **Visualizations**
   - field_map_full.html (updated citation network)
   - coauthor_map_full.html (updated collaboration network)
   - career_arcs visualization (publication trajectories)
   - kcore_map.html (updated structural density)
   - evolution_graph_full.html (temporal evolution)

6. **Career Arc Visualization** (NEW)
   - Timeline plot: publications per year × expert
   - Color by paper role (landmark, foundational, synthesis, etc.)
   - Collaboration evolution (co-authors over time)
   - Impact trajectory (citations accumulating over time)

---

## Execution Order

```
1. Load seed list
   ↓
2. Compare with corpus → missing papers list
   ↓
3. Create enrichment candidates with justification
   ↓
4. Manual review → approve/reject decisions
   ↓
5. Add approved papers to corpus
   ↓
6. Recompute all metrics (Step-by-step)
   - PageRank, HITS, betweenness
   - K-core decomposition
   - Communities
   - Author rankings
   ↓
7. Regenerate visualizations
   - Updated graphs with new edges
   - Journal club at all thresholds
   - Career arc plots
   ↓
8. Final validation
   - Check for new anomalies
   - Verify citation counts
   - Spot-check key authors
```

---

## Data Flow Diagram

```
User Seed List (200 papers)
    ↓
Compare with Corpus (7,503)
    ↓
Missing Papers
    ↓
Key Expert Analysis
    ↓
Enrichment Candidates (flagged)
    ↓
Manual Review → APPROVED
    ↓
Add to Corpus → Corpus_enriched.json
    ↓
Recompute Metrics (all papers)
    ↓
Update Rankings, K-core, Communities
    ↓
Regenerate Visualizations
    ↓
Final Output (complete, enriched pipeline)
```

---

## Key Decisions to Make

1. **Enrichment threshold:** Confidence >0.5 confirmed?
2. **Seed list scope:** Compare all 200, or just key ones?
3. **Author merge confidence:** >0.5 threshold for name merges?
4. **Career arc detail:** Show all 50 experts, or top 15?

---

## Files to Create/Update

**New files:**
- `seed_list_comparison.json` — Missing papers from seed
- `enrichment_decisions_log.json` — Flagged papers with approvals
- `corpus_enriched.json` — Updated corpus with new papers
- `career_arcs_visualization.html` — Interactive timeline

**Updated files:**
- `paper_rankings_all.json` — Recomputed metrics
- `author_rankings.json` — Recomputed with full corpus
- `journal_club_threshold_*.json` — New selections
- All visualization HTML files

---

## Timeline

- **Phase 2 (Enrichment):** 1 step — load seed list, compare, flag
- **Phase 3 (Recomputation):** 6-7 steps — can parallelize some metrics
- **Total:** Ready when you approve enrichment candidates

---

## Next Action

→ Load user seed list and compare against corpus (7,503 papers)
