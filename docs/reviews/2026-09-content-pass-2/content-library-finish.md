# Content pass 2: finishing four content-library pages

Resumed 27 September 2026 after the original agents were cut off. Branch
`compass-workshops`; nothing committed. Only the four pages below and this report were
edited. Hub and index pages belong to the nav agent; see "Links needed" at the end.

Verification method: every paper cited on the four pages was read through Europe PMC
full-text XML, NCBI BioC (for author manuscripts Europe PMC does not serve) or, for
Micheva & Smith 2007, the PMC HTML page; journal, volume, issue and pages were checked
against Europe PMC metadata for all 18 DOIs (all correct). Web sources (MICrONS tutorial
pages, release manifests, caveclient guides) were fetched on 27 September 2026. Lab
numbers were read from `assets/notebooks/microns-lab/` (`results_summary.json`,
`methods_record.json`, the executed notebook, `rerun-log.txt`).

---

## 1. `content-library/imaging/beyond-em.md` (new page)

**Status: complete.** 248 lines on arrival; read end to end; every number, date,
resolution, author and year checked against the paper it cites. Eight fixes, all small.

### Fixes made

| Where | Was | Now | Why |
|---|---|---|---|
| Front matter | `slug`, `track`, `pathways` keys | removed | No other content-library page carries them; the validator requires track metadata only under `avatars/ datasets/ tools/ tracks/ concepts/ technical-training/`, and no include reads them for content-library pages |
| "EM is the default" | 7 nm membrane, 40 nm vesicle, <100 nm axons stated bare | attributed to the EM principles page | Not in any paper read this pass; they are the figures `em-principles.md:43` uses, so the page now says so |
| Gao 2019 bullet | "higher expansion demands denser labeling and longer imaging" | "they argue that immunostaining is probably not dense enough to deliver resolution much beyond what 4× already gives" | Matches the paper's Discussion wording |
| Kuan 2020, "What it does not" | "axons of chordotonal and bristle neurons were too small to reconstruct at 150 to 200 nm" | motor, hair-plate and some campaniform axons traceable; chordotonal and bristle narrower; bristle "in particular" too small | The paper says bristle axons "in particular" were too small; chordotonal axons are described as "narrower", not as untraceable |
| Micheva & Smith | "axial resolution is now the section thickness (70 nm in their reconstructions)" | "(70 to 200 nm in their examples)" | Their volume reconstructions used 200 nm sections; 70 nm sections appear in the synapsin/PSD-95 serial example and the SEM correlation |
| Check yourself 3 | "main-branch morphology resolved at 87 to 222 nm" | "at 100 nm voxels (the measured resolution across the paper's scans ran from 87 to 222 nm)" | The PPC scans were the 100 nm-voxel scans; 87–222 nm is the range over all scans |
| "What this page does not cover", CLEM bullet | "The journal club has the papers" | points to the Lichtman & Denk entry on the imaging papers page; "the rest is not covered on this site" | `technical-training/journal-club/` has no CLEM, APEX2 or cryo-ET paper; APEX2 and cryo-ET appear nowhere else on the site |

Not changed: no `image`/`image_alt` (siblings have an SVG hero; "no new figures" rule, and
`_layouts/page.html` handles a missing image). Voice per BRAND_GUIDE §2: numbers over
adjectives, boundaries stated, no hype words; American spelling (grep clean). Links: all 13
`relative_url` targets resolve (`/datasets/catalog/fanc/` through the `_datasets`
collection permalink; the Module 7 deck HTML exists under `course/decks/marp/out/`).
Site-internal claims checked: Module 7 deck has the "Different tools for different jobs"
slide (`module07…marp.md:756`) and the LICONN open-problem line (:1261); Module 8 deck
calls LICONN "the first demonstrated LM route" and attributes "first" to the authors
(`module08…marp.md:480,503`); `initiatives.md:53–54` credits Argonne µCT and ESRF XNH
separately; Unit 02 has the AL/PM worked case (:110), the tractography check-yourself
(:130) and the tracer-atlas row (:88); `_datasets/fanc.md:22` mentions XNH.

### Source table (claim → where verified)

