---
layout: page
title: "Session Kit: Module 15: LLMs for Patch Analysis"
description: "Everything needed to run Module 15 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module15/
slug: session-module15
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module15.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4-5 hours |
| **Capability target** | Implement an LLM-assisted patch-analysis workflow with verification gates, confidence labeling, and explicit human override policies. Concretely: classify every output your workflow produces into named output classes, attach a verification method and a numeric acceptance threshold to each class before any output is used, measure whether the gate costs less than the task it replaces, and log model version, prompt, output, reviewer, and decision so a reader can reconstruct which claims a model touched. |
| **Learners leave with** | prompt + schema pack |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Segmentation and proofreading basics
- Basic scripting and data-table handling

Pre-class preparation set for learners:

- Read [proofreading tools]({{ '/content-library/proofreading/proofreading-tools/' | relative_url }}) so you know what the human-in-the-loop workflow currently is.
- Bring one real task from your own work you were considering handing to an LLM.
- Be ready to estimate how long that task takes you by hand.

## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module15.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module15.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module15/module15-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module15/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| | 00:00-08:00 scope boundaries and failure examples. Show the unpinned-query failure first, because it is the one that looks like a success. | |
| | 08:00-20:00 prompt template design, including the schema fields each gate depends on. | |
| | 20:00-34:00 run sample outputs and score reliability against a known answer; record agreement counts rather than impressions. | |
| | 34:00-46:00 define verification and override rules per output class, and estimate the cost of each gate. | |
| | 46:00-56:00 produce governance checklist and risk register, with one class explicitly marked as not yet usable. | |
| 56:00-60:00 competency check | each learner states one output class they would refuse to gate, and why. | |

## The activity

**Scenario:** Build an LLM-assisted triage helper for proofreading queues. Reviewers can inspect about 500 segments per week; the current heuristic ranks candidates by segment size and produces roughly 40% true errors in the top 500. Your team wants to know whether an LLM-assisted ranker, drawing on segment statistics and free-text QC notes, should replace it. You have a labeled holdout of 300 segments and one expert available for four hours.

1. Enumerate the output classes this helper will produce and name the one that carries the most risk.
2. Write the verification gate and numeric acceptance threshold for each class, before generating any output.
3. Estimate the cost of each gate and compare it with the cost of the task it replaces; mark any class where the gate loses.
4. Design the pilot: how many items per class, who adjudicates, and what result would cause you to abandon the helper.
5. Specify the logging schema and the human override policy, including the interface rule that prevents anchoring.
6. Write the risk register: for each output class, the failure mode, its detection method, and the fallback if the gate fails.

**What learners hand in**

- prompt + schema pack
- verification rubric with numeric thresholds per output class
- gate-cost comparison table
- risk register and override policy

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** Fluent output means correct output.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Spot-checking is enough when the output looks unusual.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** LLM assistance saves time on every task it can perform.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Chat history is sufficient traceability.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Showing the model's answer first speeds annotators up without changing their judgment.
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

- **Minimum pass:** clear task boundaries, verification logic with thresholds that can fail, and logging fields including model version and prompt.
- **Strong performance:** robust failure-mode handling, an actionable governance plan, a measured or defensibly estimated gate cost for each output class, and at least one class explicitly declared not yet usable.
- **Failure modes:** unbounded scope, no confidence policy, missing audit trail, thresholds written after seeing the outputs, and gates whose cost was never compared with the task they replace.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behaviour within one session.

## Exit prompt

For one LLM output type, define: acceptance threshold, verification method, and human override trigger.

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
