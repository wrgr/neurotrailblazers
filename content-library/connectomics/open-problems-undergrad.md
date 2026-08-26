---
layout: page
title: "Open Problems for Undergraduate Teams"
permalink: /content-library/connectomics/open-problems-undergrad/
image: /assets/images/content-library/connectomics/open-problems-undergrad.svg
image_alt: "Stylized vector art: a network graph with one community circled."
description: "A deep dive into open problems in connectomics that an undergraduate team can genuinely work on — automated proofreading, synapse detection, cell-type matching, connectome-scale graph algorithms, structure-to-function prediction, data logistics, and annotation science — with why each matters for the BRAIN CONNECTS scaling effort, current state of the art, scoped project ideas, and entry points."
topics:
  - open problems
  - undergraduate research
  - BRAIN CONNECTS
  - proofreading automation
  - synapse detection
  - cell typing
  - graph algorithms
  - structure-function
  - data infrastructure
primary_units:
  - "01"
  - "08"
  - "09"
difficulty: "Intermediate"
tags:
  - connectomics:connectome-comparison
  - connectomics:graph-construction
  - network-analysis:null-model
  - network-analysis:motif
  - network-analysis:community-detection
  - proofreading:merge-error
  - proofreading:split-error
  - proofreading:QA-metrics
  - neuroai:connectome-constrained-model
  - neuroai:structure-function
  - infrastructure:pipeline
  - infrastructure:BRAIN-Initiative
  - case-studies:FlyWire
  - case-studies:MICrONS
  - case-studies:MouseConnects
  - methodology:benchmark
  - methodology:ground-truth
  - methodology:reproducibility
micro_lesson_id: ml-conn-open-problems
combines_with:
  - connectome-history
  - network-analysis-methods
  - motif-analysis
  - neuroai-bridge
use_layout_hero: false
content_type: core
---

# Open Problems for Undergraduate Teams

This page is a working map of open problems in connectomics that satisfy two
constraints at once: **an undergraduate team can make real progress on them within
one to two semesters**, and **progress on them matters to the field's current
scaling effort** — the NIH BRAIN Initiative CONNECTS program and its flagship
projects, including [MouseConnects/HI-MC]({{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }}).

"Open problem" here does not mean "unsolved grand challenge." It means a question
where the answer is genuinely unknown, where the data and tools to attack it are
publicly available, and where a competent team's result — positive or negative —
would be worth reporting. Connectomics is unusual among neuroscience subfields in
how many such questions it currently has. The field's data production has outrun
its analysis capacity: the fly brain connectome alone (about 140,000 neurons and
roughly 50 million synapses) was released with the explicit expectation that most
of its science would be done by people outside the labs that built it, and as of
early 2026 more than 60,000 users had signed into Codex, its browser-based
explorer. Electron-microscopy-based connectomics was named Nature Methods'
**Method of the Year 2025** — recognition that the data exists; the open question
is what the community does with it and how the pipelines scale next.

## Why now, and why undergraduates

Three structural facts make this the right moment:

1. **The data is public and browser-accessible.** FlyWire (adult female fly
   brain), the Janelia male CNS connectome (the first complete male fly central
   nervous system, brain plus ventral nerve cord with an intact neck connective),
   MICrONS (a cubic millimeter of mouse visual cortex with co-registered
   functional imaging — roughly 200,000 cells and over half a billion synapses),
   H01 (a petabyte-scale fragment of human temporal cortex), the larval
   *Drosophila* CNS (3,016 neurons, Winding et al. 2023), and the eight
   developmental *C. elegans* connectomes of Witvliet et al. (2021) are all
   downloadable or queryable without institutional credentials. See
   [Datasets]({{ '/datasets/' | relative_url }}) for access routes.

2. **The analysis tooling is free and runs on a laptop.** CAVEclient, navis,
   neuprint-python, DotMotif, NetworkX/igraph, and Neuroglancer cover the whole
   path from raw query to publishable figure. Most of the projects below need no
   cluster; a Colab notebook is enough.

