---
layout: page
title: "Network Analysis Methods"
permalink: /content-library/connectomics/network-analysis-methods/
description: "Core network science methods for connectome analysis — degree distributions, clustering, path length, community detection, centrality, and spectral methods with worked examples."
topics:
  - network-analysis
  - graph-theory
  - clustering
  - community-detection
  - small-world
primary_units:
  - "09"
difficulty: "Advanced"
---

## Overview

Once a connectome is represented as a graph, a rich toolkit of network science methods becomes available. These methods quantify the structure of neural circuits at multiple scales — from individual node properties (degree, centrality) to local circuit structure (clustering, motifs) to global organization (path length, modularity, spectral properties). This document covers the core methods with mathematical definitions, biological interpretation, and practical examples.

---

## Degree distributions

### Definition

For a directed graph, each node v has:
- **In-degree** k_in(v) = number of incoming edges = number of presynaptic partners
- **Out-degree** k_out(v) = number of outgoing edges = number of postsynaptic targets

For weighted graphs, **strength** replaces degree:
- In-strength s_in(v) = sum of incoming edge weights = total synapse count received
- Out-strength s_out(v) = sum of outgoing edge weights = total synapse count sent

### What connectome degree distributions look like

Most connectomes show **heavy-tailed** degree distributions: many neurons with few connections and a few "hub" neurons with many connections. However, these are typically **not** pure power-law distributions — they are better described by lognormal, exponential-truncated, or gamma distributions (Varshney et al. 2011).

**Typical values:**
- C. elegans: mean degree ~25, max ~150 (for hub interneurons like AVA, AVB)
- Drosophila hemibrain: mean in-degree ~80, heavy tail extending to >1,000
- Mouse cortex (MICrONS): varies by cell type; pyramidal cells receive hundreds of inputs

### Hub neurons

Neurons in the high-degree tail are called hubs. In C. elegans, command interneurons (AVA, AVB, PVC) are hubs that integrate sensory information and drive motor output. In Drosophila, certain projection neurons and central complex neurons serve as hubs.

**Biological interpretation:** Hub neurons are candidates for critical integration or relay points. However, high degree alone doesn't prove functional importance — a neuron could have many weak connections that are individually negligible.

---

## Clustering coefficient

### Definition

The clustering coefficient C(v) of node v measures the density of connections among v's neighbors:

C(v) = (number of edges among neighbors of v) / (maximum possible edges among neighbors of v)

For a directed graph with k neighbors, the maximum possible edges is k(k-1) (since edges are directed). The global clustering coefficient is the average over all nodes: C = mean(C(v)).

### Biological meaning

High clustering means: if neuron A connects to both B and C, then B and C are also likely connected. This indicates **local circuit density** — triadic closure, recurrent loops, and interconnected neuronal groups.

**Empirical values:**
- C. elegans: C ≈ 0.34 (Watts & Strogatz 1998). For comparison, a random graph with the same degree distribution has C ≈ 0.05. The 7× enrichment indicates strong local circuit structure.
- Drosophila: varies by brain region, generally C > 0.1
- Random Erdos-Renyi graph with same density: C ≈ p (connection probability), typically <0.01 for sparse graphs

### Interpretation caution

High clustering can arise from spatial proximity (nearby neurons are more likely to connect simply because their arbors overlap) rather than from specific wiring rules. Spatially constrained null models (see motif-analysis.md) help distinguish these cases.

---

## Path length and small-world structure

### Shortest path length

The shortest path between nodes u and v is the minimum number of edges traversed to reach v from u. The **characteristic path length** L is the average shortest path over all pairs.

### Small-world property

A network is "small-world" (Watts & Strogatz 1998) if:
- L ≈ L_random (path lengths are short, comparable to a random graph)
- C >> C_random (clustering is much higher than random)

**Biological interpretation:** Small-world structure enables both local processing (high clustering = dense local circuits for specialized computation) and global integration (short paths = information can reach any neuron in few steps). Both C. elegans and Drosophila connectomes exhibit small-world properties.

### Global efficiency

E_global = mean(1/d(u,v)) for all pairs u,v where d is shortest path length. More robust than characteristic path length because it handles disconnected components gracefully (disconnected pairs contribute 0 instead of infinity).

---

## Centrality measures

### Betweenness centrality

B(v) = fraction of all shortest paths that pass through node v. High betweenness = the node is a critical relay or bottleneck for information flow.

**In connectomics:** Neurons with high betweenness may serve as integration hubs or relay stations. In C. elegans, interneurons like RIA and AIB have high betweenness, consistent with their role in sensorimotor integration.

### PageRank

Originally developed for web search (Brin & Page 1998), PageRank can be applied to connectomes: a neuron's importance depends on the importance of the neurons that connect to it. Iterative computation: PR(v) = (1-d)/N + d × Σ(PR(u)/k_out(u)) for all u → v.

**Application:** Identifying neurons that receive input from other highly connected neurons — capturing hierarchical importance.

### Eigenvector centrality

Similar to PageRank but using the dominant eigenvector of the adjacency matrix. Neurons with high eigenvector centrality are connected to other high-centrality neurons.

---

## Community detection

### Modularity optimization

**Modularity Q** (Newman 2006) measures whether a proposed partition of the graph into communities has more within-community edges than expected by chance:

Q = (1/2m) × Σ[A_ij - (k_i × k_j)/(2m)] × δ(c_i, c_j)

where m = total edges, k_i = degree of node i, c_i = community of node i, δ = 1 if same community.

