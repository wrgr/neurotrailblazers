---
marp: true
theme: default
paginate: true
title: "Module 04: Neuroanatomy for Connectomics"
---

# Module 04: Neuroanatomy for Connectomics
Teaching Deck

---

## Learning Objectives
- Identify major neuroanatomical compartments relevant to connectomics
- Relate anatomical context to interpretation of local EM structures
- Use region/layer context to avoid misclassification
- Communicate anatomy-based uncertainty clearly

---

## Session Outcomes
- Learners can complete the module capability target.
- Learners can produce one evidence-backed artifact.
- Learners can state one limitation or uncertainty.

---

## Agenda (60 min)
- 0-10 min: Frame and model
- 10-35 min: Guided practice
- 35-50 min: Debrief and misconception correction
- 50-60 min: Competency check + exit ticket

---

## Capability Target
Interpret a local EM region using correct anatomical context and document one confident and one uncertain structural call.

---

## Concept Focus
### 1) Cortical layers shape what you see in EM
The mammalian neocortex is organized into six layers (L1-L6), each with a characteristic cell density, cell-type composition, and neuropil texture. In EM, these layers are distinguishable by:
- **Layer 1**: Sparse cell bodies (mostly interneurons and glia), dense neuropil of apical dendritic tufts, axonal boutons, and astrocytic processes. If you see neuropil with very few soma profiles, you are likely in L1.
- **Layer 2/3**: Dense small-to-medium pyramidal neuron soma, heavily interconnected by local axon collaterals. The most densely packed neuronal layer.
- **Layer 4**: In sensory cortex, dominated by spiny stellate cells (not pyramidal) and thalamocortical axon terminals. Bouton density is high; dendritic spines are abundant.
- **Layer 5**: Large pyramidal cells (especially thick-tufted pyramidal neurons with soma up to 25 μm). If you see the largest soma profiles in the column, you are likely in L5.
- **Layer 6**: Heterogeneous; corticothalamic pyramidal cells with distinctive morphology (apical dendrites reaching only to L4, not L1). Transition to white matter below.

---

## Core Workflow
- Identify anatomical region/layer using soma density, cell-type signatures, and neuropil texture.
- Map candidate structures to known context (expected cell types, expected synapse types).
- Cross-check with neighboring slices — does the interpretation remain consistent across z?
- Annotate confidence and escalation path for ambiguous cases.

---

## 60-Minute Run-of-Show
- Review cortical layer descriptions above.
- Explore the Allen Brain Atlas online viewer and locate cortical layers in a coronal section.
- Bring one question: "How would I know which layer I'm looking at in EM?"
- **00:00-10:00 | Macro-to-micro bridge**
- Instructor shows a light microscopy image of cortex (Nissl stain showing layers) side-by-side with the same region in EM.
- Key teaching point: "The layers you learned in neuroanatomy class are the same layers you'll see in EM — but the visual cues are different. In EM, you identify layers by cell density and neuropil texture, not by staining color."
- Walk through each layer's EM signature with real images from MICrONS or H01.
- **10:00-24:00 | Guided structural identification**
- Present 4 EM patches from different layers (unlabeled). Instructor demonstrates the identification process:
- Patch A: sparse soma, dense neuropil → L1
- Patch B: large pyramidal soma with thick apical dendrite → L5
- Patch C: dense small soma, many spines → L2/3
- Patch D: mossy fiber bouton (3 μm, packed vesicles) → hippocampus CA3
- For each, articulate the evidence chain: "I see [features], which tells me [layer/region], which means I expect [cell types and synapse types]."
- **24:00-38:00 | Ambiguity case discussion**
- Present 3 ambiguous patches where layer context changes interpretation:
- A large bouton near a blood vessel: thalamocortical (L4) or local collateral (L2/3)?
- A smooth dendrite near a soma: inhibitory interneuron or astrocytic process?
- A process at the volume boundary: cannot trace to soma — how to handle?
- Group discussion: what additional evidence would resolve each ambiguity?
- **38:00-50:00 | Learner annotation round**
- Learners independently annotate 4 new patches, recording:
- Estimated layer/region
- Structure identification (cell type, compartment)
- Confidence level (high/medium/low)
- Evidence chain (which features support the call)
- **50:00-60:00 | Debrief and competency check**
- Review learner annotations as a group. Focus on:
- Did layer context affect the classification?
- Were confidence levels calibrated (not all "high")?
- Were boundary/ambiguous cases handled with explicit uncertainty?
- Exit ticket: "Name one anatomical cue that changed your interpretation today."

---

## Misconceptions to Watch
- **Misconception guardrail:** cortical layer can be read off a single EM patch without soma density or neuropil context.
- **Misconception guardrail:** the hippocampal laminar logic transfers to neocortex because both are cortex.
- **Misconception guardrail:** an atlas coordinate is a ground-truth location.
- **Misconception guardrail:** annotation confidence should be uniform across a volume.

---

## Studio Activity
**Scenario:** You are given a set of 8 EM patches from a mouse cortex volume. The patches span different layers (L1 through L6) but are presented without layer labels.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
**Minimum pass**

- Context-aware call and confidence note recorded for every patch.
- Layer identification within ±1 layer for the majority of patches.
- At least one evidence chain written in the form "features observed, therefore layer, therefore expected structures."

---

## Assessment Rubric
**Strong performance**

- Each call links at least two independent EM cues (soma density, neuropil texture, cell-type signature) to layer context.
- Confidence varies across patches in a calibrated way: boundary and volume-edge patches score lower than mid-layer patches.
- Cross-slice (z) evidence cited wherever a single-section call was ambiguous.
- Partner disagreements resolved by naming which cue was decisive, not by splitting the difference.

---

## Assessment Rubric
**Common failure to flag**

- Definitive call from a single feature without a layer or neighbor-slice check.
- Uniform "high" confidence across all patches, including boundary cases.
- Hippocampal and neocortical laminar logic applied interchangeably.

---

## Exit Ticket
Describe one case where anatomy context changes your interpretation of an EM structure.

---

## References (Instructor)
- Use module references listed on the module page.

---

## Teaching Materials
- Module page: /modules/module04/
- Slide page: /modules/slides/module04/
- Worksheet: /assets/worksheets/module04/module04-activity.md
