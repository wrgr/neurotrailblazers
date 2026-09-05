---
title: "Module 25: Portfolio, Feedback, and Final Project"
layout: module
permalink: /modules/module25/
description: "Assemble a capstone portfolio that demonstrates connectomics competencies with evidence, reflection, and iterative feedback."
module_number: 25
image: /assets/images/modules/module25.svg
image_alt: "Stylized vector art: artifacts orbiting and converging on a completed center."
difficulty: "Advanced"
duration: "5-6 hours"
learning_objectives:
  - "Curate technical artifacts that demonstrate end-to-end capability"
  - "Write reflective commentary linking decisions, errors, and growth"
  - "Integrate peer/mentor feedback into a revised final portfolio"
  - "Present a coherent research identity and next-step plan"
prerequisites: "Modules 1-24"
merit_stage: "Dissemination"
compass_skills:
  - "Synthesis"
  - "Reflective Practice"
  - "Professional Presentation"
ccr_focus:
  - "Meta-Learning - Portfolio Thinking"
  - "Skills - Scientific Storytelling"

# Normalized metadata
slug: "module25"
short_title: "Portfolio, Feedback, and Final Project"
status: "active"
audience:
  - "students"
pipeline_stage: "Dissemination"
merit_row_focus: "Dissemination"
topics:
  - "portfolio"
  - "capstone"
  - "feedback"
summary: "Build a publishable capstone portfolio that integrates technical evidence, reflection, and future pathway planning."
key_questions:
  - "Which artifacts best demonstrate technical competency?"
  - "How should failure and revision be documented constructively?"
  - "What evidence of growth is credible to reviewers?"
slides: []
notebook: []
datasets:
  - "/datasets/workflow/"
  - "/datasets/mouseconnects/"
personas:
  - "/avatars/undergradstudent"
  - "/avatars/gradstudent"
related_tools:
  - "/tools/ask-an-expert/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Completed artifacts from at least three technical modules"
  - "One writing or presentation artifact"
next_modules: []
references:
  - "Program portfolio templates and competency rubrics."
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
content_type: path
---

## Capability target
Submit a capstone portfolio that proves technical capability, communicates decision quality, and demonstrates iterative growth through feedback. Operationally: every artifact carries a caption naming the competency it proves and what a reviewer can check, the portfolio distinguishes what you did from what you were given, and at least one artifact shows a version that was wrong alongside the correction and the reason.

## Why this module matters
A portfolio is often the strongest evidence of readiness for research opportunities, and for learners without an established institutional signal it may be the only evidence a reviewer will accept. A good portfolio shows not only polished outputs, but also reasoning, revision, and integrity in how work was produced.

The reason it belongs in the Career and Community track rather than a technical one is that portfolio conventions are hidden-curriculum conventions. Nobody says out loud that a reviewer skims for two minutes, that an unexplained file called `analysis_final_v3.ipynb` is read as a warning, that including a mistake with its correction raises credibility rather than lowering it, or that the sentence describing what you personally did in a group project is the sentence a reviewer looks for hardest. Trainees who have seen a portfolio reviewed know these. Trainees who have not usually optimize for polish, which is the wrong target, and they hide the errors, which removes the most persuasive material they have.

## Concept set

### 1) Portfolio as evidence architecture
- **Technical:** artifacts should be organized by competency claims, not chronology. Six well-captioned artifacts covering distinct competencies outperform fifteen that cluster on one. Where two artifacts prove the same thing, keep the stronger and cut the other; the cut is itself evidence of judgment.
- **Plain language:** group work by what it proves you can do.
- **Misconception guardrail:** more artifacts make a stronger portfolio.

### 2) Reflection should be analytical
- **Technical:** reflections should identify assumptions, failure modes, and changes made after feedback, in that order. A usable reflection names the decision, the alternative not taken, and the evidence that settled it.
- **Plain language:** explain how your thinking improved, not just what you did.
- **Misconception guardrail:** describing what you enjoyed about a project counts as reflection.

### 3) Feedback is part of final quality
- **Technical:** major artifacts should include version history and revision rationale, so a reviewer can see the delta and its cause rather than only the endpoint.
- **Plain language:** show how critique changed your work.
- **Misconception guardrail:** a final version is stronger evidence when the earlier drafts are removed.

