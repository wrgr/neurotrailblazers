---
layout: page
title: "Assessment bank"
permalink: /teaching/assessment/
slug: assessment-bank
content_type: delivery
description: "Twenty public formative items, five per connectomics lecture, tagged to each lecture's learning objectives, with variant templates for writing secure items."
---

[Worked answers and feedback]({{ '/teaching/assessment/answers/' | relative_url }}) · [Lecture series]({{ '/teaching/lectures/' | relative_url }}) · [Module model responses]({{ '/teaching/answers/' | relative_url }})

This bank has five items for each of the four connectomics lectures. Each item is
tagged to one of that lecture's learning objectives. Items mix short answers,
calculations and claim sorting.

**Every number, identifier and scenario here is synthetic.** None is a measurement
from a published dataset. The numbers differ from the lecture worksheets, so the public
worksheet keys do not answer these items.

**This bank is public and formative.** Use it for practice, review and in-class checks.
Because the items and answers are published, they are not secure exam material.
Instructors who need secure summative items should write new variants. Each item ends
with a **variant template** line naming the quantities to change. Recompute every
answer for a variant; do not reuse this bank's answers. Nothing here has been validated
as an assessment instrument, and item difficulty and discrimination are unmeasured.

## Outcome tags

| Lecture | Tag | Objective |
|---|---|---|
| [Introduction]({{ '/teaching/lectures/connectomics-01-introduction/' | relative_url }}) | IN-1 | Explain why synapse-resolution structure requires EM, using resolution and data-volume arithmetic. |
| | IN-2 | Differentiate acquisition, reconstruction and analysis scale for a stated question. |
| | IN-3 | Classify a connectivity claim as supported by structure, by structure plus a declared assumption, or not by structure. |
| | IN-4 | Communicate challenges and opportunities without overclaiming. |
| [Synapse Detection]({{ '/teaching/lectures/synapse-detection/' | relative_url }}) | SD-1 | Distinguish localization, partner assignment and sign inference. |
| | SD-2 | Calculate precision and recall with explicit denominators. |
| | SD-3 | Explain why class-dependent misses bias counts. |
| | SD-4 | Write a defensible audit plan for a released table. |
| [Tools and Methods]({{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }}) | TM-1 | Identify tools and formats for acquisition, storage and serving. |
| | TM-2 | Trace an artifact back to the pipeline stage that produced it. |
| | TM-3 | Apply reproducible-pipeline principles to a query. |
| | TM-4 | Estimate capacity, compute and labor cost. |
| [Algorithms and Applications]({{ '/teaching/lectures/connectomics-03-algorithms-and-applications/' | relative_url }}) | AA-1 | Describe how segmentation fails structurally. |
| | AA-2 | Select quality metrics for a stated endpoint. |
| | AA-3 | Construct a graph, stating every consequential choice. |
| | AA-4 | Justify a null model and interpret a result against it. |
| | AA-5 | Assess what connectomics and machine learning give each other. |

## Introduction

**I1. Calculation (IN-1).** Take a synaptic cleft to be 20 nm across. A light
microscope in this item resolves 250 nm laterally.

(a) What is the largest pixel size that samples the cleft at least twice across?
(b) How many times coarser, linearly, is 250 nm than that pixel? How many times more
pixels per unit area does the finer sampling need?
(c) A block of 0.4 × 0.3 × 0.1 mm is imaged at 8 × 8 × 40 nm, one byte per voxel,
no compression. Give the voxel dimensions, total voxels and size in decimal TB.

*Variant template:* change the cleft width, the light-microscope resolution, the
block dimensions, the voxel size and the bytes per voxel.

**I2. Calculation (IN-3).** A synthetic reconstruction has seven eligible directed
cell pairs in a fully reviewed region. Their synapse counts are 6, 0, 4, 0, 1, 9 and 2.
Give the total synapse count, the connected fraction, the mean count per eligible pair
and the mean count per connected pair. State each denominator.

*Variant template:* change the number of pairs, the counts and how many are zero.

**I3. Claim sorting (IN-3).** In a synthetic, fully reviewed region, cell P makes 9
synapses onto cell Q, and Q makes 2 onto P. P was classified as an interneuron by
morphology alone. Nothing is known about activity. Sort each claim: **A**, supported
by the structural evidence; **B**, requires a stated structure-to-function assumption;
**C**, needs an additional measurement. Give the reason.

1. P makes nine synapses onto Q in the reviewed region.
2. P and Q are reciprocally connected in the reviewed region.
3. P inhibits Q.
4. P's effect on Q is 4.5 times stronger than Q's effect on P.
5. Silencing P would change Q's firing during a task.
6. Q receives more synapses from P than from any other cell.

*Variant template:* change the two counts, the basis of the cell classification and
which claims appear; keep at least one claim that needs more structure, not physiology.

**I4. Short answer (IN-2).** For each question, name the analysis unit and the coarsest
acquisition scale that resolves it.