3. **The scaling effort has known, named bottlenecks.** CONNECTS — a roughly
   $150 million NIH program launched in 2023 with eleven funded projects — exists
   because going from 1 mm³ (MICrONS) to 10 mm³ (MouseConnects) to a whole mouse
   brain (~500 mm³, on the order of an exabyte of raw imagery at synaptic
   resolution) breaks every stage of the current pipeline. Each break is an open
   problem, and several of them are more limited by careful benchmarking and
   analysis — undergraduate-shaped work — than by resources only large labs have.

What follows is organized as seven problem areas. For each: what is actually
open, why CONNECTS needs it solved, the current state of the art with numbers,
and concretely scoped projects with entry points.

> **Ready to start rather than read?** Every problem below is also a card with a
> five-step on-ramp — read, get the data, reproduce a known number, first
> measurement, scope the semester — at
> [Open Problems]({{ '/open-problems/' | relative_url }}). The data step of every
> ramp runs through
> [Getting Started with Data]({{ '/datasets/getting-started/' | relative_url }}),
> which exists because data access is the step most teams stall on.

---

## Problem 1 — The proofreading budget: automated error detection and "how much is enough?" {#problem-1}

**What is open.** Automated segmentation still makes merge errors (two neurons
fused into one object) and split errors (one neuron broken into fragments), and
humans currently fix them. FlyWire took a community of hundreds of proofreaders
years to finish one fly brain. Complete manual proofreading of MouseConnects'
10 mm³ is widely acknowledged to be infeasible, and a whole mouse brain is out of
the question. Two questions are open. First, **can error detection and correction
be automated well enough to replace most human effort?** Second — less glamorous
and at least as important — **how much proofreading does a given scientific claim
actually require?** Nobody has a principled answer to "this motif result is
robust once the volume is X% proofread."

**Why CONNECTS needs it.** Proofreading is the single largest human cost in the
pipeline and the stage that scales worst. Every CONNECTS project's feasibility
case assumes an order-of-magnitude reduction in per-neuron human effort.

**State of the art.** NEURD (Nature, 2025) decomposes reconstructed neurons into
graphs of processes and applies rule-based automated proofreading plus feature
extraction, and worked at MICrONS scale. ConnectomeBench (2025) tested whether
large multimodal language models can do proofreading subtasks: current models
reached 52–82% balanced accuracy on segment-type identification (chance 20–25%)
and 75–85% on split-error correction posed as multiple choice (chance 50%), but
performed poorly at detecting merge errors — the error class that matters most,
because merges silently create false edges in the graph. Supervised
merge/split-detection classifiers trained on edit histories are an active area
with no dominant solution. On the "how much is enough" question, the honest state
of the art is ad hoc: papers report proofreading coverage but rarely show how
their conclusions vary with it.

**What an undergraduate team can do.**

- *Robustness-versus-proofreading curves.* FlyWire and MICrONS preserve full
  edit histories through CAVE's versioned materializations. Reconstruct the
  connectome graph at successive proofreading stages and measure when
  standard claims stabilize: degree distributions, reciprocity, motif z-scores,
  community structure. The deliverable — "claim X is stable after Y%
  of edits; claim Z never stabilizes" — is directly usable by MouseConnects
  planners deciding where to spend human effort. Skills: Python, pandas,
  NetworkX; [Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
  and [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}).
- *A merge-error detector benchmark.* Assemble a labeled set of true merges
  from edit histories (every human split operation marks a former merge error),
  train baseline classifiers on morphology and graph features, and publish the
  benchmark. The field lacks a shared merge-detection benchmark the way
  segmentation had CREMI and SNEMI3D; creating one is a service contribution
  with lasting citations.
- *Human-effort telemetry.* Instrument a proofreading exercise (this program's
  own [proofreading side quest]({{ '/side-quests/proofreading/' | relative_url }})
  is a starting point) to measure time-per-correction by error type and
  annotator experience. Per-error-type cost numbers are inputs every scaling
  plan needs and almost none publish.

