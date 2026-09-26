---
layout: page
title: "Artifact Taxonomy"
permalink: /content-library/imaging/artifact-taxonomy/
image: /assets/images/content-library/imaging/artifact-taxonomy.svg
image_alt: "Stylized vector art: a raster imaging field crossed by artifact marks."
description: "A catalog of EM imaging artifacts in connectomics: causes, visual signatures, downstream cost to segmentation and proofreading, and mitigation."
topics:
  - artifacts
  - image-quality
  - segmentation-impact
  - quality-control
primary_units:
  - "03"
  - "05"
difficulty: "Intermediate"
tags:
  - imaging:artifact-identification
  - imaging:electron-microscopy
  - imaging:quality-control
  - proofreading:segmentation-impact
  - methodology:artifact-mitigation
micro_lesson_id: ml-img-artifacts
combines_with:
  - em-principles
  - acquisition-qa
  - tissue-preparation
content_type: core
---

{% include callouts/em-imaging-visual-note.html %}

## Overview

Every EM dataset contains artifacts. The useful questions are which ones are present, how severe they are, and what they cost downstream. Annotators and analysts who know the artifact classes avoid over-interpreting corrupted regions, know when to flag data for re-acquisition and when to work around it, and can trace an apparent segmentation error back to its imaging cause.

This document catalogs the major artifact classes encountered in connectomics EM, organized by their origin in the acquisition pipeline.

---

## Tissue preparation artifacts

### Fixation artifacts

**Cause:** Chemical fixation (typically aldehyde-based: glutaraldehyde + paraformaldehyde) stabilizes ultrastructure by crosslinking proteins. However, fixation is never instantaneous — there is always some delay between tissue death and complete fixation, during which degradation can occur.

**Visual signatures:**
- **Swollen or distorted mitochondria**: Cristae disrupted, matrix pale. Indicates poor fixation or post-mortem delay. This is one of the earliest and most sensitive indicators of fixation quality.
- **Extracted cytoplasm**: Pale, washed-out cytoplasm where soluble proteins were lost. Processes appear "empty" compared to well-fixed tissue.
- **Membrane disruption**: Incomplete or discontinuous membrane profiles. Severe cases show membrane blebbing or fragmentation.
- **Extracellular space expansion**: In chemically fixed neuropil, extracellular space is small. Korogod et al. (2015) measured 2.47% of volume after aldehyde perfusion against 15.4% after cryo fixation in adult mouse neocortex; in vivo estimates for adult rat neocortex, as cited there, are 18–22%. Large gaps between processes in chemically fixed tissue therefore suggest osmotic imbalance during fixation.

**Downstream impact:** Poor fixation degrades membrane contrast globally, increasing both merge and split error rates. Mitochondrial distortion can confuse organelle-based compartment identification.

**Mitigation:** Transcardial perfusion with buffered fixative provides the most uniform fixation for mammalian brain. Immersion fixation of resected tissue (as in human surgical samples like H01) is less uniform in general — check for a quality gradient from surface to interior.

**Reference:** For the H01 dataset specifically, see Shapson-Coe et al. (2024), which reports that rapid immersion fixation of the surgical sample gave quality comparable to perfused rodent tissue.

### Staining artifacts

**Cause:** Heavy-metal staining must penetrate uniformly through the tissue block (for volume EM) or individual sections (for ssTEM). Incomplete penetration, precipitation, or differential binding can create contrast inhomogeneities.

**Visual signatures:**
- **Staining gradients**: Contrast decreases from the block surface inward, because standard osmium protocols do not penetrate millimeter-scale blocks evenly (the problem Hua et al. 2015 set out to solve). Membranes become progressively harder to see toward the center.
- **Precipitate deposits**: Dark, irregularly shaped deposits that are not biological structures. Uranyl acetate and lead citrate are both prone to precipitation if pH or concentration is incorrect.
- **Differential staining**: Some structures over-stained relative to others. For example, excessive uranyl acetate can make chromatin so dark that it obscures nuclear detail.

