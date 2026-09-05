---
layout: page
title: "Synapse Detection"
permalink: /content-library/infrastructure/synapse-detection/
image: /assets/images/content-library/infrastructure/synapse-detection.svg
image_alt: "Stylized vector art: pipeline stages running above a chunk grid."
description: >
  How synapses are found in electron microscopy volumes, as a method rather than
  as biology: cleft detection, partner assignment and sign classification as
  three separable problems; the classical and learned approaches with their
  published numbers; what a CREMI score does and does not predict; why detectors
  degrade across datasets; and what to measure before trusting a synapse table.
topics:
  - synapse detection
  - cleft segmentation
  - synaptic partner assignment
  - excitatory-inhibitory classification
  - CREMI
  - domain shift
  - ground truth
primary_units:
  - "04"
  - "05"
  - "08"
difficulty: advanced
tags:
  - infrastructure:pipeline
  - connectomics:synapse-detection
  - connectomics:graph-construction
  - neuroai:deep-learning
  - methodology:benchmark
  - methodology:ground-truth
  - methodology:domain-shift
  - proofreading:QA-metrics
  - case-studies:H01
  - case-studies:FlyWire
micro_lesson_id: ml-infra-synapse-detection
combines_with:
  - reconstruction-pipeline
  - metrics-and-qa
  - synapse-classification
use_layout_hero: false
content_type: core
---

# Synapse Detection

A connectome is a graph, and the edges of that graph come from a synapse
detector. Everything downstream — connection weights, motif counts, cell-type
fingerprints, connectome-constrained models — inherits whatever that detector
got wrong. The
[reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }})
page describes synapse detection in five bullets as one stage of Layer 4. This
page is the argument behind those bullets: what the task is, what has been
tried, what the published numbers are, and what you have to measure before you
are entitled to use somebody else's synapse table.

This is the site's own [open problem 2]({{ '/open-problems/' | relative_url }}),
treated here as a method rather than as biology. For what a synapse looks like
and how to recognise one by eye, see
[Synapse classification]({{ '/content-library/neuroanatomy/synapse-classification/' | relative_url }}).

---

## 1. Three problems, not one

"Synapse detection" names at least three tasks that succeed and fail
independently.

**1. Localisation.** Find the synapse. Depending on the method this means
segmenting the synaptic cleft as a set of voxels, or predicting a point
annotation for the presynaptic site, or classifying the *interface* between two
already-segmented processes as synaptic or not.

**2. Partner assignment.** Given a synapse, say which segment is presynaptic
and which is postsynaptic. This is a separate learning problem: Buhmann et al.
(2021) and Turner et al. (2020) both treat it as its own network, and Huang et
al. (2018) use a U-Net for presynaptic sites and a separate multilayer
perceptron, conditioned on the local segmentation, for postsynaptic partners.

**3. Sign or type.** Say whether the connection is excitatory or inhibitory. In
mammalian cortex this is read from postsynaptic-density morphology; in
*Drosophila* it is read from transmitter identity predicted from
ultrastructure (Eckstein et al., 2024). Section 4 is about why this is the
hardest of the three.

Two structural facts change the shape of the problem depending on your tissue.
First, **insect synapses are polyadic**: one presynaptic site contacts several
postsynaptic partners, so "one cleft" is not "one edge". Huang et al. (2018)
describe theirs as "a complete solution for polyadic synapse detection", and the
WASPSYN annotations record pre- and post-synaptic coordinates "together with
their one-to-many connectivity information" (Li et al., 2024). Second, some
methods need a segmentation first and some do not: SynEM classifies borders
between already-segmented processes (Staffler et al., 2017) while Heinrich et
al. (2018) segment clefts directly out of the raw image. That decides whether
segmentation errors propagate into your synapse table, and it means the two
methods' F-scores are **not measuring the same object**.

---

## 2. What has been tried, with numbers