**Entry points.** CAVEclient + MICrONS/FlyWire materializations; NEURD's public
code; ConnectomeBench's task definitions; FlyWire edit history via CAVE.

---

## Problem 2 — Synapse detection that generalizes {#problem-2}

**What is open.** Synapse detectors are typically trained per-dataset, on one
species, one staining protocol, one microscope. Performance degrades — sometimes
badly — under domain shift to a new sample, and quantifying that degradation
requires ground truth that mostly does not exist outside a few well-annotated
volumes. Detecting the *sign* (excitatory/inhibitory) and *strength* (synapse
size as a proxy) adds further open layers. Cross-species generalization is
explicitly unsolved: 2025 work on generalized synapse detection across
invertebrate species is an early attempt, not a solution.

**Why CONNECTS needs it.** A whole-mouse-brain effort cannot afford to
re-annotate ground truth and retrain for every region and every sample. Worse,
region-dependent detector bias would masquerade as biology: if the detector finds
10% fewer synapses in hippocampus than cortex for purely image-statistical
reasons, every cross-region comparison inherits that artifact.

**State of the art.** Modern detectors reach high F1 on the domain they were
trained on; the reviews accompanying Method of the Year 2025 credit AI-driven
reconstruction with an order-of-magnitude error reduction over the past decade,
while flagging generalization and validation as the open front. Public
ground-truth synapse annotations exist for CREMI (fly), MICrONS subvolumes, and
scattered smaller sets.

**What an undergraduate team can do.**

- *Cross-dataset degradation study.* Take a published, pretrained detector and
  measure precision/recall on ground truth from a dataset it was not trained on.
  A careful negative result with error taxonomy (what does it miss — small
  symmetric synapses? obliquely cut clefts?) is publishable and directly
  actionable.
- *Ground-truth annotation with agreement statistics.* Produce a new small
  gold-standard synapse set in an under-annotated region (e.g., an H01 or
  MICrONS subvolume), with multiple independent annotators and reported
  inter-annotator agreement. Ground truth is the scarcest resource in this
  problem; a few thousand carefully triple-annotated synapses is a real
  contribution a team can finish in a semester. Prerequisite skills are exactly
  [Unit 05]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }})
  and [Synapse classification]({{ '/content-library/neuroanatomy/synapse-classification/' | relative_url }}).
- *Size-versus-strength meta-analysis.* Synaptic cleft/PSD size is used as a
  strength proxy throughout the literature. Collect the published calibrations,
  re-derive the relationship in datasets where both anatomy and physiology
  exist, and quantify how much of the field's edge-weighting rests on it.

**Entry points.** CREMI challenge data; MICrONS synapse tables via CAVEclient;
published detector weights (e.g., from the MICrONS and FlyWire pipelines).

---

## Problem 3 — Cell types: matching across individuals, sexes, species, and modalities {#problem-3}

**What is open.** Cell typing in connectomics is done by morphology and
connectivity; transcriptomic atlases type cells by gene expression. Whether
these taxonomies align — and how types correspond across individual animals,
sexes, and species — is largely open. The 2025 male fly CNS release made this
concrete: comparing male and female fly brains identified 262 sex-specific and
114 sexually dimorphic cell types, about 4.8% of central-brain types. That
comparison was possible because fly cell types are stereotyped; in mouse cortex,
where types are statistical rather than stereotyped, cross-dataset matching is
much harder and mostly unsolved.

**Why CONNECTS needs it.** MouseConnects will produce hippocampal neurons by the
hundred thousand. Without reliable automated typing, downstream analysis
(connectivity by type, comparison to cortical data, links to Alzheimer's-relevant
cell populations) stalls. And because CONNECTS spans multiple projects and
species (mouse, macaque), cross-dataset type matching is the only way their
results compose into one body of knowledge.

**State of the art.** NBLAST and its successors match neurons by morphology
within a species; connectivity-based typing (clustering neurons by their
partners) worked well in the fly hemibrain and FlyWire; MICrONS papers
demonstrated coarse type prediction from EM features. Cross-modality
(EM ↔ transcriptomics) correspondence is established for major classes, sketchy
for subtypes.

