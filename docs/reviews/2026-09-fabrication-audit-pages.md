# Fabrication audit: teaching, training, library and notebook pages

*Audited 26 September 2026 on branch `compass-workshops` (base `0c7ceba`). Companion to
[2026-09-fabrication-audit-modules.md](2026-09-fabrication-audit-modules.md), which
covers `modules/`, `assets/kits/`, `assets/worksheets/moduleNN/`, `teaching/sessions/`
and `course/decks/`. Nothing was committed.*

**Scope:** `teaching/**` except `teaching/sessions/` (pathways, lectures, answers,
assessment, syllabi, sequence, index, facilitator guide, Module 22 companion,
projectome-to-synapse), `technical-training/*.md` (not the slide decks),
`content-library/**`, `hidden-curriculum/**`, `notebooks/**`, `models.md`, `tracks/`,
`core/`, `start-here.md`, `avatars/` and `assets/worksheets/lectures/*.py`.

## The rule

Nothing fabricated. No invented number, result, finding, quote, preprint or claim may be
attributed to a real dataset, real release or materialization version, real paper, lab,
person, organization or tool. An "illustrative" label is not enough. Teaching scenarios
may use invented data only when it is labeled synthetic **and** detached from real
names. Fictional releases use a "T" prefix that cannot be mistaken for a MICrONS
materialization (real versions include 117, 343, 661, 795, 943, 1078, 1181, 1300, 1412
and 1507). Fictional volumes are called, for example, "a fictional mouse cortex volume".
Real-world facts must be sourced. If a claim could not be verified against a primary
source, it was softened or removed.

## Method

1. Grepped the scope for `MICrONS|minnie|H01|FlyWire|FAFB|hemibrain|BossDB|CAVE|neuPrint|Allen|Janelia|materialization|preprint|et al.`,
   for version-like numbers (`v[0-9]{3,4}` and each real MICrONS version), and for
   percentages or fold changes on the same line as a dataset name. Then read the
   context of each hit.
2. Read every worked example, scenario and "check yourself" section in the technical
   units and the content library.
3. Sorted each hit into one of four categories:
   - (a) a real, sourced fact;
   - (b) a procedure or template that names a real version or table without reporting
     results;
   - (c) invented values attached to real names;
   - (d) a real-world claim that is unverifiable or wrong.

   Categories (a) and (b) were left alone once the version and table names were
   confirmed real. Categories (c) and (d) were fixed.
4. Checked real-world claims against primary sources: papers (publisher pages, PMC and
   Europe PMC full text, PubMed, Crossref), the MICrONS tutorial and static-export pages,
   the MICrONS public static CSV exports, NIH RePORTER, and press releases where the
   paper itself is silent.
5. The content library was split across four parallel audit passes: case studies,
   proofreading and infrastructure, neuroanatomy with cell types and imaging, and
   connectomics with journal papers. Their rows are summarized below.

Fictional release labels used in this pass are T12, T18, T31, T32, T41, T43, T795 and
T802. None collides with a label used on the modules side. There, Module 18 is T18 and
this page's Module 18 answer key matches it.

## Findings and fixes

### Teaching, training, hidden curriculum, notebooks, other pages

