---
layout: page
title: "Module 08: model responses"
permalink: /teaching/answers/module08/
slug: module-answers-08
content_type: delivery
description: "Three exemplar hypothesis sheets for the Module 08 MICrONS scenario, peer critique and revisions, and the supported claim, non-claim and confound for the three pre-computed results in the interpretation workshop."
---

[Learner worksheet]({{ '/assets/worksheets/module08/module08-activity.md' | relative_url }}) · [Session kit]({{ '/teaching/sessions/module08/' | relative_url }}) · [Module page]({{ '/modules/module08/' | relative_url }}) · [All model responses]({{ '/teaching/answers/' | relative_url }})

This page answers every section of the Module 08 worksheet in order. The studio asks
for three hypothesis designs, not results, so the sheets below contain no counts,
ratios or p-values from MICrONS. They name a dataset version, a metric, a null and a
boundary, and they predict directions, which is all a design can do before the query
runs. The sheets are one **invented learner's** work at the kit's **Strong** level. The
interpretation workshop uses three pre-computed results that already exist on this
site; their numbers are quoted from those pages, and all three are synthetic or
illustrative by their own statement. This page is public and suitable for formative
assessment.

## Before you start

Modules 01–07 supply the vocabulary: synapse table, materialization version, merge and
split, edge threshold. A learner who has not met null models should read the null
models section of [Motif analysis]({{ '/content-library/connectomics/motif-analysis/' | relative_url }})
first, as the pre-class preparation asks.

## Questions this module answers

1. **What makes a connectomics hypothesis testable?** A structural feature that can
   be counted in a stated version of the data, a comparison that says what count
   would be uninteresting, and a boundary that says what the result would not show.
2. **Which null model supports this claim?** The one that preserves everything the
   claim is not about. If the claim is “beyond what degree and distance explain,” the
   null preserves degree and distance; a weaker null tests a different claim.

## The task

The scenario: a study of feedforward and feedback connectivity in mouse visual cortex
using MICrONS. All three sheets use the same release, so the version line is stated
once and repeated on each sheet.

**Dataset version, all sheets.** `minnie65_public`, materialization version **1300**,
with the cell-type and proofreading-status tables queried at the same version and the
query date recorded. The exemplar picks 1300 because the MICrONS team designates it
(with 943) as a long-term analysis version that stays available; a learner who queried
another version writes that one. What matters for the rubric is that the version is
on the sheet and that every table comes from the same one.

### Hypothesis sheet 1: feedforward (laminar)

- **Hypothesis.** In V1 within `minnie65_public` v1300, among excitatory neurons whose
  axons are marked as proofread and whose somata lie in L4 or L2/3, the connection
  probability from L4 excitatory cells to L2/3 pyramidal cells is higher than the
  probability in the reverse direction, among the same unordered pairs.
- **Metric.** Per ordered class pair, the fraction of eligible pairs connected by at
  least two synapses (primary) and at least one (sensitivity). Scope: per population,
  matching a population-level claim.
- **Null.** A direction-swap null. Take every unordered L4–L2/3 pair that is connected
  in either direction, keep the pair (and so its distance and the fact that the two
  arbors overlap), and assign the direction of each connection by a fair coin. Repeat
  10,000 times and record the L4-to-L2/3 fraction each time. *Uninteresting
  explanation written first:* “given which pairs touch, the two directions are equally
  likely.”
- **Analysis code outline.**
  1. Query the cell-type table at v1300; keep L4 excitatory and L2/3 pyramidal cells
     with somata inside the V1 part of the volume.
  2. Query the proofreading-status table at the same version; keep cells whose axon
     is marked extended, and record how many were dropped.
  3. Query the synapse table for pre and post both in the kept set; collapse to
     ordered pairs with synapse counts.
  4. Build the eligible-pair list; compute the two directional fractions at
     thresholds 2 and 1.
  5. Run the direction-swap null; report observed difference, null mean and sd, and
     the upper-tail permutation p.
- **Supported claim, if the difference clears the null.** Among proofread L4 and L2/3
  excitatory cells in this volume at this version, connections run L4-to-L2/3 more
  often than the reverse, beyond what an even split of directions among touching
  pairs would give.
- **Explicit non-claim.** Nothing about signal flow, timing or “feedforward
  processing.” Direction of a synapse is not direction of information at any moment.
  The result also says nothing about pairs whose axons were not proofread.

### Hypothesis sheet 2: feedback (inter-areal, compartment targeting)

- **Hypothesis.** In `minnie65_public` v1300, synapses onto V1 L2/3 pyramidal cells
  from excitatory neurons whose somata lie in the higher visual area part of the
  volume (the LM, AL and RL portion) land on the apical tuft more often than the
  target cells' overall input distribution across compartments predicts.
