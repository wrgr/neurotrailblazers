# Canonical facts registry: dataset numbers for site-wide consistency

Compiled 2026-09-26 for the September 2026 site audit. Every number below was read
from a primary source during this pass (paper full text through PMC, Europe PMC,
NCBI BioC, bioRxiv or the publisher's own PDF; official release, program and
package pages). Where two primary sources disagree, both are recorded, and one
phrasing is recommended.

**How to use this file.** Use the "Canonical phrasing" wording. If you need
a different level of detail, take the number from "Exact numbers" and give the
source. The "Don't say / check" lists are a **snapshot** from `git grep`
over `*.md`, `*.html`, `*.yml` and `*.ipynb`. The snapshot excludes `docs/`,
`scripts/`, `course/decks/marp/out/`, `_data/journal_papers.yml` and
`assets/analysis/`. Other editors are changing these files in parallel, so
**re-grep before editing**. Line numbers drift.

Legend: **OK** = consistent with the source. **FIX** = wrong or unsupported.
**CHECK** = defensible but inconsistent with the canonical phrasing.

---

## 1. MICrONS cubic millimeter (minnie65 / minnie35)

Primary: MICrONS Consortium et al. (2025) "Functional connectomics spanning multiple
areas of mouse visual cortex", *Nature* 640:435–447, doi:10.1038/s41586-025-08790-w,
PMC11981939. Secondary official: MICrONS Explorer, <https://www.microns-explorer.org/cortical-mm3>
and <https://tutorial.microns-explorer.org/> (both read 2026-09-26).

### 1a. Volume dimensions
- **Canonical:** "about 1 mm³ of mouse visual cortex (VISp plus three higher visual areas)".
  If you need dimensions, use: "1.3 × 0.87 × 0.82 mm in vivo (MICrONS Consortium 2025)".
- **Exact:**
  - Paper, Main: "at the cubic millimetre scale in mouse visual cortex (in vivo dimensions 1.3 × 0.87 × 0.82 mm³)".
  - MICrONS Explorer: "This IARPA MICrONS dataset spans a 1.4mm x .87mm x .84 mm volume of cortex in a P87 mouse."
- **Conflict:** the paper and the Explorer differ (1.3 vs 1.4 mm; 0.82 vs 0.84 mm). Prefer the paper
  and label it "in vivo". If you quote the Explorer figure, attribute it to the Explorer.
- **Animal:** one male mouse. From the paper's Methods timeline: "Perfusion: 16 March 2018 (P87)". Two-photon imaging ran P75–P80.
- **Don't say / check:** `modules/module12.md:238` ("~1.4 x 0.87 x 0.84 mm") gives the Explorer figure without attribution. **CHECK**

### 1b. Cells and neurons
- **Canonical:** "more than 200,000 cells". Do not use a single neuron count without its scope.
  If a neuron count is needed, use: "about 84,000 individually segmented neurons in the larger (65%) subvolume
  (MICrONS Consortium 2025)". The Explorer's "an estimated 120,000 neurons" may be used only
  if it is attributed to the Explorer.
- **Exact (paper):**
  - Abstract: "an electron microscopy reconstruction containing more than 200,000 cells and 0.5 billion synapses".
  - Proofreading: "we have split almost all neurons into single-soma objects, bringing the total number of
    individually segmented neurons to 84,035 (Extended Data Fig. 3)".
  - Methods, cell classification: "This model predicted 82,247 neurons detected within the larger subvolume."
  - Nuclei: "Nuclei were also automatically segmented (n = 144,120) within subvolume 65."
    The v1507 cell-info export used by the site's lab also has 144,120 nucleus rows.
  - Functional: "dense calcium imaging of around 75,000 neurons" (abstract). The exact figure is "an estimated 75,909 excitatory neurons" (2P section).
- **Exact (Explorer):** "The anatomical data contains more than an estimated 200,000 cells, and 120,000 neurons". The
  tutorial landing page says "200,000 cells, 75,000 neurons with physiology, and 523 million synapses".
- **Where "65" comes from:** minnie65 is the subvolume holding about 65% of the *sections*
  ("the other contains 65% of the sections (sections 14,816–27,904)"). It is **not** a count of 65,000 neurons.
- **Don't say / check:**
  - "65,000-neuron core dataset" (was at `content-library/case-studies/microns-visual-cortex.md:245` at first grep; since edited). **FIX** wherever it reappears.
  - "~80,000 neurons" (was in the `microns-visual-cortex.md:41` caption at first grep). **FIX**: use 84,035 or "about 84,000".
  - `modules/module12.md:238` "(~120,000 neurons)": this is the Explorer's figure. **CHECK**: attribute it, or use the paper's 84,035.
  - The "~75,000 neurons" functional count is **OK** everywhere it is labelled "functionally imaged" or "calcium imaging".

