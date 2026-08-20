# Module 13 Activity Worksheet

**Module:** Module 13: Machine Learning in Neuroscience  
**Duration:** 4-5 hours  
*Generated from the module page. Edit `modules/module13.md`, not this file.*

---

## Capability target

Design and critique an ML analysis pipeline for connectomics that includes feature rationale, evaluation plan, leakage controls, and interpretation limits. Concretely: choose a split strategy from the leakage channels present in your data rather than from convention, pick metrics from the decision the model will support, quantify how much of your reported performance survives a harder split, and write a limitation statement specific enough that a reader knows which uses of your model you would refuse.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Basic scikit-learn workflow familiarity
- [ ] Feature matrix handling in Python
- [ ] Read [neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }}) so you know what the labels mean before you model them.
- [ ] Bring a small labeled table of your own, or use the supplied fragment set.
- [ ] Be ready to state, in one sentence, the decision your model would support.

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

**Scenario:** You must classify neurite fragments into coarse categories to prioritize a proofreading queue. You have roughly 4,000 labeled fragments drawn from about 600 neurons in one dataset, five classes with prevalences of approximately 38%, 27%, 19%, 12%, and 4%, and a reviewer team that can inspect 500 segments per week. A second, differently stained dataset is available as a held-out domain.

1. Propose a feature set with a one-line rationale per feature, and flag any feature that could encode dataset identity.
2. Design the split, naming the leakage channel each choice blocks and the cost you accept for it.
3. Train one baseline and one improved model, or write the pseudocode plan if compute is unavailable.
4. Report two standard metrics, one biologically targeted metric tied to the 500-segment review capacity, and per-class recall with prevalence.
5. Sample 20 misclassified fragments, classify the failure reason by hand, and propose the one data improvement that would fix the largest group.
6. Draft a model limitation statement naming at least three unsupported uses.

### What you hand in

- Feature and split design sheet with the leakage channel named for each split choice
- Metric table including per-class recall, prevalence, and precision at *k* = 500
- Error-analysis tally of 20 hand-classified failures
- Limitation statement with supported and unsupported uses

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Write the biological decision the model will support, naming who acts on the output and what they do differently as a result.
- [ ] Enumerate leakage channels present in your data — fragment duplication, spatial adjacency, annotator provenance, label circularity — and choose the split that blocks the strongest one.
- [ ] Construct the feature set with a one-line rationale per feature, and record the segmentation version the features were computed from.
- [ ] Fit all preprocessing (scaling, imputation, feature selection) inside the training fold only.
- [ ] Train a trivial baseline first — majority class, or a single-feature threshold — and report it alongside every later model.
- [ ] Evaluate with the metric that matches the decision from step 1, plus per-class recall and prevalence.
- [ ] Run error analysis on the failures: sample 20-30 misclassified examples and classify the failure reason by hand.
- [ ] Write the model card: intended use, unsupported uses, evaluation splits, metrics with intervals, and the domain in which the numbers hold.

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
- [ ] I did not assume: A random split always gives a valid generalization estimate.
- [ ] I did not assume: A 99% accurate classifier is a useful classifier.
- [ ] I did not assume: The training labels are the truth the model is failing to reach.

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
