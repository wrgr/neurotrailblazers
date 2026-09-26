# Kit materials audit: every named material in the 25 module kits

*Audited 26 September 2026 on branch `compass-workshops` (base `fe473c1`) for
NEXT_CONTENT_PASS.md item 5. Scope: `modules/moduleNN.md`, the generated session kits
(`teaching/sessions/moduleNN.md`), worksheets (`assets/worksheets/moduleNN/`) and decks
(`course/decks/marp/modules/`). Site paths were checked against permalinks and files in
the repository. External URLs were fetched with curl. No Jekyll build was run.*

---

## Summary

Before this pass, 19 of the 25 modules (01 to 19) named at least one material that did
not resolve: a file, notebook, patch set, dataset, script or template described as
"provided", "supplied", "shared" or "pre-identified" that the site did not publish, or
an image, viewer or tool named with no link. The syllabus pass had found the problem in
Modules 03-07 and 09-11; the same pattern was in 01, 02, 08 and 12-19. Modules 20-25
name only learner-produced work, inline content or pages that exist.

| Count | Before | After |
|---|---|---|
| Named materials audited (the rows below, excluding site-path rows) | 99 | 99 |
| Missing or unlinked | 70 | 0 |
| Resolves, inline, instructor-prepared, learner-supplied or narrative | 29 | 99 |
| Distinct site paths referenced from each module's page, kit and worksheet (sum over 25 modules) | 493 | 513 |
| Of those, unresolved | 0 | 0 |

Every site path already resolved before this pass. The missing materials were named
in prose, which the link audit cannot see. Of the 70 missing items, 30 are now
**published** as synthetic kits under `assets/kits/`, 35 are **rewritten** to point at
something that exists (a public viewer, a site page, inline text, or a recipe for an
instructor-built set), and 5 are **linked** to a resource that already existed. No real
EM image or real dataset extract was created. Every published kit file is synthetic,
generated from a fixed seed by `scripts/generate_kit_materials.rb`, and says so in its
first lines.

`scripts/validate_kit_materials.rb` now fails the build on an unresolved path, on a
"provided"/"supplied"/"sample file" line that links nothing, and on kit-file drift from
`assets/kits/manifest.json`. Run against the pre-fix tree, it reports 33 trigger lines
in 11 modules (counting the worksheet and session-kit copies of each studio step). The
other missing items were phrased in ways no phrase list can catch without false
positives ("present 4 EM patches", "a light microscopy image"); this audit found those
by reading.

Status key: **resolves** (exists and is linked), **inline** (the content is written on
the page), **instructor** (the instructor prepares it and the page says how),
**learner** (the learner brings or produces it), **missing** (named, not published,
or not linked). Resolution: **published** (new file under `assets/kits/`),
**rewritten** (module text changed to point at what exists), **linked** (existing
resource, link added), **kept** (no change needed).

## Inventory

