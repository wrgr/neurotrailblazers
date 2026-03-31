# Duplicate Review Report

Multi-signal duplicate detection using five independent signals:
title similarity, DOI pattern, citation neighborhood Jaccard,
author overlap, and mutual non-citation.

**Decision column**: mark each pair as `merge`, `keep_both`, or `investigate`.

## Summary

| Category | Count | Action |
| --- | --- | --- |
| AUTO_MERGE (conf ≥ 0.70) | 296 | Merge unless flagged |
| LIKELY_DUP (conf ≥ 0.50) | 443 | Review, likely merge |
| REVIEW (conf ≥ 0.40) | 243 | Human judgment needed |
| LOW (conf ≥ 0.30) | 443 | Probably not duplicates |

Both versions in top 500 (wasting slots): **27**
Would enter top 500 if merged: **20**

## Signal Weights

| Signal | Weight | What it catches |
| --- | --- | --- |
| Title similarity | 0.35 | Same or near-same titles |
| Citation neighborhood | 0.25 | Shared references + citers (catches title changes) |
| Author overlap | 0.15 | Same first/last author |
| Mutual non-citation | 0.15 | True dupes don't cite each other |
| Preprint DOI pattern | 0.10 | bioRxiv/arXiv DOI prefix |

## Confidence Interpretation

- **≥ 0.90**: Near-certain duplicate (high title + citations + author + preprint)
- **0.70–0.89**: Very likely duplicate, auto-merge unless flagged
- **0.50–0.69**: Likely duplicate, needs quick human check
- **0.40–0.49**: Possible duplicate, needs investigation
- **0.30–0.39**: Unlikely duplicate, included for completeness

## AUTO_MERGE (296 pairs)

**1.** conf=0.884 title=1.00 cit=0.93 auth=1.0 `diff_DOIs` **⚠ BOTH IN TOP 500**
- A #244: [2002] Improved Optimization for the Robust and Accurate Linear Registration and Motion Correctio  (10589 cites)
- B #263: [2002] Improved Optimization for the Robust and Accurate Linear Registration and Motion Correctio  (9496 cites)
- Decision: ___________

**2.** conf=0.883 title=1.00 cit=0.53 auth=1.0 `A=preprint` (one in top 500)
- A #1458: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (5 cites)
- B #389: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (15 cites)
- Decision: ___________

**3.** conf=0.878 title=1.00 cit=0.51 auth=1.0 `A=preprint`
- A #1517: [2022] Multi-Layered Maps of Neuropil with Segmentation-Guided Contrastive Learning  (16 cites)
- B #562: [2023] Multi-layered maps of neuropil with segmentation-guided contrastive learning  (27 cites)
- Decision: ___________

**4.** conf=0.878 title=1.00 cit=0.51 auth=1.0 `A=preprint` (one in top 500)
- A #868: [2019] Binary and analog variation of synapses between cortical pyramidal neurons  (64 cites)
- B #39: [2022] Binary and analog variation of synapses between cortical pyramidal neurons  (100 cites)
- Decision: ___________

**5.** conf=0.877 title=0.99 cit=0.52 auth=1.0 `A=preprint` (one in top 500)
- A #1420: [2020] Input connectivity reveals additional heterogeneity of dopaminergic reinforcement in <i>Dr  (5 cites)
- B #405: [2020] Input Connectivity Reveals Additional Heterogeneity of Dopaminergic Reinforcement in Droso  (86 cites)
- Decision: ___________

**6.** conf=0.873 title=1.00 cit=0.49 auth=1.0 `A=preprint` (one in top 500)
- A #1257: [2020] Molecular resolution imaging by post-labeling expansion single-molecule localization micro  (24 cites)
- B #379: [2020] Molecular resolution imaging by post-labeling expansion single-molecule localization micro  (175 cites)
- Decision: ___________

**7.** conf=0.872 title=1.00 cit=0.49 auth=1.0 `A=preprint`
- A #1640: [2022] Petascale pipeline for precise alignment of images from serial section electron microscopy  (13 cites)
- B #1350: [2024] Petascale pipeline for precise alignment of images from serial section electron microscopy  (32 cites)
- Decision: ___________

**8.** conf=0.869 title=1.00 cit=0.48 auth=1.0 `A=preprint` (one in top 500)
- A #1421: [2018] A genetic, genomic, and computational resource for exploring neural circuit function  (43 cites)
- B #2: [2020] A genetic, genomic, and computational resource for exploring neural circuit function  (287 cites)
- Decision: ___________

**9.** conf=0.866 title=0.99 cit=0.48 auth=1.0 `A=preprint`
- A #1137: [2023] Transforming descending input into motor output: An analysis of the <i>Drosophila</i> Male  (38 cites)
- B #1813: [2024] Transforming descending input into motor output: An analysis of the Drosophila Male Adult   (20 cites)
- Decision: ___________

**10.** conf=0.866 title=1.00 cit=0.46 auth=1.0 `A=preprint` (one in top 500)
- A #1036: [2020] Information flow, cell types and stereotypy in a full olfactory connectome  (19 cites)
- B #82: [2021] Information flow, cell types and stereotypy in a full olfactory connectome  (182 cites)
- Decision: ___________

**11.** conf=0.865 title=0.99 cit=0.47 auth=1.0 `A=preprint`
- A #1885: [2023] Somatotopic organization among parallel sensory pathways that promote a grooming sequence   (4 cites)
- B #1367: [2023] Somatotopic organization among parallel sensory pathways that promote a grooming sequence   (23 cites)
- Decision: ___________

**12.** conf=0.864 title=0.99 cit=0.47 auth=1.0 `A=preprint`
- A #1109: [2023] Systematic annotation of a complete adult male <i>Drosophila</i> nerve cord connectome rev  (35 cites)
- B #1249: [2024] Systematic annotation of a complete adult male Drosophila nerve cord connectome reveals pr  (39 cites)
- Decision: ___________

**13.** conf=0.859 title=0.99 cit=0.45 auth=1.0 `A=preprint` **⚠ BOTH IN TOP 500**
- A #223: [2020] A searchable image resource of <i>Drosophila</i> GAL4-driver expression patterns with sing  (24 cites)
- B #274: [2023] A searchable image resource of Drosophila GAL4 driver expression patterns with single neur  (126 cites)
- Decision: ___________

**14.** conf=0.858 title=1.00 cit=0.83 auth=1.0 `diff_DOIs`
- A #913: [2016] 2016 ESC Guidelines for the management of atrial fibrillation developed in collaboration w  (6474 cites)
- B #885: [2016] 2016 ESC Guidelines for the management of atrial fibrillation developed in collaboration w  (6411 cites)
- Decision: ___________

**15.** conf=0.856 title=0.99 cit=0.44 auth=1.0 `A=preprint` **⚠ BOTH IN TOP 500**
- A #503: [2020] A connectome of the <i>Drosophila</i> central complex reveals network motifs suitable for   (52 cites)
- B #89: [2021] A connectome of the Drosophila central complex reveals network motifs suitable for flexibl  (386 cites)
- Decision: ___________

**16.** conf=0.854 title=1.00 cit=0.42 auth=1.0 `A=preprint` (one in top 500)
- A #1514: [2022] NeuronBridge: an intuitive web application for neuronal morphology search across large dat  (24 cites)
- B #335: [2024] NeuronBridge: an intuitive web application for neuronal morphology search across large dat  (65 cites)
- Decision: ___________

**17.** conf=0.854 title=1.00 cit=0.41 auth=1.0 `A=preprint` **⚠ BOTH IN TOP 500**
- A #131: [2020] Complete connectomic reconstruction of olfactory projection neurons in the fly brain  (33 cites)
- B #30: [2020] Complete Connectomic Reconstruction of Olfactory Projection Neurons in the Fly Brain  (201 cites)
- Decision: ___________

**18.** conf=0.853 title=0.99 cit=0.43 auth=1.0 `A=preprint` (one in top 500)
- A #1356: [2020] Connectomics analysis reveals first, second, and third order thermosensory and hygrosensor  (8 cites)
- B #103: [2020] Connectomics Analysis Reveals First-, Second-, and Third-Order Thermosensory and Hygrosens  (119 cites)
- Decision: ___________

**19.** conf=0.853 title=1.00 cit=0.81 auth=1.0 `diff_DOIs` **⚠ BOTH IN TOP 500**
- A #401: [2021] Circuits for integrating learned and innate valences in the insect brain  (62 cites)
- B #449: [2020] Circuits for integrating learned and innate valences in the insect brain.  (50 cites)
- Decision: ___________

**20.** conf=0.850 title=1.00 cit=0.40 auth=1.0 `A=preprint` (one in top 500)
- A #1691: [2023] Neuronal “parts list” and wiring diagram for a visual system  (23 cites)
- B #464: [2024] Neuronal parts list and wiring diagram for a visual system  (68 cites)
- Decision: ___________

**21.** conf=0.848 title=0.89 cit=0.55 auth=1.0 `A=preprint`
- A #1340: [2020] Citizen science, cells and CNNs – deep learning for automatic segmentation of the nuclear   (14 cites)
- B #1037: [2021] Deep learning for automatic segmentation of the nuclear envelope in electron microscopy da  (52 cites)
- Decision: ___________

**22.** conf=0.848 title=1.00 cit=0.39 auth=1.0 `A=preprint` **⚠ BOTH IN TOP 500**
- A #445: [2020] Whole-body integration of gene expression and single-cell morphology  (28 cites)
- B #340: [2021] Whole-body integration of gene expression and single-cell morphology  (147 cites)
- Decision: ___________

**23.** conf=0.848 title=1.00 cit=0.39 auth=1.0 `A=preprint` (one in top 500)
- A #617: [2020] The wiring logic of an identified serotonergic neuron that spans sensory networks  (3 cites)
- B #426: [2020] The Wiring Logic of an Identified Serotonergic Neuron That Spans Sensory Networks  (41 cites)
- Decision: ___________

**24.** conf=0.845 title=1.00 cit=0.38 auth=1.0 `A=preprint` **⚠ BOTH IN TOP 500**
- A #112: [2020] Connectomes across development reveal principles of brain maturation  (59 cites)
- B #3: [2021] Connectomes across development reveal principles of brain maturation  (429 cites)
- Decision: ___________

**25.** conf=0.843 title=1.00 cit=0.37 auth=1.0 `A=preprint`
- A #1665: [2022] RoboEM: automated 3D flight tracing for synaptic-resolution connectomics  (7 cites)
- B #1290: [2024] RoboEM: automated 3D flight tracing for synaptic-resolution connectomics  (27 cites)
- Decision: ___________

**26.** conf=0.841 title=1.00 cit=0.36 auth=1.0 `A=preprint`
- A #931: [2024] Connectome-driven neural inventory of a complete visual system  (36 cites)
- B #1013: [2025] Connectome-driven neural inventory of a complete visual system  (46 cites)
- Decision: ___________

**27.** conf=0.837 title=1.00 cit=0.35 auth=1.0 `A=preprint`
- A #1276: [2020] Transforming representations of movement from body- to world-centric space  (22 cites)
- B #762: [2021] Transforming representations of movement from body- to world-centric space  (148 cites)
- Decision: ___________

**28.** conf=0.832 title=1.00 cit=0.33 auth=1.0 `A=preprint` **⚠ BOTH IN TOP 500**
- A #124: [2020] FlyWire: Online community for whole-brain connectomics  (70 cites)
- B #67: [2021] FlyWire: online community for whole-brain connectomics  (284 cites)
- Decision: ___________

**29.** conf=0.831 title=1.00 cit=0.32 auth=1.0 `A=preprint` (one in top 500)
- A #177: [2023] CAVE: Connectome Annotation Versioning Engine  (35 cites)
- B #720: [2025] CAVE: Connectome Annotation Versioning Engine  (32 cites)
- Decision: ___________

**30.** conf=0.830 title=0.96 cit=0.38 auth=1.0 `A=preprint`
- A #1848: [2022] The neuropeptidergic connectome of <i>C. elegans</i>  (18 cites)
- B #523: [2023] The neuropeptidergic connectome of C. elegans  (160 cites)
- Decision: ___________

**31.** conf=0.829 title=0.98 cit=0.34 auth=1.0 `B=preprint` **⚠ BOTH IN TOP 500**
- A #1: [2020] A connectome and analysis of the adult Drosophila central brain  (1198 cites)
- B #185: [2020] A Connectome and Analysis of the Adult <i>Drosophila</i> Central Brain  (35 cites)
- Decision: ___________

**32.** conf=0.829 title=0.98 cit=0.34 auth=1.0 `A=preprint`
- A #1960: [2023] Fine-grained descending control of steering in walking <i>Drosophila</i>  (17 cites)
- B #1702: [2024] Fine-grained descending control of steering in walking Drosophila  (40 cites)
- Decision: ___________

**33.** conf=0.828 title=0.91 cit=0.43 auth=1.0 `A=preprint` (one in top 500)
- A #634: [2020] Circuits for integrating learnt and innate valences in the fly brain  (18 cites)
- B #449: [2020] Circuits for integrating learned and innate valences in the insect brain.  (50 cites)
- Decision: ___________

**34.** conf=0.826 title=0.91 cit=0.43 auth=1.0 `A=preprint` (one in top 500)
- A #634: [2020] Circuits for integrating learnt and innate valences in the fly brain  (18 cites)
- B #401: [2021] Circuits for integrating learned and innate valences in the insect brain  (62 cites)
- Decision: ___________

**35.** conf=0.824 title=1.00 cit=0.30 auth=1.0 `A=preprint`
- A #847: [2021] Local Shape Descriptors for Neuron Segmentation  (17 cites)
- B #701: [2022] Local shape descriptors for neuron segmentation  (51 cites)
- Decision: ___________

**36.** conf=0.823 title=0.95 cit=0.37 auth=1.0 `A=preprint`
- A #956: [2021] Oligodendrocyte precursor cells prune axons in the mouse neocortex  (19 cites)
- B #743: [2022] Oligodendrocyte precursor cells ingest axons in the mouse neocortex  (135 cites)
- Decision: ___________

**37.** conf=0.823 title=0.98 cit=0.32 auth=1.0 `A=preprint`
- A #1144: [2023] A Connectome of the Male <i>Drosophila</i> Ventral Nerve Cord  (58 cites)
- B #1040: [2024] A Connectome of the Male Drosophila Ventral Nerve Cord  (53 cites)
- Decision: ___________

**38.** conf=0.822 title=0.98 cit=0.31 auth=1.0 `A=preprint`
- A #521: [2023] Synaptic connectome of the <i>Drosophila</i> circadian clock  (23 cites)
- B #1576: [2024] Synaptic connectome of the Drosophila circadian clock  (69 cites)
- Decision: ___________

**39.** conf=0.821 title=0.99 cit=0.30 auth=1.0 `A=preprint`
- A #1952: [2023] Synaptic architecture of leg and wing premotor control networks in <i>Drosophila</i>  (18 cites)
- B #1150: [2024] Synaptic architecture of leg and wing premotor control networks in Drosophila  (65 cites)
- Decision: ___________

**40.** conf=0.819 title=1.00 cit=0.28 auth=1.0 `A=preprint` **⚠ BOTH IN TOP 500**
- A #123: [2023] Neuronal wiring diagram of an adult brain  (165 cites)
- B #6: [2024] Neuronal wiring diagram of an adult brain  (447 cites)
- Decision: ___________

**41.** conf=0.818 title=0.98 cit=0.29 auth=1.0 `A=preprint` **⚠ BOTH IN TOP 500**
- A #157: [2023] Network Statistics of the Whole-Brain Connectome of <i>Drosophila</i>  (29 cites)
- B #331: [2024] Network statistics of the whole-brain connectome of Drosophila  (98 cites)
- Decision: ___________

**42.** conf=0.816 title=0.89 cit=0.42 auth=1.0 `A=preprint` (one in top 500)
- A #1672: [2020] Automatic whole cell organelle segmentation in volumetric electron microscopy  (20 cites)
- B #317: [2021] Whole-cell organelle segmentation in volume electron microscopy  (294 cites)
- Decision: ___________

**43.** conf=0.814 title=0.99 cit=0.27 auth=1.0 `A=preprint` (one in top 500)
- A #1092: [2017] A complete electron microscopy volume of the brain of adult <i>Drosophila melanogaster</i>  (52 cites)
- B #16: [2018] A Complete Electron Microscopy Volume of the Brain of Adult Drosophila melanogaster  (1135 cites)
- Decision: ___________

**44.** conf=0.809 title=1.00 cit=0.24 auth=1.0 `A=preprint` (one in top 500)
- A #884: [2022] The connectome of an insect brain  (8 cites)
- B #5: [2023] The connectome of an insect brain  (424 cites)
- Decision: ___________

**45.** conf=0.806 title=0.95 cit=0.29 auth=1.0 `A=preprint`
- A #1062: [2024] Light-microscopy based dense connectomic reconstruction of mammalian brain tissue  (21 cites)
- B #1962: [2025] Light-microscopy-based connectomic reconstruction of mammalian brain tissue  (34 cites)
- Decision: ___________

**46.** conf=0.801 title=0.99 cit=0.23 auth=1.0 `A=preprint` (one in top 500)
- A #879: [2020] The Neural Basis for a Persistent Internal State in <i>Drosophila</i> Females  (6 cites)
- B #329: [2020] The neural basis for a persistent internal state in Drosophila females  (121 cites)
- Decision: ___________

**47.** conf=0.788 title=0.99 cit=0.16 auth=1.0 `A=preprint` (one in top 500)
- A #345: [2019] Automated Reconstruction of a Serial-Section EM <i>Drosophila</i> Brain with Flood-Filling  (70 cites)
- B #1779: [2019] Automated Reconstruction of a Serial-Section EM Drosophila Brain with Flood-Filling Networ  (65 cites)
- Decision: ___________

**48.** conf=0.787 title=1.00 cit=0.75 auth=0.0 `A=preprint`
- A #9999: [2019] Freeze-frame imaging of synaptic activity using SynTagMA  (9 cites)
- B #1195: [2020] Freeze-frame imaging of synaptic activity using SynTagMA  (54 cites)
- Decision: ___________

**49.** conf=0.782 title=0.84 cit=0.34 auth=1.0 `A=preprint`
- A #657: [2022] Tools for connectomic reconstruction and analysis of a female <i>Drosophila</i> ventral ne  (25 cites)
- B #609: [2024] Connectomic reconstruction of a female Drosophila ventral nerve cord  (98 cites)
- Decision: ___________

**50.** conf=0.781 title=0.83 cit=0.36 auth=1.0 `A=preprint` **⚠ BOTH IN TOP 500**
- A #188: [2020] The connectome of the adult <i>Drosophila</i> mushroom body: implications for function  (19 cites)
- B #17: [2020] The connectome of the adult Drosophila mushroom body provides insights into function  (418 cites)
- Decision: ___________

**51.** conf=0.777 title=1.00 cit=0.71 auth=0.0 `A=preprint`
- A #9999: [2019] A null model of the mouse whole-neocortex micro-connectome  (19 cites)
- B #9999: [2019] A null model of the mouse whole-neocortex micro-connectome  (45 cites)
- Decision: ___________

**52.** conf=0.772 title=1.00 cit=0.69 auth=0.0 `B=preprint`
- A #9999: [2018] Highly multiplexed immunofluorescence imaging of human tissues and tumors using t-CyCIF an  (725 cites)
- B #9999: [2017] Highly multiplexed immunofluorescence imaging of human tissues and tumors using t-CyCIF an  (104 cites)
- Decision: ___________

**53.** conf=0.768 title=0.99 cit=0.38 auth=0.5 `A=preprint` **⚠ BOTH IN TOP 500**
- A #299: [2020] Reconstruction of motor control circuits in adult <i>Drosophila</i> using automated transm  (35 cites)
- B #63: [2021] Reconstruction of motor control circuits in adult Drosophila using automated transmission   (279 cites)
- Decision: ___________

**54.** conf=0.762 title=1.00 cit=0.45 auth=1.0 `diff_DOIs`
- A #1433: [2004] Cluster primary ion bombardment of organic materials  (283 cites)
- B #1471: [2004] Cluster primary ion bombardment of organic materials  (226 cites)
- Decision: ___________

**55.** conf=0.762 title=0.76 cit=0.38 auth=1.0 `A=preprint`
- A #1137: [2023] Transforming descending input into motor output: An analysis of the <i>Drosophila</i> Male  (38 cites)
- B #1511: [2024] Transforming descending input into behavior: The organization of premotor circuits in the   (45 cites)
- Decision: ___________

**56.** conf=0.760 title=0.80 cit=0.33 auth=1.0 `A=preprint` **⚠ BOTH IN TOP 500**
- A #116: [2023] Whole-brain annotation and multi-connectome cell typing quantifies circuit stereotypy in <  (107 cites)
- B #72: [2024] Whole-brain annotation and multi-connectome cell typing of Drosophila  (324 cites)
- Decision: ___________

**57.** conf=0.752 title=0.86 cit=0.20 auth=1.0 `A=preprint` (one in top 500)
- A #880: [2019] Automatic Detection of Synaptic Partners in a Whole-Brain <i>Drosophila</i> EM Dataset  (25 cites)
- B #101: [2021] Automatic detection of synaptic partners in a whole-brain Drosophila electron microscopy d  (184 cites)
- Decision: ___________

**58.** conf=0.752 title=1.00 cit=0.61 auth=0.0 `A=preprint`
- A #9999: [2017] Spatial Topography of Individual-Specific Cortical Networks Predicts Human Cognition, Pers  (80 cites)
- B #9999: [2018] Spatial Topography of Individual-Specific Cortical Networks Predicts Human Cognition, Pers  (695 cites)
- Decision: ___________

**59.** conf=0.752 title=1.00 cit=0.61 auth=0.0 `A=preprint`
- A #9999: [2022] Bisected graph matching improves automated pairing of bilaterally homologous neurons from   (4 cites)
- B #9999: [2022] Bisected graph matching improves automated pairing of bilaterally homologous neurons from   (7 cites)
- Decision: ___________

**60.** conf=0.750 title=1.00 cit=0.60 auth=0.0 `B=preprint`
- A #9999: [2020] A workflow for visualizing human cancer biopsies using large-format electron microscopy  (24 cites)
- B #9999: [2019] A workflow for visualizing human cancer biopsies using large-format electron microscopy  (6 cites)
- Decision: ___________

**61.** conf=0.750 title=1.00 cit=1.00 auth=0.0 `diff_DOIs`
- A #9999: [2017] The small world of osteocytes: connectomics of the lacuno-canalicular network in bone  (152 cites)
- B #9999: [2017] The small world of osteocytes: connectomics of the lacuno-canalicular network in bone  (143 cites)
- Decision: ___________

**62.** conf=0.746 title=1.00 cit=0.58 auth=0.0 `A=preprint`
- A #9999: [2020] Three-dimensional residual channel attention networks denoise and sharpen fluorescence mic  (30 cites)
- B #1588: [2021] Three-dimensional residual channel attention networks denoise and sharpen fluorescence mic  (207 cites)
- Decision: ___________

**63.** conf=0.746 title=1.00 cit=0.58 auth=0.0 `A=preprint`
- A #9999: [2021] Regional cytoarchitecture of the adult and developing mouse enteric nervous system  (3 cites)
- B #9999: [2022] Regional cytoarchitecture of the adult and developing mouse enteric nervous system  (38 cites)
- Decision: ___________

**64.** conf=0.743 title=0.91 cit=0.50 auth=1.0 `diff_DOIs` **⚠ BOTH IN TOP 500**
- A #232: [2019] Cancer statistics, 2019  (20874 cites)
- B #196: [2020] Cancer statistics, 2020  (21282 cites)
- Decision: ___________

**65.** conf=0.743 title=1.00 cit=0.57 auth=0.0 `A=preprint`
- A #9999: [2019] Label-retention expansion microscopy  (34 cites)
- B #1073: [2021] Label-retention expansion microscopy  (81 cites)
- Decision: ___________

**66.** conf=0.742 title=0.97 cit=0.60 auth=0.0 `A=preprint`
- A #9999: [2024] An inhibitory acetylcholine receptor gates context dependent mechanosensory processing in   (1 cites)
- B #9999: [2024] An inhibitory acetylcholine receptor gates context-dependent mechanosensory processing in   (10 cites)
- Decision: ___________

**67.** conf=0.740 title=0.84 cit=0.18 auth=1.0 `A=preprint`
- A #919: [2023] Cell-type-specific inhibitory circuitry from a connectomic census of mouse visual cortex  (73 cites)
- B #1463: [2025] Inhibitory specificity from a connectomic census of mouse visual cortex  (52 cites)
- Decision: ___________

**68.** conf=0.739 title=1.00 cit=0.96 auth=0.0 `diff_DOIs`
- A #9999: [2013] Schizophrenia and abnormal brain network hubs.  (172 cites)
- B #9999: [2013] Schizophrenia and abnormal brain network hubs  (212 cites)
- Decision: ___________

**69.** conf=0.735 title=1.00 cit=0.54 auth=0.0 `A=preprint`
- A #9999: [2022] Fast imaging of millimeter-scale areas with beam deflection transmission electron microsco  (11 cites)
- B #9999: [2024] Fast imaging of millimeter-scale areas with beam deflection transmission electron microsco  (10 cites)
- Decision: ___________

**70.** conf=0.735 title=1.00 cit=0.54 auth=0.0 `A=preprint`
- A #9999: [2016] Could a Neuroscientist Understand a Microprocessor?  (87 cites)
- B #9999: [2017] Could a Neuroscientist Understand a Microprocessor?  (269 cites)
- Decision: ___________

**71.** conf=0.733 title=1.00 cit=0.53 auth=0.0 `A=preprint`
- A #9999: [2020] Non-canonical autophagy drives alternative ATG8 conjugation to phosphatidylserine  (15 cites)
- B #794: [2021] Non-canonical autophagy drives alternative ATG8 conjugation to phosphatidylserine  (197 cites)
- Decision: ___________

**72.** conf=0.733 title=1.00 cit=0.53 auth=0.0 `A=preprint`
- A #9999: [2020] Light microscopy based approach for mapping connectivity with molecular specificity  (9 cites)
- B #1218: [2020] Light microscopy based approach for mapping connectivity with molecular specificity  (56 cites)
- Decision: ___________

**73.** conf=0.732 title=1.00 cit=0.53 auth=0.0 `A=preprint`
- A #9999: [2019] Reconstruction of 1,000 projection neurons reveals new cell types and organization of long  (61 cites)
- B #1343: [2019] Reconstruction of 1,000 Projection Neurons Reveals New Cell Types and Organization of Long  (552 cites)
- Decision: ___________

**74.** conf=0.730 title=1.00 cit=0.52 auth=0.0 `A=preprint`
- A #9999: [2022] Connectomic analysis of thalamus-driven disinhibition in cortical layer 4  (3 cites)
- B #1345: [2022] Connectomic analysis of thalamus-driven disinhibition in cortical layer 4  (26 cites)
- Decision: ___________

**75.** conf=0.729 title=0.99 cit=0.53 auth=0.0 `A=preprint`
- A #9999: [2020] Circuit reorganization in the <i>Drosophila</i> mushroom body calyx accompanies memory con  (4 cites)
- B #568: [2021] Circuit reorganization in the Drosophila mushroom body calyx accompanies memory consolidat  (52 cites)
- Decision: ___________

**76.** conf=0.727 title=0.98 cit=0.53 auth=0.0 `A=preprint`
- A #9999: [2023] A neurotransmitter atlas of <i>C. elegans</i> males and hermaphrodites  (6 cites)
- B #9999: [2024] A neurotransmitter atlas of C. elegans males and hermaphrodites  (14 cites)
- Decision: ___________

**77.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Neuronal activity regulating the dauer entry decision in <i>Caenorhabditis elegans</i>  (0 cites)
- B #9999: [2025] Neuronal Activity Regulating the Dauer Entry Decision in <i>Caenorhabditis elegans</i>  (0 cites)
- Decision: ___________

**78.** conf=0.725 title=1.00 cit=0.90 auth=0.0 `diff_DOIs`
- A #9999: [2012] How to suppress undesired synchronization  (57 cites)
- B #9999: [2012] How to suppress undesired synchronization  (62 cites)
- Decision: ___________

**79.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] Selective life-long suppression of an odor processing channel in response to critical peri  (0 cites)
- B #9999: [2025] Selective life-long suppression of an odor processing channel in response to critical peri  (0 cites)
- Decision: ___________

**80.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2021] Escape Steering by Cholecystokinin Peptidergic Signaling  (0 cites)
- B #1986: [2022] Escape steering by cholecystokinin peptidergic signaling  (27 cites)
- Decision: ___________

**81.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] Close-Up of vesicular ER Exit Sites by Volume Electron Imaging using FIB-SEM  (3 cites)
- B #9999: [2025] Close-up of vesicular ER exit sites by volume electron imaging using FIB-SEM  (0 cites)
- Decision: ___________

**82.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Mechanism of barotaxis in marine zooplankton  (14 cites)
- B #9999: [2024] Mechanism of barotaxis in marine zooplankton  (3 cites)
- Decision: ___________

**83.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] A hyperpolarizing neuron recruits undocked innexin hemichannels to transmit neural informa  (0 cites)
- B #9999: [2024] A hyperpolarizing neuron recruits undocked innexin hemichannels to transmit neural informa  (5 cites)
- Decision: ___________

**84.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] Morphology and connectivity of retinal horizontal cells in two avian species  (2 cites)
- B #9999: [2025] Morphology and connectivity of retinal horizontal cells in two avian species  (5 cites)
- Decision: ___________

**85.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Accelerating the continuous community sharing of digital neuromorphology data  (1 cites)
- B #9999: [2024] Accelerating the continuous community sharing of digital neuromorphology data  (12 cites)
- Decision: ___________

**86.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Paired and solitary ionocytes in the zebrafish olfactory epithelium  (2 cites)
- B #9999: [2025] Paired and solitary ionocytes in the zebrafish olfactory epithelium  (1 cites)
- Decision: ___________

**87.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] Selective life-long suppression of an odor processing channel in response to critical peri  (0 cites)
- B #9999: [2025] Selective life-long suppression of an odor processing channel in response to critical peri  (0 cites)
- Decision: ___________

**88.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #1205: [2024] Whole-body connectome of a segmented annelid larva  (15 cites)
- B #9999: [2025] Whole-body connectome of a segmented annelid larva  (4 cites)
- Decision: ___________

**89.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- B #9999: [2025] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- Decision: ___________

**90.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2022] Cross-modality Synthesis of EM Time Series and Live Fluorescence Imaging  (1 cites)
- B #9999: [2022] Cross-modality synthesis of EM time series and live fluorescence imaging  (11 cites)
- Decision: ___________

**91.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (1 cites)
- B #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (0 cites)
- Decision: ___________

**92.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Direct segmentation of cortical cytoarchitectonic domains using ultra-high-resolution whol  (0 cites)
- B #9999: [2024] Direct segmentation of cortical cytoarchitectonic domains using ultra-high-resolution whol  (0 cites)
- Decision: ___________

**93.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Automated segmentation of synchrotron-scanned fossils  (0 cites)
- B #9999: [2025] Automated segmentation of synchrotron-scanned fossils  (0 cites)
- Decision: ___________

**94.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Spyglass: a framework for reproducible and shareable neuroscience research  (9 cites)
- B #9999: [2025] Spyglass: a framework for reproducible and shareable neuroscience research  (0 cites)
- Decision: ___________

**95.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- B #9999: [2025] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- Decision: ___________

**96.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (1 cites)
- B #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (0 cites)
- Decision: ___________

**97.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Deep Neural Networks to Register and Annotate Cells in Moving and Deforming Nervous System  (3 cites)
- B #9999: [2025] Deep Neural Networks to Register and Annotate Cells in Moving and Deforming Nervous System  (0 cites)
- Decision: ___________

**98.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Molecular identification of wide-field amacrine cells in mouse retina that encode stimulus  (5 cites)
- B #9999: [2024] Molecular identification of wide-field amacrine cells in mouse retina that encode stimulus  (2 cites)
- Decision: ___________

**99.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- B #9999: [2024] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (1 cites)
- Decision: ___________

**100.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `B=preprint`
- A #9999: [2019] Fast, Versatile and Quantitative Annotation of Complex Images  (5 cites)
- B #9999: [2018] Fast, versatile, and quantitative annotation of complex images  (0 cites)
- Decision: ___________

**101.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (1 cites)
- B #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (0 cites)
- Decision: ___________

**102.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2019] An adult brain atlas reveals broad neuroanatomical changes in independently evolved popula  (13 cites)
- B #9999: [2019] An Adult Brain Atlas Reveals Broad Neuroanatomical Changes in Independently Evolved Popula  (44 cites)
- Decision: ___________

**103.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] The Brain Image Library: A Community-Contributed Microscopy Resource for Neuroscientists  (3 cites)
- B #9999: [2024] The Brain Image Library: A Community-Contributed Microscopy Resource for Neuroscientists  (7 cites)
- Decision: ___________

**104.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Profiling presynaptic scaffolds using split-GFP reconstitution reveals cell-type-specific   (0 cites)
- B #9999: [2026] Profiling presynaptic scaffolds using split-GFP reconstitution reveals cell-type-specific   (0 cites)
- Decision: ___________

**105.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] Neural Connectome of the Ctenophore Statocyst  (0 cites)
- B #9999: [2026] Neural connectome of the ctenophore statocyst  (0 cites)
- Decision: ___________

**106.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] <i>C. elegans</i> epicuticlins define specific compartments in the apical extracellular ma  (1 cites)
- B #9999: [2024] <i>C. elegans</i> epicuticlins define specific compartments in the apical extracellular ma  (6 cites)
- Decision: ___________

**107.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Molecular identification of wide-field amacrine cells in mouse retina that encode stimulus  (5 cites)
- B #9999: [2024] Molecular identification of wide-field amacrine cells in mouse retina that encode stimulus  (2 cites)
- Decision: ___________

**108.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] ElectroPhysiomeGAN: Generation of Biophysical Neuron Model Parameters from Recorded Electr  (0 cites)
- B #9999: [2025] ElectroPhysiomeGAN: Generation of Biophysical Neuron Model Parameters from Recorded Electr  (0 cites)
- Decision: ___________

**109.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `B=preprint`
- A #9999: [2018] Connectomics of the zebrafish's lateral-line neuromast reveals wiring and miswiring in a s  (62 cites)
- B #9999: [2018] Connectomics of the zebrafish’s lateral-line neuromast reveals wiring and miswiring in a s  (5 cites)
- Decision: ___________

**110.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] ElectroPhysiomeGAN: Generation of Biophysical Neuron Model Parameters from Recorded Electr  (0 cites)
- B #9999: [2024] ElectroPhysiomeGAN: Generation of Biophysical Neuron Model Parameters from Recorded Electr  (0 cites)
- Decision: ___________

**111.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Lamellar Schwann cells in the Pacinian corpuscle potentiate vibration perception  (3 cites)
- B #9999: [2025] Lamellar Schwann cells in the Pacinian corpuscle potentiate vibration perception  (2 cites)
- Decision: ___________

**112.** conf=0.725 title=1.00 cit=0.50 auth=0.0
- A #9999: [2021] NucMM Dataset: 3D Neuronal Nuclei Instance Segmentation at Sub-Cubic Millimeter Scale  (1 cites)
- B #9999: [2021] NucMM Dataset: 3D Neuronal Nuclei Instance Segmentation at Sub-Cubic Millimeter Scale  (27 cites)
- Decision: ___________

**113.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Spyglass: a framework for reproducible and shareable neuroscience research  (9 cites)
- B #9999: [2025] Spyglass: a framework for reproducible and shareable neuroscience research  (0 cites)
- Decision: ___________

**114.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2020] Multi-modal imaging of a single mouse brain over five orders of magnitude of resolution  (3 cites)
- B #9999: [2021] Multi-modal imaging of a single mouse brain over five orders of magnitude of resolution  (32 cites)
- Decision: ___________

**115.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Deep Neural Networks to Register and Annotate Cells in Moving and Deforming Nervous System  (3 cites)
- B #9999: [2025] Deep neural networks to register and annotate cells in moving and deforming nervous system  (0 cites)
- Decision: ___________

**116.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- B #9999: [2025] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- Decision: ___________

**117.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Compression-based inference of network motif sets  (0 cites)
- B #9999: [2024] Compression-based inference of network motif sets  (3 cites)
- Decision: ___________

**118.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `B=preprint`
- A #9999: [2021] Oligodendrocyte precursor cells prune axons in the mouse neocortex  (11 cites)
- B #956: [2021] Oligodendrocyte precursor cells prune axons in the mouse neocortex  (19 cites)
- Decision: ___________

**119.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2022] Sharing Massive Biomedical Data at Magnitudes Lower Bandwidth Using Implicit Neural Functi  (3 cites)
- B #9999: [2024] Sharing massive biomedical data at magnitudes lower bandwidth using implicit neural functi  (6 cites)
- Decision: ___________

**120.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Efficient cell-wide mapping of mitochondria in electron microscopic volumes using webKnoss  (0 cites)
- B #9999: [2025] Efficient cell-wide mapping of mitochondria in electron microscopic volumes using webKnoss  (5 cites)
- Decision: ___________

**121.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2019] DeepCLIP: Predicting the effect of mutations on protein-RNA binding with Deep Learning  (59 cites)
- B #9999: [2020] DeepCLIP: predicting the effect of mutations on protein–RNA binding with deep learning  (101 cites)
- Decision: ___________

**122.** conf=0.725 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2022] Topographic axonal projection at single-cell precision supports local retinotopy in the mo  (3 cites)
- B #9999: [2023] Topographic axonal projection at single-cell precision supports local retinotopy in the mo  (22 cites)
- Decision: ___________

**123.** conf=0.723 title=1.00 cit=0.49 auth=0.0 `A=preprint`
- A #9999: [2023] mEMbrain: an interactive deep learning MATLAB tool for connectomic segmentation on commodi  (4 cites)
- B #9999: [2023] mEMbrain: an interactive deep learning MATLAB tool for connectomic segmentation on commodi  (14 cites)
- Decision: ___________

