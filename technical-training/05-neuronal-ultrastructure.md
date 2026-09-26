---
layout: page
title: "05 Neuronal Ultrastructure"
description: "How to actually read an EM image: the organelle catalog with sizes, the minimum criteria for calling a synapse, Gray type I vs II, and a calibrated confidence protocol."
permalink: /technical-training/05-neuronal-ultrastructure/
image: /assets/images/units/05-neuronal-ultrastructure.svg
image_alt: "Stylized vector art: the inside of a membrane profile: a mitochondrion, a vesicle cluster, and a postsynaptic density."
slug: 05-neuronal-ultrastructure
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
level: "Intermediate"
time_estimate: "2.5 hours reading + 75 minute studio"
prerequisites: "Units 01-03"
graded_exercise: "studio activity"
content_type: path
---

{% include callouts/community-resources.html unit="05" %}

## Before you start

| | |
|---|---|
| **Time** | **Self-study ~3.75 h:** about 2.5 h of reading plus the 75 min studio activity. **Taught:** a 95 min session, per the [lecture plan]({{ '/technical-training/slides/05-neuronal-ultrastructure/' | relative_url }}). **Deck:** the unit's slide deck is scoped to 60 min and does not follow the plan slide for slide. |
| **Prerequisites** | Units 01–03. Unit 03's artifact catalog in particular — you cannot distinguish biology from artifact without it. |
| **You need** | A public EM volume open in Neuroglancer |
| **You finish with** | Calibrated compartment and synapse calls with justified confidence tiers, plus a personal cue-reliability ranking |

Everything downstream depends on someone being able to look at a patch of grayscale
noise and say correctly what it is. Segmentation networks are trained on those
judgments. Proofreading decisions rest on them. Every synapse count in every
connectomics paper traces back to a human who decided that a particular smudge was a
postsynaptic density.

This unit teaches the visual cues with sizes: *which* organelles, *how big*, and *what
they rule out*.

---

## What you'll be able to do

1. Name the major organelles visible in EM, with approximate sizes, and say which compartment each implies.
2. Apply the three minimum criteria for calling a chemical synapse, and refuse to call one when a criterion is missing.
3. Distinguish Gray type I from type II morphology and state the inference each licenses, and its limits.
4. Assign a calibrated confidence tier with a stated evidence chain.
5. Diagnose your own errors by cue, not just by count.

---

## 1. The organelle catalog

This is the reference table. Sizes are approximate and vary with preparation, but the
*relative* sizes and the *presence/absence patterns* are what you actually use.

| Structure | Size | Appearance in EM | Found in | Practically absent from |
|---|---|---|---|---|
| **Synaptic vesicle, clear round** | 35–50 nm | Small circular profiles, clear lumen, clustered | Presynaptic terminals | Dendrites, glia |
| **Synaptic vesicle, pleomorphic/flattened** | ~35–50 nm | Oval or flattened profiles; shape is partly a fixation artifact but is diagnostically useful | Inhibitory terminals | Excitatory terminals |
| **Dense-core vesicle** | 80–120 nm | Circular with a dark core | Peptidergic/monoaminergic terminals; also in transit along axons | — |
| **Postsynaptic density (PSD)** | 30–50 nm thick, 200–800 nm wide | Dark, granular thickening under the postsynaptic membrane | Postsynaptic side | Presynaptic side |
| **Synaptic cleft** | 20–30 nm (asymmetric); ~15–20 nm (symmetric) | Uniform-width gap with parallel membranes, often with faint cross-bridges | Between synaptic partners | Random appositions have variable-width gaps |
| **Microtubule** | ~25 nm outer diameter | Tubule in longitudinal section; small ring in cross-section | Dendrites (abundant, in loose parallel arrays); axons (present, more regularly spaced) | Mature spine heads; most glial processes |
| **Neurofilament** | ~10 nm | Fine filaments, often in bundles | Axons, especially myelinated | Spines |
| **Mitochondrion** | 0.2–1 µm diameter, variable length | Double membrane with cristae | Somata, dendritic shafts, axons and boutons | Most spines; the thinnest processes |
| **Rough ER / polyribosomes** | Ribosome ~25 nm | Studded membrane sheets; ribosome rosettes | Soma, proximal dendrites, dendritic shafts | **Axons** — a workhorse discriminator |
| **Golgi apparatus** | ~1 µm stack | Stacked flattened cisternae with vesicles | Soma, proximal dendrite | Axons |
| **Smooth ER / spine apparatus** | Laminae ~30 nm | Tubules; in spines, stacked laminae with dense material between | Dendrites; spine apparatus in a minority of (mostly large) spines | — |
| **Multivesicular body** | 200–500 nm | Membrane-bound body containing small internal vesicles | Everywhere; enriched in dendrites | — |
| **Glycogen granule** | 20–30 nm | Very dark small particles, clustered | **Astrocytes** — near-diagnostic | Neurons |
| **Myelin** | A few to dozens of lamellae, more around larger axons | Regular concentric dark lamellae | Around myelinated axons | Dendrites |
| **AIS undercoating** | Thin dense layer | Granular density beneath the axolemma, plus fasciculated microtubules | Axon initial segment (the first ~20–60 µm of the axon), nodes of Ranvier | Everywhere else |