### 1c. Synapses
- **Canonical:** "about 524 million synapses (more than half a billion)".
- **Exact (paper, "Automated reconstruction"):** "We automatically detected and associated a total of 524 million synaptic
  clefts across both subvolumes (subvolume 35: 186 million, subvolume 65: 337 million)." The abstract says "0.5 billion synapses".
  Note that 186 + 337 = 523, a rounding artefact in the source.
- **Explorer:** "Automated synapse detection measured more than 523 million synapses."
- **Detection accuracy (paper):** precision 96%, recall 89%; partner assignment 98%.
- **Recommendation:** use "524 million" (the paper's text) and cite the paper. "523 million" is acceptable
  only when attributed to the Explorer. "~500 million", "0.5 billion" and "half a billion" are OK for
  rounded or outreach use.
- **Don't say / check (523 without attribution):** `content-library/case-studies/microns-visual-cortex.md:41`,
  `modules/module12.md:238`, `neuronauts/index.html:1442`. **CHECK**: switch to 524 million or attribute to the Explorer.
  Already on 524: `_datasets/microns.md:8,21,27`.

### 1d. Raw data size
- **Canonical:** "about 2 PB of raw EM imagery".
- **Exact (paper, "EM dataset"):** "A total of 26,652 sections were imaged by 5 customized automated TEMs (autoTEMs),
  which took approximately 6 months to complete and produced a dataset composed of 2 Pb of raw data at a resolution of
  approximately 4 nm". The unit is printed as "Pb" in both the Nature HTML and the PMC text. Elsewhere the paper says
  "To achieve this at petabyte scale". Arithmetic from the paper's own numbers (26,652 sections × ~1.2 × 0.82 mm
  montages at 4 nm, 8-bit) gives ~1.6 × 10¹⁵ bytes. That fits petabytes, not petabits, so read "Pb" as PB.
- **Don't say / check:** `modules/module12.md:238` ">1 PB raw imagery": true but inconsistent. **CHECK**: say "~2 PB".
  The ~2 PB statements in `_datasets/microns.md`, `microns-visual-cortex.md:143`, `reconstruction-pipeline.md:70`,
  `module07…marp.md:400`, `neuronauts/index.html:1311` and `neuronauts/index.html:2146` are **OK**.

### 1e. Voxel size and resolution
- **Canonical:** "imaged at about 4 nm per pixel, 40 nm sections (4 × 4 × 40 nm); the aligned volume used for
  segmentation is 8 × 8 × 40 nm".
- **Exact (paper):** "sectioned into 27,972 serial sections (nominal thickness 40 nm)". "Pixel sizes for all systems were
  calibrated within the range between 3.95 and 4.05 nm per pixel". "Although imaging was performed with 4 nm resolution, the
  aligned imagery volume was generated at 8 nm resolution to decrease data size for subsequent processing."
- CAVE annotation `pt_position` units are 4 × 4 × 40 nm voxels (as used in `notebooks/microns-lab`). **OK**

### 1f. Section counts
- **Canonical:** "27,972 sections cut at 40 nm; 26,652 imaged".
- **Exact (paper):** 27,972 cut; 26,652 imaged. "An 800-µm region (sections 7,931–27,904) … was selected for further processing".
  The subvolumes are sections 7,931–14,815 (~35%, minnie35) and 14,816–27,904 (~65%, minnie65).
- **Don't say / check:** `course/decks/marp/en585781/module08-tools-and-methods.marp.md:1345` "~28,000 sections" is a rounding. **OK**

### 1g. Other MICrONS numbers that are often repeated
- Proofreading: "The released segmentation now contains all 1,046,656 edits of the proofreading that had occurred as of
  16 September 2024". The paper publishes **no person-years figure**. The site's ethics lecture already says so. **OK**
- Proofread-neuron outputs: "more than 900,000 synaptic connections between neurons".

---

## 2. H01 (human temporal cortex)

Primary: Shapson-Coe A. et al. (2024) "A petavoxel fragment of human cerebral cortex reconstructed at nanoscale
resolution", *Science* 384:eadk4858, doi:10.1126/science.adk4858, PMC11718559. Read from the Science PDF.
Europe PMC returned HTTP 500 for this PMCID. Also read: bioRxiv preprint doi:10.1101/2021.05.29.446289
(version posted 25 Nov 2021), and the release page <https://h01-release.storage.googleapis.com/landing.html>.

