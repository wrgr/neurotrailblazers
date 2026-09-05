# Module 08 Activity Worksheet

**Module:** Module 08: Hypothesis Testing in Connectomics  
**Duration:** 4 hours  
*Generated from the module page. Edit `modules/module08.md`, not this file.*

---

## Capability target

Design one hypothesis test with metric, null model, and interpretation boundary statement.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Modules 01-07

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. What makes a connectomics hypothesis testable?
   - Your answer:
2. Which null model supports this claim?
   - Your answer:

---

## The task

**Scenario:** Your lab is planning a study of feedforward vs feedback connectivity in mouse visual cortex using the MICrONS dataset. You need to design three testable hypotheses about the circuit architecture.

1. Draft 3 hypotheses (one about feedforward connections, one about feedback connections, one about reciprocal connections).
2. For each: specify the metric, null model, required dataset version, and analysis code outline.
3. For each: write the supported claim and explicit non-claim.
4. Exchange with a partner. Critique their null model choices and interpretation boundaries.
5. Revise based on peer feedback.

### What you hand in

- 3 hypothesis sheets (hypothesis, metric, null, interpretation boundary, non-claim)
- Peer critique notes (minimum 2 substantive comments per hypothesis)
- Revised hypotheses incorporating feedback

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Define question and estimand: what structural feature would constrain or inform the biological question?
- [ ] Choose measurable outputs: specific metric(s) computed from the connectome graph.
- [ ] Select null model: the most stringent null relevant to the claim.
- [ ] Test and interpret results: compute metric, compare to null distribution, compute z-score and p-value.
- [ ] Document supported vs unsupported claims: what the result proves, what it doesn't, and what additional evidence would be needed.

---

## Evidence and reasoning

Fill one row per claim you make in your artifact. A claim without a limitation is
not finished.

| # | Claim | Evidence (what specifically) | Limitation / what would change my mind |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Confidence.** For your main claim, mark one and say why:

- [ ] **High** — two or more independent lines of evidence agree
- [ ] **Medium** — one strong line, or several that share a weakness
- [ ] **Uncertain** — the deciding evidence is not available to me

Why:

**One alternative I considered and rejected**, and the reason:

---

## Misconception self-check

These are the errors this module is designed to prevent. Confirm you did not make
them, or note where you nearly did:

- [ ] I did not assume: A significant result against a random-graph null is evidence of biological structure.
- [ ] I did not assume: The statistical test is the scientific step, when the choice of null model is.
- [ ] I did not assume: A metric can be chosen after seeing the data without cost to the inference.
- [ ] I did not assume: Reporting the tests that worked is sufficient without reporting how many were run.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| 00:00-08:00 | Framing: good vs bad hypotheses |
| 08:00-20:00 | Hypothesis drafting |
| 20:00-34:00 | Metric and null model selection |
| 34:00-46:00 | Interpretation workshop |
| 46:00-60:00 | Competency check |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass**
  - At least 2 of 3 hypotheses name a measurable structural endpoint, a specific comparison, and a null model — a reader could run the test from the sheet alone.
  - Each testable hypothesis states one supported claim and one explicit non-claim, and the two are different in content, not restatements.
  - The metric's scope (local vs global, per-pair vs per-population) matches the scope of the hypothesis it tests.
  - The required dataset version is stated for each hypothesis.
- **Strong performance**
  - Null model choice is justified in words: the "uninteresting explanation" the null encodes is written out before the test is described.
  - At least one hypothesis is evaluated under two nulls of different stringency, with a prediction of how the effect size should move.
  - The analysis plan states how many tests will be run and names the correction, including tests that may go unreported.
  - Peer critique identifies at least one genuine weakness per hypothesis (a confound, an over-claim, a metric mismatch), and the revision visibly responds to it.
- **Common failure to flag**
  - Vague hypothesis without measurable endpoint ("we will study connectivity patterns").
  - Missing or default null model — Erdos-Renyi used where degree structure obviously matters.
  - A functional claim ("this circuit computes X") stated as the hypothesis rather than as an interpretation boundary.

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

Write one claim and one explicit non-claim from the same test outcome.

**Your answer:**

---

## Peer review (swap worksheets)

Reviewing someone else's reasoning is the fastest way to see the gaps in your own.
Assess the **evidence quality**, not whether you agree with the conclusion.

- Is every claim paired with specific evidence?
- Is at least one limitation stated, and is it a real one?
- Is the confidence level justified by the number of *independent* evidence lines?
- One thing this person did better than me:
- One question I would ask them:

---

*Module page: `/modules/module08/` · Slides: `/modules/slides/module08/` · [Facilitator guide](/teaching/facilitator-guide/)*
