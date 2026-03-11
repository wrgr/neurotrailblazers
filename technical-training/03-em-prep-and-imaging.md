---
layout: page
title: "03 EM Prep and Imaging"
permalink: /technical-training/03-em-prep-and-imaging/
slug: 03-em-prep-and-imaging
---

## Why this unit
Acquisition quality sets the upper bound on downstream reconstruction quality.

## Learning goals
- Explain practical EM prep/imaging stages.
- Identify artifact classes that impact segmentation and proofreading.

## Core technical anchors
- Fixation/staining/sectioning/imaging chain.
- Throughput-volume-resolution tradeoffs.
- Provenance and acquisition QA.

## Course links
- Existing overlap: [module05]({{ '/modules/module05/' | relative_url }})
- Next unit: [04 Volume Reconstruction Infrastructure]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})

## Practical workflow
1. Specify target structures and required resolution.
2. Choose prep/imaging strategy compatible with that target.
3. Anticipate artifact classes and mitigation checkpoints.
4. Capture acquisition metadata for downstream reproducibility.

## Discussion prompts
- Which imaging artifact has the highest downstream cost in your workflow?
- Where should imaging QA gates be mandatory before reconstruction proceeds?

## Related resources
- Journal club list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})

## Quick activity
Identify one likely imaging artifact in a sample dataset and describe how it could affect segmentation quality.
