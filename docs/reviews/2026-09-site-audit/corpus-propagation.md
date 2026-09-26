# Corpus propagation (September 2026 site audit, follow-up to journal-papers.md)

Date: 2026-09-26. Follows the "Outside my area" list in
[journal-papers.md](journal-papers.md). Source for every value: the corrected
`_data/journal_papers.yml` (for authors, titles, venues and the text that names them) and the Crossref
REST API (`api.crossref.org/works/<doi>`, for years; responses cached during the audit, fetched
2026-09-18 to 2026-09-26; the 9 missing records were fetched again today).

## Summary counts

| What | Count |
|---|---|
| `journal_papers.yml` records changed by the audit (HEAD vs working tree, keyed by DOI) | 97 |
| Corpus records edited to match them | 93 (the other 4 were title-only fixes; the corpus titles were already correct) |
| Field edits per corpus copy (`corpus_2000`) | 186: `authors` 53, `ocar.action` 53, `venue` 40, `summaries.intermediate` 40 |
| Field edits in `corpus_1000` / `corpus_500` | 117 / 60 (same records, restricted to each tier) |
| Corpus years corrected against Crossref | **117** (95 off by 1, 15 by 2, 2 by 3, 1 by 4, 3 by 5, 1 by 6; 109 moved later, 8 earlier) |
| Years left alone | 2 ASEE proceedings DOIs with no published/issued date in Crossref (`10.18260/1-2--43271`, `10.18260/1-2--42544`); 9 DOIs not in Crossref (arXiv/DataCite, `10.1109/tmi.2024.3400276`) were not checked |
| `journal_papers.yml` records changed by the derive re-run | 117 (`year`, `citation`; `inclusion_role`/`reading_phase` on 28) |
| Era counts (history / contemporary / recent) | 944 / 640 / 416 before, 933 / 637 / 430 after |
| Files touched | `_data/corpus_{500,1000,2000}.json`, `data/corpus_{500,1000,2000}.json` (byte-identical to `_data/`), `_data/journal_papers.yml`, `_data/paper_views/{era,year,tier,dimension}.json`, `scripts/derive_journal_papers.py`, `scripts/corpus_curation/{sync_all_paper_views,export_to_site}.py`, `technical-training/journal-club/graph-data.json`, `_includes/cards/journal-paper-card.html`, `assets/css/site-styles.css` |

## 1. How the derive script maps fields

`scripts/derive_journal_papers.py` joins `journal_papers.yml` to `_data/corpus_2000.json` on DOI and
rewrites `authors` (corpus `authors`), `year` (`year`), `journal` (`venue`), `inclusion_role` and
`reading_phase` (from the year), `citation` (built from corpus authors, year and venue plus the **yml**
title), and `abstract` (`abstract`). It does not touch `title`, `ocar`, `summaries` or
`plain_language_summary`, and it rebuilds `paper_views/era.json` and `year.json`. It calls no other
script.

Before this pass a dry run reported `authors=53, journal=40`: re-running it would have reverted those
93 records. The audit's yml edits also changed text the script does not own (`ocar.action` in 53 records;
`plain_language_summary` = `summaries.intermediate` in 40, which name the venue), so those were copied
to the corpus too, keeping the corpus the single consistent source.

## 2. Author, title and venue propagation

For each of the 97 DOIs, every field that differs between `git show HEAD:_data/journal_papers.yml` and
the working copy was copied into the corpus after checking that the corpus still held the old (HEAD)
value. All three tier files hold identical records for shared DOIs, so the same edit went to each; the
`data/` download copies were rewritten from the `_data/` files and are byte-identical. Formatting is
unchanged (`json.dumps(indent=2)`, ASCII escapes, no trailing newline); the script asserted that the
original text round-tripped before writing, and a sampled `git diff` shows value-only line changes.

## 3. Year corrections

Rule: keep the corpus year if it equals the year of any of Crossref `published-print`,
`published-online`, `issued` or `published`; otherwise replace it with `published-print`, else
`published-online`, else `issued`. 79 corrections came from `published-print`, 32 from
`published-online`, 6 from `issued`. Most are a preprint year on a journal DOI.

Each corpus record's `ocar.action` and `summaries.intermediate` contain the year once as "(YYYY)";
that token was updated too (and the same token in the yml's `ocar.action`, `plain_language_summary` and
`summaries.intermediate`, 351 lines), so the card text does not contradict the year field.

Items worth a human look, because the rule picked the journal date and the record is the journal DOI:

