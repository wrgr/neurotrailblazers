# Weighted Author Contribution Implementation Guide

## ✅ Implementation Complete

The weighted author contribution system has been fully implemented and is ready to use after the deduplication and merging process.

## What Was Implemented

### Phase 1: Author Position Metadata Enrichment
**File**: `scripts/bibliometrics/02_build_graphs.py`

The `enrich_corpus_with_author_positions()` function adds position metadata to every paper:
- **first**: First author
- **last**: Last author (different from first)
- **middle**: Any author in positions 2 to n-1
- **only**: Single-author papers

This metadata is stored in each paper's `author_positions` field and preserved in the output corpus.

### Phase 2: Weighted Metrics Computation
**File**: `scripts/bibliometrics/03_compute_metrics.py`

#### New Functions Added:

**`get_author_position_weight(position, alpha=2.0)`**
- Returns weight multiplier: first/last authors get `alpha` (default 2.0), middle gets 1.0
- Single-author papers get 1.0 (no penalty)

**`compute_author_metrics_weighted(coauthorship_graph, corpus, paper_metrics, first_author_weight=2.0, last_author_weight=2.0)`**
- Computes metrics with position-based PageRank distribution
- Tracks:
  - `total_pagerank_weighted`: PageRank weighted by author position
  - `first_author_count`, `last_author_count`, `middle_author_count`, `only_author_count`
  - All standard network metrics (betweenness, degree, eigenvector centrality)

**`rank_authors_weighted(author_metrics, first_weight=2.0, last_weight=2.0)`**
- Creates composite ranking with position weighting
- Score formula (40-20-15-15-10 weighting):
  ```
  composite_score_weighted =
    0.40 * (weighted_pagerank / max_weighted_pagerank) +
    0.20 * (betweenness / max_betweenness) +
    0.15 * (weighted_degree / max_degree) +
    0.15 * (recent_papers / total_papers) +
    0.10 * (first_author_count + last_author_count) / total_papers
  ```

### Phase 3: Separate First/Last Author Analysis
**File**: `scripts/bibliometrics/03b_first_last_author_analysis.py` (NEW)

Generates three independent analyses:

1. **`first_author_rankings.json`**
   - Authors ranked by citations on papers where they're first author
   - Identifies research drivers (those initiating new work)
   - Includes: paper count, total citations, avg citations/paper, year range, journals

2. **`last_author_rankings.json`**
   - Authors ranked by citations on papers where they're last author
   - Identifies research leaders/PIs (providing senior direction)
   - Same metrics as first author analysis

3. **`single_author_rankings.json`**
   - Authors with single-author papers
   - Identifies independent researchers

4. **`first_last_author_distribution.json`**
   - Summary statistics and top-10 lists
   - Good for overview documents

## How to Run

### After Deduplication & Merging

Run the enhanced pipeline in this order:

```bash
# Step 2: Build graphs WITH author position enrichment
python scripts/bibliometrics/02_build_graphs.py

# Step 3: Compute weighted metrics
python scripts/bibliometrics/03_compute_metrics.py

# Step 3b: First/last author analysis
python scripts/bibliometrics/03b_first_last_author_analysis.py
```

### Expected Output Files

```
output/
├── corpus_merged.json                    # Updated with author_positions
├── author_rankings.json                  # Original unweighted rankings (unchanged)
├── author_rankings_weighted.json         # NEW: Position-weighted rankings (alpha=2.0)
├── first_author_rankings.json            # NEW: First authors only
├── last_author_rankings.json             # NEW: Last authors only
├── single_author_rankings.json           # NEW: Single-author papers
└── first_last_author_distribution.json   # NEW: Summary statistics
```

## Configuration: Adjusting the Alpha Weight

The weighting system is **fully configurable**. You can easily test different alpha values:

### In main() of 03_compute_metrics.py:

```python
# Default: alpha=2.0
author_metrics_weighted = compute_author_metrics_weighted(
    coauthorship_graph, corpus, paper_metrics,
    first_author_weight=2.0,
    last_author_weight=2.0
)
```

### Try Different Weights:

```python
# Conservative: alpha=1.5
first_author_weight=1.5, last_author_weight=1.5

# Aggressive: alpha=3.0
first_author_weight=3.0, last_author_weight=3.0

# Asymmetric (emphasize first more than last)
first_author_weight=3.0, last_author_weight=1.5

# First authors only (last authors as 1.0)
first_author_weight=2.0, last_author_weight=1.0
```

