---
layout: page
title: "Connectome Quality Notebooks"
description: "A computational path through connectome quality assessment: reference code for each step, and the analyses to build for yourself."
permalink: /notebooks/connectome-quality/
use_layout_hero: false
content_type: path
---

<div class="main-content">

<section class="section" markdown="1">

# Connectome Quality Notebooks

A computational path through the quality-assessment ideas in
[Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
and the [Connectome Quality]({{ '/tools/connectome-quality/' | relative_url }}) tool
page. Work these in order. Each step assumes the one before.

> **What this page is.** Reference code and specifications you implement yourself, not
> downloadable notebooks. For a runnable, version-pinned notebook with archived outputs,
> use the [MICrONS Real-Data Lab]({{ '/notebooks/microns-lab/' | relative_url }}), which
> needs no account.
>
> The snippets below were written against the `caveclient` and CloudVolume APIs but were
> not run for this page. Client libraries in this field change often, so check call
> signatures against the package docs before assuming a failure is your fault.

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

Steps 3 to 5 need a free CAVE account, and you must accept the dataset's terms before
the API will return data. Steps 1 and 2 read public CloudVolume paths and need no
account. Verify access **before** a teaching session. If tokens are set up during the
session, expect to lose the first twenty minutes to it.

</section>

<section class="section" markdown="1">

## Step 1 — Look at the data before measuring it

**Goal:** develop a visual sense of what good and bad reconstruction look like, before
any metric is computed. A metric you cannot connect to something you have seen is a
number you will misinterpret.

**Do:** pull a cutout of raw EM and the corresponding segmentation, display them side by
side, and find one place by eye where the segmentation boundary does not follow the
membrane. Save the coordinate.

```python
from cloudvolume import CloudVolume
import matplotlib.pyplot as plt

# MICrONS public release. Check the current source paths in the dataset docs;
# these move between releases. seg_m1300 is the flat segmentation at v1300, so its
# IDs match the VERSION pinned in step 3.
img = CloudVolume("precomputed://gs://iarpa_microns/minnie/minnie65/em",
                  mip=0, use_https=True, progress=False)
seg = CloudVolume("precomputed://gs://iarpa_microns/minnie/minnie65/seg_m1300",
                  mip=0, use_https=True, progress=False)

# mip 0 here is 8 x 8 x 40 nm. CAVE positions are 4 x 4 x 40 nm: halve x and y.
x, y, z = 120000, 100000, 21000          # inside both volumes
box = (slice(x, x + 512), slice(y, y + 512), slice(z, z + 1))

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(img[box][:, :, 0, 0].T, cmap="gray"); ax[0].set_title("EM")
ax[1].imshow(seg[box][:, :, 0, 0].T);              ax[1].set_title("segmentation")
for a in ax: a.axis("off")
```

**Produce:** three annotated screenshots — a clean region, a plausible split, a suspected
merge — with a sentence each on what in the image supports your reading.

</section>

<section class="section" markdown="1">

## Step 2 — Morphology as a quality signal

**Goal:** learn to spot reconstruction errors from morphology alone, without returning to
the voxels. This is the skill that lets one person screen hundreds of cells.

**Do:** load meshes for ten neurons. For each, ask: does this look like *one* cell? Look
for two somata in one object, a process terminating abruptly in mid-neuropil, or a branch
leaving the expected arbor territory.

```python
mesh = seg.mesh.get(root_id)             # root_id from the cell table, see step 3
m = mesh[root_id]
print(m.vertices.shape, m.faces.shape)
```

**Produce:** a table of ten cells with a plausibility call and the morphological feature
that drove it. Then check two of your suspicions in the raw data and report whether you
were right — that is your first calibration measurement.

</section>

<section class="section" markdown="1">

## Step 3 — Synapse queries, pinned to a version

**Goal:** retrieve connectivity reproducibly, and understand why the version matters.

```python
from caveclient import CAVEclient

client = CAVEclient("minnie65_public")

# Always look at what versions exist, then pin one explicitly.
print(client.materialize.get_versions())
VERSION = 1300                            # replace with a version you chose deliberately

# Pick a neuron with a proofread axon from the proofreading table at that version.
prf = client.materialize.query_table("proofreading_status_and_strategy",
                                     filter_equal_dict={"status_axon": "t"},
                                     materialization_version=VERSION)
root_id = prf.pt_root_id.iloc[0]          # or choose one deliberately

syn_in  = client.materialize.synapse_query(post_ids=root_id,
                                           materialization_version=VERSION)
syn_out = client.materialize.synapse_query(pre_ids=root_id,
                                           materialization_version=VERSION)

print(f"inputs {len(syn_in)}  outputs {len(syn_out)}  "
      f"distinct presynaptic partners {syn_in.pre_pt_root_id.nunique()}")

# The heavy tail: most partners contribute a single synapse.
per_partner = syn_in.groupby("pre_pt_root_id").size().sort_values(ascending=False)
per_partner.value_counts().sort_index().plot(loglog=True, marker="o")
```

Then **re-run against a second materialization version** and report what changed, and why.

**Produce:** a notebook with a five-line reproducibility header — dataset, version, client
version, date, author — and the two-version comparison.

**Why this step matters more than it looks:** analysis against an unpinned segmentation
fails silently. Your code runs, and it answers a different question than it did last
week. See
[Unit 04 §2]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}).

