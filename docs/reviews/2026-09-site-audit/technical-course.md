# Technical Course audit: units, atlas, tutorials, slide pages, dictionary, data

*Audited 26 September 2026 on branch `compass-workshops`. Nothing committed.*

**Scope:** `technical-training/index.md`, Units 01–09, `atlas-connectomics-reference.md`,
`proofreading-tutorials.md`, `technical-training/slides/*.md` (wrapper pages),
`technical-training/dictionary/`, `_data/connectomics_dictionary.yml`,
`_data/technical_track.yml`, `_data/technical_evidence.yml`,
`_data/technical_capabilities.yml`. Added by the coordinator partway through:
`_data/em_figures.yml`, `course/decks/marp/07-glia.marp.md` and
`course/decks/marp/06-axons-and-dendrites.marp.md`. The journal club is out of scope.

**Method.** Five parallel passes covered Units 01–03, Units 04–06, Units 07–09, the
atlas with tutorials, slide pages and data files, and the dictionary. I then reviewed
their diffs, fixed cross-unit inconsistencies and carried out the coordinator's follow-up
items. All arithmetic was recomputed in python3. All 29 DOIs added in this pass resolve
on Crossref with the expected first author and year. Figures were compared with the
image files themselves.

## Summary

| Type | Fixes |
|---|---:|
| Accuracy | 122 |
| Polish | 48 |
| Voice | about 98 sentence-level edits |
| Missing content | 12 |

Two sub-pass edits were reverted:
- The lecture durations in six slide wrappers had been reset to the sum of their
  per-slide minutes. That broke agreement with the units' "Time" rows. It is a teaching
  decision, listed below.
- A stale "35 exports came to 88 MB" figure had been put back. The plan had already
  retired it.

## Key accuracy fixes

- **Merge errors and motifs (Units 01 and 09, dictionary, Unit 09 cards).** The pages no
  longer say that merges inflate dense motifs "superlinearly", toward the interesting
  answer. They now match the decks (commit 9410df9): a merge can close triangles, leave
  open wedges, collapse edges or create a self-loop that the graph drops. A split can
  delete or reroute an edge. Which way the count moves depends on the motif and the
  graph-construction rules, so model the errors and do not assume they cancel. "Error
  band" is now "sensitivity band, conditional on the error model".
- **Unit 06 reciprocity.** Reversing *some* synapses within multi-synapse connections
  raises measured reciprocity (synthetic simulation: 5% → about 16%, reproduced at 17%).
  Flipping whole connections lowers it (about 4.3%). Both cases are now stated.
- **Unit 06 calibration example.** "84% overall" was impossible on 20 items. It is now
  17/20 = 85%.
- **Units 05 and tutorials.** At 40 nm sections, a 200–500 nm edge-on synapse spans
  5–12 sections, not "two to five".
- **Unit 04.** The voxel count is now 1.6 × 10¹⁵ (1 mm³ ÷ 640 nm³ = 1.5625 × 10¹⁵),
  which matches Unit 02's ~1.6 PB. The GPU arithmetic was recomputed: 1,850 GPU-days,
  3.7 days on 500 GPUs. "3–5 inference passes" is labeled a rule of thumb.
- **Pyramid overhead (Units 02 and 04, dictionary).** "+30–50%" is replaced by about 1/3
  (xy halving: 1/4 + 1/16 + …).
- **Egress claim (Unit 04, dictionary).** The claim that moving 1 PB out costs more than
  a year of storage is false at AWS list prices (about $50–90k egress against about
  $258k for a PB-year of S3 Standard). It was reworded.
- **H01 imaging time.** "326 days" is in the PMC text of the published paper, the
  author manuscript PMC11718559: "The total imaging time for the 1 mm3 sample was 326
  days." Unit 03 now cites Shapson-Coe et al. 2024 and notes that the 2021 preprint gives
  the same figure. canonical-facts §2 says "preprint only", which is out of date.