**124.** conf=0.723 title=1.00 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] An ultrastructural map of a spinal sensorimotor circuit reveals the potential of astroglia  (1 cites)
- B #9999: [2025] An ultrastructural map of a spinal sensorimotor circuit reveals the potential of astroglia  (0 cites)
- Decision: ___________

**125.** conf=0.723 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] A comprehensive mechanosensory connectome reveals a somatotopically organized neural circu  (2 cites)
- B #9999: [2025] A comprehensive mechanosensory connectome reveals a somatotopically organized neural circu  (0 cites)
- Decision: ___________

**126.** conf=0.723 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] A comprehensive mechanosensory connectome reveals a somatotopically organized neural circu  (2 cites)
- B #9999: [2025] A comprehensive mechanosensory connectome reveals a somatotopically organized neural circu  (0 cites)
- Decision: ___________

**127.** conf=0.723 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Cell type-specific driver lines targeting the <i>Drosophila</i> central complex and their   (12 cites)
- B #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (8 cites)
- Decision: ___________

**128.** conf=0.723 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Cell type-specific driver lines targeting the <i>Drosophila</i> central complex and their   (12 cites)
- B #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (0 cites)
- Decision: ___________

**129.** conf=0.723 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Cell type-specific driver lines targeting the <i>Drosophila</i> central complex and their   (12 cites)
- B #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (4 cites)
- Decision: ___________

**130.** conf=0.723 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Cell type-specific driver lines targeting the <i>Drosophila</i> central complex and their   (12 cites)
- B #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (8 cites)
- Decision: ___________

**131.** conf=0.722 title=1.00 cit=0.49 auth=0.0 `A=preprint`
- A #9999: [2023] Driver lines for studying associative learning in Drosophila  (15 cites)
- B #9999: [2024] Driver lines for studying associative learning in Drosophila  (5 cites)
- Decision: ___________

**132.** conf=0.722 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] Perisynaptic astroglial response to <i>in vivo</i> long-term potentiation and concurrent l  (0 cites)
- B #9999: [2025] Perisynaptic Astroglial Response to In Vivo Long-Term Potentiation and Concurrent Long-Ter  (1 cites)
- Decision: ___________

**133.** conf=0.722 title=1.00 cit=0.49 auth=0.0 `A=preprint`
- A #9999: [2019] DeepACSON: Automated Segmentation of White Matter in 3D Electron Microscopy  (2 cites)
- B #783: [2021] DeepACSON automated segmentation of white matter in 3D electron microscopy  (57 cites)
- Decision: ___________

**134.** conf=0.722 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Decomposed Linear Dynamical Systems (dLDS) models reveal instantaneous, context-dependent   (1 cites)
- B #9999: [2025] Decomposed Linear Dynamical Systems (dLDS) models reveal instantaneous, context-dependent   (4 cites)
- Decision: ___________

**135.** conf=0.722 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] A pair of dopaminergic neurons DAN-c1 mediate <i>Drosophila</i> larval aversive olfactory   (0 cites)
- B #9999: [2025] A pair of dopaminergic neurons DAN-c1 mediate Drosophila larval aversive olfactory learnin  (0 cites)
- Decision: ___________

**136.** conf=0.722 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] A pair of dopaminergic neurons DAN-c1 mediate <i>Drosophila</i> larval aversive olfactory   (0 cites)
- B #9999: [2025] A pair of dopaminergic neurons DAN-c1 mediate Drosophila larval aversive olfactory learnin  (0 cites)
- Decision: ___________

**137.** conf=0.722 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] A pair of dopaminergic neurons DAN-c1 mediate <i>Drosophila</i> larval aversive olfactory   (0 cites)
- B #9999: [2024] A pair of dopaminergic neurons DAN-c1 mediate Drosophila larval aversive olfactory learnin  (4 cites)
- Decision: ___________

**138.** conf=0.722 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Intricate response dynamics enhances stimulus discrimination in the resource-limited <i>C.  (3 cites)
- B #9999: [2024] Intricate response dynamics enhances stimulus discrimination in the resource-limited C. el  (5 cites)
- Decision: ___________

**139.** conf=0.722 title=1.00 cit=0.89 auth=0.0 `diff_DOIs`
- A #9999: [2013] Effect of correlations on network controllability  (202 cites)
- B #9999: [2012] Effect of correlations on network controllability  (172 cites)
- Decision: ___________

**140.** conf=0.722 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (0 cites)
- B #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (11 cites)
- Decision: ___________

**141.** conf=0.722 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (0 cites)
- B #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (0 cites)
- Decision: ___________

**142.** conf=0.722 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (0 cites)
- B #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (0 cites)
- Decision: ___________

**143.** conf=0.722 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (1 cites)
- B #9999: [2025] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- Decision: ___________

**144.** conf=0.722 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (1 cites)
- B #9999: [2025] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- Decision: ___________

**145.** conf=0.722 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] Maturation of GABAergic signalling times the opening of a critical period in <i>Drosophila  (3 cites)
- B #9999: [2025] Maturation of GABAergic signalling times the opening of a critical period in Drosophila me  (0 cites)
- Decision: ___________

**146.** conf=0.721 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Four Individually Identified Paired Dopamine Neurons Signal Taste Punishment in Larval <i>  (1 cites)
- B #9999: [2025] Four Individually Identified Paired Dopamine Neurons Signal Taste Punishment in Larval Dro  (0 cites)
- Decision: ___________

**147.** conf=0.721 title=1.00 cit=0.49 auth=0.0 `A=preprint`
- A #1205: [2024] Whole-body connectome of a segmented annelid larva  (15 cites)
- B #9999: [2024] Whole-body connectome of a segmented annelid larva  (5 cites)
- Decision: ___________

**148.** conf=0.721 title=1.00 cit=0.48 auth=0.0 `A=preprint`
- A #9999: [2018] Learning cellular morphology with neural networks  (8 cites)
- B #9999: [2019] Learning cellular morphology with neural networks  (70 cites)
- Decision: ___________

**149.** conf=0.721 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Developmental remodeling repurposes larval neurons for sexual behaviors in adult <i>Drosop  (1 cites)
- B #9999: [2024] Developmental remodeling repurposes larval neurons for sexual behaviors in adult Drosophil  (10 cites)
- Decision: ___________

**150.** conf=0.721 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2022] The unique synaptic circuitry of specialized olfactory glomeruli in <i>Drosophila melanoga  (2 cites)
- B #9999: [2023] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (2 cites)
- Decision: ___________

**151.** conf=0.721 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] A single NPFR neuropeptide F receptor neuron that regulates thirst behaviors in Drosophila  (3 cites)
- B #9999: [2025] A Single NPFR Neuropeptide F Receptor Neuron That Regulates Thirst Behaviors in <i>Drosoph  (0 cites)
- Decision: ___________

**152.** conf=0.721 title=1.00 cit=0.48 auth=0.0 `A=preprint`
- A #9999: [2024] The Oviposition Inhibitory Neuron is a potential hub of multi-circuit integration in the <  (1 cites)
- B #9999: [2025] The Oviposition Inhibitory Neuron is a Potential Hub of Multi-Circuit Integration in the <  (1 cites)
- Decision: ___________

**153.** conf=0.721 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Olfactory combinatorial coding supports risk-reward decision making in <i>C. elegans</i>  (1 cites)
- B #9999: [2025] Olfactory combinatorial coding supports risk-reward decision making in C. elegans  (0 cites)
- Decision: ___________

**154.** conf=0.721 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Olfactory combinatorial coding supports risk-reward decision making in <i>C. elegans</i>  (1 cites)
- B #9999: [2025] Olfactory combinatorial coding supports risk-reward decision making in C. elegans  (0 cites)
- Decision: ___________

**155.** conf=0.720 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of <i>Drosophila</i> larvae  (1 cites)
- B #9999: [2024] Morphology and ultrastructure of external sense organs of Drosophila larvae  (3 cites)
- Decision: ___________

**156.** conf=0.720 title=1.00 cit=0.48 auth=0.0 `B=preprint`
- A #9999: [2015] A serial multiplex immunogold labeling method for identifying peptidergic neurons in conne  (94 cites)
- B #9999: [2015] A Serial Multiplex Immunogold Labeling Method for Identifying Peptidergic Neurons in Conne  (1 cites)
- Decision: ___________

**157.** conf=0.720 title=1.00 cit=0.48 auth=1.0 `A=preprint` **⚠ BOTH IN TOP 500**
- A #86: [2020] Structured sampling of olfactory input by the fly mushroom body  (39 cites)
- B #107: [2022] Structured sampling of olfactory input by the fly mushroom body  (62 cites)
- Decision: ___________

**158.** conf=0.720 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Individuality across environmental context in <i>Drosophila melanogaster</i>  (2 cites)
- B #9999: [2024] Individuality across environmental context in Drosophila melanogaster  (1 cites)
- Decision: ___________

**159.** conf=0.720 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Individuality across environmental context in <i>Drosophila melanogaster</i>  (2 cites)
- B #9999: [2025] Individuality across environmental context in Drosophila melanogaster  (1 cites)
- Decision: ___________

**160.** conf=0.720 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Individuality across environmental context in <i>Drosophila melanogaster</i>  (2 cites)
- B #9999: [2026] Individuality across environmental context in Drosophila melanogaster  (1 cites)
- Decision: ___________

**161.** conf=0.720 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Individuality across environmental context in <i>Drosophila melanogaster</i>  (2 cites)
- B #9999: [2025] Individuality across environmental context in Drosophila melanogaster  (0 cites)
- Decision: ___________

**162.** conf=0.720 title=0.99 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2016] Neuroendocrine Modulation Sustains the <i>C. elegans</i> Forward Motor State  (0 cites)
- B #1847: [2016] Neuroendocrine modulation sustains the C. elegans forward motor state  (71 cites)
- Decision: ___________

**163.** conf=0.720 title=0.99 cit=0.49 auth=0.0 `A=preprint` (one in top 500)
- A #9999: [2020] Expansion Sequencing: Spatially Precise <i>In Situ</i> Transcriptomics in Intact Biologica  (29 cites)
- B #99: [2021] Expansion sequencing: Spatially precise in situ transcriptomics in intact biological syste  (398 cites)
- Decision: ___________

**164.** conf=0.720 title=1.00 cit=0.48 auth=0.0 `A=preprint`
- A #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (2 cites)
- B #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (21 cites)
- Decision: ___________

**165.** conf=0.720 title=1.00 cit=0.48 auth=0.0 `B=preprint`
- A #9999: [2021] A whole-brain monosynaptic input connectome to neuron classes in mouse visual cortex  (9 cites)
- B #9999: [2021] A whole-brain monosynaptic input connectome to neuron classes in mouse visual cortex  (4 cites)
- Decision: ___________

**166.** conf=0.719 title=0.98 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Spatial transcriptomics in the adult <i>Drosophila</i> brain and body  (1 cites)
- B #9999: [2025] Spatial transcriptomics in the adult Drosophila brain and body  (1 cites)
- Decision: ___________

**167.** conf=0.719 title=0.98 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Spatial transcriptomics in the adult <i>Drosophila</i> brain and body  (1 cites)
- B #9999: [2025] Spatial transcriptomics in the adult Drosophila brain and body  (1 cites)
- Decision: ___________

**168.** conf=0.719 title=0.98 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Spatial transcriptomics in the adult <i>Drosophila</i> brain and body  (1 cites)
- B #9999: [2024] Spatial transcriptomics in the adult Drosophila brain and body  (7 cites)
- Decision: ___________

**169.** conf=0.719 title=0.98 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Social Experience Shapes Fighting Strategies in <i>Drosophila</i>  (0 cites)
- B #9999: [2025] Social Experience Shapes Fighting Strategies in Drosophila  (0 cites)
- Decision: ___________

**170.** conf=0.719 title=0.98 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Social Experience Shapes Fighting Strategies in <i>Drosophila</i>  (0 cites)
- B #9999: [2025] Social experience shapes fighting strategies in Drosophila  (0 cites)
- Decision: ___________

**171.** conf=0.719 title=1.00 cit=0.48 auth=0.0 `A=preprint`
- A #9999: [2024] Molecular characterization of gustatory second-order neurons reveals integrative mechanism  (0 cites)
- B #9999: [2025] Molecular characterization of gustatory second-order neurons reveals integrative mechanism  (0 cites)
- Decision: ___________

**172.** conf=0.719 title=1.00 cit=0.48 auth=0.0 `A=preprint`
- A #9999: [2024] Molecular characterization of gustatory second-order neurons reveals integrative mechanism  (0 cites)
- B #9999: [2024] Molecular characterization of gustatory second-order neurons reveals integrative mechanism  (3 cites)
- Decision: ___________

**173.** conf=0.719 title=1.00 cit=0.48 auth=0.0 `A=preprint`
- A #9999: [2024] Molecular characterization of gustatory second-order neurons reveals integrative mechanism  (0 cites)
- B #9999: [2025] Molecular characterization of gustatory second-order neurons reveals integrative mechanism  (0 cites)
- Decision: ___________

**174.** conf=0.719 title=1.00 cit=0.47 auth=0.0 `A=preprint`
- A #9999: [2021] Visual recognition of social signals by a tecto-thalamic neural circuit  (15 cites)
- B #9999: [2022] Visual recognition of social signals by a tectothalamic neural circuit  (79 cites)
- Decision: ___________

**175.** conf=0.719 title=1.00 cit=0.47 auth=0.0 `A=preprint`
- A #9999: [2022] NBS-SNI, an extension of the Network-based statistic: Abnormal functional connections betw  (0 cites)
- B #9999: [2023] NBS-SNI, an extension of the network-based statistic: Abnormal functional connections betw  (0 cites)
- Decision: ___________

**176.** conf=0.719 title=0.98 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2026] A pilot study for whole proteome tagging in <i>C. elegans</i>  (0 cites)
- B #9999: [2026] A pilot study for whole proteome tagging in C. elegans  (0 cites)
- Decision: ___________

**177.** conf=0.719 title=0.98 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2026] A pilot study for whole proteome tagging in <i>C. elegans</i>  (0 cites)
- B #9999: [2026] A pilot study for whole proteome tagging in C. elegans  (0 cites)
- Decision: ___________

**178.** conf=0.718 title=0.98 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] Mapping the developmental structure of stereotyped and individual-unique behavioral spaces  (1 cites)
- B #9999: [2024] Mapping the developmental structure of stereotyped and individual-unique behavioral spaces  (10 cites)
- Decision: ___________

**179.** conf=0.718 title=1.00 cit=0.47 auth=0.0 `A=preprint`
- A #9999: [2019] UNI-EM: An Environment for Deep Neural Network-Based Automated Segmentation of Neuronal El  (7 cites)
- B #9999: [2019] UNI-EM: An Environment for Deep Neural Network-Based Automated Segmentation of Neuronal El  (54 cites)
- Decision: ___________

**180.** conf=0.718 title=0.98 cit=0.50 auth=0.0 `B=preprint` (one in top 500)
- A #151: [2016] Quantitative neuroanatomy for connectomics in Drosophila  (371 cites)
- B #9999: [2015] Quantitative neuroanatomy for connectomics in <i>Drosophila</i>  (43 cites)
- Decision: ___________

**181.** conf=0.718 title=0.98 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] EM-Compressor: Electron Microscopy Image Compression in Connectomics with Variational Auto  (0 cites)
- B #9999: [2025] EM-Compressor: Electron Microscopy Image Compression in Connectomics with Variational Auto  (3 cites)
- Decision: ___________

**182.** conf=0.717 title=1.00 cit=0.47 auth=0.0 `A=preprint`
- A #1205: [2024] Whole-body connectome of a segmented annelid larva  (15 cites)
- B #9999: [2025] Whole-body connectome of a segmented annelid larva  (4 cites)
- Decision: ___________

**183.** conf=0.717 title=0.98 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2020] 3D FIB-SEM reconstruction of microtubule-organelle interaction in whole primary mouse beta  (4 cites)
- B #752: [2020] 3D FIB-SEM reconstruction of microtubule–organelle interaction in whole primary mouse β ce  (112 cites)
- Decision: ___________

**184.** conf=0.717 title=1.00 cit=0.47 auth=0.0 `A=preprint`
- A #9999: [2016] The wiring diagram of a glomerular olfactory system  (21 cites)
- B #586: [2016] The wiring diagram of a glomerular olfactory system  (219 cites)
- Decision: ___________

**185.** conf=0.717 title=1.00 cit=0.47 auth=0.0 `A=preprint`
- A #9999: [2024] A connectomics-driven analysis reveals novel characterization of border regions in mouse v  (0 cites)
- B #9999: [2025] A connectomics-driven analysis reveals novel characterization of border regions in mouse v  (0 cites)
- Decision: ___________

**186.** conf=0.717 title=1.00 cit=0.47 auth=0.0 `A=preprint`
- A #9999: [2023] Mechanism of barotaxis in marine zooplankton  (14 cites)
- B #9999: [2024] Mechanism of barotaxis in marine zooplankton  (5 cites)
- Decision: ___________

**187.** conf=0.717 title=1.00 cit=0.47 auth=0.0 `A=preprint`
- A #9999: [2024] NeuroSC: Exploring Neurodevelopment via Spatiotemporal Collation of Anatomical Networks  (0 cites)
- B #9999: [2025] NeuroSC: Exploring Neurodevelopment via Spatiotemporal Collation of Anatomical Networks  (0 cites)
- Decision: ___________

**188.** conf=0.716 title=1.00 cit=0.46 auth=0.0 `B=preprint`
- A #9999: [2020] Toward an Automated HPC Pipeline for Processing Large Scale Electron Microscopy Data  (11 cites)
- B #9999: [2020] Toward an Automated HPC Pipeline for Processing Large Scale Electron Microscopy Data  (2 cites)
- Decision: ___________

**189.** conf=0.716 title=1.00 cit=0.46 auth=0.0 `B=preprint`
- A #858: [2017] Wiring variations that enable and constrain neural computation in a sensory microcircuit  (147 cites)
- B #9999: [2017] Wiring variations that enable and constrain neural computation in a sensory microcircuit  (3 cites)
- Decision: ___________

**190.** conf=0.716 title=1.00 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2024] Deriving connectivity from spiking activity in detailed models of large-scale cortical mic  (0 cites)
- B #9999: [2025] Deriving connectivity from spiking activity in detailed models of large-scale cortical mic  (0 cites)
- Decision: ___________

**191.** conf=0.716 title=0.99 cit=0.48 auth=0.0 `A=preprint`
- A #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in <i>C. elegans</i>  (0 cites)
- B #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (6 cites)
- Decision: ___________

**192.** conf=0.715 title=0.99 cit=0.48 auth=0.0 `A=preprint`
- A #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in <i>C. elegans</i>  (0 cites)
- B #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (2 cites)
- Decision: ___________

**193.** conf=0.715 title=0.99 cit=0.48 auth=0.0 `A=preprint`
- A #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in <i>C. elegans</i>  (0 cites)
- B #9999: [2024] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (2 cites)
- Decision: ___________

**194.** conf=0.715 title=0.99 cit=0.48 auth=0.0 `A=preprint`
- A #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in <i>C. elegans</i>  (0 cites)
- B #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (1 cites)
- Decision: ___________

**195.** conf=0.715 title=1.00 cit=0.46 auth=0.0 `diff_DOIs`
- A #9999: [2025] Organization of mouse prefrontal cortex subnetwork revealed by spatial single-cell multi-o  (0 cites)
- B #9999: [2026] Organization of mouse prefrontal cortex subnetwork revealed by spatial single-cell multi-o  (0 cites)
- Decision: ___________

**196.** conf=0.715 title=1.00 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2020] X-ray microscopy enables multiscale high-resolution 3D imaging of plant cells, tissues, an  (6 cites)
- B #9999: [2021] X-ray microscopy enables multiscale high-resolution 3D imaging of plant cells, tissues, an  (83 cites)
- Decision: ___________

**197.** conf=0.715 title=1.00 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2024] Temporal resolution of spike coding in feedforward networks with signal convergence and di  (0 cites)
- B #9999: [2025] Temporal resolution of spike coding in feedforward networks with signal convergence and di  (1 cites)
- Decision: ___________

**198.** conf=0.715 title=1.00 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2024] Profiling presynaptic scaffolds using split-GFP reconstitution reveals cell-type-specific   (0 cites)
- B #9999: [2025] Profiling presynaptic scaffolds using split-GFP reconstitution reveals cell-type-specific   (0 cites)
- Decision: ___________

**199.** conf=0.715 title=1.00 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2019] Neural circuits in the mouse retina support color vision in the upper visual field  (29 cites)
- B #960: [2020] Neural circuits in the mouse retina support color vision in the upper visual field  (136 cites)
- Decision: ___________

**200.** conf=0.715 title=1.00 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (2 cites)
- B #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (0 cites)
- Decision: ___________

**201.** conf=0.715 title=1.00 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2019] Reconstruction of 1,000 projection neurons reveals new cell types and organization of long  (61 cites)
- B #9999: [2019] Reconstruction of 1,000 Projection Neurons Reveals New Cell Types and Organization of Long  (1 cites)
- Decision: ___________

**202.** conf=0.715 title=1.00 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (2 cites)
- B #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (0 cites)
- Decision: ___________

**203.** conf=0.715 title=0.99 cit=0.47 auth=0.0 `A=preprint`
- A #9999: [2024] Divergent neural circuits for proprioceptive and exteroceptive sensing of the <i>Drosophil  (9 cites)
- B #9999: [2025] Divergent neural circuits for proprioceptive and exteroceptive sensing of the Drosophila l  (18 cites)
- Decision: ___________

**204.** conf=0.714 title=0.99 cit=0.47 auth=0.0 `A=preprint`
- A #9999: [2025] Mating status-dependent dopaminergic modulation of auditory sensory neurons in <i>Drosophi  (0 cites)
- B #9999: [2025] Mating status-dependent dopaminergic modulation of auditory sensory neurons in Drosophila  (0 cites)
- Decision: ___________

**205.** conf=0.714 title=1.00 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2016] Synaptic Transmission Parallels Neuromodulation in a Central Food-Intake Circuit  (12 cites)
- B #789: [2016] Synaptic transmission parallels neuromodulation in a central food-intake circuit  (165 cites)
- Decision: ___________

**206.** conf=0.714 title=1.00 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2022] Sample preparation and warping accuracy for correlative multimodal imaging in the mouse ol  (3 cites)
- B #9999: [2022] Sample Preparation and Warping Accuracy for Correlative Multimodal Imaging in the Mouse Ol  (12 cites)
- Decision: ___________

**207.** conf=0.714 title=0.98 cit=0.48 auth=0.0 `A=preprint`
- A #1361: [2024] A split-GAL4 driver line resource for <i>Drosophila</i> neuron types  (13 cites)
- B #9999: [2025] A split-GAL4 driver line resource for Drosophila neuron types  (0 cites)
- Decision: ___________

**208.** conf=0.714 title=0.98 cit=0.48 auth=0.0 `A=preprint`
- A #1361: [2024] A split-GAL4 driver line resource for <i>Drosophila</i> neuron types  (13 cites)
- B #9999: [2024] A split-GAL4 driver line resource for Drosophila neuron types  (16 cites)
- Decision: ___________

**209.** conf=0.714 title=0.98 cit=0.48 auth=0.0 `A=preprint`
- A #1361: [2024] A split-GAL4 driver line resource for <i>Drosophila</i> neuron types  (13 cites)
- B #9999: [2025] A split-GAL4 driver line resource for Drosophila neuron types  (16 cites)
- Decision: ___________

**210.** conf=0.714 title=1.00 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2023] Mechanism of barotaxis in marine zooplankton  (14 cites)
- B #9999: [2024] Mechanism of barotaxis in marine zooplankton  (5 cites)
- Decision: ___________

**211.** conf=0.713 title=0.99 cit=0.47 auth=0.0 `A=preprint`
- A #9999: [2017] Conserved neural circuit structure across <i>Drosophila</i> larval development revealed by  (1 cites)
- B #965: [2017] Conserved neural circuit structure across Drosophila larval development revealed by compar  (120 cites)
- Decision: ___________

**212.** conf=0.713 title=1.00 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2022] Ultraliser: a framework for creating multiscale, high-fidelity and geometrically realistic  (0 cites)
- B #9999: [2022] Ultraliser: a framework for creating multiscale, high-fidelity and geometrically realistic  (10 cites)
- Decision: ___________

**213.** conf=0.713 title=0.99 cit=0.47 auth=0.0 `A=preprint`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of <i>Drosophila</i> larvae  (1 cites)
- B #9999: [2023] Morphology and ultrastructure of external sense organs of Drosophila larvae  (7 cites)
- Decision: ___________

**214.** conf=0.713 title=1.00 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2024] Heterogeneous and higher-order cortical connectivity undergirds efficient, robust and reli  (12 cites)
- B #9999: [2024] Heterogeneous and higher-order cortical connectivity undergirds efficient, robust, and rel  (9 cites)
- Decision: ___________

**215.** conf=0.713 title=1.00 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2024] Synaptic architecture of a memory engram in the mouse hippocampus  (11 cites)
- B #9999: [2025] Synaptic architecture of a memory engram in the mouse hippocampus  (24 cites)
- Decision: ___________

**216.** conf=0.713 title=1.00 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2018] Image processing and analysis methods for the Adolescent Brain Cognitive Development Study  (134 cites)
- B #9999: [2019] Image processing and analysis methods for the Adolescent Brain Cognitive Development Study  (1102 cites)
- Decision: ___________

**217.** conf=0.713 title=1.00 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2023] Specific configurations of electrical synapses filter sensory information to drive choices  (2 cites)
- B #9999: [2023] Specific Configurations of Electrical Synapses Filter Sensory Information to Drive Choices  (0 cites)
- Decision: ___________

**218.** conf=0.713 title=1.00 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2024] Accelerated protein retention expansion microscopy using microwave radiation  (0 cites)
- B #9999: [2024] Accelerated protein retention expansion microscopy using microwave radiation  (1 cites)
- Decision: ___________

**219.** conf=0.712 title=0.99 cit=0.46 auth=0.0 `A=preprint`
- A #1755: [2023] A comprehensive neuroanatomical survey of the <i>Drosophila</i> Lobula Plate Tangential Ne  (15 cites)
- B #9999: [2024] A comprehensive neuroanatomical survey of the Drosophila Lobula Plate Tangential Neurons w  (12 cites)
- Decision: ___________

**220.** conf=0.712 title=1.00 cit=0.45 auth=0.0 `B=preprint`
- A #859: [2019] Convolutional nets for reconstructing neural circuits from brain images acquired by serial  (59 cites)
- B #9999: [2019] Convolutional nets for reconstructing neural circuits from brain images acquired by serial  (0 cites)
- Decision: ___________

**221.** conf=0.712 title=1.00 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2022] Seg2Link: an efficient and versatile solution for semi-automatic cell segmentation in 3D i  (1 cites)
- B #9999: [2023] Seg2Link: an efficient and versatile solution for semi-automatic cell segmentation in 3D i  (6 cites)
- Decision: ___________

**222.** conf=0.712 title=0.99 cit=0.47 auth=0.0 `A=preprint`
- A #9999: [2022] Homophilic wiring principles underpin neuronal network topology <i>in vitro</i>  (28 cites)
- B #9999: [2025] Homophilic wiring principles underpin neuronal network topology in vitro  (6 cites)
- Decision: ___________

**223.** conf=0.711 title=0.67 cit=0.30 auth=1.0 `A=preprint`
- A #1766: [2020] Towards Reproducible Brain-Wide Association Studies  (216 cites)
- B #713: [2022] Reproducible brain-wide association studies require thousands of individuals  (1930 cites)
- Decision: ___________

**224.** conf=0.711 title=0.99 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2022] The unique synaptic circuitry of specialized olfactory glomeruli in <i>Drosophila melanoga  (2 cites)
- B #9999: [2025] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (0 cites)
- Decision: ___________

**225.** conf=0.711 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] Driver lines for studying associative learning in Drosophila  (15 cites)
- B #9999: [2024] Driver lines for studying associative learning in Drosophila  (11 cites)
- Decision: ___________

**226.** conf=0.711 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] Driver lines for studying associative learning in Drosophila  (15 cites)
- B #9999: [2025] Driver lines for studying associative learning in Drosophila  (4 cites)
- Decision: ___________

**227.** conf=0.711 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] Driver lines for studying associative learning in Drosophila  (15 cites)
- B #9999: [2025] Driver lines for studying associative learning in Drosophila  (0 cites)
- Decision: ___________

**228.** conf=0.711 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] Driver lines for studying associative learning in Drosophila  (15 cites)
- B #9999: [2024] Driver lines for studying associative learning in Drosophila  (1 cites)
- Decision: ___________

**229.** conf=0.710 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] Volume Electron Microscopy Reveals Unique Laminar Synaptic Characteristics in the Human En  (2 cites)
- B #9999: [2025] Volume electron microscopy reveals unique laminar synaptic characteristics in the human en  (2 cites)
- Decision: ___________

**230.** conf=0.710 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2021] A projectome of the bumblebee central complex  (3 cites)
- B #9999: [2021] A projectome of the bumblebee central complex  (73 cites)
- Decision: ___________

**231.** conf=0.710 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #1205: [2024] Whole-body connectome of a segmented annelid larva  (15 cites)
- B #9999: [2024] Whole-body connectome of a segmented annelid larva  (3 cites)
- Decision: ___________

**232.** conf=0.710 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #1883: [2023] Multiplexed volumetric CLEM enabled by antibody derivatives provides new insights into the  (5 cites)
- B #9999: [2023] Multiplexed volumetric CLEM enabled by antibody derivatives provides new insights into the  (0 cites)
- Decision: ___________

**233.** conf=0.709 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2025] Synaptic density and relative connectivity conservation maintain circuit stability across   (0 cites)
- B #9999: [2025] Synaptic density and relative connectivity conservation maintain circuit stability across   (0 cites)
- Decision: ___________

**234.** conf=0.709 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2021] Optical Tissue Clearing Enables Rapid, Precise and Comprehensive Assessment of Three-Dimen  (3 cites)
- B #9999: [2021] Optical tissue clearing enables rapid, precise and comprehensive assessment of three-dimen  (9 cites)
- Decision: ___________

**235.** conf=0.709 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2025] Synaptic density and relative connectivity conservation maintain circuit stability across   (0 cites)
- B #9999: [2025] Synaptic density and relative connectivity conservation maintain circuit stability across   (0 cites)
- Decision: ___________

**236.** conf=0.709 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2020] Optimization of negative stage bias potential for faster imaging in large-scale electron m  (1 cites)
- B #9999: [2021] Optimization of negative stage bias potential for faster imaging in large-scale electron m  (11 cites)
- Decision: ___________

**237.** conf=0.709 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (2 cites)
- B #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (24 cites)
- Decision: ___________

**238.** conf=0.709 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] ElectroPhysiomeGAN: Generation of Biophysical Neuron Model Parameters from Recorded Electr  (0 cites)
- B #9999: [2025] ElectroPhysiomeGAN: Generation of Biophysical Neuron Model Parameters from Recorded Electr  (0 cites)
- Decision: ___________

**239.** conf=0.709 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] Mapping of multiple neurotransmitter receptor subtypes and distinct protein complexes to t  (2 cites)
- B #9999: [2024] Mapping of multiple neurotransmitter receptor subtypes and distinct protein complexes to t  (26 cites)
- Decision: ___________

**240.** conf=0.709 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2025] Emergence of Functional Heart-Brain Circuits in a Vertebrate  (1 cites)
- B #9999: [2025] Emergence of Functional Heart-Brain Circuits in a Vertebrate  (1 cites)
- Decision: ___________

**241.** conf=0.709 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2025] Emergence of Functional Heart-Brain Circuits in a Vertebrate  (1 cites)
- B #9999: [2025] Emergence of Functional Heart-Brain Circuits in a Vertebrate  (0 cites)
- Decision: ___________

**242.** conf=0.709 title=0.98 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2023] A neurotransmitter atlas of <i>C. elegans</i> males and hermaphrodites  (6 cites)
- B #9999: [2024] A neurotransmitter atlas of C. elegans males and hermaphrodites  (2 cites)
- Decision: ___________

**243.** conf=0.709 title=0.98 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2023] A neurotransmitter atlas of <i>C. elegans</i> males and hermaphrodites  (6 cites)
- B #9999: [2024] A neurotransmitter atlas of C. elegans males and hermaphrodites  (20 cites)
- Decision: ___________

**244.** conf=0.709 title=0.99 cit=0.45 auth=0.0 `B=preprint`
- A #9999: [2017] Ciliomotor circuitry underlying whole-body coordination of ciliary activity in the Platyne  (144 cites)
- B #9999: [2017] Ciliomotor circuitry underlying whole-body coordination of ciliary activity in the <i>Plat  (0 cites)
- Decision: ___________

**245.** conf=0.709 title=0.99 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2025] Inhibitory columnar feedback neurons are involved in motion processing in <i>Drosophila</i  (0 cites)
- B #9999: [2025] Inhibitory columnar feedback neurons are involved in motion processing in Drosophila  (0 cites)
- Decision: ___________

**246.** conf=0.709 title=0.99 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2022] The unique synaptic circuitry of specialized olfactory glomeruli in <i>Drosophila melanoga  (2 cites)
- B #9999: [2025] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (1 cites)
- Decision: ___________

**247.** conf=0.709 title=0.99 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2022] The unique synaptic circuitry of specialized olfactory glomeruli in <i>Drosophila melanoga  (2 cites)
- B #9999: [2023] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (5 cites)
- Decision: ___________

**248.** conf=0.709 title=1.00 cit=0.43 auth=0.0 `A=preprint` (one in top 500)
- A #9999: [2019] A Petascale Automated Imaging Pipeline for Mapping Neuronal Circuits with High-throughput   (39 cites)
- B #14: [2020] A petascale automated imaging pipeline for mapping neuronal circuits with high-throughput   (148 cites)
- Decision: ___________

**249.** conf=0.708 title=0.99 cit=0.44 auth=0.0 `A=preprint`
- A #1109: [2023] Systematic annotation of a complete adult male <i>Drosophila</i> nerve cord connectome rev  (35 cites)
- B #9999: [2024] Systematic annotation of a complete adult male Drosophila nerve cord connectome reveals pr  (10 cites)
- Decision: ___________

**250.** conf=0.708 title=1.00 cit=0.43 auth=0.0 `A=preprint` (one in top 500)
- A #9999: [2020] DotMotif: An open-source tool for connectome subgraph isomorphism search and graph queries  (2 cites)
- B #176: [2021] DotMotif: an open-source tool for connectome subgraph isomorphism search and graph queries  (35 cites)
- Decision: ___________

**251.** conf=0.708 title=1.00 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2023] ATUM-Tomo: A multi-scale approach to cellular ultrastructure by combined volume scanning e  (1 cites)
- B #9999: [2023] ATUM-Tomo: A multi-scale approach to cellular ultrastructure by combined volume scanning e  (4 cites)
- Decision: ___________

**252.** conf=0.708 title=1.00 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2022] Rewarding capacity of optogenetically activating a giant GABAergic central-brain interneur  (1 cites)
- B #9999: [2023] Rewarding Capacity of Optogenetically Activating a Giant GABAergic Central-Brain Interneur  (2 cites)
- Decision: ___________

**253.** conf=0.708 title=0.97 cit=0.47 auth=0.0 `B=preprint`
- A #9999: [2018] FluoEM, virtual labeling of axons in three-dimensional electron microscopy data for long-r  (30 cites)
- B #9999: [2018] FluoEM: Virtual labeling of axons in 3-dimensional electron microscopy data for long-range  (1 cites)
- Decision: ___________

**254.** conf=0.708 title=1.00 cit=0.43 auth=0.0 `B=preprint`
- A #630: [2017] Whole-brain serial-section electron microscopy in larval zebrafish  (401 cites)
- B #9999: [2017] Whole-brain serial-section electron microscopy in larval zebrafish  (2 cites)
- Decision: ___________

**255.** conf=0.708 title=0.99 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2024] MetaWorm: An Integrative Data-Driven Model Simulating <i>C. elegans</i> Brain, Body and En  (3 cites)
- B #9999: [2024] MetaWorm: An Integrative Data-Driven Model Simulating C. elegans Brain, Body and Environme  (0 cites)
- Decision: ___________

**256.** conf=0.708 title=0.99 cit=0.44 auth=0.0 `A=preprint`
- A #1137: [2023] Transforming descending input into motor output: An analysis of the <i>Drosophila</i> Male  (38 cites)
- B #9999: [2025] Transforming descending input into motor output: An analysis of the Drosophila Male Adult   (1 cites)
- Decision: ___________

**257.** conf=0.707 title=1.00 cit=0.43 auth=0.0 `B=preprint`
- A #9999: [2018] Guided Proofreading of Automatic Segmentations for Connectomics  (27 cites)
- B #9999: [2017] Guided Proofreading of Automatic Segmentations for Connectomics  (3 cites)
- Decision: ___________

**258.** conf=0.707 title=1.00 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2024] Profiling presynaptic scaffolds using split-GFP reconstitution reveals cell-type-specific   (0 cites)
- B #9999: [2026] Profiling presynaptic scaffolds using split-GFP reconstitution reveals cell-type-specific   (0 cites)
- Decision: ___________

**259.** conf=0.707 title=1.00 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2025] Neural Connectome of the Ctenophore Statocyst  (0 cites)
- B #9999: [2026] Neural Connectome of the Ctenophore Statocyst  (0 cites)
- Decision: ___________

**260.** conf=0.707 title=1.00 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2024] Mitochondria are absent from microglial processes performing surveillance, chemotaxis, and  (1 cites)
- B #9999: [2025] Mitochondria are absent from microglial processes performing surveillance, chemotaxis, and  (2 cites)
- Decision: ___________

**261.** conf=0.707 title=1.00 cit=0.43 auth=0.0 `B=preprint`
- A #9999: [2013] An Open Science Platform for the Next Generation of Data  (3 cites)
- B #9999: [2015] An Open Science Platform for the Next Generation of Data  (0 cites)
- Decision: ___________

**262.** conf=0.707 title=1.00 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2025] Serotonin selectively modulates visual responses of object motion detectors in <i>Drosophi  (1 cites)
- B #9999: [2025] Serotonin selectively modulates visual responses of object motion detectors in <i>Drosophi  (1 cites)
- Decision: ___________