| Method | Year | What it predicts | Reported performance | Tissue and preparation |
|---|---|---|---|---|
| ilastik synapse detection (Kreshuk et al.) | 2011 | Asymmetric (presumed excitatory) synapse segmentation from voxel features | **0.92 recall at 0.89 precision** on 111 validation synapses, "comparable to that of the experts" (three independent annotators) | Adult mammalian cortex, FIB/SEM, near-isotropic |
| Context-cue synapse segmentation (Becker et al.) | 2013 | Synapse segmentation plus synaptic orientation | Evaluated on three datasets; recovers orientation as a by-product | EM stacks, mixed |
| SyConn (Dorkenwald et al.) | 2017 | Synapses and synapse types alongside mitochondria, compartments and cell types | Framework paper; used to compute songbird basal-ganglia wiring | SBEM: zebrafish, mouse, zebra finch |
| SynEM (Staffler et al.) | 2017 | Neurite-interface classification: synaptic vs non-synaptic | **88% precision, 88% recall** per synapse; **94% precision, 89% recall** for spine synapses; **97% precision and recall** at the level of binary cortical connectomes | Mouse cortex, conventional en-bloc staining, SBEM |
| 3D U-Net cleft segmentation (Heinrich et al.) | 2018 | Synaptic cleft voxels, by regression on a signed distance transform | Reported as a significant improvement over the prior state of the art on CREMI | Adult *Drosophila*, anisotropic ssTEM; applied to ~50 teravoxels of the whole fly brain |
| Fully-automatic synapse prediction (Huang et al.) | 2018 | Presynaptic sites (U-Net) plus postsynaptic partners (MLP on segmentation-conditioned features) | Introduced connectome-scale evaluation metrics; reports that complete automatic prediction characterises most connectivity correctly | *Drosophila*, polyadic |
| Attentional voxel association networks (Turner et al.) | 2020 | Presynaptic and postsynaptic masks, generated from a cleft mask used as an attention gate | Evaluated as part of a combined cleft-plus-partner system | Mouse somatosensory cortex |
| Synful (Buhmann et al.) | 2021 | Synaptic partners directly, whole-brain | **F1 of 0.73, 0.68, 0.66 and 0.59** in four different brain areas; **244 million** putative synaptic partners extracted from FAFB; 92–96% of edges correctly sorted into weakly (<5 synapses) and strongly (≥5) connected | Adult *Drosophila*, FAFB ssTEM |
| Cerebellum-specific contact classifier (Park et al.) | 2022 | Synaptic vs non-synaptic contacts, plus pre/post side and excitatory/inhibitory type | **F1 = 0.955** on a test volume containing 508 synapses | Mouse cerebellar molecular layer |
| H01 detector (Shapson-Coe et al.) | 2024 | Three-class U-Net (background / presynaptic / postsynaptic) plus a ResNet-50 excitatory-vs-inhibitory classifier | See §4 — the numbers differ by more than threefold between excitatory and inhibitory recall | Human temporal cortex, ssEM at 4 × 4 nm, 33 nm sections |
| SimpSyn (Mohinta et al.) | 2025 | Dual-channel spherical masks around pre- and post-synaptic sites, single-stage residual U-Net | Outperforms Synful in F1 on all volumes in a four-dataset invertebrate benchmark; the authors report that **generalisation across datasets remains limited** | Adult and larval *Drosophila*, *Megaphragma viggianii* |

Three readings of that table matter more than the individual rows.

**The numbers are not on a common scale.** Kreshuk's 0.92/0.89 is per-synapse
on near-isotropic FIB/SEM; SynEM's 88/88 is per-*interface* on anisotropic
SBEM; Buhmann's 0.59–0.73 is per-partner-pair on ssTEM. A method that looks
worse here may simply have been measured on a harder unit in harder tissue.
Never rank two detectors by numbers taken from their own papers.

**Aggregation is doing enormous work.** SynEM classifies interfaces at 88%
precision and recall, and yields 97% precision and recall in binary cortical
connectomes. Nothing about the classifier changed; what changed is that a neuron
pair is usually connected by more than one synapse, so independent per-synapse
errors partly cancel when you only ask "are these two neurons connected?".
Buhmann et al. show the same effect from the other side: per-connection F1 of
0.59–0.73, but 92–96% of edges correctly assigned to the weak/strong classes
most analyses actually use. **The number you need is the one measured at the
level of your claim** — for most connectomics, the edge, not the synapse.

**The field's accounting has moved.** Huang et al. (2018) observed that as
segmentation improved, synapse annotation came to consume "upwards of 50% of
total effort". Synapse detection stopped being the pipeline's afterthought at
roughly that point, which is why the later entries above are about partners and
generalisation rather than about finding clefts.

---

## 3. Benchmarks: what a CREMI score does and does not tell you

