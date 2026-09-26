# Claim audit: Module 9 — Nanoscale Connectomics Algorithms and Applications

**Date:** 2026-09-26
**Deck:** `course/decks/marp/en585781/module09-algorithms-and-applications.marp.md` (58 slides; cover = slide 1)

## Summary

| Verdict | Count |
|---|---|
| VERIFIED | 19 |
| CORRECTED | 10 |
| QUALIFIED | 7 |
| HYPOTHETICAL | 7 |
| UNVERIFIED | 2 |

Nature, Cell/ScienceDirect, PubMed and J Neurosci pages returned captcha, 403, or redirect errors. Where that happened, I verified figures through PMC full text, the Abbott et al. 2020 PDF (Luo Lab mirror), and publisher abstracts surfaced by search. I did not open the Harris & Stevens 1989 PDF or the SNEMI3D challenge page.

## Claims

| Slide | Claim (short quote) | Verdict | Source (DOI/URL, location) | Change made |
|---|---|---|---|---|
| 1, 58 | H01 image CC BY 4.0; Shapson-Coe et al. 2024 | VERIFIED | 10.1126/science.adk4858. H01 release page: "Creative Commons Attribution 4.0" | none |
| 6 | Part A "Slides 6–21" | CORRECTED | Internal count: Part A runs slides 6–23 | 6–21 → 6–23 |
| 24 | Part B "Slides 22–39" | CORRECTED | Internal count: slides 24–40 | 22–39 → 24–40 |
| 41 | Part C "Slides 40–56" | CORRECTED | Internal count: slides 41–56 (57–58 are references/licence) | 40–56 → 41–56 |
| 7 | Neuron spans mm but ~100 nm wide; millions of instances | VERIFIED (order of magnitude) | Standard; e.g. MICrONS 2025, 10.1038/s41586-025-08790-w | none |
| 7 | "99.99% voxel accuracy can still be useless" | HYPOTHETICAL | Conditional illustration ("A pipeline with…") | none; already framed as hypothetical |
| 8 | FFN "step change in accuracy in 2018" | VERIFIED | Januszewski et al. 2018, 10.1038/s41592-018-0049-4, abstract: mean error-free path 1.1 mm, "an order of magnitude better than previously published approaches" | none |
| 8, 57 | Funke et al. 2019 TPAMI DOI; SegEM, GALA DOIs | VERIFIED | 10.1109/TPAMI.2018.2835450 (TPAMI 41:1669, July 2019; early access 2018); 10.1016/j.neuron.2015.09.003; 10.3389/fninf.2014.00034 | none |
| 9 | "a few hundred cubic micrometres is a serious effort" | QUALIFIED | Consistent with benchmark scale: CREMI volumes are 1250×1250×125 voxels at 4×4×40 nm, about 125 µm³ each. SNEMI3D size not checked | none; wording already approximate |
| 9 | SNEMI3D and CREMI are the historical public sets | VERIFIED | ISBI 2013 SNEMI3D; CREMI 2016 (cremi.org) | none |
| 10 | "A 60 nm spine neck at 40 nm z-resolution" | QUALIFIED | 40 nm = MICrONS minnie65 section thickness (4×4×40 nm). Narrowest necks are about 0.05 µm, typical ~0.1–0.2 µm (Harris et al. 1992, as cited in PMC4151245) | Speaker note: 60 nm is a thin-end example |
| 11, 57 | SynEM, SyConn, Synful, ilastik DOIs | VERIFIED | 10.7554/eLife.26414; 10.1038/nmeth.4206; 10.1038/s41592-021-01183-7; 10.1038/s41592-019-0582-9 | none |
| 13 | "the 500× to a whole mouse brain" | VERIFIED | Badea et al. 2007, NeuroImage (S1053811907004910): C57BL/6J brain 508.91 ± 23.42 mm³, vs ~1 mm³ volumes | Source added in slide 51 notes |
| 16 | "3× more synapses" | HYPOTHETICAL | Framed with "If your result is…" | none |
| 17 | "about forty person-hours"; "20 is often enough" | UNVERIFIED (heuristic) | No primary source; these are planning rules of thumb | Speaker note labels them as heuristics |
| 17 | "changed the ratio from 3.1 to 2.8" | HYPOTHETICAL | Illustrative | Added "(illustrative)" |
| 20–21 | Triage worked example (200 cells; 10/20/15/2 min; 32 + 28 min) | HYPOTHETICAL | Arithmetic checked: 20+10+2 = 32; 28 min ≈ five 5-min fixes | "Setup." → "Setup (hypothetical)." |
| 23 | "Community proofreading (EyeWire 2014, FlyWire 2024)" | CORRECTED | EyeWire launched 10 Dec 2012 (Kim et al. 2014, 10.1038/nature13240, is the landmark paper). FlyWire: Dorkenwald et al. 2024, 10.1038/s41586-024-07558-y | → "(EyeWire, launched 2012; FlyWire, Dorkenwald et al. 2024)" |
| 25 | "Common practice thresholds at ≥ 2 or ≥ 3" | CORRECTED (range widened) | FlyWire whole-brain analyses use ≥5 synapses per connection (Lin et al. 2024, 10.1038/s41586-024-07968-y) | → "≥ 2 to ≥ 5" + speaker note |
| 27, 28 | "single-synapse connections typically dominate by count" | QUALIFIED | Winding et al. 2023, 10.1126/science.add9330 (PMC7614541): 66% of edges are weak (1 or 2 synapses), range 60–91% by type. I found no general source for single-synapse alone | → "weak (1–2-synapse) connections" (both slides) |
| 27 | Notes: "1 → 3 can easily remove more than half the edges" | VERIFIED (consistent) | Same Winding figure (66% of edges have ≤2 synapses) | none |
| 27 | 400 nodes / 5,000 vs 1,800 edges | HYPOTHETICAL | Discussion prompt | none |
| 31 | ER reciprocity: p = 0.121, E = 72.7, 2.9× | VERIFIED (arithmetic) | 1200/9900 = 0.1212; p² × 4950 = 72.7; 210/72.7 = 2.89 | none; slide already says "Hypothetical graph" |
| 32 | 210/150 = 1.4×, z = 5.0 | HYPOTHETICAL (arithmetic verified) | Slide already says "illustrative, not measured" | none |
| 33 | 1.14×, z = 1.8, p ≈ 0.074 two-sided / 0.037 one-sided | VERIFIED (arithmetic) | z = 1.786 gives two-sided 0.074, one-sided 0.037 | none |
| 35 | "16 isomorphism classes"; ~1 false positive at α = 0.05 | VERIFIED | Holland & Leinhardt triad census; Milo et al. 2002, 10.1126/science.298.5594.824. 16 × 0.05 = 0.8 | none |
| 39 | Graph matching applied to larval *Drosophila* bilateral pairs | VERIFIED | Winding et al. 2023, 10.1126/science.add9330 | none |
| 40 | `minnie65_public`, materialization 943 | VERIFIED | MICrONS tutorial: v943 released 22 Jan 2024 (tutorial.microns-explorer.org/materialization-version.html) | none |
| 40 | n_nodes 412, n_edges 5,003, merge 0.8%, split 4.1%, n = 17 | HYPOTHETICAL | Example block | "(values illustrative)" added |
| 40, 54 | "Eleven lines" / "eleven-line provenance block" | CORRECTED | The YAML block has 12 lines | → "Twelve lines" / "twelve-line" |
| 42 | *C. elegans* series (Witvliet 2021) across eight stages | VERIFIED | 10.1038/s41586-021-03778-8: "eight isogenic *C. elegans*" from birth to adulthood | Source in notes |
| 42 | "Fly male and female CNS releases (2024–25)" | QUALIFIED | FlyWire (female brain) 2024. BANC female CNS, Bates et al., preprint 2025. Male CNS, Berg et al., bioRxiv Oct 2025, Cell 2026 | Speaker note with dates |
| 42 | Octopus vertical lobe connectome | VERIFIED | Bidel et al. 2023, eLife, 10.7554/eLife.84257 | none |
| 42 | *Ciona*, *Platynereis*, zebra finch | UNVERIFIED (not checked) | Non-quantitative list; not looked up | none |
| 44 | Retinal DS: "starburst inhibition onto DSGCs is organized by space–time wiring specificity… physiology confirmed it" | CORRECTED | Two findings had been merged. Briggman et al. 2011, 10.1038/nature09818: SAC→DSGC wiring depends on DSGC preferred direction. Kim et al. 2014, 10.1038/nature13240: "space–time wiring specificity" is bipolar→SAC placement plus a model ("could endow") | Rewritten to attribute each finding; "physiology confirmed it" → "physiology tested it" |
| 44 | Ring attractor: "The connectome revealed a ring of heading-tuned cells" | CORRECTED | Heading tuning was found by imaging (Seelig & Jayaraman 2015). The connectome showed the architecture (Hulse et al. 2021, 10.7554/eLife.66039; Turner-Evans et al. 2020) | → "The connectome showed that heading-tuned cells, first found by imaging, have the recurrent and inhibitory architecture…" |
| 44 | Lappalainen: model "predicts neural responses that were then tested" | CORRECTED | 10.1038/s41586-024-07939-3 (PMC11525180): predictions compared with "experimentally reported responses from 26 previously reported studies"; no new experiments | → "predicts neural responses reported in 26 prior studies" |
| 45 | Recipe: sign left free; fit to task or data | QUALIFIED | In Lappalainen, signs were fixed from transmitter/receptor profiling. Free: τ and V_rest per type plus one scale per type pair (734 parameters). Trained on optic flow. Random-parameter controls were run | Speaker note; slide text kept as the generic recipe |
| 47 | "Done in the fly visual system, where predictions were then tested" | CORRECTED | As slide 44 | → "where predictions matched published recordings" |
| 51 | "Whole mouse brain — ~800 PB" | QUALIFIED | Arithmetic: 500 mm³ at 4×4×40 nm, 8-bit ≈ 780 PB. Abbott et al. 2020, 10.1016/j.cell.2020.08.010, p. 1373: "Roughly 1 million terabytes of data" (≈1 EB), a rougher projection | → "~800 PB (est.)" + note giving the basis and the Abbott figure (owner reconciliation, see below) |
| 51 | "1 mm³ mouse and human volumes; whole adult fly brain" | VERIFIED | MICrONS 2025, 10.1038/s41586-025-08790-w; H01, 10.1126/science.adk4858; FlyWire 2024 | none |
| 51 | "SmartEM's adaptive dose" | QUALIFIED | Meirovitch et al., Nat Methods, 10.1038/s41592-025-02929-3: short dwell first, then rescan error-prone regions at longer dwell | "adaptive dose" → "adaptive dwell time" |
| 51 | FAST-EM, multibeam SEM; EyeWire; BossDB/neuPrint/CAVE | VERIFIED (existence) | CAVE: 10.1038/s41592-024-02426-z (Nat Methods 22:1112, 2025) | none |
| 52, 53 | "~1 mm³ of human temporal cortex, surgical resection, n = 1"; epilepsy patient | VERIFIED | Shapson-Coe et al. 2024: ~1 mm³ temporal cortex from neurosurgical resection, epilepsy patient; 1.4 PB | none |
| 57 | Helmstaedter 2011 (RESCOP), Milo 2002, natverse, hemibrain, MICrONS 2025, Abbott 2020 DOIs | VERIFIED | 10.1038/nn.2868; 10.1126/science.298.5594.824; 10.7554/eLife.53350; 10.7554/eLife.57443; 10.1038/s41586-025-08790-w; 10.1016/j.cell.2020.08.010 | none |

