---
layout: page
title: "Neuron Type Identification"
permalink: /content-library/cell-types/neuron-type-identification/
image: /assets/images/content-library/cell-types/neuron-type-identification.svg
image_alt: "Stylized vector art: three cell silhouettes: branched, star-form, and amoeboid."
description: "How EM connectomics assigns neuron types from morphology, compartment targeting, nucleus and soma features, and connectivity; what FlyWire and MICrONS did; classifier versus manual labels; the Petilla convention; and why the label source belongs in the same sentence as the count."
topics:
  - cell-types
  - morphology
  - classification
  - pyramidal-cells
  - interneurons
  - label-provenance
primary_units:
  - "05"
  - "06"
  - "09"
difficulty: "Advanced"
tags:
  - cell-types:neuron-classification
  - cell-types:morphological-classification
  - cell-types:connectivity-based-classification
  - connectomics:cell-census
  - neuroanatomy:cortical-circuits
  - neuroai:clustering
micro_lesson_id: ml-cell-neuron-types
combines_with:
  - axon-dendrite-classification
  - glia-recognition
  - data-formats
content_type: core
---

## Overview

A wiring diagram of unlabeled nodes explains little. Once each node carries a cell-type
label, you can say which connections are expected (excitatory neurons contacting nearby
neurons) and which are surprising (a rare long-range inhibitory projection). In EM
connectomics, types are inferred from four kinds of evidence: the shape of the arbor,
the compartments an axon targets, the ultrastructure of the nucleus and soma, and the
pattern of synaptic partners. Functional or molecular data help when a dataset has
them.

Every label in a released dataset came from somewhere: an anatomist's call, a
classifier's prediction, or a clustering. This page ends with the reporting rule that
follows: name the label source in the same sentence as the count.

---

## Instructor script: the cell-type classification challenge

### What defines a cell type?

There is no settled definition. In practice, a cell type is a group of neurons that
share morphological, physiological and molecular properties. EM gives you morphology
and connectivity but usually not molecular markers or electrophysiology. MICrONS is a
partial exception: it pairs EM with calcium imaging of about 75,000 neurons (MICrONS
Consortium 2025).

Whole-brain fly data made the definition testable. Schlegel et al. (2024) proposed "a
new definition of cell type as groups of cells that are each quantitatively more
similar to cells in a different brain than to any other cell in the same brain." They
could then check types across two brains. Although "nearly all hemibrain neurons could
be matched morphologically in FlyWire, about one-third of cell types proposed for the
hemibrain could not be reliably reidentified."

Earlier systems relied on light microscopy: Cajal and Lorente de Nó on Golgi-stained
cells, later work on intracellular fills (reviewed in Markram et al. 2004). EM gives
more complete morphology (every branch, every spine), but without the sparse staining
that makes one cell stand out against a blank background.

### Excitatory vs inhibitory is the first split

In mammalian cortex, the first split is:

**Excitatory neurons (the large majority of cortical neurons; the ratio differs by region, layer and species, so take it from the volume you are analyzing and state which you mean):**
- Glutamatergic
- Spiny dendrites (spines are sites of excitatory input)
- Pyramidal morphology in most cases; spiny stellate cells in layer 4 of some primary sensory areas
- Asymmetric (Type I) output synapses
- Project locally and to distant targets (other cortical areas, subcortical structures)

**Inhibitory interneurons (the minority; see Markram et al. 2004 for a review of their diversity):**
- GABAergic
- Smooth (aspiny) or sparsely spiny dendrites
- Diverse morphologies (basket, chandelier, Martinotti, bipolar, neurogliaform and others)
- Symmetric (Type II) output synapses
- Mostly local axons, within the same cortical area (a minority project long-range)

**EM rule of thumb:**
- Spiny dendrites + asymmetric output synapses → excitatory
- Smooth dendrites + symmetric output synapses → inhibitory

This works for most cortical neurons. It fails for sparsely spiny interneurons, and it
assumes that synapse shape predicts transmitter, which is itself an inference (Unit 05
covers the asymmetric/symmetric distinction). Write the assumption into the claim:
"putatively excitatory (spiny, asymmetric outputs)" is the sentence Technical Practice
norm 6 asks for.

---

## How types are assigned in EM: four kinds of evidence

Each kind of evidence needs a different amount of reconstruction, and each fails in a
different way. The MICrONS counts below are version-specific like any other connectome
number: Schneider-Mizell et al. (2025) analyzed their column at materialization version
795 (Data availability), and the released predictions of Elabbady et al. (2025) are the
`aibs_metamodel_celltypes_v661` table, run on features as of version 661 (see the label
table further down).