| Fact | Canonical phrasing | Exact source text (Science 2024 unless noted) |
|---|---|---|
| Volume | "about 1 mm³ (1.05 mm³ after compression correction)" | "a total imaged volume of 1.05 mm3 after correcting for a compression of 28% in the cutting direction"; summary: "1 mm3 in volume" |
| Cells | "about 57,000 cells (57,180 counted)" | Summary: "about 57,000 cells". Results: "There were 49,080 neurons and glia (Fig. 4A) and 8100 blood vessel–related cells (57,180 cells total)". The preprint says 57,216. |
| Neurons | "16,087 neurons" / "about 16,000 neurons" | "Glia outnumbered neurons 2:1 (32,315 versus 16,087)" |
| Synapses | "about 150 million synapses (149,871,669 detected)" | "In total, 149,871,669 synapses were automatically detected in the volume. A total of 111,272,315 … excitatory and 38,599,354 as inhibitory." Summary: "about 150 million synapses" |
| Aligned data size | "1.4 petabytes" | "yielding a dataset ~1.4 petabytes in size"; summary: "comprises 1.4 petabytes" |
| Raw acquisition size | "1.8 PB raw" (say "raw") | Methods summary: "a raw data size of up to 350 gigabytes per section, or 1.8 petabytes in total. From a total of 247 million tiles, 196 million image tiles were stitched". The preprint says "~2.1 petabytes (PB)". |
| Sections | "5,019 sections, mean thickness 33.9 nm" | "5019 sections with a mean thickness of 33.9 nm were collected on tape … giving a total thickness of 170 µm". The PDF glyph renders µm as "mm". The preprint says "we sectioned 5,292 sections at a section thickness that averaged 33 nm (range 30-40 nm)". |
| Pixel / voxel | "4 × 4 nm pixels, ~33 nm sections (released at 4 × 4 × 33 nm)" | "imaged by multibeam scanning EM at 4 × 4 nm2 resolution". The 33 nm z is the release grid, not a paper sentence. |
| Donor | "a 45-year-old woman with drug-resistant epilepsy" | "from the anterior part of the middle temporal gyrus of a 45-year-old female". Preprint Methods: "A 45 year old woman with a history of simple and complex partial seizures … refractory to medical management". |
| Imaging duration | "326 days of imaging" | **Published paper**: "The total imaging time for the 1 mm3 sample was 326 days." Verified 2026-09-26 in the PMC text of Shapson-Coe et al. 2024 (PMC11718559), Results, image-acquisition paragraph; also in the 2021 preprint. Cite Shapson-Coe et al. 2024. |
| Blood vessels | "about 230 mm of blood vessels" | Summary: "about 230 millimeters of blood vessels" |

- **Release-page conflict:** the landing page says "183 million annotated synapses, 100 proofread cells". The paper says 149,871,669
  synapses, and the release contains 104 proofread cells. `content-library/case-studies/h01-pipeline.md:63` already explains
  this. Do not use 183 million without that caveat.
- **"5,293 layers"** (`h01-pipeline.md:61,201`) was not verified in this pass. The preprint's 5,292 is a *sectioned* count. **CHECK**
- **Don't say / check:**
  - "1.4 PB raw" or "1.4 PB of raw data" anywhere: 1.4 PB is the aligned volume, and raw is 1.8 PB. Current uses of "1.4
    petabytes of imaging data" (`content-library/case-studies/h01-human-cortex.md:89`), `_datasets/h01.md:9` ("1.4 PB") and
    `modules/module12.md:239` are **OK** if not called "raw".
  - `content-library/case-studies/h01-human-cortex.md:166` "At 1.4 petabytes, H01 is comparable in raw data volume to MICrONS"
    compares aligned (1.4) with raw (~2). **CHECK**: say "1.8 PB raw vs ~2 PB raw".
  - `content-library/infrastructure/reconstruction-pipeline.md:70` mixes H01 and MICrONS data sizes. **CHECK** it against this table.
  - 326 days (`h01-pipeline.md:117,231,238`; `03-em-prep-and-imaging.marp.md:100,108`; `module08-tools-and-methods.marp.md:427`):
    **CHECK**: attribute to the 2021 bioRxiv preprint.
  - "4 nm XY and 33 nm Z" (`h01-human-cortex.md:88`) is **OK**. The mean section thickness is 33.9 nm.

---

## 3. FlyWire / FAFB (whole adult *Drosophila* brain)

Primary: Dorkenwald S. et al. (2024) "Neuronal wiring diagram of an adult brain", *Nature* 634:124–138,
doi:10.1038/s41586-024-07558-y, PMC11446842. Companion: Schlegel P. et al. (2024) *Nature*,
doi:10.1038/s41586-024-07686-5, PMC11446831. FAFB: Zheng Z. et al. (2018) *Cell* 174:730–743,
doi:10.1016/j.cell.2018.06.019, PMC6063995.

### 3a. Neurons
- **Canonical:** "139,255 neurons".
- **Exact:** "Our reconstruction of an entire adult brain contains 139,255 neurons (Fig. 1a …)". "Of the 139,255 proofread
  neurons in FlyWire …, 118,501 are intrinsic to the brain".
