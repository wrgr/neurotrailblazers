# Fabrication audit: modules, kits and Marp decks (September 2026)

## Rule

"Nothing fabricated." No invented number, result, finding, quote, preprint or
claim may be attributed to a real dataset, a real release or materialization
version, a real paper, lab, person, organization or tool. An "illustrative" or
"hypothetical" label is not enough. Teaching scenarios may use invented data only
when it is labeled synthetic and detached from real names. Fictional releases use a
"T" prefix ("release T18"); fictional volumes are called, for example, "a fictional
mouse cortex volume". Real facts are sourced or verified against primary sources;
anything that cannot be verified is softened or removed.

## Scope and method

Scope: `modules/*.md` (all 25), `scripts/generate_kit_materials.rb` and
`assets/kits/**` with the manifest, `scripts/generate_module_teaching_materials.rb`,
and the hand-edited Marp sources (`course/decks/marp/*.marp.md`,
`en585781/*.marp.md`, `lectures/*.marp.md`). `teaching/**` (other than the generated
`teaching/sessions`), `technical-training/**`, `content-library/**` and
`notebooks/**` were audited separately.

Method:

1. Grepped every in-scope file for
   `MICrONS|minnie|H01|FlyWire|FAFB|hemibrain|BossDB|CAVE|Allen|Janelia|v[0-9]{3,4}|materialization|preprint|et al\.`,
   then for other real names (Seung, Lichtman, Google, Eyewire, Codex, neuPrint,
   MouseConnects, real table names, 18-digit root IDs) and for the real MICrONS
   version numbers.
2. Read each hit in context and sorted it: (a) citation or link, fine; (b) procedure
   naming a real version with no output, fine; (c) invented values attached to a real
   name, fixed by moving to a fictional volume or release; (d) a real-world claim,
   verified or softened.
3. Checked (d) claims against primary sources: Dorkenwald et al. 2024 abstract
   (Europe PMC), MICrONS Consortium 2025 abstract (Europe PMC), MICrONS Explorer
   cortical-mm3 page, Shapson-Coe et al. 2024 abstract (Europe PMC), Zheng et al.
   2018 via Janelia/HHMI summaries, and the Princeton release on the FlyWire
   consortium (287 researchers, more than 76 labs, plus volunteers).
4. Edited sources only, then ran `generate_kit_materials.rb`,
   `generate_module_teaching_materials.rb` and `render_marp.sh --html`. Generated
   churn is limited to the modules and decks edited. All ten validators pass.

## Findings and fixes

