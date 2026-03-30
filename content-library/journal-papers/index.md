---
layout: page
title: "Journal Paper Collection"
permalink: /content-library/journal-papers/
description: "100+ curated connectomics journal papers organized by dimension, with summaries at beginner, intermediate, and advanced expertise levels. Each paper includes tags for cross-referencing with the content library and discussion prompts for journal club."
---

# Journal Paper Collection

A curated library of 100+ essential connectomics papers organized across 11 dimensions — from ultrastructure to MRI — and tagged for cross-referencing with the content library. Each paper includes:

- **Three-level summaries** — beginner (no prerequisites), intermediate (familiar with basics), advanced (active researcher)
- **Tags** — linking papers to the content library tag taxonomy for combinable micro lessons
- **Key figures** — which figures to focus on and what they show
- **Discussion prompts** — ready-to-use journal club questions
- **Related content** — links to content library entries for deeper context

All papers are also available as structured data in `_data/journal_papers.yml` for programmatic filtering by dimension, tag, or expertise level.

---

## By Dimension

### EM-Scale Connectomics

| Dimension | Papers | Focus |
|-----------|--------|-------|
| [Neuroanatomy]({{ '/content-library/journal-papers/neuroanatomy/' | relative_url }}) | 8 | Ultrastructure, synapses, spines, organelles, serial reconstruction |
| [Imaging & Sample Preparation]({{ '/content-library/journal-papers/imaging/' | relative_url }}) | 8 | SBEM, FIB-SEM, ATUM, tissue preparation, acquisition pipelines |
| [Computer Vision & ML]({{ '/content-library/journal-papers/computer-vision-ml/' | relative_url }}) | 10 | Segmentation (FFN, U-Net, affinity), synapse detection, error correction |
| [Data Storage & Pipelines]({{ '/content-library/journal-papers/data-storage/' | relative_url }}) | 8 | CAVE, neuPrint, CATMAID, OME-Zarr, cloud storage, pipeline engineering |
| [Proofreading & QC]({{ '/content-library/journal-papers/proofreading/' | relative_url }}) | 8 | Crowd-sourced proofreading, error detection, agglomeration, QA metrics |
| [Cell Types & Classification]({{ '/content-library/journal-papers/cell-types/' | relative_url }}) | 8 | Morphological, transcriptomic, connectivity-based classification |

### Graph Analysis & Network Science

| Dimension | Papers | Focus |
|-----------|--------|-------|
| [Graph Construction & Representation]({{ '/content-library/journal-papers/connectomics/' | relative_url }}) | 8 | Graph encoding, comparative connectomics, structure-function |
| [Network Analysis & Statistics]({{ '/content-library/journal-papers/network-analysis/' | relative_url }}) | 10 | Motifs, community detection, graph matching, null models, NBS |

### MRI & Macro-Scale

| Dimension | Papers | Focus |
|-----------|--------|-------|
| [MRI Connectomics]({{ '/content-library/journal-papers/mri-connectomics/' | relative_url }}) | 12 | Diffusion tractography, functional connectivity, HCP, parcellation |

### Cross-Cutting

| Dimension | Papers | Focus |
|-----------|--------|-------|
| [NeuroAI & Modeling]({{ '/content-library/journal-papers/neuroai/' | relative_url }}) | 8 | Structure-function, bio-inspired AI, connectome-constrained models |
| [Datasets & Case Studies]({{ '/content-library/journal-papers/case-studies/' | relative_url }}) | 10 | C. elegans, FlyWire, MICrONS, H01, landmark projects |

**Total: 100+ papers** across 11 dimensions (including recent additions from 2022–2025).

---

## How to Use This Collection

### For self-study
Start with the **beginner summary** to orient yourself, then read the paper, then compare your understanding with the **intermediate** and **advanced** summaries. Use the **key figures** list to focus your reading.

### For journal club
Use the **discussion prompts** to structure group discussion. The three-level summaries help facilitators calibrate discussion depth for mixed-expertise groups. See the [Technical Track Journal Club](/technical-training/journal-club/) for scheduling guidance.

### For micro lesson design
Use **tags** to find papers that align with specific content library entries. The `combines_with` field on content library entries and the `Related content` links on papers create a cross-referenced web for assembling multi-resource micro lessons.

### For course design
Papers are organized to follow the technical training sequence. Each dimension aligns with specific technical training units:

| Dimension | Primary units |
|-----------|---------------|
| Neuroanatomy | 05, 06 |
| Imaging | 03 |
| Computer Vision & ML | 04, 08 |
| Data Storage & Pipelines | 04, 08 |
| Proofreading | 08 |
| Cell Types | 05, 06, 07 |
| Graph Construction | 09 |
| Network Analysis | 09 |
| MRI Connectomics | 01, 02 |
| NeuroAI | 09 |
| Case Studies | 01, 02, 08, 09 |

---

## Expertise Level Guide

| Level | Assumes | Best for |
|-------|---------|----------|
| **Beginner** | No neuroscience or connectomics background | New trainees, interdisciplinary collaborators, public engagement |
| **Intermediate** | Familiar with EM, basic neuroscience, and computational concepts | Graduate students, postdocs entering the field |
| **Advanced** | Active researcher or advanced trainee | Methodological deep dives, experimental design, peer review |

---

## Structured Data Access

All papers are stored as structured YAML records in `_data/journal_papers.yml`. Each record contains:

```yaml
- id: paper-id
  title: "Paper title"
  authors: "Author list"
  year: 2024
  journal: "Journal name"
  doi: "10.xxxx/xxxxx"
  dimension: dimension-name
  tags: [dimension:tag1, dimension:tag2]
  key_figures: ["Fig. 1: description"]
  discussion_prompts: ["Prompt 1", "Prompt 2"]
  related_content: [/content-library/path/]
  summaries:
    beginner: "Plain-language summary"
    intermediate: "Technical summary"
    advanced: "Expert summary with methodological detail"
```

This enables programmatic filtering, e.g., "show all papers tagged `case-studies:FlyWire` with beginner summaries" or "find papers related to `/content-library/proofreading/error-taxonomy/`".