C15 = Chen, Tillberg & Boyden 2015, doi:10.1126/science.1260088 (PMC4312537, BioC).
Ch17 = Chang et al. 2017, doi:10.1038/nmeth.4261 (PMC5560071). G19 = Gao et al. 2019,
doi:10.1126/science.aau8302 (PMC6481610, BioC). T25 = Tavakoli et al. 2025,
doi:10.1038/s41586-025-08985-1 (PMC12158774). D17 = Dyer et al. 2017,
doi:10.1523/ENEURO.0195-17.2017 (PMC5659258). B22 = Bosch et al. 2022,
doi:10.1038/s41467-022-30199-6 (PMC9132960). K20 = Kuan et al. 2020,
doi:10.1038/s41593-020-0704-9 (PMC8354006, BioC). MS07 = Micheva & Smith 2007,
doi:10.1016/j.neuron.2007.06.014 (PMC2080672, PMC HTML). Ke16 = Kebschull et al. 2016,
doi:10.1016/j.neuron.2016.07.036 (PMC6640135, BioC). Ch19 = Chen et al. 2019,
doi:10.1016/j.cell.2019.09.023 (PMC7836778, BioC). MH17 = Maier-Hein et al. 2017,
doi:10.1038/s41467-017-01285-x (PMC5677006). M25 = MICrONS Consortium 2025,
doi:10.1038/s41586-025-08790-w. SC24 = Shapson-Coe et al. 2024, doi:10.1126/science.adk4858.
S20 = Scheffer et al. 2020, doi:10.7554/eLife.57443. (DOIs match the page's References
list; journal/volume/pages checked against Europe PMC metadata.)