- **H01 c2/c3 figures** (Unit 08, tutorials, `em_figures.yml`) are verified in
  PMC11718559. The text reads: "c3 agglomeration required 1.6-fold less correction of
  merge errors (257 vs. 400 merge correction operations per cell, p < 10⁻⁷) but 2.1-fold
  more correction of split errors (504 vs. 238 …)", over "104 randomly-selected
  neurons".
- **Counts from the site's own renders.** "11,038 voxels" and "197 objects" come from
  `scripts/render_em_figures.py` against the public H01 volume. They are credited that
  way and scoped to the image ("in this section").
- **The "astrocytic process" figure shows part of an astrocyte soma.** The nuclear
  envelope is at the right. The framing was corrected in Unit 07, `em_figures.yml` and
  the Unit 07 deck, including its instructor note. The file name was left alone.
- **Atlas.**
  - Larval fly: 3,016 neurons and about 548,000 synapses, imaged at 3.8 × 3.8 × 50 nm.
  - FlyWire: "first whole-brain connectome of an adult fly". It had been called the first
    of an animal with complex behavior, but the larval fly came first. Its numbers are
    now 139,255 neurons, about 54.5 million synapses and 33 person-years.
  - H01: multibeam SEM, not ssTEM; 1.4 PB aligned (1.8 PB raw).
  - MICrONS: about 524 million synapses.
  - MouseConnects: an in-progress 10 mm³ target, not "scaling toward whole brain".
  - The title of the Harris 2015 reference was corrected.
- **Unit 01.**
  - The unsourced "a dozen neurites per µm³" claim (an open claim-audit item) is
    replaced by an argument that follows from the unit's own size table.
  - The Shiu 2024 and Hulse 2021 citations were added.
  - The like-to-like result is attributed to Ding 2025.
  - H01's "up to 50 synapses" follows the abstract; the unsupported mouse comparison was
    removed.
- **Unit 02.**
  - "Neurites to 50–100 nm" (an open claim-audit item) is replaced by a z-sampling
    argument.
  - Array tomography is ~200 nm lateral (Micheva 2007).
  - The gyral bias in tractography was stated the wrong way round (Schilling 2018).
  - MICrONS covers VISp, AL, RL and LM, not PM.
  - The MICrONS registration fiducials are now given: 2,934, mean residual 3.8 µm. The
    paper's own parts sum to 2,936, and the page says so.
- **Unit 03.**
  - Slow-fixation signs are separated, with Korogod 2015 and Pallotto 2015 cited.
  - The MICrONS perfusate and its staining sequence without uranyl acetate (after Hua
    2015) are now given.
  - GridTape is correctly described.
  - Multibeam throughput is cited to Eberle 2015.
  - The unsourced "5–20% shrinkage" was removed.
- **Unit 04.**
  - The MICrONS lab link at `/notebooks/microns-lab/` exists. The text now describes what
    the lab does: v1507 static exports, hash-checked, with drift against v1412, and no
    token needed.
  - Examples prefer versions 943 and 1300, and the page notes that v1507 was scheduled
    to leave live CAVE on 31 July 2026.
  - Neither unit page presents a caveclient pin as current.
  - Four image cards described content that is not in the images; they were rewritten or
    removed.
- **Unit 07.**
  - "Glia occupy 20–40% of volume" had no source. It is replaced by H01's glia-to-neuron
    ratio of 2:1 (32,315 vs 16,087) and Kikuchi 2020 (12.2% of one astrocyte's
    territory).
  - "20–60 sheaths per oligodendrocyte" became "tens", because published means disagree.
  - A gap in the rubric was closed.
- **Unit 08.** VI and ERL definitions were corrected (Meilă 2007; Januszewski 2018).
  - The "steep z-trajectories" heading contradicted its own text.
  - The unsourced FlyWire claim of "millions of edits" was replaced.
  - A `[!TIP]` block did not render and promised material that does not exist; it is now
    a plain paragraph.
- **Unit 09.**
  - The degree-heterogeneity share is now 77 of 137 excess pairs (56%).
  - The worked example is labeled synthetic.
  - The Lappalainen 2024, Pedigo 2023 and Witvliet 2021 citations were added.