- **Metric.** The fraction of feedback synapses per postsynaptic compartment class
  (apical tuft, apical trunk and obliques, basal dendrite, soma), on cells whose
  dendrites are proofread and whose compartments are labeled. Scope: per synapse,
  matching a placement claim.
- **Null.** A placement null. For each target cell, assign each feedback synapse to a
  compartment with probability equal to that cell's share of all synaptic input in
  that compartment, from every presynaptic source. Repeat 10,000 times.
  *Uninteresting explanation:* “feedback axons put synapses where the cell receives
  most of its input anyway.”
- **Analysis code outline.**
  1. Cell-type table at v1300: L2/3 pyramidal cells in V1 with proofread dendrites;
     excitatory cells with somata in the higher-area portion and proofread axons.
  2. Synapse table: all inputs to the target cells (for the null) and the subset
     whose presynaptic cell is in the higher-area set (for the test).
  3. Compartment label per synapse from the skeleton annotation at the same version.
  4. Observed tuft fraction; null distribution; effect size as observed over
     expected with the null's 2.5–97.5 percentile range; upper-tail p.
- **Supported claim, if the tuft fraction clears the null.** In this volume at this
  version, higher-area excitatory axons that reach V1 place a larger share of their
  synapses on L2/3 apical tufts than the targets' input distribution predicts.
- **Explicit non-claim.** Nothing about what feedback does (gain, attention,
  prediction). Nothing about feedback axons whose somata lie outside the volume,
  which this design excludes by construction because a 1 mm³ block cannot say
  which cell they come from.

### Hypothesis sheet 3: reciprocal (two nulls)

- **Hypothesis.** In V1 within `minnie65_public` v1300, among proofread L2/3
  pyramidal cells, the number of reciprocally connected pairs exceeds the expectation
  under a null that preserves each cell's in- and out-degree and the empirical
  connection-probability-versus-distance curve.
- **Metric.** The count of unordered pairs connected in both directions, at a
  threshold of at least one synapse per direction (primary) and at least two
  (sensitivity). Scope: per population.
- **Nulls, two of different stringency.** (a) Degree-preserving rewiring, 10,000
  samples. (b) Degree- and distance-preserving rewiring, in which a swap is accepted
  only if it keeps the binned soma-distance histogram of the edge list. *Uninteresting
  explanations:* under (a), “hubs connect both ways by arithmetic”; under (b), that
  plus “reciprocal partners are near neighbors, and near neighbors connect more.”
- **Predicted movement.** The enrichment ratio falls from (a) to (b), because
  reciprocal partners are disproportionately close, so a null that keeps distance
  expects more reciprocal pairs. If the ratio survives (b) above 1 with the upper
  tail below the corrected alpha, the claim is supported; if it survives (a) only,
  the finding is proximity, not reciprocity.
- **Analysis code outline.** As sheet 1, steps 1–3, restricted to L2/3 pyramidal
  cells; then the reciprocal count, the two rewiring nulls with the bin width stated
  (25 µm), and a table with observed, null mean, sd, ratio and p under each null.
- **Supported claim, if (b) is cleared.** Reciprocal L2/3 pyramidal pairs in this
  volume at this version are more frequent than degree and soma distance predict.
- **Explicit non-claim.** Not that reciprocal pairs amplify activity, and not that
  the excess is a wiring “rule”: a distance null on soma position does not control
  for axon–dendrite overlap, which is the next confound to test.

### Test count and correction, all three sheets

Seven p-values are planned: sheets 1 and 2 at two thresholds each (four), sheet 3 at
two thresholds under null (b) (two), and sheet 3 under null (a) as the comparison
(one). The family is the seven; Holm's step-down procedure at alpha 0.05 is applied
across all of them, and the sheet commits that every one of the seven is reported
whichever way it comes out. Any threshold or class definition tried while writing the
query and then dropped is logged and counted as an extra test.

### Peer critique notes

Two substantive comments per hypothesis, as a partner wrote them:

- **Sheet 1.** (i) The direction-swap null keeps which pairs touch but not *where*
  their axons run; if L4 axons ascend into L2/3 more than L2/3 axons descend, the
  asymmetry is arbor geometry, not a wiring preference. Name that confound and say
  which null would test it. (ii) “Proofread axon” is a status label at one version;
  say how many cells the filter drops per class, or the two classes may differ in
  completeness rather than in wiring.
- **Sheet 2.** (i) The placement null uses the target's total input. If higher-area
  axons run mainly through L1, where the tufts are, a tuft excess could be axon
  geometry; a null weighted by compartment membrane area would ask a different
  question. Say which one you mean, and name the geometry confound. (ii)
  Compartment labels are automated; report their accuracy or hand-check a sample.
