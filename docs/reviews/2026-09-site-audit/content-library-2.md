# Site audit, wave 2: content library part 2

**Area:** `content-library/connectomics/**`, `content-library/cell-types/**`,
`content-library/neuroanatomy/**`, `content-library/proofreading/**`
(21 existing pages, about 59,000 words, plus one new page).
**Date:** 26 September 2026. **Branch:** `compass-workshops`. Nothing was committed.

Checked against `docs/reviews/2026-09-site-audit/canonical-facts.md`, BRAND_GUIDE §2,
`docs/reviews/2026-09-fabrication-audit-pages.md` and `docs/reviews/claim-audit/`.
Earlier fixes were kept: T31 in motif-analysis; the Turner 2022 reattributions in
neuron-type-identification, glia-recognition and neuroai-bridge; the ethics claim audit;
the Harris, Spacek & Harris, Lewis and Shepherd & Harris wording in neuroanatomy; and
T32 elsewhere.

## Summary counts

| Type | Fixes |
|---|---|
| Accuracy | 187 |
| Polish | 51 |
| Voice | 70 |
| Missing content | 39, including one new page |

- **DOIs:** every DOI added or kept in these pages was resolved through Crossref
  (api.crossref.org) or Europe PMC, and title, first author, journal, volume and pages
  were compared. About 150 references were checked.
- **Synthetic labels:**
  - Used: **T67** (cell-types), **T75**, **T76** and **T77** (proofreading).
  - Reserved but unused: T60–T66, T68–T74 and T78–T79.
  - T31 in motif-analysis was kept.
- **Validators:** all seven pass, run after every edit: `validate_frontmatter`,
  `validate_figure_refs`, `validate_technical_evidence`, `validate_paper_counts`,
  `validate_dictionary`, `validate_code_span_paths` and `validate_toggled_classes`.
