---
layout: page
title: "Session Kit: Module 08: Hypothesis Testing in Connectomics"
description: "Everything needed to run Module 08 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module08/
slug: session-module08
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module08.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4 hours |
| **Capability target** | Design one hypothesis test with metric, null model, and interpretation boundary statement. |
| **Learners leave with** | 3 hypothesis sheets (hypothesis, metric, null, interpretation boundary, non-claim) |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Modules 01-07


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module08.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module08.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module08/module08-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module08/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-08:00 | Framing: good vs bad hypotheses | |
| 08:00-20:00 | Hypothesis drafting | |
| 20:00-34:00 | Metric and null model selection | |
| 34:00-46:00 | Interpretation workshop | |
| 46:00-60:00 | Competency check | |

## The activity

**Scenario:** Your lab is planning a study of feedforward vs feedback connectivity in mouse visual cortex using the MICrONS dataset. You need to design three testable hypotheses about the circuit architecture.

1. Draft 3 hypotheses (one about feedforward connections, one about feedback connections, one about reciprocal connections).
2. For each: specify the metric, null model, required dataset version, and analysis code outline.
3. For each: write the supported claim and explicit non-claim.
4. Exchange with a partner. Critique their null model choices and interpretation boundaries.
5. Revise based on peer feedback.

**What learners hand in**

- 3 hypothesis sheets (hypothesis, metric, null, interpretation boundary, non-claim)
- Peer critique notes (minimum 2 substantive comments per hypothesis)
- Revised hypotheses incorporating feedback

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** A significant result against a random-graph null is evidence of biological structure.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** The statistical test is the scientific step, when the choice of null model is.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A metric can be chosen after seeing the data without cost to the inference.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Reporting the tests that worked is sufficient without reporting how many were run.
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

- **Minimum pass**: Coherent hypothesis/metric/null trio for at least 2 of 3 hypotheses.
- **Strong performance**: Clear uncertainty and non-claim statements. Null model choice justified. Peer critique identifies genuine issues.
- **Common failure to flag**: Vague hypothesis without measurable endpoint ("we will study connectivity patterns") or missing null model.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behaviour within one session.

## Exit prompt

Write one claim and one explicit non-claim from the same test outcome.

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
