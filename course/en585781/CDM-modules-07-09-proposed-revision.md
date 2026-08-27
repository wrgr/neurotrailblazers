# Proposed CDM revision — Modules 7–9 (Connectomics block)

**Course:** EN.585.781 Frontiers in Neuroengineering
**Module owner:** Will Gray Roncal (WGR)
**Status:** proposal for instructor and instructional-design review
**Companion material:** rebuilt lecture decks at `course/decks/marp/en585781/`

---

## Why this revision

Three things prompted it.

1. **The instructional designer's note on double-barrelled objectives.** Melissa
   Rizzuto's comment on the CDM — *"need to choose one verb per learning outcome to
   avoid double-barrel objectives"* — applies directly to modules 7–9. Six of the nine
   current MLOs carry two verbs or two objects.

2. **The decks were rebuilt from current material.** The field has moved: FlyWire's
   whole adult fly brain (2024), the MICrONS flagship (2025), connectome-constrained
   models that predict activity (2024), and LICONN's light-microscopy route to dense
   reconstruction (2025) all postdate the previous slides. The module topics should say
   so.

3. **The three modules now share one spine.** They walk a single discovery pipeline —
   question → specimen → image → reconstruction → graph → claim — with Module 7 owning
   the first and last columns conceptually, Module 8 the middle, and Module 9 the
   conversion of measurements into claims. The CDM should make that visible, because it
   is what makes the block cumulative rather than three topics.

**Nothing here changes the assessment structure, the credit weighting, or the test
schedule.** Module 9 remains a test module (modules 7–9 assessed together).

---

## Summary of changes

| | Current | Proposed |
|---|---|---|
| MLO verbs | 6 of 9 double-barrelled | One verb per outcome; 9 → 12 outcomes across the block |
| Module 7 topics | Overall challenge / Macro / Meso / Nanoscale | Why map the brain / What structure can establish / Scales and modalities / The field's eight progression streams |
| Module 8 topics | Large-Scale Storage / Reproducible Pipelines / Data Science | Acquisition and artifacts / Storage, infrastructure and cost / Reproducible, versioned pipelines |
| Module 9 topics | Machine Learning / Algorithmic Approaches / Graph Theory | Segmentation, error and proofreading / Graph construction and null models / Applications and NeuroAI |
| Macroscale coverage | A full topic (macroscale connectomics) | A contrast case only — "different tools for different jobs" |
| Graded artifacts | 5 short-answer questions per module | Unchanged, plus one named artifact per module (study brief / reproducible query / analysis card) |

### On dropping macroscale as a topic

Diffusion MRI and X-ray microtomography now appear once, as the example that different
questions need different instruments — not as material to be covered. Two reasons: the
course's other modules already cover human non-invasive methods in depth (modules 10–12
in particular), and the connectomics block earns its place by teaching what only
synapse-resolution structure can establish. Naming the boundary is pedagogically useful;
re-teaching macroscale is duplicative.

---

## Module 7 — Introduction to Connectomics

**Proposed title:** unchanged.

**Proposed topics**
- Why map the brain: the resolution and cost arguments, in numbers
- What structure can and cannot establish (the claim-bin framework)
- Scales, modalities, and representations — and the leakage between them
- The eight streams the field progresses along, and the results that mark them

**Proposed MLOs** *(one verb each)*

| # | Outcome | CLO |
|---|---|---|
| 7.1 | **Explain** why synapse-resolution structure requires electron microscopy, using the resolution and data-volume arithmetic. | CLO1 |
| 7.2 | **Differentiate** acquisition, reconstruction, and analysis scale for a stated research question. | CLO1, CLO2 |
| 7.3 | **Classify** a connectivity claim as supported by structure alone, by structure plus a declared assumption, or not by structure. | CLO3 |
| 7.4 | **Communicate** the current challenges and opportunities in connectomics without overclaiming. | CLO6 |

