# Deck Spec: 02 Brain Data Across Scales

## Session
- Duration: 75 + 15 min
- Outcome: scale-selection worksheet
- Primary sources:
  - `course/source-ingest/module12-lesson1.pptx.md`
  - `course/source-ingest/module12-lesson2.pptx.md`
  - `course/source-ingest/module12-lesson3.pptx.md`
- Figure source: `course/units/figures/02-brain-data-across-scales-selected-v1.md`

## Slide production blocks
1. Title and technical objective
- Key message: scale choice determines what biological claims are valid.
- Figure: `FIG-SRC-MODULE12_LESSON1-S02-01`

2. Data-across-scales overview
- Key message: modalities differ in resolvable structures and uncertainty.
- Figure: `FIG-SRC-MODULE12_LESSON1-S06-01`

3. Macro-to-micro pipeline bridge
- Key message: acquisition scale and analysis scale are not interchangeable.
- Figure: `FIG-SRC-MODULE12_LESSON2-S04-01`

4. Representation transitions
- Key message: volume -> segmentation -> skeleton/mesh -> graph carries information loss.
- Figure: `FIG-SRC-MODULE12_LESSON2-S05-01`

5. Engineering constraints at scale
- Key message: storage, compute, and I/O become scientific constraints.
- Figure: `FIG-SRC-MODULE12_LESSON2-S06-01`

6. Historical context and modern use
- Key message: historical imaging context informs current design choices.
- Figure: `FIG-SRC-MODULE12_LESSON3-S03-01`

7. Why connectomics needs cross-scale rigor
- Key message: incomplete scale reasoning causes invalid inference.
- Figure: `FIG-SRC-MODULE12_LESSON3-S06-01`

8. Throughput and sectioning context
- Key message: data-generation strategy constrains downstream representations.
- Figure: `FIG-SRC-MODULE12_LESSON3-S08-01`

9. Pipeline transition points
- Key message: each handoff should preserve provenance and uncertainty metadata.
- Figure: `FIG-SRC-MODULE12_LESSON3-S10-01`

10. Failure modes
- Key message: scale leakage, over-registration confidence, representation collapse.

11. Activity instructions
- Key message: choose a question and justify minimal sufficient scale.

12. Debrief and bridge to Unit 03
- Key message: acquisition quality determines what survives cross-scale analysis.

## Assessment
- Prompt: choose one question and justify scale + transform + representation choices.
- Rubric: feature resolvability, transform traceability, resource realism.
