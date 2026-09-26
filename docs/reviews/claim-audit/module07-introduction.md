# Claim audit: Module 7, Introduction to Connectomics

**Date:** 2026-09-26
**Deck:** `course/decks/marp/en585781/module07-introduction-to-connectomics.marp.md` (59 slides; the cover is slide 1)
**Scope:** every quantitative or factual-historical claim on the slides and in the speaker notes.

## Summary

| Verdict | Count |
|---|---|
| VERIFIED | 35 |
| CORRECTED | 18 |
| QUALIFIED | 19 |
| HYPOTHETICAL | 5 |
| UNVERIFIED | 4 |
| **Total** | **81** |

What changed, in short:
- **Internal cross-references.** The three Part-divider "Slides x–y" ranges were wrong, and so were three "n slides ahead" pointers.
- **Wrong numbers.** The fly brain volume and its data size were wrong, so the fly-to-mouse ratio was too. "Nine orders of magnitude" was wrong; it is about four.
- **Misattributions.** The retina result conflated Briggman and Kim. The Lappalainen predictions were described as "then tested" when they were compared with 26 prior studies.
- **Timeline dates.** Flood-filling networks is 2018, not 2017. The larval fly connectome is the brain, not the "whole larva." The male CNS work runs 2024–26. The songbird connectome is a preprint.
- **Other fixes.** The array tomography resolution was wrong. The Allen atlas sample count was out of date.
- **Estimate labels.** The extrapolation table and the whole-mouse storage figure are now marked as estimates.

## Claims

