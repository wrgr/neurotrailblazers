# Content pass 2: `content-library/case-studies/microns-visual-cortex.md`

Rewrite per NEXT_CONTENT_PASS.md item "co-registration, functional-unit matching, what
calcium data does and does not license". Done 27 September 2026. Only the case-study page
and this report were edited. Branch `compass-workshops`; nothing committed.

## Summary of changes

- Kept the front matter fields, the "Before you quote a number" callout, the Overview
  numbers (all canonical per `docs/reviews/2026-09-site-audit/canonical-facts.md` §1),
  the EM pipeline, proofreading, data access, discussion questions and references.
  Added `"04"` to `primary_units` and "co-registration" to `topics`; the `description`
  now says what the page covers.
- New section "The join is the experiment": why the anatomical null (axon–dendrite
  proximity without a synapse) is the comparison that matters, and why only a dense
  reconstruction can supply it.
- New section "Two-photon imaging came first, in one mouse": what was recorded (mouse
  line, mesoscope, 14 of 19 scans over six days, volume, frame rates, CaImAn, 8.1% of
  masks excluded), what the mouse saw (84 min per scan, natural clips, Monet2, Trippy,
  oracle trials and the oracle-score definition), and "Units are not neurons"
  (125,413 masks, 115,372 somatic, 75,909 neurons; the 10 µm / 20 µm merge rule).
- New section "Co-registration maps an optical volume onto an EM volume": the 2,934
  fiducials (1,994 somata, 942 vessels; more vascular below 400 µm; placed on a
  256 × 256 × 940 nm down-sample), the staged transform as a table with the paper's
  residual after each stage (~10, 5.6, 4.6, 3.9/3.5/3.1/2.9, 0.003 µm), the 2,933
  leave-one-out refits, the 3.8 µm average residual, the manual matching interface,
  19,181 units → 15,439 EM neurons, the residual and separation-score definitions, the
  cross-scan signal-correlation validation, the three automatch tables with their counts
  and precision (83% / 84% / 89%; 90% after dropping the bottom 30% by separation), and
  the exact filters Ding et al. applied (`coregistration_manual_v4`, one scan excluded,
  residual < 20, separation > −10; overlap volume ~560 × 1,100 × 500 µm; 43,679
  excitatory nuclei; 13,952 manually matched).
- New section "What the calcium data license, and what they do not", built on the Unit
  01 / Introduction-lecture Bin A/B/C framework: what a match gives you, six inherited
  assumptions (match, calcium→spiking proxy, depth artifacts, cross-session state,
  stimulus coverage, digital-twin caveats), and six things the data do not license
  (inhibitory function, function below the scans, `minnie35`, causation, cross-animal
  generalization, graph completeness with the 43% untraceable-axon-end figure).
- "Proofreading was targeted, and the targets were functional": the 85 / 1,188 / 1,433
  counts, edits per axon, edits per proofreader-week, NEURD's >164,000 edits, the
  `proofreading_status_and_strategy` labels, and Ding's presynaptic selection criteria.
- Companion findings expanded with numbers from the papers (Ding: 148 pre / 4,811 post,
  84 full + 64 partial, 144 / 3,920 after thresholds, ADP within 5 µm, *L*<sub>d</sub>,
  6,608 pairs, *r* = 0.032, feature vs. RF split, the V1 L2/3 orientation null result,
  common-input result in 3 of 4 projection types, RNN; Schneider-Mizell: 1,886 cells /
  1,352 neurons, >46,000 edits, >70,000 synapses, 21 + 8 of 29 disinhibitory cells;
  Elabbady: perisomatic classification). Turner 2022 kept, with its abstract quoted.
- Removed: "Inhibitory interneurons, roughly 15–20% of cortical neurons" (unsourced);
  the generic "Pyramidal Cell Morphometry" and "Connectivity Motifs" subsections (no
  sourced content; the motif point now lives in the lab pointer).
- Added a "Check yourself" block (three `<details>` questions, Unit style) and a
  "Related" list, plus Elabbady 2025 and Celii 2025 to Key References.
