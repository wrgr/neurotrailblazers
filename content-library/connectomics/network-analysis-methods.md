---
layout: page
title: "Network Analysis Methods"
permalink: /content-library/connectomics/network-analysis-methods/
image: /assets/images/content-library/connectomics/network-analysis-methods.svg
image_alt: "Stylized vector art: a network graph with one community circled."
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
tags:
  - connectomics:graph-theory
  - connectomics:degree-distribution
  - connectomics:clustering-coefficient
  - connectomics:community-detection
  - connectomics:small-world
  - connectomics:rich-club
  - connectomics:spectral-analysis
  - methodology:centrality-measures
  - methodology:modularity
  - neuroanatomy:hub-neurons
micro_lesson_id: ml-conn-network-analysis
combines_with:
  - graph-representations
  - motif-analysis
  - neuroai-bridge
content_type: core
---

## Overview

Once a connectome is a graph, the standard network-science measures apply: node properties (degree, centrality), local structure (clustering, motifs) and global organization (path length, modularity, spectral properties). Most of them were built for complete, unweighted graphs that are not embedded in space. An EM connectome is none of those, and the section "Which of these survive an EM connectome" below says which measures break first. This page gives each method's definition, what it means biologically, and a small worked example.

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

Connectome degree distributions are **heavy-tailed**: many neurons with few partners and a few "hub" neurons with many. The functional form is hard to pin down. Varshney et al. (2011) found that the tails of several *C. elegans* degree distributions could be fit by power laws, but for some of them an exponential fit could not be ruled out, and with 279 neurons the tail holds few points. Treat any claim that a connectome is "scale-free" with suspicion unless the fit was compared against alternatives.

**Typical values:**
- *C. elegans*: mean degree about 14 in the undirected 282-neuron graph that Watts & Strogatz (1998) analyzed, with command interneurons such as AVA and AVB in the high-degree tail
- Drosophila (hemibrain, FlyWire): heavy-tailed; compute the values for the release you pin rather than quoting a single number
- Mouse cortex (MICrONS): varies by cell type and by how much of each arbor lies inside the volume

### Hub neurons

Neurons in the high-degree tail are called hubs. In *C. elegans*, the command interneurons of the locomotor circuit (AVA, AVB, PVC and others) are hubs that receive from many interneurons and drive motor neurons (Towlson et al. 2013). In a fly or mouse dataset, find the hubs in the release you pin; do not assume them from another animal.

**Biological interpretation:** Hub neurons are candidates for integration or relay points. High degree alone does not prove functional importance: a neuron can have many weak connections that are individually negligible, and a neuron near the volume boundary can look like a non-hub because half its arbor is missing.

---

## Clustering coefficient

### Definition

The clustering coefficient C(v) of node v measures the density of connections among v's neighbors:

C(v) = (number of edges among neighbors of v) / (maximum possible edges among neighbors of v)

For a directed graph with k neighbors, the maximum possible number of edges among them is k(k−1), because each pair can be connected both ways. The **average clustering coefficient** is the mean of C(v) over nodes, which is what Watts & Strogatz (1998) reported. The **global clustering coefficient** (transitivity) is a different number: three times the number of triangles divided by the number of connected triples. Say which one you computed.

### Biological meaning

High clustering means: if neuron A connects to both B and C, then B and C are also likely connected. This indicates **local circuit density** — triadic closure, recurrent loops, and interconnected neuronal groups.

**Empirical values:**
- *C. elegans*: C = 0.28 (Watts & Strogatz 1998, undirected graph). A random graph with the same number of nodes and mean degree has C = 0.05, so the worm network is 5.6 times as clustered.
- Drosophila: varies by brain region and by synapse threshold; compute it for the release and threshold you pin
- Random Erdos-Renyi graph with same density: C ≈ p (connection probability), typically <0.01 for sparse graphs

### Interpretation caution

High clustering can come from spatial proximity (nearby neurons connect more often because their arbors overlap) rather than from specific wiring rules. Spatially constrained null models ([Motif Analysis]({{ '/content-library/connectomics/motif-analysis/' | relative_url }})) help separate the two.

---

## Path length and small-world structure

### Shortest path length

The shortest path between nodes u and v is the minimum number of edges traversed to reach v from u. The **characteristic path length** L is the average shortest path over all pairs.

### Small-world property

A network is "small-world" (Watts & Strogatz 1998) if:
- L ≈ L_random (path lengths are short, comparable to a random graph)
- C >> C_random (clustering is much higher than random)

**Biological interpretation:** The usual reading is that high clustering supports local processing and short paths support integration, since a signal can reach any neuron in a few steps. Watts & Strogatz (1998) showed the *C. elegans* network is small-world: L = 2.65 against 2.25 for a matched random graph, with C = 0.28 against 0.05. The section "Small-worldness in particular" below explains why that label says less than it seems to.

