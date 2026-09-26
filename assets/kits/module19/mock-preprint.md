# Mock preprint for the Module 19 review board

> **Fictional teaching document.** This preprint does not exist. Its title,
> authors, numbers, figures and claims were written for a peer-review exercise.
> No analysis of any dataset was performed to produce it, and nothing in it is a
> finding. It is written to contain four specific problems for reviewers to find.

## A feed-forward inhibitory motif is enriched in mouse visual cortex and may drive seizure propagation

**Authors:** A. Author, B. Author, C. Author, and the Data Release Consortium

### Abstract

Feed-forward inhibition shapes the timing of cortical responses. Using a public
electron microscopy connectome of mouse visual cortex (MICrONS minnie65, CAVE
materialization v661), we counted all three-node motifs among 2,114 neurons with
somata in the volume. A feed-forward inhibitory loop, in which a pyramidal cell
drives both an interneuron and a second pyramidal cell that the interneuron also
inhibits, was enriched 3.5-fold relative to a degree-preserving random graph
(p < 0.001, Bonferroni-corrected across 13 motif classes). Because this motif
controls the gain of excitation, it likely plays a causal role in seizure
propagation, and it is a candidate target for anti-epileptic therapy.

### Methods (excerpt)

[M1] Synapses were taken from the public synapse table. Neurons were included if
their soma lay within the volume. Edges were defined as one or more synapses from
one neuron to another. [M2] Motifs were counted with DotMotif. The null model was
1,000 degree-preserving rewirings of the full graph. [M3] We tested three motifs
of prior interest: the feed-forward inhibitory loop, the reciprocal excitatory
pair, and the disinhibitory chain.

### Results (excerpt)

[R1] The feed-forward inhibitory loop occurred 1,812 times, against a null mean of
518 (SD 41). **Figure 1.** Observed count against the null distribution for the
feed-forward inhibitory loop. Bars show the null histogram; the line shows the
observed count. [R2] Loops were distributed across all layers sampled.
**Figure 2.** Loop count per interneuron, sorted. Twelve interneurons participate
in more than half of all loops. No error bars are shown.

### Discussion (excerpt)

[D1] Our results establish that feed-forward inhibition is a dominant organizing
principle of visual cortex. [D2] Given that disruption of feed-forward inhibition
is observed in epilepsy, this motif likely plays a causal role in seizure
propagation.

### Author contributions

The Data Release Consortium contributed to this work.
