---
unit_slug: "03-em-prep-and-imaging"
unit_title: "EM Prep and Imaging"
status: draft_ready
primary_sources:
  - /Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/assets_outreach/metadata/figure_registry.csv
secondary_sources:
  - course/source-ingest/module12-lesson3.pptx.md
  - course/source-ingest/module13-lesson2.pptx.md
mapped_modules:
  - module05
selected_figures_file: course/units/figures/03-em-prep-and-imaging-selected-v1.md
last_updated: 2026-03-10
---

# Unit: EM Prep and Imaging

## Learning goals
- Describe why EM imaging is central to connectomics.
- Explain core imaging-prep pipeline stages at a practical level.
- Interpret how voxel/resolution decisions shape downstream reconstruction.

## Scope boundaries
- In scope:
  - imaging and preparation concepts needed by technical learners
  - practical interpretation of scale, resolution, and sectioning
- Out of scope:
  - exhaustive instrument engineering details
  - downstream segmentation/proofreading deep dive (Unit 08)

## Website draft blocks
### Hero framing
Connectomics begins with imaging choices. Resolution, sectioning strategy, and data quality constraints set the ceiling for what can be reconstructed and analyzed later.

### Core concepts
- Why EM is used for circuit-scale structural mapping.
- Sectioning, imaging, and volume assembly at high level.
- Resolution/voxel tradeoffs and their scientific consequences.

### Practical implications
- Imaging artifacts propagate into segmentation and analysis.
- Quality decisions early in the pipeline reduce correction burden later.
- Scale planning must align with target biological questions.

## Slide draft sequence (v1)
1. Why EM for connectomics
2. Historical context and current role
3. Sectioning and imaging workflow overview
4. Resolution and voxel-size tradeoffs
5. Data volume and storage implications
6. Common imaging artifacts and mitigation
7. Bridge to reconstruction/segmentation units
8. Summary + practical checklist

## Figure candidates
See: `course/units/figures/03-em-prep-and-imaging-selected-v1.md`

## Cross-links
- Related module: `module05`
- Related units: `02-brain-data-across-scales`, `04-volume-reconstruction-infrastructure`, `08-segmentation-and-proofreading`
- Related datasets: `/datasets/workflow/`, `/datasets/mouseconnects/`

## Open issues
- Add one concise prep/imaging glossary block for novice learners.
- Verify any quantitative imaging benchmarks before publication copy.

## Scope check (expert pass)
- Include prep chain: fixation, staining, embedding, sectioning, imaging.
- Clarify common EM acquisition families (serial section EM, SBF-SEM, FIB-SEM) at conceptual level.
- Name artifact classes that affect downstream segmentation: charging, knife chatter, folds/tears, misalignment.

## Technical anchors to preserve
- Resolution-volume-throughput tradeoff is fundamental.
- QA at acquisition stage is cheaper than correction downstream.
- Imaging metadata/provenance is required for reproducible reconstruction.
