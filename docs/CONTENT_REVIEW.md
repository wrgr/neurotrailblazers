# Content depth and pedagogical review

*Reviewed August 2026. Scope: the learner-facing site — technical-training units,
modules, tracks, teaching materials, dictionary, worksheets, and the content library.*

---

## Summary

The site has a **strong reference layer and a hollow instructional layer.**

The content library is genuinely good: 2,000–4,000 word pages with real numbers,
worked examples, decision protocols, and honest limitations. Someone who reads
`content-library/proofreading/metrics-and-qa.md` learns how to compute VI and ERL and
when each misleads.

The pages learners actually land on were not like that. The technical-training units —
described in `_data/technical_track.yml` as the "canonical open connectomics course" —
averaged around 700 words each and consisted almost entirely of noun-phrase bullets
that named topics without teaching them. A representative line from the original
Unit 03:

> **Tissue preparation:** Stabilize ultrastructure while minimizing shrinkage and
> extraction artifacts.

That sentence states a goal. It contains no protocol, no reagent, no number, no failure
signature, and no way to tell whether you did it. A learner cannot act on it, and an
instructor cannot teach from it. The same pattern ran through nearly every unit, the
track pages, the teaching hub, and all 25 module worksheets.

**Diagnosis: these were specifications, not instruction.** They read like a curriculum
design document — a correct and complete list of what a course *should* contain —
published as if it were the course.

That distinction also answers the second question in the brief, about whether the
approach scales to the intended audience. It does not, and the reason is specific.

---

## Why the bullet-scaffold approach does not scale here

Connectomics has a structural teaching problem that most technical curricula do not:
**the core skills are perceptual and judgemental rather than procedural.** Reading an EM
image, deciding whether a segmentation is trustworthy, choosing a null model — none of
these can be transmitted by explanation. A learner who can recite the three criteria for
calling a synapse will still, on their first real patch, call a tangentially cut
membrane a synapse.

A bullet list of topic names is the *least* effective possible format for that kind of
learning, because it provides:

- **no worked example** — so no model of expert reasoning to imitate;
- **no numbers** — so no way to calibrate what "thin" or "expensive" or "too noisy" means;
- **no retrieval practice** — so nothing that converts recognition into recall;
- **no feedback loop** — so a learner cannot discover they are wrong;
- **no answer key** — so a learner working alone, which is most of the intended audience, cannot self-assess at all.

The audience makes this worse rather than better. The site's own personas span a
first-generation undergraduate, a graduate student bridging fields, an industry AI
researcher, and a faculty mentor. Terse scaffolding works acceptably for the reader who
already knows the field and is using the page as an index. It fails hardest for the
reader with the least context — which is the audience the program exists to serve.

**The scaling verdict:** the *structure* scales; the *content depth* did not. Three
tracks, 25 modules, 10 technical units, and a rich content library is a sound
architecture. What was missing was the instructional layer bridging the reference depth
to the learner, and the self-assessment machinery that lets a learner working alone
find out whether they have actually learned anything.

---

## What was changed

### The authoring standard now applied

Every rewritten unit follows the same template, chosen because each element addresses
one of the five gaps above:

| Section | Purpose |
|---|---|
| **Before you start** | Time, prerequisites, what you need, what you finish with. Lets a learner decide whether to start. |
| **What you'll be able to do** | Observable, testable competencies — not "understand X". |
| **Numbered content sections** | Real numbers, protocols, decision tables. Every claim actionable. |
| **Check yourself** | Retrieval-practice questions with answers in collapsed `<details>`. The answers teach reasoning, not just the fact. |
| **Worked example** | One expert judgement narrated in full, including the uncertainty. |
| **Lab** | A graded exercise producing an artifact, with a rubric at three levels. |
| **Common errors and how to recover** | Each error paired with a specific recovery action. |
| **What this unit does not cover** | Honest scope, with pointers. |
| **Go deeper** | Links into the content library — the reference layer, now properly connected. |

Two design choices are worth calling out because they are what make the material usable
without an instructor:

1. **Answers are included, in collapsed disclosure elements.** A learner alone can test
   themselves honestly. The answers are written to explain the reasoning and generalize
   the principle, not merely to confirm the fact.
