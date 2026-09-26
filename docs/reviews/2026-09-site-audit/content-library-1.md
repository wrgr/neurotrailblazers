# Site audit, September 2026: content library group 1

*Audited 26 September 2026 on branch `compass-workshops`. Nothing committed.*

**Area:** `content-library/index.md`, `content-library/em-figures.md`,
`content-library/case-studies/*` (6 pages), `content-library/imaging/*` (4),
`content-library/infrastructure/*` (4). 16 files, all edited.

**Sources used:** MICrONS Consortium 2025 full text (Europe PMC, PMC11981939);
Shapson-Coe et al. 2024 (*Science* PDF text, the PMC author manuscript PMC11718559
via NCBI efetch, and the 2021 bioRxiv preprint); Dorkenwald et al. 2024 and
Schlegel et al. 2024 (PMC full text); Varshney et al. 2011 (PMC3033362); Europe PMC
abstracts for Witvliet 2021, Cook 2019, Turner 2022, Ding 2025, Schneider-Mizell
2025; Korogod et al. 2015 (PMC4530226); NIH RePORTER API for UM1NS132250; Google
Research and Harvard Gazette announcements (Sept 2023); University of Cambridge
FlyWire release (Oct 2024); the H01 release `4nm_raw/info` file and Explore page;
Crossref for every DOI listed below; `docs/reviews/2026-09-site-audit/canonical-facts.md`.

## Summary counts

| Type | Count |
|---|---|
| Accuracy fixes (wrong or unsupported claims corrected, softened or sourced) | 41 |
| Polish (typos, British to American spelling, dash chains, stale notes, wrong section refs) | 34 |
| Voice (hype, restating summaries, motivational framing) | 38 passages rewritten |
| Missing content filled from verified sources | 12 |
| DOIs checked against Crossref | 53, all resolve to the cited paper; 29 DOI links added to reference lists |
| `reference_images` blocks deleted (coordinator request) | 12 files |
| `primary_units` slugs converted to unit numbers (coordinator request) | 5 case studies |

Validators: all seven pass after the edits (`validate_paper_counts` failed once
mid-pass on `content-library/journal-papers/index.md`, another agent's area; it
passes now).

## Findings and fixes

