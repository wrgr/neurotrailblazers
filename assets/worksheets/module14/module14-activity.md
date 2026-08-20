# Module 14 Activity Worksheet

**Module:** Module 14: Computer Vision for EM  
**Duration:** 4-5 hours  
*Generated from the module page. Edit `modules/module14.md`, not this file.*

---

## Capability target

Design and evaluate a CV pipeline for EM imagery that is fit for a specific connectomics task and explicitly bounded by known failure modes.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Image-processing and matrix basics
- [ ] Foundational ML familiarity

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

**Scenario:** Compare two segmentation-support CV models for an EM subvolume.

1. Define EM task and acceptable error envelope.
2. Select baseline and candidate CV approaches.
3. Run evaluation using biologically relevant metrics.
4. Perform failure-case review on ambiguous regions.
5. Publish model card with limitations and intended use.

### What you hand in

- metric table with biological interpretation
- failure-case log
- model-card limitation statement

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Define EM task and acceptable error envelope.
- [ ] Select baseline and candidate CV approaches.
- [ ] Run evaluation using biologically relevant metrics.
- [ ] Perform failure-case review on ambiguous regions.
- [ ] Publish model card with limitations and intended use.

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

- [ ] I did not assume: One model can solve all EM tasks equally well.
- [ ] I did not assume: High benchmark score implies safe downstream use.
- [ ] I did not assume: Visual plausibility is sufficient validation.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| | 00:00-08:00 task framing + exemplar failure modes. |
| | 08:00-20:00 choose metrics tied to downstream biology. |
| | 20:00-34:00 evaluate baseline vs candidate model. |
| | 34:00-46:00 error taxonomy and triage discussion. |
| | 46:00-56:00 model card drafting. |
| | 56:00-60:00 competency check. |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass:** clear task-model rationale, biologically relevant metrics, explicit limitations.
- **Strong performance:** robust failure analysis and operational release criteria.
- **Failure modes:** metric-only reasoning, weak split design, no deployment boundaries.

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
