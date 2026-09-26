---
layout: page
title: "10-week course map"
permalink: /teaching/syllabi/10-week/
slug: syllabi-10-week
track: core-concepts-methods
content_type: delivery
description: "A quarter-length connectomics course built from the five packaged sessions, selected unit labs, four module kits and three Pathways workshops."
---

This map runs **20 meetings of 90 minutes**, two a week. It uses the four-session block,
the Ethics and Governance session, several technical-unit labs, four module kits and three
Professional Pathways workshops. Each learner carries one study question from the first
week to a final report, talk and portfolio. See the
[syllabus maps overview]({{ '/teaching/syllabi/' | relative_url }}) for assumptions and
how to adapt the meeting pattern.

**Time budget.** 30 contact hours, plus about 30 outside hours (1,825 minutes). The
outside load runs from 2 to 4 hours a week, so the full load is about 5–7 hours a week. That
is roughly one outside hour per contact hour. A two-to-one ratio needs about 60 outside
hours, and no set of existing materials closes that gap on its own. The largest additions:

- the full [Unit 01 lab]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}#rubric)
  (60 minutes), the rest of [Unit 09]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
  (90 minutes) and the [Unit 03]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }})
  QA lab (90 minutes, public viewer): 4 hours;
- the [Module 07]({{ '/teaching/sessions/module07/' | relative_url }}) and
  [Module 10]({{ '/teaching/sessions/module10/' | relative_url }}) kits as take-homes
  (4 hours each by the kits' own estimate; Module 10 needs Python and NetworkX): 8 hours;
- reading from Units 06 and 07 (3.5 hours) and Unit 03 sections 3–4 (1 hour).

Together these bring the outside total to about 47 hours. The rest has to come from a
longer final report or more reading.

## At a glance

| Week | Session(s) | Pre-work | Artifact | Links |
|---|---|---|---|---|
| 1 | A: Session 1 Introduction · B: Pathways, Orientation | Lab norms (25 min) | Study brief v1; expectations list | [Plan]({{ '/teaching/lectures/connectomics-01-introduction/' | relative_url }}#teach-a-90-minute-session) · [Orientation]({{ '/teaching/pathways/orientation/' | relative_url }}) |
| 2 | A: Session 2 Synapse Detection · B: Unit 02 scale-selection lab | Synapse Detection (20 min); Unit 02 (90 min) | Audit plan and revised brief; scale memo | [Plan]({{ '/teaching/lectures/synapse-detection/' | relative_url }}) · [Unit 02]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }}) |
| 3 | A: Session 3 Tools and Methods · B: Pathways, Resilient STEM Scholar | Unit 03 §1–2 (60 min); two short readings (15 min) | Methods record; failure diagnosis | [Plan]({{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }}#teach-a-90-minute-session) · [Resilient]({{ '/teaching/pathways/resilient-scholar/' | relative_url }}) |
| 4 | A: Unit 05 consensus studio · B: **MICrONS real-data lab** | Unit 05 (150 min); Unit 04, read in week 3 | Consensus sheet; methods record and drift note | [Unit 05]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}) · [MICrONS lab]({{ '/notebooks/microns-lab/' | relative_url }}) |
| 5 | A: Unit 08 proofreading plan · B: Session 4 Algorithms and Applications | Unit 08 §1–4 (120 min) | Proofreading plan; analysis card | [Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}) · [Plan]({{ '/teaching/lectures/connectomics-03-algorithms-and-applications/' | relative_url }}#teach-a-90-minute-session) |
| 6 | A: Ethics and Governance · B: Pathways, Savvy Researcher | Ethics reading (25 min); career mechanics (25 min) | Governance note; authorship memo; project proposal | [Ethics]({{ '/teaching/lectures/ethics-and-governance/' | relative_url }}) · [Savvy]({{ '/teaching/pathways/savvy-researcher/' | relative_url }}) |
| 7 | A: Module 17 writing kit · B: Module 19 peer-review kit | Two concept sets (60 min) | Claim-evidence matrix; structured review | [Kit 17]({{ '/teaching/sessions/module17/' | relative_url }}) · [Kit 19]({{ '/teaching/sessions/module19/' | relative_url }}) |
| 8 | A: Module 22 presentation kit · B: Project studio, peer review | Concept set (30 min); full report draft | Four-slide deck; peer review given and received | [Kit 22]({{ '/teaching/sessions/module22/' | relative_url }}) · [Kit 19 form]({{ '/teaching/sessions/module19/' | relative_url }}) |
| 9 | A and B: Module 25 portfolio kit | Concept set and artifact gathering (60 min) | Portfolio map, captions, revision plan | [Kit 25]({{ '/teaching/sessions/module25/' | relative_url }}) |
| 10 | A and B: Final talks | Talk preparation (30 min) | Final report, talk and portfolio | [Kit 25]({{ '/teaching/sessions/module25/' | relative_url }}#assessment) |

## Week by week

### Week 1: What can a wiring diagram establish?

**A. Session 1, Introduction to Connectomics.**
[Timed plan and slides]({{ '/teaching/lectures/connectomics-01-introduction/' | relative_url }}#teach-a-90-minute-session) ·
[Worksheet]({{ '/teaching/lectures/introduction-activity/' | relative_url }}) ·
[Model responses]({{ '/teaching/lectures/introduction-answers/' | relative_url }})

**B. Pathways workshop 1, Orientation** (MERIT: selection and orientation).
[Plan]({{ '/teaching/pathways/orientation/' | relative_url }}) ·
[Worksheet]({{ '/teaching/pathways/orientation-activity/' | relative_url }}) ·
[Model responses]({{ '/teaching/pathways/orientation-answers/' | relative_url }})

**Before class.** A: none, since this is the first meeting. B:
[Lab norms]({{ '/hidden-curriculum/lab-norms/' | relative_url }}) (25 minutes).

**Artifacts.** A study brief: a structural endpoint with a denominator, comparison and
explicit non-claim. An expectations list and a plan for the week-four check-in.

**Feedback.** Score the brief on the Introduction key's
[four-dimension rubric]({{ '/teaching/lectures/introduction-answers/' | relative_url }}#feedback-guide).
Score the expectations list on the Orientation
[feedback rubric]({{ '/teaching/pathways/orientation-answers/' | relative_url }}#feedback-rubric).

**After class (135 minutes).** Read
[Unit 01]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}) (90 minutes).
Add a null model, one confound and a sharper non-claim to the brief, using lab steps 5–7
of Unit 01 (30 minutes). Start the Orientation follow-through (15 minutes).
**Week total:** 3 contact hours, 160 outside minutes.

### Week 2: What errors could change the result, and what scale does the question need?

**A. Session 2, Synapse Detection.**
[Timed plan and slides]({{ '/teaching/lectures/synapse-detection/' | relative_url }}) ·
[Worksheet]({{ '/teaching/lectures/synapse-detection-activity/' | relative_url }}) ·
[Model responses]({{ '/teaching/lectures/synapse-detection-answers/' | relative_url }})

**B. Unit 02 lab, scale-selection memo.** Run sections 1–4 of the
[lab]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }}) in pairs
(60 minutes), then compare rejected modalities across the room (25 minutes). Sections 5–7
become homework.
[Slides]({{ '/technical-training/slides/02-brain-data-across-scales/' | relative_url }})

