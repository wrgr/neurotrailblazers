---
title: "MouseConnects (HI-MC) — mouse hippocampus"
short_name: "MouseConnects"
species: "Mouse"
region: "Hippocampal formation"
volume: "10 mm³ target"
size: "Projection only: ~10 PB (Harvard) to ~25 PB (Google); NIH says it \"may exceed tens of petabytes\""
resolution: "Synaptic (nanoscale EM)"
modality: "Multibeam SEM of semithin sections with ion-beam milling"
access: "In progress; not yet released"
status: "In progress (NIH award 2023–2028)"
release_year: 2023
featured: true
spotlight: true
blurb: "The NIH BRAIN CONNECTS effort to reconstruct 10 mm³ of mouse hippocampal formation, about ten times the volume of H01 or MICrONS."
source: "NIH RePORTER, award UM1NS132250, abstract: \"This work will image 10 cubic millimeters, itself an unprecedentedly large dataset that may exceed tens of petabytes. Yet the mouse brain is 50 times larger.\" Harvard Gazette, 26 September 2023: a \"10 cubic-millimeter region in the mouse hippocampal formation\", \"two 91-beam scanning electron microscopes, one at Harvard and one at Princeton\", and \"about 10,000 terabytes of data\". Google Research blog, 26 September 2023: \"10–15 cubic mm of the mouse brain\" and \"about 25,000 terabytes, or 25 petabytes\". The ten-times comparison is our arithmetic against MICrONS (about 0.9 mm³ in vivo) and H01 (about 1 mm³)."
---

MouseConnects, run by the Center for High-throughput Integrative Mouse Connectomics
(HI-MC), is a BRAIN CONNECTS project targeting 10 mm³ of mouse hippocampal formation at
synaptic resolution. That is roughly ten times the volume of H01 or MICrONS. The data size
is a projection, and the sources differ: Harvard's announcement said about 10,000 terabytes,
Google's said about 25 petabytes, and the NIH abstract says only that the dataset "may
exceed tens of petabytes". Google's post also gives the volume as 10–15 mm³.

**Why it matters to a learner now, before any data exists.** Everything on this site about
infrastructure, throughput and error budgets is scoped by projects of this size. Unit 04
spends its time on storage, alignment and versioning because a volume like this cannot be
handled any other way.

**What it does not yet support.** Anything empirical. No data is released. The numbers above
are targets and estimates, not measurements. Treat this entry as a statement of intent. The
[MouseConnects page]({{ '/datasets/mouseconnects/' | relative_url }}) has the imaging method,
the collaborators and the funding status, and the
[workflow tour]({{ '/datasets/workflow/' | relative_url }}) walks the pipeline step by step.
