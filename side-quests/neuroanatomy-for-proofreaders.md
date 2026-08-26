---
layout: page
title: "Side Quest: Neuroanatomy for Proofreaders"
description: "The EM identification training behind competent proofreading: compartment cues, confidence tiers, a unified axon-dendrite-glia decision sequence, and a self-run calibration drill on a real public volume."
permalink: /side-quests/neuroanatomy-for-proofreaders/
slug: side-quest-neuroanatomy-for-proofreaders
content_type: path
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
---

## Why this exists

The [proofreading side quest]({{ '/side-quests/proofreading/' | relative_url }}) states
its hard prerequisite in one sentence: *you can tell an axon from a dendrite from a
glial process in EM, with a confidence tier attached.* Until now the only route to that
sentence was "do [Units 05]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }})–[07]({{ '/technical-training/07-glia/' | relative_url }})
in full" — three units built for a taught track, with tutorials, studio activities, and
run-of-shows a self-studier does not need.

This side quest is the direct route. It pulls the identification material out of the
units and the [content library]({{ '/content-library/' | relative_url }}) into one
sequence, adds the one thing no existing page carries — a single decision sequence that
covers axon, dendrite, *and* glia in the same pass — and ends in a calibration drill
you run yourself on a real public volume.

One warning before the reading list, because it changes how you should spend your
hours. Identification is a **perceptual skill**. The
[hidden curriculum]({{ '/hidden-curriculum/meta-learning/' | relative_url }}) puts it
bluntly: you cannot close a perceptual gap by reading, any more than you can learn to
hear an interval by reading about intervals. The reading below exists to give you a
cue vocabulary and a decision procedure. The skill comes from the scored judgments in
stages 5 and 6, and if you have to cut hours, cut reading, never judgments.

## Before you start

<dl class="spec-strip">
  <dt>Time</dt>
  <dd>15&ndash;20 hours, workable in evenings over two or three weeks.</dd>
  <dt>Hard prerequisite</dt>
  <dd>You have looked at EM of brain tissue and know what an image stack is. <a href="{{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}">Unit 03</a> covers this; you do not need all of it, but you should recognize an artifact when one crosses your screen.</dd>
  <dt>Soft prerequisite</dt>
  <dd>Basic Neuroglancer navigation, for the drill in stage 6. Half an hour with the <a href="{{ '/datasets/access/' | relative_url }}">dataset access guide</a> covers it.</dd>
  <dt>Not required</dt>
  <dd>Python, a lab affiliation, any track, or the proofreading side quest &mdash; this quest is the on-ramp to that one, not the other way around.</dd>
  <dt>Ends with</dt>
  <dd>A scored confusion matrix with accuracy reported by confidence tier, and a one-page personal cue card in your own words.</dd>
</dl>

## The sequence

<ol class="quest-steps">

<li class="quest-step" markdown="1">

### Learn the vocabulary: organelles and synapses <span class="quest-hours">4 hours</span>

Read [Unit 05 §1–2]({{ '/technical-training/05-neuronal-ultrastructure/#1-the-organelle-catalog' | relative_url }})
— the organelle catalog and the three criteria for calling a synapse — then go one
level deeper with [Organelle annotation cues]({{ '/content-library/neuroanatomy/organelle-cues/' | relative_url }})
and [Synapse classification]({{ '/content-library/neuroanatomy/synapse-classification/' | relative_url }}).

The organelle catalog is the alphabet everything else is written in. Two entries repay
special attention because they carry the most identification weight later: **ribosomes
and rough ER**, which the library rates as the single most reliable negative marker
for axonal identity, and **synaptic vesicles**, whose presence in a cluster at a
membrane is one of the three minimum criteria for a synapse — the other two being a
parallel membrane apposition and a postsynaptic density, with persistence across
sections as the check that keeps single-plane wishful thinking honest.

Skim [Soma ultrastructure]({{ '/content-library/neuroanatomy/soma-ultrastructure/' | relative_url }})
and [Myelin and nodes of Ranvier]({{ '/content-library/neuroanatomy/myelin-and-nodes/' | relative_url }})
rather than reading them in full: what you need now is the neuron-vs-glia soma
comparison table in the first, and §7 of the second — myelin as a strong axon
identifier, and why nodes of Ranvier are where segmentations of myelinated axons
break.

<div class="quest-outcome" markdown="1">
**You finish with:** the ability to name, for any organelle you can see in a patch,
which compartments it argues for and which it argues against — not "there's a
mitochondrion" but "elongated mitochondrion, consistent with dendrite or axon, tells
me little on its own."
</div>

