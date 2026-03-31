# Weighted Author Contribution System

## Goal
Implement a weighting system where first/cofirst and last/colast authors receive higher contribution credit (e.g., 2x multiplier) compared to middle authors.

## Current State
- **File**: `scripts/bibliometrics/03_compute_metrics.py`
- **Author ranking**: Simple aggregation of PageRank contributions from all papers
- **Limitation**: Treats all author positions equally

## Implementation Plan

### Phase 1: Data Enrichment (02_build_graphs.py)
When building the co-authorship network, capture author position metadata:

```python
def build_coauthorship_graph_with_positions(corpus):
    """
    Build co-authorship graph with position-weighted edges.

    Author positions:
    - First author (position 0): 2.0x weight
    - CoFirst authors (if indicated): 2.0x weight
    - Last author: 2.0x weight
    - CoLast authors (if indicated): 2.0x weight
    - Middle authors: 1.0x weight

    Edge weights now reflect: base_collaborations * author_weight_product
    """
```

**Key change**: Store author position information in paper records:
```json
{
  "openalex_id": "...",
  "authors": [
    {"name": "Alice", "openalex_id": "A1", "position": "first", "weight": 2.0},
    {"name": "Bob", "openalex_id": "B1", "position": "middle", "weight": 1.0},
    {"name": "Carol", "openalex_id": "C1", "position": "last", "weight": 2.0}
  ]
}
```

### Phase 2: Metric Computation (03_compute_metrics.py)

#### 2a. Citation Contribution Weighting
When computing per-author contribution to PageRank:

```python
def compute_author_metrics_weighted(citation_graph, corpus):
    """
    For each paper, distribute citation weight to authors based on position.

    Current (equal): each author gets 1/num_authors of the paper's PageRank
    Weighted: author gets (position_weight / sum_of_weights) of the paper's PageRank

    Example:
    - Paper with 4 authors: first (2x), middle (1x), middle (1x), last (2x)
    - Sum = 6x, total PageRank = 1.0
    - First author: 1.0 * (2/6) = 0.333
    - Middle authors: 1.0 * (1/6) = 0.167 each
    - Last author: 1.0 * (2/6) = 0.333
    """
```

#### 2b. Co-authorship Strength
Adjust collaboration edges to reflect author importance:

```python
def compute_weighted_collaboration_strength(author1, author2, shared_papers):
    """
    Weight each shared paper by the product of author positions.

    If author1 is first (2x) and author2 is last (2x) on paper:
    - That paper counts as 2*2 = 4x collaboration strength
    - vs middle+middle collaboration = 1*1 = 1x
    """
```

### Phase 3: Ranking Updates (03_compute_metrics.py)

```python
def rank_authors_weighted(author_metrics, alpha=2.0):
    """
    Composite author ranking with weighted contributions.

    Factors:
    - total_weighted_pagerank: Papers weighted by author position
    - collaboration_network: Weighted by co-author positions
    - h-index variants: High-impact papers where author is first/last
    - recent_weighted_contribution: Recent papers with position weight
    """
```

### Phase 4: Visualization Updates
- Generate separate ranking tables: "Top Authors (Position-Weighted)"
- Add visualization: "First/Last Author Distribution"
- New analysis: "Career Archetypes" (first authors → last authors trajectory)

## Output Structure

### 1. Parallel Ranking Files
```
author_rankings.json (current - all positions equal)
author_rankings_weighted.json (NEW - position-weighted, alpha=2.0)
```

### 2. Analysis Files
```
first_last_author_distribution.json
- Papers by first author only
- Papers by last author only
- Papers by both first AND last author (full contributor)
- Analysis of career trajectories
```

### 3. Enhanced Visualizations
- `kcore-rankings_weighted.html` - K-core with weighted author importance
- `first_last_authors.html` - Distribution analysis
- Updated coauthor network showing weighted collaboration strength

## Implementation Effort
- **Phase 1 (data enrichment)**: 1-2 hours
- **Phase 2 (metrics)**: 2-3 hours
- **Phase 3 (ranking)**: 1 hour
- **Phase 4 (visualizations)**: 2-3 hours
- **Total**: ~6-9 hours including testing

## Testing & Experimentation Strategy

### Safe, Reversible Testing
Since all weights are configurable, you can safely experiment:

1. **Generate multiple ranking sets with different weights**:
   - Weight 1.0 (baseline, current system)
   - Weight 1.5 (conservative)
   - Weight 2.0 (balanced)
   - Weight 3.0 (aggressive)

2. **Compare results**:
   - Which authors move up/down with each weight?
   - Does 1.5x align better with your intuition than 2.0x?
   - Are there any unexpected effects?

3. **Validate**:
   - Known prolific first/last authors should rank higher
   - Compare against existing manual rankings
   - Check for degenerate cases (single-author papers, etc.)

4. **Choose weight** once you've verified the output makes sense
   - No lock-in: can always re-run with different weights
   - All intermediate results preserved for comparison

### Validation Checklist
- [ ] Authors with many first-authored papers rank higher than expected
- [ ] Authors with many last-authored papers rank higher than expected
- [ ] Serial middle-author contributors rank lower (expected behavior)
- [ ] No edge cases (papers with 1 author, missing author data, etc.)

## Migration Notes
- **Backwards compatible**: Original rankings remain unchanged
- **Optional feature**: Weighted rankings run in parallel
- **User choice**: Web UI can toggle between weighted/unweighted views

## Configuration (Fully Reversible)

The system uses configurable alpha coefficients - **you can adjust or disable weighting at any time**:

```python
# Alpha coefficient for author position weighting (configurable)
FIRST_AUTHOR_WEIGHT = 2.0      # Set to 1.0 to disable first-author emphasis
LAST_AUTHOR_WEIGHT = 2.0       # Set to 1.0 to disable last-author emphasis
COFIRST_WEIGHT = 2.0            # If detected in author metadata
COLAST_WEIGHT = 2.0             # If detected in author metadata
MIDDLE_AUTHOR_WEIGHT = 1.0      # Always 1.0 (baseline)
```

### Easy Rollback / Testing
You can generate rankings with different weight configurations:

```bash
# No weighting (original behavior)
python 03_compute_metrics.py --first-weight 1.0 --last-weight 1.0

# Conservative weighting (1.5x)
python 03_compute_metrics.py --first-weight 1.5 --last-weight 1.5

# Aggressive weighting (3x)
python 03_compute_metrics.py --first-weight 3.0 --last-weight 3.0

# Asymmetric (first emphasized more than last)
python 03_compute_metrics.py --first-weight 3.0 --last-weight 1.5
```

All outputs go to `author_rankings_weighted_[config].json`, so you can compare side-by-side.

## Related Questions
1. Should we use different alphas for different fields? (e.g., 3x for experimental papers?)
2. Should we weight by number of co-authors? (more co-authors = less weight per author?)
3. Should we generate "first author only" vs "last author only" separate analyses?
