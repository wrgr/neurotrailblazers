# Marp Slide Drafts (Technical Track)

These markdown files are draft slide sources that can be rendered with Marp or imported into other slide workflows.

Current draft units:
- `01-why-map-the-brain.marp.md`
- `02-brain-data-across-scales.marp.md`
- `03-em-prep-and-imaging.marp.md`
- `04-volume-reconstruction-infrastructure.marp.md`
- `05-neuronal-ultrastructure.marp.md`
- `06-axons-and-dendrites.marp.md`
- `07-glia.marp.md`
- `08-segmentation-and-proofreading.marp.md`
- `09-connectome-analysis-neuroai.marp.md`
- `atlas-connectomics-reference.marp.md`

Usage:
1. Install Marp CLI if needed.
2. Render with `./scripts/render_marp.sh`, which registers the custom themes and repairs image paths for the output directory.
3. Use `./scripts/render_marp.sh --pptx` for PowerPoint exports.
4. Run `ruby scripts/check_deck_freshness.rb` after editing sources or theme CSS.

The shared `neurotrailblazers` theme uses the nanoscale design approved in September
2026: charcoal covers with real H01 tissue, warm paper for teaching content, and
embedded Source Sans 3. Copy the cover markup from
`neurotrailblazers-template.marp.md`; retain the image's scale bar and citation.
Image paths are relative to the source file, so decks under `modules/` need one
more `../` than decks in this directory. Generate module sources with
`ruby scripts/generate_module_teaching_materials.rb` before rendering.

Notes:
- Figure paths currently use repo-local assets.
- Historical benchmark/performance claims are labeled where relevant.
