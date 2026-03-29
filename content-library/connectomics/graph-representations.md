---
layout: page
title: "Graph Representations"
permalink: /content-library/connectomics/graph-representations/
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
reference_images:
  - src: /assets/images/content-library/connectomics/graph-representations/adjacency-matrix-example.png
    alt: "Adjacency matrix of a small neural circuit with neuron labels"
    caption: "Weighted directed adjacency matrix for a 10-neuron circuit. Entry (i,j) = synapse count from neuron i to neuron j. Note sparsity and asymmetry."
  - src: /assets/images/content-library/connectomics/graph-representations/graph-encoding-comparison.png
    alt: "Comparison of neuron-level, compartment-level, and type-level graph encodings"
    caption: "Three levels of graph abstraction: neuron-level (left, N=140K nodes), compartment-level (center, N~1M), type-level (right, N~8K)."
  - src: /assets/images/content-library/connectomics/graph-representations/sparse-storage-formats.png
    alt: "Diagram of edge list, CSR, and CSC sparse storage formats"
    caption: "Three sparse matrix formats for storing connectome graphs: edge list (most compact), CSR (fast row queries), and CSC (fast column queries)."
combines_with:
  - connectome-history
  - network-analysis-methods
  - motif-analysis
---

## Overview

The connectome, at its core, is a graph: neurons are nodes, synaptic connections are edges. But the details of how you encode this graph — directed or undirected, binary or weighted, neuron-level or type-level — profoundly affect what analyses are possible and what conclusions you can draw. This document covers the representational choices that every connectomics analyst must make.

---

## Instructor script: from EM volume to graph

### The pipeline

The path from raw EM images to a queryable graph involves several lossy transformations:

1. **Raw images** → Segmentation: each voxel assigned to an object (neuron, glia, etc.)
2. **Segmentation** → Synapse detection: membrane appositions with vesicles + PSD identified as synapses
3. **Synapse detection** → Edge assignment: each synapse assigned a pre-synaptic neuron and post-synaptic neuron
4. **Edge assignment** → Graph construction: aggregate synapses into neuron-to-neuron edges

Each step can introduce errors. A segmentation merge error creates false edges. A missed synapse removes a true edge. A synapse with incorrect pre/post assignment creates a wrongly directed edge. The graph is only as reliable as the weakest link in this chain.

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

For cross-region or cross-species comparisons, individual neurons are grouped by type, and the graph represents type-to-type connectivity. For example, in C. elegans analysis, the 302 individual neurons might be grouped into ~100 neuron classes. In Drosophila, ~139,000 neurons collapse to ~8,000 types.

**Tradeoff:** Type-level graphs lose individual variation but are more robust to segmentation errors and enable statistical comparisons.

---

## Edges: what represents a connection?

### Chemical synapses as directed edges

Each chemical synapse is naturally directed: the presynaptic terminal (with vesicles) releases neurotransmitter onto the postsynaptic element (with receptors/PSD). This creates a directed edge from the presynaptic neuron to the postsynaptic neuron.

In graph notation: an edge (A → B) means "neuron A makes at least one chemical synapse onto neuron B."

### Gap junctions as undirected edges

Electrical synapses (gap junctions) allow bidirectional current flow. These are represented as undirected edges (A — B). Gap junctions are less common than chemical synapses in mammalian cortex but are prevalent in certain circuits (e.g., between inhibitory interneurons) and in invertebrate nervous systems.

### Edge weights

Most neuron pairs that are connected have multiple synapses. How to represent this?

**Binary (unweighted):** Edge exists (1) or doesn't (0). Simplest representation. Loses information about connection strength.

**Synapse count:** Edge weight = number of synapses from A to B. The most common weighting scheme. Ranges: C. elegans typically 1-50 synapses per pair; Drosophila 1-100+; mammalian cortex 1-20+ for most pairs, with some pairs having >50.

**Total contact area:** Edge weight = sum of cleft areas or PSD areas across all synapses. More biologically meaningful (larger PSD ≈ stronger synapse) but harder to measure accurately.

**Estimated strength:** In rare cases, functional data (paired recordings, calcium imaging) can estimate synaptic strength. This bridges structure and function but is available for very few connections.

### The threshold problem

A critical practical decision: **at what minimum synapse count do you call two neurons "connected"?**

