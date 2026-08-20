# Module 07 Activity Worksheet

**Module:** Module 07: Proofreading and Quality Control  
**Duration:** 4 hours  
*Generated from the module page. Edit `modules/module07.md`, not this file.*

---

## Capability target

Execute a proofreading triage cycle that ranks corrections by impact and issues a transparent QC decision.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] The module prerequisites listed on the module page

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. Which errors most affect biological conclusions?
   - Your answer:
2. What thresholds justify release versus rework?
   - Your answer:

---

## The task

**Scenario:** You are the QC lead for a 100x100x100 um subvolume that will be used in a paper analyzing reciprocal connectivity between L2/3 pyramidal cells. The segmentation has been through one round of automated error detection. You need to decide: is this subvolume ready for analysis?

1. Review the automated error report: 45 flagged errors (18 merges, 20 splits, 7 uncertain).
2. Triage: classify each by impact on the reciprocal connectivity analysis. Which errors could create false reciprocal connections? Which could hide real ones?
3. Fix the top 15 errors, documenting each correction with a one-line rationale.
4. Compute before/after metrics (provided metric computation script).
5. Write a 1-page release recommendation memo with: metrics summary, corrections summary, remaining risks, and go/no-go recommendation with explicit reasoning.

### What you hand in

- Artifact produced during the activity
- One stated limitation or uncertainty
- One revision made in response to feedback

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] **Classify** errors by type (merge/split/boundary) and estimated impact (high/medium/low). Use the error taxonomy from the content library as a reference checklist.
- [ ] **Prioritize** correction queue: high-impact merges first, then splits in the region of interest, then boundary errors. Defer or discard low-impact errors outside the analysis region.
- [ ] **Apply** corrections using Neuroglancer/CAVE split and merge operations. For each correction, note the supervoxel IDs involved and the evidence that motivated the edit.
- [ ] **Verify** each correction: check that the fix didn't introduce new errors. Splitting a merge sometimes creates an orphan fragment that needs re-merging elsewhere. Merging a split sometimes absorbs a nearby fragment that shouldn't be included. Always inspect the result in at least two orthogonal views.
- [ ] **Record** QC decision: compute metrics, compare to release thresholds, issue go/rework recommendation. If the recommendation is "rework," specify which error categories need further attention and estimate the additional effort required.

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

- [ ] I have stated one thing I am still unsure about.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| 00:00-10:00 | Triage philosophy |
| 10:00-24:00 | Queue classification exercise |
| 24:00-38:00 | Correction sprint |
| 38:00-50:00 | Threshold-based release decisions |
| 50:00-60:00 | Competency check |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass**: Consistent queueing by type and impact. Release decision justified by metrics. Correction log present.
- **Strong performance**: Impact reasoning explicitly tied to the scientific question (reciprocal connectivity). Uncertainty handling is transparent -- learner acknowledges what they could not determine and explains how that uncertainty affects the release decision. Memo is clear and actionable.
- **Common failure to flag**: Ad hoc corrections without policy -- fixing whatever looks wrong rather than systematically prioritizing by impact. Another common failure is issuing a release recommendation without referencing specific metric values.

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

Write one rule for when an error must be fixed before release. Your rule should specify: (1) the type of error, (2) the condition under which it is mandatory to fix, and (3) why that condition matters for downstream analysis. Example format: "A [type] error must be fixed before release when [condition], because [scientific reasoning]."

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

*Module page: `/modules/module07/` · Slides: `/modules/slides/module07/` · [Facilitator guide](/teaching/facilitator-guide/)*