**CREMI** (Circuit Reconstruction from Electron Microscopy Images) is the
reference benchmark. It provides three datasets, each consisting of two
(5 µm)³ volumes — training and testing, 1250 × 1250 × 125 px — of
serial-section transmission EM of the adult *Drosophila* brain at
[4, 4, 40] nm voxel resolution. Each training volume ships neuron ids,
synaptic-cleft segmentation, and (pre, post) partner pairs. Three tasks are
scored:

| CREMI task | How it is scored |
|---|---|
| Neuron segmentation | Variation of Information, Adapted Rand error, and Tolerant Edit Distance — the metrics explained in [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}) |
| Synapse detection | F-measure over false positives and false negatives, where a predicted cleft voxel beyond a threshold distance from any ground-truth cleft counts as a false positive, and vice versa for false negatives |
| Connectivity (partner identification) | F-measure over matched (pre, post) pairs, matched by solving an assignment problem that minimises Euclidean distance within a threshold |

Note what the scoring does *not* do: it does not require a predicted cleft to
overlap the ground-truth cleft voxel-for-voxel, only to fall within a distance
tolerance. Cleft detection is a localisation problem with slack, which is why
methods that regress a distance transform (Heinrich et al., 2018) rather than
classifying voxels do well on it.

**What a good CREMI score predicts.** That your method is competitive on
anisotropic fly ssTEM, at CREMI's resolution, under CREMI's convention for what
counts as a cleft. That is worth knowing, and it is why CREMI training data
underlies whole-brain fly cleft prediction: Heinrich et al. trained on CREMI's
annotated crops and then predicted clefts across roughly 50 teravoxels of the
complete *Drosophila* brain.

**What it does not predict.**

- *Performance elsewhere in the same volume.* Buhmann et al. trained one model
  and got F1 scores of 0.73, 0.68, 0.66 and 0.59 in four different brain areas
  of the same fly brain. A 0.14-point spread across regions of one sample is
  larger than the gap between many published methods.
- *Performance in mammalian tissue.* Different voxel size, different
  anisotropy, different staining chemistry, different synapse geometry, and —
  in mammals — no polyadic structure to exploit.
- *Whether your edges are right.* CREMI's connectivity task is scored on pairs,
  not on the weighted graph your analysis will use. See the aggregation point
  in §2.
- *Inhibitory recall.* CREMI does not separate the sign of the connection at
  all. §4 is where that matters.

**WASPSYN** (Li et al., 2024) is the benchmark built to measure what CREMI
cannot: domain adaptation. Its authors annotated 14 image volumes from a
biologically diverse set of *Megaphragma viggianii* brain regions drawn from
three different whole-brain datasets, and ran it as an ISBI 2023 challenge.
Their framing carries the number that defines the problem: manual annotation is
so expensive that labelled training data is "often smaller than 0.001% of the
large-scale image volumes in application". That ratio, not any single F1, is why
cross-dataset generalisation is the live question.

---

## 4. Excitatory versus inhibitory, and why it is harder

Cleft detection asks "is there a synapse here?" Sign classification asks "what
kind?" — and the evidence for the answer is thinner, more protocol-dependent,
and more asymmetric between classes.

**The morphological basis is a statistical mapping, not a rule.** Synapses sort
into Gray's type I and type II, corresponding to Colonnier's asymmetric (AS) and
symmetric (SS): AS have a thick postsynaptic density, SS a thin one. In cerebral
cortex most AS are excitatory (glutamatergic) and most SS inhibitory
(GABAergic) — "most", not all. Cano-Astorga et al. (2024) validate the
morphological call against molecular markers, using immunocytochemistry for the
vesicular GABA transporter to confirm that symmetric synapses seen under their
protocol are GABAergic.

**The discriminating feature is a few voxels thick, and staining moves it.** The
same paper shows that potassium ferrocyanide, used in modern volume-EM protocols
to enhance membrane contrast, makes postsynaptic densities *thinner* as its
concentration rises, so symmetric synapses become progressively harder to
identify; they recommend 0.1%. The consequence for a detector is stark: **the
feature your inhibitory classifier depends on is partly a property of the
sample-preparation recipe**, not only of the tissue. A classifier trained on one
lab's staining is being asked to transfer across chemistry, not just across
brains.

**The published numbers show the asymmetry directly.** In H01, Shapson-Coe et
al. (2024) report, from manual proofreading of a selection of axons across all
cortical layers:

| | Excitatory | Inhibitory |
|---|---:|---:|
| False negatives (missed synapses) | 11% | **35%** |
| False discovery rate | 3.2% | 2.7% |
| Correctly classified as this type | 86.89% | 84.98% |

Precision is excellent and near-identical for both classes. Recall is not: the
detector misses roughly one inhibitory synapse in three, and one excitatory
synapse in nine. That single asymmetry is the most consequential number on this
page, and §5 works out what it does to a result.

**In insects, sign is a different problem entirely.** Fly synapses do not give
up their sign through AS/SS morphology, so the question becomes transmitter
identity. Eckstein et al. (2024) trained networks on EM images at synaptic sites
to predict six transmitters (acetylcholine, glutamate, GABA, serotonin,
dopamine, octopamine) across a whole *Drosophila* brain, reaching **87% accuracy
for individual synapses, 94% for neurons, and 91% for known cell types**. The
87 → 94 step is the aggregation effect again: a neuron's synapses vote. It also
means fly connectome signs are properties of *neurons* in practice, so treating
per-synapse predictions as independent evidence double-counts.

---

## 5. A worked judgement: recounting H01's excitatory/inhibitory balance

Take the H01 synapse table as released and ask a routine question: what
fraction of synapses in human temporal cortex are excitatory?

**The straight count.** Shapson-Coe et al. report 149,871,669 synapses
automatically detected in the volume, of which 111,272,315 were classified as
excitatory and 38,599,354 as inhibitory. That is **74.2% excitatory, 25.8%
inhibitory**. If you pull the released table and compute a ratio, this is your
answer.

**The corrected estimate.** The authors do not report that number as their
result. Adjusting for the measured false-discovery, false-negative and
misclassification rates in the table above, they estimate the volume actually
contains 102.5 million (**67.1%**) excitatory and 50.3 million (**32.9%**)
inhibitory synapses.

**What moved.** Almost all of it is the 35% inhibitory false-negative rate.
Precision was fine for both classes, so few of the detected synapses are
spurious; the problem is the ones that were never detected, and they are
disproportionately inhibitory. Running the arithmetic the other way: the raw
table contains 38.6 M of an estimated 50.3 M inhibitory synapses — it is
short by about **23%** of the inhibitory population — while its excitatory
count of 111.3 M sits about **9% above** the 102.5 M estimate. The naive ratio
is wrong in both directions at once, which is why the error on the *ratio*
(74.2% versus 67.1%, or 7.1 percentage points) is larger than the error on
either count alone.

**How confident should you be in the correction?** Less than in the raw count.
It rests on proofreading a *selection* of axons rather than a dense
re-annotation, so the rates carry their own sampling error, and they were
measured across cortical layers that differ in inhibitory density. The corrected
figure is an estimate from a sample; the raw figure is an exact count of a
biased measurement. Neither is "the number of synapses in the tissue", and a
paper quoting either without saying which has not told you what it did.

**What follows, well beyond H01.**

1. **Any excitation/inhibition ratio computed straight from a released synapse
   table is biased toward excitation**, by an amount set by the detector's
   class-specific recall. Report the recall figures alongside the ratio, or do
   not report the ratio.
2. **Comparisons are safer than absolutes.** For two regions processed by the
   same detector and staining, the *difference* in E/I ratio survives a shared
   bias that the absolute value does not.
3. **The bias is not random, so more data will not fix it.** Ten times the
   volume buys ten times the confidence in the wrong number.

---

## 6. Why detectors do not transfer

Every one of the following differs between two EM volumes, and every one of
them can move a detector's output.

| What changes | Concrete example |
|---|---|
| Voxel size and anisotropy | CREMI/FAFB at 4 × 4 × 40 nm ssTEM; H01 at 4 × 4 nm in-plane with 33 nm sections; FIB/SEM volumes near-isotropic. Heinrich et al. built a 3D U-Net specifically "to optimally represent isotropic fields of view in non-isotropic data" — the architecture itself encodes an assumption about the sampling grid |
| Staining chemistry | Potassium ferrocyanide concentration changes apparent PSD thickness (Cano-Astorga et al., 2024) — directly attacking the inhibitory-synapse feature |
| Species ultrastructure | Polyadic insect synapses versus predominantly monadic mammalian ones; the output *structure* differs, not just the appearance |
| Annotation convention | What counts as a cleft, and where a "site" point is placed relative to it. Two ground-truth sets can disagree systematically while both being correct by their own rules |
| Region within one sample | Buhmann et al.: F1 0.59 to 0.73 across four areas of the same fly brain |

