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
| Module worksheets (×25) | ~123 words of blank template each | ~730 words each of real task content, generated from module pages |
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

Stated plainly so the remaining scope is visible.

**1. Some worksheet sections still fall back to generic text**, because the module
pages they are generated from lack the corresponding content. The generator was rebuilt
(see below) so worksheets now carry the real scenario, task steps, workflow checklist,
timing, and rubric — but where a module page has no `**Outputs**` block in its studio
activity, no misconception guardrails in its concept set, or no run-of-show, the
worksheet falls back. Current fallback rates across the 25 worksheets: outputs 11/25,
misconception self-check 8/25, session timing 6/25. **These are module content gaps, not
generator bugs**, and the fix is to add those blocks to the module pages listed by:

```
grep -l 'Artifact produced during the activity' assets/worksheets/*/*.md
```

**2. The 25 module pages average ~1,600 words** and sit between the old scaffolding and
the new unit standard. Modules 13–15 and 20–25 are thinnest. They would benefit from the
same treatment, particularly the *Check yourself* and answer-key elements.

**3. Slide pages are lecture plans, not slides.** `technical-training/slides/*` and
`modules/slides/*` describe what each slide should contain rather than containing it.
That is defensible as a design document for an instructor building a deck, but it should
be labelled as such rather than titled "Slide Deck Draft".

**4. ~~Two validation scripts fail under Ruby 3.3.~~ Fixed.** All five scripts now run:
`validate_frontmatter.rb` was updated for the Psych 4 `safe_load` keyword-argument
change, and every script that reads content files now passes `encoding: 'UTF-8'`
explicitly rather than relying on the locale's default external encoding. Two
pre-existing frontmatter warnings on the journal-club pages were also cleared. The full
current state: frontmatter, figure refs, technical evidence, and site links all pass, and
the site builds clean under Jekyll 3.10.

**5. Figure galleries were preserved verbatim but not re-captioned.** Captions such as
"Techtalk S10: motivating question framing" describe the slide's provenance rather than
what the reader should notice in the image. Instructional captions ("note the glycogen
granules at lower left, absent from the neurite above") would make the galleries teach
rather than decorate.

**6. The technical track is still marked `status: planned`** in
`_data/technical_track.yml`, and individual entries still carry
`status: mapped_to_existing`. The units are now authored; that metadata should be
revisited by whoever owns the curriculum roadmap.

---

## Recommended next steps, in priority order

1. **Close the module content gaps the worksheet fallbacks expose.** Add an
   `**Outputs**` block to each studio activity, misconception guardrails to each concept
   set, and a run-of-show where missing. The worksheets then improve automatically on the
   next generator run — this is the cheapest remaining improvement per unit of effort.
2. **Modules 13–15 and 20–25**, using the unit template. These are the thinnest pages a
   learner is likely to land on.
3. **Instructional figure captions** across the technical units.
4. **Reconcile the `planned` status metadata** with the authored state.
5. **Add the checks to CI.** All five scripts now pass; running them on push would keep
   them passing.
