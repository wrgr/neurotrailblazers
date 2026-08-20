---
layout: page
title: "07 Glia"
description: "Recognizing astrocytes, oligodendrocytes, and microglia in EM, why glia-neuron boundary errors corrupt neuronal connectivity, and a drill-based protocol for getting them right."
permalink: /technical-training/07-glia/
slug: 07-glia
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
level: "Intermediate"
time_estimate: "90 minutes reading + 60 minute drill"
prerequisites: "Units 05-06"
---

## Before you start

| | |
|---|---|
| **Time** | ~90 min, plus a 60 min discrimination drill |
| **Prerequisites** | Units 05–06 |
| **You need** | A public EM volume; the Unit 05 organelle table |
| **You finish with** | A glia recognition checklist and a measured discrimination score by cell class |

**The claim this unit has to earn:** glia are not background, and correcting glia is
not tidying up. Glia and their processes occupy roughly 20–40% of cortical tissue
volume, and astrocytic processes specifically form a fine meshwork that interleaves
with every neurite in the neuropil. That geometry is exactly what makes them the most
frequent partner in a merge error.

---

## What you'll be able to do

1. Identify astrocytes, oligodendrocytes, and microglia from soma and process features.
2. Discriminate a fine astrocytic process from a thin neurite using cues that survive poor staining.
3. Explain, with a concrete mechanism, how a single glia-neuron merge corrupts a connectivity measurement.
4. Prioritize glia corrections against other proofreading work on impact rather than count.
5. Run a discrimination drill and interpret the resulting confusion matrix.

---

## 1. Why a glia merge is expensive

Take one merge: a fine astrocytic process is fused with a nearby dendrite.

**What happens to the neuron:**
- It gains a branch that does not exist. Its total dendritic length, branch count, and
  arbor extent are all wrong.
- The astrocytic process wanders through neuropil the real dendrite never visits.
  Synapse detections along that path get attributed to this neuron — so the neuron
  gains inputs from cells it has never contacted.
- Because astrocytic processes ensheathe synapses, the merged path runs *directly
  past* a large number of synapses. The false-input yield per unit length of an
  astrocytic merge is unusually high.

**What happens to the astrocyte:** it loses territory, so any astrocyte morphometry —
domain volume, synapse coverage, vascular contact — is also wrong.

**What happens to your analysis:** the false inputs are not random. They are spatially
local, which means they preferentially connect the neuron to its *neighbours*. A
motif analysis will see enhanced local clustering; a distance-dependence analysis will
see inflated short-range connectivity. Again the bias points toward an interesting
result.

> **Consequence for triage.** Glia-neuron merges should be ranked *above* many
> neuron-neuron splits in a proofreading queue, even though a split is more visually
> obvious. The Unit 08 rule — prioritize by effect on the endpoint metric, not by
> conspicuousness — has its clearest application here.

---

## 2. Recognition: the three classes

Each class has one near-diagnostic feature. Learn those three first; everything else
is corroboration.

### Astrocyte — *diagnostic feature: glycogen granules*

| | |
|---|---|
| **Nucleus** | Pale, euchromatic, often irregular in contour |
| **Cytoplasm** | Pale and "watery"; few organelles; bundles of intermediate filaments (GFAP) ~10 nm |
| **Glycogen granules** | 20–30 nm, very dark, in clusters. **Neurons do not contain them.** |
| **Soma size** | ~8–10 µm, smaller than most neuronal somata |
| **Processes** | Irregular, sheet-like, fill the gaps between neuronal elements rather than running as cylinders |
| **Perisynaptic processes** | Extremely thin (< 100 nm), wrapping synapses — the hardest structures in the volume to segment |
| **Endfeet** | Flattened expansions covering blood vessel surfaces — a strong contextual cue |
| **Absent** | Synaptic vesicles, PSDs, and (largely) microtubules |

### Oligodendrocyte — *diagnostic feature: the darkest nucleus in the field*

| | |
|---|---|
| **Nucleus** | Small, round, extremely electron-dense heterochromatin. Distinctly darker than neuronal or astrocytic nuclei — usually identifiable at a glance and at low magnification |
| **Cytoplasm** | Dense, abundant rough ER and ribosomes, prominent Golgi, microtubules present |
| **Soma size** | ~6–8 µm |
| **Processes** | Connect the soma to myelin sheaths; each cell myelinates on the order of 20–60 axonal segments |
| **Myelin relationship** | Inner and outer tongues contain oligodendrocyte cytoplasm; paranodal loops at nodes of Ranvier |

