---
layout: page
title: "05 Neuronal Ultrastructure"
description: "How to actually read an EM image: the organelle catalogue with sizes, the minimum criteria for calling a synapse, Gray type I vs II, and a calibrated confidence protocol."
permalink: /technical-training/05-neuronal-ultrastructure/
slug: 05-neuronal-ultrastructure
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
level: "Intermediate"
time_estimate: "2.5 hours reading + 60 minute tutorial + 75 minute studio"
prerequisites: "Units 01-03"
content_type: path
---

## Before you start

| | |
|---|---|
| **Time** | ~2.5 h reading; 60 min tutorial; 75 min studio |
| **Prerequisites** | Units 01–03. Unit 03's artifact catalogue in particular — you cannot distinguish biology from artifact without it. |
| **You need** | A public EM volume open in Neuroglancer |
| **You finish with** | Calibrated compartment and synapse calls with justified confidence tiers, plus a personal cue-reliability ranking |

Everything downstream depends on someone being able to look at a patch of greyscale
noise and say correctly what it is. Segmentation networks are trained on those
judgments. Proofreading decisions rest on them. Every synapse count in every
connectomics paper traces back to a human who decided that a particular smudge was a
postsynaptic density.

This unit teaches the actual visual cues, with sizes. Not "use organelle evidence" —
*which* organelles, *how big*, and *what they rule out*.

---

## What you'll be able to do

1. Name the major organelles visible in EM, with approximate sizes, and say which compartment each implies.
2. Apply the three minimum criteria for calling a chemical synapse, and refuse to call one when a criterion is missing.
3. Distinguish Gray type I from type II morphology and state the inference each licenses — and its limits.
4. Assign a calibrated confidence tier with a stated evidence chain.
5. Diagnose your own errors by cue, not just by count.

---

## 1. The organelle catalogue

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
| **Mitochondrion** | 0.2–1 µm diameter, variable length | Double membrane with cristae | Everywhere except thin spine necks and the thinnest processes | — |
| **Rough ER / polyribosomes** | Ribosome ~25 nm | Studded membrane sheets; ribosome rosettes | Soma, proximal dendrites, dendritic shafts | **Axons** — a workhorse discriminator |
| **Golgi apparatus** | ~1 µm stack | Stacked flattened cisternae with vesicles | Soma, proximal dendrite | Axons |
| **Smooth ER / spine apparatus** | Laminae ~30 nm | Tubules; in spines, stacked laminae with dense material between | Dendrites; spine apparatus in a minority of (mostly large) spines | — |
| **Multivesicular body** | 200–500 nm | Membrane-bound body containing small internal vesicles | Everywhere; enriched in dendrites | — |
| **Glycogen granule** | 20–30 nm | Very dark small particles, clustered | **Astrocytes** — near-diagnostic | Neurons |
| **Myelin** | 10–20 lamellae | Regular concentric dark lamellae | Around myelinated axons | — |
| **AIS undercoating** | ~20 nm dense layer | Granular density beneath the axolemma, plus fasciculated microtubules | Axon initial segment (~20–60 µm from soma), nodes of Ranvier | Everywhere else |

**The two highest-value entries** for a beginner are the ones in bold logic:
*ribosomes rule out axon*, and *glycogen granules indicate astrocyte*. Those two facts
alone resolve a large share of early-annotator confusion.

### Check yourself

<details markdown="1">
<summary>A process ~400 nm across contains a mitochondrion, several microtubules, and
what look like a few ribosome rosettes. No vesicles, no PSD visible in this plane.
Best call, and what would raise your confidence?</summary>

**Probable dendrite (or a proximal dendritic branch), medium confidence.** The
ribosome rosettes are the strongest single cue — axons are effectively free of
polyribosomes in standard EM connectomics practice, so their presence argues
strongly against axon. The microtubules and mitochondrion are consistent but not
discriminating; both compartments have them.

To raise confidence, look for cues that are *independent* of the ribosome call:

- Scroll through z and look for **spines** emerging from the process. A spine with a
  head and neck is close to definitive for dendrite.