**Check yourself before moving on:**

<details markdown="1">
<summary>A process contains a tight cluster of ~40 nm round vesicles. What can you conclude, and what two things do you check before calling the compartment an axon terminal?</summary>

You can conclude that a presynaptic identity is *plausible* — clustered small round
vesicles are the strongest single presynaptic cue. Before making the call: check for a
membrane apposition with a postsynaptic density on the partner side (vesicles without
an active zone can be a passing vesicle pool, not a terminal), and scroll adjacent
sections to confirm the cluster and the contact persist. A vesicle cluster in one
plane that vanishes in the next is a tangential slice through something else — Unit 05
treats persistence across sections as the criterion that rescues you from single-plane
errors.
</details>

</li>

<li class="quest-step" markdown="1">

### Learn the tier discipline before the cues that need it <span class="quest-hours">2 hours</span>

Read [Unit 05 §3–4]({{ '/technical-training/05-neuronal-ultrastructure/#3-compartment-cues-a-decision-protocol' | relative_url }}):
the six-step compartment decision protocol, the confidence tiers defined
operationally, and the five independent cue families.

This is the stage people skip because it looks procedural rather than anatomical, and
skipping it is how you end up fast and wrong. Two rules from this material govern
everything that follows:

- **High confidence requires two cues from *different* families.** Two cues that share
  a failure mode are one cue — microtubule count and cytoplasmic density both degrade
  together under poor staining, so agreeing with each other proves nothing.
- **"Uncertain" is a valid and valuable output.** The tier definitions are evidence
  counts, not feelings: high means at least two independent cues agree *and*
  continuity across three or more sections confirms. If you cannot state the evidence
  chain, you do not have the tier.

<div class="quest-outcome" markdown="1">
**You finish with:** the three tiers memorized as operational definitions, and the
habit of writing a call as *call + tier + evidence chain* — "dendrite, high:
ribosomes (organelle family) + spine with PSD (synaptic family), continuous across
five sections."
</div>

</li>

<li class="quest-step" markdown="1">

### Axon versus dendrite, properly <span class="quest-hours">4 hours</span>

Read [Unit 06]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }}) —
the four cue families, the exceptions that break the polarity rule, and the five-step
local classification protocol — then the library's
[Axon-dendrite classification]({{ '/content-library/cell-types/axon-dendrite-classification/' | relative_url }})
for the four-pass version with reliability ratings per cue, and
[Axon biology]({{ '/content-library/neuroanatomy/axon-biology/' | relative_url }}) and
[Dendrite biology]({{ '/content-library/neuroanatomy/dendrite-biology/' | relative_url }})
for the underlying biology, each of which ends in a worked discrimination example.

Do not memorize twenty cues with equal weight; learn the reliability *ordering*.
Ribosomes rank highest. Caliber ranks low — the misconception tables in both library
entries call out "axons are always thinner than dendrites" as false, and the unit's
rule is that caliber alone never supports a high-confidence call. And learn the four
exceptions to the polarity rule (dendro-dendritic synapses, axo-axonic contacts onto
the AIS, presynaptic dendrites in the retina, unipolar invertebrate neurons) well
enough that meeting one produces "exception, check context" rather than panic.

<div class="quest-outcome" markdown="1">
**You finish with:** Unit 06's five-step decision tree reproducible from memory, with
a confidence tier at each exit, and the reliability ordering of cues — which cue you
trust when two disagree.
</div>

**Check yourself before moving on:**

<details markdown="1">
<summary>A process in cortex shows scattered ribosomes along its length, and also a vesicle cluster with an active zone facing a spine. What is the leading hypothesis, and why is it not "an exception to the polarity rule"?</summary>

The leading hypothesis is a **merge error** — one segmentation object stitched from an
axon and a dendrite. Ribosomes are the strongest dendritic cue; a presynaptic active
zone is the strongest axonal cue; both are high-reliability cues from different
families. Unit 06's rule: when two high-reliability cues from *different* families
contradict each other, the leading hypothesis is not "one cue is wrong" but "this is
not one object." The known exceptions (presynaptic dendrites in the retina, for
example) are region- and cell-type-specific, so in generic cortex the segmentation
error is the more probable explanation — and this is exactly the reasoning stage 7
turns into a proofreading move.
</details>

</li>

<li class="quest-step" markdown="1">

### Glia: the confusion that costs the most <span class="quest-hours">3 hours</span>