- **Sheet 3.** (i) A soma-distance null under-controls for cells whose arbors are
  truncated at the volume boundary; exclude or flag cells within a stated distance of
  the boundary. (ii) The 25 µm bin width is a free parameter; pre-register it, and
  report the result at one other width so the reader can see it does not drive the
  answer.

### Revised hypotheses

The revision keeps all three hypotheses and adds what the critique asked for:

- **Sheet 1** now states the arbor-geometry confound in the non-claim and adds a
  planned follow-up: an overlap-conditioned null that keeps, for each pair, the
  volume of overlap between the presynaptic axon and the postsynaptic dendrite. It
  reports the number of cells dropped by the proofreading filter per class.
- **Sheet 2** names its null as the input-weighted one, states the membrane-area
  alternative as a sensitivity run, and adds a 100-synapse hand-check of compartment
  labels with its agreement rate reported.
- **Sheet 3** adds a boundary exclusion (cells with somata within 50 µm of any volume
  face, with the number excluded reported) and a second bin width of 50 µm as a
  declared sensitivity run. Both additions are counted in the test tally, which rises
  from seven to nine, and Holm is applied across nine.

### What good looks like

- **Strong:** the uninteresting explanation is a sentence in plain words before the
  null is named; the metric's scope matches the claim (per pair, per synapse, per
  population); the non-claim says something the supported claim does not; the test
  tally includes the abandoned tries.
- **Weak:** a hypothesis that names the dataset and a “connectivity pattern” but no
  count; “degree-preserving null” written as a default with no sentence about what
  it treats as uninteresting; a non-claim that restates the claim with “not”; a
  functional phrase (“feedforward processing,” “feedback gain”) inside the
  hypothesis rather than in the interpretation.

## Working checklist

Define question and estimand: the hypothesis line and metric on each sheet. Choose
measurable outputs: the metric lines. Select the null: the null lines, with the
uninteresting explanation. Test and interpret: the code outlines and the planned
table (observed, null mean, sd, ratio, p). Document supported versus unsupported
claims: the supported-claim and non-claim lines and the revision notes.

## Evidence and reasoning

| # | Claim | Evidence | Limitation / what would change my mind |
|---|---|---|---|
| 1 | The three hypotheses are testable from the sheets alone. | Each names a version, a count, a comparison and a decision rule; a partner could write the query from the outline. | Compartment labels and proofreading status are release-specific tables. If either is absent at v1300 for the cells needed, sheet 2 and the filters in 1 and 3 must change. |
| 2 | Sheet 3's enrichment will fall when distance is added to the null. | The direction of the movement follows from Unit 09's worked reciprocity example and from the kit graphs' construction; only the direction is predicted, not the size. | If reciprocal partners in this population are not closer than average, the ratio would not move. That is itself a result. |
| 3 | Seven (revised: nine) tests is the honest family. | The sheets list every planned p-value, including the comparison null and the sensitivity thresholds. | Query drafting usually tries more variants than planned. The log of abandoned tries decides the real count. |

**Confidence:** Medium. The designs rest on one line of evidence, the published
description of what the release contains, and none has been run.

**Alternative considered and rejected:** an Erdős–Rényi null for sheet 3 because it is
one line of code. Rejected because degree heterogeneity alone makes reciprocity look
enriched, so the test would not distinguish a wiring preference from hubs.

## Misconception self-check

Feedback for each:

- **A significant result against a random-graph null is evidence of biological
  structure.** Ask: “What would the same count look like under a degree-preserving
  null?” Point to Unit 09's example: 2.9x under Erdős–Rényi, 1.4x under degree, 1.14x
  under degree and distance, on the same data.
- **The statistical test is the scientific step, when the choice of null model is.**
  Ask the learner to read their uninteresting-explanation sentence aloud. If they
  cannot write it, they do not yet know what they are testing.
- **A metric can be chosen after seeing the data without cost to the inference.**
  Ask: “Which of your metrics was fixed before the first query, and where is that
  written?” A sheet dated before the query is the answer.
- **Reporting the tests that worked is sufficient without reporting how many were
  run.** Ask for the tally, including the thresholds tried while drafting. The
  correction depends on that number, and so does the reader's trust.

## Session timing (facilitator reference)

This section has no learner task. Two blocks of the run of show have answers a
facilitator may want in hand.

**00:00–08:00, framing.** Of the four example hypotheses, the first two are testable:
each names a dataset region, a countable feature, a null and a boundary sentence. The
third (“we will study connectivity patterns in visual cortex”) has no endpoint and no
null. The fourth (“this circuit computes contrast normalization”) is a functional
claim with no structural endpoint; it belongs in an interpretation section as “would
be consistent with,” after a structural test.

**34:00–46:00, interpretation workshop.** For each pre-computed result, a supported
claim, an explicit non-claim and one confound. The numbers are quoted from the pages
named; the first two pages state that their numbers are illustrative.

