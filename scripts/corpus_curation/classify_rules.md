# Corpus classification — taxonomy and rules

Assign ONE primary `classification` (plus `subclassification` where the taxonomy has one)
to each paper in a nanoscale/EM connectomics corpus, from title + venue + abstract.

The primary label drives colour, cell membership and top-k selection, so it must answer
**"what kind of contribution is this paper?"** — not "what words appear in it". A keyword
classifier put White 1986 in `other`, FAFB in `imaging`, Hemibrain in `pipeline`, and a
Nature retina-connectomics paper in `training-outreach`. Those are the errors to fix.

## Decision order — apply the FIRST that fits

1. **`dataset`** — the paper RELEASES a reconstruction, connectome, atlas or benchmark
   corpus as its contribution. Hemibrain, FAFB, MICrONS, H01, FlyWire, CEM500K, the
   *C. elegans* connectomes. If a paper both releases a volume and analyses it, it is
   still `dataset`. Papers that merely USE a released dataset are not.
2. **`pipeline`** — a method, algorithm, tool, or infrastructure for producing or handling
   reconstructions. `subclassification`: acquisition · preparation · alignment ·
   segmentation · proofreading · infrastructure · graph-analysis.
   Includes borrowed methods the field depends on (U-Net, ResNet, Fiji, ilastik, SIFT).
3. **`imaging`** — the contribution is the imaging MODALITY or its development.
   `subclassification`: SBEM · FIB-SEM · ssTEM · ATUM · multibeam · X-ray · expansion ·
   cryo · EM (unspecified) · unspecified. A paper that develops a microscope or a staining
   protocol is `imaging`; one that develops software for the resulting data is `pipeline`.
4. **`circuit-structure`** — MEASURES OR MAPS connectivity among identified neurons, at any
   scale or modality. White 1986, "Highly Nonrandom Features of Synaptic Connectivity",
   "Functional specificity of local synaptic connections", retinal IPL circuitry papers,
   comparative connectome analyses. This is the corpus's core subject matter.
5. **`cell-types`** — the contribution is a taxonomy, census, or parts list of neurons.
   Not: a paper that merely studies one identified cell type.
6. **`neuroanatomy`** — morphology or ultrastructure WITHOUT a connectivity claim: spine
   counts, dendritic morphometry, synapse size/density, cytoarchitecture.
7. **`behaviour`** — links circuits to behaviour: motor control, navigation, courtship,
   feeding, learning and memory, decision-making.
8. **`physiology`** — synaptic/cellular physiology, coding and response properties without
   a connectivity map: receptive fields, release probability, plasticity mechanisms.
9. **`neuroai`** — connectome-constrained models, spiking/recurrent network models,
   neuromorphic engineering, simulation of neural systems.
10. **`mri`** — macro-scale human/animal connectomics: fMRI, diffusion MRI, tractography,
    EEG/MEG. (In scope, deliberately a minority of the corpus.)
11. **`health`** — disease/clinical work WITH a genuine connectivity or circuit-mapping
    element. Disease biology without one was already removed and should not appear.
12. **`training-outreach`** — education, curricula, public engagement, citizen science,
    gamified annotation (EyeWire AS A PLATFORM). **NOT** papers containing the phrase
    "training data" — that is the single most common error in the previous pass.
13. **`synthesis`** — review, perspective, opinion, primer, historical retrospective.
    `subclassification`: `field` (about connectomics as a field) · `domain` (a neuroscience
    review that cites connectomics in passing). Only if the paper's contribution is the
    synthesis itself; a research paper with a discussion section is not `synthesis`.
14. **`other`** — genuinely none of the above. Use sparingly and prefer a real category;
    `other` previously held the corpus's single most-cited paper.

`connectomics` is deliberately NOT a category: it is the corpus, not a bin within it.

## Also assign
- `secondary_classifications`: up to 2 other categories that genuinely apply (a
  connectome-constrained RNN is primary `neuroai`, secondary `pipeline/graph-analysis`).
- `organism`: any of fly · elegans · mouse · rat · zebrafish · human · macaque · other ·
  none. Multiple allowed.

## Output
Write ONLY a JSON file to the path given:
  {"<doi>": {"classification": "...", "subclassification": "..." or null,
             "secondary_classifications": [...], "organism": [...]}, ...}
Every DOI in your batch must appear exactly once. Do not modify any other file.
