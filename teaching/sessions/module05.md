---
layout: page
title: "Session Kit: Module 05: Electron Microscopy and Image Basics"
description: "Everything needed to run Module 05 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module05/
slug: session-module05
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module05.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4 hours |
| **Capability target** | Evaluate EM image patches for artifact risk and issue a justified pass/rework recommendation. |
| **Learners leave with** | Completed QA worksheet for all six patches |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Modules 01-04


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module05.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module05.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module05/module05-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module05/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-08:00 | EM basics refresher | |
| 08:00-20:00 | Artifact recognition walkthrough | |
| 20:00-34:00 | Learner triage round | |
| 34:00-46:00 | QA threshold debate | |
| 46:00-56:00 | Decision logging practice | |
| 56:00-60:00 | Competency check | |

## The activity

**Scenario:** {: #studio-activity}

1. Inspect image quality and artifact signatures.
2. Classify severity and likely impact on segmentation.
3. Decide pass/flag/rework with documented rationale.
4. Log findings in a structured QA record for reproducibility.

**What learners hand in**

- Completed QA worksheet for all six patches
- Spatial artifact map (annotated sketch or diagram)
- One-page recommendation memo with summary table

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** You can proofread your way out of a bad image.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A noisy image is worse for segmentation than a clean image with faint membranes.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Artifact severity can be judged from a count, when the spatial distribution matters more.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Quality assessment is a clerical checkpoint rather than a scientific judgement that propagates through every downstream claim.
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

- **Minimum (pass)**: Accurate identification of major artifacts across all patches, correct mapping to segmentation error type, and a defensible pass/flag/rework decision for each patch.
- **Strong (merit)**: Clear articulation of cost tradeoffs, consistent severity thresholds across patches, spatially aware analysis, and a well-structured recommendation memo with specific conditions.
- **Failure**: Artifact labels assigned without reference to downstream segmentation implications, or QA decisions made without documented rationale.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behaviour within one session.

## Exit prompt

Pick one artifact and explain how it could create a merge or split error later. Then estimate: if this artifact appears on 5% of sections, how many additional proofreading hours would it add to a 1000-section volume?

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