1. *The module's worked example, the feed-forward loop.* Observed 84 loops in a
   300-neuron subgraph; expected 22 under Erdős–Rényi, 51 under degree-preserving
   (z = 3.7), 78 under a cell-type-stratified null (z = 0.7).
   **Supported:** feed-forward loop frequency in this subgraph is consistent with its
   degree distribution and cell-type composition. **Non-claim:** the circuit does not
   lack temporal filtering, and enrichment within a single cell type is not ruled out.
   **Confound:** the result was one of 16 triad classes examined; even the z = 3.7
   needed correction across 16 correlated tests.
2. *Unit 09 §2, reciprocity under three nulls.* 100 neurons, 1,200 edges, 210
   reciprocal pairs; 2.9x under Erdős–Rényi, 1.4x under degree-preserving (z = 5.0),
   1.14x under degree and distance (z = 1.8, p about 0.07).
   **Supported:** reciprocity is consistent with what degree and spatial proximity
   predict. **Non-claim:** reciprocal wiring is not shown to be absent; the test
   lacks power to exclude a small excess. **Confound:** the distance curve is
   estimated from the same graph, and estimation error in the curve propagates into
   the null.
3. *The Algorithms and Applications worksheet, exact enumeration.* Four nodes, six
   edges, 2 reciprocal pairs observed; null mean 15/11 (about 1.364) over 924 equally
   likely graphs; inclusive upper tail 95/231 (about 0.411); at threshold two,
   1 pair against a mean of 6/11 with tail 17/33.
   **Supported:** the observed count is above the null mean but is common under a
   fixed-edge-count null; the prespecified 0.05 rule is not met at either threshold.
   **Non-claim:** the wiring is not shown to be random, and nothing follows about
   computation. **Confound:** the null preserves only the edge count, not degree,
   distance or type; with four nodes no stronger null can be built.

The pattern across all three: the supported claim shrinks as the null strengthens,
and the non-claim is not the negation of the claim.

## Rubric

A self-assessment that matches this exemplar:

- **Strongest part:** sheet 3, because it evaluates the same count under two nulls
  and predicts which way the ratio moves before the query runs.
- **Weakest part:** sheet 2 depends on compartment labels whose accuracy is not yet
  known for this version. **Next action:** hand-check 100 synapses before any tuft
  fraction is computed, and report the agreement rate on the sheet.

## Exit prompt

One claim and one explicit non-claim from the same test outcome, using sheet 3 if
null (b) is cleared:

> **Claim:** among proofread L2/3 pyramidal cells in V1 at `minnie65_public` v1300,
> reciprocally connected pairs are more frequent than a null preserving each cell's
> degree and the soma-distance dependence of connection probability predicts.
> **Non-claim:** this does not show that reciprocal pairs amplify each other's
> activity, and it does not show a wiring rule beyond what axon–dendrite overlap,
> which the null did not control, could produce.

If null (b) is not cleared, the pair becomes: **Claim:** reciprocity is consistent
with degree and proximity. **Non-claim:** reciprocal wiring is not shown to be absent.

## Peer review (swap worksheets)

A reviewer should check that each sheet's non-claim differs in content from its claim
and that the test tally includes the sensitivity runs. A good question: “If sheet 1's
asymmetry vanished under an overlap-conditioned null, what would you conclude, and is
that written on the sheet now?”

## Feedback guide

This key follows the kit's own tiers.

- **Minimum pass:** at least two of three hypotheses name a measurable structural
  endpoint, a specific comparison and a null a reader could run from the sheet; each
  states a supported claim and a non-claim that differ in content; the metric's scope
  matches the hypothesis; the dataset version is stated for each.
- **Strong performance:** the null's uninteresting explanation is written in words
  before the test; at least one hypothesis is evaluated under two nulls with a
  predicted movement; the plan states the test count and the correction, including
  tests that may go unreported; the peer critique names a real weakness per
  hypothesis and the revision responds to it.
- **Common failure to flag:** a vague hypothesis without an endpoint; a missing or
  default null (Erdős–Rényi where degree structure obviously matters); a functional
  claim stated as the hypothesis rather than as an interpretation boundary.

Do not reward a sheet that names a version number but pulls its cell-type table from
a different one. Do not reward a prediction of the effect's size; a design can predict
direction only. Do not reward a non-claim that is the claim with “not” in front of it.
Do reward a learner whose revision changes the hypothesis in response to a critique
rather than adding a sentence of defense. This is a local teaching rubric, not a
validated assessment instrument.

See [Technical Unit 09]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
for the null-model table and [Graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }})
for the construction choices each sheet commits to. Teaching material: CC BY 4.0,
NeuroTrailblazers.
