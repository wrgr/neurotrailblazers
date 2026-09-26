---
title: "Connectome Quality"
layout: tool
description: "A reconstructed connectome is only as trustworthy as its error rate. This page explains what the standard quality metrics measure, what each one misses, and how people and automated detectors split the work of finding errors."
permalink: /tools/connectome-quality/
slug: connectome-quality
track: research-in-action
pathways:
  - research workflow
  - reproducibility
summary: "Hands-on quality-control concepts, metrics, and workflows for reliable connectome reconstruction."
use_cases:
  - Quality metric education
  - Proofreading workflow training
  - Validation strategy planning
recommended_modules:
  - module06
  - module07
  - module08
  - module12
  - module18
related_datasets:
  - mouseconnects
last_reviewed: 2026-03-09
maintainer: NeuroTrailblazers Team
use_layout_hero: false
content_type: core
---

<div class="main-content">
    <div class="hero hero-spaced hero-rounded">
        <div class="hero-content">
            <div class="hero-text">
                <h1 class="hero-title-impact">{{ page.title }}</h1>
                <p class="hero-description">{{ page.description }}</p>
            </div>
        </div>
    </div>

<section class="section" markdown="1">

## What Connectome Quality Means

A reconstructed connectome is a claim: that these objects are neurons, that
these contacts are synapses, and that the wiring diagram derived from them can
carry scientific weight. Quality control is the practice of measuring how far
that claim can be trusted, and no single number does it. Each standard metric
measures one thing and is blind to another. Choosing the right metric is covered in
[Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
and the mathematics in the
[Metrics and QA reference]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}).

**Variation of information (VI)** totals the disagreement between two
segmentations and decomposes into a split component and a merge component. It
misleads when it is reported as a single number, because the two components can
move in opposite directions: total VI can improve while merge errors, the
expensive kind, get worse. Report the two components separately.

**Expected run length (ERL)** is the mean error-free path length along a
neuron's skeleton: how far can you trace before hitting an error? It fits
tracing-oriented questions. Check how a given implementation treats merges:
versions differ, and one that does not penalize them will reward over-merging.

**Synapse precision and recall** score detected synapses against ground truth.
They assume the segmentation underneath is correct. A synapse assigned to a
merged object still scores as a hit, so these numbers can look excellent on a
volume whose wiring diagram is wrong.

**Completeness** reports what fraction of a neuron was reconstructed, and says
nothing about whether what is there is correct.

Behind all four sits the field's central asymmetry: splits are visible and
bounded, while merges are invisible and unbounded, which is why pipelines are
deliberately tuned to over-segment. The metrics exist to answer one question,
and it is not "what is our VI?" It is "how much would our result change if the
remaining errors were corrected?" Unit 08's answer is to proofread a small random
sample of the cells in your analysis completely and report how the result shifts.
Unit 08 suggests about 20 cells as a starting point; that is a rule of thumb, not
a published figure.

These methods are exercised on real projects:
[MICrONS](https://www.microns-explorer.org/) provides densely reconstructed EM
volumes with functional data that serve as a testbed for quality assessment,
and CIRCUIT (Connectome Integrity and Reliability through Quantitative and
Iterative Training), developed by William Gray-Roncal and collaborators, packages
evaluation tools and metrics (topology, morphology, and synapse-based
F1 score) for use at scale.

## How Humans and Machines Divide the Work

Automated segmentation produces the reconstruction; automated detectors then
propose where it is wrong. Endpoint detectors flag likely splits (a neurite
that stops in mid-neuropil), implausible-morphology detectors flag likely
merges (organelle and shape combinations that cannot coexist in one process).
The output is a ranked queue of candidates, not a verdict.

Humans adjudicate that queue. The division holds because the two error types
demand different strengths. Splits are findable by rule, but recognizing a
merge takes the biological judgment to see that an ordinary-looking object is in
fact two cells, which is why
[Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
assigns merge classes to human review. Newcomers enter this workflow through
small, atomic proofreading tasks: validating boundaries in bounded regions, with
every correction carrying an evidence chain. That is a training design as much
as a labor one. The
[proofreading side quest]({{ '/side-quests/proofreading/' | relative_url }})
builds the skill on real public volumes, and structured task designs with
built-in quality checks let larger groups contribute without diluting the
standard.

</section>

    <div class="cards-grid">
        <div class="card">
            <h2>Learn by Doing</h2>
            <p>The hands-on route is the <a href="{{ '/side-quests/proofreading/' | relative_url }}">proofreading side quest</a>: worked scenarios, real public volumes, and an artifact a lab can read. The <a href="{{ '/notebooks/connectome-quality/' | relative_url }}">notebooks page</a> holds the reference-code steps for computing the metrics on this page.</p>
        </div>

        <div class="card">
            <h2>Where to go from here</h2>
            <ul>
                <li><a href="{{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}">Unit 08</a> — the metrics on this page taught in full, with a graded lab</li>
                <li><a href="{{ '/side-quests/proofreading/' | relative_url }}">The proofreading side quest</a> — the hands-on route, on real public volumes</li>
                <li><a href="{{ '/ask-an-expert/' | relative_url }}">Ask an Expert</a> — the site's question route</li>
            </ul>
        </div>
    </div>
</div>