### 4) What to include in a capstone portfolio
A strong connectomics capstone portfolio should contain several categories of artifacts that together demonstrate end-to-end research competency. Include annotated EM images with written interpretation explaining what structures are visible and what biological conclusions can be drawn. Graph analysis notebooks (Jupyter or similar) should show the full workflow from data loading through statistical testing, with inline commentary on analytical choices. Proofreading logs with QC metrics document hands-on data quality work and show attention to accuracy. A research brief or mini-paper (even 2-3 pages) demonstrates the ability to frame a question, present evidence, and state limitations. Presentation slides from talks or poster sessions round out the package by showing communication skill.

The portfolio serves as career material beyond the course. For graduate school applications, it demonstrates technical skills (EM annotation, Python, graph analysis), scientific rigor (QC documentation, statistical reasoning), and communication ability (writing, presentations) in a single integrated package. Organize artifacts by competency rather than by module or chronology, and include brief reflection notes explaining what was learned and what would be done differently. Version the portfolio itself, and treat it as a living document that grows as new work is completed.

### 5) Evidence captions have a fixed structure
- **Technical:** every artifact carries a four-line caption. Line one, the competency claim: what this proves I can do. Line two, what the artifact is, and explicitly what I did versus what was given to me. Line three, what a reviewer can verify and where, naming the cell, file, or number. Line four, the limitation, and what I would do differently. A caption that cannot fill line three is describing an artifact nobody can check.
- **Plain language:** the caption is what turns a file into evidence. Without it a reviewer has to guess, and reviewers guess unfavorably.
- **Misconception guardrail:** a good artifact speaks for itself and needs no caption.

### 6) Feedback has to be requested in a form that can be answered
- **Technical:** a usable request states the decision you want help with, the criterion to judge against, the stage of the work, and the deadline. "Any thoughts?" attached to a whole notebook produces line-level typo corrections, because that is the only feedback a reader can give cheaply. "I'm deciding whether to keep the distance-matched null or drop it; the criterion is whether the enrichment survives; I need this by Thursday" produces an answer to the question you actually have.
- **Plain language:** tell the reviewer what decision you are stuck on, and they can help with it.
- **Misconception guardrail:** asking a narrow question wastes the reviewer's expertise.

### 7) Permission and provenance are part of the artifact
- **Technical:** before publishing anything, check three things: whether the dataset's own citation and use guidelines permit redistribution of what you are showing, whether any part of the work is unpublished lab data that your supervisor has not agreed to make public, and whether collaborators are correctly credited by name for the parts they did. Record the dataset version alongside every result, since an analysis against an unpinned segmentation cannot be reproduced later even by you.
- **Plain language:** confirm you are allowed to show it, and say where it came from.
- **Misconception guardrail:** work you did yourself is automatically yours to publish.

## Hidden curriculum scaffold
- Unspoken portfolio expectations:
  - Reviewers look for evidence of independent judgment, not only completion. The sentence that carries the most weight is the one naming what you decided and why.
  - Clear file naming and versioning signals professionalism. Dated, descriptive names beat `final_v3`, and a README that says what to read first beats a well-organized folder without one.
  - Acknowledging mistakes with correction steps increases credibility. The most persuasive artifact most trainees hold is the one they are most inclined to delete.
  - In group work, state precisely what you did. Reviewers assume the vaguest possible reading of an unattributed contribution, so "I wrote the QC pipeline; the segmentation was produced by the consortium" is stronger than a passive description of the whole project.
  - Assume a two-minute first pass. Whatever must be seen goes at the top, in text, not inside a notebook a reviewer has to open.
- Support moves:
  - Provide the artifact-selection rubric before curation begins, not after submission.
  - Normalize inclusion of failure-to-fix examples by including one in the exemplar you show the group.
  - Use staged feedback cycles with explicit criteria at each stage, and require learners to report what they changed. The report is what makes a reviewer willing to read the next version.

## Core workflow: capstone portfolio build
1. Define the competency claims first, in writing, then ask what evidence each requires. Working the other way round produces a folder of what you happen to have.
2. Select artifacts against those claims, cutting duplicates and keeping the version that shows the most judgment rather than the most polish.
3. Write one four-line evidence caption per artifact, checking that line three names something a stranger can verify.
4. Add reflection notes on decisions, errors, and revisions, naming the alternative not taken in each case.
5. Run the permission and provenance check across every artifact, and pin dataset versions.
6. Run peer or mentor review with a stated decision, criterion, stage, and deadline for each artifact you send.
7. Revise, record what changed and why in a visible revision log, and publish the package with a README that tells a two-minute reader where to start.

## Choosing a portfolio format: decision table
The format determines who can read your evidence, so choose before you build.