**The two highest-value entries** for a beginner are the rough ER row and the glycogen
row: *ribosomes rule out axon*, and *glycogen granules indicate
astrocyte*. Those two facts settle many of the calls new annotators get stuck on.

### Check yourself

<details markdown="1">
<summary>A process ~400 nm across contains a mitochondrion, several microtubules, and
what look like a few ribosome rosettes. No vesicles, no PSD visible in this plane.
Best call, and what would raise your confidence?</summary>

**Probable dendrite (or a proximal dendritic branch), medium confidence.** The
ribosome rosettes are the strongest single cue. Axons are effectively free of
polyribosomes as seen in connectomics EM, so their presence argues strongly against
axon. The microtubules and mitochondrion are consistent but not
discriminating; both compartments have them.

To raise confidence, look for cues that are *independent* of the ribosome call:

- Scroll through z and look for **spines** emerging from the process. A spine with a
  head and neck is close to definitive for dendrite.
- Look for **incoming asymmetric synapses** where this process is postsynaptic. A
  PSD *on this process* means it is receiving, which is dendritic (or somatic).
- Follow the process toward larger caliber and check whether it thickens toward a
  soma. Dendrites taper with distance from soma; axons maintain caliber.

Note the reasoning pattern, which is the transferable skill: **do not stack more
of the same kind of evidence.** Three microtubule observations are one piece of
evidence. A ribosome plus a spine plus a taper is three.
</details>

---

## 2. Calling a synapse: the three criteria

A chemical synapse in EM requires **all three**:

1. **A presynaptic vesicle cluster**: a group of vesicles gathered at the membrane
   facing the partner. Not scattered vesicles somewhere in the profile; clustered *at
   the apposition*.
2. **A synaptic cleft**: parallel membranes with a gap of uniform width across the
   contact, typically 15–30 nm (table above). Ordinary appositions can have
   gaps of similar size, so uniform width and parallel membranes matter more than the
   exact number.
3. **A postsynaptic density**: a visible dark thickening on the receiving side.

And a fourth practical requirement that experienced annotators treat as
non-negotiable:

4. **Persistence across sections.** The features should be visible on more than one
   consecutive section. A PSD is typically 200–500 nm across. When the sections cut
   it edge-on at 40 nm each, a real one spans roughly 5 to 12 sections (200 ÷ 40 to
   500 ÷ 40). A PSD lying nearly flat in the section plane shows up on only one or two,
   as a dark patch seen face-on, so check for that before rejecting. A single-section
   "synapse" seen edge-on is one sample of a structure that should have given you
   several.

