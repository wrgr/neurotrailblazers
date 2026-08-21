---
layout: page
title: "Acquisition QA"
permalink: /content-library/imaging/acquisition-qa/
description: "Quality assurance gates for connectomics EM acquisition — per-tile monitoring, pilot reconstructions, metadata requirements, and go/no-go criteria."
topics:
  - quality-assurance
  - acquisition
  - pilot-testing
  - metadata
primary_units:
  - "03"
difficulty: "Intermediate"
tags:
  - imaging:acquisition-qa
  - imaging:electron-microscopy
  - imaging:quality-control
  - infrastructure:metadata
  - methodology:reproducibility
micro_lesson_id: ml-img-acquisition-qa
reference_images:
  - src: /assets/images/content-library/imaging/acquisition-qa/qa-checklist-visual.png
    alt: "Visual QA checklist for EM acquisition with pass/fail examples"
    caption: "Per-tile QA checklist: focus quality, brightness uniformity, stitching alignment, and artifact coverage. Red borders = fail criteria."
  - src: /assets/images/content-library/imaging/acquisition-qa/pilot-recon-validation.png
    alt: "Small pilot reconstruction used to validate acquisition parameters before full-scale imaging"
    caption: "Pilot reconstruction from 100 sections validates that segmentation quality meets threshold before committing to full acquisition."
  - src: /assets/images/content-library/imaging/acquisition-qa/go-nogo-decision-matrix.png
    alt: "Go/no-go decision matrix for acquisition quality gates"
    caption: "Decision matrix: pass/fail criteria for each QA gate with escalation paths for borderline cases."
combines_with:
  - artifact-taxonomy
  - em-principles
  - reconstruction-pipeline
content_type: core
---

## Overview

Acquisition QA is the practice of catching problems *before* they propagate into months of wasted reconstruction and proofreading effort. The core principle: imaging artifacts that degrade segmentation quality are far cheaper to detect and mitigate at acquisition time than to correct downstream. A dataset acquired without QA gates may look acceptable in raw images but harbor subtle contrast gradients, alignment drift, or staining inconsistencies that create thousands of unnecessary segmentation errors.

---

## Instructor script: the QA mindset

### The cost asymmetry

The argument for acquisition QA is not that defects are catastrophic. It is that
the cost of a defect scales with how late you find it, and the escalation is
steep enough that cheap checks pay for themselves many times over.

Take a staining gradient that reduces membrane contrast by 20% in one corner of
a 1 mm³ volume — the threshold at which Unit 03 §3 stops acquisition:

| Caught at | What it costs to deal with | Why the cost jumps |
|---|---|---|
| **Acquisition** | Hours of pilot imaging; re-stain the block or adjust parameters for that region | Nothing downstream has been built yet |
| **Segmentation** | Weeks to months of compute already spent, and spent again if you re-run | The defect raises the split rate locally, and you only see it once the full segmentation exists |
| **Proofreading** | Human hours, concentrated in the affected region | Proofreading is the most expensive input in the pipeline and the hardest to add capacity to |
| **Analysis** | Potentially the result itself | An uncaught gradient is a *spatial bias*: neurons in the under-stained region appear to have fewer connections, because more of their synapses were missed |

The last row is the one that matters. The first three cost money and time; the
fourth costs correctness, and it does so in a way that looks like a finding.

**Do the arithmetic for your own project.** The numbers differ by an order of
magnitude between labs, so a figure quoted from someone else's project is not
worth much — but the *shape* is robust, and you can establish it yourself
before committing:

1. Time a proofreader on a neuron in a clean region and one in a degraded region
   of your pilot volume. The ratio is the multiplier you actually face.
2. Multiply by the number of neurons your analysis needs and by your real hourly
   cost.
3. Compare against the cost of the acquisition-time fix, which is usually
   measured in days of one person's time.

If step 3 is smaller than step 2 — and it nearly always is by a wide margin —
the QA gate pays for itself, and you now have a number you can defend to whoever
controls the budget rather than a slogan.

### QA is not optional

In early connectomics projects (pre-2015), QA was often informal — experienced microscopists would inspect images visually and make qualitative judgments. This worked for small datasets but does not scale. Modern connectomics datasets generate terabytes to petabytes of data over months of continuous imaging. Quantitative, automated QA metrics are essential.

---

## Per-tile quality metrics

### Intensity statistics

For every tile (single acquired image), compute:

