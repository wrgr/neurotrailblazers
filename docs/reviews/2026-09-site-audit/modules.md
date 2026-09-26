# Site audit: module pages (September 2026)

Scope: `modules/index.md`, `modules/module01.md` to `module25.md`, `modules/slides/index.md`
(a redirect, unchanged), and the copy in `scripts/generate_module_teaching_materials.rb`
(read, unchanged). Generated outputs (`teaching/sessions/`, `assets/worksheets/module*/`,
`course/decks/marp/modules/` and their rendered HTML) were rebuilt with
`generate_module_teaching_materials.rb` and `render_marp.sh --html`; no generated file was
hand-edited. The render touched only the module decks whose sources changed. The
fabrication audit (`docs/reviews/2026-09-fabrication-audit-modules.md`) was read first and
none of its fixes were reversed. Real-dataset numbers were aligned to
`docs/reviews/2026-09-site-audit/canonical-facts.md`. Task steps and numbers in Modules 01,
07 and 18 are unchanged, so the answer keys still match.

## Summary

- Files edited: 26 (all 25 module pages plus the module index). Generated files rebuilt: 22
  worksheets, 22 session kits and 22 decks (modules 12, 13 and 23 changed only in
  sections the generator does not read).
- Fixes: 47 accuracy, 16 polish, 38 voice, 13 missing content. Total 114.
- Validators: all ten pass. Every `relative_url` link in `modules/*.md` resolves to a
  permalink or file.

Main accuracy fixes:

1. **Inverted misconception guardrails (Modules 16–19).** These modules wrote each
   guardrail as the correction ("more filtering is not always better"). The generator
   prints guardrails as beliefs ("I did not assume: …", "They may believe: …"), so 22
   worksheet and session-kit lines told learners and facilitators the opposite of what was
   meant. Each is now written as the belief, with the correction on a separate
   "Why it fails" line that the generator does not collect. Duplicate guardrails in
   Modules 17 and 19 were replaced.
2. **Invented or wrong citations.** Module 07's "Funke et al. (2017) A benchmark for
   evaluation of large-scale reconstruction methods" does not exist; it is now the real
   Funke et al. (2017) TED paper (*Methods* 115:119–127). Module 05's Hua et al. (2015) had
   an invented title and journal; it is now *Nature Communications* 6:7923. Also
   corrected: the CAVE paper's year (2025, *Nat Methods* 22:1112–1120) in 03, 07 and 12;
   the CloudVolume Zenodo DOI (the old one returns 404); the Margolis (2001) editor
   credit; the Lorente de Nó (1934) volume and pages; the Petilla terminology year and
   volume; and Lee et al. SNEMI3D (2017, not 2019) in 06, 13 and 14.
3. **Invented statistics.** Removed or softened: "a 20% reduction in membrane contrast can
   double the split error rate" and "five artifacts that cause 90% of segmentation
   failures" (05); "expert proofreaders disagree on 5–10% of decisions" (01); "Cost:
   10–100x the time of automated segmentation" (07); "three or more consecutive missing
   sections sever most neurites" (05).
4. **Canonical dataset numbers (Module 12 and others).** MICrONS is now about 2 PB raw
   (was ">1 PB"), 1.3 × 0.87 × 0.82 mm in vivo, 84,035 segmented neurons in the larger
   subvolume and about 524M synapses, with the Explorer's differing figures attributed.
   H01 is 1.8 PB raw and 1.4 PB aligned, with 16,087 neurons. FlyWire synapses are
   ~54.5M. The FlyWire consortium is "at least 76 labs" (was "more than"). The Module 17
   example version is now v1300; v795 is expired.
5. **Internal errors.** In the Module 06 worked example, two somata 180 µm apart could not
   sit in a 50 µm cube; they are now 40 µm apart. In Module 08, "more than half" of the
   effect removed by the degree null was really 29 of 62. Also in 08, the "most stringent
   null" rule had its two nulls reversed. Module 10 used `nx.watts_strogatz_graph` as a
   random null. Module 22 sent figure design to Module 18 (it is Module 16). Module 23 said
   "68 words" for a 60-word draft. Module 02 still said "287 proofreaders".

## Findings and fixes

