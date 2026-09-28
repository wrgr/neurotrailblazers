---
layout: page
title: "Module 25: model responses"
permalink: /teaching/answers/module25/
slug: module-answers-25
content_type: delivery
description: "An invented learner's portfolio map, four-line captions, reflection notes, feedback log, revision plan and permission check for Module 25, with a weak version of each and the kit's rubric tiers."
---

[Learner worksheet]({{ '/assets/worksheets/module25/module25-activity.md' | relative_url }}) · [Session kit]({{ '/teaching/sessions/module25/' | relative_url }}) · [Module page]({{ '/modules/module25/' | relative_url }}) · [All model responses]({{ '/teaching/answers/' | relative_url }})

This page answers every section of the Module 25 worksheet in order. A portfolio is a
learner's own work, so there is no single correct answer. The responses below are one
**invented learner's** work, Ravi (invented), written at the level the content plan
calls **Proficient**: every Minimum line of the kit's rubric met and most Strong lines
met, with each annotation saying which. His artifacts are the outputs of this site's
own module worksheets, so a reader can see what each one is; his reviewer (Amara) and
mentor (Dr. Lindqvist) are invented, and every number that describes his work (row
counts, dates, deferral rates, rehearsal times) is invented and labeled. Where a caption
cites a value from a published kit on this site, the value was recomputed from the kit's
files and is real for those files. This page is public and suitable for formative
assessment.

The exemplar deliberately does not reuse the module's worked example (Maya's
proofreading-log caption). A key that copied it would reward copying.

## Before you start

The prerequisites are completed artifacts from at least three technical modules and one
writing or presentation artifact. Ravi has eight technical outputs and two writing
ones; the map below cuts two. An acceptable question to bring: “Should I include the
notebook where I got the null model wrong?” The answer this module gives is yes, beside
the corrected one, with the reason.

## Questions this module answers

1. **Which artifacts best demonstrate technical competency?** The ones a stranger can
   check: a notebook whose cell 14 prints a number the reviewer can rerun, a log whose
   `rationale` column explains each deferral, a release note with row counts per step.
   One artifact per competency claim; a second artifact for the same claim is cut.
2. **How should failure and revision be documented constructively?** Keep the wrong
   version beside the corrected one, and write the reason for the change in the
   revision log with the reviewer's name and the date. The decision, the alternative not
   taken and the evidence that settled it are the three parts of a usable reflection.
3. **What evidence of growth is credible to reviewers?** A pair of artifacts from the
   same learner months apart where the second would have caught the first's error, and
   a revision log that names what a reviewer said and what changed because of it.
   Enthusiasm and effort are not evidence; a changed method with a stated reason is.

## The task

### 1. Portfolio map: ten candidates, eight kept, one claim each

The claims were written first, as the working checklist asks, and the artifacts were
selected against them. Ravi's format is the module's recommended combination: a public
repository holding the artifacts and a one-page PDF that captions them and links in.

| # | Artifact (module it came from) | Competency claim: “this proves I can…” | What I did / what I was given |
|---|---|---|---|
| 1 | Proofreading log with QC metrics ([Module 07]({{ '/modules/module07/' | relative_url }})) | …triage segmentation errors by their effect on the graph and record why each was fixed or deferred. | Given: the kit's segmentation and its flagged errors. Mine: every call, every correction, the `rationale` column. |
| 2 | Graph-analysis notebook on the 500-neuron column kit, versions 1 and 2 side by side ([Module 10]({{ '/modules/module10/' | relative_url }})) | …build a connectivity graph at stated thresholds and say which conclusions change between them. | Given: `nodes.csv`, `edges.csv`. Mine: the notebook, the threshold comparison, the null model, and the wrong first version. |
| 3 | Inference design sheet ([Module 20]({{ '/modules/module20/' | relative_url }})) | …choose a null model from the hypothesis and count every test I ran, including the ones I did not report. | Given: two kit graphs and the scenario. Mine: the estimand, the nulls, the test tally, the claim partition. |
| 4 | Preprocessing release note with decision log ([Module 18]({{ '/modules/module18/' | relative_url }})) | …clean a dataset transparently, with rows removed per step and the reason. | Given: the kit's noisy tables. Mine: the pipeline, the thresholds, the QC dashboard, the note. |
| 5 | Results subsection, hardened legend and one reviewer response ([Module 17]({{ '/modules/module17/' | relative_url }})) | …write a calibrated claim with its version, interval and rung, and answer a reviewer with evidence. | Given: the fictional scenario's counts. Mine: the paragraph, the legend, the response and the sensitivity sweep it cites. |
| 6 | Four-slide talk deck with speaker notes and the post-Q&A revision log ([Module 22]({{ '/modules/module22/' | relative_url }})) | …present a result with the uncertainty rung spoken, and revise a claim from critique. | Given: the synthetic result. Mine: the claim tree, the deck, the answers, the log. Peer critique from two named classmates. |
| 7 | Question-to-hypothesis sheet, month 1 and month 6 ([Module 01]({{ '/modules/module01/' | relative_url }})) | …narrow a question to a measurable structural hypothesis with a falsification condition. The pair shows the change. | Both mine. The month-6 sheet was written without looking at the month-1 one, then compared. |
| 8 | Reproducibility package with a peer's friction log ([Module 21]({{ '/modules/module21/' | relative_url }})) | …package an analysis so a stranger reruns it cold. | Given: the kit table. Mine: the package, the checklist, the fixes. The friction log is Amara's, credited by name. |