- Links: MICrONS real-data lab (`/notebooks/microns-lab/`, three places), Unit 04, Unit
  01, Unit 08, Unit 09, the Introduction lecture, provenance-and-versioning,
  reconstruction-pipeline, synapse-detection, the dataset catalog record, the
  case-study papers page, and the three sibling case studies. All resolve (checked by
  grep against `permalink:` lines; the catalog path is the `_config.yml` collection
  permalink already used on `start-here.md`).
- Validators: `validate_frontmatter.rb` (no problems), `validate_code_span_paths.rb`
  (OK, 249 permalinks / 501 files), `validate_technical_evidence.rb` (no warnings).
  Hype-word and British-spelling grep: no hits.

## Source table (claim → DOI / location)

Sources read in full through Europe PMC REST full-text XML on 27 September 2026:
MICrONS Consortium 2025 (PMC11981939), Ding et al. 2025 (PMC11981947), Schneider-Mizell
et al. 2025 (PMC11981935), CAVE (PMC12074985). Abstracts via Europe PMC `resultType=core`:
Turner et al. 2022 (PMC9337909; full text not served), Elabbady et al. 2025 (PMC11981918),
Celii et al. 2025 (PMC11981913).

M = MICrONS Consortium 2025, doi:10.1038/s41586-025-08790-w. D = Ding et al. 2025,
doi:10.1038/s41586-025-08840-3. SM = Schneider-Mizell et al. 2025,
doi:10.1038/s41586-024-07780-8.

