---
layout: page
title: "Reading and Judging a Paper"
description: "What 'read the paper' actually means at each career stage, the order experts read in, how to read a methods section for what is absent, and how to judge fragility and disagree proportionately."
permalink: /hidden-curriculum/reading-and-judging/
track: career-and-community
pathways:
  - hidden curriculum
content_type: core
---

## Why this page exists

"Read this paper" is the most frequent instruction in research training and the least
specified. Nobody says which of the four quite different activities they mean, how long
it should take, or what you should be able to do afterwards. People who grew up around
academics tend to guess correctly. Everyone else reads front to back, highlights a lot,
takes four hours, arrives at the meeting able to summarise and unable to judge, and
concludes they are slow.

They are not slow. They were given an underspecified instruction and no one noticed.

This page specifies it.

---

## What "I read the paper" means, by stage

| Stage | "I read it" means | Budget | You should be able to |
|---|---|---|---|
| First exposure | You can state the question, the headline claim, and one thing you did not understand | 30–45 min | Ask one specific question in journal club |
| Early graduate | Plus: the measurement with its units, the n and *n of what*, and the comparison the claim is against | 1–2 h | Say whether the figure shows what the abstract says |
| Senior graduate / postdoc | Plus: which single figure carries the claim, what would have to be true for it to be wrong, and one thing the methods do not state | 2–3 h, methods and one supplement | Reproduce the analysis in principle, and name its weakest joint |
| Reviewing | Plus: methods checked against every figure, arithmetic spot-checked, and a written list of what is missing | 4 h and up | Write a review that the authors can act on |

**Nobody tells you which rung they mean, because they are asking from the rung they
stand on.** A PI who says "have a look at this" over lunch usually means rung one. The
same PI saying it about the paper that scooped your project means rung three.

Ask. It is a one-line question that saves you two hours or saves you an embarrassment:

> "Do you want me to be able to discuss the result, or to be able to check it? I'll
> budget differently."

The clause that does the work is *"I'll budget differently"*. It converts the question
from a request for reassurance into a scheduling question, which is a register senior
people answer without thinking twice about you.

---

## The order experts actually read in

Not front to back. Front to back is how you read a textbook, and a paper is not a
textbook — it is an argument with the evidence stored in the middle.

1. **Title, then the last two sentences of the abstract.** That is the claim. Write it
   down in your own words before reading anything else. Two minutes.
2. **All figures and captions, in order, ignoring the body text.** Ten to fifteen
   minutes. Then answer one question: *which single figure carries the headline claim?*
   Everything else in the paper is scaffolding for that figure.
3. **The last paragraph of the introduction** (what they say they did) **and the first
   paragraph of the discussion** (what they say they found). Compare both against what
   you got from the figures. **Any gap between those three is the paper's soft spot**,
   and it is where every good journal club question comes from.
4. **The methods for the key figure only.** Not all the methods. The ones that produced
   the figure you identified in step 2.
5. **The results text for the key figure only.**
6. **Everything else, only if you still care.** Most of the time you will not, and that
   is the correct outcome.

**What to skip on a first pass, deliberately and without guilt:** the introduction's
literature review, the related-work survey, the discussion's speculation about
implications, and the entire supplement unless step 4 sent you into it with a specific
question.

**When to stop entirely.** If after step 2 you cannot state the claim, the problem is
usually vocabulary rather than reasoning. Go to the
[Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }}), fix
the three words, and return. Vocabulary gaps are cheap to close and they masquerade
convincingly as conceptual gaps — an experience common enough that the
[Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }}) treats it as a
named persona friction rather than an individual failing.

---

## Reading the methods for what is *not* there

The methods section is the only part of a paper where an omission is load-bearing. A
result section overstates by choosing words; a methods section overstates by leaving
something out.

Read it with a checklist of absences. For connectomics, these are the ones that matter,
and each is the reader-side version of a norm from
[Technical practice]({{ '/hidden-curriculum/technical-practice/' | relative_url }}):

| If you cannot find… | Then you cannot conclude… | Note to write |
|---|---|---|
| A materialization version or timestamp | That the numbers are reproducible at all | "Unpinned — cannot be re-derived" |
| An n, or an n *of what* | Anything about generality | "n = 10,000 synapses from 1 volume from 1 animal" |
| A proofreading level with written criteria | Whether a low connection count is biology or incompleteness | "Completeness unstated" |
| A named null model | That an enrichment is enrichment | "Null unstated — effect size uninterpretable" |
| A synapse threshold | That the graph density is comparable to anything | "Threshold unstated" |
| Inclusion criteria and boundary handling | That the cohort is not the finding | "Cohort selection unstated" |
| An exclusion or failure rate | That the tail was handled rather than dropped | "No exclusion rate" |
| A count of tests and a correction | That a significant result is not one of sixteen | "Tests uncounted" |
| An error rate, or its propagation | That the effect exceeds the reconstruction's own noise | "No error propagation" |

**Absence is not fraud.** Most of these omissions are inherited defaults, written by
tired people against a deadline, in fields where nobody was ever told either. Treat an
absence as a *bound on what you may conclude*, not as an accusation. The correct
response is almost always a question, not a verdict — see the disagreement ladder below.

