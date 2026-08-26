---
layout: page
title: "Technical Practice: The Norms Nobody States"
description: "Twenty-six reporting and disclosure norms that careful connectomics practitioners follow silently — each named, with who it is invisible to, what its absence looks like, and the unit that teaches it."
permalink: /hidden-curriculum/technical-practice/
track: career-and-community
pathways:
  - hidden curriculum
content_type: core
---

## What this page is

The [technical track]({{ '/technical-training/' | relative_url }}) teaches twenty-six
professional norms without stopping to call them that. They arrive as connectomics
advice — pin the materialization version, name the assumption, report the threshold — so
a reader who does not already speak the professional register files them under "things
about connectomics" and carries none of them anywhere else.

They are not really about connectomics. They are the norms that decide whether a senior
reader looks at your figure and extends you credit, or looks at it and quietly stops
relying on your numbers. Nobody will tell you which happened.

Each unit now ends with a short *"the norm behind this unit"* section naming its own
one or two. This page is where they are collected. Each entry gives the norm as a
sentence, who it is invisible to and why, what its absence looks like in real work, and
where to go for the technique underneath it.

**Almost every one costs under a minute at the time and is unrecoverable later.** That
asymmetry is why they are norms rather than preferences.

---

## Family 1 — Say what you ran it on

### 1. An object ID without a version or a timestamp is not a result

Root IDs change every time a proofreader merges or splits. The same query, the same
code, a different week, a different answer — and nothing errors.

**Invisible to whom.** Anyone who learned data analysis on static files. If your entire
prior experience is a CSV that does not change while you look at it, the idea that the
identifier itself is mutable is not a fact you forgot; it is a category you do not have.

**Absence looks like.** A figure caption with neuron IDs and no version. A collaborator
who cannot reproduce your number and assumes one of you made an arithmetic error. Six
months of notebooks that can never be re-run against the state they were written for.

**Do this.** Print available materialization versions, pin one, and put the version, the
query code, and the date in the notebook header *and* the figure caption.
[Unit 04 §2]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }});
[provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}).

### 2. When you carry IDs forward, report the churn

Mapping a six-month-old ID list onto the current segmentation produces one-to-many and
many-to-one mappings wherever proofreading happened.

**Invisible to whom.** Anyone who has not yet been handed a stale ID list — which is
everyone, exactly once.

**Absence looks like.** A silent partial resolve. Some IDs map, some vanish, some
resolve to something that is no longer the cell you meant, and the analysis runs to
completion on a set whose composition changed underneath it.

**Do this.** Map through the lineage service and report how many IDs mapped 1:1, how
many split, how many merged. That count is a direct measurement of how much proofreading
changed the objects your conclusion rests on, and it belongs in the methods. If the
original result must be reproduced exactly, query the old version instead of mapping
forward.
[Unit 04 §2]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}).

### 3. A graph is a versioned artifact with recorded parameters, not a script someone ran once

Two people can build 400-node graphs from the same dataset and get 5,000 and 1,800
edges, with neither of them having made an error.

**Invisible to whom.** Anyone whose training used datasets that arrived pre-built. If
the graph was always given to you, the six decisions that produced it never surfaced as
decisions.

**Absence looks like.** "How many edges does your graph have?" being treated as a
question about biology rather than about parameters, for several meetings.

**Do this.** Record all six construction decisions — synapse-detection confidence,
synapse threshold, weighting, direction, inclusion criteria, boundary handling — in a
config block at the top of the notebook, and publish them with the graph.
[Unit 09 §1]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }});
[graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }}).

### 4. Provenance is a pipeline stage with its own tests, not a README

If the acquisition log is not machine-readable, it does not exist.

**Invisible to whom.** Anyone who has not yet had to ask a forensic question. The value
of per-tile timestamps only becomes obvious the first time you need to know whether a
defect follows block position or acquisition time, and by then it is too late to have
recorded them.

**Absence looks like.** An anomaly nobody can diagnose, six months on, because the only
record of who ran what and when is in a spreadsheet with three inconsistent date
formats. Also: no way to roll back a bad batch, and no way to detect one annotator's
drift.

**Do this.** Emit provenance — who, when, what, and where possible why — as structured
data from every stage, and test it like code.
[Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
and [Unit 03 §3]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}),
which also covers machine-readable defect masks that reach annotators in the viewer.