### 1. Morphology needs a proofread dendrite, and in fly, a second brain

Arbor shape is the classical cue: apical dendrite, laminar position, spines, axon
trajectory. In MICrONS, Schneider-Mizell et al. (2025) described each excitatory
neuron in a 100 µm × 100 µm column with 29 features of morphology and synapse
distribution and ran "an unsupervised consensus clustering of these features,
identifying 18 'morphological types' (M-types)." The M-types "were named by the
dominant expert label," and layer 6 split cleanly: short or inverted apical dendrites
(L6short, consistent with IT) against tall apical and narrow basal dendrites (L6tall,
consistent with CT), with 142 of 143 manually assigned CT cells falling into an L6tall
M-type.

In FlyWire, morphology is compared with NBLAST similarity scores. Schlegel et al.
(2024) "used NBLAST to calculate morphological similarity scores between all hemibrain
neurons and the approximately 84,000 FlyWire neurons with arbours at least partially
contained within the hemibrain volume." The hemibrain's own types began as "5,235
morphology types" from NBLAST clustering, split by connectivity clustering into 5,620.
The limit is spatial: "Standard NBLAST similarity assumes that neurons of the same cell
type overlap closely in space," which "does not hold for repeated columnar neurons such
as those in the optic lobe."

### 2. Compartment targeting classifies an interneuron by where its output lands

"Classical neuroanatomical studies often used the postsynaptic compartments targeted by
an inhibitory neuron as a key feature of its subclass: for example, distinguishing
soma-targeting basket cells from dendrite-targeting Martinotti cells" (Schneider-Mizell
et al. 2025). With every output synapse of an interneuron mapped, that cue becomes a
measurement. Schneider-Mizell et al. defined four subclasses, each "on the basis of its
dominant anatomical property":

| Subclass | Definition (verbatim) | Molecular alignment the authors propose |
|---|---|---|
| PeriTC, perisomatic targeting | "primarily target soma or proximal dendrites" | "soma-targeting cells from multiple molecular subclasses (for example, both PV and CCK+ basket cells)" |
| DistTC, distal dendrite targeting | "primarily target distal basal or apical dendrites" | "SST+ Martinotti and non-Martinotti cells but also any neuron that strongly targets apical dendrites" |
| SparTC, sparsely targeting | "make few multisynaptic connections" | "both neurogliaform cells and all layer 1 interneurons," largely the Id2 class |
| InhTC, inhibitory targeting | "primarily target other inhibitory neurons" | "align well with disinhibitory specialist VIP neurons" |

The labels were assigned by training "a linear classifier on the basis of expert
annotations of the four cardinal subclasses for a subset of inhibitory neurons" and
applying it "to all cells." Compartment targeting needs an axon: the authors
reconstructed "extensive (but incomplete) axonal arbours" for the inhibitory neurons,
after "more than 46,000 edits" of proofreading across the column. Two limits are
stated in the paper. Some types were absent: "some cell types, such as chandelier
cells, had no examples in the column." And the scheme is not a molecular assay: a
PeriTC "would include" PV and CCK basket cells alike.

### 3. Nucleus and soma features classify cells whose arbors you do not have

Most cells in a cubic millimeter are not fully reconstructed. Elabbady et al. (2025)
state the motivation: "even for volumes of cubic millimetre scale, about a third of the
cells are close enough to the edge to have their dendrites truncated," and "a method
that could identify cell types in the dataset in a way that is insensitive to changes
in proofreading and truncation is therefore of high utility." The soma region "is
typically precise and complete" in the automated segmentation, so they built a
classifier on it.

**Features.** Nucleus volume, surface area and their ratio; the area of the nuclear
membrane inside infoldings and its fraction; cortical depth; soma volume, area and
their ratio; the number of synapses on the somatic cutout and their density; the
nucleus-to-soma volume ratio and centroid offset. For inhibitory neurons, they added
distance-binned shape features of the postsynaptic structures within 60 µm of the
nucleus.

**Training labels.** A manually annotated column of 1,619 cells across all layers of
primary visual cortex: 1,115 excitatory neurons, 143 inhibitory neurons and 361
non-neurons, "with expert-annotated labels for cellular classes and neuronal
subclasses."

**Model.** "A hierarchical model that used a cascade of classifiers to sort cells at
increasingly finer distinctions," five classifiers in all: neuron, non-neuron or
segmentation error; excitatory or inhibitory; non-neuronal subclass; excitatory
subclass; inhibitory subclass.