**Downstream impact:** Staining gradients are hard to catch because they create spatially varying segmentation quality. Models trained on well-stained regions perform poorly on under-stained ones, and the transition is gradual, so global QA metrics may miss it.

**Mitigation:** Hua et al. (2015) modified the rOTO (reduced osmium-thiocarbohydrazide-osmium) protocol specifically to remove staining gradients in blocks about 1 mm across. Pilot imaging of test blocks before committing to full acquisition is essential.

### Embedding and infiltration artifacts

**Cause:** After staining, tissue is dehydrated and infiltrated with resin (typically Epon or Durcupan). Incomplete infiltration creates voids; differential shrinkage distorts geometry.

**Visual signatures:**
- **Resin voids**: Light areas with no biological structure, often with sharp edges. Distinct from extracellular space (which has biological boundaries).
- **Shrinkage**: Tissue contracts during processing, by an amount that depends on the protocol and is worth measuring rather than assuming. Published corrections are around 15–16% per axis (see [Tissue preparation]({{ '/content-library/imaging/tissue-preparation/' | relative_url }})), but treat any single number as protocol-specific. Anisotropic shrinkage distorts cell shapes and distances. Neuropil appears denser than in vivo.
- **Chattering during sectioning**: If resin is too hard or soft, the diamond knife vibrates, creating periodic thickness variations visible as alternating light/dark bands.

---

## Sectioning artifacts

### Knife marks and chatter

**Cause:** Diamond knife vibration during ultrathin sectioning creates periodic thickness variations (chatter) or score marks (knife lines) across the section face.

**Visual signatures:**
- **Chatter**: Alternating bright/dark bands perpendicular to the cutting direction, at a regular spacing, superimposed on biological detail.
- **Knife lines**: Thin streaks parallel to the cutting direction. Usually less disruptive than chatter unless severe.

**Downstream impact:** Chatter creates false boundaries that segmentation algorithms may interpret as membranes, generating split errors. The periodic pattern can also create coherent artifacts across multiple sections, making them harder to distinguish from real structures.

**Mitigation:** Optimize cutting speed, knife angle, and block trimming geometry. Replace diamond knife when signs of wear appear. For SBEM, chatter is a persistent challenge because the knife operates inside the vacuum chamber.

### Section compression

**Cause:** The diamond knife compresses the section in the cutting direction. The magnitude varies with knife angle, cutting speed and block face, so calibrate it against a known geometry rather than applying a published figure. This creates anisotropic distortion — features are shortened along the cutting axis.

**Visual signatures:** Circular profiles appear elliptical. Grid-like patterns (if present) show directional distortion. The compression axis is consistent within a section but may vary between sections.

**Downstream impact:** Compression distorts morphological measurements (soma size, spine dimensions) and complicates registration between sections. If uncorrected, 3D reconstructions show systematic stretching artifacts.

**Mitigation:** Computational correction during section registration. Estimating compression ratio from circular structures (blood vessels, myelinated axons in cross-section) and applying inverse transform.

### Folds, tears, and wrinkles

**Cause:** Ultrathin sections (40-70 nm) are mechanically fragile. Handling during collection on grids or tapes can introduce folds (section doubled over), tears (section ripped), or wrinkles (local buckling).

**Visual signatures:**
- **Folds**: Region where two layers of section overlap, appearing as a dark band with doubled features. Borders are sharp, linear.
- **Tears**: Missing region with sharp edges, usually irregular. No data available within the tear.
- **Wrinkles**: Gentle undulations causing out-of-focus regions. Features appear blurred or show focus gradient.

**Downstream impact:** Folds create false double-membrane appearances that can be mistaken for cell boundaries. Tears create complete data gaps — any neurite crossing a tear is lost at that z-level, causing splits. Wrinkles degrade resolution locally.

**Severity hierarchy:** Tears > folds > wrinkles in terms of downstream damage. Tears are non-recoverable; folds can sometimes be computationally flattened; wrinkles rarely cause segmentation errors.

### Missing sections