### 5. Archive the next-richer representation

Decide which representation your endpoint metric requires before the pipeline runs, then
keep the one above it.

**Invisible to whom.** Anyone who has never been asked a reviewer question they could
not answer. Storage looks like a cost until the moment it is the difference between an
afternoon and re-running a pipeline.

**Absence looks like.** A team exports a connectivity graph, finds a motif enrichment,
and is asked whether spatial proximity explains it. The graph has discarded all
geometry, so the question cannot be answered without re-running from skeletons.

**Do this.** Archiving skeletons alongside a graph costs a few gigabytes and prevents
exactly that. [Unit 02 §3]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }})
has the representation table and what each one discards.

---

## Family 2 — Say what you are assuming, in the same sentence

### 6. Name the assumption in the same sentence as the claim

Asymmetric synaptic morphology predicts glutamatergic transmission well, and is still an
assumption with known exceptions. So the claim is not "excitatory".

> *"Putatively excitatory (asymmetric morphology)" costs four words.*
> — [Unit 01 §3]({{ '/technical-training/01-why-map-the-brain/' | relative_url }})

**Invisible to whom.** Anyone trained to write confidently. Years of schooling reward
the assertive sentence and penalize the hedged one; scientific writing inverts that, and
nobody announces the inversion. A first-generation researcher who has been told
throughout their education to "be more confident in your writing" is following the last
instruction they were given.

**Absence looks like.** A results section that is defensible and an abstract that is
not, because the qualifier was dropped somewhere between them. Reviewers read that as
carelessness rather than as inheritance.

**Do this.** Sort every claim into Bin A (structure alone establishes it), Bin B
(structure plus one declared assumption), or Bin C (structure cannot establish it).
Every Bin B claim carries its assumption in the same sentence or in the caption. Writing
"excitatory" instead is not a shorthand; it is a different claim.
[Unit 01 §3]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}), drilled
in [Unit 05 §2]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}).

### 7. Write the sentence you are *not* claiming

Explicitly, in the paper, next to the result.

**Invisible to whom.** Everyone reading their way into a field, because a non-claim is
by definition absent from the literature unless someone chose to write it. You can read
two hundred papers and never see the move performed except by people who were taught it
privately.

**Absence looks like.** A Bin C sentence in the abstract supported by a Bin A
measurement in the results — the most common failure in connectomics writing.

**Do this.** For every headline result, write one sentence of the form *"These data do
not establish X, and they do not establish Y."* Reviewers read it as confidence rather
than as weakness, which is exactly the fact nobody passes on. It is step 4 of Unit 01's
question repair and the closing line of Unit 09's lab report.

### 8. Size the claim to the reconstruction you actually have

"Cell X synapses onto cell Y" needs both partners proofread through the synapse. "Cell X
has n inputs" needs a closed dendritic arbor. "Type A prefers type B" needs both target
populations proofread to *comparable* completeness.

**Invisible to whom.** Analysts downstream of the reconstruction. If the data reached
you as a table, reconstruction state is not a column in it, so it is not a variable you
are thinking about.

**Absence looks like.** Differential completeness masquerading as biological preference:
two populations proofread with different effort, every difference between them
confounded with that effort, and the confound invisible in the table.

**Do this.** Use the claim-type table in
[Unit 01 §4]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}) *before*
writing the claim. Match proofreading protocol before comparing populations.

### 9. Prefer ratios to absolute counts when comparing

A ratio between comparably reconstructed populations quietly controls for a great deal
of reconstruction bias. Absolute counts are sensitive to completeness; ratios are much
less so.

**Invisible to whom.** Anyone who has not yet been burned by a completeness confound. It
is a habit experienced people reach for automatically and never explain, because to them
it is not a decision.

**Absence looks like.** A per-cell input count compared across two populations, with the
difference driven by how thoroughly each was traced.

**Do this.** When the question permits it, frame the endpoint as a ratio or a fraction
rather than a count, and say why you did.
[Unit 01 §3]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}).

---

## Family 3 — Report what you did not report

### 10. Report how many tests you ran, including the ones you did not report

A triad census is sixteen tests. At α = 0.05 you expect roughly one false positive by
chance.

