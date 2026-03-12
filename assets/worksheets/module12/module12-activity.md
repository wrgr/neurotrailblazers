# Module 12 Activity Worksheet

## Module
Module 12: Big Data in Connectomics

## Capability Target
Produce a scalable, reproducible query-and-analysis plan for a large connectomics dataset, including storage assumptions, indexing strategy, and provenance capture.

## Studio Activity Instructions


## Evidence and Reasoning Notes
- Claim:
- Evidence:
- Limitation:

## Rubric Check
- **Minimum pass**
  - Query design matches analysis goal and data shape.
  - Provenance requirements are explicit and actionable.
  - Bottlenecks are identified with one realistic mitigation.
- **Strong performance**
  - Separates exploratory and production query paths.
  - Quantifies tradeoffs (latency, cost, reproducibility).
  - Anticipates failure recovery and rollback needs.
- **Common failure modes**
  - Index choices disconnected from query workload.
  - Missing version metadata in outputs.
  - Optimization attempts without benchmark baseline.

## Exit Prompt
Document one query you use with:
1. data source/version,
2. expected runtime class,
3. one provenance field you currently miss.