- "~139,000", "~140,000" and "140K" are OK as roundings (outreach and table use).

### 3b. Synapses: the two numbers in the paper
- **Canonical:** "about 54.5 million synapses". "About 50 million" is OK only in outreach or kids' copy.
- **Exact:**
  - Abstract: "a neuronal wiring diagram of a whole brain containing 5 × 10⁷ chemical synapses between 139,255 neurons".
  - Results (intro): "contains 139,255 neurons … and 54.5 million synapses between these neurons."
  - These describe the same data. The abstract rounds to one significant figure.
  - A third figure, which is not a connectome count: "The whole brain contains 0.0175 mm3 of neuropil volume and around
    130 million synapses". That is the total after filtering the Buhmann et al. predictions (~244 million before filtering),
    including synapses not attached to proofread neurons.
  - Strong connections: "We observed 2,700,513 such connections [≥5 synapses] between 134,181 identified neurons."
- Secondary: flywire.ai "50M+ Synapses"; the Princeton release says "roughly 50 million synapses".
- **Don't say / check:** `modules/module12.md:240` "~50M": **CHECK**, use 54.5M in data tables.
  `content-library/connectomics/open-problems-undergrad.md:66` "roughly 50 million" is OK. `neuronauts/index.html:1442`
  "&gt;50 million" is OK.

### 3c. Proofreading effort
- **Canonical:** "an estimated 33 person-years of manual proofreading".
- **Exact:** "We estimate that FlyWire's brain reconstruction took around 33 person-years of manual proofreading." Methods:
  "an average time of 79 s per edit which adds up to an estimate of 33.1 person-years assuming a 2,000 h work year".
- All site uses are **OK**.

### 3d. Consortium size (secondary source only)
- **Canonical:** "researchers from at least 76 laboratories and 287 individuals, plus gamers and other volunteers (Princeton
  University, 2 Oct 2024)". Short form: "287 researchers in at least 76 labs, plus volunteers".
