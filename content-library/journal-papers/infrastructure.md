---
layout: page
title: "Journal Papers: Computational Infrastructure"
permalink: /content-library/journal-papers/infrastructure/
description: "Curated papers on reconstruction pipelines, data management, and tooling with summaries at beginner, intermediate, and advanced levels."
dimension: infrastructure
tags:
  - infrastructure:pipeline
  - infrastructure:segmentation
  - infrastructure:alignment
  - infrastructure:data-format
  - infrastructure:CAVE
  - infrastructure:neuroglancer
  - infrastructure:provenance
---

# Computational Infrastructure Journal Papers

Curated papers on reconstruction pipelines, segmentation architectures, annotation systems, and data management. Each paper includes summaries at three expertise levels.

---

## 1. Januszewski et al. (2018) — High-Precision Automated Reconstruction of Neurons with Flood-Filling Networks

**Citation:** Januszewski M, Kornfeld J, Li PH, Pope A, Blakely T, Lindsey L, et al. High-precision automated reconstruction of neurons with flood-filling networks. *Nature Methods*. 2018;15(8):605-610.
**DOI:** [10.1038/s41592-018-0049-4](https://doi.org/10.1038/s41592-018-0049-4)

**Tags:** `infrastructure:segmentation` `neuroai:flood-filling-network` `neuroai:deep-learning` `infrastructure:pipeline` `methodology:benchmark` `proofreading:QA-metrics`

### Summaries

**Beginner:** Before this paper, reconstructing individual neurons from brain images required enormous amounts of manual work. Flood-filling networks (FFNs) use deep learning to automatically "grow" a neuron's shape voxel by voxel through a 3D image, much like water filling a container. This approach dramatically reduced errors compared with previous methods and made large-scale brain mapping projects feasible.

**Intermediate:** Januszewski et al. introduced FFNs, a recurrent neural network architecture that performs instance segmentation by iteratively predicting object membership for voxels in an expanding field of view. Unlike boundary-detection approaches (U-Net + watershed), FFNs maintain an internal state that accumulates context as the segmentation grows, reducing topological errors at thin processes and branch points. The paper demonstrates state-of-the-art segmentation accuracy on multiple connectomics datasets with expected run lengths exceeding 1 mm in some cases.

**Advanced:** FFNs represent a paradigm shift from pixel-classification approaches by reformulating segmentation as a sequential decision process. Key architectural choices include the recurrent field-of-view movement policy, the object-centric (rather than boundary-centric) prediction target, and the multi-scale inference cascade. The paper's evaluation methodology — particularly the use of expected run length (ERL) as a metric that captures both merge and split errors in a single number — became the standard for connectomics segmentation benchmarking. Limitations include computational cost (inference is sequential per object), sensitivity to seed placement, and the need for agglomeration to handle objects that exceed the FOV.

**Key figures:** Fig. 1 (FFN architecture and growth process), Fig. 2 (segmentation accuracy comparison), Fig. 4 (expected run length analysis)

**Discussion prompts:**
- Why does the sequential, object-centric approach outperform boundary detection for neural segmentation?
- Which failure cases persist despite FFN automation, and how should proofreading prioritize them?
- How should FFN-style performance be reported for scientific (not only engineering) validity?

**Related content:** [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/), [Metrics and QA](/content-library/proofreading/metrics-and-qa/)

---

## 2. Funke et al. (2019) — Large Scale Image Segmentation with Structured Loss

**Citation:** Funke J, Tschopp FD, Grisaitis W, Sheridan A, Singh C, Saalfeld S, Turaga SC. Large scale image segmentation with structured loss based on partial differential equations. *IEEE Transactions on Pattern Analysis and Machine Intelligence*. 2019;41(7):1564-1578.
**DOI:** [10.1109/TPAMI.2018.2858744](https://doi.org/10.1109/TPAMI.2018.2858744)

**Tags:** `infrastructure:segmentation` `infrastructure:agglomeration` `neuroai:deep-learning` `methodology:benchmark` `proofreading:variation-of-information`

### Summaries

**Beginner:** Teaching a computer to segment neurons from brain images requires a way to measure how good its predictions are. This paper developed a new way to train segmentation algorithms by using a loss function (error measure) that directly penalizes topologically incorrect segmentations — like merging two separate neurons together. The result was a major improvement in automated segmentation quality.

**Intermediate:** Funke et al. address the metric mismatch problem in connectomics segmentation: standard per-voxel loss functions don't penalize topological errors (merges, splits) proportionally to their downstream impact. They introduce a structured loss based on the MALIS criterion, computed efficiently via PDE-based optimization, that directly minimizes variation of information (VI) during training. The approach produces affinity maps that, when combined with watershed and agglomeration, achieve state-of-the-art segmentation on the CREMI and FIB-25 benchmarks.

**Advanced:** The key insight is that boundary prediction accuracy and segmentation quality are different objectives — a classifier can be highly accurate at boundary detection while still producing topologically incorrect segmentations. The MALIS-inspired structured loss bridges this gap by backpropagating gradients that account for the global impact of local predictions on segment topology. The PDE formulation enables efficient gradient computation over large FOVs. This work influenced subsequent architectures including the local shape descriptors approach and waterz agglomeration. The tension between affinity-based and FFN-based approaches remains an active area.

**Key figures:** Fig. 1 (structured loss concept), Fig. 4 (segmentation comparison), Fig. 6 (CREMI benchmark results)

**Discussion prompts:**
- How does the choice of loss function affect the types of errors that persist in the final segmentation?
- When would you choose an affinity-based pipeline (this approach) versus FFNs?

**Related content:** [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/), [Error taxonomy](/content-library/proofreading/error-taxonomy/)

---

## 3. Dorkenwald et al. (2022) — CAVE: Connectome Annotation Versioning Engine

**Citation:** Dorkenwald S, McKellar CE, Macrina T, Kemnitz N, Lee K, Lu R, et al. CAVE: Connectome Annotation Versioning Engine. *bioRxiv*. 2022.
**DOI:** [10.1101/2023.07.26.550598](https://doi.org/10.1101/2023.07.26.550598)

**Tags:** `infrastructure:CAVE` `infrastructure:provenance` `infrastructure:versioning` `infrastructure:data-management` `proofreading:proofreading-tools` `methodology:reproducibility`

### Summaries

**Beginner:** When hundreds of people are correcting a brain map at the same time, you need a system to keep track of every change — who fixed what, when, and why. CAVE is like a version control system (similar to Google Docs' history or Git for code) but designed specifically for connectomics. It lets researchers go back to any previous version of the brain map and ensures that published analyses can always be reproduced.

**Intermediate:** CAVE provides a versioned, materialized annotation infrastructure for large-scale connectomics. It tracks the complete history of proofreading edits (merges, splits) and spatial annotations (synapse labels, cell types) in a chunked graph structure that supports efficient historical queries. "Materialization" produces timestamped snapshots that freeze a consistent state of the connectome for analysis and publication. CAVE powers both the FlyWire and MICrONS annotation systems.

**Advanced:** CAVE's architecture solves the reproducibility crisis in collaborative connectomics: when thousands of users continuously edit a shared segmentation, any analysis must be tied to a specific materialization timestamp to be reproducible. The chunked graph representation enables O(1) edit operations (rather than full-graph recomputation), the materialization pipeline produces denormalized tables for fast analytical queries, and the versioning system maintains complete edit provenance. Key design decisions include the separation of segmentation graph structure from spatial annotations, the use of supervoxel-level granularity for undo operations, and the CAVE client API that abstracts version management for downstream analysts.

**Key figures:** Fig. 1 (CAVE architecture), Fig. 2 (materialization pipeline), Fig. 3 (edit history and provenance)

**Discussion prompts:**
- How does CAVE's versioning model compare to general-purpose version control (Git)?
- What happens to published analyses when new proofreading edits change the connectome after publication?
- How should citation practices evolve to reference specific CAVE materializations?

**Related content:** [Provenance and versioning](/content-library/infrastructure/provenance-and-versioning/), [Proofreading tools](/content-library/proofreading/proofreading-tools/)

---

## 4. Macrina et al. (2021) — Petascale Neural Circuit Reconstruction

**Citation:** Macrina T, Lee K, Lu R, Turner NL, Wu J, Popovych S, et al. Petascale neural circuit reconstruction: automated methods. *bioRxiv*. 2021.
**DOI:** [10.1101/2021.08.04.455162](https://doi.org/10.1101/2021.08.04.455162)

**Tags:** `infrastructure:pipeline` `infrastructure:segmentation` `infrastructure:alignment` `infrastructure:agglomeration` `case-studies:MICrONS` `neuroai:deep-learning` `methodology:benchmark`

### Summaries

**Beginner:** Turning a million electron microscopy images into a wiring diagram of the brain requires a massive computational pipeline — like a factory assembly line for data. This paper describes the complete pipeline used for the MICrONS project: aligning images, finding neuron boundaries, stitching neurons across sections, detecting synapses, and packaging everything for analysis. It's the engineering blueprint for modern large-scale connectomics.

**Intermediate:** Macrina et al. describe the full automated reconstruction pipeline for the MICrONS mm³ cortical volume: image alignment (cross-section and cross-slab), affinity-based segmentation, supervoxel agglomeration (mean affinity agglomeration), synapse detection, and assignment of pre/post-synaptic partners. The pipeline processed ~2 petabytes of imagery to produce ~80,000 neurons with ~500 million synapses. Key quality metrics are reported at each stage, providing a template for evaluating reconstruction completeness.

**Advanced:** This paper is the definitive systems paper for the MICrONS pipeline and provides the most complete accounting of stage-by-stage error rates in a petascale connectomics reconstruction. Notable contributions: the multi-resolution alignment approach that handles both within-slab and between-slab registration, the agglomeration strategy that balances merge and split error rates, and the synapse detection pipeline that achieves ~90% precision and recall. The paper also documents the computational resources required (~millions of GPU-hours), providing essential data for cost estimation of future projects. The honest reporting of remaining error rates (e.g., split rate at high agglomeration thresholds) is particularly valuable.

**Key figures:** Fig. 1 (pipeline overview), Fig. 3 (segmentation quality), Fig. 5 (synapse detection), Fig. 7 (error rate analysis)

**Discussion prompts:**
- Which pipeline stage contributes the most errors to the final connectome, and how would you prioritize improvements?
- How do the computational costs scale with volume size?

**Related content:** [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/), [MICrONS visual cortex](/content-library/case-studies/microns-visual-cortex/), [Data formats](/content-library/infrastructure/data-formats/)

---

## 5. Scheffer et al. (2020) — A Connectome and Analysis of the Adult Drosophila Central Brain

**Citation:** Scheffer LK, Xu CS, Januszewski M, Lu Z, Takemura SY, Hayworth KJ, et al. A connectome and analysis of the adult *Drosophila* central brain. *eLife*. 2020;9:e57443.
**DOI:** [10.7554/eLife.57443](https://doi.org/10.7554/eLife.57443)

**Tags:** `infrastructure:pipeline` `infrastructure:segmentation` `case-studies:Drosophila` `connectomics:graph-theory` `connectomics:community-detection` `proofreading:proofreading-strategy`

### Summaries

**Beginner:** This paper describes the "hemibrain" — a map of about half the fruit fly brain, containing roughly 25,000 neurons and 20 million synaptic connections. It was the largest dense connectome at the time of publication and included not just the wiring diagram but also initial analyses of circuit structure, neuron types, and network properties. Think of it as both an engineering achievement and a scientific resource.

**Intermediate:** Scheffer et al. present the hemibrain connectome, reconstructed from a FIB-SEM volume of *Drosophila* central brain at 8 nm isotropic resolution. The paper covers the full pipeline: FFN-based segmentation, extensive proofreading (~50 person-years of effort), synapse detection, and neuron type assignment. Analysis sections describe connectivity patterns including cell type-specific connection profiles, circuit motifs, and cross-hemisphere symmetry. The dataset was released with extensive metadata and is queryable via neuPrint.

**Advanced:** The hemibrain paper demonstrates the current frontier of "production" connectomics. Key methodological points include: (1) the proofreading strategy that prioritized large neurons with significant downstream impact over completeness of small fragments; (2) the confidence-scoring system for connections based on synapse count thresholds; (3) the neuPrint database architecture that enables graph queries across the full connectome. Limitations include boundary effects (neurons extending outside the volume), the single-hemisphere reconstruction, and the proofreading completeness heterogeneity across brain regions. The neuron type nomenclature system and its relationship to genetic driver lines is valuable for cross-modal validation.

**Key figures:** Fig. 1 (hemibrain volume), Fig. 3 (reconstruction quality), Fig. 5 (connectivity types), Fig. 8 (circuit motifs)

**Discussion prompts:**
- How does the proofreading prioritization strategy affect which biological questions can be reliably answered?
- What are the tradeoffs of the hemibrain's FIB-SEM approach versus FlyWire's ATUM-SEM approach for the same organism?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [Proofreading strategies](/content-library/proofreading/proofreading-strategies/)

---

## 6. Berger et al. (2018) — VAST: Volume Annotation and Segmentation Tool

**Citation:** Berger DR, Seung HS, Lichtman JW. VAST (Volume Annotation and Segmentation Tool): Efficient manual and semi-automatic labeling of large 3D image stacks. *Frontiers in Neural Circuits*. 2018;12:88.
**DOI:** [10.3389/fncir.2018.00088](https://doi.org/10.3389/fncir.2018.00088)

**Tags:** `infrastructure:neuroglancer` `proofreading:proofreading-tools` `infrastructure:data-format` `infrastructure:data-management` `methodology:ground-truth`

### Summaries

**Beginner:** Before you can train a computer to find neurons in images, humans need to manually label example images to create "ground truth" data. VAST is a desktop tool designed for this manual labeling work. It lets annotators paint over neurons in 3D image stacks, assign labels, and track their work efficiently. Good ground truth data is essential for training and evaluating every automated segmentation system.

**Intermediate:** VAST provides a desktop annotation environment optimized for large-scale manual and semi-automatic segmentation of EM volumes. Features include multi-resolution rendering, efficient label management for thousands of objects, undo/redo with full history, and export to standard formats (TIFF stacks, HDF5). VAST was used to produce ground truth annotations for several landmark datasets including Kasthuri et al. (2015). Its design emphasizes annotation throughput and consistency for creating training data.

**Advanced:** While cloud-based tools (Neuroglancer, CAVE) now dominate production proofreading workflows, VAST remains relevant for ground truth creation where precise manual control is needed. The tool's architecture — local rendering with on-disk storage rather than cloud streaming — provides deterministic performance independent of network conditions. Its annotation model (paint-based rather than supervoxel-based) is well-suited for creating dense ground truth that does not inherit biases from automated pre-segmentation. For benchmark creation and segmentation validation, VAST's pixel-precise annotations remain the gold standard approach.

**Key figures:** Fig. 1 (VAST interface), Fig. 2 (annotation workflow), Fig. 4 (ground truth examples)

**Discussion prompts:**
- When should you use desktop tools (VAST) versus cloud tools (Neuroglancer/CAVE) for annotation?
- How does the choice of annotation tool affect the quality and biases of ground truth data?

**Related content:** [Proofreading tools](/content-library/proofreading/proofreading-tools/), [Metrics and QA](/content-library/proofreading/metrics-and-qa/)