(a) Across one hemisphere, do labeled axons from region R1 project more heavily to R2
or to R3?
(b) In one cortical column, do cells of type K form synapses on the axon initial
segments of pyramidal cells?
(c) For (b), state the acquisition, reconstruction and analysis scale separately.

*Variant template:* change the two questions so that one needs synapse resolution and
one does not.

**I5. Short answer (IN-4).** A press release about the study in I1(c) says:
“Researchers have mapped every connection in the mouse brain and can now read memories
from its wiring.” Name the overclaims and rewrite the sentence so it matches the study.

*Variant template:* change the species, the reconstructed volume and the functional
claim being oversold.

## Synapse Detection

**S1. Classification (SD-1).** Classify each failure as **localization**, **partner
assignment** or **sign inference**.

(a) A prediction sits on a mitochondrial membrane where there is no synapse.
(b) A real synapse is absent from the table.
(c) The cleft is correct, but the postsynaptic partner is an adjacent dendrite.
(d) Cleft and partners are correct, but the row says inhibitory and the reference says
excitatory.
(e) The cleft is correct, but the presynaptic segment is a merge of two axons, so the
row names the wrong cell.

*Variant template:* write new failure descriptions, keeping at least one whose cause
lies in segmentation rather than detection.

**S2. Calculation (SD-2).** Validation against independent exhaustive annotation,
matched one-to-one:

- **E:** 63 true positives, 7 false positives, 27 false negatives.
- **I:** 36 true positives, 12 false positives, 9 false negatives.

Give precision, recall and F1 for each class with denominators. Can accuracy be
computed? The two F1 values are close. Does that mean the classes have the same errors?

*Variant template:* change TP, FP and FN for each class, keeping one class
miss-dominated and the other false-alarm-dominated.

**S3. Calculation (SD-3).** The predicted table from S2 has 70 E rows and 48 I rows.
Give the observed E fraction. Using estimated count = predicted count × precision /
recall, correct each class and give the corrected E fraction and its change in
percentage points. Explain the direction of the change. Is recovering the reference
totals evidence that the correction works on another region?

*Variant template:* change the row counts and the S2 inputs; vary which class has the
lower recall so the direction of change is not fixed.

**S4. Calculation (SD-1, SD-2).** Of the 99 true-positive detections in S2, 84 have
both partners assigned correctly. The reference contains 135 contacts. Give partner
correctness conditional on detection and end-to-end partner-pair recall. Which number
describes the whole pipeline?

*Variant template:* change the number of correctly assigned pairs and the S2 counts.

**S5. Short answer (SD-4).** A colleague proposes: “We will sample 500 random rows of
the released table from one region, check each by eye, and report precision and recall
for the whole dataset.” Name the flaws and write a repaired plan.

*Variant template:* change the sample size, the sampling frame and the scope of the
claimed generalization.

## Tools and Methods

**T1. Matching (TM-1).** Assign each item to **acquisition**, **storage and serving**,
**viewing** or **annotation and versioning**: (a) multibeam scanning EM; (b) a chunked,
multi-resolution array format such as Zarr, N5 or Precomputed; (c) Neuroglancer;
(d) CAVE materialization; (e) an image pyramid. Then explain in two sentences why chunk
shape is an access-pattern decision.

*Variant template:* swap in other named tools from the lecture, such as FIB-SEM, ATUM
or the ChunkedGraph.

**T2. Artifact tracing (TM-2).** For each synthetic observation, name the coordinate
system it follows (block position, anatomy, acquisition time, processing grid or data
version) and the stage that most likely produced it.

(a) Staining intensity falls steadily with distance from the block's cut surface, in
every field.
(b) Brightness jumps at square boundaries every 1,024 voxels, regardless of anatomy.
(c) Sections 2,301–2,340 are blurrier than their neighbors; the log shows a beam
adjustment just before section 2,301.
(d) Synapse density is higher in one cortical layer; staining is uniform across depth
in the same sections.
(e) A cell's input count changed between two queries a month apart, with no new imaging.

*Variant template:* change which coordinate each defect follows and the section
numbers, grid size and interval.

**T3. Calculation and record (TM-3).** Count rows with post = 205, region = shell and
score ≥ 0.70. Rows are `(id, post, region, score)`.

Snapshot C:

```text
(r1, 205, shell, 0.71)
(r2, 205, shell, 0.70)
(r3, 205, core,  0.93)
(r4, 207, shell, 0.88)
(r5, 205, shell, 0.52)
(r6, 205, shell, 0.97)
```

Snapshot D keeps r1–r5, changes r5's score to 0.74, relabels r6's postsynaptic ID to
209 after a proofreading split, and adds `(r7, 205, shell, 0.69)`.

(a) List the included IDs and count for each snapshot.
(b) Repeat with score > 0.70.
(c) The two counts in (a) are equal. Is the result reproduced? What must a methods
record contain for someone else to rerun (a)?

