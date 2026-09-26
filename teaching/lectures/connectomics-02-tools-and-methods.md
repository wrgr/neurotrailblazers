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
---

*Lecture 2 of the [connectomics lecture series]({{ '/teaching/lectures/' | relative_url }}).
56 slides in three parts, about 150 minutes. Openly licensed under **CC BY-SA 4.0**.*

<div class="resource-card">
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/en585781/module08-tools-and-methods.html' | relative_url }}">Open the deck (HTML)</a>
    <a class="resource-link" href="https://github.com/wrgr/neurotrailblazers/blob/main/course/decks/marp/en585781/module08-tools-and-methods.marp.md">Slide source (Markdown)</a>
    <a class="resource-link" href="{{ '/teaching/lectures/' | relative_url }}">Series overview</a>
    <a class="resource-link" href="{{ '/teaching/lectures/tools-and-methods-activity/' | relative_url }}">Learner worksheet and offline query</a>
    <a class="resource-link" href="{{ '/teaching/lectures/tools-and-methods-answers/' | relative_url }}">Instructor model responses</a>
  </div>
  <p><small>The HTML deck presents directly in a browser. The Markdown source carries the
  speaker notes as HTML comments and is what to edit if you want to change wording.
  See <a href="{{ '/teaching/lectures/' | relative_url }}#formats">Formats</a> for PowerPoint and Google Slides.</small></p>
</div>

## Learning objectives

By the end of this lecture, participants will be able to:

1. **Identify** the tools and formats used for nanoscale acquisition, storage, and serving.
2. **Trace** an artifact in a reconstruction back to the pipeline stage that produced it.
3. **Apply** reproducible-pipeline principles to a query against a public connectomics volume.
4. **Estimate** the capacity, compute, and labor cost of a proposed acquisition.

## Teach a 90-minute session

This selected-slide route follows Introduction and Synapse Detection in the
[four-session block]({{ '/teaching/sequence/' | relative_url }}). It uses the existing
56-slide deck and embedded notes. It is Session 3 in that block, but
Lecture 2 / Module 8 in the original graduate course. Slide numbers include the cover.

**Outcome:** learners produce an auditable methods record, reproduce a small
versioned count, and estimate raw storage with stated assumptions. The full lecture's
public-volume notebook remains an optional extension, not a requirement for this session.

**Preparation:** read the worksheet/key, open the deck and provide calculators.
The paper activity needs no login or programming. For the optional code route,
download the linked standalone Python 3 script before class and test both snapshots.
Keep a copy of its output available if a learner cannot run Python. It contains only
invented records and does not query a public service.

- **0–10 min, slides 1–3, 6:** revisit the previous study brief. Ask which pipeline
  artifact supplies its measurement. Distinguish an image, a segmentation and a
  synapse table before naming software.
- **10–20 min, slides 9–10, 19, 21–22, 31:** diagnose a preparation/artifact scenario.
  Slide 31's table pairs each defect signature with the stage that produced it.
  Ask what observation distinguishes a tissue-depth effect from a processing-grid
  effect, and which QA gate would detect it before more acquisition.
- **20–30 min, slides 26–27, 33–35:** explain derived artifacts and byte accounting.
  State voxel dimensions, channels and bytes per sample before multiplying. Remind
  learners that raw capacity is not the total project budget.
- **30–40 min, slides 40, 42–46:** introduce version drift and the methods record.
  Ask “What evidence would identify the earlier inputs?” A changed count is a reason
  to inspect provenance, not proof of continued growth or improved completeness.
- **40–75 min:** pairs complete the [worksheet]({{ '/teaching/lectures/tools-and-methods-activity/' | relative_url }}).
  Allow 15 minutes for snapshots, 10 for the methods record and 10 for capacity.
  At minute 55 check whether s2's boundary score was included.
- **75–85 min, slide 51:** exchange records and reproduce the selected IDs.
  Compare with the [model responses]({{ '/teaching/lectures/tools-and-methods-answers/' | relative_url }}).
  Missing metadata is an outcome to report, not something to guess.
