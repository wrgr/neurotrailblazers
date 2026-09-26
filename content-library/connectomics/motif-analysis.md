---
layout: page
title: "Motif Analysis"
permalink: /content-library/connectomics/motif-analysis/
image: /assets/images/content-library/connectomics/motif-analysis.svg
image_alt: "Stylized vector art: a network graph with one community circled."
description: "Network motif analysis for connectomics — defining motifs, null models, statistical testing, DotMotif queries, subgraph isomorphism, and interpretation. Full instructor script with worked examples."
topics:
  - motifs
  - null-models
  - subgraph-isomorphism
  - DotMotif
  - statistics
primary_units:
  - "09"
difficulty: "Advanced"
tags:
  - connectomics:motif-analysis
  - connectomics:graph-theory
  - connectomics:subgraph-isomorphism
  - methodology:null-model
  - methodology:statistical-analysis
  - methodology:connectome-comparison
  - case-studies:c-elegans-motifs
  - case-studies:cortical-reciprocity
micro_lesson_id: ml-conn-motifs
combines_with:
  - graph-representations
  - network-analysis-methods
  - neuroai-bridge
content_type: core
---

## Overview

Network motifs are small connectivity patterns that occur more or less often than a null model predicts. Counting them is one of the few ways to turn a connectome of 10⁵ neurons into a short list of testable wiring preferences: reciprocal pairs, feed-forward loops, convergence onto one target. A motif count says which patterns the wiring favors. It does not say what those patterns compute, and the answer to "is it enriched?" depends heavily on the null model you pick. This page goes from hypothesis to interpretation, with the statistical traps on the way.

---

## Instructor script: what are network motifs?

### Definition

A **network motif** is a subgraph pattern that appears significantly more (or less) often in a network than in an appropriate null model. Milo et al. (2002) introduced the term and found that networks from different fields have different motif sets: gene regulatory networks and the *C. elegans* neuronal network shared the feed-forward loop, while food webs and the World Wide Web had motifs of their own.

### The 13 directed three-node motifs

A directed graph on 3 nodes can be connected in exactly 13 distinct ways, up to isomorphism. They run from a two-edge chain (A→B→C) to the fully reciprocal triad (A↔B, B↔C, A↔C). There is no single numbering: Sporns & Kötter (2004) label them 1 to 13, while Milo's mfinder tool uses IDs derived from the adjacency matrix (6, 12, 36, 38 and so on). When you report a motif by number, draw it as well.

Key motifs for neural circuits:

**Reciprocal pair (2-node):** A↔B. In paired recordings from layer 5 pyramidal neurons of rat visual cortex, bidirectionally connected pairs were four times more common than a random network with the same connection probability predicts (Song et al. 2005). Reciprocal connections can amplify signals, sustain persistent activity and support winner-take-all dynamics in models. Whether any given reciprocal pair does so is a separate, physiological question.

**Feed-forward loop (FFL):** A→B, A→C, B→C. Signal from A reaches C by two paths: directly (A→C) and through B (A→B→C). If both paths are excitatory, C receives input at two latencies, which can act as a temporal filter. Milo et al. (2002) found FFLs enriched in the *C. elegans* network, and Song et al. (2005) found several highly clustered three-neuron patterns over-represented in rat cortex. Perin et al. (2011) found that the probability that two pyramidal neurons in rat neocortex connect rises with the number of neighbors they share, a rule that by itself produces an excess of closed triads.

**Convergent motif:** A→C, B→C. Two independent sources project to the same target. Common in sensory integration circuits where information from multiple channels must be combined.

**Divergent motif:** A→B, A→C. One source broadcasts to multiple targets. Common in modulatory or command-neuron circuits.

**Chain:** A→B→C. Serial processing. The simplest multi-synaptic pathway.

**Feedback loop:** A→B→C→A. Cyclic structure enabling recurrence. Can sustain oscillations or maintain state.

### Motif profiles as network fingerprints

Milo et al. (2002) reported these motif sets:
- **Gene regulation (*E. coli*, yeast) and *C. elegans* neurons:** the feed-forward loop and the four-node bi-fan
- **Food webs:** the three-node chain and the bi-parallel
- **Electronic circuits:** feed-forward loops and bi-fans in combinational logic; feedback loops in sequential logic
- **World Wide Web:** triads with mutual (two-way) edges

Milo et al. (2004) compared normalized significance profiles and found "superfamilies". Neuronal wiring grouped with protein signaling and developmental gene networks, apart from microbial transcription networks, and social networks grouped with the Web. Their reading is that the motif profile reflects what the network does. That is a hypothesis about function, drawn from counts. The counts alone do not test it.

---