</section>

<section class="section" markdown="1">

## Step 4 — Measure the effect of proofreading on your own endpoint

**Goal:** produce the quality statement that actually persuades.

**Build this yourself.** Specification:

1. Choose 10–20 cells and an endpoint metric — mean input count, or the ratio of synapses
   onto spines versus shafts.
2. Record each cell's proofreading status from the dataset's cell tables.
3. Compute the endpoint separately for well-proofread and less-proofread cells.
4. Report the difference — **with the caveat that proofreading status is not randomly
   assigned.** Cells get proofread for reasons that correlate with size, position and
   type, so this is an association, not a controlled comparison. State that explicitly.

**Produce:** one number and one honest paragraph. "Cells at proofreading level N have a
mean input count of X; cells below it, Y" is the kind of statement that belongs in a
methods section, and few analyses include it.

</section>

<section class="section" markdown="1">

## Step 5 — Error sensitivity simulation

**Goal:** quantify how much your conclusion depends on the reconstruction errors you
already know are there.

**Build this yourself.** Specification:

1. Build a connectivity graph for your population, recording the six construction
   decisions from
   [Unit 09 §1]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}).
2. Compute your headline statistic — reciprocity, a motif count, a degree ratio.
3. Write a perturbation function: with probability *m*, merge two random nodes (union
   their edge sets); with probability *s*, split a random node in two.
4. Run 100 perturbations at your **measured** error rates and record the statistic each time.
5. Report the resulting spread as an error band on your effect size.

```python
import random, networkx as nx

def perturb(G, merge_p, split_p, rng=random.Random(0)):
    H = G.copy()
    for n in list(H.nodes()):
        if n in H and rng.random() < merge_p:
            others = [m for m in H.nodes() if m != n]
            if others:
                nx.contracted_nodes(H, n, rng.choice(others),
                                    self_loops=False, copy=False)
    # Splits are left for you: with probability split_p, divide a node's edges
    # between it and a new node.
    return H
```

**Produce:** a figure showing your observed value against the perturbation distribution.
If the band crosses the null expectation, your result is not robust to your own measured
error rate — and reporting that is more valuable than not knowing it.

The full version is roughly forty lines of code, and the figure belongs in a
supplement.

</section>

<section class="section" markdown="1">

## Related material

</section>

<section class="section">
  <ul class="list-tight">
    <li><a href="{{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}">Unit 08 — Segmentation and Proofreading</a> — the concepts these steps operationalize</li>
    <li><a href="{{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}">Unit 09 — Connectome Analysis</a> — graph construction and null models</li>
    <li><a href="{{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}">Metrics and QA</a> — VI, ERL, and precision/recall worked in full</li>
    <li><a href="{{ '/tools/connectome-quality/' | relative_url }}">Connectome Quality tool page</a></li>
    <li><a href="{{ '/datasets/access/' | relative_url }}">Dataset access guide</a> — clients, credentials, and upstream starter notebooks that do contain code</li>
  </ul>
</section>

</div>
