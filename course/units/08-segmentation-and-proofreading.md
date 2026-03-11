---
unit_slug: "08-segmentation-and-proofreading"
unit_title: "Segmentation and Proofreading"
status: draft_ready
primary_sources:
  - /Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/frompat/metadata/figure_registry.csv
  - /Users/wgray13/Downloads/nt_figure_extraction_package (1)/connectomics_figures/assets_outreach/metadata/figure_registry.csv
secondary_sources:
  - course/source-ingest/microns-proofreading-111821-summary.md
  - course/source-ingest/module14-lesson2.pptx.md
mapped_modules:
  - module06
  - module07
selected_figures_file: course/units/figures/08-segmentation-and-proofreading-selected-v1.md
last_updated: 2026-03-10
---

# Unit: Segmentation and Proofreading

## Learning goals
- Explain why segmentation quality is a limiting factor in connectomics.
- Identify common segmentation/proofreading error classes in EM volumes.
- Apply a practical proofreading workflow for correction and verification.
- Connect proofreading outcomes to downstream graph and analysis reliability.

## Scope boundaries
- In scope:
  - segmentation outputs and human QC workflows
  - merge/split/boundary ambiguity error taxonomy
  - practical morphology cues from mature proofreading material
- Out of scope:
  - full wet-lab EM acquisition pipeline
  - advanced NeuroAI motif-analysis theory (Unit 09)

## Source synthesis
- Core claims to preserve:
  - proofreading is essential because segmentation errors propagate to scientific inference
  - morphology-informed classification (axon/dendrite/ultrastructure/glia cues) improves QC accuracy
  - quality metrics should be attached to correction workflows, not added as afterthoughts
- Historical context to reframe:
  - older outreach pipeline visuals are context-only, not current-state authority
- Needs verification:
  - any performance or benchmark claims from outreach-derived slides

## Website draft blocks
### Hero framing
Segmentation makes connectome-scale analysis possible, but proofreading makes it reliable. This unit teaches how to recognize reconstruction errors, correct them systematically, and document quality in ways that protect downstream scientific conclusions.

### Error taxonomy
- Merge errors: two processes incorrectly fused.
- Split errors: one process incorrectly fragmented.
- Boundary ambiguity: uncertain edges in dense neuropil.
- Identity confusion: neuronal/glial or axon/dendrite misclassification.

### Practical proofreading workflow
1. Inspect local morphology and continuity in 2D/3D context.
2. Classify suspected error type.
3. Correct labels/links using tooling workflow.
4. Verify correction across neighboring slices and context views.
5. Record QC notes and confidence for auditability.

### Morphology cues used in QC
- Dendritic spine and shaft cues.
- Axonal bouton and process continuity cues.
- Synaptic vesicle/ultrastructure cues.
- Glia-neuron boundary cues in ambiguous regions.

### QC and downstream impact
- Error type distributions are quality signals.
- Corrections affect graph topology and inferred motifs.
- Reliable proofreading supports valid connectome analysis and NeuroAI conclusions.

## Slide draft sequence (v1)
1. Why proofreading matters for connectomics validity
2. Segmentation output and failure modes
3. Error taxonomy: merges, splits, boundary ambiguity
4. Axon/dendrite confusion cases
5. Ultrastructure cues for correction decisions
6. Glia-vs-neuron boundary pitfalls
7. Step-by-step proofreading workflow
8. Tool-assisted correction and logging
9. QC metrics and acceptance thresholds
10. Case study: before/after corrections
11. How QC affects downstream graph analysis
12. Summary + practical checklist

## Figure candidates
See: `course/units/figures/08-segmentation-and-proofreading-selected-v1.md`

## Cross-links
- Related modules: `module06`, `module07`
- Related datasets: `/datasets/mouseconnects/`, `/datasets/workflow/`
- Related tools: `/tools/connectome-quality/`, `/tools/ask-an-expert/`

## Open issues
- Add one notebook/lab exercise path for hands-on proofreading.
- Define rubric thresholds for student-level proofreading assignments.
- Validate any outreach-derived metric claims before publish.

## Scope check (expert pass)
- Add metrics vocabulary beyond generic QC: variation of information (VI), edge-level precision/recall, expected run length (ERL), synapse-centric F1.
- Require explicit pre/post correction logging for reproducibility.
- Include error-priority policy: high-impact topology/synapse errors first.

## Technical anchors to preserve
- Proofreading is a scientific quality-control process, not only visual cleanup.
- Metrics and correction workflow must be linked.
- Human-machine workflows should separate discovery, adjudication, and finalization steps.
