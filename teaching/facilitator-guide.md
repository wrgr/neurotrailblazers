---
layout: page
title: "Facilitator Guide"
description: "How to run NeuroTrailblazers material with real cohorts: session design, differentiation across the four learner personas, assessment that scales, and the failure modes that break connectomics teaching specifically."
permalink: /teaching/facilitator-guide/
slug: facilitator-guide
track: career-and-community
pathways:
  - classroom delivery
  - mentor support
summary: "Instructor-facing guide for pacing, differentiation, assessment, and scaling."
use_layout_hero: false
content_type: delivery
---

<div class="main-content">

<div class="hero hero-spaced hero-rounded">
  <div class="hero-content">
    <h1 class="hero-title-impact">Facilitator Guide</h1>
    <p class="hero-subtitle">Running sessions that produce measurable capability, with cohorts that differ widely in preparation.</p>
  </div>
</div>

<section class="section" markdown="1">

## Read this first: the constraint that shapes everything

In connectomics, **the gap between what a learner can be told and what they can do is
unusually wide**. The core skills (reading an EM image, judging a segmentation, choosing
a null model) are *perceptual and judgmental*, not procedural, and explanation alone does
not transmit them. A learner who can recite the three criteria for calling a synapse will
still, on their first real patch, call a tangentially cut membrane a synapse.

Everything below follows from that. The design principle throughout is:

> **Time spent making and comparing judgments beats time spent receiving
> explanations.** Aim for at least half of contact time on learner judgment with
> immediate comparison against a reference or a peer.

The corollary: a lecture-only delivery of this material can feel good and review well
while producing little transferable capability. If you have 60 minutes and can either explain thoroughly or have learners
make 20 scored judgments, choose the judgments.

</section>

<section class="section" markdown="1">

## Session design

### The standard four-phase structure

Every module and technical unit is built to run in this shape:

1. **Learn:** capability target and the concepts needed to attempt it. Short.
2. **Practice:** a studio activity producing an artifact with evidence.
3. **Check:** a rubric-based competency check.
4. **Teach:** slides and worksheet, so the learner can transfer it onward.

### The 60-minute template

| Time | Phase | What must happen |
|---|---|---|
| 00:00–08:00 | Framing | State the capability target. Activate prior knowledge with a question, not a recap |
| 08:00–20:00 | Modeling | Work **one** example aloud, including your own uncertainty. Do not work three cleanly; work one messily |
| 20:00–38:00 | Guided practice | Learners produce judgments. You circulate and ask about *evidence*, not answers |
| 38:00–50:00 | Debrief | Compare publicly. Target the named misconceptions |
| 50:00–58:00 | Competency check | Individual, written, against the rubric |
| 58:00–60:00 | Exit prompt | One thing more confident about, one thing still uncertain |

**The modeling phase is the easiest place to lose the session.** The temptation is
to present clean examples that make the method look reliable. Do the opposite: choose
an example where you genuinely have to weigh conflicting evidence, and narrate the
weighing. Watching an expert be uncertain in public is one of the few ways learners set
their own standard for "how sure should I be?"

### Question stems that work

Replace "is that right?", which teaches learners to seek your approval, with:

- "Show me your evidence chain before your label."
- "Which cue family is that from?" *(Units 05–06)*
- "Which cue would you drop first if the staining got worse?"
- "What would change your mind?"
- "What is the cheapest observation that would settle this?"
- "If you had to be wrong in one direction, which would you choose, and why?"

Use the last one most. It shows whether the learner understands the asymmetric cost of
merge versus split errors, which the whole technical track depends on.

</section>

<section class="section" markdown="1">

## Differentiation across the four personas

The site's four [learner personas]({{ '/avatars/' | relative_url }}) describe different
failure modes, and a session that works for one can fail another. A mixed cohort usually
has all four.

### Julian, first-generation undergraduate

**Predictable friction:** the hidden curriculum: the norms rather than the content.
Whether it is acceptable to say "I don't know", how to ask a question without appearing
under-prepared, what "read the paper" actually means in practice, whether their
uncertainty is normal.

**What to do:**
- **State norms explicitly, in the first five minutes, every time.** "In this session,
  'uncertain' is a passing answer and I will say so out loud when someone uses it well."
