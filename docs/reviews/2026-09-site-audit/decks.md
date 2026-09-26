# Deck audit: hand-edited Marp sources (September 2026)

Scope: `course/decks/marp/en585781/*.marp.md` (Modules 7–9),
`course/decks/marp/lectures/*.marp.md` (Synapse Detection, Ethics and Governance),
the technical-unit decks `course/decks/marp/0*.marp.md` and
`atlas-connectomics-reference.marp.md`, and `neurotrailblazers-template.marp.md`.
The generated decks in `course/decks/marp/modules/` were not touched.

Checked against `docs/reviews/2026-09-site-audit/canonical-facts.md` (numbers were re-grepped
after editing), the five `docs/reviews/claim-audit/` reports and the fabrication-audit fixes.
No claim-audit or fabrication-audit correction was reverted. Two pre-existing uncommitted edits
by earlier passes, the fictional `T795` label in Unit 04 and the fictional `T9` provenance
block in Module 9, were kept.

## Summary

| Type | Fixes |
|---|---:|
| Accuracy | 22 |
| Polish (American English, stale or wrong references, typos, consistency) | 11 rows (about 130 individual spellings) |
| Voice | 18 |

Slide counts are unchanged: Module 7 has 59 slides, Module 8 56, Module 9 58, Synapse Detection
39 and Ethics and Governance 31. Slide order is unchanged. Qualifications and sources were put in
speaker notes where possible. Slide-text edits replace words and do not add lines.

## Fixes