### Global efficiency

E_global = mean(1/d(u,v)) over all pairs u, v, where d is shortest path length (Latora & Marchiori 2001). Unlike characteristic path length, it stays defined when the graph has disconnected parts: an unreachable pair contributes 0 instead of infinity.

---

## Centrality measures

### Betweenness centrality

B(v) = the sum, over all pairs of other nodes s and t, of the fraction of shortest s-to-t paths that pass through v. A node with high betweenness sits on many shortest routes: a candidate relay or bottleneck, if signals in fact travel along shortest paths, which is an assumption.

**In connectomics:** Neurons with high betweenness may act as integration hubs or relay stations. In *C. elegans*, Towlson et al. (2013) report that the rich-club neurons, almost all interneurons of the locomotor circuits, are connector hubs with high betweenness centrality.

### PageRank

PageRank was developed for web search (Brin & Page 1998). On a connectome, a neuron scores highly if it receives input from neurons that themselves score highly. It is computed iteratively: PR(v) = (1−d)/N + d × Σ PR(u)/k_out(u), summed over all u → v, with damping factor d (conventionally 0.85). Neurons with no outputs need special handling, and a weighted version uses synapse counts in place of k_out.

**Application:** finding neurons that receive input from other well-connected neurons, which degree alone misses.

### Eigenvector centrality

Similar to PageRank but using the dominant eigenvector of the adjacency matrix. Neurons with high eigenvector centrality are connected to other high-centrality neurons.

---

## Community detection

### Modularity optimization

**Modularity Q** (Newman 2006) measures whether a proposed partition of the graph into communities has more within-community edges than expected by chance:

Q = (1/2m) × Σ[A_ij - (k_i × k_j)/(2m)] × δ(c_i, c_j)

where m = total edges, k_i = degree of node i, c_i = community of node i, δ = 1 if same community.

This is the undirected form; for a directed connectome, use the directed version (Leicht & Newman 2008) or say that you symmetrized the graph. Optimization algorithms (Louvain, Leiden) find partitions with high Q. On a connectome, the result is groups of neurons more densely interconnected than expected: candidate functional modules or cell-type communities, to be checked against other data.

### Stochastic block models (SBM)

A stochastic block model (SBM) is a generative model: each node belongs to a block, and the probability of an edge between two nodes depends only on their blocks. Peixoto (2014) developed a nested (hierarchical) version with principled model selection, implemented in graph-tool.

**Advantages over modularity:** SBMs can detect both assortative communities (dense within) and disassortative structure (dense between different groups, as in excitatory-inhibitory networks). They also provide model selection criteria for choosing the number of communities.

**Application in connectomics:** Pavlovic et al. (2014) fit a block model to the *C. elegans* connectome. Louvain and spectral methods found 4 to 5 modules; the block model found 9 groups, including a small, densely connected core that the modularity methods could not express, and the authors judged it more consistent with what is known about the worm's neurons.

### Hierarchical community structure

Neural circuits likely have nested community structure — local microcircuits within larger modules within brain-wide systems. Hierarchical SBMs and multi-resolution community detection methods can capture this nesting.

---

## Rich-club organization

### Definition

The rich-club coefficient φ(k) measures whether nodes with degree > k preferentially connect to each other. For an undirected graph with N_>k such nodes and E_>k edges among them, φ(k) = 2E_>k / (N_>k(N_>k − 1)), the density of the subgraph they form.

Hubs are densely connected to each other partly because they have many edges, so normalize against degree-preserving random graphs: φ_norm(k) = φ(k) / φ_random(k). Values reliably above 1 indicate rich-club structure.

### In connectomics

*C. elegans* has a rich club (Towlson et al. 2013). In a network of 279 neurons and 2,287 connections, 11 highly connected neurons, almost all locomotor interneurons, are densely interconnected, and the shortest paths between peripheral neurons most often pass through them. Towlson et al. read this as an integrative backbone whose high wiring cost is paid for by coordinated movement.

---

## Spectral methods

### Graph Laplacian

The Laplacian matrix L = D − A, where D is the diagonal degree matrix and A the adjacency matrix. The properties below hold for an undirected graph; symmetrize a directed connectome first, or use a directed variant. Properties:
- Eigenvalues are all non-negative
- Smallest eigenvalue is 0 (with eigenvector = all ones)
- Number of zero eigenvalues = number of connected components
- **Fiedler value** (second-smallest eigenvalue λ₂): measures how well connected the graph is. A larger λ₂ means more edges must be cut to split it.
- **Fiedler vector** (eigenvector of λ₂): naturally bisects the graph. Nodes with positive vs negative values define two communities.

### Spectral clustering

Take the eigenvectors belonging to the k smallest eigenvalues of L (usually of a normalized Laplacian) as coordinates for each node, then run k-means in that embedding (von Luxburg 2007). It works well when communities are well separated.