- Give a **worked example of the process**, not just the content: how you decided which
  paper to read first and what you skipped.
- Scaffold the first judgment heavily, then remove scaffolding fast. Under-challenge
  is as damaging as over-challenge here.
- Make office hours **scheduled and normal**, not available on request. "Optional"
  reads as "for people who are struggling" to a learner watching for signals.

### Maya, graduate student

**Predictable friction:** depth is uneven and she knows it. Strong on methods, less
secure on the biology, or the reverse, and reluctant to expose the gap in front of a
cohort.

**What to do:**
- Pair her with someone whose gap is complementary and make the pairing's purpose
  explicit, so exposure of a gap reads as the assignment rather than as a deficiency.
- Give her **teaching responsibility** for the part she is strong in. Explaining is the
  fastest route to consolidation, and this cohort member usually wants it.
- Push her toward the **assumption-naming** habit (Bin B claims, Unit 01). Learners who
  are strong at methods tend to be the ones who over-claim from them.

### Amir, AI scientist

**Predictable friction:** speed and vocabulary. Used to shipping; frustrated by the
pace and by biology terminology that seems arbitrary. Prone to assuming the biology is
a detail he can pick up later.

**What to do:**
- Front-load the [dictionary]({{ '/technical-training/dictionary/' | relative_url }}).
  Much of the apparent difficulty is vocabulary, and a week of it helps.
