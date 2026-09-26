---
layout: page
title: "Algorithms and Applications: instructor model responses"
permalink: /teaching/lectures/algorithms-and-applications-answers/
slug: algorithms-and-applications-answers
content_type: delivery
description: "Exact reciprocity calculations, null comparisons and a defensible analysis card."
---

[Learner worksheet]({{ '/teaching/lectures/algorithms-and-applications-activity/' | relative_url }})
· [Lecture plan]({{ '/teaching/lectures/connectomics-03-algorithms-and-applications/' | relative_url }}#teach-a-90-minute-session)

These are **synthetic** worked answers. The census is small enough to enumerate
exactly, so no normal approximation or random rewire sampler is involved.

## 1. Graph construction

At threshold one, all six listed ordered pairs become edges. The reciprocal pairs
are **{A,B} and {A,C}**, so R = **2**. Four of the six directed edges have a reverse:
the reciprocated-edge fraction is **2R/m = 4/6 = 2/3**.

At threshold two, B-to-A and B-to-C disappear. Four edges remain: A-to-B, A-to-C,
C-to-A and C-to-D. Only {A,C} is reciprocal: R = **1**, and 2R/m = **2/4 = 1/2**.
All four nodes remain by the stated inclusion rule. Contact multiplicity has been
used for thresholding, not retained as a weight in the final binary graph.

The edge-fraction convention matches [NetworkX's reciprocity definition](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.reciprocity.reciprocity.html).
A raw reciprocal-pair count is a different statistic; name which one is being used.

## 2. Exact null results

**Threshold one:** the mean is (480 + 2×360 + 3×20)/924 = **15/11 ≈ 1.364**.
Observed/expected is 2/(15/11) = **22/15 ≈ 1.467**. The inclusive upper tail is
(360+20)/924 = **95/231 ≈ 0.411**. The result is above the mean but does **not**
meet the prespecified 0.05 rule.

**Threshold two:** the mean is (240 + 2×15)/495 = **6/11 ≈ 0.545**.
Observed/expected is **11/6 ≈ 1.833**, but the tail is (240+15)/495 =
**17/33 ≈ 0.515**. A larger enrichment ratio does not imply stronger evidence.
The threshold changes m, so a six-edge null would no longer match this four-edge graph.

These tails count all null graphs at least as extreme in the prespecified direction.
They are not probabilities that the null is true. Failure to meet the rule is not
proof of random wiring or absence of reciprocity-related biology.

This null is the directed fixed-edge-count model described by the
[NetworkX G(n,m) documentation](https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.gnm_random_graph.html).
It controls edge count, not each node's degree, spatial opportunity or type composition.
It is deliberately simple for teaching. The supplied data have no positions or types
from which to construct a biologically informed spatial/type null.

## 3. Error scenario

Removing B-to-A from the threshold-one graph leaves **five edges**, one reciprocal
pair {A,C}, and reciprocated-edge fraction **2/5 = 0.4**. This is a **scenario
sensitivity check**, not an uncertainty interval or measured error rate. If computing
a new p-value, compare against the corresponding five-edge null rather than reusing
the six-edge tail. The scenario shows endpoint dependence on one contact; it does
not establish the probability that contact is wrong.

## 4. Example analysis card

**Hypothesis and endpoint:** the synthetic graph has an excess of unordered reciprocal
pairs, R, relative to the specified fixed-edge-count null. The primary construction
uses threshold one. The graph version is `synthetic-four-neuron-graph-v1`, with four
labeled nodes, no self-loops and one edge per qualifying ordered pair.

**Null and decision rule:** all 924 labeled four-node/six-edge directed simple graphs
are equally likely. It would be uninteresting under this null if the observed R were
common among graphs with this edge count. Use the prespecified inclusive upper tail
and 0.05 threshold, not a direction chosen after seeing the result.

**Result:** R = 2 versus a null mean of 15/11; upper tail 95/231. The teaching rule is
not met. Threshold two also fails its rule. Removing the uncertain B-to-A edge lowers
R to 1; this is a single sensitivity scenario with no assigned error probability.

**Provenance:** archive the worksheet or query source, commands and outputs, actual
execution date, Python version and emitted source hash for the code route. Exact
enumeration has no random seed. Do not claim a code run for a paper calculation.

**Non-claim:** this toy result establishes neither functional computation nor a
general rule about biological circuits. A real extension needs validated object and
partner identities, a defined population/boundary, measured error mechanisms and
the covariates required by the intended null. Null constraints follow the scientific
question; adding constraints automatically is not always the right choice.

## Feedback guide

Score **0–2 each** for graph/statistic definitions, null/tail calculation, interpretation,
and provenance/error sensitivity. Two means explicit and correct, one a recoverable
omission, zero absent or contradictory. Proficient means at least 6/8 and no zero
for null/tail reasoning or interpretation. This is a local formative rubric, not a
validated assessment instrument. A well-supported negative result earns full credit.

Teaching material: CC BY-SA 4.0, NeuroTrailblazers.