**Before class.** A: [Synapse Detection]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }}),
the opening section and sections 1, 2 and 7, on localization, partner assignment and
evaluation units (20 minutes). Bring the brief. B: [Unit 02]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }})
sections 1–5 (90 minutes).

**Artifacts.** An audit plan and a revised brief that names its most damaging error. A
two-page scale-selection memo.

**Feedback.** Synapse Detection
[rubric]({{ '/teaching/lectures/synapse-detection-answers/' | relative_url }}#feedback-guide).
Unit 02 [rubric]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }}#rubric);
weight the Resolution defense and Rejections rows most heavily.

**After class (75 minutes).** Finish the audit plan (30 minutes) and memo sections 5–7
(45 minutes). **Week total:** 3 contact hours, 185 outside minutes.

### Week 3: Can another person reproduce the number in your figure?

**A. Session 3, Tools and Methods.**
[Timed plan and slides]({{ '/teaching/lectures/connectomics-02-tools-and-methods/' | relative_url }}#teach-a-90-minute-session) ·
[Worksheet and offline query]({{ '/teaching/lectures/tools-and-methods-activity/' | relative_url }}) ·
[Model responses]({{ '/teaching/lectures/tools-and-methods-answers/' | relative_url }})

**B. Pathways workshop 2, The Resilient STEM Scholar** (MERIT: skill development). Two
weeks after Orientation. The week-four check-in is still ahead, so open by asking who
has scheduled it.
[Plan]({{ '/teaching/pathways/resilient-scholar/' | relative_url }}) ·
[Worksheet]({{ '/teaching/pathways/resilient-scholar-activity/' | relative_url }}) ·
[Model responses]({{ '/teaching/pathways/resilient-scholar-answers/' | relative_url }})

**Before class.** A: [Unit 03]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }})
sections 1–2, the preparation chain and artifact catalog (60 minutes). Bring the revised
brief and audit. B: *The test* on the
[belonging page]({{ '/hidden-curriculum/belonging/' | relative_url }}) and the four-part
mistake script on the [lab norms page]({{ '/hidden-curriculum/lab-norms/' | relative_url }})
(15 minutes).

