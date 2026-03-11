---
layout: page
title: "Connectomics Dictionary"
permalink: /technical-training/dictionary/
slug: connectomics-dictionary
---

## Purpose
A shared vocabulary for learners, mentors, and journal clubs in the technical connectomics track.

## How to use this dictionary
- Before each unit, review 5-8 terms from the relevant categories.
- During annotation or journal club, require definitions to be tied to concrete examples.
- Treat terms like `motif`, `null model`, and `provenance` as operational requirements, not just vocabulary.

## Starter term sets by unit
- Units 01-02: `connectome`, `connectomics`, `voxel`, `anisotropy`, `registration`, `null model`.
- Units 03-04: `serial section EM`, `SBF-SEM`, `FIB-SEM`, `stitching`, `multiresolution pyramid`, `provenance`.
- Units 05-07: `ultrastructure`, `axon`, `dendrite`, `bouton`, `astrocyte`, `microglia`, `oligodendrocyte`.
- Units 08-09: `segmentation`, `proofreading`, `merge error`, `split error`, `VI`, `ERL`, `subgraph isomorphism`, `DotMotif`.

<div class="cards-grid">
  {% assign terms = site.data.connectomics_dictionary.terms | sort: 'term' %}
  {% for item in terms %}
  <article class="card">
    <h3 class="card-title">{{ item.term }}</h3>
    <p><small><strong>Category:</strong> {{ item.category }}</small></p>
    <p class="card-description">{{ item.definition }}</p>
  </article>
  {% endfor %}
</div>
