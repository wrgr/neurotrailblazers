# Module 20 Activity Worksheet

**Module:** Module 20: Statistical Models and Inference for Connectomics  
**Duration:** 4-6 hours  
*Generated from the module page. Edit `modules/module20.md`, not this file.*

---

## Capability target

Design and execute a connectomics inference plan that includes null-model choice, multiplicity control, uncertainty reporting, and explicit claim boundaries.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Basic probability/statistics
- [ ] Graph representation concepts

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. Which null model is valid for this connectome hypothesis?
   - Your answer:
2. How should multiplicity be handled across motif families?
   - Your answer:
3. What claims are robust versus exploratory?
   - Your answer:

---

## The task

**Scenario:** A team reports motif enrichment in one dataset and asks whether the claim generalizes.

1. Propose at least two candidate null models and justify each.
2. Run or outline multiplicity-aware testing strategy across motif set.
3. Draft a results summary separating exploratory and confirmatory findings.
4. Add one robustness check for cross-dataset comparability.

### What you hand in

- Inference design sheet (estimand, null, tests, correction)
- One-page claim calibration summary
- Robustness plan with pass/fail criteria

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] **Question-to-test mapping**
- [ ] **Null-model design**
- [ ] **Inference execution**
- [ ] **Robustness checks**
- [ ] **Claim calibration**

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

- [ ] I did not assume: A generic random graph is an adequate null for a connectome.
- [ ] I did not assume: A small p-value speaks for itself, regardless of how many tests were run.
- [ ] I did not assume: A hypothesis found in the data can be confirmed by the same data.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| 00:00-06:00 | Framing: the null is the scientific step |
| 06:00-18:00 | Worked example: reciprocity across nulls |
| 18:00-30:00 | Guided practice: write the uninteresting explanation |
| 30:00-40:00 | Multiplicity |
| 40:00-50:00 | Robustness and error sensitivity |
| 50:00-57:00 | Competency check |
| 57:00-60:00 | Exit ticket |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass**
  - Null model is justified and the constraints it preserves are listed explicitly, in terms of what the hypothesis treats as uninteresting.
  - Total test count — including tests run and not reported — is documented, and a named correction is applied against it.
  - Claims are partitioned into exploratory and confirmatory blocks with different language in each.
- **Strong performance**
  - Sensitivity analysis spans at least two preprocessing choices (synapse threshold, inclusion criteria), with results reported for each variant.
  - Effect sizes with uncertainty intervals appear alongside every significance statement.
  - Error-sensitivity band computed at measured merge and split rates, with the direction of merge bias named.
  - Generalization boundary stated: which dataset, version, and region the claim covers, and what it says nothing about.
- **Common failure modes**
  - Null model choice disconnected from the biological question.
  - Selective reporting: significant outcomes shown, the full test count uncounted.
  - Exploratory signal conflated with validated inference.
  - Analytic p-values used where dependence between tests calls for permutation.

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

Write a 6-8 sentence inference note that includes:
1. hypothesis and estimand,
2. null-model assumptions,
3. multiplicity strategy,
4. one robust conclusion and one unresolved uncertainty.

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

*Module page: `/modules/module20/` · Slides: `/modules/slides/module20/` · [Facilitator guide](/teaching/facilitator-guide/)*
