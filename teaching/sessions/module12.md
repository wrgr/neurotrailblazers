---
layout: page
title: "Session Kit: Module 12: Big Data in Connectomics"
description: "Everything needed to run Module 12 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module12/
slug: session-module12
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module12.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4-5 hours |
| **Capability target** | Produce a scalable, reproducible query-and-analysis plan for a large connectomics dataset, including storage assumptions, indexing strategy, and provenance capture. Concretely: size a dataset from its imaging parameters before anyone quotes you a price, choose a chunk and shard layout from your actual access pattern rather than from the format everyone else uses, predict which query will dominate your bill, and pin every published number to a segmentation version a stranger can re-query a year from now. |
| **Learners leave with** | Query architecture sketch with byte and object-count estimates |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Basic SQL/Python dataframe proficiency
- Familiarity with EM volume structure

Pre-class preparation set for learners:

- Read the [data formats]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) and [provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) library pages.
- Bring one query you have actually run, with its runtime and its data source.
- Have a calculator or notebook open; the first exercise is arithmetic, not code.

## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module12.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module12.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module12/module12-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module12/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-08:00 | Architecture framing and failure examples | |
| 08:00-20:00 | Access-pattern to index mapping exercise | |
| 20:00-34:00 | Query profiling and bottleneck diagnosis | |
| 34:00-46:00 | Provenance logging implementation | |
| 46:00-56:00 | Team review of reproducibility gaps | |
| 56:00-60:00 | Competency check and next-step assignment | |

## The activity

**Scenario:** Your team delivers a weekly motif-analysis report from a store holding a ~5 x 10^8-row synapse table, a 120,000-row segment table, and cell-type annotations for about 8,400 neurons. The volume is ~1 mm³, the bytes live in cloud object storage, and your analysis cluster is on-premises. The report is regenerated every Monday and will be cited in a manuscript. Last week's run took nine hours and produced numbers that do not match the report from three weeks ago; nobody knows why.

1. Propose a storage and index layout for the expected query patterns: chunk shape, sharding decision, and which products you mirror locally, with a byte estimate for each.
2. Outline the two queries that will dominate cost, estimate runtime from a sampled measurement, and name the operation you expect to be the bottleneck.
3. Define the minimum provenance fields for the weekly output and state what happens operationally when one is missing.
4. Diagnose the three-week discrepancy: list candidate causes in the order you would check them and the evidence that distinguishes them.
5. Produce one optimization proposal with an expected speedup and its cost, and one reproducibility safeguard someone else could execute without you.

**What learners hand in**

- Query architecture sketch with byte and object-count estimates
- Baseline vs optimized query plan with measured or sampled runtimes
- Provenance checklist with a stated failure action for each field
- A one-paragraph diagnosis of the version discrepancy naming the most likely cause first

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** The format everyone else uses is automatically the right layout for your access pattern.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Storage cost is the storage line on the invoice.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** The dataset size is the petabyte figure quoted for the raw imagery.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** An object ID refers to the same neuron next month.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** "it runs eventually" is acceptable for iterative science.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Notebook history is sufficient provenance.
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
behavior within one session.

## Exit prompt

Document one query you use with:
1. data source/version,
2. expected runtime class,
3. one provenance field you currently miss.

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