**What an undergraduate team can do.**

- *Female-versus-male fly recount.* Pick a circuit with claimed dimorphism (or
  claimed stereotypy), and quantitatively compare it across FlyWire (female) and
  the male CNS dataset: neuron counts, connectivity weights, motif content. The
  datasets are both public and both proofread; the comparative literature is
  months old and thin. This is among the most immediately publishable projects
  on this page.
- *Typing-method shootout.* On a ground-truthed population (e.g., FlyWire
  neurons with community-assigned types), benchmark morphology-based (NBLAST),
  connectivity-based, and hybrid classifiers: accuracy, failure modes,
  sensitivity to proofreading completeness. The last axis ties this to
  Problem 1.
- *Skeleton-based deep classifier.* Train a graph neural network on public
  skeletons to predict type labels, and — the actually valuable part — measure
  transfer: train on FlyWire, test on the male CNS; train on one MICrONS
  region, test on another.

**Entry points.** navis + NBLAST; FlyWire Codex annotations; neuprint for
hemibrain/male CNS; MICrONS cell-type tables; Allen Institute transcriptomic
atlases for the cross-modality angle.

---

## Problem 4 — Graph algorithms and statistics at connectome scale {#problem-4}

**What is open.** Connectome graphs are now large enough (10⁵ nodes, 10⁷–10⁸
edges) that exact versions of the field's favorite analyses are intractable, and
the statistical foundations are shakier than the literature admits. Three open
strands. (a) **Combinatorial optimization:** ordering the fly connectome to
maximize feedforward flow is a minimum-feedback-arc-set problem; FlyWire's open
Minimum Feedback Challenge stands at 35,463,823 of 41,912,141 forward-pointing
synapse-weights (~85%), set in January 2026, with no known optimality bound —
beating it earns a leaderboard spot and is pure algorithms work. (b) **Null
models:** motif significance depends entirely on the null (degree-preserving vs
Erdős–Rényi vs geometry-aware), and there is no consensus null that respects
spatial embedding, multi-synapse edges, and cell types simultaneously — see
[Motif analysis]({{ '/content-library/connectomics/motif-analysis/' | relative_url }}).
(c) **Stability:** community-detection and embedding results on connectomes are
rarely reported with stability analysis across algorithm seeds, resolution
parameters, or edit-history versions.

**Why CONNECTS needs it.** Every one of these gets an order of magnitude harder
at 10 mm³. If the analysis stack's conclusions are not stable at fly scale, they
will be meaningless at mouse-hippocampus scale. Scalable approximate algorithms
with error bounds, and null models that survive peer scrutiny, are prerequisites
for the science CONNECTS is funding the data collection for.

**What an undergraduate team can do.** This is the cheapest entry point on the
page — a math/CS team needs no biology background to start, though the
interpretation payoff grows with it.

- *Attack the Minimum Feedback Challenge.* The graph is downloadable, the
  baseline code is public, submissions remain open past the original deadline,
  and the current record was itself set by an algorithms-community team.
- *Null-model sensitivity atlas.* Take three published motif claims and recompute
  them under a battery of null models. Report which claims are null-robust.
  (Worked example below.)
- *Approximate-algorithm benchmarking.* Benchmark scalable approximations
  (sampling-based motif counting, sketching, spectral methods) against exact
  answers on the fly connectome, producing accuracy-versus-compute curves that
  MouseConnects-scale analysts can use.

**Entry points.** Codex data downloads; the MFAS challenge page; DotMotif;
graph-tool/igraph for nulls at this scale (NetworkX becomes the bottleneck
around 10⁵ nodes — discovering exactly where is itself useful telemetry).

---

## Problem 5 — Structure to function: prediction and its limits {#problem-5}

