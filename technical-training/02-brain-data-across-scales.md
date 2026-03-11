---
layout: page
title: "02 Brain Data Across Scales"
permalink: /technical-training/02-brain-data-across-scales/
slug: 02-brain-data-across-scales
---

## Why this unit
Technical decisions depend on scale. Data representation, compute cost, and biological interpretation all shift from macroscale to ultrastructure.

## Learning goals
- Separate modality scale from analysis scale.
- Plan scale-aware workflows and questions.

## Core technical anchors
- Registration and coordinate consistency.
- Resolution anisotropy risks.
- Volumes, meshes, skeletons, and graphs as scale-dependent representations.

## Course links
- Existing overlap: [module04]({{ '/modules/module04/' | relative_url }}), [module05]({{ '/modules/module05/' | relative_url }}), [module12]({{ '/modules/module12/' | relative_url }})
- Next unit: [03 EM Prep and Imaging]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }})

## Practical workflow
1. Define the target biological question.
2. Select modality/scale that can resolve needed features.
3. Estimate compute/storage implications.
4. Plan cross-scale linkage and provenance.

## Discussion prompts
- What is lost and gained when moving across scales?
- Which cross-scale assumptions most often fail in practice?

## Related resources
- Journal club list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})

## Quick activity
Pick a research question and propose the minimum data scale needed to answer it, including one tradeoff you accept.