**263.** conf=0.707 title=0.99 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] Four Individually Identified Paired Dopamine Neurons Signal Taste Punishment in Larval <i>  (1 cites)
- B #9999: [2023] Four individually identified paired dopamine neurons signal taste punishment in larval Dro  (3 cites)
- Decision: ___________

**264.** conf=0.706 title=0.99 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2024] Heterogeneous responses to embryonic critical period perturbations within the <i>Drosophil  (2 cites)
- B #9999: [2025] Heterogeneous responses to embryonic critical period perturbations within the Drosophila l  (1 cites)
- Decision: ___________

**265.** conf=0.706 title=0.99 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2024] Heterogeneous responses to embryonic critical period perturbations within the <i>Drosophil  (2 cites)
- B #9999: [2025] Heterogeneous responses to embryonic critical period perturbations within the Drosophila l  (0 cites)
- Decision: ___________

**266.** conf=0.706 title=1.00 cit=0.42 auth=0.0 `A=preprint`
- A #9999: [2024] Deep Neural Networks to Register and Annotate Cells in Moving and Deforming Nervous System  (3 cites)
- B #9999: [2026] Deep neural networks to register and annotate cells in moving and deforming nervous system  (0 cites)
- Decision: ___________

**267.** conf=0.706 title=0.99 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] Four Individually Identified Paired Dopamine Neurons Signal Taste Punishment in Larval <i>  (1 cites)
- B #9999: [2025] Four Individually Identified Paired Dopamine Neurons Signal Taste Punishment in Larval Dro  (0 cites)
- Decision: ___________

**268.** conf=0.706 title=1.00 cit=0.22 auth=1.0 `diff_DOIs` **⚠ BOTH IN TOP 500**
- A #221: [1979] Principles and Techniques of Electron Microscopy: Biological Applications  (1329 cites)
- B #236: [1977] Principles and Techniques of Electron Microscopy: Biological Applications  (389 cites)
- Decision: ___________

**269.** conf=0.705 title=1.00 cit=0.42 auth=0.0 `A=preprint`
- A #9999: [2022] Synaptic wiring motifs in posterior parietal cortex support decision-making  (21 cites)
- B #9999: [2024] Synaptic wiring motifs in posterior parietal cortex support decision-making  (59 cites)
- Decision: ___________

**270.** conf=0.705 title=1.00 cit=0.42 auth=0.0 `A=preprint`
- A #9999: [2025] Connectome-seq: High-throughput Mapping of Neuronal Connectivity at Single-Synapse Resolut  (1 cites)
- B #9999: [2026] Connectome-seq: high-throughput mapping of neuronal connectivity at single-synapse resolut  (0 cites)
- Decision: ___________

**271.** conf=0.705 title=0.99 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of <i>Drosophila</i> larvae  (1 cites)
- B #9999: [2025] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- Decision: ___________

**272.** conf=0.705 title=0.99 cit=0.43 auth=0.0 `A=preprint`
- A #1755: [2023] A comprehensive neuroanatomical survey of the <i>Drosophila</i> Lobula Plate Tangential Ne  (15 cites)
- B #9999: [2024] A comprehensive neuroanatomical survey of the Drosophila Lobula Plate Tangential Neurons w  (2 cites)
- Decision: ___________

**273.** conf=0.704 title=0.98 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] Neural substrates of cold nociception in <i>Drosophila</i> larva  (0 cites)
- B #9999: [2023] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- Decision: ___________

**274.** conf=0.704 title=1.00 cit=0.42 auth=0.0 `A=preprint`
- A #9999: [2024] Enabling Electric Field Model of Microscopically Realistic Brain  (1 cites)
- B #9999: [2024] Enabling electric field model of microscopically realistic brain  (19 cites)
- Decision: ___________

**275.** conf=0.704 title=0.98 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2023] Neural substrates of cold nociception in <i>Drosophila</i> larva  (0 cites)
- B #9999: [2025] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- Decision: ___________

**276.** conf=0.704 title=0.99 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2022] Synchronous multi-segmental activity between metachronal waves controls locomotion speed i  (0 cites)
- B #1875: [2023] Synchronous multi-segmental activity between metachronal waves controls locomotion speed i  (25 cites)
- Decision: ___________

**277.** conf=0.704 title=0.99 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2025] Inhibitory columnar feedback neurons are involved in motion processing in <i>Drosophila</i  (0 cites)
- B #9999: [2026] Inhibitory columnar feedback neurons are involved in motion processing in Drosophila  (0 cites)
- Decision: ___________

**278.** conf=0.704 title=0.99 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2023] Neural circuits underlying context-dependent competition between defensive actions in <i>D  (4 cites)
- B #9999: [2024] Neural circuits underlying context-dependent competition between defensive actions in Dros  (1 cites)
- Decision: ___________

**279.** conf=0.703 title=1.00 cit=0.41 auth=0.0 `A=preprint`
- A #9999: [2023] Hierarchical communities in the larval <i>Drosophila</i> connectome: Links to cellular ann  (1 cites)
- B #9999: [2024] Hierarchical communities in the larval <i>Drosophila</i> connectome: Links to cellular ann  (12 cites)
- Decision: ___________

**280.** conf=0.703 title=1.00 cit=0.41 auth=0.0 `A=preprint`
- A #9999: [2022] Diverse states and stimuli tune olfactory receptor expression levels to modulate food-seek  (6 cites)
- B #1635: [2022] Diverse states and stimuli tune olfactory receptor expression levels to modulate food-seek  (52 cites)
- Decision: ___________

**281.** conf=0.703 title=0.99 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2025] PyReconstruct: A fully opensource, collaborative successor to <i>Reconstruct</i>  (1 cites)
- B #9999: [2025] PyReconstruct: A fully open-source, collaborative successor to Reconstruct  (2 cites)
- Decision: ___________

**282.** conf=0.703 title=0.99 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2024] Inhibitory circuits control leg movements during <i>Drosophila</i> grooming  (1 cites)
- B #9999: [2025] Inhibitory circuits control leg movements during Drosophila grooming  (1 cites)
- Decision: ___________

**283.** conf=0.702 title=1.00 cit=0.41 auth=0.0 `A=preprint`
- A #9999: [2024] Neurons and molecules involved in noxious light sensation in <i>Caenorhabditis elegans</i>  (0 cites)
- B #9999: [2025] Neurons and molecules involved in noxious light sensation in <i>Caenorhabditis elegans</i>  (3 cites)
- Decision: ___________

**284.** conf=0.702 title=1.00 cit=0.41 auth=0.0 `A=preprint`
- A #9999: [2024] A connectome manipulation framework for the systematic and reproducible study of structure  (8 cites)
- B #9999: [2024] A connectome manipulation framework for the systematic and reproducible study of structure  (4 cites)
- Decision: ___________

**285.** conf=0.702 title=0.94 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] Intercellular communication in the brain via dendritic nanotubular network  (1 cites)
- B #9999: [2025] Intercellular communication in the brain through a dendritic nanotubular network  (13 cites)
- Decision: ___________

**286.** conf=0.702 title=0.99 cit=0.43 auth=0.0 `B=preprint` (one in top 500)
- A #227: [2017] The complete connectome of a learning and memory centre in an insect brain  (568 cites)
- B #9999: [2017] The complete connectome of a learning and memory center in an insect brain  (8 cites)
- Decision: ___________

**287.** conf=0.702 title=0.93 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2024] <i>In vivo</i> human neurite exchange imaging (NEXI) at 500 mT/m diffusion gradients  (1 cites)
- B #9999: [2025] <i>In vivo</i> human neurite exchange time imaging at 500 mT/m diffusion gradients  (6 cites)
- Decision: ___________

**288.** conf=0.702 title=0.99 cit=0.42 auth=0.0 `A=preprint`
- A #9999: [2023] Rabies virus-based barcoded neuroanatomy resolved by single-cell RNA and <i>in situ</i> se  (2 cites)
- B #9999: [2023] Rabies virus-based barcoded neuroanatomy resolved by single-cell RNA and in situ sequencin  (17 cites)
- Decision: ___________

**289.** conf=0.702 title=1.00 cit=0.81 auth=0.0 `diff_DOIs`
- A #9999: [2013] Structure and function of complex brain networks.  (634 cites)
- B #9999: [2013] Structure and function of complex brain networks  (855 cites)
- Decision: ___________

**290.** conf=0.701 title=1.00 cit=0.40 auth=0.0 `A=preprint`
- A #9999: [2020] Connectomic analysis reveals an interneuron with an integral role in the retinal circuit f  (3 cites)
- B #9999: [2020] Connectomic analysis reveals an interneuron with an integral role in the retinal circuit f  (30 cites)
- Decision: ___________

**291.** conf=0.701 title=1.00 cit=0.40 auth=0.0 `A=preprint`
- A #9999: [2017] Automated 3D Axonal Morphometry of White Matter  (7 cites)
- B #9999: [2019] Automated 3D Axonal Morphometry of White Matter  (74 cites)
- Decision: ___________

**292.** conf=0.700 title=1.00 cit=0.40 auth=0.0 `B=preprint`
- A #1056: [2021] Learning and Segmenting Dense Voxel Embeddings for 3D Neuron Reconstruction  (31 cites)
- B #9999: [2019] Learning and Segmenting Dense Voxel Embeddings for 3D Neuron Reconstruction  (5 cites)
- Decision: ___________

**293.** conf=0.700 title=1.00 cit=0.40 auth=0.0 `A=preprint`
- A #9999: [2022] Functional imaging and quantification of multi-neuronal olfactory responses in <i>C. elega  (5 cites)
- B #1442: [2023] Functional imaging and quantification of multineuronal olfactory responses in <i>C. elegan  (51 cites)
- Decision: ___________

**294.** conf=0.700 title=1.00 cit=0.40 auth=0.0 `A=preprint`
- A #9999: [2019] Operations Research Methods for Estimating the Population Size of Neuron Types  (1 cites)
- B #9999: [2020] Operations research methods for estimating the population size of neuron types  (11 cites)
- Decision: ___________

**295.** conf=0.700 title=1.00 cit=0.40 auth=0.0 `A=preprint`
- A #9999: [2018] A Data Structure for real-time Aggregation Queries of Big Brain Networks  (2 cites)
- B #9999: [2019] A Data Structure for Real-Time Aggregation Queries of Big Brain Networks  (6 cites)
- Decision: ___________

**296.** conf=0.700 title=1.00 cit=0.40 auth=0.0 `A=preprint`
- A #9999: [2024] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (1 cites)
- B #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (1 cites)
- Decision: ___________

## LIKELY_DUP (443 pairs)

**1.** conf=0.700 title=1.00 cit=0.40 auth=0.0 `B=preprint`
- A #129: [2018] High-precision automated reconstruction of neurons with flood-filling networks  (389 cites)
- B #9999: [2017] High-Precision Automated Reconstruction of Neurons with Flood-filling Networks  (36 cites)
- Decision: ___________

**2.** conf=0.700 title=0.99 cit=0.42 auth=0.0 `A=preprint`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of <i>Drosophila</i> larvae  (1 cites)
- B #9999: [2023] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- Decision: ___________

**3.** conf=0.699 title=0.99 cit=0.41 auth=0.0 `A=preprint`
- A #9999: [2023] Four Individually Identified Paired Dopamine Neurons Signal Taste Punishment in Larval <i>  (1 cites)
- B #9999: [2025] Four individually identified paired dopamine neurons signal taste punishment in larval Dro  (1 cites)
- Decision: ___________

**4.** conf=0.699 title=1.00 cit=0.40 auth=0.0 `A=preprint`
- A #9999: [2018] Verifying, Challenging, and Discovering New Synapses among Fully EM-Reconstructed Neurons   (1 cites)
- B #9999: [2018] Verifying, Challenging, and Discovering New Synapses Among Fully EM-Reconstructed Neurons   (4 cites)
- Decision: ___________

**5.** conf=0.699 title=0.98 cit=0.42 auth=0.0 `A=preprint`
- A #9999: [2023] Neural substrates of cold nociception in <i>Drosophila</i> larva  (0 cites)
- B #9999: [2025] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- Decision: ___________

**6.** conf=0.698 title=0.98 cit=0.42 auth=0.0 `A=preprint`
- A #9999: [2025] Recent social experience alters song behavior in <i>Drosophila</i>  (0 cites)
- B #9999: [2026] Recent social experience alters song behavior in Drosophila  (0 cites)
- Decision: ___________

**7.** conf=0.698 title=1.00 cit=0.39 auth=0.0 `A=preprint`
- A #9999: [2024] Ensemble learning and ground-truth validation of synaptic connectivity inferred from spike  (0 cites)
- B #9999: [2024] Ensemble learning and ground-truth validation of synaptic connectivity inferred from spike  (10 cites)
- Decision: ___________

**8.** conf=0.698 title=1.00 cit=0.19 auth=1.0 `diff_DOIs`
- A #138: [1995] Support-Vector Networks  (32108 cites)
- B #83: [1995] Support-vector networks  (39987 cites)
- Decision: ___________

**9.** conf=0.697 title=0.99 cit=0.41 auth=0.0 `B=preprint`
- A #1950: [2017] Synaptic and peptidergic connectome of a neurosecretory center in the annelid brain  (142 cites)
- B #9999: [2017] Synaptic and peptidergic connectome of a neurosecretory centre in the annelid brain  (5 cites)
- Decision: ___________

**10.** conf=0.697 title=1.00 cit=0.39 auth=0.0 `A=preprint`
- A #9999: [2019] Scaling Distributed Training of Flood-Filling Networks on HPC Infrastructure for Brain Map  (1 cites)
- B #9999: [2019] Scaling Distributed Training of Flood-Filling Networks on HPC Infrastructure for Brain Map  (7 cites)
- Decision: ___________

**11.** conf=0.697 title=1.00 cit=0.39 auth=0.0 `diff_DOIs`
- A #9999: [2021] Leucokinin and Associated Neuropeptides Regulate Multiple Aspects of Physiology and Behavi  (3 cites)
- B #9999: [2021] Leucokinin and Associated Neuropeptides Regulate Multiple Aspects of Physiology and Behavi  (36 cites)
- Decision: ___________

**12.** conf=0.697 title=1.00 cit=0.39 auth=0.0 `A=preprint`
- A #9999: [2023] Hierarchical regulation of functionally antagonistic neuropeptides expressed in a single n  (4 cites)
- B #9999: [2024] Hierarchical regulation of functionally antagonistic neuropeptides expressed in a single n  (13 cites)
- Decision: ___________

**13.** conf=0.697 title=1.00 cit=0.39 auth=0.0 `A=preprint`
- A #9999: [2020] Leveraging Tools from Autonomous Navigation for Rapid, Robust Neuron Connectivity  (1 cites)
- B #9999: [2020] Leveraging Tools from Autonomous Navigation for Rapid, Robust Neuron Connectivity  (1 cites)
- Decision: ___________

**14.** conf=0.697 title=1.00 cit=0.39 auth=0.0 `A=preprint`
- A #9999: [2023] OME-Zarr: a cloud-optimized bioimaging file format with international community support  (22 cites)
- B #1608: [2023] OME-Zarr: a cloud-optimized bioimaging file format with international community support  (108 cites)
- Decision: ___________

**15.** conf=0.697 title=1.00 cit=0.39 auth=0.0 `A=preprint`
- A #9999: [2019] The neuroanatomical ultrastructure and function of a biological ring attractor  (34 cites)
- B #313: [2020] The Neuroanatomical Ultrastructure and Function of a Biological Ring Attractor  (163 cites)
- Decision: ___________

**16.** conf=0.697 title=0.94 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2023] Neural mechanisms to incorporate visual counterevidence in self motion estimation  (3 cites)
- B #9999: [2023] Neural mechanisms to incorporate visual counterevidence in self-movement estimation  (5 cites)
- Decision: ___________

**17.** conf=0.696 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2024] Efficient cell-wide mapping of mitochondria in electron microscopic volumes using webKnoss  (0 cites)
- B #9999: [2024] Efficient Cell-Wide Mapping of Mitochondria in Electron Microscopic Volumes Using webKnoss  (0 cites)
- Decision: ___________

**18.** conf=0.696 title=0.98 cit=0.41 auth=0.0 `A=preprint`
- A #9999: [2023] Neural substrates of cold nociception in <i>Drosophila</i> larva  (0 cites)
- B #9999: [2023] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- Decision: ___________

**19.** conf=0.696 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2025] Emergence of clustered synapses during the development of a nervous system  (0 cites)
- B #9999: [2026] Emergence of clustered synapses during the development of a nervous system  (0 cites)
- Decision: ___________

**20.** conf=0.695 title=1.00 cit=0.18 auth=1.0 `diff_DOIs`
- A #307: [1987] Marching cubes: A high resolution 3D surface construction algorithm  (10126 cites)
- B #623: [1987] Marching cubes: A high resolution 3D surface construction algorithm  (8453 cites)
- Decision: ___________

**21.** conf=0.695 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2020] nAdder: A scale-space approach for the 3D analysis of neuronal traces  (2 cites)
- B #9999: [2022] nAdder: A scale-space approach for the 3D analysis of neuronal traces  (1 cites)
- Decision: ___________

**22.** conf=0.695 title=1.00 cit=0.38 auth=0.0 `B=preprint`
- A #594: [2017] SynEM, automated synapse detection for connectomics  (71 cites)
- B #9999: [2017] SynEM: Automated synapse detection for connectomics  (3 cites)
- Decision: ___________

**23.** conf=0.695 title=0.99 cit=0.40 auth=0.0 `A=preprint`
- A #9999: [2023] Neural circuits underlying context-dependent competition between defensive actions in <i>D  (4 cites)
- B #9999: [2025] Neural circuits underlying context-dependent competition between defensive actions in Dros  (5 cites)
- Decision: ___________

**24.** conf=0.695 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2022] Generative network modeling reveals quantitative definitions of bilateral symmetry exhibit  (0 cites)
- B #113: [2023] Generative network modeling reveals quantitative definitions of bilateral symmetry exhibit  (12 cites)
- Decision: ___________

**25.** conf=0.694 title=0.98 cit=0.40 auth=0.0 `A=preprint`
- A #9999: [2020] Synaptic counts approximate synaptic contact area in <i>Drosophila</i>  (5 cites)
- B #651: [2022] Synaptic counts approximate synaptic contact area in Drosophila  (30 cites)
- Decision: ___________

**26.** conf=0.694 title=0.99 cit=0.39 auth=0.0 `A=preprint`
- A #9999: [2021] Synaptic targets of photoreceptors specialized to detect color and skylight polarization i  (1 cites)
- B #599: [2021] Synaptic targets of photoreceptors specialized to detect color and skylight polarization i  (72 cites)
- Decision: ___________

**27.** conf=0.694 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2024] niiv: Interactive Self-supervised Neural Implicit Isotropic Volume Reconstruction  (2 cites)
- B #9999: [2026] niiv: Interactive Self-supervised Neural Implicit Isotropic Volume Reconstruction  (0 cites)
- Decision: ___________

**28.** conf=0.694 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2025] Neural Connectome of the Ctenophore Statocyst  (0 cites)
- B #9999: [2025] Neural Connectome of the Ctenophore Statocyst  (1 cites)
- Decision: ___________

**29.** conf=0.694 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2023] Femtosecond laser preparation of resin embedded samples for correlative microscopy workflo  (1 cites)
- B #9999: [2023] Femtosecond laser preparation of resin embedded samples for correlative microscopy workflo  (10 cites)
- Decision: ___________

**30.** conf=0.694 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2023] Permanent deconstruction of intracellular primary cilia in differentiating granule cell ne  (2 cites)
- B #1977: [2024] Permanent deconstruction of intracellular primary cilia in differentiating granule cell ne  (22 cites)
- Decision: ___________

**31.** conf=0.694 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2021] A simple and robust method for automating analysis of naïve and regenerating peripheral ne  (3 cites)
- B #9999: [2021] A simple and robust method for automating analysis of naïve and regenerating peripheral ne  (11 cites)
- Decision: ___________

**32.** conf=0.694 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2023] Mechanism of barotaxis in marine zooplankton  (14 cites)
- B #9999: [2024] Mechanism of barotaxis in marine zooplankton  (0 cites)
- Decision: ___________

**33.** conf=0.694 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2024] Adjacent Neuronal Fascicle Guides Motoneuron 24 Dendritic Branching and Axonal Routing Dec  (1 cites)
- B #9999: [2024] Adjacent Neuronal Fascicle Guides Motoneuron 24 Dendritic Branching and Axonal Routing Dec  (1 cites)
- Decision: ___________

**34.** conf=0.694 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2018] Open Source Brain: a collaborative resource for visualizing, analyzing, simulating and dev  (17 cites)
- B #9999: [2019] Open Source Brain: A Collaborative Resource for Visualizing, Analyzing, Simulating, and De  (86 cites)
- Decision: ___________

**35.** conf=0.694 title=1.00 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2025] Neural Connectome of the Ctenophore Statocyst  (0 cites)
- B #9999: [2025] Neural connectome of the ctenophore statocyst  (3 cites)
- Decision: ___________

**36.** conf=0.693 title=0.91 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2025] Neurons exploit stochastic growth to rapidly and economically build dense radially oriente  (1 cites)
- B #9999: [2025] Neurons exploit stochastic growth to rapidly and economically build dense dendritic arbors  (4 cites)
- Decision: ___________

**37.** conf=0.693 title=0.99 cit=0.39 auth=0.0 `A=preprint`
- A #1979: [2022] Mating activates neuroendocrine pathways signaling hunger in <i>Drosophila</i> females  (8 cites)
- B #9999: [2023] Mating activates neuroendocrine pathways signaling hunger in Drosophila females  (29 cites)
- Decision: ___________

**38.** conf=0.692 title=0.96 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2021] Rapid reconstruction of neural circuits using tissue expansion and lattice light sheet mic  (8 cites)
- B #597: [2022] Rapid reconstruction of neural circuits using tissue expansion and light sheet microscopy  (61 cites)
- Decision: ___________

**39.** conf=0.692 title=0.99 cit=0.39 auth=0.0 `A=preprint`
- A #9999: [2018] An unbiased template of the <i>Drosophila</i> brain and ventral nerve cord  (20 cites)
- B #56: [2020] An unbiased template of the Drosophila brain and ventral nerve cord  (154 cites)
- Decision: ___________

**40.** conf=0.692 title=0.98 cit=0.40 auth=0.0 `A=preprint`
- A #9999: [2023] Dissecting the Functional Organization of the <i>C. elegans</i> Serotonergic System at Who  (2 cites)
- B #1518: [2023] Dissecting the functional organization of the C. elegans serotonergic system at whole-brai  (68 cites)
- Decision: ___________

**41.** conf=0.691 title=1.00 cit=0.37 auth=0.0 `A=preprint`
- A #9999: [2018] Dense connectomic reconstruction in layer 4 of the somatosensory cortex  (48 cites)
- B #325: [2019] Dense connectomic reconstruction in layer 4 of the somatosensory cortex  (354 cites)
- Decision: ___________

**42.** conf=0.691 title=1.00 cit=0.36 auth=0.0 `A=preprint`
- A #9999: [2025] Synaptic Targets of Circadian Clock Neurons Influence Core Clock Parameters  (0 cites)
- B #9999: [2025] Synaptic targets of circadian clock neurons influence core clock parameters  (1 cites)
- Decision: ___________

**43.** conf=0.690 title=0.99 cit=0.37 auth=0.0 `A=preprint`
- A #9999: [2016] Genetically targeted 3D visualisation of <i>Drosophila</i> neurons under Electron Microsco  (0 cites)
- B #9999: [2016] Genetically targeted 3D visualisation of Drosophila neurons under Electron Microscopy and   (36 cites)
- Decision: ___________

**44.** conf=0.690 title=1.00 cit=0.36 auth=0.0 `A=preprint`
- A #9999: [2021] VICE: Visual Identification and Correction of Neural Circuit Errors  (1 cites)
- B #9999: [2021] VICE: Visual Identification and Correction of Neural Circuit Errors  (10 cites)
- Decision: ___________

**45.** conf=0.690 title=0.99 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2023] Evolution of chemosensory tissues and cells across ecologically diverse <i>Drosophilids</i  (2 cites)
- B #9999: [2024] Evolution of chemosensory tissues and cells across ecologically diverse Drosophilids  (21 cites)
- Decision: ___________

**46.** conf=0.689 title=1.00 cit=0.36 auth=0.0 `A=preprint`
- A #9999: [2016] Functional Genetic Screen to Identify Interneurons Governing Behaviorally Distinct Aspects  (1 cites)
- B #9999: [2016] Functional Genetic Screen to Identify Interneurons Governing Behaviorally Distinct Aspects  (29 cites)
- Decision: ___________

**47.** conf=0.689 title=1.00 cit=0.36 auth=0.0 `A=preprint`
- A #9999: [2021] Desmosomal connectomics of all somatic muscles in an annelid larva  (0 cites)
- B #1594: [2022] Desmosomal connectomics of all somatic muscles in an annelid larva  (14 cites)
- Decision: ___________

**48.** conf=0.689 title=0.99 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of <i>Drosophila</i> larvae  (0 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of Drosophila larvae  (0 cites)
- Decision: ___________

**49.** conf=0.689 title=0.99 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of <i>Drosophila</i> larvae  (0 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of Drosophila larvae  (0 cites)
- Decision: ___________

**50.** conf=0.689 title=0.99 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2023] Conserved autism-associated genes tune social feeding behavior in <i>C. elegans</i>  (0 cites)
- B #9999: [2024] Conserved autism-associated genes tune social feeding behavior in C. elegans  (16 cites)
- Decision: ___________

**51.** conf=0.689 title=0.71 cit=0.16 auth=1.0 `A=preprint`
- A #547: [2023] Connectome-constrained deep mechanistic networks predict neural responses across the fly v  (29 cites)
- B #663: [2024] Connectome-constrained networks predict neural activity across the fly visual system  (83 cites)
- Decision: ___________

**52.** conf=0.689 title=0.97 cit=0.40 auth=0.0 `A=preprint`
- A #9999: [2022] Neuronal contact predicts connectivity in the <i>C. elegans</i> brain  (0 cites)
- B #1375: [2023] Neuronal contact predicts connectivity in the C. elegans brain  (35 cites)
- Decision: ___________

**53.** conf=0.688 title=0.98 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2021] Learning accurate path integration in a ring attractor model of the head direction system  (1 cites)
- B #9999: [2022] Learning accurate path integration in ring attractor models of the head direction system  (24 cites)
- Decision: ___________

**54.** conf=0.688 title=0.99 cit=0.36 auth=0.0 `A=preprint`
- A #9999: [2023] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (0 cites)
- B #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (5 cites)
- Decision: ___________

**55.** conf=0.687 title=1.00 cit=0.35 auth=0.0 `B=preprint`
- A #1710: [2016] Connectivity map of bipolar cells and photoreceptors in the mouse retina  (194 cites)
- B #9999: [2016] Connectivity map of bipolar cells and photoreceptors in the mouse retina  (9 cites)
- Decision: ___________

**56.** conf=0.686 title=0.93 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2024] Asymmetry in synaptic connectivity balances redundancy and reachability in the <i>C. elega  (0 cites)
- B #9999: [2024] Asymmetry in synaptic connectivity balances redundancy and reachability in the Caenorhabdi  (0 cites)
- Decision: ___________

**57.** conf=0.686 title=1.00 cit=0.34 auth=0.0 `A=preprint`
- A #9999: [2023] Three-dimensional reconstructions of mechanosensory end organs suggest a unifying mechanis  (9 cites)
- B #1995: [2023] Three-dimensional reconstructions of mechanosensory end organs suggest a unifying mechanis  (47 cites)
- Decision: ___________

**58.** conf=0.686 title=1.00 cit=0.34 auth=0.0 `A=preprint`
- A #9999: [2025] MoMo - Combining Neuron Morphology and Connectivity for Interactive Motif Analysis in Conn  (0 cites)
- B #9999: [2025] MoMo - Combining Neuron Morphology and Connectivity for Interactive Motif Analysis in Conn  (0 cites)
- Decision: ___________

**59.** conf=0.686 title=1.00 cit=0.34 auth=0.0 `A=preprint`
- A #9999: [2024] Scaling Properties for Artificial Neural Network Models of a Small Nervous System  (0 cites)
- B #9999: [2024] Scaling Properties for Artificial Neural Network Models of a Small Nervous System  (0 cites)
- Decision: ___________

**60.** conf=0.686 title=1.00 cit=0.34 auth=0.0 `A=preprint`
- A #9999: [2023] Structure, interaction, and nervous connectivity of beta cell primary cilia  (10 cites)
- B #9999: [2024] Structure, interaction and nervous connectivity of beta cell primary cilia  (16 cites)
- Decision: ___________

**61.** conf=0.685 title=1.00 cit=0.34 auth=0.0 `A=preprint`
- A #9999: [2025] Infrequent strong connections constrain connectomic predictions of neuronal function  (2 cites)
- B #9999: [2025] Infrequent strong connections constrain connectomic predictions of neuronal function  (7 cites)
- Decision: ___________

**62.** conf=0.685 title=0.99 cit=0.36 auth=0.0 `A=preprint`
- A #9999: [2025] Polyadic synapses introduce unique wiring architectures in T5 cells of <i>Drosophila</i>  (0 cites)
- B #9999: [2025] Polyadic synapses introduce unique wiring architectures in T5 cells of Drosophila  (0 cites)
- Decision: ___________

**63.** conf=0.685 title=1.00 cit=0.34 auth=0.0 `A=preprint`
- A #9999: [2024] Dense, Continuous Membrane Labeling and Expansion Microscopy Visualization of Ultrastructu  (6 cites)
- B #9999: [2025] Dense, continuous membrane labeling and expansion microscopy visualization of ultrastructu  (12 cites)
- Decision: ___________

**64.** conf=0.684 title=0.92 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2024] Statistical signature of subtle behavioural changes in large-scale behavioural assays  (1 cites)
- B #9999: [2025] Statistical signature of subtle behavioral changes in large-scale assays  (2 cites)
- Decision: ___________

**65.** conf=0.683 title=1.00 cit=0.33 auth=0.0 `B=preprint`
- A #9999: [2016] Deep learning in bioinformatics  (1518 cites)
- B #9999: [2016] Deep Learning in Bioinformatics  (21 cites)
- Decision: ___________

**66.** conf=0.683 title=1.00 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2025] PRMix: Primary Region Mix Augmentation and Benchmark Dataset for Precise Whole Mouse Brain  (1 cites)
- B #9999: [2026] PRMix: Primary Region Mix Augmentation and Benchmark Dataset for Precise Whole Mouse Brain  (0 cites)
- Decision: ___________

**67.** conf=0.683 title=1.00 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2025] Conservation and diversification of mating behavior patterns among three sibling species i  (1 cites)
- B #9999: [2025] Conservation and diversification of mating behavior patterns among three sibling species i  (0 cites)
- Decision: ___________

**68.** conf=0.683 title=1.00 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2018] Threat of Adversarial Attacks on Deep Learning in Computer Vision: A Survey  (168 cites)
- B #1827: [2018] Threat of Adversarial Attacks on Deep Learning in Computer Vision: A Survey  (2012 cites)
- Decision: ___________

**69.** conf=0.683 title=1.00 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2022] Descending neuron population dynamics during odor-evoked and spontaneous limb-dependent be  (0 cites)
- B #1606: [2022] Descending neuron population dynamics during odor-evoked and spontaneous limb-dependent be  (44 cites)
- Decision: ___________

**70.** conf=0.683 title=1.00 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2025] RETINA: Reconstruction-based Pre-Trained Enhanced TransUNet for Electron Microscopy Segmen  (0 cites)
- B #9999: [2025] RETINA: Reconstruction-based pre-trained enhanced TransUNet for electron microscopy segmen  (3 cites)
- Decision: ___________

**71.** conf=0.683 title=1.00 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2024] Differential temporal filtering in the fly optic lobe  (0 cites)
- B #9999: [2025] Differential temporal filtering in the fly optic lobe  (0 cites)
- Decision: ___________

**72.** conf=0.683 title=1.00 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2023] Noise-induced synaptopathy impacts the long and short sensory hair cells differently in th  (0 cites)
- B #9999: [2023] Noise-Induced Synaptopathy Impacts the Long and Short Sensory Hair Cells Differently in th  (0 cites)
- Decision: ___________

**73.** conf=0.683 title=0.99 cit=0.35 auth=0.0 `A=preprint`
- A #9999: [2021] Extrasynaptic signaling enables an asymmetric juvenile motor circuit to produce a symmetri  (1 cites)
- B #1737: [2022] Extrasynaptic signaling enables an asymmetric juvenile motor circuit to produce symmetric   (28 cites)
- Decision: ___________

**74.** conf=0.682 title=0.99 cit=0.34 auth=0.0 `A=preprint`
- A #9999: [2025] Peripheral anatomy and central connectivity of proprioceptive sensory neurons in the <i>Dr  (1 cites)
- B #9999: [2026] Peripheral anatomy and central connectivity of proprioceptive sensory neurons in the Droso  (0 cites)
- Decision: ___________

**75.** conf=0.681 title=0.98 cit=0.35 auth=0.0 `A=preprint`
- A #9999: [2025] A High-Resolution Atlas of the Brain Predicts Lineage and Birth Order Underly Neuronal Ide  (2 cites)
- B #9999: [2025] A high-resolution atlas of the brain predicts lineage and birth order underlying neuronal   (3 cites)
- Decision: ___________

**76.** conf=0.680 title=1.00 cit=0.32 auth=0.0 `A=preprint`
- A #9999: [2022] A tonically active master neuron modulates mutually exclusive motor states at two timescal  (2 cites)
- B #9999: [2024] A tonically active master neuron modulates mutually exclusive motor states at two timescal  (19 cites)
- Decision: ___________

**77.** conf=0.680 title=1.00 cit=0.32 auth=0.0 `A=preprint`
- A #9999: [2022] Generating parallel representations of position and identity in the olfactory system  (10 cites)
- B #1730: [2023] Generating parallel representations of position and identity in the olfactory system  (71 cites)
- Decision: ___________

**78.** conf=0.680 title=0.99 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2022] Heterogeneous Receptor Expression Underlies Non-uniform Peptidergic Modulation of Olfactio  (2 cites)
- B #9999: [2023] Heterogeneous receptor expression underlies non-uniform peptidergic modulation of olfactio  (14 cites)
- Decision: ___________

**79.** conf=0.680 title=1.00 cit=0.32 auth=0.0 `A=preprint`
- A #9999: [2021] Analysis of Rod/Cone Gap Junctions from the Reconstruction of Mouse Photoreceptor Terminal  (0 cites)
- B #9999: [2022] Analysis of rod/cone gap junctions from the reconstruction of mouse photoreceptor terminal  (29 cites)
- Decision: ___________

**80.** conf=0.680 title=1.00 cit=0.32 auth=0.0 `A=preprint`
- A #9999: [2024] Prediction of neural activity in connectome-constrained recurrent networks  (2 cites)
- B #9999: [2025] Prediction of neural activity in connectome-constrained recurrent networks  (3 cites)
- Decision: ___________

**81.** conf=0.680 title=1.00 cit=0.32 auth=0.0 `A=preprint`
- A #9999: [2024] Daily ultrastructural remodeling of clock neurons  (3 cites)
- B #9999: [2025] Daily ultrastructural remodeling of clock neurons  (1 cites)
- Decision: ___________

**82.** conf=0.680 title=1.00 cit=0.32 auth=0.0 `A=preprint`
- A #9999: [2022] Presynaptic contact and activity opposingly regulate postsynaptic dendrite outgrowth  (1 cites)
- B #9999: [2022] Presynaptic contact and activity opposingly regulate postsynaptic dendrite outgrowth  (14 cites)
- Decision: ___________

**83.** conf=0.680 title=1.00 cit=0.32 auth=0.0 `A=preprint`
- A #9999: [2022] Flexible specificity of memory in Drosophila depends on a comparison between choices  (0 cites)
- B #9999: [2023] Flexible specificity of memory in Drosophila depends on a comparison between choices  (5 cites)
- Decision: ___________

**84.** conf=0.679 title=1.00 cit=0.32 auth=0.0 `A=preprint`
- A #9999: [2022] Taste quality and hunger interactions in a feeding sensorimotor circuit  (7 cites)
- B #1193: [2022] Taste quality and hunger interactions in a feeding sensorimotor circuit  (60 cites)
- Decision: ___________

**85.** conf=0.679 title=0.98 cit=0.34 auth=0.0 `A=preprint`
- A #9999: [2020] Transsynaptic mapping of <i>Drosophila</i> mushroom body output neurons  (3 cites)
- B #1429: [2021] Transsynaptic mapping of Drosophila mushroom body output neurons  (62 cites)
- Decision: ___________

**86.** conf=0.679 title=1.00 cit=0.32 auth=0.0 `A=preprint`
- A #9999: [2020] Accurate and Versatile 3D Segmentation of Plant Tissues at Cellular Resolution  (14 cites)
- B #722: [2020] Accurate and versatile 3D segmentation of plant tissues at cellular resolution  (323 cites)
- Decision: ___________

**87.** conf=0.679 title=0.92 cit=0.42 auth=0.0 `A=preprint`
- A #9999: [2021] The anterior paired lateral neuron normalizes odour-evoked activity at the mushroom body c  (0 cites)
- B #9999: [2021] The anterior paired lateral neuron normalizes odour-evoked activity in the Drosophila mush  (18 cites)
- Decision: ___________

**88.** conf=0.678 title=0.90 cit=0.45 auth=0.0 `A=preprint`
- A #9999: [2025] Inhibitory columnar feedback neurons are involved in motion processing in <i>Drosophila</i  (0 cites)
- B #9999: [2025] Inhibitory columnar feedback neurons are required for motion processing in Drosophila  (1 cites)
- Decision: ___________

**89.** conf=0.677 title=0.99 cit=0.32 auth=0.0 `A=preprint`
- A #9999: [2017] Communication from learned to innate olfactory processing centers is required for memory r  (10 cites)
- B #1483: [2018] Communication from Learned to Innate Olfactory Processing Centers Is Required for Memory R  (124 cites)
- Decision: ___________

