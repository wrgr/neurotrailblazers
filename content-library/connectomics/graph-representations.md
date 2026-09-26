---
layout: page
title: "Graph Representations"
permalink: /content-library/connectomics/graph-representations/
image: /assets/images/content-library/connectomics/graph-representations.svg
image_alt: "Stylized vector art: a network graph with one community circled."
description: "How connectomes are represented as graphs — nodes, edges, weights, adjacency matrices, and the tradeoffs of different graph encodings for neural circuit analysis."
topics:
  - graphs
  - adjacency-matrix
  - network-science
  - data-structures
primary_units:
  - "09"
difficulty: "Intermediate"
tags:
  - connectomics:graph-theory
  - connectomics:adjacency-matrix
  - connectomics:directed-graph
  - connectomics:weighted-graph
  - methodology:data-format
  - methodology:graph-storage
  - infrastructure:segmentation
  - cell-types:type-level-graph
micro_lesson_id: ml-conn-graphs
combines_with:
  - connectome-history
  - network-analysis-methods
  - motif-analysis
content_type: core
---

## Overview

A connectome is a graph: neurons are nodes, synaptic connections are edges. How you encode it (directed or undirected, binary or weighted, neuron-level or type-level) decides which analyses are possible and which conclusions hold. The same synapse table can yield graphs with very different degree distributions depending on a threshold nobody reported. This page covers the choices every connectomics analyst makes, whether or not they notice making them.

---

## Instructor script: from EM volume to graph

### The pipeline

The path from raw EM images to a queryable graph has several lossy steps:

1. **Segmentation:** each voxel is assigned to an object (neuron, glia and so on).
2. **Synapse detection**, usually run on the images in parallel with segmentation: clefts with presynaptic vesicles and a postsynaptic density are marked as synapses.
3. **Partner assignment:** each synapse gets a presynaptic and a postsynaptic segment.
4. **Graph construction:** synapses are aggregated into neuron-to-neuron edges.

Each step adds errors of its own. A merge error in segmentation creates false edges. A missed synapse removes a true one. A synapse with its pre and post sides swapped creates an edge in the wrong direction. Errors in any step carry into the graph.

**Teaching point:** "When you analyze a connectome graph, you are analyzing the output of a computational pipeline, not ground truth. Every edge carries implicit uncertainty from segmentation and synapse detection."

---

## Nodes: what represents a neuron?

### Neuron-level nodes

The most common representation: each reconstructed neuron is one node. Node attributes may include:

| Attribute | Source | Example |
|-----------|--------|---------|
| Cell type | Morphological classification or molecular markers | "L2/3 pyramidal", "PV+ basket" |
| Soma position | Centroid of soma segmentation | (x=2045.3, y=891.2, z=1567.8) μm |
| Laminar position | Depth from pia | Layer 2/3, 250 μm from pia |
| Morphological features | Computed from skeleton/mesh | Total cable length: 4,521 μm |
| Functional properties | From correlative calcium imaging (MICrONS) | Orientation selectivity: 45° |
| Reconstruction completeness | Fraction of arbor within volume | 0.72 (72% of estimated total) |

### Compartment-level nodes

Sometimes it's useful to split a neuron into compartments: soma, axon, individual dendritic branches. Each compartment becomes its own node. This enables questions like "which branch of neuron A receives input from neuron B?" but dramatically increases graph size.

### Type-level nodes

For cross-region or cross-species comparisons, individual neurons are grouped by type, and the graph represents type-to-type connectivity. White et al. (1986) grouped the 302 neurons of the *C. elegans* hermaphrodite into 118 classes. In the adult fly brain, FlyWire's 139,255 neurons (Dorkenwald et al. 2024) were assigned to more than 8,400 cell types (Schlegel et al. 2024).

**Tradeoff:** Type-level graphs lose individual variation but are less sensitive to individual segmentation errors and allow comparisons across animals.

---

## Edges: what represents a connection?

### Chemical synapses as directed edges

Each chemical synapse is naturally directed: the presynaptic terminal (with vesicles) releases neurotransmitter onto the postsynaptic element (with receptors/PSD). This creates a directed edge from the presynaptic neuron to the postsynaptic neuron.

