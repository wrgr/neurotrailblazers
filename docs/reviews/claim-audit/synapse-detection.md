# Claim audit: Synapse Detection (graduate lecture)

**Date:** 2026-09-26
**Deck:** `course/decks/marp/lectures/synapse-detection.marp.md` (39 slides; cover = slide 1)

## Summary

| Verdict | Count |
|---|---:|
| VERIFIED | 45 |
| CORRECTED | 9 |
| QUALIFIED | 3 |
| HYPOTHETICAL | 0 |
| UNVERIFIED | 3 |

No illustrative or invented numbers were found. Every figure on the slides is a reported result from a cited paper, or plain arithmetic on those results. The single hypothetical ("if a detector has 88%…", slide 5) is a discussion prompt that uses SynEM's real number.

## Claims

| Slide # | Claim (short quote) | Verdict | Source (DOI/URL + where in source) | Change made |
|---|---|---|---|---|
| 5 | "88% precision and recall per synapse" (question premise) | VERIFIED | Staffler et al. 2017, doi:10.7554/eLife.26414, Results: "SynEM automatically classified these at 88% precision and recall (Fig. 3e, F1 score of 0.883)" | None |
| 6 | SynEM ~97% binary-connectome P/R; ~88% per synapse; Table 3 varies thresholds | VERIFIED (quick re-check of prior pass) | Staffler 2017 abstract ("97% precision and recall in binary cortical connectomes"); Table 3 caption: thresholds θs (single synapse) vs θnn (neuron-to-neuron), for nn = 1 and nn = 2 | None |
| 6 | H01 "149.9 million synapses", "3.2% / 2.7% FDR" | VERIFIED | Shapson-Coe et al. 2024, doi:10.1126/science.adk4858, section "Synapse prediction": "149,871,669 synapses were automatically detected"; "false discovery rate … 3.2 and 2.7%" | None |
| 7 | H01 missed "11%" E and "35%" I synapses | VERIFIED | Shapson-Coe 2024, "Synapse prediction": "number of missed synapses (false negatives) for excitatory and inhibitory synapses was 11 and 35%" | None |
| 7, 18, 20, 31, 33 | Synful F1 "0.59 to 0.73" across four areas of one brain | VERIFIED | Buhmann et al. 2021, doi:10.1038/s41592-021-01183-7 (PMC7611460): "0.73, 0.68, 0.66 and 0.59 for … calyx, lateral horn, ellipsoid body, and protocerebral bridge" | None |
| 7 | "As of 2025, the cross-dataset benchmarks say this is still open" | VERIFIED | Mohinta et al. 2025, arXiv:2509.17041, abstract: "generalization across datasets remains limited" | None |
| 8, 16, 25 | Part slide ranges "8–15", "16–24", "25–35" | VERIFIED | Internal slide count | None |
| 9 | Huang 2018: U-Net for presynaptic sites, MLP conditioned on segmentation for postsynaptic | VERIFIED | Huang, Scheffer & Plaza 2018, doi:10.3389/fncir.2018.00087, Methods (3D U-Net T-bar detector; single-hidden-layer MLP on segment-interface features) | None |
| 10 | Quotes "a complete solution for polyadic synapse detection" / "together with their one-to-many connectivity information" | VERIFIED | Huang 2018 (text); Li et al. 2024, doi:10.1109/TMI.2024.3400276 (PMC11585350), dataset description | None |
| 11 | Kreshuk 2011: "0.92 recall at 0.89 precision", 111 synapses, three annotators, "comparable to that of the experts"; FIB/SEM, near-isotropic | VERIFIED | Kreshuk et al. 2011, doi:10.1371/journal.pone.0024899, abstract (verbatim match); rat S1 L2/3, 5 nm pixels, 9 nm milling depth | None |
| 11 | Becker 2013: three datasets; orientation as a by-product | VERIFIED | Becker et al. 2013, doi:10.1109/TMI.2013.2267747, abstract | None |
| 11 | SyConn: SBEM of zebrafish, mouse, zebra finch; songbird basal ganglia | VERIFIED | Dorkenwald et al. 2017, doi:10.1038/nmeth.4206, abstract | None |
| 11 | SynEM "88% / 88%"; spine "94% / 89%"; binary "97% / 97%"; mouse cortex, en-bloc, SBEM | VERIFIED | Staffler 2017, Results (spine synapses: "94% precision and 89% recall"); Methods (SBEM, L4 of mouse S1, conventionally en-bloc stained) | None |
| 11, 18 | Heinrich 2018: significant improvement on CREMI; "~50 teravoxels" whole fly brain | VERIFIED | Heinrich et al. 2018, doi:10.1007/978-3-030-00934-2_36 (arXiv:1805.02718), abstract: "significant improvement over the state of the art"; "50 tera-voxels dataset of the complete Drosophila brain" | None |
| 11 | Huang 2018: connectome-scale metrics; "most connectivity characterised correctly" | VERIFIED | Huang 2018, abstract ("effectively characterize most of the connectivity correctly") | None |
| 12 | Turner 2020: cleft mask as attention gate; combined system; mouse somatosensory cortex | VERIFIED | Turner et al. 2020, doi:10.1109/ISBI45749.2020.9098489 (arXiv:1904.09947), abstract | None |
| 12 | Synful "244 million" putative partners | VERIFIED | Buhmann 2021 (PMC7611460): "244 million putative synaptic partners" | None |
| 12 | Synful "92–96% of edges correctly sorted weak (<5) vs strong (≥5)" | QUALIFIED | Buhmann 2021: "For γ = 5, between 92% and 96% of edges are correctly identified … 96% and 92% … for calyx and lateral horn respectively" (only two of the four areas) | Added "(two areas)" |
| 12 | Park 2022: "F1 = 0.955" on 508 synapses; mouse cerebellar molecular layer; synaptic/non, pre/post, E/I | VERIFIED | Park et al. 2022, doi:10.3389/fnana.2022.760279, abstract ("0.955 in F1-score for a test volume of CML containing 508 synapses") | None |
| 12 | H01: three-class U-Net + ResNet-50 E/I classifier | VERIFIED | Shapson-Coe et al. bioRxiv 10.1101/2021.05.29.446289v4, Methods: 3D U-Net "to label three classes: background, pre-synaptic, and post-synaptic"; "two-class ResNet50 classifier". The Science supplementary methods were not accessed | None |
| 12 | "E and I **recall** differ by more than threefold" | CORRECTED | Shapson-Coe 2024: miss rates 11% vs 35% (ratio ≈ 3.2); recall is 89% vs 65% (ratio ≈ 1.4), so it was the *miss rate*, not the recall, that differed threefold | "recall" → "miss rates" |
| 12, 31 | H01 "33 nm sections" | QUALIFIED | Shapson-Coe 2024: "5019 sections with a mean thickness of 33.9 nm"; Fig. 1 legend "sectioned at ~33 nm"; "4 × 4 nm² pixels" | "33 nm" → "~33 nm" (both slides) |
| 12 | SimpSyn: residual U-Net, dual-channel spherical masks; beats Synful on all volumes; limited generalization; adult/larval *Drosophila*, *M. viggianii* | VERIFIED | Mohinta 2025, arXiv:2509.17041, abstract ("consistently outperforms Synful in F1-score across all volumes for synaptic site detection") | None |
| 13 | Unit table (Kreshuk 0.92/0.89; SynEM 88/88; Buhmann 0.59–0.73) | VERIFIED | As above | None |
| 13 | "Park et al.'s F1 of 0.955 is the **highest number** on the previous two slides" | CORRECTED | SynEM's 97% / 97% binary-connectome figure and Synful's 96% (slide 11–12) are higher; 0.955 is the highest *per-synapse* score | "highest number" → "highest per-synapse score" |
| 14 | Synful "Per-connection F1 of 0.59–0.73" | CORRECTED | Buhmann 2021: F1 is over synaptic partner pairs (per synapse), not per neuron-to-neuron connection. The deck's own slide 13 says "per partner pair" | "Per-connection" → "Partner-level" |
| 14 | "92–96% of edges … weak/strong classes" | QUALIFIED | Buhmann 2021 (calyx 96%, lateral horn 92%) | Added "(calyx, lateral horn)" |
| 14 | Huang: "as segmentation improved … 'upwards of 50% of total effort'" | VERIFIED | Huang 2018, Introduction: "as segmentation improved, we observed that synapse annotation consumes a more significant fraction of overall reconstruction time (upwards of 50% of total effort)" | None |
| 17 | CREMI: three datasets, each two (5 µm)³ volumes, 1250 × 1250 × 125 px, [4, 4, 40] nm, adult *Drosophila* ssTEM; neuron ids, clefts, (pre, post) pairs | VERIFIED | cremi.org home ("three datasets, each consisting of two (5 μm)³ volumes (training and testing, each 1250 px × 1250 px × 125 px)"); cremi.org/data | None |
| 17 | CREMI scoring: VOI/ARAND/TED; cleft F-score with a distance threshold; partners matched by an assignment minimizing Euclidean distance | VERIFIED | cremi.org/metrics. No combined overall formula on that page, which agrees with the speaker note | None |
| 18 | Heinrich trained on CREMI crops, predicted ~50 teravoxels | VERIFIED | Heinrich 2018 abstract | None |
| 18 | "A 0.14-point spread … **exceeds** the gap between many published methods" | UNVERIFIED (softened) | 0.73 − 0.59 = 0.14 is verified. No source compares that spread with method-to-method gaps | "exceeds the gap between many" → "can exceed the gap between" |
| 19 | WASPSYN: 14 volumes, *M. viggianii*, three whole-brain datasets, ISBI 2023; "smaller than 0.001%" | VERIFIED | Li et al. 2024 (PMC11585350): abstract and dataset section, verbatim quote | None |
| 19 | "0.001% is one part in 100,000 … five orders of magnitude" | VERIFIED | Arithmetic (10⁻⁵); the source says "smaller than", so five orders of magnitude is a lower bound | None |
| 20 | "4 × 4 × 40 nm" adult-fly ssTEM | VERIFIED | cremi.org/data | None |
| 21 | Gray I/II ↔ Colonnier AS/SS; thick vs thin PSD; most AS excitatory, SS inhibitory; VGAT immunocytochemistry | VERIFIED | Cano-Astorga et al. 2024, doi:10.3389/fnana.2024.1348032, abstract | None |
| 22 | PSDs thin as ferrocyanide concentration rises; recommend 0.1% | VERIFIED | Cano-Astorga 2024 abstract: "postsynaptic densities become thinner with increasing concentrations of potassium ferrocyanide"; "a low concentration of potassium ferrocyanide (0.1%)". Concentrations compared: 0%, 0.1%, 1% | None |
| 22 | Title: "a few voxels thick" | UNVERIFIED (framing) | Not a sourced figure. How many voxels depends on the voxel size | None; flagged |
| 23 | H01 table: FN 11% / 35%; FDR 3.2% / 2.7%; correctly classified 86.89% / 84.98%; from proofreading a selection of axons across all layers | VERIFIED | Shapson-Coe 2024, "Synapse prediction" paragraph (verbatim) | None |
| 23 | "one inhibitory synapse in three … one excitatory in nine" | VERIFIED | 35% ≈ 1/3; 11% ≈ 1/9. The slide already says "roughly" | None |
| 24 | Eckstein 2024: six transmitters; 87% synapses / 94% neurons / 91% known cell types | VERIFIED | Eckstein et al. 2024, doi:10.1016/j.cell.2024.03.016 (PMC11106717), abstract | None |
| 27 | 149,871,669 total; 111,272,315 E; 38,599,354 I | VERIFIED | Shapson-Coe 2024, "Synapse prediction" | None |
| 27 | Shares 74.2% / 25.8% | VERIFIED | Computed from the counts above (74.25%, 25.75%). The paper does not print these shares | None |
| 27 | Corrected 102.5 M (67.1%) E, 50.3 M (32.9%) I | VERIFIED | Shapson-Coe 2024: "102.5 million (67.1%) excitatory synapses and 50.3 million (32.9%) inhibitory synapses" | None |
| 28 | "short by about 23%", "about 9% above" | VERIFIED | Arithmetic: 38.6/50.3 = 0.767; 111.3/102.5 = 1.086 | None |
| 28 | "error on the *ratio* — 7.1 percentage points — is **larger than** the error on either count alone" | CORRECTED | Compared percentage points with percent: 7.1 pp is not larger than the 23% inhibitory shortfall. Supportable version: the share moves further than either count's error alone would move it (inhibitory error alone → 68.9%, excitatory alone → 72.6%, both → 74.2%) | Reworded without adding numbers: "That is why the share moves — … **7.1 percentage points** — further than either count's error alone would move it." |
| 30 | "Ten times the volume buys **ten times the confidence**" | CORRECTED | Implied quantitative claim is wrong: interval width shrinks roughly with √n, not n | "…buys a tighter interval around the wrong number." |
| 30 | Cold-open sentence 74.2% / 67.1% | VERIFIED | As slide 27 | None |
| 31 | "CREMI/FAFB at 4 × 4 × 40 nm ssTEM" | UNVERIFIED (FAFB part) | The CREMI part is verified (cremi.org/data). The FAFB voxel size (Zheng et al. 2018, doi:10.1016/j.cell.2018.06.019) could not be fetched from the primary source this pass; it is widely documented as 4 × 4 × 40 nm | None; flagged (low risk) |
| 31 | Heinrich quote "to optimally represent isotropic fields of view in non-isotropic data" | VERIFIED | Heinrich 2018 abstract | None |
| 32 | Heinrich "generalizes well to areas far away…", "including lamina" | VERIFIED | Heinrich 2018 abstract; full text §Results: "Even in areas with different characteristics than the CREMI training volumes (such as the lamina), synaptic cleft predictions are mostly correct" | None |
| 32 | SynapseNet "built explicit domain-adaptation functionality in **rather than relying on a large training set**" | CORRECTED | Muth et al. 2025, doi:10.1091/mbc.e24-11-0519: it uses "a large annotated dataset **and** domain adaptation functionality" | → "SynapseNet pairs a large annotated training set with explicit domain-adaptation functionality." |
| 32 | WASPSYN quote "…are in urgent need" | VERIFIED | Li 2024 (PMC11585350), abstract | None |
| 33 | Kreshuk "111 synapses, three experts"; SynEM "235 synapses among 20,319 non-synaptic interfaces"; SynEM 88 vs 97; H01 FDR/FN; Buhmann 0.59–0.73 | VERIFIED | Kreshuk 2011 abstract; Staffler 2017 Results ("the test set contained 235 synapses and 20319 non-synaptic interfaces"); others as above | None |
| 34 | SynAnno (Lauenburg et al., 2025): guided, neuron-centric proofreading with model-assisted error detection | VERIFIED | doi:10.1101/2025.08.09.669342 (bioRxiv), abstract. A peer-reviewed IEEE TVCG version also appears to exist (doi:10.1109/tvcg.2025.3634824); not checked | None |
| 34 | SynEM experts "93.6–94.6% precision and 97.9–98.9% recall" | CORRECTED | Staffler 2017, Methods: "The precision and recall of the two experts … was 93.6%, 94.6% (expert 1) and 97.9%, 98.9% (expert 2), respectively." The pairs are per expert (P, R), not a precision range and a recall range. They come from a separate dense validation volume of 278 synapses | → "SynEM reports its two experts at **93.6% / 94.6%** and **97.9% / 98.9%** precision / recall." |
| 34 | "Agreement in the mid-90s" | CORRECTED | The expert figures above span 93.6–98.9% | "mid-90s" → "mid-to-high 90s" |
| 35 | 35% vs 11%; ~23% short; 67:33; ~7 pp | VERIFIED | As slides 23, 27, 28 | None |
| 38 | "Muth et al. **2024** (10.1091/mbc.e24-11-0519)" | CORRECTED | Crossref: published in *Mol. Biol. Cell* 2025 (issued 2025-10-01); the bioRxiv preprint is from Dec 2024 | 2024 → 2025 |
| 38 | Other reference DOIs | VERIFIED | All resolve at doi.org to the matching paper (Heinrich MICCAI title confirmed via Crossref) | None |

