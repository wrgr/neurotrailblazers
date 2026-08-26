---
layout: page
title: "Session Kit: Module 06: Segmentation 101"
description: "Everything needed to run Module 06 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module06/
slug: session-module06
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module06.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4 hours |
| **Capability target** | Detect and categorize core segmentation errors and execute one correction cycle with documented quality impact. |
| **Learners leave with** | Ranked error list with type classifications and impact estimates |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Modules 01-05


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module06.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module06.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module06/module06-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module06/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-08:00 | Segmentation goals | |
| 08:00-22:00 | Error taxonomy with real examples | |
| 22:00-36:00 | Guided correction round | |
| 36:00-48:00 | Quality metric interpretation | |
| 48:00-60:00 | Debrief and competency check | |

## The activity

**Scenario:** Your team has a freshly segmented 50x50x50 um subvolume containing approximately 200 neuron fragments. Automated error detection has flagged 25 candidate errors. You have time to fix 10.

1. Review all 25 flagged candidates and classify each by error type (merge/split/boundary/uncertain).
2. Rank by estimated impact: which corrections would most change the connectivity graph?
3. Fix the top 10 in priority order, documenting each correction.
4. Compute before/after metrics for the subvolume.
5. Write a 3-sentence "release note" summarizing what was fixed and what remains.

**What learners hand in**

- Ranked error list with type classifications and impact estimates
- Correction log with before/after evidence for each fix
- Metric summary table
- Release note

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** Merge and split errors are equally costly, so error counts alone rank corrections.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** An object that looks like a plausible neuron is evidence that the segmentation is correct.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** The most visually obvious errors are the ones most worth fixing.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A segmentation can be finished, rather than released at a stated level with stated remaining error.
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

- **Minimum pass**: Correct error labels and at least one valid correction with evidence.
- **Strong performance**: Correction prioritization explicitly tied to downstream analysis impact. Metrics show measurable improvement.
- **Common failure to flag**: Correction without evidence of quality change — fixing things without checking whether it helped.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behavior within one session.

## Exit prompt

Explain when you would defer a correction instead of fixing immediately.

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