| File | Issue | Type | Fix |
|---|---|---|---|
| module01 | "Expert proofreaders disagree on 5–10% of decisions" unsourced | Accuracy | Softened to "disagree on some calls" |
| module01 | Closing script promised "we will revisit them in Module 06"; Module 06 does not | Accuracy | Now points to Module 25, where a matching sentence was added |
| module01 | "Connectomics landscape" heading; "Let's ground this"; "powerful but directionless" | Voice | Heading states the content; plain sentences |
| module01 | "more than 76 labs" | Accuracy | "at least 76 labs" (canonical) |
| module01 | No next step for the motivation gap | Missing | Links The Resilient STEM Scholar workshop |
| module02 | "287 proofreaders across dozens of institutions" (missed by the fabrication audit) | Accuracy | Consortium wording per canonical facts |
| module02 | "Disagreements … resolved through consensus protocols, not authority" unsourced | Accuracy | Each project sets its own rule |
| module02 | Margolis & Romero (2001) | Accuracy | Margolis, E. (Ed.) (2001) |
| module02 | "not a soft skill --- it is a core technical competency"; "Let's" ×2 | Voice | Rewritten |
| module02 | No link to the hidden-curriculum page or the Orientation workshop | Missing | Added both |
| module03 | "NeuPrint"; FlyWire and MICrONS listed as separate client platforms | Accuracy | "neuPrint"; CAVE serves FlyWire and MICrONS |
| module03 | "Precomputed, Neuroglancer" listed as two formats | Accuracy | "Neuroglancer Precomputed" |
| module03 | CAVE paper 2024; CloudVolume DOI 404 | Accuracy | 2025, vol. 22; Zenodo 5671443 |
| module03 | "not optional --- it is", "is a screenshot", "Let's" ×3, "robust", "essential" | Voice | Rewritten |
| module04 | L4 "dominated by spiny stellate cells" (not true of mouse V1, the MICrONS volume) | Accuracy | Barrel cortex vs visual cortex stated separately |
| module04 | L2/3 "the most densely packed neuronal layer" | Accuracy | Removed superlative |
| module04 | Mossy fiber boutons "the largest in the brain (3–5 µm)" | Accuracy | "Among the largest" |
| module04 | Lorente de Nó 1934 cited with Part I's volume and pages | Accuracy | Part II, 46:113–177 |
| module04 | "not optional — it is essential" | Voice | Rewritten |
| module05 | Invented contrast/split-rate and "90% of failures" statistics | Accuracy | Removed |
| module05 | SBEM ">1 mm³"; FIB-SEM limit omitted the hemibrain slab method; "MICrONS uses SBEM or ssTEM" | Accuracy | Corrected: MICrONS ssTEM, H01 multibeam SEM, hemibrain slabs |
| module05 | Hua et al. 2015 invented title and journal | Accuracy | Real title, *Nat Commun* 6:7923 |
| module05 | Unlinked "content library entry" references ×2 | Polish | Linked |
| module05 | "not merely aesthetic — it is the single most consequential"; "key insight" | Voice | Rewritten |
| module06 | Two somata 180 µm apart in a 50 µm subvolume | Accuracy | 40 µm |
| module06 | Identity errors "rare but catastrophic" unsupported | Accuracy | Softened |
| module06 | Lee et al. 2019 | Accuracy | 2017 (arXiv 1706.00120) |
| module06 | "it's the foundation", "insidious", "key insight", "essential" | Voice | Rewritten |
| module06 | Unlinked pre-class reading | Polish | Linked |
| module07 | Nonexistent Funke 2017 "benchmark" citation | Accuracy | Real Funke 2017 TED paper |
| module07 | "10–100x the time" cost figure; FlyWire "consensus mechanisms"; CAVE logs "why" automatically | Accuracy | Softened or corrected |
| module07 | CAVE paper year | Accuracy | 2025 |
| module07 | "more than 76 labs" | Accuracy | "at least 76" |
| module07 | Unlinked pre-class readings | Polish | Linked |
| module08 | Most-stringent-null rule had the two nulls reversed | Accuracy | Corrected |
| module08 | "More than half" of the effect removed by the degree null (was 29 of 62) | Accuracy | "Nearly half (29 of 62)" |
| module08 | Unlinked pre-class reading | Polish | Linked |
| module09 | "Axons tend to be more tortuous than dendrites" unsourced | Accuracy | Removed; compare within a compartment |
| module09 | "Inhibitory neurons ~0 spines" | Accuracy | "Most inhibitory interneurons few or none" |
| module09 | Petilla terminology 2007, 8(7) | Accuracy | 2008, 9(7) |
| module09 | Unlinked pre-class reading | Polish | Linked |
| module10 | "4× enriched in cortex" given without scope | Accuracy | Scoped to rat L5 slices (Song 2005) |
| module10 | Watts-Strogatz graph used as the random null | Accuracy | Degree-preserving `nx.directed_edge_swap`; WS noted as a small-world reference |
| module10 | "retraction-in-waiting" | Voice | Rewritten |
| module11 | AIS input "exclusively from chandelier cells" | Accuracy | "Predominantly" |
| module11 | "L4 stellate" in a MICrONS (visual cortex) example | Accuracy | "L4 excitatory cell" |
| module11 | "4× enriched in cortex" without scope | Accuracy | Scoped |
| module11 | "workhorses", "uniquely powerful", "publishable and durable" | Voice | Rewritten |
| module11 | DotMotif title truncated; unlinked readings | Polish | Fixed; linked |
| module12 | MICrONS ">1 PB raw", Explorer dimensions and neuron count unattributed, 523M; H01 "1.4 PB" as raw; FlyWire ~50M | Accuracy | Aligned to canonical facts, with sources |
| module12 | "the field's most common silent bug" (unsupported superlative) | Accuracy | "Fails silently" |
| module12 | CAVE paper year | Accuracy | 2025 |
| module12 | "doesn't just run slowly —" | Voice | Rewritten |
| module13 | Automated proofreading via "reinforcement learning" unsupported | Accuracy | "Learned merge/split scoring" |
| module13 | Lee 2019 | Accuracy | 2017 |
| module13 | "not a model that performs badly — it is"; "robustly" | Voice | Rewritten |
| module14 | Lee 2019 | Accuracy | 2017 |
| module14 | "leverage", "robust failure analysis" | Voice | Rewritten |
| module15 | Placeholder front-matter references shown on the deck ("Internal patch-analysis workflow guidance") | Missing | Two real references (Ji et al. 2023; Walters & Wilder 2023) |
| module15 | Example prompt credits Dorkenwald 2024 with cell typing (that is Schlegel et al. 2024); "4× enriched" unscoped | Accuracy | Fixed |
| module15 | "LLMs cannot generate new knowledge", "Current models fabricate" as absolutes | Accuracy | Softened to what the module can support |
| module15 | "not a bug — it is"; "robust" | Voice | Rewritten |
| module16 | Guardrails inverted (5) | Accuracy | Rewritten as beliefs plus "Why it fails" |
| module16 | "Matplotlib colorblind check" does not exist; Sholl plot "scale bar" | Accuracy | colorspacious; radius axis in µm |
| module16 | 8% / 0.5% color-vision figure given without population | Accuracy | Scoped to Northern European ancestry |
| module16 | Placeholder front-matter reference | Missing | Tufte, Borland & Taylor, Weissgerber |
| module16 | MICrONS paper title "Visual cortex reconstruction" | Polish | Real title and volume |
| module16 | "science itself is compromised", "unmatched", "Let us" | Voice | Rewritten |
| module17 | Guardrails inverted (7); two duplicates | Accuracy | Rewritten; duplicate replaced with a distinct misconception |
| module17 | Checklist example used the expired v795 | Accuracy | v1300 (canonical) |
| module17 | Journal Club page listed as a "video" | Polish | Removed |
| module17 | "not merely incomplete --- it is scientifically irresponsible"; "not boilerplate --- it is" | Voice | Rewritten |
| module18 | Guardrails inverted (6) | Accuracy | Rewritten as beliefs; the answer key already used belief wording |
| module18 | Two unit pages listed as "videos" | Polish | Removed |
| module18 | "not model failures first; they are"; "not just good practice --- it is" | Voice | Rewritten |
| module19 | Guardrails inverted (6), one duplicate | Accuracy | Rewritten |
| module19 | Macaque interareal distance-rule paper cited for local cortical wiring; "distance-dependent Erdos-Renyi" | Accuracy | Citation dropped; "distance-dependent null model" |
| module19 | "Thousands of volunteers" for FlyWire and Eyewire together | Accuracy | "Many volunteers" |
| module19 | No next step | Missing | Savvy Researcher and Professional Conduct workshops |
| module20 | Studio scenario was one line with no data | Missing | Uses the Module 11 and Module 10 synthetic kits as the two datasets |
| module20 | Bare author-year link list | Polish | Full references |
| module21 | Studio scenario was one line | Missing | Names the package and the no-contact constraint |
| module21 | Worked example cited "two excluded tiles and one failed run" that never appear in it | Accuracy | Generic excluded samples and failed runs |
| module21 | "most common silent correctness failure in the field" ×2 | Accuracy | Softened |
| module21 | "not paperwork; they are … infrastructure" | Voice | Rewritten |
| module22 | Maya's opener claims "almost nobody has counted them at synapse resolution" (a claim about the real literature) | Accuracy | Rewritten with no literature claim |
| module22 | Figure design sent to Module 18 | Accuracy | Module 16 |
| module22 | "Education Models" link label for /models/ | Polish | "Program Models" |
| module22 | No next step | Missing | Communicating Science I and II |
| module23 | "68 words" for a 60-word draft | Accuracy | 60 |
| module23 | "The 250-word limit" (limits vary; some meetings count characters); GRC size "roughly a hundred"; SfN "dedicated connectomics sessions" | Accuracy | Softened |
| module23 | Stale link label; no next step | Polish/Missing | Program Models; Building Your STEM Entourage |
| module24 | "a unusually" | Polish | "an unusually" |
| module24 | Placeholder front-matter references | Missing | NASEM 2019 and 2018 reports |
| module24 | Two links labeled as different frameworks both go to /models/ | Polish | One "Program Models" link |
| module24 | Connectome history described as covering "career opportunities" | Accuracy | Description corrected |
| module24 | "Support being deliberately withdrawn" reads as a warning sign | Voice | "Deliberately handing over control" |
| module24 | No next step | Missing | Charting Your Course, Building Your Entourage and Future Forward |
| module25 | Placeholder front-matter reference | Missing | Removed |
| module25 | No link back to the Module 01 artifacts; stale framework label | Missing/Polish | First-and-last pair sentence; Future Forward link |
| index | Markdown heading and paragraph inside an HTML `<div>` (kramdown leaves them raw) | Polish | Converted to HTML with a heading that states the claim |
| index | Teaching-materials line did not mention session kits, answers or syllabi (all now exist) | Missing | Updated with links |
| index | Character list out of order (21 before 17) | Polish | Reordered |

