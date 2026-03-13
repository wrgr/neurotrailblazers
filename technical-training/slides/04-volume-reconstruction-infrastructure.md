---
layout: page
title: "Slide Deck Draft: Volume Reconstruction Infrastructure"
permalink: /technical-training/slides/04-volume-reconstruction-infrastructure/
slug: slides-04-volume-reconstruction-infrastructure
---

## Session profile
- Audience: technical leads and trainees operating reconstruction pipelines.
- Duration: 80 minutes lecture + 10 minutes architecture critique.
- Output: pipeline architecture diagram with release and rollback policy.

## Slide-by-slide lecture plan
1. Slide 1 (2 min): Title and architecture mindset
2. Slide 2 (5 min): Why connectomics is a systems problem
3. Slide 3 (6 min): Reference architecture overview
   - Ingest, transform, inference, post-process, serving.
4. Slide 4 (6 min): Data contracts between stages
5. Slide 5 (6 min): Orchestration and idempotency
6. Slide 6 (6 min): Provenance schema design
7. Slide 7 (6 min): Storage and chunking strategies
8. Slide 8 (6 min): API/query layer for proofreading and analysis
9. Slide 9 (6 min): Release engineering for model updates
10. Slide 10 (6 min): SLOs and monitoring dashboards
11. Slide 11 (5 min): Failure modes
    - Non-determinism, provenance drift, hotspot bottlenecks.
12. Slide 12 (5 min): Cost-performance tradeoff framework
13. Slide 13 (5 min): Case study: bad release and rollback plan
14. Slide 14 (6 min): Bridge to biological interpretation units (05-07).

## Figure integration points
- Primary shortlist: `course/units/figures/04-volume-reconstruction-infrastructure-selected-v1.md`.
- Include one pipeline diagram and one QC dashboard mockup.

## Speaker notes (expert-level)
- Treat reproducibility as a first-class feature, not documentation afterthought.
- Show how region-scoped reprocessing prevents full-pipeline reruns.

## Assessment and artifacts
- Deliverable: staged architecture plan with lineage fields.
- Rubric dimensions: reliability, traceability, scalability, and recovery readiness.

## Connections
- Unit page: [Volume Reconstruction Infrastructure]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
- Journal club: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Dictionary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Existing module overlap: [module12]({{ '/modules/module12/' | relative_url }}), [module18]({{ '/modules/module18/' | relative_url }})

## Slide artifacts
<div class="resource-card">
  <p>Use the links below to access the rendered lecture artifacts for this unit.</p>
  <div class="resource-links">
    <a class="resource-link" href="{{ '/course/decks/marp/out/' | append: page.slug | remove: 'slides-' | append: '.html' | relative_url }}">Open HTML Deck</a>
    <a class="resource-link" href="{{ '/course/decks/marp/out/' | append: page.slug | remove: 'slides-' | append: '.pptx' | relative_url }}">Download PowerPoint (.pptx)</a>
    <a class="resource-link" href="{{ '/technical-training/' | append: page.slug | remove: 'slides-' | append: '/' | relative_url }}">Open Unit Page</a>
  </div>
  <p><strong>Slide source path:</strong> <code>course/decks/marp/{{ page.slug | remove: "slides-" }}.marp.md</code></p>
  <p><strong>Batch render helper:</strong> <code>./scripts/render_marp.sh</code></p>
</div>