Optimization algorithms (Louvain, Leiden) find partitions that maximize Q. Applied to connectomes, this reveals groups of neurons that are more densely interconnected than expected — candidate functional modules or cell-type communities.

### Stochastic block models (SBM)

SBMs (Peixoto 2014) provide a probabilistic framework: assume the graph was generated by a model where each node belongs to a block (community), and the probability of an edge between two nodes depends only on their block memberships.

**Advantages over modularity:** SBMs can detect both assortative communities (dense within) and disassortative structure (dense between different groups, as in excitatory-inhibitory networks). They also provide model selection criteria for choosing the number of communities.

**Application in connectomics:** SBMs have been used to discover cell-type communities from connectivity alone in Drosophila and C. elegans, then validated against morphological or molecular cell types.

### Hierarchical community structure

Neural circuits likely have nested community structure — local microcircuits within larger modules within brain-wide systems. Hierarchical SBMs and multi-resolution community detection methods can capture this nesting.

---

## Rich-club organization

### Definition

The rich-club coefficient ρ(k) measures whether nodes with degree > k preferentially connect to each other: ρ(k) = E_>k / E_>k_max, where E_>k = actual edges among high-degree nodes and E_>k_max = maximum possible.

Normalize against degree-preserving random graphs: ρ_norm(k) = ρ(k) / ρ_random(k). Values >1 indicate rich-club structure.

### In connectomics

**C. elegans** shows significant rich-club organization (Towlson et al. 2013): hub interneurons are densely interconnected, forming a "rich club" that may serve as an integrative backbone. Damage to rich-club nodes is predicted to be disproportionately disruptive to global information flow.

---

## Spectral methods

### Graph Laplacian

The Laplacian matrix L = D - A, where D = diagonal degree matrix and A = adjacency matrix. Properties:
- Eigenvalues are all non-negative
- Smallest eigenvalue is 0 (with eigenvector = all ones)
- Number of zero eigenvalues = number of connected components
- **Fiedler value** (second-smallest eigenvalue λ₂): measures graph connectivity. Larger λ₂ = more robust connectivity.
- **Fiedler vector** (eigenvector of λ₂): naturally bisects the graph. Nodes with positive vs negative values define two communities.

### Spectral clustering

Use the k smallest eigenvectors of L (excluding the trivial all-ones vector) as features for each node. Apply k-means clustering in this spectral embedding. Effective for finding well-separated communities.

### Diffusion maps

Random walks on the graph define a diffusion process. The diffusion distance between two nodes captures how "similar" they are in terms of connectivity (not just direct connections but multi-hop paths). Diffusion maps embed neurons in a low-dimensional space where proximity reflects connectivity similarity.

---

## Worked example: analyzing a small circuit

**Given:** 10 neurons in a local circuit, with the following synapse-count adjacency matrix (rows = pre, columns = post):

```
     N1  N2  N3  N4  N5  N6  N7  N8  N9  N10
N1  [ 0   5   3   0   0   0   0   0   0   0 ]
N2  [ 4   0   6   0   0   0   0   0   0   0 ]
N3  [ 2   7   0   4   0   0   0   0   0   0 ]
N4  [ 0   0   3   0   5   2   0   0   0   0 ]
...
```

**Analysis steps:**
1. **Degree distribution:** Count in-degree and out-degree for each neuron. Identify any hubs (degree > 2× mean).
2. **Reciprocity:** For each pair, check if both A[i,j] > 0 and A[j,i] > 0. Compute fraction of reciprocal pairs.
3. **Clustering:** For each neuron, compute C(v). Compute global C.
4. **Community detection:** Apply Louvain algorithm. Do the detected communities correspond to known cell types?
5. **Path length:** Compute all-pairs shortest paths. Is the network small-world (short paths + high clustering)?

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "High degree = important neuron" | Degree measures connectivity, not functional importance; a hub could have many weak connections | Combine with centrality, functional data |
| "Small-world is special" | Many networks (social, technological, biological) are small-world; it's a necessary but not sufficient condition for specific computational properties | Small-world describes structure, not function |
| "Modularity finds the 'true' communities" | Modularity has a resolution limit and can find communities in random graphs | Validate detected communities with external information |
| "Spectral methods always work" | Spectral clustering assumes well-separated communities; real neural circuits may have graded, overlapping structure | Check assumptions; try multiple methods |

---

## References

- Humphries MD, Gurney K (2008) "Network 'small-world-ness': a quantitative method for determining canonical network equivalence." *PLoS ONE* 3(4):e0002051.
- Milo R et al. (2002) "Network motifs: simple building blocks of complex networks." *Science* 298(5594):824-827.
- Newman MEJ (2006) "Modularity and community structure in networks." *PNAS* 103(23):8577-8582.
- Peixoto TP (2014) "Hierarchical block structures and high-resolution model selection in large networks." *Physical Review X* 4(1):011047.
- Rubinov M, Sporns O (2010) "Complex network measures of brain connectivity: Uses and interpretations." *NeuroImage* 52(3):1059-1069.
- Sporns O (2010) *Networks of the Brain*. MIT Press.
- Towlson EK et al. (2013) "The rich club of the *C. elegans* neuronal connectome." *Journal of Neuroscience* 33(15):6380-6387.
- Varshney LR et al. (2011) "Structural properties of the *Caenorhabditis elegans* neuronal network." *PLoS Computational Biology* 7(2):e1001066.
- von Luxburg U (2007) "A tutorial on spectral clustering." *Statistics and Computing* 17(4):395-416.
- Watts DJ, Strogatz SH (1998) "Collective dynamics of 'small-world' networks." *Nature* 393(6684):440-442.