| Format | Who can actually read it | What it proves well | Maintenance cost | What it costs you |
|---|---|---|---|---|
| Public code repository | Anyone technical; some reviewers will not clone it | Reproducibility, code quality, commit history as a genuine revision trace | Low once set up, but a stale repository is visible | Requires that everything in it be publishable, and the commit history is public whether or not it flatters you |
| Static personal site | Anyone, including non-technical reviewers | Communication, framing, and the two-minute first pass | Moderate; it decays quietly if you stop updating | Setup time, and a real risk of spending effort on design that should have gone into captions |
| Single PDF dossier | Anyone, including committees that will not follow links | Curation and writing; survives being emailed and printed | Low, but every update means regenerating and resending | Cannot show code running or interactive results, and versions proliferate across recipients |
| One annotated notebook | Technical readers who will open it | End-to-end analytical reasoning in one place | Low | Proves one competency deeply and others not at all; weak as a whole portfolio, strong as its centerpiece |
| Institutional or program page | Whoever is directed there | Affiliation and legitimacy signal | None, and that is the problem | You do not control it, cannot update it on your schedule, and lose it when you leave |

For most trainees the workable combination is a public repository holding the artifacts plus a one-page PDF that captions them and links in, because it satisfies both the reviewer who will clone and the reviewer who will not.

## 60-minute tutorial run-of-show
1. **00:00-08:00 | Portfolio quality exemplar**
   - Show one strong and one weak portfolio side by side, including a strong one that contains a documented error. Ask which one the room would trust with a dataset.
2. **08:00-20:00 | Competency-claim mapping**
   - Learners write claims before selecting artifacts. Circulate asking "what would falsify this claim?" to force claims specific enough to be checked.
3. **20:00-34:00 | Artifact curation and caption drafting**
   - Four-line captions, with line three enforced. Any caption that cannot name a verifiable item is returned rather than discussed.
4. **34:00-46:00 | Feedback exchange round**
   - Each learner sends one artifact with a stated decision, criterion, stage, and deadline. Reviewers must answer the stated question before offering anything else.
5. **46:00-56:00 | Revision planning**
   - Convert feedback into a dated revision list ordered by how much each change alters what the portfolio proves, not by how easy it is.
6. **56:00-60:00 | Final submission checklist**
   - Permission check, dataset versions pinned, README present, contribution statements written.

## Worked example: turning a file into evidence
Maya has `proofreading_log.csv`: 340 rows, one per segment she reviewed over six weeks, with columns for segment ID, error type, action taken, and time spent. Her first caption reads:

> "Proofreading log from my time on the project. Shows the segments I worked on."

This is a file description, not evidence. It names no competency, gives a reviewer nothing to check, and describes effort rather than judgment. Effort is not the thing being assessed.

The four-line rewrite:

> **Competency:** I can triage segmentation errors by downstream impact and document the decision trail.
>
> **Artifact:** A log of 340 segments I personally reviewed across six weeks. The segmentation and the automated error flags were produced by the consortium pipeline; the triage decisions, the corrections, and this log are mine.
>
> **Verifiable:** Rows 112 to 140 are the merge-error cluster near the volume boundary. Column `action` records which I corrected and which I deferred, and column `rationale` gives the reason in each case. My deferral rate is 22 percent, concentrated in cases where I could not resolve the boundary from a single section.
>
> **Limitation:** I triaged by conspicuousness in the first two weeks and by endpoint impact afterwards, once I understood that a merge on a heavily connected axon costs far more than a split on a terminal branch. The first eighty rows would be triaged differently now.

The fourth line is the one most people delete, and it is the strongest line in the caption. It shows a learner who changed method for a stated reason, which is the thing a reviewer is trying to detect and cannot detect from polished work.

**The feedback exchange.** Maya sends it with a specific request: "I'm deciding whether to include the first eighty rows at all. The criterion is whether they weaken the competency claim. This is near-final and I need an answer by Friday." Her reviewer answers the question asked: "Keep them, but move the limitation line above the verifiable line, because right now a skimming reviewer sees the deferral rate before they see that you know why it changed."

**The revision, logged.** Maya reorders the caption and adds one sentence to the reflection note. Her revision log entry reads: `2026-03-04 — reordered caption lines after peer review (S. Adeyemi): limitation ahead of verification, so the method change is read before the numbers. Kept rows 1-80; removing them would have hidden the change that is the point of the artifact.` The log entry names the reviewer, the change, and the reasoning for the change that was not made. That last part is what a reviewer reads as judgment rather than compliance.