## Null models: the critical choice

### Why null models matter

A motif count means something only against a null expectation. In a hypothetical graph, "feed-forward loops appear 1,847 times" says nothing on its own. "Feed-forward loops appear 1,847 times, 3.2 standard deviations above the mean of 1,204 ± 198 in degree-preserving random graphs" is a claim someone can check.

**The null model is the most consequential choice in a motif analysis.** Each null asks a different question.

### Erdos-Renyi (ER) random graph

**Construction:** Each possible edge exists independently with probability p = (total edges) / (N × (N-1)).

**What it tests:** "Is this motif more common than in a completely random graph with the same density?"

**Problem:** ER graphs don't preserve degree distribution. Since hubs naturally participate in more motifs (purely by having more connections), comparing to ER will find almost everything enriched. **Rarely appropriate for connectomics.**

### Configuration model (degree-preserving)

**Construction:** Give each node its observed in-degree and out-degree, then connect the "stubs" at random. The result has exactly the degree sequence of the real network, though naive stub matching can create self-loops and duplicate edges that have to be rejected.

**What it tests:** "Is this motif more common than expected from the degree distribution alone?"

**Implementation:** the edge-swap method used by Maslov & Sneppen (2002). Pick two edges (A→B, C→D) at random and swap their targets to (A→D, C→B), rejecting any swap that creates a self-loop or a duplicate edge. A common rule of thumb is about 10 swaps per edge; check that your motif counts have stopped drifting before you trust the ensemble.

**This is the usual baseline in connectomics motif analyses**, and the weakest one you should report.

### Spatially constrained null model

**Construction:** Preserve the degree sequence and additionally preserve the distance-dependent connection probability. Neurons that are physically closer are more likely to be connected regardless of specific wiring rules.

**What it tests:** "Is this motif more common than expected from degree distribution AND spatial proximity?"

**Why it matters:** In cortical neuropil, nearby neurons have more arbor overlap, so connection probability falls with distance. A motif that looks enriched against a degree-preserving null may be explained by proximity alone: three neurons that are close together are more likely to be mutually connected. A motif that stays enriched after controlling for space is evidence of wiring specificity beyond proximity.

### Cell-type-stratified null model

**Construction:** Preserve connection rates within and between cell types. If, in your data, excitatory→inhibitory connections are three times as common as excitatory→excitatory ones, the null keeps that ratio.

**What it tests:** "Is this motif more common than expected from cell-type-specific connectivity rates?"

**Why it matters:** Excitatory-inhibitory structure alone biases motif counts. A disynaptic E→I→E pattern, or a feed-forward loop with an inhibitory middle node, can look enriched simply because E→I and I→E connections are common, with no three-neuron wiring rule involved.

---

## Statistical testing

### Z-score

z = (observed_count - mean_null) / std_null

This is the number of standard deviations above or below the null mean. |z| > 2 is the usual threshold for a single test, but see the correction for multiple comparisons below. A z-score turns into a p-value only if the null distribution is roughly normal, and motif counts in sparse graphs often are not.

### P-value from the null distribution

Generate K randomizations (typically 1,000 to 10,000) and count how many null graphs have a motif count at least as large as the observed one. Call that r. The empirical p-value is (r + 1) / (K + 1); the +1 counts the observed graph as one draw from the null and stops you reporting p = 0.

With K randomizations the smallest p you can report is 1/(K + 1). With 10,000 nulls, that is about 10⁻⁴, however large z is. For anything smaller you need more randomizations or an analytical approximation, and you should say which.

### Multiple comparison correction

If you test all 13 three-node motifs, you run 13 tests. There are 199 connected four-node directed patterns, so adding those takes you past 200. Correction options:
- **Bonferroni:** Divide significance threshold by number of tests. Conservative.
- **FDR (Benjamini-Hochberg):** Control false discovery rate. Less conservative, more appropriate when testing many motifs.

### Sensitivity analysis

Report results across multiple null models and thresholds:
- Does the enrichment hold for degree-preserving AND spatially constrained nulls?
- Does it hold at synapse-count thresholds of 1, 3, and 5?
- Does it survive a newer proofreading version of the same dataset?

If a finding disappears under any one of these, report that. It may still be real, but you cannot yet tell it apart from how the graph was built.

---

## DotMotif query language

### What it is

DotMotif (Matelsky et al. 2021) is a small query language and Python library for finding motif instances in connectome graphs. You write the pattern as text; an "executor" runs the search against a NetworkX graph, a Neo4j database or the pure-Python GrandIso engine.

### Syntax

```dotmotif
# Feed-forward loop
A -> B
A -> C
B -> C
```

