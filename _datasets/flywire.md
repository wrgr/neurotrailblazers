---
title: "FlyWire — complete adult fly brain"
short_name: "FlyWire"
species: "Drosophila melanogaster (female)"
region: "Whole brain, including optic lobes"
volume: "Whole brain"
cells: "139,255 neurons; 8,453 cell types"
synapses: "~54.5 million"
size: "~50 TB"
resolution: "4 nm in-plane, 40 nm sections"
modality: "Serial-section TEM, community proofread"
portal: "https://flywire.ai/"
paper_doi: "10.1038/s41586-024-07558-y"
paper_url: "https://www.nature.com/articles/s41586-024-07558-y"
press_url: "https://www.princeton.edu/news/2024/10/02/mapping-entire-fly-brain-step-toward-understanding-diseases-human-brain"
access: "Open; Codex browser and CAVEclient"
status: "Released"
release_year: 2024
featured: true
blurb: "The first complete connectome of an adult animal brain: every neuron, every synapse, hierarchically annotated, and proofread by a distributed community over several years."
source: "Dorkenwald et al. (2024), Nature 10.1038/s41586-024-07558-y; FlyWire Codex."
---

FlyWire is the existence proof that a whole-brain connectome of a behaving animal is
achievable. An adult female fly brain was imaged by ssTEM, segmented automatically, and then
corrected by a community of proofreaders — thousands of hours of human labour — to 139,255
neurons and about 54.5 million synaptic connections, with a hierarchical annotation of classes,
cell types and developmental units.

**What it is good for.** Graph analysis with a complete edge list. It is the only large dataset
where "I have the whole network" is true, so it is the right place to learn null models: you can
compare an observed motif count against a degree-preserving randomisation without worrying that
your finding is an artefact of a truncated volume. It is also the clearest case study in what
proofreading costs and who gets credit for it.

**What it does not support.** Generalisation to a second fly. This is one individual; the
across-animal variability of the connectome is an open question, and the hemibrain and MANC
datasets exist partly to address it. It is also structure only — no activity was recorded from
this brain.
