---
layout: page
title: "Module 02: model responses"
permalink: /teaching/answers/module02/
slug: module-answers-02
content_type: delivery
description: "An exemplar lab navigation playbook for Module 02: five unwritten norms, three communication scripts, a mentor map with backups, an ethics commitment and the exit email, with misconception feedback."
---

[Learner worksheet]({{ '/assets/worksheets/module02/module02-activity.md' | relative_url }}) · [Session kit]({{ '/teaching/sessions/module02/' | relative_url }}) · [Module page]({{ '/modules/module02/' | relative_url }}) · [All model responses]({{ '/teaching/answers/' | relative_url }})

This page answers every section of the Module 02 worksheet in order. The worksheet
asks learners to write about their own research setting, so there is no single correct
answer. The responses below are one **invented learner's** work, written to show the
level of the kit's **Strong** criteria. The learner, the lab and every name in the mentor
map are invented. Where a script names a segment ID, that ID is invented too. This page
is public and suitable for formative assessment.

The invented learner is a second-year undergraduate who has just joined a lab that
analyzes a public cortical EM release and proofreads cells in a shared segmentation.
A learner in a different setting should expect different norms and different names,
and the same standard: each item is specific enough to act on tomorrow.

## Before you start

Module 01 is the only prerequisite. An acceptable question to bring: “When I do not
understand something in lab meeting, is it better to ask there or afterwards?” The
exemplar's Part A norm 3 and the Block 1 scenarios answer it.

## Questions this module answers

1. **What norms are assumed but rarely taught?** How to ask a question so it gets
   answered, when to disagree and how, what counts as “your” region in a shared
   segmentation, which version a number came from, and who gets named when work is
   shown. Nobody writes these down; people learn them by getting them wrong once.
2. **How do I ask for help effectively in research spaces?** State what you are
   working on, how long you have been stuck, what you have tried, the exact point of
   failure, and one specific request with a size (“ten minutes,” “one example query”).

## The task

### Norms inventory (Part A)

| # | (a) The norm | (b) How it is learned | (c) What a violation costs |
|---|---|---|---|
| 1 ★ | Bring the failure, not a summary of it. A question about a broken query carries the exact query, the dataset version and what you already tried. | By watching a senior student get a 30-second answer to a question that took me a week, because theirs came with the error message. | The question is deferred (“send me the details”), then forgotten. After a few, people stop answering quickly. |
| 2 | Every number travels with its version. A count on a slide names the dataset, the materialization version and the query date. | The hard way: a synapse count changed between two materializations and nobody could say which one the slide used. | The number cannot be reproduced. The slide is redone. Trust in your other numbers drops. |
| 3 ★ | Disagree in the meeting, as a question, not after it, as a complaint. | By observing that the people whose objections changed decisions raised them in the room, with evidence, and phrased as “what would we expect if…”. | The objection never reaches the decision. Raised afterwards, it reads as undermining rather than engaging. |
| 4 | Do not edit segments outside your assigned region without asking. In a shared segmentation, an edit changes other people's cells. | From a lab announcement after someone “helpfully” split a branch that another student was analyzing. | Someone's analysis changes without their knowledge. Edits get reverted. Some projects remove edit rights. |
| 5 | Credit is given at the point of use. When a figure rests on someone else's code, annotations or proofreading, their name is on the slide, not only in the final paper. | By seeing a slide go up without a name and watching the room notice. | The person who was not named stops helping. A later authorship dispute starts here, months before the paper. |

★ The two starred norms are the hardest for this learner: norm 1 because asking for
help still feels like admitting failure, and norm 3 because disagreeing with a senior
person in public feels riskier than staying quiet. Naming the barrier is what the
kit's Strong criterion (“reflection on barriers”) asks for.

### Communication scripts (Part B)

**Asking for help.**

> I have been working on the L2/3 synapse query for about three hours. Here is what
> I have tried: running the synapse query with the cell-type table joined; re-running
> on a smaller bounding box; checking my column names against the tutorial notebook.
> I am stuck on the join returning zero rows even though both tables return rows on
> their own. Could you look at my query with me for ten minutes this afternoon, or
> point me to one example that joins those two tables?

**Giving feedback.**

> I noticed that segment 7203 [invented ID] is in both your proofreading list and mine,
> and the split you made on Tuesday detached a branch I traced last week. I wanted to
> flag it because our two analyses now use different versions of that cell and neither
> of us knew. Would it help to look at it together in the viewer and agree who owns it?

**Admitting uncertainty.**

> I am not confident about the merge I flagged at the boundary of segment 4418
> [invented ID], because the membrane is low-contrast for three sections and I could
> not find the continuation. My best guess is that it is a real merge, but I would like
> a second opinion before I edit it, so I have left it in the review queue instead of
> fixing it.

Each script fills every bracket in the worksheet's template with something a reader
could act on: a time, a list of attempts, one failure point, one sized request.

