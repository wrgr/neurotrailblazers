---
layout: page
title: "Session Kit: Module 20: Statistical Models and Inference for Connectomics"
description: "Everything needed to run Module 20 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module20/
slug: session-module20
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module20.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4-6 hours |
| **Capability target** | Design and execute a connectomics inference plan that includes null-model choice, multiplicity control, uncertainty reporting, and explicit claim boundaries. |
| **Learners leave with** | Inference design sheet (estimand, null, tests, correction) |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Basic probability/statistics
- Graph representation concepts


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module20.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module20.pptx' | relative_url }}">Download deck (.pptx)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module20/module20-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module20/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-06:00 | Framing: the null is the scientific step | |
| 06:00-18:00 | Worked example: reciprocity across nulls | |
| 18:00-30:00 | Guided practice: write the uninteresting explanation | |
| 30:00-40:00 | Multiplicity | |
| 40:00-50:00 | Robustness and error sensitivity | |
| 50:00-57:00 | Competency check | |
| 57:00-60:00 | Exit ticket | |

## The activity

**Scenario:** A team reports motif enrichment in one dataset and asks whether the claim generalizes.

1. Propose at least two candidate null models and justify each.
2. Run or outline multiplicity-aware testing strategy across motif set.
3. Draft a results summary separating exploratory and confirmatory findings.
4. Add one robustness check for cross-dataset comparability.

**What learners hand in**

- Inference design sheet (estimand, null, tests, correction)
- One-page claim calibration summary
- Robustness plan with pass/fail criteria

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** A generic random graph is rarely an adequate connectomics null.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Reporting only p-values without multiplicity context is incomplete.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Post-hoc storytelling is not confirmatory inference.
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

- **Minimum pass**
- **Strong performance**
- **Common failure modes**

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behaviour within one session.

## Exit prompt

Write a 6-8 sentence inference note that includes:
1. hypothesis and estimand,
2. null-model assumptions,
3. multiplicity strategy,
4. one robust conclusion and one unresolved uncertainty.

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