**Invisible to whom.** Everyone, structurally — the tests nobody reported are by
construction absent from every paper you could learn the norm from. It transmits only by
a supervisor saying it out loud, which is precisely the mechanism that distributes
unevenly.

**Absence looks like.** A single significant motif class reported as *the* finding, with
fifteen silent siblings. And the slower version: trying nulls until one gives
significance, which no correction applied afterwards can repair.

**Do this.** State the number of tests and the correction. Prefer permutation inference,
because triad counts are strongly dependent and analytic p-values overstate confidence.
Report every null you tried, not the one that worked.
[Unit 09 §3]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}).

### 11. State the threshold, and re-run the headline result at a second one

The synapses-per-connection distribution is heavy-tailed and single-synapse connections
usually dominate by count, so a threshold of ≥ 1 versus ≥ 3 can remove more than half
your edges — non-uniformly across cell types.

**Invisible to whom.** Anyone who inherited a working pipeline. A default in someone
else's config file does not present itself as a scientific choice.

**Absence looks like.** A density difference between two labs' graphs, discussed as
biology.

**Do this.** Report the threshold. Re-run at a second one and report what changed.
**If the conclusion flips, that is the finding.**
[Unit 09 §1]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}).

### 12. State the inclusion criteria — either choice is defensible, neither is defensible silently

Include only well-proofread cells and you have conditioned on a variable correlated with
cell size, position and type. Include everything and you have mixed completeness levels.

**Invisible to whom.** Anyone who experiences this step as data cleaning. It feels like
tidying, so it happens before the analysis notebook starts and never appears in it.

**Absence looks like.** A methods section describing the statistics in detail and the
cohort in one clause.

**Do this.** Write the inclusion rule as a sentence, put it in the config block, and
state which of the two biases you accepted and why.
[Unit 09 §1]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}).

### 13. Report the proofreading level of the cells the result rests on

Not proofread/not-proofread — a level, with written criteria a second annotator would
apply the same way.

> *"A result that does not is uninterpretable, because the reader cannot tell whether a
> low measured connection count reflects biology or incompleteness."*
> — [Unit 08 §4]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})

**Invisible to whom.** Analysts who have never proofread. If you have not watched a
cell's input count change after fixing three errors, "proofreading level" reads as
project management rather than as a term in your result.

**Absence looks like.** A per-cell input count reported with a standard error and no
statement of completeness: a precise number of unknown accuracy. Almost no published
analysis includes it, which is exactly why including it gets noticed.

**Do this.** Carry level as per-cell metadata, filter analyses by required level, and
state the level and its criteria in the methods. To make it concrete for yourself, do
Unit 08's lab: count a neuron's inputs, fix its three highest-impact errors, recount.

### 14. A stated exclusion rate is honest and cheap; an unbudgeted tail is neither

Proofreading time per neuron is heavy-tailed. Budget from the median and the shortfall
arrives at the end of the project, when it does the most damage.

**Invisible to whom.** Anyone who has never held a budget. Trainees are usually
protected from the money, so the tail arrives as a mysterious project-wide panic rather
than as a forecasting error someone could have avoided.

**Absence looks like.** A half-corrected volume, no defensible reporting, and a methods
paragraph that cannot say what was left out because nobody tracked it.

**Do this.** Define the stopping rule so pathological cells are excluded *by policy*
after a stated time cap, and report the exclusion rate. Estimate from the mean, on a
sample large enough to contain tail cases.
[Unit 08 lab]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}).

### 15. Report distributions with the maximum, never a global mean

A mean registration residual of 3 µm over a whole volume can hide a 40 µm failure in one
corner.

**Invisible to whom.** Anyone whose statistical training emphasized summary over
structure. A mean is the socially expected number to report, and it is the wrong one
whenever the failure is local — which, in volume EM, it usually is.

**Absence looks like.** Functional traces assigned to somata in a region where the
transform silently extrapolates. Or four consecutive lost sections and four scattered
lost sections reported as the same headline number, despite having entirely different
consequences.

**Do this.** Report a residual map, or per-region distributions with the maximum. Same
for stitching and section-to-section alignment residuals, and for defect counts: the
distribution, not the count.
[Unit 02 §4]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }}) and
[Unit 03 §3]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}).

### 16. Separate data loss from labor when you report quality