- **Dictionary.**
  - Expected Run Length's merge sensitivity had been stated backwards.
  - En bloc staining happens before embedding.
  - The microglia soma size had been copied from the oligodendrocyte entry.
  - Idempotency had been defined as determinism.
  - Section references in the storage entries were wrong.
  - Entries were re-aligned to the revised unit text: oligodendrocyte sheaths, myelin
    lamellae, pyramid overhead and merge-error motifs.
  - A unit filter was added, which the page already promised.
- **`technical_evidence.yml`.** Four truncated or paraphrased paper titles now match
  Crossref.

## Fix table (condensed; one row per substantive change)

| File | Issue | Type | Fix (source) |
|---|---|---|---|
| index.md | Description said "Canonical…"; opening paragraph duplicated the hero; one long paragraph of dashes; headings named topics; `last_reviewed` was March | Voice/Polish | Plain description; three short paragraphs; headings state the claim (the total hours sentence still sums the units in Liquid); review date updated |
| index.md | Did not say that the atlas is excluded from the hours total | Accuracy | Stated. Liquid sums only `content_type: path` |
| 01 | "Dozen neurites per µm³" had no source | Accuracy | Derived from the unit's own size table |
| 01, 09 | Merges inflate motifs superlinearly toward the interesting answer | Accuracy | Direction depends on the motif and graph rules; model the errors (deck commit 9410df9) |
| 01 | H01/MICrONS PB sizes; human-brain bytes; fly "first"; BRAIN CONNECTS framing | Accuracy | canonical-facts §1, §2, §3, §8 |
| 01 | Central complex and taste model had no citations | Accuracy | Hulse 2021 (10.7554/eLife.66039); Shiu 2024 (10.1038/s41586-024-07763-9) |
| 01–03 | No sources list | Missing content | "Sources for the numbers in this unit" added, with DOIs checked on Crossref |
| 02 | Array tomography, expansion microscopy and MAPseq ranges | Accuracy | Micheva 2007; Gao 2019; Chen 2019 (3,579 cells) |
| 02 | Gyral bias stated backwards | Accuracy | Schilling 2018 (10.1002/hbm.23936) |
| 02 | Registration anchors had no source | Accuracy | MICrONS 2025 fiducials (PMC11981939); notes the paper's 2,936 vs 2,934 sum |
| 02, 04 | Pyramid "+30–50%" | Accuracy | About 1/3, arithmetic shown |
| 03 | Fixation signs; shrinkage figure; perfusate; stain sequence | Accuracy | Korogod 2015; Pallotto 2015; MICrONS Methods (PMC11981939); Hua 2015 |
| 03 | "1 mm³ takes about a year"; multibeam "gigapixel/s" | Accuracy | Recomputed (about 90 d continuous); Eberle 2015; 326 d attributed to Shapson-Coe 2024 (PMC11718559) |
| 03 | ROTO/rOTO spelling; triage answer gaps | Polish/Accuracy | rOTO; 160/200 nm, 80 nm, 0.02% |
| 01–03 | Visual-card captions did not match the images (EM micrograph, Street View, stock images, resin block) | Accuracy | Captions and alt text rewritten after viewing each file |
| 04 | Part A lab pointer was vague; "pick any version" | Accuracy | Lab contents described; versions 943/1300 preferred; v1507 expiry noted (canonical §10) |
| 04 | "Microseconds" per merge; ChunkedGraph claimed for DVID/CATMAID/neuPrint | Accuracy | Softened; CAVE only |
| 04 | 1.5 vs 1.6 × 10¹⁵ voxels; GPU-days | Accuracy | 1.6 × 10¹⁵; 1,850 GPU-days; 3.7 d on 500 GPUs |
| 04 | Egress cost comparison | Accuracy | Reworded (AWS S3 price page) |
| 04, 05, 06 | Image cards did not match images; decorative and stock cards | Accuracy/Polish | Rewritten; easy-button and title-background cards removed |
| 05 | Section-persistence arithmetic | Accuracy | 5–12 sections at 40 nm |
| 05 | Cleft width contradicted its own table; mitochondria said to be in spines; lamellae count | Accuracy | 15–30 nm uniform; "practically absent from most spines"; "a few to dozens" |
| 06 | Reciprocity direction | Accuracy | Both cases stated; simulation labeled synthetic |
| 06 | 84% impossible on 20 items; rubric gap; "no statistical correction" | Accuracy/Polish | 17/20 = 85%; < 80%; points to §4 |
| 06 | S18 image is Sheng & Kim 2011 Fig. 3 | Accuracy | Cited (10.1101/cshperspect.a005678) |
| 07 | 20–40% glia volume; "neurons do not contain glycogen"; 20–60 sheaths; OPC agreement | Accuracy | H01 2:1; Kikuchi 2020 (10.1093/cercor/bhz343); "rarely"; "tens"; reasoned, not asserted |
| 07, em_figures, 07 deck | "Astrocytic process" figure is a soma | Accuracy | Reframed as part of an astrocyte cell body |
| 08 | VI and ERL definitions | Accuracy | Meilă 2007; Januszewski 2018 |
| 08 | FlyWire "millions of edits"; "a few dozen person-hours"; `[!TIP]` block | Accuracy | 33 person-years (Dorkenwald 2024); price it from Part A; plain paragraph |
| 08 | VI check-yourself had no numbers | Missing content | Synthetic split/merge VI table |
| 09 | "Two-thirds" degree share; unlabeled synthetic data; missing citations | Accuracy | 77/137 (56%); labeled; Lappalainen 2024, Pedigo 2023, Witvliet 2021 |
| atlas | Larval fly, FlyWire, MANC, retina, Harris CA1, MICrONS, H01, zebrafish, MouseConnects and *C. elegans* rows | Accuracy | canonical-facts §1–§6; Janelia MANC page; Hildebrand 2017; Harris 2015 title (10.1038/sdata.2015.46) |
| atlas | Pointed to "Unit 03's cost arithmetic", which does not exist | Accuracy | Unit 01 §2 |
| tutorials | Caption said "red is a separate process" (there are two); voxel count not scoped; dead VAST link | Accuracy | "Processes"; "in this one section"; lichtman.rc.fas.harvard.edu/vast/ |
| slides/*.md | Export size; em dashes; self-link on slides/05; "robust" | Polish | Kept "tens of megabytes"; unit link; "reliable" |
| slides/index.md | No technical-deck size given | Missing content | "Ten decks of 14 to 19 slides", counted in `out/` |
| technical_evidence.yml | Four truncated titles | Accuracy | Crossref titles |
| technical_track.yml | Atlas summary claimed "reference figures"; "Canonical"; `last_updated` stale | Accuracy/Voice | Fixed |
| dictionary.yml | ERL, en bloc, microglia soma, lost-section gate, egress, pyramid, FIB-SEM, AIS, sign inference, spine apparatus, idempotency, synapse threshold, Peters' rule, FFN, anisotropy, merge error | Accuracy | Unit sections; Scheffer 2020; Winding 2023; Kasthuri 2015; Januszewski 2018; Lappalainen 2024 |
| dictionary.yml | Typical values that repeated the "matters" line (Proofreading, rOTO, en bloc) | Missing content | FlyWire 33 and hemibrain 50+ person-years; stain sequence |
| dictionary/index.md | Promised a unit filter it did not have; search skipped `typical` | Polish | Unit filter from `data-units`; `typical` searchable; attributes escaped |
| em_figures.yml | 11,038 voxels unscoped; "exclude axonal identity"; British spellings | Accuracy/Polish | "in this section"; softened; gray, color, labeled |
| 06 deck notes | "Ribosomes absent from axons" | Accuracy | "…past the initial segment" |
| all | Hype words (robust, landscape, leverage), British spellings, em-dash chains | Voice/Polish | Plain wording |

## Needs owner decision

1. **Lecture durations.** Six lecture plans' per-slide minutes do not sum to their stated
   lengths: 04 is 76 vs 80, 05 is 80 vs 75, 06 is 76 vs 75, 07 is 76 vs 70, 09 is 80 vs
   85, and the atlas is 60 vs 55. The stated lengths feed the units' "Taught" times. I
   reverted a sub-pass change so they stay consistent. Pick which number wins.
2. **canonical-facts §2.** "326 days" is in the published paper (PMC11718559), not the
   preprint only. Update the registry.
3. **Image reuse.** Unit 06's S18 is Sheng & Kim 2011 Fig. 3 (CSH Perspectives). Is
   reuse permitted? The "Pat Rivlin training materials" credits in Units 07–09 are
   unverified.
4. **Stock and duplicate images.** Units 02 and 03 share a stock "circuit-board brain"
   image, and Units 01–03 share one EM micrograph. Replace them with real data figures.
5. **Unit 07 glia volume.** Kikuchi's 12.2% is one astrocyte's territory in young rat. An
   adult whole-neuropil glia fraction needs a primary source.
6. **Filter key "building robust pipelines".** It is a hype word, but it is a filter key
   in both `_data/technical_track.yml:53` and `_data/concepts.yml:87`. Change both
   together or leave both.
7. **Not re-verified, left in.**
   - Kasthuri "~1,500 µm³" (attributed via Motta 2019).
   - Multibeam "61 or 91 beams" and "~1 Gpx/s peak".
   - The Gray type I/II cleft widths (textbook values; Gray 1959 would strengthen them).
   - Unit 01's resolution-table sizes, Unit 02's modality ranges and Unit 03's imaging
     parameter ranges. These are now labeled typical or estimates.
8. **Dictionary style.** About 20 entries use a spaced hyphen as a dash; it was left as
   house style.
9. **Proofreading tutorials figures.** Figures of a confirmed false split and a confirmed
   orphan are still open. They need a render from `proofread_104` against `c2`.

## Outside my area

- `notebooks/microns-lab/index.md:108`: `CAVEclient("minnie65_public", version=1507)`
  is past its expiry. Use 1300 or 943, or a `timestamp=`.
- `content-library/case-studies/h01-pipeline.md`:
  - Line 156: "ROTO" should be "rOTO".
  - Lines 117, 231 and 238: attribute "326 days" to Shapson-Coe 2024.
  - Line 237: "Parallel-beam imaging is the entire reason…" is wrong; MICrONS used five
    TEMs.
- `content-library/case-studies/mouseconnects-himc.md:11,43`: "flagship" should read "a
  BRAIN CONNECTS-funded project".
- `course/decks/04-*.md`, `course/decks/05-*.md`, `course/decks/06-*.md` and
  `course/units/figures/0[34]-*-selected-v1.md`: the same image-caption mismatches fixed
  on the unit pages. The S08 easy-button image in Unit 04 and the S01 decorative image in
  Unit 06 are still used.
- `course/decks/marp/02-brain-data-across-scales.marp.md:131` and
  `modules/module12.md:104`: "pyramid +30–50%" should read "up to ~33%".
- `course/decks/marp/06-axons-and-dendrites.marp.md` (S18): add the Sheng & Kim 2011
  citation.
- `_data/concepts.yml:87`: see decision 6.
- `_datasets/manc.md`: Janelia's page gives "about 23,000 neurons, 10 million
  pre-synaptic sites, 74 million post-synaptic densities", which can be cited.
- `content-library/journal-papers/index.md`: `validate_paper_counts` now reports "states
  96 papers, linked pages contain 95". This comes from another agent's concurrent edit.

## Validation

`validate_frontmatter`, `validate_figure_refs`, `validate_technical_evidence`,
`validate_dictionary` (127 terms, 126 with a typical value; "Connectomics" is exempt by
design), `validate_code_span_paths` and `validate_toggled_classes` all pass.
`validate_paper_counts` fails on `content-library/journal-papers/index.md`, which is
outside this area. `./scripts/render_marp.sh --html` re-rendered 41 decks. The glia deck
still has 18 slides and the axons-and-dendrites deck 19. `check_deck_freshness.rb`
reports that all 41 are fresh.