- **Residual grep across the area:** no hits for these hype words: audacious,
  revolutionary, unlock, empower, cutting-edge, delve, leverage, seamless, crucial,
  transformative, groundbreaking. No British spellings remain (licence, labour,
  neighbour, colour, centre). None of the wrong canonical figures remain ("7,000
  chemical", "550,000", "65,000", "287 proofreaders", `version=1507`), and no
  TODO, TBD or "coming soon" markers.

## New content

- **`content-library/connectomics/comparative-connectomics.md`** (new, permalink
  `/content-library/connectomics/comparative-connectomics/`). It covers the backlog item
  in `NEXT_CONTENT_PASS.md` §"reference layer": what transfers across worm, fly, mouse and
  human, and what does not. All numbers on the page come from primary sources read in this pass:
  - **Datasets and scale:** canonical facts for White 1986, Winding 2023, FlyWire,
    hemibrain, MICrONS and H01.
  - **Weak edges and reproducibility:** Schlegel 2024, PMC11446831, full text. A single-synapse
    hemibrain edge has a 42% chance of appearing in one FlyWire hemisphere and 16% in both.
    Edges of more than 10 synapses reproduce over 90% of the time; they are 16% of edges
    but about 79% of synapses.
  - **Cell types:** Schlegel 2024 reports 8,453 types and that about a third of hemibrain
    types could not be reliably re-identified.
  - **Worm variability:** Witvliet 2021, PMC8756380 via NCBI BioC. About 43% of connections
    are not conserved between isogenic animals, but these hold only 16% of synapses. Brain
    synapses rise from about 1,300 to about 8,000 over development.
  - **MICrONS proofreading:** MICrONS 2025, PMC11981939. 1,433 neurons have proofread axons,
    and axons took 100–1,000 edits each.
  - **Supporting sources:** H01 glia-to-neuron ratio; Cook 2019 (385 male neurons); Badea 2007
    (mouse brain about 500 mm³).
  - **Structure:** it ends with five questions to ask before comparing datasets and a
    "what this page does not cover" section.
- Other gaps filled inside existing pages are listed in the table: a completed 10 × 10
  synthetic matrix in network-analysis-methods, a sparsity-only control in neuroai-bridge,
  a T67 connectivity example in neuron-type-identification, and the BRAIN CONNECTS awards
  from NIH RePORTER in connectome-history.

## Fixes

| File | Issue | Type | Fix (source) |
|---|---|---|---|
| connectomics/connectome-history | Credited Nichol Thomson with most of the tracing | Accuracy | Thomson did the sectioning and micrographs. Southgate and White did the tracing, over about 15 years (Emmons 2015, doi:10.1098/rstb.2014.0309) |
| connectomics/connectome-history | "Key findings" of White 1986 included motifs and sex dimorphism | Accuracy | Replaced with what the abstract says. Motifs are credited to Varshney 2011, the male tail to Jarrell 2012 and the whole male to Cook 2019 (DOIs verified) |
| connectomics/connectome-history | Sporns 2005 scales mapped to MRI, tracing and EM; Gray Type I/II equated with excitatory/inhibitory; Palay credited with PSDs | Accuracy | Corrected against the primary texts (PMC1239902, PMC1244535, doi:10.1083/jcb.2.4.193) |
| connectomics/connectome-history | MICrONS "2021, ~500M"; larval fly "~3,016"; Helmstaedter "~1,000"; FlyWire "76 labs" | Accuracy | Now 2025 *Nature*, >200,000 cells, ~524M synapses; 3,016 neurons and ~548,000 synapses; 950 neurons; "at least 76 labs" (canonical facts; doi:10.1038/nature12346) |
| connectomics/connectome-history | BRAIN CONNECTS section was vague, and MouseConnects was credited to "Lichtman, Jain" | Accuracy / Content | Canonical first-award facts, plus four real awards from NIH RePORTER (UM1NS132250, UM1NS132253, U01NS132161, UM1NS132358) |
| connectomics/connectome-history | Hype: "Volume EM revolution", "the field is accelerating" | Voice | Replaced with checkable numbers (15 years for 302 neurons vs 33 person-years for 139,255) |
| connectomics/open-problems-undergrad | Unsourced FlyWire "expectation", the "widely acknowledged" claim, "zettabytes", EyeWire "hundreds of thousands", 2025 synapse-detection work with no citation | Accuracy | Sourced or removed: Codex >60,000 users (codex.flywire.ai); RePORTER abstract quotes; human-brain figure shown as our arithmetic (~1.9 ZB); EyeWire 350,000 (blog, 31 Mar 2025); Mohinta et al. arXiv:2509.17041 |
| connectomics/open-problems-undergrad | Graph size "10⁵ nodes, 10⁷–10⁸ edges"; exabyte figure unattributed | Accuracy | FlyWire has 139,255 neurons and 2.7M edges of 5 or more synapses; the exabyte figure is now attributed to Abbott 2020 (doi:10.1016/j.cell.2020.08.010) |
| connectomics/open-problems-undergrad | Worked example on reciprocity had no source and ignored prior work | Accuracy / Content | Cites Song 2005 and Lin 2024 (PMC11446825), and explains how a student project can still be new |
| connectomics/open-problems-undergrad | Helmstaedter NRN review misdated; many references lacked DOIs | Polish | Now Helmstaedter 2026, 27:101–120; DOIs added |
| connectomics/ethics-and-governance | British spellings (licence, labour, centre and others) | Polish | Converted to American outside quotations. The claim-audit content is unchanged |
| connectomics/motif-analysis | "≈4×" reciprocity credited to Song and Perin, and called "most robust" | Accuracy | Credited to Song 2005 only (rat L5). Perin 2011 is cited for the common-neighbor rule (PMC1054880, PMC3069183) |
| connectomics/motif-analysis | "Milo convention" motif numbering; misstated motif profiles; E→I→E called an FFL | Accuracy | Sporns & Kötter numbering explained; profiles taken from Milo 2002 and 2004; E→I→E corrected to a disynaptic chain |
| connectomics/motif-analysis | Empirical p = r/K; p < 10⁻¹⁰ from 10,000 nulls; igraph `subisomorphic()` | Accuracy | Now (r+1)/(K+1), p ≈ 10⁻⁴, and `subisomorphic_vf2`/`motifs_randesu`. DotMotif executors checked against PMC8219732 |
| connectomics/graph-representations | "~100 classes"; "~8,000 types"; unsourced synapse ranges; "<1% of neighbors" | Accuracy | 118 classes (White 1986); more than 8,400 types (Schlegel); 66% of edges have 1–2 synapses (Winding); nearby pairs 11.6% (Song 2005) |
| connectomics/graph-representations | Worked example used an invented CAVE schema | Accuracy | Real MICrONS columns (`pre_pt_root_id`, `post_pt_root_id`, `size`); drops root ID 0 |
| connectomics/network-analysis-methods | Varshney cited for "lognormal, not power law"; small-world and hub claims for fly unsourced; SBM credited to Peixoto | Accuracy | Corrected to Varshney's text (PMC3033362); Watts & Strogatz values; Pavlovic 2014; Peixoto credited with the nested SBM |
| connectomics/network-analysis-methods | Worked-example matrix ended in "..." | Content | Completed synthetic 10 × 10 matrix (N1–N10) with computed answers |
| connectomics/neuroai-bridge | Transformers listed as recurrent; Schlegel said to use GNNs; vague *C. elegans* ablation claim; Billeh overclaim | Accuracy | Corrected; Yan 2017 (doi:10.1038/nature24056) as the ablation-prediction example |
| connectomics/neuroai-bridge | Worked example had no sparsity control | Content | Third RNN variant added, with the arithmetic |
| cell-types/axon-dendrite-classification | Calibers, branching angles, "smooth" axons, mitochondria and polarity claims | Accuracy | Aligned with Unit 06; notes that EM does not show microtubule polarity (Baas 1988) |
| cell-types/axon-dendrite-classification | "Bin A/B/C" called site vocabulary, but the site uses it for claims | Accuracy | Renamed to high/medium/uncertain |
| cell-types/axon-dendrite-classification | H01 figure caption said "six-class" | Accuracy | States that 3 of 6 classes are present and the labels are model output |
| cell-types/neuron-type-identification | FlyWire "~8,000 types"; Elabbady and Schneider-Mizell cited incompletely | Accuracy | 8,453 types; *Nature* 640:478–486 and 640:448–458 (PMC11981918, PMC11981935) |
| cell-types/neuron-type-identification | Worked example concluded "callosal-projecting" | Accuracy | Target is now "unknown", because it cannot be told within the volume |
| cell-types/neuron-type-identification | No operational definition of a type; no connectivity example | Content | Schlegel cross-brain definition; synthetic example on release T67; Scala 2021 on continuous variation |
| cell-types/glia-recognition | Microglia said to make no synapse contacts; OPCs said to have no synapses; inner tongue misdescribed | Accuracy | Wake 2009, Tremblay 2010, Bergles 2000 (DOIs verified); outer and inner tongue corrected |
| cell-types/glia-recognition | Astrocyte figure caption described a "process" | Accuracy | The frame shows perinuclear cytoplasm beside a nucleus |
| neuroanatomy/dendrite-biology | Mushroom threshold ">0.6 µm³" (it is a 0.6 µm head diameter); unsourced type frequencies | Accuracy | Harris 1992 and Arellano 2007 (PMC2518053) |
| neuroanatomy/dendrite-biology | "Ribosomes absent / no local translation in axons"; microtubule polarity numbers; Steward & Levy overstated | Accuracy | Shigeoka 2016; Baas 1988; Steward & Levy 1982 values (71% under mounds) |
| neuroanatomy/myelin-and-nodes | Myelin period; "optimal g-ratio 0.6–0.7 for CNS"; unsourced wrap-count table | Accuracy | Kirschner 2010; Rushton ~0.6 against CNS ~0.77 (Chomiak & Hu 2009); lamellae computed as arithmetic |
| neuroanatomy/myelin-and-nodes | H01 caption said "a few percent", but the image reads 13.4% | Accuracy | The caption now separates count from area |
| neuroanatomy/myelin-and-nodes | Node and internode numbers; unmyelinated "local interneurons" | Accuracy | Arancibia-Cárcamo 2017; Micheva 2016 (PV basket-cell myelin) |
| neuroanatomy/soma-ultrastructure | Somatic mitochondria "largest, 1–10 µm"; "COPI/COPII visible"; neuromelanin duplicated; Bhatt 2009 off-topic | Accuracy | Corrected against the H01 figure scale bar; Bhatt removed |
| neuroanatomy/axon-biology | "All axonal proteins made in soma"; "vesicles never in dendrites"; "no ribosomes in AIS" | Accuracy | Hafner 2019; Rall 1966; Palay 1968 (PMC2107452) |
| neuroanatomy/axon-biology | Unsourced bouton, shaft and mitochondria sizes; calyx "~600 active zones"; mossy fiber boutons called terminal | Accuracy | Shepherd & Harris 1998; Lewis 2018; Sätzler 2002 (554); Rollenhagen 2007 |
| neuroanatomy/synapse-classification | Gap junction described as "pentalaminar" (that is a tight junction) | Accuracy | 2 nm gap (Revel & Karnovsky 1967), below one pixel at 4–8 nm |
| neuroanatomy/synapse-classification | Gray 1959 credited with the vesicle-shape criterion; unsourced PSD, cleft and target figures | Accuracy | Uchizono 1965; Colonnier 1968; Harris & Weinberg 2012; High 2015; Beaulieu & Colonnier 1985 |
| neuroanatomy/synapse-classification | One bouton onto two dendrites called "convergent" | Accuracy | Changed to divergent |
| neuroanatomy/organelle-cues | Mitochondria size rules; "neurons do not store glycogen"; vesicles rule out dendrites | Accuracy | Lewis 2018 and Faitg 2021 (region-dependent); Saez 2014; dendrodendritic footnote |
| neuroanatomy/* (6 files), proofreading/* (5 files) | Slug-style `primary_units` never rendered the "Backs Unit" pill | Polish | Now two-digit unit numbers ("05"–"08") matched against `_data/technical_track.yml` |
| proofreading/proofreading-tools | CAVE deployments vague; CAVE "paradigm shift" claim; split and merge mechanics; seed placement contradicted FlyWire 101 | Accuracy | CAVE paper (PMC12074985) and FlyWire 101 |
| proofreading/proofreading-tools | Materializations described as permanent; Neuroglancer panels called anatomical planes | Accuracy | Versions 943 and 1300 are long-lived and v1507 has expired (canonical §10); panels are XY/XZ/YZ |
| proofreading/proofreading-tools | Ohyama 2015 called "the larval connectome"; unsourced CATMAID "petabyte bottleneck" | Accuracy | Winding 2023 added; the claim is removed |
| proofreading/worked-examples | Invented segment IDs without a synthetic release | Accuracy | Scenarios moved to release T75; the H01 figure is marked as the only real data |
| proofreading/worked-examples | Rules of thumb presented as standards; the public MICrONS release implied to be editable | Accuracy | Softened; `minnie65_public` is read-only |
| proofreading/error-taxonomy | c2/c3 1.6×/2.1× caption unsourced; Plaza 2014 misattributed; "180° branches never biological" | Accuracy | Verified in Shapson-Coe 2024 (PMC11718559; 257 vs 400 merge fixes, 504 vs 238 split fixes per cell); Plaza attribution removed; T-branches exist |
| proofreading/error-taxonomy | Funke cited as arXiv v1 | Accuracy | IEEE TPAMI 41(7):1669–1680, doi:10.1109/TPAMI.2018.2835450 |
| proofreading/proofreading-strategies | FlyWire accuracy check stated without its result | Content | 826 random neurons re-proofread gave an average F1 of 99.2% by volume (Dorkenwald 2024, PMC11446842, full text) |
| proofreading/proofreading-strategies | Exhaustive-cost arithmetic implied, then closed on a slogan ("not a plan, it is an alternative to having one") | Voice / Accuracy | States 200,000–400,000 person-hours, which is 100–200 years at 2,000 h a year |
| proofreading/proofreading-strategies | Li 2020 listed but never used | Content | Cited for compartment-based merge detection: 90.6% of inter-class merges at 2.7% false positives (Crossref abstract, doi:10.1007/978-3-030-59722-1_9) |
| proofreading/proofreading-strategies | EyeWire 120,000 (2014) conflicted with other site figures | Accuracy | Kept with its date and added "350,000 players over thirteen years" (EyeWire blog, 31 Mar 2025, read this pass) |
| proofreading/proofreading-strategies | "Not all proofreading is created equal"; "dramatically"; "neighbouring"; "comprehensive" | Voice / Polish | Plain wording |
| proofreading/metrics-and-qa | The synapse-level example said a shifted synapse produces no edge-level error, but a new A→C edge is a false positive | Accuracy | Corrected |
| proofreading/metrics-and-qa | ERL "introduced by Januszewski 2018"; "ERL 1,000 µm means neurons are fully correct" | Accuracy | Now "used by" Januszewski 2018; the overclaim is removed |
| proofreading/metrics-and-qa | Quality targets could be read as published standards | Accuracy | Labeled as our suggested starting points |
| proofreading/metrics-and-qa | MICrONS cited as the 2021 bioRxiv preprint; Funke cited as the arXiv version; no DOIs | Accuracy / Polish | *Nature* 640:435–447 (2025); TPAMI 2019; all DOIs checked on Crossref |

## Needs owner decision

1. **`reference_images` front matter (57 entries on the 21 pages).**
   - None of the image files exist, and no layout renders the blocks (see the
     `_includes/figure.html` comment).
   - `NEXT_CONTENT_PASS.md:414` schedules clearing them, so they were left in place.
   - Several captions assert results for figures that were never made:
     - motif-analysis:30 says "observed vs expected in *C. elegans* … reciprocal motifs
       significantly overrepresented". Milo 2002 reports FFL and bi-fan motifs, not reciprocity.
     - network-analysis-methods:35 claims optic-lobe modules match "known visual layers".
     - neuron-type-identification:33 claims a UMAP that "validates connectivity".
     - graph-representations:32 gives "N~1M" compartments and "~8K" types.
     - myelin g-ratio caption says "0.6–0.7 optimal", which contradicts the corrected text.
     - soma caption gives "5,000x magnification".
     - connectome-history includes a timeline and a scale plot.
     - organelle-cues includes a decision flowchart and an MVB-frequency claim.
   - Recommendation: delete the blocks now rather than wait.
2. **MouseConnects and NeuroTrailblazers students** (open-problems, Problem 7). The old
   text said MouseConnects "explicitly" plans on NeuroTrailblazers-trained students. The
   public award abstract only commits to involving undergraduates. Restore the claim
   only if a source exists.
3. **Ethics open items carried from the claim audit:**
   - where H01's consent and IRB statement is (the supplement is still unchecked);
   - whether to keep "nothing published so far identifies anyone";
   - which hemibrain license governs;
   - Laird 2021 is characterized from its abstract only.
4. **Unsourced textbook values left as approximate** in neuroanatomy: AIS length 20–60 µm,
   SER 30–80 nm, MVB 250–500 nm, lysosome and autophagosome sizes, ER–mitochondria
   contact 10–30 nm. Decide whether to source these or mark them "approximate".
5. **References listed but never cited:**
   - Bhatt 2009, in two neuroanatomy pages;
   - Rasband 2010 and Kole & Stuart 2012, in axon-biology.
   Keep them as further reading, or drop them.
6. **Two smaller checks:**
   - The ~80% excitatory figure (DeFelipe & Fariñas 1992; Markram 2004) is kept but
     hedged; neither primary text was readable.
   - The glia astrocyte worked example keeps a "high" confidence call on two glycogen
     granules. Decide whether it should be "medium".
7. **Unconfirmed H01 figures:**
   - "11,038 voxels" in the H01 before/after caption comes from
     `scripts/render_em_figures.py` and was not re-run. The caption now says "of this section".
   - The NeuTu row gives the hemibrain as its largest published use. Scheffer 2020's
     methods were not checked for NeuTu specifically.
8. **Spelling convention.** This area is now American English. The ethics lecture deck and
   `teaching/lectures/ethics-and-governance.md:53` still say "licence". Pick one convention
   for the whole site.

## Outside my area

- **`content-library/index.md`:**
  - Add a row for the new
    `/content-library/connectomics/comparative-connectomics/` page in the connectomics table.
  - Line 97 says "portal licences", which should be "licenses" to match the page.
- **`docs/planning/NEXT_CONTENT_PASS.md:410`:** tick the comparative-connectomics item,
  with a one-line note of its sources.
- **EyeWire player counts:**
  - `neuronauts/index.html:1512` says about 120,000 and `initiatives/outreach.md:41` says
    200,000+.
  - The EyeWire blog of 31 Mar 2025 says 350,000 over thirteen years; 120,000 was the 2014 figure.
  - Date each figure or use 350,000.
- **Astrocyte "process" framing:**
  - `_data/em_figures.yml:59-60`, `technical-training/07-glia.md:130-131` and
    `course/decks/marp/07-glia.marp.md:84-94` describe the H01 astrocyte frame as a fine
    process. It shows perinuclear cytoplasm beside a nucleus.
  - `_data/em_figures.yml` also says "neighbours".
- **`_data/em_figures.yml:89`:** "11,038 voxels" should say "in this section".
- **`course/decks/marp/06-axons-and-dendrites.marp.md:62`:** "ribosomes effectively absent
  from axons" should add "past the initial segment" (Palay 1968).
- **Slug-style `primary_units`** that never render also appear in
  `content-library/case-studies/{c-elegans-revisited,flywire-whole-brain,h01-human-cortex,microns-visual-cortex,mouseconnects-himc}.md`.
- **`content-library/case-studies/mouseconnects-himc.md:320`:** check that "NeuroTrailblazers-trained
  students contribute to MouseConnects" does not imply a formal role.
- **`content-library/case-studies/c-elegans-revisited.md`:** the coordinator flagged
  "~7,000 chemical synapses". A re-grep on 26 Sep finds no "7,000" in the file, so it has
  already been fixed.