**What is open.** The founding bet of connectomics is that wiring constrains
function. It is now testable, and the early answers are mixed in interesting
ways. Connectome-constrained models of the fly visual system (Lappalainen et
al., Nature 2024) predicted neural responses of unrecorded cell types from
wiring plus task training — a landmark positive. But 2025 work in Cell on
MICrONS-style functional connectomics found that connectomic predictions are
accurate for some response properties (orientation tuning) and surprisingly poor
for others (receptive field size), with infrequent strong connections carrying
disproportionate weight; and Nature Neuroscience work on connectome-constrained
recurrent networks concluded the connectome alone is generally insufficient —
pairing it with sparse recordings is what makes activity in unrecorded neurons
predictable. Mapping **where the predictive boundary lies** — which functional
properties wiring determines, which it merely biases, and which it leaves free —
is the central open scientific question of the field.

**Why CONNECTS needs it.** It is the justification for the whole program. If
function cannot be usefully constrained by structure, a mouse connectome is an
expensive atlas; if it can, it is a foundation for mechanistic neuroscience and
disease modeling. Every negative result that sharpens the boundary changes how
the next billion dollars of acquisition is prioritized (e.g., how much
co-registered functional data CONNECTS projects must collect).

**State of the art.** Besides the above: ZAPBench (ICLR 2025) provides a
whole-brain cellular-resolution activity-forecasting benchmark in larval
zebrafish, built to meet the forthcoming zebrafish connectome; current baselines
show video-based models beating trace-based ones, and the connectome-conditioned
frontier is essentially unexplored.

**What an undergraduate team can do.**

- *Benchmark entries.* ZAPBench is a leaderboard-style ML benchmark with public
  data and code — a standard ML-course-project shape with genuine scientific
  stakes. Any improvement, or any careful analysis of *why* models fail where
  they do, is a contribution.
- *Prediction-versus-physiology audits.* Take one published
  connectome-derived functional prediction in the fly (there are now dozens,
  many never checked) and test it against existing published physiology, or
  against the model outputs of released connectome-constrained models. This is
  literature-heavy, compute-light work that produces exactly the "which
  predictions held up" accounting the field lacks.
- *Simulation lesion studies.* Using released fly-visual-system models, ask
  which structural features the predictions actually depend on: randomize edge
  weights within type, delete weak edges, perturb sign assignments, and measure
  prediction degradation. This quantifies how much of Problem 2's (synapse
  weight) and Problem 1's (proofreading) error the structure-function claims can
  tolerate — tying three problems on this page together.

**Entry points.** ZAPBench data and code; the flyvis package (Lappalainen et
al.'s released model); MICrONS functional data via the public releases;
[NeuroAI bridge]({{ '/content-library/connectomics/neuroai-bridge/' | relative_url }}).

---

## Problem 6 — Data logistics at exabyte scale {#problem-6}

**What is open.** A whole mouse brain at synaptic resolution is on the order of
an exabyte of raw imagery; a human brain estimate runs to zettabytes. Storage,
compression, formats, and access patterns at that scale are unsolved in
practice: what lossy compression is scientifically safe (does 10× compression
change segmentation output? synapse detection output?), how should petabyte
volumes be chunked and served for the access patterns proofreaders and analysts
actually have, and how can acquisition QA (detecting folds, debris, focus drift,
misalignment) be automated well enough that errors are caught in hours rather
than after months of downstream compute?

**Why CONNECTS needs it.** Several CONNECTS awards are explicitly for scalable
acquisition and "intelligent image acquisition and reconstruction." Storage
costs are a first-order line item in every proposal; safe lossy compression at
even 5× changes project budgets by millions. Acquisition QA failures are the
most expensive kind: re-imaging destroyed tissue is impossible.

**State of the art.** The stack that got the field to petabyte scale —
precomputed/sharded formats, OME-Zarr, CloudVolume, CAVE (published in Nature
Methods, 2025), Neuroglancer — is public and battle-tested at 1 mm³. The
exabyte-scale question marks (compression safety, tiered storage economics,
QA automation) are documented as open in the field's own scaling reviews.

**What an undergraduate team can do.** This is the natural home for a pure
CS/data-engineering team.

- *Compression-safety benchmark.* Apply modern learned and conventional codecs
  to public EM volumes at increasing ratios, rerun published segmentation and
  synapse-detection models on the results, and report the ratio at which
  downstream outputs measurably change. This number is directly requested by
  scaling planning documents and does not currently exist in public,
  systematic form.
- *Access-pattern profiling.* Instrument open tools (Neuroglancer sessions,
  CAVE query logs where shareable) to characterize real read patterns, then
  evaluate chunking/sharding schemes against them.
- *Automated artifact QA.* Train detectors for section folds, staining
  artifacts, and alignment failures using the labeled examples that exist in
  public volumes ([Artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }})
  is the domain primer). Even a high-recall screener that flags sections for
  human review addresses a named CONNECTS bottleneck.

