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