**Accuracy, as reported.** "Across all subclasses, the hierarchical model on the
column had a cross-validated accuracy of 91% and a dataset-wide test set accuracy of
82%." The test set was 1,700 cells: 100 randomly sampled predictions per subclass,
each assessed by anatomical experts. Within the cascade, neuron versus non-neuron
versus error reached 95.6% with soma and nucleus features, non-neuronal classes 97.5%,
excitatory subclasses 90%, and inhibitory subclasses 90%, rising to 94% with the
postsynaptic shape features.

**Scope.** The model "provided classifications for 88% of the cellular objects in the
dataset (94,010/106,761 cells)." The authors' claim is that "the perisomatic region is
sufficient to identify cell types, including types defined primarily on the basis of
their connectivity patterns." They tested it on a rare type: among the 20 nearest
neighbors of one proofread chandelier cell in perisomatic feature space, 16 had
chandelier-like output onto axon initial segments, against none of 20 random
interneurons and none of the 143 column interneurons.

### 4. Connectivity classifies by partners, and can circle back on itself

Even without a full arbor, a neuron with proofread partners has an input fingerprint
(which types provide its synapses, in what proportions) and an output fingerprint
(which types and compartments receive them). Neurons of the same type tend to share
fingerprints, so the connectome graph itself supports clustering. Three cautions:

- **It needs partners proofread to comparable completeness** (Technical Practice
  norm 8). A fingerprint computed against unproofread targets measures reconstruction
  effort as much as biology.
- **It can be circular.** Schlegel et al. (2024) warn that "connectivity-based typing
  is typically used iteratively and especially when used within a single dataset this
  may lead to selection of idiosyncratic features." Their remedy was a second brain:
  cosine similarity of connectivity between matched types across FlyWire and the
  hemibrain was only slightly lower than within a brain (effect size 0.045 ± 0.096).
- **It can be predicted from elsewhere.** Elabbady et al. found that "connectivity
  profile correlates with the perisomatic features we extracted," which is why a
  soma-based classifier can recover connectivity-defined subclasses.

### The four compared

| Evidence | Needs | Used in | Fails when |
|---|---|---|---|
| Morphology | Proofread dendrite; for fine types, the axon | 18 M-types (Schneider-Mizell 2025); NBLAST typing (Schlegel 2024) | Arbor truncated at the volume edge; columnar neurons that do not overlap in space |
| Compartment targeting | An extended axon with output synapses assigned to target compartments | PeriTC / DistTC / SparTC / InhTC (Schneider-Mizell 2025) | Axon incomplete; type absent from the sampled column |
| Nucleus and soma | A complete soma, not cut by the volume edge | 94,010 cells classified (Elabbady 2025) | The 12% of objects that were cut off or erroneous; 18% test-set error dataset-wide |
| Connectivity | Proofread partners on both sides | Linear classifier on cardinal subclasses (Schneider-Mizell 2025); cross-brain cosine similarity (Schlegel 2024) | Partners unproofread; features chosen within one dataset |

Function and molecules, when present, corroborate rather than decide. Orientation
tuning from calcium imaging is shared by many excitatory and inhibitory types, so it
narrows nothing on its own.

---

## Morphological classification in EM

### Pyramidal neurons

The most common excitatory neuron in cortex (layers 2-6):

**Identification cues:**
- **Soma**: triangular or pyramidal in 3D, which is harder to see in a single section cut at an arbitrary angle. Size varies with layer and subtype; measure it in your volume rather than borrowing a range.
- **Apical dendrite**: one thick, spiny dendrite rising from the apex of the soma toward the pia, with oblique branches along the way. In many pyramidal cells it ends in a tuft in layer 1; in layer 6 corticothalamic cells it usually stops lower (see the table). It is the most distinctive feature of the type.
- **Basal dendrites**: several spiny dendrites leaving the base of the soma and branching locally.
- **Axon**: leaves the base of the soma (or a proximal basal dendrite) and heads toward the white matter; it is often myelinated. Local collaterals make synapses nearby.

**Subtype classification by layer and projection:**

| Subtype | Layer | Projection target | EM distinguishing features |
|---------|-------|-------------------|---------------------------|
| Layer 2/3 pyramidal | 2/3 | Other cortical areas (callosal, associational) | Medium soma, prominent apical reaching L1 |
| Layer 4 spiny stellate | 4 (in some primary sensory areas) | Local (within column) | Stellate dendrites (no clear apical), heavily spiny |
| Layer 5 thick-tufted (ET) | 5 | Subcortical (thalamus, brainstem, spinal cord) | Large soma, thick apical with prominent L1 tuft, thick axon |
| Layer 5 thin-tufted (IT) | 5 | Other cortical areas | Smaller soma, thinner apical, less prominent tuft |
| Layer 6 corticothalamic | 6 | Thalamus | Short apical that usually ends in L4, not L1 |

