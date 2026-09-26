---
layout: page
title: "Assessment bank: worked answers"
permalink: /teaching/assessment/answers/
slug: assessment-bank-answers
content_type: delivery
description: "Worked answers and error-specific feedback for the twenty synthetic assessment bank items, with every calculation recomputed."
---

[Assessment bank items]({{ '/teaching/assessment/' | relative_url }}) · [Lecture series]({{ '/teaching/lectures/' | relative_url }})

These answers use the bank's **synthetic** data. They are public and formative. Every
calculation was recomputed independently with exact fractions in Python, including
full enumeration of the A3 null censuses; the results match the values below. For each
item, the feedback lines name a specific wrong answer or reasoning error and what to
say to a learner who gives it.

This bank is not secure. For summative use, write a variant from the template on each
item and recompute its answers. Nothing here is a validated assessment instrument.

## Scoring

Score each short-answer and claim-sorting item **0–2**: two for a correct answer with
its reason, one for a correct answer with a missing or partial reason, zero for an
incorrect or unsupported answer. Score each calculation **0–2**: two for correct values
with denominators or units shown, one for a single recoverable slip with correct
setup, zero for a wrong setup. Credit a correct reason attached to a defensible
alternative classification where the feedback says so. This is a local teaching
rubric, not a validated assessment instrument.

## Introduction

### I1 (IN-1)

(a) **10 nm.** Sampling a 20 nm structure at least twice across needs a pixel no
larger than half its width.
(b) **250/10 = 25** times coarser linearly, and **25² = 625** times more pixels per
unit area.
(c) 400,000 × 300,000 × 100,000 nm divided by 8 × 8 × 40 nm gives
**50,000 × 37,500 × 2,500 voxels = 4,687,500,000,000 (4.6875 × 10¹²)**. At one byte per
voxel this is **4.6875 TB**, about 4.69 TB decimal.

Feedback by error:

- **20 nm pixel.** “How many pixels would fall across the cleft?” One sample across a
  structure cannot resolve it.
- **12.5×.** The learner compared 250 nm with the cleft, not the pixel. Ask which
  quantity the microscope has to match.
- **25× for area.** Resolution applies in both lateral dimensions; the pixel count scales
  with the square.
- **Answer off by 10³ or 10⁶.** Check 1 mm = 10⁶ nm and 1 µm = 10³ nm before dividing.
- **4.26.** Correct only if labeled TiB (binary). Accept it when the unit is stated.

### I2 (IN-3)

Total **22** synapses. Connected fraction **5/7 = 71.4%** (denominator: eligible pairs).
Mean per eligible pair **22/7 ≈ 3.14**. Mean per connected pair **22/5 = 4.4**.

Feedback by error:

- **4.4 reported as “mean per pair.”** That excludes the two zero pairs. Ask which
  denominator the claim needs.
- **“71% of cells are connected.”** The unit is a directed pair, not a cell.
- **Zeros dropped from the table.** A reviewed zero is data. Removing it inflates both
  the fraction and the mean.

### I3 (IN-3)

1. **A.** A direct structural count in the reviewed region.
2. **A.** Both directions were observed in the reviewed region.
3. **B.** It assumes that the morphological class predicts an inhibitory transmitter and
   effect. Accept **C** if the learner says the assumption is untested and names the
   measurement (transmitter identity or physiology). Do not accept A.
4. **B.** It assumes synapse count scales with physiological effect. The defensible
   version is “P makes 4.5 times as many synapses onto Q as Q makes onto P.” Testing
   the stronger claim needs paired recording.
5. **C.** A causal claim; it needs a perturbation during the task.
6. **C, but the missing measurement is structural.** No other inputs to Q were reported.
   Counting all of Q's reviewed inputs would test it within the region. Even then it
   would not extend beyond the region.

Feedback by error:

- **Claim 6 marked C “because it needs physiology.”** Ask what data would settle it.
  More structure, not physiology, is needed.
- **Claim 4 marked A because 9/2 = 4.5.** The arithmetic is right; the word “effect”
  is the assumption.
- **Claim 3 marked A.** A morphological label is not a measured sign.

### I4 (IN-2)

(a) The analysis unit is a **region-to-region projection** from labeled axons. Light
microscopy at mesoscale resolves it. EM would multiply data volume by orders of
magnitude with no gain for this unit.
(b) The unit is a **synapse on a specific subcellular compartment of an identified
partner**. Only synapse-resolving EM identifies the synapse and the axon initial segment
on the same cell.
(c) **Acquisition:** nanometer-scale voxels over the column. **Reconstruction:** traced
neurites of type-K cells and pyramidal cells, with synapses assigned to partners and
compartments. **Analysis:** counts of type-K synapses per pyramidal axon initial segment,
over cells in the column.