Read [Unit 07]({{ '/technical-training/07-glia/' | relative_url }}) — why a glia
merge is expensive, the three classes with one near-diagnostic feature each, and the
six-step identification protocol — then the library's
[Glia recognition]({{ '/content-library/cell-types/glia-recognition/' | relative_url }})
for the per-class cue detail and the two worked edge cases (astrocyte vs. thin
dendrite, OPC vs. small neuron).

The discrimination that matters most is **astrocyte process versus thin neurite**,
and the unit's table for it deserves to be learned outright: glycogen granules,
absence of synaptic participation, absence of organized microtubules, and — the cue
that survives weak staining better than glycogen does — cross-sectional *shape*,
space-filling and angular where neurites are tubes. Learn the error asymmetry too:
calling an astrocyte a neurite feeds merge errors that inject false connectivity;
calling a neurite an astrocyte produces a visible, locally fixable split. The two
mistakes are not equally priced, and the drill in stage 6 scores them separately.

<div class="quest-outcome" markdown="1">
**You finish with:** one diagnostic feature per glial class recallable on demand, the
astrocyte-vs-thin-neurite table internalized, and the ability to say which direction
of glial misidentification costs more and why.
</div>

</li>

<li class="quest-step" markdown="1">

### Build the unified checklist <span class="quest-hours">1–2 hours</span>

No existing page carries the three-way discrimination in one pass — Unit 06's tree
covers axon vs. dendrite, Unit 07's protocol covers glia and hands off to Unit 06 at
step 2, and holding two fenced protocols in your head mid-drill does not work. So the
merge is this quest's contribution, and then, deliberately, yours.

Start from this synthesis of the two protocols and the library's tables:

```
0. ARTIFACT CHECK   Is this tissue? Folds, tears, staining dropout, myelin-
                    mimicking artifacts -> flag the location, not the biology.
1. NUCLEUS VISIBLE  Use the soma tables: chromatin pattern, nucleolus, Nissl.
                    Neuron / astrocyte / oligodendrocyte / microglia from the
                    nucleus alone gets you most of the way. (Unit 07 §3, soma
                    ultrastructure §9)
2. NEURITE OR GLIA  Glycogen granules, synaptic participation, organized
                    microtubules, cross-sectional shape: space-filling and
                    angular -> glial; tube -> neurite. (Unit 07 §2)
3. WHICH GLIA       One diagnostic feature per class: glycogen (astrocyte),
                    darkest nucleus in the field (oligodendrocyte), dense
                    bean-shaped nucleus + lysosomes (microglia). (Unit 07 §2)
4. AXON OR DENDRITE Ribosomes/RER -> dendrite. Vesicle cluster + active zone
                    on the sending side -> axon. Then geometry, then context.
                    Caliber alone never upgrades confidence. (Unit 06 §1, §3)
5. CUE CONFLICT     Two high-reliability cues from different families that
                    disagree -> suspect a segmentation error, not exotic
                    biology. Record it; stage 7 is about this. (Unit 06)
6. ASSIGN TIER      High = 2 independent families + continuity across >= 3
                    sections. Uncertain is an output, not a failure. (Unit 05)
```

Then rewrite it in your own words, at most one page, ordered the way *you* actually
check. The rewriting is not busywork: the facilitator guide's observation is that
learners who can describe cues and learners who can apply them are different
populations, and compressing the protocol into your own words is the cheapest way to
find out which you currently are.

<div class="quest-outcome" markdown="1">
**You finish with:** a one-page cue card, in your own words, that you will use — and
revise — during the drill. Revision marks on the card afterward are evidence of
learning, not of a bad first draft.
</div>

</li>

<li class="quest-step" markdown="1">

### Run the calibration drill on a real volume <span class="quest-hours">3 hours</span>

The units specify scored drills on curated patch sets, and this site does not host
one — the [side quest index]({{ '/side-quests/' | relative_url }}) has said so
honestly since the gap was named. What you can run today, alone, is the self-run
version: a public volume with a released segmentation, where the segmentation plays
the role of the answer key *and* of the thing you are learning to distrust.

**The protocol:**

1. Open a public EM volume with a released segmentation in Neuroglancer — the
   [dataset access guide]({{ '/datasets/access/' | relative_url }}) routes you to
   MICrONS and FlyWire. Write down the dataset and segmentation version.
2. Build a set of 20 locations before you start judging: drop annotation points
   semi-randomly through neuropil, resisting the pull toward clean-looking spots. Add
   a few deliberately hard ones — a myelinated bundle, a perivascular region, dense
   neuropil.
3. For each location, **hide the segmentation layer first.** At native EM resolution,
   make the call from your cue card: compartment, confidence tier, and the evidence
   chain (which cues, which families). Scroll adjacent sections — the units are
   emphatic that single-plane calls are a habit to break, not a shortcut to allow.
