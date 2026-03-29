---
layout: page
title: "Journal Papers: MRI Connectomics"
permalink: /content-library/journal-papers/mri-connectomics/
description: "Curated papers on macro-scale brain connectivity from diffusion MRI and functional MRI, with summaries at beginner, intermediate, and advanced levels."
dimension: mri-connectomics
tags:
  - mri-connectomics:diffusion-MRI
  - mri-connectomics:tractography
  - mri-connectomics:structural-connectivity
  - mri-connectomics:functional-connectivity
  - mri-connectomics:Human-Connectome-Project
  - mri-connectomics:parcellation
---

# MRI Connectomics Journal Papers

Curated papers on macro-scale brain connectivity mapping using diffusion MRI tractography and functional MRI. Each paper includes summaries at three expertise levels. These complement the EM-scale papers elsewhere in this collection.

---

## 1. Sporns, Tononi & Kötter (2005) — The Human Connectome: A Structural Description of the Human Brain

**Citation:** Sporns O, Tononi G, Kötter R. The human connectome: A structural description of the human brain. *PLoS Computational Biology*. 2005;1(4):e42.
**DOI:** [10.1371/journal.pcbi.0010042](https://doi.org/10.1371/journal.pcbi.0010042)

**Tags:** `mri-connectomics:structural-connectivity` `mri-connectomics:parcellation` `methodology:experimental-design` `connectomics:graph-theory`

### Summaries

**Beginner:** This is the paper that coined the word "connectome" — a complete map of all the connections in a brain. The authors argued that just as the Human Genome Project mapped all our genes, neuroscience needs a systematic effort to map all the brain's wiring. They proposed using non-invasive brain imaging (MRI) to build region-to-region connection maps of the human brain.

**Intermediate:** Sporns et al. introduced the term "connectome" and outlined a research program for mapping structural connectivity in the human brain at the macro scale. They proposed combining diffusion MRI tractography (for white matter pathways) with cortical parcellation (dividing the cortex into regions) to produce a network representation of brain organization. The paper discusses how graph-theoretic analysis of such networks could reveal organizational principles including modularity, small-world architecture, and hub structure.

**Advanced:** This foundational paper established the conceptual framework for macro-scale connectomics, distinct from but complementary to the micro-scale EM connectomics pursued by White et al. and subsequent projects. Key contributions: (1) formal definition of the connectome as a comprehensive structural description at a given scale; (2) the argument that network analysis requires complete (or near-complete) connectivity data rather than pairwise studies; (3) the recognition that connectomes exist at multiple scales (macro/meso/micro) with different methods appropriate at each. The paper's vision directly motivated the Human Connectome Project.

**Key figures:** Fig. 1 (connectome concept), Fig. 2 (parcellation and connectivity matrix)

**Discussion prompts:**
- How does the macro-scale "connectome" from MRI relate to the micro-scale connectome from EM?
- What information is lost when representing connectivity at the region level rather than the neuron level?

**Related content:** [Connectome history](/content-library/connectomics/connectome-history/), [Graph representations](/content-library/connectomics/graph-representations/)

---

## 2. Van Essen et al. (2013) — The WU-Minn Human Connectome Project

**Citation:** Van Essen DC, Smith SM, Barch DM, Behrens TEJ, Yacoub E, Ugurbil K. The WU-Minn Human Connectome Project: an overview. *NeuroImage*. 2013;80:62-79.
**DOI:** [10.1016/j.neuroimage.2013.05.041](https://doi.org/10.1016/j.neuroimage.2013.05.041)

**Tags:** `mri-connectomics:Human-Connectome-Project` `mri-connectomics:diffusion-MRI` `mri-connectomics:functional-connectivity` `mri-connectomics:multi-modal` `methodology:open-science`

### Summaries

**Beginner:** The Human Connectome Project (HCP) is a massive effort to map the brain's wiring in 1,200 healthy adults using advanced brain scanning. This paper describes the project's design: each participant undergoes multiple types of brain scans plus behavioral testing, and all the data is shared freely with researchers worldwide. HCP produced the highest-quality brain connectivity data ever collected and has become the reference dataset for human brain network research.

**Intermediate:** Van Essen et al. describe the design and implementation of the WU-Minn Human Connectome Project, which acquired high-resolution structural MRI, diffusion MRI (for tractography), resting-state fMRI, task fMRI, and MEG/EEG from 1,200 healthy young adults, alongside extensive behavioral and genetic data. Key technical innovations include customized MRI hardware (stronger gradients for better diffusion imaging), optimized acquisition protocols, and a comprehensive preprocessing pipeline (including surface-based analysis with FreeSurfer and the HCP Workbench). All data is publicly released through the ConnectomeDB platform.

**Advanced:** The HCP established the technical and data-sharing standards for population-scale connectomics. Key methodological contributions: (1) the multi-modal parcellation approach combining architecture, function, connectivity, and topography; (2) the demonstration that higher b-value, multi-shell diffusion acquisitions substantially improve tractography accuracy; (3) the surface-based analysis framework (CIFTI format) that enables better spatial correspondence across subjects than volume-based approaches. The HCP's open-data model accelerated the field enormously. For EM connectomics, HCP provides the macro-scale context — region-level connectivity patterns that constrain interpretation of micro-scale circuits.

**Key figures:** Fig. 1 (HCP overview), Fig. 3 (diffusion imaging quality), Fig. 5 (functional connectivity matrices)

**Discussion prompts:**
- How can HCP macro-scale connectivity data constrain or validate findings from EM micro-scale connectomics?
- What are the fundamental resolution limits of diffusion MRI tractography compared to EM?

**Related content:** [Connectome history](/content-library/connectomics/connectome-history/), [Network analysis methods](/content-library/connectomics/network-analysis-methods/)

---

## 3. Maier-Hein et al. (2017) — The Challenge of Mapping the Human Connectome Based on Diffusion Tractography

**Citation:** Maier-Hein KH, Neher PF, Houde JC, Côté MA, Garyfallidis E, Zhong J, et al. The challenge of mapping the human connectome based on diffusion tractography. *Nature Communications*. 2017;8:1349.
**DOI:** [10.1038/s41467-017-01285-x](https://doi.org/10.1038/s41467-017-01285-x)

**Tags:** `mri-connectomics:tractography` `mri-connectomics:diffusion-MRI` `mri-connectomics:structural-connectivity` `methodology:benchmark` `methodology:ground-truth`

### Summaries

**Beginner:** Can we trust the brain wiring maps made from MRI scans? This study created a realistic digital brain phantom (a computer simulation of brain tissue) and challenged 96 different tractography methods to reconstruct known fiber pathways. The sobering result: all methods produced many false connections — pathways that don't actually exist. This paper is a critical reality check on the accuracy of MRI-based brain connectivity maps.

**Intermediate:** Maier-Hein et al. organized the ISMRM Tractography Challenge using a physical phantom with known ground-truth fiber configurations. 96 tractography pipelines from 20 research groups were evaluated on their ability to reconstruct valid bundles while avoiding invalid ones. Key finding: all methods exhibited high false-positive rates — the more sensitive a method was to detecting true bundles, the more false bundles it also produced. No method achieved both high sensitivity and high specificity. The paper identifies crossing fibers, fanning fibers, and sharp turns as the most problematic configurations.

**Advanced:** This paper fundamentally changed how the field interprets tractography-derived connectomes. The false-positive problem — where tractography creates plausible but non-existent connections — means that MRI-derived connectivity matrices contain systematic errors that are difficult to distinguish from true connectivity. This is qualitatively different from EM connectomics, where false positives arise from segmentation merge errors (detectable and correctable) rather than fundamental methodological limitations. The paper motivated development of filtering methods (SIFT, COMMIT, LiFE) that use the diffusion signal to weight or prune streamlines. For cross-scale integration, the implication is that MRI tractography provides connectivity hypotheses rather than ground truth, while EM provides ground truth within a limited volume.

**Key figures:** Fig. 1 (phantom design), Fig. 2 (tractography results), Fig. 3 (sensitivity vs. specificity), Fig. 4 (error analysis by configuration)

**Discussion prompts:**
- How should MRI tractography results be interpreted given the false-positive problem?
- What role can EM connectomics play in validating or calibrating tractography methods?
- How do the error modes of tractography compare with segmentation errors in EM connectomics?

**Related content:** [Connectome history](/content-library/connectomics/connectome-history/), [Graph representations](/content-library/connectomics/graph-representations/)

---

## 4. Sotiropoulos & Zalesky (2019) — Building Connectomes Using Diffusion MRI

**Citation:** Sotiropoulos SN, Zalesky A. Building connectomes using diffusion MRI: why, how and but. *NMR in Biomedicine*. 2019;32(4):e3752.
**DOI:** [10.1002/nbm.3752](https://doi.org/10.1002/nbm.3752)

**Tags:** `mri-connectomics:diffusion-MRI` `mri-connectomics:tractography` `mri-connectomics:structural-connectivity` `mri-connectomics:parcellation` `methodology:experimental-design`

### Summaries

**Beginner:** This review is a practical guide to building brain connectivity maps from diffusion MRI scans. It walks through the entire process: how to divide the brain into regions (parcellation), how to trace fiber pathways between regions (tractography), and how to turn the results into a network that can be analyzed. Importantly, it also explains the many pitfalls and choices that can dramatically change the results.

**Intermediate:** Sotiropoulos and Zalesky provide a comprehensive methodological review of diffusion MRI connectome construction. They systematically cover each pipeline step — parcellation scheme selection, diffusion model fitting (DTI, CSD, multi-shell), tractography algorithm choice (deterministic vs. probabilistic), streamline filtering, and connectivity matrix construction (binary vs. weighted, thresholding strategies). For each step, they describe the methodological options, their impact on downstream results, and current best practices. The "but" section addresses known limitations including the false-positive problem, resolution limits, and test-retest reliability.

**Advanced:** This review is the most complete methodological reference for MRI connectome construction pipelines. Key points for cross-scale integration: (1) parcellation granularity determines the "node" definition — coarser parcellations are more reliable but lose spatial detail; (2) streamline count is a poor proxy for connection strength, motivating microstructure-informed weighting; (3) group-level connectome construction requires careful handling of inter-subject variability in both parcellation alignment and tractography output. The discussion of how each methodological choice propagates into network-level statistics is directly relevant to interpreting any MRI connectomics result.

**Key figures:** Fig. 1 (connectome construction pipeline), Fig. 2 (parcellation comparison), Fig. 4 (tractography method comparison), Fig. 6 (reliability analysis)

**Discussion prompts:**
- Which pipeline choices have the largest impact on the resulting connectome, and which are relatively inconsequential?
- How should parcellation granularity be chosen for different scientific questions?

**Related content:** [Graph representations](/content-library/connectomics/graph-representations/), [Network analysis methods](/content-library/connectomics/network-analysis-methods/)
