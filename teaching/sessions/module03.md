---
layout: page
title: "Session Kit: Module 03: Python and Jupyter for Neuroscience"
description: "Everything needed to run Module 03 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module03/
slug: session-module03
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module03.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4 hours |
| **Capability target** | Create a reproducible Jupyter notebook that ingests a connectomics dataset slice, performs one analysis, and exports documented outputs. Demonstrate familiarity with the core Python libraries used in connectomics research: CAVEclient, CloudVolume, NetworkX, pandas, and matplotlib. |
| **Learners leave with** | A notebook that runs clean from a restarted kernel, with a header cell recording title, author, date, dataset, and materialization version |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Modules 01-02


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module03.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module03.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module03/module03-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module03/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| | Header: title, author, date, dataset version, materialization version. | |
| | Setup: imports and environment configuration. | |
| | Data loading: queries and schema validation. | |
| | Analysis: computation cells with markdown explanations. | |
| | Export: saving outputs with metadata. | |
| | Initialize CAVEclient and set materialization version (3 min). | |
| | Query synapse table filtered by brain region (5 min). | |
| | Group by pre/post cell type and count synapses (5 min). | |
| | Build a NetworkX graph from the grouped data (5 min). | |
| | Plot a bar chart of top 10 connections by synapse count (4 min). | |

## The activity

**Scenario:** {: #studio-activity}

1. Create a new notebook with a header cell: title, your name, date, dataset name, materialization version.
2. Create a setup cell with all imports and version pinning.
3. Initialize CAVEclient (or load a provided sample CSV if CAVE access is unavailable).
4. Query or load a synapse table. Validate: print column names, data types, row count, and first 5 rows.
5. Add a markdown cell explaining what the dataset contains and what version you are using.
6. Choose one descriptive analysis from the following options:
7. Write the analysis code with markdown cells explaining each step.
8. Compute at least one summary statistic (mean, median, max, or standard deviation) and report it in a markdown cell.
9. Create at least one publication-quality figure with labeled axes, title, and legend.
10. Add a markdown caption below the figure explaining what it shows and what conclusions (if any) can be drawn.
11. Export your data table as CSV and your figure as PNG.
12. Create a metadata JSON cell recording dataset version, query parameters, and analysis date.
13. Restart kernel and run all cells.
14. Verify all outputs regenerate correctly.
15. If any cell fails, fix it and re-run.

**What learners hand in**

- A notebook that runs clean from a restarted kernel, with a header cell recording title, author, date, dataset, and materialization version
- One descriptive analysis with at least one summary statistic reported in a markdown cell
- One labeled figure exported as PNG, with a caption stating what it shows and what it does not license you to conclude
- The underlying data table exported as CSV, plus a metadata JSON recording dataset version, query parameters, and analysis date
- If any cell fails, fix it and re-run

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** You need to be an expert programmer to do connectomics.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** If the code runs on my machine, it is reproducible.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Version control is only for software engineers.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Code comments are sufficient documentation.
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

- **Minimum:** runnable notebook from clean kernel, clear outputs, basic metadata, at least one plot with labels.
- **Strong:** clean linear structure, robust error handling, repeatable rerun, markdown narrative explaining every step, exported metadata JSON, version-pinned requirements file.
- **Failure:** hidden state dependencies, undocumented assumptions, plots without labels, no dataset version recorded.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behavior within one session.

## Exit prompt

Add one markdown cell documenting input version, processing steps, and output files. Then write a code cell that queries a synapse table and computes the mean number of synapses per neuron for one brain region.

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