- Let him start at [Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
  or [Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
  where his systems intuitions transfer directly, then send him back to Units 05–07.
  Entry point order is negotiable; skipping 05–07 entirely is not.
- **Be direct about why the biology matters.** "A model trained on annotations from
  people who cannot distinguish an astrocytic process from a dendrite will learn to
  make that mistake at scale" lands better than an appeal to thoroughness.

### Dr. Linh Nguyen, assistant professor

**Predictable friction:** wants material she can hand to a trainee tomorrow, and has no
time to adapt it.

**What to do:**
- Point at the [teaching kits]({{ '/teaching/' | relative_url }}) and the rubrics rather
  than the reading. What she needs is the rubric and the run of show.
- The [technical units]({{ '/technical-training/' | relative_url }}) are written so that
  a trainee can work through one unsupervised and produce a reviewable artifact. That is
  the property she is looking for.

### Mixed-cohort rule

Do not differentiate by *content*. Differentiate by **scaffolding and entry point**,
holding the capability target constant. Everyone reaches the same competency check;
they arrive with different amounts of support and by different routes. Splitting the
target itself produces a two-tier cohort and is visible to everyone in the room.

</section>

<section class="section" markdown="1">

## Assessment that scales

### Grade the reasoning, not the answer

For every judgment task, the artifact is **label + confidence + evidence chain + one
alternative considered**. Grade the last three. A correct label with no evidence chain
should not outscore a well-reasoned incorrect one. Say so publicly at the start.

This also helps with scale: peers can review evidence chains against a rubric, whereas
they often cannot judge correctness at all.

### Calibration is the metric that matters

Track, per learner: accuracy overall, and **accuracy within their high-confidence
calls**. A learner at 84% overall with 100% accuracy on high-confidence calls and a
non-zero uncertain rate is performing better than one at 90% flat with no uncertain
calls, because the first learner's confidence carries information a team can act on.
These numbers are an illustration, not a benchmark.

Teach this explicitly. It runs against what conventional exams reward, and it transfers
to every judgment task in the track.

### Peer review, structured

Peer assessment scales, provided:
- The rubric is specific enough that two reviewers agree.
- Reviewers assess **evidence quality**, not correctness.
- You spot-check ~10% and publish the agreement rate between your marks and theirs. If
  peer marks diverge from yours, that is a rubric problem to fix, not a learner problem
  to complain about.

### Run a calibration round before the cohort matters

Have everyone score the same three items, then compare publicly before proceeding.
Expect a wide spread on the first attempt and a narrower one after a round of
discussion. **The narrowing is the learning.** It also shows why annotation protocols
need calibration sessions, which production proofreading teams run for the same reason.

</section>

<section class="section" markdown="1">

## Running without live instruction

Much of the intended audience will work through this material alone. Design for it.

**A self-study path that works:**

1. Read the unit's *Before you start* and *What you'll be able to do*.
2. Read the numbered sections, attempting each **Check yourself** before opening the
   answer. Opening it first converts a retrieval exercise into re-reading, which feels
   productive and is not.
3. Do the lab. Produce the artifact.
4. Self-grade against the rubric, honestly, then find one person to review the artifact:
   a peer, a mentor or a lab-mate. **One external review is worth more than three
   self-reviews**, because self-assessment cannot see the thing you did not know to
   check.
5. Log which rubric row you scored lowest on and target it in the next unit.

**What a lone learner cannot get from the page**, and should seek deliberately:
calibration against other people's judgments, and exposure to genuinely ambiguous
cases someone has curated. Both are reasons to join a journal club or a community
proofreading effort, and it is worth telling learners that directly rather than
implying the reading is sufficient.

</section>

<section class="section" markdown="1">

## Failure modes specific to this material

**Lecturing the perceptual units.** Units 05–07 taught as lectures produce learners who
can describe cues and cannot apply them. Convert at least half the time to scored drills
on short z-stacks.

**Single-image practice.** Any ultrastructure or glia exercise built from single images
teaches the single-plane call, a habit the units explicitly tell learners to break. Always use short z-stacks, even when it is more work to prepare.

**Clean examples only.** A curated set of unambiguous patches produces overconfidence
that collapses on real data. Every drill needs ambiguous cases, and at least one case
where the correct answer is "this is a segmentation error, not a biological structure".

**Rewarding speed.** If throughput is what you praise, throughput is what you get, with
accuracy quietly falling. Praise well-justified uncertainty at least once, early, and
visibly.

**Skipping the null-model discussion in Unit 09.** It is the least visual section and
the easiest to skip, and a wrong null is one of the commonest ways a motif claim goes
wrong. If you must cut something from Unit 09, cut the survey in §4, "Beyond motifs", not
the worked reciprocity example in §2.

**Treating the labs as homework.** The labs *are* the curriculum. The reading exists to
make the labs possible. A cohort that does the reading and skips the labs has not done
the course.

</section>

<section class="section" markdown="1">

## Preparation checklist

Before a session, confirm:

- [ ] You can state the capability target in one sentence without reading it.
- [ ] You have **one** worked example you will narrate, including where you are unsure.
- [ ] Your practice set includes ambiguous cases and at least one trap.
- [ ] Practice items are z-stacks, not single images, for any perceptual unit.
- [ ] The rubric is visible to learners **before** they start, not after.
- [ ] You know the two or three misconceptions this unit names, and how you will surface them.
- [ ] You have decided what "uncertain" earns, and you will say so out loud.
- [ ] Data access works (accounts, viewer, notebook), checked today, not last week.

</section>

<section class="section" markdown="1">

## Where to find materials

</section>

<section class="section">
  <div class="resource-card">
    <div class="resource-links">
      <a class="resource-link" href="{{ '/teaching/sessions/' | relative_url }}">Session kits, one page per module</a>
      <a class="resource-link" href="{{ '/teaching/' | relative_url }}">Teaching Hub</a>
      <a class="resource-link" href="{{ '/technical-training/' | relative_url }}">Technical course units</a>
      <a class="resource-link" href="{{ '/technical-training/slides/' | relative_url }}">Technical slide plans</a>
      <a class="resource-link" href="{{ '/modules/slides/' | relative_url }}">Module slide pages</a>
      <a class="resource-link" href="{{ '/technical-training/dictionary/' | relative_url }}">Connectomics Dictionary</a>
      <a class="resource-link" href="{{ '/content-library/' | relative_url }}">Content library, instructor-depth reference</a>
      <a class="resource-link" href="{{ '/datasets/access/' | relative_url }}">Dataset access and starter notebooks</a>
      <a class="resource-link" href="{{ '/avatars/' | relative_url }}">Learner personas</a>
    </div>
    <p><strong>Artifact directories:</strong> <code>course/decks/marp/out/modules/</code> for rendered decks and <code>assets/worksheets/moduleNN/</code> for worksheets.</p>
  </div>
</section>

</div>
