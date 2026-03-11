# Deck Spec: 04 Volume Reconstruction Infrastructure

## Session
- Duration: 80 + 10 min
- Outcome: architecture and rollback plan
- Primary sources:
  - `course/source-ingest/module14-lesson1.pptx.md`
  - `course/source-ingest/module13-lesson1.pptx.md`
  - `course/source-ingest/module14-lesson2.pptx.md` (secondary)
- Figure source: `course/units/figures/04-volume-reconstruction-infrastructure-selected-v1.md`

## Slide production blocks
1. Title and systems framing
- Key message: connectome reconstruction is a full-stack engineering problem.
- Figure: `FIG-SRC-MODULE14_LESSON1-S02-01`

2. High-level architecture
- Key message: ingest, transform, inference, and serving layers must be explicit.
- Figure: `FIG-SRC-MODULE14_LESSON1-S04-01`

3. Ingest service and data contracts
- Key message: validation and checksums are mandatory entry gates.
- Figure: `FIG-SRC-MODULE14_LESSON1-S05-01`

4. Workflow/API integration
- Key message: orchestration and APIs determine operational throughput.
- Figure: `FIG-SRC-MODULE14_LESSON1-S07-01`

5. Processing and downsampling stages
- Key message: multiresolution storage should serve both proofreading and analysis.
- Figure: `FIG-SRC-MODULE14_LESSON1-S09-01`

6. Service decomposition
- Key message: modular services improve recoverability and independent scaling.
- Figure: `FIG-SRC-MODULE14_LESSON1-S12-01`

7. Pipeline deep-dive element
- Key message: stage-level lineage metadata is required for reproducibility.
- Figure: `FIG-SRC-MODULE14_LESSON1-S14-01`

8. System summary
- Key message: architecture should be reviewed against quality/cost SLOs.
- Figure: `FIG-SRC-MODULE14_LESSON1-S19-01`

9. Storage and analytics context
- Key message: analytics workloads feed back into pipeline design decisions.
- Figure: `FIG-SRC-MODULE13_LESSON1-S08-01`

10. Operations risk and rollback
- Key message: every release needs rollback criteria and region-scoped reprocessing.
- Figure: `FIG-SRC-MODULE13_LESSON1-S12-01`

11. Activity instructions
- Key message: draft one architecture with required lineage fields and rollback path.

12. Debrief and bridge to Unit 05
- Key message: infrastructure reliability is a prerequisite for biological interpretation.

## Assessment
- Prompt: produce a staged pipeline with three mandatory lineage fields per stage.
- Rubric: traceability, resilience, and operational realism.