- **85–90 min, slide 54:** collect the methods record and exit ticket. Learners add
  the version, filter and query identity their own endpoint needs to the study
  brief, and bring it to Algorithms and Applications.

Unselected slides are optional depth for this route; 55–56 hold sources and credit.
The full-course assignment on slide 52 is separate from the offline worksheet.
The broader 150-minute route below covers acquisition choices and infrastructure
in more detail. Do not describe the short exercise as a completed public-data analysis.

**Assessment:** use the answer key's four-dimension rubric. A reproducible count
can still be biologically biased; the non-claim and quality checks remain required.

## Structure

### Part A: From tissue to voxels

The preparation chain step by step with the failure each step produces, sectioning and imaging families, the dose budget, and the QA gates that stop acquisition.

### Part B: Storage, infrastructure, and what it costs

The eight-stage reference pipeline, chunked multi-resolution arrays, chunk shape as an access-pattern decision, and a worked capacity and cost model.

### Part C: Reproducible pipelines

Why object IDs are not stable, the ChunkedGraph and materialization versions, the reproducibility header, and the platform landscape.

## What students produce

A **reproducible query** against a public volume: a notebook carrying a six-line reproducibility header, a pinned materialization version, stated inclusion criteria, and one stated limitation. It must run end to end from a clean environment.

## The centerpiece

The version problem in Part C. In the hypothetical example, a figure reports 1,412
input synapses and a rerun returns 1,530 for “the same cell.” The discrepancy alone
does not establish which result is correct or why it changed. Students must inspect
the versions, object lineage, query and archived inputs before interpreting it.

## Notes for whoever teaches it

**The diagnostic question runs through the whole lecture.** For any defect: which coordinate system does it live in: block position, anatomy, acquisition time, or the processing grid? That single question identifies the stage that produced it, and it is the transferable skill here.

**The staining-gradient case is worth dwelling on.** A depth-dependent staining gradient runs in the same direction as cortical layer depth. A team that does not check the coordinate system can publish a "laminar difference in synapse density" that is entirely a penetration artifact. Ask the room how they would distinguish the two.

**Make them physically add the reproducibility header.** It takes ninety seconds and is the habit from this lecture most worth keeping. Few people adopt it until an unreproducible number has cost them time, so have them write it in class. The assignment on slide 52 grades it.

## License and credit

**CC BY-SA 4.0.** Teach from this lecture anywhere, including commercially; copy and
redistribute it in any medium; and re-cut, shorten, translate, or merge it into your own
material. No permission needed. Two conditions: credit the original and say if you
changed anything, and distribute your adapted version under
[the same license]({{ '/teaching/lectures/' | relative_url }}#license).

> Gray-Roncal, W. (2026). *Nanoscale Connectomics: Tools and Methods* (EN.585.781 Frontiers in Neuroengineering,
> Module 8). NeuroTrailblazers. CC BY-SA 4.0.
> https://neurotrailblazers.org/teaching/lectures/

For an adaptation, prefix with *"Adapted from"* and note what you changed.

The H01 cover image retains **CC BY 4.0**, with credit to Lichtman Lab / Harvard
and Connectomics at Google, Shapson-Coe et al. (2024), doi:10.1126/science.adk4858.
Preserve that separate attribution when adapting the deck.

Found something wrong or out of date, or built a version worth sharing back?
[Open an issue](https://github.com/wrgr/neurotrailblazers/issues).

## Related

- [Series overview]({{ '/teaching/lectures/' | relative_url }})
- [Lecture 1: Introduction to Connectomics]({{ '/teaching/lectures/connectomics-01-introduction/' | relative_url }})
- [Lecture 3: Algorithms and Applications]({{ '/teaching/lectures/connectomics-03-algorithms-and-applications/' | relative_url }})
- [Technical training units]({{ '/technical-training/' | relative_url }}): the long-form material behind these slides
- [Journal club]({{ '/technical-training/journal-club/' | relative_url }}): papers and discussion prompts
