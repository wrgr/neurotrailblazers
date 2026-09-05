---
layout: page
title: "Session Kit: Module 10: Network Science and Graph Representation"
description: "Everything needed to run Module 10 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module10/
slug: session-module10
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module10.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4 hours |
| **Capability target** | Build one connectome graph representation and justify two metric choices for a defined hypothesis. |
| **Learners leave with** | Graph statistics summary table |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Modules 01-09


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module10.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module10.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module10/module10-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module10/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| 00:00-08:00 | Graph abstraction choices | |
| 08:00-20:00 | Graph build demo | |
| 20:00-34:00 | Metric computation | |
| 34:00-46:00 | Interpretation and null concerns | |
| 46:00-60:00 | Competency check | |

## The activity

**Scenario:** You have the connectivity graph of 500 neurons in a cortical column from the MICrONS dataset. Your PI asks: "Is this circuit small-world? Are there hub neurons? Are there communities?"

1. Load the graph and compute basic statistics (nodes, edges, density, components).
2. Compute: degree distribution, clustering coefficient, average path length.
3. Compare to degree-preserving random graph and Watts-Strogatz small-world reference.
4. Identify candidate hub neurons (top 5% by degree or betweenness centrality).
5. Run community detection (Louvain or Leiden). Do detected communities align with cell types?
6. Write a 1-page graph analysis report with figures, metrics, null comparisons, and biological interpretation.

**What learners hand in**

- Graph statistics summary table
- Degree distribution plot (log-log scale)
- Community detection results with cell-type comparison
- 1-page report

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** The connectivity graph is the data, rather than one lossy projection of it that discards all geometry.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** The synapse threshold is a technical detail that does not need reporting.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** A graph metric means the same thing biologically as it does in its original network-science context.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Erdos-Renyi is an acceptable null for a spatially embedded, degree-heterogeneous connectome.
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
  - The node/edge schema is stated explicitly — node definition, edge direction, weighting, and synapse threshold — before any metric appears.
  - Each reported metric is paired with a null-model comparison; no bare metric values stand alone.
  - At least two metrics are linked in writing to the specific question they answer for the PI's three asks (small-world, hubs, communities).
  - The report names at least one piece of information the graph abstraction discarded and one question it therefore cannot answer.
- **Strong performance**
  - The headline result is re-run at a second synapse threshold, and the report states which conclusions held and which moved.
  - Degree outliers are checked against the underlying reconstruction before being reported as hubs, with the check documented.
  - More than one null model is used, or the limits of the single null are stated in words (what it does and does not control for).
  - Detected communities are compared against external labels (cell types), and disagreement is reported as a finding rather than suppressed.
- **Common failure to flag**
  - Metric dumping — computing every available metric without explaining what question each answers.
  - Hub or community claims made without checking whether a merge error or threshold choice manufactured them.
  - A significance claim against Erdos-Renyi only, on a graph with obvious degree heterogeneity.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behavior within one session.

## Exit prompt

State one reason a graph metric might be misleading in your current dataset.

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
