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
use_layout_hero: false
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
---

## 5. Hagmann et al. (2008) — Mapping the Structural Core of Human Cerebral Cortex

**Citation:** Hagmann P, Cammoun L, Gigandet X, Meuli R, Honey CJ, Wedeen VJ, Sporns O. Mapping the structural core of human cerebral cortex. *PLoS Biology*. 2008;6(7):e159.
**DOI:** [10.1371/journal.pbio.0060159](https://doi.org/10.1371/journal.pbio.0060159)

**Tags:** `mri-connectomics:diffusion-MRI` `mri-connectomics:structural-connectivity` `mri-connectomics:parcellation` `network-analysis:hub` `network-analysis:rich-club`

### Summaries

**Beginner:** This study built whole-brain wiring maps from MRI scans of living people and found that some regions act as hubs — heavily connected crossroads that most paths run through. Those hubs cluster in the middle of the brain, in a set of regions the authors called the structural core.

**Intermediate:** Using diffusion spectrum imaging in a small cohort, Hagmann et al. constructed structural connectivity matrices at several parcellation resolutions and applied graph measures — degree, centrality, efficiency, modularity — to identify a densely interconnected posterior medial and parietal core. They also showed the structural network's community structure corresponded partly to resting-state functional networks measured in the same participants.

**Advanced:** This is the paper that put hubs and cores on the agenda for human connectomics, and it is worth reading together with paper 3 on this page rather than alone. Its conclusions rest on tractography, so the hub locations inherit tractography's known biases — notably that gyral crowns and long association pathways are reconstructed with systematically different reliability, which can concentrate apparent centrality in regions that are simply easier to track into. The structure-function correspondence it reports is real but partial, and the causal direction is not established by the data. Treat it as the origin of a hypothesis that later work, including the rich-club literature, refined rather than as a settled description.

**Key figures:** Connectivity matrices at multiple scales; centrality maps identifying the structural core; structural-functional correspondence.

**Discussion prompts:**
- How much of the identified "core" could be explained by regional differences in tractography reliability rather than by connectivity?
- What would an EM-scale measurement have to look like to test a hub claim made at this scale?

**Related content:** [Network analysis methods](/content-library/connectomics/network-analysis-methods/), [Connectome history](/content-library/connectomics/connectome-history/)

---

## 6. Bullmore & Sporns (2009) — Complex Brain Networks

**Citation:** Bullmore E, Sporns O. Complex brain networks: graph theoretical analysis of structural and functional systems. *Nature Reviews Neuroscience*. 2009;10:186-198.
**DOI:** [10.1038/nrn2575](https://doi.org/10.1038/nrn2575)

**Tags:** `network-analysis:small-world` `network-analysis:modularity` `network-analysis:centrality` `mri-connectomics:functional-connectivity` `connectomics:graph-theory`

### Summaries

**Beginner:** The review that taught neuroscience to think about the brain as a network. It explains what graph measures mean — how clustered a network is, how short its paths are, which nodes are hubs — and why those descriptions might matter for brain function and disease.

**Intermediate:** Bullmore and Sporns survey graph-theoretic analysis of structural and functional brain networks: construction choices, the standard measure set, small-world and modular organization, hubs, and applications to clinical populations. It is the conceptual bridge between network science and neuroimaging.

**Advanced:** Enormously influential and worth reading critically. Two cautions have aged into the literature since. First, small-worldness has been shown to be a weakly discriminating statistic — a great many networks satisfy it, so reporting it distinguishes little. Second, nearly every measure here is sensitive to network density and to the thresholding applied when building the graph, which means group comparisons can reflect density differences rather than topology. The companion methods paper (Rubinov & Sporns 2010, listed under [network analysis](/content-library/journal-papers/network-analysis/)) is explicit about these sensitivities; read the two together. For a nanoscale reader, the transferable point is that whole-graph summary statistics are a poor match for local microcircuit hypotheses at any scale.

**Key figures:** Graph construction schematic; measure definitions; small-world and modular organization; clinical applications.

**Discussion prompts:**
- Which measures in this review would you trust on a partially proofread EM connectome, and which would you not?
- What does a "small-world" finding actually rule out?

**Related content:** [Network analysis methods](/content-library/connectomics/network-analysis-methods/), [Network analysis papers](/content-library/journal-papers/network-analysis/)

---

## 7. Yendiki et al. (2011) — TRACULA

**Citation:** Yendiki A, Panneck P, Srinivasan P, Stevens A, Zöllei L, Augustinack J, et al. Automated probabilistic reconstruction of white-matter pathways in health and disease using an atlas of the underlying anatomy. *Frontiers in Neuroinformatics*. 2011;5:23.
**DOI:** [10.3389/fninf.2011.00023](https://doi.org/10.3389/fninf.2011.00023)

**Tags:** `mri-connectomics:tractography` `mri-connectomics:diffusion-MRI` `methodology:reproducibility` `methodology:inter-lab-comparison`

### Summaries

**Beginner:** Tracing the same white-matter bundle consistently across many people and many scans is harder than it sounds. This work built an automated method that uses prior anatomical knowledge to find the same pathway in each brain, so that results can be compared across subjects and studies.

**Intermediate:** TRACULA performs global probabilistic tractography constrained by an atlas of the anatomical neighbourhood each pathway passes through. Because the priors describe surroundings rather than exact coordinates, the method tolerates individual variation and pathology while still producing consistent, automatically labelled bundles — removing the manual ROI placement that had made cross-study comparison unreliable.

**Advanced:** The methodological contribution most relevant to this curriculum is reproducibility rather than accuracy. Manual ROI-based tractography embeds operator judgement in every result, which is the macroscale analogue of unreported annotation protocol at the EM scale, and it produces the same problem: differences between studies confounded with differences in who did the tracing. Automating the constraint makes the protocol explicit and shareable. The residual limitation is inherited, not solved — atlas priors cannot rescue a pathway the diffusion model cannot resolve, so the false-positive concerns of paper 3 still apply.

**Key figures:** Anatomical priors; pathway reconstructions across subjects; reproducibility across scan sessions.

**Discussion prompts:**
- How does encoding a protocol in software change what a cross-study comparison means?
- What is the EM-scale equivalent of "manual ROI placement", and how is it addressed?

**Related content:** [Provenance and versioning](/content-library/infrastructure/provenance-and-versioning/), [Metrics and QA](/content-library/proofreading/metrics-and-qa/)

---

## 8. Thomas et al. (2014) — Anatomical Accuracy of Tractography Is Inherently Limited

**Citation:** Thomas C, Ye FQ, Irfanoglu MO, Modi P, Saleem KS, Leopold DA, Pierpaoli C. Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. *Proceedings of the National Academy of Sciences*. 2014;111(46):16574-16579.
**DOI:** [10.1073/pnas.1405672111](https://doi.org/10.1073/pnas.1405672111)

**Tags:** `mri-connectomics:tractography` `methodology:ground-truth` `methodology:benchmark` `mri-connectomics:structural-connectivity`

### Summaries

**Beginner:** Researchers scanned monkey brains at very high quality and compared the pathways MRI predicted against pathways established by injecting tracers into the same species — a far more reliable method. Many MRI-predicted connections were not real, and some real ones were missed, and pushing scan quality higher did not fix it.

**Intermediate:** Using high-quality ex vivo macaque diffusion data with tract-tracing as reference, the authors show a persistent sensitivity-specificity trade-off: parameter settings that recover more true pathways also generate more false ones. Critically, the trade-off did not disappear with better data, implicating the inference problem itself rather than acquisition quality.

**Advanced:** Read alongside paper 3. Together they make the strongest available case that tractography's false-positive problem is structural rather than technical: the diffusion signal in a voxel constrains local orientation but does not identify which incoming pathway continues into which outgoing one, so long-range trajectories are inferred rather than observed. The consequence for anyone comparing scales is that a tractography "connection" and an EM synapse are not the same kind of claim, and a disagreement between them is often not a contradiction — see [Unit 02](/technical-training/02-brain-data-across-scales/), which works this exact case.

**Key figures:** Tractography versus tracer-derived connectivity; sensitivity-specificity trade-off curves; error analysis by pathway.

**Discussion prompts:**
- Why does improving acquisition quality not resolve the false-positive problem?
- If tractography yields hypotheses rather than observations, how should a paper word its connectivity claims?

**Related content:** [Unit 02: Brain Data Across Scales](/technical-training/02-brain-data-across-scales/), [Connectome history](/content-library/connectomics/connectome-history/)

---

## 9. Glasser et al. (2016) — A Multi-Modal Parcellation of Human Cerebral Cortex

**Citation:** Glasser MF, Coalson TS, Robinson EC, Hacker CD, Harwell J, Yacoub E, et al. A multi-modal parcellation of human cerebral cortex. *Nature*. 2016;536:171-178.
**DOI:** [10.1038/nature18933](https://doi.org/10.1038/nature18933)

**Tags:** `mri-connectomics:parcellation` `mri-connectomics:Human-Connectome-Project` `mri-connectomics:functional-connectivity` `cell-types:cell-census`

### Summaries

**Beginner:** Before you can say which brain regions connect, you have to agree on what the regions are. This work combined several different kinds of MRI measurement to divide the cortex into 180 areas per hemisphere, using boundaries where multiple measurements changed at once.

**Intermediate:** Using Human Connectome Project data, the authors delineated 180 areas per hemisphere from concordant gradients in cortical thickness, myelin content, task activation, and functional connectivity, then trained a classifier to identify those areas in new individuals. The multi-modal criterion is the methodological core: a boundary is accepted where independent measures agree.

**Advanced:** Parcellation is the node-definition step, and node definition determines every connectivity result computed afterwards — the direct macroscale analogue of "what is a node?" in [Unit 09 §1](/technical-training/09-connectome-analysis-neuroai/). Two things to hold onto. The multi-modal concordance criterion is a strong methodological idea and generalizes: a boundary supported by independent measurement types is more trustworthy than one supported by a single measure, which is the same cue-independence logic annotators use at the EM scale. But the resulting atlas is a model with uncertainty, not a ground-truth map, and areas whose boundaries were weakly supported carry that uncertainty into every downstream connectivity matrix that uses them.

**Key figures:** Multi-modal gradient maps; the 180-area parcellation; classifier performance on new subjects.

**Discussion prompts:**
- How does the choice of parcellation change a connectivity result, and how would you test that sensitivity?
- Where does the multi-modal concordance idea appear in EM-scale cell typing?

**Related content:** [Unit 09: Connectome Analysis](/technical-training/09-connectome-analysis-neuroai/), [Cell types papers](/content-library/journal-papers/cell-types/)

---

## 10. Schilling et al. (2019) — Limits to Anatomical Accuracy Using Modern Approaches

**Citation:** Schilling KG, Nath V, Hansen C, Parvathaneni P, Blaber J, Gao Y, et al. Limits to anatomical accuracy of diffusion tractography using modern approaches. *NeuroImage*. 2019;185:1-11.
**DOI:** [10.1016/j.neuroimage.2018.10.029](https://doi.org/10.1016/j.neuroimage.2018.10.029)

**Tags:** `mri-connectomics:tractography` `methodology:ground-truth` `methodology:benchmark` `methodology:inter-lab-comparison`

### Summaries

**Beginner:** A follow-up check on whether newer, more sophisticated tractography methods had fixed the accuracy problem. They had improved in places, but the core limitation remained.

**Intermediate:** Benchmarking contemporary tractography approaches against tracer-derived ground truth, the authors find that advances in modelling and algorithms improved some measures without eliminating the false-positive burden, and that method choice remains a substantial source of variance in derived connectivity.

**Advanced:** The value of this paper is as evidence about a trajectory rather than about a single method: across a decade of methodological progress, the sensitivity-specificity trade-off narrowed but did not close. That pattern is itself informative — it points at the inference problem rather than at any implementation, and it argues for reporting connectivity claims with method and parameters attached, since method choice contributes variance comparable to the biological effects often under study. The parallel at the EM scale is real but the situations differ in one important way: EM merge and split errors are in principle detectable and correctable by inspecting the voxels, whereas a tractography false positive has no underlying observation to return to.

**Key figures:** Method comparison against tracer ground truth; accuracy trends across approaches; variance attributable to method choice.

**Discussion prompts:**
- What does a decade of narrowing-but-not-closing error tell you about where the limitation lies?
- How should a connectivity paper report method dependence so a reader can judge it?

**Related content:** [Unit 02: Brain Data Across Scales](/technical-training/02-brain-data-across-scales/), [Metrics and QA](/content-library/proofreading/metrics-and-qa/)

---

## Reading this page alongside the EM material

Papers 3, 8, and 10 form one argument, and it is the argument a nanoscale reader most
needs from this page: tractography infers long-range trajectories from local orientation
measurements, so a tractography "connection" is a model output, not an observation. That
is not a criticism of the method — it is the only method that measures whole living human
brains — but it means macroscale and nanoscale connectivity claims are different kinds of
statement and cannot be compared without saying so. [Unit 02]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }})
works a case where an EM study and a tractography study disagree and both are correct.

Papers 5, 6, and 9 supply the other half: the measures, the node definitions, and the
hub-and-module vocabulary that macroscale network neuroscience contributed, much of which
transfers to EM graphs with the density and thresholding caveats noted above.