| Claim on the page | Source, location |
|---|---|
| LM diffraction limit ~250 nm lateral; confocal axial rarely better than 700 nm (citing Pawley 1995) | MS07 Introduction |
| 4 nm pixels, 33–40 nm sections (MICrONS, H01); 8 nm isotropic FIB-SEM (hemibrain); ~2 PB per mm³; ~6 months / 326 days | canonical-facts.md §1e, §2, §4, §11 |
| ExM: swellable polyelectrolyte gel, anchored labels, protease digestion, 4.5-fold linear; ~70 nm lateral / ~200 nm axial effective; microtubule FWHM 82.4 ± 6.01 nm → ~60 nm effective; 500 × 180 × 100 µm (~10⁷ µm³) of hippocampus, three labels, spinning-disk confocal; Bassoon–Homer1 169 ± 32.6 nm, n = 277 synapses; overlapping pre-expansion; RMS length error <1% of distance above the PSF size; Thy1-YFP cytosolic label | C15 Abstract, Results (gel, distortion, microtubules, synapses, volume) |
| iExM: second gel in the space opened by the first; ~4.5 × 4.5 ≈ 20×; ~25 nm resolution; hollow microtubules (~25 nm outer diameter) resolved by confocal | Ch17 Abstract, Results |
| ExLLSM: 4× expansion + lattice light-sheet; ~60 × 60 × 90 nm; whole fly brain in 62.5 h; up to 25,000 tiles, multi-terabyte; 8× iterated protocol showed regions of clear distortion (irregular somata and nuclei); chose 4×; immunostaining density limits resolution beyond 4×; synapses per fly brain region; spine morphology across cortical depth (1900 × 280 × 70 µm pia to WM) | G19 Abstract, Results (expansion factor, stitching, spines, fly brain), Discussion |
| LICONN: triple-hydrogel, ~16× (15.44 ± 1.68 s.d.), NHS-ester pan-protein stain, spinning-disc confocal, FFN segmentation; 280 nm / 730 nm → ~20 nm / ~50 nm; ~10 × 10 × 25 nm voxels (actual 9.7 × 9.7 × 25.9); ~1 × 10⁶ µm³, 396 × 109 × 22 µm, layers II/III–IV S1; 132 tiles, 6 × 22 grid, 0.47 teravoxels, 6.5 h; 85 × 69 × 14 µm box, 68.6 gigavoxels, hippocampal CA1; 99 skeletons (69 axons, 1.8 mm; 30 dendrites, 1,041 spines); 0 mergers, 413 splits, 80.1%; agglomeration 92.8%, 31 splits; 83/1,041 spines (8.0%); 285/306 (93.1%) and 281/301 (93.4%) spine tracing; bassoon, PSD95, SHANK2, gephyrin; 1,059 test synapses, F1 0.90 full / 0.94 pre / 0.95 post (913 µm³ CA1 test volume); 11 dendrites, 123 µm, 322 spines, 2.8 ± 1.2 per µm, 2.6 ± 1.1 SHANK2+; 0.6 mm working distance; 12 rounds, 3 × 3 × 12 grid, 205 µm; "has been out of reach"; spine density 1.0 ± 0.3 per µm³ | T25 Abstract, Results (hydrogel, resolution, cortex volume, FFN, traceability, synapse prediction, axial extension), Methods (objective) |
| µCT: 2-BM beamline, APS; ~1 µm³ isotropic; millimeter-scale; without sectioning; aldehyde-fixed, heavy-metal-stained, plastic-embedded; cell bodies, vessels, large apical dendrites, myelinated axons segmented and counted | D17 Abstract, Introduction, Methods |
| Bosch: propagation-based phase contrast, 325 nm voxels, ~2–3 µm FSC resolution; olfactory bulb and hippocampus; targeted SBEM at 50 nm isotropic (olfactory bulb) | B22 Abstract, Results |
| XNH: ID16A, ESRF; mouse cortex, fly brain, VNC, leg; 30–120 nm voxels; FSC 87–222 nm; "sub-100 nm" in abstract; 120 K; warped scans excluded; 30 nm voxels show mitochondria, ER, dendrites, myelinated axons, identification leaning on prior 3D-shape knowledge; two overlapping PPC scans, layers I–V, ~8 h, 3,234 cells classified as pyramidal/interneuron/glia; 100 nm voxels for those scans; EM of the same tissue ~150 h; ultrastructure incl. chemical synapses preserved; small cracks and bubbles possibly from XNH; superficial pyramidal cells receive stronger apical inhibition; intact fly leg, motor axons traced muscle → CNS; 150–200 nm leg resolution; bristle axons too small, chordotonal narrower | K20 Abstract, Results (imaging, resolution, PPC, leg), Methods (cryo stage, EM) |
| Array tomography: ribbons of 50–200 nm sections, LR White, glass slides; 70 nm and 200 nm sections in examples; eluted and restained, "no apparent limit"; nine cycles of double immunostaining; 10 synapses through 6 rounds of synapsin; SEM after heavy-metal staining on the same 70 nm section; synapsin/PSD-95 followed through serial 70 nm sections | MS07 Summary, Results (Fig. 5, 6, 7 text) |
| MAPseq: Sindbis library; 30-nt barcode ≈ 10¹⁸ diversity vs ~10⁸ neurons; MAPP-nλ carrier (from a presynaptic protein); 995 barcodes, four animals, 249 ± 103; olfactory bulb and 22 coronal 300 µm slices; idiosyncratic patterns, some almost exclusively one target; < 1 week; does not distinguish fibers of passage, minimized by avoiding fiber bundles; "roughly corresponding to an equal number of LC neurons"; resolution set by dissection | Ke16 Abstract, Results, Discussion |
| BARseq: in situ sequencing of barcodes; 3,579 neurons, auditory cortex, 11 areas; laminar organization of IT, PT-like, CT; projection type "restricted almost exclusively to transcriptionally-defined subtypes of IT neurons"; fibers of passage small because carrier protein enriched at synapses | Ch19 Abstract, Results, Discussion |
| Hemibrain ~25,000 neurons (comparison-table FIB-SEM row) | S20 abstract via canonical-facts.md §4 |
| iExM table row: "cells and tissues", synaptic proteins, dendritic-spine architecture in mouse brain | Ch17 Abstract (re-read 28 Sep 2026 via Europe PMC) |
| Tractography: simulated brain, 25 ground-truth bundles; 96 submissions, 20 groups; 90% of bundles recovered "to at least some extent"; more invalid than valid bundles; half of invalid bundles recur across groups | MH17 Abstract, Results |

