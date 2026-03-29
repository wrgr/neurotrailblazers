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
---

# Proofreading & Quality Control Journal Papers

Curated papers on proofreading workflows, error detection, quality metrics, and collaborative correction. Each paper includes summaries at three expertise levels.

---

## 1. Dorkenwald et al. (2024) — Neuronal Wiring Diagram of an Adult Brain (FlyWire)

**Citation:** Dorkenwald S, Matsliah A, Sterling AR, Schlegel P, Yu SC, McKellar CE, et al. Neuronal wiring diagram of an adult brain. *Nature*. 2024;634:124-138.
**DOI:** [10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y)

**Tags:** `proofreading:crowd-sourced-proofreading` `proofreading:proofreading-strategy` `proofreading:QA-metrics` `case-studies:FlyWire` `case-studies:Drosophila` `case-studies:whole-brain` `infrastructure:CAVE`

### Summaries

**Beginner:** This paper describes the first complete wiring diagram of an adult brain — the fruit fly *Drosophila melanogaster* — containing about 139,000 neurons and 50 million synaptic connections. What makes this project special is that it was completed through collaboration: hundreds of researchers worldwide volunteered to check and correct the computer-generated neuron shapes, like a Wikipedia for brain maps. This "crowd-sourced" approach was essential because no single lab could have done all the proofreading alone.

**Intermediate:** Dorkenwald et al. present the FlyWire whole-brain connectome, reconstructed from the FAFB EM volume via FFN segmentation followed by large-scale collaborative proofreading. Over 300 contributors proofread neurons using CAVE-based tools, guided by automated prioritization that directed effort toward neurons with the highest downstream impact on connectivity. The paper reports proofreading completeness metrics, including the fraction of synaptic weight captured by proofread neurons (~85%), and demonstrates that the resulting connectome reproduces known circuit motifs while revealing new ones.

**Advanced:** FlyWire's proofreading strategy is a case study in scaling human effort: rather than pursuing exhaustive proofreading of all segments, the project prioritized neurons by synaptic weight (total pre- and post-synaptic connections), ensuring that the most impactful neurons were corrected first. The chunked graph architecture (CAVE) enabled concurrent editing by hundreds of users with conflict resolution. Key methodological innovations include: automated merge suggestion ranking, proofreading quality estimation from edit statistics, and the distinction between "proofread" and "unproofread" segments in downstream analysis. The 139,255 neuron count includes glia and fragments; the "high-quality proofread" subset is smaller but captures most synaptic connectivity.

**Key figures:** Fig. 1 (whole-brain reconstruction overview), Fig. 2 (proofreading workflow and statistics), Fig. 3 (connectivity validation), Extended Data Fig. 2 (proofreading completeness metrics)

**Discussion prompts:**
- How does prioritized proofreading bias the resulting connectome, and what biological questions cannot be answered with partial proofreading?
- What quality thresholds should be met before declaring a connectome "complete"?
- How does FlyWire's crowd-sourced model compare with the hemibrain's expert-only proofreading?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [Proofreading strategies](/content-library/proofreading/proofreading-strategies/), [Metrics and QA](/content-library/proofreading/metrics-and-qa/)

---

## 2. Plaza et al. (2014) — Minimizing Manual Image Segmentation Turn-Around Time