Projection targets in this table come from tracing studies, not from the EM volume.
In a 1 mm³ volume most long-range axons leave the block, so the EM supports the layer
and shape columns; the target column is an inference. Schneider-Mizell et al. (2025)
compared their M-types with "expert labels of layer and long-range projection type"
(IT, ET, NP, CT) for the same reason: the projection label is prior knowledge attached
to a shape, not a measurement in the volume.

### Inhibitory interneuron types

Inhibitory neurons are far more varied in shape. The types most often recognized in EM:

**Basket cells (usually PV+):**
- Smooth or sparsely spiny dendrites
- Axon wraps target somata in basket-like arrays of boutons (perisomatic synapses)
- Symmetric synapses onto the soma and proximal dendrites of pyramidal cells and of other interneurons
- Fast-spiking, if electrophysiology is available
- EM cue: symmetric synapses concentrated on somata

**Chandelier cells (often PV+):**
- Axon terminals form "cartridges": vertical rows of boutons along the axon initial segment (AIS) of pyramidal cells
- The only interneuron type that targets the AIS this selectively
- EM cue: strings of symmetric synapses on an AIS, which you recognize by the dense undercoating of its membrane and its fasciculated microtubules

**Martinotti cells (SST+):**
- Found in layers 2–6, most often in layer 5
- Ascending axon that branches in layer 1 and synapses on distal dendritic tufts
- EM cue: an axon climbing to layer 1 with symmetric synapses on distal dendrites

**Bipolar/VIP+ cells:**
- Elongated soma with two main dendritic trunks running vertically (up and down)
- Narrow axonal arbor that often targets other interneurons
- EM cue: bipolar dendrites and output concentrated on interneurons

**Neurogliaform cells:**
- Small soma with a dense local axonal arbor
- A single cell releases enough GABA to act by volume transmission within its axonal cloud, without needing synapses (Oláh et al. 2009)
- EM cue: a dense, fine local axon cloud. Do not expect every bouton to face a clear postsynaptic partner, and do not count "missing" partners as a detection failure

### The Petilla convention: name the features, then the type

The names above carry molecular claims (PV+, SST+, VIP+) that EM cannot check. The
Petilla Interneuron Nomenclature Group (Ascoli et al. 2008) addressed this for the
whole field. "Cortical interneurons are typically described and classified according to
various morphological, molecular and physiological features," and the group proposed
"a standardized nomenclature of interneuron properties" so that those features are
reported the same way everywhere. The scope is stated exactly: "the nomenclature
proposed does not attempt to give names to different classes of interneurons; instead,
it defines the features that can be used for their identification." Familiar names
such as basket and chandelier are used "for ease of reference and illustration."

Two Petilla feature descriptions map directly onto EM. On axonal terminals:
"'Clustered' terminal branches are often seen in chandelier or axo-axonic cells that
innervate pyramidal-cell axon initial segments." On basket cells: "Typically, large
basket cell boutons establish multiple axo-somatic contacts on other neurons." Those
are the cues you can measure. The molecular half of the description (PV, calbindin,
CCK, somatostatin) is not in the volume.

The convention for an EM label, then, is to state the measured features and mark the
rest as inference: "perisomatic-targeting interneuron (PeriTC; 55% of output onto
somata), putatively a PV+ basket cell." Schneider-Mizell et al. (2025) followed this
logic when they named subclasses after targeting rather than after markers, and noted
which molecular classes each subclass "would include." Write the label the same way in
a figure legend. "PV basket cell" from EM alone is the different, stronger claim that
Technical Practice norm 6 warns against.

---

## Connectivity-based classification

### The connectivity fingerprint

Even without morphological reconstruction, neurons can be classified by their
connectivity pattern alone:

- **Input fingerprint**: Which cell types provide synaptic input, and in what proportions?
- **Output fingerprint**: Which cell types receive synaptic output, and onto which compartments?

Neurons of the same type tend to have similar connectivity fingerprints. This allows
clustering-based classification using the connectome graph directly.

### Methods

1. **Feature engineering**: For each neuron, compute: in-degree, out-degree, fraction of input from excitatory vs inhibitory sources, fraction of output onto soma vs dendrites, laminar distribution of inputs/outputs.
2. **Dimensionality reduction**: PCA, UMAP, or t-SNE on the feature vectors.
3. **Clustering**: K-means, hierarchical clustering, or Gaussian mixture models on the reduced representation.
4. **Validation**: Compare to morphological types (where known) or molecular markers (if available from correlative data), and, where a second volume exists, to the same types there.

### FlyWire: 8,453 types from morphology, connectivity and a second brain