| Claim on the page | Source, location |
|---|---|
| 1.3 × 0.87 × 0.82 mm in vivo; >200,000 cells; 524 M synapses; ~75,000 / 75,909 neurons; ~4 nm, 40 nm; 27,972 cut / 26,652 imaged; ~2 PB; 65% = share of sections; 84,035 segmented neurons; 1,046,656 edits to 16 Sep 2024 | M Main, Abstract, "2P calcium imaging", "The EM volume", "Automated reconstruction", "Proofreading"; canonical-facts.md §1a–1g |
| GCaMP6s via Slc17a7-Cre × Ai162; 14 scans; P75–P81; 1,200 × 1,100 × 500 µm; layers 2–5; four areas; ~50% VISp / 50% HVA | M "2P calcium imaging"; Methods "Imaging site selection" |
| 19 completed scans over 6 days; 14 released; 11 scans at 6.3 Hz with 4 depths, 2 at 8.6 Hz, 1 at 9.6 Hz; 10–15 µm depth increments; site re-found by vessels and somata (GCaMP6s exclusion); CaImAn CNMF; classifier excluded 8.1% of masks | M Methods "2P functional imaging" |
| Timeline: 2P 4–9 March 2018; perfusion 16 March 2018 (P87) | M Methods "Timeline" |
| Stimulus ~84 min; 64 min natural clips (films, Sports-1M, rendered POV); Monet2 and Trippy 10 min each; 6 oracle clips × 10 repeats totaling 1 min, conserved across scans; oracle-score definition (jackknife mean of leave-one-out correlation) | M "Behavioural tracking and visual stimulation"; Methods "Stimulus composition", "Global directional parametric stimulus", "Local directional parametric stimulus Trippy", "Oracle score" |
| Monet2: smoothed Gaussian noise with coherent orientation and motion, 16 directions | M Methods "Global directional parametric stimulus" |
| Head-fixed, left visual field, treadmill velocity, eye and pupil recorded | M "Behavioural tracking and visual stimulation" |
| 125,413 masks; 115,372 somatic; 75,909 neurons; greedy 3D-proximity assignment | M "2P calcium imaging" (last two paragraphs) |
| Merge rule: closest pairs from different scans merged until all ≥10 µm apart or mask >20 µm tall in z | M Methods "2P structural stack" |
| Structural stack 1,412 × 1,322 × 670 µm at 0.5 px/µm; Dextran Texas Red vessel label | M "2P calcium imaging"; Methods "2P structural stack" |
| Unit keys: session, scan_idx, field, unit_id | M Methods "Generating the fiducial-vessel agreement automatch table" |
| Tissue: perfusion fixative, vibratome slice, osmium staining, resin, trimming | M Methods "Tissue preparation" |
| ~95 million tiles; systematic residual trends on the scale of knife cleanings / tape changes | M "The EM volume"; Methods "Transform" |
| 2,934 fiducials = 1,994 somata + 942 vessels; more vascular fiducials below 400 µm; fiducials placed at 256 × 256 × 940 nm | M "Functional–structural co-registration"; Methods "Transform" |
| Transform stages and residuals: polynomial ~10 µm; z-bins (5, then 21) 5.6 and 4.6 µm; TPS grids n = 3, 5, 10, 12 → 3.9, 3.5, 3.1, 2.9 µm; final TPS 0.003 µm; 2,933 leave-one-out refits | M Methods "Transform" |
| Average residual 3.8 µm | M "Functional–structural co-registration"; Methods "Transform" (canonical-facts audit figure re-verified) |
| Manual matching interface: average × correlation image; EM at 1 µm³ transformed to 2P; vessel overlay; soma constellation; Neuroglancer confirmation; table `coregistration_manual_v4`; recommended table listed at microns-explorer.org/cortical-mm3#f-coreg | M Methods "Assigning manual matches" |
| 19,181 functional ROIs from 14 scans → 15,439 EM neurons; multiple ROIs per neuron | M "Functional–structural co-registration" |
| Residual and separation-score definitions; negative separation = matcher overrode nearest neighbor | M Methods "Evaluating manual matches"; Extended Data Fig. 4 legend |
| Cross-scan signal-correlation validation; stronger at oracle > 0.2 | M Methods "Evaluating manual matches"; Extended Data Fig. 4 |
| Fiducial automatch: 84,198 ROIs → 37,364 neurons, 83%; filtered 90% with 59,934 / 31,042; table `coregistration_auto_phase3_fwd`; `linear_sum_assignment` | M "Functional–structural co-registration"; Methods "Generating the fiducial-based automatch" |
| Vessel automatch: B-spline (SimpleITK), no fiducials; 75,856 → 34,712, 84%; filtered 90% with 53,248 / 28,233; table `apl_functional_coreg_vess_fwd` | M "Functional–structural co-registration"; Methods "Vessel-based co-registration and automatch" |
| Agreement table: 89%, 60,091 / 29,620 | M "Functional–structural co-registration" |
| Precision computed on commonly attempted rows; residual thresholded as a maximum, separation as a minimum, via percentiles | M Methods "Evaluating automatch tables" |
| Ding used `coregistration_manual_v4`; excluded session 7 scan 4 (water ran out ~20 min); residual < 20, score > −10; highest-oracle unit kept per neuron | D Methods "Preprocessing of neural responses…", "2P–EM matching", "In vivo reliability threshold" |
| Overlap volume ~560 × 1,100 × 500 µm; 82,247 nuclei; 43,679 excitatory in overlap; 13,952 excitatory neurons manually matched | D "MICrONS functional connectomic dataset" |
| Digital twin: core trained on eight other mice, readouts per scan; 250 novel 10 s clips; feature vs. RF factorization; validated in separate mice; results replicate with in vivo correlations; RF centers shifted toward monitor center; "care should be taken in interpreting their internal representations" | D "Similarity across spatial scales", "Factorized in silico representation", Discussion, Methods "Model architecture…", Extended Data Figs. 2–4 |
| "simultaneously recording single action potentials … constrained by sensor dynamics and optical sampling constraints"; depth artifacts from scattering and out-of-plane fluorescence; multi-session state caveat | M Discussion "Importance of functional connectomics" and "Advances and limits in large-scale EM" |
| `minnie35`: only a synapse table; little proofreading | M "Integrated analysis" |
| "consistent with an underlying Hebbian plasticity mechanism"; conservative estimate due to incomplete reconstructions; possible bias toward larger synapses | D "Similarity across spatial scales"; Discussion |
| Single-animal limitation quotes | SM "Limitations"; D Discussion |
| Median untraceable ends: dendrites 1% (n = 148), axons 43% (n = 84), boundary ends excluded | D Methods "Manual proofreading completion" |
| Sectioning supervised around the clock for 12 days; 5 autoTEMs; ~6 months; 800 µm span, sections 7,931–27,904, ~0.1% loss; subvolume section ranges; composite image at interface | M "The EM volume" |
| Coarse/fine alignment; five-pixel polynomial threshold; CNN displacement fields; 8 nm aligned volume | M "The EM volume" (Reconstruction paragraph) |
| Affinity CNN + mean-affinity agglomeration; segmentation skipped where alignment insufficient; dendrites/spines good; larger-caliber and inhibitory axons better; pia/WM errors | M "Automated reconstruction"; "Proofreading" (inhibitory axons thicker) |
| 144,120 nuclei; SVM 96.9% precision / 99.6% recall; 82,247 neurons predicted | M "Automated reconstruction"; Methods "Cell classification" |
| 524 M = 186 M + 337 M; 8,611 synapses in 70 subvolumes; 96% / 89%; 98% partner assignment on 191 held-out | M "Automated reconstruction" |
| ChunkedGraph / CAVE; modified Neuroglancer; REST API; all proofreading in subvolume 65; quarterly updates; 85 fully proofread excitatory; 1,188 dendrite-only; 1,433 with proofread axons; 100–1,000 edits per axon; 400–600 edits per week; NEURD >164,000 edits; 7,050 multi-soma objects; VORTEX | M "Proofreading"; Methods "Proofreading" |
| Table `proofreading_status_and_strategy`; `status_dendrite`, `status_axon`, `strategy_axon`; labels `axon_fully_extended`, `axon_partially_extended`, `axon_interareal` | M Methods "Manual proofreading of dendritic and axonal processes" |
| Ding presynaptic selection: oracle > 0.25, model test correlation > 0.15; columns in V1 and RL from retinotopy; first 40 unblinded, rest blind | D Methods "Presynaptic neuron selection" |
| Ding graph: 148 pre / 4,811 post; 84 full + 64 partial (HVA→V1 feedback branches); NEURD cleaning; CCmax > 0.4, CCabs > 0.2; 144 / 3,920 pass; >1.5 m reconstructed | D "MICrONS functional connectomic dataset"; Methods "Functional unit inclusion criteria", "Axonal proofreading"; Discussion |
| ADP within 5 µm; *L*<sub>d</sub>; synapses within 3 µm of a proximity; three cohorts | D "Multi-scale anatomical controls"; Methods "Anatomical controls" |
| Connected > ADP > same-region for all four projection types; graded *L*<sub>d</sub> and synapse-density effects | D "Similarity across spatial scales", Fig. 2 |
| 6,608 pairs; cleft volume *r* = 0.032, *P* < 0.001; multi-synapse pairs more correlated | D "Similarity across spatial scales", Fig. 2h–j |
| Feature similarity predicts synaptic scale; RF distance uncorrelated or anticorrelated in V1 | D "Different rules at synaptic scale", Fig. 3 |
| No orientation like-to-like within V1 L2/3; unconnected pairs equally similar; local orientation bias | D "Like-to-like orientation tuning in V1" |
| Common-input cohorts more similar in 3 of 4 projection types | D "Neurons with common input are similar", Fig. 5 |
| RNN like-to-like; ablation | D "Like-to-like connectivity in RNNs", Fig. 6 |
| Turner 2022: ~250 × 140 × 90 µm L2/3 V1; "pyramidal cells receiving more connections from nearby cells exhibit stronger and more reliable visual responses"; configuration model | Turner et al. 2022 abstract, doi:10.1016/j.cell.2022.01.023 |
| "many more overall connections, but still only twice the number of functionally characterized cells"; Lee et al. 50 cells | M Discussion "Importance of functional connectomics" |
| SM column: 100 × 100 µm box, L1 to WM; 1,886 cells; 1,352 neurons; >46,000 edits; >70,000 synapses; 21 + 8 of 29 InhTCs; basket-targeting specialist new; "principal concern … single animal, in one location near the edge of VISp" | SM Abstract, Main, "Dense neuron population…", "Inhibition of inhibitory neurons", Methods "Column description", "Limitations" |
| PTC = basket cells, DTC = Martinotti cells | M Fig. 7 legend |
| Elabbady: perisomatic features suffice to classify cells incl. connectivity-defined types | Elabbady et al. 2025 abstract, doi:10.1038/s41586-024-07765-7 |
| NEURD: mesh → annotated graph; automated merge-error proofreading; spines; ADPs | Celii et al. 2025 abstract, doi:10.1038/s41586-025-08660-5 |
| CAVE citation, *Nat Methods* 22:1112–1120 | doi:10.1038/s41592-024-02426-z (Europe PMC record) |
| DataJoint; NWB on DANDI dandiset 000402; cloud-volume; synapse table 337.3 M rows | M "Integrated analysis" |
| Marginal cost ranking (labor, compute, grid tape); no fundamental barrier to more volumes | M Discussion "Advances and limits in large-scale EM" |
| H01 aspect-ratio comparison | M Discussion "Comparison with other EM studies" |
| Versions 943 and 1300 long-lived; static exports; lab checksums | canonical-facts.md §10; `notebooks/microns-lab/index.md` |

