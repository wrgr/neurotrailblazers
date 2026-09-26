---
marp: true
theme: neurotrailblazers
paginate: true
footer: "Module 08 · NeuroTrailblazers"
title: "Module 08: Hypothesis Testing in Connectomics"
---

<!-- _class: title nanoscale -->
<img class="cover-image" src="../../../../assets/images/content-library/case-studies/h01/10b-segmentation-overlay.jpg" alt="H01 electron microscopy with object segmentation and original 2 µm scale bar">
<span class="eyebrow">NeuroTrailblazers · Module 08</span>

# Hypothesis Testing in Connectomics
Teaching Deck

<p class="cover-label">Human cortex · H01<br>Object segmentation over electron microscopy</p>
<p class="source">H01 release · Lichtman Lab / Harvard &amp; Connectomics at Google · CC BY 4.0<br>Shapson-Coe et al. (2024) · doi:10.1126/science.adk4858</p>

---

## Learning Objectives
- Translate biological questions into testable hypotheses
- Select metrics and null models for structural data
- Interpret outcomes with uncertainty discipline
- Separate supported claims from exploratory signals

---

## Session Outcomes
- Learners can complete the module capability target.
- Learners can produce one evidence-backed artifact.
- Learners can state one limitation or uncertainty.

---

## Capability Target
Design one hypothesis test with metric, null model, and interpretation boundary statement.

---

## Concept Focus
### 1) What makes a connectomics hypothesis testable?
A testable connectomics hypothesis must specify: (a) a structural feature that can be measured from the reconstructed data (e.g., synapse count, motif frequency, path length), (b) a comparison or null expectation (e.g., "more frequent than in a degree-preserving random graph"), and (c) an interpretation boundary (what the result does and does not prove). Many fascinating biological questions ("How does the cortex generate consciousness?") are not directly testable with connectomics because they lack measurable structural endpoints.

---

## Core Workflow
- Define question and estimand: what structural feature would constrain or inform the biological question?
- Choose measurable outputs: specific metric(s) computed from the connectome graph.
- Select null model: the most stringent null relevant to the claim.
- Test and interpret results: compute metric, compare to null distribution, compute z-score and p-value.
- Document supported vs unsupported claims: what the result proves, what it doesn't, and what additional evidence would be needed.

---

## Run of Show (60 min)
- 00:00-08:00 | Framing: good vs bad hypotheses
- 08:00-20:00 | Hypothesis drafting
- 20:00-34:00 | Metric and null model selection
- 34:00-46:00 | Interpretation workshop
- 46:00-60:00 | Competency check

<!--
Pre-class preparation (10 min async)
  Read the motif analysis content library entry (focus on null models section)
  Draft one biological question you'd like to test with connectomics data
  Minute-by-minute plan

00:00-08:00 | Framing: good vs bad hypotheses
  Show 4 example hypotheses (2 good, 2 poor). Group identifies which are testable and why:
  "In this L2/3 subgraph, reciprocal pyramidal-pyramidal pairs are more frequent than under a degree-preserving null. This would support local recurrent excitation but would not show that it amplifies activity in vivo."
  "Basket-cell synapses onto pyramidal cells land on the soma and proximal dendrite more often than a placement null weighted by membrane area predicts."
  "We will study connectivity patterns in visual cortex." (no endpoint, no null)
  "This circuit computes contrast normalization." (a functional claim with no structural endpoint)
  Key criteria: measurable endpoint, specified null, interpretation boundary.

08:00-20:00 | Hypothesis drafting
  Each learner drafts a hypothesis using a template:
  "In [dataset/region], [structural feature] is [comparison] compared to [null model]."
  "This would support [interpretation] but would NOT prove [over-claim]."
  Peer review: partner evaluates whether the hypothesis is testable.

20:00-34:00 | Metric and null model selection
  For each drafted hypothesis, select the appropriate metric and null model.
  Instructor walks through one example end-to-end: hypothesis → metric → null → expected result → interpretation.
  Discussion: "What happens if you use the wrong null model?" Show how the same data looks significant or non-significant depending on null choice.

34:00-46:00 | Interpretation workshop
  Present 3 pre-computed results: the feed-forward loop in this module's worked example, the reciprocity example under three nulls in [Technical Unit 09](/technical-training/09-connectome-analysis-neuroai/) (section 2), and the exact-enumeration result on the [Algorithms and Applications worksheet](/teaching/lectures/algorithms-and-applications-activity/). For each, learners write:
  Supported claim (what the data shows)
  Explicit non-claim (what the data does NOT show)
  One confound that could explain the result
  Group discussion of each result.

46:00-60:00 | Competency check
  Each learner submits their final hypothesis with metric, null model, and interpretation boundaries.
  Exit ticket: "Write one claim and one explicit non-claim from the same test outcome."
-->

---

## Misconceptions to Watch
- **Misconception guardrail:** a significant result against a random-graph null is evidence of biological structure.
- **Misconception guardrail:** the statistical test is the scientific step, when the choice of null model is.
- **Misconception guardrail:** a metric can be chosen after seeing the data without cost to the inference.
- **Misconception guardrail:** reporting the tests that worked is sufficient without reporting how many were run.

---

## Studio Activity
**Scenario:** Your lab is planning a study of feedforward vs feedback connectivity in mouse visual cortex using the MICrONS dataset. You need to design three testable hypotheses about the circuit architecture.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
**Minimum pass**

- At least 2 of 3 hypotheses name a measurable structural endpoint, a specific comparison, and a null model — a reader could run the test from the sheet alone.
- Each testable hypothesis states one supported claim and one explicit non-claim, and the two are different in content, not restatements.
- The metric's scope (local vs global, per-pair vs per-population) matches the scope of the hypothesis it tests.
- The required dataset version is stated for each hypothesis.

---

## Assessment Rubric
**Strong performance**

- Null model choice is justified in words: the "uninteresting explanation" the null encodes is written out before the test is described.
- At least one hypothesis is evaluated under two nulls of different stringency, with a prediction of how the effect size should move.
- The analysis plan states how many tests will be run and names the correction, including tests that may go unreported.
- Peer critique identifies at least one genuine weakness per hypothesis (a confound, an over-claim, a metric mismatch), and the revision visibly responds to it.

---

## Assessment Rubric
**Common failure to flag**

- Vague hypothesis without measurable endpoint ("we will study connectivity patterns").
- Missing or default null model — Erdos-Renyi used where degree structure obviously matters.
- A functional claim ("this circuit computes X") stated as the hypothesis rather than as an interpretation boundary.

---

## Exit Ticket
Write one claim and one explicit non-claim from the same test outcome.

---

## References (Instructor)
- Use module references listed on the module page.

---

## Teaching Materials
- Module page: /modules/module08/
- Session kit: /teaching/sessions/module08/
- Worksheet: /assets/worksheets/module08/module08-activity.md