Each configuration generates identical output filenames, so you can **test multiple weights sequentially**:

```bash
# Test alpha=1.5
# Edit 03_compute_metrics.py with first_weight=1.5, last_weight=1.5
python scripts/bibliometrics/03_compute_metrics.py
cp output/author_rankings_weighted.json output/author_rankings_weighted_alpha1.5.json

# Test alpha=2.0
# Edit 03_compute_metrics.py with first_weight=2.0, last_weight=2.0
python scripts/bibliometrics/03_compute_metrics.py
cp output/author_rankings_weighted.json output/author_rankings_weighted_alpha2.0.json

# Test alpha=3.0
# Edit 03_compute_metrics.py with first_weight=3.0, last_weight=3.0
python scripts/bibliometrics/03_compute_metrics.py
cp output/author_rankings_weighted.json output/author_rankings_weighted_alpha3.0.json
```

Then compare the three files to determine which alpha best matches your intuition.

## Backward Compatibility

✅ **Original unweighted rankings are unchanged**
- `author_rankings.json` remains the same
- All original analysis files (`paper_rankings.json`, `communities.json`, etc.) unaffected
- You can compare old vs new side-by-side

## Understanding the Output

### author_rankings_weighted.json

Each author entry includes:

```json
{
  "author_id": "https://openalex.org/A123456",
  "name": "Alice Smith",
  "paper_count": 45,
  "first_author_count": 12,
  "last_author_count": 8,
  "middle_author_count": 25,
  "only_author_count": 0,
  "total_pagerank_weighted": 4.523,
  "composite_score_weighted": 0.742,
  "weighted_degree": 89.5,
  "betweenness": 0.034,
  "eigenvector": 0.156,
  "recent_paper_count": 8
}
```

**Interpretation**:
- `composite_score_weighted`: Overall importance (0.0-1.0, higher is better)
- `first_author_count`: Papers where she led/initiated work (12)
- `last_author_count`: Papers where she provided senior direction (8)
- `middle_author_count`: Collaborative roles (25)
- `total_pagerank_weighted`: Citation influence accounting for position

### Comparing Weighted vs Unweighted Rankings

Authors who wrote many *first*-author papers will rank higher in weighted rankings.
Authors who contributed mainly as middle authors will rank lower in weighted rankings.
This helps identify:
- **Research drivers** (high in first-author rankings)
- **Research leaders** (high in last-author rankings)
- **Prolific collaborators** (high in both unweighted rankings)

## Validation & Testing

### Sanity Checks

1. **Known first-author researchers** should rank higher in weighted rankings
2. **Known PI/group leaders** should rank higher in last-author rankings
3. **Prolific middle-author contributors** should rank lower in weighted rankings

### Generate Multiple Alphas

To find the right weight:

```bash
# Generate rankings for alpha = 1.0 (no weighting), 1.5, 2.0, 3.0
for alpha in 1.0 1.5 2.0 3.0; do
  # Edit 03_compute_metrics.py with your alpha value
  # Then run:
  python scripts/bibliometrics/03_compute_metrics.py
  cp output/author_rankings_weighted.json output/author_rankings_weighted_alpha${alpha}.json
done

# Now compare the top 20 authors across all four alphas
```

## Example: Analyzing Career Arcs

The new metadata enables career trajectory analysis:

```python
# Which authors transition from first→last author over their career?
# Those are likely PIs who grew successful research programs

for author in top_authors:
    first_author_papers_by_year = {
        paper['year']: count
        for paper in author_papers
        if paper['position'] == 'first'
    }
    # Plot this over time to see career trajectory
```

## Rollback / Reset

If you want to start over:

```bash
# Delete generated files and re-run
rm output/author_rankings_weighted.json
rm output/first_author_rankings.json
rm output/last_author_rankings.json
rm output/single_author_rankings.json
rm output/first_last_author_distribution.json

# Then re-run the pipeline
python scripts/bibliometrics/02_build_graphs.py
python scripts/bibliometrics/03_compute_metrics.py
python scripts/bibliometrics/03b_first_last_author_analysis.py
```

## Next Steps

1. **Run the pipeline** after your next deduplication pass
2. **Compare rankings**: Check if weighted ranking makes intuitive sense
3. **Adjust alpha**: If needed, modify the weight and re-run (fast operation)
4. **Update visualizations**: Use weighted rankings in web visualizations if desired
5. **Document findings**: Write up key insights about author contributions

## Questions?

See `WEIGHTED_AUTHOR_CONTRIBUTION.md` for the original design document and theoretical background.