### Diffusion maps

Random walks on the graph define a diffusion process. The diffusion distance between two nodes captures how "similar" they are in terms of connectivity (not just direct connections but multi-hop paths). Diffusion maps embed neurons in a low-dimensional space where proximity reflects connectivity similarity.

---

## Worked example: analyzing a small circuit

**Given:** a synthetic circuit of 10 neurons, N1 to N10, invented for this exercise. The matrix gives synapse counts (rows = presynaptic, columns = postsynaptic). Treat every non-zero entry as an edge.

```
     N1  N2  N3  N4  N5  N6  N7  N8  N9  N10
N1  [ 0   5   3   0   0   0   0   0   0   0 ]
N2  [ 4   0   6   0   0   0   0   0   0   0 ]
N3  [ 2   7   0   4   0   0   0   0   0   0 ]
N4  [ 0   0   3   0   5   2   0   0   0   0 ]
N5  [ 0   0   2   1   0   0   0   0   0   0 ]
N6  [ 0   0   0   0   0   0   4   3   0   0 ]
N7  [ 0   0   0   0   0   3   0   5   2   0 ]
N8  [ 0   0   0   1   0   0   2   0   4   0 ]
N9  [ 0   0   0   0   0   0   0   3   0   6 ]
N10 [ 0   0   0   0   0   0   2   0   5   0 ]
```

**Analysis steps:**
1. **Degree:** count in-degree and out-degree for each neuron. Call a neuron a hub if its total degree is more than twice the mean.
2. **Reciprocity:** a pair is reciprocal if both A[i,j] > 0 and A[j,i] > 0. Compute the fraction of connected pairs that are reciprocal.
3. **Clustering:** ignoring direction and weight, compute C(v) for each neuron and the average clustering coefficient.
4. **Communities:** compute modularity Q (undirected, unweighted) for the split {N1–N5}, {N6–N10}, then run Louvain and see whether it finds the same split.
5. **Path length:** compute all-pairs shortest paths. Is it meaningful to call this network small-world?

**Check yourself** (computed from the matrix above):

1. There are 24 directed edges. Out-degree is 2 or 3 for every neuron; in-degree runs from 1 (N5, N10) to 4 (N3). Mean total degree is 4.8, and the largest is 7 (N3), so no neuron passes the 2× rule. A 10-neuron circuit rarely has hubs by this definition, and that is a fair result.
2. Of 15 connected pairs, 9 are reciprocal (60%); 18 of the 24 edges belong to a reciprocal pair (75%). Both definitions are in use, so say which one you report.
3. Average C = 0.70. N3 and N4 have the lowest values (0.33 each), because their neighbors sit in different groups. The undirected density is 15/45 = 0.33, which is also the expected C of a random graph with this density, so clustering is about 2.1× random.
4. Q = 0.36 for the {N1–N5}, {N6–N10} split. Only two undirected edges (N4–N6 and N4–N8) cross it.
5. Ignoring direction, the mean shortest path is 2.27 edges and the longest is 5 (for example N1 to N10). Following direction, every neuron can reach every other, with a mean path of 2.58. With 10 neurons and a density of 0.33 there is no meaningful random baseline to be "small" relative to, so the honest answer to the small-world question is that it cannot be asked of a graph this size.

---

## Which of these survive an EM connectome

The measures above are the standard network-science toolkit, and most of them
were developed on graphs that differ from a connectome in ways that matter:
complete, unweighted, unsigned, and not embedded in space. A nanoscale
connectome is none of those things. Before applying any of them, work out which
column you are in.

| Measure | Sensitive to thresholding? | Sensitive to incompleteness? | Usable on a truncated volume? |
|---|---|---|---|
| **Degree** | Strongly — most edges are single-synapse | Strongly — boundary truncation removes real partners | Only for cells whose arbor is fully contained |
| **Clustering coefficient** | Strongly | Strongly | Rarely |
| **Path length / small-worldness** | Strongly | Severely — a missing edge can change many paths | No |
| **Betweenness centrality** | Strongly | Severely, for the same reason | No |
| **Modularity** | Moderately | Moderately | With care, if modules are local |
| **Motif counts (local)** | Strongly | Moderately | Yes, within the contained region |
| **Reciprocity** | Strongly | Moderately | Yes, for contained pairs |

The pattern: **anything defined over global paths is the first thing to break,
and the last thing people check.** Path length and betweenness assume you can
see the whole graph. In a cubic millimeter of cortex you cannot — most
long-range axons leave the volume — so a path-based statistic is measuring your
volume boundary as much as the circuit.

### Small-worldness in particular

