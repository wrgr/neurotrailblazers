---
layout: page
title: "Atlas Connectomics Reference"
permalink: /technical-training/atlas-connectomics-reference/
slug: atlas-connectomics-reference
---

## Purpose
A living reference hub for papers, datasets, and tools aligned to the technical track.

## Technical scope
The atlas is curated for operational use, not just bibliography. Each entry should support one or more concrete tasks in the connectomics workflow and include enough metadata to assess applicability, maturity, and reproducibility.

## Scope
- Organize references by workflow stage and evidence type.
- Maintain provenance fields (year, species, modality, scale, access).
- Link every reference family back to at least one track unit.

## Planned structure
- Imaging and acquisition references
- Reconstruction and segmentation references
- Analysis and NeuroAI references
- Dataset and benchmark references

## Visual context set (draft)
<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/atlas-connectomics-reference/FIG-SRC-21_02388_X_TECHTALK_-S44-01.png' | relative_url }}" alt="Developmental motifs reference context visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Techtalk S44:</strong> developmental motif reference context.</p>
  </article>
</div>

<p><small>Attribution: neuroAI source deck (historical/context visual). Planned module14-lesson3 atlas figures remain pending extraction/import.</small></p>

## Required metadata schema (minimum)
- `citation`: standardized citation string.
- `workflow_stage`: acquisition, reconstruction, proofreading, analysis, or cross-cutting.
- `species` and `brain_region`.
- `modality` and `effective_resolution`.
- `dataset_or_code_access`: URL plus access constraints.
- `maturity`: concept, validated prototype, production-validated.
- `known_limits`: concise statement of technical boundaries.
- `mapped_units`: links to technical-training unit slugs.

## Curation policy
1. Add only resources with clear technical contribution or benchmark value.
2. Mark historical methods as historical when superseded, but keep if pedagogically useful.
3. Prefer references with reproducible artifacts (data, code, or explicit protocol).
4. Re-review entries on schedule and retire stale links.

## Quality-control checks
- Link health check for every external URL.
- Metadata completeness validation against required schema.
- Duplicate detection (same method presented across multiple venues).
- Coverage audit to avoid over-weighting one workflow stage.

## Course links
- Return to [Technical Training hub]({{ '/technical-training/' | relative_url }})

## Practical workflow
1. Start from a workflow stage (imaging, reconstruction, proofreading, analysis).
2. Select core references and datasets for that stage.
3. Cross-link chosen references to relevant technical-track units.
4. Record update date and curator for each entry group.

## Discussion prompts
- Which references are foundational versus context-only for current learners?
- What deprecation criteria should remove outdated resources from the atlas?

## Mini-lab
Curate one new atlas entry and include:
1. Complete metadata schema fields.
2. One sentence on technical contribution.
3. One sentence on limitation or failure context.
4. One linked unit in this technical-training track.

## Related resources
- Journal club list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})

## Quick activity
Select one reference from each workflow stage and explain in one sentence how each supports a different unit in the track.


## Draft lecture deck
- Slide draft page: [Atlas Connectomics Reference deck draft]({{ '/technical-training/slides/atlas-connectomics-reference/' | relative_url }})