The honest summary is narrower than "models do not transfer".

**Within a volume and preparation, spatial generalisation is often fine.**
Heinrich et al. report that their model, trained on CREMI's small annotated
crops, "generalizes well to areas far away from where training data was
available" — across a whole fly brain, including lamina.

**Across preparations, it is not.** SimpSyn's authors, benchmarking on four
invertebrate datasets, conclude that generalisation across datasets remains
limited even for the model that wins within each dataset. SynapseNet's authors
built explicit domain-adaptation functionality into their tool rather than
relying on a large training set. And WASPSYN exists because, in the organisers'
words, methods that "utilize in-domain labeled data and generalize to
out-of-domain unlabeled data are in urgent need".

That distinction is operational. If you are analysing one released volume, its
detector was probably trained on that volume and the within-sample evidence
applies to you. If you are bringing a published detector to *new* tissue, you
are in the regime where the evidence says it will degrade, by an amount nobody
can tell you in advance.

---

## 7. Before you trust a synapse table

You will usually not be running a detector. You will be downloading a table
someone else's detector produced. This is the checklist.

| Ask | Why it changes what you can claim |
|---|---|
| **Which detector, which version, which materialization?** | Synapse tables are regenerated. A result that does not name the version is not reproducible — see [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) |
| **What was the ground truth: how many synapses, annotated by whom, with what agreement?** | Kreshuk et al. validated on 111 synapses with three independent experts; SynEM's test set was 235 synapses among 20,319 non-synaptic interfaces. Numbers from a test set of a few hundred carry visible sampling error |
| **Is the reported figure per synapse or per connection?** | SynEM: 88% versus 97%. Both are true; they answer different questions |
| **Are precision and recall reported separately for excitatory and inhibitory?** | H01: 3.2% versus 2.7% FDR, but 11% versus 35% false negatives. A single combined F1 hides exactly the error that will bite you |
| **Is performance stratified by region?** | Buhmann et al.: 0.59 to 0.73 within one brain. A whole-volume average tells you nothing about your region |
| **What is the polyadicity convention: one row per synaptic site, or one per (pre, post) pair?** | Miscounting this inflates or deflates every insect connection weight |
| **What distance tolerance was used in the evaluation?** | CREMI-style scoring matches within a threshold. A generous threshold flatters everything |
| **Was the evaluation on the same preparation as the volume you are using?** | If not, §6 applies and the published number is an upper bound at best |

**If none of that is available**, you can still bound your own risk in an
afternoon. Take a random subvolume, annotate every synapse in it by hand, and
compare against the table: missed table entries give you recall, spurious ones
give you precision. Two calibration points set expectations. Kreshuk et al.
found their algorithm's error rate "comparable to that of the experts", and
SynEM reports its expert annotators at 93.6–94.6% and 97.9–98.9%
precision/recall — so **agreement in the mid-90s is roughly what two competent
humans achieve**. A detector matching your annotations more closely than that
should make you suspicious of your annotations, not confident in the detector.
For the manual pass itself, SynAnno (Lauenburg et al., 2025) provides guided,
neuron-centric synapse proofreading with model-assisted error detection.

---

## Self-check

1. SynEM reports 88% precision and recall per synapse and 97% for binary
   connectomes. What changed, and when may you quote the 97%?
2. A team beats the published CREMI cleft F1. What have they demonstrated, and
   what have they not?
3. You compute an excitatory:inhibitory ratio of 74:26 from H01's released
   table. Name the measurement that makes this wrong, and the direction.

**Answers.**

1. Nothing about the classifier changed; the *unit of the question* did. Neuron
   pairs are usually connected by several synapses, so independent per-synapse
   errors partly cancel when you only ask whether an edge exists. Quote 97% when
   your claim is about the existence of connections in comparable tissue; not
   when it is about synapse counts, connection weights, or anything per-synapse.
2. Competitiveness on anisotropic adult-fly ssTEM at 4 × 4 × 40 nm under CREMI's
   annotation convention and distance-tolerant scoring. Not: mammalian tissue,
   other regions of a fly brain (Buhmann et al. span 0.59–0.73 within one
   brain), sign classification, or the accuracy of the weighted graph a user
   would build.