Feedback by error:

- **EM for (a).** “What is the unit in your conclusion?” The rule is the coarsest scale
  that resolves the unit, not the finest available.
- **Voxel size given as the analysis scale.** The analysis unit is a cell pair or a
  compartment, not an image feature.

### I5 (IN-4)

Overclaims: **“every connection in the mouse brain”** (the study imaged a
0.4 × 0.3 × 0.1 mm block, and reconstruction misses some synapses) and **“read memories
from its wiring”** (a functional claim structure alone cannot support).

Rewrite: “Researchers reconstructed synaptic wiring in a small block of mouse cortex.
The map shows which reconstructed cells contact which. It does not show what those
cells encode or remember.”

Feedback by error:

- **Rewrite that removes all interest.** “Structure cannot tell us anything” is also
  wrong. The map says exactly which additional experiment a memory claim would need.
- **Only the scope fixed.** Ask which word still claims function.

## Synapse Detection

### S1 (SD-1)

(a) **Localization** (false positive). (b) **Localization** (false negative).
(c) **Partner assignment.** (d) **Sign inference.** (e) **Partner assignment**, caused
by a segmentation merge. The detection itself was correct.

Feedback by error:

- **(e) labeled localization.** The cleft is in the right place. The error enters
  through the segment ID, so fixing the detector would not fix it.
- **(b) labeled partner assignment.** There is no row, so no partner was assigned.

### S2 (SD-2)

| Class | Precision | Recall | F1 |
|---|---|---|---|
| E | 63/70 = **0.900** | 63/90 = **0.700** | 126/160 = **0.788** |
| I | 36/48 = **0.750** | 36/45 = **0.800** | 72/93 = **0.774** |

**Accuracy cannot be computed.** There are no true negatives and no defined negative
universe. The F1 values are close, but the errors differ: E is **miss-dominated**
(27 false negatives), I is **false-alarm-dominated** (12 false positives). F1 hides that.

Feedback by error:

- **Recall as TP/(TP+FP).** That is precision. Ask what denominator counts the reference
  synapses.
- **F1 = 0.800 for E and 0.775 for I.** The learner averaged precision and recall. F1 is
  the harmonic mean, 2TP/(2TP+FP+FN).
- **Accuracy = 0.649 or 0.632.** That is TP/(TP+FP+FN), a different statistic. It is not
  accuracy.
- **“Equal F1 means equal errors.”** Compare the FP and FN columns directly.

### S3 (SD-3)

Observed E fraction: **70/118 = 59.3%**.

- E: 70 × 0.900 / 0.700 = **90**.
- I: 48 × 0.750 / 0.800 = **45**.
- Corrected E fraction: 90/135 = **66.7%**, up **7.3 percentage points**.

E has the lower recall and the higher precision, so its correction is larger. The E
fraction rises. The direction depends on the class-specific errors; it is not fixed.

Recovering 90 and 45 is **algebraic**: those are the reference totals (63 + 27 and
36 + 9) that produced the precision and recall. It is not independent validation.
Applying the correction elsewhere assumes that class-specific error rates transfer,
matching rules are the same and class labels are stable.

Feedback by error:

- **“The E fraction goes down.”** The learner applied a remembered direction. Ask which
  class misses more.
- **7.3% reported as a relative change.** The change is in percentage points; say so.
- **Correction treated as exact.** The estimates carry sampling uncertainty from the
  validation counts.

### S4 (SD-1, SD-2)

Conditional partner correctness: **84/99 = 84.8%**. End-to-end partner-pair recall:
**84/135 = 62.2%**. The second describes the pipeline, because it counts the 36 reference
contacts that were never detected.

Feedback by error:

- **84.8% reported as pipeline recall.** Ask where the missed contacts appear in that
  denominator. They do not.
- **84/118.** The learner used predicted rows. False positives have no true partner, so
  they belong to neither denominator.

### S5 (SD-4)

Flaws:

- **Recall cannot be estimated from existing rows.** Missed synapses are not in the table.
- **One region does not represent the dataset.** It cannot support a whole-dataset
  claim.
- **No independent reference.** Checking predictions “by eye” is biased toward accepting
  them.
- **No version, class breakdown or uncertainty** is specified.

Repaired plan: record the table version and threshold. Choose several prespecified
regions, including difficult image conditions. Annotate every synapse in them
independently of the predictions, then match one-to-one under a stated rule. Report
TP, FP and FN by class and region, partner correctness separately, and uncertainty that
accounts for clustering within regions. State which regions the result represents.

Feedback by error:

- **“Increase the sample to 5,000 rows.”** A larger sample of rows still cannot find
  misses.
- **Region sampling without independent annotation.** The same limit applies.

## Tools and Methods

### T1 (TM-1)

