# Module 09 Activity Worksheet

**Module:** Module 09: Neuron Morphology and Skeletonization  
**Duration:** 4 hours  
*Generated from the module page. Edit `modules/module09.md`, not this file.*

---

## Capability target

Produce a skeleton-based morphology summary with at least three descriptors and one explicit limitation.

You are done when you can demonstrate this, not when you have filled in every box below.

---

## Before you start

Check that you have:

- [ ] The module prerequisites listed on the module page

Bring one question you already have about this topic. Write it here so you can check
at the end whether it was answered:

> My question:

## Questions this module answers

Keep these in view. At the end, answer each in one sentence.

1. Which morphology features are robust across reconstructions?
   - Your answer:
2. How should skeleton uncertainty be communicated?
   - Your answer:

---

## The task

**Scenario:** You have skeletons for 10 neurons in L2/3 of mouse visual cortex. Your task is to classify them as pyramidal vs interneuron based on morphology alone, then validate against synapse-based classification (excitatory vs inhibitory output synapses).

1. Compute morphological descriptors for all 10 neurons (cable length, branch points, spine density, Strahler number, arbor volume).
2. Create a summary table and scatter plot (e.g., spine density vs cable length).
3. Classify each neuron as pyramidal or interneuron based on morphological criteria.
4. Compare your morphological classification to the synapse-based classification (provided). Do they agree?
5. For any mismatches, investigate: was the morphological measurement affected by reconstruction quality?

### What you hand in

- Artifact produced during the activity
- One stated limitation or uncertainty
- One revision made in response to feedback

---

## Working checklist

Tick as you go. If you skip a step, write why — a skipped step with a stated reason
is a decision; a skipped step without one is a gap.

- [ ] Build skeleton from volumetric segmentation using TEASAR or equivalent algorithm.
- [ ] Quality-check the skeleton: prune spurious branches, verify branch points, check for disconnected fragments.
- [ ] Compute descriptors: cable length, branch points, Strahler number, Sholl profile, spine density.
- [ ] Compare against reference patterns: does this neuron match the expected morphology for its putative cell type?
- [ ] Report interpretation confidence: which descriptors are robust, which are affected by reconstruction quality?

---

## Evidence and reasoning

Fill one row per claim you make in your artifact. A claim without a limitation is
not finished.

| # | Claim | Evidence (what specifically) | Limitation / what would change my mind |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Confidence.** For your main claim, mark one and say why:

- [ ] **High** — two or more independent lines of evidence agree
- [ ] **Medium** — one strong line, or several that share a weakness
- [ ] **Uncertain** — the deciding evidence is not available to me

Why:

**One alternative I considered and rejected**, and the reason:

---

## Misconception self-check

These are the errors this module is designed to prevent. Confirm you did not make
them, or note where you nearly did:

- [ ] I have stated one thing I am still unsure about.

---

## Session timing (facilitator reference)

| Time | Segment |
|---|---|
| 00:00-10:00 | Morphology overview |
| 10:00-24:00 | Skeleton extraction demo |
| 24:00-38:00 | Descriptor calculation |
| 38:00-50:00 | Interpretation and caveats |
| 50:00-60:00 | Competency check |

---

## Rubric

Score yourself before anyone else does. Where you fall short, name the specific next
action rather than a general intention.

- **Minimum pass**: Valid skeleton and descriptor set for all neurons. At least 3 descriptors.
- **Strong performance**: Robust interpretation linking descriptors to cell-type identity. Explicit uncertainty framing for borderline cases. Investigation of mismatches.
- **Common failure to flag**: Descriptor list without biological context — reporting numbers without explaining what they mean for the neuron's identity.

**My self-assessment:**

- Strongest part of my work, and the evidence for that:
- Weakest part, and the specific next action:

---

## Exit prompt

Explain one morphology feature that could be confounded by reconstruction quality.

**Your answer:**

---

## Peer review (swap worksheets)

Reviewing someone else's reasoning is the fastest way to see the gaps in your own.
Assess the **evidence quality**, not whether you agree with the conclusion.

- Is every claim paired with specific evidence?
- Is at least one limitation stated, and is it a real one?
- Is the confidence level justified by the number of *independent* evidence lines?
- One thing this person did better than me:
- One question I would ask them:

---

*Module page: `/modules/module09/` · Slides: `/modules/slides/module09/` · [Facilitator guide](/teaching/facilitator-guide/)*
