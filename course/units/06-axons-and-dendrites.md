---
unit_slug: "06-axons-and-dendrites"
unit_title: "Axons and Dendrites"
status: draft_ready
primary_sources:
  - /Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/frompat/metadata/figure_registry.csv
secondary_sources:
  - course/source-ingest/microns-proofreading-dendrites-axons-111821.pptx.md
mapped_modules:
  - module04
  - module09
selected_figures_file: course/units/figures/06-axons-and-dendrites-selected-v1.md
last_updated: 2026-03-10
---

# Unit: Axons and Dendrites

## Learning goals
- Distinguish axonal and dendritic structures in EM imagery.
- Use organelle and morphology cues for robust process classification.
- Handle ambiguous cases in proofreading with context-aware decisions.

## Scope boundaries
- In scope:
  - morphology-first discrimination of axons vs dendrites
  - proofreading cues and common misclassification traps
- Out of scope:
  - full synapse-typing deep dive (handled in ultrastructure/synapse units)

## Website draft blocks
### Hero framing
Accurate axon/dendrite identification is one of the most important practical skills in connectomics. This unit focuses on visual cues that support reliable classification during proofreading.

### Core cues
- Process caliber and branching patterns.
- Spine-associated vs bouton-associated context.
- Organelle signatures and continuity behavior across slices.

### Practical workflow
1. Start with local morphology.
2. Check organelle/context clues.
3. Track continuity in neighboring sections.
4. Assign provisional class and confidence.
5. Resolve edge cases with broader neighborhood context.

### Common pitfalls
- Overreliance on single-slice appearance.
- Misclassification in dense neuropil crossings.
- Ignoring nearby synaptic context and process continuity.

## Slide draft sequence (v1)
1. Why axon/dendrite discrimination matters
2. Morphology cues overview
3. Organelle cues overview
4. Dendrite-focused examples
5. Axon-focused examples
6. Ambiguous examples and error taxonomy
7. Practical proofreading checklist
8. Summary + quick-reference cue table

## Figure candidates
See: `course/units/figures/06-axons-and-dendrites-selected-v1.md`

## Cross-links
- Related modules: `module04`, `module09`
- Related unit: `05-neuronal-ultrastructure`
- Related tool: `/tools/connectome-quality/`

## Open issues
- Add a learner-facing decision tree graphic for classification.
- Validate terminology consistency with Unit 05 glossary.

## Scope check (expert pass)
- Emphasize probabilistic classification in ambiguous neuropil regions.
- Add explicit edge cases: en passant boutons, thin dendrites, branch points, truncated processes.
- Require multi-slice continuity checks before final class assignment.

## Technical anchors to preserve
- Morphology + organelle + local connectivity cues should be combined.
- Confidence scoring improves auditability and inter-rater consistency.
- Misclassification at this stage propagates to network-level interpretation errors.
