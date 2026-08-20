# Module 13 Activity Worksheet

**Module:** Module 13: Machine Learning in Neuroscience  
**Duration:** 4-5 hours  
*Generated from the module page. Edit `modules/module13.md`, not this file.*

---

## Capability target

Design and critique an ML analysis pipeline for connectomics that includes feature rationale, evaluation plan, leakage controls, and interpretation limits.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Basic scikit-learn workflow familiarity
- [ ] Feature matrix handling in Python

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. Which ML task framing matches this connectomics question?
   - Your answer:
2. How do we avoid leakage and overfitting in structural data?
   - Your answer:
3. Which metrics matter scientifically, not only computationally?
   - Your answer:

---

## The task

**Scenario:** You need to classify neurite fragments into coarse categories for downstream proofreading prioritization.

1. Propose feature set and leakage-safe split design.
2. Train one baseline and one improved model (or pseudocode plan).
3. Report two standard metrics and one biologically targeted metric.
4. Draft a model limitation statement with non-supported use cases.

### What you hand in

- Feature + split design sheet
- Metric table with interpretation notes
- Limitation statement

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Define task and biological decision context.
- [ ] Construct feature set with rationale and preprocessing log.
- [ ] Choose split strategy that blocks leakage pathways.
- [ ] Train baseline + candidate models and compare error profiles.
- [ ] Report metrics, limitations, and deployment constraints.

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

- [ ] I did not assume: Adding more features always improves science.
- [ ] I did not assume: One summary metric is enough.
- [ ] I did not assume: Random split always gives valid generalization estimates.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| 00:00-08:00 | Task framing and leakage examples |
| 08:00-20:00 | Feature rationale workshop |
| 20:00-34:00 | Split strategy and baseline modeling |
| 34:00-46:00 | Error analysis and biologically relevant metrics |
| 46:00-56:00 | Model-card limitation writing |
| 56:00-60:00 | Competency checkpoint |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass**
- **Strong performance**
- **Common failure modes**

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

For one candidate model, write:
1. one plausible leakage pathway,
2. one metric blind spot,
3. one limitation you would report publicly.

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

*Module page: `/modules/module13/` · Slides: `/modules/slides/module13/` · [Facilitator guide](/teaching/facilitator-guide/)*