**Artifacts.** A recoverable methods record and a storage estimate. A failure diagnosis
and a bad-week report. The private verdict stays with the learner.

**Feedback.** Tools and Methods
[rubric]({{ '/teaching/lectures/tools-and-methods-answers/' | relative_url }}#feedback-guide):
no zero in provenance or interpretation. Resilient Scholar
[rubric]({{ '/teaching/pathways/resilient-scholar-answers/' | relative_url }}#feedback-rubric).

**After class (150 minutes).** Finish the methods record (20 minutes). Read
[Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
sections 1–5 before week 4B (120 minutes). Keep the EXPECTED-line follow-through for one
week (about 10 minutes). **Week total:** 3 contact hours, 225 outside minutes.

### Week 4: What does the image support, and what does a reproducible query cost?

**A. Unit 05 studio, ultrastructure consensus round.** Run the 75-minute
[studio]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}) with a
15-minute debrief on disagreement types.
[Slides]({{ '/technical-training/slides/05-neuronal-ultrastructure/' | relative_url }}).
*Preparation:* the studio needs a borderline patch set. Draw it from the unit's visual
training set or a public volume. Use short z-stacks, not single images, as the Facilitator
Guide requires.

**B. MICrONS real-data lab.**
The [MICrONS real-data lab]({{ '/notebooks/microns-lab/' | relative_url }}) is the
real-data version of Sessions 3 and 4. It reads static public exports pinned to
materialization v1507, so no account is needed. It checks file hashes, applies stated
inclusion rules to 2,070 proofread cells, compares reciprocity with three nulls, and
writes a methods record. Learners need a laptop with Python 3.11–3.13, about 90 MB of
downloads and 2 GB of free memory. A run took under a minute on the test machine and can
take several minutes on an older laptop. Have learners install the requirements before
class.

1. Check installs and open the notebook; pair anyone whose setup fails with someone
   whose works (15 minutes).
2. Run the notebook and compare the key numbers with the archived outputs on the lab
   page (35 minutes, pairs).
3. Write the methods record into the study brief and read the v1412 → v1507 drift
   section: which cells a stale root-ID join would silently lose (25 minutes).
4. Debrief: which null should the headline use, and why the uniform null overstates
   the effect (15 minutes).

**Offline fallback** (no network or no Python): read the archived executed notebook on
the lab page instead of running it, or run Unit 04 lab Part B, the capacity plan (no
data), plus the Session 3 offline query on the
[worksheet]({{ '/teaching/lectures/tools-and-methods-activity/' | relative_url }})
under a second inclusion threshold.

**Before class.** A: [Unit 05]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }})
sections 1–4 (150 minutes). B: Unit 04, read in week 3.

