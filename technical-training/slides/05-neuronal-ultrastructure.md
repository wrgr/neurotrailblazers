---
layout: page
title: "Lecture Plan: Neuronal Ultrastructure"
permalink: /technical-training/slides/05-neuronal-ultrastructure/
slug: slides-05-neuronal-ultrastructure
---

## What this document is

This page is a **build plan for an instructor assembling a lecture** on this unit. It gives the
slide sequence, per-slide timing, the points at which figures belong, and the speaker notes that
carry the argument. It is a design document, not a rendered deck: there are no slides on this
page to project, and nothing here is written to be shown to learners as it stands.

A separately maintained Marp deck for this unit does exist, and it is linked at the foot of this
page under *Rendered deck artifacts*. That deck was authored in its own right and does not follow
this plan slide for slide, so treat this page as the teaching design and the Marp file as one
existing implementation of it. The learner-facing material is the unit page linked under
*Connections*.

## Session profile
- Audience: annotators, proofreaders, and analysts needing ultrastructure fluency.
- Duration: 75 minutes lecture + 20 minutes image annotation drill.
- Output: labeled cue sheet with confidence scores and ambiguity notes.

## Slide-by-slide lecture plan
1. Slide 1 (2 min): Title and practical stakes
2. Slide 2 (5 min): Ultrastructure as operational language
3. Slide 3 (6 min): Compartment refresher
   - Soma, dendrite, axon, boutons, spines.
4. Slide 4 (6 min): Synapse architecture essentials
   - Vesicles, active zone, PSD, cleft context.
5. Slide 5 (6 min): Organelle cues
   - Mitochondria, ER, microtubules in context.
6. Slide 6 (6 min): Multi-slice evidence protocol
7. Slide 7 (7 min): Worked example I
   - Easy compartment call with converging evidence.
8. Slide 8 (7 min): Worked example II
   - Ambiguous case and confidence annotation.
9. Slide 9 (6 min): Annotation disagreement analysis
10. Slide 10 (5 min): Frequent error modes
11. Slide 11 (5 min): QC metrics for ultrastructure calls
12. Slide 12 (5 min): Standardized decision log template
13. Slide 13 (7 min): Hands-on labeling prompt
14. Slide 14 (7 min): Debrief and bridge to process classification.

## Figure integration points
- Primary shortlist: `course/units/figures/05-neuronal-ultrastructure-selected-v1.md`.
- Use at least three cue-comparison panels and one ambiguity panel.

## Speaker notes (expert-level)
- Require cue triangulation (morphology + organelle + context) before hard labels.
- Keep uncertain labels explicit; uncertainty is signal, not failure.

## Assessment and artifacts
- Deliverable: cue-based annotation sheet with confidence tiers.
- Rubric dimensions: evidence quality, consistency, and uncertainty handling.

## Connections
- Unit page: [Neuronal Ultrastructure]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }})
- Journal club: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dictionary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Existing module overlap: [module04]({{ '/modules/module04/' | relative_url }}), [module09]({{ '/modules/module09/' | relative_url }}), [module11]({{ '/modules/module11/' | relative_url }})

## Rendered deck artifacts
<div class="resource-card">
  <p>These are the separately maintained Marp deck artifacts for this unit. They are not generated from the plan above, so their sequence and timing differ from it.</p>
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/' | append: page.slug | remove: 'slides-' | append: '.html' | relative_url }}">Open HTML Deck</a>
    <a class="resource-link" href="{{ '/course/decks/marp/out/' | append: page.slug | remove: 'slides-' | append: '.pptx' | relative_url }}">Download PowerPoint (.pptx)</a>
    <a class="resource-link" href="{{ '/technical-training/' | append: page.slug | remove: 'slides-' | append: '/' | relative_url }}">Open Unit Page</a>
  </div>
  <p><strong>Marp source path:</strong> <code>course/decks/marp/{{ page.slug | remove: "slides-" }}.marp.md</code></p>
  <p><strong>Batch render helper:</strong> <code>./scripts/render_marp.sh</code></p>
</div>