- **Mean intensity**: Should be stable across tiles within a section and across sections over time. Gradual drift indicates charging, staining changes, or detector degradation.
- **Standard deviation**: Proxy for contrast. Low standard deviation in a tile that should contain neuropil suggests contrast loss.
- **Min/max intensity**: Saturation (max=255 in 8-bit) indicates detector overflow; floor values (min=0) may indicate dead pixels or extreme charging.

**Implementation:** Log these per tile in a database. Plot as time series and spatial heatmaps. Set alert thresholds (e.g., mean deviating >2σ from running average).

### Signal-to-noise ratio (SNR)

Define SNR as the ratio of contrast between membrane and lumen to the noise floor. Methods:

1. **Membrane detection confidence**: Run a lightweight membrane detector (even a simple edge filter) on each tile. The average confidence score is a proxy for staining quality.
2. **Power spectral density**: Well-stained neuropil has characteristic spatial frequency content (peak at membrane spacing ~200-500 nm). Loss of this peak indicates contrast degradation.

### Focus quality

For SEM-based methods, focus is set per imaging session. Focus drift between tile acquisitions can blur images:

- **Sharpness metric**: Variance of the Laplacian (or similar edge-detection operator). Low values indicate out-of-focus images.
- **Automated refocusing triggers**: If sharpness drops below threshold, pause imaging and refocus.

### Tile-to-tile consistency

Adjacent tiles should have similar intensity distributions (they image neighboring tissue regions). Discrepancies indicate:

- **Stitching errors**: Tiles misregistered during mosaic assembly.
- **Illumination non-uniformity**: Beam profile not flat across field of view.
- **Stage positioning errors**: Tiles don't overlap correctly.

---

## Section-to-section monitoring

### Alignment residuals

After section registration, compute residual displacement at control points:

- **Median residual**: Should be <1 pixel. Large residuals indicate section distortion, missing sections, or registration failure.
- **Spatial pattern of residuals**: Uniform residuals suggest global shift (acceptable after correction). Spatially heterogeneous residuals suggest local distortion (warping, compression).

### Missing-section detection

Automated detection of missing or severely damaged sections:

1. **Cross-correlation between consecutive sections**: Normal sections have high correlation (>0.7 for neuropil). A sudden correlation drop flags a missing or damaged section.
2. **Object continuity checks**: Count the number of segment IDs that appear in section N but not N+1 (and vice versa). Spikes indicate discontinuity.

### Intensity drift

Plot mean section intensity over the entire z-stack:

- **Gradual drift**: May indicate detector aging, filament degradation, or slow charging buildup. Can often be corrected computationally (histogram normalization).
- **Step changes**: Indicate instrument events (filament replacement, vacuum change, knife replacement). Document in acquisition log.

---

## Pilot reconstructions

### The principle

Before committing to full-volume imaging and reconstruction (which may take months and cost hundreds of thousands of dollars), run a small pilot reconstruction to verify that the preparation and imaging quality supports adequate segmentation.

### Pilot protocol

