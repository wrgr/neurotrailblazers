---
title: "Hemibrain — Drosophila central brain"
short_name: "Hemibrain"
species: "Drosophila melanogaster (female)"
region: "Central brain (about half)"
volume: "~250 × 250 × 250 μm sample"
cells: "~25,000 neurons"
synapses: "~20 million chemical synapses"
size: "26 teravoxels (8-bit)"
resolution: "8 nm isotropic"
modality: "FIB-SEM"
portal: "https://neuprint.janelia.org/"
paper_doi: "10.7554/eLife.57443"
paper_url: "https://elifesciences.org/articles/57443"
press_url: "https://www.janelia.org/news/unveiling-the-biggest-and-most-detailed-map-of-the-fly-brain-yet"
access: "Open; neuPrint (Google sign-in). License: treat as CC BY-NC 4.0 (noncommercial). The v1.0 data deposit is registered CC BY-NC 4.0; Janelia's project page says CC BY 4.0. Use the more restrictive terms until Janelia confirms otherwise"
status: "Released"
release_year: 2020
featured: true
blurb: "A densely reconstructed half of the Drosophila central brain, imaged by FIB-SEM at isotropic resolution. Most fly circuit analysis before FlyWire was built on it."
source: "Scheffer et al. (2020), eLife (sample size, 26 teravoxels, neuron and synapse counts, and 'over 50 person-years of proofreading effort'); neuPrint. License: janelia.org/project-team/flyem/hemibrain and DataCite 10.25378/janelia.11676099."
---

The hemibrain covers roughly half the central brain of an adult female fly at 8 nm
isotropic resolution. FIB-SEM mills the block rather than cutting sections, so it avoids the
section-alignment problems of serial-section EM. The sample was about 250 μm on a side and
was cut into 20 μm slabs so each could be milled without artifacts. The reconstruction holds
about 25,000 neurons and 20 million chemical synapses, and took over 50 person-years of
proofreading. The neuPrint interface made the connectivity queryable without downloading
anything.

**What it is good for.** Learning to query a connectome. neuPrint's Cypher interface is the
gentlest way in to thinking of neurons as a graph, and the circuits it resolved (mushroom
body learning, central complex navigation, circadian clock) are the worked examples the
field teaches from.

**What it does not support.** Whole-brain claims. The optic lobes and much of the periphery
are absent, so any neuron whose arbor leaves the volume is truncated. Comparisons with
FlyWire need care, since the two use different synapse-detection pipelines and different
criteria for what counts as a connection. Before you redistribute hemibrain data, check the
license: Treat as CC BY-NC 4.0 (noncommercial) until Janelia confirms otherwise. The v1.0 deposit is registered CC BY-NC 4.0; Janelia's project page says CC BY 4.0.
