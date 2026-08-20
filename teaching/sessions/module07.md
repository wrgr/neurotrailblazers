---
layout: page
title: "Session Kit: Module 07: Proofreading and Quality Control"
description: "Everything needed to run Module 07 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module07/
slug: session-module07
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module07.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4 hours |
| **Capability target** | Execute a proofreading triage cycle that ranks corrections by impact and issues a transparent QC decision. |
| **Learners leave with** | Triage table with impact ratings and one-line justifications |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Modules 01-06


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module07.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module07.pptx' | relative_url }}">Download deck (.pptx)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module07/module07-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module07/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-10:00 | Triage philosophy | |
| 10:00-24:00 | Queue classification exercise | |
| 24:00-38:00 | Correction sprint | |
| 38:00-50:00 | Threshold-based release decisions | |
| 50:00-60:00 | Competency check | |

## The activity

**Scenario:** You are the QC lead for a 100x100x100 um subvolume that will be used in a paper analyzing reciprocal connectivity between L2/3 pyramidal cells. The segmentation has been through one round of automated error detection. You need to decide: is this subvolume ready for analysis?

1. Review the automated error report: 45 flagged errors (18 merges, 20 splits, 7 uncertain).
2. Triage: classify each by impact on the reciprocal connectivity analysis. Which errors could create false reciprocal connections? Which could hide real ones?
3. Fix the top 15 errors, documenting each correction with a one-line rationale.
4. Compute before/after metrics (provided metric computation script).
5. Write a 1-page release recommendation memo with: metrics summary, corrections summary, remaining risks, and go/no-go recommendation with explicit reasoning.

**What learners hand in**

- Triage table with impact ratings and one-line justifications
- Correction log with before/after segment IDs and rationale for each fix
- Metrics comparison table (pre- and post-proofreading)
- Release recommendation memo with explicit go/no-go decision

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** Proofreading is cleanup that ends when the data looks right, rather than an allocation problem under a fixed budget.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A single aggregate quality score is enough to decide whether a release is good.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Throughput is a sufficient measure of annotator performance without agreement statistics alongside it.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A result can be reported without stating the proofreading level of the cells it rests on.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"

## Naming the norm

Every session is a chance to make one piece of the hidden curriculum explicit.
Pick a moment where you would normally just *do* the professional thing, and say
out loud why you are doing it — then ask whether anyone was taught that.

For this session, the candidate is whichever norm the activity most depends on:
stating an assumption in the same sentence as the claim, recording the version a
number came from, or saying "uncertain" and having it count as a real answer.
See [the hidden curriculum]({{ '/hidden-curriculum/' | relative_url }}) for the
collected set and why naming them is a fairness intervention rather than etiquette.

## Assessment

- **Minimum pass**: Consistent queueing by type and impact. Release decision justified by metrics. Correction log present.
- **Strong performance**: Impact reasoning explicitly tied to the scientific question (reciprocal connectivity). Uncertainty handling is transparent -- learner acknowledges what they could not determine and explains how that uncertainty affects the release decision. Memo is clear and actionable.
- **Common failure to flag**: Ad hoc corrections without policy -- fixing whatever looks wrong rather than systematically prioritizing by impact. Another common failure is issuing a release recommendation without referencing specific metric values.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behaviour within one session.

## Exit prompt

Write one rule for when an error must be fixed before release. Your rule should specify: (1) the type of error, (2) the condition under which it is mandatory to fix, and (3) why that condition matters for downstream analysis. Example format: "A [type] error must be fixed before release when [condition], because [scientific reasoning]."

## If this session goes wrong

- **Nobody talks in the debrief.** You asked "any questions?" Ask instead: "Which
  cue would you drop first if the data got worse?"
- **Everyone finishes early.** They are pattern-matching, not judging. Give an
  ambiguous case where the answer is "uncertain" and see what happens.
- **Nobody finishes.** The scaffolding came off too fast. Work the next case
  together rather than pressing on.
- **A learner is silently lost.** The most likely cause is unstated vocabulary.
  Point them at the [dictionary]({{ '/technical-training/dictionary/' | relative_url }}) and check back.

---

*[All session kits]({{ '/teaching/sessions/' | relative_url }}) · [Facilitator guide]({{ '/teaching/facilitator-guide/' | relative_url }})*