| Slide # | Claim (short quote) | Verdict | Source (DOI/URL + where in source) | Change made |
|---|---|---|---|---|
| 1 | Cover image H01, CC BY 4.0, Shapson-Coe et al. (2024) doi:10.1126/science.adk4858 | VERIFIED | h01-release.storage.googleapis.com/data.html: "All released datasets are licensed under a Creative Commons Attribution 4.0 License." Crossref confirms DOI, Science, 10 May 2024 | None |
| 6 | "Slides 6–20" (Part A range) | CORRECTED | Deck count: Part A content is slides 7–26 | 6–20 → 7–26 |
| 10 | "We come back to this in eleven slides" | CORRECTED | Cold open is slide 10; "Back to the cold open" is slide 22 | eleven → twelve |
| 11 | Light microscopy resolves ~200–250 nm | QUALIFIED | Diffraction limit (textbook, ~λ/2NA); consistent with 200–300 nm used on slide 30 | None |
| 11 | Structure sizes (soma 10–25 µm; spine neck 50–200 nm; unmyelinated axon 80–300 nm; PSD 30–50 nm, etc.) | QUALIFIED | Textbook ranges. EM morphometry reports unmyelinated axons of about 0.1–0.5 µm (Sci Rep 2018, doi:10.1038/s41598-018-22361-2, optic nerve). No single primary source covers the table | Speaker note added: approximate ranges, not tied to one source |
| 11 | "Electron microscopy at 4 × 4 × 40 nm" | VERIFIED | MICrONS 2025 (doi:10.1038/s41586-025-08790-w, PMC11981939): ~4 nm pixels, 40 nm nominal sections. H01 uses 4 × 4 nm pixels, ~33 nm sections | None |
| 12 | "a 1 µm³ box contains on the order of a dozen distinct neurites" | UNVERIFIED | No primary source found. Plausible from cortical axon length density, but not confirmed | None; flagged for owner |
| 12 | "at 250 nm two membranes 20 nm apart are one blur" | QUALIFIED | Follows from diffraction limit and ~20 nm cleft (textbook) | None |
| 14 | ~40 nm vesicles; ~20 nm cleft | QUALIFIED | Textbook values (synaptic vesicle ~40 nm; cleft ~20 nm). Not fetched from a primary paper | None |
| 14 | "the Bin B assumption from three slides ahead" | CORRECTED | Bin B slide is slide 20, six slides after slide 14 | three → six |
| 15 | 1 mm³ at 4 × 4 × 40 nm = 1.56 × 10¹⁵ voxels ≈ 1.56 PB at 8-bit | VERIFIED | Arithmetic: 10¹⁸ nm³ ÷ 640 nm³ = 1.5625 × 10¹⁵ | None |
| 15 | H01 and MICrONS "roughly 1 mm³", "1.4–2 PB" | VERIFIED | H01 paper text: "1.4 petabytes", "cubic millimeter". MICrONS PMC11981939: EM volume "1.3 × 0.87 × 0.82 mm³", "2 Pb of raw data" | None |
| 16 | Raw-data column (all rows) | QUALIFIED | Column is arithmetic, not measured sizes | Header now "(est.)"; speaker note explains derivation |
| 16 | *C. elegans* nervous system ~0.00005 mm³, ~0.1 TB | QUALIFIED | No direct primary measurement found. Consistent with Abbott et al. 2020 (doi:10.1016/j.cell.2020.08.010), Fig. 1: "A 10-Million-Fold Increase in Brain Volume" worm → mouse (500 mm³ ÷ 10⁷ = 5 × 10⁻⁵ mm³) | Speaker note: rough estimate |
| 16 | Adult *Drosophila* brain "~0.02–0.03 mm³", "~40 TB" | CORRECTED | Zheng et al. 2018 (Cell, PMC6063995): brain "∼8 × 10⁷ μm³" (0.08 mm³), FAFB "∼106 TB". FlyWire (PMC11446842) gives *neuropil* volume 0.0175 mm³, which is likely where the old figure came from | ~0.02–0.03 mm³ / ~40 TB → ~0.08 mm³ / ~125 TB (arithmetic). Note cites the measured 106 TB |
| 16 | Mouse 1 mm³ ~1.6 PB | VERIFIED | Arithmetic above; matches H01 1.4 PB / MICrONS 2 PB | None |
| 16 | Whole mouse brain ~500 mm³, ~800 PB | QUALIFIED | Badea et al. 2007, NeuroImage: C57BL/6J brain 508.91 ± 23.42 mm³. 500 × 1.5625 PB = 781 PB (4 × 4 × 40 nm, 8-bit, uncompressed). Abbott et al. 2020, p. 1373: "Roughly 1 million terabytes of data" (~1 EB) | Header "(est.)". Note records that Abbott et al. 2020 give ~1 EB. Kept ~800 PB per coordinator's cross-deck ruling |
| 16 | Whole human brain ~1.2 × 10⁶ mm³, ~10²¹ bytes | QUALIFIED | Human brain volume ~1,130 cm³ (female) to ~1,260 cm³ (male) (Cosgrove et al. 2007, Biol Psychiatry, as summarized in PMC2711771). 1.2 × 10⁶ × 1.56 × 10¹⁵ ≈ 2 × 10²¹ B, so "~10²¹" is order-of-magnitude only | Covered by "(est.)" header and note |
| 16 | "Fly → mouse mm³ is ~40×" | CORRECTED | 1 mm³ ÷ 0.08 mm³ ≈ 12.5 | ~40× → ~12× |
| 16 | "mm³ → whole mouse brain is ~500×" | VERIFIED | 508.91 mm³ (Badea 2007) | None |
| 16 | NIH BRAIN CONNECTS first awards 2023 | VERIFIED | CSHL news, 26 Sep 2023 ("Mitra among first awarded NIH BRAIN CONNECTS grant"). NIH: initial round of 11 grants, ~$150M over 5 years | None |
| 17 | 0.05 mm³ at 8 nm isotropic ≈ 10¹⁴ voxels ≈ 100 TB; z 10× coarser at 4 × 4 × 40 | VERIFIED | Arithmetic: 5 × 10¹⁶ ÷ 512 = 9.8 × 10¹³; 40/4 = 10 | None |
| 19 | "42 synapses", "4× more often" | HYPOTHETICAL | Example claim sentences, presented as quoted examples | None needed (clearly examples) |
| 22 | "It took the connectome plus a decade of physiology" | QUALIFIED | Heading-cell physiology (Seelig & Jayaraman 2015) predates the hemibrain central-complex connectome (Hulse et al. 2021, eLife). "A decade" is not supportable as a count | "a decade of physiology" → "years of physiology" |
| 23–24 | Worked example (distance bins, ≥50 proofread cells) | HYPOTHETICAL | Worked example of a study design | None needed (slide titled "Worked example") |
| 27 | "Slides 21–37" (Part B range) | CORRECTED | Part B content is slides 28–40 | 21–37 → 28–40 |
| 28 | Reconstruction scale "roughly 50–100 nm" at 4 × 4 × 40 nm | UNVERIFIED | No primary source found for a reliable-segmentation floor | None; flagged for owner |
| 29 | Spine necks 50–200 nm | QUALIFIED | As slide 11 | None |
| 29 | Light-sheet at 1 µm "costs about five orders of magnitude less"; "five-order-of-magnitude error" | CORRECTED | Cost is not sourced. Voxel arithmetic: 1 µm³ ÷ 640 nm³ = 1.56 × 10⁶ (about six orders, not five) | → "needs roughly a million times fewer voxels"; box → "a million-fold error in data volume" |
| 30 | Array tomography "~50–100 nm lateral, 70 nm sections" | CORRECTED | Micheva & Smith 2007 (Neuron, doi:10.1016/j.neuron.2007.06.014) and CSH Protocols: ultrathin sections "70–200 nm", "ordinary high-NA, diffraction-limited optics" (lateral ~200 nm) | → "~200 nm lateral (optical), 70–200 nm sections" |
| 30 | Other modality-chart ranges (dMRI, light-sheet, confocal, ExM, SBEM, FIB-SEM, volumes) | QUALIFIED | Typical ranges; the slide footer already says "typical rather than record-setting". Spot checks: SBEM voxel sizes match Briggman 2011 / songbird SBEM 10 × 10 × 25 nm (bioRxiv 10.1101/2025.10.25.684569); FIB-SEM hemibrain 8 nm | None |
| 30 | MAPseq/BARseq "10⁴–10⁶ cells" | QUALIFIED | Axonal BARseq >8,000 neurons in one mouse (Nat Commun 2024, doi:10.1038/s41467-024-52756-x); BRAIN Initiative: 100,000+ neurons per experiment. The 10⁶ end refers to BARseq transcriptomic cell counts (Chen et al. 2024 Nature), not all with projections | None (also on slide 33) |
| 31 | Multibeam SEM "61 or 91 beams" | VERIFIED | ZEISS MultiSEM product page: "61 or even 91 electron beams"; Eberle et al. 2015 (doi:10.1111/jmi.12224): 61 beams | None |
| 31 | SmartEM (2025), FAST-EM (2024), LICONN (2025) | QUALIFIED | Crossref: SmartEM doi:10.1038/s41592-025-02929-3 online 29 Dec 2025, issue Jan 2026. FAST-EM doi:10.1515/mim-2024-0005, Aug 2024. LICONN doi:10.1038/s41586-025-08985-1, Nature 2025 | None (2025 = online date) |
| 32 | dMRI 0.5–2 mm; XRM ~0.1–1 µm; "cohorts of thousands" | QUALIFIED | Typical ranges; not fetched from a primary source | None |
| 33 | Allen connectivity atlas "across hundreds of animals" | CORRECTED | Oh et al. 2014 used 469 injections; the atlas now has 1,751 public tracing experiments (PMC10745083, "Modeling the cell-type-specific mesoscale murine connectome") | → "from well over a thousand tracer experiments" |
| 34 | Serial sections "30–50 nm" | VERIFIED | MICrONS 40 nm nominal; H01 ~33 nm; FAFB 35–40 nm (Zheng 2018) | None |
| 35 | "Registration residuals (four slides on)" | CORRECTED | Registration slide is 38; scale-leakage slide is 35 | four → three |
| 36 | Size per neuron (GB / 10–100 MB / 0.1–5 MB / KB); "a few GB" for skeletons | QUALIFIED | Order-of-magnitude illustrations; no primary source | Header → "Size per neuron (rough)" |
| 37 | "measure the offset on 20 cells" | HYPOTHETICAL | Illustrative procedure | None needed |
| 38–39 | Residual scenario (3 µm / 40 µm; 5 µm / 15 µm / 10 µm; 2.1 / 31 µm) | HYPOTHETICAL | Invented worked scenario, framed as an exercise | None needed |
| 39 | Isotropic operator "wrong by a factor of 10 in z" | VERIFIED | 40 nm ÷ 4 nm | None |
| 41 | "Slides 38–56" (Part C range) | CORRECTED | Part C is slides 42–59 (including references and credits) | 38–56 → 42–59 |
| 43 | 1986 *C. elegans* hermaphrodite (White et al.) | VERIFIED | Phil Trans R Soc B 314:1–340 (1986), doi:10.1098/rstb.1986.0056 | None |
| 43 | 2004 SBF-SEM (Denk & Horstmann) | VERIFIED | Crossref doi:10.1371/journal.pbio.0020329, 19 Oct 2004 | None |
| 43 | 2011 Briggman (retina); Bock (functional ssTEM) | VERIFIED | Bock: Crossref doi:10.1038/nature09802, Nature Mar 2011. Briggman et al., Nature 471:183 (2011), bibliographic record, not fetched | None |
| 43 | 2013 Helmstaedter IPL | VERIFIED | Nature 500:168 (2013), bibliographic record, not fetched | None |
| 43 | 2014 EyeWire (Kim et al.) | VERIFIED | Crossref doi:10.1038/nature13240, Nature 509:331, May 2014 | None |
| 43 | 2015 Kasthuri; multibeam SEM | VERIFIED | Cell 162:648 (Aug 2015, PubMed 26232230); Eberle 2015 J Microsc (Crossref) | None |
| 43 | "2017 Flood-filling networks (Januszewski)" | CORRECTED | Nature Methods 15:605 (2018), doi:10.1038/s41592-018-0049-4 (bioRxiv preprint Oct 2017). Slide 51 already said 2018 | FFN moved to 2018 row; streams adjusted (2017: **1**; 2018: **1**, **3**) |
| 43 | 2017 whole-brain larval zebrafish (Hildebrand) | VERIFIED | Nature 545:345–349 (2017), doi:10.1038/nature22356 | Wording "Whole-brain larval zebrafish ssEM" |
| 43 | 2018 FAFB (Zheng & Bock) | VERIFIED | Cell 174:730 (2018), PMC6063995 | None |
| 43 | 2020 hemibrain "largest proofread connectome" | CORRECTED | Scheffer et al. 2020 (doi:10.7554/eLife.57443). It was the largest in 2020; FlyWire (2024) is larger | → "then-largest" |
| 43 | 2021 H01, MICrONS, Witvliet | QUALIFIED | H01 bioRxiv May 2021 (doi:10.1101/2021.05.29.446289), paper 2024. MICrONS paper received Apr 2023, published Apr 2025. Witvliet Nature 596:257 (2021) | → "H01 human cortex and MICrONS mm³ released (preprints)" |
| 43 | 2023 "Whole-larva brain connectome" (Winding) | CORRECTED | Science 379:eadd9330 (2023), "The connectome of an insect brain": larval *Drosophila* brain, 3,016 neurons, 548,000 synapses. Not the whole larva | → "Larval fly brain connectome" |
| 43 | 2024 FlyWire (Dorkenwald); Lappalainen | VERIFIED | Nature 634:124 (Oct 2024); Nature 634:1132 (Crossref 31 Oct 2024) | None |
| 43 / 45 | "2024–25" male CNS releases | CORRECTED | Male CNS: bioRxiv Oct 2025 (doi:10.1101/2025.10.09.680999), published Cell Sep 2026 ("Sexual dimorphism in the complete Drosophila male central nervous system connectome") | 2024–25 → 2024–26 (slides 43 and 45) |
| 43 | 2025 MICrONS flagship; LICONN | VERIFIED | MICrONS Nature, 9–10 Apr 2025; LICONN Nature 642:398 (2025) | None |
| 43 | 2025 songbird basal ganglia connectome | QUALIFIED | bioRxiv 25 Oct 2025, doi:10.1101/2025.10.25.684569 (preprint; peer-reviewed status not confirmed) | Added "(preprint)" |
| 44 | 302 neurons, complete since 1986 | VERIFIED | White et al. 1986: hermaphrodite "302 neurons" | None |
| 44 | Cook 2019 both sexes; Witvliet 2021 eight stages | VERIFIED | Cook, Nature 571:63 (doi:10.1038/s41586-019-1352-7). Witvliet, Nature 596:257: "eight isogenic ... individuals across postnatal stages" (eight animals from birth to adulthood) | None |
| 45 | hemibrain ~25,000 neurons | VERIFIED | Scheffer et al. 2020 abstract: "~25,000 neurons" | None |
| 45 | FlyWire ~139,000 neurons, ~54.5 million synapses | VERIFIED | Dorkenwald et al. 2024 (PMC11446842): "139,255 neurons ... and 54.5 million synapses between these neurons" | None |
| 45 | Models "predicted taste and behavioral responses, which were then tested experimentally" | VERIFIED | Shiu et al. 2024, Nature 634:210 (doi:10.1038/s41586-024-07763-9): taste-circuit predictions tested experimentally | None |
| 46 | MICrONS ~200,000 cells, ~500 million synapses | VERIFIED | PMC11981939: "more than 200,000 cells", "524 million synaptic clefts" | None |
| 46 | H01 ~57,000 cells, ~150 million synapses; surgically resected | VERIFIED | H01 paper: "about 57,000 cells ... about 150 million synapses", tissue "surgically removed to gain access to an underlying epileptic focus" | None |
| 46 | "axons forming dozens of synapses onto a single target" | VERIFIED | H01 paper: powerful axonal "inputs of up to 50 synapses" | None |
| 47 | Retina: "starburst amacrine inhibition onto DSGCs organized by space–time wiring specificity" (Briggman 2011; Kim 2014) | CORRECTED | Kim et al. 2014 (doi:10.1038/nature13240) abstract: space–time wiring specificity is *bipolar → starburst* wiring. Briggman 2011 is SAC → DSGC direction-specific wiring. The two were conflated | Rewritten to attribute each finding correctly. "physiology confirmed it" → "physiology tested it" |
| 47 | Lappalainen: model "predicts neural responses that were then tested" | CORRECTED | Lappalainen et al. 2024 abstract: predictions "agreed with experimental measurements of neural activity across 26 studies" (prior data, not new tests) | → "that agreed with measurements from 26 prior studies" |
| 48 | *C. elegans* 8 stages; *Ciona*; *Platynereis*; *Octopus* vertical lobe; zebrafish; male vs female fly | VERIFIED | Witvliet 2021; Ryan et al. 2016 eLife (177 CNS neurons); Verasztó et al. (bioRxiv 2020; eLife 2025 whole-body connectome, doi:10.7554/eLife.97964); Bidel et al. 2023 eLife (doi:10.7554/eLife.84257); Hildebrand 2017; male CNS (above) | None |
| 48 | Songbird basal ganglia (2025) | QUALIFIED | Preprint, as above | → "(2025 preprint)" |
| 49 | BossDB holds MICrONS, H01, Kasthuri, Witvliet, zebrafish | UNVERIFIED (partly) | Confirmed BossDB project pages: bossdb.org/project/witvliet2020 and bossdb.org/project/hildebrand2017. Could not confirm an H01 project page (its primary host is h01-release on Google Cloud). MICrONS and Kasthuri are not confirmed from the page (the site is client-rendered) | None; flagged for owner |
| 50 | Whole mouse brain "~800 PB" | QUALIFIED | As slide 16 | → "~800 PB (est.)" |
| 50 | LICONN (2025) | VERIFIED | doi:10.1038/s41586-025-08985-1 | None |
| 51 | Volume "grown by roughly nine orders of magnitude ... from ~0.00005 mm³ to a mouse mm³" | CORRECTED | 1 ÷ 5 × 10⁻⁵ = 2 × 10⁴, about four orders | nine → four |
| 51 | FFN "changed the human labor per millimeter ... by orders of magnitude" | UNVERIFIED | Januszewski et al. 2018 report accuracy "an order of magnitude better than ... previous approaches" (expected run length), not a labor measurement | Softened → "sharply cut the human labor per millimeter of reconstructed cable" |
| 51 | EyeWire (2014), FlyWire (2024) | VERIFIED | Kim et al. 2014; Dorkenwald et al. 2024 | None |
| 52 | H01 is tissue from a patient with epilepsy | VERIFIED | H01 paper: "middle temporal gyrus of a 45-year-old female ... epileptic focus in the underlying hippocampus" | None |
| 54 | "63 proofread cells", "1.4×", "3.1 to 2.8", "20-cell sample" | HYPOTHETICAL | Illustrative phrasings, not real results | "**Defensible**" → "**Defensible** (illustrative numbers)" |
| 55 | Journal club: Dorkenwald 2024, MICrONS 2025, Shapson-Coe, Tavakoli 2025 | VERIFIED | DOIs above | None |
| 58 | Reference DOIs (17 checked: Cook, Kim, Scheffer, MICrONS, Denk, Knott, Bock, Eberle, Xu, Phelps, Kievits, Tavakoli, SmartEM, Milo, Lappalainen, Abbott, Shapson-Coe) | VERIFIED | All resolve on api.crossref.org with matching titles and first authors | None. SmartEM "2025" is the online date; print is Jan 2026 |

