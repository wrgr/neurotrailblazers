# Citation Neighborhood vs PRIMARY Corpus

## Overview
- **Citation neighborhood reference papers:** 30
- **Total papers in expansion:** 5802
- **PRIMARY corpus:** 959

## Key Finding
Only 12 of 30 reference papers are in our 7,925-paper citation graph.

This creates a fundamental constraint:
- We can compute k-core only on papers in the existing graph
- Most of the 5,802-paper expansion is outside the graph
- Full analysis requires rebuilding the citation graph

## Papers in Graph vs Not in Graph
- In graph: 12 (40%)
- NOT in graph: 18 (60%)

## Recommendation
The citation neighborhood expansion strategy is sound, but:

1. **For focused analysis**: Use the 12 papers already in citation graph
   - Can apply k-core filtering immediately
   - Compare to PRIMARY (959)
   - See overlap and gaps

2. **For comprehensive analysis**: Rebuild citation graph from 5,802 papers
   - Takes longer but captures full expansion
   - Can then apply k-core filtering properly
   - More accurate k-core values

Which approach serves your needs better?