```dotmotif
# Reciprocal pair with synapse count constraint
A -> B [weight >= 3]
B -> A [weight >= 3]
```

```dotmotif
# Cell-type-constrained motif
A -> B
A -> C
A.type = "excitatory"
B.type = "inhibitory"
C.type = "excitatory"
```

```dotmotif
# Feed-forward loop with no extra edges: forbid the three reverse edges
A -> B
A -> C
B -> C
B !> A
C !> A
C !> B
```

The last example matters for counting. An edge you do not mention is allowed but not required, so the first FFL query also matches triads that contain extra reverse edges. The `!>` operator forbids an edge. Counting "FFLs" with and without the prohibitions gives different numbers, and the 13-motif census assumes the strict (induced) version. Say which you counted.

### How queries execute

DotMotif compiles a query to a subgraph isomorphism search: find every place in the large graph where the small pattern fits. By default a symmetric pattern is returned once per automorphism (a reciprocal pair A↔B comes back twice, as A=1, B=2 and A=2, B=1); the `exclude_automorphisms` option returns one match per instance. Run time depends on graph density, hub degree and how many constraints prune the search, so time a small subgraph before launching a whole-connectome query.

### Alternative tools

- **graph-tool** (Python with a C++ core): `graph_tool.topology.subgraph_isomorphism()` for matching, and `graph_tool.clustering.motif_significance()` for counts with z-scores against a randomized ensemble.
- **NetworkX** (Python): `DiGraphMatcher` in `networkx.algorithms.isomorphism`. Its `subgraph_isomorphisms_iter()` finds induced matches and `subgraph_monomorphisms_iter()` non-induced ones. Pure Python, so slower on large graphs.
- **igraph** (C core, Python and R interfaces): `Graph.subisomorphic_vf2()` and `Graph.subisomorphic_lad()` in Python; `Graph.motifs_randesu()` (Python) or `motifs()` (R) counts all 3- or 4-node motifs in one pass.
- **SQL or Cypher**: for connectomes stored in a database, a motif query is a series of joins on the edge table.

---

## Subgraph isomorphism complexity

### The theory

Subgraph isomorphism (does pattern graph H occur as a subgraph of target graph G?) is NP-complete (Cook 1971). No known algorithm is efficient on every input.

### In practice

The pattern is tiny and the target is sparse, which is the easy case. For 3- and 4-node motifs in a graph of 10⁵ neurons, the usual tools work:

- **VF2** (Cordella et al. 2004): backtracking search with pruning rules. It is the algorithm behind NetworkX's matcher and one of igraph's two.
- **Constraint filtering**: shrink the candidate set first, by degree, cell type or synapse-count threshold. Constraints written into a DotMotif query do this for you.
- **Parallel search**: split candidate start nodes across cores or machines.

Cost rises steeply with pattern size, because the number of partial matches grows roughly with the degree raised to the motif size. So 3-node counts on a 10⁵-node graph are routine, 4-node counts usually feasible, and exhaustive 5- and 6-node enumeration is often impractical. These are rough guides, not benchmarks. Hubs dominate the cost, so a graph with a few neurons of degree 10⁴ can be far slower than its size suggests. For large motifs, sampling methods estimate counts without enumerating every instance.

---

## Interpreting motif results

### An enriched motif is a wiring preference, not a function

A statistically enriched motif is not thereby a "functional circuit". Enrichment describes wiring preferences, not dynamics. Whether a feed-forward loop in the connectome filters anything in time depends on synapse strengths, time constants and neuromodulatory state, and the graph records none of them.

Bargmann & Marder (2013) argue that the same circuit can produce different outputs depending on neuromodulatory state, and that different circuits can produce similar outputs. Structure constrains function; it does not determine it.

### What motif analysis can tell you

- Wiring preferences: which local patterns are favored or avoided
- Organizational principles: does the circuit resemble a random graph, a feed-forward cascade, a recurrent network, or something else?
- Hypotheses for functional experiments: enriched motifs are candidates for targeted optogenetic or pharmacological manipulation
- Cross-species comparison: are the same motifs enriched in worm, fly, and mouse?

---

## Worked example: reciprocal connection analysis

**Question:** Are reciprocal connections (A↔B) enriched in mouse cortex layer 2/3?

The numbers below are **synthetic**, from a fictional mouse cortex volume at "release T31". They show the procedure and the arithmetic; they are not results from any real dataset. On real data, pin a real materialization version (for MICrONS, a numbered version of `minnie65_public`) and report it.

**Step 1: Define the motif.** Reciprocal pair: A→B AND B→A, with ≥3 synapses in each direction.

**Step 2: Count in the data.** Query the fictional volume at release T31. Among all L2/3 excitatory neuron pairs: 2,847 reciprocal pairs.