| Module | Material | Where named | Status before | Resolution |
|---|---|---|---|---|
| 01 | TED clip, Seung, "I am my connectome" | Run-of-show block 1; front matter `videos` | resolves (external, 200) | kept |
| 01 | Before/after of raw EM and its reconstruction | Block 1 | missing | rewritten: the raw and segmented H01 pair, Step 6 of `/content-library/case-studies/h01-pipeline/` |
| 01 | Three case studies (C. elegans, FlyWire, MouseConnects) | Block 2 | inline | kept |
| 01 | Three example hypotheses with non-claims | Block 4 | instructor | kept; the worked example on the page supplies one |
| 01 | 21 site paths (content library, units, kit, worksheet, deck) | Page, kit, worksheet | resolves | kept |
| 02 | Five hidden-curriculum scenarios | Block 1 | inline | kept |
| 02 | Role-expectation worksheet | Block 2 | missing | rewritten: a three-column table described inline |
| 02 | Script templates for five situations | Block 4 | missing (3 of 5 inline in studio) | rewritten: the other two templates written inline |
| 02 | 16 site paths | Page, kit, worksheet | resolves | kept |
| 03 | "The sample notebook I have shared" | Block 1 | missing | rewritten: instructor builds the five-section skeleton live |
| 03 | Bad notebook shown beside a good one | Block 1 | missing | rewritten: made live from a copy (cells out of order, markdown deleted, hidden state) |
| 03 | "A provided sample CSV" when CAVE is unavailable | Studio step 3 | missing | published: `assets/kits/module03/synapses_sample.csv`, `.meta.json`, `README.md` |
| 03 | CAVEclient, CloudVolume, NetworkX, pandas, matplotlib | Concept set, block 2 | learner (pip install) | kept |
| 03 | 17 site paths | Page, kit, worksheet | resolves | kept |
| 04 | Allen Brain Atlas viewer | Pre-class | missing (no link) | linked: `https://atlas.brain-map.org/` (200) |
| 04 | Nissl light-microscopy image beside EM of the same region | 00:00-10:00 | missing | rewritten: Allen Atlas section beside the H01 layer-segmentation figure (H01, Step by Step, Step 8) |
| 04 | "Real images from MICrONS or H01" | 00:00-10:00 | missing (no link) | linked: MICrONS Explorer, H01 Explore (both 200) |
| 04 | Four unlabeled guided patches (A-D, D is a CA3 mossy fiber bouton) | 10:00-24:00 | missing | rewritten: instructor patch set from MICrONS, recipe under "Building the patch set"; Patch D described from the worked example (see owner decisions) |
| 04 | Three ambiguous patches | 24:00-38:00 | missing | rewritten: from the patch set |
| 04 | Four learner annotation patches | 38:00-50:00 | missing | rewritten: from the patch set |
| 04 | Eight unlabeled L1-L6 patches | Studio scenario | missing | rewritten: from the patch set; scenario names the source |
| 04 | 26 site paths | Page, kit, worksheet | resolves | kept |
| 05 | Three sample patches "posted to the course portal" | Pre-class | missing | rewritten: the artifact gallery on the Artifact taxonomy page |
| 05 | Projected gallery of 8-10 patches | Materials | missing | rewritten: instructor patch set from MICrONS or H01, recipe under "Building the patch set" |
| 05 | QA decision worksheet | Materials | missing (no link; file existed) | linked: `/assets/worksheets/module05/module05-activity.md` |
| 05 | Artifact reference card | Materials | missing | rewritten: print the severity section of the Artifact taxonomy page |
| 05 | Four modality images (ssTEM, SBEM, FIB-SEM, ambiguous) | 00:00-08:00 | missing | rewritten: three public-volume images from different instruments plus one ambiguous |
| 05 | Annotated artifact examples | 08:00-20:00 | missing | rewritten: Artifact taxonomy page |
| 05 | Segmentation output over each artifact | 08:00-20:00 | missing | rewritten: the public viewer's segmentation layer |
| 05 | Six patches per pair | 20:00-34:00 | missing | rewritten: from the patch set |
| 05 | "The six provided image patches" | Studio step 1 | missing | rewritten: from the patch set; recipe says they stand in for the scenario's pilot images |
| 05 | One new patch for the competency check | 56:00-60:00 | missing | rewritten: from the patch set |
| 05 | "Course dataset" for the post-class assignment | Post-class | missing | rewritten: three locations in MICrONS or H01, with coordinates |
| 05 | Slides PDF | Front matter `slides` | resolves | kept |
| 05 | 17 site paths | Page, kit, worksheet | resolves | kept |
| 06 | "The practice dataset in Neuroglancer" | Pre-class | missing | rewritten: MICrONS Explorer |
| 06 | Well-segmented region beside raw EM | 00:00-08:00 | missing | rewritten: H01 Step 6 pair |
| 06 | Real merge, split and boundary examples | 08:00-22:00 | missing | rewritten: worked-examples Scenarios 1 and 2; boundary case from the kit |
| 06 | "3 pre-identified errors" | 22:00-36:00 | missing | published: chosen from `assets/kits/module06/flagged_candidates.csv` |
| 06 | Metric computation before and after | 36:00-48:00, studio step 4 | missing | published: `assets/kits/module06/qc_metrics.py` |
| 06 | 25 flagged candidates in a 50 µm subvolume | Studio scenario | missing | published: `flagged_candidates.csv`, `ground_truth.csv`, `kit.json`, `README.md` |
| 06 | 23 site paths | Page, kit, worksheet | resolves | kept |
| 07 | "12 pre-identified errors" | 10:00-24:00 | missing | published: rows `E01`-`E12` of the error report |
| 07 | "The practice dataset" for the correction sprint | 24:00-38:00 | missing | rewritten: fix on paper, apply with `qc_metrics.py` |
| 07 | Metrics before and after | 38:00-50:00 | missing | published: `qc_metrics.py` |
| 07 | Automated error report, 45 flags (18/20/7) | Studio step 1 | missing | published: `assets/kits/module07/error_report.csv`, `ground_truth.csv`, `kit.json`, `README.md` |
| 07 | "Provided metric computation script" | Studio step 4 | missing | published: `assets/kits/module07/qc_metrics.py` |
| 07 | Connectome Quality tool, "interactive metric computation and threshold visualization" | Teaching resources | resolves, but misdescribed (the page is static) | rewritten: "Metric definitions and where each one fails" |
| 07 | Slides PDF | Front matter `slides` | resolves | kept |
| 07 | 20 site paths | Page, kit, worksheet | resolves | kept |
| 08 | Four example hypotheses (two good, two poor) | 00:00-08:00 | missing | rewritten: written inline |
| 08 | Hypothesis template | 08:00-20:00 | inline | kept |
| 08 | "3 pre-computed results" | 34:00-46:00 | missing | rewritten: this module's worked example, Unit 09 section 2, the Algorithms and Applications worksheet |
| 08 | 20 site paths | Page, kit, worksheet | resolves | kept |
| 09 | NeuroM | Pre-class | learner (install) | kept; `morphometry.py` published as a no-install alternative |
| 09 | A segmented neuron to skeletonize | 10:00-24:00 | missing | rewritten: a MICrONS Explorer neuron, or `cell01.swc` from the kit |
| 09 | A skeleton with spurious branches | 10:00-24:00 | missing | published: `cell07.swc` |
| 09 | "Provided scripts" for five descriptors | 24:00-38:00 | missing | published: `assets/kits/module09/morphometry.py` |
| 09 | Skeletons for 10 L2/3 neurons | Studio scenario | missing | published: `skeletons/cell01.swc`-`cell10.swc`, `spines.csv`, `volume.json` |
| 09 | Synapse-based classification "(provided)" | Studio step 4 | missing | published: `synapse_labels.csv` |
| 09 | "The provided synapse table" | Worked example, step 5 | narrative | rewritten: "the synapse table" |
| 09 | 22 site paths | Page, kit, worksheet | resolves | kept |
| 10 | A synapse table for the live graph build | 08:00-20:00 | missing | published: `assets/kits/module10/edges.csv` |
| 10 | Connectivity graph of 500 neurons "from the MICrONS dataset" | Studio scenario | missing | published: `nodes.csv`, `edges.csv`; scenario now says synthetic stand-in |
| 10 | 21 site paths | Page, kit, worksheet | resolves | kept |
| 11 | Three EM synapses (spine, perisomatic, AIS) | 00:00-10:00 | instructor | kept |
| 11 | Three motifs "in the MICrONS dataset" with EM evidence | 10:00-24:00 | missing (no link) | linked: MICrONS Explorer; instructor locates them beforehand |
| 11 | Small subgraph, 15 neurons and 50 synapses | 24:00-38:00 | missing | published: `small_nodes.csv`, `small_synapses.csv` (exactly 15 and 50) |
| 11 | 200-neuron L2/3-L4 subgraph "from the MICrONS dataset" | Studio scenario | missing | published: `nodes.csv`, `synapses.csv` with compartment and Gray type; scenario now says synthetic stand-in |
| 11 | 21 site paths | Page, kit, worksheet | resolves | kept |
| 12 | "A supplied query" on a 0.1% sample, and its pre-joined version | 20:00-34:00 | missing | published: `assets/kits/module12/profile_join.py` |
| 12 | The learner's own query with runtime | Pre-class | learner | kept |
| 12 | Slides PDF | Front matter `slides` | resolves | kept |
| 12 | 27 site paths | Page, kit, worksheet | resolves | kept |
| 13 | "The supplied fragment set" | Pre-class | missing | published: `assets/kits/module13/fragments.csv`, `heldout_domain.csv` |
| 13 | 25 site paths | Page, kit, worksheet | resolves | kept |
| 14 | An EM subvolume with visible artifacts | Pre-class | learner (no link) | linked: Dataset Access |
| 14 | VI components, ERL and error counts for two models | 20:00-34:00 | missing | published: `assets/kits/module14/model_comparison.csv` (clean rows match the worked example) |
| 14 | Failure cases to classify by cause | 34:00-46:00, studio step 3 | missing | published: `failure_cases.csv`, `failure_cases_key.csv` |
| 14 | Model outputs and two ground-truth regions | Studio scenario | missing | published: per-region metrics and the case log; scenario reworded |
| 14 | 29 site paths | Page, kit, worksheet | resolves | kept |
| 15 | "Sample outputs" to score | 20:00-34:00 | missing (unspecified) | rewritten: generated live for the worked example's three output classes |
| 15 | The learner's own task | Pre-class | learner | kept |
| 15 | 21 site paths | Page, kit, worksheet | resolves | kept |
| 16 | Three good and three bad figures | Materials, 00:00-10:00 | instructor | kept (the page says how to prepare them) |
| 16 | Shared dataset: 20 x 30 matrix and one neuron mesh | Materials | missing | published: `assets/kits/module16/` (a 20 x 30 block of the matrix; a skeleton, since a Sholl plot needs one) |
| 16 | "Notebooks pre-loaded; Neuroglancer link ready" | Materials | missing | rewritten: learner-started notebook; MICrONS Explorer linked |
| 16 | Colorblind simulation tool | Materials | missing (no link) | linked: Coblis (200) |
| 16 | Critique rubric | Materials | missing | rewritten: the four questions in the 47:00-55:00 block |
| 16 | "The provided notebook" | 20:00-35:00 | missing | rewritten: learners load the kit files |
| 16 | 50 x 50 matrix, three example neurons, layer distributions | Studio scenario | missing | published: `celltype_synapses.csv`, `celltype_connections.csv`, `neurons/*.swc`, `neurons.csv`, `input_synapses_by_layer.csv`, `morphometry.py` |
| 16 | Slides PDF | Front matter `slides` | resolves | kept |
| 16 | 17 site paths | Page, kit, worksheet | resolves | kept |
| 17 | Mock figure set (three panels) with data tables | Materials, 08:00-18:00 | missing | rewritten: the learner's Module 16 package, or figures made from the Module 16 kit |
| 17 | Claim-evidence matrix template | Materials | missing | rewritten: the seven columns in studio task 2 |
| 17 | Methods reproducibility checklist | Materials | inline (Concept 5) | rewritten to point at Concept 5 |
| 17 | Two mock reviewer comments | Materials, 38:00-50:00 | inline | kept; materials line points to them |
| 17 | A deliberately incomplete methods section | 28:00-38:00 | instructor | rewritten: an example written inline |
| 17 | "The provided scenario" | Studio task 1 | inline | rewritten: "the scenario above" |
| 17 | 16 site paths | Page, kit, worksheet | resolves | kept |
| 18 | Noisy synapse table | Materials, 08:00-18:00 | missing | published: `assets/kits/module18/noisy_synapses.csv`, `cell_types.csv` |
| 18 | Segment table spanning five orders of magnitude | Materials | missing | published: `segments.csv` |
| 18 | Preprocessing decision sheet | Materials | missing | rewritten: the studio's five columns |
| 18 | QC dashboard template | Materials | missing | published: in the kit README |
| 18 | "The provided distributions" | 32:00-44:00 | missing | published: the kit |
| 18 | 18 site paths | Page, kit, worksheet | resolves | kept |
| 19 | Mock preprint with four seeded issues | Materials, 12:00-28:00 | missing | published: `assets/kits/module19/mock-preprint.md`, marked fictional |
| 19 | Structured review form | Materials | missing | published: `review-form.md` |
| 19 | Ethics-risk checklist | Materials, 28:00-38:00 | missing | published: in `review-form.md` |
| 19 | "Two examples of real reviewer comments" | Materials, 00:00-08:00 | missing, and cannot honestly be supplied as real | rewritten: two comments written for the session, labeled as such, in `review-form.md` |
| 19 | Connectomics review criteria | 08:00-12:00 | inline | kept |
| 19 | 17 site paths | Page, kit, worksheet | resolves | kept |
| 20 | Unit 09 section 2 reciprocity example | Pre-class, 06:00-18:00 | resolves | kept |
| 20 | 21 site paths | Page, kit, worksheet | resolves | kept |
| 21 | One real analysis walked through | Run-of-show | instructor (worked example on the page) | kept |
| 21 | 20 site paths | Page, kit, worksheet | resolves | kept |
| 22 | Two versions of an opener; the learner's own result or the inline scenario | Run-of-show, studio | inline | kept |
| 22 | 22 site paths | Page, kit, worksheet | resolves | kept |
| 23 | Learner's pitch, poster and follow-up template | Studio | learner | kept |
| 23 | 18 site paths | Page, kit, worksheet | resolves | kept |
| 24 | Learner's real targets and outreach drafts | Studio | learner | kept |
| 24 | 16 site paths | Page, kit, worksheet | resolves | kept |
| 25 | One strong and one weak portfolio | Run-of-show | instructor (worked example on the page) | kept |
| 25 | 22 site paths | Page, kit, worksheet | resolves | kept |

