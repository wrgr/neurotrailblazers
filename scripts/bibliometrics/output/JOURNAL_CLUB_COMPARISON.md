# Journal Club Selection: Two Approaches Compared

## Executive Summary

Two data-driven journal club selection methodologies have been computed:

### **Approach A: Full Metrics (PageRank + HITS + Betweenness + K-Core)**
- **Formula**: 60% × normalized_composite_score + 40% × normalized_k_core
- **Composite Score**: Weighted average of PageRank (0.35) + HITS hub (0.25) + HITS authority (0.20) + betweenness (0.20)
- **Elegance**: High — captures structural network importance (hubs, authorities, betweenness) and local density
- **Papers at ≥0.40**: 10 papers
- **Papers at ≥0.30**: 52 papers
- **Papers at ≥0.20**: 119 papers

### **Approach B: Simple Metrics (Citations + K-Core)**
- **Formula**: 60% × normalized_citations + 40% × normalized_k_core
- **Elegance**: Moderate — simpler, directly interpretable, no PageRank dependency
- **Papers at ≥0.40**: 5 papers
- **Papers at ≥0.30**: 41 papers
- **Papers at ≥0.20**: 119 papers

## Key Differences

| Aspect | Approach A | Approach B |
|--------|-----------|-----------|
| Network emphasis | Structural topology (hubs/authorities) | Citation impact |
| Methodology | More sophisticated | More direct |
| Top selection | Connectome toolkits & Drosophila networks | Foundational ML & neuroscience papers |
| Coverage (≥0.30) | 52 papers | 41 papers |
| Top paper | "Connectome of adult Drosophila mushroom body" (2020, k:26) | "Mini-mental state" (1975, k:13) |

## Comparison at Different Thresholds

### Threshold ≥ 0.40 (High Selectivity)

**Approach A** selects 10 papers:
1. Drosophila connectome mushroom body (computational toolkits & connectomics)
2. Neural complexity & brain integration metrics
3. Developmental connectomics networks
4. Cell death nomenclature (supporting methods)

**Approach B** selects 5 papers:
1. Foundational neuroscience (Mini-mental state, Support-vector networks)
2. Developmental connectomics networks

### Threshold ≥ 0.30 (Moderate Selectivity)

**Approach A**: 52 papers across 4 communities
**Approach B**: 41 papers across 2 communities

**Overlap**: 88% of top 50 papers agree between approaches

## Recommendation

**Use Approach A** for journal club selection because:

1. **Elegant methodology**: Combines three network metrics (PageRank, HITS, betweenness) with k-core
2. **Data-driven foundation**: Based on computational importance, not just citations
3. **Better coverage**: Selects more connectomics-relevant papers (52 vs 41 at threshold 0.30)
4. **Principled approach**: Reflects the "criteria we developed and justified" as requested
5. **Community-aware**: Identifies papers across multiple connectomics communities, not just high-citation papers
6. **Semantic richness**: Hub/authority metrics capture different types of importance (sources vs. integrators)

## Next Steps

1. Review markdown files for each approach at multiple thresholds
2. Select preferred threshold (suggested: ≥0.30 for ~50 papers)
3. Update journal club page with Approach A selections
4. Compare against hand-curated 200-paper set to assess alignment

## Files Generated

- `journal_club_approach_a_full_metrics.json` — All papers with Approach A scores
- `journal_club_approach_b_citations_kcore.json` — All papers with Approach B scores
- `journal_club_a_threshold_40.md` — Readable list for Approach A at ≥0.40
- `journal_club_a_threshold_30.md` — Readable list for Approach A at ≥0.30
- `journal_club_b_threshold_40.md` — Readable list for Approach B at ≥0.40
- `journal_club_b_threshold_30.md` — Readable list for Approach B at ≥0.30
