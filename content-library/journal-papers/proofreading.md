---
layout: page
title: "Journal Papers: Proofreading & Quality Control"
permalink: /content-library/journal-papers/proofreading/
description: "Curated papers on connectome proofreading, error correction, and quality metrics with summaries at beginner, intermediate, and advanced levels."
dimension: proofreading
tags:
  - proofreading:merge-error
  - proofreading:split-error
  - proofreading:proofreading-strategy
  - proofreading:QA-metrics
  - proofreading:proofreading-tools
  - proofreading:crowd-sourced-proofreading
use_layout_hero: false
content_type: core
---

# Proofreading & Quality Control Journal Papers

Curated papers on proofreading workflows, error detection, quality metrics, and collaborative correction. Each paper includes summaries at three expertise levels.

---

## 1. Dorkenwald et al. (2024) — Neuronal Wiring Diagram of an Adult Brain (FlyWire)

**Citation:** Dorkenwald S, Matsliah A, Sterling AR, Schlegel P, Yu SC, McKellar CE, et al. Neuronal wiring diagram of an adult brain. *Nature*. 2024;634:124-138.
**DOI:** [10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y)

**Tags:** `proofreading:crowd-sourced-proofreading` `proofreading:proofreading-strategy` `proofreading:QA-metrics` `case-studies:FlyWire` `case-studies:Drosophila` `case-studies:whole-brain` `infrastructure:CAVE`

### Summaries

**Beginner:** This paper describes the first complete wiring diagram of an adult brain — the fruit fly *Drosophila melanogaster* — containing about 139,000 neurons and 54.5 million synapses between them. What makes this project special is that it was completed through collaboration: hundreds of researchers and proofreaders worldwide helped check and correct the computer-generated neuron shapes, like a Wikipedia for brain maps. This "crowd-sourced" approach was essential because no single lab could have done all the proofreading alone.

**Intermediate:** Dorkenwald et al. present the FlyWire whole-brain connectome, reconstructed from the FAFB EM volume via automated segmentation with boundary-detecting convolutional nets followed by large-scale collaborative proofreading. Hundreds of scientists and proofreaders from more than 50 laboratories joined FlyWire, more than 200 of whom made over 100 edits; in the later phase, centralized teams at Princeton and Cambridge proofread most of the remaining neurons, with contributions from citizen scientists. The authors estimate the reconstruction took about 33 person-years of proofreading. The paper reports completeness and accuracy evaluations (for example, re-proofreading 826 central-brain neurons, against which the released segments scored an average F1 of 99.2% by volume) and analyses of information flow, projections between regions, and cross-hemisphere connectivity.

**Advanced:** FlyWire's proofreading is a case study in scaling human effort: an open community in the early phase, focused on neurons of interest to participating labs, followed by centralized professional teams to finish the remainder. The chunked supervoxel graph (the ChunkedGraph, later part of CAVE) enabled concurrent editing by many users while keeping the segmentation consistent. Two points matter for anyone analyzing the data. First, the reconstruction is released in versions (the paper's analyses use version 783) and remains open for further proofreading, so any analysis should cite the version it used. Second, the connectome includes only chemical synapses, and the authors identify incomplete attachment of small twigs to backbones as the main current limit on accuracy — which affects weak connections more than strong, multi-synapse ones. The 139,255 count is of neurons; only a few glia were proofread.

**Key figures:** Fig. 1 (whole-brain reconstruction overview), Fig. 2 (neuron categories by flow and superclass), Fig. 4 (neuropil-to-neuropil projections), Extended Data Fig. 2 (completeness and accuracy of the reconstruction)

**Discussion prompts:**
- If some connections are missed because small twigs remain unattached, how does that bias the resulting connectome, and which biological questions are most affected?
- What quality thresholds should be met before declaring a connectome "complete"?
- How does FlyWire's open community model compare with the hemibrain's closed proofreading process by paid teams?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [Proofreading strategies](/content-library/proofreading/proofreading-strategies/), [Metrics and QA](/content-library/proofreading/metrics-and-qa/)

---

## 2. Plaza et al. (2014) — Toward Large-Scale Connectome Reconstructions

