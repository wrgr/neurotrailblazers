---
layout: page
title: "Presentation Decks"
permalink: /technical-training/slides/
slug: technical-training-slides
content_type: delivery
---

Open a deck to present it in your browser. Choose a graduate lecture for a longer
class, a technical-unit deck for a focused session, or a module session kit for
slides paired with activities and worksheets.

**Need a complete taught session?** Start with [the short lecture sequence]({{ '/teaching/sequence/' | relative_url }}):
timed plans, slides, learner activities and model responses for Introduction to
Connectomics, Synapse Detection, Tools and Methods, and Algorithms and Applications.

- [Graduate lectures](#ready-to-present-graduate-lectures)
- [Standalone graduate lectures](#standalone-graduate-lectures-from-the-reference-layer)
- [Technical-unit decks](#technical-unit-decks)
- [Module decks and activities]({{ '/teaching/sessions/' | relative_url }})

## Ready-to-present graduate lectures

Three finished decks exist for the connectomics block of EN.585.781, Frontiers in
Neuroengineering. These are **presentation decks**: 56&ndash;59
slides each, a custom lecture-hall theme, DOI-pinned citations, and a CC BY-SA 4.0 footer. One
discovery pipeline &mdash; question, specimen, image, reconstruction, graph, claim &mdash; runs
through all three, and eight progression streams introduced in the first are revisited as a
scorecard at the end of the third. They draw on units 01&ndash;04, 08 and 09.

<div class="cards-grid">
  <article class="card">
    <h3 class="card-title"><a href="{{ '/course/decks/marp/out/en585781/module07-introduction-to-connectomics.html' | relative_url }}">Introduction to connectomics</a></h3>
    <p class="card-description">The case for mapping &middot; three scales &middot; the field as it stands. 59 slides.</p>
    <p><a href="{{ '/teaching/lectures/connectomics-01-introduction/' | relative_url }}">Teaching plan, worksheet and answers</a> · <a href="{{ site.deck_source_base }}/en585781/module07-introduction-to-connectomics.marp.md">Markdown source</a></p>
  </article>
  <article class="card">
    <h3 class="card-title"><a href="{{ '/course/decks/marp/out/en585781/module08-tools-and-methods.html' | relative_url }}">Tools and methods</a></h3>
    <p class="card-description">Tissue to voxels &middot; storage and infrastructure &middot; reproducible pipelines. 56 slides.</p>
    <p><a href="{{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }}">Teaching plan, worksheet and answers</a> · <a href="{{ site.deck_source_base }}/en585781/module08-tools-and-methods.marp.md">Markdown source</a></p>
  </article>
  <article class="card">
    <h3 class="card-title"><a href="{{ '/course/decks/marp/out/en585781/module09-algorithms-and-applications.html' | relative_url }}">Algorithms and applications</a></h3>
    <p class="card-description">Segmentation, error and labour &middot; graph construction and nulls &middot; applications and NeuroAI. 58 slides.</p>
    <p><a href="{{ '/teaching/lectures/connectomics-03-algorithms-and-applications/' | relative_url }}">Teaching plan, worksheet and answers</a> · <a href="{{ site.deck_source_base }}/en585781/module09-algorithms-and-applications.marp.md">Markdown source</a></p>
  </article>
</div>

These are numbered 7&ndash;9 as lectures within that graduate course. They are not curriculum
modules 07&ndash;09, which are Proofreading, Hypothesis Testing and Morphology.

## Standalone graduate lectures from the reference layer

Two further presentation decks, built in the same theme and to the same standard, but not part
of EN.585.781 or any other course. Each is drawn entirely from one content-library page, carries
that page's numbers and citations, and ends with a slide stating what the page does not cover.
Both are sized for a single 50&ndash;60 minute lecture and carry the same CC BY-SA 4.0 licence
and speaker notes as the decks above.

<div class="cards-grid">
  <article class="card">
    <h3 class="card-title"><a href="{{ '/course/decks/marp/out/lectures/synapse-detection.html' | relative_url }}">Synapse detection</a></h3>
    <p class="card-description">Three problems and the published record &middot; benchmarks and the sign problem &middot; using somebody else's synapse table. 39 slides, from <a href="{{ '/content-library/infrastructure/synapse-detection/' | relative_url }}">Synapse Detection</a>.</p>
    <p><a href="{{ '/teaching/lectures/synapse-detection/' | relative_url }}">Teaching plan, worksheet and answers</a> · <a href="{{ site.deck_source_base }}/lectures/synapse-detection.marp.md">Markdown source</a></p>
  </article>
  <article class="card">
    <h3 class="card-title"><a href="{{ '/course/decks/marp/out/lectures/ethics-and-governance.html' | relative_url }}">Connectomics ethics and governance</a></h3>
    <p class="card-description">Human tissue: consent and de-identification &middot; licences &middot; dual use and credit for proofreading. 31 slides, from <a href="{{ '/content-library/connectomics/ethics-and-governance/' | relative_url }}">Ethics and Governance</a>.</p>
    <p><a href="{{ '/teaching/lectures/ethics-and-governance/' | relative_url }}">Teaching plan, worksheet and answers</a> · <a href="{{ site.deck_source_base }}/lectures/ethics-and-governance.marp.md">Markdown source</a></p>
  </article>
</div>

Need full module teaching kits? Visit the [Teaching Hub]({{ '/teaching/' | relative_url }}).

## Technical-unit decks

<div class="cards-grid">
  {% for item in site.data.technical_track.modules %}
  {% assign deck = item.slug %}
  <article class="card">
    <h3 class="card-title"><a href="{{ '/course/decks/marp/out/' | append: deck | append: '.html' | relative_url }}">{{ item.title }}</a></h3>
    <p class="card-description">Presentation slides with speaker notes and figure sources.</p>
    <p><a href="{{ '/technical-training/slides/' | append: item.slug | append: '/' | relative_url }}">Instructor lecture plan</a> — sequence, timing, and teaching prompts.</p>
    <p><a href="{{ '/technical-training/' | append: item.slug | append: '/' | relative_url }}">Open unit page</a></p>
    <p><a href="{{ '/course/decks/marp/out/' | append: deck | append: '.html' | relative_url }}">Open rendered deck (HTML)</a> | <a href="{{ site.deck_source_base }}/{{ deck }}.marp.md">Markdown source</a></p>
  </article>
  {% endfor %}
</div>

## Lecture plans for the technical track

The instructor plans linked beside each technical deck describe a proposed teaching
sequence, timing, and activities. They are planning documents; their sequence can
differ from the presentation deck. Learners should use the linked unit pages.

## Rendered decks and slide sources

Each deck links to its editable Markdown source. Contributors can render HTML with
`./scripts/render_marp.sh`, or export PowerPoint with `./scripts/render_marp.sh --pptx`.