Tally note: rows that group several claims count once. Slides 43 and 45 "2024–26" count as one CORRECTED row.

## Needs owner decision

1. **Slide 12: "a 1 µm³ box contains on the order of a dozen distinct neurites."** No primary source found. It is plausible from cortical neurite length densities, but I did not verify it. Options: cite a dense-reconstruction source (e.g., Kasthuri 2015 object counts), or soften to "many distinct neurites."
2. **Slide 28: "reliably segment neurites down to roughly 50–100 nm."** No primary source found for a segmentation-reliability floor. Options: cite a segmentation error-vs-caliber analysis, or soften to "somewhat coarser than the voxel size."
3. **Slide 49: BossDB "holds ... H01."** Witvliet and Hildebrand are confirmed on BossDB. H01's canonical host is the Google Cloud h01-release bucket, and I could not confirm a BossDB H01 project page. MICrONS and Kasthuri on BossDB are likely but were not confirmed from the page, which is client-rendered. Suggest the owner check bossdb.org/projects in a browser, and move H01 to a "Google Cloud / Neuroglancer" note if it is not hosted there.
4. **Slide 51: FFN labor reduction.** I softened it, removing "by orders of magnitude." If the owner wants a number, the FFN paper supports "an order-of-magnitude accuracy gain," which is not the same as a labor reduction.