In graph notation: an edge (A → B) means "neuron A makes at least one chemical synapse onto neuron B."

### Gap junctions as undirected edges

Electrical synapses (gap junctions) allow bidirectional current flow. These are represented as undirected edges (A — B). In mammalian cortex they are much rarer than chemical synapses but common between some inhibitory interneurons. *C. elegans* has about 600 of them against about 5,000 chemical synapses (White et al. 1986). Most EM pipelines cannot detect them at all (see the table below).

### Edge weights

A connected pair can share one synapse or many, so the edge needs a weight, or a decision to drop the weight. The usual choice is **synapse count**, the number of synapses from A to B. The distribution is typically skewed toward 1 with a long tail; in the larval fly connectome, 66% of edges have one or two synapses (Winding et al. 2023). The maximum per pair, and the shape of the tail, differ between datasets and proofreading levels, so compute them for yours rather than borrowing a range. The alternatives to synapse count, and what each costs, are compared under "Weights: what the number on the edge is" below.

### The threshold problem

The practical decision with the largest effect: **at what minimum synapse count do you call two neurons "connected"?**

- Threshold = 1: Include all detected synapses. Maximizes sensitivity but includes many false positives (single-synapse connections are noisy and may be detection errors).
- Threshold = 3-5: Common in published analyses. Reduces noise but may miss real weak connections.
- No threshold: Use continuous weights (synapse count) and avoid binarizing.

**Thresholding changes the graph a lot, so measure its effect rather than
assume it.** Synapse counts per connected pair are skewed toward one, so a
large share of the edges in a raw graph are single-synapse, and raising the
threshold from 1 to 3 removes far more than a trim. The exact fraction depends on the dataset, the synapse detector's
precision, and the proofreading level, so it is not a constant worth quoting.

Get it for your own graph in a few lines, on a named dataset at a pinned
version:

```python
import numpy as np
# weights: synapse count per connected pair, from your materialized synapse table
weights = np.asarray(weights)
for t in (1, 2, 3, 5, 10):
    print(t, int((weights >= t).sum()))
```

Then re-run your headline statistic at each threshold. Degree distributions,
clustering coefficients and motif counts all move, and if your result only holds
at one threshold that is something a reader needs to know.

**Every analysis must report its threshold and justify it.** The justification
has to be about biology or detector precision, not about which value made the
effect significant.

---

## What the volume boundary does to your graph

Every EM volume is a box cut out of a brain, and the cut is not random with
respect to connectivity. This biases graph statistics in a direction you can
predict and should correct for.

- **Degree is truncated, unevenly.** A cell whose soma sits at the center of the
  volume keeps more of its arbor than one near the face. So measured degree
  correlates with distance from the boundary. That artifact looks exactly
  like a spatial gradient in connectivity.
- **Long-range connections are systematically missing.** Local axons stay;
  projection axons leave. A cubic millimeter of cortex captures local
  connectivity well and inter-areal connectivity barely at all, which means
  "this circuit is locally recurrent" is nearly guaranteed by the sampling.
- **The bias is not fixable by normalization.** You cannot divide it out,
  because you do not know what is missing. What you can do is restrict the node
  set to cells whose relevant arbor is contained, and say so.

**The practical rule:** state, for every graph statistic you report, which cells
were eligible and why. "Cells with a soma in the volume and at least 80% of the
dendritic arbor contained" is a checkable statement. "Cells in the volume" is
not.

---

## Edges that are not connections, and connections that are not edges

The mapping from biology to graph is lossier than the tidy definition suggests.

| Situation | What the graph usually does | What it should probably do |
|---|---|---|
| **Polyadic synapse** — one presynaptic site, several postsynaptic partners (the norm in *Drosophila*) | Counts one edge per partner, each weight 1 | Depends on the question; if presynaptic resources are shared, the partners are not independent |
| **Two synapses from one bouton onto one target** | Weight 2 | Reasonable, but note this is one contact site, not two independent connections |
| **Gap junction** | Usually absent — most pipelines detect chemical synapses only | Say explicitly that electrical coupling is out of scope |
| **Contact without a synapse** | No edge, correctly | But "no edge" is only meaningful in a densely reconstructed volume |
| **Connection below your threshold** | No edge | An absent edge and a weak edge are different claims; a binarized graph cannot tell them apart |