Schlegel et al. (2024) annotated the FlyWire whole-brain connectome (Dorkenwald et al.
2024) in a hierarchy: "flow > superclass > class > cell type." The first two levels
are dense: "every neuron is either afferent, efferent or intrinsic to the brain (flow)
and falls into one of the nine superclasses." Between class and type sits the
developmental unit, the hemilineage; they "identified 120 neuroblast lineages in
FlyWire comprising 183 hemilineages for 88% (30,233 total) of central brain neurons."
Cell types were then assigned by combining:

- Morphological similarity (NBLAST), within FlyWire and against the hemibrain
- Connectivity, on the assumption "that homologous neurons share synaptic partners"
- Expert review and the existing hemibrain type names
- Matching across three hemispheres: the left and right of FlyWire, and the hemibrain

The result: "Of 8,453 annotated cell types, 3,643 were previously proposed in the
partial hemibrain connectome, and 4,581 are new types, mostly from brain regions
outside the hemibrain subvolume." Types cover "96.4% of all neurons in the brain—98%
and 92% for the central brain and optic lobes, respectively." The comparison across
brains is what lets them test a type rather than just name it: they treated "each cell
type in the hemibrain as a prediction: if we can reidentify a distinct group of cells
with the same properties in both hemispheres of the FlyWire dataset, then we conclude
that a proposed hemibrain cell type has been tested and validated." Under that test,
"1,651 (32%) hemibrain cell types could not be reidentified in FlyWire," and the
3,584 that were reidentified "map onto 3,643 consensus cell types."

### MICrONS: two routes to cell types

In the MICrONS cubic millimeter of mouse visual cortex, two 2025 *Nature* papers take
two routes, described in detail above:

- Elabbady et al. (2025) classified 94,010 cells from features of the nucleus and soma
  region, trained on 1,619 manually labeled column cells. Perisomatic features are
  enough to identify cell types, including types defined mainly by connectivity, and
  they work for cells whose arbors are cut off.
- Schneider-Mizell et al. (2025) reconstructed "a continuous population of 1,352
  neurons in a column spanning from layer 1 to white matter," classifying all 1,886
  cells in the column "as excitatory neurons, inhibitory neurons or non-neuronal cells
  on the basis of morphology." They classified 163 analyzed interneurons by the
  compartments they target and excitatory neurons into 18 M-types, over a wiring
  diagram that "included 70,884 synapses from inhibitory neurons onto excitatory
  neurons."

### Worked example: typing from a connectivity fingerprint

This example uses a synthetic release, **"Aspen"**, with invented cells and counts. It is
not drawn from any real dataset.

In Aspen, four interneurons (IN-a to IN-d) have proofread axons, and every output
synapse is labeled with the compartment it lands on:

| Cell | Output synapses | Onto soma | Onto proximal dendrite | Onto distal dendrite / tuft | Onto AIS |
|---|---|---|---|---|---|
| IN-a | 400 | 220 | 140 | 40 | 0 |
| IN-b | 350 | 200 | 120 | 30 | 0 |
| IN-c | 300 | 10 | 30 | 260 | 0 |
| IN-d | 120 | 0 | 0 | 0 | 120 |

As fractions of each cell's output, IN-a is 55% soma and 35% proximal, IN-b 57% and
34%, IN-c 87% distal, and IN-d 100% AIS. IN-a and IN-b share a perisomatic fingerprint
(PeriTC in the Schneider-Mizell scheme; basket-like). IN-c fits a distal-targeting,
Martinotti-like profile (DistTC). IN-d targets only the AIS, the chandelier signature.

What the table does not show: whether IN-a and IN-b are one type or two. Two cells
cannot settle that. You need enough cells to see whether the fingerprints form separate
clusters or a continuum, and ideally a match in a second volume.

---

## Classifier labels and manual labels: report which one you used

A released dataset carries several label tables, made by different methods, on
different subsets of cells. The MICrONS annotation-table reference (read 27 September
2026) documents the three that matter most, and the differences are the point:

| Table | Method, as documented | Cells | What the documentation warns |
|---|---|---:|---|
| `allen_v1_column_types_slanted_ref` | "A subset of nucleus detections in a 100 um column (n=2204) in VISp were manually classified by anatomists at the Allen Institute into categories of cell subclasses" | 1,357 neuron reference annotations | An "Unsure" inhibitory label "is used for all likely-inhibitory neurons that did not match other types" |
| `aibs_metamodel_celltypes_v661` | "a hierarchical classifier trained on features of the cell body and nucleus of cells," trained on the manual tables above; "run with cell-based features as of version 661 of the dataset" (Elabbady et al. 2025) | 94,014 | "sometimes confuses layer 5 inhibitory neurons as being excitatory" |
| `baylor_log_reg_cell_type_coarse_v1` | "a logistic regression classifier trained on properties of neuronal dendrites" (Celii et al. 2025) | 55,063 | "required more data than soma and nucleus features alone and thus more cells did not complete the pipeline"; "a good table to double check E/I classifications" |