| File | Context | Category | Fix |
|---|---|---|---|
| modules/module18.md | Studio scenario: "MICrONS minnie65 (CAVE materialization v795)", 4.2 million rows and other counts | c | Now "a fictional mouse cortex volume, release T18"; all numbers and tasks unchanged; labeled synthetic |
| modules/module18.md | "cleft score > 50 in CAVE synapse tables" as a general norm | d | Softened to "a minimum cleft score; check the dataset's documentation" |
| modules/module17.md | Instructor-script example sentence "n=847 connections, MICrONS v795" | c | "release T17", with the label "invented figures from a fictional mouse cortex volume" |
| modules/module17.md | Studio scenario: "MICrONS minnie65 data, CAVE materialization v795", 1,247 pairs, 2.1x | c | "a fictional mouse cortex volume, release T17"; numbers unchanged; labeled synthetic |
| modules/module17.md | Checklist example "MICrONS minnie65, CAVE materialization v795" | b | Kept: a citation format with no result attached |
| modules/module19.md | Scenario: mock preprint "uses MICrONS minnie65 data (CAVE materialization v661)" with 3.5x enrichment | c | "a fictional mouse visual cortex volume (release T19)" |
| modules/module19.md | "community proofreading projects (e.g., FlyWire Codex, Eyewire)" | d | Codex is a browser, not the proofreading project: now "FlyWire, Eyewire" |
| assets/kits/module19/mock-preprint.md (via generator) | Abstract: "public ... connectome (MICrONS minnie65, CAVE materialization v661)" with invented counts | c | "a fictional mouse visual cortex volume (release T19)"; banner now says the volume and release are fictional too. "Data Release Consortium" was already fictional |
| assets/kits/module10/README.md (via generator) | "It stands in for a MICrONS column" | c | "It is shaped like a column extracted from a real cortical volume but is not one" |
| modules/module10.md, module11.md | Scenario: "a synthetic stand-in for a MICrONS column/subgraph" | c | "a synthetic graph/subgraph invented for teaching, not sampled from any real dataset" |
| modules/module15.md | Worked example: query "against materialization version 943 returns 1,197 rows" | c | "a pinned version (the fictional release T15)"; numbers unchanged; label updated |
| modules/module15.md | Table prompt "... at materialization version 943" | b | Kept: a procedure with no output |
| modules/module21.md | Worked example: "query materialization version 795 ... recover 4,712 ... version 1042 ... 5,103" | c | Fictional releases T21 and T27; numbers unchanged; label updated |
| modules/module22.md | Fallback result "3.2x ... 847 connections" in "a cortical EM volume" | c (unlabeled) | Now labeled "synthetic result (invented numbers from a fictional cortical EM volume, not a real finding)" |
| modules/module23.md | Model abstract with invented numbers and "reciprocity has not been counted at synaptic resolution" | c/d | Lead-in says the numbers are the Module 17 synthetic ones (release T17); gap sentence reframed to "our cortical circuit model assumes ... not been checked", which makes no claim about the literature |
| modules/module13.md | "well-stained MICrONS data may fail on under-stained H01 regions" | d | Unsupported claim about H01 staining removed; now a generic domain-shift example |
| modules/module14.md | FFNs "Used in FlyWire and other Google-based reconstructions" | d (wrong) | FlyWire's segmentation was not FFN-based. Now "Google-led reconstructions such as the Drosophila hemibrain (Scheffer et al. 2020) and H01 (Shapson-Coe et al. 2024)" |
| modules/module04.md | Trisynaptic circuit "has never been mapped at synaptic resolution across a large volume" | d | Softened to "Mapping this pathway ... is a key goal of MouseConnects" |
| modules/module01.md, 02, 07 | "287 proofreaders / contributors / people", "the 287 FlyWire proofreaders were co-authors" | d | Verified: a consortium of 287 researchers in more than 76 labs plus citizen-science volunteers, with the FlyWire Consortium credited as an author. Wording corrected in all six places; neuron count 139,255 |
| modules/module12.md | Scale table: MICrONS "~80,000 neurons, ~500M, ~2 PB"; FlyWire "~54.5M, ~100 TB"; MouseConnects ">10 PB"; prose "1.4-2 PB range" | d | MICrONS: >200,000 cells (~120,000 neurons), ~523M synapses, >1 PB raw (MICrONS Explorer). FlyWire: 139,255 neurons, ~50M synapses (Dorkenwald 2024), ~106 TB raw FAFB (Zheng 2018). MouseConnects storage: "not yet published". Prose now says H01 1.4 PB and MICrONS more than a petabyte. Sources line added |
| modules/module03.md | Example `query_table('synapses_nt_v1')` "returns ... neurotransmitter predictions" | d | Table name and columns not verified; replaced with the generic `get_tables()` / `query_table(table_name)` pattern |
| course/decks/marp/en585781/module09-algorithms-and-applications.marp.md | Provenance block: `minnie65_public`, materialization 943, invented n_nodes, n_edges, exclusion and error rates | c | `fictional_cortex_volume`, release T9; label says the dataset, release and values are invented |
| course/decks/marp/04-volume-reconstruction-infrastructure.marp.md | Speaker note: invented 1,412 / 1,530 case "used materialization 795" | c | T795, labeled fictional, matching the Technical Unit 04 fix |
| course/decks/marp/en585781/module08-tools-and-methods.marp.md | Header template `minnie65_public`, `MAT_VERSION = 943`; "e.g. version 943"; question prompt "For MICrONS materialization v943 ..." | b | Kept: configuration and questions, not results |
| course/decks/marp/en585781/module07-introduction-to-connectomics.marp.md | Defensible-claim examples (illustrative) | a/b | Detached from real names except the H01 provenance line, which is factual |
| assets/kits/** (other kits) | Synthetic banners, `synthetic-synapses-v1`, six-digit IDs, no real table names | a | No change needed |

## Owner decisions

1. **MICrONS neuron count.** MICrONS Explorer gives about 120,000 neurons in the
   anatomical reconstruction. The deleted "~80,000" figure and other counts in
   use elsewhere (the case study calls minnie65 "the 65,000-neuron core dataset")
   do not agree. Choose one sourced number site-wide.
2. **MICrONS raw size.** Graduate deck module07 (speaker notes) and module08
   still say "MICrONS ~2 PB raw" or "1.4–2 PB range". No primary source for 2 PB was
   found; MICrONS Explorer and the paper say "petabytes" or give no figure. Keep it
   only if you have a citation.
3. **FlyWire synapse count.** The deck uses "~54.5 million". The paper abstract says
   5 × 10^7. Module 12 now says ~50M. Align, or cite the exact source for 54.5M.
4. **`caveclient 5.21.0`** in the module08 deck header template is a real tool
   version string, labeled illustrative. It makes no claim, but it should be checked
   against PyPI or replaced with a placeholder.
5. **Module 17 checklist example** ("MICrONS minnie65, CAVE materialization v795")
   was kept as a real citation format. Swap it for v1507 (the version the MICrONS lab
   notebook pins) if you want one version used consistently.