A *labor* artifact means the reconstruction will be correct eventually, after paying
for it in proofreading hours. A *data loss* artifact means some biological question is
permanently unanswerable in that region.

**Invisible to whom.** Anyone who has only ever consumed a quality score. One number
looks more decision-ready than two, so the distinction gets averaged away by exactly the
person who most needed it.

**Absence looks like.** A QA report with a single quality score, which conceals the only
distinction the project actually needs — "expensive to fix" versus "unanswerable
forever".

**Do this.** Use the two cost classes from
[Unit 03 §2]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }})'s
artifact table and report them separately. Report error rate by region and by process
calibre too; it is never uniform.

---

## Family 4 — Make your uncertainty carry information

### 17. Negative calls are data. An annotator who never says "no" is not calibrated

The correct output for a dark thickening with no vesicle cluster that vanishes on the
adjacent section is *not a synapse* — plus a logged uncertain patch that enters the
calibration set.

**Invisible to whom.** Everyone who has been assessed by examination. For fifteen years
a blank has been worth zero and a guess has had positive expected value. Nobody
announces that the payoff matrix changed on the first day of research, and learners
suppress uncertainty because they read it as failure.

**Absence looks like.** An annotator with a 0% uncertain rate and high throughput, whose
confidence tells a downstream analyst nothing at all.

**Do this.** Produce label + confidence + evidence chain + one alternative considered.
Log ambiguous patches into the calibration set instead of resolving them silently. Track
your accuracy *within your high-confidence calls*: 84% overall with 100% on
high-confidence calls beats 90% flat with no uncertain calls, because the first person's
confidence is actionable.
[Unit 05 §2]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }});
assessed this way in the
[Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }}). If you
facilitate: say out loud, once and early, that well-justified uncertainty earns credit.

### 18. Two cues from different families, or it is not high confidence

Three observations that share a failure mode are one observation. Microtubule count and
cytoplasmic density both degrade under poor staining; vesicle presence and vesicle shape
fail together.

**Invisible to whom.** Anyone who has been taught to accumulate evidence without being
taught to check it for independence. Adding a third correlated cue *feels* like getting
more certain, and the feeling is the problem.

**Absence looks like.** A confident call in a weakly stained region built entirely from
staining-dependent cues — the single most common reasoning error in annotation.

**Do this.** Use the five independent families — geometry, organelle content, synaptic
role, neighborhood context, long-range continuity — and require two from different
families before calling high confidence. The rule's real value is that it is
*checkable*: a reviewer can look at an evidence chain and see whether it draws on one
family or two.
[Unit 05 §4]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}).

### 19. Report confidence per call, then re-run the headline on high-confidence calls only

**Invisible to whom.** Anyone who thinks of confidence as a private feeling rather than
as a column in a table. If it is not recorded per item, this check is not available
later, and nobody tells you to record it at the time.

**Absence looks like.** An effect that rests entirely on the ambiguous calls, and no way
to find out.

**Do this.** Record confidence per call. Re-run the headline analysis on the
high-confidence subset. If the effect survives, say so. If it does not, you have learned
the most important thing about your result — and reporting *that* is what marks a
careful analyst.
[Unit 06 §4]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }}).

### 20. Run the error-sensitivity check, and report the band even when it crosses the null

Take your own measured merge and split rates, perturb the reconstructed graph at those
rates a hundred times, recompute the statistic, report the spread as an error band.

**Invisible to whom.** Anyone who has not watched a senior person do this and survive.
Nobody volunteers a check capable of killing their own result until they have seen it
modeled, which makes this norm almost purely a function of who supervised you.

**Absence looks like.** A clean effect size with no band, and a reviewer who runs the
check mentally and stops believing the paper.

**Do this.** It is a few dozen lines of code and one of the strongest things you can put
in a supplement. Note the asymmetry that makes it urgent: merge errors inflate dense
motifs superlinearly, and direction errors push reciprocity measurements *upward*. The
bias points at the interesting answer, which is the worst possible property for an error
to have.
[Unit 09 §3]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
and [Unit 06 §4]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }}).

---

## Family 5 — Commit before you look

### 21. Write the null in words before you choose one

The null is a statement of what would count as an *uninteresting* explanation. Choosing
it is the scientific step; running the test is bookkeeping.

