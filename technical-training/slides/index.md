---
layout: page
title: "Technical Training Lecture Plans"
permalink: /technical-training/slides/
slug: technical-training-slides
content_type: delivery
---

## Lecture plans for the technical track
These pages are **instructor build plans**, one for each technical-training unit. Each gives a
slide-by-slide sequence with per-slide timing, the points where figures belong, expert-level
speaker notes, and the artifact the session should produce.

They are design documents, not rendered decks. Nothing on these pages is projectable as it
stands, and they are not written for learners — the learner-facing material is the unit page,
linked from each plan.

Each plan contains:
- Session profile (audience, duration, expected output).
- Slide-by-slide sequence with timing and technical talking points.
- Figure integration points, keyed to the extracted asset shortlists.
- Assessment artifacts and rubric dimensions.

## Rendered decks and slide sources
A separate set of Marp decks exists for these units. They are maintained alongside the plans
rather than generated from them, so their slide sequence and timing differ from the plan on the
matching page.

- Marp sources: `course/decks/marp/`
- Reference guide: `course/decks/marp/README.md`
- Rendered HTML: `course/decks/marp/out/` (committed, and what the site links to)
- Batch render helper: `./scripts/render_marp.sh` &mdash; add `--pptx` for PowerPoint,
  which is not committed because the full set runs to tens of megabytes

## Ready-to-present graduate lectures

Three finished decks exist for the connectomics block of EN.585.781, Frontiers in
Neuroengineering. Unlike the build plans above, these are **presentation decks**: 56&ndash;59
slides each, a custom lecture-hall theme, DOI-pinned citations, and a CC BY-SA 4.0 footer. One
discovery pipeline &mdash; question, specimen, image, reconstruction, graph, claim &mdash; runs
through all three, and eight progression streams introduced in the first are revisited as a
scorecard at the end of the third. They draw on units 01&ndash;04, 08 and 09.

<div class="cards-grid">
  <article class="card">
    <h3 class="card-title"><a href="{{ '/course/decks/marp/out/en585781/module07-introduction-to-connectomics.html' | relative_url }}">Introduction to connectomics</a></h3>
    <p class="card-description">The case for mapping &middot; three scales &middot; the field as it stands. 59 slides.</p>
    <p><a href="{{ site.deck_source_base }}/en585781/module07-introduction-to-connectomics.marp.md">Markdown source</a></p>
  </article>
  <article class="card">
    <h3 class="card-title"><a href="{{ '/course/decks/marp/out/en585781/module08-tools-and-methods.html' | relative_url }}">Tools and methods</a></h3>
    <p class="card-description">Tissue to voxels &middot; storage and infrastructure &middot; reproducible pipelines. 56 slides.</p>
    <p><a href="{{ site.deck_source_base }}/en585781/module08-tools-and-methods.marp.md">Markdown source</a></p>
  </article>
  <article class="card">
    <h3 class="card-title"><a href="{{ '/course/decks/marp/out/en585781/module09-algorithms-and-applications.html' | relative_url }}">Algorithms and applications</a></h3>
    <p class="card-description">Segmentation, error and labour &middot; graph construction and nulls &middot; applications and NeuroAI. 58 slides.</p>
    <p><a href="{{ site.deck_source_base }}/en585781/module09-algorithms-and-applications.marp.md">Markdown source</a></p>
  </article>
</div>

These are numbered 7&ndash;9 as lectures within that graduate course. They are not curriculum
modules 07&ndash;09, which are Proofreading, Hypothesis Testing and Morphology.

Need full module teaching kits? Visit the [Teaching Hub]({{ '/teaching/' | relative_url }}).

<div class="cards-grid">
  {% for item in site.data.technical_track.modules %}
  {% assign deck = item.slug %}
  <article class="card">
    <h3 class="card-title"><a href="{{ '/technical-training/slides/' | append: item.slug | append: '/' | relative_url }}">{{ item.title }}</a></h3>
    <p class="card-description">Instructor build plan: slide sequence, timing, figure placement, speaker notes, and the session artifact.</p>
    <p><a href="{{ '/technical-training/' | append: item.slug | append: '/' | relative_url }}">Open unit page</a></p>
    <p><a href="{{ '/course/decks/marp/out/' | append: deck | append: '.html' | relative_url }}">Open rendered deck (HTML)</a> | <a href="{{ site.deck_source_base }}/{{ deck }}.marp.md">Markdown source</a></p>
  </article>
  {% endfor %}
</div>