| File | Issue | Type | Fix (source) |
|---|---|---|---|
| case-studies/microns-visual-cortex.md | Caption "about 523 million synapses" | Accuracy | 524 million (paper's text; canonical §1c) |
| microns-visual-cortex.md | "SEM imaging at high throughput" under a TEM pipeline | Accuracy | "TEM imaging" (MICrONS used autoTEMs) |
| microns-visual-cortex.md | Proofreading "using ... the Spelunker interface" | Accuracy | ChunkedGraph (now CAVE) with a modified Neuroglancer (paper, "Proofreading" methods) |
| microns-visual-cortex.md | "manually matched thousands of fiducial points" | Accuracy / numbers | 2,934 fiducials (1,994 somata, 942 vessel points), 3.8 µm mean residual, 19,181 ROIs to 15,439 EM neurons (paper) |
| microns-visual-cortex.md | "required person-years of effort" | Accuracy | Paper gives no person-years figure; replaced with 1,046,656 edits to 16 Sep 2024 (paper) |
| microns-visual-cortex.md | minnie35 "released as unproofread automated output" | Unsupported | Removed; states why there are two subvolumes (re-trim and knife change, paper) and that the names count sections |
| microns-visual-cortex.md | Discussion Q quoted "real but modest", which appears nowhere | Accuracy | Reworded as a statistical rule |
| microns-visual-cortex.md | Hype: "one of the most ambitious", "unprecedented scale", "flagship", "the future of the field" | Voice | Rewritten; added what the combination does not show (causation) |
| microns-visual-cortex.md | Missing: detection accuracy, segmentation resolution, Ding's feature-vs-spatial result | Missing | 96% precision / 89% recall on 8,611 synapses; 8 × 8 × 40 nm; Ding 2025 abstract |
| case-studies/flywire-whole-brain.md | "first complete connectome of an adult animal brain" (C. elegans is an adult animal) | Accuracy | "first complete synaptic-resolution wiring diagram of an adult fly brain" |
| flywire-whole-brain.md | "~139,255" (tilde on an exact count) | Polish | 139,255 |
| flywire-whole-brain.md | 8,453 cell types attributed to the Dorkenwald dataset; "most complete catalog ... to date" | Accuracy | Attributed to Schlegel 2024 with 96.4% coverage, 3,643 hemibrain / 4,581 new, and the authors' "largest ever proposed" wording |
| flywire-whole-brain.md | Topic "flood-filling networks", tag `methodology:flood-filling-networks` | Accuracy | FlyWire did not use FFNs; now convolutional-network segmentation / `methodology:automated-segmentation` |
| flywire-whole-brain.md | "Convergence / Divergence / Recurrence: feedback loops are pervasive" (unsourced general claims) | Accuracy | Replaced with Dorkenwald 2024: information-flow tracing, half of optic lobe neurons receive ≥5 synapses from VCNs, mixed pre/post neurites; Lin et al. 2024 added (Crossref-verified 634:153-165) |
| flywire-whole-brain.md | "Navis/NAVis ... direct queries" | Accuracy | NAVis plus fafbseg; other access routes as listed in Dorkenwald 2024 Fig. 1c |
| flywire-whole-brain.md | FAFB section described only as "21 million images" | Missing | 7,062 sections, 4 nm/px, ~106 TB (Zheng 2018; canonical §3e) |
| flywire-whole-brain.md | Consortium size | Accuracy | Cambridge wording kept with attribution ("more than 76 ... 287 researchers", verified on cam.ac.uk); Princeton's "at least 76" noted |
| flywire-whole-brain.md | "mouse brain is several hundred times larger" (my own draft, caught) | Accuracy | "about 500 mm³ (Badea 2007), roughly 500× the MICrONS mm³" (canonical §7) |
| flywire-whole-brain.md | Hype: "landmark", "monumental", "pioneered", "state-of-the-art", "opening of a new era" | Voice | Rewritten; closing section now says what the snapshot does not show (sex differences, variability) per Dorkenwald 2024 |
| case-studies/h01-human-cortex.md | "the first nanoscale connectomic reconstruction of human brain tissue"; "H01 provides the first opportunity"; "H01 is the only dataset of its kind" | Accuracy | Loomba et al. 2022 also reports human cortex EM connectomics; now "largest volume ... to their knowledge" attributed to the PMC author manuscript, Loomba cited |
| h01-human-cortex.md | "At 1.4 petabytes, H01 is comparable in raw data volume to MICrONS" | Accuracy | 1.8 PB raw vs ~2 PB raw; 1.4 PB labeled aligned (canonical §2) |
| h01-human-cortex.md | "Current consensus is that [re-identification] is extremely unlikely" | Unsupported | "Nobody has shown it can, and nobody has shown it cannot"; link to Ethics and governance |
| h01-human-cortex.md | CAVE "seeded from the c3 agglomeration" | Unverified | Removed (paper says CAVE hosts proofreading; seeding not stated) |
| h01-human-cortex.md | "extensive supplementary tables with cell-type classifications ..." | Unverified | Narrowed to table S8 (counts of inputs), which the paper cites |
| h01-human-cortex.md | Hype: "watershed moment", "profound implications", "resolution never before achieved", "first step on this path" | Voice | Rewritten with the authors' own verified quotes |
| case-studies/h01-pipeline.md | "5,293" layers unverified (canonical CHECK) | Accuracy | Verified: the release `4nm_raw/info` z-size is 5,293; the preprint says 5,292; both now stated |
| h01-pipeline.md | 326 days unattributed (canonical CHECK) | Accuracy | Attributed to the PMC author manuscript (PMC11718559) and the 2021 preprint; the sentence is not in the *Science* PDF text |
| h01-pipeline.md | 287 + 96 invalid sections; 110–135 sections per wafer; three FFN models at 32/16/8 nm; kimimaro; fixative recipe | Verified | All in the 2021 preprint; "287 + 96" now attributed to it |
| h01-pipeline.md | 32.2% / 33.7% detached spines (flagged by technical-course audit) | Verified | Found in the PMC author manuscript text; attribution added |
| h01-pipeline.md | "ROTO" | Polish | "rOTO", noting the paper writes "ROTO" |
| h01-pipeline.md | "Parallel-beam imaging is the entire reason petascale volume EM is feasible"; "longer than a research career" | Accuracy | MICrONS reached petascale with five TEMs; unsupported single-beam comparison removed |
| h01-pipeline.md | Neuron table omitted 868 unclassifiable neurons | Missing | Added 868 (5.4%) and 8,803 pyramidal-shaped (Science text) |
| h01-pipeline.md | CAVE "seeded from the c3 agglomeration" | Unverified | Removed |
| h01-pipeline.md | Preprint license "more restrictive" without naming it | Missing | CC BY-NC-ND 4.0 (preprint page footer) |
| h01-pipeline.md | British spellings (millimetre, neighbour, colour, licence, organised, greyscale, anaesthetised, Skeletonisation, catalogued ...) | Polish | American spelling throughout, including alt text; quotes untouched |
| h01-pipeline.md | "genuinely", "far worse", "extraordinarily strong", "stark", "The honest reading" | Voice | Plainer wording |
| case-studies/c-elegans-revisited.md | "Before you quote" box described re-materialized releases, which do not exist for this dataset | Accuracy | Rewritten for reconstructions (White, Varshney, Cook, Witvliet) |
| c-elegans-revisited.md | "Key Early Findings" credited White 1986 with motif analysis and "genetically specified" wiring | Accuracy | Motif counting attributed to later work (Varshney 2011); stereotypy qualified by Witvliet 2021 |
| c-elegans-revisited.md | "No central brain"; "Mostly hardwired ... limited plasticity" | Accuracy | Contradicted Witvliet ("full brain"; substantial individual differences). Now "no layered or columnar architecture" and "stereotyped, but not identical" |
| c-elegans-revisited.md | "Mutants ... available for most of the 302 neurons" | Unsupported | Replaced with CeNGEN whole-nervous-system expression profiling (Taylor et al. 2021, *Cell* 184(16):4329-4347, Crossref-verified) |
| c-elegans-revisited.md | "the only organism for which a relatively complete pipeline exists" | Accuracy | "first ... and one of the most complete" |
| c-elegans-revisited.md | Varshney "re-examined ... notebooks, corrected errors" | Accuracy | Precise: used White's notebooks and micrographs to assign left/right neurons (Varshney full text); "over 3,000 contacts" now says it includes gap junctions and NMJs |
| c-elegans-revisited.md | Missing numbers | Missing | Cook 2019 node counts (460 / 579); Witvliet ~1,300 → ~8,000 chemical synapses, brain only (canonical §5) |
| c-elegans-revisited.md | "heroic", "remarkable", "modern incarnation" | Voice | Removed |
| case-studies/mouseconnects-himc.md | "flagship" (description, caption, NeuroTrailblazers section) | Accuracy | Removed; no source uses it |
| mouseconnects-himc.md | Volume described as "spanning CA1, CA3, the dentate gyrus"; aims listed as complete DG/CA3/CA2/CA1 wiring and full mossy-fiber and Schaffer reconstructions | Unsupported | Replaced with the RePORTER abstract's aims; subregion coverage stated as unknown |
| mouseconnects-himc.md | Method was "serial sectioning with multibeam SEM" building on H01; topic "serial-section TEM" | Accuracy | Semithin sections, multibeam SEM plus ion-beam milling, micro-CT targeting, Allen atlas registration (RePORTER abstract); two 91-beam SEMs (Harvard Gazette, verified); topic now multibeam SEM |
| mouseconnects-himc.md | CAVE implied as the project's platform | Unsupported | "The abstract does not name the proofreading platform" |
| mouseconnects-himc.md | Single data-size figure | Accuracy | All three projections given with sources (NIH, Harvard ~10,000 TB, Google ~25 PB) |
| mouseconnects-himc.md | "how many granule cells each mossy fiber contacts" (mossy fibers are granule-cell axons) | Accuracy | Corrected to entorhinal divergence onto granule cells and mossy-fiber contacts onto CA3 |
| mouseconnects-himc.md | NeuroTrailblazers section implied a formal role ("students ... will be equipped to contribute directly", project "benefits from additional proofreading labor") | Accuracy | Now: developed within HI-MC; no formal role; the abstract's undergraduate commitment quoted verbatim |
| mouseconnects-himc.md | Missing funding and partner facts | Missing | PI, dates, partners, $30M + $3M (Harvard Gazette), RePORTER budget years through FY2026 |
| mouseconnects-himc.md | "Previous projects have consistently encountered unforeseen obstacles" | Voice | One concrete example: MICrONS perfused 2018, main paper 2025 |
| imaging/em-principles.md | "reduced OsO₄ penetration at block edges" (gradient runs the other way) | Accuracy | "toward the block center" |
| em-principles.md | Table row "ssTEM (ATUM)"; ATUM tape is opaque | Accuracy | "ssTEM (grids or GridTape)"; "Multi-beam SEM (ATUM sections)" |
| em-principles.md | Multi-beam SEM "combines the throughput advantages of SBEM with the image quality of TEM" | Unsupported | Replaced with what it does: sections survive imaging; H01 at 125–190 Mpx/s |
| em-principles.md | "routine biological EM achieves 1-5 nm resolution" | Accuracy | Resolution for stained tissue is set by stain and pixel size; volumes imaged at 4–8 nm/px |
| imaging/tissue-preparation.md | "Even 5-10 minutes of ischemia can produce visible degradation" | Unsupported | Number removed; H01 immediate-immersion practice cited (preprint Methods) |
| tissue-preparation.md | Shrinkage "10-20% linear" here but "10-30%" in misconceptions | Accuracy | Sourced: 16% linear (Kalimo 1976) and 15% per axis (Kinney 2013) as cited by Korogod 2015; ECS 15.4% cryo vs 2.47% chemical (Korogod 2015, Crossref-verified) |
| tissue-preparation.md | "Typical project duration" row unsourced | Accuracy | Replaced with MICrONS ~6 months and H01 326 days as anchors |
| imaging/artifact-taxonomy.md | ECS "~20% in vivo, often <5% fixed" | Accuracy | Korogod 2015 values, in vivo 18–22% as cited there |
| artifact-taxonomy.md | "osmium penetration limit, typically 200-500 μm"; chatter "0.5-5 μm"; beam damage "~10-100 e/Å²"; "several hundred nanometers below" | Unsupported | Numbers removed; mechanisms kept; cryo-EM threshold explicitly distinguished |
| artifact-taxonomy.md | ATUM "sections ... rather than destroyed as they are imaged, so a lost region can sometimes be re-imaged" | Accuracy | Separates handling losses (reduced by ATUM/GridTape) from imaging failures (re-imageable); H01 knife-change loss (preprint) |
| artifact-taxonomy.md | "Missing sections are the most common cause of split errors"; 100 nm axon "spans only 3-4 sections" | Accuracy | "a major cause"; geometry qualified (axon parallel to the section plane) |
| artifact-taxonomy.md | Worked example put a penetration gradient "near the edge of the block" | Accuracy | "deep in the block, far from every face" |
| imaging/acquisition-qa.md | "pre-2015 QA was often informal"; PSD peak "~200-500 nm"; cross-correlation ">0.7"; "hundreds of thousands of dollars" | Unsupported | Replaced with H01's per-tile workflow manager (247 M tiles); thresholds now calibrated on your own data; mini-pilot interval labeled a heuristic |
| infrastructure/reconstruction-pipeline.md | MICrONS "more than 2 petabytes" | Accuracy | "about 2 PB of raw imagery" (canonical §1d) |
| reconstruction-pipeline.md | Drift arithmetic: 0.5 px × 10,000 sections "accumulates to ~70 px" | Accuracy | Random walk gives 0.5 × √10,000 = 50 px (~400 nm at 8 nm/px); systematic bias grows linearly |
| reconstruction-pipeline.md | Layer labels inconsistent (L4 "Agglomerated objects" vs "Post-processing"; worked example used L4 for synapses) | Polish | Diagram and headings aligned |
| infrastructure/data-formats.md | "as Unit 04 §2 sets them out" (storage table is in §5) | Polish | §5, linked |
| data-formats.md | "compression 2-10×"; "a single pyramidal cell mesh can be >100 MB" | Unsupported | Qualitative wording |
| infrastructure/provenance-and-versioning.md | "You can always go back to a specific materialization version" | Accuracy | Versions expire; 943 and 1300 are the long-lived MICrONS versions; static exports outlive live CAVE (canonical §10) |
| provenance-and-versioning.md | CAVE users listed as "MICrONS (minnie65, minnie35)" and vague "Allen Institute datasets" | Accuracy | `minnie65_public` and H01 |
| provenance-and-versioning.md | `caveclient==5.14.0` pin read as current (canonical §9) | Accuracy | Labeled as a pattern; 8.2.1 (PyPI, 26 Sep 2026) stated as current |
| provenance-and-versioning.md | "Anyone can re-run the analysis years later" | Accuracy | The image pins software, not data availability |
| infrastructure/synapse-detection.md | British spellings (localisation, generalisation, labelled, judgement ...) | Polish | American; quotations untouched; the anchor id `start-here-this-is-a-solved-problem-with-three-residuals` kept for inbound links |
| index.md | "licences", "labour", "localisation", "catalogue" | Polish | American spelling |
| index.md | Stale note about `reference_images` metadata | Polish | Removed (blocks deleted) |
| index.md | New page `connectomics/comparative-connectomics` not listed | Missing | Row added |
| index.md | FlyWire "140K neurons"; MouseConnects "flagship ... ongoing project"; "richly detailed", "landmark", "DRY" | Voice / accuracy | 139,255; "in progress, no data released"; plainer description |
| index.md | "Deep dives into landmark connectomics projects" | Accuracy | "How four published connectomes were built ..., plus one project still in progress" |
| em-figures.md | "29 of 35 decks had silently gone stale" undated | Accuracy | Dated to the August 2026 check recorded in `scripts/check_deck_freshness.rb`; CI step confirmed in `.github/workflows/validate.yml` |
| em-figures.md | Size table presented as exact | Polish | Labeled approximate textbook values |

Paper-count claims in `index.md` (300, 300, 242, 240, 160 ×3, 142, 115, 100, 42, 21, 16 `other`,
2 `mri`) were recounted from `_data/corpus_2000.json` and all match.

## Needs owner decision

1. **H01 imaging duration and other author-manuscript-only facts.** The 326 days, the
   32.2% / 33.7% spine figures and the "largest volume of human cortex" sentence
   are in the PMC author manuscript (PMC11718559) but not in the *Science* PDF text
   I could read. The pages now attribute them to the author manuscript. Canonical
   facts §2 says 326 days is "preprint only". The author manuscript is a second
   source for it, and canonical-facts could be updated to say so.
2. **MouseConnects funding status.** `datasets/mouseconnects.md` (another area) says
   the award was among Harvard grants terminated in April 2025. I could not verify
   the termination from RePORTER, so the case study says only that RePORTER shows
   budget-year awards through FY2026. Decide whether to state the termination and
   reinstatement, and with what source.
3. **The Explorer's MICrONS dimensions.** The case study now gives the paper's in vivo
   1.3 × 0.87 × 0.82 mm, per canonical facts. The two-source conflict itself is still
   open.
4. **Unit mapping for case studies.** The case studies' `primary_units` came from the
   Primary units column of the library index (for example MICrONS 01, 03, 08, 09). The
   old slugs (for example `unit-02-em-acquisition`) did not match the real unit
   numbering, so a content owner should confirm the new mapping.
5. **`synapse-detection.md` anchor id.** The first heading keeps the legacy anchor
   `#start-here-this-is-a-solved-problem-with-three-residuals`, which no longer matches
   the heading text. I kept it in case other pages link to it. Rename it once inbound
   links are checked.

## Outside my area

- `content-library/journal-papers/index.md`: `validate_paper_counts` reported "claims
  10 papers for network-analysis, but network-analysis.md contains 9". That was
  mid-pass, and it passes now, so presumably the owning agent fixed it.
- `datasets/mouseconnects.md`: the April 2025 termination claim (see owner decision 2).
- `docs/reviews/2026-09-site-audit/canonical-facts.md` §2: add the PMC author
  manuscript as a source for the 326 days, and mark "5,293 layers" as verified
  against the release `4nm_raw/info` z-size (5,293; the preprint says 5,292).
- `modules/module12.md:238` and `neuronauts/index.html:1442` still carry "523 million"
  per canonical facts §1c (not re-checked; not my area).
- `technical-training/03-em-prep-and-imaging.md:132` says shrinkage is "5–20% linearly
  depending on protocol". That is consistent with, but broader than, the Korogod-cited
  15–16% now used in the imaging pages; consider citing Korogod 2015 there too.