| File | Line/context | Cat | Fix |
|---|---|---|---|
| teaching/pathways/communicating-science-1-activity.md | Rosa's notebook result (2.7×, 2.1×, 58 neurons, 1,904 synapses) at "materialization version 1078" in "mouse visual cortex" | c | Now "a fictional mouse cortex volume ... release T12". The case note says the volume and release are fictional. Numbers are unchanged. |
| teaching/pathways/communicating-science-1-answers.md | Invariants "materialization version 1078"; peer register "materialization v1078" | c | "one fictional mouse cortex volume, layer 2/3, release T12"; "(release T12)" |
| teaching/pathways/communicating-science-2-activity.md | Talk summary "at materialization version 1078" | c | "from a fictional mouse cortex volume at release T12" |
| teaching/pathways/communicating-science-2-answers.md | Model answer "Mine is version 1078"; outline "v1078" | c | "Mine is release T12"; "One fictional mouse cortex volume, layer 2/3, release T12". All arithmetic (2.7, 2.1, 58) is unchanged. |
| teaching/answers/module18.md | Scenario figures "not measurements from a MICrONS release"; release note "cited as its stated materialization" | c | Matches Module 18's new scenario: "a fictional mouse cortex volume, release T18"; "cited as release T18 of the fictional volume". Kit-derived values are unchanged. |
| technical-training/04-volume-reconstruction-infrastructure.md | Worked example: invented 1,412 vs 1,530 inputs, pinned to "materializations 795 and 802" (795 is real) | c | T795 and T802, labeled fictional for this invented case. This matches the Unit 04 deck edit on the modules side. |
| hidden-curriculum/lab-norms.md | Bad-news script: counts "computed against materialization version 943, but the cell list came from 917" | c | T43 and T41 |
| hidden-curriculum/lab-norms.md | "FlyWire whole-brain connectome credited its 287 proofreaders as co-authors" | d | Dorkenwald et al. 2024 lists "The FlyWire Consortium" as an author, and its members "contributed proofreading and annotations" (PMC11446842). The number 287 is not in the paper; it comes from the Cambridge press release and counts researchers, not proofreaders. The sentence now states the verified form. |
| content-library/connectomics/motif-analysis.md | Worked example: "Query MICrONS minnie65 at materialization version 943 ... 2,847 reciprocal pairs", nulls, z-scores; "Consistent with Song et al. (2005) and Perin et al. (2011)" | c | Labeled synthetic, from a fictional mouse cortex volume at release T31, with a note on how to pin a real version. Song 2005 is now cited only for what it reports (bidirectional connections over-represented in rat layer 5 paired recordings), with "synthetic numbers replicate nothing". Perin removed. Arithmetic is unchanged. |
| content-library/infrastructure/provenance-and-versioning.md | Methods-text template: "4.2× enriched" result; "version 943 (2025-01-15)"; cell types "from the minnie65_public nucleus detection table" | c/d | The result number was removed and the sentences are labeled wording templates. The date was wrong: v943 is January 2024 (MICrONS tutorial release table). Cell-type labels now come from `aibs_metamodel_celltypes_v661`, since the nucleus table does not carry cell types. `synapses_pni_2` and `minnie65_public` are confirmed real (MICrONS tutorial). |
| content-library/infrastructure/provenance-and-versioning.md | Opening scenario (3.2× vs 1.8×) tied to real mouse visual cortex dates | c | The proofreading/infrastructure pass changed it to a fictional release. It was then renamed T32 to avoid colliding with the Communicating Science T12. |
| content-library/cell-types/neuron-type-identification.md | "Turner et al. (2022) classified neurons ... using spine density, axonal projection pattern, calcium responses" | d | Turner 2022 did not do this. Replaced with Elabbady et al. 2025 (perisomatic features) and Schneider-Mizell et al. 2025 (inhibitory targeting, 1,352-cell column), both verified, and added to the references. |
| content-library/cell-types/neuron-type-identification.md | Layer 2/3 worked example: ~200 excitatory and ~50 inhibitory inputs, ~300 outputs, unlabeled | c | Labeled as invented counts for a truncated cell. The label notes that a complete cell receives thousands of synapses. |
| content-library/cell-types/glia-recognition.md | "In MICrONS, glia-neuron merges are ~5-10% of all merge errors (Turner et al. 2022)" | d | Not in Turner 2022, and no source was found. The page now says no published share is known and quotes none. |
| content-library/connectomics/neuroai-bridge.md | "MICrONS (Turner et al. 2022): similar orientation tuning more likely connected ... explains ~5-10% of variance" | d | Reattributed to Ding et al. 2025 (*Nature* 640:459-469, like-to-like connectivity across layers and areas). The variance figure was removed. Reference added. |
| content-library/connectomics/neuroai-bridge.md | "reproduce some locomotion patterns (Izquierdo & Beer 2016)" | d | Izquierdo & Beer 2016 is a review, so this now reads "(reviewed in Izquierdo & Beer 2016)". Full reference added. |
| content-library/journal-papers/case-studies.md | FlyWire "generated through FFN segmentation" | d | FlyWire used its own convolutional-network segmentation (Dorkenwald 2022). Now says "convolutional-network segmentation". |
| models.md | "Cervantes, C. et al. (2022). CIRCUIT: A framework for inclusive and equitable STEM mentorship. *Cell* 185(15):2620-2624" | d | This reference does not exist: there is no PubMed entry at that citation and no Crossref match. It was replaced with the real paper, Cervantes, Floryanzia, Sharp, Gray-Roncal & Johnson, "Empowering trailblazers toward scalable, systematized, research-based workforce development", ASEE Annual Conference proceedings (2023 per Crossref), doi:10.18260/1-2--43271. |
| notebooks/connectome-quality/index.md | `root_id = 864691135474648896  # any proofread neuron` | d | This ID is not in the v1507 public proofreading table and could not be checked at v1300, so the "proofread" claim was unverifiable. Replaced with a query that picks a neuron with a proofread axon from `proofreading_status_and_strategy` at the pinned version. The table and column names are from the MICrONS tutorial. |

