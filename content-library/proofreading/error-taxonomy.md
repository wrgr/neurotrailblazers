---
layout: page
title: "Error Taxonomy in Connectome Proofreading"
permalink: /content-library/proofreading/error-taxonomy/
image: /assets/images/content-library/proofreading/error-taxonomy.svg
image_alt: "Stylized vector art: a traced process with marked error sites under review."
description: >
  A comprehensive reference on the types of errors found in automated neural
  segmentation, their causes, downstream consequences, visual signatures, and
  relative frequency. Includes worked identification examples and common
  misconceptions.
topics:
  - merge errors
  - split errors
  - boundary errors
  - identity errors
  - error frequency
  - segmentation quality
  - downstream impact
primary_units:
  - "08"
difficulty: intermediate
tags:
  - proofreading:merge-error
  - proofreading:split-error
  - proofreading:boundary-error
  - proofreading:identity-error
  - connectomics:segmentation
  - methodology:qa-metrics
  - imaging:electron-microscopy
micro_lesson_id: ml-proof-errors
combines_with:
  - proofreading-strategies
  - proofreading-tools
  - metrics-and-qa
  - worked-examples
use_layout_hero: false
content_type: core
---

# Error Taxonomy in Connectome Proofreading

## Instructor Notes

This is a standalone instructor script: narrative, references, worked
examples and a misconceptions table. Cut depth and pacing to suit the
room. The worked examples in §§2–5 are set in **release T76 of a fictional
mouse cortex volume**; their section numbers and measurements are invented
for teaching. The two H01 figures are real data and are labeled as such.

---

## 1. Why Errors Matter

### 1.1 The Scale Problem

Automated segmentation is now very good on benchmarks. Lee et al. (2017)
reported "superhuman" accuracy on the SNEMI3D segmentation challenge. Yet
even a small per-edge error rate becomes a near-certain error per neuron at
connectome scale.

**Key calculation to present on the board:**

Consider a neuron whose arbor passes through 1,000 supervoxel-to-supervoxel
edges in the segmentation graph. If each edge has a 1 % probability of
being wrong, the probability that the neuron is completely error-free is:

    P(no error) = (1 - 0.01)^1000 = 0.99^1000 ≈ 0.000043

That is a 99.996% chance of at least one error somewhere along the neuron.
Even at a 0.1% per-edge error rate, the probability of a fully correct
neuron with 1,000 edges is only about 37% (0.999^1000 ≈ 0.368).

What the calculation does not show: it assumes errors are independent and
equally likely on every edge, and the 1,000 edges and the error rates are
round numbers for the board, not measurements. Real errors cluster at thin
processes and bad sections, so some neurons come out clean and others
carry many errors.

**Instructor tip:** Do this calculation live. It shows in two lines why
proofreading is still needed after a "superhuman" benchmark score.

### 1.2 Errors Are Not Equally Harmful

A boundary shifted by two voxels matters much less than a merge that fuses
two excitatory neurons into one. The sections below run merge, split,
boundary, identity. That order is not a frequency ranking: §6 explains why
no field-wide frequency ranking exists. It is roughly the order in which
each type corrupts connectome analyses in practice, although a single
identity error can be as damaging as a merge.

---

## 2. Merge Errors

### 2.1 Definition

A merge error occurs when two or more distinct neurons are incorrectly
joined into a single segment by the automated pipeline. In the supervoxel
graph representation, this means there is at least one false edge linking
supervoxels that belong to different ground-truth neurons.

### 2.2 Causes

| Cause | Mechanism | Typical context |
|---|---|---|
| Close membrane apposition | The gap between two membranes is only a voxel or two wide, or is blurred across a thick section, so the boundary signal is weak | Parallel axons in dense neuropil |
| Low staining contrast | Membrane signal drops, model cannot distinguish boundary | Poor fixation regions, section edges |
| Blood vessel boundaries | Vessel endothelium creates a false membrane-like boundary that "bridges" two neurites | Capillaries running through neuropil |
| Glial wrapping | Thin astrocytic processes wrap around neurites; model confuses glial membrane for neuronal continuity | Perisynaptic astrocyte processes |
| Alignment artifacts | Section-to-section registration errors shift a membrane out of alignment, creating an apparent connection | Regions with tissue folds or tears |

### 2.3 Downstream Impact