**90.** conf=0.677 title=1.00 cit=0.31 auth=0.0 `A=preprint`
- A #9999: [2024] Finding a path: Local search behavior of <i>Drosophila</i> larvae  (1 cites)
- B #9999: [2025] Finding a path: local search behavior of <i>Drosophila</i> larvae  (0 cites)
- Decision: ___________

**91.** conf=0.677 title=1.00 cit=0.31 auth=0.0 `A=preprint`
- A #9999: [2021] Decoding gene regulation in the fly brain  (11 cites)
- B #1999: [2022] Decoding gene regulation in the fly brain  (185 cites)
- Decision: ___________

**92.** conf=0.677 title=0.99 cit=0.32 auth=0.0 `A=preprint`
- A #9999: [2023] Ultrastructural analysis reveals mitochondrial placement independent of synapse placement   (1 cites)
- B #9999: [2024] Ultrastructural Analysis Reveals Mitochondrial Placement Independent of Synapse Placement   (2 cites)
- Decision: ___________

**93.** conf=0.676 title=1.00 cit=0.30 auth=0.0 `A=preprint`
- A #9999: [2023] Segment Anything for Microscopy  (63 cites)
- B #9999: [2025] Segment Anything for Microscopy  (144 cites)
- Decision: ___________

**94.** conf=0.676 title=1.00 cit=0.30 auth=0.0 `A=preprint`
- A #9999: [2025] Specialized parallel pathways for adaptive control of visual object pursuit  (3 cites)
- B #9999: [2026] Specialized parallel pathways for adaptive control of visual object pursuit  (0 cites)
- Decision: ___________

**95.** conf=0.675 title=0.95 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2022] The synaptic organization in the <i>C. elegans</i> neural network suggests significant loc  (0 cites)
- B #9999: [2023] The synaptic organization in the <i>Caenorhabditis elegans</i> neural network suggests sig  (12 cites)
- Decision: ___________

**96.** conf=0.675 title=1.00 cit=0.30 auth=0.0 `A=preprint`
- A #9999: [2024] Cascades and convergence: dynamic signal flow in a synapse-level brain network  (1 cites)
- B #9999: [2026] Cascades and convergence: Dynamic signal flow in a synapse-level brain network  (0 cites)
- Decision: ___________

**97.** conf=0.675 title=1.00 cit=0.30 auth=0.0 `A=preprint`
- A #9999: [2020] Electron Microscopic Reconstruction of Neural Circuitry in the Cochlea  (3 cites)
- B #567: [2021] Electron Microscopic Reconstruction of Neural Circuitry in the Cochlea  (73 cites)
- Decision: ___________

**98.** conf=0.675 title=1.00 cit=0.30 auth=0.0 `A=preprint`
- A #9999: [2022] MoBIE: A Fiji plugin for sharing and exploration of multi-modal cloud-hosted big image dat  (9 cites)
- B #1364: [2023] MoBIE: a Fiji plugin for sharing and exploration of multi-modal cloud-hosted big image dat  (33 cites)
- Decision: ___________

**99.** conf=0.674 title=0.90 cit=0.43 auth=0.0 `A=preprint`
- A #9999: [2021] Neuronal circuits integrating visual motion information in <i>Drosophila</i>  (0 cites)
- B #596: [2022] Neuronal circuits integrating visual motion information in Drosophila melanogaster  (65 cites)
- Decision: ___________

**100.** conf=0.674 title=1.00 cit=0.69 auth=0.0 `diff_DOIs`
- A #1272: [2011] Focussed Ion Beam Milling and Scanning Electron Microscopy of Brain Tissue  (104 cites)
- B #9999: [2011] Focussed Ion Beam Milling and Scanning Electron Microscopy of Brain Tissue  (31 cites)
- Decision: ___________

**101.** conf=0.674 title=0.99 cit=0.31 auth=0.0 `A=preprint`
- A #9999: [2021] Stereotyped Behavioral Maturation and Rhythmic Quiescence in <i>C. elegans</i> Embryos  (0 cites)
- B #9999: [2022] Stereotyped behavioral maturation and rhythmic quiescence in C. elegans embryos  (11 cites)
- Decision: ___________

**102.** conf=0.673 title=0.92 cit=0.41 auth=0.0 `A=preprint`
- A #9999: [2023] TWISP: A Transgenic Worm for Interrogating Signal Propagation in <i>C. elegans</i>  (1 cites)
- B #1846: [2024] TWISP: a transgenic worm for interrogating signal propagation in <i>Caenorhabditis elegans  (6 cites)
- Decision: ___________

**103.** conf=0.673 title=0.95 cit=0.36 auth=0.0 `A=preprint`
- A #9999: [2021] Extrasynaptic signaling enables an asymmetric juvenile motor circuit to produce a symmetri  (1 cites)
- B #9999: [2021] Extrasynaptic Signaling Enables an Asymmetric Juvenile Motor Circuit to Produce a Symmetri  (0 cites)
- Decision: ___________

**104.** conf=0.673 title=1.00 cit=0.69 auth=0.0 `diff_DOIs`
- A #9999: [2023] Atlas of Plasmodium falciparum intraerythrocytic development using expansion microscopy  (64 cites)
- B #9999: [2023] Atlas of Plasmodium falciparum intraerythrocytic development using expansion microscopy  (63 cites)
- Decision: ___________

**105.** conf=0.672 title=0.99 cit=0.30 auth=0.0 `A=preprint`
- A #9999: [2018] Developmentally arrested precursors of pontine neurons establish an embryonic blueprint of  (0 cites)
- B #9999: [2019] Developmentally Arrested Precursors of Pontine Neurons Establish an Embryonic Blueprint of  (44 cites)
- Decision: ___________

**106.** conf=0.672 title=0.99 cit=0.30 auth=0.0 `A=preprint`
- A #9999: [2024] Nervous system-wide analysis of all C. elegans cadherins reveals neuron-specific functions  (1 cites)
- B #9999: [2025] Nervous system–wide analysis of all <i>C. elegans</i> cadherins reveals neuron-specific fu  (9 cites)
- Decision: ___________

**107.** conf=0.672 title=0.98 cit=0.31 auth=0.0 `A=preprint`
- A #1835: [2022] Eye structure shapes neuron function in <i>Drosophila</i> motion vision  (30 cites)
- B #9999: [2025] Eye structure shapes neuron function in Drosophila motion vision  (8 cites)
- Decision: ___________

**108.** conf=0.671 title=1.00 cit=0.29 auth=0.0 `A=preprint`
- A #9999: [2024] Ultrastructural membrane dynamics of mouse and human cortical synapses  (1 cites)
- B #9999: [2025] Ultrastructural membrane dynamics of mouse and human cortical synapses  (1 cites)
- Decision: ___________

**109.** conf=0.671 title=0.98 cit=0.31 auth=0.0 `A=preprint`
- A #1144: [2023] A Connectome of the Male <i>Drosophila</i> Ventral Nerve Cord  (58 cites)
- B #9999: [2024] A Connectome of the Male Drosophila Ventral Nerve Cord  (15 cites)
- Decision: ___________

**110.** conf=0.670 title=0.90 cit=0.42 auth=0.0 `A=preprint`
- A #9999: [2021] Dendro-somatic synaptic inputs to ganglion cells violate receptive field and connectivity   (0 cites)
- B #9999: [2021] Dendro-somatic synaptic inputs to ganglion cells contradict receptive field and connectivi  (16 cites)
- Decision: ___________

**111.** conf=0.670 title=0.94 cit=0.36 auth=0.0 `diff_DOIs`
- A #9999: [2019] Leveraging Domain Knowledge to improve EM image segmentation with Lifted Multicuts.  (1 cites)
- B #9999: [2019] Leveraging Domain Knowledge to Improve Microscopy Image Segmentation With Lifted Multicuts  (1 cites)
- Decision: ___________

**112.** conf=0.669 title=1.00 cit=0.28 auth=0.0 `A=preprint`
- A #9999: [2025] Relative value learning in <i>Drosophila melanogaster</i> larvae  (1 cites)
- B #9999: [2026] Relative value learning in <i>Drosophila melanogaster</i> larvae  (0 cites)
- Decision: ___________

**113.** conf=0.668 title=0.77 cit=0.40 auth=1.0 `diff_DOIs`
- A #1813: [2024] Transforming descending input into motor output: An analysis of the Drosophila Male Adult   (20 cites)
- B #1511: [2024] Transforming descending input into behavior: The organization of premotor circuits in the   (45 cites)
- Decision: ___________

**114.** conf=0.668 title=1.00 cit=0.27 auth=0.0 `A=preprint`
- A #9999: [2019] Dense neuronal reconstruction through X-ray holographic nano-tomography  (12 cites)
- B #144: [2020] Dense neuronal reconstruction through X-ray holographic nano-tomography  (157 cites)
- Decision: ___________

**115.** conf=0.667 title=1.00 cit=0.27 auth=0.0 `A=preprint`
- A #9999: [2023] Unveiling the Odor Representation in the Inner Brain of <i>Drosophila</i> through Compress  (0 cites)
- B #9999: [2024] Unveiling the odor representation in the inner brain of <i>Drosophila</i> through compress  (0 cites)
- Decision: ___________

**116.** conf=0.667 title=1.00 cit=0.27 auth=0.0 `A=preprint`
- A #9999: [2018] Neural circuitry of a polycystin-mediated hydrodynamic startle response for predator avoid  (5 cites)
- B #9999: [2018] Neural circuitry of a polycystin-mediated hydrodynamic startle response for predator avoid  (91 cites)
- Decision: ___________

**117.** conf=0.667 title=0.99 cit=0.28 auth=0.0 `A=preprint`
- A #831: [2024] Anti-diuretic hormone ITP signals via a guanylate cyclase receptor to modulate systemic ho  (3 cites)
- B #9999: [2025] Anti-diuretic hormone ITP signals via a guanylate cyclase receptor to modulate systemic ho  (0 cites)
- Decision: ___________

**118.** conf=0.666 title=1.00 cit=0.26 auth=0.0 `A=preprint`
- A #9999: [2020] Click-ExM enables expansion microscopy for all biomolecules  (19 cites)
- B #840: [2020] Click-ExM enables expansion microscopy for all biomolecules  (164 cites)
- Decision: ___________

**119.** conf=0.664 title=0.88 cit=0.42 auth=0.0 `A=preprint`
- A #9999: [2022] Instance segmentation of mitochondria in electron microscopy images with a generalist deep  (9 cites)
- B #1383: [2023] Instance segmentation of mitochondria in electron microscopy images with a generalist deep  (101 cites)
- Decision: ___________

**120.** conf=0.662 title=1.00 cit=0.25 auth=0.0 `B=preprint`
- A #9999: [2017] Quantifying Mesoscale Neuroanatomy Using X-Ray Microtomography  (99 cites)
- B #9999: [2016] Quantifying mesoscale neuroanatomy using X-ray microtomography  (0 cites)
- Decision: ___________

**121.** conf=0.662 title=1.00 cit=0.25 auth=0.0 `A=preprint`
- A #9999: [2025] Bridging macroscopic and microscopic modeling of electric field by brain stimulation  (0 cites)
- B #9999: [2025] Bridging macroscopic and microscopic modeling of electric field by brain stimulation  (7 cites)
- Decision: ___________

**122.** conf=0.662 title=1.00 cit=0.25 auth=0.0 `A=preprint`
- A #9999: [2025] Divergent organelle allocation in the evolution of sperm gigantism revealed from subcellul  (0 cites)
- B #9999: [2025] Divergent organelle allocation in the evolution of sperm gigantism revealed from subcellul  (1 cites)
- Decision: ___________

**123.** conf=0.662 title=1.00 cit=0.25 auth=0.0 `A=preprint`
- A #9999: [2019] Recurrent U-Net for Resource-Constrained Segmentation  (12 cites)
- B #9999: [2019] Recurrent U-Net for Resource-Constrained Segmentation  (107 cites)
- Decision: ___________

**124.** conf=0.662 title=1.00 cit=0.25 auth=0.0 `A=preprint`
- A #9999: [2019] Retinal horizontal cells use different synaptic sites for global feedforward and local fee  (4 cites)
- B #9999: [2021] Retinal horizontal cells use different synaptic sites for global feedforward and local fee  (34 cites)
- Decision: ___________

**125.** conf=0.662 title=0.82 cit=0.50 auth=0.0 `A=preprint`
- A #9999: [2023] Quantifying network behavior in the rat prefrontal cortex: a reproducibility crisis  (0 cites)
- B #9999: [2024] Quantifying network behavior in the rat prefrontal cortex  (0 cites)
- Decision: ___________

**126.** conf=0.661 title=0.96 cit=0.30 auth=0.0 `A=preprint`
- A #9999: [2022] Early-life experience reorganizes neuromodulatory regulation of stage-specific behavioral   (1 cites)
- B #9999: [2023] Early-life experience reorganizes neuromodulatory regulation of stage-specific behavioral   (23 cites)
- Decision: ___________

**127.** conf=0.661 title=0.84 cit=0.46 auth=0.0 `A=preprint`
- A #9999: [2022] Dopaminergic neurons dynamically update sensory values during navigation  (2 cites)
- B #9999: [2023] Dopaminergic neurons dynamically update sensory values during olfactory maneuver  (19 cites)
- Decision: ___________

**128.** conf=0.660 title=0.99 cit=0.26 auth=0.0 `A=preprint`
- A #9999: [2024] Inhibitory circuits control leg movements during <i>Drosophila</i> grooming  (1 cites)
- B #9999: [2026] Inhibitory circuits control leg movements during Drosophila grooming  (0 cites)
- Decision: ___________

**129.** conf=0.660 title=0.99 cit=0.26 auth=0.0 `A=preprint`
- A #9999: [2024] Inhibitory circuits control leg movements during <i>Drosophila</i> grooming  (1 cites)
- B #9999: [2025] Inhibitory circuits control leg movements during Drosophila grooming  (0 cites)
- Decision: ___________

**130.** conf=0.659 title=0.99 cit=0.25 auth=0.0 `A=preprint`
- A #9999: [2024] Vascular development of fetal and postnatal neocortex of the pig, the European wild boar <  (1 cites)
- B #9999: [2024] Vascular Development of Fetal and Postnatal Neocortex of the Pig, the European Wild Boar <  (3 cites)
- Decision: ___________

**131.** conf=0.659 title=0.93 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2021] Neuropeptide signalling shapes feeding and reproductive behaviours in male <i>C. elegans</  (0 cites)
- B #9999: [2022] Neuropeptide signalling shapes feeding and reproductive behaviours in male <i>Caenorhabdit  (17 cites)
- Decision: ___________

**132.** conf=0.657 title=1.00 cit=0.23 auth=0.0 `A=preprint`
- A #9999: [2024] Universal consensus 3D segmentation of cells from 2D segmented stacks  (15 cites)
- B #9999: [2025] Universal consensus 3D segmentation of cells from 2D segmented stacks  (6 cites)
- Decision: ___________

**133.** conf=0.655 title=0.99 cit=0.24 auth=0.0 `A=preprint`
- A #9999: [2024] A neural circuit for context-dependent multimodal signaling in <i>Drosophila</i>  (2 cites)
- B #9999: [2025] A neural circuit for context-dependent multimodal signaling in Drosophila  (1 cites)
- Decision: ___________

**134.** conf=0.655 title=0.88 cit=0.39 auth=0.0 `A=preprint`
- A #9999: [2024] Brain rewiring during developmental transitions: A Comparative Analysis of Larva and Adult  (2 cites)
- B #9999: [2025] Brain rewiring during development: A comparative analysis of larval and adult <i>Drosophil  (0 cites)
- Decision: ___________

**135.** conf=0.654 title=0.99 cit=0.23 auth=0.0 `A=preprint`
- A #9999: [2024] Inhibitory circuits control leg movements during <i>Drosophila</i> grooming  (1 cites)
- B #9999: [2026] Inhibitory circuits control leg movements during Drosophila grooming  (0 cites)
- Decision: ___________

**136.** conf=0.653 title=0.99 cit=0.22 auth=0.0 `A=preprint`
- A #9999: [2022] Mushroom body output neurons MBONa1/a2 define an odor intensity channel that regulates beh  (0 cites)
- B #9999: [2023] Mushroom body output neurons MBON-a1/a2 define an odor intensity channel that regulates be  (1 cites)
- Decision: ___________

**137.** conf=0.653 title=1.00 cit=0.21 auth=0.0 `A=preprint`
- A #9999: [2023] Non-destructive X-ray tomography of brain tissue ultrastructure  (19 cites)
- B #9999: [2025] Nondestructive X-ray tomography of brain tissue ultrastructure  (4 cites)
- Decision: ___________

**138.** conf=0.652 title=1.00 cit=0.21 auth=0.0 `A=preprint`
- A #9999: [2021] Morphomics via Next-generation Electron Microscopy  (2 cites)
- B #9999: [2023] Morphomics via next-generation electron microscopy  (9 cites)
- Decision: ___________

**139.** conf=0.652 title=1.00 cit=0.21 auth=0.0 `A=preprint`
- A #9999: [2024] Biological volume EM with focused Ga ion beam depends on formation of radiation-resistant   (5 cites)
- B #9999: [2025] Biological volume EM with focused Ga ion beam depends on formation of radiation-resistant   (0 cites)
- Decision: ___________

**140.** conf=0.652 title=0.94 cit=0.29 auth=0.0 `A=preprint`
- A #9999: [2019] Cell-type specific innervation of cortical pyramidal cells at their apical tufts  (1 cites)
- B #40: [2020] Cell-type specific innervation of cortical pyramidal cells at their apical dendrites  (107 cites)
- Decision: ___________

**141.** conf=0.651 title=0.94 cit=0.29 auth=0.0 `A=preprint`
- A #9999: [2021] Structural analysis of the <i>C. elegans</i> dauer larval anterior sensilla by Focused Ion  (1 cites)
- B #9999: [2021] Structural Analysis of the Caenorhabditis elegans Dauer Larval Anterior Sensilla by Focuse  (17 cites)
- Decision: ___________

**142.** conf=0.651 title=0.90 cit=0.35 auth=0.0 `A=preprint`
- A #9999: [2024] Pathogen infection induces sickness behaviors by recruiting neuromodulatory systems linked  (4 cites)
- B #9999: [2025] Pathogen infection induces sickness behaviors through neuromodulators linked to stress and  (5 cites)
- Decision: ___________

**143.** conf=0.651 title=0.99 cit=0.21 auth=0.0 `A=preprint`
- A #9999: [2021] Functional and multiscale 3D structural investigation of brain tissue through correlative   (6 cites)
- B #944: [2022] Functional and multiscale 3D structural investigation of brain tissue through correlative   (42 cites)
- Decision: ___________

**144.** conf=0.650 title=0.96 cit=0.26 auth=0.0 `A=preprint`
- A #9999: [2018] A neural circuit arbitrates between perseverance and withdrawal in hungry Drosophila  (10 cites)
- B #1711: [2019] A Neural Circuit Arbitrates between Persistence and Withdrawal in Hungry Drosophila  (149 cites)
- Decision: ___________

**145.** conf=0.646 title=0.98 cit=0.22 auth=0.0 `A=preprint`
- A #9999: [2022] Brain-wide representations of behavior spanning multiple timescales and states in <i>C. el  (6 cites)
- B #873: [2023] Brain-wide representations of behavior spanning multiple timescales and states in C. elega  (86 cites)
- Decision: ___________

**146.** conf=0.643 title=0.97 cit=0.21 auth=0.0 `A=preprint`
- A #9999: [2022] Dendrite architecture determines mitochondrial distribution patterns <i>in vivo</i>  (4 cites)
- B #9999: [2024] Dendrite architecture determines mitochondrial distribution patterns in vivo  (10 cites)
- Decision: ___________

**147.** conf=0.642 title=1.00 cit=0.17 auth=0.0 `A=preprint`
- A #9999: [2024] The GABAA receptor RDL modulates the auditory sensitivity of malaria mosquitoes.  (4 cites)
- B #9999: [2025] The GABAA receptor RDL modulates the auditory sensitivity of malaria mosquitoes  (2 cites)
- Decision: ___________

**148.** conf=0.642 title=1.00 cit=0.17 auth=0.0 `diff_DOIs`
- A #9999: [2023] Theory of Morphodynamic Information Processing: Linking Sensing to Behaviour  (1 cites)
- B #9999: [2025] Theory of morphodynamic information processing: Linking sensing to behaviour  (6 cites)
- Decision: ___________

**149.** conf=0.641 title=0.99 cit=0.18 auth=0.0 `A=preprint`
- A #9999: [2023] A competitive disinhibitory network for robust optic flow processing in <i>Drosophila</i>  (12 cites)
- B #9999: [2025] A competitive disinhibitory network for robust optic flow processing in Drosophila  (10 cites)
- Decision: ___________

**150.** conf=0.639 title=0.80 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2018] Flexible Learning-Free Segmentation and Reconstruction for Sparse Neuronal Circuit Tracing  (0 cites)
- B #9999: [2018] Flexible Learning-Free Segmentation and Reconstruction of Neural Volumes  (18 cites)
- Decision: ___________

**151.** conf=0.634 title=0.95 cit=0.00 auth=1.0 `diff_DOIs`
- A #281: [2023] Cancer statistics, 2023  (16277 cites)
- B #573: [2024] Cancer statistics, 2024  (8526 cites)
- Decision: ___________

**152.** conf=0.634 title=1.00 cit=0.54 auth=0.0 `diff_DOIs`
- A #9999: [2024] A split-GAL4 driver line resource for Drosophila neuron types  (16 cites)
- B #9999: [2025] A split-GAL4 driver line resource for Drosophila neuron types  (16 cites)
- Decision: ___________

**153.** conf=0.634 title=0.92 cit=0.24 auth=0.0 `A=preprint`
- A #9999: [2020] Primate neuronal connections are sparse as compared to mouse  (1 cites)
- B #645: [2021] Primate neuronal connections are sparse in cortex as compared to mouse  (43 cites)
- Decision: ___________

**154.** conf=0.634 title=0.96 cit=0.19 auth=0.0 `B=preprint`
- A #9999: [2018] Neural Reconstruction Integrity: A Metric for Assessing the Connectivity Accuracy of Recon  (13 cites)
- B #9999: [2017] Neural Reconstruction Integrity: A metric for assessing the connectivity of reconstructed   (0 cites)
- Decision: ___________

**155.** conf=0.633 title=1.00 cit=0.33 auth=0.0 `diff_DOIs`
- A #9999: [2023] Cognitive limits of larval <i>Drosophila</i> : Testing for conditioned inhibition, sensory  (0 cites)
- B #9999: [2024] Cognitive limits of larval <i>Drosophila</i> : testing for conditioned inhibition, sensory  (7 cites)
- Decision: ___________

**156.** conf=0.632 title=1.00 cit=0.13 auth=0.0 `A=preprint`
- A #355: [2022] All-optical visualization of specific molecules in the ultrastructural context of brain ti  (38 cites)
- B #9999: [2025] All-optical visualization of specific molecules in the ultrastructural context of brain ti  (4 cites)
- Decision: ___________

**157.** conf=0.632 title=0.91 cit=0.06 auth=1.0 `diff_DOIs`
- A #647: [2015] Global, regional, and national incidence, prevalence, and years lived with disability for   (6465 cites)
- B #358: [2017] Global, regional, and national incidence, prevalence, and years lived with disability for   (13428 cites)
- Decision: ___________

**158.** conf=0.631 title=1.00 cit=0.12 auth=0.0 `B=preprint`
- A #9999: [2015] An automated images-to-graphs framework for high resolution connectomics  (25 cites)
- B #9999: [2014] An Automated Images-to-Graphs Framework for High Resolution Connectomics  (1 cites)
- Decision: ___________

**159.** conf=0.631 title=0.85 cit=0.34 auth=0.0 `A=preprint`
- A #1883: [2023] Multiplexed volumetric CLEM enabled by antibody derivatives provides new insights into the  (5 cites)
- B #9999: [2024] Multiplexed volumetric CLEM enabled by scFvs provides insights into the cytology of cerebe  (8 cites)
- Decision: ___________

**160.** conf=0.630 title=0.86 cit=0.32 auth=0.0 `A=preprint`
- A #9999: [2021] Regulation of coordinated muscular relaxation by a pattern-generating intersegmental circu  (2 cites)
- B #906: [2021] Regulation of coordinated muscular relaxation in Drosophila larvae by a pattern-regulating  (45 cites)
- Decision: ___________

**161.** conf=0.629 title=1.00 cit=0.52 auth=0.0 `diff_DOIs`
- A #9999: [2024] Systematic annotation of a complete adult male Drosophila nerve cord connectome reveals pr  (10 cites)
- B #1249: [2024] Systematic annotation of a complete adult male Drosophila nerve cord connectome reveals pr  (39 cites)
- Decision: ___________

**162.** conf=0.628 title=0.99 cit=0.12 auth=0.0 `A=preprint`
- A #9999: [2024] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (1 cites)
- B #9999: [2025] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- Decision: ___________

**163.** conf=0.627 title=0.84 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2023] A neurotransmitter atlas of <i>C. elegans</i> males and hermaphrodites  (6 cites)
- B #9999: [2024] A neurotransmitter atlas of the nervous system of C. elegans males and hermaphrodites  (3 cites)
- Decision: ___________

**164.** conf=0.627 title=0.84 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2024] A Distribution-aware Semi-Supervised Pipeline for Cost-effective Neuron Segmentation in Vo  (0 cites)
- B #9999: [2025] A distribution-aware semi-supervised pipeline for cost-effective neuron segmentation  (0 cites)
- Decision: ___________

**165.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Social Experience Shapes Fighting Strategies in Drosophila  (0 cites)
- B #9999: [2025] Social experience shapes fighting strategies in Drosophila  (0 cites)
- Decision: ___________

**166.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (1 cites)
- B #9999: [2025] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- Decision: ___________

**167.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (11 cites)
- B #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (0 cites)
- Decision: ___________

**168.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Bio-inspired multimodal learning with organic neuromorphic electronics for behavioral cond  (0 cites)
- B #9999: [2024] Bio-inspired multimodal learning with organic neuromorphic electronics for behavioral cond  (32 cites)
- Decision: ___________

**169.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2022] Research data management for bioimaging: the 2021 NFDI4BIOIMAGE community survey  (6 cites)
- B #9999: [2022] Research data management for bioimaging: the 2021 NFDI4BIOIMAGE community survey  (8 cites)
- Decision: ___________

**170.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- B #9999: [2025] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- Decision: ___________

**171.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] A split-GAL4 driver line resource for Drosophila neuron types  (0 cites)
- B #9999: [2025] A split-GAL4 driver line resource for Drosophila neuron types  (16 cites)
- Decision: ___________

**172.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (0 cites)
- B #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (0 cites)
- Decision: ___________

**173.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Individuality across environmental context in Drosophila melanogaster  (1 cites)
- B #9999: [2025] Individuality across environmental context in Drosophila melanogaster  (1 cites)
- Decision: ___________

**174.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2014] Network Identification via Node Knockout  (64 cites)
- B #9999: [2012] Network Identification via Node Knockout  (65 cites)
- Decision: ___________

**175.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- B #9999: [2025] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- Decision: ___________

**176.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2026] A pilot study for whole proteome tagging in C. elegans  (0 cites)
- B #9999: [2026] A pilot study for whole proteome tagging in C. elegans  (0 cites)
- Decision: ___________

**177.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (8 cites)
- B #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (4 cites)
- Decision: ___________

**178.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] A neurotransmitter atlas of C. elegans males and hermaphrodites  (14 cites)
- B #9999: [2024] A neurotransmitter atlas of C. elegans males and hermaphrodites  (2 cites)
- Decision: ___________

**179.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (1 cites)
- B #9999: [2025] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- Decision: ___________

**180.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Olfactory combinatorial coding supports risk-reward decision making in C. elegans  (0 cites)
- B #9999: [2025] Olfactory combinatorial coding supports risk-reward decision making in C. elegans  (0 cites)
- Decision: ___________

**181.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Individuality across environmental context in Drosophila melanogaster  (0 cites)
- B #9999: [2026] Individuality across environmental context in Drosophila melanogaster  (1 cites)
- Decision: ___________

**182.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Individuality across environmental context in Drosophila melanogaster  (1 cites)
- B #9999: [2026] Individuality across environmental context in Drosophila melanogaster  (1 cites)
- Decision: ___________

**183.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (0 cites)
- B #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (4 cites)
- Decision: ___________

**184.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Driver lines for studying associative learning in Drosophila  (11 cites)
- B #9999: [2025] Driver lines for studying associative learning in Drosophila  (4 cites)
- Decision: ___________

**185.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] A neurotransmitter atlas of C. elegans males and hermaphrodites  (2 cites)
- B #9999: [2024] A neurotransmitter atlas of C. elegans males and hermaphrodites  (20 cites)
- Decision: ___________

**186.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Spyglass: a framework for reproducible and shareable neuroscience research  (0 cites)
- B #9999: [2025] Spyglass: a framework for reproducible and shareable neuroscience research  (0 cites)
- Decision: ___________

**187.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (4 cites)
- B #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (8 cites)
- Decision: ___________

**188.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (11 cites)
- B #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (0 cites)
- Decision: ___________

**189.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (0 cites)
- B #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (0 cites)
- Decision: ___________

**190.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] A pair of dopaminergic neurons DAN-c1 mediate Drosophila larval aversive olfactory learnin  (0 cites)
- B #9999: [2025] A pair of dopaminergic neurons DAN-c1 mediate Drosophila larval aversive olfactory learnin  (0 cites)
- Decision: ___________

**191.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Individuality across environmental context in Drosophila melanogaster  (1 cites)
- B #9999: [2026] Individuality across environmental context in Drosophila melanogaster  (1 cites)
- Decision: ___________

**192.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- B #9999: [2025] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- Decision: ___________

**193.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Inhibitory circuits control leg movements during Drosophila grooming  (0 cites)
- B #9999: [2026] Inhibitory circuits control leg movements during Drosophila grooming  (0 cites)
- Decision: ___________

**194.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] A comprehensive neuroanatomical survey of the Drosophila Lobula Plate Tangential Neurons w  (12 cites)
- B #9999: [2024] A comprehensive neuroanatomical survey of the Drosophila Lobula Plate Tangential Neurons w  (2 cites)
- Decision: ___________

**195.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Are Transformers Truly Foundational for Robotics?  (0 cites)
- B #9999: [2025] Are transformers truly foundational for robotics?  (3 cites)
- Decision: ___________

**196.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2019] Biological Sample Preparation by High-pressure Freezing, Microwave-assisted Contrast Enhan  (17 cites)
- B #9999: [2019] Biological Sample Preparation by High-pressure Freezing, Microwave-assisted Contrast Enhan  (5 cites)
- Decision: ___________

**197.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2022] SARS-CoV-2 nucleocapsid protein adheres to replication organelles before viral assembly at  (113 cites)
- B #9999: [2022] SARS-CoV-2 nucleocapsid protein adheres to replication organelles before viral assembly at  (101 cites)
- Decision: ___________

**198.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Molecular characterization of gustatory second-order neurons reveals integrative mechanism  (0 cites)
- B #9999: [2025] Molecular characterization of gustatory second-order neurons reveals integrative mechanism  (0 cites)
- Decision: ___________

**199.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] A neurotransmitter atlas of C. elegans males and hermaphrodites  (14 cites)
- B #9999: [2024] A neurotransmitter atlas of C. elegans males and hermaphrodites  (20 cites)
- Decision: ___________

**200.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Statistics of C. elegans turning behavior reveals optimality under biasing constraints  (0 cites)
- B #9999: [2024] Statistics of C. elegans turning behavior reveals optimality under biasing constraints  (0 cites)
- Decision: ___________

**201.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Driver lines for studying associative learning in Drosophila  (1 cites)
- B #9999: [2025] Driver lines for studying associative learning in Drosophila  (0 cites)
- Decision: ___________

**202.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (0 cites)
- B #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (0 cites)
- Decision: ___________

**203.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2022] Aversive Associative Learning and Memory Formation by Pairing Two Chemicals in &lt;em&gt;C  (1 cites)
- B #9999: [2022] Aversive Associative Learning and Memory Formation by Pairing Two Chemicals in &lt;em&gt;C  (0 cites)
- Decision: ___________

**204.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2023] A high-throughput 3D X-ray histology facility for biomedical research and preclinical appl  (4 cites)
- B #9999: [2023] A high-throughput 3D X-ray histology facility for biomedical research and preclinical appl  (9 cites)
- Decision: ___________

**205.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Selective life-long suppression of an odor processing channel in response to critical peri  (0 cites)
- B #9999: [2025] Selective life-long suppression of an odor processing channel in response to critical peri  (0 cites)
- Decision: ___________

**206.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (0 cites)
- B #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (8 cites)
- Decision: ___________

**207.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Molecular identification of wide-field amacrine cells in mouse retina that encode stimulus  (2 cites)
- B #9999: [2024] Molecular identification of wide-field amacrine cells in mouse retina that encode stimulus  (2 cites)
- Decision: ___________

**208.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] A Connectome of the Male Drosophila Ventral Nerve Cord  (15 cites)
- B #1040: [2024] A Connectome of the Male Drosophila Ventral Nerve Cord  (53 cites)
- Decision: ___________

**209.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- B #9999: [2025] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- Decision: ___________

**210.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (8 cites)
- B #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (8 cites)
- Decision: ___________

**211.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2026] Identity and functions of monoaminergic neurons in the predatory nematode Pristionchus pac  (0 cites)
- B #9999: [2026] Identity and functions of monoaminergic neurons in the predatory nematode Pristionchus pac  (0 cites)
- Decision: ___________

**212.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Individuality across environmental context in Drosophila melanogaster  (1 cites)
- B #9999: [2025] Individuality across environmental context in Drosophila melanogaster  (0 cites)
- Decision: ___________

**213.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (0 cites)
- B #9999: [2025] Cell type-specific driver lines targeting the Drosophila central complex and their use to   (8 cites)
- Decision: ___________

**214.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2014] NSF Workshop Report: Discovering General Principles of Nervous System Organization by Comp  (54 cites)
- B #9999: [2014] NSF workshop report: Discovering general principles of nervous system organization by comp  (41 cites)
- Decision: ___________

**215.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Emergence of Functional Heart-Brain Circuits in a Vertebrate  (1 cites)
- B #9999: [2025] Emergence of Functional Heart-Brain Circuits in a Vertebrate  (0 cites)
- Decision: ___________

**216.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Spatial transcriptomics in the adult Drosophila brain and body  (1 cites)
- B #9999: [2025] Spatial transcriptomics in the adult Drosophila brain and body  (1 cites)
- Decision: ___________

**217.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Spatial transcriptomics in the adult Drosophila brain and body  (7 cites)
- B #9999: [2025] Spatial transcriptomics in the adult Drosophila brain and body  (1 cites)
- Decision: ___________

**218.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] A pair of dopaminergic neurons DAN-c1 mediate Drosophila larval aversive olfactory learnin  (4 cites)
- B #9999: [2025] A pair of dopaminergic neurons DAN-c1 mediate Drosophila larval aversive olfactory learnin  (0 cites)
- Decision: ___________

**219.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Synaptic density and relative connectivity conservation maintain circuit stability across   (0 cites)
- B #9999: [2025] Synaptic density and relative connectivity conservation maintain circuit stability across   (0 cites)
- Decision: ___________

**220.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Spatial transcriptomics in the adult Drosophila brain and body  (7 cites)
- B #9999: [2025] Spatial transcriptomics in the adult Drosophila brain and body  (1 cites)
- Decision: ___________

**221.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Homosensory and heterosensory dishabituation engage distinct circuits in Drosophila  (0 cites)
- B #9999: [2025] Homosensory and heterosensory dishabituation engage distinct circuits in Drosophila  (0 cites)
- Decision: ___________

**222.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (1 cites)
- B #9999: [2025] Ultrastructural sublaminar-specific diversity of excitatory synaptic boutons in layer 1 of  (0 cites)
- Decision: ___________

**223.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Individuality across environmental context in Drosophila melanogaster  (1 cites)
- B #9999: [2025] Individuality across environmental context in Drosophila melanogaster  (0 cites)
- Decision: ___________

**224.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2005] Non-participant observation: using video tapes to collect data in nursing research  (108 cites)
- B #9999: [2005] Non-participant observation: using video tapes to collect data in nursing research  (28 cites)
- Decision: ___________

**225.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Molecular characterization of gustatory second-order neurons reveals integrative mechanism  (3 cites)
- B #9999: [2025] Molecular characterization of gustatory second-order neurons reveals integrative mechanism  (0 cites)
- Decision: ___________

**226.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Neural connectome of the ctenophore statocyst  (3 cites)
- B #9999: [2025] Neural Connectome of the Ctenophore Statocyst  (1 cites)
- Decision: ___________

**227.** conf=0.625 title=1.00 cit=0.50 auth=0.0
- A #9999: [2019] Probabilistic Atlases to Enforce Topological Constraints  (0 cites)
- B #9999: [2020] Probabilistic Atlases to Enforce Topological Constraints  (5 cites)
- Decision: ___________

**228.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] A pair of dopaminergic neurons DAN-c1 mediate Drosophila larval aversive olfactory learnin  (4 cites)
- B #9999: [2025] A pair of dopaminergic neurons DAN-c1 mediate Drosophila larval aversive olfactory learnin  (0 cites)
- Decision: ___________

**229.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] A split-GAL4 driver line resource for Drosophila neuron types  (16 cites)
- B #9999: [2025] A split-GAL4 driver line resource for Drosophila neuron types  (0 cites)
- Decision: ___________

**230.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Population parameters of Drosophila larval cooperative foraging.  (0 cites)
- B #9999: [2024] Population parameters of Drosophila larval cooperative foraging  (5 cites)
- Decision: ___________

**231.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of Drosophila larvae  (0 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of Drosophila larvae  (0 cites)
- Decision: ___________

**232.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (0 cites)
- B #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (0 cites)
- Decision: ___________

**233.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] ElectroPhysiomeGAN: Generation of Biophysical Neuron Model Parameters from Recorded Electr  (0 cites)
- B #9999: [2025] ElectroPhysiomeGAN: Generation of Biophysical Neuron Model Parameters from Recorded Electr  (0 cites)
- Decision: ___________