- Look for **incoming asymmetric synapses** where this process is postsynaptic — a
  PSD *on this process* means it is receiving, which is dendritic (or somatic).
- Follow the process toward larger calibre and check whether it thickens toward a
  soma. Dendrites taper with distance from soma; axons maintain calibre.

Note the reasoning pattern, which is the transferable skill: **do not stack more
of the same kind of evidence.** Three microtubule observations are one piece of
evidence. A ribosome plus a spine plus a taper is three.
</details>

---

## 2. Calling a synapse: the three criteria

A chemical synapse in EM requires **all three**:

1. **A presynaptic vesicle cluster** — a group of vesicles gathered at the membrane
   facing the partner. Not scattered vesicles somewhere in the profile; clustered *at
   the apposition*.
2. **A synaptic cleft** — parallel membranes with a consistent gap, wider than the
   ~10–20 nm typical of casual membrane apposition, and of uniform width across the
   contact.
3. **A postsynaptic density** — a visible dark thickening on the receiving side.

And a fourth practical requirement that experienced annotators treat as
non-negotiable:

4. **Persistence across sections.** The features should be visible on more than one
   consecutive section. A single-section "synapse" at 40 nm z-resolution is one
   sample of a structure that is typically 200–500 nm wide — if it is real, you should
   see it two to five times.

> **The single most common beginner error** is calling a synapse from dark contrast
> alone. Dark contrast at a membrane can be: a genuine PSD, a tangentially cut
> membrane (very common — a membrane sliced obliquely looks thick and dark), staining
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

**Not a synapse — do not annotate one.** Criterion 1 fails (no vesicle cluster) and
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

Most likely the second contact is not a synapse from this bouton — check for a
vesicle cluster at *that* apposition specifically. A single terminal's vesicle pool
can sit near several membranes; only the apposition with an adjacent vesicle
cluster and a cleft counts.

If a vesicle cluster genuinely is present at both, you have a **multi-synaptic
bouton**, which is real and common. Note that one terminal making both an
asymmetric contact onto a spine and a symmetric contact onto a shaft would be
unusual and worth flagging for expert review — it may indicate a **merge error**
that has fused two different axons into one object. This is a good example of
ultrastructural reading catching a segmentation error: the biology looks wrong, so
suspect the segmentation.
</details>

---

## 3. Compartment cues: a decision protocol

Work in this order. The order matters — cheap, reliable cues first.

**Step 1 — Local geometry.** Diameter and its variation. Boutons are swellings
connected by thin intervaricose segments; dendritic shafts have relatively smooth
calibre; spine heads sit on necks.

**Step 2 — Organelles present, and just as important, organelles *absent*.**
Ribosomes present → not axon. Glycogen granules → astrocyte. Vesicle cluster →
presynaptic. Absence is evidence when the structure would be visible if present at
this magnification and plane.

**Step 3 — Synaptic role.** Does the process bear PSDs (receiving) or vesicle clusters
(sending)? Many processes do both, but the balance is informative.

**Step 4 — Continuity across sections.** This is where most single-plane calls get
overturned. Scroll. A process that looked like a bouton may be a dendritic varicosity;
a "vesicle cluster" may be a tangential slice through something else.

**Step 5 — Neighbourhood.** What is around it? An axon in a myelinated bundle, a
process wrapping a capillary, a profile inside a glial sheath — context frequently
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

**"Uncertain" is a valid and valuable output.** A dataset in which 8% of calls are
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

1. Geometry and calibre profile
2. Organelle content (presence and absence)
3. Synaptic role
4. Neighbourhood and tissue context
5. Long-range continuity — where the process *goes*

**Rule for high confidence: two cues from different families.** This single rule does
more for annotation quality than any amount of exhortation to "be careful", because it
is checkable — a reviewer can look at an evidence chain and see whether it draws on
one family or two.

### Worked example: a full evidence chain

> **Patch:** a ~250 nm process in layer 2/3 neuropil, containing a small cluster of
> round clear vesicles and one mitochondrion, apposed to a bulbous ~600 nm profile.