- `10.7554/elife.99693` (Isbister et al., eLife): 2024 → 2026. Crossref's published-online and
  issued dates are 2026; the DOI record was created in 2024, which suggests the corpus year came from an
  earlier reviewed-preprint version.
- `10.1038/s41593-022-01219-x`: 2021 → 2023 (print 2023, online 2022).
- `10.1101/2022.07.18.500521` (NeuVue) and `10.1101/2022.07.20.499976`: bioRxiv posted 2022, corpus
  said 2026 and 2024.

## 4. Derive re-run

After steps 2 and 3, the derive script was first run in a scratch copy of the repo and its output diffed
against the pre-run yml: the only changed keys were `year` (117), `citation` (117, year only),
`inclusion_role` and `reading_phase` (28), plus `era.json`/`year.json`. It was then run in place; the
result is byte-identical to the scratch run, and a second `--dry-run` reports no changes. Compared with
the yml as the audit left it, every difference is explained by the year change (0 unexplained
differences across all fields, checked in code).

## 5. `graph-data.json` organisms

`technical-training/journal-club/graph-data.json` (a Liquid template) set `organism` to the whole `tags`
list, so `none`, the domain and `tier_500` appeared as organisms. Tags are always
`[organism…, dimension, tier_N]`; the template now takes the tags before the dimension and tier tags and
keeps only `fly, mouse, elegans, human, rat, macaque, zebrafish, other`, else `["unspecified"]`.
Rendered with Jekyll 3.10 (repo Gemfile) against the real yml: all 2,000 records equal the corpus
`organism` field with `none` → `unspecified` (1,092 unspecified, 367 fly, 238 mouse, 126 elegans, 104
human, 61 other, 59 rat, 33 macaque, 13 zebrafish). This includes the one paper whose organism and
domain are both `other`.

## 6. Journal paper card

`_includes/cards/journal-paper-card.html` now shows, above the OCAR block: "Domain-level notes: the OCAR
steps and summaries below are written per research domain and shared by every paper in it, with this
paper's title, authors or venue filled in. Read the paper's abstract (DOI link) for what it found."
The collapsible "🔬 Analysis Protocol & Ecosystem" block is renamed "Domain, tier and domain-level
notes", and its labels "Methodological Action / Empirical Resolution / Open Horizons" are now "Action /
Resolution (typical for the domain) / Future work (typical for the domain)", matching the prompt-builder
wording. One CSS rule (`.jc-ocar-note`) added.

## 7. View labels

| File | Before | After | Generator |
|---|---|---|---|
| `tier.json` | Top 500 Core Flagships; Top 1,000 Landmark Corpus; Top 2,000 Comprehensive Network (and "landmark / high-impact / complete" descriptions) | Top 500; Top 1,000; Top 2,000 ("The 500 top-ranked papers; contained in the Top 1,000 and Top 2,000", "The 1,000 top-ranked papers; includes the Top 500", "All 2,000 papers in the corpus") | `sync_all_paper_views.py` |
| `era.json` | History & Classics (≤2018); Contemporary Surge (2019-2023); State of the Art (2024-2026+) | History (2018 and earlier); Contemporary (2019-2023); Recent (2024 onward) | `derive_journal_papers.py`, `sync_all_paper_views.py` |
| `dimension.json` | Behaviour & Circuit Dynamics | Behavior & Circuit Dynamics (key `behaviour` unchanged) | `sync_all_paper_views.py` |

The obsolete `export_to_site.py` (older schema, not the source of the current files) got the same tier
and era wording. `sync_all_paper_views.py` was run into a scratch directory: `tier.json` and
`dimension.json` differ from the committed files only in the strings above, and were copied in.
Its `era.json` and `year.json` are **wrong** (built from the stale years in `final_selection.json`), so
they were not used; a caution to that effect is now in the script's docstring. `organism.json`,
`kcore.json` and `manifest.json` came out identical.

## Checks

`validate_frontmatter`, `validate_paper_counts` ("95 authored across 11 dimensions, 2000 in corpus"),
`validate_code_span_paths` and `validate_toggled_classes` all pass. The four edited view files pass
`python3 -m json.tool`; all six corpus files `json.load`; `YAML.load_file("_data/journal_papers.yml")`
parses 2,000 records.

## Unresolved

- The corpus `metadata.description` strings still say "complete 5-part OCAR research cards" and
  "5,460+" (the exact count is 5,460); not changed here.
