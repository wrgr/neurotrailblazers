# Graduate deck claim audit — 26 September 2026

Every quantitative, historical and regulatory claim on the five graduate decks (243
slides, including speaker notes) was checked against primary sources. One report per
deck sits beside this file, with a row per claim: slide, claim, verdict, source and
location in the source, and the change made.

| Deck | Slides | Verified | Corrected | Qualified | Hypothetical (labeled) | Unverified |
|---|---:|---:|---:|---:|---:|---:|
| [Introduction (Module 7)](module07-introduction.md) | 59 | 35 | 18 | 19 | 5 | 4 |
| [Tools and Methods (Module 8)](module08-tools-and-methods.md) | 56 | 28 | 24 | 8 | 6 | 3 |
| [Algorithms and Applications (Module 9)](module09-algorithms-and-applications.md) | 58 | 19 | 10 | 7 | 7 | 2 |
| [Synapse Detection](synapse-detection.md) | 39 | 45 | 9 | 3 | 0 | 3 |
| [Ethics and Governance](ethics-and-governance.md) | 31 | 39 | 9 | 10 | 2 | 2 |
| **Total** | **243** | **166** | **70** | **47** | **20** | **14** |

**Verdicts.** *Verified* matches the named source. *Corrected* was wrong or
misattributed and has been fixed. *Qualified* was approximately right but needed an
estimate label, date, version or hedge. *Hypothetical* is an invented teaching number,
now labeled on the slide. *Unverified* could not be traced to a primary source; each
is softened or listed for a decision below.

## Corrections worth knowing about

- **Retinal direction selectivity (Modules 7, 9).** Two papers had been merged into one
  finding. Briggman et al. 2011 is starburst → direction-selective ganglion cell wiring;
  Kim et al. 2014 is bipolar → starburst space–time wiring.
- **Lappalainen et al. 2024 (Modules 7, 9).** The model's predictions were compared
  with recordings from 26 prior studies, not "then tested" in new experiments.
- **Fly brain scale (Module 7, Unit 01).** ~0.08 mm³ and ~125 TB at 4×4×40 nm, not
  0.02–0.03 mm³ and 40 TB (that was neuropil only). The fly-to-mouse-mm³ jump is ~12×,
  not ~40×. Growth from worm to mm³ is four orders of magnitude, not nine.
- **EM versus light (Module 7, Unit 02, Introduction plan).** The saving is roughly a
  million-fold in voxels; there is no source for "five orders of magnitude" in cost.
- **Whole-mouse-brain storage (Modules 7–9, Unit 01).** Kept at ~800 PB, now labeled an
  estimate with its basis (500 mm³ at 4×4×40 nm, 8-bit, uncompressed). Abbott et al.
  2020 give a rougher ~1 EB, now cited alongside.
- **H01 miss rates (Synapse Detection).** Excitatory and inhibitory *miss rates* (11% vs
  35%) differ threefold; recall (89% vs 65%) does not.
- **Ethics references.** DOI 10.1016/j.neuroimage.2021.118579 is Laird (2021), not
  Betzel & Bhatt. UNESCO adopted its neurotechnology Recommendation on 11 November
  2025. H01 data are CC BY 4.0 per the release data page.
- **BossDB (Module 8).** H01 is not a BossDB collection. The dedicated BossDB paper is
  Hider et al. 2022 (10.3389/fninf.2022.828787).

## Propagated to site pages

The same errors appeared outside the decks and were fixed to match:
`technical-training/01-why-map-the-brain.md` (fly row, jump ratio, storage basis),
`technical-training/02-brain-data-across-scales.md` (voxel ratio),
`teaching/lectures/connectomics-01-introduction.md` (voxel ratio),
`content-library/infrastructure/synapse-detection.md` (miss rates, Synful scope, expert
agreement, SynapseNet, ~33 nm sections, Muth 2025), and
`content-library/connectomics/ethics-and-governance.md` with its seed-paper record.

## Needs owner decision

1. **Hemibrain licence.** Janelia's project page says CC BY 4.0; the DataCite record for
   the v1.0 deposit says CC BY-NC 4.0. The deck flags the conflict. Ask Janelia.
2. **Unsourced heuristics.** "About forty person-hours" per cell and "20 cells is often
   enough" (Module 9, slide 17); "pilot is 1–2% of the project" and "3–5 full inference
   passes" (Module 8, slides 21, 24, 36). Now labeled as heuristics; cite or keep.
3. **"A dozen distinct neurites" per µm³** (Module 7, slide 12; Unit 01) and
   **"segment neurites down to 50–100 nm"** (Module 7, slide 28). No primary source found.
4. **BossDB hosting list** (Module 7, slide 49). Witvliet and Hildebrand confirmed; H01
   is hosted on Google Cloud; MICrONS and Kasthuri need a browser check of
   bossdb.org/projects.
5. **H01 consent.** The *Science* supplement was not reachable, so the consent location
   (Ethics, slide 9) rests on softened wording. *(Imaging duration resolved 26 September:
   "326 days" is in the published paper's text, PMC11718559.)*
4a. **BossDB hosting** *(resolved in the site audit: MICrONS, Kasthuri, Witvliet and the
   zebrafish volume are on BossDB; H01 is not).*
6. **Synapse Detection.** The within-brain F1 spread versus method gaps (slide 18) and
   the FAFB voxel size (slide 31; almost certainly 4×4×40 nm, full text not reached).

## Access limits

Nature, Science, Cell and PubMed pages were frequently blocked (403 or CAPTCHA).
Auditors used PubMed Central and Europe PMC full text, Crossref metadata, bioRxiv and
author-hosted PDFs instead. Each report names what it could not reach.

## Verification after edits

All five decks re-rendered from source; `check_deck_freshness.rb` passes. A browser
check of all 243 rendered slides found no text outside slide bounds and no broken
images (the check was confirmed to flag an injected overflow).