## Needs owner decision

1. **Slide 17 heuristics** ("about forty person-hours", "20 is often enough to be informative"). There is no primary source for either. They are now labeled as heuristics in the speaker notes. Keep them as teaching rules of thumb, or cite a project's reported per-cell proofreading time.
2. **Cross-deck consistency on whole-mouse-brain storage.** *Resolved in review:* the auditor first changed this slide to ~1 EB. The ~800 PB figure is the correct arithmetic for the stated 4×4×40 nm, 8-bit basis used in Module 07 and Unit 01, so all decks now say ~800 PB (est.) and cite Abbott et al.'s ~1 EB as a rougher published projection.
3. **Slide 42, *Ciona* / *Platynereis* / zebra finch.** These are non-quantitative and were not individually checked. Consider adding citations (e.g. Ryan et al. 2016 *Ciona*; Kornfeld et al. 2017 zebra finch HVC). I have not verified those as part of this audit.
4. **Slide 57 references without DOIs** (Winding 2023, Dorkenwald 2024, Briggman 2011, Bassett 2018). The DOIs are verified above (10.1126/science.add9330; 10.1038/s41586-024-07558-y; 10.1038/nature09818) and could be added if the refs slide has room.

## Image credits

- There is one image in the deck: the cover (`assets/images/content-library/case-studies/h01/10b-segmentation-overlay.jpg`). It has an image-specific credit and licence on slide 1 (H01 release, Lichtman Lab / Harvard & Connectomics at Google, CC BY 4.0, Shapson-Coe et al. 2024) and again on slide 58. The licence is verified against the H01 release page.
- No other images. No missing credits.
