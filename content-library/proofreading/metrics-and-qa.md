---
layout: page
title: "Metrics and Quality Assurance for Connectome Proofreading"
permalink: /content-library/proofreading/metrics-and-qa/
image: /assets/images/content-library/proofreading/metrics-and-qa.svg
image_alt: "Stylized vector art: a traced process with marked error sites under review."
description: >
  An instructor reference on quantitative metrics for evaluating
  segmentation and proofreading quality, including Variation of Information,
  Expected Run Length, edge and synapse precision/recall, and completeness
  metrics. Covers dashboard design, worked computation examples, and guidance
  on when metrics disagree.
topics:
  - variation of information
  - expected run length
  - precision and recall
  - synapse metrics
  - completeness metrics
  - quality assurance
  - dashboard design
  - segmentation evaluation
primary_units:
  - "08"
difficulty: advanced
tags:
  - methodology:qa-metrics
  - methodology:variation-of-information
  - methodology:expected-run-length
  - connectomics:edge-f1
  - connectomics:synapse-f1
  - proofreading:inter-annotator-agreement
  - methodology:benchmarking
micro_lesson_id: ml-proof-metrics
combines_with:
  - error-taxonomy
  - proofreading-strategies
  - worked-examples
use_layout_hero: false
content_type: core
---

# Metrics and Quality Assurance for Connectome Proofreading

## Instructor Notes

This document is a standalone instructor script. It provides the full
mathematical framework, intuitive explanations, worked numerical examples,
and practical guidance on designing QA systems. The math is presented at a
level accessible to students with basic probability and information theory
background; provide additional scaffolding for younger or less mathematical
audiences.

---

## 1. Why Metrics Matter

### 1.1 The Problem with Subjective Quality

Without quantitative measures, proofreading quality is a matter of
opinion. "It looks pretty good" is not a publishable quality statement.
Metrics enable:

- **Comparing segmentation methods.** Which pipeline produces fewer errors
  on the same dataset? Metrics provide an objective answer.
- **Tracking proofreading progress.** After 100 hours of proofreading, is
  the dataset meaningfully better? Metrics quantify improvement.
- **Setting release criteria.** "We will release the dataset when ERL
  exceeds 100 um" is a concrete, verifiable standard.
- **Communicating quality to downstream users.** A connectome analysis
  paper can report: "The segmentation has VI_merge = 0.02, VI_split = 0.05,
  and ERL = 150 um in the proofread region."

### 1.2 No Single Metric Is Sufficient

Each metric captures a different aspect of quality, and a segmentation can
score well on one and poorly on another. Before you report a metric, be able
to say what it measures and what it misses. Section 9 gives three cases where
they disagree.

---

## 2. Variation of Information (VI)

### 2.1 Definition

Variation of Information is an information-theoretic measure of the
distance between two clusterings (segmentations). Given a predicted
segmentation S and a ground-truth segmentation T over the same set of
voxels:

    VI(S, T) = H(S|T) + H(T|S)

where H(S|T) is the conditional entropy of S given T, and H(T|S) is the
conditional entropy of T given S.

### 2.2 Intuition

- **H(S|T) measures over-segmentation (split errors).** If you know the
  ground-truth label of a voxel, how much additional information do you
  need to determine its predicted label? High H(S|T) means the predicted
  segmentation splits ground-truth segments into many pieces.

- **H(T|S) measures under-segmentation (merge errors).** If you know the
  predicted label of a voxel, how much additional information do you need
  to determine its ground-truth label? High H(T|S) means the predicted
  segmentation merges distinct ground-truth segments.

### 2.3 Mathematical Detail

Let N be the total number of voxels. Let p_i = |S_i|/N be the fraction
of voxels in predicted segment i, and q_j = |T_j|/N be the fraction in
ground-truth segment j. Let r_ij = |S_i intersect T_j|/N.

    H(S|T) = - sum_{i,j} r_ij * log(r_ij / q_j)
    H(T|S) = - sum_{i,j} r_ij * log(r_ij / p_i)

### 2.4 Properties

- **Range:** 0 (perfect agreement) to log(N) (every voxel in its own
  segment vs. all voxels in one segment).
- **Decomposable:** The split and merge components are separate, so you
  can diagnose whether over- or under-segmentation dominates.
- **Metric:** VI satisfies the mathematical definition of a metric
  (non-negative, symmetric, triangle inequality). Cited from Meila (2007).
