# Deck Spec: 08 Segmentation and Proofreading

## Session
- Duration: 80 + 15 min
- Outcome: prioritized triage plan + correction log template
- Primary sources:
  - `course/source-ingest/microns-proofreading-111821-summary.md`
  - `course/source-ingest/module14-lesson2.pptx.md`
- Figure source: `course/units/figures/08-segmentation-and-proofreading-selected-v1.md`

## Slide production blocks
1. Title and QC thesis
- Key message: proofreading is the scientific quality layer for segmentation outputs.
- Figure: `FIG-SRC-MODULE14_LESSON2-S03-01`

2. Error taxonomy
- Key message: merges, splits, boundary ambiguity, identity confusion.
- Figure: `FIG-SRC-MODULE14_LESSON2-S08-01`

3. Ultrastructure cues for correction
- Key message: neuronal context cues improve correction precision.
- Figure: `FIG-RIV-ULTRA-S06-01`

4. Synapse-aware correction decisions
- Key message: synaptic context guards against topology-breaking edits.
- Figure: `FIG-RIV-ULTRA-S09-01`

5. Organelle and boundary ambiguity
- Key message: organelle cues help disambiguate uncertain boundaries.
- Figure: `FIG-RIV-ULTRA-S11-01`

6. Comparative ambiguity panel
- Key message: similar local textures can map to different correction actions.
- Figure: `FIG-RIV-ULTRA-S17-01`

7. Boundary failure case
- Key message: unresolved boundary ambiguity should remain explicitly tagged.
- Figure: `FIG-RIV-ULTRA-S23-01`

8. Identity disambiguation (axon/dendrite)
- Key message: identity checks reduce downstream motif distortion.
- Figure: `FIG-RIV-AXDEN-S13-01`

9. Edge-case process morphology
- Key message: difficult morphology requires adjudication, not solo correction.
- Figure: `FIG-RIV-AXDEN-S18-01`

10. High-complexity correction panel
- Key message: correction priority should track downstream impact.
- Figure: `FIG-RIV-AXDEN-S22-01`

11. Metrics and release gates
- Key message: pair VI, edge P/R, ERL, and synapse-centric F1 with audit logs.
- Figure: `FIG-SRC-MODULE14_LESSON2-S13-01`

12. Activity and bridge
- Key message: write one correction log with metric deltas; bridge to motif analysis.
- Figure: `FIG-SRC-MODULE14_LESSON2-S10-01`

## Assessment
- Prompt: complete one correction log with metric deltas and rationale.
- Rubric: error diagnosis, correction rigor, reproducibility.