The last row is the one that changes results. **Absence of an edge means three
different things** — no contact, contact without synapse, or synapse count below
threshold — and a binary adjacency matrix collapses all three. If your claim
depends on absence, say which kind you mean and how you established it.

---

## Weights: what the number on the edge is

Synapse count is the default weight and it is a proxy, not a measurement of
strength. Alternatives, with what each buys:

- **Synapse count:** cheap, standard, comparable across studies. Ignores that
  synapses differ in size by an order of magnitude.
- **Summed cleft or PSD size:** closer to a physiological correlate, because
  larger synapses tend to be stronger, and available from the segmentation.
  Sensitive to boundary errors, the error class that is hardest to see.
- **Contact area:** measures apposition, not transmission. Useful for
  Peters'-rule-style questions and misleading for connectivity ones.
- **Binary:** throws away the most informative variable you have. Justified
  only when the analysis needs it.
- **Estimated strength:** paired recordings or calcium imaging can estimate
  synaptic strength for a few connections. It links structure to function, but
  covers a tiny fraction of the edges in any EM graph.

Whatever you choose, the **proofreading level enters the weight**. An edge
weight of 3 on an unproofread pair and an edge weight of 3 on a fully verified
pair are not the same number, and averaging over both without saying so is one
of the quieter ways a connectomics result goes wrong.

---

## Adjacency matrices

### Definition

For N neurons, the adjacency matrix **A** is an N×N matrix where entry A[i,j] = the weight of the edge from neuron i to neuron j (0 if no connection).

**Properties:**
- **Directed graph:** A is generally asymmetric (A[i,j] ≠ A[j,i] unless the connection is reciprocal with equal weight)
- **Sparse:** Most entries are zero. Nearby cortical pyramidal neurons can connect at rates around 10% (11.6% for layer 5 pairs in Song et al. 2005), but most pairs in a volume are too far apart for their arbors to touch, so the full matrix is overwhelmingly zeros.
- **Row sums = out-degree** (for binary) or total output weight
- **Column sums = in-degree** or total input weight

### Sparse representation

For 100,000 neurons, the full adjacency matrix has 10^10 entries — ~40 GB at 32-bit floats, mostly zeros. In practice, connectomes are stored as sparse matrices:

- **Edge list** (COO in `scipy.sparse`): three columns, source, target and weight, one row per non-zero entry. The simplest and most portable format; it is what a synapse-table query gives you.
- **Compressed Sparse Row (CSR):** replaces the source column with N + 1 row pointers, so it is slightly smaller than an edge list and fast for row operations ("all outputs of neuron X").
- **Compressed Sparse Column (CSC):** the same idea by column, fast for "all inputs to neuron X".

### Tools for graph manipulation

| Tool | Language | Strengths |
|------|----------|-----------|
| **NetworkX** | Python | Easy API and many algorithms; pure Python, so slow on graphs with millions of edges |
| **igraph** | C core; R and Python interfaces | Fast on large graphs; motif counting built in |
| **graph-tool** | C++ core; Python interface | Fast on large graphs; stochastic block model inference |
| **scipy.sparse** | Python | Sparse matrix operations that integrate with NumPy |
| **Neo4j** | Java; queried with Cypher | Graph database for persistent storage and queries |

---

## Multigraphs and multi-layer networks

### Multigraphs

Two neurons may be connected by multiple synapses. Representing each synapse as a separate edge creates a multigraph. This preserves spatial information (each synapse has a location on the pre and post neuron) but is more complex to analyze.

**Common simplification:** Collapse multigraph to weighted simple graph where weight = synapse count.

### Multi-layer networks

Different connection types can be represented as separate graph layers:
- Layer 1: Excitatory chemical synapses
- Layer 2: Inhibitory chemical synapses
- Layer 3: Gap junctions