### Content library, delegated passes (summary)

Most rows are (d): real papers or datasets credited with numbers or methods they do not
report.

| Area | Files changed | Main fixes |
|---|---|---|
| Case studies | h01-pipeline, h01-human-cortex, microns-visual-cortex, flywire-whole-brain, c-elegans-revisited, mouseconnects-himc | **(c)** Invented cell and neuron counts, "findings" and layer claims were replaced with the papers' own numbers:<br>• H01: 57,180 cells, 16,087 neurons, 149,871,669 synapses, 104 proofread.<br>• MICrONS: >200,000 cells, 523M synapses.<br>• FlyWire: 1,303 descending and 2,362 ascending neurons.<br>• C. elegans: about 5,000 chemical synapses and 600 gap junctions (White 1986).<br>**(d)** Fixes to methods and attributions:<br>• Corrected imaging and segmentation methods: MICrONS used GridTape plus TEM with affinity-CNN segmentation, not ATUM plus mSEM with FFN. FlyWire did not use FFN.<br>• The like-to-like finding is reattributed from Turner 2022 to Ding 2025.<br>• "Quotes" were replaced with verbatim *Science* text.<br>• "287 proofreaders, all co-authors" is attributed to the Cambridge release.<br>• The H01 corrected E/I estimate is set to the published *Science* values (102.5M / 50.3M).<br>• The MouseConnects PI is corrected, and its milestones are labeled illustrative. |
| Proofreading and infrastructure | error-taxonomy, metrics-and-qa, proofreading-strategies, proofreading-tools, worked-examples, data-formats, provenance-and-versioning, reconstruction-pipeline | **(c)** Removed a table of VI, ERL and F1 values invented for FlyWire, MICrONS, hemibrain and CREMI. The "MICrONS dataset" merge-split example is now a fictional volume. Worked examples are no longer called "drawn from real-world projects".<br>**(d)** Corrections:<br>• Lee 2017 (not 2019), with ERL credited to Januszewski 2018.<br>• The ERL example is recomputed to the published definition.<br>• EyeWire player count is now about 120,000.<br>• Tool and feature claims for Spelunker and NeuTu are corrected, along with the CAVE year (2025).<br>• A 100× voxel-count error is fixed (1 mm³ at 4×4×40 nm is ~1.6×10^15 voxels).<br>• H01 raw data is 1.8 PB (1.4 PB aligned).<br>• FAIR "R" means Reusable.<br>• The Docker pin `caveclient==5.15.0` does not exist on PyPI and is now 5.14.0.<br>• Unsupported citations were removed from the worked examples.<br>• The autapse rarity claim is corrected (Tamás et al. 1997). |
| Neuroanatomy, cell types, imaging | axon-biology, synapse-classification, dendrite-biology, organelle-cues, soma-ultrastructure, neuron-type-identification (reference only), em-principles, tissue-preparation, artifact-taxonomy, acquisition-qa | **(c)** Unattributed "real examples" in acquisition QA are relabeled as composite scenarios, and their numbers were removed.<br>**(d)** Corrections:<br>• Percentages credited to Shepherd & Harris 1998, Harris 1992 and Spacek & Harris 1997 are replaced with what those abstracts report.<br>• Wrong ATUM, rOTO and multibeam attributions are fixed (ATUM is Hayworth 2006; MICrONS used TEM, FAFB used TEMCA2, H01 used ATUM with mSEM).<br>• The Xu et al. reference is fixed (it had pointed to the BonVision paper).<br>• H01 lipofuscin and fixation claims now match the paper.<br>• Missing references were added. |
| Connectomics and journal papers | connectome-history, network-analysis-methods, motif-analysis, neuroai-bridge, open-problems-undergrad; 12 journal-papers pages | **(d)** Paper counts, volumes and years are fixed across connectome-history, including White 1986, Takemura 2013, Motta 2019, MICrONS and Hayworth 2014 ATUM.<br>C. elegans graph statistics are now from Watts & Strogatz (C = 0.28 vs 0.05).<br>Two paraphrases presented as Bargmann & Marder quotes are unquoted.<br>Song 2005 is now described as layer 5 of rat visual cortex.<br>In open-problems-undergrad:<br>• The male CNS numbers match Berg et al. 2025.<br>• The MFAS record is updated and the claim about who set it removed.<br>• The fly functional-connectomics work is reattributed to Currier & Clandinin 2025, not MICrONS.<br>• ZAPBench is credited to Immer et al.<br>Journal-paper summaries were corrected against their abstracts, for example Kasthuri's pages and volume, H01's title and "1 mm³, not 1 cm³", FAFB imaged by TEMCA2 rather than ATUM, and invented Cook 2019 and Witvliet 2021 findings replaced. |