- **Size-sensitive:** Large segments contribute more to VI than small ones,
  which is usually desirable (errors on large neurons matter more).

### 2.5 Limitations

- **Hard to interpret biologically.** A VI of 0.15 bits does not
  immediately tell you how many neurons are wrong or how many connections
  are affected.
- **Sensitive to segment size distribution.** Datasets with many small
  segments (e.g., dense neuropil with lots of thin axons) tend to have
  higher VI even at similar per-neuron accuracy.
- **Requires voxel-level ground truth.** This is expensive to produce.

### 2.6 Instructor Tip

Present VI as a standard metric for segmentation benchmarks (CREMI
scores neuron segmentation with VI alongside adapted Rand error; SNEMI3D
ranks by adapted Rand error) but explain that its biological
interpretability is limited. Students should be able to compute it and
interpret which component (split vs. merge) is dominant, but should not
rely on it alone.

---

## 3. Expected Run Length (ERL)

### 3.1 Definition

Expected Run Length is the average distance (in micrometers) that you can
trace along a ground-truth neurite before encountering a topological error
(merge or split) in the predicted segmentation. Januszewski et al. (2018)
used it to evaluate flood-filling networks, and it has since become a
standard way to report segmentation quality in large volumes.

### 3.2 Computation

1. Take the ground-truth skeleton of each neuron.
2. Look up the predicted segment label at each skeleton node.
3. Cut each skeleton into runs wherever the predicted label changes. Each
   cut is a **split error**.
4. If a run's predicted segment also contains nodes of a different
   ground-truth neuron, that segment is a **merge error**, and the run
   contributes zero length.
5. ERL is the expected length of the run that contains a randomly chosen
   point on the ground-truth skeletons. Each run is weighted by its own
   length: ERL = (sum of run length squared) / (total skeleton length).

### 3.3 Intuition

ERL answers the practical question: "If I pick a random point on a random
neuron and start tracing, how far can I go before the segmentation
misleads me?"

- **ERL = 10 um** means errors are very dense; you hit one every 10 um
  of tracing. The segmentation is barely usable without heavy proofreading.
- **ERL = 100 um** means you can trace typical dendritic branches
  end-to-end without encountering an error. Good for many analyses.
- **ERL = 1,000 um** means errors are rare at the scale of a local arbor.
  Long-range axons will still cross errors.

### 3.4 Properties

- **Biologically interpretable.** Researchers can immediately assess
  whether ERL is sufficient for their specific analysis.
- **Weighted toward merges.** A merge zeroes the run length of every
  skeleton path in the merged segment. Recomputing ERL with merges ignored
  shows how much of the loss comes from splits alone.
- **Scale-dependent.** ERL improves as segment quality improves but also
  depends on the density and morphology of neurons in the volume.

### 3.5 Limitations

- **Requires skeleton ground truth.** Dense voxel-level ground truth is
  not sufficient; you need topological skeleton annotations.
- **Sensitive to skeleton topology.** How the skeleton is constructed
  (node spacing, branch point placement) affects ERL values.
- **Not intuitive for non-tracing applications.** If your analysis is
  purely connectivity-based (you only care about the graph, not the
  morphology), ERL is an indirect measure.

---

## 4. Edge Precision and Recall

### 4.1 Definition

Treat the connectome as a directed graph where each edge represents a
synaptic connection from neuron A to neuron B. Compare the predicted
graph to the ground-truth graph:

- **True Positive (TP):** An edge exists in both predicted and ground
  truth.
- **False Positive (FP):** An edge exists in predicted but not ground
  truth.
- **False Negative (FN):** An edge exists in ground truth but not
  predicted.

Then:

    Precision = TP / (TP + FP)
    Recall    = TP / (TP + FN)
    F1        = 2 * Precision * Recall / (Precision + Recall)

### 4.2 Intuition

- **Precision** answers: "Of the connections the segmentation claims
  exist, what fraction are real?" Low precision means many false
  connections (typically caused by merge errors).
- **Recall** answers: "Of the real connections, what fraction did the
  segmentation recover?" Low recall means many missed connections
  (typically caused by split errors).
- **F1** is the harmonic mean, balancing both.

### 4.3 Relationship to Error Types

- **Merge errors decrease precision** by creating false edges (neuron A
  is incorrectly merged with B, so all of B's partners appear as A's
  partners too).
- **Split errors decrease recall** by fragmenting neurons so that their
  synapses are attributed to orphan segments rather than the parent neuron.

