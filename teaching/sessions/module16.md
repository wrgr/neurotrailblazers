---
layout: page
title: "Session Kit: Module 16: Scientific Visualization for Connectomics"
description: "Everything needed to run Module 16 as a taught session: prep, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/module16/
slug: session-module16
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

*Generated from `modules/module16.md`. Edit the module page, not this file.*

## At a glance

| | |
|---|---|
| **Duration** | 4 hours |
| **Capability target** | Produce a figure set that communicates connectomics findings accurately, including uncertainty and data-quality context, for both expert and mixed audiences. Students will leave this module able to choose the right visualization form for a given scientific claim, build publication-quality figures using standard tools, and defend every design choice in terms of clarity and honesty. |
| **Learners leave with** | Three-figure set exported at publication resolution with complete captions |

## Before you walk in

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Data access works — accounts, viewer, notebook — **verified today, not last week**.
- [ ] The rubric is visible to learners before they start, not after.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.

Learners should arrive having covered:

- Basic plotting library familiarity
- Understanding of analysis outputs


## Materials

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module16.html' | relative_url }}">Open deck (HTML)</a>
    <a class="resource-link" href="{{ site.deck_source_base }}/modules/module16.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/assets/worksheets/module16/module16-activity.md' | relative_url }}">Learner worksheet</a>
    <a class="resource-link" href="{{ '/modules/module16/' | relative_url }}">Full module page</a>
  </div>
</div>

## Run of show

| Time | Segment | Your note |
|---|---|---|
| | "Excitatory neurons in layer 4 receive more synaptic input than those in layer 2/3." | |
| | "Reciprocal connections are enriched between Martinotti cells." | |
| | "Axonal arbors of chandelier cells are spatially restricted to a 100-micron radius." | |

## The activity

**Scenario:** You are preparing a three-figure package for a short connectomics paper reporting cell-type-specific connectivity patterns in a cortical volume. Your dataset includes a 50x50 cell-type adjacency matrix, morphological reconstructions for three example neurons, and synapse count distributions across layers.

1. **Map each claim to required visual evidence.** For every result sentence, identify what figure panel and what visual encoding will support it.
2. **Select the appropriate plot type.** Use the decision framework: topology questions get node-link diagrams or matrices; quantity questions get heatmaps or bar charts; spatial questions get renderings; distribution questions get histograms or violins.
3. **Draft candidate visuals with uncertainty layers.** Include error bars, confidence bands, or explicit missing-data indicators from the start --- do not plan to "add them later."
4. **Run critique for misinterpretation risk.** Show the draft to someone unfamiliar with the analysis and ask them what they conclude. If their conclusion differs from your intent, revise.
5. **Check accessibility.** Run the figure through a colorblind simulator (e.g., Coblis or the Matplotlib colorblind check). Verify grayscale legibility.
6. **Revise for clarity, accessibility, and reproducibility.** Add scale bars, axis labels, panel letters, and complete captions.
7. **Export figure package with caption metadata.** Include figure files at publication resolution (300+ DPI for raster, vector preferred), caption text, and a note on the dataset version and code used to generate each panel.

**What learners hand in**

- Three-figure set exported at publication resolution with complete captions
- Uncertainty annotation strategy document (one paragraph per figure explaining what uncertainty is shown and why)
- Revision log from peer critique (at least two specific changes made in response to feedback)
- Accessibility check report (colorblind simulation screenshot for each figure)

## Misconceptions to target

These are the errors this session exists to prevent. Surface them in the debrief
rather than pre-empting them in the lecture — a misconception a learner has
voiced is far easier to correct than one they are holding silently.

- **They may believe:** Making a figure "look good" is not the same as making it truthful. A beautiful 3D rendering with no scale bar and no uncertainty indicators is worse than an ugly but complete 2D plot.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** There is no single "best" visualization. The best choice depends on the claim.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Complexity in a figure does not equal rigor. Simplicity with completeness is the standard.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Cleaner-looking plots are not always better. A plot that hides uncertainty is less honest than one that shows it.
  - *Surface it by asking:* "What would have to be true for that to hold? What would change your mind?"
- **They may believe:** Aesthetics cannot replace methodological clarity. A beautiful figure that only some people can read is not a good figure.
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

- **Minimum pass:** visuals map clearly to claims, include uncertainty context, use perceptually uniform colormaps, and have complete axis labels and scale bars.
- **Strong performance:** high clarity across expert and non-expert audiences, minimal misinterpretation risk, colorblind-safe design, explicit documentation of dataset version and code used for each panel, and thoughtful caption language that narrows interpretation bounds.
- **Failure modes:** overloaded figures with too many overlapping elements, missing scale context, hidden uncertainty, rainbow colormaps, gratuitous 3D renderings, captions that do not mention data quality or limitations.

**Grade the reasoning, not the answer.** A correct call with no evidence chain
should not outscore a well-reasoned incorrect one — and saying so publicly changes
behavior within one session.

## Exit prompt

Take one existing connectomics figure (from a paper, a classmate, or your own work) and perform a full audit:
1. Identify the claim the figure is supposed to support.
2. Add one uncertainty cue (error bar, confidence band, or missing-data indicator).
3. Replace the colormap with a perceptually uniform alternative if needed.
4. Write a two-sentence caption that narrows interpretation bounds and specifies the dataset version.
5. Run the figure through a colorblind simulator and note any issues.

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