**Invisible to whom.** Anyone whose statistics training came through software. The
library supplies a default, the default returns a p-value, and a p-value looks like an
answer, so no decision appears to have been taken.

**Absence looks like.** Unit 09's reciprocity example, the clearest demonstration of
fragility on this site. In its illustrative figures, the same 210 reciprocal pairs
support "2.9-fold enrichment" under Erdős–Rényi, "1.4-fold, z = 5.0" under a
degree-preserving null, and "no detectable effect" once distance is preserved as well.
Nothing about the data changed.

**Do this.** Write the sentence *"the uninteresting explanation for this would be…"*
before selecting a null. If you cannot write it, you do not yet know what you are
testing. Preserve everything you are not asking about. Pre-register the null, or report
the result under all three.
[Unit 09 §2]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }});
[motif analysis]({{ '/content-library/connectomics/motif-analysis/' | relative_url }}).

### 22. State the stopping rule in advance, so that someone who is not you could check it

"Keep going until it looks good" has no termination condition and no defensible
reporting.

**Invisible to whom.** Anyone whose prior work had deadlines rather than completion
criteria. If everything you have ever done stopped when it was due, "how will we know we
are finished?" is not a question you have needed.

**Absence looks like.** Effort spent where it was most conspicuous rather than where it
mattered, and a project that stops when the money does.

**Do this.** Prefer a convergence rule — *"stop when a second independent pass over a
20-cell sample changes the endpoint metric by less than 5%"* — because it directly
measures whether more effort would change the answer. Design the stopping rule and the
budget together, not sequentially.
[Unit 08 §4]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}).

### 23. Pilot the whole pipeline before you commit the spend

Take a sub-volume on the order of 100 × 100 × 100 µm through align, segment, skeletonize
and human proofreading, and measure the error rate.

**Invisible to whom.** Anyone who has never been responsible for a capital cost. A pilot
looks like delay if you are not the person who will discover, after acquiring a
petabyte, that the staining protocol produces a merge rate the segmentation cannot
handle.

**Absence looks like.** A dataset that cannot be reconstructed and cannot be reacquired.
Unit 03 calls skipping it the most expensive habit in the field.

**Do this.** Budget 1–2% of the project for the pilot, and run it *while you can still
change the protocol*.
[Unit 03 §3]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}).

---

## Family 6 — Spend effort where it changes the answer

### 24. Rank by effect on the endpoint, not by how obvious the error looks

A small glia–neuron merge routinely outranks a large, conspicuous split.

**Invisible to whom.** Anyone who has only ever been assessed on effort. Fixing the
visible thing feels like work and reads like diligence; fixing the invisible expensive
thing looks, from outside, like doing less.

**Absence looks like.** A queue built by eye, in which the errors that most corrupt the
result are the ones nobody noticed. An astrocytic process fused to a dendrite adds
inputs the neuron never had, and adds them *locally*, so a motif analysis sees enhanced
clustering and a distance analysis sees inflated short-range connectivity — again in the
interesting direction.

**Do this.** Score candidates on a written rubric combining effect on the endpoint
metric, path centrality, and cost to fix; then audit a sample of your own decisions
against it.
[Unit 08 §4]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
and [Unit 07 §1]({{ '/technical-training/07-glia/' | relative_url }});
[proofreading strategies]({{ '/content-library/proofreading/proofreading-strategies/' | relative_url }}).

### 25. Measure what your correction pass did to the endpoint, once, and reuse the number

Recompute per-neuron input counts and dendritic length before and after a correction
pass on a sample. *"Correcting glia changed mean input count by X%"* is one sentence and
it does a specific job.

**Invisible to whom.** Anyone who has never had to argue for resources. Without a
number, careful work reads as tidying, and tidying does not get funded.

**Absence looks like.** A quality problem everyone agrees is real and nobody budgets
for.

**Do this.** Measure it once, put it in the project's QC report, and reuse it every time
the work needs defending.
[Unit 07 §5]({{ '/technical-training/07-glia/' | relative_url }}).

### 26. Choose the cheaper error deliberately, and say that you did

Merge errors cost more than split errors, so bias yourself toward splits — on purpose,
and on the record.

**Invisible to whom.** Anyone taught that accuracy is symmetric. Every exam you have
taken weighted all mistakes equally; almost no real measurement does.