1. **Acquire a small subvolume**: 20-50 μm on a side, from a representative region. This takes hours to days, not months.
2. **Run automated segmentation**: Use the same model/parameters planned for the full volume.
3. **Manual evaluation**: An expert annotator reviews 50-100 neurites in the pilot reconstruction, checking for:
   - Merge error rate (# merges per 100 μm of traced neurite)
   - Split error rate (# splits per 100 μm)
   - Membrane detection quality (are membranes consistently visible?)
   - Synapse detection quality (are active zones and PSDs detectable?)
4. **Quantitative metrics**: Compute VI and ERL against the manually corrected pilot as ground truth.
5. **Go/no-go decision**: If metrics fall below project thresholds, investigate root cause (staining? imaging? model?) before proceeding.

### What pilot reconstructions catch

Real examples from connectomics projects:

- **Insufficient osmium penetration**: Pilot showed membrane contrast fading >100 μm from block surface. Action: switched to rOTO protocol before full acquisition.
- **Excessive charging in SBEM**: Pilot showed split error rate 5× normal in a region near a large blood vessel. Action: adjusted beam parameters and applied additional conductive coating.
- **Z-alignment drift**: Pilot showed accumulating misalignment over 200 sections due to stage thermal drift. Action: added periodic fiducial reimaging for alignment correction.

---

## Metadata requirements

### Why metadata matters

Metadata is the provenance chain that makes your acquisition reproducible and your errors diagnosable. Without metadata, a contrast artifact is just a mystery; with metadata, you can trace it to a specific instrument setting, timestamp, or protocol deviation.

### Required metadata per section/block-face

| Field | Example | Purpose |
|-------|---------|---------|
| Timestamp | 2025-03-15T14:23:07Z | Correlate with instrument events |
| Accelerating voltage | 2.0 kV | Affects penetration depth, contrast |
| Beam current | 1.6 nA | Affects dose, SNR, charging |
| Dwell time | 1.0 μs/pixel | Affects SNR vs throughput |
| Pixel size (XY) | 8.0 nm × 8.0 nm | Spatial calibration |
| Section thickness (Z) | 30 nm | Z calibration |
| Detector type/gain | BSE, gain=12 | Signal chain |
| Vacuum level | 5.2e-3 Pa | Affects charging, beam stability |
| Working distance | 5.0 mm | Affects resolution, depth of field |
| Focus score | 0.87 | Automated quality metric |
| Operator notes | "Knife replaced at section 4521" | Event log |

### Required metadata per tile

| Field | Example | Purpose |
|-------|---------|---------|
| Tile position (X, Y) | (3, 7) in mosaic | Spatial localization |
| Stage coordinates | (12045.3, -8921.1) μm | Absolute positioning |
| Mean intensity | 127.4 | Intensity monitoring |
| Intensity std dev | 34.2 | Contrast monitoring |
| Sharpness score | 0.91 | Focus monitoring |

### Machine-readable format

Store metadata in structured formats (JSON, HDF5 attributes, database records) — not handwritten notebooks. Automated QA pipelines must be able to query metadata programmatically.

---

## QA dashboard design

A production connectomics acquisition should have a live dashboard showing:

1. **Acquisition progress**: Section count, estimated completion date, volume coverage
2. **Intensity trends**: Mean, std, min, max per section over time
3. **Focus quality**: Sharpness metric per section/tile
4. **Alignment quality**: Registration residuals per section
5. **Anomaly alerts**: Flagged sections (missing, damaged, out-of-spec intensity or focus)
6. **Pilot results**: Latest segmentation quality metrics from periodic pilot reconstructions
7. **Instrument health**: Beam current, vacuum, temperature (if logged)

---

## Worked example: acquisition QA decision tree

**Situation:** During SBEM acquisition of a mouse cortex block (planned 8,000 sections), the QA dashboard shows that mean intensity has dropped 15% between sections 2,000 and 2,100.

**Decision tree:**

1. **Is the drop sudden or gradual?**
   - Sudden (1-2 sections): likely instrument event (beam instability, vacuum fluctuation). Check instrument logs.
   - Gradual (over 100 sections): likely charging buildup, staining gradient reaching surface, or detector degradation.

2. **Is contrast (standard deviation) also affected?**
   - Yes: staining or contrast issue — biological structures are less visible.
   - No: intensity shift only — may be correctable with histogram normalization.

3. **Run quick segmentation test on affected sections:**
   - If segmentation quality is maintained → proceed, apply intensity correction in post-processing.
   - If segmentation quality drops → pause acquisition, investigate root cause.

4. **If pausing:** Check knife condition (chatter?), beam alignment, charging patterns. Consider re-coating block face or adjusting beam parameters.

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "If the images look good to my eye, they're fine" | Human visual inspection misses subtle contrast gradients that affect automated segmentation | Always use quantitative metrics alongside visual inspection |
| "QA slows down acquisition" | QA prevents costly rework; the net effect is faster project completion | Compare cost of 1 day of QA vs weeks of re-proofreading |
| "One pilot reconstruction is enough" | Tissue quality can vary across the block; periodic pilot checks catch developing problems | Run mini-pilots every 500-1,000 sections |
| "Metadata is just bookkeeping" | Metadata is essential for diagnosing problems, reproducing results, and sharing data | Treat metadata as a first-class data product |

---

## References

- Briggman KL, Bock DD (2012) "Volume electron microscopy for neuronal circuit reconstruction." *Current Opinion in Neurobiology* 22(1):154-161.
- Hayworth KJ et al. (2014) "Ultrastructurally smooth thick partitioning and volume stitching for large-scale connectomics." *Nature Methods* 12:319-322.
- Hua Y, Laserstein P, Helmstaedter M (2015) "Large-volume en-bloc staining for electron microscopy-based connectomics." *Nature Communications* 6:7923.
- Scheffer LK et al. (2020) "A connectome and analysis of the adult *Drosophila* central brain." *eLife* 9:e57443.
- Zheng Z et al. (2018) "A complete electron microscopy volume of the brain of adult *Drosophila melanogaster*." *Cell* 174(3):730-743.
