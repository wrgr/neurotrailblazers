# Module 02-09 assessment fan-out

## Status and release boundary

This is a work definition, not a claim that authors or agents are running. Worker tasks begin as unassigned. The user requested parallel assessment development after the combined usability release.

Baseline inspected: `4ae3596bfee1a8bbfd0c8c947218965cb594c4f5` (merged PR #188). The eight lesson blobs and `_data/module_interactives.yml` were checked against that revision.

Integration branch: `codex/module02-09-assessment-integration`.

Use one canonical assessment integration PR into `main`. Module workers return isolated commits; do not create competing deployment PRs, push to the integration branch, alter `main`, merge, or deploy. The coordinator alone integrates reviewed commits. The earlier approval to deploy #188 is not approval to publish these assessments.

All eight modules remain `in_development` until a maintainer explicitly reviews the particular module's instruction, assessment, fixtures, and rendered experience. Passing software checks is not evidence of assessment validity or learner proficiency.

## Parallel boundaries

Eight independent content workers, one per module. A separate review pass checks content before one coordinator changes shared code. Learning prerequisites are not authoring dependencies: workers read existing prerequisite lessons rather than waiting for other workers' new assessments.

| Module | Lesson | Assessment focus | Worker branch |
|---|---|---|---|
| 02 | Research Foundations and the Hidden Curriculum | Research navigation, help-seeking, attribution, responsible boundaries | `codex/assessment-module02` |
| 03 | Python and Jupyter for Neuroscience | Reproducible notebooks, data inspection, interpretable outputs | `codex/assessment-module03` |
| 04 | Neuroanatomy for Connectomics | Context-aware structural interpretation and justified uncertainty | `codex/assessment-module04` |
| 05 | Electron Microscopy and Image Basics | Artifact diagnosis and justified pass/flag/rework decisions | `codex/assessment-module05` |
| 06 | Segmentation 101 | Error classification and one evidenced correction cycle | `codex/assessment-module06` |
| 07 | Proofreading and Quality Control | Scientific-impact triage, adjudication, release decisions | `codex/assessment-module07` |
| 08 | Hypothesis Testing in Connectomics | Hypotheses, metrics, null models, interpretation boundaries | `codex/assessment-module08` |
| 09 | Neuron Morphology and Skeletonization | Skeleton descriptors, measurement sensitivity, bounded classification | `codex/assessment-module09` |

Each worker writes ONLY:

- `_data/module_assessment_drafts/moduleNN.json`: submission, including runtime-compatible quiz and microtask plus review metadata. Jekyll can read JSON data, but no production template reads this staging namespace yet.
- `docs/assessment-fanout/reviews/moduleNN.md`: alignment map, source verification, known gaps, and test evidence. Do not self-approve.
- `docs/assessment-fanout/fixtures/moduleNN/`: small self-contained fixtures and answer-checking tests needed for that module, with provenance. These are excluded from the published site; the coordinator promotes reviewed learner assets deliberately.

Worker branch names are proposed, not automatically provisioned. Start workers from the integration scaffold commit, use a separate worktree per worker, and return the branch name and exact commit SHA. The coordinator checks file ownership before cherry-picking.

Workers MUST NOT edit `_data/module_interactives.yml`, `_data/module_status.yml`, shared templates, shared JavaScript/CSS, navigation, workflows, other modules, or generated worksheets/decks/session pages. Propose necessary lesson corrections in the review document. The coordinator applies approved lesson changes and regenerates artifacts once, preserving the required source headings.

## Required reading and evidence

Read the COMPLETE `modules/moduleNN.md`, especially its actual learning objectives, Capability target, Studio activity, Core workflow, worked examples, and Assessment rubric. Read `CONTRIBUTING.md`, `.agents/rules/performance.md`, and the lesson's linked content-library references. Read `_includes/ui/module-interactive-lab.html`, `_data/module_interactives.yml`, and `assets/js/module-interactives.js` for compatibility, not for permission to copy generic questions.

Do not equate module numbers with technical-course unit numbers. The old Module 02-09 microtasks are known to be mismapped; they are not content exemplars. Do not use the generic default quiz as a replacement for module-specific evidence.

Use the lesson to establish curricular scope, not as an infallible scientific answer key. Verify assessable scientific claims and software behavior against primary sources or executable fixtures. Flag contradictions instead of teaching or scoring them as facts. Do not add unsupported clinical claims, arbitrary numerical thresholds, or invented image labels. State what each cited source actually supports.

## Submission contract (version 1)

The JSON root has these fields:

- `schema_version`: integer `1`.
- `module_slug`: exact `module02` ... `module09`.
- `source_revision`: inspected full Git commit SHA.
- `source_lesson`: `modules/moduleNN.md`.
- `source_lesson_blob_sha`: Git blob SHA of that lesson at the inspected revision.
- `status`: `draft` or `needs_review`, never `available`.
- `objectives`: array of `{id, text}` using stable IDs `moduleNN-o1` onward. Preserve the meaning of the lesson objectives; explicitly flag unsupported objectives.
- `quiz`: `{title, pass_score, questions}`. `pass_score` is the number of correct answers, NOT a percentage. Each question contains the existing renderer fields `prompt`, `options`, `correct_index` (zero-based), and `explanation`, plus review fields `id`, `objective_ids`, `cognitive_target`, `source_refs`, and `option_rationales` (one per option). Use stable item IDs `moduleNN-q01` onward.
- `task`: existing fields `{title, prompt, options, correct_index, correct_feedback, incorrect_feedback}`, plus `id`, `objective_ids`, and `source_refs`. This is a scored micro-decision, not a substitute for doing the practical task.
- `transfer_task`: `{id, title, prompt, inputs, expected_artifact, objective_ids, worked_solution, rubric, limitations}`. Inputs must exist or be fully supplied inline. `rubric` is an array of `{criterion, not_yet, proficient, strong}` with observable distinctions.
- `sources`: array of `{id, location, section, supports, verified}`. Locations can be exact repository paths/anchors or primary-source URLs. `verified` records actual verification, not an intention. Only references actually read or tested can be marked true.
- `validation_cases`: executable case references or explicit `{case, input, expected, rationale}` records for correct, incorrect, incomplete, ambiguous, and boundary cases where applicable.
- `assessment_limits`: what these tasks do and do not establish.
- `known_gaps`: unresolved evidence, missing instruction/fixtures, or integration requirements. Empty only when genuinely none are known.

Use plain text or deliberately escaped code in strings; do not introduce arbitrary HTML or scripts. Keep code examples readable. The coordinator is responsible for safe rendering and disclosure of answers.

## Content quality gate

Aim for eight checkpoint items per module; use six to ten only with a coverage rationale. Assess every supported objective, using multiple items where the judgment is central. An objective requiring execution also needs performance evidence; multiple-choice coverage alone does not satisfy it. Prefer application, interpretation, troubleshooting, and a meaningful uncertainty decision over definition recall. Do not impose identical question formats across unlike skills.

Use three or four plausible options with one defensible best answer under the stated conditions. Explain why every distractor fails and where to revisit the lesson. Avoid answer-length clues, moralistic caricatures, and repeated boilerplate. Correct-answer positions must vary; always choosing the first option must not pass. A proposed threshold is a formative teaching choice, not an empirically validated mastery cut score. State its rationale in the review.

Include one module-specific scored microtask and one small transfer/performance task with a worked response and a Not yet / Proficient / Strong rubric. Do not duplicate an entire four-hour lab. The small task may sample capability, but it must not claim to establish the whole module's performance objective.

Use self-contained inputs. Where no validated EM patches exist, supply an explicitly synthetic evidence table for a decision exercise and mark perceptual image-reading assessment as a remaining gap. Do not invent ground truth for decorative figures or arbitrary hotspots. For any actual image task, inspect the image, verify labels/coordinates, document provenance/licensing, and provide a meaningful accessible alternative.

An independent review pass must try to break the answer key, identify alternate defensible answers, check numeric calculations, inspect source alignment, and distinguish deficient instruction from deficient learner performance. A second automated pass is not to be described as independent human review or learner validation.

## Module-specific guardrails

**02:** Assess whether a learner can build an actionable research-navigation plan and reason about help-seeking, roles, attribution, dataset boundaries, and escalation. Do not grade conformity to one lab's unwritten social rules or require private disclosures. Score decision rationale rather than personality, confidence, or familiarity with academic culture. A fictional lab policy must be labeled fictional.

**03:** Supply a tiny local table and notebook/code example. Test hidden execution state, data types/missing values, units, labels, provenance, and clean-kernel reproducibility. Include expected outputs verified by execution. No credentials, cloud account, external dataset download, or current service availability may be needed for the basic checkpoint. Document environment requirements; do not reward memorizing library APIs at the expense of reproducibility.

**04:** Assess anatomical context and evidence chains without pretending an ambiguous local patch uniquely identifies a layer or cell type. Include a defensible request for more context. Distinguish confidence from correctness. Do not use decorative module artwork as labeled EM evidence.

**05:** Link image/artifact observations to downstream consequences and concrete actions. Include pass, flag/inspect, and rework conditions rather than treating every artifact as an automatic rejection. Any severity cutoffs or cost figures supplied for a scenario must be explicitly scenario assumptions. Distinguish an artifact's appearance from a verified diagnosis.

**06:** Classify merge, split, boundary, and uncertain cases and document a before/after correction. Use a tiny verifiable fixture if actual segmentation editing is assessed. Do not present a multiple-choice choice as an executed correction. Include an intervention that could introduce another error and require checking the resulting quality metric.

**07:** Focus on prioritization, adjudication, unresolved risk, and release evidence. Module 06 owns basic classification/correction. A learner must justify priorities against a stated scientific endpoint; do not teach an unconditional rule that merges always outrank splits. Release and deferral decisions need stated consequences and limits, not just a higher aggregate score.

**08:** Supply a small analysis scenario with defined sampling units. Assess a measurable hypothesis, scope-matched metric, justified null, uncertainty, multiple testing when relevant, and a supported claim/non-claim pair. Label simulated values. Check probability calculations independently. Do not imply a structural association establishes causal neural computation.

**09:** Supply a small skeleton with coordinates, units, parent links, and a declared root. Verify at least three descriptor calculations using executable checks, with explicit conventions and tolerances. Include truncation or a spurious branch and interpret its effect. Morphology alone must not be scored as uniquely establishing cell identity in an ambiguous case. Verify format terminology against its primary documentation rather than repeating an unchecked expansion from the lesson.

## Coordinator-only integration

1. Confirm the final baseline includes merged #188 and preserves its paper-list/map, non-sticky filter, accessibility, and progress fixes. No competing navigation work.
2. Check each worker's changed paths. Preserve the module-specific draft and review history. Resolve scientific/assessment concerns before enabling any item.
3. Choose one canonical data-loading strategy: a reviewed per-module namespace with a documented fallback for untouched modules, or a deterministic import into the legacy shared data file. Do not maintain two competing editable truths. No runtime model calls or answer-key generation.
4. Gate draft assessment visibility deliberately: the present template checks whether a module-specific quiz exists separately from the practice-readiness flag. Merely adding a quiz to the live legacy file could expose it while the module is still marked in development. Staged drafts must not leak into production.
5. Version assessment state so legacy mismapped task results do not become passes for new tasks. Keep self-reported activity progress, scored checkpoint results, and rubric-based capability evidence distinct. Test persistence, reset, retry, incomplete answers, and cross-module isolation.
6. Render option feedback accessibly; answers/explanations must not leak before the attempt merely because a question exists in the DOM. These are transparent formative assessments, not secure examinations; do not make security claims about client-side answer keys.
7. Where lesson changes are approved, preserve the generator's source headings and run `ruby scripts/generate_module_teaching_materials.rb`. Regenerate outputs centrally; do not hand-edit generated worksheets, session pages, or module decks.
8. Add content/schema tests for all eight submissions: unique IDs, valid indices and pass scores, objective/source coverage, varying key positions, fixture existence, and no generic/default fallback. Verify correct/wrong/incomplete attempts in a real browser at 390px and desktop width, with normal clicks and keyboard navigation. Retain all #188 wrong-button and paper-browser regressions.
9. Run the FULL existing Validate suite on the exact final combined commit and review the built preview. Update `_data/module_status.yml` only for modules with an explicit, recorded maintainer readiness decision. Remaining gaps stay visible and in development.
10. Keep one draft integration PR; no auto-merge or deployment. Seek explicit approval of the reviewed assessment release.

## Worker handoff format

Return the exact commit and owned paths, learning-objective coverage table, item/task inventory, verified source list, fixture/test commands with observed results, remaining gaps, and a reviewer checklist. Clearly distinguish authored, tested, reviewed, and learner-validated. Do not call planned work completed.
