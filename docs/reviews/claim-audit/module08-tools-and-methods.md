# Claim audit: Module 8, Tools and Methods

- **Date:** 2026-09-26
- **Deck:** `course/decks/marp/en585781/module08-tools-and-methods.marp.md` (56 slides; the cover is slide 1)
- **Method:** I checked each quantitative or historical claim against the primary papers, using Europe PMC full text, Crossref metadata and official project or API pages. The nature.com and science.org pages would not load, so I read those papers through PMC full text or the author PDFs.

## Summary counts

| Verdict | Count |
|---|---|
| VERIFIED | 28 |
| CORRECTED | 24 |
| QUALIFIED | 8 |
| HYPOTHETICAL (labeled) | 6 |
| UNVERIFIED | 3 |

The table has 69 rows. Some rows group several related claims, such as reference DOIs.

## Claims

| Slide # | Claim (short quote) | Verdict | Source (DOI/URL + where in source) | Change made |
|---|---|---|---|---|
| 1 | Cover image: H01, CC BY 4.0, Shapson-Coe et al. 2024 | VERIFIED | doi:10.1126/science.adk4858. Google Neural Mapping datasets page: "All released datasets are licensed under a Creative Commons Attribution 4.0 License" | None |
| 2 | "1 mm³ at 4 × 4 × 40 nm ≈ 1.6 PB raw" | VERIFIED | Arithmetic: (10⁶/4)² × (10⁶/40) = 1.56 × 10¹⁵ voxels at 1 byte, uncompressed | None |
| 5 | "Slides 6–21" (Part A range) | CORRECTED | Deck structure: Part A content runs from slide 6 to slide 24 | "Slides 6–21" → "Slides 6–24" |
| 7 | "The pilot reconstruction (slide 19)" | CORRECTED | The pilot rule is on slide 21 | "slide 19" → "slide 21" |
| 8 | "commonly ~2–2.5% glutaraldehyde plus 2% paraformaldehyde in 0.1 M cacodylate or phosphate" | CORRECTED | Hua et al. 2015 (doi:10.1038/ncomms8923, Methods, "Sample extraction and fixation") and MICrONS 2025 (doi:10.1038/s41586-025-08790-w, Methods) both use 2.5% PFA, 1.25% GA, 2 mM CaCl₂, 0.08 M cacodylate, pH 7.4 | Replaced with the verified recipe, attributed to Hua et al. 2015 and MICrONS |
| 9 | rOTO order: OsO₄, then ferrocyanide, TCH, OsO₄, UA, lead aspartate | VERIFIED | Hua et al. 2015, Methods, "Sample staining": 2% OsO₄ → 2.5% ferrocyanide → TCH → 2% OsO₄ → 1% UA → lead aspartate | None |
| 11 | "dehydration shrinks tissue, typically 5–20% linearly" | CORRECTED | Korogod et al. 2015 (doi:10.7554/eLife.05793, Results/Fig. 1): 16% loss of cortical thickness, 18% rostrocaudal, 0% mediolateral, ~30% volume after chemical fixation. The paper also cites Kalimo 1976 (16% linear) and Kinney 2013 (15% per axis). This covers the whole preparation, not dehydration alone. I found no source for the 5% lower bound. | → "chemical preparation shrinks tissue — reported ~15–18% linearly, not always isotropically"; sources added to the speaker notes |
| 12 | Sections 30–50 nm; FIB mills "a few nanometers" | VERIFIED | MICrONS 40 nm nominal; H01 33.9 nm mean (Shapson-Coe 2024 main text); Xu et al. 2017 | None |
| 12 | Citation years (Denk & Horstmann 2004; Knott 2008; Xu 2017; Hayworth 2014/2015/2019; Phelps 2021) | VERIFIED | Crossref: pbio.0020329; JNEUROSCI.3189-07.2008; eLife.25916 (2017); fncir.2014.00068 (2014); nmeth.3292 (2015); s41592-019-0641-2 (online 2019-11-18, print 2020); cell.2020.12.013 (Feb 2021) | None |
| 13 | ssTEM/TEMCA 4 × 4 × 40 nm, up to ~mm³ | VERIFIED | MICrONS 2025: ~4 nm, 40 nm sections, ~mm³ | None |
| 13 | ssSEM + ATUM 4 × 4 × 30–40 nm, up to ~mm³ | VERIFIED | H01: 4 × 4 × 33 nm, ~1 mm³ | None |
| 13 | GridTape TEM "~10⁵–10⁶ µm³" | CORRECTED | MICrONS 2025 Results: "27,972 serial sections (nominal thickness 40 nm) onto grid tape", imaged by 5 autoTEMs in ~6 months, ~mm³ volume | → "Up to ~mm³" |
| 13 | Multibeam "~mm³ in months" | QUALIFIED | H01 was imaged in 326 days on a 61-beam multiSEM (Collins et al. 2025, arXiv 2405.10488; the H01 main text gives no duration) | None on the slide; note on slide 15 |
| 13 | SBEM 10–20 × 10–20 × 25–50 nm, "10⁶–10⁷ µm³" | CORRECTED | Voxel sizes verified: Motta 2019 about 11 × 11 × 28 nm, Svara 2022 14 × 14 × 25, Hua 2015 12 × 12 × 30. Volumes: Motta 2019 ~5 × 10⁵ µm³ (doi:10.1126/science.aay3134, abstract); Svara 2022 0.058 mm³ = 5.8 × 10⁷ µm³ (doi:10.1038/s41592-022-01621-0) | → "10⁵–~6 × 10⁷ µm³"; sources in the notes |
| 13 | FIB-SEM 4–8 nm isotropic, 10⁵–10⁶ µm³ | VERIFIED | Xu et al. 2017 abstract: continuously imaged volumes "> 10⁶ µm³" | None; the upper bound is noted in the speaker notes |
| 14 | Landing energy "1–2 keV" | CORRECTED | Eberle 2015: "Typical landing energies of the multibeam … 1–3 keV". Hua 2015: 2.8 keV. Pallotto 2015: 1.4–2.4 keV | → "~1–3 keV" |
| 14 | Dwell "0.1–2 µs" | CORRECTED | Hua 2015: 3.2 µs. Pallotto 2015: 0.45–2 µs. Multibeam per-beam dwell is ~0.1 µs (from Eberle's rates) | → "~0.1–3 µs" |
| 14 | Tile overlap 5–15%; beam current pA–nA | QUALIFIED | Hua 2015: 6–9% overlap. Pallotto 2015: ~200 pA–1 nA | None on the slide; notes say these are typical ranges |
| 14 | SNR ∝ √dose; 2× SNR ≈ 4× time | VERIFIED | Poisson shot-noise statistics. Eberle 2015 ties SNR to current × dwell | None |
| 15 | "61 or 91 electron beams … on the order of a gigapixel per second" | CORRECTED | Eberle et al. 2015 (doi:10.1111/jmi.12224): 61 beams; figures at 0.18–0.72 GPixel/s; "approaching 1 GHz". ZEISS MultiSEM 506 has 91 beams (zeiss.com product page) | → "61 (later 91) … peak rates approaching a gigapixel per second" |
| 15 | "moved 1 mm³ … to an eighteen-month project" | CORRECTED | H01 imaging took 326 days (Collins et al. 2025, citing Shapson-Coe) | → "under a year of imaging (H01)"; source caveat in the notes |
| 15 | "FAST-EM (Kievits & Hoogenboom 2024)", optical detection | CORRECTED | doi:10.1515/mim-2024-0005 has 10 authors: Kievits … Hoogenboom. Abstract: 64 beams, "makes use of optical detection" | → "Kievits et al. 2024" (also on slides 53 and 55) |
| 15 | SmartEM (2025), ML-guided dwell allocation | VERIFIED | Meirovitch et al., Nat Methods, doi:10.1038/s41592-025-02929-3 (online 2025-12-29; print Jan 2026). Abstract: rescans "only the small subareas where a higher quality signal is required"; up to ~7-fold faster | Reworded "changes the square-root relationship" → "changes how the square-root dose budget is spent", because SmartEM reallocates dose and does not change shot-noise physics |
| 16 | Hot-knife (Hayworth 2015); GCIB-SEM (Hayworth 2019), ~10 nm isotropic | VERIFIED | nmeth.3292; s41592-019-0641-2, whose title says "10 nm isotropic resolution" (online 2019) | None |
| 17 | ExM "~25–70 nm effective" | CORRECTED | Chen et al. 2015 (doi:10.1126/science.1260088): ~70 nm. Chang et al. 2017 (doi:10.1038/nmeth.4261): ~25 nm. LICONN: ~20 nm lateral, ~50 nm axial | → "~20–70 nm"; sources in the notes |
| 17 | LICONN "first demonstrated LM route to dense, synapse-level" | QUALIFIED | Tavakoli et al. 2025 abstract: dense synapse-level LM reconstruction "has been out of reach" | Notes mark this as the authors' framing |
| 18 | 800 µm cube at 0.2 Gpx/s → 8 × 10¹⁴ px, ~46 days, ~77 days at 60% | VERIFIED (hypothetical inputs) | Arithmetic checked. The problem statement labels the instrument rate as "your instrument" | None |
| 18 | 1 mm³ takes "about a year" | VERIFIED | H01: 326 days of imaging (secondary source, see above) | None |
| 20 | 4 consecutive losses = 160 nm gap | VERIFIED | 4 × 40 nm | None |
| 20 | Triage scenario (20,000 sections, 15%, 10%) | HYPOTHETICAL | Posed as a question | None |
| 21 | Pilot ~100 µm cube "costs perhaps 1–2% of the project" | UNVERIFIED | No source found. The slide already hedges it | None (see owner items) |
| 22 | Gate thresholds | HYPOTHETICAL | Labeled "Example threshold" | None |
| 24 | "The pilot reconstruction is 1–2% of the project" | UNVERIFIED | Same as slide 21 | → "is perhaps 1–2% of the project (est.)" |
| 25 | "Slides 22–38" | CORRECTED | Part B content runs from slide 26 to slide 38 | → "Slides 26–38" |
| 28 | 0.1 voxel/section × 20,000 = 2,000-voxel drift | VERIFIED | Arithmetic; assumes a systematic bias | None |
| 28 | Saalfeld 2012 elastic alignment | VERIFIED | doi:10.1038/nmeth.2072 | None |
| 30 | SynEM 2017, SyConn 2017, Synful 2021 DOIs | VERIFIED | Europe PMC and Crossref | None |
| 33 | Chunks "commonly 64³ to 512³" | QUALIFIED | Common Neuroglancer precomputed practice; no single normative source | None |
| 33 | Pyramid "30–50% extra storage" | CORRECTED | Geometric series: isotropic 2× ≈ 14%; xy-only 2× ≈ 33% | → "15–33%"; arithmetic in the notes |
| 35 | Raw ~1.5 PB | VERIFIED | 1.56 × 10¹⁵ B (same arithmetic as slide 2) | Assumptions added to the notes |
| 35 | Aligned pyramid ~2 PB, "Base + 30–50%" | CORRECTED | 1.56 × 1.33 ≈ 2.1 PB | Note → "Base + ~33% (xy-only 2× pyramid)" |
| 35 | Affinity maps "~1.5 PB" | CORRECTED | Equals raw only for a single 8-bit channel; 3-channel affinities are 3× | → "≥1.5 PB"; assumption in the notes |
| 35 | Segmentation, mesh, skeleton and table sizes | HYPOTHETICAL | The column is labeled "Estimate"; now also stated in the notes | Notes added |
| 35/38 | ~5 × 10⁸ synapse rows | VERIFIED | MICrONS 2025 abstract: "0.5 billion synapses" | None |
| 36 | 1.5e15/1e7 = 1.5e8 GPU-s ≈ 1,736 GPU-days; ~3.5 days on 500 GPUs | VERIFIED (hypothetical inputs) | Arithmetic; the rate is prefaced "Suppose" | Notes label the inputs as assumptions |
| 36 | "Budget 3–5 full inference passes" | UNVERIFIED | Rule of thumb; no source | None (see owner items) |
| 36 | Proofreading is the dominant cost | VERIFIED | MICrONS 2025 Discussion: "Proofreading and analysis remains the largest overall expense in terms of person hours" | Source added to the notes |
| 36 | "a few hours … per neuron" | HYPOTHETICAL | Conditional ("At even…") | None |
| 37 | Egress "can cost more than storing it for a year" | CORRECTED | AWS S3 pricing (aws.amazon.com/s3/pricing, US East, checked 2026-09): egress $0.05–0.09/GB (~$50k+/PB); Standard storage ~$0.023/GB-mo (~$250k+/PB-yr). True only against cold tiers | → "more than a year of cold-tier storage"; pricing note added |
| 37 | Small-object overhead "can exceed storage costs" | QUALIFIED | Plausible from per-request pricing against cold-tier storage; hedged with "can" | None |
| 37 | "Affinity maps are the size of the raw data" | CORRECTED | See slide 35 | → "at least the size" |
| 39 | "Slides 39–56" | CORRECTED | Part C content runs from slide 40 to slide 54 (55–56 are references and credit); changed for consistency with Parts A and B | → "Slides 40–54" |
| 41 | "A merge is adding an edge. Microseconds" | CORRECTED | CAVE (Dorkenwald et al., doi:10.1038/s41592-024-02426-z, Results, Fig. 2i): merges median 4,116 ms; splits median 5,813 ms on MICrONS65 | → "Seconds, not gigabytes (median ~4 s in CAVE)" |
| 41 | DVID (Katz & Plaza 2019); CATMAID (Saalfeld 2009) | VERIFIED | doi:10.3389/fncir.2019.00005; doi:10.1093/bioinformatics/btp266 | None |
| 42/44/49 | MICrONS materialization v943; datastack `minnie65_public` | VERIFIED | tutorial.microns-explorer.org/materialization-version.html: v943, 2024-01-22 | None |
| 43 | 1,412 vs 1,530 synapses | HYPOTHETICAL | Labeled "Hypothetical situation" | None |
| 44 | Header values (caveclient 5.21.0, hash, date, seed) | HYPOTHETICAL | caveclient 5.21.0 exists on PyPI (2024-04-26). The notes said the values were illustrative, but the slide did not | Header comment → "reproducibility header (illustrative values)" |
| 44 | "six lines" | VERIFIED | The header has six assignments | None |
| 48 | BossDB serves "MICrONS, H01, Kasthuri, Witvliet, zebrafish" | CORRECTED | The BossDB collection list (api.bossdb.io/v1/collection/, public token, 2026-09-26) includes `microns`, `kasthuri2015`, `witvliet2020` and `hildebrand` (zebrafish), but no H01 or Shapson-Coe collection | Removed "H01" |
| 48/55 | BossDB citation doi:10.1038/s41592-018-0181-1 | CORRECTED | That DOI is Vogelstein et al. 2018, the NeuroData ecosystem paper. The dedicated BossDB paper is Hider et al. 2022, doi:10.3389/fninf.2022.828787 | Slide 48 src → Hider DOI; slide 55 lists both |
| 48 | neuPrint, webKnossos, VAST DOIs | VERIFIED | Crossref: fninf.2022.896292; nmeth.4331; fncir.2018.00088 | None |
| 50 | "500×" (whole mouse brain vs 1 mm³) | VERIFIED | Mouse brain ~500 mm³ (Collins et al. 2025, citing primary refs; Abbott et al. 2020) | None |
| 50 | "Lost-section rates tolerable at 20,000 sections" | CORRECTED | MICrONS: 27,972 sections | → "~28,000 sections" |
| 50 | "Millions of sections" for a whole brain | CORRECTED | The section count scales with depth, not volume: shortest mouse-brain axis ≤ ~8 mm (Allen CCFv3 bounding box) ÷ 40 nm ≈ 2 × 10⁵ | → "~2 × 10⁵ far larger sections (est.)" |
| 50 | "~1 Gpx/s with multibeam" | QUALIFIED | Eberle 2015: "approaching 1 GHz" peak | → "Approaching 1 Gpx/s peak (multibeam)" |
| 50 | "~2 PB hot per mm³ → ~800 PB" | QUALIFIED | 800 PB is 500 × 1.56 PB raw (4×4×40 nm, 8-bit, uncompressed), not 500 × 2 PB hot. Abbott et al. 2020 (doi:10.1016/j.cell.2020.08.010) give roughly 1 million TB (~1 EB). This follows the coordinator's cross-deck guidance to keep ~800 PB as an estimate | → "~1.6 PB raw per mm³ / ~800 PB raw (est.)"; notes cite Abbott ~1 EB |
| 53 | Januszewski 2018; Dorkenwald 2025; Tavakoli 2025; SmartEM 2025 | VERIFIED | Crossref: FFN online 2018-07-16; CAVE online 2025-04-09; LICONN 2025; SmartEM online 2025-12-29 | Only Kievits fixed (see slide 15) |
| 55 | Other reference DOIs (Mikula & Denk 2015, Pallotto 2015, Bock 2011, Berning 2015, Funke 2019) | VERIFIED | Titles match through Europe PMC and Crossref | None |
| 55 | "SmartEM 2025" reference without authors | QUALIFIED | Meirovitch et al. | Added "Meirovitch et al." |

## Needs owner decision

1. **Pilot cost "1–2% of the project" (slides 21, 24).** I found no source. Slide 24 is now hedged ("perhaps … (est.)") to match slide 21. Keep it as the author's estimate, or cite a project that reports its pilot cost.
2. **"Budget 3–5 full inference passes" (slide 36).** This is an unsourced rule of thumb. It could be labeled "rule of thumb" or tied to a project that reports how many inference passes it ran.
3. **Storage rows for segmentation (0.2–0.8 PB), meshes (1–10 TB), skeletons (10–100 GB) and the synapse table (50–200 GB) (slide 35).** These are order-of-magnitude assumptions under a column labeled "Estimate". They are unverified, and the notes now say so. The owner could anchor them to the published MICrONS or H01 release sizes.
4. **H01 imaging duration of 326 days (slide 15 and notes).** This comes from a secondary source (Collins et al. 2025). The H01 main text does not state it, and I could not reach the Science supplementary materials.
5. **Chunk sizes of 64³–512³ (slide 33).** This is typical practice with no single primary source. I left it unchanged.

## Image credits

- **Slide 1 (cover):** `h01/10b-segmentation-overlay.jpg` has an image-specific credit on the slide ("H01 release · Lichtman Lab / Harvard & Connectomics at Google · Image: CC BY 4.0 · Shapson-Coe et al. (2024) · doi:10.1126/science.adk4858"). It is repeated on slide 56. The licence is confirmed by Google's Neural Mapping datasets page (CC BY 4.0).
- The deck has no other images. No credits are missing.
