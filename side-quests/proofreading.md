---
layout: page
title: "Side Quest: Proofreading"
description: "Correcting reconstruction errors as an allocation problem under a fixed budget. A distinct skill, worth a lab's attention on its own, and not a prerequisite for anything."
permalink: /side-quests/proofreading/
slug: side-quest-proofreading
content_type: path
track: research-in-action
pathways:
  - research workflow
  - project execution
---

## Why this is a side quest and not a stage

Proofreading appears inside two tracks — as [Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
in Core Concepts & Methods, and as [Module 07]({{ '/modules/module07/' | relative_url }})
in Research in Action. In both it is one step among ten, which is the wrong frame for it.

Treated properly, proofreading is not cleanup. It is an **allocation problem under a
fixed budget**: a finite number of human hours against an error population you cannot
enumerate, where the errors differ by orders of magnitude in what they cost your
specific scientific claim. That is a distinct skill with its own literature, its own
metrics, its own failure modes, and its own tooling. It is also, bluntly, the skill
most likely to get an early-career person taken seriously by a connectomics lab,
because it is the bottleneck and because competence at it is checkable.

So it is listed on its own. **You do not need to have finished a track to start here,
and finishing here does not put you further along one.**

## Before you start

| | |
|---|---|
| **Time** | 20–30 hours, workable in evenings over a few weeks |
| **Hard prerequisite** | You can tell an axon from a dendrite from a glial process in EM, with a confidence tier attached. If you cannot, do [Units 05–07]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}) first — proofreading without that is guessing at speed |
| **Soft prerequisite** | Comfort navigating a volume in Neuroglancer. Half an hour with the [dataset access guide]({{ '/datasets/access/' | relative_url }}) covers it |
| **Not required** | Python, a lab affiliation, statistics beyond arithmetic, or any other track |
| **Ends with** | A proofreading plan and a release memo that a lab can read and disagree with |

## The sequence

### 1. Learn what can go wrong, and what each failure costs — 4 hours

Read [Error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }})
in full, then [Unit 08 §2]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}).

The thing to extract is the **asymmetry**. A merge error fuses two cells and invents
connections that do not exist; a split error fragments one cell and hides connections
that do. These are not equally bad, and which is worse depends entirely on what you are
claiming. A merge that creates a false reciprocal pair destroys a paper about reciprocal
connectivity. A split in the same volume might cost nothing.

**You finish with:** the ability to look at a flagged error and say what it would do to a
named scientific claim — not "it's bad," but "it would inflate my reciprocal count."

### 2. Learn what the metrics are blind to — 5 hours

Read [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}),
then [Unit 08 §3]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}).

Variation of information, expected run length, edge precision and recall, synapse-centric
precision and recall, completeness. Each one is a real measurement and each one is blind
to something. Learn the blind spots in the same pass as the definitions, because the
characteristic failure here is optimising a dashboard number while the thing your paper
reports gets worse.

**You finish with:** for each metric, one sentence naming what it cannot see.

**Check yourself before moving on:**

<details markdown="1">
<summary>Your ERL improved by 40% after a proofreading round, and your synapse precision is unchanged. What are the two most likely explanations, and which would you check first?</summary>

Either (a) you fixed splits, which lengthen runs, while leaving merges — which are what
usually damage synapse precision — untouched; or (b) you concentrated effort on a few
long, well-behaved axons where run length responds strongly, while the bulk of the volume
is unchanged.

Check (a) first, by looking at your own correction log: count what fraction of your fixes
were split repairs. If it is most of them, you have an answer, and you also have a triage
bias to correct. ERL is a skeleton-path metric and rewards exactly the corrections that
extend paths, which is why it should never be read alone.
</details>

### 3. Learn the strategies, and when each is wrong — 4 hours

Read [Proofreading strategies]({{ '/content-library/proofreading/proofreading-strategies/' | relative_url }}).

Exhaustive local, targeted/skeleton-guided, priority-ranked, crowd-sourced, and hybrids.
Section 7 — *when to stop* — is the one to read twice. A stopping rule someone else could
apply is the difference between a proofreading effort and an open-ended one, and almost
nobody writes theirs down.

**You finish with:** a defensible answer to "why this strategy for this question," and a
stopping rule stated as a condition rather than as a feeling.

### 4. Learn the tools you would actually use — 3 hours

Read [Proofreading tools]({{ '/content-library/proofreading/proofreading-tools/' | relative_url }}),
then open a real volume and try the edit operations.

CAVE, Neuroglancer, Spelunker, NeuTu, CATMAID. You do not need all of them. You need to
understand versioning and materialization well enough that you can say which segmentation
version your corrections apply to — because an uncited version makes a correction log
worthless to anyone else.

**You finish with:** a scratch volume you have made at least one edit in, and the version
string written down.

### 5. Work the scenarios — 4 hours

Do all five in [Worked examples]({{ '/content-library/proofreading/worked-examples/' | relative_url }}):
merge at a blood vessel, split through low-contrast sections, false autapse from a merge,
priority triage for a campaign, and cross-annotator disagreement.