## Needs owner decision

1. **Slide 18: "0.14-point spread … can exceed the gap between published methods."** The spread is verified. The comparison with method-to-method gaps has no source. I softened "exceeds … many" to "can exceed". Either cite a specific pair of methods whose gap on a common benchmark is under 0.14 F1, or cut the clause.
2. **Slide 31: FAFB voxel size 4 × 4 × 40 nm.** I could not reach Zheng et al. 2018 (Cell) this pass. This is almost certainly correct; confirm against the paper's Methods, or rephrase as "CREMI at 4 × 4 × 40 nm ssTEM (FAFB-derived)".
3. **Slide 22 title: "a few voxels thick".** This is rhetorical, and the thickness in voxels depends on the voxel size. Keep it as framing, or change it to "a few nanometres thick" only if a PSD-thickness figure is sourced.
4. **Content-library page propagation (not edited — outside scope).** The source page `content-library/infrastructure/synapse-detection.md` line 142 has the same "E and I recall differ by more than threefold" wording. It probably also repeats the SynEM expert-range reading and the SynapseNet wording. Those should get the same corrections so that the deck and page agree.

## Image credits

- **Slide 1 (cover):** `assets/images/content-library/case-studies/h01/10b-segmentation-overlay.jpg`. It has an image-specific credit on the slide: "H01 release · Lichtman Lab / Harvard & Connectomics at Google · Image: CC BY 4.0 · Shapson-Coe et al. (2024) · doi:10.1126/science.adk4858". It is repeated on slide 39. The file exists. OK.
- No other slide uses an image. No credits are missing.