Re-checked 28 September 2026 (third pass): every number on the page maps to a row above;
two rows added (hemibrain count, iExM table row) and the legend now gives each DOI. MH17
abstract re-read: "most state-of-the-art algorithms produce tractograms containing 90% of
the ground truth bundles (to at least some extent)" matches the page. No page edits needed.

Unverifiable or not established, left as stated: none remaining. The membrane/vesicle/axon
figures are now attributed to the site's EM principles page rather than to a paper.

---

## 2. `content-library/case-studies/microns-visual-cortex.md`

**Status: complete; no page edits this pass.** Rewritten 27 September 2026; the full
source table is in [`microns-case-study.md`](microns-case-study.md). Re-checked 28
September 2026 end to end (749 lines): no half-finished sections; co-registration
(fiducials, staged transform, manual and automatic matching), functional-unit vs neuron
counting, and "What the calcium data license" are all present, with Check yourself (3),
Discussion questions, Related and Key References.

Spot re-verification against MICrONS 2025 full text (PMC11981939, Europe PMC XML) and
Ding et al. 2025 (PMC11981947):

| Claim | Source, location | Result |
|---|---|---|
| 2,934 expert-matched fiducials | M "Functional–structural co-registration" | matches |
| Average residual 3.8 µm | M same section ("The average residual was 3.8 μm") | matches |
| Final TPS 0.003 µm | M Methods "Transform" | matches |
| Segmentation at 8 × 8 × 40 nm; aligned volume at 8 nm | M "The EM volume"; Methods (affinity and cleft networks "applied … at 8 × 8 × 40 nm3") | matches |
| Ding: cleft size "a proxy for synaptic strength" (Check yourself ii) | D "Similarity across spatial scales" | matches |
| Long-lived versions 943 and 1300; static exports | canonical-facts.md §10 | matches; page does not mention v1507 |

Links: all 13 `relative_url` targets resolve against `permalink:` lines or the
`_datasets` collection permalink, including `/notebooks/microns-lab/` (three places).

---

## 3. `content-library/infrastructure/provenance-and-versioning.md`

**Status: complete.** All brief items present: materialization versions (CAVE 2025),
root vs supervoxel IDs, long-lived vs expired MICrONS versions with the v1507 gray zone,
timestamp queries, the reproducibility header (links Technical Practice norms 1–5 and
Unit 04 rather than restating them), the worked example from the lab's real outputs, the
seven-group methods record, and a drift failure-mode table. Five fixes this pass.

### Fixes made

| Where | Was | Now | Why |
|---|---|---|---|
| "The question provenance answers" | fictional release label `T32` | `"Birch"` | T32 is on the reserved-label list |
| MICrONS policy quote | quote ran through "v117, v943, v1300" | quote closes at "foreseable future", list given outside it | the page lists the versions as separate items, not a comma list |
| Frozen/not-frozen table; drift table "Living label tables" | "(MICrONS v1621 release manifest)" | "(MICrONS v1718 …)" | "New cells will be added as more changes arise from continued manual efforts …" is in the v1718 manifest (under the corrected `aibs_metamodel_celltypes_v661` / `mtypes_v661_v2` tables); not found in the cached v1621 manifest |
| Pipeline provenance | norm 4 only | adds a link to Unit 04 §4 for the per-stage output fields | brief asks to link Unit 04's reproducibility section, not duplicate it. Note: the brief said "§5"; in the current unit §4 is "Reproducibility requirements" and §5 is "Capacity and cost"; §2 holds the materialization rule the page already cites |
| Methods-record sentence templates | "Session 3 of the lecture series" | "Session 3 of the four-session teaching block" | `teaching/sequence.md` numbers it Session 3 of the block (Lecture 2 in EN.585.781) |

### Source table (claim → where verified)

CAVE = Dorkenwald et al. 2025, *Nat Methods* 22:1112–1120, doi:10.1038/s41592-024-02426-z
(PMC12074985, Europe PMC full text). MV = MICrONS tutorial "Materialization and
Versioning" page; Mnnnn = release manifest for version nnnn (fetched 26–27 Sep 2026).
CG / CM = caveclient ChunkedGraph / Materialization guides (fetched 27 Sep 2026). Lab =
`assets/notebooks/microns-lab/` files.