Because each error type maps onto one of the two numbers, edge metrics tell
you which kind of fix to prioritize. Schneider-Mizell et al. (2016) examine how tracing errors affect measured
connectivity in a *Drosophila* reconstruction.

### 4.4 Limitations

- **Binary:** An edge is either present or absent. This does not capture
  the weight (number of synapses) of each connection.
- **Sensitive to thresholding.** If you only count edges with >= 3
  synapses, you get different results than counting all edges.

---

## 5. Synapse-Centric Precision and Recall

### 5.1 Definition

Similar to edge metrics but evaluated at the individual synapse level.
For each synapse in the ground truth:

- **TP synapse:** The synapse is detected, and both its presynaptic and
  postsynaptic neurons are correctly identified.
- **FP synapse:** A detected synapse that either does not exist in ground
  truth or has an incorrect pre/post assignment.
- **FN synapse:** A ground-truth synapse that is not detected or has
  incorrect assignment.

### 5.2 Why Synapse-Level Matters

Consider two neurons, A and B, connected by 5 synapses. If a boundary
error shifts one synapse from B to a neighboring neuron C:

- **Edge-level:** The A-to-B edge still exists (4 synapses remain), so it
  still counts as a true positive. The weakening goes unrecorded. The only
  edge-level change is a false A-to-C edge, and only if A had no real
  synapse onto C already.
- **Synapse-level:** One FN (the misassigned synapse from A-to-B) and one
  FP (a new false synapse from A-to-C) are recorded.

Synapse-level metrics are more granular and capture errors that edge-level
metrics miss.

### 5.3 The Metric Most Relevant to Connectomics

For most connectome analyses (connection strengths, motifs, circuit models),
synapse-level accuracy is the measure that matters most. If every synapse is
correctly assigned, the graph is correct even where the morphology is not.
Analyses that use morphology, such as where on a dendrite inputs land, still
need the shapes to be right.

---

## 6. Completeness Metrics

### 6.1 Neuron Completeness

What fraction of neurons in the volume are fully reconstructed (no split
errors, no merge errors, correct morphology)?

- **Fully proofread:** Every branch traced and verified.
- **Partially proofread:** Soma and major branches correct, but distal
  tips may have errors.
- **Not proofread:** Automated segmentation only.

### 6.2 Volume Coverage

What fraction of the total volume has been proofread?

- **Exhaustively proofread region:** X % of the volume.
- **Targeted proofreading:** Y neurons fully proofread, covering Z % of
  the neuropil by volume.

### 6.3 Segment Size Distribution

Compare the size distribution of segments before and after proofreading:

- **Before:** Many very small segments (fragments from split errors) and a
  few very large segments (multi-neuron merges).
- **After:** The distribution should more closely match the expected
  biological distribution of neuron sizes for the tissue type.

A shift toward fewer extreme outliers (both small and large) indicates
effective proofreading.

---

## 7. Dashboard Design

### 7.1 What a Proofreading QA Dashboard Should Show

A dashboard lets supervisors and proofreaders watch quality as the
campaign runs. Four panels cover most needs:

**Per-region metrics panel:**
- VI (split and merge components) for each proofread subregion.
- ERL for each subregion.
- Segment size histogram with biological reference distribution overlaid.

**Temporal trends panel:**
- Metrics over time (e.g., ERL vs. cumulative proofreading hours).
- Edits per day, broken down by type (split, merge, other).
- Diminishing returns curve: rate of metric improvement per hour.

**Annotator performance panel:**
- Edits per annotator per session.
- Inter-annotator agreement rate on double-annotated tasks.
- Error introduction rate (edits that were later reversed by reviewers).

**Cost tracking panel:**
- Person-hours spent per region.
- Cost per correction (total hours / total edits).
- Projected time to reach quality targets at current rate.

### 7.2 Instructor Tip

Show students an example dashboard (even a mockup) and ask them to
interpret it. "Region A has VI_merge = 0.01 but VI_split = 0.08. Region B
has VI_merge = 0.06 and VI_split = 0.02. Which region needs more merge
fixes? Which needs more split fixes? Where would you allocate proofreading
effort?"

---

## 8. Worked Example: Computing VI and ERL on a Small Example

### 8.1 Setup

Consider a tiny volume with 100 voxels and 3 ground-truth neurons:
- T1: voxels 1-40 (40 voxels)
- T2: voxels 41-70 (30 voxels)
- T3: voxels 71-100 (30 voxels)