> **The most common beginner error** is calling a synapse from dark contrast alone.
> Dark contrast at a membrane can be a genuine PSD, a tangentially cut membrane (very
> common: a membrane sliced obliquely looks thick and dark), staining
> precipitate, a glial apposition, or a puncta adherens / adherens junction. Criterion
> 1 is what separates these: **no vesicles, no synapse.**

### Adherens junctions: the classic false positive

Puncta adherentia have symmetric densities on *both* sides and no vesicle cluster.
They look convincing at first glance. The tell is symmetry plus the absence of a
vesicle pool.

### Gray type I vs type II

| | **Type I (asymmetric)** | **Type II (symmetric)** |
|---|---|---|
| PSD | Thick, prominent, clearly asymmetric | Thin, roughly equal to the presynaptic density |
| Cleft | Wider, ~20–30 nm | Narrower, ~15–20 nm |
| Vesicles | Round, clear | Pleomorphic / flattened |
| Usual location | Dendritic spines; some shafts | Shafts, soma, AIS |
| Usual inference | Excitatory (glutamatergic) | Inhibitory (GABAergic) |

**The inference is a Bin B claim** in the Unit 01 sense. It is a well-supported
statistical association, not an identity. Known complications: vesicle shape depends
on fixation and can be unreliable; some glutamatergic synapses onto interneuron shafts
appear less asymmetric; neuromodulatory terminals do not fit the dichotomy at all.

**Therefore:** write "putatively excitatory (asymmetric)" rather than "excitatory",
and where the claim matters, corroborate with the identity of the presynaptic cell
type, which is usually the stronger evidence.

### Check yourself

<details markdown="1">
<summary>You see a dark thickening between two processes. On the section above and
below, the thickening is absent. One process contains a mitochondrion; neither shows a
clear vesicle cluster. Call?</summary>

**Not a synapse. Do not annotate one.** Criterion 1 fails (no vesicle cluster) and
criterion 4 fails (not persistent).

The most likely explanations are a tangentially sectioned membrane or a
non-synaptic apposition. The presence of a mitochondrion is not evidence either
way; mitochondria are everywhere.

The correct output is a *negative* call, and if the region is ambiguous enough to
have cost you time, log it as an uncertain patch so it enters the calibration set.
Negative calls are data. An annotator who never says "no" is not calibrated.
</details>

<details markdown="1">
<summary>A bouton contains round clear vesicles, makes a contact with a thick PSD onto
a spine head, and *also* contacts a nearby dendritic shaft with a thin symmetric
density. What is going on?</summary>

Most likely the second contact is not a synapse from this bouton. Check for a
vesicle cluster at *that* apposition specifically. A single terminal's vesicle pool
can sit near several membranes; only the apposition with an adjacent vesicle
cluster and a cleft counts.

If a vesicle cluster genuinely is present at both, you have a **multi-synaptic
bouton**, which is real and common. Note that one terminal making both an
asymmetric contact onto a spine and a symmetric contact onto a shaft would be
unusual and worth flagging for expert review. It may indicate a **merge error**
that has fused two different axons into one object. This is a good example of
ultrastructural reading catching a segmentation error: the biology looks wrong, so
suspect the segmentation.
</details>

---

## 3. Compartment cues: a decision protocol

Work in this order: cheap, reliable cues first.

**Step 1 — Local geometry.** Diameter and its variation. Boutons are swellings
connected by thin intervaricose segments; dendritic shafts have relatively smooth
caliber; spine heads sit on necks.

**Step 2 — Organelles present, and just as important, organelles *absent*.**
Ribosomes present → not axon. Glycogen granules → astrocyte. Vesicle cluster →
presynaptic. Absence is evidence when the structure would be visible if present at
this magnification and plane.

**Step 3 — Synaptic role.** Does the process bear PSDs (receiving) or vesicle clusters
(sending)? Many processes do both, but the balance is informative.

**Step 4 — Continuity across sections.** This is where most single-plane calls get
overturned. Scroll. A process that looked like a bouton may be a dendritic varicosity;
a "vesicle cluster" may be a tangential slice through something else.