4. Reveal the segmentation and adjudicate. Agreement is provisional truth.
   Disagreement goes to one of two bins: *my error* (the segmentation, plus scrolling,
   shows a cue you missed or misweighted) or **candidate segmentation error** — your
   anatomy call stands and the released object looks wrong. Do not force either bin;
   an unresolvable case is recorded as uncertain.
5. Score into a confusion matrix: axon / dendrite / glia / uncertain against
   adjudicated truth. Compute overall accuracy, accuracy **within your
   high-confidence tier**, and your uncertain rate.

**Reading the score.** Unit 06's standard: high-confidence calls right at least 90%
of the time, with a non-trivial share of calls left uncertain. If your high-tier
accuracy matches your overall accuracy, your tiers are decoration and the fix is
tier discipline, not more anatomy. Interpret each off-diagonal cell the way Unit 07's
drill does — "astrocyte called dendrite" and "dendrite called astrocyte" are
different failures with different costs — and let the worst cell pick which stage you
reread before the second round.

Then make it a habit rather than an event: the
[hidden curriculum]({{ '/hidden-curriculum/meta-learning/' | relative_url }})
prescribes exactly this as a weekly mixed set, scored by tier, for as long as you are
doing identification work at all.

<div class="quest-outcome" markdown="1">
**You finish with:** a confusion matrix with accuracy by tier, an uncertain rate, a
dataset and segmentation version written down, and — if the volume cooperated — one
or two candidate segmentation errors you found by anatomy alone.
</div>

</li>

<li class="quest-step" markdown="1">

### Turn cues into proofreading calls <span class="quest-hours">2 hours</span>

Read [Error taxonomy §2–3]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }})
for the visual signatures of merges and splits, then Scenarios 2 and 5 of the
[proofreading worked examples]({{ '/content-library/proofreading/worked-examples/' | relative_url }}),
watching specifically for where the resolution turns on anatomy: caliber and
organelle-content match before committing a merge operation, smooth-ER continuity as
evidence that two fragments are one process, an excitatory-only branch beside an
inhibitory-only branch flagging a merge.

Everything you trained in stages 1–6 lands here as a short mapping, which is the
actual point of this quest:

| You observe | Suspect | The proofreading move |
|---|---|---|
| Ribosomes and a presynaptic active zone in the same object | Merge joining an axon and a dendrite | Walk the object to the join point; split there |
| A ~500 nm dendrite becoming a ~100 nm axon at a branch point | Merge at a false branch | Examine the branch point across sections |
| A process dead-ending with no terminal bouton, no vesicle cluster | Split — the rest of the cell is another fragment | Search past the break, guided by trajectory and caliber |
| Glycogen, no synapses, space-filling shape inside a "neuron" | Glia&ndash;neuron merge | Split at the boundary; these seed false inputs |
| A myelinated axon "disappearing" between sections | Node of Ranvier, not necessarily an error | Check ~20&ndash;30% caliber narrowing before editing anything |
| Impossible ~180&deg; hairpin branching in 3D | Merge | View the mesh in 3D; find the join |

The deeper habit under the table: **cue conflict is a segmentation-error detector.**
An annotator sees a weird object and doubts their anatomy; a proofreader sees the same
object and doubts the segmentation. Knowing which doubt to reach for — and holding it
with a stated confidence tier rather than certainty in either direction — is the
competence this quest exists to build.

<div class="quest-outcome" markdown="1">
**You finish with:** the prerequisite sentence of the
[proofreading side quest]({{ '/side-quests/proofreading/' | relative_url }}) true of
you, with evidence — which is your cue to start that quest.
</div>

</li>

</ol>

## The artifact

Three things, all of which stages 5 and 6 already produced in draft:

1. **The cue card.** One page, your own words, revised at least once during the drill.
2. **The calibration record.** The confusion matrix; overall accuracy, accuracy within
   your high tier, and uncertain rate; the dataset and segmentation version; and a
   one-line interpretation of your worst off-diagonal cell.
3. **Five evidence chains.** Written out in full — call, tier, cues, families,
   continuity — including at least one uncertain call and, if you found one, the
   candidate segmentation error with your reasoning.

This artifact is smaller than the proofreading quest's release memo, and that is
deliberate: it is the *entry* evidence a lab would want before letting you near a
correction queue. Calibration — a stated confidence that tracks actual accuracy — is
worth more to them than raw accuracy, because a calibrated annotator's uncertain flags
are a usable review queue and an overconfident annotator's errors are invisible.

## What "done" looks like