**Step 3: Generate null ensemble.** 10,000 degree-preserving random rewirings of the L2/3 excitatory subgraph. Mean reciprocal pairs in null: 712 ± 89.

**Step 4: Compute statistics.** z = (2,847 − 712) / 89 = 24.0. None of the 10,000 null graphs reached 2,847, so the empirical p-value is 1/10,001, about 10⁻⁴. That is the smallest p this ensemble can support. Do not convert z = 24 into p < 10⁻¹⁰ through a normal approximation the null distribution has not been shown to follow.

**Step 5: Control for space.** Spatially constrained null (preserving distance-dependent connection probability): mean 1,423 ± 124. z = (2,847 − 1,423) / 124 = 11.5, and again no null graph reached the observed count.

**Step 6: Interpret.** Reciprocal pairs are enriched 4.0× over the degree-preserving expectation (2,847 / 712) and 2.0× over the spatial one (2,847 / 1,423). The spatial null removed half of the apparent effect; what remains is the part worth a biological claim. The direction matches the overrepresentation of bidirectional connections that Song et al. (2005) reported from paired recordings in rat layer 5, but synthetic numbers replicate nothing. On real data, this pattern would suggest a specific wiring rule favoring reciprocity beyond what spatial proximity and degree structure predict.

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "Enriched motifs are functional circuits" | Enrichment reveals wiring preference, not function | Combine with functional experiments |
| "Degree-preserving null is always sufficient" | Spatial and cell-type structure create additional baselines | Use the most stringent null relevant to your question |
| "More motifs tested = more thorough" | Testing many motifs inflates false positives | Correct for multiple comparisons; focus on hypothesis-driven motifs |
| "Motif counts are deterministic" | Proofreading updates change the graph → motif counts shift | Pin to a specific data version; report sensitivity |
| "z = 24, so p is astronomically small" | An empirical p-value cannot be smaller than 1/(K + 1) for K null graphs, and the null distribution need not be normal | Report r/K alongside z; state K |
| "A feed-forward-loop query counts feed-forward loops" | A pattern with unmentioned edges also matches triads that have extra edges | Decide between induced and non-induced counts before counting; in DotMotif, forbid edges with `!>` |

---

## References

- Bargmann CI, Marder E (2013) "From the connectome to brain function." *Nature Methods* 10(6):483-490. [10.1038/nmeth.2451](https://doi.org/10.1038/nmeth.2451)
- Cook SA (1971) "The complexity of theorem-proving procedures." *Proceedings of the Third Annual ACM Symposium on Theory of Computing*, 151-158. [10.1145/800157.805047](https://doi.org/10.1145/800157.805047)
- Cordella LP, Foggia P, Sansone C, Vento M (2004) "A (sub)graph isomorphism algorithm for matching large graphs." *IEEE Transactions on Pattern Analysis and Machine Intelligence* 26(10):1367-1372. [10.1109/TPAMI.2004.75](https://doi.org/10.1109/TPAMI.2004.75)
- Maslov S, Sneppen K (2002) "Specificity and stability in topology of protein networks." *Science* 296(5569):910-913. [10.1126/science.1065103](https://doi.org/10.1126/science.1065103)
- Matelsky JK et al. (2021) "DotMotif: an open-source tool for connectome subgraph isomorphism search and graph queries." *Scientific Reports* 11:13045. [10.1038/s41598-021-91025-5](https://doi.org/10.1038/s41598-021-91025-5)
- Milo R et al. (2002) "Network motifs: simple building blocks of complex networks." *Science* 298(5594):824-827. [10.1126/science.298.5594.824](https://doi.org/10.1126/science.298.5594.824)
- Milo R et al. (2004) "Superfamilies of evolved and designed networks." *Science* 303(5663):1538-1542. [10.1126/science.1089167](https://doi.org/10.1126/science.1089167)
- Perin R, Berger TK, Markram H (2011) "A synaptic organizing principle for cortical neuronal groups." *PNAS* 108(13):5419-5424. [10.1073/pnas.1016051108](https://doi.org/10.1073/pnas.1016051108)
- Song S, Sjöström PJ, Reigl M, Nelson S, Chklovskii DB (2005) "Highly nonrandom features of synaptic connectivity in local cortical circuits." *PLoS Biology* 3(3):e68. [10.1371/journal.pbio.0030068](https://doi.org/10.1371/journal.pbio.0030068)
- Sporns O, Kötter R (2004) "Motifs in brain networks." *PLoS Biology* 2(11):e369. [10.1371/journal.pbio.0020369](https://doi.org/10.1371/journal.pbio.0020369)