| Claim on the page | Source, location |
|---|---|
| 1,046,656 edits to 16 Sep 2024 | MICrONS 2025 "Proofreading"; canonical-facts §1 |
| Annotations anchored on points; points bound to supervoxels; "materialization" definition; "1 per h"; daily snapshots; "prohibits a user's ability…" | CAVE Results (annotation and materialization sections) |
| ChunkedGraph hierarchy; 112 billion supervoxels in MICrONS65; lineage graph of altered roots | CAVE Results (ChunkedGraph section, Fig. 2e text) |
| Five published datasets; ~2 billion annotations; >4 million edits by >500 users | CAVE opening section ("Proofreading and analysis of connectomics datasets") |
| Arbitrary-time-point queries; overhead over snapshots | CAVE Abstract; Results (analysis queries) |
| "A root id is associated with a particular agglomeration…"; "A new root id is generated…" | CG "Getting supervoxels for a root id" |
| "18-digit … will change every time it is proofread"; "always associated with the same collection of supervoxels"; static label indexing; multi-soma split question; `suggest_latest_roots` "best guess" | MV |
| "approximately 1 year after their release"; "WILL NOT expire … foreseable future" v117 v943 v1300 | MV status section |
| Version timestamps and statuses table; v1822 latest | Mnnnn manifests; MV status table; canonical-facts §10 |
| "v1507 will expire July 31, 2026"; "All publicly released annotation data is available as a static download" | M1507 |
| v1507 static exports returned HTTP 200 on 26 Sep 2026 | canonical-facts §10; lab index |
| `get_versions()`: "Each version has a timestamp…"; "varying expiration times…" | CM |
| `timestamp=` → "will call live_query automatically"; UTC; `ValueError` | CM |
| Living correction tables ("New cells will be added as more changes arise…") | M1718 |
| caveclient 8.2.1 latest on PyPI | pypi.org JSON API (8.2.1 uploaded 10 Jul 2026; still latest 28 Sep 2026) |
| Five-line header | Unit 04 Lab Part A step 6 |
| Norms 1–5 wording (header + caption; churn 1:1/split/merge; six decisions; structured provenance; next-richer representation); norms 7, 12, 13, 21 | `hidden-curriculum/technical-practice.md` §§1–5, 7, 12, 13, 21 |
| Unit 04 fictional 1,412 → 1,530 worked example | `technical-training/04-…md:222–256` |
| Pins: datastack, v1507, timestamp 2025-07-31T08:10:01.117494+00:00, access string; four data files with bytes and SHA-256 prefixes; seed 20250731; 200 samples; T = 1/2; 4 × 4 × 40 nm; numpy 2.3.5, pandas 2.3.3, Python 3.13.5; macOS 15.7.9 arm64; code hash `a50d89761feb6371…` | Lab `methods_record.json` |
| 2,182 → 2,141 → 2,088 → 2,070 → 2,070 → 2,070 (41/53/18/0/0); 1,732 exc / 338 inh; 258,812 synapses; 31,542 autapses; 134,753 edges; 17,022 reciprocal pairs; 8,652 expected (1.97×) | Lab `results_summary.json` (`inclusion`, `reciprocity` distance × class, T = 1) |
| Drift: 1,953 / 2,070 / 1,942 matched / 11 dropped / 128 new / 118 root changed / 129 absent; 93 days; 6.6% | Lab `results_summary.json` `version_drift`; arithmetic (129 / 1,953 = 6.6%; 29 Apr → 31 Jul 2025 = 93 days) |
| 2,089,627 synapse rows from 2,141 presynaptic cells; 144,120 nucleus rows | Lab executed notebook output |
| Four byte-identical runs under 3.11.14 and 3.13.5; SHA-256 `d9a218e1d5153dc8…` | Lab `rerun-log.txt` |
| Newer-package development run gave the same reciprocity numbers | `notebooks/microns-lab/index.md:305–306` |
| Non-claim paragraph | `notebooks/microns-lab/index.md:254` |
| Module 21 rubric row; worksheet "Repair the methods record" | `modules/module21.md:212`; `teaching/lectures/tools-and-methods-activity.md:53` |