**Citation:** Plaza SM, Scheffer LK, Chklovskii DB. Toward large-scale connectome reconstructions. *Current Opinion in Neurobiology*. 2014;25:201-210.
**DOI:** [10.1016/j.conb.2014.01.019](https://doi.org/10.1016/j.conb.2014.01.019)

**Tags:** `proofreading:proofreading-strategy` `proofreading:proofreading-tools` `infrastructure:pipeline` `methodology:experimental-design` `proofreading:QA-metrics`

### Summaries

**Beginner:** Early connectomes were heroic efforts that took person-months of manual work per neuron — an approach that cannot scale to whole brains. This review asks what would have to change to make much larger connectomes practical, from how the images are collected to how the finished wiring diagram is analyzed.

**Intermediate:** Plaza et al. identify five areas that need more attention before connectomes can grow substantially: (1) imaging better suited to automatic reconstruction, with excellent z-resolution; (2) automatic detection, validation, and measurement of synapses; (3) reconstruction methods that keep and use uncertainty metrics for every object, from the initial images through segmentation, reconstruction, and connectome queries; (4) fully incremental processes, so the connectome can be used before it is complete; and (5) better tools for analyzing connectomes once they exist.

**Advanced:** Two of the five recommendations are the most relevant to proofreading. Carrying uncertainty for every object through to connectome queries means a proofreader's effort can be directed at the uncertain decisions that most affect a scientific question, rather than applied uniformly. Fully incremental processes mean the connectome is usable, and versioned, while proofreading continues — the model that later large projects adopted with versioned releases. Read the review alongside the FlyWire and MICrONS papers and ask which of the five areas each project addressed, and which remain open.

**Key figures:** Read it for the argument; the five areas listed above are the core of the paper.

**Discussion prompts:**
- How do you determine the "good enough" threshold for proofreading in your specific scientific context?
- Which pipeline improvements would most reduce proofreading burden?

**Related content:** [Proofreading strategies](/content-library/proofreading/proofreading-strategies/), [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/)

---

## 3. Zung et al. (2017) — An Error Detection and Correction Framework for Connectomics

**Citation:** Zung J, Tartavull I, Lee K, Seung HS. An error detection and correction framework for connectomics. *Advances in Neural Information Processing Systems*. 2017;30.

**Tags:** `proofreading:merge-error` `proofreading:split-error` `neuroai:deep-learning` `infrastructure:segmentation` `methodology:benchmark`

### Summaries

**Beginner:** After a computer segments neurons in brain images, it inevitably makes mistakes — sometimes fusing two neurons together (merge error) or breaking one neuron into pieces (split error). This paper describes a neural network that can automatically detect these mistakes and suggest corrections. Think of it as an automated quality checker that flags problems for human review, saving time compared to checking everything manually.

**Intermediate:** Zung et al. define two tasks that operate on a candidate object: the raw image plus a binary mask of one segmented object. Error detection outputs a map of where the object contains split or merge errors. Error correction outputs the true object, framed as "object mask pruning": the candidate mask is treated as a superset of the true object, and the network removes what does not belong. Both tasks use multiscale 3D convolutional networks. The framework operates on the segmentation output rather than modifying the segmentation algorithm, so it can sit downstream of any pipeline.

**Advanced:** The error detection approach decouples quality improvement from the segmentation algorithm itself, enabling a modular pipeline where detection and correction are independently improvable. The authors report high error-detection accuracy, and that the error-correcting network performs better when given "advice" from the detector — the union of erroneous objects — as an extra input. That coupling is the idea to take away: a detector's output can be used both to steer an automated corrector and to build a ranked queue for human proofreaders.

**Key figures:** Look for the task definitions (detection and object mask pruning), the example error maps, and the comparison of correction with and without advice from the detector.

**Discussion prompts:**
- At what detection precision threshold should errors be corrected automatically versus routed to humans?
- How do error detection rates differ for merge versus split errors, and why?

**Related content:** [Error taxonomy](/content-library/proofreading/error-taxonomy/), [Worked examples](/content-library/proofreading/worked-examples/)

---

## 4. Matejek et al. (2019) — Biologically-Constrained Graphs for Global Connectomics Reconstruction

**Citation:** Matejek B, Haehn D, Zhu H, Wei D, Parag T, Pfister H. Biologically-constrained graphs for global connectomics reconstruction. In: *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. 2019:2084-2093.
**DOI:** [10.1109/CVPR.2019.00219](https://doi.org/10.1109/CVPR.2019.00219)

**Tags:** `infrastructure:segmentation` `infrastructure:agglomeration` `proofreading:merge-error` `proofreading:split-error` `neuroai:deep-learning` `methodology:benchmark`

### Summaries

**Beginner:** When computers trace neurons through brain images, they often break one neuron into several pieces, especially at its thinnest points. This paper uses knowledge about how real neurons are shaped to decide which pieces should be joined back together, and uses the whole picture rather than just the local image to make those decisions.

**Intermediate:** Standard pipelines have two steps: pixel-based segmentation (affinity prediction and watershed) and agglomeration that merges over-segmented regions. Matejek et al. add a third refinement step. They extract a graph from the segmentation, with nodes for segments and edges for potential split errors, use biologically inspired geometric constraints based on neuron morphology to reduce the number of nodes and edges, and train two neural networks that learn neuronal shapes to help build the graph. Region merging is then reformulated as a graph partitioning problem so that global context informs each decision.

**Advanced:** The paper addresses a fundamental weakness of purely local agglomeration: whether two pieces belong together is often obvious from the shape of the whole neuron but invisible to a classifier looking at a small neighborhood. Using morphology to prune candidate edges keeps the graph small enough for global partitioning to be practical. Tested on four connectomics datasets, the method improved variation of information by an average of 21.3%. The approach is complementary to error detection methods (Zung et al., 2017) and can be added after an existing agglomeration pipeline.

**Key figures:** Look for the graph construction from the segmentation, the examples of neurons split at thin points, and the variation-of-information results across datasets.

**Discussion prompts:**
- Which biological constraints are robust across species and brain regions, and which are context-dependent?
- How do you balance the risk of over-constraining (increased splits) against under-constraining (increased merges)?

**Related content:** [Error taxonomy](/content-library/proofreading/error-taxonomy/), [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/)

---

## 5. Dorkenwald et al. (2017) — Automated Synaptic Connectivity Inference for Volume EM

**Citation:** Dorkenwald S, Schubert PJ, Killinger MF, Urban G, Mikula S, Svara F, Kornfeld J. Automated synaptic connectivity inference for volume electron microscopy. *Nature Methods*. 2017;14(4):435-442.
**DOI:** [10.1038/nmeth.4206](https://doi.org/10.1038/nmeth.4206)

**Tags:** `infrastructure:segmentation` `infrastructure:agglomeration` `neuroanatomy:synapse` `proofreading:QA-metrics` `neuroai:deep-learning`

### Summaries

**Beginner:** Once neurons are traced in 3D, you need to figure out where they connect to each other — finding all the synapses — and what kinds of cells and cell parts are involved. This paper describes a method that starts from hand-traced neuron skeletons and automatically fills in synapses, cell compartments, and cell types to produce a wiring diagram. Getting this right is critical because the synaptic connections are the actual wiring diagram — they determine how information flows through the brain.

**Intermediate:** Dorkenwald et al. present SyConn, a framework that uses deep convolutional neural networks and random forest classifiers to infer a richly annotated synaptic connectivity matrix from manual neurite skeleton reconstructions. It automatically identifies mitochondria, synapses and their types, axons, dendrites, spines, myelin, somata, and cell types. The authors tested it on serial block-face EM datasets from zebrafish, mouse, and zebra finch, and computed the synaptic wiring of songbird basal ganglia (Area X).

**Advanced:** The key design decision is to combine human skeleton tracing, which is fast and reliable for following neurites, with automated classifiers for everything else: synapse detection and typing, compartment labels (axon, dendrite, soma, spine), and cell type. This division of labor makes each automated stage separately checkable. The biological results show what a richly annotated connectome allows: in the songbird basal ganglia, cell types with high firing rates in vivo had higher densities of mitochondria and vesicles, and synapse sizes and numbers scaled systematically with the postsynaptic cell type. For proofreading, the lesson is that every automated annotation layer adds its own error rate, and those errors propagate into the connectivity matrix.

**Key figures:** Look for the overview of the SyConn workflow, the examples of automatically identified structures, and the songbird basal ganglia connectivity analysis.

**Discussion prompts:**
- How do synapse detection error rates propagate into connectome-level connectivity analysis?
- Which automated annotation layers (synapse type, compartment, cell type) would you validate first, and how?

**Related content:** [Synapse classification](/content-library/neuroanatomy/synapse-classification/), [Metrics and QA](/content-library/proofreading/metrics-and-qa/)

---

## 6. Beier et al. (2017) — Multicut Brings Automated Neurite Segmentation Closer to Human Performance

**Citation:** Beier T, Pape C, Rahaman N, Prange T, Berg S, Bock DD, et al. Multicut brings automated neurite segmentation closer to human performance. *Nature Methods*. 2017;14(2):101-102.
**DOI:** [10.1038/nmeth.4151](https://doi.org/10.1038/nmeth.4151)

**Tags:** `infrastructure:agglomeration` `infrastructure:segmentation` `methodology:benchmark` `proofreading:merge-error` `proofreading:split-error`

### Summaries

**Beginner:** After an algorithm breaks a brain image into millions of tiny pieces (supervoxels), it needs to decide which pieces belong to the same neuron. This "grouping" problem is mathematically related to a classic optimization problem called graph partitioning. This paper uses a technique called "multicut" that finds the best grouping by considering all the evidence simultaneously, rather than making greedy piece-by-piece decisions.

**Intermediate:** Multicut formulations for segmentation agglomeration treat the problem as a graph partitioning optimization: given a graph of supervoxels with edge weights indicating merge probability, find the optimal partition that minimizes total cost. The "lifted multicut" extends this by adding long-range edges that encode non-local constraints. Compared to greedy agglomeration (which processes edges in sorted order), multicut finds globally better solutions at higher computational cost. As the title says, the approach brings automated performance closer to human-level on benchmark datasets.

**Advanced:** The multicut formulation provides theoretical guarantees (optimal under the model assumptions) that greedy agglomeration lacks. The lifted multicut extension is particularly relevant for connectomics because it enables encoding constraints between non-adjacent supervoxels — for example, that two supervoxels on opposite sides of a cell membrane should not be merged even if intermediate supervoxels suggest otherwise. The computational cost is the main limitation: exact multicut is NP-hard, so practical implementations rely on approximate solvers. The tradeoff between solution quality and computation time determines when multicut is preferred over simpler greedy approaches.

**Key figures:** This is a short correspondence; read it with its supplementary material for the method details and benchmark comparisons.

**Discussion prompts:**
- When is the computational cost of multicut justified over greedy agglomeration?
- How do long-range lifted edges improve segmentation in practice?

**Related content:** [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/), [Error taxonomy](/content-library/proofreading/error-taxonomy/)

---

## 7. Dorkenwald et al. (2022) — FlyWire: Online Community for Whole-Brain Connectomics

**Citation:** Dorkenwald S, McKellar CE, Macrina T, Kemnitz N, Lee K, Lu R, et al. FlyWire: online community for whole-brain connectomics. *Nature Methods*. 2022;19:119-128.
**DOI:** [10.1038/s41592-021-01330-0](https://doi.org/10.1038/s41592-021-01330-0)

**Tags:** `proofreading:crowd-sourced-proofreading` `proofreading:proofreading-tools` `case-studies:FlyWire` `data-storage:CAVE` `methodology:open-science`

### Summaries

**Beginner:** Building a complete brain wiring diagram requires checking millions of computer-traced neurons by hand — far too much work for any single lab. This paper introduces FlyWire, an online platform where researchers around the world can collaboratively proofread the fruit fly brain, much like Wikipedia lets anyone edit an encyclopedia. The platform provides specialized tools for viewing 3D neurons and fixing errors, and tracks all changes so nothing is lost.

**Intermediate:** Dorkenwald et al. describe the FlyWire platform architecture for collaborative proofreading at scale. FlyWire represents the segmentation as a spatially chunked supervoxel graph (the ChunkedGraph, later incorporated into CAVE, the Connectome Annotation Versioning Engine), so that many users can edit the same neurons concurrently without introducing inconsistencies. The platform includes a Neuroglancer-based interface for browser-based 3D proofreading and keeps the full edit history, which is programmatically accessible for uses such as estimating proofreading accuracy or building incentive systems. The paper analyzes proofreading of a set of 183 neurons proofread three times and demonstrates circuit analysis by reconstructing the connectome of mechanosensory neurons.

**Advanced:** FlyWire's technical contribution is the integration of a chunked supervoxel graph data structure (making interactive edits practical on a whole-brain segmentation), collaborative editing that keeps every user on the latest state, and community management infrastructure. Key design decisions include: editing a supervoxel graph rather than individual voxels (merges add graph edges; splits use a max-flow min-cut on a local cutout of the graph), which trades spatial precision for speed; a recorded edit history analogous to a wiki's page history; and an open community that requires sharing reconstructions with attribution rather than restricting membership. The platform demonstrated that distributed proofreading can scale to whole-brain datasets while maintaining quality through community oversight.

**Key figures:** Fig. 2 (proofreading the supervoxel graph), Fig. 3 (the ChunkedGraph approach), Fig. 5 (analysis of triple-proofread neurons), Fig. 6 (mechanosensory neuron connectivity)

**Discussion prompts:**
- What are the advantages and risks of open community proofreading compared to expert-only approaches?
- How does a chunked supervoxel graph let many users edit the same neuron without introducing inconsistencies?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [Proofreading strategies](/content-library/proofreading/proofreading-strategies/)

---

## 8. Seung (2009) — Reading the Book of Memory: Sparse Sampling Versus Dense Mapping of Connectomes

**Citation:** Seung HS. Reading the book of memory: sparse sampling versus dense mapping of connectomes. *Neuron*. 2009;62(1):17-29.
**DOI:** [10.1016/j.neuron.2009.03.020](https://doi.org/10.1016/j.neuron.2009.03.020)

**Tags:** `proofreading:proofreading-strategy` `methodology:experimental-design` `connectomics:graph-theory`

### Summaries

**Beginner:** Many theories of the brain assume rules about which kinds of neurons connect to which. How should we test those rules? One way is to record from pairs of connected neurons, sampling a few pairs from many animals (sparse sampling). Another is to map every connection in one animal's brain region (dense mapping) and then work out the neurons' properties from the map. This paper compares the two, and argues that the most exciting prospect for dense maps is reading out memories stored in the wiring.

**Intermediate:** Seung contrasts two ways of testing pairwise models of connectivity, in which connection rules depend on the cell types or functional properties of the two neurons. Sparse sampling measures the functional properties of connected pairs, drawing pairs from many specimens. Dense mapping finds a connectome — every connection in a single specimen — and infers the functional properties of neurons through computational analysis of the map. The paper weighs what each can and cannot reveal, and argues that dense maps could go beyond pairwise rules to decoding the memories hypothesized to be stored in connections.

**Advanced:** This paper laid the theoretical groundwork for the strategic decisions that shaped subsequent connectomics projects. The dense vs. sparse dichotomy maps directly onto proofreading strategy: dense reconstruction demands exhaustive proofreading within a bounded volume, while sparse sampling requires accurate reconstruction of individual neurons but tolerates gaps. The contrast between pooling pairs across many specimens and analyzing one complete specimen remains a useful framework for project planning. It also raises the "n-of-one" problem that later work confronted directly: a single dense reconstruction cannot by itself distinguish stereotyped wiring from individual variation, which motivates comparing connectomes across individuals.

**Key figures:** Read it for the argument contrasting sparse sampling of connected pairs with dense mapping of a single specimen.

**Discussion prompts:**
- How has the dense vs. sparse tradeoff shifted as automation has improved since 2009?
- What scientific questions absolutely require dense reconstruction, and which can be answered with sparse sampling?

**Related content:** [Proofreading strategies](/content-library/proofreading/proofreading-strategies/), [Graph representations](/content-library/connectomics/graph-representations/)