2. **Rubrics have three levels — Not yet / Proficient / Strong.** "Strong" is
   consistently defined as *doing the thing that separates a practitioner from someone
   who followed the steps*: naming the assumption, measuring calibration rather than
   accuracy, reporting the error band.

### Depth delivered

| Page | Before | After |
|---|---|---|
| Unit 01 — Why Map the Brain | 700 | 3,386 |
| Unit 02 — Brain Data Across Scales | 681 | 3,169 |
| Unit 03 — EM Prep and Imaging | 673 | 3,897 |
| Unit 04 — Volume Reconstruction Infrastructure | 644 | 3,652 |
| Unit 05 — Neuronal Ultrastructure | 1,486 | 3,647 |
| Unit 06 — Axons and Dendrites | 673 | 2,947 |
| Unit 07 — Glia | 569 | 2,462 |
| Unit 08 — Segmentation and Proofreading | 838 | 3,483 |
| Unit 09 — Connectome Analysis and NeuroAI | 1,029 | 3,701 |
| Atlas — Connectomics Reference | 544 | 1,689 |
| Facilitator Guide | 282 | 2,169 |
| Education Models (MERIT) | 201 | 1,664 |
| Connectome Quality notebooks | 58 | 1,015 |
| Dictionary | 40 one-line terms | 127 entries with typical values, practical consequence, and common confusions |
| Module worksheets (×25) | ~123 words of blank template each | ~1,054 words each of real task content, generated from module pages |
| Modules 12-15, 22-25 | 706-876 words each | 3,090-3,596 each |
| Journal club corpus | 1 of 200 papers reachable | all 200 |
| MRI connectomics reading list | 4 papers (index claimed 12) | 10 |
| start-here first-run experience | self-referential checklist | a first hour ending in a written artifact, plus a track decision table |
| README | documented a directory that does not exist | current layout, scripts, and which files are generated |
| Journal papers: Computer Vision & ML | did not exist (linked from three pages) | 3,350 |
| Journal papers: Network Analysis & Statistics | did not exist (linked from two pages) | 3,303 |

Word count is a proxy, not the point. What changed substantively:

- **Numbers everywhere they were missing.** Structure sizes, resolutions, staining
  protocols, dose tradeoffs, data volumes, GPU-days, storage multipliers, proofreading
  hours. A learner can now estimate rather than gesture.
- **Worked examples with the reasoning shown.** Unit 01 repairs a vague research
  question in four explicit moves. Unit 05 narrates a full evidence chain across four
  cue families. Unit 09 works a reciprocity analysis whose effect size collapses from
  2.9× to non-significant as the null model strengthens — the same data supporting
  either "p < 10⁻⁶" or "no detectable effect" depending on a choice made before any test
  was run.
- **Cost reasoning, which was entirely absent.** Merge errors versus split errors,
  data-loss versus labour artifacts, triage by endpoint impact rather than
  conspicuousness. This is the field's central operational logic and the units did not
  previously mention it.
- **Calibration as an explicit skill.** Confidence tiers are defined operationally by
  cue count and cue independence, and Unit 06's lab scores accuracy *within* the
  high-confidence tier. The material now argues, and demonstrates, that calibration is
  worth more than raw accuracy in production annotation.
- **Reproducibility made concrete.** Materialization versions, root-ID instability, and
  version-pinned queries appear in Unit 04, Unit 09, the notebook path, and the
  dictionary — because analysis against an unpinned segmentation is the most common
  silent correctness bug in this field.
- **Learner paths.** Each track now carries a time estimate, an ordered sequence with
  per-step outcomes, capability-based completion criteria, and the common detours.

### The worksheet generator, rebuilt

`scripts/generate_module_teaching_materials.rb` previously emitted worksheets containing
the first paragraph of three module sections plus three blank fields. It now pulls the
full studio-activity scenario and task steps, the core workflow as a tick-list, the
learning questions, the pre-class preparation, the session timing table, and the complete
rubric — and adds an evidence-and-reasoning table, an operational confidence scale, a
misconception self-check, a self-assessment prompt, and a structured peer-review section.
Worksheets went from ~123 words of blank template to ~730 words of usable task material.

The generator's section matching was also made resilient to the heading variations across
module pages ("60-minute tutorial run-of-show" vs "Detailed run-of-show (90 minutes)",
"Studio activity" vs "Studio activity: ..."), which had been silently degrading five
modules' decks to "See module page for details".