**Entry points.** CloudVolume + public MICrONS/H01/FlyWire image volumes;
OME-Zarr tooling; [Data formats]({{ '/content-library/infrastructure/data-formats/' | relative_url }})
and [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}).

---

## Problem 7 — The human side: annotation science and distributed proofreading {#problem-7}

**What is open.** Connectomics has quietly run some of the largest distributed
scientific-annotation efforts ever — Eyewire's hundreds of thousands of
registered players, FlyWire's citizen-scientist community that out-proofread
professionals in places — but the *science of that work* is thin. Open
questions: what actually predicts annotator accuracy and how fast do learners
reach expert agreement; which errors do novices systematically make (and can
training target them); how should consensus be aggregated when annotators
disagree; what task designs keep volunteers engaged without degrading quality?
These are tractable human-subjects/HCI questions with direct pipeline impact.

**Why CONNECTS needs it.** Even heavily automated pipelines keep humans in the
loop for the hard residue, and MouseConnects-scale efforts plan on distributed
communities — including, explicitly, NeuroTrailblazers-trained students. Every
percentage point of annotator accuracy and retention changes the labor budget
of a five-year project. This is also the one problem area where an education-,
psychology-, or HCI-leaning team has the home advantage.

**What an undergraduate team can do.**

- *Learning-curve study.* Run cohorts through a structured proofreading
  curriculum (this site's [Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
  and side quest provide the instrument), measuring time-to-competence against
  expert-consensus gold standards, and identify which error classes
  ([Error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }}))
  training moves and which it does not. Requires IRB/ethics review — plan for
  that in semester timelines.
- *Consensus-aggregation benchmark.* Using multiply-annotated data, compare
  aggregation schemes (majority vote, weighted by track record, model-assisted
  arbitration) for recovering gold-standard answers.
- *Contribution analytics.* Public edit histories permit retrospective analysis
  of real communities: contribution distributions, accuracy-versus-experience,
  the effect of gamification events. Retrospective, non-interventional analyses
  of public logs sidestep much of the human-subjects overhead.

**Entry points.** FlyWire/Eyewire published community analyses; CAVE edit
logs; this program's own worksheets as standardized training instruments.

---

## Choosing: a decision protocol {#choosing}

Four questions, in order, will land a team on the right problem:

1. **What is the team's strongest existing skill?** Algorithms/math → Problem 4.
   ML engineering → Problems 1, 2, 5. Biology/microscopy → Problems 2, 3.
   Systems/data engineering → Problem 6. Psychology/education/HCI → Problem 7.
   Choosing a problem that needs a skill nobody has is the most common failure
   mode; the biology can be learned alongside a skill-matched problem, but not
   instead of one.
2. **Is the data truly in hand in week one?** Every project above is scoped to
   public data. Verify by downloading a working subset before committing —
   "the data exists" and "we have the data loading in a notebook" are separated
   by weeks of format wrangling ([Datasets]({{ '/datasets/' | relative_url }})
   shortcuts most of it).
3. **What is the minimum reportable result?** Scope so that a negative or
   partial answer is still a deliverable: a benchmark, a sensitivity table, a
   documented failure taxonomy. Projects whose only success mode is "beat the
   state of the art" are lottery tickets; projects whose worst case is a
   careful measurement are investments.
