# Navigation pass (September 2026, content pass 2)

Scope: site chrome, hubs, sequences, last-reviewed dates, what's-new page, crawl and test run.
Branch: compass-workshops. Nothing committed by this pass.

## Done so far

- (resumed) Previous run: restructured `_data/navigation.yml`, added `_includes/ui/breadcrumb.html` and `_includes/ui/page-nav.html` driven by `_data/sequences.yml`, wired both into `_layouts/default.html`, added CSS, added hub links.
- Reviewed those diffs. Menu: six groups (Start Here, Learn 9, Reference 9, Teaching 10 links under two headings, Tools 6, About 8). Footer repeats the six hubs plus What's new, License, Contact, GitHub. Layout guards `subitem.url` before comparing, so heading rows do not break the active-group test. No Liquid errors found by reading; confirmed by build below.
- `_data/sequences.yml`: added `/hidden-curriculum/funding-and-jobs/` to the hidden-curriculum list (last, since the hub page does not list it yet).
- New `scripts/refresh_last_reviewed.rb` (`--check` mode reports only). Ran it: 34 pages moved to 2026-09-26, 7 already current. The 25 module pages, four personas, datasets index, connectome-quality tool, connectivity, initiatives and models pages all changed in the 2026-09-26 audit commits, so they all read 2026-09-26; today's uncommitted edits will move dates again after the next commit and rerun. Documented in README.md (one table row).
- New `whats-new.md` (/whats-new/, layout page, content_type navigation): dated entries for 2026-09-27 (this pass), 09-26, 09-25, 09-24, 09-15/16, 09-07/08 and 09-05, each grounded in a commit message; every link points at a page that exists in the tree. Already in the About menu and footer from the previous run.
- Ticked the `last_reviewed` / what's-new line in docs/planning/NEXT_CONTENT_PASS.md.
- `_includes/ui/breadcrumb.html`: a hub that no dropdown lists now falls back to the menu group whose URL is its longest prefix, so `/teaching/answers/…` reads Home > Teaching > Module Model Responses and the hub itself gets "Up: Teaching"; same for the journal paper corpus under Reference.
- `about.md`: one sentence linking What's New (the page had no body inbound link).
- `teaching/answers/index.md`: the keys table is generated from the pages under `teaching/answers/` (10 today), with titles from `_data/modules.yml`, so new keys appear without editing the index. `teaching/index.md` and `teaching/sessions/index.md` derive their "N of the 25 modules" count the same way instead of naming three modules.
- `scripts/smoke_site.cjs`: added the September menu items, the Teaching headings, breadcrumb, previous/next in every sequence, hub and Up cases, home without chrome, footer hubs. `scripts/check_site_layout.cjs`: 13 more routes (chrome-bearing pages and the September surfaces).
- Built twice more after the fixes; all checks rerun and green (below). Disk image detached and deleted; no `_site` in the repository.
- (third run, 2026-09-28) Rechecked against `git log --since=2026-09-01`: every dated entry in whats-new.md matches commits on that date. The top entry described work not yet committed, so its heading is now "Latest" instead of 2026-09-27; whoever commits this pass should replace it with the commit date. Model-response count in that entry (02, 08, 17, 19, 21, 22, 25 plus 01, 07, 18) matches the ten files in `teaching/answers/`.
- `start-here.md`: the hidden-curriculum row now links Funding and jobs (it had no hub link in this area; the hidden-curriculum hub itself is listed under Links needed).

## Prev/next coverage

All rendered by `_includes/ui/page-nav.html`; verified in the built HTML and by the smoke test.

| Sequence | Source of order | Steps | Companion links on each step |
|---|---|---|---|
| Technical units 01-09 | `_data/technical_track.yml` | 9 | Unit page, Lecture plan, Slide deck |
| Lecture plans 01-09 (`/technical-training/slides/NN-*/`) | same | 9 | same |
| Modules 01-25 | `_data/modules.yml` | 25 | Module page, Session kit, Learner worksheet, Model responses (when one exists) |
| Session kits 01-25 | same | 25 | same |
| Module model responses | the pages under `teaching/answers/` (10 today: 01, 02, 07, 08, 17, 18, 19, 21, 22, 25) | 10 | same |
| Short lecture series, Sessions 1-5 | `_data/sequences.yml` | 5 x (plan, worksheet, answers) | Plan and slides, Learner worksheet, Model responses |
| Pathways workshops 1-10 | `_data/sequences.yml` | 10 x (plan, worksheet, answers) | Workshop plan, Learner worksheet, Model responses |
| Hidden curriculum | `_data/sequences.yml`, hub order plus funding-and-jobs last | 8 | none |

Previous/next stays inside the reader's role (worksheet to worksheet). The last step links back to the hub ("End of sequence"). Every other page below a hub shows "Up: <hub>"; a hub outside any dropdown (Module Model Responses, the journal paper corpus) now falls back to the menu group whose URL is its longest prefix, so it gets a group crumb and an Up link too. Home shows no breadcrumb and no page navigation; the six group hubs show the breadcrumb only.

## Crawl results