**Family 1 (geometry):** the small process swells locally and narrows on either side
across z — a bouton on an intervaricose segment. The partner is bulbous with a narrow
attachment visible two sections down — a spine head on a neck.

**Family 2 (organelles):** round clear vesicles clustered at the apposition. No
ribosomes in the small process. The spine head contains no microtubules and shows a
faint spine apparatus.

**Family 3 (synaptic role):** thick asymmetric PSD on the spine-head side; cleft of
uniform width; visible across four consecutive sections.

**Family 4 (context):** several other boutons in the neighbourhood contact spines
similarly — consistent with normal excitatory neuropil, not with an artifact region.

**Call:** presynaptic axonal bouton making a type I synapse onto a dendritic spine
head. **Confidence: high** — families 1, 2, and 3 agree independently, and continuity
is confirmed over four sections.

**Inference licensed:** putatively excitatory (asymmetric morphology; sign inferred,
not observed).

**Not licensed:** any statement about synaptic strength, or about the identity of the
presynaptic cell without tracing the axon to a soma.

---

## Visual training set

Work these panels with the organelle table in §1 open, and name the cue family behind every call you make. They are stills, and single-plane inspection is precisely the habit this unit exists to break — step 4 of the protocol overturns more calls than any other. Treat the panel as a reference for what a cue looks like, and do your actual calling in a volume you can scroll through z.

<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S04-01.png' | relative_url }}" alt="Ultrastructure training visual: neuron structure overview" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S04:</strong> Neuron structure at the compartment level. Use it to fix vocabulary before you meet anything ambiguous: for each compartment, recall from §1 which organelles you would expect present and, more usefully, which would be absent. Ribosomes ruling out axon is the highest-value entry in that table.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S08-01.png' | relative_url }}" alt="Ultrastructure training visual: dendritic context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S08:</strong> A somatic region — nuclear envelope with heterochromatin above, one long mitochondrion below. Use it to anchor the soma end of the compartment table in §1: rough ER and a nucleus put you in a cell body, and that is the one place where the ribosome cue is unambiguous rather than a judgement call.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S09-01.png' | relative_url }}" alt="Ultrastructure training visual: synapse cues" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S09:</strong> The synapse cue set. Hold anything you would call to all three criteria in §2: a vesicle cluster at the apposition itself, a cleft of uniform width, and a density on the receiving side. Dark contrast alone is the commonest beginner error — no vesicles, no synapse.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S10-01.png' | relative_url }}" alt="Ultrastructure training visual: vesicle and organellar detail" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S10:</strong> Vesicles and organelles at annotation scale. Check size against §1 before naming anything — clear synaptic vesicles run 35–50 nm and dense-core vesicles 80–120 nm, so this is a measurement rather than an impression. Remember that vesicle shape is partly a fixation artifact and is not independent of vesicle visibility.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S14-01.png' | relative_url }}" alt="Ultrastructure training visual: comparative panel" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S14:</strong> A comparative panel. Use it for the discipline §4 calls the whole game: pick two features that differ between profiles and ask whether they come from different cue families or share a failure mode. Two cues that degrade together under poor staining are one cue.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S20-01.png' | relative_url }}" alt="Ultrastructure training visual: ambiguity case" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S20:</strong> A two-panel reference — an EM micrograph with a 1&nbsp;µm scale bar beside a labelled schematic naming presynaptic terminal, presynaptic and postsynaptic membranes, cleft, vesicles, and the postsynaptic dendrite. Read the schematic first, then find each labelled part in the micrograph beside it. That translation — idealised diagram to real noisy tissue — is the step §2's three criteria have to survive.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/05-neuronal-ultrastructure/FIG-RIV-ULTRA-S24-01.png' | relative_url }}" alt="Ultrastructure training visual: advanced structural example" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S24:</strong> An advanced case for review. Build a full evidence chain in the form of the §4 worked example — geometry, organelle content, synaptic role, neighbourhood — and stop at the point where the chain would need continuity across sections that a single still cannot supply.</p>
  </article>
</div>