Front-matter `datasets` and `related_tools` paths on all 25 pages resolve. All 28
unique external URLs in the module pages were fetched with curl, including the five
added in this pass (Allen Brain Atlas, Coblis, MICrONS Explorer, its terms page, H01
Explore). Twenty-one returned 200 or 202. Six publisher pages (two at Science, the
Royal Society, COPE, ICMJE, Tufte) returned 403 and American Scientist returned 503.
Those are bot blocks on publisher sites, not dead links.

## Files created

| Path | What it is |
|---|---|
| `assets/kits/module03/` | Offline synapse table (3,000 rows, 76 with a blank post type), metadata, README |
| `assets/kits/module06/` | 25 flagged candidates, ground truth, `kit.json`, `qc_metrics.py` (copy), README |
| `assets/kits/module07/` | 45-flag error report, ground truth, `kit.json`, `qc_metrics.py` (hand-written), README |
| `assets/kits/module09/` | Ten SWC skeletons, spine table, synapse-based calls, volume bounds, `morphometry.py` (hand-written), README |
| `assets/kits/module10/` | 500-node, 11,388-edge column graph, README |
| `assets/kits/module11/` | 200-neuron, 2,979-synapse subgraph with compartments; 15-neuron, 50-synapse warm-up; README |
| `assets/kits/module12/` | `profile_join.py` (hand-written), README |
| `assets/kits/module13/` | 4,000 labeled fragments, 1,000 held-out-domain fragments, README |
| `assets/kits/module14/` | Metrics by model and region, 30 failure cases, key, README |
| `assets/kits/module16/` | 50 x 50 synapse and connection matrices, three SWC neurons, layer counts, `morphometry.py` (copy), README |
| `assets/kits/module18/` | 30,450-row noisy synapse table, 2,000 segments, cell-type labels, README with QC dashboard template |
| `assets/kits/module19/` | Fictional mock preprint, review form with ethics checklist and two invented comments, README with key |
| `assets/kits/manifest.json` | SHA-256 of all 61 kit files |
| `scripts/generate_kit_materials.rb` | Deterministic generator for every kit data file and README, and the manifest |
| `scripts/validate_kit_materials.rb` | The gate, wired into `.github/workflows/validate.yml` |