**Step 5 — Neighborhood.** What is around it? An axon in a myelinated bundle, a
process wrapping a capillary, a profile inside a glial sheath. Context frequently
settles calls that local features cannot.

**Step 6 — Assign confidence with a stated evidence chain.**

### The confidence tiers, defined operationally

Tiers are useless unless everyone means the same thing. Define them by *evidence
count and independence*, not by feeling:

| Tier | Definition | Example |
|---|---|---|
| **High** | ≥ 2 *independent* cues agree, and continuity across ≥ 3 sections confirms | Ribosomes + a spine + taper toward soma → dendrite |
| **Medium** | 1 strong cue, or ≥ 2 non-independent cues; continuity checked but partially ambiguous | Vesicle cluster present, PSD unclear on the partner |
| **Uncertain** | Cues conflict, or the decisive cue is not visible in available sections | Process crosses a fold; identity plausible but unverifiable |

**"Uncertain" is a valid and valuable output.** A dataset in which, say, 8% of calls are
flagged uncertain with reasons is more useful than one in which 100% are forced,
because the uncertain set is exactly the training and review priority queue. The
uncertain rate per region is also the best available proxy for local data difficulty
(Unit 03).

---

## 4. Independence of cues, and why it is the whole game

Two cues that share a failure mode are one cue.

- Microtubule count and cytoplasmic density both degrade together under poor staining.
  In a weakly stained region, they are not independent.
- Vesicle *presence* and vesicle *shape* are not independent; if you cannot see
  vesicles clearly, you cannot use their shape either.
- Diameter and organelle content are partly dependent, because a thin process has less
  room for organelles regardless of type.

Genuinely independent cue families:

1. Geometry and caliber profile
2. Organelle content (presence and absence)
3. Synaptic role
4. Neighborhood and tissue context
5. Long-range continuity: where the process *goes*

**Rule for high confidence: two cues from different families.** This single rule does
more for annotation quality than any amount of exhortation to "be careful", because it
is checkable: a reviewer can look at an evidence chain and see whether it draws on
one family or two.

### Worked example: a full evidence chain

> **Patch:** a ~250 nm process in layer 2/3 neuropil, containing a small cluster of
> round clear vesicles and one mitochondrion, apposed to a bulbous ~600 nm profile.

**Family 1 (geometry):** the small process swells locally and narrows on either side
across z: a bouton on an intervaricose segment. The partner is bulbous with a narrow
attachment visible two sections down: a spine head on a neck.

**Family 2 (organelles):** round clear vesicles clustered at the apposition. No
ribosomes in the small process. The spine head contains no microtubules and shows a
faint spine apparatus.

**Family 3 (synaptic role):** thick asymmetric PSD on the spine-head side; cleft of
uniform width; visible across four consecutive sections.

**Family 4 (context):** several other boutons in the neighborhood contact spines
similarly, which fits normal excitatory neuropil rather than an artifact region.

**Call:** presynaptic axonal bouton making a type I synapse onto a dendritic spine
head. **Confidence: high.** Families 1, 2 and 3 agree independently, and continuity
is confirmed over four sections.

**Inference licensed:** putatively excitatory (asymmetric morphology; sign inferred,
not observed).

**Not licensed:** any statement about synaptic strength, or about the identity of the
presynaptic cell without tracing the axon to a soma.

---

## Visual training set

Work these panels with the organelle table in §1 open, and name the cue family behind every call you make. They are stills, and single-plane inspection is the habit this unit exists to break: step 4 of the protocol, continuity across sections, is where most single-plane calls get overturned. Treat the panel as a reference for what a cue looks like, and do your actual calling in a volume you can scroll through z.

