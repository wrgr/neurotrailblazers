---
layout: page
title: "Research corpus and reading guides"
permalink: /content-library/journal-papers/
description: "Find connectomics publications, inspect source-checked contributions, and download bibliographic records."
use_layout_hero: false
content_type: core
---

# Research corpus and reading guides

[Search research papers]({{ '/technical-training/journal-club/' | relative_url }}) or [explore recorded citation links]({{ '/technical-training/journal-club/graph/' | relative_url }}).
These are two views of the **same {{ site.data.journal_papers.papers.size }}-paper corpus**, not separate curated collections.

## What the records establish

Publication metadata and recorded abstracts help you locate original work. A **source-checked contribution note**, where available, states what a publication reports, its test context, limitations, the source used, and how it was checked. An AI-assisted abstract check is not full-text review, expert review, or independent validation.

Topic and organism tags are navigation aids. They do not establish use of a named dataset, a protocol, an affiliation, a result, or scientific importance. In particular, scanning electron microscopy does not imply MICrONS dataset use. A citation is a recorded reference, not evidence of agreement or methodological reuse.

Historical category-generated research notes and unsupported dataset/method associations have been removed from the public cards and exports. A missing contribution note means it has not been source-checked here; it does not mean the publication has no contribution.

## Download the corpus

The three nested subsets retain their existing selection. Subset membership and imported network metrics are **not an editorial ranking of demonstrated scientific wins**.

[500-paper subset]({{ '/data/corpus_500.json' | relative_url }}) · [1,000-paper subset]({{ '/data/corpus_1000.json' | relative_url }}) · [Full corpus]({{ '/data/corpus_2000.json' | relative_url }})

Export schema version 2 contains bibliography, recorded abstracts, citation references, navigational tags, and DOI-specific contribution notes where available. Legacy generated annotation fields are null or empty. Consumers should inspect the schema version rather than assume earlier summaries remain available.

[How the collection is maintained]({{ '/content-library/journal-papers/methodology/' | relative_url }}).

## Topic reading guides

The separate course reading guides below remain available. Reading guides provide context; check substantive claims against their cited publications.

| Category | Count | Focus |
| :--- | :---: | :--- |
| [Neuroanatomy]({{ '/content-library/journal-papers/neuroanatomy/' | relative_url }}) | 8 | Ultrastructural foundations, synapses, and organelles |
| [Imaging]({{ '/content-library/journal-papers/imaging/' | relative_url }}) | 8 | Volume EM, FIB-SEM, and serial sectioning |
| [Computer Vision &amp; ML]({{ '/content-library/journal-papers/computer-vision-ml/' | relative_url }}) | 10 | Automated segmentation, affinity graphs, and FFNs |
| [Data Storage &amp; Infrastructure]({{ '/content-library/journal-papers/data-storage/' | relative_url }}) | 8 | Petascale volumetric cloud stores and spatial indexing |
| [Proofreading &amp; Annotation]({{ '/content-library/journal-papers/proofreading/' | relative_url }}) | 8 | Human-in-the-loop proofreading and citizen science |
| [Cell Types &amp; Morphology]({{ '/content-library/journal-papers/cell-types/' | relative_url }}) | 8 | Morphological classification and synaptic fingerprints |
| [Connectomics]({{ '/content-library/journal-papers/connectomics/' | relative_url }}) | 8 | Saturated reference connectomes across species |
| [Network Analysis]({{ '/content-library/journal-papers/network-analysis/' | relative_url }}) | 10 | Graph theory, motifs, and topological invariance |
| [MRI &amp; Meso-Connectomics]({{ '/content-library/journal-papers/mri-connectomics/' | relative_url }}) | 10 | Diffusion MRI and macroscale tractography |
| [NeuroAI &amp; Biophysics]({{ '/content-library/journal-papers/neuroai/' | relative_url }}) | 8 | Connectome-constrained artificial neural networks |
| [Case Studies]({{ '/content-library/journal-papers/case-studies/' | relative_url }}) | 10 | Biological circuit discoveries and behavioral mechanisms |

**Total: 96 papers** across the 11 linked reading guides; these are guide entries, not 96 additional corpus records.
