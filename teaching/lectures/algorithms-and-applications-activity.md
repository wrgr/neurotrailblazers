---
layout: page
title: "Algorithms and Applications: learner worksheet"
permalink: /teaching/lectures/algorithms-and-applications-activity/
slug: algorithms-and-applications-activity
content_type: delivery
description: "An exact toy-graph exercise in reciprocity, null models and error sensitivity."
---

[Lecture plan and slides]({{ '/teaching/lectures/connectomics-03-algorithms-and-applications/' | relative_url }}#teach-a-90-minute-session)
· [Teaching sequence]({{ '/teaching/sequence/' | relative_url }})

**35 minutes plus peer review.** All nodes, contacts and null results below are
**synthetic teaching data**, not measurements from a biological connectome.
Paper and a calculator suffice. Optional Python 3 code requires no packages or accounts.

## Data and analysis contract

The graph version is `synthetic-four-neuron-graph-v1`. The labeled nodes are A, B,
C and D. Directed contact counts are:

```text
A to B: 3     B to A: 1
A to C: 2     C to A: 2
B to C: 1     C to D: 3
```

All other directed pairs have zero contacts in this invented, fully specified graph.
Keep all four nodes, omit self-loops, and create one binary edge per ordered pair
with at least **one** contact. Do not count parallel edges. A reciprocal pair is an
**unordered** pair with both directed edges present; count it once.

For this exercise, the prespecified question is whether reciprocal pairs are more
numerous than expected under a **uniform fixed-edge-count null**. It preserves the
four labeled nodes and total directed edge count, but not degrees, distances or types.
The teaching decision rule is an **upper-tail probability ≤ 0.05**. Threshold two
is a declared sensitivity analysis, not an opportunity to choose a better p-value.

## 1. Construct and count (10 minutes)

List the binary edges, total edge count, reciprocal pairs, and the fraction of
directed edges that have a reverse edge. Explain why reciprocal-pair count and
reciprocated-edge fraction are different quantities.

Repeat with a minimum of **two** contacts per edge. Which edges disappear? Does
the number of underlying nodes change under the stated inclusion rule?

## 2. Compare to the null (10 minutes)

There are 12 possible directed edges without self-loops. Selecting six produces
924 equally likely labeled graphs under the threshold-one null. Their exact census is:

- 0 reciprocal pairs: 64 graphs.
- 1 reciprocal pair: 480 graphs.
- 2 reciprocal pairs: 360 graphs.
- 3 reciprocal pairs: 20 graphs.

Calculate the mean reciprocal-pair count, observed/expected ratio, and fraction of
graphs with **at least** the observed count. Is “above the mean” sufficient to meet
the decision rule? What biological structure does this null leave uncontrolled?

For threshold two, the four-edge null has 495 graphs: 240 with zero reciprocal
pairs, 240 with one and 15 with two. Recalculate the expected count and upper tail.
Why must the null's edge count change with the graph-construction threshold?

**Optional code:** download [the exact enumeration script]({{ '/assets/worksheets/lectures/algorithms-and-applications-query.py' | relative_url }})
as `algorithms-and-applications-query.py`, then run:

```bash
python3 algorithms-and-applications-query.py --threshold 1
python3 algorithms-and-applications-query.py --threshold 2
```

It enumerates every permitted graph, rather than sampling rewires. Save the command,
output, execution date and source file. The output includes a source hash and Python
version. No random seed or Monte Carlo correction is needed for this exact census.

## 3. Test a possible error (5 minutes)

Suppose B-to-A's single contact is flagged as uncertain. Remove that edge only,
keeping the threshold-one construction otherwise unchanged. Recompute the observed
pair count and reciprocated-edge fraction. Is this one deletion a confidence interval,
a measured merge/split error rate, or a scenario sensitivity check? Explain.

## 4. Write an analysis card (10 minutes)

Include the hypothesis, endpoint, graph version and construction, null constraints,
prespecified rule, result, threshold/error sensitivity and non-claim. Finish:
“This would be uninteresting under my null if ___.” Explain what additional data
would be needed to choose a distance- or type-aware null for a real circuit.

**Peer review:** reproduce the pair count and tail probability from your partner's
card. Check whether their conclusion is narrower than “the brain is random” or
“reciprocity causes computation.” Neither claim follows from this exercise.

**Exit ticket:** finish “My result is conditional on ___; the next measurement that
could change it is ___.” Then, on the study brief you carried from Session 1, write
the null you would use for your own endpoint and one structure it must hold fixed.

[Instructor model responses]({{ '/teaching/lectures/algorithms-and-applications-answers/' | relative_url }})
are public; attempt the activity first. Teaching material: CC BY-SA 4.0, NeuroTrailblazers.