## Links needed (other agents' pages)

- `content-library/index.md:145` — the MICrONS case-study row lists units "01, 03, 08, 09".
  The page's `primary_units` now also includes 04. Suggested cell: `01, 03, 04, 08, 09`.
- `technical-training/04-volume-reconstruction-infrastructure.md` — in §2 ("editable graph")
  or the lab intro, one line: "The [MICrONS case study]({{ '/content-library/case-studies/microns-visual-cortex/' | relative_url }})
  walks through the co-registration tables and the proofreading-status labels this lab filters on."
- `technical-training/01-why-map-the-brain.md` §3 (bins) — one line after the Bin C list:
  "For a worked case of what a second measurement does and does not move out of Bin C, see
  the [MICrONS case study]({{ '/content-library/case-studies/microns-visual-cortex/' | relative_url }})."
  (The unit's Go-deeper list at line 479 already links the page.)
- `notebooks/microns-lab/index.md` — near the data-citation box: "Background on the
  `proofreading_status_and_strategy` labels and the co-registration tables:
  [MICrONS case study]({{ '/content-library/case-studies/microns-visual-cortex/' | relative_url }})."
- `_datasets/microns.md` — optional, in "What it does not support": link the case study's
  "What the calcium data license" section.
- `content-library/journal-papers/case-studies.md` — the Ding entry (if one is added) can
  point to this page's "Like-to-like wiring, with the anatomical null in place".

## Unverifiable items left out, and source discrepancies noted

- **Soma diameter.** The first draft said "a cortical soma is roughly 10 to 20 µm across".
  No source read gives that figure; replaced with the paper's own 10 µm merge threshold.
- **Inhibitory fraction "15–20%".** Was on the old page; not in any source read. Removed.
- **Person-years of proofreading.** The paper publishes none; the page says so.
- **Whether 3.8 µm is the leave-one-out figure.** The Results give 3.8 µm as "the average
  residual"; the Methods describe the leave-one-out procedure separately and do not attach
  a number to it. The page reports 3.8 µm as the paper's average residual and describes the
  leave-one-out measure without asserting they are the same number.
- **Turner 2022 animal.** The first draft said "from a different mouse". Neither the
  Turner abstract nor the 2025 paper says so in text I read. Removed.
- **Imaging ages.** M Results say scans were "collected between postnatal day 75 (P75) and
  P81"; M Methods "Timeline" gives 2P imaging 4–9 March 2018 (P75–P80). The page gives
  both, attributed. Canonical-facts §1a uses P75–P80.
- **Structural-stack date.** M Methods "Timeline" prints "Structural Stack: 21 March 2018
  (P83)" after "Perfusion: 16 March 2018 (P87)". With birth 19 December 2017, P83 is 12
  March; the printed date is a typo in the source. The page does not quote the stack date.
- **Layer coverage of the 2P volume.** M Results say the imaged neurons span "cortical
  layers 2 to 5"; M Methods "Imaging site selection" says the target volume spanned "layer
  2 to layer 6", and Ding says "layers 2 to 6". The page says scans reached ~500 µm and
  quotes "layers 2 to 5" for the released neurons, without claiming layer 6 is absent.
- **Separation-score sign.** Extended Data Fig. 4 defines it as "the difference between the
  residual of the matched pair and the residual of the nearest EM neuronal nucleus that was
  not matched", which read literally would be negative for a good match; the Methods say
  "Negative separation indicates that the nearest EM neuron … was not chosen" and "larger
  separation scores indicate higher confidence". The page follows the Methods'
  interpretation (nearest-unmatched residual minus matched residual).
- **Precision figures for Ding's filtered manual matches.** Not published; the page gives
  only the thresholds.
- **Live CAVE table names and materialization status** were not queried (auth required);
  table names are as printed in the 2025 paper.
- **Turner 2022 full text** is not served by Europe PMC; only the abstract was used, and
  the page quotes it verbatim.