<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S04-01.png' | relative_url }}" alt="Schematic neuron with cell body, dendrites, an axon labeled as less than 1 mm to more than 1 m long, and terminal branches ending in nerve terminals" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S04:</strong> A textbook neuron: cell body, dendrites, one axon (under 1 mm to over 1 m long) and its terminal branches. Use it to fix vocabulary before you meet anything ambiguous. For each compartment, recall from §1 which organelles you would expect present and, more usefully, which would be absent. Ribosomes ruling out axon is the highest-value entry in that table.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S08-01.png' | relative_url }}" alt="Electron micrograph of part of a cell body: nucleus with dark heterochromatin at the top and one long mitochondrion with cristae below it" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S08:</strong> A somatic region: nucleus with heterochromatin above, one long mitochondrion below. Use it to anchor the soma end of the compartment table in §1. A nucleus puts you in a cell body without any judgment call; everywhere else, compartment identity has to be argued from cues.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S09-01.png' | relative_url }}" alt="Low-magnification electron micrograph of neuropil: a myelinated axon in cross-section at top left, long processes cut lengthwise, and many dark mitochondria" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S09:</strong> Neuropil at low magnification: a myelinated axon in cross-section (top left), processes cut lengthwise, dark mitochondria throughout. Name what this field lets you call and what it does not. Myelin settles one profile as an axon. No synapse can be called here, because a vesicle cluster, a uniform cleft and a PSD (§2) are not resolvable at this zoom, and dark contrast alone is the commonest beginner error.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S10-01.png' | relative_url }}" alt="Electron micrograph with a large process in cross-section, its cytoplasm dotted with microtubules and holding several mitochondria, surrounded by many small round profiles" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S10:</strong> A large process in cross-section, dotted with microtubules and holding several mitochondria, among many small round profiles. Microtubules and mitochondria are consistent with a dendritic shaft, but both compartments have them (§1). Name the independent cue that would settle it: ribosomes inside, a PSD on its membrane, or a spine leaving it in a nearby section.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S14-01.png' | relative_url }}" alt="Electron micrograph of neuropil with a profile packed with small round vesicles and a mitochondrion at left, among processes containing dark mitochondria" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S14:</strong> A vesicle-filled profile beside processes with dark mitochondria. Use it for the discipline §4 calls the whole game: pick two features that differ between profiles and ask whether they come from different cue families or share a failure mode. Two cues that degrade together under poor staining are one cue.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S20-01.png' | relative_url }}" alt="Two panels: an electron micrograph with a 1 micrometre scale bar, and a labeled schematic of a presynaptic terminal, vesicles, cleft and postsynaptic dendrite" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S20:</strong> A two-panel reference: an EM micrograph with a 1&nbsp;µm scale bar beside a labeled schematic naming presynaptic terminal, presynaptic and postsynaptic membranes, cleft, vesicles and the postsynaptic dendrite. Read the schematic first, then find each labeled part in the micrograph. That translation, from idealized diagram to noisy tissue, is the step §2's three criteria have to survive.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S24-01.png' | relative_url }}" alt="High-magnification electron micrograph of a vesicle-filled terminal with a dark membrane density at lower left and a dark ring-shaped structure at right" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S24:</strong> An advanced case for review. Build a full evidence chain in the form of the §4 worked example (geometry, organelle content, synaptic role, neighborhood) and stop at the point where the chain would need continuity across sections that a single still cannot supply.</p>
  </article>
</div>

<p><small>Attribution: Pat Rivlin training materials (MICrONS proofreading deck).</small></p>

---

## 5. Studio activity: ultrastructure consensus round (75 min)

**Scenario.** Your team is preparing a training-ready annotation subset for
segmentation QC. It deliberately contains borderline cases.

1. **Independently** label each patch: compartment, synapse status, confidence tier.
2. Record two supporting cues **with their families** and one uncertainty per patch.
3. Compare within the group; classify each disagreement as *cue conflict*, *missing
   context*, or *vocabulary mismatch*.
4. Resolve what can be resolved; escalate genuine ambiguity with a written rationale.
5. **Revise one rubric rule** to reduce future disagreement of the type you saw most.

**Outputs:** consensus annotation sheet; disagreement log with counts by type; one
rubric revision with rationale.