**Artifacts.** A consensus annotation sheet, a disagreement log and one rubric revision. A
methods record with the v1507 version, inclusion rules and file hashes, and a note on
what the v1412 → v1507 drift would do to a stale join.

**Feedback.** Unit 05
[assessment rubric]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}#assessment-rubric).
For B, use the Unit 04 [rubric]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}#rubric)
rows for storage, compute and labor. Apply its Version discipline row to the two
thresholds.

**After class (50 minutes).** Finish the disagreement log (20 minutes) and methods record
(30 minutes). **Week total:** 3 contact hours, 200 outside minutes.

### Week 5: How much proofreading does the claim need, and does it beat the null?

**A. Unit 08 lab Part B, proofreading plan.** Write the plan for 200 cells from the
[lab]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}) (60 minutes),
then peer-review it against the rubric (30 minutes). Part A is omitted, because it needs a
proofreading-capable viewer and account. Learners take fix times from the unit's worked
figures and label them as assumed, not measured.
[Slides]({{ '/technical-training/slides/08-segmentation-and-proofreading/' | relative_url }})

**B. Session 4, Algorithms and Applications.**
[Timed plan and slides]({{ '/teaching/lectures/connectomics-03-algorithms-and-applications/' | relative_url }}#teach-a-90-minute-session) ·
[Worksheet and offline analysis]({{ '/teaching/lectures/algorithms-and-applications-activity/' | relative_url }}) ·
[Model responses]({{ '/teaching/lectures/algorithms-and-applications-answers/' | relative_url }})

**Before class.** A: [Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
sections 1–4 (120 minutes). B: bring the brief, audit and methods record.

**Artifacts.** A two-page proofreading plan. An analysis card.

**Feedback.** Unit 08 [rubric]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}#rubric).
Without Part A, the Budget row's "derived from measured timing" cannot be met, so grade
stated assumptions and sensitivity instead. Algorithms and Applications
[rubric]({{ '/teaching/lectures/algorithms-and-applications-answers/' | relative_url }}#feedback-guide).

**After class (60 minutes).** Finish the plan (45 minutes) and the analysis card
(15 minutes). **Week total:** 3 contact hours, 180 outside minutes.

### Week 6: Who may use the data, and who gets credit?

**A. Ethics and Governance** (optional fifth session of the block, included here).
[Timed plan and slides]({{ '/teaching/lectures/ethics-and-governance/' | relative_url }}) ·
[Worksheet]({{ '/teaching/lectures/ethics-and-governance-activity/' | relative_url }}) ·
[Model responses]({{ '/teaching/lectures/ethics-and-governance-answers/' | relative_url }})

**B. Pathways workshop 7, The Savvy Researcher** (MERIT: advanced research). Three weeks
after Resilient. Scheduled after Ethics so the proofreading-credit rule feeds the
authorship memo. Open with the Resilient follow-through, the session this cohort ran last.
[Plan]({{ '/teaching/pathways/savvy-researcher/' | relative_url }}) ·
[Worksheet]({{ '/teaching/pathways/savvy-researcher-activity/' | relative_url }}) ·
[Model responses]({{ '/teaching/pathways/savvy-researcher-answers/' | relative_url }})

**Before class.** A: [Ethics and Governance]({{ '/content-library/connectomics/ethics-and-governance/' | relative_url }})
(25 minutes). B: [career mechanics]({{ '/hidden-curriculum/career-mechanics/' | relative_url }})
sections 1, 2 and 5 (25 minutes).

**Artifacts.** A license audit table and governance note. An authorship memo and system
map. A one-page final project proposal naming the question, the artifacts it will reuse and
the claim it will not make.

**Feedback.** Ethics
[rubric]({{ '/teaching/lectures/ethics-and-governance-answers/' | relative_url }}#feedback-guide):
no zero in license accuracy or handling of uncertainty. Savvy Researcher
[rubric]({{ '/teaching/pathways/savvy-researcher-answers/' | relative_url }}#feedback-rubric).
For the proposal, check three things: the question matches the brief's endpoint, every
reused artifact is named, and a non-claim is stated.

**After class (120 minutes).** Add the license, ethics-statement location and credit
model to the brief (15 minutes). Write the proposal (45 minutes). Read
[Unit 09]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
sections 1–2 on graph construction and null models (60 minutes).
**Week total:** 3 contact hours, 170 outside minutes.

### Week 7: Can a reader trace every claim to its evidence?

**A. Module 17 kit, scientific writing.** Run activity steps 1–4. Learners may use the
kit's scenario or their own analysis card; step 5, the reviewer response, is homework.
[Session kit]({{ '/teaching/sessions/module17/' | relative_url }}) ·
[Module page]({{ '/modules/module17/' | relative_url }})

**B. Module 19 kit, peer review and scientific ethics.** Run all four steps on the kit's
preprint scenario.
[Session kit]({{ '/teaching/sessions/module19/' | relative_url }}) ·
[Module page]({{ '/modules/module19/' | relative_url }})

**Before class.** A: Module 17 concept set (30 minutes). B: Module 19 concept set (30 minutes).

**Artifacts.** A claim-evidence matrix and methods paragraph. A structured review form and
decision memo.

**Feedback.** Kit 17 [assessment]({{ '/teaching/sessions/module17/' | relative_url }}#assessment)
and Kit 19 [assessment]({{ '/teaching/sessions/module19/' | relative_url }}#assessment)
minimum and strong criteria.

**After class (120 minutes).** Draft the final report: results and methods, at most
1,500 words, built from the brief, audit, methods record and analysis card.
**Week total:** 3 contact hours, 180 outside minutes.

### Week 8: Can someone outside the work follow it?

**A. Module 22 kit, scientific writing and presentation.** Learners build the four-slide,
three-minute talk from their own project. They deliver it and answer two questions in
groups (kit steps 1–4). Week 10 uses this format.
[Session kit]({{ '/teaching/sessions/module22/' | relative_url }}) ·
[Module page]({{ '/modules/module22/' | relative_url }})

**B. Project studio: peer review.** Pairs exchange report drafts and review each other
with the Module 19 structured review form from week 7 (60 minutes). Each author then
writes a response in quote, response and location format (30 minutes). This meeting is
all learner judgment and needs no new materials.

**Before class.** A: Module 22 concept set (30 minutes). B: bring a complete report draft.

**Artifacts.** A four-slide deck. A peer review given and a response to the one received.

**Feedback.** Kit 22 [assessment]({{ '/teaching/sessions/module22/' | relative_url }}#assessment).
For the review, reuse the Kit 19 minimum criteria: comments are specific and tied to
evidence, and the recommendation is consistent with the findings.

**After class (135 minutes).** Revise the report (90 minutes) and the deck (45 minutes).
**Week total:** 3 contact hours, 165 outside minutes.

### Week 9: What does your portfolio prove?

**A and B. Module 25 kit, portfolio, feedback and final project.** In A, run steps 1–2:
select 6–10 artifacts, map each to one competency and write captions. In B, run steps 3–4:
peer review against the rubric and a dated revision plan. Use the last 20 minutes of B for
a 90-second talk run-through in pairs.
[Session kit]({{ '/teaching/sessions/module25/' | relative_url }}) ·
[Module page]({{ '/modules/module25/' | relative_url }})

**Before class.** Module 25 concept set (30 minutes). Gather every artifact from weeks 1–8
into one folder (30 minutes).

**Artifacts.** A portfolio map, reflection set, peer feedback log, revision plan and
permission and provenance check.

**Feedback.** Kit 25 [assessment]({{ '/teaching/sessions/module25/' | relative_url }}#assessment).
Flag portfolios that dump artifacts without competency mapping.

**After class (180 minutes).** Captions and reflections (60 minutes), revisions from the
plan (90 minutes), talk rehearsal (30 minutes). **Week total:** 3 contact hours, 240 outside minutes.

### Week 10: Final talks

**A and B. Three-minute talks** in the Module 22 format: four slides and a visible timer.
Each talk gets two audience questions, and the speaker names each question's type before
answering. At about seven minutes per learner, two meetings hold roughly 24 learners.
With a larger cohort, run parallel rooms. The audience writes one question per talk, which
keeps the meetings on learner judgment rather than listening.

**Before class.** Talk preparation (30 minutes).

**Artifacts.** The final report, talk and revised portfolio, due at the end of the week.

**Feedback.** Kit 25 [assessment]({{ '/teaching/sessions/module25/' | relative_url }}#assessment)
for the portfolio. For the report and talk, apply the four-dimension rubric from the
Introduction key to the final claim. Also check that every number carries its version or
threshold.

**After class (90 minutes).** Final portfolio submission. **Week total:** 3 contact hours,
120 outside minutes.

## What this map uses and omits

**Uses.** All four sessions of the [block]({{ '/teaching/sequence/' | relative_url }}),
plus Ethics and Governance. Lab work from Units 02, 04 (Part B), 05 and 08 (Part B), and
reading from Units 01, 03, 04, 05, 08 and 09. Module kits 17, 19, 22 and 25. Pathways
workshops 1 Orientation, 2 The Resilient STEM Scholar and 7 The Savvy Researcher.

**Pathways omitted.** Seven workshops are left out: STEM Identity and Purpose, Charting
Your Course, Building Your STEM Entourage, Communicating Science I and II, Professional
Conduct and Future Forward. Ten weeks allow at most four workshops at two-week spacing.
The [hub]({{ '/teaching/pathways/' | relative_url }}) names these three as the short
version, since they cover unstated expectations, misread failure and late credit. Make
two swaps if they apply. If the cohort is about to join active labs, run Professional
Conduct in week 6 in place of Savvy Researcher. If you can add a fourth slot, use STEM
Identity and Purpose in week 2 in place of the Unit 02 lab; the hub asks for it in the
first month.

**Technical work omitted.** The Unit 06 and 07 calibration labs are omitted. They need
instructor-built patch sets and work best repeated. The Unit 03 viewer lab and the Unit 09
analysis lab are omitted because both need live data. Part A of Units 04 and 08 is omitted
for the same reason.

**Module kits omitted.** The other 21 kits are left out for time or overlap. Missing
files are no longer a reason: every material a kit names now resolves, either to synthetic files under
`assets/kits/` or, for Modules 04 and 05, to a recipe for an instructor-built patch set.
Two kits fit if you can make room:

- The [Module 07 kit]({{ '/teaching/sessions/module07/' | relative_url }}) triages a
  synthetic 45-flag error report and computes release metrics with a script, and it has
  [model responses]({{ '/teaching/answers/module07/' | relative_url }}). Its 60–75 minute
  studio can replace the Unit 08 Part B plan in week 5A if you want learners to compute
  release metrics rather than budget labor. Grade the release memo in its place.
- The [Module 10 kit]({{ '/teaching/sessions/module10/' | relative_url }}) graph report
  works as a take-home after Session 4 for learners with Python.

The others either overlap work already on this map or need more time than ten weeks
allow. The [16-week map]({{ '/teaching/syllabi/16-week/' | relative_url }}#what-this-map-uses-and-omits)
gives the reason for each kit.

## Suggested grading weights

This is a suggestion, not a validated scheme. Every rubric it draws on is a local teaching
rubric.

| Component | Weight | Evidence |
|---|---|---|
| Carried-forward study package | 30% | Brief, audit, methods record, analysis card and governance note, graded on the revision rather than the first worksheet |
| Technical labs | 20% | Scale memo, consensus sheet, MICrONS methods record and drift note, proofreading plan |
| Writing and review | 15% | Claim-evidence matrix, structured review, peer review given |
| Pathways workshops | 10% | Shareable artifact submitted and follow-through attempted; complete or incomplete, with private parts never collected |
| Final report, talk and portfolio | 25% | Module 25 criteria and the final claim scored on the four-dimension rubric |

[Syllabus maps]({{ '/teaching/syllabi/' | relative_url }}) · [16-week map]({{ '/teaching/syllabi/16-week/' | relative_url }}) · [Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }})

Syllabus map: CC BY-SA 4.0, NeuroTrailblazers.