**Cut, with the reason recorded in the README.** A motif notebook from Module 11
proved the same claim as artifact 3 and counted no tests, so 3 is the stronger evidence.
A figure set from Module 16 duplicated the figure that artifact 5's legend already
hardens. Two cuts from ten candidates; the README says which two and why, because the
cut is itself evidence of judgment.

**Why this meets the rubric.** Every artifact maps to one claim and no claim has two
artifacts (Minimum: claims evidence-backed; the failure mode “artifact dump” avoided).
The did-versus-given column is filled for every row, including the two where a
classmate's work is inside the artifact (Minimum: contributions in group work stated).
Artifacts 2 and 7 are the cross-module pair that shows growth (Strong: cross-module
synthesis; earlier wrong version shown).

**A weak version, and what is missing.** A folder named `portfolio_final` with twelve
notebooks sorted by module number, no claims, and a README that says “my work from the
course.” The reviewer cannot tell what any file proves, which parts the learner wrote,
or where to start, and the two-minute pass ends on the folder listing.

### 2. Four-line captions and reflection notes

Each caption follows the module's fixed structure: claim, what I did versus what I was
given, what a reviewer can verify and where, and the limitation. Two in full:

**Artifact 2, graph-analysis notebook, versions 1 and 2.**

> 1. This proves I can build a connectivity graph at stated thresholds and say which
>    conclusions change between them.
> 2. Given: the Module 10 kit's `nodes.csv` and `edges.csv`. Mine: both notebook
>    versions, the threshold comparison and the null model. Version 1 compared
>    reciprocity to a random graph; version 2 replaced it with a degree-preserving null
>    after I saw that the random graph was beaten by almost any structure.
> 3. Verify: cell 4 prints 11,388 edges at one synapse or more and 2,332 at three or
>    more, and 55.4% of edges carry exactly one synapse. Cell 6 excludes object 20432,
>    which has two somata.
> 4. Limitation: the degree-preserving null keeps the spatial structure the kit was
>    built with, so version 2 still overstates any enrichment. Next I would add a
>    distance-preserving null, as artifact 3 does.

**Artifact 3, inference design sheet.**

> 1. This proves I can choose a null model from the hypothesis and count every test I
>    ran, including the ones I did not report.
> 2. Given: the Module 11 and Module 10 kit graphs and the scenario. Mine: the estimand
>    (reciprocal E–I pairs), four nulls, the 24-test tally and the split between
>    exploratory and confirmatory claims.
> 3. Verify: in the Module 11 kit, 41 reciprocal E–I pairs at one synapse or more; the
>    ratio to the null falls from 2.47 (degree-preserving) to 0.92 once type and soma
>    distance are also preserved. The script and seed are in `inference/README.md`.
> 4. Limitation: the error band uses assumed merge and split rates, because the kits
>    carry no measured ones. With measured rates the band could move.

The kit values in lines three were recomputed from the kit files for this page. The
null ratios are stochastic and match the
[Module 20 model responses]({{ '/teaching/answers/module20/' | relative_url }}) to within
sampling error.

Line three for the other six, in brief:

