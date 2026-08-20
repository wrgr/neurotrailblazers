---
layout: page
title: "Connectome Quality Notebooks"
description: "A computational path through connectome quality assessment: what to run, in what order, with the reference notebooks and the analyses to build for yourself."
permalink: /notebooks/connectome-quality/
use_layout_hero: false
---

<div class="main-content">

<section class="section" markdown="1">

# Connectome Quality Notebooks

A computational path through the quality-assessment ideas in
[Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
and the [Connectome Quality]({{ '/tools/connectome-quality/' | relative_url }}) tool
page. Work these in order — each one assumes the previous.

The available starter notebooks are listed at each step. Where a step has no packaged
notebook yet, the specification is complete enough to build it yourself in an hour or
two, and doing so is a better exercise than running someone else's.

</section>

<section class="section" markdown="1">

## Environment

```bash
pip install caveclient cloud-volume numpy pandas matplotlib networkx
# For hemibrain instead of MICrONS:
pip install neuprint-python
# For BossDB-hosted volumes:
pip install intern
```

A free CAVE account is required for MICrONS access. Verify access before a teaching
session — account provisioning is the single most common reason a hands-on session
loses its first twenty minutes.

</section>

<section class="section" markdown="1">

## Step 1 — Look at the data before measuring it

**Goal:** develop a visual sense of what good and bad reconstruction look like, before
any metric is computed. A metric you cannot connect to something you have seen is a
number you will misinterpret.

**Run:** [Image and segmentation download]({{ '/notebooks/intro/ImageAndSegmentationDownload.ipynb' | relative_url }})

**Do:** pull a cutout of raw EM and the corresponding segmentation. Display them
side by side. Find, by eye, one place where the segmentation boundary does not follow
the membrane. Save the coordinate.

**Produce:** three annotated screenshots — a clean region, a plausible split, a
suspected merge — with a sentence each on what in the image supports your reading.

</section>

<section class="section" markdown="1">

## Step 2 — Morphology as a quality signal

**Goal:** learn to spot reconstruction errors from morphology alone, without returning
to the voxels. This is the skill that lets one person screen hundreds of cells.

**Run:** [Mesh example]({{ '/notebooks/intro/MeshExample.ipynb' | relative_url }}) and
[3D scale bar rendering]({{ '/notebooks/intro/Render3DScaleBar.ipynb' | relative_url }})

**Do:** load meshes for ten neurons. For each, ask: does this look like one cell? Look
for two somata in one object, a process that terminates abruptly in mid-neuropil, or a
branch that leaves the expected arbor territory.

**Produce:** a table of ten cells with a plausibility call and the morphological feature
that drove it. Then check two of your suspicions in the raw data and report whether you
were right — this is your first calibration measurement.

</section>

<section class="section" markdown="1">

## Step 3 — Synapse queries, pinned to a version

**Goal:** retrieve connectivity reproducibly, and understand why the version matters.

**Run:** [Most synapses in and out]({{ '/notebooks/intro/MostSynapsesInAndOut.ipynb' | relative_url }})
and [Dash synapse explorer]({{ '/notebooks/intro/DashSynapseExplorer.ipynb' | relative_url }})

**Do:**
1. List available materialization versions. **Pin one explicitly** and record it.
2. For one neuron, retrieve input and output synapses; report counts and distinct partners.
3. Plot the synapses-per-partner distribution on log axes. Note the heavy tail.
4. Re-run against a second version and report what changed, and why.

**Produce:** a notebook with a five-line reproducibility header — dataset, version,
client version, date, author — and the two-version comparison.

**Why this step matters more than it looks:** analysis against an unpinned segmentation
is the most common silent correctness bug in connectomics. Your code runs fine; it
answers a different question than it did last week. See
[Unit 04 §2]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}).

</section>

<section class="section" markdown="1">

## Step 4 — Build a proofreading-effect measurement

**Goal:** produce the quality statement that actually persuades — the effect of
proofreading on your endpoint.

**Build this yourself.** Specification:

1. Choose a small population of cells (10–20) and an endpoint metric — for example
   mean input count, or the ratio of synapses onto spines versus shafts.
2. Record each cell's proofreading status from the dataset's metadata.
3. Compute the endpoint separately for well-proofread and less-proofread cells.
4. Report the difference, with the caveat that proofreading status is not randomly
   assigned — cells get proofread for reasons that correlate with size, position, and
   type, so this is an association, not a controlled comparison. State that explicitly.

**Produce:** one number and one honest paragraph. "Cells at proofreading level N have a
mean input count of X; cells below level N have Y" is the kind of statement that belongs
in a methods section, and almost no analysis includes it.

</section>

<section class="section" markdown="1">

## Step 5 — Error sensitivity simulation

**Goal:** quantify how much your conclusion depends on the reconstruction errors you
already know are there.

**Build this yourself.** Specification:

1. Build a connectivity graph for your population (record the six construction
   decisions from [Unit 09 §1]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})).
2. Compute your headline statistic — reciprocity, a motif count, a degree ratio.
3. Write a perturbation function: with probability *m*, merge two random nodes (union
   their edge sets); with probability *s*, split a random node into two.
4. Run 100 perturbations at your measured error rates and record the statistic each time.
5. Report the resulting spread as an error band on your effect size.

**Produce:** a figure showing your observed value against the perturbation distribution.
If the band crosses the null expectation, your result is not robust to your own measured
error rate — and reporting that is more valuable than not knowing it.

This is roughly forty lines of code and it is among the strongest things you can put in
a supplement.

</section>

<section class="section" markdown="1">

## Related material

</section>

<section class="section">
  <ul class="list-tight">
    <li><a href="{{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}">Unit 08 — Segmentation and Proofreading</a> — the concepts these notebooks operationalize</li>
    <li><a href="{{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}">Unit 09 — Connectome Analysis</a> — graph construction and null models</li>
    <li><a href="{{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}">Metrics and QA</a> — VI, ERL, and precision/recall worked in full</li>
    <li><a href="{{ '/tools/connectome-quality/' | relative_url }}">Connectome Quality tool page</a></li>
    <li><a href="{{ '/datasets/access/' | relative_url }}">Dataset access guide</a> — clients and credentials</li>
    <li><a href="{{ '/assets/notebooks/module07/module07-proofreading-and-quality-control.ipynb' | relative_url }}">Module 07 notebook — Proofreading and Quality Control</a></li>
    <li><a href="{{ '/assets/notebooks/module12/module12-big-data-in-connectomics.ipynb' | relative_url }}">Module 12 notebook — Big Data in Connectomics</a></li>
  </ul>
</section>

</div>