Two more facts from the same reference. The `v661` in a table name records the
materialization whose features the model was run on, not the version you are querying.
And corrections are "living" tables: the `aibs_metamodel_mtypes_v661_v2_corrections`
table adds cells "as more changes arise from continued manual efforts and evolving
automated methods" (v1718 release manifest). "Both corrections tables are hierarchically
incorporated in the super view of cell type: `aibs_cell_info`" (same manifest), and the
static export of that view carries a `broad_type_source` column naming where each
cell's label came from.

### What the site's lab found

The [MICrONS real-data lab]({{ '/notebooks/microns-lab/' | relative_url }}) reads the
v1507 export of `aibs_cell_info` and keeps 2,070 proofread cells. Its executed notebook
prints where each cell's excitatory/inhibitory label came from:

| `broad_type_source` | Cells |
|---|---:|
| `allen_v1_column_types_slanted_ref` (manual) | 1,341 |
| `baylor_log_reg_cell_type_coarse_v1` (classifier, dendritic features) | 598 |
| `aibs_metamodel_celltypes_v661` (classifier, soma and nucleus features) | 127 |
| `aibs_metamodel_celltypes_v661_corrections` (manual correction) | 4 |

So 1,345 of the 2,070 labels are manual (1,341 column reference calls, 65%, plus 4
corrections) and 725 are classifier predictions. The
lab treats neither as ground truth, and its limitations section says what a wrong
label does to the analysis: it "moves a cell's pairs into the wrong null stratum."

### The rule: the label source goes in the same sentence as the count

A count of cells by type is a count of labels, and a label is a measurement with a
source, a version and an error rate. Write them together.

- **Too little:** "The graph contained 1,732 excitatory and 338 inhibitory neurons."
- **Enough:** "The graph contained 1,732 excitatory and 338 inhibitory neurons by
  `broad_type` in the v1507 `aibs_cell_info` view, where 1,341 labels are manual column
  reference calls (`allen_v1_column_types_slanted_ref`), 4 are manual corrections, and
  725 are classifier predictions (`baylor_log_reg_cell_type_coarse_v1`, 598;
  `aibs_metamodel_celltypes_v661`, 127)."

The second sentence is longer by one clause and answers the three questions a reader
will otherwise have to ask: who labeled, at what version, and how much of the count
rests on a model. When a classifier's published accuracy is known, add it: for the
hierarchical model, 82% on a dataset-wide test set of 1,700 expert-checked cells
(Elabbady et al. 2025). Where the count is a headline result, rerun it on the manual
subset and say what changed, the same move Technical Practice norm 19 asks for with
confidence tiers.

---

## Worked example: classifying a neuron in layer 2/3

**Given:** A fully reconstructed neuron in layer 2/3 of mouse visual cortex.

**Step 1: Excitatory or inhibitory?**
- Dendrites: densely spiny → excitatory
- Output synapses: asymmetric (thick PSD, round vesicles) → excitatory, by a second, independent cue

**Step 2: Morphological subtype**
- Soma: triangular, ~15 μm diameter, in layer 2/3
- One prominent apical dendrite ascending toward layer 1, with terminal tuft
- 5 basal dendrites extending laterally
- Axon: descends from soma base, sends collaterals in layers 2/3 and 5, main axon continues toward white matter
→ **Layer 2/3 pyramidal cell**

**Step 3: Connectivity check** (invented counts for this example cell, whose arbor is cut off by the volume edge; a complete layer 2/3 pyramidal cell receives thousands of synapses, so counts this low are themselves a sign of truncation)
- Receives ~200 excitatory synapses (mostly on spines from other L2/3 and L4 neurons)
- Receives ~50 inhibitory synapses (mostly on soma and proximal dendrites from basket cells)
- Makes ~300 excitatory synapses on nearby L2/3 and L5 neurons
→ Connectivity profile consistent with L2/3 pyramidal cell

**Step 4: Functional data (if available)**
- Calcium imaging shows orientation-selective responses to visual stimuli
→ Consistent with a layer 2/3 cell in visual cortex, but weak evidence for type: many excitatory and inhibitory neurons in V1 are orientation-selective