- **Connectivity graph corruption:** A merge between neuron A and neuron B
  means every synapse onto A is also attributed to B and vice versa. The
  connectivity matrix gains false edges.
- **Inflated morphological statistics:** Cell volume, total cable length,
  and branch count are all overestimated for the merged segment.
- **Artificial motifs:** Network motif analysis (e.g., reciprocal
  connections, feed-forward triplets) can produce false positives when
  merges create phantom connections.

### 2.4 Visual Signatures

- **Implausible branching in 3D:** Two large branches leaving a point in
  opposite directions, with mismatched caliber, deserve a look in 2D. The
  angle alone is not proof: some real branches are T-shaped (cerebellar
  granule-cell axons split into parallel fibers running in opposite
  directions).
- **Sudden caliber changes:** If a 500-nm-diameter dendrite suddenly
  becomes a 100-nm axon at a branch point, suspect a merge.
- **Biologically implausible morphology:** A segment that crosses brain
  region boundaries it should not, or that has an impossibly large arbor
  for its cell type.

### 2.5 Worked Example: Identifying a Merge Error

1. You are examining a 3D mesh of a putative pyramidal cell in release T76.
2. The cell has a normal-looking apical dendrite, but one basal branch
   suddenly changes caliber from ~400 nm to ~120 nm and takes a sharp
   90-degree turn.
3. You navigate to the turn point in 2D (XY) slices.
4. From z = 311 to z = 315 you see two profiles side by side. A faint
   membrane separates them in z = 311, 312, 314 and 315. In z = 313 the
   membrane is not visible and both profiles carry one label.
5. Diagnosis: merge error caused by a one-section gap in membrane signal.
6. Action: split at the merge point.
7. Verification: after splitting, each segment has consistent caliber and
   biologically plausible trajectory.

---

{% include figure.html
   src="/assets/images/content-library/em/segmentation-c2-vs-c3.jpg"
   alt="The same field of human cortex shown twice with segmentation overlaid: on the left the c2 agglomeration labels a region as one object in purple; on the right the c3 agglomeration splits the same region into two objects in red and blue."
   caption="The merge/split trade-off, on one real object. H01 ships two agglomerations of the same segmentation: aggressive <strong>c2</strong> (left) calls this region <em>one</em> object; conservative <strong>c3</strong> (right) calls it <em>two</em>. Neither is a bug. On 104 randomly selected neurons proofread in both, c3 needed 1.6-fold fewer merge corrections (257 vs 400 per cell) and 2.1-fold more split corrections (504 vs 238 per cell) than c2 (Shapson-Coe et al. 2024). The merge/split ratio is a setting the pipeline chooses, and this is what changing it looks like."
   credit="H01 human cortex, Lichtman Lab (Harvard) &amp; Connectomics at Google, CC BY 4.0. Shapson-Coe et al., <em>Science</em> 384, eadk4858 (2024). Rendered by <code>scripts/render_em_figures.py</code>." %}

## 3. Split Errors

### 3.1 Definition

A split error occurs when a single neuron is broken into two or more
disconnected segments. In the supervoxel graph, a true edge is missing.

### 3.2 Causes

| Cause | Mechanism | Typical context |
|---|---|---|
| Thin processes | A thin axon is only a few voxels across at segmentation resolution, so one faint or misaligned section can break it | Small-caliber axons in cortical neuropil |
| Low contrast regions | Membrane signal too faint for model confidence | Same as merge causes, but model errs conservatively |
| Missing or damaged sections | Physical section lost during collection | Any region; creates a gap in z |
| Sharp turns in z | A process that curves sharply between sections appears to "jump" in xy | Ascending/descending axons |
| Alignment errors | Misregistration makes a continuous process appear discontinuous | Tissue fold boundaries |

### 3.3 Downstream Impact

- **Missing connections:** If a neuron is split, synapses on the
  disconnected fragment are attributed to an orphan segment rather than the
  parent neuron. The connectivity matrix loses true edges.
- **Underestimated arbor:** Cable length, branch count, and volume are all
  underestimated.
- **Inflated cell counts:** Each fragment may be counted as a separate
  neuron in census analyses.

### 3.4 Visual Signatures

- **Dead-end processes:** A neurite that stops flat, inside the volume,
  often at a bad section. Real neurites do end (dendritic tips, axon
  terminals), but a real ending tapers or finishes in a bouton with
  vesicles.
