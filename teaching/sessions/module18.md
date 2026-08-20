---
layout: page
title: "Session Kit: Module 18: Data Cleaning and Preprocessing"
description: "Everything needed to run Module 18 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module18/
slug: session-module18
track: career-and-community
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module18.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4-5 hours |
| **Capability target** | Produce a reproducible preprocessing release that transforms raw or intermediate connectomics outputs into analysis-ready data, with explicit quality gates and full provenance. Students will be able to identify the specific cleaning operations that shape biological conclusions, justify every threshold decision, and document their preprocessing pipeline so that another researcher can audit and reproduce it. |
| **Learners leave with** | Preprocessing decision table (one row per issue, columns: issue, policy, threshold, rationale, impact) |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Basic dataframe manipulation in Python
- Familiarity with segmentation/proofreading outputs


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module18.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module18.pptx' | relative_url }}">Download deck (.pptx)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module18/module18-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module18/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-08:00 | Setup and target framing | |
| 08:00-18:00 | Instructor modeling: ingest and anomaly screening | |
| 18:00-32:00 | Team preprocessing design | |
| 32:00-44:00 | QC pass | |
| 44:00-54:00 | Cross-team review | |
| 54:00-60:00 | Competency checkpoint | |

## The activity

**Scenario:** Your team receives a connectomics export from MICrONS minnie65 (CAVE materialization v795) containing: a synapse table (4.2 million rows) with confidence scores, a segment table (120,000 segments) with volumes, and a cell-type annotation table (8,400 classified neurons). Initial inspection reveals: 12% of synapses have confidence scores below 30, 35,000 segments have fewer than 2 synapses, 847 segments intersect the volume bounding box, and 23 segment IDs appear in the synapse table but not in the segment table.

1. **Artifact triage:** classify each issue (low-confidence synapses, small segments, boundary neurons, orphan IDs) by likely biological impact and propose a cleaning policy for each.
2. **Threshold justification:** for synapse confidence and segment size thresholds, propose two candidate values each and argue for your preferred choice. Explain what biological signal you might lose at each threshold.
3. **Implement preprocessing pipeline:** write pseudocode or notebook-level steps for the full cleaning workflow, from ingest through release.
4. **QC comparison:** compute (or estimate) pre/post metrics: total synapse count, total segment count, mean degree, graph density, and the fraction of each cell type remaining after cleaning.
5. **Release note:** produce a one-page release note that includes: input dataset version, all thresholds and parameters, code reference, QC metrics with pass/fail calls, and known residual risks (e.g., "boundary neurons were excluded, which may underrepresent connectivity of neurons near volume edges").

**What learners hand in**

- Preprocessing decision table (one row per issue, columns: issue, policy, threshold, rationale, impact)
- QC metric summary with thresholds and pass/fail calls
- Release note (inputs, transforms, outputs, limitations)

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** "raw data is always better." In connectomics, raw segmentation output contains systematic artifacts that will corrupt analysis if left uncleaned. The question is not whether to clean, but how to clean transparently.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** There is no single "correct" threshold. If your result depends on a specific threshold choice, it is fragile and should be reported with a sensitivity analysis.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** More filtering is not always better. Aggressive cleaning can create the appearance of clean results while actually removing biological signal.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Version-control notes alone are insufficient without data lineage. Git tracks code changes, but you also need to track which data version was processed with which code version.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Documenting preprocessing after the fact is unreliable. Document decisions in real time.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Reporting metrics without thresholds is not quality control. Every metric needs an associated action.
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

Take one connectomics table (real or mock) and write:
1. Three cleaning rules with rationale tied to specific data artifacts.
2. Two QC thresholds with associated pass/fail actions and biological justification.
3. One sensitivity analysis: what happens to your key metric if you relax or tighten your primary threshold by 20%?
4. One limitation that remains after preprocessing, stated concretely enough to guide interpretation.

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
