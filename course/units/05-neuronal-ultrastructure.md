---
unit_slug: "05-neuronal-ultrastructure"
unit_title: "Neuronal Ultrastructure"
status: review_needed
capability_status: activity_drafted
primary_sources:
  - /Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/frompat/metadata/figure_registry.csv
secondary_sources:
  - course/source-ingest/microns-proofreading-neuronal-ultrastructure-111821.pptx.md
mapped_modules:
  - module04
  - module09
  - module11
selected_figures_file: course/units/figures/05-neuronal-ultrastructure-selected-v1.md
last_updated: 2026-03-11
---

# Unit: Neuronal Ultrastructure

## Learning goals
- Identify key ultrastructural components in neuronal EM data.
- Relate ultrastructure cues to synaptic interpretation and proofreading choices.
- Build a shared morphology vocabulary for downstream units.

## Scope boundaries
- In scope:
  - neuron ultrastructure features relevant to connectomics
  - practical interpretation for annotation/proofreading
- Out of scope:
  - full molecular/cellular neurobiology beyond EM-visible features

## Website draft blocks
### Hero framing
Neuronal ultrastructure is the visual language of connectomics. This unit establishes the structural cues needed to interpret EM volumes confidently and consistently.

### Core features
- Soma and process ultrastructure.
- Synaptic structures and vesicle context.
- Organelles and local subcellular signatures.

### Practical interpretation workflow
1. Identify structural landmarks in context.
2. Distinguish neuronal compartments.
3. Evaluate synaptic and vesicle cues.
4. Record uncertainty and verify with neighboring views.

### Why this matters
Ultrastructure interpretation underpins accurate segmentation, robust proofreading, and trustworthy downstream graph analysis.

## Slide draft sequence (v1)
1. Why ultrastructure matters for connectomics
2. Neuron structure overview
3. Dendritic ultrastructure cues
4. Axonal ultrastructure cues
5. Synapse and vesicle interpretation
6. Ambiguity and proofreading decisions
7. Case examples and cue integration
8. Summary + morphology reference sheet

## Figure candidates
See: `course/units/figures/05-neuronal-ultrastructure-selected-v1.md`

## Cross-links
- Related modules: `module04`, `module09`, `module11`
- Related units: `06-axons-and-dendrites`, `08-segmentation-and-proofreading`
- Related tool: `/tools/connectome-quality/`

## Open issues
- Add concise glossary that can be shared with Units 06/07/08.
- Add one short self-check quiz block for morphology recognition.

## Capability deepening pass (2026-03-11)
- Added explicit concept payload blocks (definition, plain-language translation, misconception guardrails).
- Added full studio activity structure with outputs tied to consensus quality.
- Added assessment rubric tiers (minimum pass, strong performance, failure modes).

## Scope check (expert pass)
- Include clear compartment boundaries: soma, dendrite, axon, bouton, spine, synapse.
- Include core ultrastructural cues: vesicle pools, PSD/active zones, mitochondria, ER, microtubules.
- Distinguish recognition heuristics from hard labels; confidence should be explicit in ambiguous regions.

## Technical anchors to preserve
- Ultrastructure interpretation is context-dependent (single slice is often insufficient).
- Synaptic interpretation must be tied to local morphology and neighborhood context.
- Consistent vocabulary reduces annotation drift across annotators.