### Mentor and support map (Part C)

All names are invented.

| Name | Role | What I can ask them | How to reach them | Backup contact |
|---|---|---|---|---|
| Jo | Undergraduate in the same lab, one year ahead (peer) | Anything I am embarrassed to ask anyone else; how the lab actually works; a first look at a broken query | Lab chat, or the desk next to mine, any afternoon | Priya, the other undergraduate |
| Lena | Postdoc who supervises my proofreading (senior) | Whether a merge call is right; what to do when a cell leaves my region; whether a result is ready to show | Weekly 30-minute check-in (Tuesdays); lab chat for one-line questions, with a 24-hour reply expectation | Marcus, graduate student on the same project |
| Dr. Adeyemi | Principal investigator (senior) | Scope decisions, authorship questions, anything Lena says to escalate | Office hours Thursdays; email with “[decision needed]” in the subject and a date | Lena carries it if the PI is traveling |
| Rafael | Department research-computing help desk (outside the team) | Cluster access, environment problems, storage quotas; things the lab assumes I already know | Ticket system; drop-in Wednesday mornings | The documentation wiki, then Jo |
| Dr. Okafor | Former course instructor, other department (outside the team) | A second opinion when the lab's advice conflicts, career questions, whether a problem is normal | Email; a coffee once a semester | The department's undergraduate research coordinator |

Five rows, at least one in each required category (peer, senior, outside the team),
and every row has a backup. The Strong criterion asks for backups because the
person you need is often the one who is away.

### Ethics commitment (Part D)

> Every count I report will carry the dataset name, the materialization version and
> the query date, in the notebook that produced it and on the slide that shows it. I
> will keep a running contributions file for my project that lists who wrote each
> piece of code and who proofread each cell I analyze, and I will name them whenever
> the work is shown, not only in a paper. I will log my own errors, with what each one
> taught me, in an error log I share with Lena at our weekly check-in. When I find an
> error in someone else's work, I will tell that person first, directly and with the
> evidence, before anyone else hears about it. If I am asked to use tissue-derived
> data whose consent terms I have not read, I will read them before I run a query.

Five sentences, covering provenance, attribution and error handling, each with a
practice (a file, a log, a first-contact rule) rather than a value statement.

### What good looks like

- **Strong:** every norm names a cost a reader can picture (“the slide is redone”);
  every script fills the brackets with specifics; every mentor row has a backup; the
  ethics commitment names files and moments (“at our weekly check-in”). The two
  starred norms come with a stated reason they are hard.
- **Weak:** norms stated as virtues (“be respectful,” “communicate well”) with no cost;
  scripts that keep the template's brackets or fill them with “my project”; a mentor
  map of three people who are all in the same lab; an ethics commitment that promises
  to “always be careful with data.”

## Working checklist

Decode one setting's unwritten rules: Part A. Map roles and communication paths: the
mentor map, with the reach-and-backup columns as the paths. Practice the help-seeking
script: Part B, first script. Define the support network: Part C. Identify ethical
considerations for the dataset: Part D and the exit prompt. Draft attribution and
collaboration norms: Part D sentences 2 and 4, and norm 5.

## Evidence and reasoning

| # | Claim | Evidence | Limitation / what would change my mind |
|---|---|---|---|
| 1 | Bringing the failure with the question gets a faster answer. | Observed twice in my lab: the question with the error message was answered in the meeting; mine without it was deferred. | Two observations in one lab. A lab that prefers written tickets might reward a different form. |
| 2 | Editing outside my region can change someone else's result. | A shared segmentation has one version of each cell; a split I make is the version everyone queries next. | Some projects have per-user branches or review queues that hold edits until approved. Then the cost is delay, not corruption. |
| 3 | Naming contributors at the point of use prevents later disputes. | The module's concept set says attribution should credit proofreaders, not just PIs; the dispute in norm 5 started with an unnamed slide. | This is prevention, not proof. I have not seen a dispute avoided, only one that was not. |

**Confidence:** Medium. Claim 1 rests on two observations in one setting; the other
two share the weakness that they describe my lab, not labs in general.

**Alternative considered and rejected:** listing the lab handbook's written rules as
the norms. Rejected because the worksheet asks for unwritten ones, and the handbook's
rules are the ones people already get told.

## Misconception self-check

Accept a response that names where the learner nearly made an error. Feedback for
each:

- **You will be taught everything you need to know.** Ask: “Which of your five norms
  was written down anywhere?” Usually none. That is the point of the inventory.
- **If the data is publicly available, there are no ethical considerations.** Ask:
  “Whose proofreading edits are in the version you queried, and where are they
  named?” Public access is a license to use, not a release from attribution,
  versioning or consent terms.
- **Research is a solitary activity.** Point at the mentor map: five people before
  the first result. Ask what the learner will do on the day the postdoc is away.