(a) **Acquisition.** (b) **Storage and serving.** (c) **Viewing.** (d) **Annotation and
versioning.** (e) **Storage and serving**: downsampled levels let a viewer fetch only the
resolution it needs.

Chunk shape: data are read one chunk at a time. Chunks shaped to match how the data
will be read, such as thin slabs for section viewing or cubes for 3D neurite tracing,
reduce the bytes fetched per request.

Feedback by error:

- **Neuroglancer as storage.** It reads chunked formats; it does not define them.
- **CAVE as a viewer.** CAVE tracks edits and versions of annotations; the viewer is
  separate.

### T2 (TM-2)

(a) **Block position**: staining penetration during preparation. It can mimic a laminar
difference.
(b) **Processing grid**: tile or chunk-wise normalization or stitching.
(c) **Acquisition time**: an imaging change logged before section 2,301.
(d) **Anatomy**: plausibly biological, because staining is uniform with depth. It still
needs its own check before it is reported.
(e) **Data version**: proofreading or materialization changes, not tissue change.

Feedback by error:

- **(a) called a laminar biology result.** Ask whether the gradient follows the cut
  surface or the layers. That test separates them.
- **(e) called growth or better detection.** Ask what evidence identifies the two
  versions before interpreting the change.

### T3 (TM-3)

(a) Snapshot C: **r1, r2, r6; count 3**. Excluded: r3 (region), r4 (post), r5 (score).
Snapshot D: **r1, r2, r5; count 3**. Excluded: r3, r4, r6 (post now 209) and r7 (0.69).
(b) With score > 0.70: C gives **r1, r6 (2)**; D gives **r1, r5 (2)**. r2 sits exactly at
the threshold.
(c) **Not reproduced.** The counts match but the IDs differ: r6 left after a split and
r5 entered after a score revision. Compare IDs, not only counts. A methods record needs
the snapshot identifier, the exact filter including ≥ versus >, the object and region
scope, the query code and its version, the run date and environment, and the returned
IDs.

Feedback by error:

- **“Same count, so reproduced.”** Ask for the ID lists side by side.
- **r2 excluded in (a).** Check the inclusive sign.
- **r6 still counted in D.** The postsynaptic label changed; IDs change with proofreading.

### T4 (TM-4)

250,000 × 200,000 × 60,000 nm divided by 8 × 8 × 30 nm gives
**31,250 × 25,000 × 2,000 voxels = 1,562,500,000,000 (1.5625 × 10¹²)**. At one byte:
**1,562.5 GB**. Two copies: **3,125 GB**. One transfer at 250 MB/s:
1.5625 × 10¹² / 2.5 × 10⁸ = **6,250 s, about 104 minutes**.

Omitted: segmentation and other derived arrays, image pyramids, metadata and chunk
overhead, backups beyond two copies, protocol overhead, and any compression effect.

Feedback by error:

- **Z voxel taken as 8 nm.** That multiplies the result by 3.75. Read all three voxel
  dimensions.
- **3,125 GB for one copy.** That is two bytes per voxel. The item specifies one.
- **Transfer time treated as acquisition time.** They are unrelated quantities.

### T5 (TM-4)

1,500 × 4 = **6,000 hours = 4.0 annotator-years**. With a second review of 20% of cells:
6,000 + 0.20 × 6,000 = **7,200 hours = 4.8 annotator-years**.

Still omitted: training time, supervision and adjudication, variation in hours per cell,
tool and storage costs, and turnover.

Feedback by error:

- **4.2 annotator-years.** The learner added 0.2 to the annotator-years instead of
  adding 20% of the hours. Recompute from hours: 7,200 / 1,500 = 4.8.
- **Calendar time from annotator-years alone.** Calendar time depends on how many
  people work in parallel.

## Algorithms and Applications

### A1 (AA-1)

(a) **Merge.** (b) **Split.** (c) **Split**; the detached spine head is an orphan
fragment. (d) **Merge.**

The direction of the change cannot always be said in advance. A split that detaches a
synapse from one of the two cells removes it from the count. A merge can add a false
partner, or it can join the two cells so their synapses become internal and disappear
from the pair. The effect depends on which cells are involved.

Feedback by error:

- **“Merges always raise counts and splits always lower them.”** Give the case of a merge
  that joins the two cells in the pair.
- **(c) called a merge.** One object became two.

### A2 (AA-2)

(a) **ERL.** It measures how far one can trace before an error, which bears on path
length. (b) **Synapse/edge precision and recall**, with partner correctness. (c) **VI**,
with merge and split components; it needs ground truth.

The claim is **not supported**. ERL measures tracing length, not synapse or partner
accuracy. A reciprocity estimate needs edge-level precision and recall, and merges near
synapses can create false reciprocal pairs even when ERL is long.