**Classification:** Layer 2/3 pyramidal neuron. Confidence: **high**, from spines,
asymmetric outputs, an apical dendrite and laminar position. Source: manual, from the
reconstruction, not from a classifier table. Projection target: **unknown**. An axon
heading for the white matter fits a callosal or an ipsilateral cortico-cortical
projection, and the volume cannot tell the two apart.

---

## Challenges and limitations

### Incomplete reconstructions

Most neurons in a connectomics volume are not fully reconstructed: their axons or
dendrites leave the imaged block. Elabbady et al. (2025) put a number on the edge
effect alone: "about a third of the cells are close enough to the edge to have their
dendrites truncated." A call from partial morphology is less reliable. Record which
parts you had, weight the call accordingly, and flag the cell as incomplete.
Perisomatic features are one way to type cells whose arbors are cut off, at the
accuracy stated above.

### Continuous variation

Some types grade into each other rather than forming clean clusters. In more than
1,300 Patch-seq neurons from mouse motor cortex, Scala et al. (2021) found that broad
families (Pvalb, Sst, Vip and so on) had distinct, non-overlapping morpho-electric
phenotypes, but neighboring transcriptomic types within a family formed a continuum
without clear boundaries. Whether to split one group into two, or keep one type with
variation, depends on the analysis question. Say which you chose and why.

### Species differences

Taxonomies built in mouse may not carry over to human or fly. The same feature can
mark different types in different species, so comparing across species needs explicit
homology mapping.

### Labels are versioned

A classifier table is run at one materialization and served at later ones; a
corrections table grows. The label a cell carries can change while its nucleus ID does
not. Record the table, the version and the source per cell, as the
[provenance page]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
describes for every other annotation.

---

## Check yourself

<details markdown="1">
<summary>A methods section says "inhibitory neurons (n = 338) were identified using the MICrONS cell-type table." Which questions can you not answer from that sentence?</summary>

Which table (there are at least three, made by different methods on different cells);
which version; and how many of the 338 are manual calls versus classifier predictions.
The lab's own count is the fix: 338 inhibitory by `broad_type` in the v1507
`aibs_cell_info` view, with the per-source split printed. Without the split you cannot
rerun the headline on the manual subset, so you cannot tell whether the result depends
on classifier error.
</details>

<details markdown="1">
<summary>An interneuron in a new volume puts 60% of its output onto somata and proximal dendrites. Your collaborator wants to call it a PV basket cell. What is the defensible label?</summary>

A perisomatic-targeting interneuron (PeriTC in the Schneider-Mizell scheme), putatively
a basket cell. PV is a molecular claim the volume cannot test, and Schneider-Mizell et
al. note that PeriTCs "would include" both PV and CCK basket cells. The Petilla
convention is to report the measured features (targeting, bouton arrangement) and mark
the marker as inference. Also check the axon's completeness: a targeting fraction from
a partially extended axon is a property of the reconstruction as well as the cell.
</details>

<details markdown="1">
<summary>Why did Schlegel et al. treat a hemibrain cell type as a "prediction," and what fraction failed the test?</summary>

Because a type defined in one brain is a claim that the same distinct group of cells
will exist in another. FlyWire supplied two more hemispheres to test it in. A hemibrain
type counted as validated only if "a distinct group of cells with the same properties"
could be reidentified in both FlyWire hemispheres. 1,651 hemibrain types, 32%, could
not be reidentified, even though nearly all individual hemibrain neurons could be
matched by morphology. The lesson transfers to mouse: a type named in one column is a
prediction about the next column.
</details>

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "Cell types are discrete and obvious" | Many neurons fall on continua between types (Scala et al. 2021), and 32% of hemibrain types could not be reliably re-identified in a second brain (Schlegel et al. 2024) | Report classification confidence and criteria |
| "Morphology alone is sufficient" | Molecular markers and physiology can distinguish types that look similar in EM | Use all available evidence; flag morphology-only classifications |
| "A classifier label is a measurement" | It is a prediction with a stated accuracy: 82% on the dataset-wide test set for the MICrONS hierarchical model (Elabbady et al. 2025) | Name the table and the source in the same sentence as the count |
| "PV+, SST+ and VIP+ are EM labels" | EM measures targeting and morphology; the marker is inferred (Petilla convention) | Write "perisomatic-targeting, putatively PV+" |
| "The same types exist in all species" | Cell-type diversity varies across species and regions | Don't assume mouse taxonomy applies to fly or human |
| "More types = better classification" | Over-splitting creates types with too few members for statistical analysis | Balance granularity with statistical power |
| "Orientation tuning (or any single functional property) identifies the type" | Many excitatory and inhibitory cells share the same tuning | Use function as corroboration, not as the deciding cue |

---

## Related

