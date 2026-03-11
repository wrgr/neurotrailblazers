---
unit_slug: "04-volume-reconstruction-infrastructure"
unit_title: "Volume Reconstruction Infrastructure"
status: draft_ready
primary_sources:
  - /Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/assets_outreach/metadata/figure_registry.csv
secondary_sources:
  - course/source-ingest/module14-lesson1.pptx.md
  - course/source-ingest/module13-lesson1.pptx.md
mapped_modules:
  - module12
  - module18
selected_figures_file: course/units/figures/04-volume-reconstruction-infrastructure-selected-v1.md
last_updated: 2026-03-10
---

# Unit: Volume Reconstruction Infrastructure

## Learning goals
- Describe the end-to-end infrastructure required to reconstruct large EM volumes.
- Explain key system components: ingest, storage, preprocessing, and service APIs.
- Identify scaling bottlenecks and reliability tradeoffs in reconstruction pipelines.

## Scope boundaries
- In scope:
  - systems architecture for large-scale connectomics reconstruction
  - data movement, preprocessing, and service orchestration
- Out of scope:
  - low-level imaging acquisition details (Unit 03)
  - advanced analysis/NeuroAI interpretation (Unit 09)

## Website draft blocks
### Hero framing
Reconstructing connectomes is a systems problem as much as a neuroscience problem. This unit covers the infrastructure patterns that make petascale-to-exascale reconstruction feasible.

### Core architecture layers
- Ingest and normalization services.
- Multi-resolution storage and access patterns.
- Preprocessing and transformation pipelines.
- API/service layer for downstream tools and users.

### Operational concerns
- Throughput vs accuracy tradeoffs.
- Failure handling and observability.
- Cost/performance constraints at scale.

### Why this matters
Infrastructure choices shape what analyses are feasible, how reproducible results are, and how quickly scientific teams can iterate.

## Slide draft sequence (v1)
1. Why infrastructure is the hidden bottleneck
2. End-to-end reconstruction architecture
3. Ingest and normalization
4. Storage/multiscale representation
5. Preprocessing pipeline stages
6. Service/API layer
7. Throughput, cost, and reliability tradeoffs
8. Case study: scaling lessons learned
9. Integration with segmentation/proofreading and analysis units
10. Summary + architecture checklist

## Figure candidates
See: `course/units/figures/04-volume-reconstruction-infrastructure-selected-v1.md`

## Cross-links
- Related modules: `module12`, `module18`
- Related units: `03-em-prep-and-imaging`, `08-segmentation-and-proofreading`
- Related datasets: `/datasets/workflow/`, `/datasets/mouseconnects/`

## Open issues
- Add a simplified reference architecture diagram for web readability.
- Separate “historical implementation” from “recommended current pattern” language.

## Scope check (expert pass)
- Cover alignment, stitching, normalization, and chunked storage explicitly.
- Include provenance/versioning requirements for derived volumes and annotations.
- Treat workflow orchestration and failure recovery as core, not optional, system concerns.

## Technical anchors to preserve
- Multi-resolution pyramids for interactive and batch workloads.
- Separation of storage, compute, and annotation services.
- Cost-aware architecture choices for petascale workloads.