Not established, stated as such on the page: whether `CAVEclient(…, version=1507)` still
works (live list needs a token). The Dockerfile pins are labeled as a pattern, not a
recommendation. Links: all 14 `relative_url` targets resolve.

---

## 4. `content-library/cell-types/neuron-type-identification.md`

**Status: complete.** All brief items present: type assignment in EM by four kinds of
evidence (morphology, compartment targeting, nucleus/soma, connectivity) with Elabbady
2025, Schneider-Mizell 2025 and Schlegel 2024; FlyWire's 8,453 types; classifier vs
manual label tables with the lab's per-source counts; Petilla (Ascoli et al. 2008); the
"label source in the same sentence as the count" rule with a worked sentence. No new
figures. Seven fixes this pass.

### Fixes made

| Where | Was | Now | Why |
|---|---|---|---|
| E/I split headings | "about 80% of neurons … DeFelipe & Fariñas 1992; Markram et al. 2004" / "about 20%" | "the large majority … take it from the volume you are analyzing" / "the minority" (Markram 2004 kept as a diversity review) | Percentage not in the Markram 2004 abstract; DeFelipe & Fariñas 1992 not retrievable from Europe PMC in two tries; full texts not open. Omitted per timebox rule |
| Pyramidal soma cue | "Roughly 10–25 µm across" | size varies; measure it in your volume | No source read gives the range (the MICrONS case-study pass removed a similar soma-size figure for the same reason) |
| "Four kinds of evidence" intro | "The two MICrONS papers … were analyzed at materialization version 795 (Schneider-Mizell, Data availability)" | 795 attributed to Schneider-Mizell only; Elabbady's released predictions tied to the `_v661` table | Elabbady's Data availability names no version |
| Worked example | synthetic release `T67` | `"Aspen"` | T67 is on the reserved-label list |
| Label tables paragraph | living-table quote cited to "v1621 release manifest"; "folded into a combined view" | cited to v1718 manifest; quotes "Both corrections tables are hierarchically incorporated in the super view of cell type: `aibs_cell_info`"; notes the export's `broad_type_source` column | Both quotes are in the cached v1718 manifest, not v1621 |
| Lab counts sentence and the "Enough" template | "1,341 manual and 729 classifier predictions" | 1,345 manual (1,341 column reference + 4 corrections), 725 classifier | The table labels the 4 `…_corrections` rows as manual; 729 counted them as classifier output. 598 + 127 = 725 |
| References | "v1621 release manifest" | "v1718 release manifest" | as above |

### Source table (claim → where verified)

E = Elabbady et al. 2025, *Nature* 640(8058):478–486, doi:10.1038/s41586-024-07765-7
(PMC11981918). SM = Schneider-Mizell et al. 2025, *Nature* 640(8058):448–458,
doi:10.1038/s41586-024-07780-8 (PMC11981935). S = Schlegel et al. 2024, *Nature*
634(8032):139–152, doi:10.1038/s41586-024-07686-5 (PMC11446831). P = Ascoli et al. 2008,
*Nat Rev Neurosci* 9(7):557–568, doi:10.1038/nrn2402 (PMC2868386). All four DOIs, volumes,
issues and pages re-checked against Europe PMC metadata on 28 September 2026; quotes
checked against Europe PMC full-text XML. AT = MICrONS "Annotation Tables" page; M1718 =
v1718 release manifest (cached 27 Sep 2026).

