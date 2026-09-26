---
layout: page
title: "Lecture 3: Algorithms and Applications"
description: "Segmentation and its error taxonomy, proofreading triage, graph construction and null models, and an honest account of what connectomics and machine learning give each other."
permalink: /teaching/lectures/connectomics-03-algorithms-and-applications/
slug: lecture-connectomics-03-algorithms-and-applications
track: core-concepts-methods
content_type: delivery
pathways:
  - classroom delivery
  - graduate teaching
summary: "From voxels to a defensible claim: segmentation error, null models, and NeuroAI."
use_layout_hero: false
---

*Lecture 3 of the [connectomics lecture series]({{ '/teaching/lectures/' | relative_url }}).
58 slides in three parts, about 150 minutes. Openly licensed — **CC BY-SA 4.0**.*

## What this lecture covers

Segmentation and its error taxonomy, proofreading triage, graph construction and null models, and an honest account of what connectomics and machine learning give each other.

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/en585781/module09-algorithms-and-applications.html' | relative_url }}">Open the deck (HTML)</a>
    <a class="resource-link" href="https://github.com/wrgr/neurotrailblazers/blob/main/course/decks/marp/en585781/module09-algorithms-and-applications.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/teaching/lectures/' | relative_url }}">Series overview</a>
    <a class="resource-link" href="{{ '/teaching/lectures/algorithms-and-applications-activity/' | relative_url }}">Learner worksheet and offline analysis</a>
    <a class="resource-link" href="{{ '/teaching/lectures/algorithms-and-applications-answers/' | relative_url }}">Instructor model responses</a>
  </div>
  <p><small>The HTML deck presents directly in a browser. The Markdown source carries the
  speaker notes as HTML comments and is what to edit if you want to change wording —
  see <a href="{{ '/teaching/lectures/' | relative_url }}#formats">Formats</a> for PowerPoint and Google Slides.</small></p>
</div>

## Learning objectives

By the end of this lecture, participants will be able to:

1. **Describe** how automated segmentation works and where it fails structurally.
2. **Select** quality metrics appropriate to a stated endpoint.
3. **Construct** a connectivity graph from a reconstruction, stating every consequential choice.
4. **Justify** a null model for a stated hypothesis and interpret a motif result against it.
5. **Assess** what connectomics and machine learning currently give each other.

## Teach a 90-minute session

This selected-slide route is Session 4 in the [short teaching sequence]({{ '/teaching/sequence/' | relative_url }}),
but Lecture 3 / Module 9 in the original graduate course. Use the existing 58-slide
deck and embedded notes; slide numbers include the cover. The full two-hour lab on
slide 54 is an extension, not additional work required in this short session.

**Outcome:** build a directed graph under stated rules, compare reciprocity with an
explicit null, and produce an analysis card that distinguishes enrichment, evidence
and error sensitivity. Bring the study brief, audit and provenance record from the
preceding sessions. Fractions are sufficient; no graph-library knowledge is assumed.

**Preparation:** open the deck and worksheet/key, check the definitions of reciprocal
pairs versus reciprocated edges, and provide calculators. Optional Python 3 code
enumerates a tiny synthetic null without packages or accounts. Test both thresholds
before class; the same exact census is supplied on paper as a fallback.

- **0–10 min, slides 1–4, 12:** trace the endpoint back to segmentation and synapses.
  Ask whether a split, merge or partner mistake would affect this endpoint in the
  same way. Do not assume error directions cancel or always have the same sign.
- **10–20 min, slides 16, 19–21:** discuss proofreading priorities. Ask which
  correction would change the analysis most, and what evidence supports that ranking.
- **20–30 min, slides 25–28:** state node, edge, threshold and boundary rules.
  On the worksheet, count {A,B} once even though it supplies two directed edges.
- **30–40 min, slides 29–30, 34:** choose null constraints from the question. Explain
  the worksheet's fixed-edge-count model and prespecified upper-tail rule. Distinguish
  it from an independent-edge model that fixes only the expected number of edges.
- **40–75 min:** pairs complete the [worksheet]({{ '/teaching/lectures/algorithms-and-applications-activity/' | relative_url }}):
  10 minutes constructing graphs, 10 comparing nulls, 5 checking the uncertain edge,
  and 10 writing the card. At minute 60, check whether anyone has confused enrichment
  ratio with tail probability.