**The specific trap in this field.** "Data available on request" plus a public dataset
name is not the same as a reproducible analysis. The public dataset changes underneath
the paper as proofreading continues, so a paper naming a dataset without naming a
version has told you the ingredient and not the recipe. This is not a hypothetical:
[Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
calls unpinned analysis the number-one reproducibility failure in connectomics, and it
is silent — the code runs, it just answers a different question than it did last week.

---

## Strong or fragile: four questions

Ask these in order. Any one of them can end the assessment.

### 1. What is the null, and what is the uninteresting explanation?

Write out, in words, the sentence *"a boring reason this pattern could appear is…"* If
the paper does not let you write it, the effect size means nothing yet.

[Unit 09 §2]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
carries the site's clearest worked demonstration of this, and it is worth doing by hand
once. In its illustrative example, 100 neurons with 1,200 edges and 210 reciprocal pairs
give **2.9-fold enrichment** under an Erdős–Rényi null, **1.4-fold with z = 5.0** under a
degree-preserving null, and **1.14-fold, not significant** once the empirical
distance–probability curve is preserved as well. Nothing about the data changed. Roughly
two-thirds of the apparent effect was degree heterogeneity, and most of the rest was
spatial proximity.

So: a connectomics paper reporting motif or reciprocity enrichment against an
Erdős–Rényi null has reported almost nothing. This is common in older literature and it
is the single highest-yield check a beginner can run.

### 2. What is n, and n of *what*?

Volume EM invites a specific error. A dataset containing ten thousand annotated synapses
from one volume from one animal is not n = 10,000 for any claim about a species, a cell
type, or a cortical area. It is n = 1 for the animal, n = 1 for the preparation, n = 1
for the staining protocol, and possibly n = 1 for the segmentation model.

Ask which level of that hierarchy the claim is pitched at, and whether the reported n
matches it. Papers are usually honest about the number and silent about its level.

### 3. What would have been reported if it had failed?

Imagine the negative version of this paper. If you cannot picture it being written,
submitted and published, the result is weakly evidenced regardless of its p-value —
because you are looking at a filter, not a measurement.

The follow-up question is sharper: *was a check run that could have killed this?* An
error-sensitivity simulation, a second synapse threshold, a stronger null, a held-out
region. A paper that reports a check it might have failed is telling you something about
the authors that the result itself cannot.

### 4. Does the effect survive the authors' own stated error rate?

If the methods state a merge and split rate — many do — and the analysis does not
propagate it, do the reasoning yourself. Two asymmetries from the technical track make
this quick:

- **Merge errors inflate dense motifs superlinearly**, because one merge fuses two
  partner lists and manufactures triangles that never existed
  ([Unit 01 §4]({{ '/technical-training/01-why-map-the-brain/' | relative_url }})).
- **Direction errors push reciprocity measurements upward**, because a flipped edge both
  removes a true edge and adds a false reverse one
  ([Unit 06 §4]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }})).

Both biases point toward the more interesting answer. So for any claim about dense
motifs or reciprocity, an unpropagated error rate is not conservative — it is biased in
the direction of the paper's conclusion.

### The triage, compressed

| Reads as strong | Reads as fragile |
|---|---|
| Null stated in words and justified; result reported under more than one | Null unstated, or Erdős–Rényi |
| Headline re-run at a second threshold, with the difference reported | One threshold, no sensitivity |
| Error rate measured and propagated into a band on the effect size | Error rate mentioned in discussion, absent from the analysis |
| Per-cell completeness or proofreading level reported | "Proofread" as a binary, or unmentioned |
| An explicit non-claim in the discussion | Abstract claims a mechanism the measurement cannot reach |
| Number of tests reported and corrected | One significant class of sixteen, siblings unmentioned |
| n stated at the level the claim is pitched at | Large n from a single specimen |

Three or more fragile rows and the result is a hypothesis, not a finding. That is a
perfectly respectable thing for it to be — say so in those words rather than dismissing
it.

---

## How to disagree proportionately

Most bad disagreement in research is not wrong, it is **mis-sized**: a level-one
observation delivered as a level-four accusation, usually because the speaker was
nervous. Match the claim, the evidence and the venue.

### Level 1 — "I couldn't tell from the methods whether…"

The cheapest and most useful move in existence, and the one almost everyone
under-produces. It is a statement about the paper, not about the authors, and not about
you.

> "I couldn't tell from the methods which materialization version this was run against.
> If it was pinned, the timing question I had goes away."

The second sentence is the important one: it shows you have thought about what the
answer would change. Without it the question reads as box-ticking; with it, it reads as
engagement.

**Venue:** anywhere. Journal club, lab meeting, a conference poster, an email to the
authors. Level 1 is always in season.

### Level 2 — "The framing goes further than the measurement"

The abstract makes a Bin C claim; the results contain a Bin A measurement. This is the
most common defect in connectomics writing and it is usually a writing failure rather
than an analysis failure.