| Claim on the page | Source, location |
|---|---|
| Cell-type definition "quantitatively more similar to cells in a different brain…"; "about one-third of cell types proposed for the hemibrain could not be reliably reidentified" | S Abstract / Results |
| NBLAST vs ~84,000 FlyWire neurons; hemibrain 5,235 morphology types → 5,620; NBLAST assumption fails for columnar optic-lobe neurons | S Results (hemibrain matching) |
| "typically used iteratively … idiosyncratic features"; cross-brain cosine similarity effect size 0.045 ± 0.096 | S Results (cross-dataset connectivity) |
| flow > superclass > class > cell type; nine superclasses; 120 lineages, 183 hemilineages, 88% (30,233); "homologous neurons share synaptic partners"; 8,453 types, 3,643 previously proposed, 4,581 new; 96.4% (98% / 92%); "as a prediction"; 1,651 (32%) not reidentified; 3,584 → 3,643 consensus types | S Abstract, Results (annotation hierarchy, hemilineages, cell typing) |
| 29 features; consensus clustering; 18 M-types; "dominant expert label"; L6short/L6tall; 142 of 143 CT cells | SM Results "Dense neuron population…", Fig. 3 text |
| Compartment-targeting quote; four subclass definitions; "would include" PV and CCK basket; DistTC SST Martinotti and non-Martinotti; SparTC neurogliaform and L1 (Id2); InhTC ≈ VIP; linear classifier on expert labels; "extensive (but incomplete)"; >46,000 edits; no chandelier cells in column | SM Results "Inhibitory subclasses", "Dense neuron population…" |
| 1,352-neuron continuous population; all 1,886 cells classified; 163 interneurons; 70,884 inhibitory→excitatory synapses; "expert labels of layer and long-range projection type"; version 795 | SM Main, Results, Data availability |
| "about a third … truncated"; "insensitive to changes in proofreading"; "typically precise and complete"; feature list; 60 µm postsynaptic shapes | E Introduction, Results, Methods |
| Column 1,619 = 1,115 exc + 143 inh + 361 non-neurons; five-classifier cascade; 91% CV / 82% test; 1,700-cell test set (100 per subclass); 95.6%, 97.5%, 90%, 90% → 94%; 88% (94,010/106,761); "sufficient to identify cell types…"; 16 of 20 chandelier neighbors vs none of 20 random and none of 143 column interneurons; "connectivity profile correlates…" | E Results (training data, hierarchical model, evaluation, chandelier search) |
| Petilla quotes ("typically described and classified…"; "standardized nomenclature…"; "does not attempt to give names…"; "for ease of reference"; "'Clustered' terminal branches…"; "large basket cell boutons…") | P Introduction; Axonal features section |
| Neurogliaform volume transmission | Oláh et al. 2009 abstract, doi:10.1038/nature08503 (PMC2771344) |
| >1,300 Patch-seq neurons; families distinct, types within family continuous | Scala et al. 2021 abstract, doi:10.1038/s41586-020-2907-3 (PMC8113357) |
| Label tables: `allen_v1_column_types_slanted_ref` (n=2204 column; 1,357 neuron annotations; "Unsure" note); `aibs_metamodel_celltypes_v661` (hierarchical classifier; "as of version 661"; 94,014; L5 inhibitory confusion); `baylor_log_reg_cell_type_coarse_v1` (logistic regression on dendrites; 55,063; "required more data…"; "good table to double check") | AT |
| Corrections tables are living; "New cells will be added as more changes arise…"; both folded into `aibs_cell_info` | M1718 "Corrections tables" |
| Lab: 2,070 cells; sources 1,341 / 598 / 127 / 4; 1,732 exc / 338 inh | `assets/notebooks/microns-lab/microns-lab-executed.ipynb` output ("class label source: …"); `results_summary.json` |
| "moves a cell's pairs into the wrong null stratum" | `notebooks/microns-lab/index.md:323–325` |
| Norms 6, 8, 19 | `hidden-curriculum/technical-practice.md` |

Brief discrepancy noted: the brief summarized the lab as "`aibs_metamodel_celltypes_v661`
+ manual labels for 1,341 cells". The executed notebook shows four sources; the largest
classifier source is `baylor_log_reg_cell_type_coarse_v1` (598), not the v661 metamodel
(127). The page reports all four.

Left as qualitative, unsourced on this page (textbook-level, no numbers): interneuron
morphology cues (basket, chandelier, Martinotti, bipolar/VIP), the pyramidal subtype
table (which the page already flags as tracing-derived inference). Links: all 13
`relative_url` targets resolve.

---

## Validators (28 September 2026, after all edits)

- `ruby scripts/validate_frontmatter.rb`: no problems found.
- `ruby scripts/validate_code_span_paths.rb`: OK (262 permalinks, 514 files).
- `ruby scripts/validate_technical_evidence.rb`: no warnings.
- Reserved synthetic labels (T9, T12, T15, T17–T19, T21, T27, T31, T32, T41, T43, T67,
  T75–T77, T795, T802): none remain on the four pages.