*Variant template:* change the rows, the filter values and the snapshot edits, keeping
one row exactly at the threshold and one edit that changes an ID.

**T4. Calculation (TM-4).** A hypothetical acquisition covers 250 × 200 × 60 µm at
8 × 8 × 30 nm, one channel, one byte per voxel, no compression. Give the voxel
dimensions, total voxels and decimal GB. Give the capacity for two total copies and the
ideal transfer time for one copy at a sustained 250 MB/s. Use 1 GB = 10⁹ bytes and
1 MB = 10⁶ bytes. Name two things the estimate omits.

*Variant template:* change the volume, voxel size, bytes per voxel, copy count and
transfer rate.

**T5. Calculation (TM-4).** A synthetic project will proofread 1,500 cells at 4 hours
per cell. Take one annotator-year as 1,500 productive hours. How many annotator-years
is that? If 20% of cells also receive a second review taking the same time, what is the
new total? Name one cost the estimate still leaves out.

*Variant template:* change the cell count, hours per cell, productive hours per year
and review fraction.

## Algorithms and Applications

**A1. Classification (AA-1).** Classify each synthetic segmentation failure as a
**merge** or **split**.

(a) Two axons cross where the membrane between them is faint and become one object.
(b) A thin axon passes through a missing section and becomes two objects.
(c) A spine neck is cut, and the spine head with its synapse becomes a separate object.
(d) A glial process is joined to a dendrite.

For an endpoint of “synapse count between two identified cells,” can you say in
advance whether each error raises or lowers the count?

*Variant template:* change the structures and imaging conditions; include one error
whose effect on the endpoint depends on which cells are involved.

**A2. Matching and claim check (AA-2).** Match each endpoint to the most relevant
metric: **expected run length (ERL)**, **variation of information (VI)** or
**synapse/edge precision and recall**.

(a) Total dendritic path length of reconstructed cells.
(b) Connection probability between two cell types.
(c) Overall agreement between a segmentation and a ground-truth region, split into
merge and split components.

Then evaluate: “ERL is 120 µm, so our reciprocity estimate is reliable.”

*Variant template:* change the endpoints and the quoted metric value.

**A3. Calculation (AA-3, AA-4).** Graph version `synthetic-five-node-graph-v1` has
nodes V, W, X, Y and Z. Directed contact counts:

```text
V to W: 3    W to V: 2    V to X: 1    X to V: 1    W to X: 4
X to Y: 2    Y to X: 1    Y to Z: 5    Z to W: 2    Z to V: 1
```

All other ordered pairs have zero contacts. Keep all five nodes, omit self-loops, and
make one binary edge per ordered pair meeting the threshold. A reciprocal pair is an
unordered pair with both directions present, counted once. The null is uniform over all
directed simple graphs on these five labeled nodes with the same edge count. The
prespecified rule is an inclusive upper tail ≤ 0.05.

Exact null censuses of reciprocal pairs R:

- **10 edges:** R = 0: 1,024; 1: 23,040; 2: 80,640; 3: 67,200; 4: 12,600; 5: 252
  (184,756 graphs).
- **6 edges:** R = 0: 13,440; 1: 20,160; 2: 5,040; 3: 120 (38,760 graphs).
- **9 edges:** R = 0: 5,120; 1: 46,080; 2: 80,640; 3: 33,600; 4: 2,520 (167,960 graphs).

(a) At threshold one contact, give the edge count, R and the reciprocated-edge fraction.
Give the null mean, observed/expected ratio and upper tail. Is the rule met?
(b) Repeat at threshold two contacts.
(c) The single X-to-V contact is flagged as uncertain. Remove that edge only, at
threshold one. Recompute R, the fraction and the tail against the correct null.

*Variant template:* change the contact counts so the edge counts and R change, and
regenerate the exact censuses by enumeration.

**A4. Short answer (AA-4).** For each hypothesis, name the property the null must hold
fixed and why the uniform fixed-edge-count null of A3 is not enough.

(a) Reciprocity exceeds what physical proximity between cells alone would produce.
(b) Reciprocity is concentrated among a few highly connected cells.
(c) Reciprocity is higher within a cell type than between types.

*Variant template:* change the hypotheses and the motif (for example, a feedforward
triangle instead of a reciprocal pair).

**A5. Claim sorting (AA-5).** Label each statement **defensible**, **overclaim** or
**dismissive underclaim**, and give the reason.

1. Machine-learning segmentation has made large-volume reconstruction feasible.
2. A network model constrained by a connectome is guaranteed to reproduce the animal's
   behavior.
3. Connectomics has nothing to offer machine learning.
4. So far, machine learning has given connectomics more than connectomics has given
   machine learning.
5. Because both are networks of “neurons,” a connectome reveals the brain's learning rule.

*Variant template:* write new statements, keeping at least one of each label.

Teaching material: CC BY-SA 4.0, NeuroTrailblazers.