The predicted segmentation has 3 segments:
- S1: voxels 1-50 (T1's 40 voxels + T2's first 10 voxels) -- merge error
- S2: voxels 51-70 (T2's remaining 20 voxels) -- split from T2
- S3: voxels 71-100 (T3's 30 voxels) -- correct

### 8.2 Computing VI

First, compute the overlap matrix r_ij = |S_i intersect T_j| / N:

|       | T1   | T2   | T3   |
|-------|------|------|------|
| S1    | 0.40 | 0.10 | 0.00 |
| S2    | 0.00 | 0.20 | 0.00 |
| S3    | 0.00 | 0.00 | 0.30 |

Marginals: p1=0.50, p2=0.20, p3=0.30; q1=0.40, q2=0.30, q3=0.30.

H(T|S) (merge component):
= -[0.40*log(0.40/0.50) + 0.10*log(0.10/0.50)
  + 0.20*log(0.20/0.20) + 0.30*log(0.30/0.30)]
= -[0.40*log(0.80) + 0.10*log(0.20) + 0.20*log(1.0) + 0.30*log(1.0)]
= -[0.40*(-0.322) + 0.10*(-2.322) + 0 + 0]   (using log base 2)
= -[-0.129 + (-0.232)]
= 0.361 bits

This is nonzero because S1 contains voxels from both T1 and T2 (a merge).

H(S|T) (split component):
= -[0.40*log(0.40/0.40) + 0.10*log(0.10/0.30)
  + 0.20*log(0.20/0.30) + 0.30*log(0.30/0.30)]
= -[0.40*log(1.0) + 0.10*log(0.333) + 0.20*log(0.667) + 0]
= -[0 + 0.10*(-1.585) + 0.20*(-0.585) + 0]
= -[-0.159 + (-0.117)]
= 0.276 bits

This is nonzero because T2 is split across S1 and S2.

VI = 0.361 + 0.276 = 0.637 bits.

Interpretation: the merge component (0.361) is larger than the split
component (0.276), indicating that merge errors are the more serious
problem in this example.

### 8.3 Computing ERL (Simplified)

Suppose the ground-truth skeletons have these path lengths:
- T1: 80 um total cable
- T2: 60 um total cable
- T3: 50 um total cable

**For T1:** tracing along T1's skeleton, the predicted label is S1 the whole
way, so there is no split. But S1 also contains part of T2, so S1 is a merged
segment. Under the definition in §3.2, a run inside a merged segment
contributes zero length. T1's 80 um run counts as **0**.

This is worth pausing on, because it is the most common misreading of ERL.
The trace along T1 looks clean, and T1's own voxels are all correct. ERL
still scores it as zero, because a user who picks up S1 is handed a mixture of
two neurons. A merge penalizes every neuron whose skeleton lies in the merged
segment, which is why ERL weights merges heavily.

**For T2:** the first 10 um of T2's skeleton (the portion inside S1) carries
label S1; the remaining 50 um (inside S2) carries label S2. The label changes at
the 10 um mark, so the skeleton breaks into two runs. The 10 um run lies in the
merged segment S1 and counts as **0**. The 50 um run in S2 is clean: **50 um**.

**For T3:** S3 = T3 exactly. One clean run of **50 um**.

Each run is weighted by its own length, over 190 um of total cable:

    ERL = (80·0 + 10·0 + 50·50 + 50·50) / 190 = 5000 / 190 ≈ 26.3 um

**ERL ≈ 26 um.** For comparison, ignore the merge and count only the split:
the runs are then 80, 10, 50 and 50 um, and

    ERL (splits only) = (80·80 + 10·10 + 50·50 + 50·50) / 190 = 11500 / 190 ≈ 60.5 um

The single split in T2 costs a little; the merge that contaminates S1 costs
much more, because it removes all 90 um of cable in S1 from the tally.

One caveat on that arithmetic. Real implementations sample skeleton nodes
rather than measuring exact run lengths, so a production ERL will differ in
the second digit. The teaching point survives: **which segments are
contaminated, not the volume of misassigned voxels, is what moves the
number.**

### 8.4 Instructor Tip

Walk through this computation on a whiteboard. The numbers are small
enough to compute by hand. The key takeaway: VI told us merge > split, and
ERL agrees, but in different units: the merge cuts the expected error-free
trace from about 60 um to about 26 um. Both are useful; neither tells the
whole story.

---

## 9. When Metrics Disagree

### 9.1 Good VI, Bad ERL

This happens when errors are few but strategically placed -- e.g., a
single split in the middle of a long axon. VI sees one small error on a
volumetric basis (tiny fraction of voxels affected), but ERL sees a
neuron cut in half (every trace along that axon hits the split).

**Which to trust:** If your question is about tracing or morphology, trust
ERL. If your question is about overall volumetric accuracy, trust VI.

### 9.2 Good ERL, Bad VI

This happens when there are many small boundary errors that shift segment
borders by a few voxels each. ERL does not detect these because the
skeleton stays within the correct segment, but VI accumulates the voxel
misassignments across the entire volume.

**Which to trust:** If your question is about synapse assignment or fine
morphology, the boundary errors captured by VI matter. If your question is
about connectivity topology, ERL is more relevant.

### 9.3 Good Voxel Metrics, Bad Edge Metrics

This happens when the segmentation is volumetrically accurate (low VI)
and topologically sound (high ERL), but synapse detection or assignment is
poor. The segments are correct, but the connections between them are not.

**Lesson:** Always report both segmentation metrics (VI, ERL) and
connectivity metrics (edge F1, synapse precision/recall). They measure
different things.

---

## 10. Setting Quality Standards

### 10.1 Published Benchmarks

There is no common table of VI, ERL and edge F1 across the large
connectomes. Each project reports its own quality measures, on its own
evaluation region and ground truth, and often with different metrics:
FlyWire (Dorkenwald et al., 2024), the hemibrain (Scheffer et al., 2020)
and MICrONS (MICrONS Consortium, 2025) are not directly comparable. Before
you quote a number from one of these papers, check what it measures, on
which neurons, and against what ground truth. Do not copy it into a
comparison table with numbers from another project. Challenge leaderboards
such as CREMI's give comparable numbers, but only for their small test
volumes.

### 10.2 Setting Your Own Targets

Targets should come from the scientific question. The numbers below are
starting points we suggest for discussion, not published standards; set
yours from a pilot on your own data:

- **Cell census study:** Needs high completeness but can tolerate moderate
  per-neuron errors. Target: >80 % of neurons identified, ERL > 50 um.
- **Circuit connectivity study:** Needs high edge F1. Target: edge
  F1 > 0.85, synapse precision > 0.90.
- **Fine morphology study:** Needs low VI (especially low boundary error).
  Target: VI < 0.10 bits, with VI_merge < 0.03.

---

## 11. References

- Funke, J., Tschopp, F., Grisaitis, W., Sheridan, A., Singh, C.,
  Saalfeld, S., & Turaga, S. C. (2019). Large scale image segmentation with
  structured loss based deep learning for connectome reconstruction.
  *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 41(7),
  1669-1680. doi:10.1109/TPAMI.2018.2835450. (Preprint: arXiv:1709.02974.)
  Reports results on the CREMI benchmark cited in §2.6.
- Januszewski, M., Kornfeld, J., Li, P. H., Pope, A., Blakely, T.,
  Lindsey, L., Maitin-Shepard, J., Tyka, M., Denk, W., & Jain, V. (2018).
  High-precision automated reconstruction of neurons with flood-filling
  networks. *Nature Methods*, 15(8), 605-610. doi:10.1038/s41592-018-0049-4.
- Meila, M. (2007). Comparing clusterings -- an information based
  distance. *Journal of Multivariate Analysis*, 98(5), 873-895.
  doi:10.1016/j.jmva.2006.11.013.
- Schneider-Mizell, C. M., et al. (2016). Quantitative neuroanatomy for
  connectomics in Drosophila. *eLife*, 5, e12059. doi:10.7554/eLife.12059.
- Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult
  brain. *Nature*, 634, 124-138. doi:10.1038/s41586-024-07558-y.
- MICrONS Consortium, et al. (2025). Functional connectomics spanning
  multiple areas of mouse visual cortex. *Nature*, 640, 435-447.
  doi:10.1038/s41586-025-08790-w. (Preprint: bioRxiv 2021.07.28.454025.)
- Scheffer, L. K., et al. (2020). A connectome and analysis of the adult
  Drosophila central brain. *eLife*, 9, e57443. doi:10.7554/eLife.57443.

---

*End of instructor script: Metrics and Quality Assurance for Connectome Proofreading*
