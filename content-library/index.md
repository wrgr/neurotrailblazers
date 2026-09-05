---
layout: page
title: "Content Library"
permalink: /content-library/
description: "Canonical reference scripts, worked examples, and case studies for the NeuroTrailblazers technical curriculum. Each entry is a self-contained teaching document designed for reuse across unit pages, slide decks, instructor scripts, and student handouts."
content_type: core
---

## What this is

The content library is [core reference material]({{ '/core/' | relative_url }}): the
depth behind the one-sentence claims made in the [technical
units]({{ '/technical-training/' | relative_url }}) and [modules]({{ '/modules/' | relative_url }}).

It has **no order and no end**. You are not meant to work through it. Come here when
a unit asserts something you want the argument for, when you need the worked example
rather than the result, or when you are about to do a specific technical thing and
want to read how it is done properly first.

If you want an order, that is what a [track]({{ '/tracks/' | relative_url }}) is for.

## How this library works

Every entry below is a **standalone, richly detailed reference document**. Each contains:

- Full instructor-ready narrative (not just bullet points)
- Real scientific references with context
- Worked examples with step-by-step reasoning
- Common misconceptions and how to address them
- **Tags** for cross-referencing across dimensions
- **Combines-with** links identifying entries that pair well together, shown at the top of each entry
- **Real electron micrographs** on the entries that make visual claims, rendered from the public H01 human cortex volume — see the [EM figure library]({{ '/content-library/em-figures/' | relative_url }}). Entries also carry older `reference_images` front matter describing figures that were specified but never produced; that metadata is not rendered, and is being replaced by the figures above as each entry is covered

Unit pages, slide decks, and modules **link to** these entries rather than duplicating content. This keeps the curriculum DRY (Don't Repeat Yourself) and ensures a single source of truth for each topic.

### Tag dimensions

Content is tagged across 9 dimensions for flexible combination:

| Dimension | Color | Example tags |
|-----------|-------|-------------|
| Neuroanatomy | #4A90D9 | soma, dendrite, axon, synapse, spine, organelle |
| Imaging | #7B68EE | electron-microscopy, SEM, TEM, FIB-SEM, SBEM, ATUM |
| Infrastructure | #E67E22 | pipeline, segmentation, alignment, CAVE, neuroglancer |
| Proofreading | #E74C3C | merge-error, split-error, QA-metrics, expected-run-length |
| Cell Types | #27AE60 | neuron-classification, glia, pyramidal-cell, interneuron |
| Connectomics | #F39C12 | graph-theory, motif, community-detection, hub, modularity |
| NeuroAI | #9B59B6 | structure-function, bio-inspired-architecture, deep-learning |
| Case Studies | #1ABC9C | FlyWire, MICrONS, H01, C-elegans, Drosophila |
| Methodology | #95A5A6 | experimental-design, reproducibility, benchmark, ground-truth |

---

## Neuroanatomy

Ultrastructural biology of neurons as seen in electron microscopy.

[Browse the 160 neuroanatomy papers in the journal club]({{ '/technical-training/journal-club/?dimension=neuroanatomy' | relative_url }}) &rarr;

| Entry | Scope | Primary units |
|-------|-------|---------------|
| [Soma ultrastructure]({{ '/content-library/neuroanatomy/soma-ultrastructure/' | relative_url }}) | Nuclear envelope, Nissl substance, Golgi, lipofuscin; EM identification | 05 |
| [Dendrite biology]({{ '/content-library/neuroanatomy/dendrite-biology/' | relative_url }}) | Spine types, PSDs, microtubule organization, local translation | 05, 06 |
| [Axon biology]({{ '/content-library/neuroanatomy/axon-biology/' | relative_url }}) | AIS, myelinated segments, boutons, vesicle pools, active zones | 05, 06 |
| [Synapse classification]({{ '/content-library/neuroanatomy/synapse-classification/' | relative_url }}) | Gray Type I/II, asymmetric vs symmetric, cleft structure | 05, 08 |
| [Organelle annotation cues]({{ '/content-library/neuroanatomy/organelle-cues/' | relative_url }}) | Mitochondria, ER, MVBs, lysosomes as compartment indicators | 05, 06 |
| [Myelin and nodes of Ranvier]({{ '/content-library/neuroanatomy/myelin-and-nodes/' | relative_url }}) | Compact myelin, paranodal loops, Schmidt-Lanterman incisures | 05, 06 |

## Proofreading

Quality control of automated segmentation at connectome scale.

[Proofreading and quality-control reading list]({{ '/content-library/journal-papers/proofreading/' | relative_url }}) &rarr; (the corpus has no separate proofreading dimension; proofreading papers sit under [pipeline]({{ '/technical-training/journal-club/?dimension=pipeline' | relative_url }}))

| Entry | Scope | Primary units |
|-------|-------|---------------|
| [Error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }}) | Merge, split, boundary, and identity errors with examples | 08 |
| [Proofreading strategies]({{ '/content-library/proofreading/proofreading-strategies/' | relative_url }}) | Exhaustive, targeted, priority-ranked, crowd-sourced approaches | 08 |
| [Proofreading tools]({{ '/content-library/proofreading/proofreading-tools/' | relative_url }}) | CAVE, Neuroglancer, FlyWire, NeuTu; editing operations | 08 |
| [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}) | VI, ERL, edge F1, synapse-centric F1 with formulas | 08 |
| [Worked examples]({{ '/content-library/proofreading/worked-examples/' | relative_url }}) | Step-by-step correction scenarios for merge, split, synapse errors | 08 |