3. The 35% false-negative rate for inhibitory synapses against 11% for
   excitatory. The released table is short by roughly 23% of the estimated
   inhibitory population, so the ratio is biased toward excitation; the authors'
   corrected estimate is 67:33, about 7 percentage points away.

---

## What this page does not cover

- **Synapse biology.** What a synapse is, vesicle pools, active-zone
  architecture, spine types, and how to identify one by eye belong to
  [Synapse classification]({{ '/content-library/neuroanatomy/synapse-classification/' | relative_url }}),
  [Axon biology]({{ '/content-library/neuroanatomy/axon-biology/' | relative_url }})
  and [Dendrite biology]({{ '/content-library/neuroanatomy/dendrite-biology/' | relative_url }}).
- **Neurite segmentation.** Affinity prediction, watershed, agglomeration and
  flood-filling networks are the
  [reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }})
  page's subject, and their error modes are
  [Error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }}).
- **The mathematics of the metrics.** Variation of Information, Expected Run
  Length and the F1 family are derived, with worked arithmetic, in
  [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}).
- **Gap junctions.** Electrical synapses are a genuinely separate detection
  problem; no performance figures are quoted here because none were sourced.
- **Synapse size as a strength proxy.** Cleft and PSD area are used throughout
  the literature to weight edges. Assessing that calibration is a live open
  problem — see
  [Open problems for undergraduate teams]({{ '/content-library/connectomics/open-problems-undergrad/' | relative_url }}),
  Problem 2 — and this page does not evaluate it.
- **Leaderboard standings and the exact CREMI score formula.** No CREMI or
  WASPSYN leaderboard position is quoted; leaderboards move, and the numbers
  here come from papers that can be re-checked. CREMI's metric *family* is
  described above, but the precise weighting that combines components into one
  ranking score was not recovered from the primary source, so none is stated.
- **Compute cost on current hardware.** The only sourced throughput figures —
  Heinrich et al.'s 2018 fly-brain run and SynEM's CPU-hours — predate current
  accelerators by years. Do not plan a budget from them.
- **Non-EM synapse mapping.** Array tomography, expansion microscopy and
  light-microscopy connectomics work from entirely different evidence.

---

## Go deeper

- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }})
  — where this stage sits and what it costs relative to the rest.
- [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }})
  — the metric definitions, including synapse-centric precision and recall.
- [Synapse classification]({{ '/content-library/neuroanatomy/synapse-classification/' | relative_url }})
  — the biology this page presupposes.
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
  — how to pin the synapse table you actually used.
- [H01 human cortex]({{ '/content-library/case-studies/h01-human-cortex/' | relative_url }})
  and [H01, step by step]({{ '/content-library/case-studies/h01-pipeline/' | relative_url }})
  — the volume behind §4 and §5.
- [Journal papers: computer vision and ML]({{ '/content-library/journal-papers/computer-vision-ml/' | relative_url }})
  — the reading list for the methods above.
- [Unit 08: segmentation and proofreading]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
  — the hands-on counterpart.

---

## References