**Cause:** Section lost during collection, or section too damaged to image. Creates a gap in the z-stack.

**Visual signatures:** Jump in z — structures appear to teleport between adjacent surviving sections. Registration metrics show anomalous displacement.

**Downstream impact:** Missing sections are a major cause of split errors in neurite tracing. A thin axon (~100 nm across) running roughly parallel to the section plane appears in only 3-4 consecutive 30 nm sections. Losing one removes a quarter to a third of the local z-evidence, which can be enough to lose the axon entirely.

**Mitigation:** Automated collection (ATUM tape, GridTape) cuts handling losses compared with picking sections up by hand, and because collected sections survive imaging, a section that was badly *imaged* can be imaged again. A section lost during cutting or collection is gone. H01 lost no more than the equivalent of three 30 nm sections during one knife change (Shapson-Coe et al. 2021 preprint). Track your own rate against the gates in [Unit 03]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}) §3 rather than assuming a published figure applies. SBEM and FIB-SEM avoid collection losses because nothing is collected, though a failed cut still leaves a gap. Computational approaches: interpolation of the missing section, or explicit "uncertain gap" annotation.

---

## Imaging artifacts

### Charging

**Cause:** Electron beam deposits charge in non-conductive regions of the specimen. If charge cannot dissipate fast enough (through conductive coating or staining), the accumulated charge deflects the beam, distorting the image.

**Visual signatures:**
- **Bright streaks or halos**: Charge buildup creates abnormal brightness patterns, often at edges of structures or near poorly stained regions.
- **Image drift/distortion**: Accumulated charge creates local electric fields that deflect the beam, causing spatial distortion.
- **Contrast inversion**: In severe cases, charged regions can appear with inverted contrast.

**Downstream impact:** Charging creates false contrast patterns that segmentation models may interpret as biological boundaries. Spatial distortion degrades registration accuracy.

**Mitigation:** Adequate heavy-metal staining provides conductivity. Conductive coating (carbon, gold-palladium) of block face or section surface. Reducing beam current or dwell time (at cost of SNR). Variable-pressure SEM modes help but reduce resolution.

### Beam damage

**Cause:** Cumulative electron dose degrades the specimen. Organic material is sensitive to dose, and the tolerable dose depends on the resin, the stain, the accelerating voltage and what detail you need to keep; measure it on test blocks rather than borrowing a threshold from cryo-EM, where the specimen is unstained and the target is atomic detail.

**Visual signatures:**
- **Mass loss**: Specimen appears to thin or develop holes with prolonged exposure.
- **Bubbling**: Volatile decomposition products create bubbles within the resin.
- **Contrast loss**: Staining patterns fade with repeated imaging.

**Downstream impact:** In block-face imaging (SBEM, FIB-SEM), the beam deposits energy below the imaged surface, to a depth that grows with accelerating voltage. The material that the next cut or mill will expose has already been dosed, which can degrade its image and make thin cuts less reliable.

**Mitigation:** Optimize dose: use the minimum beam current and dwell time that produce adequate SNR. Single-pass imaging (no repeat imaging of the same area). For SBEM/FIB-SEM, accelerating voltage affects the depth of beam penetration and thus pre-damage.

### Drift and jitter

**Cause:** Mechanical or thermal instabilities in the microscope stage cause the specimen to move during imaging. Fast drift = jitter (within a single tile), slow drift = systematic displacement between tiles.

**Visual signatures:**
- **Jitter**: Horizontal or vertical line-by-line offsets within a single image, giving a "sheared" appearance.
- **Drift**: Systematic offset between adjacent tiles in a mosaic, or between consecutive sections. Visible as seams in stitched images.

**Downstream impact:** Jitter degrades local resolution. Drift creates tile-boundary artifacts that segmentation may misinterpret, and complicates inter-section registration.

---

## Computational/alignment artifacts

### Stitching seams

**Cause:** Large areas are imaged as tile mosaics and computationally stitched. Imperfect tile registration creates visible seams — brightness discontinuities, small spatial offsets, or duplicated/missing strips at tile boundaries.