**Why step 5 matters.** Vocabulary mismatch is often the largest category on a first
run, and better protocol wording can fix it without anyone becoming a better
microscopist. Run the loop two or three times and record inter-annotator agreement
each round. Whatever gain you measure came from the protocol, not the eye, and that
is the part of annotation quality that scales to a team.

---

## Assessment rubric

| | Not yet | Proficient | Strong |
|---|---|---|---|
| **Evidence quality** | Single-cue calls presented as definitive | Two cues per call | Two cues from *different families*, with independence argued |
| **Synapse criteria** | Calls from contrast alone | Applies all three criteria | Applies all three plus persistence; correctly rejects adherens junctions and tangential membranes |
| **Confidence** | Missing or inconsistent | Tiers applied consistently | Tier justified against the operational definitions; uncertain rate is reasonable, neither zero nor excessive |
| **Inference discipline** | "Excitatory synapse" | "Putatively excitatory (asymmetric)" | Names the assumption and proposes corroboration via presynaptic cell type |
| **Error analysis** | Counts errors | Classifies disagreements by type | Converts the dominant disagreement type into a concrete protocol revision |

---

## Common errors and how to recover

**Single-slice overconfidence.** Recover: make scrolling a mandatory step in the
protocol, not a suggestion. Add a checkbox to the annotation sheet.

**Stacking dependent cues.** Recover: label each cue with its family. Three cues from
one family is one cue.

**Forcing labels.** Recover: define and reward the uncertain tier; track the uncertain
rate per annotator as a calibration statistic, not a performance penalty.

**Label drift along a long trace.** Recover: build in periodic re-checks. Every N
micrometers of tracing, re-verify the compartment call from scratch rather than
carrying the earlier decision forward.

**Reading artifact as biology.** Recover: keep the Unit 03 artifact catalog open.
When something is anomalous, ask whether its shape follows tissue or follows the
section/tile/scan geometry.

---

## The norm behind this unit

Some of what this unit teaches is technique. Some of it is **professional norm** — the
things experienced people do without being asked, and which nobody states out loud
because they assume you already know. Those are worth naming, because they are
[distributed unequally by background]({{ '/hidden-curriculum/' | relative_url }}) rather
than by ability.

From this unit:

- **"Uncertain" is a real answer and should be rewarded out loud.**
  An annotator who never says "no" is not calibrated. Learners suppress uncertainty because they read it as failure; a facilitator has to say the opposite explicitly, once, early.

- **Two cues from different families, or it is not high confidence.**
  Three observations that share a failure mode are one observation. Nobody states this, and it is the single most common reasoning error in annotation.

The collected set, and why making these explicit is a fairness intervention rather than
etiquette, is in [the hidden curriculum]({{ '/hidden-curriculum/technical-practice/' | relative_url }}).

## What this unit does not cover

Systematic axon-vs-dendrite classification, which gets its own treatment in Unit 06;
glial identification in Unit 07; and how these calls feed proofreading triage in
Unit 08.

---

## Go deeper

- [Synapse classification]({{ '/content-library/neuroanatomy/synapse-classification/' | relative_url }}) — type I/II in depth, with edge cases
- [Organelle cues]({{ '/content-library/neuroanatomy/organelle-cues/' | relative_url }}) — extended organelle reference
- [Soma ultrastructure]({{ '/content-library/neuroanatomy/soma-ultrastructure/' | relative_url }}) — somatic features and nuclear morphology
- [Dendrite biology]({{ '/content-library/neuroanatomy/dendrite-biology/' | relative_url }}) — spines, shafts, and the spine apparatus
- [Neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }}) — from ultrastructure to cell type

## Course links

- Reading list: [Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Related modules: [Module 04]({{ '/modules/module04/' | relative_url }}), [Module 09]({{ '/modules/module09/' | relative_url }}), [Module 11]({{ '/modules/module11/' | relative_url }})
- Lecture plan: [Neuronal Ultrastructure lecture plan]({{ '/technical-training/slides/05-neuronal-ultrastructure/' | relative_url }})
- **Next unit:** [06 Axons and Dendrites]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }})