The practical difficulty is not the mature oligodendrocyte — it is the
**oligodendrocyte precursor cell (OPC/NG2 cell)**, which has a paler nucleus and can
resemble a small neuron or an astrocyte. If a cell looks "sort of oligodendrocyte but
the nucleus is not dark enough", OPC is the leading hypothesis and the correct action
is usually to flag rather than force.

### Microglia — *diagnostic feature: dense elongated nucleus plus lysosomal content*

| | |
|---|---|
| **Nucleus** | Dark, often elongated or bean-shaped, with heterochromatin clumped along the nuclear envelope |
| **Cytoplasm** | Dense, with characteristic long, narrow ER cisternae; lysosomes, phagosomes, and lipofuscin-like inclusions |
| **Processes** | Fine, highly irregular contours; frequently seen contacting synapses and vessels |
| **State-dependence** | Morphology changes substantially with activation state, which makes microglia the least stereotyped of the three |

### Astrocyte vs thin neurite: the discrimination that matters most

This is where most errors occur, so it gets its own table.

| Feature | Astrocytic process | Thin neurite |
|---|---|---|
| **Glycogen granules** | Present | Absent |
| **Synaptic participation** | None (no vesicles, no PSD) | Vesicles (axon) or PSD (dendrite) |
| **Microtubules** | Absent or very rare | Usually present |
| **Cross-sectional shape** | Irregular, angular, sheet-like; fills residual space between other profiles | Roughly circular or elliptical; a coherent tube |
| **Cytoplasm** | Pale, few organelles | Denser, organelles visible |
| **Intermediate filaments** | Fine bundles (GFAP) | Absent (neurofilaments differ in distribution and context) |
| **Trajectory across sections** | Wanders, changes shape section to section | Maintains a continuous, traceable trajectory |

> **The shape cue is underused and it is robust.** Astrocytic processes are *space
> filling* — their cross-section is whatever shape is left over after the neurites are
> packed. Neurites are *tubes* — their cross-section is a shape in its own right. This
> cue survives weak staining better than glycogen granules do, which makes it valuable
> exactly in the regions where everything else fails.

### Check yourself

<details markdown="1">
<summary>A pale, irregular profile sits between three neurites. You see no glycogen
granules. Is it an astrocytic process?</summary>

**Probably, but this is a medium-confidence call at best, and the reasoning matters
more than the answer.**

Absence of glycogen granules is weak evidence here: granules are clustered and
sparse, so a given thin process may contain none in a given section even when it is
astrocytic. This is the Unit 06 lesson about over-reading absence.

Better evidence to seek, in order:

1. **Shape and space-filling** across several sections — does it change contour to
   fill gaps, or does it hold a tube shape?
2. **Synaptic participation** — scroll for any vesicle cluster or PSD on it. Finding
   one converts this to a neurite call immediately.
3. **Continuity toward a soma or an endfoot** — following it to a vessel endfoot is
   close to definitive for astrocyte.
4. **Microtubules** at higher magnification.

If cues 1–4 do not resolve it, the correct output is *uncertain*, with a note that
the deciding cue was not resolvable. That is a useful annotation.
</details>

---

## 3. The identification protocol

```
1. Is this a soma (nucleus visible)?
   YES -> nucleus first:
      very dark, small, round      -> oligodendrocyte (check for myelin links)
      dark, elongated, peripheral
        heterochromatin + lysosomes-> microglia
      pale, irregular, glycogen    -> astrocyte
      pale, round, big nucleolus,
        Nissl/rER, dendrites       -> neuron
      pale but "not quite"         -> OPC candidate -> FLAG
   NO  -> continue to 2

2. Does the process participate in a synapse
   (vesicle cluster or PSD on it)?
   YES -> neurite. Go to Unit 06 for axon/dendrite.
   NO  -> continue

3. Glycogen granules present?
   YES -> astrocyte (high confidence)
   NO  -> continue (absence is weak evidence)

4. Cross-sectional character over 5-10 sections:
   space-filling, contour changes to fit gaps -> astrocyte (medium-high)
   coherent tube, stable contour              -> neurite (medium)

5. Context:
   wraps a capillary (endfoot)        -> astrocyte (high)
   inner/outer tongue of a myelin
     sheath, or paranodal loop        -> oligodendrocyte (high)
   irregular contour + lysosome-rich
     parent process                   -> microglia (medium)

6. Unresolved -> UNCERTAIN, with the missing cue named.
   Route to the glia review queue.
```