**234.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Deep neural networks to register and annotate cells in moving and deforming nervous system  (0 cites)
- B #9999: [2025] Deep Neural Networks to Register and Annotate Cells in Moving and Deforming Nervous System  (0 cites)
- Decision: ___________

**235.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (2 cites)
- B #9999: [2024] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (2 cites)
- Decision: ___________

**236.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2024] Molecular characterization of gustatory second-order neurons reveals integrative mechanism  (3 cites)
- B #9999: [2025] Molecular characterization of gustatory second-order neurons reveals integrative mechanism  (0 cites)
- Decision: ___________

**237.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Heterogeneous responses to embryonic critical period perturbations within the Drosophila l  (0 cites)
- B #9999: [2025] Heterogeneous responses to embryonic critical period perturbations within the Drosophila l  (1 cites)
- Decision: ___________

**238.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (0 cites)
- B #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (0 cites)
- Decision: ___________

**239.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (1 cites)
- B #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (2 cites)
- Decision: ___________

**240.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] A comprehensive mechanosensory connectome reveals a somatotopically organized neural circu  (0 cites)
- B #9999: [2025] A comprehensive mechanosensory connectome reveals a somatotopically organized neural circu  (0 cites)
- Decision: ___________

**241.** conf=0.625 title=1.00 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (1 cites)
- B #9999: [2024] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (2 cites)
- Decision: ___________

**242.** conf=0.625 title=0.83 cit=0.34 auth=0.0 `A=preprint`
- A #9999: [2024] Structural diversity of mitochondria in the neuromuscular system across development  (0 cites)
- B #9999: [2025] Structural Diversity of Mitochondria in the Neuromuscular System across Development Reveal  (0 cites)
- Decision: ___________

**243.** conf=0.625 title=0.91 cit=0.23 auth=0.0 `A=preprint`
- A #9999: [2025] Proprioceptive limit detectors mediate sensorimotor control of the <i>Drosophila</i> leg  (6 cites)
- B #9999: [2026] Proprioceptive limit detectors contribute to sensorimotor control of the Drosophila leg  (1 cites)
- Decision: ___________

**244.** conf=0.625 title=0.99 cit=0.11 auth=0.0 `A=preprint`
- A #9999: [2024] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (1 cites)
- B #9999: [2026] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- Decision: ___________

**245.** conf=0.622 title=1.00 cit=0.49 auth=0.0 `diff_DOIs`
- A #9999: [2025] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (0 cites)
- B #9999: [2025] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (1 cites)
- Decision: ___________

**246.** conf=0.622 title=0.91 cit=0.21 auth=0.0 `A=preprint`
- A #9999: [2022] 3D reconstruction of the cerebellar germinal layer reveals intercytoplasmic connections be  (3 cites)
- B #1903: [2023] 3D reconstruction of the cerebellar germinal layer reveals tunneling connections between d  (18 cites)
- Decision: ___________

**247.** conf=0.621 title=1.00 cit=0.49 auth=0.0 `diff_DOIs`
- A #9999: [2024] Whole-body connectome of a segmented annelid larva  (5 cites)
- B #9999: [2025] Whole-body connectome of a segmented annelid larva  (4 cites)
- Decision: ___________

**248.** conf=0.621 title=0.57 cit=0.69 auth=0.0 `B=preprint`
- A #1873: [2013] The open connectome project data cluster  (49 cites)
- B #9999: [2013] The Open Connectome Project Data Cluster: Scalable Analysis and Vision for High-Throughput  (26 cites)
- Decision: ___________

**249.** conf=0.620 title=1.00 cit=0.48 auth=0.0 `diff_DOIs`
- A #9999: [2024] Driver lines for studying associative learning in Drosophila  (11 cites)
- B #9999: [2025] Driver lines for studying associative learning in Drosophila  (0 cites)
- Decision: ___________

**250.** conf=0.620 title=1.00 cit=0.48 auth=0.0 `diff_DOIs`
- A #9999: [2024] Driver lines for studying associative learning in Drosophila  (11 cites)
- B #9999: [2024] Driver lines for studying associative learning in Drosophila  (1 cites)
- Decision: ___________

**251.** conf=0.620 title=1.00 cit=0.48 auth=0.0 `diff_DOIs`
- A #9999: [2024] Driver lines for studying associative learning in Drosophila  (1 cites)
- B #9999: [2025] Driver lines for studying associative learning in Drosophila  (4 cites)
- Decision: ___________

**252.** conf=0.620 title=1.00 cit=0.48 auth=0.0 `diff_DOIs`
- A #9999: [2025] Driver lines for studying associative learning in Drosophila  (0 cites)
- B #9999: [2025] Driver lines for studying associative learning in Drosophila  (4 cites)
- Decision: ___________

**253.** conf=0.620 title=1.00 cit=0.48 auth=0.0 `diff_DOIs`
- A #9999: [2023] Combining array tomography with electron tomography provides insights into leakiness of th  (0 cites)
- B #9999: [2024] Combining array tomography with electron tomography provides insights into leakiness of th  (3 cites)
- Decision: ___________

**254.** conf=0.620 title=0.85 cit=0.29 auth=0.0 `A=preprint`
- A #9999: [2020] Astrocyte-neuron crosstalk through Hedgehog signaling mediates cortical circuit assembly  (2 cites)
- B #9999: [2022] Astrocyte-neuron crosstalk through Hedgehog signaling mediates cortical synapse developmen  (88 cites)
- Decision: ___________

**255.** conf=0.619 title=1.00 cit=0.48 auth=0.0 `diff_DOIs`
- A #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (0 cites)
- B #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (24 cites)
- Decision: ___________

**256.** conf=0.619 title=1.00 cit=0.48 auth=0.0 `diff_DOIs`
- A #9999: [2025] Inhibitory columnar feedback neurons are involved in motion processing in Drosophila  (0 cites)
- B #9999: [2026] Inhibitory columnar feedback neurons are involved in motion processing in Drosophila  (0 cites)
- Decision: ___________

**257.** conf=0.619 title=1.00 cit=0.48 auth=0.0 `diff_DOIs`
- A #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (0 cites)
- B #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (24 cites)
- Decision: ___________

**258.** conf=0.619 title=0.43 cit=0.28 auth=1.0 `A=preprint`
- A #254: [2020] Multiscale and multimodal reconstruction of cortical structure and function  (42 cites)
- B #84: [2022] Reconstruction of neocortex: Organelles, compartments, cells, circuits, and activity  (211 cites)
- Decision: ___________

**259.** conf=0.619 title=1.00 cit=0.47 auth=0.0 `diff_DOIs`
- A #9999: [2023] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- B #9999: [2025] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- Decision: ___________

**260.** conf=0.619 title=0.98 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2017] Divergent Connectivity of Homologous Command-like Neurons Mediates Segment-Specific Touch   (133 cites)
- B #9999: [2018] Divergent Connectivity of Homologous Command Neurons Mediates Segment-Specific Touch Respo  (2 cites)
- Decision: ___________

**261.** conf=0.618 title=1.00 cit=0.47 auth=0.0 `diff_DOIs`
- A #9999: [2023] Four individually identified paired dopamine neurons signal taste punishment in larval Dro  (3 cites)
- B #9999: [2025] Four individually identified paired dopamine neurons signal taste punishment in larval Dro  (1 cites)
- Decision: ___________

**262.** conf=0.617 title=0.98 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2023] Screening for differentially expressed memory genes on a diabetes model induced by high su  (0 cites)
- B #9999: [2023] Screening for Differentially Expressed Memory Genes on a Diabetes Model Induced by High-Su  (0 cites)
- Decision: ___________

**263.** conf=0.617 title=1.00 cit=0.47 auth=0.0 `diff_DOIs`
- A #9999: [2025] Whole-body connectome of a segmented annelid larva  (4 cites)
- B #9999: [2025] Whole-body connectome of a segmented annelid larva  (4 cites)
- Decision: ___________

**264.** conf=0.617 title=0.99 cit=0.48 auth=0.0 `diff_DOIs`
- A #9999: [2023] Current Progress and Challenges in Large-scale3D Mitochondria Instance Segmentation  (0 cites)
- B #9999: [2023] Current Progress and Challenges in Large-scale 3D Mitochondria Instance Segmentation  (0 cites)
- Decision: ___________

**265.** conf=0.617 title=1.00 cit=0.47 auth=0.0 `diff_DOIs`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of Drosophila larvae  (7 cites)
- B #9999: [2024] Morphology and ultrastructure of external sense organs of Drosophila larvae  (3 cites)
- Decision: ___________

**266.** conf=0.617 title=1.00 cit=0.47 auth=0.0 `diff_DOIs`
- A #9999: [2025] Four Individually Identified Paired Dopamine Neurons Signal Taste Punishment in Larval Dro  (0 cites)
- B #9999: [2025] Four individually identified paired dopamine neurons signal taste punishment in larval Dro  (1 cites)
- Decision: ___________

**267.** conf=0.617 title=1.00 cit=0.47 auth=0.0 `diff_DOIs`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of Drosophila larvae  (7 cites)
- B #9999: [2025] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- Decision: ___________

**268.** conf=0.617 title=1.00 cit=0.47 auth=0.0 `diff_DOIs`
- A #9999: [2024] Whole-body connectome of a segmented annelid larva  (3 cites)
- B #9999: [2025] Whole-body connectome of a segmented annelid larva  (4 cites)
- Decision: ___________

**269.** conf=0.617 title=1.00 cit=0.47 auth=0.0 `diff_DOIs`
- A #9999: [2015] Reconstruction, Electron Microscopy  (0 cites)
- B #9999: [2014] Reconstruction, Electron Microscopy  (0 cites)
- Decision: ___________

**270.** conf=0.616 title=0.78 cit=0.38 auth=0.0 `A=preprint`
- A #9999: [2020] Electrophysiological validation of premotor interneurons monosynaptically connected to the  (5 cites)
- B #1659: [2022] Electrophysiological Validation of Monosynaptic Connectivity between Premotor Interneurons  (13 cites)
- Decision: ___________

**271.** conf=0.616 title=1.00 cit=0.46 auth=0.0 `diff_DOIs`
- A #1813: [2024] Transforming descending input into motor output: An analysis of the Drosophila Male Adult   (20 cites)
- B #9999: [2025] Transforming descending input into motor output: An analysis of the Drosophila Male Adult   (1 cites)
- Decision: ___________

**272.** conf=0.615 title=1.00 cit=0.46 auth=0.0 `diff_DOIs`
- A #9999: [2025] Profiling presynaptic scaffolds using split-GFP reconstitution reveals cell-type-specific   (0 cites)
- B #9999: [2026] Profiling presynaptic scaffolds using split-GFP reconstitution reveals cell-type-specific   (0 cites)
- Decision: ___________

**273.** conf=0.615 title=1.00 cit=0.46 auth=0.0 `diff_DOIs`
- A #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (6 cites)
- B #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (2 cites)
- Decision: ___________

**274.** conf=0.615 title=1.00 cit=0.46 auth=0.0 `diff_DOIs`
- A #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (6 cites)
- B #9999: [2024] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (2 cites)
- Decision: ___________

**275.** conf=0.615 title=1.00 cit=0.46 auth=0.0 `diff_DOIs`
- A #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (6 cites)
- B #9999: [2023] Toolkits for detailed and high-throughput interrogation of synapses in C. elegans  (1 cites)
- Decision: ___________

**276.** conf=0.615 title=1.00 cit=0.46 auth=0.0 `diff_DOIs`
- A #9999: [2023] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (2 cites)
- B #9999: [2025] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (0 cites)
- Decision: ___________

**277.** conf=0.615 title=1.00 cit=0.46 auth=0.0 `diff_DOIs`
- A #1343: [2019] Reconstruction of 1,000 Projection Neurons Reveals New Cell Types and Organization of Long  (552 cites)
- B #9999: [2019] Reconstruction of 1,000 Projection Neurons Reveals New Cell Types and Organization of Long  (1 cites)
- Decision: ___________

**278.** conf=0.614 title=0.97 cit=0.50 auth=0.0
- A #9999: [2003] Intracranially administered anti-Abeta antibodies reduce beta-amyloid deposition by mechan  (267 cites)
- B #9999: [2003] Intracranially Administered Anti-Αβ Antibodies Reduce β-Amyloid Deposition by Mechanisms B  (229 cites)
- Decision: ___________

**279.** conf=0.614 title=1.00 cit=0.46 auth=0.0 `diff_DOIs`
- A #9999: [2024] Neural circuits underlying context-dependent competition between defensive actions in Dros  (1 cites)
- B #9999: [2025] Neural circuits underlying context-dependent competition between defensive actions in Dros  (5 cites)
- Decision: ___________

**280.** conf=0.614 title=1.00 cit=0.46 auth=0.0 `diff_DOIs`
- A #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (21 cites)
- B #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (24 cites)
- Decision: ___________

**281.** conf=0.614 title=1.00 cit=0.46 auth=0.0 `diff_DOIs`
- A #9999: [2024] Whole-body connectome of a segmented annelid larva  (5 cites)
- B #9999: [2025] Whole-body connectome of a segmented annelid larva  (4 cites)
- Decision: ___________

**282.** conf=0.614 title=1.00 cit=0.45 auth=0.0 `diff_DOIs`
- A #9999: [2024] Mechanism of barotaxis in marine zooplankton  (5 cites)
- B #9999: [2024] Mechanism of barotaxis in marine zooplankton  (5 cites)
- Decision: ___________

**283.** conf=0.614 title=1.00 cit=0.45 auth=0.0 `diff_DOIs`
- A #9999: [2024] Mechanism of barotaxis in marine zooplankton  (3 cites)
- B #9999: [2024] Mechanism of barotaxis in marine zooplankton  (5 cites)
- Decision: ___________

**284.** conf=0.614 title=0.93 cit=0.16 auth=0.0 `A=preprint`
- A #9999: [2023] The Synaptic Architecture of Layer 5 Thick Tufted Excitatory Neurons in the Visual Cortex   (7 cites)
- B #9999: [2025] The synaptic architecture of layer 5 thick tufted excitatory neurons in mouse visual corte  (8 cites)
- Decision: ___________

**285.** conf=0.613 title=1.00 cit=0.45 auth=0.0 `diff_DOIs`
- A #9999: [2024] Driver lines for studying associative learning in Drosophila  (5 cites)
- B #9999: [2025] Driver lines for studying associative learning in Drosophila  (4 cites)
- Decision: ___________

**286.** conf=0.613 title=1.00 cit=0.45 auth=0.0 `diff_DOIs`
- A #9999: [2024] Driver lines for studying associative learning in Drosophila  (11 cites)
- B #9999: [2024] Driver lines for studying associative learning in Drosophila  (5 cites)
- Decision: ___________

**287.** conf=0.613 title=1.00 cit=0.45 auth=0.0 `diff_DOIs`
- A #9999: [2024] Driver lines for studying associative learning in Drosophila  (5 cites)
- B #9999: [2025] Driver lines for studying associative learning in Drosophila  (0 cites)
- Decision: ___________

**288.** conf=0.613 title=1.00 cit=0.45 auth=0.0 `diff_DOIs`
- A #9999: [2024] Driver lines for studying associative learning in Drosophila  (5 cites)
- B #9999: [2024] Driver lines for studying associative learning in Drosophila  (1 cites)
- Decision: ___________

**289.** conf=0.613 title=1.00 cit=0.45 auth=0.0 `diff_DOIs`
- A #9999: [2023] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (2 cites)
- B #9999: [2025] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (1 cites)
- Decision: ___________

**290.** conf=0.612 title=1.00 cit=0.45 auth=0.0 `diff_DOIs`
- A #9999: [2023] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (2 cites)
- B #9999: [2023] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (5 cites)
- Decision: ___________

**291.** conf=0.612 title=1.00 cit=0.45 auth=0.0 `diff_DOIs`
- A #9999: [2023] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- B #9999: [2025] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- Decision: ___________

**292.** conf=0.612 title=1.00 cit=0.45 auth=0.0 `diff_DOIs`
- A #9999: [2024] Exploring neurodevelopment via spatiotemporal collation of anatomical networks with NeuroS  (0 cites)
- B #9999: [2025] Exploring neurodevelopment via spatiotemporal collation of anatomical networks with NeuroS  (0 cites)
- Decision: ___________

**293.** conf=0.611 title=1.00 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2025] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- B #9999: [2026] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- Decision: ___________

**294.** conf=0.610 title=1.00 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2023] Four individually identified paired dopamine neurons signal taste punishment in larval Dro  (3 cites)
- B #9999: [2025] Four Individually Identified Paired Dopamine Neurons Signal Taste Punishment in Larval Dro  (0 cites)
- Decision: ___________

**295.** conf=0.610 title=1.00 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2023] Four individually identified paired dopamine neurons signal taste punishment in larval Dro  (3 cites)
- B #9999: [2025] Four Individually Identified Paired Dopamine Neurons Signal Taste Punishment in Larval Dro  (0 cites)
- Decision: ___________

**296.** conf=0.610 title=1.00 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2024] Whole-body connectome of a segmented annelid larva  (3 cites)
- B #9999: [2025] Whole-body connectome of a segmented annelid larva  (4 cites)
- Decision: ___________

**297.** conf=0.609 title=1.00 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2024] ElectroPhysiomeGAN: Generation of Biophysical Neuron Model Parameters from Recorded Electr  (0 cites)
- B #9999: [2025] ElectroPhysiomeGAN: Generation of Biophysical Neuron Model Parameters from Recorded Electr  (0 cites)
- Decision: ___________

**298.** conf=0.609 title=1.00 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2024] Morphology and ultrastructure of external sense organs of Drosophila larvae  (3 cites)
- B #9999: [2025] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- Decision: ___________

**299.** conf=0.609 title=1.00 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (21 cites)
- B #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (0 cites)
- Decision: ___________

**300.** conf=0.609 title=1.00 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2025] Four Individually Identified Paired Dopamine Neurons Signal Taste Punishment in Larval Dro  (0 cites)
- B #9999: [2025] Four Individually Identified Paired Dopamine Neurons Signal Taste Punishment in Larval Dro  (0 cites)
- Decision: ___________

**301.** conf=0.609 title=1.00 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2024] Generation of biophysical neuron model parameters from recorded electrophysiological respo  (1 cites)
- B #9999: [2025] Generation of biophysical neuron model parameters from recorded electrophysiological respo  (0 cites)
- Decision: ___________

**302.** conf=0.609 title=1.00 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2025] Adjoint propagation of error signal through modular recurrent neural networks for biologic  (0 cites)
- B #9999: [2026] Adjoint propagation of error signal through modular recurrent neural networks for biologic  (0 cites)
- Decision: ___________

**303.** conf=0.609 title=1.00 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2025] ElectroPhysiomeGAN: Generation of Biophysical Neuron Model Parameters from Recorded Electr  (0 cites)
- B #9999: [2025] ElectroPhysiomeGAN: Generation of Biophysical Neuron Model Parameters from Recorded Electr  (0 cites)
- Decision: ___________

**304.** conf=0.609 title=1.00 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (21 cites)
- B #9999: [2023] Hunger- and thirst-sensing neurons modulate a neuroendocrine network to coordinate sugar a  (0 cites)
- Decision: ___________

**305.** conf=0.609 title=0.38 cit=0.30 auth=1.0 `A=preprint`
- A #31: [2020] Chandelier cell anatomy and function reveal a variably distributed but common signal  (40 cites)
- B #115: [2021] Structure and function of axo-axonic inhibition  (90 cites)
- Decision: ___________

**306.** conf=0.607 title=1.00 cit=0.43 auth=0.0 `diff_DOIs`
- A #9999: [2025] Neural connectome of the ctenophore statocyst  (3 cites)
- B #9999: [2026] Neural Connectome of the Ctenophore Statocyst  (0 cites)
- Decision: ___________

**307.** conf=0.607 title=1.00 cit=0.43 auth=0.0 `diff_DOIs`
- A #9999: [2026] Neural Connectome of the Ctenophore Statocyst  (0 cites)
- B #9999: [2026] Neural connectome of the ctenophore statocyst  (0 cites)
- Decision: ___________

**308.** conf=0.607 title=1.00 cit=0.43 auth=0.0 `diff_DOIs`
- A #9999: [2026] Profiling presynaptic scaffolds using split-GFP reconstitution reveals cell-type-specific   (0 cites)
- B #9999: [2026] Profiling presynaptic scaffolds using split-GFP reconstitution reveals cell-type-specific   (0 cites)
- Decision: ___________

**309.** conf=0.607 title=1.00 cit=0.43 auth=0.0 `diff_DOIs`
- A #9999: [2025] Neural Connectome of the Ctenophore Statocyst  (1 cites)
- B #9999: [2026] Neural Connectome of the Ctenophore Statocyst  (0 cites)
- Decision: ___________

**310.** conf=0.607 title=0.91 cit=0.16 auth=0.0 `A=preprint`
- A #9999: [2023] Organization of an Ascending Circuit that Conveys Flight Motor State  (3 cites)
- B #9999: [2024] Organization of an ascending circuit that conveys flight motor state in Drosophila  (27 cites)
- Decision: ___________

**311.** conf=0.607 title=1.00 cit=0.43 auth=0.0 `diff_DOIs`
- A #9999: [2024] Whole-body connectome of a segmented annelid larva  (3 cites)
- B #9999: [2024] Whole-body connectome of a segmented annelid larva  (5 cites)
- Decision: ___________

**312.** conf=0.606 title=1.00 cit=0.42 auth=0.0 `diff_DOIs`
- A #9999: [2025] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- B #9999: [2025] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- Decision: ___________

**313.** conf=0.606 title=1.00 cit=0.42 auth=0.0 `diff_DOIs`
- A #9999: [2025] Deep neural networks to register and annotate cells in moving and deforming nervous system  (0 cites)
- B #9999: [2026] Deep neural networks to register and annotate cells in moving and deforming nervous system  (0 cites)
- Decision: ___________

**314.** conf=0.606 title=1.00 cit=0.42 auth=0.0 `diff_DOIs`
- A #9999: [2025] Deep Neural Networks to Register and Annotate Cells in Moving and Deforming Nervous System  (0 cites)
- B #9999: [2026] Deep neural networks to register and annotate cells in moving and deforming nervous system  (0 cites)
- Decision: ___________

**315.** conf=0.606 title=0.87 cit=0.00 auth=1.0 `diff_DOIs`
- A #972: [2019] Global, regional, and national burden of neurological disorders, 1990–2016: a systematic a  (5555 cites)
- B #746: [2021] Global, regional, and national burden of stroke and its risk factors, 1990–2019: a systema  (7183 cites)
- Decision: ___________

**316.** conf=0.605 title=0.49 cit=0.14 auth=1.0 `A=preprint`
- A #188: [2020] The connectome of the adult <i>Drosophila</i> mushroom body: implications for function  (19 cites)
- B #1171: [2020] Visual Input into the Drosophila melanogaster Mushroom Body  (40 cites)
- Decision: ___________

**317.** conf=0.605 title=0.27 cit=0.44 auth=1.0 `A=preprint`
- A #1820: [2020] Expansion Revealing: Decrowding Proteins to Unmask Invisible Brain Nanostructures  (24 cites)
- B #1631: [2022] Revealing nanostructures in brain tissue via protein decrowding by iterative expansion mic  (83 cites)
- Decision: ___________

**318.** conf=0.604 title=1.00 cit=0.42 auth=0.0 `diff_DOIs`
- A #9999: [2024] Mechanism of barotaxis in marine zooplankton  (5 cites)
- B #9999: [2024] Mechanism of barotaxis in marine zooplankton  (3 cites)
- Decision: ___________

**319.** conf=0.604 title=1.00 cit=0.42 auth=0.0 `diff_DOIs`
- A #9999: [2023] Brain Size Scaling Through Development in the Whitelined Sphinx Moth (Hyles Lineata) Shows  (0 cites)
- B #9999: [2024] Brain size scaling through development in the whitelined sphinx moth (Hyles lineata) shows  (3 cites)
- Decision: ___________

**320.** conf=0.604 title=1.00 cit=0.42 auth=0.0 `diff_DOIs`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- B #9999: [2025] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- Decision: ___________

**321.** conf=0.604 title=1.00 cit=0.42 auth=0.0 `diff_DOIs`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- B #9999: [2024] Morphology and ultrastructure of external sense organs of Drosophila larvae  (3 cites)
- Decision: ___________

**322.** conf=0.603 title=1.00 cit=0.41 auth=0.0 `diff_DOIs`
- A #9999: [2023] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- B #9999: [2025] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- Decision: ___________

**323.** conf=0.603 title=1.00 cit=0.41 auth=0.0 `diff_DOIs`
- A #9999: [2025] Four Individually Identified Paired Dopamine Neurons Signal Taste Punishment in Larval Dro  (0 cites)
- B #9999: [2025] Four individually identified paired dopamine neurons signal taste punishment in larval Dro  (1 cites)
- Decision: ___________

**324.** conf=0.602 title=1.00 cit=0.41 auth=0.0 `diff_DOIs`
- A #9999: [2023] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (5 cites)
- B #9999: [2025] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (0 cites)
- Decision: ___________

**325.** conf=0.602 title=1.00 cit=0.41 auth=0.0 `diff_DOIs`
- A #9999: [2024] Mechanism of barotaxis in marine zooplankton  (0 cites)
- B #9999: [2024] Mechanism of barotaxis in marine zooplankton  (5 cites)
- Decision: ___________

**326.** conf=0.601 title=1.00 cit=0.41 auth=0.0 `diff_DOIs`
- A #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (11 cites)
- B #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (5 cites)
- Decision: ___________

**327.** conf=0.600 title=1.00 cit=0.40 auth=0.0 `diff_DOIs`
- A #9999: [2023] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (5 cites)
- B #9999: [2025] The unique synaptic circuitry of specialized olfactory glomeruli in Drosophila melanogaste  (1 cites)
- Decision: ___________

**328.** conf=0.600 title=1.00 cit=0.40 auth=0.0 `diff_DOIs`
- A #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (0 cites)
- B #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (1 cites)
- Decision: ___________

**329.** conf=0.600 title=1.00 cit=0.40 auth=0.0 `diff_DOIs`
- A #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (0 cites)
- B #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (1 cites)
- Decision: ___________

**330.** conf=0.600 title=1.00 cit=0.00 auth=0.0 `A=preprint`
- A #9999: [2024] TriSAM: Tri-Plane SAM for zero-shot cortical blood vessel segmentation in VEM images  (6 cites)
- B #9999: [2025] TriSAM: Tri-Plane SAM for Zero-Shot Cortical Blood Vessel Segmentation in VEM Images  (5 cites)
- Decision: ___________

**331.** conf=0.600 title=1.00 cit=0.40 auth=0.0 `diff_DOIs`
- A #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (0 cites)
- B #9999: [2025] Probing the role of synaptic adhesion molecule RTN4RL2 in setting up cochlear connectivity  (1 cites)
- Decision: ___________

**332.** conf=0.598 title=1.00 cit=0.39 auth=0.0 `diff_DOIs`
- A #9999: [2023] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- B #9999: [2023] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- Decision: ___________

**333.** conf=0.598 title=1.00 cit=0.39 auth=0.0 `diff_DOIs`
- A #9999: [2025] Profiling presynaptic scaffolds using split-GFP reconstitution reveals cell-type-specific   (0 cites)
- B #9999: [2026] Profiling presynaptic scaffolds using split-GFP reconstitution reveals cell-type-specific   (0 cites)
- Decision: ___________

**334.** conf=0.598 title=1.00 cit=0.39 auth=0.0 `diff_DOIs`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- B #9999: [2023] Morphology and ultrastructure of external sense organs of Drosophila larvae  (7 cites)
- Decision: ___________

**335.** conf=0.598 title=1.00 cit=0.39 auth=0.0 `diff_DOIs`
- A #9999: [2023] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- B #9999: [2025] Neural substrates of cold nociception in Drosophila larva  (0 cites)
- Decision: ___________

**336.** conf=0.597 title=1.00 cit=0.39 auth=0.0 `diff_DOIs`
- A #9999: [2023] Balance of activity during a critical period tunes a developing network  (20 cites)
- B #9999: [2024] Balance of activity during a critical period tunes a developing network  (13 cites)
- Decision: ___________

**337.** conf=0.596 title=1.00 cit=0.38 auth=0.0 `diff_DOIs`
- A #9999: [2024] Efficient Cell-Wide Mapping of Mitochondria in Electron Microscopic Volumes Using webKnoss  (0 cites)
- B #9999: [2025] Efficient cell-wide mapping of mitochondria in electron microscopic volumes using webKnoss  (5 cites)
- Decision: ___________

**338.** conf=0.594 title=0.91 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2025] Inhibitory columnar feedback neurons are involved in motion processing in Drosophila  (0 cites)
- B #9999: [2025] Inhibitory columnar feedback neurons are required for motion processing in Drosophila  (1 cites)
- Decision: ___________

**339.** conf=0.594 title=0.91 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2012] Properties of original impactors estimated from three‐dimensional analysis of whole Stardu  (5 cites)
- B #9999: [2012] Properties of original impactors estimated from three-dimensional analysis of whole  (0 cites)
- Decision: ___________

**340.** conf=0.594 title=1.00 cit=0.38 auth=0.0 `diff_DOIs`
- A #9999: [2025] Neural connectome of the ctenophore statocyst  (3 cites)
- B #9999: [2026] Neural connectome of the ctenophore statocyst  (0 cites)
- Decision: ___________

**341.** conf=0.594 title=1.00 cit=0.38 auth=0.0 `diff_DOIs`
- A #9999: [2025] Neural Connectome of the Ctenophore Statocyst  (1 cites)
- B #9999: [2026] Neural connectome of the ctenophore statocyst  (0 cites)
- Decision: ___________

**342.** conf=0.594 title=1.00 cit=0.38 auth=0.0 `diff_DOIs`
- A #9999: [2024] Mechanism of barotaxis in marine zooplankton  (0 cites)
- B #9999: [2024] Mechanism of barotaxis in marine zooplankton  (3 cites)
- Decision: ___________

**343.** conf=0.594 title=1.00 cit=0.38 auth=0.0 `diff_DOIs`
- A #9999: [2024] Mechanism of barotaxis in marine zooplankton  (5 cites)
- B #9999: [2024] Mechanism of barotaxis in marine zooplankton  (0 cites)
- Decision: ___________

**344.** conf=0.593 title=1.00 cit=0.37 auth=0.0 `diff_DOIs`
- A #9999: [2026] Inhibitory circuits control leg movements during Drosophila grooming  (0 cites)
- B #9999: [2026] Inhibitory circuits control leg movements during Drosophila grooming  (0 cites)
- Decision: ___________

**345.** conf=0.593 title=1.00 cit=0.37 auth=0.0 `diff_DOIs`
- A #9999: [2025] Inhibitory circuits control leg movements during Drosophila grooming  (0 cites)
- B #9999: [2026] Inhibitory circuits control leg movements during Drosophila grooming  (0 cites)
- Decision: ___________

**346.** conf=0.591 title=1.00 cit=0.36 auth=0.0 `diff_DOIs`
- A #9999: [2022] High-throughput segmentation of unmyelinated axons by deep learning  (22 cites)
- B #9999: [2021] High-throughput segmentation of unmyelinated axons by deep learning  (1 cites)
- Decision: ___________

**347.** conf=0.591 title=1.00 cit=0.36 auth=0.0 `diff_DOIs`
- A #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (5 cites)
- B #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (0 cites)
- Decision: ___________

**348.** conf=0.591 title=1.00 cit=0.36 auth=0.0 `diff_DOIs`
- A #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (5 cites)
- B #9999: [2024] Feedback inhibition by a descending GABAergic neuron regulates timing of escape behavior i  (0 cites)
- Decision: ___________

**349.** conf=0.589 title=0.92 cit=0.06 auth=0.0 `A=preprint`
- A #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of <i>Drosophila</i> larvae  (0 cites)
- B #9999: [2025] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- Decision: ___________

**350.** conf=0.589 title=1.00 cit=0.35 auth=0.0 `diff_DOIs`
- A #9999: [2023] Current Progress and Challenges in Large-scale 3D Mitochondria Instance Segmentation  (0 cites)
- B #9999: [2023] Current Progress and Challenges in Large-Scale 3D Mitochondria Instance Segmentation  (22 cites)
- Decision: ___________

**351.** conf=0.588 title=0.91 cit=0.48 auth=0.0 `diff_DOIs`
- A #9999: [2025] Inhibitory columnar feedback neurons are required for motion processing in Drosophila  (1 cites)
- B #9999: [2026] Inhibitory columnar feedback neurons are involved in motion processing in Drosophila  (0 cites)
- Decision: ___________

**352.** conf=0.588 title=1.00 cit=0.35 auth=0.0 `diff_DOIs`
- A #9999: [2023] Online citizen science with the Zooniverse for analysis of biological volumetric data  (0 cites)
- B #9999: [2023] Online citizen science with the Zooniverse for analysis of biological volumetric data  (9 cites)
- Decision: ___________

**353.** conf=0.588 title=1.00 cit=0.35 auth=0.0 `diff_DOIs`
- A #9999: [2024] Reviewer #3 (Public Review): Feedback inhibition by a descending GABAergic neuron regulate  (0 cites)
- B #9999: [2024] Reviewer #3 (Public Review): Feedback inhibition by a descending GABAergic neuron regulate  (0 cites)
- Decision: ___________

**354.** conf=0.586 title=0.43 cit=0.14 auth=1.0 `A=preprint`
- A #1796: [2016] Flood-Filling Networks  (38 cites)
- B #129: [2018] High-precision automated reconstruction of neurons with flood-filling networks  (389 cites)
- Decision: ___________

**355.** conf=0.585 title=0.52 cit=0.41 auth=1.0 `diff_DOIs`
- A #532: [2020] The cortical wiring scheme of hierarchical information processing  (13 cites)
- B #1419: [2020] A multi-scale cortical wiring space links cellular architecture and functional dynamics in  (110 cites)
- Decision: ___________