### The facilitator guide, rewritten around the actual constraint

The previous guide gave a session template and a materials list. It did not address the
thing that determines whether this material works: that half of contact time must be
spent on learner judgement compared against a reference, because the skills are
perceptual. The rewritten guide covers session design, differentiation across the four
personas by *scaffolding and entry point* rather than by content, calibration-based
assessment, a self-study path for learners working alone, and the failure modes specific
to this material — including the observation that a lecture-only delivery will feel
good, review well, and produce very little transferable capability.

---

## What has not been addressed

Stated plainly so the remaining scope is visible. Items 1, 3, 4, 5, and 6 from the
original review are now closed; what follows is what is genuinely still open.

**1. Eight module pages remain between 1,100 and 1,500 words** — modules 04, 06, 08-11,
20, and 21. They are no longer scaffolding (each has real concept content, guardrails,
and a working studio activity) but they sit below the 2,000-2,600 band the rest of the
library now occupies. Modules 06, 08, 10, and 11 are the ones a learner is most likely to
land on from a technical unit, so they are the priority within this set.

**2. The technical units are not evenly matched to the modules they overlap.** The
`mapping_note` fields in `_data/technical_track.yml` describe the relationship
accurately, but no page yet tells a learner working through, say, module 08 that Unit 09
is the depth behind it and covers the null-model reasoning the module compresses. The
modules-vs-units table on `/modules/` explains the two sequences in general; a per-module
pointer would be better.

**3. Figure captions now teach, but nobody has checked them against the images.** The
captions were rewritten by an agent that could not see the images, so they are phrased as
instructions to look for something rather than assertions about what is present, and they
are grounded in each unit's own content. That is honest but it is not verified. A
subject-matter reviewer with the source slides open could improve them materially,
particularly in `09-connectome-analysis-neuroai.md`, where twelve of the source captions
were pure provenance stubs.

**4. Two of the site's data pipelines are unowned.** `_data/journal_papers.yml` was
generated with malformed indentation that made 199 of its 200 papers unreachable, and the
journal-club dimension filter had drifted to the point where five of its eleven options
matched no paper. Both are fixed, and the filter is now generated from the corpus so it
cannot drift again — but the generator that produced the broken YAML is not in this repo,
so the same corruption could return on the next regeneration. Whoever owns that pipeline
should add a `papers.size` assertion to it.

**5. The bibliometrics assets under `assets/analysis/` and `assets/bibliometrics/` were
not reviewed.** They parse, and they are outside the learner-facing content this review
covers, but they carry paper counts (925, 1,064, 2,213) that do not obviously reconcile
with each other or with the 200-paper journal club.

## Recommended next steps, in priority order

1. **Modules 06, 08, 10, and 11**, using the unit template. Highest learner-facing impact
   of what remains, and the shortest path for each: they already have the structure.
2. **Per-module pointers to the technical unit that holds the depth**, so the two
   sequences connect at the point of use rather than only on the library index.
3. **A subject-matter pass over the figure captions** by someone who can see the images.
4. **A size assertion in whatever pipeline generates `journal_papers.yml`**, so a
   recurrence of the indentation bug fails loudly instead of silently shipping one paper.
5. **Reconcile the bibliometrics paper counts** with the journal club corpus, or state
   plainly that they are different corpora.

---

## A note on what this review found the second time

The original review diagnosed thin content. That was correct but incomplete: a
significant share of what looked like missing content turned out to be **working content
that nothing could reach**.

- 199 of 200 journal-club papers, unreachable through a YAML indentation error.
- Eleven worksheets showing placeholder text for prerequisites that were sitting in front
  matter the generator never read.
- Eleven more falling back on outputs blocks that existed but were labelled in a form the
  parser did not match.
- Ten Concept Explorer deep links pointing at headings that had been renamed.
- Five journal-club filter options matching no paper, and six real dimensions with no
  option.

None of these were visible as gaps. Every one of them rendered as a page that looked
finished. The lesson for anyone maintaining this site is that **the checks matter as much
as the content**: before this pass, four of the repo's five validation scripts printed
warnings and exited zero regardless, so nothing they checked could ever fail a build.
They now gate, and each gate was verified by injecting a fault rather than assumed.