---

## Visual training set

Work these against the identification protocol in §3, naming the step that decides each case. They are single planes and the decisive glial cue usually is not one: step 4 asks how a cross-section behaves over five to ten sections, and perisynaptic astrocytic sheets under 100 nm thick are the hardest structures in the volume. Use the panel as a reference for what the cues look like, and do the calling in a volume you can scroll through z.

<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/07-glia/FIG-RIV-GLIA-S01-01.png' | relative_url }}" alt="Glia training visual: overview context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-GLIA S01:</strong> Orientation for glia proofreading. Set the stake before you start looking: glia occupy roughly 20–40% of cortical volume, and a glia-neuron merge does not merely add a branch — it drags a neuron’s arbor past synapses it never contacted, so the false-input yield per micrometre of merged path is unusually high.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/07-glia/FIG-RIV-GLIA-S03-01.png' | relative_url }}" alt="Glia training visual: astrocyte context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-GLIA S03:</strong> Astrocyte morphology in a synaptic neighbourhood. Read cross-sectional shape before anything else: an astrocytic process is space-filling, taking whatever contour is left over after the neurites pack, where a neurite holds a tube shape of its own. That cue survives weak staining better than glycogen granules do, which makes it the one to reach for where everything else fails.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/07-glia/FIG-RIV-GLIA-S09-01.png' | relative_url }}" alt="Glia training visual: microglia context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-GLIA S09:</strong> Microglia cues. Look for the pairing that carries the call — a dark, often elongated or bean-shaped nucleus with heterochromatin clumped against the envelope, plus lysosomal and phagosomal content in dense cytoplasm. Microglia are the least stereotyped of the three classes because morphology tracks activation state, so weight nuclear evidence above process shape.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/07-glia/FIG-RIV-GLIA-S15-01.png' | relative_url }}" alt="Glia training visual: oligodendrocyte reconstruction" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-GLIA S15:</strong> Oligodendrocyte identification. Where a nucleus is in view it is the cue that works even at low magnification: small, round, and the densest in the field. If it reads as oligodendrocyte but the nucleus is not dark enough, OPC is the leading hypothesis and the correct action is to flag rather than force the call.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/07-glia/FIG-RIV-GLIA-S16-01.png' | relative_url }}" alt="Glia training visual: myelin-related glia context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-GLIA S16:</strong> Myelin context. Check where oligodendrocyte cytoplasm sits relative to the sheath — inner and outer tongues and paranodal loops are glial, and absorbing them into the axon is a merge waiting to happen. Myelin also settles a Unit 06 question for free: dendrites are never myelinated.</p>
  </article>
</div>

<p><small>Attribution: Pat Rivlin training materials (MICrONS proofreading deck). Two manifest-listed IDs (`S02`, `S07`) were not present in extracted thumbnails and are pending recovery.</small></p>

---

## 4. Drill: glia discrimination (60 minutes)

Recognition improves with **spaced, scored repetition on many short examples**, not
with reading. This drill is built for that.

**Build the set.** 40 patches: 10 astrocytic processes, 10 thin neurites, 5 astrocyte
somata, 5 oligodendrocyte somata, 5 microglia somata, 5 ambiguous or OPC cases. Show
each as a short z-stack (5–10 sections), not a single image — single-plane practice
teaches a habit you want to break.

**Run it.**

1. **Timed round.** 30 seconds per patch. Record: class call, confidence, and the one
   cue used. The time limit is deliberate; it forces reliance on the cue you actually
   trust rather than the one you would like to trust.
2. **Score into a confusion matrix** (true class × called class). Do not just count
   correct.
3. **Read the matrix.** The informative content is in the off-diagonal:
   - **Astrocyte called neurite** → you are under-weighting shape and space-filling.
     This is the error that causes merges.
   - **Neurite called astrocyte** → you are over-weighting pallor. This is the safer
     direction, but it wastes review effort.
   - **Oligodendrocyte called microglia** (or vice versa) → you are relying on "dark
     nucleus" without checking shape and cytoplasmic content.
   - **Anything called OPC** → check whether you are using OPC as a synonym for
     "unsure". It should not be.