**356.** conf=0.583 title=0.91 cit=0.06 auth=0.0 `B=preprint`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of Drosophila larvae  (7 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of <i>Drosophila</i> larvae  (0 cites)
- Decision: ___________

**357.** conf=0.583 title=1.00 cit=0.33 auth=0.0 `diff_DOIs`
- A #62: [1989] Co-planar stereotaxic atlas of the human brain  (7608 cites)
- B #44: [1988] Co-Planar Stereotaxic Atlas of the Human Brain  (11679 cites)
- Decision: ___________

**358.** conf=0.583 title=1.00 cit=0.33 auth=0.0
- A #9999: [2021] The Difference in Expression of Autophagy-Related Proteins in Lesional and Perilesional Sk  (8 cites)
- B #9999: [2021] The Difference in Expression of Autophagy-Related Proteins in Lesional and Perilesional Sk  (10 cites)
- Decision: ___________

**359.** conf=0.582 title=0.91 cit=0.06 auth=0.0 `B=preprint`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of <i>Drosophila</i> larvae  (0 cites)
- Decision: ___________

**360.** conf=0.581 title=0.99 cit=0.33 auth=0.0 `diff_DOIs`
- A #9999: [2023] Current Progress and Challenges in Large-scale3D Mitochondria Instance Segmentation  (0 cites)
- B #9999: [2023] Current Progress and Challenges in Large-Scale 3D Mitochondria Instance Segmentation  (22 cites)
- Decision: ___________

**361.** conf=0.581 title=0.91 cit=0.05 auth=0.0 `A=preprint`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of <i>Drosophila</i> larvae  (1 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of Drosophila larvae  (0 cites)
- Decision: ___________

**362.** conf=0.581 title=0.91 cit=0.05 auth=0.0 `A=preprint`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of <i>Drosophila</i> larvae  (1 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of Drosophila larvae  (0 cites)
- Decision: ___________

**363.** conf=0.579 title=0.95 cit=0.39 auth=0.0 `diff_DOIs`
- A #9999: [2021] Oligodendrocyte precursor cells prune axons in the mouse neocortex  (11 cites)
- B #743: [2022] Oligodendrocyte precursor cells ingest axons in the mouse neocortex  (135 cites)
- Decision: ___________

**364.** conf=0.577 title=0.76 cit=0.25 auth=0.0 `A=preprint`
- A #9999: [2024] Aberrant neuronal hyperactivation causes an age- and diet-dependent decline in associative  (1 cites)
- B #9999: [2024] Aberrant neuronal hyperactivation causes an age-dependent behavioral decline in <i>Caenorh  (6 cites)
- Decision: ___________

**365.** conf=0.575 title=1.00 cit=0.30 auth=0.0 `diff_DOIs`
- A #9999: [2013] The Cytoarchitectonic Map of Constantin von Economo and Georg N. Koskinas  (10 cites)
- B #9999: [2013] The Cytoarchitectonic Map of Constantin von Economo and Georg N. Koskinas  (5 cites)
- Decision: ___________

**366.** conf=0.572 title=1.00 cit=0.29 auth=0.0 `diff_DOIs`
- A #9999: [2025] Inhibitory circuits control leg movements during Drosophila grooming  (1 cites)
- B #9999: [2025] Inhibitory circuits control leg movements during Drosophila grooming  (0 cites)
- Decision: ___________

**367.** conf=0.572 title=1.00 cit=0.29 auth=0.0 `diff_DOIs`
- A #9999: [2025] Inhibitory circuits control leg movements during Drosophila grooming  (1 cites)
- B #9999: [2026] Inhibitory circuits control leg movements during Drosophila grooming  (0 cites)
- Decision: ___________

**368.** conf=0.572 title=0.80 cit=0.17 auth=0.0 `A=preprint`
- A #9999: [2024] Brain-wide mapping of oligodendrocyte organization and oligodendrogenesis across the murin  (10 cites)
- B #9999: [2026] Brain-wide mapping of oligodendrocyte organization, oligodendrogenesis, and myelin injury  (0 cites)
- Decision: ___________

**369.** conf=0.571 title=0.47 cit=0.03 auth=1.0 `B=preprint`
- A #400: [2008] Autophagy fights disease through cellular self-digestion  (6389 cites)
- B #486: [2007] Autophagy: process and function  (3921 cites)
- Decision: ___________

**370.** conf=0.570 title=0.46 cit=0.04 auth=1.0 `A=preprint`
- A #185: [2020] A Connectome and Analysis of the Adult <i>Drosophila</i> Central Brain  (35 cites)
- B #803: [2021] A connectome is not enough – what is still needed to understand the brain of<i>Drosophila<  (36 cites)
- Decision: ___________

**371.** conf=0.570 title=0.87 cit=0.46 auth=0.0 `diff_DOIs`
- A #9999: [2013] Exploring Brain Connectivity in Insect Model Systems of Learning and Memory Neuroanatomy R  (0 cites)
- B #9999: [2013] Exploring Brain Connectivity in Insect Model Systems of Learning and Memory  (11 cites)
- Decision: ___________

**372.** conf=0.569 title=0.94 cit=0.36 auth=0.0 `diff_DOIs`
- A #9999: [2021] Extrasynaptic Signaling Enables an Asymmetric Juvenile Motor Circuit to Produce a Symmetri  (0 cites)
- B #1737: [2022] Extrasynaptic signaling enables an asymmetric juvenile motor circuit to produce symmetric   (28 cites)
- Decision: ___________

**373.** conf=0.566 title=0.89 cit=0.42 auth=0.0 `diff_DOIs`
- A #1812: [2010] Visualization of image data from cells to organisms  (270 cites)
- B #9999: [2010] Visualization of image data from cells to  (1 cites)
- Decision: ___________

**374.** conf=0.563 title=0.85 cit=0.46 auth=0.0 `diff_DOIs`
- A #9999: [2024] A neurotransmitter atlas of the nervous system of C. elegans males and hermaphrodites  (3 cites)
- B #9999: [2024] A neurotransmitter atlas of C. elegans males and hermaphrodites  (14 cites)
- Decision: ___________

**375.** conf=0.559 title=1.00 cit=0.44 auth=0.0 `A=preprint`
- A #9999: [2024] The Neuron as a Direct Data-Driven Controller  (1 cites)
- B #9999: [2024] The neuron as a direct data-driven controller  (14 cites)
- Decision: ___________

**376.** conf=0.558 title=1.00 cit=0.23 auth=0.0 `diff_DOIs`
- A #9999: [2025] Inhibitory circuits control leg movements during Drosophila grooming  (1 cites)
- B #9999: [2026] Inhibitory circuits control leg movements during Drosophila grooming  (0 cites)
- Decision: ___________

**377.** conf=0.554 title=0.44 cit=0.00 auth=1.0 `B=preprint`
- A #1327: [2020] The temporal structure of the inner retina at a single glance  (30 cites)
- B #1835: [2022] Eye structure shapes neuron function in <i>Drosophila</i> motion vision  (30 cites)
- Decision: ___________

**378.** conf=0.552 title=1.00 cit=0.81 auth=0.0 `diff_DOIs`
- A #9999: [2022] Chemoreceptor co-expression in Drosophila melanogaster olfactory neurons  (144 cites)
- B #9999: [2021] Chemoreceptor co-expression in Drosophila melanogaster olfactory neurons.  (119 cites)
- Decision: ___________

**379.** conf=0.549 title=0.62 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2020] Ultrastructural view of astrocyte-astrocyte and astrocyte-synapse contacts within the hipp  (14 cites)
- B #1304: [2022] Ultrastructural view of astrocyte arborization, astrocyte-astrocyte and astrocyte-synapse   (117 cites)
- Decision: ___________

**380.** conf=0.548 title=0.42 cit=0.00 auth=1.0 `A=preprint`
- A #1458: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (5 cites)
- B #1133: [2021] A Survey of Convolutional Neural Networks: Analysis, Applications, and Prospects  (4580 cites)
- Decision: ___________

**381.** conf=0.547 title=1.00 cit=0.19 auth=0.0 `diff_DOIs`
- A #9999: [2023] Online conversion of reconstructed neural morphologies into standardized SWC format  (1 cites)
- B #9999: [2023] Online conversion of reconstructed neural morphologies into standardized SWC format  (21 cites)
- Decision: ___________

**382.** conf=0.544 title=0.89 cit=0.54 auth=0.0 `A=preprint`
- A #1887: [2020] Chemoreceptor Co-Expression in <i>Drosophila</i> Olfactory Neurons  (28 cites)
- B #9999: [2022] Chemoreceptor co-expression in Drosophila melanogaster olfactory neurons  (144 cites)
- Decision: ___________

**383.** conf=0.540 title=0.87 cit=0.35 auth=1.0 `diff_DOIs`
- A #1828: [2012] Learning Context Cues for Synapse Segmentation in EM Volumes  (27 cites)
- B #1339: [2013] Learning Context Cues for Synapse Segmentation  (66 cites)
- Decision: ___________

**384.** conf=0.540 title=0.34 cit=0.08 auth=1.0 `diff_DOIs`
- A #1235: [2016] Optimally controlling the human connectome: the role of network topology  (236 cites)
- B #1072: [2017] The specificity and robustness of long-distance connections in weighted, interareal connec  (249 cites)
- Decision: ___________

**385.** conf=0.539 title=0.40 cit=0.00 auth=1.0 `A=preprint`
- A #642: [2020] EASE: EM-Assisted Source Extraction from calcium imaging data  (19 cites)
- B #964: [2020] GTree: an Open-source Tool for Dense Reconstruction of Brain-wide Neuronal Population  (49 cites)
- Decision: ___________

**386.** conf=0.538 title=0.85 cit=0.36 auth=0.0 `diff_DOIs`
- A #9999: [2024] A neurotransmitter atlas of the nervous system of C. elegans males and hermaphrodites  (3 cites)
- B #9999: [2024] A neurotransmitter atlas of C. elegans males and hermaphrodites  (20 cites)
- Decision: ___________

**387.** conf=0.538 title=0.85 cit=0.36 auth=0.0 `diff_DOIs`
- A #9999: [2024] A neurotransmitter atlas of the nervous system of C. elegans males and hermaphrodites  (3 cites)
- B #9999: [2024] A neurotransmitter atlas of C. elegans males and hermaphrodites  (2 cites)
- Decision: ___________

**388.** conf=0.537 title=0.82 cit=0.40 auth=1.0 `diff_DOIs`
- A #312: [2006] Surface-wave array tomography in SE Tibet from ambient seismic noise and two-station analy  (1020 cites)
- B #723: [2008] Surface wave array tomography in SE Tibet from ambient seismic noise and two-station analy  (551 cites)
- Decision: ___________

**389.** conf=0.537 title=0.40 cit=0.39 auth=1.0 `diff_DOIs`
- A #364: [2020] Tissue clearing and its applications in neuroscience  (616 cites)
- B #1090: [2020] Whole-Brain Profiling of Cells and Circuits in Mammals by Tissue Clearing and Light-Sheet   (226 cites)
- Decision: ___________

**390.** conf=0.536 title=0.37 cit=0.03 auth=1.0 `B=preprint`
- A #1442: [2023] Functional imaging and quantification of multineuronal olfactory responses in <i>C. elegan  (51 cites)
- B #157: [2023] Network Statistics of the Whole-Brain Connectome of <i>Drosophila</i>  (29 cites)
- Decision: ___________

**391.** conf=0.536 title=0.92 cit=0.05 auth=0.0 `diff_DOIs`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of <i>Drosophila</i> larvae  (1 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of <i>Drosophila</i> larvae  (0 cites)
- Decision: ___________

**392.** conf=0.535 title=0.39 cit=0.00 auth=1.0 `B=preprint`
- A #1462: [2019] UNet++: Redesigning Skip Connections to Exploit Multiscale Features in Image Segmentation  (3913 cites)
- B #642: [2020] EASE: EM-Assisted Source Extraction from calcium imaging data  (19 cites)
- Decision: ___________

**393.** conf=0.534 title=0.61 cit=0.28 auth=0.0 `A=preprint`
- A #816: [2024] Comparative connectomics of the descending and ascending neurons of the <i>Drosophila</i>   (24 cites)
- B #9999: [2025] Comparative connectomics of Drosophila descending and ascending neurons  (26 cites)
- Decision: ___________

**394.** conf=0.531 title=1.00 cit=0.12 auth=0.0 `diff_DOIs`
- A #9999: [2020] Viv: Multiscale Visualization of High-Resolution Multiplexed Bioimaging Data on the Web  (14 cites)
- B #1416: [2022] Viv: multiscale visualization of high-resolution multiplexed bioimaging data on the web  (62 cites)
- Decision: ___________

**395.** conf=0.531 title=1.00 cit=0.12 auth=0.0 `diff_DOIs`
- A #9999: [2025] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- B #9999: [2025] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- Decision: ___________

**396.** conf=0.531 title=1.00 cit=0.12 auth=0.0 `diff_DOIs`
- A #9999: [2025] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- B #9999: [2025] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- Decision: ___________

**397.** conf=0.531 title=1.00 cit=0.12 auth=0.0 `diff_DOIs`
- A #832: [2019] A Cellular-Resolution Atlas of the Larval Zebrafish Brain  (283 cites)
- B #9999: [2018] A Cellular-Resolution Atlas of the Larval Zebrafish Brain  (12 cites)
- Decision: ___________

**398.** conf=0.531 title=0.32 cit=0.07 auth=1.0 `A=preprint`
- A #345: [2019] Automated Reconstruction of a Serial-Section EM <i>Drosophila</i> Brain with Flood-Filling  (70 cites)
- B #17: [2020] The connectome of the adult Drosophila mushroom body provides insights into function  (418 cites)
- Decision: ___________

**399.** conf=0.529 title=0.56 cit=0.33 auth=0.0 `A=preprint`
- A #9999: [2020] Neuroscience Cloud Analysis As a Service  (20 cites)
- B #9999: [2022] Neuroscience Cloud Analysis As a Service: An open-source platform for scalable, reproducib  (38 cites)
- Decision: ___________

**400.** conf=0.529 title=0.50 cit=0.21 auth=1.0 `diff_DOIs`
- A #774: [2012] Beyond the connectome: How neuromodulators shape neural circuits  (533 cites)
- B #393: [2013] From the connectome to brain function  (597 cites)
- Decision: ___________

**401.** conf=0.529 title=0.35 cit=0.03 auth=1.0 `A=preprint`
- A #1276: [2020] Transforming representations of movement from body- to world-centric space  (22 cites)
- B #193: [2022] En bloc preparation of Drosophila brains enables high-throughput FIB-SEM connectomics  (20 cites)
- Decision: ___________

**402.** conf=0.528 title=0.37 cit=0.00 auth=1.0 `A=preprint`
- A #345: [2019] Automated Reconstruction of a Serial-Section EM <i>Drosophila</i> Brain with Flood-Filling  (70 cites)
- B #1133: [2021] A Survey of Convolutional Neural Networks: Analysis, Applications, and Prospects  (4580 cites)
- Decision: ___________

**403.** conf=0.528 title=1.00 cit=0.11 auth=0.0 `diff_DOIs`
- A #9999: [2025] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- B #9999: [2026] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- Decision: ___________

**404.** conf=0.528 title=1.00 cit=0.11 auth=0.0 `diff_DOIs`
- A #9999: [2025] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- B #9999: [2026] A three-dimensional immunofluorescence atlas of the brain of the hackled-orb weaver spider  (0 cites)
- Decision: ___________

**405.** conf=0.527 title=0.35 cit=0.01 auth=1.0 `B=preprint`
- A #1779: [2019] Automated Reconstruction of a Serial-Section EM Drosophila Brain with Flood-Filling Networ  (65 cites)
- B #188: [2020] The connectome of the adult <i>Drosophila</i> mushroom body: implications for function  (19 cites)
- Decision: ___________

**406.** conf=0.525 title=0.36 cit=0.00 auth=1.0 `A=preprint`
- A #188: [2020] The connectome of the adult <i>Drosophila</i> mushroom body: implications for function  (19 cites)
- B #1133: [2021] A Survey of Convolutional Neural Networks: Analysis, Applications, and Prospects  (4580 cites)
- Decision: ___________

**407.** conf=0.524 title=0.34 cit=0.02 auth=1.0 `A=preprint`
- A #1458: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (5 cites)
- B #1171: [2020] Visual Input into the Drosophila melanogaster Mushroom Body  (40 cites)
- Decision: ___________

**408.** conf=0.524 title=0.29 cit=0.09 auth=1.0 `B=preprint`
- A #620: [2017] Automated synaptic connectivity inference for volume electron microscopy  (152 cites)
- B #868: [2019] Binary and analog variation of synapses between cortical pyramidal neurons  (64 cites)
- Decision: ___________

**409.** conf=0.522 title=0.89 cit=0.45 auth=0.0 `A=preprint`
- A #1887: [2020] Chemoreceptor Co-Expression in <i>Drosophila</i> Olfactory Neurons  (28 cites)
- B #9999: [2021] Chemoreceptor co-expression in Drosophila melanogaster olfactory neurons.  (119 cites)
- Decision: ___________

**410.** conf=0.521 title=0.35 cit=0.00 auth=1.0 `B=preprint`
- A #807: [2021] Machinery, regulation and pathophysiological implications of autophagosome maturation  (527 cites)
- B #1835: [2022] Eye structure shapes neuron function in <i>Drosophila</i> motion vision  (30 cites)
- Decision: ___________

**411.** conf=0.521 title=0.31 cit=0.05 auth=1.0 `A=preprint`
- A #123: [2023] Neuronal wiring diagram of an adult brain  (165 cites)
- B #720: [2025] CAVE: Connectome Annotation Versioning Engine  (32 cites)
- Decision: ___________

**412.** conf=0.520 title=0.29 cit=0.08 auth=1.0 `A=preprint`
- A #124: [2020] FlyWire: Online community for whole-brain connectomics  (70 cites)
- B #39: [2022] Binary and analog variation of synapses between cortical pyramidal neurons  (100 cites)
- Decision: ___________

**413.** conf=0.519 title=0.32 cit=0.03 auth=1.0 `A=preprint`
- A #254: [2020] Multiscale and multimodal reconstruction of cortical structure and function  (42 cites)
- B #552: [2021] The connectome predicts resting-state functional connectivity across the Drosophila brain  (36 cites)
- Decision: ___________

**414.** conf=0.519 title=0.34 cit=0.00 auth=1.0 `B=preprint`
- A #735: [2020] Ferroptosis: past, present and future  (3937 cites)
- B #1458: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (5 cites)
- Decision: ___________

**415.** conf=0.518 title=0.34 cit=0.00 auth=1.0 `B=preprint`
- A #127: [2020] A pneumonia outbreak associated with a new coronavirus of probable bat origin  (23190 cites)
- B #642: [2020] EASE: EM-Assisted Source Extraction from calcium imaging data  (19 cites)
- Decision: ___________

**416.** conf=0.518 title=0.75 cit=0.42 auth=1.0 `diff_DOIs`
- A #1114: [2020] Circuit and Behavioral Mechanisms of Sexual Rejection by Drosophila Females  (85 cites)
- B #353: [2020] Neural circuit mechanisms of sexual receptivity in Drosophila females  (170 cites)
- Decision: ___________

**417.** conf=0.518 title=0.90 cit=0.21 auth=1.0 `diff_DOIs`
- A #647: [2015] Global, regional, and national incidence, prevalence, and years lived with disability for   (6465 cites)
- B #488: [2016] Global, regional, and national incidence, prevalence, and years lived with disability for   (7320 cites)
- Decision: ___________

**418.** conf=0.517 title=1.00 cit=0.07 auth=0.0 `diff_DOIs`
- A #9999: [2020] Retinal Connectomics  (0 cites)
- B #9999: [2017] Retinal Connectomics  (0 cites)
- Decision: ___________

**419.** conf=0.516 title=1.00 cit=0.26 auth=0.0 `A=preprint`
- A #9999: [2022] Reward expectations direct learning and drive operant matching in <i>Drosophila</i>  (12 cites)
- B #9999: [2023] Reward expectations direct learning and drive operant matching in <i>Drosophila</i>  (19 cites)
- Decision: ___________

**420.** conf=0.516 title=0.33 cit=0.00 auth=1.0 `A=preprint`
- A #10: [2020] A Connectome of the Adult <i>Drosophila</i> Central Brain  (147 cites)
- B #1870: [2020] The Role of Autophagy in Gastric Cancer Chemoresistance: Friend or Foe?  (65 cites)
- Decision: ___________

**421.** conf=0.515 title=0.28 cit=0.07 auth=1.0 `B=preprint`
- A #1779: [2019] Automated Reconstruction of a Serial-Section EM Drosophila Brain with Flood-Filling Networ  (65 cites)
- B #1458: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (5 cites)
- Decision: ___________

**422.** conf=0.515 title=0.51 cit=0.14 auth=1.0 `diff_DOIs`
- A #1202: [2003] Economic small-world behavior in weighted networks  (765 cites)
- B #309: [2001] Efficient Behavior of Small-World Networks  (5061 cites)
- Decision: ___________

**423.** conf=0.514 title=0.53 cit=0.31 auth=1.0 `B=preprint`
- A #64: [2020] Recurrent architecture for adaptive regulation of learning in the insect brain  (183 cites)
- B #634: [2020] Circuits for integrating learnt and innate valences in the fly brain  (18 cites)
- Decision: ___________

**424.** conf=0.514 title=0.28 cit=0.07 auth=1.0 `diff_DOIs`
- A #71: [2011] Wiring specificity in the direction-selectivity circuit of the retina  (931 cites)
- B #844: [2009] Maximin affinity learning of image segmentation  (69 cites)
- Decision: ___________

**425.** conf=0.513 title=0.32 cit=0.01 auth=1.0 `A=preprint`
- A #188: [2020] The connectome of the adult <i>Drosophila</i> mushroom body: implications for function  (19 cites)
- B #389: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (15 cites)
- Decision: ___________

**426.** conf=0.512 title=0.78 cit=0.36 auth=0.0 `diff_DOIs`
- A #9999: [2014] Structural Controllability and Controlling Centrality of Temporal Networks  (63 cites)
- B #9999: [2014] Structural controllability of temporal networks  (84 cites)
- Decision: ___________

**427.** conf=0.511 title=1.00 cit=0.04 auth=0.0 `diff_DOIs`
- A #9999: [2010] Cortical hubs form a module for multisensory integration on top of the hierarchy of cortic  (349 cites)
- B #9999: [2010] Cortical hubs form a module for multisensory integration on top of the hierarchy of cortic  (17 cites)
- Decision: ___________

**428.** conf=0.510 title=0.47 cit=0.18 auth=1.0 `diff_DOIs`
- A #875: [2017] The comprehensive connectome of a neural substrate for ‘ON’ motion detection in Drosophila  (230 cites)
- B #306: [2017] A connectome of a learning and memory center in the adult Drosophila brain  (391 cites)
- Decision: ___________

**429.** conf=0.509 title=0.85 cit=0.25 auth=0.0 `diff_DOIs`
- A #9999: [2023] Multiplexed volumetric CLEM enabled by antibody derivatives provides new insights into the  (0 cites)
- B #9999: [2024] Multiplexed volumetric CLEM enabled by scFvs provides insights into the cytology of cerebe  (8 cites)
- Decision: ___________

**430.** conf=0.509 title=0.31 cit=0.00 auth=1.0 `B=preprint`
- A #1714: [2020] The effect of network thresholding and weighting on structural brain networks in the UK Bi  (129 cites)
- B #956: [2021] Oligodendrocyte precursor cells prune axons in the mouse neocortex  (19 cites)
- Decision: ___________

**431.** conf=0.509 title=0.31 cit=0.00 auth=1.0 `B=preprint`
- A #1623: [2017] The fundamental advantages of temporal networks  (491 cites)
- B #345: [2019] Automated Reconstruction of a Serial-Section EM <i>Drosophila</i> Brain with Flood-Filling  (70 cites)
- Decision: ___________

**432.** conf=0.509 title=0.42 cit=0.25 auth=1.0 `diff_DOIs`
- A #668: [2020] Autophagy and microbial pathogenesis  (81 cites)
- B #1929: [2020] Autophagy Pathways in CNS Myeloid Cell Immune Functions  (14 cites)
- Decision: ___________

**433.** conf=0.508 title=0.31 cit=0.00 auth=1.0 `B=preprint`
- A #1038: [2018] 30 Years of Lithium‐Ion Batteries  (5776 cites)
- B #1458: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (5 cites)
- Decision: ___________

**434.** conf=0.507 title=0.76 cit=0.36 auth=0.0 `diff_DOIs`
- A #1511: [2024] Transforming descending input into behavior: The organization of premotor circuits in the   (45 cites)
- B #9999: [2025] Transforming descending input into motor output: An analysis of the Drosophila Male Adult   (1 cites)
- Decision: ___________

**435.** conf=0.507 title=0.31 cit=0.00 auth=1.0 `B=preprint`
- A #621: [2017] MotionCor2: anisotropic correction of beam-induced motion for improved cryo-electron micro  (8716 cites)
- B #1092: [2017] A complete electron microscopy volume of the brain of adult <i>Drosophila melanogaster</i>  (52 cites)
- Decision: ___________

**436.** conf=0.506 title=0.30 cit=0.00 auth=1.0 `B=preprint`
- A #807: [2021] Machinery, regulation and pathophysiological implications of autophagosome maturation  (527 cites)
- B #1755: [2023] A comprehensive neuroanatomical survey of the <i>Drosophila</i> Lobula Plate Tangential Ne  (15 cites)
- Decision: ___________

**437.** conf=0.504 title=0.43 cit=0.22 auth=1.0 `diff_DOIs`
- A #279: [2002] Assortative Mixing in Networks  (5003 cites)
- B #186: [2004] Finding and evaluating community structure in networks  (13957 cites)
- Decision: ___________

**438.** conf=0.504 title=0.22 cit=0.11 auth=1.0 `A=preprint`
- A #1517: [2022] Multi-Layered Maps of Neuropil with Segmentation-Guided Contrastive Learning  (16 cites)
- B #39: [2022] Binary and analog variation of synapses between cortical pyramidal neurons  (100 cites)
- Decision: ___________

**439.** conf=0.503 title=0.69 cit=0.05 auth=0.0 `A=preprint`
- A #9999: [2019] Structure and function of a neocortical synapse  (22 cites)
- B #115: [2021] Structure and function of axo-axonic inhibition  (90 cites)
- Decision: ___________

**440.** conf=0.501 title=0.55 cit=0.23 auth=0.0 `A=preprint`
- A #9999: [2018] Oxygen plasma focused ion beam scanning electron microscopy for biological samples  (32 cites)
- B #9999: [2021] Oxygen Plasma Focused Ion Beam: Optimised Beam Chemistry to Improve the Throughput of FIB/  (0 cites)
- Decision: ___________

**441.** conf=0.501 title=0.29 cit=0.00 auth=1.0 `B=preprint`
- A #612: [2020] A unified connectomic target for deep brain stimulation in obsessive-compulsive disorder  (322 cites)
- B #188: [2020] The connectome of the adult <i>Drosophila</i> mushroom body: implications for function  (19 cites)
- Decision: ___________

**442.** conf=0.501 title=0.68 cit=0.44 auth=0.0 `diff_DOIs`
- A #9999: [2007] Surface wave tomography of the western United States from ambient seismic noise: Rayleigh   (208 cites)
- B #9999: [2008] Surface wave tomography of China from ambient seismic noise correlation  (164 cites)
- Decision: ___________

**443.** conf=0.500 title=0.57 cit=0.20 auth=1.0 `B=preprint`
- A #290: [2020] Light microscopy of proteins in their ultrastructural context  (204 cites)
- B #355: [2022] All-optical visualization of specific molecules in the ultrastructural context of brain ti  (38 cites)
- Decision: ___________

## REVIEW (243 pairs)

**1.** conf=0.498 title=0.57 cit=0.19 auth=0.0 `A=preprint`
- A #9999: [2023] Connectomic reconstruction predicts the functional organization of visual inputs to the na  (14 cites)
- B #1539: [2024] Connectomic reconstruction predicts visual features used for navigation  (25 cites)
- Decision: ___________

**2.** conf=0.498 title=0.28 cit=0.00 auth=1.0 `A=preprint`
- A #345: [2019] Automated Reconstruction of a Serial-Section EM <i>Drosophila</i> Brain with Flood-Filling  (70 cites)
- B #612: [2020] A unified connectomic target for deep brain stimulation in obsessive-compulsive disorder  (322 cites)
- Decision: ___________

**3.** conf=0.497 title=0.93 cit=0.08 auth=1.0 `diff_DOIs`
- A #488: [2016] Global, regional, and national incidence, prevalence, and years lived with disability for   (7320 cites)
- B #358: [2017] Global, regional, and national incidence, prevalence, and years lived with disability for   (13428 cites)
- Decision: ___________

**4.** conf=0.496 title=0.27 cit=0.00 auth=1.0 `B=preprint`
- A #1038: [2018] 30 Years of Lithium‐Ion Batteries  (5776 cites)
- B #345: [2019] Automated Reconstruction of a Serial-Section EM <i>Drosophila</i> Brain with Flood-Filling  (70 cites)
- Decision: ___________

**5.** conf=0.495 title=0.24 cit=0.05 auth=1.0 `B=preprint`
- A #67: [2021] FlyWire: online community for whole-brain connectomics  (284 cites)
- B #1517: [2022] Multi-Layered Maps of Neuropil with Segmentation-Guided Contrastive Learning  (16 cites)
- Decision: ___________

**6.** conf=0.494 title=0.38 cit=0.04 auth=1.0 `diff_DOIs`
- A #345: [2019] Automated Reconstruction of a Serial-Section EM <i>Drosophila</i> Brain with Flood-Filling  (70 cites)
- B #188: [2020] The connectome of the adult <i>Drosophila</i> mushroom body: implications for function  (19 cites)
- Decision: ___________

**7.** conf=0.494 title=0.27 cit=0.00 auth=1.0 `B=preprint`
- A #1038: [2018] 30 Years of Lithium‐Ion Batteries  (5776 cites)
- B #188: [2020] The connectome of the adult <i>Drosophila</i> mushroom body: implications for function  (19 cites)
- Decision: ___________

**8.** conf=0.493 title=1.00 cit=0.57 auth=0.0 `diff_DOIs`
- A #231: [1999] Cortical Surface-Based Analysis  (6372 cites)
- B #150: [1999] Cortical Surface-Based Analysis  (11343 cites)
- Decision: ___________

**9.** conf=0.492 title=0.23 cit=0.05 auth=1.0 `A=preprint`
- A #123: [2023] Neuronal wiring diagram of an adult brain  (165 cites)
- B #562: [2023] Multi-layered maps of neuropil with segmentation-guided contrastive learning  (27 cites)
- Decision: ___________

**10.** conf=0.490 title=0.26 cit=0.00 auth=1.0 `B=preprint`
- A #1522: [2022] Data-Efficient Brain Connectome Analysis via Multi-Task Meta-Learning  (18 cites)
- B #1960: [2023] Fine-grained descending control of steering in walking <i>Drosophila</i>  (17 cites)
- Decision: ___________

**11.** conf=0.490 title=0.26 cit=0.00 auth=1.0 `A=preprint`
- A #1276: [2020] Transforming representations of movement from body- to world-centric space  (22 cites)
- B #1737: [2022] Extrasynaptic signaling enables an asymmetric juvenile motor circuit to produce symmetric   (28 cites)
- Decision: ___________

**12.** conf=0.489 title=0.23 cit=0.04 auth=1.0 `A=preprint`
- A #1517: [2022] Multi-Layered Maps of Neuropil with Segmentation-Guided Contrastive Learning  (16 cites)
- B #6: [2024] Neuronal wiring diagram of an adult brain  (447 cites)
- Decision: ___________

**13.** conf=0.489 title=0.30 cit=0.33 auth=1.0 `diff_DOIs`
- A #1477: [2020] Expansion Microscopy for Cell Biology Analysis in Fungi  (52 cites)
- B #1391: [2020] Nanoscale imaging of bacterial infections by sphingolipid expansion microscopy  (78 cites)
- Decision: ___________

**14.** conf=0.488 title=0.92 cit=0.06 auth=0.0 `diff_DOIs`
- A #9999: [2025] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of Drosophila larvae  (0 cites)
- Decision: ___________

**15.** conf=0.488 title=0.92 cit=0.06 auth=0.0 `diff_DOIs`
- A #9999: [2025] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of Drosophila larvae  (0 cites)
- Decision: ___________

**16.** conf=0.488 title=0.39 cit=0.01 auth=1.0 `diff_DOIs`
- A #1458: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (5 cites)
- B #188: [2020] The connectome of the adult <i>Drosophila</i> mushroom body: implications for function  (19 cites)
- Decision: ___________

**17.** conf=0.487 title=0.24 cit=0.01 auth=1.0 `B=preprint`
- A #1850: [2017] TDat: An Efficient Platform for Processing Petabyte-Scale Whole-Brain Volumetric Images  (63 cites)
- B #345: [2019] Automated Reconstruction of a Serial-Section EM <i>Drosophila</i> Brain with Flood-Filling  (70 cites)
- Decision: ___________

**18.** conf=0.487 title=0.66 cit=0.02 auth=0.0 `A=preprint`
- A #41: [2020] Neural circuit mechanisms for steering control in <i>walking Drosophila</i>  (75 cites)
- B #353: [2020] Neural circuit mechanisms of sexual receptivity in Drosophila females  (170 cites)
- Decision: ___________

**19.** conf=0.487 title=0.92 cit=0.06 auth=0.0 `diff_DOIs`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of Drosophila larvae  (0 cites)
- Decision: ___________

**20.** conf=0.487 title=0.92 cit=0.06 auth=0.0 `diff_DOIs`
- A #9999: [2023] Morphology and ultrastructure of external sense organs of Drosophila larvae  (2 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of Drosophila larvae  (0 cites)
- Decision: ___________

**21.** conf=0.486 title=0.48 cit=0.08 auth=1.0 `diff_DOIs`
- A #1171: [2020] Visual Input into the Drosophila melanogaster Mushroom Body  (40 cites)
- B #17: [2020] The connectome of the adult Drosophila mushroom body provides insights into function  (418 cites)
- Decision: ___________

**22.** conf=0.485 title=0.24 cit=0.00 auth=1.0 `B=preprint`
- A #735: [2020] Ferroptosis: past, present and future  (3937 cites)
- B #188: [2020] The connectome of the adult <i>Drosophila</i> mushroom body: implications for function  (19 cites)
- Decision: ___________

**23.** conf=0.485 title=0.92 cit=0.05 auth=0.0 `diff_DOIs`
- A #9999: [2024] Morphology and ultrastructure of external sense organs of Drosophila larvae  (3 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of Drosophila larvae  (0 cites)
- Decision: ___________

**24.** conf=0.485 title=0.92 cit=0.05 auth=0.0 `diff_DOIs`
- A #9999: [2024] Morphology and ultrastructure of external sense organs of Drosophila larvae  (3 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of Drosophila larvae  (0 cites)
- Decision: ___________

**25.** conf=0.484 title=0.24 cit=0.00 auth=1.0 `B=preprint`
- A #1269: [2021] Ciliary Type III Adenylyl Cyclase in the VMH Is Crucial for High‐Fat Diet‐Induced Obesity   (12 cites)
- B #1960: [2023] Fine-grained descending control of steering in walking <i>Drosophila</i>  (17 cites)
- Decision: ___________

**26.** conf=0.483 title=0.22 cit=0.02 auth=1.0 `A=preprint`
- A #345: [2019] Automated Reconstruction of a Serial-Section EM <i>Drosophila</i> Brain with Flood-Filling  (70 cites)
- B #1171: [2020] Visual Input into the Drosophila melanogaster Mushroom Body  (40 cites)
- Decision: ___________

**27.** conf=0.481 title=0.66 cit=0.00 auth=0.0 `B=preprint`
- A #9999: [2023] Spatial transcriptomics in neuroscience  (50 cites)
- B #9999: [2023] Spatial transcriptomics in the adult <i>Drosophila</i> brain and body  (1 cites)
- Decision: ___________

**28.** conf=0.481 title=0.89 cit=0.08 auth=0.0 `diff_DOIs`
- A #9999: [2014] Structural controllability of temporal networks  (84 cites)
- B #9999: [2016] Structural Controllability of Temporally Switching Networks  (65 cites)
- Decision: ___________

**29.** conf=0.480 title=0.32 cit=0.27 auth=1.0 `diff_DOIs`
- A #567: [2021] Electron Microscopic Reconstruction of Neural Circuitry in the Cochlea  (73 cites)
- B #1345: [2022] Connectomic analysis of thalamus-driven disinhibition in cortical layer 4  (26 cites)
- Decision: ___________

**30.** conf=0.480 title=0.23 cit=0.00 auth=1.0 `A=preprint`
- A #345: [2019] Automated Reconstruction of a Serial-Section EM <i>Drosophila</i> Brain with Flood-Filling  (70 cites)
- B #735: [2020] Ferroptosis: past, present and future  (3937 cites)
- Decision: ___________

**31.** conf=0.479 title=0.51 cit=0.00 auth=1.0 `diff_DOIs`
- A #1501: [2016] Wireless communications with unmanned aerial vehicles: opportunities and challenges  (3965 cites)
- B #682: [2017] Neuronal cell-type classification: challenges, opportunities and the path forward  (921 cites)
- Decision: ___________

**32.** conf=0.477 title=0.18 cit=0.06 auth=1.0 `B=preprint`
- A #535: [2018] Progress and remaining challenges in high-throughput volume electron microscopy  (130 cites)
- B #98: [2020] An anatomical substrate of credit assignment in reinforcement learning  (36 cites)
- Decision: ___________

**33.** conf=0.476 title=0.43 cit=0.11 auth=1.0 `diff_DOIs`
- A #1613: [2020] The interplay of autophagy and non-apoptotic cell death pathways  (49 cites)
- B #1172: [2021] Autophagy and organelle homeostasis in cancer  (228 cites)
- Decision: ___________

**34.** conf=0.476 title=0.80 cit=0.18 auth=0.0 `diff_DOIs`
- A #9999: [2016] Structural Controllability of Temporally Switching Networks  (65 cites)
- B #1906: [2018] Structural Controllability of Symmetric Networks  (65 cites)
- Decision: ___________

**35.** conf=0.475 title=0.36 cit=0.19 auth=1.0 `diff_DOIs`
- A #1438: [2009] Human brain networks in health and disease  (916 cites)
- B #1872: [2010] Efficient Physical Embedding of Topologically Complex Information Processing Networks in B  (427 cites)
- Decision: ___________

**36.** conf=0.474 title=0.90 cit=0.04 auth=0.0 `diff_DOIs`
- A #488: [2016] Global, regional, and national incidence, prevalence, and years lived with disability for   (7320 cites)
- B #396: [2018] Global, regional, and national incidence, prevalence, and years lived with disability for   (13807 cites)
- Decision: ___________

**37.** conf=0.473 title=0.39 cit=0.14 auth=1.0 `diff_DOIs`
- A #1287: [2013] Observability of complex systems  (521 cites)
- B #1763: [2012] Control Centrality and Hierarchical Structure in Complex Networks  (329 cites)
- Decision: ___________

**38.** conf=0.473 title=0.44 cit=0.28 auth=1.0 `A=preprint`
- A #1257: [2020] Molecular resolution imaging by post-labeling expansion single-molecule localization micro  (24 cites)
- B #1889: [2020] Tracking down the molecular architecture of the synaptonemal complex by expansion microsco  (52 cites)
- Decision: ___________

**39.** conf=0.469 title=0.47 cit=0.02 auth=1.0 `diff_DOIs`
- A #1680: [1995] Schizophrenia: a disconnection syndrome?  (1336 cites)
- B #534: [1994] Functional and effective connectivity in neuroimaging: A synthesis  (2479 cites)
- Decision: ___________

**40.** conf=0.469 title=0.20 cit=0.00 auth=1.0 `A=preprint`
- A #1458: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (5 cites)
- B #612: [2020] A unified connectomic target for deep brain stimulation in obsessive-compulsive disorder  (322 cites)
- Decision: ___________

**41.** conf=0.468 title=0.23 cit=0.35 auth=1.0 `diff_DOIs`
- A #1200: [2004] Sequence-independent segmentation of magnetic resonance images  (2161 cites)
- B #671: [2003] Automatically Parcellating the Human Cerebral Cortex  (4426 cites)
- Decision: ___________

**42.** conf=0.467 title=0.73 cit=0.25 auth=1.0 `diff_DOIs`
- A #1676: [2009] Hierarchical modularity in human brain functional networks  (688 cites)
- B #1230: [2008] Age-related changes in modular organization of human brain functional networks  (781 cites)
- Decision: ___________

**43.** conf=0.467 title=0.19 cit=0.00 auth=1.0 `A=preprint`
- A #1421: [2018] A genetic, genomic, and computational resource for exploring neural circuit function  (43 cites)
- B #1670: [2018] Simple statistical identification and removal of contaminant sequences in marker-gene and   (3403 cites)
- Decision: ___________

**44.** conf=0.466 title=0.43 cit=0.06 auth=1.0 `diff_DOIs`
- A #1086: [2022] Anatomical distribution and functional roles of electrical synapses in Drosophila  (54 cites)
- B #1507: [2023] Multilevel visual motion opponency in Drosophila  (13 cites)
- Decision: ___________

**45.** conf=0.465 title=0.58 cit=0.05 auth=0.0 `A=preprint`
- A #41: [2020] Neural circuit mechanisms for steering control in <i>walking Drosophila</i>  (75 cites)
- B #9999: [2023] Neural circuit mechanisms for transforming learned olfactory valences into wind-oriented m  (31 cites)
- Decision: ___________

**46.** conf=0.465 title=0.61 cit=0.01 auth=0.0 `A=preprint`
- A #1158: [2024] Connectomic reconstruction of a cortical column  (26 cites)
- B #609: [2024] Connectomic reconstruction of a female Drosophila ventral nerve cord  (98 cites)
- Decision: ___________

**47.** conf=0.465 title=0.14 cit=0.07 auth=1.0 `A=preprint`
- A #98: [2020] An anatomical substrate of credit assignment in reinforcement learning  (36 cites)
- B #1563: [2020] Image Processing for Volume Electron Microscopy  (6 cites)
- Decision: ___________

**48.** conf=0.464 title=0.57 cit=0.05 auth=0.0 `B=preprint`
- A #9999: [2022] Volume electron microscopy reveals age-related circuit remodeling in the auditory brainste  (5 cites)
- B #9999: [2023] Volume Electron Microscopy Reveals Unique Laminar Synaptic Characteristics in the Human En  (2 cites)
- Decision: ___________

**49.** conf=0.464 title=0.17 cit=0.03 auth=1.0 `diff_DOIs`
- A #167: [2011] Volume electron microscopy for neuronal circuit reconstruction  (346 cites)
- B #844: [2009] Maximin affinity learning of image segmentation  (69 cites)
- Decision: ___________

**50.** conf=0.463 title=0.41 cit=0.08 auth=1.0 `diff_DOIs`
- A #1951: [2012] Computational methods and challenges for large-scale circuit mapping  (75 cites)
- B #27: [2013] Connectomic reconstruction of the inner plexiform layer in the mouse retina  (1074 cites)
- Decision: ___________

**51.** conf=0.463 title=0.77 cit=0.18 auth=1.0 `diff_DOIs`
- A #1233: [2007] Studying the human brain anatomical network via diffusion-weighted MRI and Graph Theory  (513 cites)
- B #1838: [2007] Characterizing brain anatomical connections using diffusion weighted MRI and graph theory  (351 cites)
- Decision: ___________

**52.** conf=0.463 title=0.74 cit=0.21 auth=1.0 `diff_DOIs`
- A #186: [2004] Finding and evaluating community structure in networks  (13957 cites)
- B #225: [2006] Modularity and community structure in networks  (12046 cites)
- Decision: ___________

**53.** conf=0.462 title=0.36 cit=0.15 auth=1.0 `diff_DOIs`
- A #175: [2020] Transforming FIB-SEM Systems for Large-Volume Connectomics and Cell Biology  (29 cites)
- B #350: [2021] An open-access volume electron microscopy atlas of whole cells and tissues  (196 cites)
- Decision: ___________

**54.** conf=0.462 title=0.61 cit=0.00 auth=0.0 `A=preprint`
- A #9999: [2024] Synaptic architecture of a memory engram in the mouse hippocampus  (11 cites)
- B #1150: [2024] Synaptic architecture of leg and wing premotor control networks in Drosophila  (65 cites)
- Decision: ___________

**55.** conf=0.461 title=0.59 cit=0.02 auth=0.0 `A=preprint`
- A #1158: [2024] Connectomic reconstruction of a cortical column  (26 cites)
- B #1539: [2024] Connectomic reconstruction predicts visual features used for navigation  (25 cites)
- Decision: ___________

**56.** conf=0.461 title=0.77 cit=0.17 auth=1.0 `diff_DOIs`
- A #557: [2018] Imaging cellular ultrastructures using expansion microscopy (U-ExM)  (570 cites)
- B #1132: [2020] Ultrastructure expansion microscopy (U-ExM)  (160 cites)
- Decision: ___________

**57.** conf=0.461 title=0.17 cit=0.00 auth=1.0 `A=preprint`
- A #10: [2020] A Connectome of the Adult <i>Drosophila</i> Central Brain  (147 cites)
- B #70: [2020] Cross-species functional alignment reveals evolutionary hierarchy within the connectome  (265 cites)
- Decision: ___________

**58.** conf=0.461 title=0.33 cit=0.18 auth=1.0 `diff_DOIs`
- A #1872: [2010] Efficient Physical Embedding of Topologically Complex Information Processing Networks in B  (427 cites)
- B #1621: [2009] Cognitive fitness of cost-efficient brain functional networks  (449 cites)
- Decision: ___________

**59.** conf=0.460 title=0.58 cit=0.03 auth=0.0 `A=preprint`
- A #1952: [2023] Synaptic architecture of leg and wing premotor control networks in <i>Drosophila</i>  (18 cites)
- B #9999: [2025] Synaptic architecture of a memory engram in the mouse hippocampus  (24 cites)
- Decision: ___________

**60.** conf=0.459 title=0.16 cit=0.01 auth=1.0 `A=preprint`
- A #1458: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (5 cites)
- B #17: [2020] The connectome of the adult Drosophila mushroom body provides insights into function  (418 cites)
- Decision: ___________

**61.** conf=0.459 title=0.64 cit=0.34 auth=1.0 `diff_DOIs`
- A #226: [2001] A global optimisation method for robust affine registration of brain images  (7138 cites)
- B #263: [2002] Improved Optimization for the Robust and Accurate Linear Registration and Motion Correctio  (9496 cites)
- Decision: ___________

**62.** conf=0.459 title=0.60 cit=0.00 auth=0.0 `A=preprint`
- A #9999: [2022] Connectomic analysis of thalamus-driven disinhibition in cortical layer 4  (3 cites)
- B #9999: [2025] Connectomic analysis of taste circuits in Drosophila  (12 cites)
- Decision: ___________

**63.** conf=0.458 title=0.77 cit=0.16 auth=0.0 `diff_DOIs`
- A #1132: [2020] Ultrastructure expansion microscopy (U-ExM)  (160 cites)
- B #9999: [2021] Ultrastructure expansion microscopy in <i>Trypanosoma brucei</i>  (50 cites)
- Decision: ___________

**64.** conf=0.458 title=0.64 cit=0.34 auth=1.0 `diff_DOIs`
- A #244: [2002] Improved Optimization for the Robust and Accurate Linear Registration and Motion Correctio  (10589 cites)
- B #226: [2001] A global optimisation method for robust affine registration of brain images  (7138 cites)
- Decision: ___________

**65.** conf=0.457 title=0.42 cit=0.04 auth=1.0 `diff_DOIs`
- A #1529: [2008] Structural Insights into Aberrant Topological Patterns of Large-Scale Cortical Networks in  (988 cites)
- B #1968: [2008] Electrophysiological correlates of the brain's intrinsic large-scale functional architectu  (697 cites)
- Decision: ___________

**66.** conf=0.456 title=0.29 cit=0.23 auth=1.0 `diff_DOIs`
- A #850: [2008] Hierarchical Organization of Human Cortical Networks in Health and Schizophrenia  (1265 cites)
- B #1621: [2009] Cognitive fitness of cost-efficient brain functional networks  (449 cites)
- Decision: ___________

**67.** conf=0.456 title=0.60 cit=0.39 auth=1.0 `diff_DOIs`
- A #64: [2020] Recurrent architecture for adaptive regulation of learning in the insect brain  (183 cites)
- B #401: [2021] Circuits for integrating learned and innate valences in the insect brain  (62 cites)
- Decision: ___________

**68.** conf=0.455 title=0.44 cit=0.00 auth=1.0 `diff_DOIs`
- A #1891: [2022] Joint Embedding of Structural and Functional Brain Networks with Graph Neural Networks for  (39 cites)
- B #667: [2022] Strong Structural Controllability of Boolean Networks: Polynomial-Time Criteria, Minimal N  (110 cites)
- Decision: ___________

**69.** conf=0.455 title=0.69 cit=0.25 auth=0.0 `diff_DOIs`
- A #396: [2018] Global, regional, and national incidence, prevalence, and years lived with disability for   (13807 cites)
- B #746: [2021] Global, regional, and national burden of stroke and its risk factors, 1990–2019: a systema  (7183 cites)
- Decision: ___________

**70.** conf=0.454 title=0.31 cit=0.18 auth=1.0 `diff_DOIs`
- A #1438: [2009] Human brain networks in health and disease  (916 cites)
- B #1621: [2009] Cognitive fitness of cost-efficient brain functional networks  (449 cites)
- Decision: ___________

**71.** conf=0.453 title=0.72 cit=0.21 auth=0.0 `diff_DOIs`
- A #972: [2019] Global, regional, and national burden of neurological disorders, 1990–2016: a systematic a  (5555 cites)
- B #561: [2018] Global, regional, and national age-sex-specific mortality for 282 causes of death in 195 c  (8565 cites)
- Decision: ___________

**72.** conf=0.451 title=0.24 cit=0.07 auth=1.0 `diff_DOIs`
- A #124: [2020] FlyWire: Online community for whole-brain connectomics  (70 cites)
- B #1517: [2022] Multi-Layered Maps of Neuropil with Segmentation-Guided Contrastive Learning  (16 cites)
- Decision: ___________

**73.** conf=0.448 title=0.93 cit=0.49 auth=0.0 `diff_DOIs`
- A #9999: [2007] Surface wave tomography of the western United States from ambient seismic noise: Rayleigh   (208 cites)
- B #939: [2008] Surface wave tomography of the western United States from ambient seismic noise: Rayleigh   (812 cites)
- Decision: ___________

**74.** conf=0.448 title=0.42 cit=0.00 auth=1.0 `diff_DOIs`
- A #389: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (15 cites)
- B #1133: [2021] A Survey of Convolutional Neural Networks: Analysis, Applications, and Prospects  (4580 cites)
- Decision: ___________

**75.** conf=0.448 title=0.42 cit=0.00 auth=1.0 `diff_DOIs`
- A #97: [2020] Neural circuitry linking mating and egg laying in Drosophila females  (222 cites)
- B #1314: [2021] Neural representations of the amount and the delay time of reward in intertemporal decisio  (43 cites)
- Decision: ___________

**76.** conf=0.447 title=0.38 cit=0.05 auth=1.0 `diff_DOIs`
- A #1486: [2007] Reconstruction of an average cortical column in silico  (88 cites)
- B #256: [2008] 3D structural imaging of the brain with photons and electrons  (172 cites)
- Decision: ___________

**77.** conf=0.447 title=0.51 cit=0.08 auth=0.0 `A=preprint`
- A #9999: [2021] A neural circuit linking two sugar sensors regulates satiety-dependent fructose drive in <  (3 cites)
- B #9999: [2022] A neural circuit linking learning and sleep in Drosophila long-term memory  (31 cites)
- Decision: ___________

**78.** conf=0.447 title=0.60 cit=0.35 auth=1.0 `diff_DOIs`
- A #64: [2020] Recurrent architecture for adaptive regulation of learning in the insect brain  (183 cites)
- B #449: [2020] Circuits for integrating learned and innate valences in the insect brain.  (50 cites)
- Decision: ___________

**79.** conf=0.447 title=0.85 cit=0.00 auth=0.0 `diff_DOIs`
- A #647: [2015] Global, regional, and national incidence, prevalence, and years lived with disability for   (6465 cites)
- B #396: [2018] Global, regional, and national incidence, prevalence, and years lived with disability for   (13807 cites)
- Decision: ___________

**80.** conf=0.445 title=0.41 cit=0.00 auth=1.0 `diff_DOIs`
- A #859: [2019] Convolutional nets for reconstructing neural circuits from brain images acquired by serial  (59 cites)
- B #1695: [2021] A locomotor neural circuit persists and functions similarly in larvae and adult Drosophila  (47 cites)
- Decision: ___________

**81.** conf=0.444 title=0.29 cit=0.17 auth=1.0 `diff_DOIs`
- A #1654: [2020] Pik3c3 deficiency in myeloid cells imparts partial resistance to experimental autoimmune e  (22 cites)
- B #1269: [2021] Ciliary Type III Adenylyl Cyclase in the VMH Is Crucial for High‐Fat Diet‐Induced Obesity   (12 cites)
- Decision: ___________

**82.** conf=0.443 title=0.37 cit=0.05 auth=1.0 `diff_DOIs`
- A #1547: [2009] Uncovering Intrinsic Modular Organization of Spontaneous Brain Activity in Humans  (635 cites)
- B #1968: [2008] Electrophysiological correlates of the brain's intrinsic large-scale functional architectu  (697 cites)
- Decision: ___________

**83.** conf=0.443 title=0.74 cit=0.14 auth=1.0 `diff_DOIs`
- A #213: [2019] Whole-animal connectomes of both Caenorhabditis elegans sexes  (964 cites)
- B #475: [2020] The connectome of the <scp> <i>Caenorhabditis elegans</i> </scp> pharynx  (51 cites)
- Decision: ___________

**84.** conf=0.443 title=0.45 cit=0.14 auth=1.0 `B=preprint`
- A #82: [2021] Information flow, cell types and stereotypy in a full olfactory connectome  (182 cites)
- B #116: [2023] Whole-brain annotation and multi-connectome cell typing quantifies circuit stereotypy in <  (107 cites)
- Decision: ___________

**85.** conf=0.442 title=0.23 cit=0.05 auth=1.0 `diff_DOIs`
- A #1517: [2022] Multi-Layered Maps of Neuropil with Segmentation-Guided Contrastive Learning  (16 cites)
- B #123: [2023] Neuronal wiring diagram of an adult brain  (165 cites)
- Decision: ___________

**86.** conf=0.442 title=0.41 cit=0.00 auth=1.0 `diff_DOIs`
- A #1588: [2021] Three-dimensional residual channel attention networks denoise and sharpen fluorescence mic  (207 cites)
- B #1430: [2021] Deep-Learning-Based Automated Neuron Reconstruction From 3D Microscopy Images Using Synthe  (29 cites)
- Decision: ___________

**87.** conf=0.442 title=0.30 cit=0.14 auth=1.0 `diff_DOIs`
- A #1024: [2012] Globally Optimal Closed-Surface Segmentation for Connectomics  (101 cites)
- B #1743: [2011] 3D segmentation of SBFSEM images of neuropil by a graphical model over supervoxel boundari  (45 cites)
- Decision: ___________

**88.** conf=0.442 title=0.52 cit=0.04 auth=0.0 `B=preprint`
- A #9999: [2023] Comparative connectomics and escape behavior in larvae of closely related Drosophila speci  (16 cites)
- B #816: [2024] Comparative connectomics of the descending and ascending neurons of the <i>Drosophila</i>   (24 cites)
- Decision: ___________

**89.** conf=0.442 title=0.42 cit=0.17 auth=1.0 `B=preprint`
- A #274: [2023] A searchable image resource of Drosophila GAL4 driver expression patterns with single neur  (126 cites)
- B #1361: [2024] A split-GAL4 driver line resource for <i>Drosophila</i> neuron types  (13 cites)
- Decision: ___________

**90.** conf=0.440 title=0.76 cit=0.10 auth=0.0 `diff_DOIs`
- A #9999: [2016] Correlative light and electron microscopy methods for the study of virus–cell interactions  (99 cites)
- B #9999: [2016] Correlative Light and Electron Microscopy: Methods and Applications  (5 cites)
- Decision: ___________

**91.** conf=0.440 title=0.54 cit=0.00 auth=0.0 `A=preprint`
- A #9999: [2023] Volume Electron Microscopy Reveals Unique Laminar Synaptic Characteristics in the Human En  (2 cites)
- B #9999: [2024] Volume electron microscopy reveals age-related ultrastructural differences of globular bus  (0 cites)
- Decision: ___________

**92.** conf=0.439 title=0.77 cit=0.07 auth=0.0 `diff_DOIs`
- A #689: [2016] Global, regional, and national life expectancy, all-cause mortality, and cause-specific mo  (6646 cites)
- B #561: [2018] Global, regional, and national age-sex-specific mortality for 282 causes of death in 195 c  (8565 cites)
- Decision: ___________

**93.** conf=0.438 title=0.40 cit=0.00 auth=1.0 `diff_DOIs`
- A #1680: [1995] Schizophrenia: a disconnection syndrome?  (1336 cites)
- B #75: [1995] Spatial registration and normalization of images  (3748 cites)
- Decision: ___________

**94.** conf=0.438 title=0.76 cit=0.08 auth=0.0 `diff_DOIs`
- A #9999: [2013] Structural controllability of unidirectional bipartite networks  (101 cites)
- B #9999: [2014] Structural controllability of temporal networks  (84 cites)
- Decision: ___________

**95.** conf=0.438 title=1.00 cit=0.35 auth=0.0 `diff_DOIs`
- A #9999: [2014] Controllability metrics, limitations and algorithms for complex networks  (83 cites)
- B #1519: [2014] Controllability Metrics, Limitations and Algorithms for Complex Networks  (610 cites)
- Decision: ___________

**96.** conf=0.438 title=0.61 cit=0.29 auth=1.0 `diff_DOIs`
- A #97: [2020] Neural circuitry linking mating and egg laying in Drosophila females  (222 cites)
- B #353: [2020] Neural circuit mechanisms of sexual receptivity in Drosophila females  (170 cites)
- Decision: ___________

**97.** conf=0.437 title=0.38 cit=0.01 auth=1.0 `diff_DOIs`
- A #258: [2020] Conservation and divergence of related neuronal lineages in the Drosophila central brain  (59 cites)
- B #1695: [2021] A locomotor neural circuit persists and functions similarly in larvae and adult Drosophila  (47 cites)
- Decision: ___________

**98.** conf=0.437 title=0.37 cit=0.03 auth=1.0 `diff_DOIs`
- A #243: [2006] Wiring optimization can relate neuronal structure and function  (662 cites)
- B #1624: [2008] Revealing Modular Architecture of Human Brain Structural Networks by Using Cortical Thickn  (489 cites)
- Decision: ___________

**99.** conf=0.437 title=0.52 cit=0.02 auth=0.0 `B=preprint`
- A #9999: [2020] Volume electron microscopy: analyzing the lung  (32 cites)
- B #9999: [2023] Volume Electron Microscopy Reveals Unique Laminar Synaptic Characteristics in the Human En  (2 cites)
- Decision: ___________

**100.** conf=0.436 title=0.39 cit=0.00 auth=1.0 `diff_DOIs`
- A #176: [2021] DotMotif: an open-source tool for connectome subgraph isomorphism search and graph queries  (35 cites)
- B #1117: [2021] An Integrated Toolkit for Extensible and Reproducible Neuroscience  (13 cites)
- Decision: ___________

**101.** conf=0.436 title=0.52 cit=0.02 auth=0.0 `A=preprint`
- A #816: [2024] Comparative connectomics of the descending and ascending neurons of the <i>Drosophila</i>   (24 cites)
- B #9999: [2025] Comparative connectomics of two distantly related nematode species reveals patterns of ner  (11 cites)
- Decision: ___________

**102.** conf=0.436 title=0.51 cit=0.02 auth=0.0 `B=preprint`
- A #9999: [2015] Quantitative neuroanatomy of all Purkinje cells with light sheet microscopy and high-throu  (40 cites)
- B #9999: [2015] Quantitative neuroanatomy for connectomics in <i>Drosophila</i>  (43 cites)
- Decision: ___________

**103.** conf=0.435 title=0.46 cit=0.50 auth=0.0 `diff_DOIs`
- A #9999: [2022] LC3-Associated Phagocytosis in Bacterial Infection  (31 cites)
- B #9999: [2024] LC3-associated phagocytosis of neutrophils triggers tumor ferroptotic cell death in gliobl  (17 cites)
- Decision: ___________

**104.** conf=0.434 title=0.38 cit=0.00 auth=1.0 `diff_DOIs`
- A #1189: [2012] NODDI: Practical in vivo neurite orientation dispersion and density imaging of the human b  (3321 cites)
- B #761: [2014] An RNA-Sequencing Transcriptome and Splicing Database of Glia, Neurons, and Vascular Cells  (5285 cites)
- Decision: ___________

**105.** conf=0.434 title=0.53 cit=0.00 auth=0.0 `A=preprint`
- A #9999: [2016] Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering  (1701 cites)
- B #1333: [2018] Convolutional neural networks: an overview and application in radiology  (4464 cites)
- Decision: ___________

**106.** conf=0.434 title=0.38 cit=0.00 auth=1.0 `diff_DOIs`
- A #353: [2020] Neural circuit mechanisms of sexual receptivity in Drosophila females  (170 cites)
- B #1314: [2021] Neural representations of the amount and the delay time of reward in intertemporal decisio  (43 cites)
- Decision: ___________

**107.** conf=0.433 title=0.48 cit=0.06 auth=0.0 `diff_DOIs`
- A #9999: [2024] Volume electron microscopy analysis of synapses in primary regions of the human cerebral c  (9 cites)
- B #9999: [2025] Volume Electron Microscopy of Cortical Organoids: Methods for Region Identification, Conne  (0 cites)
- Decision: ___________

**108.** conf=0.433 title=0.38 cit=0.00 auth=1.0 `diff_DOIs`
- A #243: [2006] Wiring optimization can relate neuronal structure and function  (662 cites)
- B #1209: [2005] Real-time quantification of microRNAs by stem-loop RT-PCR  (4966 cites)
- Decision: ___________

**109.** conf=0.433 title=0.38 cit=0.00 auth=1.0 `diff_DOIs`
- A #524: [2016] Control principles of complex systems  (667 cites)
- B #1799: [2014] Aggregation and morphology control enables multiple cases of high-efficiency polymer solar  (3077 cites)
- Decision: ___________

**110.** conf=0.432 title=0.50 cit=0.03 auth=0.0 `B=preprint`
- A #9999: [2021] Three-dimensional reconstruction of a whole insect reveals its phloem sap-sucking mechanis  (42 cites)
- B #9999: [2023] Three-dimensional reconstructions of mechanosensory end organs suggest a unifying mechanis  (9 cites)
- Decision: ___________

**111.** conf=0.431 title=0.35 cit=0.04 auth=1.0 `diff_DOIs`
- A #762: [2021] Transforming representations of movement from body- to world-centric space  (148 cites)
- B #193: [2022] En bloc preparation of Drosophila brains enables high-throughput FIB-SEM connectomics  (20 cites)
- Decision: ___________

**112.** conf=0.431 title=0.28 cit=0.14 auth=1.0 `diff_DOIs`
- A #1555: [2018] Expansion Stimulated Emission Depletion Microscopy (ExSTED)  (185 cites)
- B #181: [2019] Cortical column and whole-brain imaging with molecular contrast and nanoscale resolution  (395 cites)
- Decision: ___________

**113.** conf=0.431 title=0.35 cit=0.03 auth=1.0 `diff_DOIs`
- A #140: [2003] The Structure and Function of Complex Networks  (18482 cites)
- B #853: [2005] Power laws, Pareto distributions and Zipf's law  (5724 cites)
- Decision: ___________

**114.** conf=0.431 title=0.91 cit=0.05 auth=0.0 `B=preprint`
- A #9999: [2024] Morphology and ultrastructure of external sense organs of Drosophila larvae  (3 cites)
- B #9999: [2025] Morphology and ultrastructure of pharyngeal sense organs of <i>Drosophila</i> larvae  (0 cites)
- Decision: ___________

**115.** conf=0.430 title=0.23 cit=0.19 auth=1.0 `diff_DOIs`
- A #1355: [2012] High-cost, high-capacity backbone for global brain communication  (830 cites)
- B #1693: [2010] Aberrant Frontal and Temporal Complex Network Structure in Schizophrenia: A Graph Theoreti  (691 cites)
- Decision: ___________

**116.** conf=0.430 title=0.35 cit=0.04 auth=1.0 `diff_DOIs`
- A #1442: [2023] Functional imaging and quantification of multineuronal olfactory responses in <i>C. elegan  (51 cites)
- B #331: [2024] Network statistics of the whole-brain connectome of Drosophila  (98 cites)
- Decision: ___________

**117.** conf=0.430 title=0.37 cit=0.00 auth=1.0 `diff_DOIs`
- A #75: [1995] Spatial registration and normalization of images  (3748 cites)
- B #534: [1994] Functional and effective connectivity in neuroimaging: A synthesis  (2479 cites)
- Decision: ___________

**118.** conf=0.430 title=0.35 cit=0.03 auth=1.0 `diff_DOIs`
- A #1779: [2019] Automated Reconstruction of a Serial-Section EM Drosophila Brain with Flood-Filling Networ  (65 cites)
- B #17: [2020] The connectome of the adult Drosophila mushroom body provides insights into function  (418 cites)
- Decision: ___________

**119.** conf=0.430 title=0.37 cit=0.00 auth=1.0 `diff_DOIs`
- A #1779: [2019] Automated Reconstruction of a Serial-Section EM Drosophila Brain with Flood-Filling Networ  (65 cites)
- B #1133: [2021] A Survey of Convolutional Neural Networks: Analysis, Applications, and Prospects  (4580 cites)
- Decision: ___________

**120.** conf=0.429 title=0.49 cit=0.02 auth=0.0 `B=preprint`
- A #9999: [2023] Three-dimensional ultrastructure analysis of organelles in injured motor neuron  (6 cites)
- B #9999: [2025] Three-dimensional ultrastructural differences between thalamic and non-thalamic recipient   (0 cites)
- Decision: ___________

**121.** conf=0.429 title=0.37 cit=0.00 auth=1.0 `diff_DOIs`
- A #1428: [2021] Cytoarchitecture and innervation of the mouse cochlear amplifier revealed by large‐scale v  (12 cites)
- B #1314: [2021] Neural representations of the amount and the delay time of reward in intertemporal decisio  (43 cites)
- Decision: ___________

**122.** conf=0.428 title=0.48 cit=0.04 auth=0.0 `A=preprint`
- A #9999: [2023] Connectomic reconstruction predicts the functional organization of visual inputs to the na  (14 cites)
- B #609: [2024] Connectomic reconstruction of a female Drosophila ventral nerve cord  (98 cites)
- Decision: ___________

**123.** conf=0.427 title=0.35 cit=0.02 auth=1.0 `diff_DOIs`
- A #51: [1984] Microcircuitry of bipolar cells in cat retina  (248 cites)
- B #275: [1984] Patterns of synaptic input to layer 4 of cat striate cortex  (273 cites)
- Decision: ___________

**124.** conf=0.427 title=0.36 cit=0.00 auth=1.0 `diff_DOIs`
- A #1530: [2017] The antimicrobial activity of nanoparticles: present situation and prospects for the futur  (3843 cites)
- B #1456: [2019] TeraVR empowers precise reconstruction of complete 3-D neuronal morphology in the whole br  (109 cites)
- Decision: ___________

**125.** conf=0.427 title=0.36 cit=0.00 auth=1.0 `diff_DOIs`
- A #612: [2020] A unified connectomic target for deep brain stimulation in obsessive-compulsive disorder  (322 cites)
- B #17: [2020] The connectome of the adult Drosophila mushroom body provides insights into function  (418 cites)
- Decision: ___________

**126.** conf=0.426 title=0.36 cit=0.00 auth=1.0 `diff_DOIs`
- A #1259: [2018] Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition  (4698 cites)
- B #822: [2020] Structural basis for the recognition of SARS-CoV-2 by full-length human ACE2  (5569 cites)
- Decision: ___________

**127.** conf=0.426 title=0.35 cit=0.02 auth=1.0 `diff_DOIs`
- A #1968: [2008] Electrophysiological correlates of the brain's intrinsic large-scale functional architectu  (697 cites)
- B #697: [2007] Small-World Anatomical Networks in the Human Brain Revealed by Cortical Thickness from MRI  (1348 cites)
- Decision: ___________

**128.** conf=0.426 title=0.62 cit=0.24 auth=1.0 `diff_DOIs`
- A #1413: [2010] Modular and Hierarchically Modular Organization of Brain Networks  (1210 cites)
- B #1676: [2009] Hierarchical modularity in human brain functional networks  (688 cites)
- Decision: ___________

**129.** conf=0.426 title=0.36 cit=0.00 auth=1.0 `diff_DOIs`
- A #1042: [2020] Flexible motor sequence generation during stereotyped escape responses  (57 cites)
- B #1428: [2021] Cytoarchitecture and innervation of the mouse cochlear amplifier revealed by large‐scale v  (12 cites)
- Decision: ___________

**130.** conf=0.425 title=0.36 cit=0.00 auth=1.0 `diff_DOIs`
- A #1714: [2020] The effect of network thresholding and weighting on structural brain networks in the UK Bi  (129 cites)
- B #743: [2022] Oligodendrocyte precursor cells ingest axons in the mouse neocortex  (135 cites)
- Decision: ___________

**131.** conf=0.424 title=0.36 cit=0.20 auth=1.0 `diff_DOIs`
- A #1930: [2015] Generative models of the human connectome  (340 cites)
- B #1072: [2017] The specificity and robustness of long-distance connections in weighted, interareal connec  (249 cites)
- Decision: ___________

**132.** conf=0.424 title=0.50 cit=0.00 auth=0.0 `B=preprint`
- A #9999: [2023] Volume Electron Microscopy Workflows for the study of Large-Scale Neural Connectomics  (3 cites)
- B #9999: [2023] Volume Electron Microscopy Reveals Unique Laminar Synaptic Characteristics in the Human En  (2 cites)
- Decision: ___________

**133.** conf=0.423 title=0.31 cit=0.06 auth=1.0 `diff_DOIs`
- A #225: [2006] Modularity and community structure in networks  (12046 cites)
- B #853: [2005] Power laws, Pareto distributions and Zipf's law  (5724 cites)
- Decision: ___________

**134.** conf=0.423 title=0.74 cit=0.06 auth=0.0 `diff_DOIs`
- A #9999: [2013] Structural controllability of unidirectional bipartite networks  (101 cites)
- B #9999: [2016] Structural Controllability of Temporally Switching Networks  (65 cites)
- Decision: ___________

**135.** conf=0.423 title=0.78 cit=0.00 auth=0.0 `diff_DOIs`
- A #9999: [2015] Developmental Changes in Brain Network Hub Connectivity in Late Adolescence  (181 cites)
- B #9999: [2015] Developmental changes in large-scale network connectivity in autism  (277 cites)
- Decision: ___________

**136.** conf=0.423 title=0.49 cit=0.01 auth=0.0 `A=preprint`
- A #9999: [2023] Volume Electron Microscopy Reveals Unique Laminar Synaptic Characteristics in the Human En  (2 cites)
- B #9999: [2025] Volume Electron Microscopy: Imaging Principles, Computational Advances and Applications in  (0 cites)
- Decision: ___________

**137.** conf=0.423 title=0.35 cit=0.00 auth=1.0 `diff_DOIs`
- A #912: [2019] Dynamic Graph CNN for Learning on Point Clouds  (6500 cites)
- B #97: [2020] Neural circuitry linking mating and egg laying in Drosophila females  (222 cites)
- Decision: ___________

**138.** conf=0.423 title=0.49 cit=0.00 auth=0.0 `diff_DOIs`
- A #9999: [2023] Volume Electron Microscopy Workflows for the study of Large-Scale Neural Connectomics  (3 cites)
- B #9999: [2025] Volume Electron Microscopy of Cortical Organoids: Methods for Region Identification, Conne  (0 cites)
- Decision: ___________

**139.** conf=0.423 title=0.76 cit=0.62 auth=0.0 `diff_DOIs`
- A #771: [2006] Ambient noise Rayleigh wave tomography across Europe  (602 cites)
- B #1064: [2007] Ambient noise Rayleigh wave tomography of New Zealand  (305 cites)
- Decision: ___________

**140.** conf=0.422 title=0.65 cit=0.18 auth=1.0 `diff_DOIs`
- A #1413: [2010] Modular and Hierarchically Modular Organization of Brain Networks  (1210 cites)
- B #1230: [2008] Age-related changes in modular organization of human brain functional networks  (781 cites)
- Decision: ___________

**141.** conf=0.421 title=0.41 cit=0.11 auth=1.0 `A=preprint`
- A #177: [2023] CAVE: Connectome Annotation Versioning Engine  (35 cites)
- B #562: [2023] Multi-layered maps of neuropil with segmentation-guided contrastive learning  (27 cites)
- Decision: ___________

**142.** conf=0.420 title=0.34 cit=0.00 auth=1.0 `diff_DOIs`
- A #749: [2015] Deep Learning Face Attributes in the Wild  (7549 cites)
- B #759: [2017] NF-κB signaling in inflammation  (7850 cites)
- Decision: ___________

**143.** conf=0.419 title=0.34 cit=0.00 auth=1.0 `diff_DOIs`
- A #1224: [2021] SLC45A4 promotes glycolysis and prevents AMPK/ULK1‐induced autophagy in TP53 mutant pancre  (18 cites)
- B #1986: [2022] Escape steering by cholecystokinin peptidergic signaling  (27 cites)
- Decision: ___________

**144.** conf=0.419 title=0.31 cit=0.04 auth=1.0 `diff_DOIs`
- A #552: [2021] The connectome predicts resting-state functional connectivity across the Drosophila brain  (36 cites)
- B #84: [2022] Reconstruction of neocortex: Organelles, compartments, cells, circuits, and activity  (211 cites)
- Decision: ___________

**145.** conf=0.419 title=0.66 cit=0.15 auth=1.0 `diff_DOIs`
- A #446: [2012] The Human Connectome Project: A data acquisition perspective  (2760 cites)
- B #172: [2013] The WU-Minn Human Connectome Project: An overview  (6094 cites)
- Decision: ___________

**146.** conf=0.419 title=0.34 cit=0.00 auth=1.0 `diff_DOIs`
- A #735: [2020] Ferroptosis: past, present and future  (3937 cites)
- B #389: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (15 cites)
- Decision: ___________

**147.** conf=0.419 title=0.34 cit=0.00 auth=1.0 `diff_DOIs`
- A #1430: [2021] Deep-Learning-Based Automated Neuron Reconstruction From 3D Microscopy Images Using Synthe  (29 cites)
- B #1079: [2023] Ascending neurons convey behavioral state to integrative sensory and action selection brai  (63 cites)
- Decision: ___________

**148.** conf=0.419 title=0.34 cit=0.00 auth=1.0 `diff_DOIs`
- A #175: [2020] Transforming FIB-SEM Systems for Large-Volume Connectomics and Cell Biology  (29 cites)
- B #70: [2020] Cross-species functional alignment reveals evolutionary hierarchy within the connectome  (265 cites)
- Decision: ___________

**149.** conf=0.419 title=0.47 cit=0.02 auth=0.0 `diff_DOIs`
- A #9999: [2022] Volume electron microscopy reveals age-related circuit remodeling in the auditory brainste  (5 cites)
- B #9999: [2025] Volume Electron Microscopy of Cortical Organoids: Methods for Region Identification, Conne  (0 cites)
- Decision: ___________

**150.** conf=0.419 title=0.74 cit=0.04 auth=0.0 `diff_DOIs`
- A #1671: [2020] Autophagy and Autophagy-Related Diseases: A Review  (313 cites)
- B #1337: [2023] Autophagy and autophagy-related pathways in cancer  (1229 cites)
- Decision: ___________

**151.** conf=0.419 title=0.33 cit=0.01 auth=1.0 `diff_DOIs`
- A #258: [2020] Conservation and divergence of related neuronal lineages in the Drosophila central brain  (59 cites)
- B #1056: [2021] Learning and Segmenting Dense Voxel Embeddings for 3D Neuron Reconstruction  (31 cites)
- Decision: ___________

**152.** conf=0.418 title=0.67 cit=0.13 auth=0.0 `diff_DOIs`
- A #9999: [2019] Expansion microscopy for the analysis of centrioles and cilia  (62 cites)
- B #1477: [2020] Expansion Microscopy for Cell Biology Analysis in Fungi  (52 cites)
- Decision: ___________

**153.** conf=0.418 title=0.32 cit=0.02 auth=1.0 `diff_DOIs`
- A #874: [2020] Automatic Reconstruction of Mitochondria and Endoplasmic Reticulum in Electron Microscopy   (52 cites)
- B #1366: [2022] Organization of the gravity-sensing system in zebrafish  (51 cites)
- Decision: ___________

**154.** conf=0.418 title=0.31 cit=0.04 auth=1.0 `diff_DOIs`
- A #1171: [2020] Visual Input into the Drosophila melanogaster Mushroom Body  (40 cites)
- B #389: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (15 cites)
- Decision: ___________

**155.** conf=0.418 title=0.47 cit=0.02 auth=0.0 `B=preprint`
- A #1539: [2024] Connectomic reconstruction predicts visual features used for navigation  (25 cites)
- B #9999: [2025] Connectomic reconstruction from hippocampal CA3 reveals spatially graded mossy fiber input  (1 cites)
- Decision: ___________

**156.** conf=0.418 title=0.60 cit=0.23 auth=0.0 `diff_DOIs`
- A #9999: [2016] Structural Controllability of Temporally Switching Networks  (65 cites)
- B #9999: [2017] Structural controllability of multi-agent systems with absolute protocol under fixed and s  (51 cites)
- Decision: ___________

**157.** conf=0.417 title=0.34 cit=0.00 auth=1.0 `diff_DOIs`
- A #1456: [2019] TeraVR empowers precise reconstruction of complete 3-D neuronal morphology in the whole br  (109 cites)
- B #353: [2020] Neural circuit mechanisms of sexual receptivity in Drosophila females  (170 cites)
- Decision: ___________

**158.** conf=0.417 title=0.33 cit=0.20 auth=1.0 `B=preprint`
- A #890: [1997] Akt Phosphorylation of BAD Couples Survival Signals to the Cell-Intrinsic Death Machinery  (5689 cites)
- B #1346: [1999] Cellular survival: a play in three Akts  (4218 cites)
- Decision: ___________

**159.** conf=0.417 title=0.44 cit=0.06 auth=0.0 `diff_DOIs`
- A #9999: [2025] Volume Electron Microscopy: Imaging Principles, Computational Advances and Applications in  (0 cites)
- B #9999: [2025] Volume Electron Microscopy of Cortical Organoids: Methods for Region Identification, Conne  (0 cites)
- Decision: ___________

**160.** conf=0.417 title=0.12 cit=0.30 auth=1.0 `diff_DOIs`
- A #378: [2002] Whole Brain Segmentation  (8910 cites)
- B #1154: [2001] Automated manifold surgery: constructing geometrically accurate and topologically correct   (1802 cites)
- Decision: ___________

**161.** conf=0.416 title=0.33 cit=0.00 auth=1.0 `diff_DOIs`
- A #1462: [2019] UNet++: Redesigning Skip Connections to Exploit Multiscale Features in Image Segmentation  (3913 cites)
- B #127: [2020] A pneumonia outbreak associated with a new coronavirus of probable bat origin  (23190 cites)
- Decision: ___________

**162.** conf=0.416 title=0.33 cit=0.00 auth=1.0 `diff_DOIs`
- A #1042: [2020] Flexible motor sequence generation during stereotyped escape responses  (57 cites)
- B #353: [2020] Neural circuit mechanisms of sexual receptivity in Drosophila females  (170 cites)
- Decision: ___________

**163.** conf=0.416 title=0.28 cit=0.07 auth=1.0 `diff_DOIs`
- A #1779: [2019] Automated Reconstruction of a Serial-Section EM Drosophila Brain with Flood-Filling Networ  (65 cites)
- B #389: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (15 cites)
- Decision: ___________

**164.** conf=0.415 title=0.22 cit=0.15 auth=1.0 `diff_DOIs`
- A #1775: [2020] Super-Resolution Three-Dimensional Imaging of Actin Filaments in Cultured Cells and the Br  (40 cites)
- B #1736: [2021] Epitope-preserving magnified analysis of proteome (eMAP)  (47 cites)
- Decision: ___________

**165.** conf=0.415 title=0.33 cit=0.00 auth=1.0 `diff_DOIs`
- A #612: [2020] A unified connectomic target for deep brain stimulation in obsessive-compulsive disorder  (322 cites)
- B #1133: [2021] A Survey of Convolutional Neural Networks: Analysis, Applications, and Prospects  (4580 cites)
- Decision: ___________

**166.** conf=0.415 title=0.33 cit=0.00 auth=1.0 `diff_DOIs`
- A #1088: [2021] Functional architecture of neural circuits for leg proprioception in Drosophila  (41 cites)
- B #1588: [2021] Three-dimensional residual channel attention networks denoise and sharpen fluorescence mic  (207 cites)
- Decision: ___________

**167.** conf=0.415 title=0.60 cit=0.22 auth=1.0 `diff_DOIs`
- A #28: [2011] Controllability of complex networks  (3263 cites)
- B #1763: [2012] Control Centrality and Hierarchical Structure in Complex Networks  (329 cites)
- Decision: ___________

**168.** conf=0.415 title=0.67 cit=0.12 auth=0.0 `diff_DOIs`
- A #9999: [2019] Dopaminergic modulation of retinal processing from starlight to sunlight  (99 cites)
- B #9999: [2020] Dopaminergic Modulation of Signal Processing in a Subset of Retinal Bipolar Cells  (22 cites)
- Decision: ___________

**169.** conf=0.414 title=0.30 cit=0.03 auth=1.0 `diff_DOIs`
- A #859: [2019] Convolutional nets for reconstructing neural circuits from brain images acquired by serial  (59 cites)
- B #1824: [2020] 3D mesh processing using GAMer 2 to enable reaction-diffusion simulations in realistic cel  (71 cites)
- Decision: ___________

**170.** conf=0.414 title=0.33 cit=0.00 auth=1.0 `diff_DOIs`
- A #759: [2017] NF-κB signaling in inflammation  (7850 cites)
- B #1728: [2019] Pathways for practical high-energy long-cycling lithium metal batteries  (3260 cites)
- Decision: ___________

**171.** conf=0.414 title=0.33 cit=0.00 auth=1.0 `diff_DOIs`
- A #1456: [2019] TeraVR empowers precise reconstruction of complete 3-D neuronal morphology in the whole br  (109 cites)
- B #1314: [2021] Neural representations of the amount and the delay time of reward in intertemporal decisio  (43 cites)
- Decision: ___________

**172.** conf=0.414 title=0.33 cit=0.00 auth=1.0 `diff_DOIs`
- A #1700: [2014] A modular hierarchical approach to 3D electron microscopy image segmentation  (69 cites)
- B #1763: [2012] Control Centrality and Hierarchical Structure in Complex Networks  (329 cites)
- Decision: ___________

**173.** conf=0.414 title=0.33 cit=0.00 auth=1.0 `diff_DOIs`
- A #1179: [2013] The Cancer Imaging Archive (TCIA): Maintaining and Operating a Public Information Reposito  (4508 cites)
- B #1011: [2013] Whatever next? Predictive brains, situated agents, and the future of cognitive science  (5679 cites)
- Decision: ___________

**174.** conf=0.414 title=0.32 cit=0.00 auth=1.0 `diff_DOIs`
- A #769: [2021] Expansion tomography for large volume tissue imaging with nanoscale resolution  (18 cites)
- B #1430: [2021] Deep-Learning-Based Automated Neuron Reconstruction From 3D Microscopy Images Using Synthe  (29 cites)
- Decision: ___________

**175.** conf=0.413 title=0.64 cit=0.15 auth=0.0 `diff_DOIs`
- A #9999: [2015] Controllability and observability of Boolean networks arising from biology  (50 cites)
- B #9999: [2017] Controllability and observability in complex networks – the effect of connection types  (50 cites)
- Decision: ___________

**176.** conf=0.413 title=0.47 cit=0.00 auth=0.0 `B=preprint`
- A #9999: [2023] Volume electron microscopy reconstruction uncovers a physical barrier that limits virus to  (4 cites)
- B #9999: [2023] Volume Electron Microscopy Reveals Unique Laminar Synaptic Characteristics in the Human En  (2 cites)
- Decision: ___________

**177.** conf=0.413 title=0.32 cit=0.00 auth=1.0 `diff_DOIs`
- A #1950: [2017] Synaptic and peptidergic connectome of a neurosecretory center in the annelid brain  (142 cites)
- B #549: [2018] 2018 ESC/ESH Guidelines for the management of arterial hypertension  (10258 cites)
- Decision: ___________

**178.** conf=0.413 title=0.63 cit=0.17 auth=0.0 `diff_DOIs`
- A #1477: [2020] Expansion Microscopy for Cell Biology Analysis in Fungi  (52 cites)
- B #9999: [2022] Expansion Microscopy for Imaging the Cell–Material Interface  (29 cites)
- Decision: ___________

**179.** conf=0.412 title=0.32 cit=0.00 auth=1.0 `diff_DOIs`
- A #1358: [2019] Cancer treatment and survivorship statistics, 2019  (4375 cites)
- B #1613: [2020] The interplay of autophagy and non-apoptotic cell death pathways  (49 cites)
- Decision: ___________

**180.** conf=0.412 title=0.32 cit=0.00 auth=1.0 `diff_DOIs`
- A #1462: [2019] UNet++: Redesigning Skip Connections to Exploit Multiscale Features in Image Segmentation  (3913 cites)
- B #964: [2020] GTree: an Open-source Tool for Dense Reconstruction of Brain-wide Neuronal Population  (49 cites)
- Decision: ___________

**181.** conf=0.412 title=0.48 cit=0.37 auth=1.0 `diff_DOIs`
- A #260: [1992] Objective analysis of the topological organization of the primate cortical visual system  (471 cites)
- B #390: [1993] The organization of neural systems in the primate cerebral cortex  (286 cites)
- Decision: ___________

**182.** conf=0.412 title=0.32 cit=0.00 auth=1.0 `diff_DOIs`
- A #1845: [2003] Experiments and theory in strain gradient elasticity  (2964 cites)
- B #1204: [2003] Pulmonary Toxicity of Single-Wall Carbon Nanotubes in Mice 7 and 90 Days After Intratrache  (1988 cites)
- Decision: ___________

**183.** conf=0.412 title=0.32 cit=0.00 auth=1.0 `diff_DOIs`
- A #822: [2020] Structural basis for the recognition of SARS-CoV-2 by full-length human ACE2  (5569 cites)
- B #155: [2020] Mouse Retinal Cell Atlas: Molecular Identification of over Sixty Amacrine Cell Types  (346 cites)
- Decision: ___________

**184.** conf=0.412 title=0.32 cit=0.00 auth=1.0 `diff_DOIs`
- A #912: [2019] Dynamic Graph CNN for Learning on Point Clouds  (6500 cites)
- B #1496: [2020] Brain connectomes come of age  (16 cites)
- Decision: ___________

**185.** conf=0.412 title=0.32 cit=0.00 auth=1.0 `diff_DOIs`
- A #840: [2020] Click-ExM enables expansion microscopy for all biomolecules  (164 cites)
- B #1515: [2021] Temporal transitions in the post-mitotic nervous system of Caenorhabditis elegans  (56 cites)
- Decision: ___________

**186.** conf=0.411 title=0.32 cit=0.00 auth=1.0 `diff_DOIs`
- A #1986: [2022] Escape steering by cholecystokinin peptidergic signaling  (27 cites)
- B #1214: [2024] Methyltransferase Setd2 prevents T cell–mediated autoimmune diseases via phospholipid remo  (29 cites)
- Decision: ___________

**187.** conf=0.411 title=0.57 cit=0.24 auth=1.0 `diff_DOIs`
- A #110: [2015] Expansion microscopy  (1542 cites)
- B #560: [2016] Nanoscale imaging of RNA with expansion microscopy  (421 cites)
- Decision: ___________

**188.** conf=0.411 title=0.58 cit=0.03 auth=0.0 `diff_DOIs`
- A #1952: [2023] Synaptic architecture of leg and wing premotor control networks in <i>Drosophila</i>  (18 cites)
- B #9999: [2024] Synaptic architecture of a memory engram in the mouse hippocampus  (11 cites)
- Decision: ___________

**189.** conf=0.411 title=0.32 cit=0.00 auth=1.0 `diff_DOIs`
- A #970: [2006] Automatic atom type and bond type perception in molecular mechanical calculations  (5535 cites)
- B #60: [2004] Image quality assessment: from error visibility to structural similarity  (54590 cites)
- Decision: ___________

**190.** conf=0.410 title=0.52 cit=0.31 auth=1.0 `diff_DOIs`
- A #671: [2003] Automatically Parcellating the Human Cerebral Cortex  (4426 cites)
- B #1154: [2001] Automated manifold surgery: constructing geometrically accurate and topologically correct   (1802 cites)
- Decision: ___________

**191.** conf=0.410 title=0.32 cit=0.00 auth=1.0 `diff_DOIs`
- A #1259: [2018] Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition  (4698 cites)
- B #155: [2020] Mouse Retinal Cell Atlas: Molecular Identification of over Sixty Amacrine Cell Types  (346 cites)
- Decision: ___________

**192.** conf=0.410 title=0.31 cit=0.00 auth=1.0 `diff_DOIs`
- A #1623: [2017] The fundamental advantages of temporal networks  (491 cites)
- B #1779: [2019] Automated Reconstruction of a Serial-Section EM Drosophila Brain with Flood-Filling Networ  (65 cites)
- Decision: ___________

**193.** conf=0.410 title=0.31 cit=0.01 auth=1.0 `diff_DOIs`
- A #1088: [2021] Functional architecture of neural circuits for leg proprioception in Drosophila  (41 cites)
- B #769: [2021] Expansion tomography for large volume tissue imaging with nanoscale resolution  (18 cites)
- Decision: ___________

**194.** conf=0.409 title=0.17 cit=0.20 auth=1.0 `diff_DOIs`
- A #1053: [2020] Topographic gradients of intrinsic dynamics across neocortex  (175 cites)
- B #1963: [2022] Network structure and transcriptomic vulnerability shape atrophy in frontotemporal dementi  (83 cites)
- Decision: ___________

**195.** conf=0.409 title=0.31 cit=0.00 auth=1.0 `diff_DOIs`
- A #1331: [2021] Nanoscale 3D EM reconstructions reveal intrinsic mechanisms of structural diversity of che  (20 cites)
- B #667: [2022] Strong Structural Controllability of Boolean Networks: Polynomial-Time Criteria, Minimal N  (110 cites)
- Decision: ___________

**196.** conf=0.409 title=0.55 cit=0.26 auth=1.0 `diff_DOIs`
- A #73: [2000] Error and attack tolerance of complex networks  (7085 cites)
- B #65: [2002] Statistical mechanics of complex networks  (20311 cites)
- Decision: ___________

**197.** conf=0.409 title=0.31 cit=0.00 auth=1.0 `diff_DOIs`
- A #1331: [2021] Nanoscale 3D EM reconstructions reveal intrinsic mechanisms of structural diversity of che  (20 cites)
- B #1891: [2022] Joint Embedding of Structural and Functional Brain Networks with Graph Neural Networks for  (39 cites)
- Decision: ___________

**198.** conf=0.408 title=0.31 cit=0.00 auth=1.0 `diff_DOIs`
- A #1986: [2022] Escape steering by cholecystokinin peptidergic signaling  (27 cites)
- B #1079: [2023] Ascending neurons convey behavioral state to integrative sensory and action selection brai  (63 cites)
- Decision: ___________

**199.** conf=0.408 title=0.94 cit=0.31 auth=0.0 `diff_DOIs`
- A #358: [2017] Global, regional, and national incidence, prevalence, and years lived with disability for   (13428 cites)
- B #396: [2018] Global, regional, and national incidence, prevalence, and years lived with disability for   (13807 cites)
- Decision: ___________

**200.** conf=0.408 title=0.31 cit=0.00 auth=1.0 `diff_DOIs`
- A #970: [2006] Automatic atom type and bond type perception in molecular mechanical calculations  (5535 cites)
- B #1991: [2008] Altered small‐world brain functional networks in children with attention‐deficit/hyperacti  (484 cites)
- Decision: ___________

**201.** conf=0.408 title=0.31 cit=0.00 auth=1.0 `diff_DOIs`
- A #1038: [2018] 30 Years of Lithium‐Ion Batteries  (5776 cites)
- B #389: [2020] Neuronal Subcompartment Classification and Merge Error Correction  (15 cites)
- Decision: ___________

**202.** conf=0.408 title=0.31 cit=0.00 auth=1.0 `diff_DOIs`
- A #621: [2017] MotionCor2: anisotropic correction of beam-induced motion for improved cryo-electron micro  (8716 cites)
- B #16: [2018] A Complete Electron Microscopy Volume of the Brain of Adult Drosophila melanogaster  (1135 cites)
- Decision: ___________

**203.** conf=0.408 title=0.24 cit=0.10 auth=1.0 `diff_DOIs`
- A #1007: [2011] Functional and Effective Connectivity: A Review  (3443 cites)
- B #607: [2010] The free-energy principle: a unified brain theory?  (7439 cites)
- Decision: ___________

**204.** conf=0.408 title=0.31 cit=0.00 auth=1.0 `diff_DOIs`
- A #1038: [2018] 30 Years of Lithium‐Ion Batteries  (5776 cites)
- B #1171: [2020] Visual Input into the Drosophila melanogaster Mushroom Body  (40 cites)
- Decision: ___________

**205.** conf=0.408 title=0.31 cit=0.00 auth=1.0 `diff_DOIs`
- A #749: [2015] Deep Learning Face Attributes in the Wild  (7549 cites)
- B #524: [2016] Control principles of complex systems  (667 cites)
- Decision: ___________

**206.** conf=0.408 title=0.31 cit=0.00 auth=1.0 `diff_DOIs`
- A #137: [2021] Barcoded oligonucleotides ligated on RNA amplified for multiplexed and parallel <i>in situ  (63 cites)
- B #1332: [2021] Connectomic features underlying diverse synaptic connection strengths and subcellular comp  (40 cites)
- Decision: ___________

**207.** conf=0.408 title=0.53 cit=0.29 auth=0.0 `diff_DOIs`
- A #9999: [2006] Suppression and enhancement of non-native molecules within biological systems  (30 cites)
- B #9999: [2007] Suppression and enhancement of secondary ion formation due to the chemical environment in   (74 cites)
- Decision: ___________

**208.** conf=0.407 title=0.37 cit=0.10 auth=1.0 `B=preprint`
- A #105: [2010] An Integrated Micro- and Macroarchitectural Analysis of the Drosophila Brain by Computer-A  (388 cites)
- B #672: [2009] Drosophila Brain Development: Closing the Gap between a Macroarchitectural and Microarchit  (16 cites)
- Decision: ___________

**209.** conf=0.407 title=0.28 cit=0.04 auth=1.0 `diff_DOIs`
- A #1779: [2019] Automated Reconstruction of a Serial-Section EM Drosophila Brain with Flood-Filling Networ  (65 cites)
- B #1171: [2020] Visual Input into the Drosophila melanogaster Mushroom Body  (40 cites)
- Decision: ___________

**210.** conf=0.407 title=0.45 cit=0.00 auth=0.0 `diff_DOIs`
- A #9999: [2023] Volume electron microscopy reconstruction uncovers a physical barrier that limits virus to  (4 cites)
- B #9999: [2025] Volume Electron Microscopy of Cortical Organoids: Methods for Region Identification, Conne  (0 cites)
- Decision: ___________

**211.** conf=0.406 title=0.43 cit=0.02 auth=0.0 `B=preprint`
- A #9999: [2024] Comparative connectomics of dauer reveals developmental plasticity  (23 cites)
- B #816: [2024] Comparative connectomics of the descending and ascending neurons of the <i>Drosophila</i>   (24 cites)
- Decision: ___________

**212.** conf=0.406 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #1623: [2017] The fundamental advantages of temporal networks  (491 cites)
- B #1038: [2018] 30 Years of Lithium‐Ion Batteries  (5776 cites)
- Decision: ___________

**213.** conf=0.406 title=0.59 cit=0.20 auth=0.0 `diff_DOIs`
- A #9999: [2013] Structural controllability of multi-agent networks: Robustness against simultaneous failur  (87 cites)
- B #9999: [2016] Structural Controllability of Temporally Switching Networks  (65 cites)
- Decision: ___________

**214.** conf=0.406 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #735: [2020] Ferroptosis: past, present and future  (3937 cites)
- B #1133: [2021] A Survey of Convolutional Neural Networks: Analysis, Applications, and Prospects  (4580 cites)
- Decision: ___________

**215.** conf=0.406 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #1042: [2020] Flexible motor sequence generation during stereotyped escape responses  (57 cites)
- B #1114: [2020] Circuit and Behavioral Mechanisms of Sexual Rejection by Drosophila Females  (85 cites)
- Decision: ___________

**216.** conf=0.406 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #1654: [2020] Pik3c3 deficiency in myeloid cells imparts partial resistance to experimental autoimmune e  (22 cites)
- B #1522: [2022] Data-Efficient Brain Connectome Analysis via Multi-Task Meta-Learning  (18 cites)
- Decision: ___________

**217.** conf=0.406 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #874: [2020] Automatic Reconstruction of Mitochondria and Endoplasmic Reticulum in Electron Microscopy   (52 cites)
- B #1332: [2021] Connectomic features underlying diverse synaptic connection strengths and subcellular comp  (40 cites)
- Decision: ___________

**218.** conf=0.406 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #183: [2011] RSEM: accurate transcript quantification from RNA-Seq data with or without a reference gen  (22985 cites)
- B #1721: [2009] Brain Anatomical Network and Intelligence  (605 cites)
- Decision: ___________

**219.** conf=0.406 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #735: [2020] Ferroptosis: past, present and future  (3937 cites)
- B #17: [2020] The connectome of the adult Drosophila mushroom body provides insights into function  (418 cites)
- Decision: ___________

**220.** conf=0.406 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #1779: [2019] Automated Reconstruction of a Serial-Section EM Drosophila Brain with Flood-Filling Networ  (65 cites)
- B #612: [2020] A unified connectomic target for deep brain stimulation in obsessive-compulsive disorder  (322 cites)
- Decision: ___________

**221.** conf=0.405 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #1114: [2020] Circuit and Behavioral Mechanisms of Sexual Rejection by Drosophila Females  (85 cites)
- B #1314: [2021] Neural representations of the amount and the delay time of reward in intertemporal decisio  (43 cites)
- Decision: ___________

**222.** conf=0.405 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #1456: [2019] TeraVR empowers precise reconstruction of complete 3-D neuronal morphology in the whole br  (109 cites)
- B #1114: [2020] Circuit and Behavioral Mechanisms of Sexual Rejection by Drosophila Females  (85 cites)
- Decision: ___________

**223.** conf=0.405 title=0.61 cit=0.17 auth=1.0 `diff_DOIs`
- A #535: [2018] Progress and remaining challenges in high-throughput volume electron microscopy  (130 cites)
- B #1563: [2020] Image Processing for Volume Electron Microscopy  (6 cites)
- Decision: ___________

**224.** conf=0.405 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #1332: [2021] Connectomic features underlying diverse synaptic connection strengths and subcellular comp  (40 cites)
- B #1207: [2023] MCU Upregulation Overactivates Mitophagy by Promoting VDAC1 Dimerization and Ubiquitinatio  (40 cites)
- Decision: ___________

**225.** conf=0.404 title=0.29 cit=0.02 auth=1.0 `diff_DOIs`
- A #1496: [2020] Brain connectomes come of age  (16 cites)
- B #353: [2020] Neural circuit mechanisms of sexual receptivity in Drosophila females  (170 cites)
- Decision: ___________

**226.** conf=0.404 title=0.66 cit=0.10 auth=1.0 `diff_DOIs`
- A #1287: [2013] Observability of complex systems  (521 cites)
- B #28: [2011] Controllability of complex networks  (3263 cites)
- Decision: ___________

**227.** conf=0.404 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #912: [2019] Dynamic Graph CNN for Learning on Point Clouds  (6500 cites)
- B #1114: [2020] Circuit and Behavioral Mechanisms of Sexual Rejection by Drosophila Females  (85 cites)
- Decision: ___________

**228.** conf=0.404 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #1269: [2021] Ciliary Type III Adenylyl Cyclase in the VMH Is Crucial for High‐Fat Diet‐Induced Obesity   (12 cites)
- B #1522: [2022] Data-Efficient Brain Connectome Analysis via Multi-Task Meta-Learning  (18 cites)
- Decision: ___________

**229.** conf=0.404 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #1736: [2021] Epitope-preserving magnified analysis of proteome (eMAP)  (47 cites)
- B #1398: [2022] Gliotransmission of D-serine promotes thirst-directed behaviors in Drosophila  (41 cites)
- Decision: ___________

**230.** conf=0.404 title=0.44 cit=0.00 auth=0.0 `diff_DOIs`
- A #9999: [2024] Volume electron microscopy reveals age-related ultrastructural differences of globular bus  (0 cites)
- B #9999: [2025] Volume Electron Microscopy of Cortical Organoids: Methods for Region Identification, Conne  (0 cites)
- Decision: ___________

**231.** conf=0.403 title=0.30 cit=0.00 auth=1.0 `diff_DOIs`
- A #353: [2020] Neural circuit mechanisms of sexual receptivity in Drosophila females  (170 cites)
- B #1428: [2021] Cytoarchitecture and innervation of the mouse cochlear amplifier revealed by large‐scale v  (12 cites)
- Decision: ___________

**232.** conf=0.403 title=0.72 cit=0.00 auth=0.0 `diff_DOIs`
- A #9999: [2017] Author response: A connectome of a learning and memory center in the adult Drosophila brai  (6 cites)
- B #9999: [2020] Author response: A connectome and analysis of the adult Drosophila central brain  (14 cites)
- Decision: ___________

**233.** conf=0.403 title=0.58 cit=0.20 auth=0.0 `diff_DOIs`
- A #9999: [2019] Expansion microscopy for the analysis of centrioles and cilia  (62 cites)
- B #595: [2020] Expansion Microscopy for Beginners: Visualizing Microtubules in Expanded Cultured HeLa Cel  (37 cites)
- Decision: ___________

**234.** conf=0.402 title=0.29 cit=0.00 auth=1.0 `diff_DOIs`
- A #456: [2014] Aspirin plus Clopidogrel as Secondary Prevention after Stroke or Transient Ischemic Attack  (11546 cites)
- B #1189: [2012] NODDI: Practical in vivo neurite orientation dispersion and density imaging of the human b  (3321 cites)
- Decision: ___________

**235.** conf=0.402 title=0.29 cit=0.00 auth=1.0 `diff_DOIs`
- A #1799: [2014] Aggregation and morphology control enables multiple cases of high-efficiency polymer solar  (3077 cites)
- B #266: [2016] Inflammasome-activated gasdermin D causes pyroptosis by forming membrane pores  (3105 cites)
- Decision: ___________

**236.** conf=0.402 title=0.29 cit=0.00 auth=1.0 `diff_DOIs`
- A #1492: [2017] Nanoscale imaging of clinical specimens using pathology-optimized expansion microscopy  (239 cites)
- B #1619: [2018] NeuTu: Software for Collaborative, Large-Scale, Segmentation-Based Connectome Reconstructi  (58 cites)
- Decision: ___________

**237.** conf=0.401 title=0.58 cit=0.20 auth=0.0 `diff_DOIs`
- A #9999: [2021] A survey on adversarial attacks and defences  (363 cites)
- B #9999: [2022] A survey on adversarial attacks in computer vision: Taxonomy, visualization and future dir  (76 cites)
- Decision: ___________

**238.** conf=0.401 title=0.29 cit=0.00 auth=1.0 `diff_DOIs`
- A #1224: [2021] SLC45A4 promotes glycolysis and prevents AMPK/ULK1‐induced autophagy in TP53 mutant pancre  (18 cites)
- B #1430: [2021] Deep-Learning-Based Automated Neuron Reconstruction From 3D Microscopy Images Using Synthe  (29 cites)
- Decision: ___________

**239.** conf=0.401 title=0.29 cit=0.00 auth=1.0 `diff_DOIs`
- A #1531: [2013] A Comprehensive Wiring Diagram of the Protocerebral Bridge for Visual Information Processi  (161 cites)
- B #1651: [2013] High-resolution 3D shallow crustal structure in Long Beach, California: Application of amb  (437 cites)
- Decision: ___________

**240.** conf=0.401 title=0.29 cit=0.00 auth=1.0 `diff_DOIs`
- A #193: [2022] En bloc preparation of Drosophila brains enables high-throughput FIB-SEM connectomics  (20 cites)
- B #1689: [2024] Spatial patterns of noise-induced inner hair cell ribbon loss in the mouse mid-cochlea  (16 cites)
- Decision: ___________

**241.** conf=0.401 title=0.28 cit=0.01 auth=1.0 `diff_DOIs`
- A #1824: [2020] 3D mesh processing using GAMer 2 to enable reaction-diffusion simulations in realistic cel  (71 cites)
- B #1056: [2021] Learning and Segmenting Dense Voxel Embeddings for 3D Neuron Reconstruction  (31 cites)
- Decision: ___________

**242.** conf=0.400 title=0.29 cit=0.00 auth=1.0 `diff_DOIs`
- A #1224: [2021] SLC45A4 promotes glycolysis and prevents AMPK/ULK1‐induced autophagy in TP53 mutant pancre  (18 cites)
- B #1588: [2021] Three-dimensional residual channel attention networks denoise and sharpen fluorescence mic  (207 cites)
- Decision: ___________

**243.** conf=0.400 title=0.29 cit=0.00 auth=1.0 `diff_DOIs`
- A #1482: [2013] Structural and Functional Brain Networks: From Connections to Cognition  (2124 cites)
- B #1706: [2014] Excitatory Synaptic Inputs to Mouse On-Off Direction-Selective Retinal Ganglion Cells Lack  (84 cites)
- Decision: ___________

## Papers That Would Enter Top 500 If Merged (20)

- #562 → ~#395 | **Multi-Layered Maps of Neuropil with Segmentation-Guided Contrastive Le** (16+27 cites)
- #885 → ~#411 | **2016 ESC Guidelines for the management of atrial fibrillation develope** (6474+6411 cites)
- #931 → ~#439 | **Connectome-driven neural inventory of a complete visual system** (36+46 cites)
- #762 → ~#440 | **Transforming representations of movement from body- to world-centric s** (22+148 cites)
- #523 → ~#399 | **The neuropeptidergic connectome of <i>C. elegans</i>** (18+160 cites)
- #701 → ~#365 | **Local Shape Descriptors for Neuron Segmentation** (17+51 cites)
- #743 → ~#391 | **Oligodendrocyte precursor cells prune axons in the mouse neocortex** (19+135 cites)
- #1040 → ~#496 | **A Connectome of the Male <i>Drosophila</i> Ventral Nerve Cord** (58+53 cites)
- #521 → ~#379 | **Synaptic connectome of the <i>Drosophila</i> circadian clock** (23+69 cites)
- #609 → ~#310 | **Tools for connectomic reconstruction and analysis of a female <i>Droso** (25+98 cites)
- #713 → ~#483 | **Towards Reproducible Brain-Wide Association Studies** (216+1930 cites)
- #547 → ~#297 | **Connectome-constrained deep mechanistic networks predict neural respon** (29+83 cites)
- #746 → ~#394 | **Global, regional, and national burden of neurological disorders, 1990–** (5555+7183 cites)
- #532 → ~#370 | **The cortical wiring scheme of hierarchical information processing** (13+110 cites)
- #642 → ~#366 | **EASE: EM-Assisted Source Extraction from calcium imaging data** (19+49 cites)
- #642 → ~#422 | **UNet++: Redesigning Skip Connections to Exploit Multiscale Features in** (3913+19 cites)
- #620 → ~#345 | **Automated synaptic connectivity inference for volume electron microsco** (152+64 cites)
- #735 → ~#455 | **Ferroptosis: past, present and future** (3937+5 cites)
- #668 → ~#481 | **Autophagy and microbial pathogenesis** (81+14 cites)
- #621 → ~#378 | **MotionCor2: anisotropic correction of beam-induced motion for improved** (8716+52 cites)


---

# Part 2: Author Name Disambiguation

Five signals: name similarity, first-name compatibility, co-author overlap,
citation neighborhood overlap, and shared-paper flag.

| Signal | Weight | What it catches |
| --- | --- | --- |
| Name string similarity | 0.25 | Obvious name variants |
| First name/initial match | 0.20 | 'J. Friedman' = 'Jerome H. Friedman' |
| Co-author Jaccard | 0.25 | Same collaborators → same person |
| Citation neighborhood | 0.15 | Same research topic |
| No shared paper | 0.15 | Co-authors on same paper → different people |

| Category | Count |
| --- | --- |
| SAME_PERSON | 10 |
| LIKELY_SAME | 111 |
| REVIEW | 814 |
| DIFFERENT_PEOPLE | 45 |

## SAME_PERSON — merge these

- ★ **Nicole Neubarth** (1p) = **Nicole N. Neubarth** (1p) | conf=0.797 coauth=0.60 refs=0.46 | 2 in top 500
  - Decision: ___________
- ★ **Ingrid Andrade** (4p) = **Ingrid V Andrade** (1p) | conf=0.763 coauth=0.33 refs=0.64 | 3 in top 500
  - Decision: ___________
- ★ **Fabian C. Roth** (1p) = **Fabian Roth** (1p) | conf=0.746 coauth=0.60 refs=0.18 | 2 in top 500
  - Decision: ___________
- ★ **J. Friedman** (1p) = **Jerome H. Friedman** (1p) | conf=0.730 coauth=1.00 refs=0.00 | 2 in top 500
  - Decision: ___________
- ★ **Caitlyn A. Bishop** (1p) = **Caitlyn Bishop** (2p) | conf=0.727 coauth=0.33 refs=0.45 | 2 in top 500
  - Decision: ___________
- **Zhang J. Chen** (3p) = **Zhang Chen** (1p) | conf=0.695 coauth=0.29 refs=0.37 | 0 in top 500
  - Decision: ___________
- ★ **Gregory S. Couch** (1p) = **Greg S. Couch** (1p) | conf=0.681 coauth=0.60 refs=0.11 | 1 in top 500
  - Decision: ___________
- **Ji-Youn Seo** (1p) = **Ji‐Youn Seo** (1p) | conf=0.678 coauth=0.60 refs=0.00 | 0 in top 500
  - Decision: ___________
- **Fan Yang** (1p) = **Fujun Yang** (1p) | conf=0.672 coauth=0.75 refs=0.00 | 0 in top 500
  - Decision: ___________
- ★ **Leighton H. Duncan** (1p) = **Leighton H Duncan** (1p) | conf=0.651 coauth=0.00 refs=0.39 | 1 in top 500
  - Decision: ___________

## LIKELY_SAME — quick human check

- ★ **Mark W. Moyle** (1p) ≈ **Mark W Moyle** (1p) | conf=0.648 coauth=0.00 refs=0.39
  - Decision: ___________
- ★ **Agnes L. Bodor** (1p) ≈ **Agnes L Bodor** (1p) | conf=0.641 coauth=0.14 refs=0.10
  - Decision: ___________
- ★ **Evan R Daugharthy** (1p) ≈ **Evan R. Daugharthy** (1p) | conf=0.633 coauth=0.14 refs=0.03
  - Decision: ___________
- **Der‐Fen Suen** (1p) ≈ **Der-Fen Suen** (1p) | conf=0.629 coauth=0.40 refs=0.00
  - Decision: ___________
- ★ **Lukas C Kapitein** (1p) ≈ **Lukas C. Kapitein** (1p) | conf=0.627 coauth=0.00 refs=0.23
  - Decision: ___________
- ★ **Ross D. Markello** (6p) ≈ **Ross D Markello** (1p) | conf=0.614 coauth=0.00 refs=0.14
  - Decision: ___________
- ★ **Ben Fulcher** (4p) ≈ **Ben D Fulcher** (1p) | conf=0.610 coauth=0.06 refs=0.11
  - Decision: ___________
- ★ **M. P. Young** (1p) ≈ **MP Young** (1p) | conf=0.601 coauth=0.00 refs=0.67
  - Decision: ___________
- ★ **Joshua T. Vogelstein** (1p) ≈ **Joshua T Vogelstein** (3p) | conf=0.594 coauth=0.00 refs=0.00
  - Decision: ___________
- ★ **Patricia K. Rivlin** (2p) ≈ **Patricia Rivlin** (1p) | conf=0.592 coauth=0.00 refs=0.10
  - Decision: ___________
- ★ **Albert-Ĺaszló Barabási** (12p) ≈ **Albert-László Barabási** (1p) | conf=0.588 coauth=0.17 refs=0.04
  - Decision: ___________
- ★ **Steven L. Petersen** (1p) ≈ **Steven E. Petersen** (5p) | conf=0.586 coauth=0.00 refs=0.00
  - Decision: ___________
- **Robert G. Smith** (1p) ≈ **Robert E. Smith** (2p) | conf=0.583 coauth=0.00 refs=0.00
  - Decision: ___________
- **M. P. Schmidt** (1p) ≈ **Martin Schmidt** (2p) | conf=0.582 coauth=0.40 refs=0.17
  - Decision: ___________
- ★ **Albert-László Barabási** (1p) ≈ **A.-L. Barabási** (1p) | conf=0.577 coauth=0.00 refs=0.80
  - Decision: ___________
- ★ **Stephen J Smith** (4p) ≈ **Stephen M. Smith** (15p) | conf=0.576 coauth=0.00 refs=0.00
  - Decision: ___________
- **G M Edelman** (1p) ≈ **Gerald M. Edelman** (1p) | conf=0.570 coauth=0.33 refs=0.00
  - Decision: ___________
- **Søren T. Christensen** (1p) ≈ **Søren Rahn Christensen** (1p) | conf=0.562 coauth=0.00 refs=0.00
  - Decision: ___________
- ★ **Satoshi Ogawa** (1p) ≈ **Shotaro Ogawa** (1p) | conf=0.561 coauth=0.17 refs=0.50
  - Decision: ___________
- **Jielin Xu** (1p) ≈ **Jingli Xu** (1p) | conf=0.559 coauth=0.00 refs=0.50
  - Decision: ___________
- ★ **Hawoong Jeong** (2p) ≈ **H. Jeong** (1p) | conf=0.557 coauth=0.00 refs=0.67
  - Decision: ___________
- ★ **Josh Morgan** (4p) ≈ **Joshua Morgan** (1p) | conf=0.556 coauth=0.08 refs=0.12
  - Decision: ___________
- ★ **Giulio Tononi** (2p) ≈ **G Tononi** (1p) | conf=0.554 coauth=0.25 refs=0.07
  - Decision: ___________
- ★ **JK Stevens** (1p) ≈ **John K. Stevens** (1p) | conf=0.552 coauth=0.25 refs=0.00
  - Decision: ___________
- **Xinan Zhang** (1p) ≈ **Xi Zhang** (1p) | conf=0.551 coauth=0.00 refs=0.33
  - Decision: ___________
- ★ **Jack W. Scannell** (2p) ≈ **JW Scannell** (1p) | conf=0.550 coauth=0.00 refs=0.38
  - Decision: ___________
- ★ **Albert Cardona** (12p) ≈ **Alberto Cardona** (1p) | conf=0.547 coauth=0.00 refs=0.10
  - Decision: ___________
- **Luke E. Brezovec** (2p) ≈ **Bella E. Brezovec** (1p) | conf=0.547 coauth=0.57 refs=0.38
  - Decision: ___________
- **Yuanhua Li** (1p) ≈ **Yuan Li** (1p) | conf=0.546 coauth=0.00 refs=0.33
  - Decision: ___________
- ★ **Michael Newman** (1p) ≈ **Michelle G. Newman** (1p) | conf=0.545 coauth=0.00 refs=0.35
  - Decision: ___________

... and 81 more (see author_dedup_review.tsv)

## DIFFERENT_PEOPLE — do NOT merge

- ** Zamin Iqbal ** ≠ ** Zamin Iqbal** (share 1 paper(s))
- **Salman Khan** ≠ **Sher Afzal Khan** (share 1 paper(s))
- **Mahaly Baptiste** ≠ **Maya R. Baptiste** (share 1 paper(s))
- **C Baigent** ≠ **Colin Baigent** (share 1 paper(s))
- **Fengting Huang** ≠ **Jing Huang** (share 1 paper(s))
- **Weina Wang** ≠ **Zhenshan Wang** (share 1 paper(s))
- **Jianzhong Cui** ≠ **Ying Cui** (share 1 paper(s))
- **Qiang Wang** ≠ **Pinchun Wang** (share 1 paper(s))
- **Fei Jiang** ≠ **Yong Jiang** (share 1 paper(s))
- **Changmeng Cui** ≠ **Jianzhong Cui** (share 1 paper(s))
- **Pengcheng Zhou** ≠ **Ding Zhou** (share 1 paper(s))
- **Xin‐Ying Lin** ≠ **Yuanyuan Lin** (share 1 paper(s))
- **Zhiyuan Xu** ≠ **Handong Xu** (share 1 paper(s))
- **Shan Wang** ≠ **Ziming Wang** (share 1 paper(s))
- **Qiang Wang** ≠ **Yajie Wang** (share 1 paper(s))

... and 30 more