Feedback by error:

- **VI chosen for (b).** VI summarizes segmentation agreement; it does not say which
  connections are right.
- **Claim accepted because 120 µm is “high.”** Ask what the metric counts.

### A3 (AA-3, AA-4)

(a) **Threshold one:** all 10 listed pairs are edges. Reciprocal pairs **{V,W}, {V,X},
{X,Y}**, so **R = 3**. Reciprocated-edge fraction **2R/m = 6/10 = 3/5 = 0.600**.

- Null mean: (23,040 + 2 × 80,640 + 3 × 67,200 + 4 × 12,600 + 5 × 252) / 184,756 =
  **45/19 ≈ 2.368**.
- Observed/expected: 3 / (45/19) = **19/15 ≈ 1.267**.
- Upper tail, R ≥ 3: (67,200 + 12,600 + 252) / 184,756 = 80,052/184,756 =
  **20,013/46,189 ≈ 0.433**. The rule is **not met**.

(b) **Threshold two:** V-to-X, X-to-V, Y-to-X and Z-to-V drop out. Six edges remain:
V-to-W, W-to-V, W-to-X, X-to-Y, Y-to-Z, Z-to-W. Only **{V,W}** is reciprocal: **R = 1**,
fraction **2/6 = 1/3 ≈ 0.333**. All five nodes remain under the stated rule.

- Null mean: (20,160 + 2 × 5,040 + 3 × 120) / 38,760 = **15/19 ≈ 0.789**.
- Observed/expected: **19/15 ≈ 1.267**, the same ratio as (a).
- Upper tail, R ≥ 1: (20,160 + 5,040 + 120) / 38,760 = **211/323 ≈ 0.653**. **Not met.**

The ratio is identical at both thresholds, but the tails differ. Enrichment ratio is not
evidence strength. The null's edge count must match the graph's, so each threshold
needs its own census.

(c) **Error scenario:** removing X-to-V leaves **9 edges**, **R = 2** ({V,W}, {X,Y}),
fraction **4/9 ≈ 0.444**. Against the nine-edge null, mean **36/19 ≈ 1.895**, tail
R ≥ 2: (80,640 + 33,600 + 2,520) / 167,960 = **2,919/4,199 ≈ 0.695**. This is a
**scenario sensitivity check**. It shows the endpoint depends on one contact; it is not
a confidence interval or a measured error rate.

The mean can be checked without the census: with 10 unordered pairs and 20 ordered
pairs, E[R] = 10 × m(m − 1) / (20 × 19). For m = 10, 6 and 9 this gives 45/19, 15/19
and 36/19.

Feedback by error:

- **R = 6 at threshold one.** The learner counted reciprocated directed edges, not
  unordered pairs. Name which statistic is reported.
- **Tail computed as R > 3 (12,852/184,756 ≈ 0.070).** The rule is inclusive; count graphs at least as
  extreme as observed.
- **Ten-edge census reused at threshold two.** The null must match the graph's edge
  count.
- **“O/E above 1, so reciprocity is enriched.”** Above the mean is not the decision rule.
- **“Not met, so wiring is random.”** Failing the rule does not show absence of
  structure; this null also leaves degree, distance and type uncontrolled.

### A4 (AA-4)

(a) Hold fixed **the distance or contact opportunity** between cells, for example by
drawing edges with probabilities that depend on measured axon–dendrite proximity. A
uniform null ignores that nearby cells connect more in both directions.
(b) Hold fixed **each node's in- and out-degree**. Highly connected cells produce more
reciprocal pairs by chance; the uniform null does not preserve degree.
(c) Hold fixed **the cell-type labels and the number of edges within and between types**.
Otherwise type-specific density alone can create a within-type excess.

Feedback by error:

- **“Add every constraint.”** Constraints follow the hypothesis. Holding fixed the
  property under test removes the effect.
- **Degree-preserving null for (a).** Degree does not control spatial opportunity.

### A5 (AA-5)

1. **Defensible.** Automated segmentation is what makes large volumes tractable.
2. **Overclaim.** Wiring constrains a model; it does not supply dynamics, weights and
   neuromodulation, and it guarantees no behavior.
3. **Dismissive underclaim.** Dismissing the connection outright is the symmetric error.
   A defensible view is that the contribution so far is smaller and more specific.
4. **Defensible.** This is the lecture's stated position.
5. **Overclaim.** A shared word is not shared mechanism, and a wiring diagram does not
   reveal a learning rule.

Feedback by error:

- **Statement 3 marked defensible.** The lecture names two errors, not one; this is the
  second.
- **Statement 4 marked an underclaim.** It is a comparative claim about the present, not
  a dismissal.

Teaching material: CC BY-SA 4.0, NeuroTrailblazers.