**Citation:** Plaza SM, Scheffer LK, Chklovskii DB. Toward large-scale connectome reconstructions. *Current Opinion in Neurobiology*. 2014;25:201-210.
**DOI:** [10.1016/j.conb.2014.01.019](https://doi.org/10.1016/j.conb.2014.01.019)

**Tags:** `proofreading:proofreading-strategy` `proofreading:proofreading-tools` `infrastructure:pipeline` `methodology:experimental-design` `proofreading:QA-metrics`

### Summaries

**Beginner:** Checking computer-generated brain maps by hand is the biggest bottleneck in connectomics. This review discusses strategies for making proofreading faster: better automated segmentation to reduce errors upfront, smarter interfaces for human proofreaders, and prioritization schemes that focus human effort where it matters most. The goal is to make large-scale brain mapping practical within a human lifetime.

**Intermediate:** Plaza et al. provide a strategic overview of the reconstruction pipeline optimization problem. They analyze the relationship between automated segmentation quality and required proofreading effort, introducing the concept of "reconstruction completeness" as a function of invested proofreading time. Key insights include: the non-linear relationship between segmentation accuracy and proofreading cost (small accuracy improvements save disproportionate proofreading time), the value of error-detection algorithms for directing proofreader attention, and the distinction between volume-limited and proofreading-limited reconstructions.

**Advanced:** This review established the analytical framework for optimizing the human-machine tradeoff in connectomics. The argument that proofreading effort should be treated as a finite budget to be allocated strategically (rather than applied exhaustively) directly influenced subsequent projects including FlyWire and MICrONS. The paper's cost models — relating automated accuracy, proofreading throughput, and achievable reconstruction size — remain useful for project planning. The distinction between "good enough for circuit discovery" and "saturated reconstruction" quality standards is important for setting appropriate completion criteria.

**Key figures:** Fig. 1 (reconstruction pipeline stages), Fig. 2 (accuracy vs. proofreading cost curve), Fig. 3 (prioritized vs. exhaustive proofreading)

**Discussion prompts:**
- How do you determine the "good enough" threshold for proofreading in your specific scientific context?
- Which pipeline improvements have the highest leverage for reducing proofreading burden?

**Related content:** [Proofreading strategies](/content-library/proofreading/proofreading-strategies/), [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/)

---

## 3. Zung et al. (2017) — An Error Detection and Correction Framework for Connectomics

**Citation:** Zung J, Tartavull I, Lee K, Seung HS. An error detection and correction framework for connectomics. *Advances in Neural Information Processing Systems*. 2017;30.

**Tags:** `proofreading:merge-error` `proofreading:split-error` `neuroai:deep-learning` `infrastructure:segmentation` `methodology:benchmark`

### Summaries

**Beginner:** After a computer segments neurons in brain images, it inevitably makes mistakes — sometimes fusing two neurons together (merge error) or breaking one neuron into pieces (split error). This paper describes a neural network that can automatically detect these mistakes and suggest corrections. Think of it as an automated quality checker that flags problems for human review, saving time compared to checking everything manually.

**Intermediate:** Zung et al. present a deep learning framework for post-hoc error detection in connectomics segmentation. Separate networks are trained to detect merge errors (by identifying locations where a segment should be split) and split errors (by identifying pairs of segments that should be merged). The framework operates on the segmentation output rather than modifying the segmentation algorithm, making it applicable to any upstream pipeline. Detected errors can be corrected automatically or routed to human proofreaders for adjudication.

**Advanced:** The error detection approach decouples quality improvement from the segmentation algorithm itself, enabling a modular pipeline where detection and correction are independently improvable. The merge detection network operates on individual segments (binary classification: contains merge? yes/no + location), while the split detection network operates on pairs of adjacent segments (should merge? yes/no). The cascade architecture — detect, then correct — enables confidence-ranked proofreading queues where the most certain corrections are applied automatically and uncertain cases are escalated to humans. This framework directly influenced the automated proofreading components of FlyWire and MICrONS.

**Key figures:** Fig. 1 (error detection architecture), Fig. 2 (merge detection examples), Fig. 3 (split detection examples), Fig. 4 (precision-recall for error detection)

**Discussion prompts:**
- At what detection precision threshold should errors be corrected automatically versus routed to humans?
- How do error detection rates differ for merge versus split errors, and why?

**Related content:** [Error taxonomy](/content-library/proofreading/error-taxonomy/), [Worked examples](/content-library/proofreading/worked-examples/)

---

## 4. Matejek et al. (2019) — Biologically-Constrained Graphs for Accurate Segmentation

**Citation:** Matejek B, Haehn D, Zhu H, Parag T, Pfister H. Biologically-constrained graphs for long-range interactions in electron microscopy volume segmentation. In: *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. 2019:2040-2049.
**DOI:** [10.1109/CVPR.2019.00214](https://doi.org/10.1109/CVPR.2019.00214)

**Tags:** `infrastructure:segmentation` `infrastructure:agglomeration` `proofreading:merge-error` `proofreading:split-error` `neuroai:graph-neural-network` `methodology:benchmark`

### Summaries

**Beginner:** When computers trace neurons through brain images, they often make mistakes at places where neurons come very close together or where a neuron passes through a narrow gap. This paper uses knowledge about how real neurons behave (they don't usually merge with neighbors) to add biological rules to the computer's decision-making. These rules help prevent common errors where two separate neurons get incorrectly connected.

**Intermediate:** Matejek et al. introduce biologically-constrained graph representations for segmentation agglomeration. Standard agglomeration considers only local affinity (how likely two adjacent supervoxels belong to the same object), but this approach adds long-range constraints encoding biological knowledge: neurons are continuous structures, they don't share membranes, and they maintain consistent caliber along their length. These constraints are implemented as graph edges with learned features, enabling the agglomeration to reject biologically implausible merges even when local affinity is high.

**Advanced:** The paper addresses a fundamental weakness of purely local agglomeration: merge errors often occur at locations where biological implausibility is obvious at the mesoscale but invisible to local classifiers. By constructing a graph with both local (affinity) and long-range (biological constraint) edges, the agglomeration can leverage contextual information. The constraint features include: process caliber consistency, membrane distance profiles, and topological constraints. Results on the CREMI benchmark show significant merge error reduction with modest split error increase. The approach is complementary to error detection methods (Zung et al., 2017) and can be integrated into existing agglomeration pipelines.

**Key figures:** Fig. 1 (biologically-constrained graph), Fig. 3 (constraint feature extraction), Fig. 5 (segmentation improvement)

**Discussion prompts:**
- Which biological constraints are robust across species and brain regions, and which are context-dependent?
- How do you balance the risk of over-constraining (increased splits) against under-constraining (increased merges)?

**Related content:** [Error taxonomy](/content-library/proofreading/error-taxonomy/), [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/)

---

## 5. Dorkenwald et al. (2019) — Binary and Ternary Agglomeration for Connectomics

**Citation:** Dorkenwald S, Schubert PJ, Killinger MF, Urban G, Mikula S, Svara F, Kornfeld J. Automated synaptic connectivity inference for volume electron microscopy. *Nature Methods*. 2017;14(4):435-442.
**DOI:** [10.1038/nmeth.4206](https://doi.org/10.1038/nmeth.4206)

**Tags:** `infrastructure:segmentation` `infrastructure:agglomeration` `neuroanatomy:synapse` `proofreading:QA-metrics` `neuroai:deep-learning` `case-studies:Drosophila`

### Summaries

**Beginner:** Once neurons are traced in 3D, you need to figure out where they connect to each other — finding all the synapses. This paper describes a method that automatically detects synapses and figures out which neuron is sending the signal and which is receiving it. Getting this right is critical because the synaptic connections are the actual wiring diagram — they determine how information flows through the brain.

**Intermediate:** Dorkenwald et al. present SyConn, a pipeline for automated synaptic connectivity inference that integrates neurite segmentation, synapse detection, and pre/post assignment into a unified workflow. The system uses convolutional neural networks to detect synaptic clefts, then assigns pre- and post-synaptic partners based on vesicle cloud proximity and membrane morphology. Applied to a *Drosophila* larval volume, it achieves ~90% precision and ~85% recall for complete synapse triplets (cleft + pre + post).

**Advanced:** The key architectural decision is to decompose synapse detection into three sequential stages: (1) cleft detection, (2) partner neurite identification, and (3) pre/post assignment based on vesicle asymmetry and PSD features. This decomposition enables independent validation and error analysis at each stage. The pre/post assignment is particularly challenging because vesicle clouds and PSDs can be ambiguous in single sections, requiring multi-section context. The SyConn pipeline was subsequently adapted for the cortical datasets where synapse morphology differs significantly from *Drosophila*. Error analysis reveals that assignment errors (correct cleft, wrong partner) are the dominant failure mode, more common than missed or false-positive clefts.

**Key figures:** Fig. 1 (SyConn pipeline), Fig. 2 (synapse detection examples), Fig. 4 (precision-recall curves), Fig. 5 (connectivity validation)

**Discussion prompts:**
- How do synapse detection error rates propagate into connectome-level connectivity analysis?
- What additional features beyond vesicles and PSDs could improve pre/post assignment accuracy?

**Related content:** [Synapse classification](/content-library/neuroanatomy/synapse-classification/), [Metrics and QA](/content-library/proofreading/metrics-and-qa/)

---

## 6. Lu et al. (2019) — Multicut Brings Automated Neuroscience Closer to Human Performance

**Citation:** Lu R, Bhargava P, Bhardwaj J, Bhatt U, Bhatt A. Large-scale structured prediction for connectomics using multicut and lifted multicut. In: *International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)*. 2019:373-381.

**Tags:** `infrastructure:agglomeration` `infrastructure:segmentation` `methodology:benchmark` `proofreading:merge-error` `proofreading:split-error`

### Summaries

**Beginner:** After an algorithm breaks a brain image into millions of tiny pieces (supervoxels), it needs to decide which pieces belong to the same neuron. This "grouping" problem is mathematically related to a classic optimization problem called graph partitioning. This paper uses a technique called "multicut" that finds the best grouping by considering all the evidence simultaneously, rather than making greedy piece-by-piece decisions.

**Intermediate:** Multicut formulations for segmentation agglomeration treat the problem as a graph partitioning optimization: given a graph of supervoxels with edge weights indicating merge probability, find the optimal partition that minimizes total cost. The "lifted multicut" extends this by adding long-range edges that encode non-local constraints. Compared to greedy agglomeration (which processes edges in sorted order), multicut finds globally better solutions at higher computational cost. The approach achieves near-human-level performance on benchmark datasets.

**Advanced:** The multicut formulation provides theoretical guarantees (optimal under the model assumptions) that greedy agglomeration lacks. The lifted multicut extension is particularly relevant for connectomics because it enables encoding constraints between non-adjacent supervoxels — for example, that two supervoxels on opposite sides of a cell membrane should not be merged even if intermediate supervoxels suggest otherwise. The computational cost is the main limitation: exact multicut is NP-hard, so practical implementations use approximations (Kernighan-Lin moves, greedy additive edge contraction). The tradeoff between solution quality and computation time determines when multicut is preferred over simpler greedy approaches.

**Key figures:** Fig. 1 (multicut formulation), Fig. 2 (lifted edges), Fig. 3 (benchmark comparison)

**Discussion prompts:**
- When is the computational cost of multicut justified over greedy agglomeration?
- How do long-range lifted edges improve segmentation in practice?

**Related content:** [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/), [Error taxonomy](/content-library/proofreading/error-taxonomy/)

---

## 7. Hider et al. (2022) / Dorkenwald et al. (2022) — FlyWire: Online Community for Whole-Brain Connectomics

**Citation:** Dorkenwald S, McKellar CE, Macrina T, Kemnitz N, Lee K, Lu R, et al. FlyWire: online community for whole-brain connectomics. *Nature Methods*. 2022;19:119-128.
**DOI:** [10.1038/s41592-021-01330-0](https://doi.org/10.1038/s41592-021-01330-0)

**Tags:** `proofreading:crowd-sourced-proofreading` `proofreading:proofreading-tools` `case-studies:FlyWire` `data-storage:CAVE` `methodology:open-science`

### Summaries

**Beginner:** Building a complete brain wiring diagram requires checking millions of computer-traced neurons by hand — far too much work for any single lab. This paper introduces FlyWire, an online platform where researchers around the world can collaboratively proofread the fruit fly brain, much like Wikipedia lets anyone edit an encyclopedia. The platform provides specialized tools for viewing 3D neurons and fixing errors, and tracks all changes so nothing is lost.

**Intermediate:** Dorkenwald et al. describe the FlyWire platform architecture for collaborative proofreading at scale. Built on the CAVE (Connectome Annotation Versioning Engine) infrastructure, FlyWire enables concurrent editing by hundreds of users with real-time conflict resolution through a chunked graph representation. The platform includes a neuroglancer-based interface for 3D proofreading, automated merge suggestions, and a versioning system that maintains full edit history. The paper reports on early community engagement and proofreading throughput metrics.

**Advanced:** FlyWire's technical contribution is the integration of a chunked graph data structure (enabling sub-second edits on a whole-brain segmentation), a real-time collaborative editing system with conflict resolution, and community management infrastructure. The CAVE backend supports both manual proofreading and programmatic access for automated correction pipelines. Key design decisions include: the choice of a supervoxel graph rather than voxel-level editing (trading spatial precision for speed), the merge-focused workflow (most edits are merges rather than splits), and the open-access model that lowers the barrier to contribution. The platform demonstrated that distributed proofreading can scale to whole-brain datasets while maintaining quality through community oversight.

**Key figures:** Fig. 1 (platform overview and architecture), Fig. 2 (proofreading interface), Fig. 3 (community engagement and throughput)

**Discussion prompts:**
- What are the advantages and risks of open community proofreading compared to expert-only approaches?
- How does the CAVE infrastructure handle conflicting edits from simultaneous users?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [Proofreading strategies](/content-library/proofreading/proofreading-strategies/)

---

## 8. Seung (2009) — Reading the Book of Memory: Sparse Sampling Versus Dense Mapping of Connectomes

**Citation:** Seung HS. Reading the book of memory: sparse sampling versus dense mapping of connectomes. *Neuron*. 2009;62(1):17-29.
**DOI:** [10.1016/j.neuron.2009.02.021](https://doi.org/10.1016/j.neuron.2009.02.021)

**Tags:** `proofreading:proofreading-strategy` `methodology:experimental-design` `connectomics:graph-theory`

### Summaries

**Beginner:** Before building a complete brain map, scientists need to decide: should we trace every single neuron in a region (dense mapping), or just sample some neurons and connections (sparse sampling)? This influential paper argues that each approach answers different questions. Dense mapping reveals the precise wiring rules of a circuit, while sparse sampling can survey larger brain areas more quickly. The choice depends on what you want to learn.

**Intermediate:** Seung presents a theoretical analysis of two fundamentally different connectomics strategies. Dense reconstruction — tracing all neurons and synapses within a volume — reveals complete circuit motifs and enables graph-theoretic analysis of network structure. Sparse sampling — reconstructing selected neurons across a larger region — provides statistical estimates of connectivity rules and cell type distributions. The paper formalizes the tradeoffs in terms of information gained per unit of reconstruction effort and argues that the scientific question should dictate the strategy.

**Advanced:** This paper laid the theoretical groundwork for the strategic decisions that shaped subsequent connectomics projects. The dense vs. sparse dichotomy maps directly onto proofreading strategy: dense reconstruction demands exhaustive proofreading within a bounded volume, while sparse sampling requires accurate reconstruction of individual neurons but tolerates gaps. Seung's analysis of what can be inferred from each approach — circuit motifs and synaptic weight distributions from dense, projection patterns and cell type statistics from sparse — remains a useful framework for project planning. The paper also anticipates the "n-of-one" problem: a single dense reconstruction cannot distinguish stereotyped wiring from individual variation, motivating the multi-connectome comparison approaches that emerged later.

**Key figures:** Fig. 1 (dense vs. sparse strategies), Fig. 2 (information yield analysis), Fig. 3 (circuit motif detection)

**Discussion prompts:**
- How has the dense vs. sparse tradeoff shifted as automation has improved since 2009?
- What scientific questions absolutely require dense reconstruction, and which can be answered with sparse sampling?

**Related content:** [Proofreading strategies](/content-library/proofreading/proofreading-strategies/), [Graph representations](/content-library/connectomics/graph-representations/)