> "The measurement here is where feedback input lands on the dendritic tree, which is
> solid. The abstract says these synapses carry prediction error, and I don't think
> anything in the paper reaches that. Am I missing a figure?"

*"Am I missing a figure?"* is not false modesty. It is the clause that keeps the
conversation about the paper if you are right, and saves the exchange if you are wrong.

**Venue:** journal club, lab meeting, a review. Not a public post about a named author.

### Level 3 — "This is under-specified in a way that could change the conclusion"

You now owe a direction. Saying "this could be affected by merge errors" is a level 1
question wearing a level 3 coat. Saying "merge errors bias dense motif counts upward,
and the reported rate is high enough that I'd want the error band before believing the
effect size" is a level 3 claim.

> "The motif enrichment is against a degree-preserving null, which is the right minimum.
> But soma positions are available in this dataset, and reciprocal partners are
> disproportionately near neighbours, so I'd expect a distance-preserving null to reduce
> the effect — possibly to nothing. I think this is a question the authors could settle
> in an afternoon."

The last sentence is deliberate. It states the cost of resolving your objection, which
is what determines whether anyone acts on it.

**Venue:** a review, an email to the authors, a comment on a preprint. Say it to the
authors before you say it to a room.

### Level 4 — "The analysis is wrong"

This requires arithmetic you have actually done and can show, and it is worth the
seriousness it demands. Write it down, with numbers. Show it to one person who will look
for the flaw in *your* reasoning first.

**Venue:** in writing, with the working attached, to the authors, before anywhere else.

### The rules that hold across all four levels

- **State the strongest version of their claim before you disagree with it.** One
  sentence. It is the single most reliable way to make a junior objection land with a
  senior audience, and its absence is the most common reason a correct objection gets
  dismissed.
- **Never move up a level because you are annoyed, and never move down one because the
  authors are eminent.** Both happen constantly; both are visible to everyone in the
  room except the person doing it.
- **Keep disagreement about a result separate from disagreement about a person.** They
  are different acts with different consequences, and conflating them is how a defensible
  technical objection becomes a reputational problem for the objector.
- **The asymmetry is real.** A junior researcher's level 4 objection against a
  well-resourced group will be scrutinised harder than the same objection from a
  professor, and that is unfair. The workable response is not to lower your standards for
  the claim but to raise your standards for the write-up: numbers attached, one reader
  first, no adjectives.

---

## Journal club, used properly

The site's [Journal Club]({{ '/technical-training/journal-club/' | relative_url }}) is
200 papers, each with an OCAR summary — Opportunity, Challenge, Action, Resolution,
Future Work — level-tiered summaries, and discussion prompts.

Use it like this:

- **Bootstrap vocabulary with the tiered summary, then read the paper.** The summaries
  are a ramp, not a substitute; reading the advanced summary and skipping the paper
  produces exactly the confident-but-uncheckable state this page exists to prevent.
- **Read the OCAR *Resolution* field, then go and test it with the four questions
  above.** Resolution is where a summary is most likely to inherit a claim the paper did
  not establish, which makes it the ideal place to practise.
- **Prepare in 45 minutes**, not three hours: the reading order (steps 1–3), one absence
  from the methods checklist, and one of the four fragility questions with an attempted
  answer. That is a fuller preparation than most people in the room will have done.
- **Bring the level 1 sentence every time.** "I couldn't tell from the methods whether X"
  is never a stupid contribution, because it is a claim about the document.

If you are running a journal club: assign the four fragility questions to four people
rather than assigning a presenter. The presenter format produces a summary; the question
format produces a judgement, which is the capability being trained.

---

## Two smaller cases

**Preprints.** Read them the same way, and note the one real difference: nobody has yet
had an incentive to ask the level 3 question. That makes preprints excellent material for
practising on and poor material for citing as settled. Say "preprint" out loud when you
cite one in a meeting.

**Papers outside your subfield.** Steps 1–3 still work; step 4 will not, because you
cannot detect an absence in a methods section whose conventions you do not know. The
honest position is *"I can tell you what they claim, I can't tell you if it's solid"* —
which is a useful thing to be able to say precisely, and far better than the two common
alternatives of silent over-trust and vague suspicion.

---

## Related

- [The Hidden Curriculum hub]({{ '/hidden-curriculum/' | relative_url }})
- [Technical practice]({{ '/hidden-curriculum/technical-practice/' | relative_url }}) —
  the same norms from the writing side
- [Lab norms]({{ '/hidden-curriculum/lab-norms/' | relative_url }}) — how meetings and
  journal clubs actually work as social events
- [Conflict]({{ '/hidden-curriculum/conflict/' | relative_url }}) — when a disagreement
  stops being about the paper
- [Unit 09: Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}) —
  null models, motif analysis, error sensitivity
- [Unit 01: Why Map the Brain]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}) —
  the Bin A / B / C claim discipline used throughout this page
- [Journal Club]({{ '/technical-training/journal-club/' | relative_url }}) and the
  [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- [Network analysis methods]({{ '/content-library/connectomics/network-analysis-methods/' | relative_url }})