The Python scripts use the standard library only and were run on Python 3.14.
Kit size on disk is 2.4 MB.

## Instructor notes on what each kit plants

These are the answers the kits are built to produce. They live here, not on the site,
where they would be one click from the learner.

- **Module 06.** Eight true merges (five on analysis-set pyramidal cells), ten splits,
  four boundary errors, three non-errors among the `implausible morphology` rows. Baseline
  edge F1 0.827. Ranking by analysis-set membership and partner count reaches F1 0.935 with
  ten fixes and spends two of them on non-errors.
- **Module 07.** Baseline: edge precision 0.729, recall 0.833, F1 0.777; run-length proxy
  27.0 µm; 44 reciprocal pairs counted, 17 of them spurious, 13 real pairs hidden. An
  impact-first ranking (analysis-ROI pyramidal cells, merges before splits, larger
  synapse counts first) picks E06, E08, E11, E16, E24, E26, E31, E32, E35, E36, E37, E38,
  E39, E43, E45 and reaches F1 0.939, 42 pairs counted with 4 spurious; the oracle
  best is F1 0.951. Ranking by detector score reaches 0.799, and ranking by synapse count 0.882. The run-length proxy
  moves from 27.0 to 27.3 µm whatever is fixed, so it never passes the run-of-show's 30 µm
  threshold while F1 does. That disagreement is intended: the memo has to say which metric
  the reciprocal-connectivity question depends on.
