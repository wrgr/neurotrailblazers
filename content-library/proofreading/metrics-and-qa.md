---
layout: page
title: "Metrics and Quality Assurance for Connectome Proofreading"
permalink: /content-library/proofreading/metrics-and-qa/
description: >
  A comprehensive instructor reference on quantitative metrics for evaluating
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
  - proofreading-fundamentals
  - segmentation-quality
  - data-analysis
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
reference_images:
  - src: /assets/images/content-library/proofreading/metrics-and-qa/metric-formulas.png
    alt: "Mathematical formulas for VI, ERL, edge F1, and synapse F1 metrics"
    caption: "Core proofreading quality metrics with formulas. VI measures information-theoretic distance; ERL measures average error-free path length."
  - src: /assets/images/content-library/proofreading/metrics-and-qa/qa-dashboard-example.png
    alt: "Example QA dashboard showing metric trends over proofreading iterations"
    caption: "QA dashboard tracking ERL improvement over proofreading rounds. Dotted line = release threshold."
  - src: /assets/images/content-library/proofreading/metrics-and-qa/vi-decomposition-diagram.png
    alt: "Diagram showing VI decomposition into merge and split components with example segmentations"
    caption: "VI decomposition: H(T|S) captures merge errors (under-segmentation), H(S|T) captures split errors (over-segmentation)."
combines_with:
  - error-taxonomy
  - proofreading-strategies
  - worked-examples
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

Each metric captures a different aspect of quality. A segmentation can
score well on one metric and poorly on another. Understanding what each
metric measures -- and what it misses -- is essential.

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

Present VI as the "gold standard" metric for segmentation benchmarks
(used in CREMI, SNEMI3D challenges) but explain that its biological
interpretability is limited. Students should be able to compute it and
interpret which component (split vs. merge) is dominant, but should not
rely on it alone.

---

## 3. Expected Run Length (ERL)

### 3.1 Definition

Expected Run Length is the average distance (in micrometers) that you can
trace along a ground-truth neurite before encountering a topological error
(merge or split) in the predicted segmentation. Introduced by Funke et al.
(2017).

### 3.2 Computation

1. Take the ground-truth skeleton of each neuron.
2. Sample random paths along the skeleton (e.g., random walks from random
   starting nodes).
3. For each path, walk along it and check the predicted segmentation at
   each node:
   - If the predicted label changes (but the ground-truth neuron has not
     ended), you have hit a **split error**. Record the distance traveled.
   - If a different ground-truth neuron shares the same predicted label,
     you have detected a **merge error**. Record the distance traveled.
4. ERL is the average of all recorded distances, weighted by path length.

### 3.3 Intuition

ERL answers the practical question: "If I pick a random point on a random
neuron and start tracing, how far can I go before the segmentation
misleads me?"

- **ERL = 10 um** means errors are very dense; you hit one every 10 um
  of tracing. The segmentation is barely usable without heavy proofreading.
- **ERL = 100 um** means you can trace typical dendritic branches
  end-to-end without encountering an error. Good for many analyses.
- **ERL = 1,000 um** means most neurons with arbors under 1 mm are fully
  correct. Excellent quality.

### 3.4 Properties

- **Biologically interpretable.** Researchers can immediately assess
  whether ERL is sufficient for their specific analysis.
- **Separable.** ERL can be decomposed into merge-ERL and split-ERL to
  diagnose the dominant error type.
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

This direct mapping to error types makes edge metrics highly actionable.
Cite Schneider-Mizell et al. (2016) for the framework.

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

- **Edge-level:** The A-to-B edge still exists (4 synapses remain). No
  edge-level error is detected.
- **Synapse-level:** One FN (the misassigned synapse from A-to-B) and one
  FP (a new false synapse from A-to-C) are recorded.

Synapse-level metrics are more granular and capture errors that edge-level
metrics miss.

### 5.3 The Metric Most Relevant to Connectomics