Small-worldness is the most-reported and least-informative statistic in this
list. Two problems compound. First, it is weakly discriminating: an enormous
range of networks satisfy it, so reporting that a connectome is small-world
distinguishes it from very little. Second, it is highly sensitive to density
and therefore to your synapse threshold — so a difference in small-worldness
between two datasets can be a difference in how the graphs were built rather
than in how the brains are wired.

If you find yourself reporting it, ask what claim it is supporting that a more
specific local statistic would not support better. Usually there is one, and
usually it is a motif or a cell-type-pair connection probability.

---

## Working an analysis end to end

The measures are easy; the decisions around them are the work. A defensible
analysis states each decision before it produces a number.

1. **Define the node set, and say what it excludes.** Cells with somata in the
   volume? Cells with any process in it? The two differ by an order of
   magnitude and support different claims. Truncated cells cannot carry degree.
2. **Define the edge, and report the threshold.** Synapse count per ordered
   pair, thresholded at some value. Re-run the analysis at two or three
   thresholds and report whether the conclusion moves.
3. **Pin the version.** Dataset, materialization, date, query. Without it the
   analysis is not repeatable, including by you in six months.
4. **Choose the null before you look.** For a spatially embedded,
   degree-heterogeneous graph, Erdős–Rényi will call almost anything
   structured. A degree-preserving configuration model controls for one thing;
   a distance-preserving null controls for the one that usually dominates.
   State which you pre-specified.
5. **Correct for the tests you ran**, not only the ones you report. A full
   triad census has sixteen classes, thirteen of them connected, so it is
   thirteen to sixteen simultaneous tests.
6. **Put an error band on it.** Inject merge and split errors at the rates your
   dataset reports and re-measure. If the effect does not survive, that is the
   result.

Steps 4 through 6 are where connectomics network analyses are most often weak.
[Unit
09]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
works a reciprocity example in which the same data supports "2.9× enrichment,
p < 10⁻⁶" or "no detectable effect" depending only on which null was chosen
before any test ran.

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "High degree = important neuron" | Degree measures connectivity, not functional importance; a hub could have many weak connections | Combine with centrality, functional data |
| "Small-world is special" | Many networks (social, technological, biological) are small-world, so the label distinguishes a connectome from very little | Small-world describes structure, not function |
| "Modularity finds the 'true' communities" | Modularity has a resolution limit and can find communities in random graphs | Validate detected communities with external information |
| "Spectral methods always work" | Spectral clustering assumes well-separated communities; real neural circuits may have graded, overlapping structure | Check assumptions; try multiple methods |

---

## References

- Brin S, Page L (1998) "The anatomy of a large-scale hypertextual Web search engine." *Computer Networks and ISDN Systems* 30(1-7):107-117. [10.1016/S0169-7552(98)00110-X](https://doi.org/10.1016/S0169-7552(98)00110-X)
- Humphries MD, Gurney K (2008) "Network 'small-world-ness': a quantitative method for determining canonical network equivalence." *PLoS ONE* 3(4):e0002051.
- Latora V, Marchiori M (2001) "Efficient behavior of small-world networks." *Physical Review Letters* 87(19):198701. [10.1103/PhysRevLett.87.198701](https://doi.org/10.1103/PhysRevLett.87.198701)
- Leicht EA, Newman MEJ (2008) "Community structure in directed networks." *Physical Review Letters* 100(11):118703. [10.1103/PhysRevLett.100.118703](https://doi.org/10.1103/PhysRevLett.100.118703)
- Milo R et al. (2002) "Network motifs: simple building blocks of complex networks." *Science* 298(5594):824-827.
- Newman MEJ (2006) "Modularity and community structure in networks." *PNAS* 103(23):8577-8582.
- Pavlovic DM, Vértes PE, Bullmore ET, Schafer WR, Nichols TE (2014) "Stochastic blockmodeling of the modules and core of the *Caenorhabditis elegans* connectome." *PLoS ONE* 9(7):e97584. [10.1371/journal.pone.0097584](https://doi.org/10.1371/journal.pone.0097584)
- Peixoto TP (2014) "Hierarchical block structures and high-resolution model selection in large networks." *Physical Review X* 4(1):011047.
- Rubinov M, Sporns O (2010) "Complex network measures of brain connectivity: Uses and interpretations." *NeuroImage* 52(3):1059-1069.
- Sporns O (2010) *Networks of the Brain*. MIT Press.
- Towlson EK et al. (2013) "The rich club of the *C. elegans* neuronal connectome." *Journal of Neuroscience* 33(15):6380-6387.
- Varshney LR et al. (2011) "Structural properties of the *Caenorhabditis elegans* neuronal network." *PLoS Computational Biology* 7(2):e1001066.
- von Luxburg U (2007) "A tutorial on spectral clustering." *Statistics and Computing* 17(4):395-416.
- Watts DJ, Strogatz SH (1998) "Collective dynamics of 'small-world' networks." *Nature* 393(6684):440-442.