## Connectomics

Graph analysis, motif search, and the bridge to NeuroAI.

[Browse the 300 circuit-structure papers in the journal club]({{ '/technical-training/journal-club/?dimension=circuit-structure' | relative_url }}) &rarr; (or the curated [network analysis and statistics list]({{ '/content-library/journal-papers/network-analysis/' | relative_url }}))

| Entry | Scope | Primary units |
|-------|-------|---------------|
| [Connectome history]({{ '/content-library/connectomics/connectome-history/' | relative_url }}) | C. elegans through FlyWire and MICrONS; milestones and lessons | 01, 09 |
| [Graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }}) | Nodes, edges, weights, adjacency matrices, multigraphs | 09 |
| [Network analysis methods]({{ '/content-library/connectomics/network-analysis-methods/' | relative_url }}) | Degree, clustering, path length, community detection, spectral | 09 |
| [Motif analysis]({{ '/content-library/connectomics/motif-analysis/' | relative_url }}) | DotMotif, null models, subgraph isomorphism, statistics | 09 |
| [NeuroAI bridge]({{ '/content-library/connectomics/neuroai-bridge/' | relative_url }}) | Structure-function, bio-inspired architectures, connectome-constrained models | 09 |
| [Open problems for undergraduate teams]({{ '/content-library/connectomics/open-problems-undergrad/' | relative_url }}) | Seven open problem areas scoped for undergrad teams, tied to BRAIN CONNECTS bottlenecks | 01, 08, 09 |
| [Ethics and governance]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }}) | H01's consent and provenance, de-identification in EM, portal licences and what they oblige, dual use, credit for proofreading labour | 01, 08 |

## Imaging

EM acquisition, image formation, and artifact management.

[Browse the 160 volume-EM and optics papers in the journal club]({{ '/technical-training/journal-club/?dimension=imaging' | relative_url }}) &rarr;

| Entry | Scope | Primary units |
|-------|-------|---------------|
| [EM principles]({{ '/content-library/imaging/em-principles/' | relative_url }}) | Beam physics, contrast mechanisms, SEM vs TEM, resolution limits | 03 |
| [Artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}) | Knife chatter, charging, folds, tears, drift; downstream impact | 03, 05 |
| [Tissue preparation]({{ '/content-library/imaging/tissue-preparation/' | relative_url }}) | Fixation, heavy-metal staining, embedding, sectioning strategies | 03 |
| [Acquisition QA]({{ '/content-library/imaging/acquisition-qa/' | relative_url }}) | Per-tile QC, pilot reconstructions, metadata requirements | 03 |

## Infrastructure

Reconstruction pipelines, data formats, and reproducibility.

[Browse the 300 pipeline and software-engineering papers in the journal club]({{ '/technical-training/journal-club/?dimension=pipeline' | relative_url }}) &rarr;