## Studio activity: capstone evidence review board
{: #studio-activity}
**Scenario:** You are preparing your final portfolio for a competitive research opportunity. Assume the reviewer spends two minutes on the first pass and opens exactly one artifact.

**Tasks**
1. Select 6-10 artifacts and map each to one competency claim, cutting duplicates.
2. Write four-line evidence captions and reflection notes, with line three naming something verifiable.
3. Receive peer review against rubric criteria, having stated a decision, a criterion, and a deadline for each artifact.
4. Produce a revision plan with priorities and deadlines, ordered by effect on what the portfolio proves.

**Expected outputs**
- Portfolio map (artifact -> competency).
- Reflection set.
- Peer feedback log.
- Final revision plan.
- Permission and provenance check across all artifacts.

## Assessment rubric
- **Minimum pass:** portfolio claims are evidence-backed; reflection identifies at least one meaningful revision loop; feedback is incorporated with clear changes; contributions in group work are stated explicitly.
- **Strong performance:** demonstrates cross-module synthesis and transfer, highlights uncertainty and correction with technical maturity, communicates a future growth plan with concrete milestones, and includes at least one artifact whose earlier wrong version is shown alongside the correction and its reason.
- **Common failure to flag:** artifact dump with weak competency mapping, reflection limited to narrative without analytical depth, and minimal response to peer critique. Also flag portfolios where every caption line three is missing, since that is the difference between a folder and evidence.

## Common errors and how to recover
- **You have twenty artifacts and no claims.** Stop curating. Write the six competency claims first, then delete every artifact that does not map to one. The deletion is the work, and a reviewer will read a tight set as judgment rather than as a thin record.
- **A reviewer gave you only typo corrections.** That is a symptom of the request, not the reviewer. Send it again with a stated decision, criterion, stage, and deadline. Most reviewers give the cheapest useful feedback available; a narrow question makes substantive feedback the cheapest option.
- **Your best artifact contains an error you found after submission.** Do not quietly replace it. Add a dated note stating the error, its effect on the claim, and the correction. A visible correction strengthens the portfolio; a silent replacement, if noticed, destroys it.
- **The work was collaborative and you cannot claim it cleanly.** Write the contribution statement at the level of the specific task: what you built, what you were given, whose code you called. Ask your collaborators to confirm the wording. Vague attribution is read as inflation, which costs more than the smaller honest claim.
- **You cannot publish an artifact because the data are unpublished or restricted.** Substitute a version built on a public dataset with the same method, and say in the caption that the original was run on restricted data. The competency claim survives; the specific result does not need to.
- **The portfolio has not been updated in a year and no longer matches what you can do.** Set a fixed review date twice a year and change one thing at each: retire the weakest artifact, add the newest, update the README. A portfolio maintained on a schedule stays current at a fraction of the cost of periodic rebuilding.

## What this module does not cover
- **How to produce the technical artifacts themselves.** Annotation, proofreading, QC metrics, and graph analysis are taught across the [technical track]({{ '/technical-training/' | relative_url }}), particularly [Segmentation and Proofreading]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}) and [Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }}).
- **Where the portfolio is pointed.** Program and role selection, outreach, and application timing are [Module 24]({{ '/modules/module24/' | relative_url }}).
- **Manuscript and talk preparation.** See [Module 17]({{ '/modules/module17/' | relative_url }}) and [Module 22]({{ '/modules/module22/' | relative_url }}).
- **Reproducibility engineering.** Environment pinning, data formats, and FAIR release practice are [Module 21]({{ '/modules/module21/' | relative_url }}); this module only checks that versions are recorded.
- **Authorship disputes and credit conflicts.** Where a contribution statement is contested rather than merely unclear, that is [Module 19]({{ '/modules/module19/' | relative_url }}).
- **Legal advice on data licensing.** The permission check here is a prompt to ask, not a substitute for the dataset's own terms or your institution's guidance.

## Teaching resources
- Career planning context: [Module 24]({{ '/modules/module24/' | relative_url }})
- Presentation context: [Module 22]({{ '/modules/module22/' | relative_url }})
- Mentorship support: [Ask-an-Expert]({{ '/tools/ask-an-expert/' | relative_url }})
- Framework context: [Research Incubator Model]({{ '/models/' | relative_url }})
- Provenance reference: [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
- Differentiation guidance: [Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }})

## Quick practice prompt
Choose one artifact and write its four lines: one competency claim it supports, what you did versus what you were given, one thing a reviewer can verify and where, and one limitation with the revision you would make next.