Each layer may have different topology. Analysis can examine each layer independently or study inter-layer relationships.

---

## Worked example: constructing a graph from a synapse table

**Given:** a synapse table exported from CAVE to CSV at a pinned materialization version. The column names below follow the MICrONS `minnie65_public` synapse table: `id`, `pre_pt_root_id`, `post_pt_root_id` and `size` (the detected cleft size in voxels). Check the names in your own table before running. EM synapse detectors find chemical synapses only, so there is no synapse-type column to filter on.

```python
import pandas as pd
import networkx as nx

synapses = pd.read_csv("synapses.csv")

# Drop synapses onto or from unsegmented space (root ID 0) and autapses,
# which in EM are more often segmentation errors than real self-contacts
synapses = synapses[(synapses.pre_pt_root_id != 0) & (synapses.post_pt_root_id != 0)]
synapses = synapses[synapses.pre_pt_root_id != synapses.post_pt_root_id]

# Aggregate: count synapses and sum cleft size per ordered neuron pair
edges = synapses.groupby(["pre_pt_root_id", "post_pt_root_id"]).agg(
    synapse_count=("id", "count"),
    total_size=("size", "sum"),
).reset_index()

# Apply threshold
edges_filtered = edges[edges.synapse_count >= 3]

# Build a directed graph with both weights as edge attributes
G = nx.from_pandas_edgelist(
    edges_filtered,
    source="pre_pt_root_id",
    target="post_pt_root_id",
    edge_attr=["synapse_count", "total_size"],
    create_using=nx.DiGraph,
)

print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
```

Root IDs are not neurons. A root ID can be a neuron, a fragment of one, or a merger of several, so restrict the node set to proofread cells (a proofreading or cell-type table) before you read anything off the graph.

**Exercise:** Re-run with thresholds of 1, 5, and 10. Plot the degree distribution at each threshold and observe how it changes.

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "The connectome is a fixed object" | Representation choices (threshold, weighting) create different graphs from the same data | Always report representational choices |
| "More edges = more accurate" | Low-threshold graphs include more noise from false synapse detections | Balance sensitivity and specificity |
| "Binary graphs are sufficient" | Synapse count carries information about connection strength | Use weighted graphs when possible |
| "The adjacency matrix is the connectome" | The matrix is one representation; the underlying biology includes spatial structure, dynamics, and molecular identity | The graph is a model, not the territory |

---

## References

- Rubinov M, Sporns O (2010) "Complex network measures of brain connectivity: Uses and interpretations." *NeuroImage* 52(3):1059-1069.
- Sporns O (2010) *Networks of the Brain*. MIT Press.
- Varshney LR et al. (2011) "Structural properties of the *Caenorhabditis elegans* neuronal network." *PLoS Computational Biology* 7(2):e1001066.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634:124-138. [10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y)
- Scheffer LK et al. (2020) "A connectome and analysis of the adult *Drosophila* central brain." *eLife* 9:e57443. [10.7554/eLife.57443](https://doi.org/10.7554/eLife.57443)
- Schlegel P et al. (2024) "Whole-brain annotation and multi-connectome cell typing of *Drosophila*." *Nature* 634:139-152. [10.1038/s41586-024-07686-5](https://doi.org/10.1038/s41586-024-07686-5)
- Song S, Sjöström PJ, Reigl M, Nelson S, Chklovskii DB (2005) "Highly nonrandom features of synaptic connectivity in local cortical circuits." *PLoS Biology* 3(3):e68. [10.1371/journal.pbio.0030068](https://doi.org/10.1371/journal.pbio.0030068)
- White JG, Southgate E, Thomson JN, Brenner S (1986) "The structure of the nervous system of the nematode *Caenorhabditis elegans*." *Philosophical Transactions of the Royal Society B* 314(1165):1-340. [10.1098/rstb.1986.0056](https://doi.org/10.1098/rstb.1986.0056)
- Winding M et al. (2023) "The connectome of an insect brain." *Science* 379(6636):eadd9330. [10.1126/science.add9330](https://doi.org/10.1126/science.add9330)