**Absence looks like.** An annotator quietly favoring one error type and never saying
so, which is indistinguishable from carelessness to anyone reading the output.

**Do this.** State the asymmetric loss function you are applying and why. "I bias toward
splits because a split is visible and locally repairable, and a merge is neither" is a
sentence that converts a habit into a method.
[Unit 06 §4]({{ '/technical-training/06-axons-and-dendrites/' | relative_url }});
[error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }}).

---

## What the twenty-six have in common

Every one is a **disclosure that is cheap now and impossible later**, and every one is
enforced in private: a supervisor's note in the margin of a draft, a reviewer report the
trainee never sees, a hallway remark between two senior people about whether a lab's
numbers can be trusted. None of those channels reaches someone without a supervisor who
does margin notes.

That is the whole mechanism by which this knowledge distributes unequally. The norms are
not secret. They are transmitted through channels that require you to already be inside.

## Install them where you cannot forget them

Norms you have to remember are norms you will drop under deadline. Put them in artifacts
instead.

**A notebook header block.** Materialization version. Dataset. All six
graph-construction parameters. Inclusion rule. Required proofreading level. Date. Write
it before the first analysis cell, not at submission.

**A figure caption template.** *Result. n = , of what. Version. Proofreading level and
its criteria. Null model. Number of tests and correction. Threshold, and what happened
at the second one.* A caption you cannot fill in means a figure that is not finished.

**A methods paragraph, drafted early.** Unit 08's lab asks you to write the data-quality
paragraph you will eventually publish *before* doing the work. That is not busywork: a
paragraph you cannot write yet is a decision you have not yet made.

**A rubric row.** If you supervise or facilitate, put "version pinned, assumptions named,
exclusions reported" in the rubric. Learners correctly infer that anything ungraded is
decorative. [Module 21]({{ '/modules/module21/' | relative_url }}) already carries the
reproducibility version of this row.

## The two that will actually cost you something

Norms 20 and 21 can kill your result. Reporting an error band that crosses the null, or
a headline effect that evaporates under a distance-preserving null, means writing up a
negative finding after months of work. In the short term that is genuinely worse for you
than not running the check, and pretending otherwise would be dishonest.

Run them anyway, for a reason that is not about virtue. A clean negative result against
a strong null is durable: *"reciprocity in this circuit is fully explained by degree
distribution and spatial proximity"* constrains the space of wiring rules that need
explaining, and it will not need revisiting in five years. Motif enrichment reported
against a weak null will. The work still cited in a decade is disproportionately the
work whose authors ran the check.

## Audit yourself in ten minutes

Open your most recent figure. Answer without looking anything up:

1. Which materialization version is it built on, and is that version in the caption?
2. Which of its claims are Bin B, and is the assumption in the same sentence?
3. What is the non-claim — the sentence you are explicitly not making?
4. What proofreading level are the cells, and by whose written criteria?
5. How many tests did you run to produce it?
6. What threshold, and what happened at the second one?
7. What is the null, and can you state the uninteresting explanation in words?
8. What is the exclusion rate, and where is it written down?
9. Is there a confidence value per call, and does the effect survive on the
   high-confidence subset?
10. Where is the error band from your own measured merge and split rates?
11. Are your quality numbers distributions with a maximum, or means?
12. If someone asked whether spatial proximity explains this, could you answer without
    re-running the pipeline?

Each question you cannot answer is a specific, fixable defect with a named unit attached
to it. That is a better outcome than the alternative, which is a reviewer answering them
for you.

## Related

- [The Hidden Curriculum hub]({{ '/hidden-curriculum/' | relative_url }})
- [Reading and judging]({{ '/hidden-curriculum/reading-and-judging/' | relative_url }}) —
  these same norms applied to other people's papers
- [Lab norms]({{ '/hidden-curriculum/lab-norms/' | relative_url }}) — what to do when one
  of these failures affects a colleague's work
- [Meta-learning]({{ '/hidden-curriculum/meta-learning/' | relative_url }}) — how to build
  the habits rather than merely agreeing with them
- [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }}) —
  materialization, VI, ERL, proofreading level
- [Module 21: Reproducibility and FAIR Principles]({{ '/modules/module21/' | relative_url }})
- [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}) and
  [error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }})
