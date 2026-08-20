---
layout: page
title: "Session Kit: Module 14: Computer Vision for EM"
description: "Everything needed to run Module 14 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module14/
slug: session-module14
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module14.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4-5 hours |
| **Capability target** | Design and evaluate a CV pipeline for EM imagery that is fit for a specific connectomics task and explicitly bounded by known failure modes. Concretely: choose an architecture from the shape of the task rather than from the benchmark leaderboard, decompose error into merges and splits instead of reporting one score, convert that decomposition into a downstream cost using a ratio your team has actually measured, and write a release gate that says in advance what result would stop the model from shipping. |
| **Learners leave with** | metric table with biological interpretation, split by region |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Image-processing and matrix basics
- Foundational ML familiarity

Pre-class preparation set for learners:

- Read [metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}) for VI and ERL, and [artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}) for what the model must survive.
- Bring or download one EM subvolume with visible artifacts.
- Be ready to state which downstream product your segmentation would feed.

## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module14.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module14.pptx' | relative_url }}">Download deck (.pptx)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module14/module14-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module14/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| | 00:00-08:00 task framing + exemplar failure modes. Show one split and one merge in the viewer and ask which is worse; collect reasons before giving the answer. | |
| | 08:00-20:00 choose metrics tied to downstream biology. Each learner writes the metric they would gate on and the threshold, before seeing any model output. | |
| | 20:00-34:00 evaluate baseline vs candidate model. Learners compute or are given VI components, ERL, and error counts for two models, then solve for the break-even merge-to-split ratio. | |
| | 34:00-46:00 error taxonomy and triage discussion. Sample failure cases, classify each by cause, and identify which causes augmentation could have addressed. | |
| | 46:00-56:00 model card drafting, including at least one unsupported use and the region breakdown of the metrics. | |
| 56:00-60:00 competency check | each learner states their release gate as a sentence that could fail. | |

## The activity

**Scenario:** Compare two segmentation-support CV models for an EM subvolume. You are given the model outputs, a proofread ground-truth subvolume of roughly 40 mm of traced path drawn from a clean region, and a second, smaller ground-truth patch from a region containing a partial fold and two lost sections. Your team maintains the production segmentation and must recommend one model.

1. Compute or tabulate VI with its split and merge components, ERL, and error counts for both models, reported separately for the clean and the artifact-heavy region.
2. Solve for the merge-to-split cost ratio at which the two models tie, and state which side of that ratio your team is on and how you know.
3. Sample at least 15 failure cases across both models and classify each by cause.
4. Write a release gate: a numeric criterion, decided before looking at the winner, that the chosen model must pass.
5. Draft the model card limitation statement, including one use you would refuse to support.

**What learners hand in**

- metric table with biological interpretation, split by region
- failure-case log with causes tallied
- break-even ratio calculation with the assumption behind it named
- model-card limitation statement

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** One architecture solves all EM tasks equally well.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A higher benchmark score means safer downstream use.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Visual plausibility is sufficient validation.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** The held-out ground truth is representative of the volume.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** More augmentation is always better than less.
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

- **Minimum pass:** clear task-model rationale, biologically relevant metrics reported with merge and split separated, explicit limitations naming at least one unsupported use.
- **Strong performance:** robust failure analysis by cause, a release gate written before the result was known, and a downstream cost argument that names the merge-to-split ratio as a measured quantity rather than an assumption.
- **Failure modes:** metric-only reasoning, pooling clean and artifact-heavy regions into one number, weak split design, no deployment boundaries, thresholds chosen after seeing which model they would favor.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behaviour within one session.

## Exit prompt

Document one CV result with one supported use case and one forbidden use case.

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
