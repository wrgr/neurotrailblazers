---
title: "FlyWire — complete adult fly brain"
short_name: "FlyWire"
species: "Drosophila melanogaster (female)"
region: "Whole brain, including optic lobes"
volume: "Whole brain"
cells: "139,255 neurons; more than 8,400 cell types"
synapses: "~54.5 million"
size: "~106 TB (FAFB imagery)"
resolution: "4 × 4 × 40 nm"
modality: "Serial-section TEM, community proofread"
portal: "https://codex.flywire.ai/"
paper_doi: "10.1038/s41586-024-07558-y"
paper_url: "https://www.nature.com/articles/s41586-024-07558-y"
press_url: "https://www.princeton.edu/news/2024/10/02/mapping-entire-fly-brain-step-toward-understanding-diseases-human-brain"
access: "Open; Codex browser and downloads, CAVEclient with a free token. Data CC BY-NC 4.0 (flywire.ai/guidelines)"
status: "Released"
release_year: 2024
featured: true
blurb: "The first complete connectome of an adult animal brain: every neuron and synapse in one fly's brain, annotated by cell type, and proofread by a distributed community over several years."
source: "Dorkenwald et al. (2024), Nature: neuron and synapse counts, the 33 person-year proofreading estimate, and the analysis release (v783). Cell-type count from Schlegel et al. (2024), as cited in Dorkenwald et al. Imagery size from Zheng et al. (2018), Cell (FAFB). Data license from flywire.ai/guidelines."
---

FlyWire showed that a whole-brain connectome of an adult animal can be finished. An adult
female fly brain (the FAFB volume, imaged by Zheng, Bock and colleagues) was segmented
automatically and then corrected by a community of proofreaders. The authors estimate about
33 person-years of manual proofreading. The result is 139,255 neurons and about 54.5 million
synapses, with a companion annotation of more than 8,400 cell types. The paper's analyses
use release v783.

**What it is good for.** Graph analysis with a complete edge list. It is the only large dataset
where "I have the whole network" is true, so it is the right place to learn null models: you can
compare an observed motif count against a degree-preserving randomization without worrying
that your finding comes from a truncated volume. It is also the clearest case study in what
proofreading costs and who gets credit for it.

**What it does not support.** Generalization to a second fly. This is one individual, and
how much connectomes vary between animals is still an open question; the hemibrain and the
male CNS datasets are the first comparisons. It is also structure only: no activity was
recorded from this brain. And the data license is non-commercial (CC BY-NC 4.0), even though
the paper itself is CC BY 4.0.