| # | Line three: what a reviewer can verify, and where |
|---|---|
| 1 | The `rationale` column in the proofreading log, one entry for each of the 45 flags in the Module 07 kit's error report. |
| 4 | The release note's row table: 447 exact duplicate rows removed at step 1a, as in the Module 18 kit. |
| 5 | The version, interval and rung in the figure legend, with the sensitivity sweep's notebook cell cited by number. |
| 6 | The revision log entry dated after the Q&A, naming the claim changed and who asked. |
| 7 | The falsification condition on each sheet, the month-6 one naming a pinned release. |
| 8 | Amara's friction log, with each item's fix committed and linked. |

**Reflection note, artifact 2** (decision, alternative not taken, evidence that settled it):

> I kept version 1 in the portfolio rather than describing it. The alternative was a
> caption sentence saying “an earlier version used an inadequate null.” What settled it
> was Amara's review: reading the two side by side showed the change, and the sentence
> alone read as a confession. The error was mine; the fix came from reading the module's
> concept on null models, not from a reviewer catching it.

**Why this meets the rubric.** Every caption has a line three a stranger can check
(so the flagged failure of missing line threes is avoided). The reflection names a
decision and the alternative, not what Ravi enjoyed (Minimum: a meaningful revision
loop). Artifact 2 shows the wrong version beside the correction with its reason
(Strong).

**A weak version, and what is missing.** “Graph analysis notebook. I really enjoyed
learning NetworkX and exploring the data. This project taught me a lot about
connectomics.” No claim, no split between given and done, nothing to verify and no
limitation. The reflection describes a feeling, which is the misconception the module
names.

### 3. Peer review with a stated decision, criterion and deadline

Each artifact sent for review went with four things: the decision, the criterion, the
stage and the deadline. Two requests and what came back [dates and names invented]:

**Request for artifact 2, to Amara (peer), sent 2026-09-08.**

> I'm deciding whether to show version 1 of the graph notebook, the one with the wrong
> null, in the portfolio at all, or only describe it in the caption. The criterion is
> whether seeing it makes the competency claim stronger or just makes me look careless.
> The notebook pair is near-final. I need an answer by Thursday 11 September.

Amara's reply, which answered the question asked before anything else:

> Show it. Reading the two side by side is how I understood what changed; the caption
> alone read as a confession. But put the reason for the change in the caption's first
> line, not the last, because a skimmer stops after one line. One more thing you did not
> ask: cell 9 in version 2 still says “random null” in a comment. Fix the comment.

**Request for artifact 6, to Dr. Lindqvist (mentor), sent 2026-09-09.**

> I'm deciding whether the revision log after the talk should include the change I
> refused to make (keeping the analogy on slide 2). The criterion is whether a reviewer
> reads a refused change as judgment or as stubbornness. Draft stage; I need this by
> Monday 15 September.

Reply: “Judgment, if the reason is one sentence and names who asked. Stubbornness if it
is a paragraph. Keep it to one sentence.”

**The feedback log** records, per request: date, reviewer, decision asked, criterion,
answer received, and what was done with it. Amara's unasked-for comment is logged too,
marked “outside the request, acted on,” because a reviewer who volunteers something
worth fixing should be able to see it was used.

**Why this meets the rubric.** Every request states decision, criterion, stage and
deadline (working checklist step 6), and the log shows the answer and the resulting
change (Minimum: feedback incorporated with clear changes). The two reviewers are
different roles, peer and mentor, and each was asked the question that role can answer.

**A weak version, and what is missing.** “Hi Amara, attached is my portfolio, any
thoughts? No rush.” What comes back is what a reader can give cheaply: two typo
corrections and “looks great.” The learner's actual decision, whether to show the wrong
version, was never asked, so it was never answered, and the deadline “no rush” means the
reply arrives after the submission.

### 4. Revision plan

Ordered by how much each change alters what the portfolio proves, not by how easy it is.
Dates invented; the submission deadline is 2026-09-30.