| Deck | Slide | Issue | Type | Fix |
|---|---|---|---|---|
| Template | 7 (stat) | "2,000 GB per cubic millimetre" is 2 TB, which is wrong by a factor of 1,000. MICrONS raw EM is ~2 PB | Accuracy | "~2 PB", "Raw EM imagery for about one cubic millimeter of mouse cortex"; source is now MICrONS Consortium 2025 (doi:10.1038/s41586-025-08790-w) |
| Unit 02 | 6 (notes) | Light-sheet "about five orders of magnitude cheaper". The claim audit already removed this from Module 7 and Unit 02 because no cost source exists | Accuracy | "about a million-fold fewer voxels than 4 × 4 × 40 nm EM (1 µm³ / 640 nm³ ≈ 1.6 × 10⁶)" |
| Unit 03 | 7 + notes | H01's 326 days was unattributed. The figure appears only in the 2021 bioRxiv preprint. Raw and aligned sizes were not both given | Accuracy | Slide: "1.8 PB raw (1.4 PB aligned); 326 days on a 61-beam SEM (2021 preprint)". Notes cite doi:10.1101/2021.05.29.446289 |
| Unit 04 | 7 (notes) | "A merge is adding an edge — microseconds". Module 8 was corrected to a median of ~4 s (CAVE, Fig. 2i) | Accuracy | "seconds of work (median ~4 s in CAVE, per Module 8)" |
| Unit 05 | 8 | "Large branched mitochondria … excludes axonal identity" overstates the cue, since axons carry mitochondria | Accuracy | "argues against axonal identity" |
| Unit 01 | 10 (notes) | "Merges manufacture triangles … biased toward the interesting answer." Module 9 (commit 9410df9) replaced this claim: the direction depends on the motif and construction rules | Accuracy | Aligned to Module 9: merges can add, collapse or redirect edges, so simulate and recompute |
| Unit 09 | 13 + notes | Same superlinear/one-direction merge claim; "error band" | Accuracy | Notes aligned to Module 9. Slide: "under a stated error model", "sensitivity band" (same line count) |
| Module 7 | 9 | "Module 9 spends most of Part B on why merges bias results in a specific and predictable direction", which contradicts Module 9 slide 36 | Accuracy | "Module 9 Part B shows how merges distort motif counts, and why you must test the direction rather than assume it" |
| Module 7 | 15 | "both are reported in the 1.4–2 PB range, depending on what is counted and how it is compressed" | Accuracy | "H01 is 1.8 PB raw (1.4 PB aligned), MICrONS about 2 PB raw" |
| Module 7 | 16 (notes) | "H01 is 1.4 PB and MICrONS ~2 PB raw" compares aligned with raw | Accuracy | "H01 is 1.8 PB raw (1.4 PB aligned) and MICrONS ~2 PB raw (MICrONS Consortium 2025)" |
| Module 7 | 25 | Table row "inflate dense motifs superlinearly" and box "biased toward the interesting answer" | Accuracy | Row and box now match Module 9: direction must be tested; unproofread segmentation is not automatically conservative |
| Module 7 | 26 | Checkpoint: "Merges bias results toward dense motifs" | Accuracy | "Merges and splits shift motif counts in directions you have to test, not assume" |
| Module 7 | 45 (new notes) | FlyWire, hemibrain and taste-model claims had no sources on the slide or the references slide | Accuracy | Speaker notes cite Dorkenwald 2024, Scheffer 2020 and Shiu et al. 2024 (doi:10.1038/s41586-024-07763-9) |
| Module 7 | 46 | MICrONS "~200,000 cells, ~500 million synapses". Canonical: more than 200,000 cells and 524 million synapses | Accuracy | ">200,000 cells, ~524 million synapses". New notes give the canonical MICrONS and H01 figures (84,035 segmented neurons in the larger subvolume; 57,180 cells, 16,087 neurons; 149,871,669 synapses) |
| Module 7 | 49 | BossDB "Holds: MICrONS, H01, …". This was an owner decision in the claim audit. BossDB's live project list (bossdb-metadata-snapshot…/mongo-data.json, read 26 Sep 2026) has MICrONS, kasthuri2015, witvliet2020 and hildebrand2017, and no H01 | Accuracy | H01 removed from the BossDB row. The Neuroglancer row reads "e.g. H01 (Google Cloud)". The check is recorded in the notes |
| Module 7 | 1 (notes) | "assignment and journal club paper are both on the last two slides". The last two slides are references and the license | Polish | "on slides 55 and 56" |
| Module 8 | 15 (notes) | 326 days attributed only to Collins et al. 2025 | Accuracy | Primary attribution is now the 2021 bioRxiv preprint, with Collins kept as secondary |
| Module 8 | 33 | Pyramid overhead "15–33%", but the notes compute ≈14% | Accuracy | "14–33%" |
| Module 8 | 44 | `caveclient 5.21.0` could read as current (current is 8.2.1) | Accuracy | Comment is now "# old example pin; record yours". The block was already labeled illustrative |
| Module 8 | 50 (notes) | Mouse brain ~500 mm³ cited to Collins et al. 2025. Canonical source is Badea et al. 2007 | Accuracy | "Badea et al. 2007, doi:10.1016/j.neuroimage.2007.05.046: 508.9 ± 23.4 mm³, C57BL/6J" |
| Module 9 | 42 | "Fly male and female CNS releases (2024–25)", while the notes and Module 7 give Cell 2026 and 2024–26 | Accuracy | "(2024–26)" |
| Ethics | 7 + notes | "Dataset: About 1.4 petabytes" did not say aligned or raw. Neurons missing | Accuracy | "1.4 PB aligned (1.8 PB raw)"; "About 57,000 cells (16,087 neurons); about 150 million synapses". Notes quote the Science figures |
| Ethics | 14 (notes) | "the pathology caveat two slides back" points to slide 12. The caveat is on slide 10 | Polish | "on slide 10" |
| Synapse Detection | 37 | "Cleft detection is solved" contradicts slide 5, which the claim audit softened to "can perform well in evaluated tissue" | Accuracy | "Cleft detection works well in evaluated tissue." |
| All five graduate decks | license slide | "Licence", "link the licence", "its own licences" | Polish | "License"/"license"/"licenses" |
| Ethics | throughout | 37 × licence/licences, 8 × labour, plus centralised, analysed, reanalyse, practising, neighbouring, millimetre, centre, judgement, labelling (front-matter description included) | Polish | American spellings. Quoted text was left alone; "Creative Commons Attribution 4.0 License" was already US spelling |
| Synapse Detection | throughout | localisation (5), generalisation (5), labelled (4), recognise, characterised, minimising, analysing, neighbouring, judgement (2) | Polish | American spellings. The quoted "generalizes well" was unchanged |
| Module 7 | 36, 3 (notes) | calibre, double-barrelled | Polish | caliber, double-barreled |
| Module 8 | 10 | centre | Polish | center |
| Module 9 | 7, 8, 9, 33 | millimetre (2), neighbouring, micrometres, neighbours | Polish | American spellings |
| Units 04–07 | several | colour (2), labelling, labelled (3), judgement, neighbourhood (4), fibre (3), micrometre, nanometres, behaviour, grey-matter (text only; the image filename was kept), licence | Polish | American spellings |
| Template | 9, 10 | behaviour, organisation | Polish | behavior, organization |
| Modules 8, 9 | 2, 10 | "The organizing question all module:", "for every defect, all module:" | Polish | "for the module", "in this module" |
| Module 8 | 4, 39, 48 | Heading "The platform landscape" (a banned hype word), repeated in the roadmap and divider | Voice | "The platforms you will actually use" in all three places |
| Unit 06 | 4 | Heading "Why this unit is high leverage" | Voice | "Why axon/dendrite errors are expensive" |
| Unit 03 | 17 | "infrastructure for robust reconstruction" | Voice | "the infrastructure that turns trusted acquisition into a versioned reconstruction" |
| Module 7 | 29 | "is not caution. It is a million-fold error" | Voice | "costs a million-fold more data and buys nothing" |
| Module 7 | 32 | "These are not weaker connectomics. They are …" | Voice | Single sentence with the claim first |
| Module 7 | 46 | "The important thing is not the size. It is the co-registration." | Voice | "What matters more than the size is the co-registration." |
| Module 7 | 47 | "That — not simulation — is what a wiring diagram is for." | Voice | "That, more than simulation, is …" (also Module 9 slide 44) |
| Module 7 | 50 | "Not compute, not storage. It is …" (fragment triad) | Voice | "…, ahead of compute and storage." |
| Module 7 | 51 | "is not a microscopy problem. It is …" | Voice | "depends on … more than on microscopes" |
| Module 7 | 52 | "That is not a disclaimer; it is a variable." | Voice | "Treat that as a variable in the analysis, not a disclaimer." |
| Module 8 | 32 | "the field's quiet superpower" | Voice | "The consequence: anyone can serve a volume." |
| Module 8 | 54 | "Reproducibility is not paperwork. It is the only thing …" | Voice | "Reproducibility is what lets you say which number you are defending." |
| Module 9 | 10 | "These are not bugs. They are consequences …" | Voice | "These follow from the physics and the data; they are not bugs to be patched." |
| Module 9 | 53 | "is not modesty; it is credibility" | Voice | "Saying that clearly builds credibility." |
| Synapse Detection | 1 (notes), 7, 14, 22 | "The goal is not … It is …"; "The honest budget line is not … It is:"; "aggregation is doing enormous work"; "is stark" | Voice | Stated directly: "The realistic budget line: …"; heading "aggregation changes the number" |
| Synapse Detection | 37 | "is not a property of the detector — it is a property of …" | Voice | "depends on its recall by class, …" |
| Ethics | 23 | "The mitigation is not a policy. It is writing …" | Voice | "The mitigation is a writing habit. Write the sample description into the claim, every time." |
| Units 01, 02, 09 | notes | "deliberately not about microscopes … It is"; "Not the finest … — the coarsest that works"; "Saying that plainly is part of …" | Voice | Plain declaratives |