**Visual signatures:** Linear brightness changes or offset patterns at regular intervals matching the tile grid.

**Downstream impact:** Seams create false boundaries. Segmentation algorithms may split neurites at seam locations. Even after intensity normalization, subtle spatial offsets can persist.

### Section-to-section misalignment

**Cause:** Even with automated registration, residual misalignment between consecutive sections (1-10 nm) can accumulate over many sections.

**Visual signatures:** Structures appear to oscillate or drift when scrolling through z. Fine processes may appear to jump discontinuously.

**Downstream impact:** Misalignment creates false branch points and false terminations. For the thinnest processes (a few tens of nanometers across), a misalignment of a few pixels (4-8 nm each) can move the process off its own footprint in the next section, causing a split.

---

## Artifact severity classification for proofreading triage

| Severity | Examples | Action |
|----------|----------|--------|
| **Critical** (blocks reconstruction) | Missing sections, large tears, severe misalignment | Flag for re-acquisition or exclude region |
| **Major** (increases error rate significantly) | Staining gradients, charging, persistent chatter | Run pilot segmentation; quantify error rate penalty; consider targeted re-imaging |
| **Minor** (manageable in proofreading) | Occasional knife lines, mild compression, small wrinkles | Proceed with awareness; include in proofreading QA checks |
| **Cosmetic** (no downstream impact) | Slight focus variation, minor brightness non-uniformity | No action needed |

---

## Worked example: diagnosing a region with elevated split errors

**Scenario (invented for teaching):** A proofreader notices that a specific 20×20×20 μm subvolume has 3× the normal split error rate. The segmentation model is the same one used across the entire volume.

**Diagnostic steps:**

1. **Inspect raw images in the subvolume.** Look for: contrast changes, staining differences, artifacts.
2. **Finding:** The subvolume lies deep in the tissue block, far from every face. Membrane contrast is visibly reduced compared with regions near the surface: a staining gradient from incomplete osmium penetration.
3. **Verify:** Plot mean membrane contrast (e.g., using membrane probability maps from the segmentation model) as a function of distance from the nearest block face. Confirm the gradient.
4. **Root cause:** Under-stained membranes → lower model confidence at membrane predictions → more split errors where model fails to detect thin, low-contrast membranes.
5. **Decision:** (a) Flag region as reduced-quality in metadata. (b) Consider re-running segmentation with lower boundary threshold (accepting more merge errors in exchange for fewer splits). (c) Allocate extra proofreading time to this region. (d) Report to the acquisition team for future protocol adjustment.

---

## References

- Briggman KL, Bock DD (2012) "Volume electron microscopy for neuronal circuit reconstruction." *Current Opinion in Neurobiology* 22(1):154-161.
- Denk W, Horstmann H (2004) "Serial block-face scanning electron microscopy to reconstruct three-dimensional tissue nanostructure." *PLoS Biology* 2(11):e329.
- Hayworth KJ et al. (2015) "Ultrastructurally smooth thick partitioning and volume stitching for large-scale connectomics." *Nature Methods* 12:319-322.
- Hua Y, Laserstein P, Helmstaedter M (2015) "Large-volume en-bloc staining for electron microscopy-based connectomics." *Nature Communications* 6:7923.
- Kasthuri N et al. (2015) "Saturated reconstruction of a volume of neocortex." *Cell* 162(3):648-661.
- Korogod N, Petersen CCH, Knott GW (2015) "Ultrastructural analysis of adult mouse neocortex comparing aldehyde perfusion with cryo fixation." *eLife* 4:e05793.
- Shapson-Coe A et al. (2021) "A connectomic study of a petascale fragment of human cerebral cortex." *bioRxiv* 2021.05.29.446289.
- Shapson-Coe A et al. (2024) "A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution." *Science* 384(6696):eadk4858.
- Xu CS et al. (2017) "Enhanced FIB-SEM systems for large-volume 3D imaging." *eLife* 6:e25916.
