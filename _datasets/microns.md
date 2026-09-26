---
title: "MICrONS — mouse visual cortex"
short_name: "MICrONS"
species: "Mouse"
region: "Visual cortex (VISp, VISrl, VISal, VISlm)"
volume: "~1.3 × 0.87 × 0.82 mm (in vivo dimensions)"
cells: "More than 200,000 in EM; ~75,000 neurons calcium-imaged"
synapses: "524 million (automatically detected)"
size: "~2 PB raw imagery"
resolution: "~4 nm in-plane, 40 nm sections"
modality: "Serial-section TEM co-registered with two-photon calcium imaging"
portal: "https://www.microns-explorer.org/"
paper_doi: "10.1038/s41586-025-08790-w"
paper_url: "https://www.nature.com/articles/s41586-025-08790-w"
press_url: "https://www.princeton.edu/news/2025/04/09/first-time-scientists-map-half-billion-connections-allow-mice-see"
access: "Open; CAVEclient, static CSV exports without an account, and BossDB. CC BY 4.0 (microns-explorer.org terms)"
status: "Released"
release_year: 2025
featured: true
blurb: "A cubic millimeter of mouse visual cortex where the same neurons were both recorded in a living animal and reconstructed in EM. It lets you ask, at cubic-millimeter scale, what a measured cell is wired to."
source: "MICrONS Consortium (2025), Nature (volume, cell and neuron counts, 524 million synapses and ~2 PB raw data, from the abstract and Results); microns-explorer.org (terms). The public data went out in stages from 2021; 2025 is the flagship paper."
---

MICrONS is the dataset behind almost every structure-and-function question on this site.
An awake mouse viewed natural and synthetic stimuli while calcium imaging recorded around
75,000 neurons across four visual areas. The same tissue was then cut into about 28,000
sections, imaged by EM and reconstructed, yielding more than 200,000 cells and 524 million
automatically detected synapses. Co-registration links a subset of the functionally imaged
neurons to their EM reconstructions.

**What it is good for.** Any question of the form "does the wiring predict the response?", and
learning proofreading against a segmentation that is good but not finished. The CAVE
infrastructure behind it is also the practical introduction to versioned connectomics data:
every query you run must pin a materialization version or it is not reproducible. The site's
[MICrONS real-data lab]({{ '/notebooks/microns-lab/' | relative_url }}) is a worked,
version-pinned example that needs no account.

**What it does not support.** Treating the functional and anatomical populations as the same
set. Only a subset of imaged neurons is matched to EM, and the paper cautions that calcium
signals degrade with depth below the pia, so tuning differences across layers can be optical
rather than biological. Synapse counts from the automated pipeline carry both false positives
and misses. The published analyses account for this, and yours must too.