- `scripts/corpus_curation/final_selection.json` and `scripts/journal_papers_v2_staging.yml` still carry
  the old authors, venues and years. Anything regenerated from them (`sync_all_paper_views.py` era/year,
  `generate_journal_papers_yml.py`) would reintroduce errors.
- Owner decisions 2–4 in journal-papers.md (off-scope and mismatched-DOI records, including
  `10.18260/1-2--42544`) are unchanged.
- Years for the 9 non-Crossref DOIs and the 2 undated ASEE DOIs were not verified.
- Hand-written topic pages were not rechecked for the corrected years (the audit had already cited
  those papers from Crossref).

## Year-correction log (117)

Sorted by size of the correction.

| DOI | Title | Corpus year | Crossref year | Crossref field used |
|---|---|---|---|---|
| `10.1093/cercor/bhae405` | Reconciliation of weak pairwise spike–train correlations and highly... | 2018 | 2024 | published-print |
| `10.1093/cercor/bhaf073` | Information transfer and recovery for the sense of touch | 2020 | 2025 | published-print |
| `10.1145/3065386` | ImageNet classification with deep convolutional neural networks | 2012 | 2017 | published-print |
| `10.3389/fcomp.2021.613981` | FusionNet: A Deep Fully Residual Convolutional Neural Network for I... | 2016 | 2021 | published-online |
| `10.1101/2022.07.18.500521` | NeuVue: A scalable and customizable framework for electron microsco... | 2026 | 2022 | issued |
| `10.7554/elife.66135` | Decoding locomotion from population neural activity in moving C. el... | 2018 | 2021 | published-online |
| `10.7554/elife.85300` | Homophilic wiring principles underpin neuronal network topology in ... | 2022 | 2025 | published-online |
| `10.1038/s41467-024-44851-w` | A presynaptic source drives differing levels of surround suppressio... | 2022 | 2024 | published-online |
| `10.1038/s41467-025-59635-z` | Cadherins orchestrate specific patterns of perisomatic inhibition o... | 2023 | 2025 | published-online |
| `10.1038/s41586-020-03134-2` | Structure and function of a neocortical synapse | 2019 | 2021 | published-print |
| `10.1038/s41586-023-07006-3` | Converting an allocentric goal into an egocentric steering signal | 2022 | 2024 | published-print |
| `10.1038/s41586-024-07088-7` | Synaptic wiring motifs in posterior parietal cortex support decisio... | 2022 | 2024 | published-print |
| `10.1038/s41592-024-02226-5` | RoboEM: automated 3D flight tracing for synaptic-resolution connect... | 2022 | 2024 | published-print |
| `10.1038/s41592-024-02580-4` | Segment Anything for Microscopy | 2023 | 2025 | published-print |
| `10.1038/s41593-020-00776-3` | Targeted photostimulation uncovers circuit motifs supporting short-... | 2019 | 2021 | published-print |
| `10.1038/s41593-022-01219-x` | A whole-brain monosynaptic input connectome to neuron classes in mo... | 2021 | 2023 | published-print |
| `10.1101/2022.07.20.499976` | Perisomatic Features Enable Efficient and Dataset Wide Cell-Type Cl... | 2024 | 2022 | issued |
| `10.1109/tmi.2021.3097826` | Learning and Segmenting Dense Voxel Embeddings for 3D Neuron Recons... | 2019 | 2021 | published-print |
| `10.1371/journal.pcbi.1001066` | Structural Properties of the Caenorhabditis elegans Neuronal Network | 2009 | 2011 | published-online |
| `10.1371/journal.pcbi.1006781` | Leveraging heterogeneity for neural computation with fading memory ... | 2017 | 2019 | published-online |
| `10.7554/elife.68848` | Corollary discharge promotes a sustained motor state in a neural ci... | 2019 | 2021 | published-online |
| `10.7554/elife.99693` | Modeling and simulation of neocortical micro- and mesocircuitry (Pa... | 2024 | 2026 | published-online |
| `10.1002/cne.24866` | The brain of a nocturnal migratory insect, the Australian Bogong moth | 2019 | 2020 | published-print |
| `10.1002/cne.25294` | The lateral posterior clock neurons of Drosophila melanogaster expr... | 2021 | 2022 | published-print |
| `10.1002/hipo.20768` | Coordination of size and number of excitatory and inhibitory synaps... | 2010 | 2011 | published-print |
| `10.1007/s12021-020-09461-z` | A Systematic Evaluation of Interneuron Morphology Representations f... | 2019 | 2020 | published-print |
| `10.1016/j.biopsych.2019.11.009` | Reconciling Dimensional and Categorical Models of Autism Heterogene... | 2019 | 2020 | published-print |
| `10.1016/j.cell.2020.11.048` | A circuit logic for sexually shared and dimorphic aggressive behavi... | 2020 | 2021 | published-print |
| `10.1016/j.cell.2020.12.012` | NeuroPAL: A Multicolor Atlas for Whole-Brain Neuronal Identificatio... | 2020 | 2021 | published-print |
| `10.1016/j.cell.2024.11.037` | Configuration of electrical synapses filter sensory information to ... | 2024 | 2025 | published-print |
| `10.1016/j.cell.2025.11.040` | Neuronal calcium spikes enable vector inversion in the Drosophila b... | 2025 | 2026 | published-print |
| `10.1016/j.celrep.2024.115088` | Contextual modulation emerges by integrating feedforward and feedba... | 2024 | 2025 | published-print |
| `10.1016/j.conb.2011.10.019` | Nanoscale analysis of structural synaptic plasticity | 2011 | 2012 | published-print |
| `10.1016/j.conb.2017.12.002` | Do the right thing: neural network mechanisms of memory formation, ... | 2017 | 2018 | published-print |
| `10.1016/j.conb.2018.10.007` | Connectomics and function of a memory network: the mushroom body of... | 2018 | 2019 | published-print |
| `10.1016/j.conb.2023.102822` | Descending control of motor sequences in | 2023 | 2024 | published-print |
| `10.1016/j.cub.2010.11.056` | Three-Dimensional Reconstruction of Brain-wide Wiring Networks in D... | 2010 | 2011 | published-print |
| `10.1016/j.cub.2021.10.069` | A neuropeptidergic circuit gates selective escape behavior of Droso... | 2021 | 2022 | published-print |
| `10.1016/j.cub.2021.11.005` | Dendro-somatic synaptic inputs to ganglion cells contradict recepti... | 2021 | 2022 | published-print |
| `10.1016/j.cub.2021.11.055` | Retinal horizontal cells use different synaptic sites for global fe... | 2021 | 2022 | published-print |
| `10.1016/j.cub.2024.11.010` | Ectopic Reconstitution of a Spine-Apparatus Like Structure Provides... | 2024 | 2025 | published-print |
| `10.1016/j.cub.2024.11.023` | Layer-specific anatomical and physiological features of the retina’... | 2024 | 2025 | published-print |
| `10.1016/j.cub.2024.11.064` | A recurrent neural circuit in Drosophila temporally sharpens visual... | 2024 | 2025 | published-print |
| `10.1016/j.cub.2025.11.035` | Drosophila DNp03 descending neurons serve as a hub within a flight ... | 2025 | 2026 | published-print |
| `10.1016/j.isci.2021.103601` | Multi-scale light microscopy/electron microscopy neuronal imaging f... | 2021 | 2022 | published-print |
| `10.1016/j.isci.2024.111585` | Heterogeneous and higher-order cortical connectivity undergirds eff... | 2024 | 2025 | published-print |
| `10.1016/j.isci.2025.114313` | Deriving connectivity from spiking activity in detailed models of l... | 2025 | 2026 | published-print |
| `10.1016/j.jmp.2016.06.009` | A primer on encoding models in sensory neuroscience | 2016 | 2017 | published-print |
| `10.1016/j.jneumeth.2007.07.021` | Contour-propagation algorithms for semi-automated reconstruction of... | 2007 | 2008 | published-print |
| `10.1016/j.jsb.2008.11.005` | 3D Imaging of mammalian cells with ion-abrasion scanning electron m... | 2008 | 2009 | published-print |
| `10.1016/j.jsb.2014.10.009` | Investigation of resins suitable for the preparation of biological ... | 2014 | 2015 | published-print |
| `10.1016/j.media.2011.11.004` | 3D segmentation of SBFSEM images of neuropil by a graphical model o... | 2011 | 2012 | published-print |
| `10.1016/j.neuroimage.2015.09.041` | Generative models of the human connectome | 2015 | 2016 | published-print |
| `10.1016/j.neuroimage.2016.11.006` | Multi-scale brain networks | 2016 | 2017 | published-print |
| `10.1016/j.neuron.2019.10.011` | Cortical Output Is Gated by Horizontally Projecting Neurons in the ... | 2019 | 2020 | published-print |
| `10.1016/j.neuron.2019.10.037` | Nested Neuronal Dynamics Orchestrate a Behavioral Hierarchy across ... | 2019 | 2020 | published-print |
| `10.1016/j.neuroscience.2006.12.015` | Non-synaptic dendritic spines in neocortex | 2006 | 2007 | published-print |
| `10.1016/j.neuroscience.2012.04.061` | Beyond counts and shapes: Studying pathology of dendritic spines in... | 2012 | 2013 | published-print |
| `10.1016/j.pbiomolbio.2021.06.013` | Mesoscale microscopy and image analysis tools for understanding the... | 2021 | 2022 | published-print |
| `10.1016/j.preteyeres.2019.07.004` | Persistent remodeling and neurodegeneration in late-stage retinal d... | 2019 | 2020 | published-print |
| `10.1016/j.tins.2016.11.007` | Weighing the Evidence in Peters’ Rule: Does Neuronal Morphology Pre... | 2016 | 2017 | published-print |
| `10.1016/j.xgen.2025.101103` | A high-resolution atlas of the brain predicts lineage and birth ord... | 2025 | 2026 | published-print |
| `10.1016/j.ydbio.2019.10.012` | Effector gene expression underlying neuron subtype-specific traits ... | 2019 | 2020 | published-print |
| `10.1038/s41467-019-09581-4` | Glutamate spillover in C. elegans triggers repetitive behavior thro... | 2018 | 2019 | published-online |
| `10.1038/s41467-019-12225-2` | Reconstructing neuronal circuitry from parallel spike trains | 2018 | 2019 | published-online |
| `10.1038/s41467-021-25436-3` | Stimulus-dependent representational drift in primary visual cortex | 2020 | 2021 | published-online |
| `10.1038/s41467-022-30452-y` | C. elegans enteric motor neurons fire synchronized action potential... | 2021 | 2022 | published-online |
| `10.1038/s41467-023-37180-x` | Catalyzing next-generation Artificial Intelligence through NeuroAI | 2022 | 2023 | published-online |
| `10.1038/s41467-026-69392-2` | Efficient pheromone navigation via antagonistic detectors in Caenor... | 2025 | 2026 | published-online |
| `10.1038/s41592-019-0501-0` | BigStitcher: reconstructing high-resolution image datasets of clear... | 2018 | 2019 | published-print |
| `10.1038/s41592-021-01105-7` | SNT: a unifying toolbox for quantification of neuronal anatomy | 2020 | 2021 | published-print |
| `10.1038/s41593-019-0431-2` | Targeting neuronal and glial cell types with synthetic promoter AAV... | 2018 | 2019 | published-print |
| `10.1038/s41593-023-01549-4` | Single-cell transcriptomics reveals that glial cells integrate home... | 2023 | 2024 | published-print |
| `10.1038/s41598-019-42648-2` | Automated 3D Axonal Morphometry of White Matter | 2018 | 2019 | published-online |
| `10.1038/s41598-021-81590-0` | Dense cellular segmentation for EM using 2D–3D neural network ensem... | 2020 | 2021 | published-online |
| `10.1038/s41598-021-91244-w` | A convolutional neural network for estimating synaptic connectivity... | 2020 | 2021 | published-online |
| `10.1038/s42003-026-10044-y` | Astrocyte-mediated higher-order control of synaptic plasticity | 2025 | 2026 | published-online |
| `10.1073/pnas.1720186115` | Specificity and robustness of long-distance connections in weighted... | 2017 | 2018 | published-print |
| `10.1091/mbc.e24-11-0519` | SynapseNet: Deep learning for automatic synapse reconstruction | 2024 | 2025 | published-print |
| `10.1093/brain/awaa406` | Three-dimensional analysis of synaptic organization in the hippocam... | 2020 | 2021 | published-print |
| `10.1093/cercor/bhz322` | Anatomy and Physiology of Macaque Visual Cortical Areas V1, V2, and... | 2019 | 2020 | published-print |
| `10.1093/cercor/bhz343` | Volume Electron Microscopy Study of the Relationship Between Synaps... | 2019 | 2020 | published-print |
| `10.1093/pnasnexus/pgae261` | Nondifferentiable activity in the brain | 2023 | 2024 | published-print |
| `10.1097/wnr.0000000000002012` | Adaptation-induced sharpening of orientation tuning curves in the m... | 2023 | 2024 | published-print |
| `10.1101/2024.02.07.579245` | Anti-diuretic hormone ITP signals via a guanylate cyclase receptor ... | 2025 | 2024 | issued |
| `10.1101/2024.06.14.599047` | Ultrastructural sublaminar-specific diversity of excitatory synapti... | 2025 | 2024 | issued |
| `10.1101/2024.09.07.611785` | niiv: Interactive Self-supervised Neural Implicit Isotropic Volume ... | 2025 | 2024 | issued |
| `10.1101/2025.05.02.651904` | Distinct evolutionary trajectories of two integration centres, the ... | 2026 | 2025 | issued |
| `10.1103/prxlife.2.013013` | Effect of Synaptic Heterogeneity on Neuronal Coordination | 2023 | 2024 | published-online |
| `10.1109/tbme.2011.2168396` | A Multiscale Parallel Computing Architecture for Automated Segmenta... | 2011 | 2012 | published-print |
| `10.1109/tmi.2016.2613019` | Residual Deconvolutional Networks for Brain Electron Microscopy Ima... | 2016 | 2017 | published-print |
| `10.1109/tnsre.2023.3346456` | Impact of Network Topology on Neural Synchrony in a Model of the Su... | 2023 | 2024 | published-print |
| `10.1109/tpami.2018.2835450` | Large Scale Image Segmentation with Structured Loss Based Deep Lear... | 2018 | 2019 | published-print |
| `10.1109/tpami.2020.2980827` | The Mutex Watershed and its Objective: Efficient, Parameter-Free Gr... | 2020 | 2021 | published-print |
| `10.1109/tvcg.2015.2467441` | NeuroBlocks – Visual Tracking of Segmentation and Proofreading for ... | 2015 | 2016 | published-print |
| `10.1126/science.aaz5357` | Correlative three-dimensional super-resolution and block face elect... | 2019 | 2020 | published-print |
| `10.1126/science.abb4534` | Postnatal connectomic development of inhibition in mouse barrel cortex | 2020 | 2021 | published-print |
| `10.1146/annurev-psych-122414-033634` | Modular Brain Networks | 2015 | 2016 | published-print |
| `10.1152/physrev.00019.2019` | Neuronal Circuits in Barrel Cortex for Whisker Sensory Perception | 2020 | 2021 | published-print |
| `10.1162/netn_a_00124` | Impact of higher order network structure on emergent cortical activity | 2019 | 2020 | published-print |
| `10.1162/netn_a_00428` | Combined topological and spatial constraints are required to captur... | 2024 | 2025 | published-print |
| `10.1162/netn_a_00455` | The exponential distance rule-based network model predicts topology... | 2024 | 2025 | published-print |
| `10.1167/jov.20.2.2` | A minimal synaptic model for direction selective neurons in Drosophila | 2019 | 2020 | published-print |
| `10.1242/jcs.181842` | Fast and precise targeting of single tumor cells in vivo by multimo... | 2016 | 2015 | published-online |
| `10.1242/jcs.188433` | 3D correlative light and electron microscopy of cultured cells usin... | 2017 | 2016 | published-online |
| `10.1371/journal.pcbi.1008374` | DeepMIB: User-friendly and open-source software for training of dee... | 2020 | 2021 | published-online |
| `10.1523/eneuro.0195-17.2017` | Quantifying Mesoscale Neuroanatomy Using X-Ray Microtomography | 2016 | 2017 | published-print |
| `10.1523/jneurosci.4500-08.2009` | Correlated connectivity and the distribution of firing rates in the... | 2008 | 2009 | published-print |
| `10.3389/fcomp.2022.777728` | Labkit: Labeling and Segmentation Toolkit for Big Image Data | 2021 | 2022 | published-online |
| `10.7554/elife.102309` | Dimorphic neural network architecture prioritizes sexual-related be... | 2025 | 2026 | published-online |
| `10.7554/elife.106446` | Inhibitory circuits control leg movements during Drosophila grooming | 2025 | 2026 | published-online |
| `10.7554/elife.108159` | Deep neural networks to register and annotate cells in moving and d... | 2025 | 2026 | published-online |
| `10.7554/elife.29915` | Excitatory motor neurons are local oscillators for backward locomotion | 2017 | 2018 | published-online |
| `10.7554/elife.63392` | Permeabilization-free en bloc immunohistochemistry for correlative ... | 2020 | 2021 | published-online |
| `10.7554/elife.79042` | Hierarchical architecture of dopaminergic circuits enables second-o... | 2022 | 2023 | published-online |
| `10.7554/elife.87866` | Rabies virus-based barcoded neuroanatomy resolved by single-cell RN... | 2023 | 2024 | published-online |
| `10.7554/elife.98358` | Synaptic enrichment and dynamic regulation of the two opposing dopa... | 2024 | 2025 | published-online |