- **Module 09.** `cell07` is the worked example's truncated pyramidal cell: soma 30 µm
  from the +x face, five of six dendrites cut, eight terminal branches under 2 µm, whole-cell
  spine density 0.61/µm (between the pyramidal cluster near 1.2 and the interneuron cluster
  near 0.03), 1.10/µm on its one uncut dendrite, and the shortest cable of the ten. Synapse
  call: excitatory, medium confidence. `cell05` is an interneuron with a merged spiny
  fragment: whole-cell density 0.29/µm, one dendrite at 0.88/µm against 0.03 or less on the
  others. Synapse call: inhibitory.
- **Module 10.** Node 20432 has `soma_count` 2: two basket cells more than 300 µm apart,
  fused. Degree 194 against 117 for the runner-up. Connection probability falls off with
  soma distance (150 µm), so a degree-preserving null leaves spatial structure in place.
- **Module 11.** Basket-type cells put most synapses on the soma or proximal dendrite;
  Martinotti-type cells put most on distal dendrites. E to I to E loop enrichment against a
  degree-preserving null comes from type composition and distance, not a loop rule.
- **Module 13.** A 1-nearest-neighbor check on the eight morphological features gave
  0.77 accuracy on a random split and 0.68 grouped by parent (0.82 and 0.70 with
  `mean_intensity` added), and 0.72 on the held-out domain, where smooth dendrites fall to
  0.32. Learners' models will differ; the ordering should not.
