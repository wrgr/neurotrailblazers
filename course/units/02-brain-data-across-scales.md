---
unit_slug: "02-brain-data-across-scales"
unit_title: "Brain Data Across Scales"
status: draft_ready
primary_sources:
  - /Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/assets_outreach/metadata/figure_registry.csv
secondary_sources:
  - course/source-ingest/module12-lesson1.pptx.md
  - course/source-ingest/module12-lesson2.pptx.md
  - course/source-ingest/module12-lesson3.pptx.md
mapped_modules:
  - module04
  - module05
  - module12
selected_figures_file: course/units/figures/02-brain-data-across-scales-selected-v1.md
last_updated: 2026-03-10
---

# Unit: Brain Data Across Scales

## Learning goals
- Explain what changes (and what does not) across macro-to-micro brain data scales.
- Relate scale decisions to storage, processing, and interpretation constraints.
- Connect scale-aware thinking to later reconstruction and analysis workflows.

## Website draft blocks
### Hero framing
Brain data exists across many scales, from coarse anatomical maps to ultrastructural EM volumes. This unit builds the mental model needed to navigate scale, resolution, and data complexity in connectomics.

### Core concepts
- Scale tiers and their typical data representations.
- Resolution and voxel-size implications.
- Why “more detail” changes compute and interpretation costs.

### Practical bridge
- How scale impacts pipeline design.
- How scale choices constrain downstream methods.
- How to choose the right scale for a research question.

## Slide draft sequence (v1)
1. Why scale matters in connectomics
2. Macro-to-micro data overview
3. Resolution and voxel tradeoffs
4. Scale-specific data types and formats
5. Processing implications at each scale
6. Case examples from outreach sources
7. Bridge to imaging/reconstruction units
8. Summary + scale-selection checklist

## Figure candidates
See: `course/units/figures/02-brain-data-across-scales-selected-v1.md`

## Open issues
- Add one compact comparison table (scale vs data size vs use case).

## Scope check (expert pass)
- Explicitly separate modality scale (e.g., MRI/light/EM) from analysis scale (network/microcircuit/synapse).
- Add coordinate-system and registration concerns as first-class issues.
- Include anisotropy/resolution mismatch as core interpretation risk.

## Technical anchors to preserve
- Scale-aware question design (choose data scale to fit biological hypothesis).
- Data representation shift across scales (volumes, meshes, skeletons, graphs).
- Cross-scale interoperability and provenance tracking.