### Checked and left alone (a/b)

- `notebooks/microns-lab/`: every number in "Expected outputs" matches the archived
  outputs in `assets/notebooks/microns-lab/` (`results_summary.json`, CSVs,
  `methods_record.json`). The only exception is 201, which is the 200 null samples plus
  one. File sizes and hashes match the methods record. Two statements were verified on
  the MICrONS versioning page: v117, v943 and v1300 are the non-expiring "major
  versions", and v1507 is scheduled to expire. The ~20 GB full synapse export was
  verified on the static-repositories page.
- `teaching/syllabi/*`: v1412 and v1507 refer to the real-data lab, so they are real and
  sourced.
- `teaching/lectures/*-activity.md`, `*-answers.md`,
  `assets/worksheets/lectures/*.py`: all data is labeled invented or synthetic and
  named `snapshot-a` and `snapshot-b`, with no real dataset names. The ethics-lecture
  licence facts and the person-year figures (FlyWire about 33, hemibrain 50) match
  Dorkenwald 2024.
- `teaching/assessment/*`: all items use unnamed, hypothetical volumes.
- `technical-training/*` worked examples and "check yourself" items: none attach
  numbers to a real dataset, other than the Unit 04 case fixed above. The Unit 07
  caption "H01's myelin mask covers 13.4% of the field" is computed by
  `scripts/render_em_figures.py` from the public volume. The H01 E/I classifier accuracy
  (84.98% and 86.89%) matches the paper.
- `teaching/pathways/*`: invented people (Rosa, Sam, and Drs. Kimura, Halvorsen,
  Adeyemi, Brennan and others) carry no real affiliations. None is the surname of a
  prominent connectomics PI.
- `core/connects-ecosystem.md` and `teaching/projectome-to-synapse.md`: the IC3 and APEX
  roles match NIH RePORTER and grantee descriptions.
- `start-here.md`: the Kasthuri card had said "Mouse visual cortex" (Kasthuri 2015 is
  somatosensory cortex). The parallel modules and site pass had already rewritten the
  card when this pass reached it.

## Needs an owner decision

1. **FlyWire "287" in Module 02.** The only primary source for "287 researchers in more
   than 76 labs" is the University of Cambridge release of 2 October 2024. The number is
   not in the *Nature* paper. The FlyWire case study now cites the release. Module 02
   (the other agent's scope) should cite it too, or drop the number.
2. **H01 corrected E/I estimate.** The preprint and PMC manuscript give 111.6M / 70.7M;
   the published *Science* version gives 102.5M / 50.3M. The site now uses the published
   figures throughout.
3. **H01 spine-detachment figures** (32.2% c2 / 33.7% c3) in `h01-pipeline.md` were
   found in neither the paper nor the preprint. They may be in the *Science* supplement.
   They were left in; verify or remove them.
4. **Berg et al. male CNS** is cited as the bioRxiv preprint. A *Cell* 2026 version may
   exist.
5. **FlyWire front-matter tags** `methodology:flood-filling-networks` are now inaccurate.
   They were left alone because tags may drive the site taxonomy.
6. **Unverified, left in:** the MICrONS "Spelunker" proofreading claim; the Billeh 2020
   "reproduced orientation selectivity..." summary; the EyeWire consensus bullet;
   Kasthuri's "~1,500 µm³" in `proofreading-strategies.md`; general unsourced textbook
   figures (symmetric synapses "15-20%", calyx "~600 active zones", "5-10 minutes of
   ischemia"); and the microns-lab claim that v1507 is the only version whose static
   export includes the proofread-axon synapse table.
7. **`models.md` CIRCUIT citation.** The fabricated *Cell* reference was replaced with
   the real ASEE paper. Confirm that this paper is the one intended.

## Validation

`ruby scripts/validate_frontmatter.rb`: no problems found.
`ruby scripts/validate_code_span_paths.rb`: every site path resolves.