4. **Re-drill the dominant off-diagonal cell only**, with 10 fresh patches. Targeted
   repetition on the confusion you actually have is far more efficient than repeating
   the whole set.
5. **Write your checklist** — no more than six lines, phrased as checks you can
   perform in 30 seconds.

### Rubric

| | Not yet | Proficient | Strong |
|---|---|---|---|
| **Overall accuracy** | < 70% | ≥ 80% | ≥ 85% with a non-zero uncertain rate |
| **Error asymmetry** | More astrocyte→neurite than neurite→astrocyte | Balanced | Errors skew toward the safe direction, deliberately, and you can say why |
| **Cue awareness** | Cannot name the deciding cue | Names it | Names it and identifies which cue fails first as staining degrades |
| **Matrix reading** | Reports accuracy only | Produces the matrix | Diagnoses the dominant confusion and targets the re-drill at it |
| **Checklist** | Restates the tables | Six actionable checks | Checks ordered by cost, cheapest and most reliable first |

<details markdown="1">
<summary>Why "errors skewed toward the safe direction" counts as Strong</summary>

The two error directions have very different costs.

**Astrocyte called neurite** is the merge-generating error. It puts glial membrane
inside a neuron, with all the consequences in §1.

**Neurite called astrocyte** produces a split — the neurite loses a piece. It is
visible (the arbor looks truncated), it is locally fixable, and it does not
manufacture false connectivity.

So a well-calibrated annotator working under time pressure should be *deliberately
biased* toward calling ambiguous cases astrocyte or uncertain. This is not
sloppiness; it is choosing the cheaper error on purpose, which is what asymmetric
loss functions mean in practice. The same logic drives the over-segmentation choice
in the pipeline (Unit 04 §1, Stage 4) — the field consistently trades splits for
merges, at every level, on purpose.
</details>

---

## 5. QA metrics for glia labelling

- **Glia–neuron boundary error rate** on a validation subset, reported separately from
  overall segmentation error, because it is a different failure with a different cost.
- **Per-class agreement** (astrocyte / oligodendrocyte / microglia / OPC). Aggregate
  agreement hides the fact that OPC agreement is usually much worse than the rest.
- **Unresolved-glia rate after second-pass review** — a proxy for whether your protocol
  is under-specified for this dataset.
- **Effect on neuronal statistics**: recompute per-neuron input counts and total
  dendritic length before and after a glia-correction pass on a sample. This number —
  "correcting glia changed mean input count by X%" — is the argument that gets glia
  correction into the proofreading budget. Measure it once and reuse it.

---

## Common errors and how to recover

**Treating glia as out of scope.** Recover: measure the §5 last metric on your own
data and put the number in the project's QC report.

**Over-calling microglia from fragments.** Recover: require a nucleus or a
lysosome-rich parent process before assigning microglia to a process fragment.

**Using OPC as a label for uncertainty.** Recover: separate the two. "Uncertain" and
"OPC candidate" are different annotations with different follow-ups.

**Single-plane calls.** Recover: build drills from z-stacks, never single images.

**Ignoring astrocyte territory corruption.** Recover: if the project makes any glial
claim at all, glia must be proofread to a stated standard, not opportunistically.

---

## What this unit does not cover

Vasculature and the neurovascular unit beyond astrocytic endfeet, and glial biology
beyond what is needed for identification. Ependymal cells and peripheral glia are out
of scope for cortical volume EM.

---

## Go deeper

- [Glia recognition]({{ '/content-library/cell-types/glia-recognition/' | relative_url }}) — full identification reference with worked examples
- [Myelin and nodes of Ranvier]({{ '/content-library/neuroanatomy/myelin-and-nodes/' | relative_url }}) — oligodendrocyte myelin biology and annotation implications
- [Axon–dendrite classification]({{ '/content-library/cell-types/axon-dendrite-classification/' | relative_url }}) — distinguishing glia from neuronal processes
- [Organelle cues]({{ '/content-library/neuroanatomy/organelle-cues/' | relative_url }}) — the organelle reference underlying these calls

## Course links

- Reading list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Related module: [Module 04]({{ '/modules/module04/' | relative_url }})
- Lecture plan: [Glia lecture plan]({{ '/technical-training/slides/07-glia/' | relative_url }})
- **Next unit:** [08 Segmentation and Proofreading]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
