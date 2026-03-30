---
layout: page
title: "Content Library"
permalink: /content-library/
description: "Canonical reference scripts, worked examples, and case studies for the NeuroTrailblazers technical curriculum. Each entry is a self-contained teaching document designed for reuse across unit pages, slide decks, instructor scripts, and student handouts."
---

## How this library works

Every entry below is a **standalone, richly detailed reference document**. Each contains:

- Full instructor-ready narrative (not just bullet points)
- Real scientific references with context
- Worked examples with step-by-step reasoning
- Common misconceptions and how to address them
- **Tags** for cross-referencing across dimensions (using the taxonomy in `_data/content_tags.yml`)
- **Reference images** with alt text and captions (placeholders for teaching illustrations)
- **Micro lesson IDs** for combining entries into modular learning sequences
- **Combines-with** links identifying entries that pair well for combined micro lessons

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

| Entry | Scope | Primary units |
|-------|-------|---------------|
| [Error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }}) | Merge, split, boundary, and identity errors with examples | 08 |
| [Proofreading strategies]({{ '/content-library/proofreading/proofreading-strategies/' | relative_url }}) | Exhaustive, targeted, priority-ranked, crowd-sourced approaches | 08 |
| [Proofreading tools]({{ '/content-library/proofreading/proofreading-tools/' | relative_url }}) | CAVE, Neuroglancer, FlyWire, NeuTu; editing operations | 08 |
| [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}) | VI, ERL, edge F1, synapse-centric F1 with formulas | 08 |
| [Worked examples]({{ '/content-library/proofreading/worked-examples/' | relative_url }}) | Step-by-step correction scenarios for merge, split, synapse errors | 08 |

## Connectomics

Graph analysis, motif search, and the bridge to NeuroAI.

| Entry | Scope | Primary units |
|-------|-------|---------------|
| [Connectome history]({{ '/content-library/connectomics/connectome-history/' | relative_url }}) | C. elegans through FlyWire and MICrONS; milestones and lessons | 01, 09 |
| [Graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }}) | Nodes, edges, weights, adjacency matrices, multigraphs | 09 |
| [Network analysis methods]({{ '/content-library/connectomics/network-analysis-methods/' | relative_url }}) | Degree, clustering, path length, community detection, spectral | 09 |
| [Motif analysis]({{ '/content-library/connectomics/motif-analysis/' | relative_url }}) | DotMotif, null models, subgraph isomorphism, statistics | 09 |
| [NeuroAI bridge]({{ '/content-library/connectomics/neuroai-bridge/' | relative_url }}) | Structure-function, bio-inspired architectures, connectome-constrained models | 09 |

## Imaging

EM acquisition, image formation, and artifact management.

| Entry | Scope | Primary units |
|-------|-------|---------------|
| [EM principles]({{ '/content-library/imaging/em-principles/' | relative_url }}) | Beam physics, contrast mechanisms, SEM vs TEM, resolution limits | 03 |
| [Artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}) | Knife chatter, charging, folds, tears, drift; downstream impact | 03, 05 |
| [Tissue preparation]({{ '/content-library/imaging/tissue-preparation/' | relative_url }}) | Fixation, heavy-metal staining, embedding, sectioning strategies | 03 |
| [Acquisition QA]({{ '/content-library/imaging/acquisition-qa/' | relative_url }}) | Per-tile QC, pilot reconstructions, metadata requirements | 03 |

## Infrastructure

Reconstruction pipelines, data formats, and reproducibility.

| Entry | Scope | Primary units |
|-------|-------|---------------|
| [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) | Ingest, alignment, segmentation, agglomeration, serving | 04 |
| [Data formats and representations]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) | Volumes, meshes, skeletons, graphs; when to use each | 02, 04 |
| [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) | Lineage metadata, CAVE materialization, reproducible reprocessing | 04, 08 |

## Cell types

Identification and classification of neuronal and glial cell types in EM.

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
| [C. elegans revisited]({{ '/content-library/case-studies/c-elegans-revisited/' | relative_url }}) | The first connectome, re-analysis, developmental connectomics | 01, 09 |
| [MouseConnects HI-MC]({{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }}) | NIH CONNECTS flagship, 10 mm³ hippocampus, ongoing project | 01, 04 |

## Journal paper collection

100+ curated papers across 11 connectomics dimensions, each with summaries at **beginner**, **intermediate**, and **advanced** expertise levels. All papers are also available as structured data in `_data/journal_papers.yml` for programmatic filtering. See the [full collection]({{ '/content-library/journal-papers/' | relative_url }}).

| Dimension | Papers | Focus |
|-----------|--------|-------|
| [Neuroanatomy]({{ '/content-library/journal-papers/neuroanatomy/' | relative_url }}) | 8 | Ultrastructure, synapses, spines, serial reconstruction |
| [Imaging]({{ '/content-library/journal-papers/imaging/' | relative_url }}) | 8 | SBEM, FIB-SEM, ATUM, acquisition pipelines |
| [Computer Vision & ML]({{ '/content-library/journal-papers/computer-vision-ml/' | relative_url }}) | 10 | FFN, U-Net, affinity prediction, synapse detection |
| [Data Storage & Pipelines]({{ '/content-library/journal-papers/data-storage/' | relative_url }}) | 8 | CAVE, neuPrint, CATMAID, OME-Zarr, pipeline engineering |
| [Proofreading & QC]({{ '/content-library/journal-papers/proofreading/' | relative_url }}) | 8 | Error detection, crowd-sourced correction, QA metrics |
| [Cell Types]({{ '/content-library/journal-papers/cell-types/' | relative_url }}) | 8 | Morphological, transcriptomic, connectivity-based classification |
| [Graph Construction]({{ '/content-library/journal-papers/connectomics/' | relative_url }}) | 8 | Graph encoding, comparative connectomics |
| [Network Analysis]({{ '/content-library/journal-papers/network-analysis/' | relative_url }}) | 10 | Motifs, community detection, graph matching, NBS |
| [MRI Connectomics]({{ '/content-library/journal-papers/mri-connectomics/' | relative_url }}) | 12 | Diffusion tractography, functional connectivity, HCP |
| [NeuroAI]({{ '/content-library/journal-papers/neuroai/' | relative_url }}) | 8 | Structure-function, bio-inspired AI, model taxonomy |
| [Case Studies]({{ '/content-library/journal-papers/case-studies/' | relative_url }}) | 10 | C. elegans, FlyWire, MICrONS, H01, landmark datasets |