*Change note.* Current 7.1 ("Explain the scope … across scales") and 7.2 ("Differentiate
macro-, meso-, and nanoscale approaches") overlapped. The replacement 7.2 is sharper and
is the one students actually need: matching scale to question. New 7.3 makes the
claim-sorting skill an explicit outcome — it is the block's central competency and it was
previously only implicit.

**Instructional activities and assessments** — unchanged in kind, plus:
**graded artifact — a one-page study brief** containing a measurable endpoint, a null
model, and an explicit non-claim.

---

## Module 8 — Nanoscale Connectomics Tools and Methods

**Proposed title:** unchanged.

**Proposed topics**
- From tissue to voxels: preparation, sectioning, imaging, and their artifact signatures
- Storage and infrastructure: chunked multi-resolution arrays, serving, capacity and cost
- Reproducible, versioned pipelines: the ChunkedGraph, materializations, and provenance

**Proposed MLOs**

| # | Outcome | CLO |
|---|---|---|
| 8.1 | **Identify** the tools and formats used for nanoscale acquisition, storage, and serving. | CLO2 |
| 8.2 | **Trace** an artifact in a reconstruction back to the pipeline stage that produced it. | CLO3 |
| 8.3 | **Apply** reproducible-pipeline principles to a query against a public connectomics volume. | CLO3, CLO4 |
| 8.4 | **Estimate** the capacity, compute, and labor cost of a proposed acquisition. | CLO2, CLO5 |

*Change note.* Current 8.2 ("Apply principles of reproducible pipelines") and 8.3
("Propose innovative strategies for scaling") were both broad; 8.3 in particular had no
observable artifact. The replacement 8.3 is assessable — a notebook that returns the same
number a year later — and new 8.2 and 8.4 name skills the module already taught but never
listed.

**Instructional activities and assessments** — unchanged in kind, plus:
**graded artifact — a reproducible query** with a pinned materialization version, stated
inclusion criteria, and one stated limitation.

---

## Module 9 — Nanoscale Connectomics Algorithms and Applications

**Proposed title:** unchanged.

**Proposed topics**
- Segmentation, error taxonomy, quality metrics, and proofreading triage
- Graph construction and null models: the choices that determine the answer
- Applications, comparative connectomics, and NeuroAI

**Proposed MLOs**

| # | Outcome | CLO |
|---|---|---|
| 9.1 | **Describe** how automated segmentation works and where it fails structurally. | CLO4 |
| 9.2 | **Select** quality metrics appropriate to a stated endpoint. | CLO4 |
| 9.3 | **Construct** a connectivity graph from a reconstruction, stating every consequential choice. | CLO3, CLO4 |
| 9.4 | **Justify** a null model for a stated hypothesis and interpret a motif result against it. | CLO4, CLO5 |
| 9.5 | **Assess** what connectomics and machine learning currently give each other. | CLO5, CLO6 |

*Change note.* Current 9.3 ("Synthesize and communicate algorithmic insights") combined
two verbs and two CLOs. Splitting it into 9.4 (justify) and 9.5 (assess) makes both
gradable. Current 9.2 ("Interpret graph-theoretic models") is subsumed by the sharper 9.3
and 9.4.

**Instructional activities and assessments** — unchanged in kind, plus:
**graded artifact — an analysis card** (hypothesis, estimand, null model, success
criterion, error band, non-claim, provenance). Test 3 covers modules 7–9 as scheduled.

---

## Two smaller notes for the CDM as a whole

**Module numbering and order.** Brock Wester's comments ask whether the modules are
listed out of order and whether a preferred order should be re-established. From the
connectomics block's side: modules 7–9 are internally sequential and must stay in that
order relative to each other, but the block as a whole can sit anywhere after the
introductory modules. It does not depend on modules 1–6.

**Module 16's MLO numbering.** Module 16's learning objectives are currently numbered
14.1–14.3, duplicating module 14. Flagging it here since it is a one-line fix and this
document is already going to the same reviewers. Not a connectomics-block issue.

---

## What is already built

The three rebuilt decks — 59, 56, and 58 slides, each in three parts — are in the
NeuroTrailblazers repository at `course/decks/marp/en585781/`, with rendered HTML and
PowerPoint exports, and are published for community use at
`/teaching/lectures/` under **CC BY-SA 4.0**. They are written to the proposed MLOs above. If the MLOs change in
review, the decks will be updated to match rather than the other way round.