4. **Who is the customer?** For each problem above the customer is named — a
   pipeline team, the analysis community, a challenge leaderboard, a planning
   document. Write the abstract of the final report in week two, addressed to
   that customer, and let it steer scope.

## Worked example: scoping the null-model sensitivity project

To make the scoping concrete, here is Problem 4's second project taken from idea
to plan, with the reasoning shown.

**Claim selection.** Start from a published, specific, quantitative claim — for
example, over-representation of reciprocal connectivity among excitatory neurons,
reported in both fly and cortical data. Reciprocity is a two-node motif, so
counting is trivial even at full-connectome scale; the entire difficulty, and the
entire scientific content, lives in the null model. That asymmetry — cheap
statistic, contested null — is exactly what makes it a good undergraduate
target. A team tempted instead by, say, five-node motifs would spend the
semester on subgraph-isomorphism scaling (a Problem-4a computational project —
legitimate, but a different one) and never reach the statistics.

**Design.** Fix one dataset snapshot and record its version identifier — CAVE
materializations make analyses reproducible only if the version is pinned, which
is why [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
is a week-one reading. Compute observed reciprocity for one well-defined cell
population. Then recompute expectation and z-score under at least four nulls of
increasing biological fidelity: Erdős–Rényi (edge count preserved);
configuration model (in/out degree sequences preserved); a distance-dependent
null (connection probability as the empirical function of inter-soma distance,
preserving spatial embedding); and a type-aware null (block structure by cell
type preserved). Each null answers a different question, and writing down *which
question* before running it is the actual intellectual work: significance under
Erdős–Rényi but not under the distance null means "neurons are near each other,"
not "the circuit seeks reciprocity."

**Anticipated result shapes.** All-nulls-significant strengthens the published
claim and the deliverable is a robustness certificate. Significance that
disappears under the distance or type null is the more interesting outcome — a
documented case that a standard claim is a geometry or composition artifact.
Either way the minimum reportable result (question 3 above) is the sensitivity
table itself, which is why this project passes the protocol.

**Timeline honesty.** Weeks 1–3: data access, version pinning, population
definition (slower than expected — always). Weeks 4–6: observed statistics and
the two easy nulls. Weeks 7–10: the distance-dependent null, which requires
fitting the empirical distance-probability curve and is where the project's real
effort concentrates. Weeks 11–13: type-aware null, sensitivity table,
write-up. A second semester extends the same machinery to more claims, the male
CNS comparison (Problem 3 crossover), or proofreading-stage sensitivity
(Problem 1 crossover).

## Self-check

Answer before reading the answers.

1. Why is merge-error detection considered harder-to-automate and
   higher-stakes than split-error detection?
2. A team proposes: "we will build a better segmentation model than Google's
   flood-filling networks." Which decision-protocol questions does this fail?
3. Your motif is significant under a configuration-model null but not under a
   distance-dependent null. What is the correct interpretation?
4. Name two ways the proofreading problem (Problem 1) and the
   structure-function problem (Problem 5) are coupled.

**Answers.**

1. Splits are conspicuous — a fragment with no soma, an axon ending mid-volume —
   and correcting one candidate pair is a well-posed local question, which is why
   models already do fairly well on it (75–85% in ConnectomeBench's forced-choice
   setup). A merge produces a plausible-looking chimera; detecting it requires
   noticing that a single object's morphology or connectivity is internally
   inconsistent, a global judgment. Stakes: an undetected merge fabricates
   edges between unrelated neurons, corrupting the graph silently; an undetected
   split mostly loses edges, a more visible and more recoverable error.
2. Primarily question 1 (skill match against industrial teams with training
   infrastructure no undergraduate team can replicate) and question 3 (the only
   success mode is beating a heavily resourced state of the art; a near-miss
   yields no deliverable). Re-scoped as *benchmarking* existing models under
   domain shift (Problem 2), the same interest passes the protocol.
3. The motif occurs more often than random wiring with matched degrees would
   produce, but not more often than expected given how close the neurons are to
   each other: spatial proximity, not motif-specific selection, is the
   parsimonious explanation. It is a claim about geometry, not circuit
   computation — and it is a finding, not a failure.
4. (a) Structure-function models consume the graph that proofreading produces;
   robustness-versus-proofreading curves determine how much reconstruction error
   those models' predictions can tolerate. (b) Lesion/perturbation studies on
   connectome-constrained models identify which structural features predictions
   depend on, which tells proofreading campaigns where accuracy actually matters
   — e.g., the Cell 2025 finding that infrequent strong connections carry
   disproportionate functional weight implies proofreading effort should
   prioritize exactly the edges most affected by merge errors.

## What this page does not cover

- **Wet-lab and acquisition problems** — sample preparation, staining, expansion
  microscopy, multi-beam instrument development. These are core CONNECTS
  problems but require facilities undergraduate teams rarely have; this page
  deliberately selects for public-data, laptop-scale entry.
- **MRI-scale connectomics** — tractography and functional connectivity have
  their own open-problem landscape (see the
  [MRI connectomics papers]({{ '/content-library/journal-papers/mri-connectomics/' | relative_url }})),
  distinct from the synaptic-resolution scope here.
- **A guarantee of novelty.** This field moves fast; between this page's
  writing and your project's start, check whether a listed gap has closed. The
  first hour of any project is a literature search scoped to the last twelve
  months — the [journal club corpus]({{ '/technical-training/journal-club/' | relative_url }})
  shows how to do this systematically.
- **Numbers as facts about tissue.** Dataset figures quoted here (neuron
  counts, synapse counts, challenge scores) are properties of particular
  releases and leaderboard dates, and they move. Re-pull them from the source
  before quoting them anywhere that matters.

## Key references

- Nature Methods editorial (2025). Method of the Year 2025:
  electron-microscopy-based connectomics. *Nature Methods*.
- *Synaptic connectomics: status and prospects.* (2025). *Nature Reviews
  Neuroscience*.
- *Synaptic-resolution connectomics: towards large brains and connectomic
  screening.* (2025). *Nature Reviews Neuroscience*.
- Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain.
  *Nature*, 634, 124–138. (FlyWire)
- Schlegel, P., et al. (2024). Whole-brain annotation and multi-connectome cell
  typing of *Drosophila*. *Nature*, 634, 139–152.
- MICrONS Consortium (2025). Functional connectomics spanning multiple areas of
  mouse visual cortex. *Nature*, 640.
- Janelia FlyEM Project Team (2025). Male CNS connectome resources.
  janelia.org/project-team/flyem/male-cns-connectome.
- Celii, B., et al. (2025). NEURD offers automated proofreading and feature
  extraction for connectomics. *Nature*.
- *ConnectomeBench: can LLMs proofread the connectome?* (2025). arXiv:2511.05542.
- Lappalainen, J. K., et al. (2024). Connectome-constrained networks predict
  neural activity across the fly visual system. *Nature*, 634, 1132–1140.
- *Prediction of neural activity in connectome-constrained recurrent networks.*
  (2025). *Nature Neuroscience*.
- *Infrequent strong connections constrain connectomic predictions of neuronal
  function.* (2025). *Cell*.
- Lueckmann, J.-M., et al. (2025). ZAPBench: a benchmark for whole-brain
  activity prediction in zebrafish. *ICLR 2025*. arXiv:2503.02618.
- Winding, M., et al. (2023). The connectome of an insect brain. *Science*,
  379, eadd9330.
- Witvliet, D., et al. (2021). Connectomes across development reveal principles
  of brain maturation. *Nature*, 596, 257–261.
- Dorkenwald, S., et al. (2025). CAVE: Connectome Annotation Versioning Engine.
  *Nature Methods*.
- FlyWire Minimum Feedback Challenge. codex.flywire.ai/app/mfas_challenge.