| Priority | Change | Effect on what the portfolio proves | Deadline | Status |
|---|---|---|---|---|
| 1 | Move the reason for the null-model change to line one of artifact 2's caption (Amara, 2026-09-10). | Turns the wrong version from an admission into the portfolio's strongest evidence of judgment. Without it, the reviewer who opens exactly one artifact may read the wrong thing. | 2026-09-12 | Done |
| 2 | Write the README's first section as the two-minute path: which three captions to read and which one artifact to open (artifact 2). | Decides what the two-minute pass sees. A README without it leaves the choice to the reviewer, who chooses the first file alphabetically. | 2026-09-15 | Done |
| 3 | Pin the kit versions in every caption (the kit manifest's file hashes) and add the T25 [invented version label] materialization to artifact 7's month-6 sheet. | A number without a version cannot be checked, which empties every caption's line three. | 2026-09-18 | Done |
| 4 | Add the refused change to artifact 6's revision log as one sentence (Dr. Lindqvist, 2026-09-12). | Small, but it is the only place the portfolio shows a critique being weighed rather than obeyed. | 2026-09-18 | Done |
| 5 | Fix the stale “random null” comment in artifact 2, cell 9. | Nil for the claim; nonzero for trust, because a reviewer who finds it stops believing the rest of the notebook. | 2026-09-12 | Done |
| 6 | Add a future growth plan to the README: a merge-injection sensitivity check on artifact 3's design sheet by December, a rerun of artifact 8's package on a third operating system by November. | Converts “what I can do” into “what I will do next,” which the Strong tier asks for. | 2026-09-25 | Open |
| 7 | Replace the artifact 6 talk recording with a re-recorded version at the revised claim language. | Low: the revision log already shows the change, and the recording is supporting material. Do last, or not at all. | If time remains | Open |

The revision log, kept in the repository as `REVISIONS.md`, carries one dated entry per
row with the reviewer's name where a reviewer prompted it.

**Why this meets the rubric.** The order follows effect on proof, with the cosmetic
change last and the low-effort, high-trust fix (row 5) placed by its effect rather
than its cost (working checklist step 7). Row 6 is the future growth plan with concrete
milestones (Strong).

**A weak version, and what is missing.** A to-do list ordered by ease: “fix typos, rename
files, update README, maybe re-record talk.” No dates, no reviewer names, no statement
of what each change does to the claims, and the change that matters most (row 1) is
missing because it was the hardest.

### 5. Permission and provenance check

The module's three questions, asked of every artifact, plus the version pin:

| # | Data allowed to be shown? | Unpublished lab data? | Collaborators credited? | Version pinned |
|---|---|---|---|---|
| 1 | Yes: the Module 07 kit is synthetic teaching material on this site | No | Not applicable | Kit file hash from the kit manifest |
| 2 | Yes: Module 10 kit, synthetic | No | Not applicable | Kit file hash |
| 3 | Yes: Module 11 and Module 10 kits, synthetic | No | Not applicable | Kit file hashes, script seed |
| 4 | Yes: Module 18 kit, synthetic | No | Not applicable | Kit file hash |
| 5 | Yes: the counts come from a fictional scenario and are labeled as such | No | Not applicable | Scenario named in the caption |
| 6 | Yes | No | Two classmates named for their critique | Deck date in the file name |
| 7 | Month-6 sheet cites a public release | No | Not applicable | Materialization T25 [invented label] |
| 8 | Yes: Module 03 kit, synthetic | No | Amara credited by name for the friction log | Kit file hash |

One change came out of the check. Ravi's first draft of artifact 5 had a figure that
reused a lab-meeting slide from his rotation, built on the lab's unpublished data. It
was cut and replaced with the kit-based figure. The caption now says the method was
first used on restricted data, as the module's recovery step advises. Asking was the
check. The lab's answer was not his to assume.

This site's kits are covered by the site's CC BY 4.0 content license, which asks for
attribution. The check records that, and each caption credits the kit. It does not
replace reading a real dataset's own terms before publishing work on it.

### What good looks like

- **Strong:** claims written before artifacts were chosen; one artifact per claim with
  the cuts explained; every caption's line three names a file, cell or number; one
  wrong version shown beside its correction; review requests with decision, criterion,
  stage and deadline; a revision plan ordered by effect on proof; a permission check
  that changed something.
- **Weak:** a folder in module order, captions that describe rather than claim,
  reflections about enjoyment, “any thoughts?” review requests, a revision list ordered
  by ease and no permission check.

## Working checklist

The seven steps map to the sections above: claims first and selection (section 1),
captions and reflections (section 2), the permission check (section 5), review
(section 3) and revision with a README and log (section 4). Ravi ran the permission
check before review, as the checklist orders it, so the reviewers never saw the cut
lab-meeting figure.

## Evidence and reasoning

| # | Claim | Evidence | Limitation / what would change my mind |
|---|---|---|---|
| 1 | The portfolio proves eight distinct competencies. | Eight claims, one artifact each; two duplicates cut, with reasons in the README. | A reviewer who reads two claims as the same competency would count seven. |
| 2 | Artifact 2 shows growth in judgment, not only in skill. | Versions 1 and 2 side by side; the caption's first line gives the reason for the change. | It shows one corrected error. A second, independent correction would make the claim stronger. |
| 3 | Every artifact can be shown publicly. | The permission table; one figure cut because it used unpublished lab data. | The check covered this site's kits. A future artifact on real data needs that dataset's terms read. |

**Confidence:** Medium. The map and captions are one strong line of evidence, but
every reviewer so far is a classmate or mentor who knows the course, which is a shared
weakness. A reviewer from outside would be the second line.

**Alternative considered and rejected:** include all ten candidates to show breadth.
Rejected because two proved the same claims as stronger artifacts, and the module's
guidance is that duplicates dilute the two-minute pass.

## Misconception self-check

Feedback for each error:

- **More artifacts make a stronger portfolio.** Ask which claim each artifact proves.
  Where two answer the same claim, ask which one the learner would open first, and cut
  the other.
- **Describing what you enjoyed counts as reflection.** Ask for the decision, the
  alternative not taken and the evidence that settled it.
- **A final version is stronger evidence when the earlier drafts are removed.** Point
  to artifact 2. The wrong version plus the reason is the evidence of judgment.
- **A good artifact speaks for itself and needs no caption.** Ask a stranger to find
  the verifiable number in the artifact in two minutes without the caption.
- **Asking a narrow question wastes the reviewer's expertise.** Compare Amara's
  answer to the “any thoughts?” reply in section 3.
- **Work you did yourself is automatically yours to publish.** The cut lab-meeting
  figure in section 5 was Ravi's own work on data he did not own.

## Session timing (facilitator reference)

This section has no learner task. In the 00:00–08:00 exemplar block a facilitator can
show the module's Maya caption. This page deliberately uses different artifacts, so
learners can compare two exemplars without copying either.

## Rubric

A self-assessment that matches this exemplar:

- **Strongest part:** artifact 2's caption and reflection, because they show a wrong
  version, its correction and the reason, and a stranger can check the numbers in
  line three.
- **Weakest part:** no reviewer from outside the course has read the portfolio.
  **Next action:** send the two-minute README path to one researcher outside the course
  by the submission date, with the question “Which artifact would you open, and why?”

## Exit prompt

Artifact 8, the reproducibility package:

> 1. This proves I can package an analysis so a stranger reruns it cold.
> 2. Given: the Module 03 kit's `synapses_sample.csv`. Mine: the package, the
>    checklist and the fixes. The friction log is Amara's.
> 3. Verify: the clean-room run in the README reproduces `top_pairs.csv` from the
>    kit file, and each friction item links to the commit that fixed it.
> 4. Limitation: it has been rerun on two operating systems, both by course members.
>    Next I would have it rerun on a third by someone outside the course, the growth
>    milestone set for November.

## Peer review (swap worksheets)

A reviewer should pick one caption at random and try to verify its line three in two
minutes. If they cannot, that caption fails, however good the artifact is. A good
question to ask Ravi: “Which artifact would you cut next if the limit were six, and
why?”

## Feedback guide

This key follows the kit's own tiers.

- **Minimum pass:** claims backed by evidence; at least one meaningful revision loop in
  the reflections; feedback incorporated with the changes shown; contributions in group
  work stated.
- **Strong:** synthesis across modules; uncertainty and correction handled with
  technical maturity; a growth plan with dated milestones; at least one earlier wrong
  version shown beside the correction and its reason.
- **Failures to flag:** an artifact dump with weak mapping; reflection that is
  narrative only; minimal response to critique; captions with no line three.

Do not reward volume, visual polish or a personal website over captions. Do not
penalize a learner for showing a mistake; reward the reason given for the fix. Accept
any set of six to ten artifacts that maps one claim to each. Accept artifacts from
modules other than those used here. This is a local teaching rubric, not a validated
assessment instrument.

See [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
for version records. Teaching material: CC BY 4.0, NeuroTrailblazers.