## Needs owner decision

1. **Canonical versus fabrication-audit numbers.** Module 12 now says about 2 PB raw for
   MICrONS and ~54.5M FlyWire synapses, per the canonical-facts registry. The fabrication
   audit had set ">1 PB" and "~50M". The registry quotes the paper text for both.
2. **MouseConnects "10 mm³" and "about 10x MICrONS".** Used in Modules 01 and 12. It
   matches the site's MouseConnects pages but is not in the canonical-facts registry.
   Verify against the NIH award text.
3. **Module 01: "FlyWire … first whole-brain connectome of an adult animal with complex
   behavior".** This matches the paper's framing but was not re-verified word for word.
4. **Module 05 heuristics** (ssTEM ~4 nm XY and ~30 nm Z; SBEM ~8 × 25 nm; FIB-SEM 4–8 nm)
   and **Module 14 ERL bands** (10 / 100 / 1,000 µm) are typical values with no source
   given. Add a source or label them rules of thumb.
5. **Module 09 "SWC (Stockley-Wheal-Cole)"** expansion is widely repeated but not verified
   against a primary source.
6. **Module 23 Gordon conference size.** It now says "up to about two hundred". Confirm
   against GRC's current policy.

## Outside my area

- `teaching/answers/module01.md:156` refers to "the landscape segment". Module 01's
  Block 2 is now titled "Three projects, three driving questions".
- The generator's session-kit template (`scripts/generate_module_teaching_materials.rb`,
  "Naming the norm") calls naming norms "a fairness intervention rather than etiquette".
  This is minor and was left unchanged.
- `content-library/case-studies/*` and `datasets/mouseconnects.md` carry the 10 mm³
  MouseConnects figure. Verify it there when owner decision 2 is settled.
- The canonical-facts registry flags the remaining "more than 76 labs" wording in teaching
  sessions and initiatives pages. The session kits regenerate from the modules and are now
  correct; initiatives pages are outside this area.