- **Module 14.** Causes are in `failure_cases_key.csv`. Clean-region metrics equal the
  worked example; break-even r = 5 there. In the artifact region model B's merge count is
  more than three times A's.
- **Module 18.** 30,450 rows. Planted: 450 duplicated rows (447 still exact duplicates),
  90 autapses (115 in total with chance ones), 300 presynaptic IDs not in the segment
  table, 14% blank cell types, a third of segments under 1 µm³ (range 0.01 to about
  1,600 µm³), and boundary-touching neurons. Cleft scores are bimodal around 35 and 140.
- **Module 19.** The key is in the kit README (see owner decisions).

## Module 07 changes, for reconciling the model answers

Task steps and their order are unchanged. Five lines in `modules/module07.md` changed,
plus one resource line added:

1. Studio step 1: "Review the automated error report: 45 flagged errors (18 merges, 20
   splits, 7 uncertain)." became "Review the automated error report in the [Module 07
   kit](/assets/kits/module07/README.md) (synthetic): 45 flagged errors (18 merges, 20
   splits, 7 uncertain)."
2. Studio step 4: "Compute before/after metrics (provided metric computation script)."
   became "Compute before/after metrics (metric computation script: `qc_metrics.py` in
   the [Module 07 kit](/assets/kits/module07/README.md))."