- **Orphan fragments:** Small segments near the dead end that match in
  caliber and trajectory.
- **Size distribution anomalies:** An excess of very small segments in a
  region suggests widespread splitting.

### 3.5 Worked Example: Identifying a Split Error

1. You are tracing a descending axon from a layer 2/3 pyramidal cell in
   release T76.
2. At z = 487, the axon segment ends abruptly. There is no terminal bouton.
3. You scroll to z = 488. Section 488 is visibly damaged (knife mark across
   the tissue). The axon profile is not segmented in this section.
4. At z = 489, a small orphan fragment appears at approximately the same
   (x, y) position, with matching caliber (~130 nm) and trajectory.
5. Diagnosis: split error caused by a damaged section.
6. Action: merge the upstream segment with the downstream fragment.
7. Verification: the merged segment has smooth, continuous trajectory
   across the damaged section.

---

## 4. Boundary Errors

### 4.1 Definition

A boundary error occurs when the membrane position is shifted relative to
ground truth, causing partial volume sharing between adjacent segments.
Neither segment is topologically wrong (no false merge, no false split),
but the exact border is inaccurate.

### 4.2 Impact

- **Synapse misassignment:** A synapse located near the true membrane may
  be attributed to the wrong neuron if the predicted boundary is shifted by
  even 2-3 voxels. This is especially problematic for small synapses with
  tight postsynaptic compartments (e.g., spine heads).
- **Morphology distortion:** Measurements of neurite diameter, spine
  volume, and organelle distribution are corrupted.
- **Silent corruption:** Unlike merge/split errors, boundary errors rarely
  produce dramatic visual signatures. They tend to be discovered only when
  quantitative measurements disagree with expectations.

### 4.3 Worked Example

1. You are measuring spine head volumes for a population of excitatory
   synapses in release T76. Several spine heads have volumes 30–40% larger
   than expected.
2. On inspection, the segmentation boundary around those spines extends
   2-3 voxels into the adjacent dendritic shaft or into the presynaptic
   bouton.
3. Diagnosis: boundary error. The spine volume is inflated by the extra
   voxels.
4. Action: manual boundary correction or exclude affected spines from
   quantitative analysis.

---

## 5. Identity Errors

### 5.1 Definition

An identity error occurs when the segmentation boundary is correct, but
the cell label assigned to a region is wrong. This typically happens as a
side effect of proofreading itself: when a merge is split, the two
resulting fragments must each receive a label, and the wrong label may be
propagated to the wrong fragment. In CAVE-based systems both fragments get
new root IDs, and a cell's identity follows whichever fragment holds its
annotation point (its soma or cell-type point), so a point on the wrong
side carries the identity with it.

### 5.2 Impact

- **Catastrophic for connectivity:** Every synapse in the mislabeled region
  is attributed to the wrong neuron. If the mislabeled region is large,
  this can completely corrupt the connectivity profile of two neurons.
- **Hard to detect:** Because the boundary looks correct, the
  error is invisible in standard 2D or 3D inspection. It is usually
  discovered only when downstream connectivity analysis produces
  impossible results (e.g., a known inhibitory neuron appearing to make
  excitatory synapses).

### 5.3 Worked Example

1. In release T76, after splitting a merge between neuron A (inhibitory basket cell) and
   neuron B (excitatory pyramidal cell), the proofreader assigns the
   perisomatic basket terminals to neuron B by mistake.
2. Downstream analysis flags neuron B as making an unusual number of
   perisomatic synapses, inconsistent with pyramidal cell biology.
3. Re-inspection reveals the identity swap.
4. Action: reassign the segment to neuron A.

---

## 6. Relative Frequency and Impact Hierarchy

**There is no field-wide error frequency distribution, and you should be
suspicious of any table that offers one.** The merge/split ratio is not a
property of connectomics; it is an *output* of the agglomeration threshold,
which the pipeline sets. A conservative threshold (merge only when very sure)
produces more splits and fewer merges; an aggressive one does the reverse.
H01 measured this directly: on the same 104 neurons, the conservative c3
agglomeration needed 1.6-fold fewer merge corrections and 2.1-fold more split
corrections than c2 (Shapson-Coe et al., 2024; figure above). Two groups
running different thresholds on the same volume get different distributions,
and both are correct about their own data.

So the useful hierarchy is by **cost**, which is stable across pipelines, rather
than by frequency, which is not:

| Error type | Downstream impact | Detectability | Cost to fix |
|---|---|---|---|
| **Merge** | Very high: adds connections that do not exist, across the whole merged object | Poor. The merged object still looks like a plausible neuron | High: requires locating the join, often across many sections |
| **Split** | High: removes real connections, mostly on thin processes | Good. Dead ends are visible and searchable | Low once found: joining is a single operation |
| **Boundary** | Moderate: biases spine volume, bouton size, synapse area | Poor. Only visible quantitatively | Moderate |
| **Identity** | Very high per instance | Very poor | High, and often introduced *by* proofreading |

The asymmetry that matters is between the second and third columns: **the errors
that are easy to see are the cheap ones**. If you tune a segmentation only to
reduce the errors you can see, you tend to push error toward merges, the kind
that corrupts connectivity and hides from inspection.

### What to measure on your own volume

Rather than importing a frequency table, get the distribution for the pipeline
and tissue you are actually working with:

1. Take a small subvolume and reconstruct it densely by hand, or use an existing
   gold standard for the same dataset.
2. Compare against the automated segmentation, and count merges and splits
   separately. Report them separately: a summed VI hides which dominates.
3. Repeat at two agglomeration thresholds. The change between them tells you how
   much of your error population is a choice rather than a limitation.

That number is worth more than any published range, because it is the one your
proofreading budget has to absorb. The pilot reconstruction in
[Unit 03]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }})
exists for this purpose, and the proofreading-plan lab in
[Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
is built around it.

### On automated error detection

Detector performance is also specific to the pipeline and dataset, and recall
differs by error class. One thing holds generally enough to plan around: no
current detector is complete enough to skip a human verification pass on a
sample. Quote the recall figure from the detector you are using, on data
resembling yours, not a range from a review.

## 7. Common Misconceptions

| Misconception | Reality |
|---|---|
| "Superhuman accuracy means proofreading is unnecessary." | Superhuman refers to a score on a small benchmark volume. At connectome scale, even small error rates compound to near-certainty of errors per neuron. |
| "Merge errors are always obvious in 3D." | Small merges (e.g., two thin axons fused for a few sections) can be nearly invisible in 3D mesh views. They are often found only through connectivity analysis. |
| "Split errors are less harmful than merge errors." | For connectivity analysis, split errors cause missing edges, which can be just as damaging as the false edges from merges, depending on the scientific question. |
| "Boundary errors don't matter." | For any analysis involving synapse assignment or fine morphological measurement (spine volume, bouton size), boundary errors can bias the result. |
| "More proofreading always helps." | Poorly executed proofreading can introduce new errors (especially identity errors). Verify a sample of edits, as you would verify the segmentation. |
| "Automated error detection finds all errors." | No current detector is complete, and recall differs by error class, so a human verification pass on a sample cannot be skipped. Quote the figure from the detector you are actually running. |

---

## 8. References and further reading

- Berger, D. R., Seung, H. S., & Lichtman, J. W. (2018). VAST (Volume
  Annotation and Segmentation Tool): Efficient manual and semi-automatic
  labeling of large 3D image stacks. *Frontiers in Neural Circuits*, 12, 88.
- Funke, J., Tschopp, F., Grisaitis, W., Sheridan, A., Singh, C.,
  Saalfeld, S., & Turaga, S. C. (2019). Large scale image segmentation
  with structured loss based deep learning for connectome reconstruction.
  *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 41(7),
  1669-1680. (Preprint: arXiv:1709.02974.)
- Lee, K., Zung, J., Li, P., Jain, V., & Seung, H. S. (2017). Superhuman
  accuracy on the SNEMI3D connectomics challenge. *arXiv preprint
  arXiv:1706.00120*.
- Plaza, S. M., Scheffer, L. K., & Chklovskii, D. B. (2014). Toward
  large-scale connectome reconstructions. *Current Opinion in
  Neurobiology*, 25, 201-210.
- Schneider-Mizell, C. M., et al. (2016). Quantitative neuroanatomy for
  connectomics in Drosophila. *eLife*, 5, e12059.
- Shapson-Coe, A., et al. (2024). A petavoxel fragment of human cerebral
  cortex reconstructed at nanoscale resolution. *Science*, 384, eadk4858.

---

*End of instructor script: Error Taxonomy in Connectome Proofreading*