| Entry | Scope | Primary units |
|-------|-------|---------------|
| [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) | Ingest, alignment, segmentation, agglomeration, serving | 04 |
| [Data formats and representations]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) | Volumes, meshes, skeletons, graphs; when to use each | 02, 04 |
| [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) | Lineage metadata, CAVE materialization, reproducible reprocessing | 04, 08 |
| [Synapse detection]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }}) | Cleft localisation, partner assignment, E/I classification; CREMI and what it predicts; cross-dataset degradation; what to check before trusting a synapse table | 04, 05, 08 |

## Cell types

Identification and classification of neuronal and glial cell types in EM.

[Browse the 160 cell-type papers in the journal club]({{ '/technical-training/journal-club/?dimension=cell-types' | relative_url }}) &rarr;

| Entry | Scope | Primary units |
|-------|-------|---------------|
| [Axon-dendrite classification]({{ '/content-library/cell-types/axon-dendrite-classification/' | relative_url }}) | Multi-cue discrimination, edge cases, confidence scoring | 06 |
| [Glia recognition]({{ '/content-library/cell-types/glia-recognition/' | relative_url }}) | Astrocytes, microglia, oligodendrocytes; boundary ambiguities | 07 |
| [Neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }}) | Morphological and connectivity-based classification | 05, 06, 09 |

## Case studies

Deep dives into landmark connectomics projects.

| Entry | Scope | Primary units |
|-------|-------|---------------|
| [FlyWire whole-brain connectome]({{ '/content-library/case-studies/flywire-whole-brain/' | relative_url }}) | 140K neurons, collaborative proofreading, brain-wide circuit analysis | 08, 09 |
| [MICrONS visual cortex]({{ '/content-library/case-studies/microns-visual-cortex/' | relative_url }}) | mm³ mouse cortex, functional connectomics, structure-function linking | 01, 03, 08, 09 |
| [H01 human cortex]({{ '/content-library/case-studies/h01-human-cortex/' | relative_url }}) | Petavoxel human fragment, unique challenges, pathological features | 05, 08 |
| [H01, step by step]({{ '/content-library/case-studies/h01-pipeline/' | relative_url }}) | The full production pipeline — tissue, staining, sectioning, 61-beam imaging, alignment, segmentation, synapse detection — with figures rendered from the public volume | 03, 04, 08 |
| [C. elegans revisited]({{ '/content-library/case-studies/c-elegans-revisited/' | relative_url }}) | The first connectome, re-analysis, developmental connectomics | 01, 09 |
| [MouseConnects HI-MC]({{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }}) | NIH BRAIN CONNECTS flagship, 10 mm³ hippocampus, ongoing project | 01, 04 |

## EM figure library

Every electron micrograph on this site in one place — with captions, attribution and
ready-to-paste slide lines. All rendered from the public H01 human cortex volume and
reusable under CC BY 4.0.

[Browse the EM figure library]({{ '/content-library/em-figures/' | relative_url }}) &rarr;

## Journal paper collection & literature corpus

A curated collection of **2,000 landmark connectomics papers** stratified across 12 research domains and 3 nested tiers (Top 500, Top 1,000, Top 2,000). Features complete unabridged abstracts, 5-part OCAR research cards, 3-tier pedagogical summaries, and seminar discussion prompts.

