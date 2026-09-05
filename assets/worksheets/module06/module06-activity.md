# Module 06 Activity Worksheet

**Module:** Module 06: Segmentation 101  
**Duration:** 4 hours  
*Generated from the module page. Edit `modules/module06.md`, not this file.*

---

## Capability target

Detect and categorize core segmentation errors and execute one correction cycle with documented quality impact.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] Modules 01-05

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. How do segmentation errors affect biological interpretation?
   - Your answer:
2. Which corrections should be prioritized first?
   - Your answer:

---

## The task

**Scenario:** Your team has a freshly segmented 50x50x50 um subvolume containing approximately 200 neuron fragments. Automated error detection has flagged 25 candidate errors. You have time to fix 10.

1. Review all 25 flagged candidates and classify each by error type (merge/split/boundary/uncertain).
2. Rank by estimated impact: which corrections would most change the connectivity graph?
3. Fix the top 10 in priority order, documenting each correction.
4. Compute before/after metrics for the subvolume.
5. Write a 3-sentence "release note" summarizing what was fixed and what remains.

### What you hand in

- Ranked error list with type classifications and impact estimates
- Correction log with before/after evidence for each fix
- Metric summary table
- Release note

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Load segmented patch in Neuroglancer or equivalent viewer.
- [ ] Identify merge/split candidates by scrolling through z and checking 3D meshes for implausible morphology.
- [ ] Apply correction: split merged segments at the boundary, merge split fragments by verifying continuity.
- [ ] Recalculate quality indicators: did the correction improve local metrics?
- [ ] Log decisions: record what was changed, why, and what evidence supported the decision.

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

- [ ] I did not assume: Merge and split errors are equally costly, so error counts alone rank corrections.
- [ ] I did not assume: An object that looks like a plausible neuron is evidence that the segmentation is correct.
- [ ] I did not assume: The most visually obvious errors are the ones most worth fixing.
- [ ] I did not assume: A segmentation can be finished, rather than released at a stated level with stated remaining error.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| 00:00-08:00 | Segmentation goals |
| 08:00-22:00 | Error taxonomy with real examples |
| 22:00-36:00 | Guided correction round |
| 36:00-48:00 | Quality metric interpretation |
| 48:00-60:00 | Debrief and competency check |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass**
  - Every flagged candidate carries an error-type label (merge/split/boundary/uncertain), and mislabels affect fewer than 3 of the 25 candidates.
  - At least one correction is executed with the supporting evidence stated in the log before the edit, not reconstructed afterward.
  - The correction log records object ID, operation, location, and the specific visual evidence — a reader could re-find the site from the log alone.
  - Before/after quality indicators are computed for at least one correction, with the direction of change stated.
- **Strong performance**
  - The priority ranking ties each candidate to its expected effect on the downstream connectivity graph, and merges outrank splits of comparable size with the reason stated.
  - Before/after metrics are reported for the whole subvolume, and any metric that moved the wrong way is explained rather than omitted.
  - At least one flagged candidate is explicitly deferred with a recorded reason (cost to fix, ambiguity, outside analysis set) rather than silently skipped.
  - The release note states what remains unexamined and what error types are still expected, not only what was fixed.
- **Common failure to flag**
  - Correction without evidence of quality change — fixing things without checking whether it helped.
  - Ranking by visual conspicuousness rather than by impact on the analysis.
  - A merge introduced while fixing a split, because continuity was assumed from appearance instead of verified across sections.

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

Explain when you would defer a correction instead of fixing immediately.

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

*Module page: `/modules/module06/` · Slides: `/modules/slides/module06/` · [Facilitator guide](/teaching/facilitator-guide/)*
