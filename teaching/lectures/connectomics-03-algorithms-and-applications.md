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
58 slides in three parts, about 150 minutes. Openly licensed — **CC BY-ND 4.0**.*

## What this lecture covers

Segmentation and its error taxonomy, proofreading triage, graph construction and null models, and an honest account of what connectomics and machine learning give each other.

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/en585781/module09-algorithms-and-applications.html' | relative_url }}">Open the deck (HTML)</a>
    <a class="resource-link" href="https://github.com/wrgr/neurotrailblazers/blob/main/course/decks/marp/en585781/module09-algorithms-and-applications.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/teaching/lectures/' | relative_url }}">Series overview</a>
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

## Structure

### Part A — Segmentation, error, and the labor problem

How automated segmentation works and where it fails structurally, the error taxonomy, quality metrics and their blind spots, and triage by endpoint change per annotator-minute.

### Part B — From segmentation to a defensible graph

Six consequential construction choices, null models, the triad census, merge-error bias, and the error-sensitivity check.

### Part C — Applications, NeuroAI, and what to claim

Comparative connectomics, cell typing, three results that actually landed, and the two symmetric errors about connectomics and machine learning.

## What students produce

An **analysis card**: hypothesis, estimand, graph provenance block, null model with the "it would be uninteresting if…" sentence written out, success criterion set in advance, error band from measured merge and split rates, non-claim, and provenance.

## The centrepiece

The reciprocity worked example in Part B, across three slides. The same data — 100 neurons, 1,200 edges, 210 reciprocal pairs — supports "2.9-fold enrichment, p < 10⁻⁶" under Erdős–Rényi, "1.4×, z = 5.0" under a degree-preserving null, and "no detectable effect" once distance is preserved too. Nothing about the data changed; only the question did.

## Notes for whoever teaches it

**Merge bias points toward the interesting answer.** A merge fuses two neurons' partner lists and manufactures triangles among partners never connected through one cell, so merges inflate dense motifs superlinearly while splits deflate everything proportionally. The errors do not cancel. Motif analysis on unproofread segmentation is not conservative — it is biased toward the result you were hoping for.

**Parts A and B join at the error-sensitivity check.** The Part A resample gives you measured merge and split rates; the Part B check turns them into an error bar on the motif claim. Neither half is useful alone, and students tend to treat them as separate topics until this is pointed out.

**The NeuroAI section is written to prevent two errors, not one.** Dismissing the connection and overselling it are both wrong. The accurate position — machine learning has given connectomics far more than the reverse — is specific, defensible, and slightly boring, which is usually the sign that it is right.

## Licence and credit

**CC BY-ND 4.0.** Teach from this lecture anywhere, including commercially; copy and
redistribute it in any medium; present it unmodified. No permission needed. Publicly
distributing a modified version is not permitted — but
[ask]({{ '/teaching/lectures/' | relative_url }}#licence), because the project would
rather grant permission than have the material go unused.

> Gray Roncal, W. (2026). *Nanoscale Connectomics: Algorithms and Applications* (EN.585.781 Frontiers in Neuroengineering,
> Module 9). NeuroTrailblazers. CC BY-ND 4.0.
> https://neurotrailblazers.org/teaching/lectures/

Found something wrong or out of date?
[Open an issue](https://github.com/wrgr/neurotrailblazers/issues).

## Related

- [Series overview]({{ '/teaching/lectures/' | relative_url }})
- [Lecture 1: Introduction to Connectomics]({{ '/teaching/lectures/connectomics-01-introduction/' | relative_url }})
- [Lecture 2: Tools and Methods]({{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }})
- [Technical training units]({{ '/technical-training/' | relative_url }}) — the long-form material behind these slides
- [Journal club]({{ '/technical-training/journal-club/' | relative_url }}) — papers and discussion prompts