For most connectome analyses -- computing connection strengths, identifying
motifs, modeling circuit function -- synapse-level accuracy is the
ultimate measure of quality. If every synapse is correctly assigned, the
connectome is correct regardless of any morphological imperfections.

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

A well-designed dashboard enables supervisors and proofreaders to monitor
quality in real time. Essential components:

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

For T1: S1 contains all of T1, and no other ground-truth neuron shares
S1's label on T1's skeleton. ERL contribution from T1 = 80 um (no error
encountered along T1's skeleton within S1, because S1 only has merge
contamination from T2 voxels, which are not on T1's skeleton path).

Wait -- the merge error means S1 also contains part of T2. If we trace
along T1's skeleton, the predicted label is S1 the entire way. Since no
other neuron's skeleton overlaps with this path in the prediction, there
is no merge error detected from T1's perspective.

For T2: the first 10 um of T2's skeleton (the portion in S1) has label
S1. Then the remaining 50 um (in S2) has label S2. There is a split error
at the 10 um mark. So ERL contribution from T2: two runs of 10 um and
50 um. However, the 10 um portion in S1 also constitutes a merge error
(S1 contains T1 voxels too), so this run is terminated by both a split
and a merge.

For T3: S3 = T3 exactly. ERL contribution = 50 um.

Weighted average ERL = (80 + 10 + 50 + 50) / 4 paths... (The precise
calculation depends on the sampling method, but the key point is that T2's
fragmentation reduces the average.)

**Simplified ERL estimate:** approximately 47 um (indicating that on
average you can trace ~47 um before hitting an error).

### 8.4 Instructor Tip

Walk through this computation on a whiteboard. The numbers are small
enough to compute by hand. The key takeaway: VI told us merge > split,
while ERL told us that the practical tracing impact is moderate (47 um).
Both are useful; neither tells the whole story.

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

| Dataset | VI (bits) | ERL (um) | Edge F1 | Reference |
|---|---|---|---|---|
| CREMI challenge (best) | ~0.10 | ~150 | N/A | CREMI leaderboard |
| FlyWire (proofread) | ~0.05 | >200 | ~0.85 | Dorkenwald et al. (2024) |
| MICrONS (proofread) | ~0.08 | ~120 | ~0.80 | MICrONS Consortium (2021) |
| Hemibrain (proofread) | ~0.06 | ~180 | ~0.82 | Scheffer et al. (2020) |

These numbers are approximate and depend on the evaluation region, ground
truth quality, and computation details. They provide rough targets for
new projects.

### 10.2 Setting Your Own Targets

Targets should be driven by the scientific question:

- **Cell census study:** Needs high completeness but can tolerate moderate
  per-neuron errors. Target: >80 % of neurons identified, ERL > 50 um.
- **Circuit connectivity study:** Needs high edge F1. Target: edge
  F1 > 0.85, synapse precision > 0.90.
- **Fine morphology study:** Needs low VI (especially low boundary error).
  Target: VI < 0.10 bits, with VI_merge < 0.03.

---

## 11. References

- Funke, J., Tschopp, F., Grisaitis, W., Sherber, A., Singh, C.,
  Saalfeld, S., & Turaga, S. C. (2017). A deep structured learning
  approach towards automating connectome reconstruction from 3D electron
  microscopy data. *arXiv preprint arXiv:1709.02974*.
- Meila, M. (2007). Comparing clusterings -- an information based
  distance. *Journal of Multivariate Analysis*, 98(5), 873-895.
- Schneider-Mizell, C. M., et al. (2016). Quantitative neuroanatomy for
  connectomics in Drosophila. *eLife*, 5, e12059.
- Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult
  brain. *Nature*, 634, 124-138.
- MICrONS Consortium. (2021). Functional connectomics spanning multiple
  areas of mouse visual cortex. *bioRxiv*, 2021.07.28.454025.
- Scheffer, L. K., et al. (2020). A connectome and analysis of the adult
  Drosophila central brain. *eLife*, 9, e57443.

---

*End of instructor script: Metrics and Quality Assurance for Connectome Proofreading*