3. Run-of-show 10:00-24:00: "Present 12 pre-identified errors with brief descriptions."
   became "Present 12 errors with brief descriptions (rows `E01` to `E12` of the error
   report in the Module 07 kit)."
4. Run-of-show 24:00-38:00: "Learners fix their top 5 errors in the practice dataset."
   became "Learners fix their top 5 errors on paper and apply them with the kit's
   `qc_metrics.py`."
5. Run-of-show 38:00-50:00: "Compute metrics before and after the correction sprint."
   gained "with `qc_metrics.py`".
6. Teaching resources: the Connectome Quality tool is now described as "Metric
   definitions and where each one fails" (it was described as interactive, which it is
   not), and a Module 07 kit line was added.

Only items 1 and 2 reach the worksheet and session kit. The scenario, the triage
guidance, the time budget, the outputs and the rubric are unchanged. The kit's
numbers are in the instructor notes above.

## Owner decisions

1. **Modules 17 and 18 attribute specific numbers to real data.** Module 17's scenario
   says "MICrONS minnie65 data, CAVE materialization v795 ... 1,247 reciprocal pairs ...
   2.1x", and Module 18's says "MICrONS minnie65 (CAVE materialization v795) containing a
   synapse table (4.2 million rows)". Neither was checked against a release. *Resolved
   26 September:* both scenarios and the Module 17 example paragraph now say
   "illustrative figures, not measured from a MICrONS release". The numbers and Module
   18's task steps are unchanged, because its model answers use them.
2. **Module 04 Patch D (CA3 mossy fiber bouton).** No public volume the site links covers
   hippocampus, so the patch is now described from the worked example. Either source
   hippocampal EM, or drop Patch D from the guided round.
3. **Publish a curated EM patch set?** Modules 04 and 05 now ask the instructor to build
   a patch set from MICrONS or H01. A curated screenshot set under `assets/kits/`, with
   coordinates and credit lines, would make both self-contained. H01 is CC BY 4.0. MICrONS
   has its own terms, which someone should read before redistribution.
4. **Keys on the public site.** `ground_truth.csv` (Modules 06, 07),
   `failure_cases_key.csv` (14) and the Module 19 README key are published beside the
   learner files. Item 3 of the plan says public formative keys should stay distinct from
   secure material. If these kits will be graded, move the keys off the site.
5. **A fictional preprint about a real dataset.** Module 19's mock preprint claims an
   invented result on MICrONS minnie65 v661, as the studio scenario already did. It is
   marked fictional in its first lines, and the scenario no longer names the MICrONS
   Consortium as a co-author (it now says "a data consortium"). Confirm that this is
   acceptable.
6. **Instructor-prepared items left as they are.** Module 01 (three example
   hypotheses), 11 (three EM synapses), 16 (six example figures), 21 and 25 (walk-throughs)
   remain instructor-prepared, each supported by a worked example on its page. The gate
   accepts these because none is described as supplied.