- **Source:** Princeton University press release, 2 Oct 2024 (EurekAlert! <https://www.eurekalert.org/news-releases/1059340>):
  "The FlyWire Consortium includes researchers from at least 76 laboratories and 287 individuals around the world as well as a
  network of gamers and other volunteers". This is **not** in the Nature paper text. Cite it as a press release.
- **Don't say / check:**
  - "287 proofreaders" or "287 contributors" (as proofreaders): the 287 are consortium researchers, not the full proofreader
    count, since volunteers are extra. Earlier grep hits were in `content-library/case-studies/flywire-whole-brain.md` at
    lines 41, 84, 145, 171, 176 and 283. The current snapshot finds none, but re-grep. **FIX** if found.
  - "more than 76 labs" (in modules 01/02/07, teaching sessions, initiatives) is **CHECK**: the source says "at least 76".

### 3e. FAFB image volume (Zheng et al. 2018)
- **Canonical:** "FAFB: 7,062 sections of ~40 nm, imaged by serial-section TEM (TEMCA2 and ATPS) at 4 nm/pixel,
  about 106 TB (~21 million camera images)".
- **Exact (Zheng 2018):** "To span the depth (∼250 μm) of the entire fly brain, 7,062 serial ∼40-nm thin sections were cut
  … In total, 7,050 (99.8%) sections were successfully imaged, resulting in a ∼106 TB dataset comprising ∼21 million camera
  images." Imaging: "At 4 nm/pixel". Sectioning: "at a thickness of 35-40 nm".
- **Voxel size:** Dorkenwald 2024: "FlyWire's reconstruction is based on a full adult fly brain (FAFB) dataset of 4 × 4 × 40
  nm³ images acquired by serial section transmission electron microscopy (ssTEM)".
- **Don't say:** "ATUM-SEM" for FAFB (sections were on slot grids and imaged by TEM). The current text in
  `content-library/journal-papers/imaging.md:87` is correct. **FIX** any reappearance.
- Other FAFB/FlyWire counts: "8,053 neurons" are VPNs. The larger-than-8,000 cell-type figure comes from Schlegel et al.;
  keep the site's "more than 8,400 cell types" attributed to Schlegel.

---

## 4. Hemibrain (Janelia FlyEM)

Primary: Scheffer L.K. et al. (2020) "A connectome and analysis of the adult *Drosophila* central brain", *eLife*
9:e57443, doi:10.7554/eLife.57443, PMC7546738.

- **Neurons. Canonical:** "about 25,000 neurons".
  - Exact (abstract): "it contains around 25,000 neurons, most of which were rigorously clustered and named".
  - **21,662 "traced" neurons:** this is in the Fig. 1 table, which is an image. **Not verified in this pass**, because the
    figure could not be retrieved. It is not in use on the site now. Do not introduce it without checking Fig. 1.
- **Synapses. Canonical:** "about 20 million chemical synapses".
  - Exact: "with about 20 million chemical synapses between them". Detail: "We identified in total 64 million PSDs and
    9.5 million T-bars in the hemibrain volume".
- **Data. Canonical:** "26 teravoxels (8-bit), 8 × 8 × 8 nm isotropic FIB-SEM".
  - Exact: "a dataset consisting of 26 teravoxels of data, each with 8 bits of grayscale information". Raw data is "larger
    than 20 TB".
- **Proofreading effort. Canonical:** "over 50 person-years of proofreading effort".
  - Exact (Results): "over 50 person-years of proofreading effort over ≈2 calendar years". Appendix 1: "Overall, we estimate
    that we undertook ≈ 50–100 proofreading years of reconstruction effort." Dorkenwald 2024 cites it as "hemibrain
    proofreading required 50 person-years for a part of the brain".
  - Recommendation: "over 50 person-years" (the paper's headline). Mention "50–100" only when discussing uncertainty.
- **License conflict (unresolved; keep flagging it):**
  - Janelia project page (<https://www.janelia.org/project-team/flyem/hemibrain>): "Hemibrain is licensed under CC-BY",
    linking to CC BY 4.0.
  - DataCite record for the v1.0 data deposit cited in the paper, doi:10.25378/janelia.11676099 ("Data for A Connectome of
    the Adult Drosophila Central Brain v1.0"): rights "Creative Commons Attribution Non Commercial 4.0 International"
    (`cc-by-nc-4.0`). Re-verified through api.datacite.org on 2026-09-26.
  - **Canonical:** "CC BY 4.0 per Janelia's hemibrain page; the v1.0 data deposit is registered as CC BY-NC 4.0. Check before
    redistributing." This is already the wording in `content-library/connectomics/ethics-and-governance.md:196` and
    `course/decks/marp/lectures/ethics-and-governance.marp.md:373`. **OK**
- **Also note:** Scheffer 2020 contains a mouse-brain projection: "a mouse brain of 500 mm3, at a typical FIB-SEM resolution of
  8 nm isotropic, would require almost 1000 petabytes." See §7.

---

## 5. *C. elegans*

- **White J.G. et al. (1986)** *Phil. Trans. R. Soc. B* 314:1–340, doi:10.1098/rstb.1986.0056 (abstract read through Europe PMC):
  "The hermaphrodite nervous system has a total complement of 302 neurons … there are 118 such classes … These consist of
  about 5000 chemical synapses, 2000 neuromuscular junctions and 600 gap junctions."
- **Cook S.J. et al. (2019)** *Nature* 571:63–71, doi:10.1038/s41586-019-1352-7, PMC6889226: "The graph of the hermaphrodite
  connectome has 460 nodes (302 neurons, 132 muscles, and 26 non-muscle end organs), whereas the male graph has 579 nodes
  (385 neurons, 155 muscles, and 39 non-muscle end organs)."
- **Witvliet D. et al. (2021)** *Nature* 596:257–261, doi:10.1038/s41586-021-03778-8, PMC8756380: "the full brain of eight isogenic
  C. elegans individuals across postnatal stages". "The total number of chemical synapses increased 6-fold (~1300 at birth to
  ~8000 in adults)". This counts the *brain* only (nerve ring plus ventral ganglion).
- **Canonical:** "302 neurons in the hermaphrodite (385 in the male, Cook et al. 2019); White et al. (1986) described about
  5,000 chemical synapses, 2,000 neuromuscular junctions and 600 gap junctions."
- **Don't say / check:**
  - "~7,000 chemical synapses" (`content-library/case-studies/c-elegans-revisited.md:42` caption; check line 135 too). **FIX**:
    White gives ~5,000 chemical synapses. The number 7,000 only works as 5,000 chemical + 2,000 NMJ.
  - `_datasets/c-elegans-white.md:15` "about 7,000 synaptic contacts". **CHECK**: say "about 5,000 chemical synapses and 2,000
    neuromuscular junctions", or at least "about 7,000 chemical synapses and neuromuscular junctions".

---

## 6. Larval *Drosophila* (Winding et al. 2023)

Primary: Winding M. et al. (2023) "The connectome of an insect brain", *Science* 379:eadd9330, doi:10.1126/science.add9330,
PMC7614541 (Europe PMC author manuscript).

- **Canonical:** "3,016 neurons and about 548,000 synapses".
- **Exact:** Abstract: "comprising 3016 neurons and 548,000 synapses". Results: "The resulting dataset contains 480 input neurons
  and 2536 differentiated brain neurons (3016 neurons total), and ~548,000 synaptic sites".
- **Weak edges:** "Most edges were weak (1 or 2 synapses) for all connection types (a-d: 60%, a-a: 75%, d-d: 79%, d-a: 91%; 66%
  across all types). However, strong edges (≥5 synapse) contained the majority (a-d: 61%; across all types: 55%; fig. S6B)".
  **Canonical:** "66% of edges have only 1–2 synapses, but edges of 5 or more synapses carry 55% of all synapses."
- **Imaging:** "4841 z-slices with an x,y,z resolution of 3.8 × 3.8 × 50 nm".
- Dorkenwald 2024 rounds this dataset to "(3,000 neurons, 5 × 10⁵ synapses)".
- **Don't say / check:**
  - "550,000 connections" (`content-library/journal-papers/network-analysis.md:220`). **FIX**: these are synapses, not
    connections, and the figure is 548,000.
  - `technical-training/atlas-connectomics-reference.md:43` "~3,000 neurons; ~550,000 synapses". **CHECK**: use 3,016 and 548,000.

---

## 7. Whole mouse brain: volume and projected storage

- **Volume. Canonical:** "about 500 mm³ (Badea et al. 2007: 508.9 ± 23.4 mm³, C57BL/6J)".
  - Badea A., Ali-Sharief A.A., Johnson G.A. (2007) *NeuroImage* 37:683–693, doi:10.1016/j.neuroimage.2007.05.046, PMC2176152
    (PMC full text): "The whole brain averaged 508.91±23.42 mm3." This was measured by in-skull MR microscopy of fixed, stained brains.
- **Projected storage. Canonical:** "roughly 800 PB of raw imagery at 4 × 4 × 40 nm, 8-bit, uncompressed. This is our
  arithmetic, a projection and not a measurement. Abbott et al. (2020) give 'roughly 1 million terabytes' (about 1 EB)."
  - Arithmetic: 500 mm³ ÷ (4 × 4 × 40 nm³) = 7.8 × 10¹⁷ voxels, which is 781 PB at 1 byte/voxel. At 508.9 mm³ it is 795 PB.
    "~800 PB" is correct as an estimate.
  - Abbott L.F. et al. (2020) "The Mind of a Mouse", *Cell* 182:1372–1376, doi:10.1016/j.cell.2020.08.010: "Roughly 1 million
    terabytes of data will need to be acquired and analyzed to provide a complete mouse brain connectome". It also mentions
    "uniform osmium staining of nearly a cubic centimeter of brain tissue".
  - Scheffer et al. 2020 (eLife): "a mouse brain of 500 mm3, at a typical FIB-SEM resolution of 8 nm isotropic, would require
    almost 1000 petabytes".
- **Don't say / check:** the `_data/open_problems.yml:150` and `open-problems-undergrad.md:96,378` "an exabyte" statements are
  **OK** if attributed to Abbott 2020. Do not present ~800 PB and ~1 EB as conflicting: the first is a raw-voxel projection,
  the second a rougher whole-project estimate. Decks module07/08/09 and `technical-training/01-why-map-the-brain.md:137`
  already label ~800 PB "(est.)". **OK**

---

## 8. BRAIN CONNECTS

- **Canonical:** "NIH's BRAIN Initiative Connectivity Across Scales (BRAIN CONNECTS) program announced its first awards on
  26 September 2023: 11 grants projected to total $150 million over 5 years, with collaborators at over 40 institutions."
- **Source:** NIH BRAIN Initiative blog, "NIH BRAIN Initiative awards new projects to develop innovative brain mapping
  technologies", September 26, 2023. The original URL
  (braininitiative.nih.gov/news-events/blog/nih-brain-initiative-awards-new-projects-develop-innovative-brain-mapping) now
  redirects to nih.gov/brain, so it was read from the Internet Archive capture. The NINDS and nih.gov copies returned 403.
  Verbatim:
  - "This initial round of BRAIN CONNECTS awards supports 11 grants projected to total $150 million over 5 years."
  - Scope sentence: "The goal of this project is to support the development of technologies that will generate wiring
    diagrams to comprehensively map neural connections in both humans and laboratory animals."
  - "The awards support diverse research teams with collaborators at over 40 universities and research institutions across
    the globe."
  - Themes: "Electron microscopy pipelines to map the mouse brain; Developing DNA sequencing tools to 'barcode' and map
    neurons; Novel imaging methods for human and non-human primate brains".
- **Don't say:** "launched in 2022". The funding opportunities (e.g., RFA-NS-22-048) were 2022, but the awards were September 2023.
  Current site uses ("first awards 2023", "launched in 2023 with eleven funded projects", neuronauts "11 awards, roughly
  $150 million over five years, 40+ institutions") are **OK**.

---

## 9. caveclient

- **Canonical:** "caveclient 8.2.1 (latest on PyPI as of 26 September 2026; released 10 July 2026; requires Python ≥ 3.9)".
- **Source:** <https://pypi.org/pypi/caveclient/json>, `info.version` = 8.2.1, upload time 2026-07-10T21:20:54, `requires_python` ">=3.9".
- **Site pins:** `content-library/infrastructure/provenance-and-versioning.md:169` (`caveclient==5.14.0`) and
  `course/decks/marp/en585781/module08-tools-and-methods.marp.md:1182` (`"caveclient 5.21.0"`). These are illustrative pins in
  reproducibility examples. **CHECK**: fine as examples of pinning, but do not present them as current. If a "current
  version" is stated, use 8.2.1 with its date.

---

## 10. MICrONS materialization versions (minnie65_public)

Source: MICrONS tutorial site, "Materialization and Versioning" page and the per-version Release Manifests
(<https://tutorial.microns-explorer.org/materialization-version.html>,
`…/release_manifests/version-NNNN.html`), read 2026-09-26.

**Policy (verbatim):** "Long-term releases are made available for analysis, but are not permanent." Older pages say "We have
begun archiving release versions that are more 2 years old". Newer pages say "more 1 years old". "All publicly released
annotation data is available as a static download."

| Version | Release date (manifest) | Status on the tutorial site, 2026-09-26 |
|---|---|---|
| 117 | 11 Jun 2021 (first public release) | Available |
| 343 | 24 Feb 2022 | Archived / Expired |
| 661 | 6 Apr 2023 (the nav label says "Jun 2023") | Archived / Expired |
| 795 | 23 Aug 2023 | Archived / Expired |
| **943** | 22 Jan 2024 | **Available: "Major version … persisting beyond this limit for the foreseable future because it is a major analysis version."** |
| 1078 | 5 Jun 2024 | Archived / Expired |
| 1181 | 16 Sep 2024 | Archived / Expired |
| **1300** | 13 Jan 2025 | **Available: "Major version … will persist beyond this limit for the foreseable future"** |
| 1412 | 29 Apr 2025 | Archived / Expired |
| **1507** | 31 Jul 2025, 08:10:01.117494 UTC | **Conflicting. See below.** |
| 1621 | 25 Nov 2025 | Available |
| 1718 | 7 Mar 2026 | Available. The status table's timestamp typo reads "2025, 3, 07". |
| 1822 | 27 Jun 2026 (latest; "second quarterly release of 2026") | Not yet in the status table |

- **Long-term supported:** 943 and 1300 are the two flagged "major analysis versions". 117 also remains available as the
  first release. 343 and 661 are **expired**, contrary to the premise that 343/661 are LTS. The Cubic Millimeter page on
  microns-explorer.org is stale. It lists "8 publicly available versions … 117, 343, 661, 785 [sic], 943, 1078, 1181, and 1300"
  and says flattened static segmentations exist for 117, 343, 943 and 1300.
- **v1507 conflict:**
  - The v1507 manifest page says "Upcoming archival … **v1507 will expire July 31, 2026**."
  - The "Materialization and Versioning" page has a banner "Upcoming Archival: v1507", but its status table still lists
    1507 as "Available". That table is stale, because it lacks 1822.
  - The live CAVE version list requires authentication and was not checked. As of today, 26 Sep 2026, v1507 is **past its
    announced expiry date**.
  - The **static exports** the site's lab uses are still served. A HEAD request to
    `https://storage.googleapis.com/mat_dbs/public/minnie65_phase3_v1/v1507/proofreading_status_and_strategy_merged_header.csv`
    returned HTTP 200 on 2026-09-26. The lab's own index also records that all files returned 200 on 26 Sep 2026.
  - **Canonical:** "v1507 (31 July 2025), read from the public static CSV exports. The MICrONS team scheduled v1507 to leave the
    live CAVE service on 31 July 2026, so `CAVEclient(..., version=1507)` may no longer work. Use the static exports, a
    `timestamp=` query, or a major version (943 or 1300)."
- **Don't say / check:**
  - `notebooks/microns-lab/index.md:108` "Connect with `CAVEclient("minnie65_public", version=1507)`". **FIX**: v1507 has passed
    its announced CAVE expiry. Point to 1300 or 943, or to `timestamp=datetime(2025,7,31,8,10,1,117494,tzinfo=utc)`.
  - `modules/module17.md:107` example "CAVE materialization v795": v795 is expired. **CHECK**: use 943 or 1300 in examples.
  - `version 943` examples (`provenance-and-versioning.md:111,184–186`, `module08…marp.md:1140,1328`, `module15.md:184`,
    `technical-training/04-volume-reconstruction-infrastructure.md:213`) are **OK**. 943 is a major version.
    `provenance-and-versioning.md:111` says "as long as version 943 stays" available, which is correct phrasing.
  - `course/decks/marp/neurotrailblazers-template.marp.md:203` `materialization_version=1300` is **OK**.

---

## 11. Other widely repeated numbers noticed

- **MICrONS imaging time:** "approximately 6 months" with 5 autoTEMs (paper). **OK** where used.
- **FlyWire public release version:** v783, an October 2023 snapshot, CC BY-NC 4.0 (flywire.ai/guidelines, as verified in
  `docs/reviews/claim-audit/ethics-and-governance.md`). Not re-checked in this pass.
- **Hemibrain vs FlyWire "uncropped" neurons:** Dorkenwald 2024 describes the hemibrain as "around 20,000 neurons that are
  'uncropped' … and 14 million synapses between them". This differs from Scheffer's "around 25,000 neurons … about 20 million
  chemical synapses" because it counts a different subset. Do not mix the two.
- **EyeWire players:** the site has "about 120,000 players/people" (`content-library/proofreading/proofreading-strategies.md:311`,
  `neuronauts/index.html:1512`) and "200,000+ players" (`initiatives/outreach.md:41`). Not verified in this pass. **CHECK**
  these against each other before the next edit. They may be different dates.

---

## Recommended site-wide wording

1. **MICrONS:** "about 1 mm³ of mouse visual cortex containing more than 200,000 cells and about 524 million synapses, with
   calcium imaging of about 75,000 neurons (MICrONS Consortium 2025); about 2 PB of raw EM imagery at ~4 × 4 × 40 nm, from
   27,972 sections." Give neuron counts only with scope: "84,035 individually segmented neurons (larger subvolume)". Never say
   "65,000-neuron".
2. **H01:** "about 1 mm³ of temporal cortex from a 45-year-old woman with drug-resistant epilepsy: 57,180 cells (16,087
   neurons), about 150 million synapses (149,871,669 detected), 5,019 sections at 33.9 nm mean thickness, 4 × 4 nm pixels;
   1.4 PB aligned (1.8 PB raw)." Attribute "326 days" to the 2021 bioRxiv preprint.
3. **FlyWire:** "139,255 neurons and about 54.5 million synapses, proofread with an estimated 33 person-years (Dorkenwald et
   al. 2024), from the ~106 TB FAFB volume at 4 × 4 × 40 nm (Zheng et al. 2018)." Consortium: "287 researchers in at least
   76 labs, plus volunteers (Princeton, 2024)". Do not say "287 proofreaders".
4. **Hemibrain:** "about 25,000 neurons and about 20 million synapses, 8 nm isotropic FIB-SEM, over 50 person-years of
   proofreading (Scheffer et al. 2020)". Licence: "CC BY 4.0 per Janelia's page; the v1.0 deposit is registered CC BY-NC 4.0.
   Check before redistributing."
5. ***C. elegans*:** "302 neurons (hermaphrodite; 385 in the male); about 5,000 chemical synapses, 2,000 neuromuscular
   junctions and 600 gap junctions (White et al. 1986)". Never say "7,000 chemical synapses".
6. **Larval fly:** "3,016 neurons and about 548,000 synapses; 66% of edges have 1–2 synapses (Winding et al. 2023)." Never say
   "550,000 connections".
7. **Whole mouse brain:** "about 500 mm³; roughly 800 PB raw at 4 × 4 × 40 nm, 8-bit (our estimate); Abbott et al. (2020):
   'roughly 1 million terabytes'."
8. **BRAIN CONNECTS:** "first awards 26 September 2023: 11 grants, about $150 million over 5 years, 40+ institutions."
9. **caveclient:** "8.2.1 (PyPI, 10 July 2026)", and only if a current version must be stated.
10. **MICrONS versions:** the long-lived analysis versions are **943** and **1300** (plus 117). Label **v1507** as "static
    export, 31 July 2025; scheduled to leave live CAVE on 31 July 2026". Don't use 343, 661 or 795 as live examples.

## Unresolved conflicts to track

- MICrONS dimensions: paper 1.3 × 0.87 × 0.82 mm (in vivo) vs Explorer 1.4 × 0.87 × 0.84 mm.
- MICrONS neurons: paper 84,035 (segmented, subvolume 65) / 82,247 (model-predicted) vs Explorer "an estimated 120,000".
- MICrONS synapses: paper 524 M vs Explorer 523 M (the paper's subvolume sum is 523). The raw-size unit is printed "Pb".
- H01: 1.4 PB aligned vs 1.8 PB raw (Science) vs ~2.1 PB (2021 preprint). Sections: 5,019 (Science) vs 5,292 (preprint) vs
  "5,293 layers" (site claim, unverified). Synapses: 149.9 M (paper) vs 183 M (release page). 326 days is in the preprint only.
- Hemibrain licence: CC BY 4.0 (Janelia page) vs CC BY-NC 4.0 (v1.0 DataCite record). 21,662 traced neurons is unverified (Fig. 1 image).
- v1507: expiry date 31 Jul 2026 on its manifest vs "Available" in the stale status table. Live CAVE status is unverified (auth required).