Attempt each before reading its resolution. Scenario 5 — disagreement — is the one people
skip and the one that matters most in a real lab, because it is where you find out whether
your confidence carries information or is just volume.

**You finish with:** your own call on each scenario, and a written note wherever yours
differed from the worked answer and why.

### 6. Produce the artifact — 6–8 hours

Do the [Unit 08 lab]({{ '/technical-training/08-segmentation-and-proofreading/#lab-proofreading-plan-with-a-defended-budget-2-hours' | relative_url }})
and the [Module 07 release-decision activity]({{ '/modules/module07/' | relative_url }}),
on a real public volume rather than a hypothetical one.

This is the part that is worth something outside this site. See below.

## The artifact

One document, three or four pages, that a lab could read cold:

1. **The claim.** What scientific question the proofreading is in service of. Not "improve
   quality" — a specific measurable endpoint.
2. **A triage rule.** How you rank a flagged error, stated so that two people applying it
   to the same queue would broadly agree.
3. **Defined levels.** What "proofread" means for each class of object in your volume.
   "Fully proofread" is not a level; "all merges resolved on the axon within 50 µm of the
   soma, splits unaddressed" is.
4. **A stopping rule.** The condition under which you stop, decided before you start.
5. **A correction log.** Before and after segment IDs, the segmentation version, and a
   one-line rationale per fix.
6. **A release memo.** Metrics before and after, remaining risks named rather than
   implied, and a go/no-go with the reasoning visible.

Item 6 is where most people's version falls down, and it falls down in a specific way: the
memo recommends release without referencing a single metric value. If yours does that,
it is not finished.

**Grade the reasoning, not the answer.** A no-go call with a clear evidence chain is
stronger work than a go call with none.

## What "done" looks like

- You can state, for a given error, what it would do to a named claim — not in general terms.
- You can defend a stopping rule against "but you could keep going."
- Your correction log lets someone else reconstruct what you did, including the version.
- You report a quality number and, in the same breath, what it is blind to.
- You have said "uncertain" about a real case and treated that as an answer rather than a failure.

## Common detours

- **Fixing what looks wrong instead of what matters.** The most common failure by a wide
  margin. Ad hoc correction feels productive and is uncorrelated with impact.
- **Optimising an aggregate score.** VI and ERL are proxies. Your paper does not report them.
- **Proofreading without a version pin.** The corrections are real; the record is not.
- **Skipping cross-annotator disagreement** because it is uncomfortable. It is the only
  calibration signal available to you.
- **Treating throughput as performance.** Corrections per hour without an agreement
  statistic beside it measures speed, not quality — and rewards exactly the wrong behaviour
  in anyone being watched.

## What this side quest does not cover

- **Automated proofreading.** Rule-based and learned systems now detect and correct a
  substantial share of errors before a human sees them; NEURD (Dorkenwald et al.,
  *Nature Methods*, 2024, [10.1038/s41592-024-02515-z](https://doi.org/10.1038/s41592-024-02515-z))
  is the reference implementation. This material teaches the human loop, which is what you
  are still doing when the automation hands you the residue — but the allocation problem
  changes shape when the easy errors are already gone, and none of the reference entries
  here reflect that yet. Read the paper alongside stage 3.
- **Running a campaign with other people.** Recruitment, training, agreement monitoring and
  pay are covered thinly in the crowd-sourcing section and not at all elsewhere.
- **Building the tools.** This is about using them.
- **Anything that certifies you.** Nothing here is a credential. The artifact is the thing
  you show; there is no gate behind it, and this site currently has no way to tell you
  whether your calls are actually right. That is the honest limit of
  [self-study]({{ '/modes/#self-study' | relative_url }}) here, and it is the gap the
  [research intensive]({{ '/modes/#research-intensive' | relative_url }}) would have to close.

## Where this connects

<div class="cards-grid cards-grid-wide">
  <article class="card">
    <h3 class="card-title"><a href="{{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}">Unit 08</a></h3>
    <p class="card-description">The same material as a taught unit inside Core Concepts &amp; Methods, with the lab this side quest borrows.</p>
  </article>
  <article class="card">
    <h3 class="card-title"><a href="{{ '/modules/module07/' | relative_url }}">Module 07</a></h3>
    <p class="card-description">The release-decision simulation, with a rubric. Has a <a href="{{ '/teaching/sessions/module07/' | relative_url }}">session kit</a> if you are running this for a group.</p>
  </article>
  <article class="card">
    <h3 class="card-title"><a href="{{ '/tools/connectome-quality/' | relative_url }}">Connectome Quality</a></h3>
    <p class="card-description">The quality-checking tool page, with the criteria this side quest's metrics stage assumes.</p>
  </article>
  <article class="card">
    <h3 class="card-title"><a href="{{ '/content-library/journal-papers/' | relative_url }}">The literature</a></h3>
    <p class="card-description">Proofreading and QA papers with what each established and what it did not, in the journal paper collection.</p>
  </article>
</div>

---

*[All side quests]({{ '/side-quests/' | relative_url }}) · [The core]({{ '/core/' | relative_url }}) · [Tracks]({{ '/tracks/' | relative_url }})*