- **Good researchers do not make mistakes.** Ask for the error log rather than a
  promise of accuracy. The module's own line: labs that punish errors get fewer error
  reports, not fewer errors.
- **Scripted communication is inauthentic.** Ask the learner to read their help
  script aloud, then ask whether it says anything untrue. A script is a scaffold for
  the first few times; the tenth time it is just how they talk.

## Session timing (facilitator reference)

This section has no learner task. Block 1 (00:00–15:00) presents five scenarios and
asks for a recommended approach after learners respond. Approaches consistent with the
module's concept set:

1. **You disagree with a senior member's interpretation at lab meeting.** Ask a
   question that exposes the evidence: “Which version was that count from? I got a
   different number at the one I pinned; can we compare after?” Then follow up
   one-to-one with your data. Do not stay silent and do not relitigate it in the
   hallway.
2. **You find a bug in shared analysis code.** Reproduce it in the smallest case you
   can, then file it where the lab tracks issues, with the input, the version, what
   you expected and what happened. Tell the author directly. Do not patch the shared
   copy silently.
3. **You need help and your mentor is busy.** Use the map: a peer first, then the
   backup senior contact, then a written question in the lab channel with what you
   have tried. Set a time box (“if I am still stuck at 3 pm, I ask”).
4. **You are asked to proofread outside your assigned region.** Ask who owns that
   region and whether the request went through whoever coordinates edits. If the
   project has a rule that requires coordination, decline until it is cleared, and say
   why.
5. **A collaborator uses your annotation work in a paper without credit.** Assume an
   oversight first. Write to them naming the figure and what you contributed, and ask
   for the credit the project's written criteria give it. If there is no reply or no
   written criteria, take it to your mentor with the same note.

The other two script templates the module names, receiving feedback and escalating a
problem, are in Block 4 of the run of show and are not in the worksheet; do not mark a
learner down for omitting them.

## Rubric

A self-assessment that matches this exemplar:

- **Strongest part:** the mentor map, because every row has a backup and two contacts
  are outside the lab, so no single absence blocks me.
- **Weakest part:** the giving-feedback script is written for a proofreading conflict
  and I have not yet had one; it is untested. **Next action:** use it once on a
  low-stakes case (a naming inconsistency in shared code) within two weeks and revise
  it from how that goes.

## Exit prompt

**Email requesting clarification on an unclear expectation.** All names are invented.

> Subject: Progress updates: format and frequency?
>
> Dear Dr. Adeyemi,
>
> I want to check what you expect from me on progress updates. I have been sending
> Lena a short message each Friday with my proofread-cell count and one problem I hit.
> I am not sure whether you also want to see those, whether a written note or a slide
> in lab meeting is better, or whether weekly is too often.
>
> My default, unless you say otherwise, is to keep the Friday note to Lena and add a
> one-slide update to lab meeting every two weeks. If you would prefer something else,
> a one-line reply is enough.
>
> Thank you,
> [Learner]

The email names the specific ambiguity, states what the learner is already doing,
proposes a default and asks for a small reply.

**Two-sentence ethics commitment on attribution in collaborative proofreading:**

> I will keep a per-cell record of who proofread what, from the first edit, so that
> credit is a lookup and not a memory. When the work is shown or written up, I will
> name the proofreaders at the level the project's written criteria set, and I will
> ask for those criteria in writing if they do not exist yet.

## Peer review (swap worksheets)

A reviewer of this exemplar should note that each norm has an observed cost and each
claim in the evidence table names a limitation. A good question to ask its author:
“Your map has two contacts outside the lab. Which one would you go to if the lab's
advice and the course's advice conflicted, and why that one?”

## Feedback guide

This key follows the kit's own tiers rather than a numeric score.

- **Minimum:** a clear norms list (five norms, each with how it is learned and what a
  violation costs), a help-seeking plan (the map and the first script), and at least
  one communication script with the brackets filled.
- **Strong:** realistic escalation paths (a backup in every mentor row, an escalation
  route to the PI with a trigger); reflection on barriers (why the starred norms are
  hard); an ethics commitment with specific practices (a file, a log, a first-contact
  rule); a mentor map with backup contacts.
- **Failure:** generic advice without actionable steps (“communicate clearly,” “be
  ethical”); no personalization to the learner's own context (a map with role titles
  and no way to reach anyone; scripts that could be about any project).

Do not reward length or a large mentor map; three rows with real backups outrank
eight without. Do not reward a script that sounds confident but has no specific
request. Do not penalize a learner whose setting is hypothetical (they have not joined
a lab yet) if the plan names who they will find and how. This is a local teaching
rubric, not a validated assessment instrument.

See [the hidden curriculum]({{ '/hidden-curriculum/' | relative_url }}) for the
collected norms and [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
for what a version record contains. Teaching material: CC BY 4.0, NeuroTrailblazers.
