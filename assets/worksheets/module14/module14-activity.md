# Module 14 Activity Worksheet

**Module:** Module 14: Computer Vision for EM  
**Duration:** 4-5 hours  
*Generated from the module page. Edit `modules/module14.md`, not this file.*

---

## Capability target

Design and evaluate a CV pipeline for EM imagery that is fit for a specific connectomics task and explicitly bounded by known failure modes. Concretely: choose an architecture from the shape of the task rather than from the benchmark leaderboard, decompose error into merges and splits instead of reporting one score, convert that decomposition into a downstream cost using a ratio your team has actually measured, and write a release gate that says in advance what result would stop the model from shipping.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Image-processing and matrix basics
- [ ] Foundational ML familiarity
- [ ] Read [metrics and QA](/content-library/proofreading/metrics-and-qa/) for VI and ERL, and [artifact taxonomy](/content-library/imaging/artifact-taxonomy/) for what the model must survive.
- [ ] Bring or download one EM subvolume with visible artifacts.
- [ ] Be ready to state which downstream product your segmentation would feed.

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. Which CV model class is appropriate for each EM task?
   - Your answer:
2. How should CV error be measured for biological use cases?
   - Your answer:
3. What validation evidence is needed before downstream use?
   - Your answer:

---

## The task

**Scenario:** Compare two segmentation-support CV models for an EM subvolume. You are given the model outputs, a proofread ground-truth subvolume of roughly 40 mm of traced path drawn from a clean region, and a second, smaller ground-truth patch from a region containing a partial fold and two lost sections. Your team maintains the production segmentation and must recommend one model.

1. Compute or tabulate VI with its split and merge components, ERL, and error counts for both models, reported separately for the clean and the artifact-heavy region.
2. Solve for the merge-to-split cost ratio at which the two models tie, and state which side of that ratio your team is on and how you know.
3. Sample at least 15 failure cases across both models and classify each by cause.
4. Write a release gate: a numeric criterion, decided before looking at the winner, that the chosen model must pass.
5. Draft the model card limitation statement, including one use you would refuse to support.

### What you hand in

- metric table with biological interpretation, split by region
- failure-case log with causes tallied
- break-even ratio calculation with the assumption behind it named
- model-card limitation statement

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Write the EM task as a sentence naming the input, the output, and the downstream consumer of that output.
- [ ] Define the acceptable error envelope in decomposed terms: maximum merge rate, minimum ERL, and the region in which those numbers must hold.
- [ ] Select a baseline and at most two candidate approaches, using the approach table and the voxel geometry of your data.
- [ ] Assemble evaluation data that includes at least one deliberately hard region, and keep clean-region and hard-region metrics separate.
- [ ] Evaluate with VI decomposed, ERL, and a connectivity-level metric; never report a single aggregate score alone.
- [ ] Convert the error counts into downstream cost using a merge-to-split ratio your team measured rather than assumed.
- [ ] Review 20-30 failure cases by eye in ambiguous regions and classify each by cause: weak stain, section loss, fold, thin neurite, or genuine ambiguity.
- [ ] Publish a model card with intended use, unsupported uses, the evaluation regions, the metrics with their region breakdown, and the release gate the model passed.

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

- [ ] I did not assume: One architecture solves all EM tasks equally well.
- [ ] I did not assume: A higher benchmark score means safer downstream use.
- [ ] I did not assume: Visual plausibility is sufficient validation.
- [ ] I did not assume: The held-out ground truth is representative of the volume.
- [ ] I did not assume: More augmentation is always better than less.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| | 00:00-08:00 task framing + exemplar failure modes. Show one split and one merge in the viewer and ask which is worse; collect reasons before giving the answer. |
| | 08:00-20:00 choose metrics tied to downstream biology. Each learner writes the metric they would gate on and the threshold, before seeing any model output. |
| | 20:00-34:00 evaluate baseline vs candidate model. Learners compute or are given VI components, ERL, and error counts for two models, then solve for the break-even merge-to-split ratio. |
| | 34:00-46:00 error taxonomy and triage discussion. Sample failure cases, classify each by cause, and identify which causes augmentation could have addressed. |
| | 46:00-56:00 model card drafting, including at least one unsupported use and the region breakdown of the metrics. |
| 56:00-60:00 competency check | each learner states their release gate as a sentence that could fail. |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass:** clear task-model rationale, biologically relevant metrics reported with merge and split separated, explicit limitations naming at least one unsupported use.
- **Strong performance:** robust failure analysis by cause, a release gate written before the result was known, and a downstream cost argument that names the merge-to-split ratio as a measured quantity rather than an assumption.
- **Failure modes:** metric-only reasoning, pooling clean and artifact-heavy regions into one number, weak split design, no deployment boundaries, thresholds chosen after seeing which model they would favor.

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

Document one CV result with one supported use case and one forbidden use case.

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

*Module page: `/modules/module14/` · Slides: `/modules/slides/module14/` · [Facilitator guide](/teaching/facilitator-guide/)*