- Becker, C., Ali, K., Knott, G., & Fua, P. (2013). Learning context cues for
  synapse segmentation. *IEEE Transactions on Medical Imaging*.
  [10.1109/TMI.2013.2267747](https://doi.org/10.1109/TMI.2013.2267747)
- Buhmann, J., Sheridan, A., Malin-Mayor, C., Schlegel, P., Gerhard, S.,
  Kazimiers, T., … Funke, J. (2021). Automatic detection of synaptic partners
  in a whole-brain *Drosophila* electron microscopy data set. *Nature Methods*.
  [10.1038/s41592-021-01183-7](https://doi.org/10.1038/s41592-021-01183-7)
- Cano-Astorga, N., Plaza-Alonso, S., Turégano-López, M., Rodrigo-Rodríguez, J.,
  Merchán-Pérez, Á., & DeFelipe, J. (2024). Unambiguous identification of
  asymmetric and symmetric synapses using volume electron microscopy.
  *Frontiers in Neuroanatomy*.
  [10.3389/fnana.2024.1348032](https://doi.org/10.3389/fnana.2024.1348032)
- CREMI: MICCAI Challenge on Circuit Reconstruction from Electron Microscopy
  Images. Data and metric definitions at [cremi.org](https://cremi.org/).
- Dorkenwald, S., Schubert, P. J., Killinger, M. F., Urban, G., Mikula, S.,
  Svara, F., & Kornfeld, J. (2017). Automated synaptic connectivity inference
  for volume electron microscopy. *Nature Methods*.
  [10.1038/nmeth.4206](https://doi.org/10.1038/nmeth.4206)
- Eckstein, N., Bates, A. S., Champion, A. S., Du, M., Yin, Y., Schlegel, P.,
  … Funke, J. (2024). Neurotransmitter classification from electron microscopy
  images at synaptic sites in *Drosophila melanogaster*. *Cell*.
  [10.1016/j.cell.2024.03.016](https://doi.org/10.1016/j.cell.2024.03.016)
- Heinrich, L., Funke, J., Pape, C., Nunez-Iglesias, J., & Saalfeld, S. (2018).
  Synaptic cleft segmentation in non-isotropic volume electron microscopy of
  the complete *Drosophila* brain. *MICCAI*.
  [10.1007/978-3-030-00934-2_36](https://doi.org/10.1007/978-3-030-00934-2_36)
- Huang, G. B., Scheffer, L. K., & Plaza, S. M. (2018). Fully-automatic synapse
  prediction and validation on a large data set. *Frontiers in Neural
  Circuits*.
  [10.3389/fncir.2018.00087](https://doi.org/10.3389/fncir.2018.00087)
- Kreshuk, A., Straehle, C. N., Sommer, C., Koethe, U., Cantoni, M., Knott, G.,
  & Hamprecht, F. A. (2011). Automated detection and segmentation of synaptic
  contacts in nearly isotropic serial electron microscopy images. *PLoS ONE*.
  [10.1371/journal.pone.0024899](https://doi.org/10.1371/journal.pone.0024899)
- Lauenburg, L., Troidl, J., Gohain, A., Lin, Z., Pfister, H., & Wei, D.
  (2025). SynAnno: interactive guided proofreading of synaptic annotations.
  *bioRxiv*.
  [10.1101/2025.08.09.669342](https://doi.org/10.1101/2025.08.09.669342)
- Li, Y., Li, W., Chen, Q., Huang, W., Zou, Y., Xiao, X., … Wu, J. (2024).
  WASPSYN: a challenge for domain adaptive synapse detection in microwasp brain
  connectomes. *IEEE Transactions on Medical Imaging*.
  [10.1109/TMI.2024.3400276](https://doi.org/10.1109/TMI.2024.3400276)
- Mohinta, S., Franco-Barranco, D., Lee, S. Y., & Cardona, A. (2025). Towards
  generalized synapse detection across invertebrate species.
  [arXiv:2509.17041](https://arxiv.org/abs/2509.17041)
- Muth, S., et al. (2024). SynapseNet: deep learning for automatic synapse
  reconstruction.
  [10.1091/mbc.e24-11-0519](https://doi.org/10.1091/mbc.e24-11-0519)
- Park, C., Gim, J., Lee, S., Lee, K. J., & Kim, J. S. (2022). Automated synapse
  detection method for cerebellar connectomics. *Frontiers in Neuroanatomy*.
  [10.3389/fnana.2022.760279](https://doi.org/10.3389/fnana.2022.760279)
- Shapson-Coe, A., Januszewski, M., Berger, D. R., Pope, A., Wu, Y., Blakely,
  T., … Lichtman, J. W. (2024). A petavoxel fragment of human cerebral cortex
  reconstructed at nanoscale resolution. *Science*, 384, eadk4858.
  [10.1126/science.adk4858](https://doi.org/10.1126/science.adk4858)
- Staffler, B., Berning, M., Boergens, K. M., Gour, A., van der Smagt, P., &
  Helmstaedter, M. (2017). SynEM, automated synapse detection for connectomics.
  *eLife*, 6, e26414.
  [10.7554/eLife.26414](https://doi.org/10.7554/eLife.26414)
- Turner, N. L., Lee, K., Lu, R., Wu, J., Ih, D., & Seung, H. S. (2020).
  Synaptic partner assignment using attentional voxel association networks.
  *IEEE ISBI*.
  [10.1109/ISBI45749.2020.9098489](https://doi.org/10.1109/ISBI45749.2020.9098489)