- You can produce the three-way call — axon, dendrite, glia — with a tier and an
  evidence chain, without consulting the card for routine cases.
- Your high-confidence accuracy is measurably better than your overall accuracy, and
  you can say by how much.
- You have written "uncertain" on real cases and can defend why that was the right
  output, not a failure.
- You have looked at a released segmentation and correctly doubted it at least once —
  or can explain why your volume gave you no occasion to.
- The exceptions to the polarity rule produce "check the context" rather than a
  forced call.

## Common detours

- **Reading all six library entries end-to-end before judging anything.** The entries
  are references, not a novel. The over-reading failure mode is
  [named in the hidden curriculum]({{ '/hidden-curriculum/meta-learning/' | relative_url }})
  — reading is private and cannot be judged, which is precisely its appeal and its
  danger. Get to stage 6 with hours still in the budget.
- **Single-plane calls.** The units repeat it because everyone does it: scroll.
  Every cue table you have read assumes continuity checking, and most wrong calls in
  practice are right-looking calls made in one plane.
- **Treating caliber as a cue family.** It is one weak cue inside geometry, and the
  misconception every beginner imports from textbook diagrams.
- **Forcing every drill disagreement into "my error."** Released segmentations
  contain errors; that is the entire premise of proofreading. If your evidence chain
  is sound and the object still looks wrong, "candidate segmentation error" is the
  honest bin — and the more valuable finding.
- **Scoring overall accuracy only.** The number that matters is accuracy *within your
  high tier*. Overall accuracy improves with caution; calibration only improves with
  honesty.

## What this side quest does not cover

- **A hosted, scored drill corpus.** The self-run protocol in stage 6 is the workable
  substitute, but it is not the curated set with planted errors that Units 05–07
  specify, and its answer key — a released segmentation — is itself imperfect, which
  the protocol turns into a feature but cannot fully escape. A hosted corpus with
  known ground truth remains an open gap, and the
  [side quest index]({{ '/side-quests/' | relative_url }}) will say so until it exists.
- **Cell typing.** Telling an axon from a dendrite is not telling a basket cell from
  a chandelier cell; that is
  [Neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }})
  and Unit 09's territory.
- **Synapse partner assignment at scale.** Stage 1 teaches you to call one synapse
  properly; production synapse proofreading has its own error modes, covered in
  [Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}).
- **The proofreading operation itself.** Budgets, triage, metrics, stopping rules,
  and the release decision are the
  [proofreading side quest]({{ '/side-quests/proofreading/' | relative_url }}), which
  this quest exists to make honest for you to start.
- **Anything that certifies you.** Same honest limit as every self-study path here:
  the artifact is the thing you show, and one external review of it is worth more
  than three self-reviews.

## Where this connects

<div class="arch-grid">
  <article class="arch-card" style="--accent: var(--layer-quest); --accent-tint: var(--layer-quest-tint);">
    <h3 class="arch-title"><a href="{{ '/side-quests/proofreading/' | relative_url }}">Proofreading side quest</a></h3>
    <p class="arch-body">The quest whose hard prerequisite this one satisfies. Start it as soon as stage 7 is done &mdash; the momentum transfers.</p>
  </article>
  <article class="arch-card" style="--accent: var(--layer-quest); --accent-tint: var(--layer-quest-tint);">
    <h3 class="arch-title"><a href="{{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}">Units 05&ndash;07</a></h3>
    <p class="arch-body">The same material as taught units, with tutorials, studio activities, and rubrics, for anyone working through Core Concepts &amp; Methods in order.</p>
  </article>
  <article class="arch-card" style="--accent: var(--layer-quest); --accent-tint: var(--layer-quest-tint);">
    <h3 class="arch-title"><a href="{{ '/content-library/' | relative_url }}">The content library</a></h3>
    <p class="arch-body">The neuroanatomy and cell-types entries this quest sequences, kept as standalone references for when one call needs the full argument.</p>
  </article>
  <article class="arch-card" style="--accent: var(--layer-quest); --accent-tint: var(--layer-quest-tint);">
    <h3 class="arch-title"><a href="{{ '/technical-training/dictionary/' | relative_url }}">The dictionary</a></h3>
    <p class="arch-body">Working definitions for the Units 05&ndash;07 vocabulary &mdash; postsynaptic density, Gray types, cue family, confidence tier &mdash; when a term in the reading will not resolve.</p>
  </article>
</div>

---

*[All side quests]({{ '/side-quests/' | relative_url }}) · [The core]({{ '/core/' | relative_url }}) · [Tracks]({{ '/tracks/' | relative_url }})*
