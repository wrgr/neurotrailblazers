---
title: "FANC — female adult nerve cord"
short_name: "FANC"
species: "Drosophila melanogaster (female)"
region: "Ventral nerve cord"
cells: "14,600 neuronal cell bodies"
synapses: "~45 million"
modality: "Serial-section TEM (GridTape), automated segmentation"
portal: "https://github.com/htem/FANC_auto_recon"
paper_doi: "10.1038/s41586-024-07389-x"
paper_url: "https://www.nature.com/articles/s41586-024-07389-x"
access: "Open; CAVE with a free token (access instructions in the FANC_auto_recon repository)"
status: "Released"
release_year: 2024
blurb: "The reconstructed female fly ventral nerve cord: 14,600 cell bodies and about 45 million synapses, with leg and wing motor neurons mapped to the muscles they drive."
source: "Azevedo et al. (2024), Nature; cell-body and synapse counts are from the abstract. The underlying imagery is the Phelps, Hildebrand & Graham (2021) GridTape volume, cataloged separately."
---

FANC is the segmentation and synapse reconstruction built on the Phelps, Hildebrand &
Graham GridTape volume of the adult female *Drosophila* ventral nerve cord. Azevedo and
colleagues report roughly 45 million synapses and 14,600 neuronal cell bodies. They paired
the connectome with a motor-neuron atlas built from genetic driver lines and X-ray
holographic nanotomography, so leg and wing motor neurons are matched to the muscles they
innervate.

**What it is good for.** Circuits that end in a muscle. Most connectomes stop at the nervous
system. This one identifies the effector, which makes it the clearest dataset for asking how a
motor command is assembled.

**What it does not support.** Brain circuits. The VNC is the fly's spinal-cord analog, and
descending input from the brain enters the volume already cut off. For circuits that cross
that boundary, use BANC, which joins the two.
