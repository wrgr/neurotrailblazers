---
layout: page
title: "Journal Paper Collection"
permalink: /content-library/journal-papers/
description: "96 connectomics papers hand-annotated across 11 teaching dimensions, with summaries at beginner, intermediate, and advanced expertise levels, key figures, and discussion prompts."
use_layout_hero: false
content_type: core
---

# Journal Paper Collection

**96 papers**, hand-annotated across 11 teaching dimensions — from ultrastructure to MRI —
and tagged for cross-referencing with the content library. Each entry carries:

- **Three-level summaries** — beginner (no prerequisites), intermediate (familiar with basics), advanced (active researcher)
- **Tags** — linking papers to the content library tag taxonomy for combinable micro lessons
- **Key figures** — which figures to focus on and what they show
- **Discussion prompts** — ready-to-use journal club questions
- **Related content** — links to content library entries for deeper context

## One collection, two ways to read it

This page is a hand-curated **deep-dive subset** of the same underlying collection that
powers the [journal club]({{ '/technical-training/journal-club/' | relative_url }}) — not
a second library. The journal club now holds the **full visible core**,
{{ site.data.journal_papers.papers | size }} papers selected and annotated by the field's
citation graph. These eleven pages are a hand-picked ~96-paper path through the same
territory, written to lay out the argument of each paper rather than to be filtered
programmatically. See the [methodology page]({{ '/content-library/journal-papers/methodology/' | relative_url }})
for how the full collection was built.

| | This collection | [Full corpus]({{ '/technical-training/journal-club/' | relative_url }}) |
|---|---|---|
| **Size** | 96 papers | {{ site.data.journal_papers.papers | size }} papers |
| **Selected by** | Hand, for teaching a specific dimension | Citation-graph inclusion bar over the field's literature |
| **Lives in** | These eleven markdown pages | `_data/journal_papers.yml` |
| **Each entry has** | Three-level summaries, key figures, discussion prompts, related content | OCAR structure, three-level summaries, discussion prompts, graph place (k-core, in/out links), filterable metadata |
| **Reach for it when** | You are teaching or studying a topic and want the argument laid out | You are surveying what exists, browsing by organism/dataset/method/era, or exploring the citation graph |

At least 36 of the 96 papers here (matched by DOI) are also in the full corpus — the rest
predate it, are more specialized than its inclusion bar, or are texts (books, standards)
the corpus doesn't track. If you want programmatic filtering, browse the corpus; if you
want a paper's argument laid out with key figures, use this collection.

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
| [MRI Connectomics]({{ '/content-library/journal-papers/mri-connectomics/' | relative_url }}) | 10 | Diffusion tractography, functional connectivity, HCP, parcellation |

### Cross-Cutting

| Dimension | Papers | Focus |
|-----------|--------|-------|
| [NeuroAI & Modeling]({{ '/content-library/journal-papers/neuroai/' | relative_url }}) | 8 | Structure-function, bio-inspired AI, connectome-constrained models |
| [Datasets & Case Studies]({{ '/content-library/journal-papers/case-studies/' | relative_url }}) | 10 | C. elegans, FlyWire, MICrONS, H01, landmark projects |

**Total: 96 papers** across 11 dimensions. The counts above are maintained by hand and
checked in CI by `scripts/validate_paper_counts.rb`, which counts the actual entries on
each page and fails the build if this table drifts from them again.

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

## Structured data access

The pages above are markdown, not generated from data — the annotations are written by
hand, which is why they carry key figures and related-content links that no data file
holds.

Structured records exist for the **full {{ site.data.journal_papers.papers | size }}-paper corpus** in
`_data/journal_papers.yml`. Its schema is:

```yaml
- id: paper-id
  uuid: "10.xxxx/xxxxx"           # DOI lowercased, else a stable catalog work id
  title: "Paper title"
  authors: "Author list"
  year: 2024
  journal: "Journal name"
  doi: "10.xxxx/xxxxx"
  landing_url: "https://…"
  dimension: connectomics         # see below for the valid set
  reading_phase: 1_foundations
  role: methods                   # methods / biology / survey / review / bridge
  inclusion_role: contemporary    # history / contemporary / sota
  era: "2019–2024"
  k_core: 5                       # place in the citation-graph's densest core
  in_degree: 2
  out_degree: 4
  tags: [tag1, tag2]
  streams:                        # pipeline stage, organism, dataset, method, axis
    axis: pipeline_stage
    organism: [mouse]
    method: [FIB-SEM]
  related:
    cites: ["10.xxxx/…"]
    cited_by: ["10.xxxx/…"]
  ocar:                           # Opportunity / Challenge / Action / Resolution
    opportunity: "…"
  plain_language_summary: "…"
  summaries:
    beginner: "…"
    intermediate: "…"
    advanced: "…"
  discussion_prompts: ["Prompt 1", "Prompt 2"]
```

Its `dimension` values are citation-graph categories and are **not** the eleven teaching
dimensions used on this page: `image-acquisition` (230), `connectomics` (207),
`graph-analysis` (205), `segmentation` (142), `infrastructure` (107), `proofreading`
(78), `neuroai` (26), `methods-general` (24), `neuroanatomy` (23), `cell-types` (22),
`review` (10).

That enables filtering such as "every `graph-analysis` paper from before 2010, at k-core
≥5, with beginner summaries" — but it will not find the key figures or related-content
links from this collection, because those live only in the markdown. See the
[methodology page]({{ '/content-library/journal-papers/methodology/' | relative_url }})
for how inclusion, k-core, and the other views are defined.
