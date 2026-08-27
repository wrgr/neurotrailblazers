---
layout: page
title: "Connectomics Lecture Series"
description: "Three full lectures on nanoscale connectomics, openly licensed for community use: slides, speaker notes, run-of-show, and assignments."
permalink: /teaching/lectures/
slug: lectures-index
track: core-concepts-methods
content_type: delivery
pathways:
  - classroom delivery
  - graduate teaching
summary: "Three ready-to-teach connectomics lectures, CC BY-SA 4.0."
use_layout_hero: false
---

## What this is

Three complete graduate lectures on nanoscale connectomics, released for anyone to
teach. Each is roughly 150 minutes of material in three parts of about 50 minutes, with
speaker notes, in-class discussion prompts, and a graded artifact.

They were written for **EN.585.781 Frontiers in Neuroengineering** at Johns Hopkins,
where they run as modules 7–9. Nothing in them depends on that course: the sequence is
self-contained and assumes only introductory neuroscience.

This is a different kind of page from the
[technical training slides]({{ '/technical-training/slides/' | relative_url }}), which
are *build plans* for an instructor assembling their own lecture. These are the
lectures themselves — written to be projected.

---

## The three lectures

<div class="cards-grid">
  <article class="card">
    <h3><a href="{{ '/teaching/lectures/connectomics-01-introduction/' | relative_url }}">1 &middot; Introduction to Connectomics</a></h3>
    <p class="card-description"><strong>59 slides.</strong> Why synapse-resolution structure needs electron microscopy, what a wiring diagram can and cannot establish, the three scales, and the state of the field through 2025.</p>
  </article>
  <article class="card">
    <h3><a href="{{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }}">2 &middot; Tools and Methods</a></h3>
    <p class="card-description"><strong>56 slides.</strong> How tissue becomes a queryable petascale dataset: preparation and its artifacts, storage and infrastructure, and the versioning that makes a result reproducible.</p>
  </article>
  <article class="card">
    <h3><a href="{{ '/teaching/lectures/connectomics-03-algorithms-and-applications/' | relative_url }}">3 &middot; Algorithms and Applications</a></h3>
    <p class="card-description"><strong>58 slides.</strong> Segmentation and its error taxonomy, proofreading triage, graph construction and null models, and an honest account of connectomics and machine learning.</p>
  </article>
</div>

---

## What holds the three together

**One discovery pipeline.** Question → specimen → image → reconstruction → graph →
claim. The same diagram opens every lecture, marked to show which columns that lecture
owns. Students learn to read it left to right as how a dataset is built, and right to
left as how you debug a number you do not believe.

**Eight progression streams.** Scale; throughput and automation; segmentation quality;
modality integration; organism and lifespan coverage; structure → function; openness and
community; translation and people. Introduced in lecture 1, tagged into the milestone
table, and revisited as a scorecard at the end of lecture 3. The point is that progress
in this field is not one curve, and that reading a paper by asking *which stream does
this advance* is more useful than ranking it.

**One claim discipline.** Every connectivity claim sorts into evidence supported by
structure alone, structure plus a declared assumption, or not supportable by structure
at all. It is introduced in lecture 1 and is what the lecture 3 lab is graded against.

**A note on scope.** Diffusion MRI and X-ray microtomography appear once, as the example
that different questions need different instruments. These lectures are about what only
synapse-resolution structure can establish.

---

## Teaching from them

**Timing.** Three parts of roughly 50 minutes, with natural breaks at the part dividers.
A 90-minute slot takes Parts A and B; Part C works as a standalone seminar. A single
75-minute survey can be built from lecture 1 Part A plus lecture 3 Part C.

**What students produce.** One artifact per lecture, each building on the last:

| Lecture | Artifact | What it must contain |
|---|---|---|
| 1 | Study brief | A measurable endpoint, a null model, an explicit non-claim |
| 2 | Reproducible query | A pinned materialization version, stated inclusion criteria, one stated limitation |
| 3 | Analysis card | Hypothesis, estimand, null model, success criterion, error band, non-claim, provenance |

**Prerequisites.** Introductory neuroscience helps and is not required. Lecture 2's
assignment assumes basic Python; the lecture itself does not.

**No data or accounts needed to teach.** The lectures reference public platforms —
neuPrint, FlyWire Codex, BossDB, CAVE — but nothing in the slides requires a login. The
lecture 2 assignment does.

---

## Formats

Each lecture page links its rendered HTML deck, which presents directly in a browser.
The Marp markdown source is the version to take if you want to work with the text —
speaker notes are in the source as HTML comments and export to PowerPoint notes.

For **Google Slides**, render to PowerPoint and use *File → Import slides*. Be aware
that Marp's PowerPoint export renders each slide as an image, so text is not editable in
Slides. If you want to change wording, edit the markdown and re-render.

```bash
git clone https://github.com/wrgr/neurotrailblazers
cd neurotrailblazers
npm install --no-save @marp-team/marp-cli
./scripts/render_marp.sh --pptx
```

Exports land in `course/decks/marp/out/en585781/`.

---

## Licence

**Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).**
<https://creativecommons.org/licenses/by-sa/4.0/>

**You may** teach from these lectures in any setting, including commercially; copy and
redistribute them in any medium; and **re-cut, shorten, translate, restyle, or merge them
into your own material** — and distribute the result. No permission needed.

**Two conditions.** *Attribution* — credit the original, link the licence, and indicate
whether you changed anything. *ShareAlike* — if you adapt the material, distribute your
version under this same licence, so adaptations stay as open as what they were built
from.

**How to credit:**

> Gray Roncal, W. (2026). *Introduction to Connectomics* (EN.585.781 Frontiers in
> Neuroengineering, Module 7). NeuroTrailblazers. CC BY-SA 4.0.
> https://neurotrailblazers.org/teaching/lectures/

For an adaptation, prefix with *"Adapted from"* and note what you changed. A credit line
on a title slide or in a syllabus is sufficient.

**If your adaptation improves the teaching**, the project would like to hear about it —
[open an issue](https://github.com/wrgr/neurotrailblazers/issues). Re-cut versions for
different course lengths are exactly the thing worth sharing back.

**On the contents.** These decks contain no third-party figures — they are text, tables,
and ASCII diagrams — so redistributing or adapting them raises no image-licensing
questions, and nothing in them is encumbered by a licence incompatible with ShareAlike.
They cite published work extensively; citation is not reproduction, and the cited papers
carry their own licences. If you add figures to an adaptation, check they are compatible
with CC BY-SA 4.0 before distributing it.

---

## Corrections

The field moves quickly, and "state of the field" claims age. If you find something
wrong or out of date, please
[open an issue](https://github.com/wrgr/neurotrailblazers/issues) — corrections from
people teaching this material are the most useful kind.

## Related

- [Technical training units]({{ '/technical-training/' | relative_url }}) — the long-form
  material these lectures were built from
- [Lecture plans]({{ '/technical-training/slides/' | relative_url }}) — build plans for
  assembling your own lecture on a unit
- [Journal club]({{ '/technical-training/journal-club/' | relative_url }}) — papers with
  discussion prompts, for the assigned readings
- [Teaching hub]({{ '/teaching/' | relative_url }}) — module session kits and the
  facilitator guide
