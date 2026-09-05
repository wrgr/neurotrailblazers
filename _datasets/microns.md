---
title: "MICrONS — mouse visual cortex"
short_name: "MICrONS"
species: "Mouse"
region: "Visual cortex (VISp, VISrl, VISal, VISlm)"
volume: "1.4 × 0.87 × 0.84 mm"
cells: "~200,000 anatomical; ~75,000 functionally imaged"
synapses: "523 million"
size: "1.6 PB"
resolution: "4 nm in-plane, 40 nm sections"
modality: "Serial-section EM co-registered with two-photon calcium imaging"
portal: "https://www.microns-explorer.org/"
paper_doi: "10.1038/s41586-025-08790-w"
paper_url: "https://www.nature.com/articles/s41586-025-08790-w"
press_url: "https://www.princeton.edu/news/2025/04/09/first-time-scientists-map-half-billion-connections-allow-mice-see"
access: "Open; CAVEclient for programmatic access"
status: "Released"
release_year: 2025
featured: true
blurb: "A cubic millimetre of mouse visual cortex where the same neurons were both recorded in a living animal and reconstructed in EM. It is the only large volume that lets you ask what a measured cell is wired to."
source: "MICrONS Consortium (2025), Nature 10.1038/s41586-025-08790-w; microns-explorer.org."
---

MICrONS is the dataset behind almost every structure-and-function question on this site.
An awake mouse viewed natural and synthetic stimuli while calcium imaging recorded around 75,000
neurons; the same tissue was then imaged by EM and reconstructed, yielding roughly 200,000 cells
and 523 million synapses. Co-registration links a subset of the functional cells to their
anatomical reconstructions.

**What it is good for.** Any question of the form "does the wiring predict the response?" — and
for learning proofreading against a segmentation that is good but demonstrably not finished.
The CAVE infrastructure behind it is also the practical introduction to versioned connectomics
data: every query you run must pin a materialization version or it is not reproducible.

**What it does not support.** Treating the functional and anatomical populations as the same set.
Co-registration succeeds for a fraction of cells, and that fraction is not random — it is biased
toward cells near the imaged surface. Synapse counts from the automated pipeline carry both false
positives and misses; the published analyses correct for this and yours must too.
