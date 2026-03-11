# Technical Track Deck Authoring Pack

These files are production-oriented slide authoring specs for the canonical Technical Training: Nanoscale Connectomics track.

Each unit file includes:
- session targets and timing
- slide-by-slide content blocks
- figure hooks (mapped to `course/units/figures/*`)
- speaker-note prompts and assessment cues

Suggested workflow:
1. Build slides from each `course/decks/*.md` file.
2. Pull visuals from the mapped figure shortlist.
3. Keep claims with dates/benchmarks labeled as historical unless revalidated.
4. Export to PPTX/Google Slides and link final artifacts in unit frontmatter (`slides:`).

Unit files:
- `01-why-map-the-brain.md`
- `02-brain-data-across-scales.md`
- `03-em-prep-and-imaging.md`
- `04-volume-reconstruction-infrastructure.md`
- `05-neuronal-ultrastructure.md`
- `06-axons-and-dendrites.md`
- `07-glia.md`
- `08-segmentation-and-proofreading.md`
- `09-connectome-analysis-neuroai.md`
- `atlas-connectomics-reference.md`