Also for the owner:
- **Slide 16, whole-mouse storage.** Kept ~800 PB (est.) per the coordinator's cross-deck ruling. The speaker note records that Abbott et al. 2020 give ~1 EB.
- **Textbook values not tied to a primary paper.** The slide 11 size ranges and the slide 30 and 32 modality ranges are marked QUALIFIED, not VERIFIED. They are textbook values; I did not trace them to individual primary papers.

## Image credits

- The deck has one image: the cover, `assets/images/content-library/case-studies/h01/10b-segmentation-overlay.jpg`. The file exists.
- **Slide 1** carries an image-specific credit: "Image: CC BY 4.0 · Shapson-Coe et al. (2024) · doi:10.1126/science.adk4858". **Slide 59** repeats it.
- The licence is verified against the H01 release page: "All released datasets are licensed under a Creative Commons Attribution 4.0 License."
- No missing credits.

## Access limitations

- **Paywalled pages.** Nature and Science article pages returned 403 or redirects. The paper text came instead from:
  - the H01 paper: a PDF mirror;
  - MICrONS and FlyWire: PMC or Europe PMC full text;
  - Abbott et al. 2020: an author-lab PDF.
- **PubMed.** Returned a CAPTCHA.
- **Checked from bibliographic records only.** Briggman 2011, Helmstaedter 2013 and Micheva & Smith 2007. I did not fetch their full text.
