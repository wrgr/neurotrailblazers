---
layout: page
title: "07 Glia"
permalink: /technical-training/07-glia/
slug: 07-glia
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
---

## Why this unit
Glia are central to reliable annotation and interpretation, not background objects.

## Learning goals
- Recognize astrocytes, microglia, and oligodendrocyte cues.
- Reduce glia-neuron boundary errors during proofreading.

## Core technical anchors
- Glia-specific ambiguity patterns in dense neuropil.
- Myelin context cues for oligodendrocyte interpretation.
- Reusable glia recognition checklist.

## Method deep dive: glia identification workflow
1. Candidate detection:
   Mark processes with non-neuronal morphology and atypical organelle distribution.
2. Context enrichment:
   Inspect vascular adjacency, myelin relationships, and neighboring synaptic density.
3. Cell-class discrimination:
   Compare astrocyte-like branching, microglial surveillance morphology, and oligodendrocyte/myelin patterns.
4. Temporal/section continuity:
   Follow process across slices to avoid single-plane misclassification.
5. Adjudication:
   Escalate low-confidence cases into a shared glia review queue.

## Quantitative QA checkpoints
- Glia-vs-neuron boundary error rate on validation subset.
- Class-specific agreement (astrocyte, microglia, oligodendrocyte).
- Rate of unresolved glia labels after second-pass review.
- Impact of corrected glia labels on neuronal graph statistics.

## Frequent failure modes
- Astrocyte-neurite confusion in dense neuropil:
  Require neighborhood and boundary-context confirmation.
- Over-calling microglia based on fragmentary appearance:
  Use multi-slice morphology before class assignment.
- Oligodendrocyte/myelin ambiguity:
  Trace sheath context and nearby axonal relationships.
- Ignoring glia in proofreading priorities:
  Include glia corrections in high-impact QC queues.

## Visual training set
<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/07-glia/FIG-RIV-GLIA-S01-01.png' | relative_url }}" alt="Glia training visual: overview context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-GLIA S01:</strong> opening context visual for glia-focused proofreading.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/07-glia/FIG-RIV-GLIA-S03-01.png' | relative_url }}" alt="Glia training visual: astrocyte context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-GLIA S03:</strong> astrocyte-related morphology and synaptic neighborhood context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/07-glia/FIG-RIV-GLIA-S09-01.png' | relative_url }}" alt="Glia training visual: microglia context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-GLIA S09:</strong> microglia recognition cues in local structural context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/07-glia/FIG-RIV-GLIA-S15-01.png' | relative_url }}" alt="Glia training visual: oligodendrocyte reconstruction" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-GLIA S15:</strong> oligodendrocyte-focused morphology/reconstruction cue.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/07-glia/FIG-RIV-GLIA-S16-01.png' | relative_url }}" alt="Glia training visual: myelin-related glia context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-GLIA S16:</strong> myelin-related context for glia interpretation.</p>
  </article>
</div>

<p><small>Attribution: Pat Rivlin training materials (MICrONS proofreading deck). Two manifest-listed IDs (`S02`, `S07`) were not present in extracted thumbnails and are pending recovery.</small></p>

## Course links
- Existing overlap: [module04]({{ '/modules/module04/' | relative_url }})
- Next unit: [08 Segmentation and Proofreading]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})

## Practical workflow
1. Identify candidate glial morphology in local context.
2. Compare against neuronal look-alikes in neighboring slices.
3. Confirm with vascular/myelin/synaptic adjacency cues.
4. Record class decision and uncertainty for review.

## Discussion prompts
- Which glia-neuron ambiguities are most error-prone in your data?
- What minimum evidence should be required before final glia labels?

## Related resources
- Journal club list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})

## Quick activity
Review one glia image and list two features that distinguish it from a neuronal process in the same neighborhood.


## Teaching slide deck
- Slide draft page: [Glia deck draft]({{ '/technical-training/slides/07-glia/' | relative_url }})
