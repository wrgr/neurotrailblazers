# Answer keys, batch 2: 02, 08, 17, 19, 20, 21, 22, 25

Status log, appended step by step.

## Step 1: module20.md

Computation done (python3, standard library; scripts in the session scratchpad, not the repo).
Estimand: reciprocal E-I pairs (E->I and I->E). E = L23_pyr, L4_exc, L5_pyr, L6_pyr.

- Module 11 kit, >=1 synapse: 200 nodes, 1,453 edges; reciprocal EE 8, EI 41, II 7.
  EI null means (999 samples, seed 20): ER 9.97, DEG 16.63, DEG+TYPE 29.93, DEG+TYPE+DIST 44.75.
  Ratios 4.11 / 2.47 / 1.37 / 0.92; p 0.001 / 0.001 / 0.029 / 0.841.
- >=2 synapses: 745 edges; EI 13; ratios 4.95 / 3.01 / 1.59 / 0.96.
- 24-test family on kit 11: Bonferroni keeps 4 (ER and DEG EI at both thresholds); BH keeps 5.
- Module 10 kit (20432, soma_count 2, excluded): 499 nodes, 11,194 edges, EI 554;
  DEG+TYPE ratio 1.69 (p 0.002), DEG+TYPE+DIST 1.01 (p 0.340).
  Matched subset (L2/3+L4, shared types): 248 nodes, 4,363 edges, EI 195; 1.42 / 1.03.
- Error band (module's illustrative 2% merge / 6% split): EI 33-42; split lowers, merge raises.
- Basket-E reciprocal 34, Martinotti 6, VIP 1. Median soma distance: reciprocal EI 119.1 um vs all E->I 183.1 um.

module20.md complete (339 lines): all worksheet sections in order, four nulls with mixing
check, 24-test family with max-statistic permutation + Bonferroni + BH, exploratory vs
confirmatory blocks, matched-subset robustness check (pass), error band, rubric tiers.

## Step 2: module25.md completeness

Found incomplete: section 2 (captions and reflection), section 5 (permission check),
"What good looks like" and every section from Working checklist to Feedback guide were
headings only. Section 2 now written (kit values recomputed: Module 10 kit 11,388 edges,
2,332 at >=3, 55.4% single-synapse; Module 07 kit 45 flags; Module 18 kit 447 duplicates).
Section 5, What good looks like, and all remaining sections now written; module25 complete.

License defect (all eight keys): footers said "CC BY-SA 4.0"; LICENSE puts teaching material
under CC BY 4.0 (BY-SA is a deliberate exception for decks only). Fixed in the eight keys.
NOT fixed (out of scope): teaching/answers/module01.md, 07, 18, index.md, teaching/faq.md,
teaching/assessment/answers.md, teaching/sequence.md, teaching/syllabi/two-day.md.

## Step 3: verification of all eight keys

Section order: all eight keys answer the worksheet's sections in order (Before you start,
Questions, The task with numbered steps and hand-ins, Working checklist, Evidence and
reasoning, Misconception self-check, Session timing, Rubric, Exit prompt, Peer review),
plus a Feedback guide. Front matter: all eight have layout, title, permalink, slug,
content_type delivery, description.

- 21: recomputed from assets/kits/module03/synapses_sample.csv: 3,000 rows, 76 blank
  (2.53%), 2,924 kept, top-ten pair counts and shares, 11th/12th tie at 107, largest
  excluded group 22 (L23_pyr), 175,514 bytes, sha256 f8bd40f456ca... All match.
- 08: quoted numbers match their source pages (module08 worked example 84/22/51/78,
  z 3.7/0.7, 300 neurons; Unit 09 210 pairs, 2.9x/1.4x/1.14x, z 5.0/1.8, p ~0.07).
  Exact enumeration recomputed: 924 graphs, mean 15/11, tail 95/231; threshold two:
  495 graphs, mean 6/11, tail 17/33. v1300 as long-term version matches the site's
  provenance page.
- 22: intro now names "Module 22: Scientific Presentation" (module page title). Note: the
  generated worksheet header still says "Scientific Writing and Presentation" (stale;
  regenerate from the module page; not edited here).
- 19: arithmetic recomputed against the kit's mock-preprint (1,812 / 518 = 3.50,
  z = 31.6, 0.05/13 = 0.0038, 0.05/3 = 0.017, 1/1,001). Match.
- 17, 22: scenario figures (1,247 of 12,891, 2.1x, threshold 50; 3.2x, 847, a third
  proofread) match the module pages; all extra figures labeled invented.
- 02: invented learner, lab and names; no real-world claims found.
- All relative_url links in the eight keys resolve; every key carries "This is a local
  teaching rubric, not a validated assessment instrument."

## Validators

- `ruby scripts/validate_frontmatter.rb`: no problems found.
- `ruby scripts/validate_code_span_paths.rb`: OK (262 permalinks, 514 files).

Nothing committed.
