---
unit_slug: "07-glia"
unit_title: "Glia"
status: draft_ready
primary_sources:
  - /Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/frompat/metadata/figure_registry.csv
secondary_sources:
  - course/source-ingest/microns-proofreading-glia-111821.pptx.md
mapped_modules:
  - module04
selected_figures_file: course/units/figures/07-glia-selected-v1.md
last_updated: 2026-03-10
---

# Unit: Glia

## Learning goals
- Distinguish major glial cell classes in connectomics imagery.
- Recognize practical EM cues for astrocytes, microglia, and oligodendrocytes.
- Avoid common glia-vs-neuron proofreading errors.
- Explain why glia interpretation matters for circuit-level conclusions.

## Scope boundaries
- In scope:
  - glia morphology for connectomics and proofreading workflows
  - practical recognition cues and ambiguity handling
- Out of scope:
  - deep molecular glia biology not needed for EM QC decisions

## Source synthesis
- Core claims to preserve:
  - glia are structurally and functionally central in connectomic reconstructions
  - glial morphology can be recognized with repeatable visual cues
  - glia-neuron boundary quality directly affects annotation reliability
- Historical context to reframe:
  - training-deck language should be adapted for course tone and current framing
- Needs verification:
  - any non-attributed claims beyond the deck’s cited resources

## Website draft blocks
### Hero framing
Glia are not background cells. In connectomics, accurate glial identification is essential for trustworthy circuit reconstruction and interpretation.

### Core cell classes
- Astrocytes: branching support cells with characteristic process context near synapses.
- Microglia: immune-surveillance morphology with distinct local context cues.
- Oligodendrocytes: myelination-related morphology and process patterns.

### Recognition cues for proofreading
- Cytoplasmic texture and process morphology.
- Local neighborhood context (synapses, vessels, myelinated regions).
- Boundary behavior across adjacent slices.

### Common pitfalls
- Mislabeling glial processes as neuronal branches.
- Over-segmentation in dense glial-neuronal interface regions.
- Missing context when classifying from single-slice views.

### Why this matters
Correct glia annotation improves segmentation quality, reduces downstream graph artifacts, and supports biologically grounded interpretation of connectomic data.

## Slide draft sequence (v1)
1. Why glia matter in connectomics
2. Astrocyte recognition cues
3. Microglia recognition cues
4. Oligodendrocyte/myelin recognition cues
5. Glia-neuron boundary ambiguity examples
6. Proofreading checklist for glia annotations
7. Case examples and correction patterns
8. Summary + quick-reference cue table

## Figure candidates
See: `course/units/figures/07-glia-selected-v1.md`

## Cross-links
- Related modules: `module04`
- Related datasets: `/datasets/mouseconnects/`, `/datasets/workflow/`
- Related tool: `/tools/connectome-quality/`

## Open issues
- Add compact glossary of glia-specific morphology terms.
- Confirm attribution/citation blocks for all selected figures.

## Scope check (expert pass)
- Include glia-specific pitfalls: astrocytic fine processes vs dendritic branches; microglia process complexity vs neurites.
- Include myelin context cues for oligodendrocyte-related interpretation.
- Keep glia examples tied to proofreading decisions, not only descriptive biology.

## Technical anchors to preserve
- Glia annotation quality affects neuronal boundary confidence and topology.
- Cell-type context improves error triage during proofreading.
- Consistent glia cues should be taught as a reusable checklist.
