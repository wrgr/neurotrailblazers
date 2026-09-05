---
layout: page
title: "Session Kit: Module 11: Synapses and Circuit Logic"
description: "Everything needed to run Module 11 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module11/
slug: session-module11
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module11.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4 hours |
| **Capability target** | Generate one synapse-to-motif interpretation with explicit evidence chain and one alternative explanation. |
| **Learners leave with** | Motif count table (observed vs expected vs z-score for each motif type) |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Modules 01-10


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module11.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module11.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module11/module11-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module11/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-10:00 | Synapse cue recap | |
| 10:00-24:00 | Motif construction examples | |
| 24:00-38:00 | Learner motif analysis | |
| 38:00-50:00 | Alternative explanation challenge | |
| 50:00-60:00 | Competency check | |

## The activity

**Scenario:** You are analyzing a 200-neuron subgraph from the MICrONS dataset, spanning L2/3 and L4 of mouse visual cortex. Your goal: characterize the local circuit motif profile and identify any enriched patterns that suggest specific wiring rules.

1. Enumerate all 2-node and 3-node motifs in the subgraph (use DotMotif or equivalent tool).
2. Generate 1,000 degree-preserving random rewirings. Count motifs in each.
3. Compute z-scores for each motif type.
4. Identify the top 3 most enriched motifs. For each: draw the circuit diagram, propose a functional interpretation, and state one alternative explanation.
5. Write a 1-page "circuit logic brief" summarizing the motif profile of this circuit.

**What learners hand in**

- Motif count table (observed vs expected vs z-score for each motif type)
- Circuit diagrams for top 3 enriched motifs
- 1-page circuit logic brief with interpretations and caveats

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** Asymmetric morphology means a synapse is excitatory, rather than putatively excitatory under a stated assumption.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Reconstruction errors add symmetric noise to motif counts, when merges bias them toward denser motifs.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A motif observed more often than expected is a functional building block.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Synapse count is a direct measure of connection strength rather than a proxy for it.
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
  - The motif count table reports observed, expected, and z-score for every motif class examined, not only the enriched ones.
  - At least one motif carries a complete evidence chain: detection method, count, null comparison, and interpretation, in that order.
  - Each claim in the circuit logic brief is paired with an explicit caveat stating what it does not prove.
  - The synapse threshold and data version used to build the subgraph are stated in the brief.
- **Strong performance**
  - Every enriched motif has at least one non-functional alternative explanation (spatial proximity, cell-type composition, reconstruction error) named and, where possible, tested.
  - A second null model or a stratified analysis is applied to at least one motif, with the change in effect size reported.
  - Synapse-level evidence — compartment targeting, Gray type — is used to subdivide or qualify at least one motif class rather than treating graph edges as interchangeable.
  - Sensitivity to reconstruction quality is quantified: the headline count is re-run at a second synapse threshold or across proofreading versions, and the difference is reported.
- **Common failure to flag**
  - Motif claim without error-awareness — treating every enriched pattern as a functional circuit without considering artifacts or spatial confounds.
  - Functional language ("this circuit gates," "this loop amplifies") presented as a finding rather than as a consistency statement.
  - Enrichment reported against a single weak null with no statement of what it fails to control.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behavior within one session.

## Exit prompt

Write one motif claim and one plausible confound.

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
