---
layout: page
title: "Lecture 2: Tools and Methods"
description: "How tissue becomes a queryable petascale dataset: preparation and its artifact signatures, storage and infrastructure, and the versioning that makes a result reproducible."
permalink: /teaching/lectures/connectomics-02-tools-and-methods/
slug: lecture-connectomics-02-tools-and-methods
track: core-concepts-methods
content_type: delivery
pathways:
  - classroom delivery
  - graduate teaching
summary: "How tissue becomes a queryable petascale dataset, and what makes a result reproducible."
use_layout_hero: false
---

*Lecture 2 of the [connectomics lecture series]({{ '/teaching/lectures/' | relative_url }}).
56 slides in three parts, about 150 minutes. Openly licensed — **CC BY-SA 4.0**.*

## What this lecture covers

How tissue becomes a queryable petascale dataset: preparation and its artifact signatures, storage and infrastructure, and the versioning that makes a result reproducible.

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/en585781/module08-tools-and-methods.html' | relative_url }}">Open the deck (HTML)</a>
    <a class="resource-link" href="https://github.com/wrgr/neurotrailblazers/blob/main/course/decks/marp/en585781/module08-tools-and-methods.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/teaching/lectures/' | relative_url }}">Series overview</a>
  </div>
  <p><small>The HTML deck presents directly in a browser. The Markdown source carries the
  speaker notes as HTML comments and is what to edit if you want to change wording —
  see <a href="{{ '/teaching/lectures/' | relative_url }}#formats">Formats</a> for PowerPoint and Google Slides.</small></p>
</div>

## Learning objectives

By the end of this lecture, participants will be able to:

1. **Identify** the tools and formats used for nanoscale acquisition, storage, and serving.
2. **Trace** an artifact in a reconstruction back to the pipeline stage that produced it.
3. **Apply** reproducible-pipeline principles to a query against a public connectomics volume.
4. **Estimate** the capacity, compute, and labor cost of a proposed acquisition.

## Structure

### Part A — From tissue to voxels

The preparation chain step by step with the failure each step produces, sectioning and imaging families, the dose budget, and the QA gates that stop acquisition.

### Part B — Storage, infrastructure, and what it costs

The eight-stage reference pipeline, chunked multi-resolution arrays, chunk shape as an access-pattern decision, and a worked capacity and cost model.

### Part C — Reproducible pipelines

Why object IDs are not stable, the ChunkedGraph and materialization versions, the reproducibility header, and the platform landscape.

## What students produce

A **reproducible query** against a public volume: a notebook carrying a six-line reproducibility header, a pinned materialization version, stated inclusion criteria, and one stated limitation — that runs end to end from a clean environment.

## The centrepiece

The version problem in Part C. A figure reports 1,412 input synapses; re-running the notebook returns 1,530 for "the same cell". Both numbers are correct and the paper is wrong, because it reported a version-dependent quantity without its version. This is the field's most common silent failure and students have usually never met it.

## Notes for whoever teaches it

**The diagnostic question runs through the whole lecture.** For any defect: which coordinate system does it live in — block position, anatomy, acquisition time, or the processing grid? That single question identifies the stage that produced it, and it is the transferable skill here.

**The staining-gradient case is worth dwelling on.** A depth-dependent staining gradient runs in the same direction as cortical layer depth. A team that does not check the coordinate system can publish a "laminar difference in synapse density" that is entirely a penetration artifact. Ask the room how they would distinguish the two.

**Make them physically add the reproducibility header.** It takes ninety seconds, it is the highest-value habit in the lecture, and essentially nobody adopts it until they have been burned once. The assignment rubric awards points for it explicitly.

## Licence and credit

**CC BY-SA 4.0.** Teach from this lecture anywhere, including commercially; copy and
redistribute it in any medium; and re-cut, shorten, translate, or merge it into your own
material. No permission needed. Two conditions: credit the original and say if you
changed anything, and distribute your adapted version under
[the same licence]({{ '/teaching/lectures/' | relative_url }}#licence).

> Gray Roncal, W. (2026). *Nanoscale Connectomics: Tools and Methods* (EN.585.781 Frontiers in Neuroengineering,
> Module 8). NeuroTrailblazers. CC BY-SA 4.0.
> https://neurotrailblazers.org/teaching/lectures/

For an adaptation, prefix with *"Adapted from"* and note what you changed.

Found something wrong or out of date — or built a version worth sharing back?
[Open an issue](https://github.com/wrgr/neurotrailblazers/issues).

## Related

- [Series overview]({{ '/teaching/lectures/' | relative_url }})
- [Lecture 1: Introduction to Connectomics]({{ '/teaching/lectures/connectomics-01-introduction/' | relative_url }})
- [Lecture 3: Algorithms and Applications]({{ '/teaching/lectures/connectomics-03-algorithms-and-applications/' | relative_url }})
- [Technical training units]({{ '/technical-training/' | relative_url }}) — the long-form material behind these slides
- [Journal club]({{ '/technical-training/journal-club/' | relative_url }}) — papers and discussion prompts
