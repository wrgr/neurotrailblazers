---
asset_root: "/Users/wgray13/Downloads/nt_figure_extraction_package (1)"
indexed_on: 2026-03-10
status: active
---

# Asset Manifest Index

Canonical asset/manifest root for this project:
- `/Users/wgray13/Downloads/nt_figure_extraction_package (1)`

## Manifest sets

### neuroAI
- Summary: `/Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/neuroAI/metadata/summary.json`
- Source inventory: `/Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/neuroAI/metadata/source_inventory.csv`
- Figure registry: `/Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/neuroAI/metadata/figure_registry.csv`
- Counts: 1 source, 87 figures
- Main source id: `SRC-21_02388_X_TECHTALK_`
- Track relevance: `09-connectome-analysis-neuroai` (primary)

### frompat
- Summary: `/Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/frompat/metadata/summary.json`
- Source inventory: `/Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/frompat/metadata/source_inventory.csv`
- Figure registry: `/Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/frompat/metadata/figure_registry.csv`
- Counts: 4 sources, 51 figures
- Main source ids:
  - `RIV-AXDEN` -> axons/dendrites
  - `RIV-ULTRA` -> neuronal ultrastructure
  - `RIV-GLIA` -> glia
- Track relevance: `05`, `06`, `07`, `08`

### assets_outreach
- Summary: `/Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/assets_outreach/metadata/summary.json`
- Source inventory: `/Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/assets_outreach/metadata/source_inventory.csv`
- Figure registry: `/Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/assets_outreach/metadata/figure_registry.csv`
- Counts: 10 sources, 296 figures
- Main source ids:
  - `SRC-MODULE12_LESSON1/2/3`
  - `SRC-MODULE13_LESSON1/2/3`
  - `SRC-MODULE14_LESSON1/2/3`
- Track relevance: `02`, `03`, `04`, `05`, `06`, `08`, `09`

## Figure-selection workflow (for each unit pass)
1. Pick source ids for the target unit.
2. Filter `figure_registry.csv` by `source_id` and `source_slide_or_page`.
3. Use `thumbnail_path` + `contact_sheet_path` for visual review.
4. Copy selected assets into canonical site paths under `assets/images/technical-track/<unit>/`.
5. Record attribution/citation on-page and in unit source doc.

## Priority source-id queue
1. `SRC-MODULE13_LESSON3` (09-connectome-analysis-neuroai)
2. `SRC-MODULE14_LESSON2` (08-segmentation-and-proofreading)
3. `RIV-GLIA` (07-glia)
4. `RIV-AXDEN` (06-axons-and-dendrites)
5. `RIV-ULTRA` (05-neuronal-ultrastructure)