- **75–85 min, slides 36–38, 40:** exchange cards and compare with the
  [model responses]({{ '/teaching/lectures/algorithms-and-applications-answers/' | relative_url }}).
  A one-edge deletion is a scenario check, not a confidence interval. Ask what data
  would support a realistic error model.
- **85–90 min, slide 52:** collect cards and exit tickets: “My result is conditional
  on ___; the next measurement that could change it is ___.” A justified negative
  result meets the learning objective.

Unselected slides are optional depth for this route; 57–58 carry references and
credit. The full lecture adds segmentation algorithms, the larger hypothetical
null comparison and applications/NeuroAI. Use the key's four-dimension rubric for
the short session rather than the original course exam requirements on slide 55.

## Structure

The full, approximately 150-minute route uses all three parts.

### Part A — Segmentation, error, and the labor problem

How automated segmentation works and where it fails structurally, the error taxonomy, quality metrics and their blind spots, and triage by endpoint change per annotator-minute.

### Part B — From segmentation to a defensible graph

Six consequential construction choices, null models, the triad census, merge-error bias, and the error-sensitivity check.

### Part C — Applications, NeuroAI, and what to claim

Comparative connectomics, cell typing, three results that actually landed, and the two symmetric errors about connectomics and machine learning.

## What students produce

An **analysis card**: hypothesis, estimand, graph provenance block, null model with
the “it would be uninteresting if…” sentence written out, success criterion set in
advance, error sensitivity under a stated model, non-claim, and provenance. The
full lab uses measured error rates; the short session uses a declared toy scenario.

## The centrepiece

The full lecture compares **hypothetical** null summaries for 100 neurons, 1,200
edges and 210 reciprocal pairs. The interpretation depends on the null and test
direction, not just the enrichment ratio. Those illustrative summaries are not
outputs from supplied biological data. The short-session worksheet instead provides
a four-node graph whose entire fixed-edge-count null can be checked exactly.

## Notes for whoever teaches it

**Error direction depends on the graph and endpoint.** Merging nodes can combine
partner lists, remove self-edges or collapse duplicate edges. Splitting can remove
or redistribute connections. Neither a universal upward motif bias nor cancellation
is guaranteed. Demonstrate a concrete perturbation and state what it changes.

**Parts A and B join at the error-sensitivity check.** The validation sample informs
an error model; perturbing the graph then shows how the endpoint behaves under that
model. Rates alone do not specify which nodes or edges are wrong. The resulting
spread is conditional sensitivity, not automatically a confidence interval.

**The NeuroAI section is written to prevent two errors, not one.** Dismissing the connection and overselling it are both wrong. The accurate position — machine learning has given connectomics far more than the reverse — is specific, defensible, and slightly boring, which is usually the sign that it is right.

## Licence and credit

**CC BY-SA 4.0.** Teach from this lecture anywhere, including commercially; copy and
redistribute it in any medium; and re-cut, shorten, translate, or merge it into your own
material. No permission needed. Two conditions: credit the original and say if you
changed anything, and distribute your adapted version under
[the same licence]({{ '/teaching/lectures/' | relative_url }}#licence).

> Gray Roncal, W. (2026). *Nanoscale Connectomics: Algorithms and Applications* (EN.585.781 Frontiers in Neuroengineering,
> Module 9). NeuroTrailblazers. CC BY-SA 4.0.
> https://neurotrailblazers.org/teaching/lectures/

For an adaptation, prefix with *"Adapted from"* and note what you changed.

The H01 cover image retains **CC BY 4.0**, with credit to Lichtman Lab / Harvard
and Connectomics at Google, Shapson-Coe et al. (2024), doi:10.1126/science.adk4858.
Preserve that separate attribution when adapting the deck.

Found something wrong or out of date — or built a version worth sharing back?
[Open an issue](https://github.com/wrgr/neurotrailblazers/issues).

## Related

- [Series overview]({{ '/teaching/lectures/' | relative_url }})
- [Lecture 1: Introduction to Connectomics]({{ '/teaching/lectures/connectomics-01-introduction/' | relative_url }})
- [Lecture 2: Tools and Methods]({{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }})
- [Technical training units]({{ '/technical-training/' | relative_url }}) — the long-form material behind these slides
- [Journal club]({{ '/technical-training/journal-club/' | relative_url }}) — papers and discussion prompts