<p><small>Attribution: Pat Rivlin training materials (MICrONS proofreading deck).</small></p>

---

## 5. Sixty-minute tutorial: run-of-show

### Pre-class (10–15 min, async)

- Read §1 and §2 of this unit. Bring the organelle table.
- Open the figure panel above and preview at least three figures.
- Bring one cue you find ambiguous.

### Materials

- [Neuronal Ultrastructure lecture plan]({{ '/technical-training/slides/05-neuronal-ultrastructure/' | relative_url }})
- The figure panel above (RIV-ULTRA shortlist)
- A shared annotation sheet with columns: patch ID | compartment call | synapse call |
  confidence tier | cue family 1 | cue family 2 | what would change my mind

The last column is the one that produces learning. Insist on it.

### Minute by minute

| Time | Activity | Instructor focus |
|---|---|---|
| 00:00–05:00 | **Framing.** Prompt: "What goes wrong if we force a label too early?" | Set the capability target; state that "uncertain" is a passing answer |
| 05:00–12:00 | **Expert modelling.** Work one patch aloud, following the §3 protocol | Think aloud about *uncertainty*, not just conclusions. Name each cue's family explicitly |
| 12:00–20:00 | **Guided practice 1.** Two easy patches, in pairs | Circulate; ask "which family is that cue from?" rather than "is that right?" |
| 20:00–30:00 | **Public debrief.** Compare calls openly | Target the three misconceptions below |
| 30:00–42:00 | **Guided practice 2.** Two borderline patches, independently | Require two independent cues plus one uncertainty statement per patch |
| 42:00–52:00 | **Consensus round.** Groups reconcile using the tier definitions | Classify each disagreement: cue conflict / missing context / vocabulary mismatch |
| 52:00–58:00 | **Competency check.** One fully justified call each | Label + confidence + evidence chain + one alternative considered and rejected |
| 58:00–60:00 | **Exit ticket.** "One cue I trust more now; one I still mistrust" | Collect these — they are your calibration data for next session |

### The three misconceptions to target explicitly

1. **"Small process = axon."** Size alone is unreliable; thin dendritic branches and
   spine necks are small too. Counter with a ribosome-bearing thin process.
2. **"Dark contrast = synapse."** Counter with a tangentially sectioned membrane and
   with an adherens junction.
3. **"Every patch must end in a hard label."** Counter by praising a well-justified
   "uncertain" in the public debrief. Learners calibrate to what gets rewarded, so
   reward it visibly, once, early.

### Formative checkpoints

- **At 20 min:** ≥ 80% of pairs cite two cues from *different families*. If not, stop
  and re-teach §4 — proceeding without this makes the rest of the session unproductive.
- **At 42 min:** the disagreement log distinguishes cue conflict from missing context.
- **At 58 min:** each learner justifies one call with explicit uncertainty language.

### Post-class (20–30 min)

Annotate three new patches; submit call, confidence, cue rationale by family, and one
unresolved ambiguity with an escalation note.

---

## 6. Studio activity: ultrastructure consensus round (75 min)

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

**Why step 5 matters.** Vocabulary mismatch is usually the largest category on a first
run, and it is entirely fixable by better protocol wording. Teams that run this loop
two or three times typically see inter-annotator agreement rise substantially without
anyone becoming a better microscopist — the gain comes from the protocol, not the eye.
That is the scalability lesson of this unit.

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

**Label drift along a long trace.** Recover: build in periodic re-checks — every N
micrometres of tracing, re-verify the compartment call from scratch rather than
carrying the earlier decision forward.

**Reading artifact as biology.** Recover: keep the Unit 03 artifact catalogue open.
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

- Reading list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Related modules: [Module 04]({{ '/modules/module04/' | relative_url }}), [Module 09]({{ '/modules/module09/' | relative_url }}), [Module 11]({{ '/modules/module11/' | relative_url }})
- Lecture plan: [Neuronal Ultrastructure lecture plan]({{ '/technical-training/slides/05-neuronal-ultrastructure/' | relative_url }})
- **Next unit:** [06 Axons and Dendrites]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }})
