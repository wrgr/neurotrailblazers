---
title: "Hemibrain — Drosophila central brain"
short_name: "Hemibrain"
species: "Drosophila melanogaster (female)"
region: "Central brain (~50%)"
volume: "250 × 250 × 250 μm"
cells: "~25,000 neurons"
synapses: "~20 million"
size: "~100 TB"
resolution: "8 nm isotropic"
modality: "FIB-SEM"
portal: "https://neuprint.janelia.org/"
paper_doi: "10.7554/eLife.57443"
paper_url: "https://elifesciences.org/articles/57443"
press_url: "https://www.janelia.org/news/unveiling-the-biggest-and-most-detailed-map-of-the-fly-brain-yet"
access: "Open; neuPrint query interface"
status: "Released"
release_year: 2020
featured: true
blurb: "A densely reconstructed half of the Drosophila central brain, imaged by FIB-SEM at isotropic resolution and the dataset on which most fly circuit analysis before FlyWire was built."
source: "Scheffer et al. (2020), eLife 10.7554/eLife.57443; neuPrint."
---

The hemibrain covers roughly half the central brain of an adult female fly at 8 nm
isotropic resolution — the highest-quality large fly volume, because FIB-SEM mills rather than
sections and so avoids the alignment problems of serial sectioning. It contains about 25,000
neurons and 20 million synapses, and the neuPrint interface made connectivity queryable without
downloading anything.

**What it is good for.** Learning to query a connectome. neuPrint's Cypher interface is the
gentlest on-ramp to thinking of neurons as a graph, and the circuits it resolved — mushroom body
learning, central complex navigation, circadian — are the worked examples the field teaches from.

**What it does not support.** Whole-brain claims: the optic lobes and much of the periphery are
absent, so any neuron whose arbor leaves the volume is truncated. Comparisons with FlyWire need
care, since the two use different synapse-detection pipelines and different criteria for what
counts as a connection.