## Verification

- Slide references were re-checked against the rendered slide numbers: Module 7 ("twelve
  slides", "six slides ahead", "three slides on", part ranges); Module 8 ("slide 21", part
  ranges); Module 9 part ranges; Synapse Detection ("previous two", "next four" ×2); Ethics
  ("two slides on", part ranges). Only the two notes fixed above were wrong.
- Arithmetic was recomputed: 1 mm³ at 4 × 4 × 40 nm = 1.5625 × 10¹⁵ voxels; the 800 µm cube is
  8 × 10¹⁴ px, 46 days (77 at 60% uptime); 0.05 mm³ at 8 nm isotropic ≈ 9.8 × 10¹³ voxels;
  GPU cost is 1,736 GPU-days, or 3.5 days on 500 GPUs; the reciprocity null is 72.7 expected pairs
  and 2.9×; egress for 1 PB is $50–90k; H01 E/I shares are 74.2%/67.1%; H01 classifier accuracy is
  86.89%/84.98% (Science text). All correct.
- `./scripts/render_marp.sh --html` finished, and `ruby scripts/check_deck_freshness.rb` reports
  "OK: all 41 Marp decks are rendered from their current sources". `validate_figure_refs`,
  `validate_generated_materials` and `validate_toggled_classes` pass.
- Overflow check: the scratchpad `slidecheck.cjs` (puppeteer-core, 1280×720) was run on all
  16 decks in scope, 430 slides. No element extends past its `<section>`, and no image is
  broken.

## Needs owner decision

1. **Merge-error direction, site-wide.** The Module 9 revision says the direction depends on the
   motif and the construction rules. Module 7 and the Unit 01 and Unit 09 deck notes now say the
   same. The unit pages still teach the older claim, "merges inflate dense motifs superlinearly …
   toward the interesting answer": `technical-training/01-why-map-the-brain.md:281,286` and
   `technical-training/09-connectome-analysis-neuroai.md:231–232,400`. Confirm the Module 9
   position, then align those pages. They are outside this area.
2. **Unit 06 reciprocity note** (deck slide 4 notes; unit §4). The claim is that random direction
   flips *raise* measured reciprocity. That holds only under the unit's multi-synapse argument,
   in which some synapses of a connection are reversed. Flipping whole edges lowers
   reciprocity. The unit page explains this; the deck note compresses it. Left as is, but worth
   one clarifying sentence on the unit page.
3. **Unchanged open items from the claim audit:** the hemibrain license conflict; the
   unsourced heuristics (forty person-hours, 20 cells, 1–2% pilot, 3–5 inference passes); "a
   dozen neurites per µm³" and "segment down to 50–100 nm" (Module 7 slides 12 and 28, Unit 02
   notes); the H01 consent location.
4. **Uncited counts on technical decks:** Unit 04 slide 7 ("197 distinct objects"), Unit 08
   slide 7 ("104 proofread cells … c3 needed 1.6× fewer merge fixes and 2.1× more split fixes")
   and Unit 08 slide 8 ("11,038 voxels"). These are site renders and case-study figures that
   could not be traced to a primary source in this pass. Keep them only if the H01 case study
   documents them.
5. **Third-party figure permissions** (flagged on the slides, unchanged): Sheng & Kim 2011 (CSHL
   Press, all rights reserved) on Unit 06 slide 13, and the SynapseWeb astrocyte image on Unit 07
   slide 6.

## Outside this area

- `technical-training/01-why-map-the-brain.md:281,286` and
  `technical-training/09-connectome-analysis-neuroai.md:231–232,400`: superlinear/one-direction
  merge claim (see owner decision 1).