* Explore the full structured corpus: [Journal Paper Corpus &amp; Literature Hub]({{ '/content-library/journal-papers/' | relative_url }})
* Browse filterable cards by tier and expertise level: [Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
* Explore the interactive network: [Citation Graph Explorer]({{ '/technical-training/journal-club/graph/' | relative_url }})

### Where each corpus domain leads

Every paper in the corpus carries one of twelve domain labels. The **domain name
links to the journal club filtered to that domain** — that is the corpus itself,
and it always works. The **reading list** column is a hand-annotated deep dive of
8–10 papers where one exists for that domain, and says so plainly where one does
not. The **library entry point** is the reference page on this site that covers
the same ground in prose.

Paper counts are the labels actually carried by the 2,000 shipped records, not
the design allocation. The design allocation — the target share and tier split
per domain — is on the
[corpus hub]({{ '/content-library/journal-papers/' | relative_url }}).

| Corpus domain | Papers | Curated reading list | Library entry point |
| :--- | ---: | :--- | :--- |
| [Circuit Structure &amp; Connectomes]({{ '/technical-training/journal-club/?dimension=circuit-structure' | relative_url }}) | 300 | [Connectomics]({{ '/content-library/journal-papers/connectomics/' | relative_url }}) | [Connectome history]({{ '/content-library/connectomics/connectome-history/' | relative_url }}) |
| [Pipeline &amp; Software Engineering]({{ '/technical-training/journal-club/?dimension=pipeline' | relative_url }}) | 300 | [Data storage &amp; pipelines]({{ '/content-library/journal-papers/data-storage/' | relative_url }}) · [Computer vision &amp; ML]({{ '/content-library/journal-papers/computer-vision-ml/' | relative_url }}) | [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) · [Synapse detection]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }}) |
| [Physiological Validation &amp; Function]({{ '/technical-training/journal-club/?dimension=physiology' | relative_url }}) | 242 | *None yet — the largest gap in the deep-dive set* | [MICrONS visual cortex]({{ '/content-library/case-studies/microns-visual-cortex/' | relative_url }}) |
| [Behaviour &amp; Circuit Dynamics]({{ '/technical-training/journal-club/?dimension=behaviour' | relative_url }}) | 240 | [Case studies]({{ '/content-library/journal-papers/case-studies/' | relative_url }}) | [FlyWire whole-brain connectome]({{ '/content-library/case-studies/flywire-whole-brain/' | relative_url }}) |
| [Volume EM &amp; Advanced Optics]({{ '/technical-training/journal-club/?dimension=imaging' | relative_url }}) | 160 | [Imaging &amp; sample preparation]({{ '/content-library/journal-papers/imaging/' | relative_url }}) | [EM principles]({{ '/content-library/imaging/em-principles/' | relative_url }}) |
| [Cell Types &amp; Morphological Census]({{ '/technical-training/journal-club/?dimension=cell-types' | relative_url }}) | 160 | [Cell types &amp; morphology]({{ '/content-library/journal-papers/cell-types/' | relative_url }}) | [Neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }}) |
| [Neuroanatomy &amp; Ultrastructure]({{ '/technical-training/journal-club/?dimension=neuroanatomy' | relative_url }}) | 160 | [Neuroanatomy]({{ '/content-library/journal-papers/neuroanatomy/' | relative_url }}) | [Synapse classification]({{ '/content-library/neuroanatomy/synapse-classification/' | relative_url }}) |
| [Synthesis, Theory &amp; Reviews]({{ '/technical-training/journal-club/?dimension=synthesis' | relative_url }}) | 142 | [Network analysis &amp; statistics]({{ '/content-library/journal-papers/network-analysis/' | relative_url }}) | [Open problems for undergraduate teams]({{ '/content-library/connectomics/open-problems-undergrad/' | relative_url }}) |
| [Benchmark Datasets &amp; Repositories]({{ '/technical-training/journal-club/?dimension=dataset' | relative_url }}) | 115 | [Datasets &amp; case studies]({{ '/content-library/journal-papers/case-studies/' | relative_url }}) | [Datasets catalogue]({{ '/datasets/' | relative_url }}) |
| [NeuroAI, Biophysics &amp; Models]({{ '/technical-training/journal-club/?dimension=neuroai' | relative_url }}) | 100 | [NeuroAI &amp; computational modeling]({{ '/content-library/journal-papers/neuroai/' | relative_url }}) | [NeuroAI bridge]({{ '/content-library/connectomics/neuroai-bridge/' | relative_url }}) |
| [Health, Disease &amp; Translation]({{ '/technical-training/journal-club/?dimension=health' | relative_url }}) | 42 | *None yet* | [H01 human cortex]({{ '/content-library/case-studies/h01-human-cortex/' | relative_url }}) |
| [Workforce Training &amp; Outreach]({{ '/technical-training/journal-club/?dimension=training-outreach' | relative_url }}) | 21 | *None yet* | [Ethics and governance]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }}) |

Two labels sit outside the twelve: 16 papers classified `other`, and 2 classified
`mri`. Macroscale connectivity is out of scope for a nanoscale corpus, which is
why the count is 2 — but the curated
[MRI &amp; meso-connectomics reading list]({{ '/content-library/journal-papers/mri-connectomics/' | relative_url }})
(10 papers on diffusion MRI and tractography) exists for readers arriving from
that side of the field. It is a bridge out of this library, not a route into it.

How the corpus was selected, tiered and annotated is a separate question, and it
has its own page: [How the paper collection is built]({{ '/content-library/journal-papers/methodology/' | relative_url }}).