- [Axon-dendrite classification]({{ '/content-library/cell-types/axon-dendrite-classification/' | relative_url }}), the process-level call that precedes a cell-type call
- [Glia recognition]({{ '/content-library/cell-types/glia-recognition/' | relative_url }}), the non-neuronal branch of the same hierarchy
- [Soma ultrastructure]({{ '/content-library/neuroanatomy/soma-ultrastructure/' | relative_url }}), the features Elabbady et al. measured
- [Synapse classification]({{ '/content-library/neuroanatomy/synapse-classification/' | relative_url }}), asymmetric and symmetric synapses
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}), why label tables carry a version
- [MICrONS real-data lab]({{ '/notebooks/microns-lab/' | relative_url }}), the label-source counts quoted above
- [Cell types and morphology reading list]({{ '/content-library/journal-papers/cell-types/' | relative_url }}), the three papers at three reading levels
- [MICrONS visual cortex]({{ '/content-library/case-studies/microns-visual-cortex/' | relative_url }}) and [FlyWire whole brain]({{ '/content-library/case-studies/flywire-whole-brain/' | relative_url }})
- [Technical Practice]({{ '/hidden-curriculum/technical-practice/' | relative_url }}), norms 6, 8 and 19
- [Unit 05: Neuronal ultrastructure]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}) and [Unit 06: Axons and dendrites]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }})

---

## References

- Ascoli GA, Alonso-Nanclares L, Anderson SA, et al. (Petilla Interneuron Nomenclature Group) (2008) "Petilla terminology: nomenclature of features of GABAergic interneurons of the cerebral cortex." *Nature Reviews Neuroscience* 9(7):557-568. [10.1038/nrn2402](https://doi.org/10.1038/nrn2402). PMC2868386.
- Celii B, Papadopoulos S, Ding Z, et al. (2025) "NEURD offers automated proofreading and feature extraction for connectomics." *Nature* 640:487-496. [10.1038/s41586-025-08660-5](https://doi.org/10.1038/s41586-025-08660-5).
- DeFelipe J, Fariñas I (1992) "The pyramidal neuron of the cerebral cortex: morphological and chemical characteristics of the synaptic inputs." *Progress in Neurobiology* 39(6):563-607.
- DeFelipe J et al. (2013) "New insights into the classification and nomenclature of cortical GABAergic interneurons." *Nature Reviews Neuroscience* 14(3):202-216.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634:124-138.
- Elabbady L, Seshamani S, Mu S, et al. (2025) "Perisomatic ultrastructure efficiently classifies cells in mouse cortex." *Nature* 640(8058):478-486. [10.1038/s41586-024-07765-7](https://doi.org/10.1038/s41586-024-07765-7). PMC11981918.
- Harris KD, Shepherd GMG (2015) "The neocortical circuit: themes and variations." *Nature Neuroscience* 18(2):170-181.
- Markram H et al. (2004) "Interneurons of the neocortical inhibitory system." *Nature Reviews Neuroscience* 5(10):793-807.
- MICrONS Consortium et al. (2025) "Functional connectomics spanning multiple areas of mouse visual cortex." *Nature* 640:435-447. [10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w)
- MICrONS Explorer tutorial, "Annotation Tables" (<https://tutorial.microns-explorer.org/annotation-tables.html>) and the v1718 release manifest, read 27 September 2026.
- Oláh S et al. (2009) "Regulation of cortical microcircuits by unitary GABA-mediated volume transmission." *Nature* 461:1278-1281. [10.1038/nature08503](https://doi.org/10.1038/nature08503)
- Scala F et al. (2021) "Phenotypic variation of transcriptomic cell types in mouse motor cortex." *Nature* 598:144-150. [10.1038/s41586-020-2907-3](https://doi.org/10.1038/s41586-020-2907-3)
- Schlegel P, Yin Y, Bates AS, et al. (2024) "Whole-brain annotation and multi-connectome cell typing of *Drosophila*." *Nature* 634(8032):139-152. [10.1038/s41586-024-07686-5](https://doi.org/10.1038/s41586-024-07686-5). PMC11446831.
- Schneider-Mizell CM, Bodor AL, Brittain D, et al. (2025) "Inhibitory specificity from a connectomic census of mouse visual cortex." *Nature* 640(8058):448-458. [10.1038/s41586-024-07780-8](https://doi.org/10.1038/s41586-024-07780-8). PMC11981935.
- Turner NL et al. (2022) "Reconstruction of neocortex: Organelles, compartments, cells, circuits, and activity." *Cell* 185(6):1082-1100.
- Zeng H, Sanes JR (2017) "Neuronal cell-type classification: challenges, opportunities and the path forward." *Nature Reviews Neuroscience* 18(9):530-546.