- Threshold = 1: Include all detected synapses. Maximizes sensitivity but includes many false positives (single-synapse connections are noisy and may be detection errors).
- Threshold = 3-5: Common in published analyses. Reduces noise but may miss genuine weak connections.
- No threshold: Use continuous weights (synapse count) and avoid binarizing.

**The effect of thresholding is dramatic.** In a typical cortical dataset:
- At threshold = 1: ~500,000 edges
- At threshold = 3: ~150,000 edges
- At threshold = 5: ~60,000 edges

Degree distributions, clustering coefficients, and motif counts all change substantially with threshold. **Every analysis must report its threshold and justify the choice.**

---

## Adjacency matrices

### Definition

For N neurons, the adjacency matrix **A** is an N×N matrix where entry A[i,j] = the weight of the edge from neuron i to neuron j (0 if no connection).

**Properties:**
- **Directed graph:** A is generally asymmetric (A[i,j] ≠ A[j,i] unless the connection is reciprocal with equal weight)
- **Sparse:** Most entries are zero. In cortex, each neuron connects to <1% of its neighbors, so >99% of the matrix is zeros.
- **Row sums = out-degree** (for binary) or total output weight
- **Column sums = in-degree** or total input weight

### Sparse representation

For 100,000 neurons, the full adjacency matrix has 10^10 entries — ~40 GB at 32-bit floats, mostly zeros. In practice, connectomes are stored as sparse matrices:

- **Edge list format:** Three columns: source, target, weight. Only non-zero entries stored. Most compact for very sparse graphs.
- **Compressed Sparse Row (CSR):** Efficient for row-wise operations (e.g., "find all outputs of neuron X").
- **Compressed Sparse Column (CSC):** Efficient for column-wise operations (e.g., "find all inputs to neuron X").

### Tools for graph manipulation

| Tool | Language | Strengths |
|------|----------|-----------|
| **NetworkX** | Python | Easy API, rich algorithms, good for <100K nodes |
| **igraph** | R/Python/C | Fast, good for medium graphs (<1M nodes) |
| **graph-tool** | Python/C++ | Fastest for large graphs, excellent SBM implementation |
| **scipy.sparse** | Python | Direct sparse matrix operations, integrates with NumPy |
| **Neo4j** | Java/Cypher | Graph database, good for persistent storage and queries |

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

**Given:** A synapse table from CAVE with columns: `synapse_id`, `pre_segment_id`, `post_segment_id`, `synapse_type`, `cleft_area`

```python
import pandas as pd
import networkx as nx

# Load synapse table
synapses = pd.read_csv("synapses.csv")

# Filter to chemical synapses only
chem = synapses[synapses.synapse_type == "chemical"]

# Aggregate: count synapses per neuron pair
edges = chem.groupby(["pre_segment_id", "post_segment_id"]).agg(
    synapse_count=("synapse_id", "count"),
    total_cleft_area=("cleft_area", "sum")
).reset_index()

# Apply threshold
edges_filtered = edges[edges.synapse_count >= 3]

# Build graph
G = nx.DiGraph()
for _, row in edges_filtered.iterrows():
    G.add_edge(
        row.pre_segment_id,
        row.post_segment_id,
        weight=row.synapse_count,
        cleft_area=row.total_cleft_area
    )

print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
```

**Exercise:** Re-run with thresholds of 1, 5, and 10. Plot the degree distribution at each threshold and observe how it changes.

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "The connectome is a fixed object" | Representation choices (threshold, weighting) create different graphs from the same data | Always report representational choices |
| "More edges = more accurate" | Low-threshold graphs include more noise from false synapse detections | Balance sensitivity and specificity |
| "Binary graphs are sufficient" | Synapse count carries biologically meaningful information about connection strength | Use weighted graphs when possible |
| "The adjacency matrix is the connectome" | The matrix is one representation; the underlying biology includes spatial structure, dynamics, and molecular identity | The graph is a model, not the territory |

---

## References

- Rubinov M, Sporns O (2010) "Complex network measures of brain connectivity: Uses and interpretations." *NeuroImage* 52(3):1059-1069.
- Sporns O (2010) *Networks of the Brain*. MIT Press.
- Varshney LR et al. (2011) "Structural properties of the *Caenorhabditis elegans* neuronal network." *PLoS Computational Biology* 7(2):e1001066.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634:124-138.
- Scheffer LK et al. (2020) "A connectome and analysis of the adult *Drosophila* central brain." *eLife* 9:e57443.
