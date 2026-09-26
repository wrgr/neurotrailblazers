---
marp: true
theme: neurotrailblazers
paginate: true
title: "NeuroTrailblazers deck template"
footer: "NeuroTrailblazers"
---

<!-- _class: title nanoscale -->
<!-- _paginate: skip -->

<img class="cover-image" src="../../../assets/images/content-library/case-studies/h01/10b-segmentation-overlay.jpg" alt="H01 electron microscopy with object segmentation and original 2 µm scale bar">
<span class="eyebrow">NeuroTrailblazers · Deck template</span>

# Nanoscale connectomics

Membranes, neurites, and the connections between them.

<p class="presenter">Presenter name · Affiliation · Date</p>
<p class="cover-label">Human cortex · H01<br>Object segmentation over electron microscopy</p>
<p class="source">H01 release · Lichtman Lab / Harvard &amp; Connectomics at Google · CC BY 4.0<br>Shapson-Coe et al. (2024) · doi:10.1126/science.adk4858</p>

---

## How to use this deck

<div class="cols">
<div>

**Start here**

1. Copy `neurotrailblazers-template.marp.md` and rename it.
2. Keep `theme: neurotrailblazers` in the front matter.
3. Set `footer:` to the unit or module name.
4. Render with `./scripts/render_marp.sh`, which registers the theme.

**One idea per slide.** If you need a second heading, you need a second slide.

</div>
<div>

**Slide classes available**

| Class | Use for |
|---|---|
| `title` | Opener, once |
| `section` | Divider between parts |
| *(none)* | Standard content |
| `mist` | Agenda, summary, quiet slides |
| `figure` | Image gets the room |
| `stat` | One number that matters |
| `dark` | Emphasis content slide |
| `closing` | Last slide |

</div>
</div>

---

<!-- _class: section -->

<span class="pill">Part 1</span>

# Section divider

One sentence saying what this part settles, in the reader's terms.

---

## Standard content slide

A short heading identifies the subject or states a supported finding.

- **Lead with the mechanism.** Say what happens, then why it matters for the learner's next decision.
- **Numbers over adjectives.** "About 2 PB per mm³" beats "very large".
- **One callout at most.** A slide with two boxes has two slides in it.
- Third-level detail belongs in the speaker notes, not on the slide.

<div class="note">

**Note callout.** Use for the caveat that a careful practitioner would raise unprompted: an assumption, a version pin, a boundary of the claim.

</div>

<p class="source">Source: unit page or DOI-pinned citation. Every figure or number slide carries one of these.</p>

<!--
Speaker notes go here. Marp keeps HTML comments as presenter notes.
-->

---

## Two columns: text against evidence

<div class="cols wide-left">
<div>

### What the learner should be able to do

- Decide whether a merge error or a split error is the more expensive fix for a given task.
- State the proofreading budget that makes a connectivity claim defensible.
- Name the null model before the metric.

### What this slide does not claim

That proofreading rates transfer across datasets. They do not; calibrate per volume.

</div>
<div>

![H01 neuronal soma with original scale bar](../../../assets/images/content-library/em/soma-ultrastructure.jpg)

<p class="caption">A compartment label needs evidence from the tissue.</p>

</div>
</div>

<p class="source">H01 release · site render · CC BY 4.0 · Shapson-Coe et al. (2024), doi:10.1126/science.adk4858</p>

---

<!-- _class: figure -->

## Membranes and model labels

![h:430 Raw EM alongside subcompartment classification, with original scale bars](../../../assets/images/content-library/em/neuropil-raw-vs-subcompartments.jpg)

<p class="caption">The same field, before and after classification. A model label is a hypothesis to check.</p>

<p class="source">H01 release · site render · CC BY 4.0 · Shapson-Coe et al. (2024), doi:10.1126/science.adk4858</p>

---

<!-- _class: stat -->

<p class="big">2,000<span style="font-size:0.45em"> GB</span></p>

Per cubic millimetre of imaged cortex, before any reconstruction. The infrastructure unit exists because of this number.

<p class="source">Source: Unit 04, Volume reconstruction infrastructure; MICrONS data release.</p>

---

<!-- _class: stat -->

## Three numbers, when one is not enough

<div class="stats">
<div>
<p class="big">9</p>
<p>technical units, each ending in a graded lab</p>
</div>
<div>
<p class="big">25</p>
<p>session kits with worksheets, rubrics and decks</p>
</div>
<div>
<p class="big">127</p>
<p>dictionary terms with a typical value and a common confusion</p>
</div>
</div>

---

## Tables and rubrics

| Level | Segmentation call | Evidence required |
|---|---|---|
| **Not yet** | Trusts the automated merge | No inspection recorded |
| **Proficient** | Inspects at branch points | Screenshot and coordinate per decision |
| **Strong** | Reports its own error rate | Blind re-check on a held-out sample |

<div class="good">

**Good callout.** The behaviour that separates a practitioner from someone who followed the steps.

</div>

<div class="warn">

**Warn callout.** The failure that looks like success: the query runs, the number is plausible, the version was never pinned.

</div>

---

<!-- _class: dark -->

## Dark content slide for the turn in the argument

Use sparingly, for the one slide where the room should sit up.

<div class="key">

**Key point.** Structure is evidence of organisation and constraint, <strong>not</strong> direct proof of dynamics. The connectome bounds what the circuit can do; it does not say what it did.

</div>

```python
# Code stays short and pinned
client = CAVEclient("minnie65_public")
syn = client.materialize.synapse_query(post_ids=[root_id],
                                       materialization_version=1300)
```

---

<!-- _class: mist -->

## Summary slide, quiet background

<div class="cols">
<div>

**Settled in this session**

- The claim, in one sentence.
- The metric, and the null it beat.
- The boundary: what this does not show.

</div>
<div>

**Next**

- Lab: produce the artifact and rubric-score it.
- Read: the unit's "Go deeper" links.
- Bring: one question the figure did not answer.

</div>
</div>

---

<!-- _class: closing -->
<!-- _paginate: skip -->

# Mapping connections. Making connections.

Questions, corrections and pull requests: **neurotrailblazers.org** · github.com/wrgr/neurotrailblazers

Supported by the NIH BRAIN CONNECTS program. Content CC BY 4.0 unless noted.
