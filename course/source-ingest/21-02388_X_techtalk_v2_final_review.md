---
source_type: pptx
source_file: /Users/wgray13/Downloads/nt_figure_extraction_package (1)/21-02388_X_techtalk_v2_final_review.pptx
ingested_on: 2026-03-10
status: draft-ingested
---

# Source Ingest: 21-02388_X_techtalk_v2_final_review.pptx

## High-level scope
This deck is primarily a NeuroAI/motif-search talk. It is strongest for:
- `09-connectome-analysis-neuroai`

Secondary overlap:
- `01-why-map-the-brain` (motivation: close gap between natural and artificial intelligence)
- `02-brain-data-across-scales` ("What does brain data look like?")
- `atlas-connectomics-reference` (references/tools links can seed the reference unit)

Low direct overlap (likely minimal reuse without rewrite):
- `03-em-prep-and-imaging`
- `04-volume-reconstruction-infrastructure`
- `05-neuronal-ultrastructure`
- `06-axons-and-dendrites`
- `07-glia`
- `08-segmentation-and-proofreading`

## Extracted storyline (first-pass)
1. Audacious goal: derive AI function from biological form.
2. Current ML limitations and motivation for bio-derived approaches.
3. Brain/connectome data and reverse-engineering analogy.
4. NeuroAI pipeline and ring-attractor concept.
5. Motif search framing (subnetwork computational primitives).
6. Query tooling: DotMotif, GrandCypher, GrandIso, Motif Studio.
7. Performance and methodology tradeoffs in motif search.
8. Developmental motif analysis example (C. elegans).
9. References and external resources.

## Slide anchors by theme (approximate)
- Motivation/problem framing: slides 2-10, 20-23
- Brain data + reverse engineering: slides 11-12
- NeuroAI pipeline and ring attractor: slides 13-14
- Motif methods and tools: slides 24-35, 42-45
- Hypothesis/literature/developmental analysis: slides 36-44
- References: slide 46

## Candidate reuse into technical track
- For `09-connectome-analysis-neuroai`:
  - Keep core narrative and tool chain (DotMotif/GrandIso/etc.)
  - Convert to course language with explicit learning objectives and prerequisites
  - Add links to existing modules: `module10`, `module13`, `module14`, `module15`, `module20`

- For `01-why-map-the-brain`:
  - Reuse motivational framing only (slides 8-10, 20-22)
  - Strip tool-specific detail

- For `atlas-connectomics-reference`:
  - Harvest references, project/tool links, and citations from slides 42-46

## Gaps for website+course use
- Needs explicit pedagogical segmentation (concept -> method -> practice -> assessment).
- Needs clear distinction between historical examples (talk date: 2021-07-12) and current state.
- Needs image-level mapping from your extraction manifest for figure attribution and placement.

## Next ingest inputs needed
- Image manifest path (CSV/JSON/MD) for this deck.
- Any speaker notes export if available.
- Priority decision:
  - Option A: rewrite this source into `09-connectome-analysis-neuroai` first
  - Option B: carve out only motivation pieces for `01-why-map-the-brain` first