Third run (2026-09-28), fresh build (13 s, no Liquid warnings), same method: 273 content pages, 12 redirects. Beyond 3 clicks: the same 5 Neuronauts print READMEs, nothing else. Zero inbound body links: the same 3 READMEs. Pages with no body link (em-figures, two-day syllabus, dictionary, journal-club graph) all render an Up link, so no dead ends. `/hidden-curriculum/funding-and-jobs/`, `/teaching/faq/`, `/teaching/assessment/units/`, `/teaching/syllabi/two-day/`, `/content-library/imaging/beyond-em/`, `/content-library/connectomics/comparative-connectomics/`, `/notebooks/microns-lab/`, `/teaching/answers/`, `/kb/` and `/modes/` are all linked from the menu or a hub.

Earlier run:


Final crawl of the scratchpad build (370 HTML files; 273 content pages after excluding 12 redirect stubs, 41 Marp decks and files under /assets/ and /course/), counting header and footer links as one click from any page:

- Not reachable within 3 clicks: 5, all Neuronauts print-folder READMEs (`/neuronauts/3d-print/`, `/neuronauts/3d-print-color/` and its three `service-exports*` / `unpack-first` READMEs). They are asset-folder notes Jekyll renders as pages; the Neuronauts page links the STL and ZIP downloads directly, not these. See Links needed.
- Zero inbound body links (chrome excluded): 3, the same Neuronauts READMEs. (`/whats-new/` was a fourth until About gained a line.) Everything else has at least one body link in.
- Dead ends (no internal link in the body and no sequence or Up link): 0.
- Pages rendering neither sequence nor Up navigation: the six group hubs (/start-here/, /tracks/, /content-library/, /teaching/, /tools/, /about/), which is intended; home renders no chrome at all.

## Test results

Third run (2026-09-28): validate_frontmatter, validate_code_span_paths, validate_toggled_classes pass; check_site_links clean; smoke_site PASS; check_site_layout PASS (58 routes, four widths, Neuronauts 200%). check_anchor_links: **2 broken fragments, both in `teaching/faq.md`** (new since the earlier run; see Links needed). Image detached and deleted; no `_site` in the repository.

Earlier run:


Against the scratchpad build (Ruby 3.1.6, Bundler 2.6.9, case-sensitive image; build 19 s, no Liquid warnings):

- `validate_frontmatter.rb`, `validate_code_span_paths.rb`, `validate_toggled_classes.rb`: pass.
- `check_site_links.rb`: no missing internal links. `check_anchor_links.rb`: 374 fragment links, none broken.
- `smoke_site.cjs` (extended: the four September menu items, the two Teaching headings, breadcrumb, previous/next across units, lecture plans, modules, kits, keys, Pathways worksheets, lectures and hidden curriculum, hub and Up cases, home has no chrome, footer has six hubs): PASS.
- `check_site_layout.cjs` (58 routes; added the chrome-bearing pages and the September surfaces): PASS at 320, 390, 768 and 1440 px, and Neuronauts at 200% text.

## Links needed

Outside this pass's area. Exact places:

- `hidden-curriculum/index.md`, the page list at lines 82-96 (ends with Conflict at line 96): add a row for [Funding and jobs](/hidden-curriculum/funding-and-jobs/). The sequence already places it last, so the hub should list it last too.
- `teaching/syllabi/index.md`: no link to `/teaching/syllabi/two-day/` yet (0 mentions); add it beside the 10-week and 16-week links. The Teaching Hub already links it.
- `teaching/assessment/index.md`: no link to `/teaching/assessment/units/` (the only assessment link is `/teaching/assessment/answers/` at line 10); add a line to the unit bank and its answers (`/teaching/assessment/units-answers/`). The Teaching Hub and the model-responses index link the unit bank already.
- `teaching/answers/index.md`, "Backlog order" (lines 30-40): says "Twenty-two module keys remain" and lists 02, 08, 19, 21, 17, 22, 25 as pending; keys for those modules now exist in the tree. The table above it is now generated from the pages that exist, so only this prose is stale. Whoever finishes the keys should recount.
- `neuronauts/index.html` (download buttons around lines 2323-2326): the print-folder READMEs render as pages (`/neuronauts/3d-print/`, `/neuronauts/3d-print-color/`, and its `service-exports/`, `service-exports-2inch/`, `neuronauts-2inch-download-unpack-first/`) and nothing links them. Either link the two folder READMEs next to the STL and ZIP buttons as "print notes", or exclude `neuronauts/3d-print/README.md` and `neuronauts/3d-print-color/**/README.md` in `_config.yml` so they stop being pages.
- `modules/moduleNN.md` (25 files) and eight other pages: `scripts/refresh_last_reviewed.rb` rewrote only the `last_reviewed:` line, to 2026-09-26 (their last commit). No other change; the dates will move again after this pass is committed and the script rerun.
- `teaching/faq.md` line 222: `#detection-performance-depends-on-the-claim` does not exist on `/content-library/infrastructure/synapse-detection/` (nearest heading id is `#6-why-detectors-do-not-transfer`); fix the anchor or drop it.
- `teaching/faq.md` line 455: `#pacing-notes` does not exist on `/teaching/syllabi/` (ids there: meeting-pattern, audience-and-prerequisites, how-the-pieces-fit, the-real-data-lab, assessment); fix the anchor or add the section.
- `whats-new.md` top entry is headed "Latest" because it describes uncommitted work; replace with the commit date when this pass is committed.
