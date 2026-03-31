## Jekyll Content Model Refactor (NeuroTrailblazers)

This document tracks incremental, content-preserving refactors to improve the site's content model and maintainability.

### Goals

- Preserve existing authored content and URLs wherever possible.
- Normalize front matter for key content types (modules, personas, datasets, tools, frameworks).
- Centralize navigation and structured metadata in `_data/`.
- Move repeated layout structure into layouts and includes over time, without breaking existing pages.

### Changes (Initial Batch)

- **Navigation data**
  - Added `_data/navigation.yml` as the canonical source for primary navigation items.
  - Updated `_layouts/default.html` to prefer `site.data.navigation.items` when present, with a fallback to `site.navigation` from `_config.yml`.
  - No navigation URLs or labels were changed.

- **Module front matter normalization**
  - Augmented front matter for **all** module files in `modules/` with normalized fields (content bodies unchanged).
  - Added fields such as: `slug`, `short_title`, `status`, `audience`, `pipeline_stage`, `merit_row_focus`, `topics`, `summary`, `learning_objectives`, `key_questions`, `slides`, `notebook`, `datasets`, `personas`, `related_tools`, `related_frameworks`, `prerequisites_list`, `next_modules`, `references`, `videos`, `downloads`, `last_reviewed`, `maintainer`.
  - Existing fields (`title`, `layout`, `permalink`, `description`, `module_number`, etc.) were preserved.
  - Where possible, values were aligned with `_data/modules.yml` (e.g., `short_title`, `summary`, and `pipeline_stage`/`stage`).

- **Frontmatter validation helper**
  - Added `scripts/validate_frontmatter.rb` to perform lightweight checks across `modules/`, `avatars/`, `datasets/`, and `tools/`.
  - Script validates presence of key fields by content type (e.g., `module_number` and `slug` for modules) and reports inconsistencies (e.g., `slug` not matching filename) without modifying files.

### Known Follow-Ups

- Replace placeholder/shim slide assets for exemplar modules (`05`, `07`, `12`, `16`) with real PPTX/PDF deliverables at canonical `assets/slides/moduleNN/` paths.
- Expand module-level relationship metadata and cards progressively across remaining modules as editorial review completes.

### Changes (Priority A Batch)

- **Persona front matter normalization (`avatars/*.md`)**
  - Added/normalized: `layout`, `title`, `role`, `permalink`, `slug`, `summary`, `strengths`, `challenges`, `goals`.
  - Added link-style and stewardship fields: `recommended_modules`, `recommended_datasets`, `recommended_tools`, `image`, `last_reviewed`, `maintainer`.
  - Existing authored HTML body content remains unchanged.

- **Dataset front matter normalization (`datasets/*.md`)**
  - Added/normalized toward a dataset model: `layout`, `slug`, `summary`, `modality`, `species`, `scale`, `access_level`, `use_cases`, `recommended_modules`, `related_tools`, `related_frameworks`, `resource_links`, `image`, `last_reviewed`, `maintainer`.
  - Preserved existing page bodies and existing permalinks; added explicit permalinks where missing for consistency.

- **Tool front matter normalization (`tools/ask-an-expert.md`, `tools/connectome-quality.md`)**
  - Added/normalized: `layout`, `slug`, `summary`, `use_cases`, `recommended_modules`, `related_datasets`, `last_reviewed`, `maintainer`.
  - Added `_layouts/tool.html` as a thin wrapper over `default` to keep rendering behavior unchanged with typed layout metadata.

- **Framework front matter normalization (`models.md`, `education/models.md`)**
  - Added framework-shape fields: `layout`, `slug`, `summary`, `framework_type`, `related_modules`, `related_tools`, `last_reviewed`, `maintainer`.
  - Added `_layouts/framework.html` as a thin wrapper over `default` for typed layout support without visual behavior changes.

- **Validation script extension**
  - Updated `scripts/validate_frontmatter.rb` to validate required keys for `avatars`, `datasets`, `tools`, and `frameworks`.
  - Added framework file coverage for `models.md` and `education/models.md`.
  - Added slug-vs-filename consistency checks for avatars, datasets, and tools.

### Changes (Priority B Batch, Part 1)

- **New landing pages**
  - Added `avatars/index.md` to list persona pages via `site.pages` filtering.
  - Added `tools/index.md` to list tool pages via `site.pages` filtering.
  - Added `frameworks/index.md` to aggregate framework pages (`models.md` and `education/models.md`).
  - These pages frame the site's emerging canonical open connectomics course as a complementary technical track.

- **Reusable card includes**
  - Added `_includes/cards/persona-card.html`.
  - Added `_includes/cards/tool-card.html`.
  - Added `_includes/cards/framework-card.html`.
  - Initial use is limited to landing pages to avoid changing authored module/dataset prose pages.

- **Validation updates for landing pages**
  - Expanded `scripts/validate_frontmatter.rb` to scan `frameworks/*.md`.
  - Added index-page exceptions for `avatars/index.md` and `tools/index.md` so strict type checks only apply to detail pages.

- **Planning note captured (not implemented)**
  - Future technical connectomics track slug sketch (for later content buildout):  
    `01-why-map-the-brain`, `02-brain-data-across-scales`, `03-em-prep-and-imaging`, `04-volume-reconstruction-infrastructure`, `05-neuronal-ultrastructure`, `06-axons-and-dendrites`, `07-glia`, `08-segmentation-and-proofreading`, `09-connectome-analysis-neuroai`, `atlas-connectomics-reference`.

### Changes (Priority B/C Bridge Batch)

- **Navigation discoverability**
  - Updated `_data/navigation.yml` to add first-class links to `/avatars/`, `/tools/`, and `/frameworks/`.
  - Consolidated tool-specific links under a `Tools` dropdown (`Ask Expert`, `Proofreading`) while preserving their URLs.

- **Module related-content include**
  - Added `_includes/ui/related-content.html` to render optional related links from module front matter fields:
    - `datasets`
    - `personas`
    - `related_tools`
    - `related_frameworks`
    - `next_modules`
  - Updated `_layouts/module.html` to include this partial after page content, keeping module markdown/HTML files unchanged.

- **Validation and checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - Full Jekyll build was not run in this environment because no `Gemfile` is present (`Bundler::GemfileNotFound`).

### Changes (Technical Track Planning Data)

- **Canonical technical track data model (planned content only)**
  - Added `_data/technical_track.yml` as the structured source of truth for the planned technical connectomics track sequence.
  - Captures course positioning, status, and the current planned module slugs/titles.
  - This does not create or rename any pages.

- **Reusable roadmap include**
  - Added `_includes/ui/technical-track-roadmap.html` to render the planned track list from data.
  - Included this roadmap on:
    - `start-here.md`
    - `modules/index.md`
  - Roadmap is explicitly labeled planned, not yet implemented as module pages.

### Changes (Local Jekyll Runtime Setup)

- **Bundler/Jekyll project setup**
  - Added `Gemfile` and generated `Gemfile.lock` for local reproducible Jekyll runs.
  - Added compatibility pins for this environment:
    - `ffi < 1.17`
    - `jekyll-sass-converter ~> 2.2`
  - These avoid Ruby 2.6 incompatibilities seen with newer transitive dependencies.

- **Build artifact ignore rules**
  - Updated `.gitignore` to ignore:
    - `/.bundle/`
    - `/vendor/bundle/`
    - `/_site/`

- **Build verification**
  - Verified successful build with:
    - `BUNDLE_PATH=vendor/bundle BUNDLE_DISABLE_SHARED_GEMS=true bundle exec jekyll build`

### Changes (Technical Track Mapping)

- **Mapped planned track items to existing modules**
  - Extended `_data/technical_track.yml` with:
    - `mapped_modules` arrays (existing `moduleNN` links where overlap exists)
    - `mapping_note` context per track item
  - Updated `_includes/ui/technical-track-roadmap.html` to render:
    - planned track slug/title
    - current coverage links to existing modules
    - mapping notes

### Changes (Priority C Batch, Layout + Cards)

- **Generic page hero partial (opt-in)**
  - Added `_includes/ui/page-hero.html`.
  - Hero rendering is opt-in via `use_layout_hero: true` to avoid double-hero issues on pages that already define custom hero sections.

- **Strengthened type-specific layouts**
  - Updated:
    - `_layouts/page.html`
    - `_layouts/module.html`
    - `_layouts/avatar.html`
    - `_layouts/dataset.html`
    - `_layouts/tool.html`
    - `_layouts/framework.html`
  - Each now wraps content in a type-specific `layout-*` container and can render the shared page hero include.
  - `_layouts/module.html` still includes `_includes/ui/related-content.html` after page content.

- **Additional reusable card includes**
  - Added `_includes/cards/module-card.html`.
  - Added `_includes/cards/dataset-card.html`.

- **Card include adoption on listing pages**
  - `modules/index.md` now includes a generated “Module Catalog (Generated Cards)” section using `site.modules` + `module-card`.
  - `datasets/index.md` now includes a generated “Dataset Pages (Generated Cards)” section using dataset pages + `dataset-card`.
  - Existing authored sections on both pages were preserved.

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `bundle exec jekyll build` passes with local bundle env vars.

### Changes (Priority D Batch, Asset Conventions)

- **Documented and applied slide/notebook conventions**
  - Canonical conventions established:
    - Slides: `assets/slides/moduleNN/moduleNN-<slug>.pdf` (with optional `.pptx` companion when available)
    - Notebooks: `assets/notebooks/moduleNN/moduleNN-<slug>.ipynb`
  - Created convention directories for exemplar modules:
    - `assets/slides/module05`, `module07`, `module12`, `module16`
    - `assets/notebooks/module05`, `module07`, `module12`, `module16`
    - with `.gitkeep` placeholders.

- **Exemplar module alignment (without breaking legacy links)**
  - Updated frontmatter in:
    - `modules/module05.md`
    - `modules/module07.md`
    - `modules/module12.md`
    - `modules/module16.md`
  - Added canonical `slides` entries and canonical `notebook` entries.
  - Preserved existing notebook links by keeping them in `notebook` and mirroring them under `downloads` for backward compatibility during transition.

- **Placeholder slide files for exemplar modules**
  - Added canonical placeholder PDF files (non-final content) for:
    - `assets/slides/module05/module05-electron-microscopy-and-image-basics.pdf`
    - `assets/slides/module07/module07-proofreading-and-quality-control.pdf`
    - `assets/slides/module12/module12-big-data-in-connectomics.pdf`
    - `assets/slides/module16/module16-scientific-visualization-for-connectomics.pdf`
  - Exemplar module frontmatter now points to the canonical PDF paths so links resolve during content authoring.

### Changes (Priority D Follow-Up: Compatibility Shims)

- **Notebook compatibility shims added**
  - Created canonical notebook shim files for exemplar modules:
    - `assets/notebooks/module05/module05-electron-microscopy-and-image-basics.ipynb`
    - `assets/notebooks/module07/module07-proofreading-and-quality-control.ipynb`
    - `assets/notebooks/module12/module12-big-data-in-connectomics.ipynb`
    - `assets/notebooks/module16/module16-scientific-visualization-for-connectomics.ipynb`
  - Added legacy-path shim notebooks under `notebooks/intro/` to avoid breakage for existing references:
    - `ImageAndSegmentationDownload.ipynb`
    - `MostSynapsesInAndOut.ipynb`
    - `DashSynapseExplorer.ipynb`
    - `MeshExample.ipynb`
    - `Render3DScaleBar.ipynb`
  - Shim notebooks explicitly point between legacy and canonical paths for transition clarity.

### Changes (Priority D Follow-Up: Validator Hardening)

- **Asset-link validation for modules**
  - Extended `scripts/validate_frontmatter.rb` with module asset checks for:
    - `slides`
    - `notebook`
    - `downloads`
  - Validator now warns when these fields:
    - are not arrays
    - contain non-URL entries that do not start with `/`
    - point to local files that do not exist
  - This improves enforcement of the canonical asset-link convention while remaining read-only (warnings only).

### Changes (Technical Track Buildout: Draft Pages)

- **Technical training site area added**
  - Added a dedicated track hub at:
    - `/technical-training/`
  - Added draft unit pages at:
    - `/technical-training/01-why-map-the-brain/`
    - `/technical-training/02-brain-data-across-scales/`
    - `/technical-training/03-em-prep-and-imaging/`
    - `/technical-training/04-volume-reconstruction-infrastructure/`
    - `/technical-training/05-neuronal-ultrastructure/`
    - `/technical-training/06-axons-and-dendrites/`
    - `/technical-training/07-glia/`
    - `/technical-training/08-segmentation-and-proofreading/`
    - `/technical-training/09-connectome-analysis-neuroai/`
    - `/technical-training/atlas-connectomics-reference/`

- **Source-priority and unit-production workspace**
  - Added `course/` workspace with:
    - `decision-rules.md` (source precedence: `frompat` > `neuroAI` > `assets_outreach`)
    - `workboard.md` (unit production status)
    - per-unit source docs and figure shortlist files
  - This workspace drives both web-page drafts and future presentation synthesis.

- **Discoverability and prominence updates**
  - Added top navigation link to `/technical-training/`.
  - Updated homepage hero/CTA and resource cards to emphasize:
    - `Technical Training: Nanoscale Connectomics`
    - direct entry to `/technical-training/`

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `bundle exec jekyll build` passes.
  - Internal link scan over generated `_site` reports no broken internal links.

### Changes (Technical Track Enrichment: Journal Club + Dictionary)

- **Journal club list added (separate from module pages)**
  - Added `/technical-training/journal-club/` with:
    - 3 required papers
    - 3 optional papers
    - 3 relevant videos/media resources
  - Each entry includes plain-language contribution text and module-fit mapping.

- **Connectomics dictionary added**
  - Added `_data/connectomics_dictionary.yml` as structured glossary source.
  - Added `/technical-training/dictionary/` page to render terms, categories, and definitions.

- **Unit visual integration started**
  - Added selected glia training images under:
    - `assets/images/technical-training/07-glia/`
  - Updated `/technical-training/07-glia/` with draft visual training section and attribution note.
  - Noted missing thumbnails for two manifest-listed glia IDs (`S02`, `S07`) pending recovery.

- **Additional unit visual integration (morphology sequence)**
  - Added selected axon/dendrite training images under:
    - `assets/images/technical-training/06-axons-and-dendrites/`
  - Added selected neuronal-ultrastructure training images under:
    - `assets/images/technical-training/05-neuronal-ultrastructure/`
  - Updated:
    - `/technical-training/06-axons-and-dendrites/`
    - `/technical-training/05-neuronal-ultrastructure/`
    with visual training galleries and attribution notes.
  - Noted missing extracted thumbnails for some `RIV-AXDEN` manifest-listed IDs (`S04`, `S06`, `S10`, `S16`) and replaced with available neighboring cues.

- **Additional unit visual integration (analysis + proofreading sequence)**
  - Added selected figure assets under:
    - `assets/images/technical-training/08-segmentation-and-proofreading/`
    - `assets/images/technical-training/09-connectome-analysis-neuroai/`
  - Updated:
    - `/technical-training/08-segmentation-and-proofreading/`
    - `/technical-training/09-connectome-analysis-neuroai/`
    with draft visual training galleries, historical-context notes, and source attribution.
  - Noted and handled missing extracted IDs with documented fallbacks:
    - `RIV-AXDEN-S06-01`, `RIV-AXDEN-S09-01`
    - `SRC-MODULE14_LESSON2-S04-01`, `SRC-MODULE14_LESSON2-S07-01`
    - `SRC-21_02388_X_TECHTALK_-S34-01`
    - `SRC-MODULE13_LESSON3-S10-01`

- **Unit structure consistency pass**
  - Standardized instructional structure across technical unit pages with:
    - practical workflow steps
    - discussion prompts
    - related resource links (journal club + dictionary)
    - quick activity blocks for active learning

- **Dual review artifacts added**
  - `course/reviews/technical-accuracy-review.md`
  - `course/reviews/instructional-design-accessibility-review.md`
- Reviews include findings ordered by severity, applied fixes, and residual risks.

### Changes (Technical Track: Lecture and Deck Production Pass)

- **Lecture-ready slide draft pages expanded**
  - Upgraded all technical-track slide draft pages under `/technical-training/slides/` from generic 12-step placeholders to lecture-ready outlines.
  - Each unit now includes:
    - audience/session profile
    - timed slide sequence
    - technical talking points
    - assessment artifacts and rubric dimensions
    - explicit figure integration hooks

- **Deck authoring pack added**
  - Added `course/decks/` with one production-oriented deck spec per unit plus `README.md`.
  - Each deck spec defines:
    - slide-by-slide production blocks
    - source priorities
    - figure IDs and usage guidance
    - instructor notes and assessment prompts

- **Content import planning formalized**
  - Added `course/decks/content-import-matrix.md` to map source families to units and establish acceptance criteria for imported technical claims.
  - Priority policy captured explicitly:
    - `frompat` (primary morphology/proofreading)
    - `neuroAI` (primary for Unit 09)
    - `assets_outreach` (historical/context support)

- **Figure shortlist correction pass**
  - Corrected `course/units/figures/06-axons-and-dendrites-selected-v1.md` to match available extracted image IDs.
  - Corrected `course/units/figures/07-glia-selected-v1.md` to remove unavailable manifest IDs and document fallback handling.

- **Marp slide-source workflow added**
  - Added `course/decks/marp/` with draft markdown slide sources for:
    - `01` through `09`
    - `atlas-connectomics-reference`
  - Added `course/decks/marp/README.md` with usage instructions.
  - Updated `technical-training/slides/index.md` to point maintainers to the Marp source directory.

- **Checks**
  - `bundle exec jekyll build` passes after all deck and marp additions.
  - `ruby scripts/validate_frontmatter.rb` remains passing.

### Changes (Technical Track: Visual Coverage and Validation Automation)

- **Source figure import automation**
  - Added `scripts/import_deck_figures.rb` to import `FIG-*` assets referenced by `course/decks/*.md` from the local extraction package into:
    - `assets/images/technical-training/<unit-slug>/`
  - Used this to populate visual assets for:
    - `01-why-map-the-brain`
    - `02-brain-data-across-scales`
    - `03-em-prep-and-imaging`
    - `04-volume-reconstruction-infrastructure`
    - `atlas-connectomics-reference` (partial, then remapped to available extracted IDs)

- **Figure-reference validation helper**
  - Added `scripts/validate_figure_refs.rb`.
  - Validates `FIG-*` references in production deck/page docs against locally available assets.
  - Also validates local image paths in Marp slide sources.
  - Current result: no missing figure references in production docs after atlas remap.

- **Atlas reference visual remap**
  - Updated atlas shortlist and deck spec to use available module14-lesson3 extracted IDs (for example `S03-02`, `S05-01`, `S08-01`, `S10-01`, `S13-01`, `S19-01`, `S20-03`) instead of unavailable originally planned IDs.
  - Expanded `/technical-training/atlas-connectomics-reference/` visual section accordingly.

- **Unit page visual parity**
  - Added draft visual-context galleries to previously text-heavy units:
    - `/technical-training/01-why-map-the-brain/`
    - `/technical-training/02-brain-data-across-scales/`
    - `/technical-training/03-em-prep-and-imaging/`
    - `/technical-training/04-volume-reconstruction-infrastructure/`
  - This brings visual depth closer to units 05-09.

### Changes (Track-First IA Refactor, Fadel-Aligned)

- **Three canonical tracks introduced**
  - Added `_data/track_catalog.yml` defining the new learner-facing architecture:
    - `Core Concepts & Methods` (Knowledge + Skills)
    - `Research in Action` (Skills + Meta-learning)
    - `Career & Community` (Character + Meta-learning)
  - Each track includes pathway tags and curated resource links.

- **New track pages**
  - Added:
    - `/tracks/`
    - `/tracks/core-concepts-methods/`
    - `/tracks/research-in-action/`
    - `/tracks/career-and-community/`
  - These pages are now the canonical entry point for curriculum navigation.

- **Navigation and homepage shifted to track-first**
  - Updated `_data/navigation.yml`:
    - Added top-level `Tracks` menu with 3 track links.
    - Renamed `Modules` to `Legacy Modules`.
  - Updated `index.html` and `start-here.md` to emphasize track-based pathways over module numbering.
  - Updated `footer.md` to reflect track language in place of COMPASS branding at the global footer level.

- **Legacy module framing demoted (not removed)**
  - Updated `/modules/` index to `Legacy Module Archive` framing.
  - Kept module URLs/pages intact for compatibility and archival access.

- **Metadata transition to track model**
  - Added `track` and `pathways` front matter fields across technical training, journal club, dictionary, and start-here pages.
  - This enables future filtering/personalization without relying on module IDs.

- **Cleanup**
  - Removed `.DS_Store` artifacts and added ignore patterns to `.gitignore`.

### Changes (Concept-First Discovery Layer)

- **Concept explorer added**
  - Added `_data/concepts.yml` with concept records mapped to:
    - track
    - user-needs tags
    - resource links
  - Added `/concepts/` as a concept-first discovery page to reduce dependence on module numbering.
  - Added interactive concept filtering by track and user-need tags on `/concepts/`.

- **Reusable concept and track includes**
  - Added `_includes/cards/concept-card.html`.
  - Added `_includes/ui/learning-tracks.html` to render track cards consistently across landing pages.

- **Entry-point wiring for concept-first navigation**
  - Added top-nav entry for `/concepts/`.
  - Added concept-track CTAs/sections on:
    - homepage
    - start-here
    - datasets index
    - tools index
    - frameworks index
    - avatars index
    - models pages
    - technical-training hub
    - modules archive notice

- **Track pages linked to concepts**
  - Added concept-preview sections on each `/tracks/*` page using concept cards filtered by track.
  - This supports quick pivots between track-based and need-based navigation.
  - Added query-parameter prefiltering on `/concepts/` (`track`, `need`) and wired shortcut links from home/start pages for common user-needs entry points.
  - Added reusable `_includes/ui/track-need-explorer.html` so each track page now supports on-page concept filtering by user need.

- **Framework wording refinement**
  - Updated models pages and legacy module archive copy to de-emphasize COMPASS as primary branding.
  - Current framing uses `professional pathways workshops` with explicit historical note where needed.

- **Positioning update**
  - Discovery now emphasizes:
    - `tracks` (high-level structure)
    - `concepts` (needs-based entry)
  - Legacy modules remain available as delivery/archive objects rather than primary learner navigation.

- **Track metadata expanded across detail pages**
  - Added `track` and `pathways` fields to detail pages in:
    - `avatars/*.md`
    - `datasets/{access,mouseconnects,workflow}.md`
    - `tools/{ask-an-expert,connectome-quality}.md`
  - This supports future user-need filtering without relying on module IDs.
  - Also cleaned duplicate `recommended_modules` keys in tool frontmatter.

- **Validation guardrail for track model**
  - Extended `scripts/validate_frontmatter.rb` to warn when `track`/`pathways` metadata is missing on track-first learner-facing pages.
  - Added track metadata to `tracks/*.md` and `/concepts/` to align with the validator.

- **Checks**
  - `bundle exec jekyll build` passes.
  - `ruby scripts/validate_frontmatter.rb` passes.
  - Internal link scan reports no broken internal links.

### Changes (Priority B Follow-Up: Frameworks + Card Consistency)

- **Frameworks landing refinement**
  - Updated `frameworks/index.md` with complementary-track context text.
  - Added the technical track roadmap include to `/frameworks/` for direct framework-to-track visibility.

- **Card include consistency cleanup**
  - Standardized card description fallback behavior across:
    - `_includes/cards/persona-card.html`
    - `_includes/cards/tool-card.html`
    - `_includes/cards/framework-card.html`
    - `_includes/cards/module-card.html`
    - `_includes/cards/dataset-card.html`
  - Pattern now consistently prefers `summary`, then falls back to `description` where available.

### Changes (Priority B/C/D Sequential Batch)

- **Redirect stub strategy implemented**
  - Added `_layouts/redirect.html` for static, plugin-free redirects (meta refresh + JS + canonical).
  - Added compatibility redirect stubs:
    - `/frameworks/models/` -> `/models/`
    - `/frameworks/research-incubator-model/` -> `/models/`
    - `/frameworks/education-models/` -> `/education/models/`
    - `/tools/ask-an-expert/` -> `/ask-an-expert/`
  - Updated validator to skip `layout: redirect` pages so strict content-type field checks apply only to content pages.

- **Deeper tools/framework progression wiring**
  - Added `_includes/ui/track-progression.html` to render a progression-aligned view from `_data/technical_track.yml`.
  - Includes mapped-module links and optional contextual overlays:
    - tools aligned by overlap with `recommended_modules`
    - frameworks aligned by overlap with `related_modules`
  - Wired progression include into:
    - `tools/index.md` (`show_tools=true`)
    - `frameworks/index.md` (`show_frameworks=true`)

- **Tool/framework metadata alignment**
  - Added concrete `recommended_modules` and `related_datasets` to:
    - `tools/ask-an-expert.md`
    - `tools/connectome-quality.md`
  - Added concrete `related_modules`/`related_tools` to:
    - `models.md`
    - `education/models.md`

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Content Linking Batch: Modules 01-08 + Personas + Datasets)

- **Module relationship metadata populated (01-08)**
  - Updated `modules/module01.md` through `modules/module08.md` to replace placeholder arrays with concrete links for:
    - `datasets`
    - `personas`
    - `related_tools`
    - `related_frameworks`
    - `next_modules`
  - Goal: make `_includes/ui/related-content.html` render meaningful connections instead of empty sections.

- **Persona recommendations populated**
  - Updated all core persona pages:
    - `avatars/undergradstudent.md`
    - `avatars/gradstudent.md`
    - `avatars/researcher.md`
    - `avatars/mentor.md`
  - Replaced empty placeholders for:
    - `recommended_modules`
    - `recommended_datasets`
    - `recommended_tools`

- **Dataset relationship metadata populated**
  - Updated:
    - `datasets/access.md`
    - `datasets/workflow.md`
    - `datasets/mouseconnects.md`
    - `datasets/index.md`
  - Replaced empty placeholders for:
    - `recommended_modules`
    - `related_tools`
    - `related_frameworks`

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Content Linking Batch: Modules 09-16)

- **Module relationship metadata populated (09-16)**
  - Updated `modules/module09.md` through `modules/module16.md` to replace placeholder arrays with concrete links for:
    - `datasets`
    - `personas`
    - `related_tools`
    - `related_frameworks`
    - `next_modules`
  - This extends the same linking pattern used in modules `01-08` to cover the remainder of the early-to-mid technical track progression.

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Concept Explorer Recommendation UX)

- **Dynamic recommendations tied to current filters**
  - Updated `concepts/index.md` to add a "Recommended Next Resources" panel below the filtered concept cards.
  - The page script now computes up to five deduplicated links from currently visible cards (respecting `track` and `need` filters) and renders them in `#recommended-list`.
  - This keeps concept discovery action-oriented without requiring users to open each card to find a concrete next step.

- **Checks**
  - `bundle exec jekyll build` passes.

### Changes (Need-Based Technical Entry Points)

- **Technical course map enriched with learner-need metadata**
  - Updated `_data/technical_track.yml` for all 10 units to include:
    - `primary_concepts`
    - `user_needs`
  - This allows the technical sequence to remain available while enabling concept-first routing.

- **Technical training hub shifted further from sequence-first navigation**
  - Updated `technical-training/index.md` with:
    - a "Start by learner need" shortcut section
    - need tags on each unit card linking to pre-filtered Concept Explorer views
    - legacy module overlap retained as secondary context (`small` annotation)

- **Language cleanup**
  - Updated `start-here.md` quick-start checklist item from "Begin your first module" to "Begin with one concept or technical unit."

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Concept Links Embedded in Technical Units)

- **Reusable technical-unit concept include**
  - Added `_includes/ui/technical-unit-concepts.html`.
  - For technical unit pages, this include surfaces:
    - related concept summaries
    - direct links into pre-filtered Concept Explorer views
    - learner-need tags for quick pivoting

- **Layout-level integration**
  - Updated `_layouts/page.html` to auto-include `ui/technical-unit-concepts.html` for `/technical-training/*` unit pages.
  - Explicitly excluded:
    - `/technical-training/` hub
    - `/technical-training/slides/*`
    - `/technical-training/journal-club/*`
    - `/technical-training/dictionary/*`
  - Result: unit pages get concept context automatically without per-page edits.

- **Track hub prominence for technical course**
  - Updated `tracks/index.md` with an explicit featured link to the canonical technical course.

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Capability-First Authoring Layer)

- **Structured capability data for all technical units**
  - Added `_data/technical_capabilities.yml` with per-unit:
    - `capability_statement`
    - `expertise` roles
    - `core_concepts` (term + plain-language description)
    - `studio_activity` (objective, prompt, steps, outputs)
    - `success_artifacts`
  - This enables consistent capability development independent of legacy module framing.

- **Automatic page rendering of capability briefs**
  - Added `_includes/ui/technical-capability-brief.html`.
  - Updated `_layouts/page.html` to auto-include capability briefs on technical unit pages (same scope/exclusions as concept-link include).
  - Result: each technical unit now surfaces required expertise, concept payload, activity design, and assessment artifacts in-page.

- **Production workflow support docs**
  - Added `course/capability-development-plan.md` defining 1x1 execution model, ownership lanes, definition of done, and prioritized unit order.
  - Added `course/templates/capability-spec-template.md` for unit-level authoring and SME review.
  - Updated `course/workboard.md` to track `capability_status` in addition to draft status.

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Capability Deepening Pass: Unit 05)

- **Unit 05 content expansion (`technical-training/05-neuronal-ultrastructure.md`)**
  - Added explicit technical scope and measurable capability target.
  - Added concept payload section with:
    - technical definition framing
    - plain-language explanation
    - misconception guardrails
  - Added a full studio activity design:
    - scenario
    - task sequence
    - expected outputs
  - Added unit-level assessment rubric with pass/strong/failure criteria.

- **Production tracking updates**
  - Updated `course/units/05-neuronal-ultrastructure.md` status metadata and deepening notes.
  - Updated `course/workboard.md`:
    - unit status set to `review_needed`
    - capability status set to `activity_drafted`

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Instructional Framework Adoption + Module 18 Rewrite)

- **Instructional framework adoption**
  - Added `course/instructional-framework.md`.
  - Adopted combined model for authoring and review:
    - Understanding by Design (backward design)
    - Bloom's Taxonomy (depth targets)
    - Cognitive Apprenticeship (modeling -> coaching -> fading -> reflection)
    - UDL (accessibility and multiple expression pathways)
  - Updated `course/templates/capability-spec-template.md` to include:
    - Bloom target
    - cognitive-apprenticeship plan
    - UDL expression options
    - accessibility check requirements

- **Module 18 deep rewrite**
  - Replaced weak outline page content in `modules/module18.md` with a full capability-based module:
    - explicit capability target
    - concept payload (technical + plain-language + misconception guardrails)
    - preprocessing workflow
    - studio activity + expected outputs
    - assessment rubric
    - concrete teaching resource links
  - Normalized metadata to align with technical content:
    - title/description/summary now consistent with Data Cleaning and Preprocessing.

- **Concept teaching-resource packs**
  - Expanded `_data/concepts.yml` with `explanation` and `teaching_resources` for all concept entries.
  - Updated `_includes/cards/concept-card.html` to render teaching packs:
    - lesson
    - activity
    - slides
    - references
  - Result: concepts now expose a complete "how to learn this" bundle directly in the explorer.

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Evidence-First Technical Content Anchoring)

- **Canonical evidence library and unit mappings**
  - Added `_data/technical_evidence.yml` with:
    - canonical paper library (DOI/source links)
    - canonical dataset library
    - per-unit evidence mappings for all technical units (`01`-`09`, `atlas`)
    - per-unit competency checks tied to evidence usage

- **Automatic in-page evidence packs**
  - Added `_includes/ui/technical-evidence-pack.html`.
  - Updated `_layouts/page.html` to auto-render evidence packs on technical unit pages (excluding hub/slides/journal-club/dictionary).
  - Result: each technical unit now surfaces key papers, key datasets, and competency checks in-page.

- **Evidence validation script**
  - Added `scripts/validate_technical_evidence.rb`.
  - Script checks:
    - every `technical_track` unit has an evidence entry
    - each unit has minimum evidence anchors (papers/datasets/competency checks)
    - mapped paper/dataset IDs exist in the shared library

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `ruby scripts/validate_technical_evidence.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Deep Rewrites: Modules 17 and 19)

- **Module 17 rewritten from outline to capability unit**
  - Replaced generic card content in `modules/module17.md` with:
    - capability target
    - concept set with misconception guardrails
    - concrete connectomics writing workflow
    - studio activity and deliverables
    - assessment rubric
    - evidence anchors (papers + datasets + competency checks)
  - Metadata aligned to dissemination-stage scientific writing focus.

- **Module 19 rewritten from outline to capability unit**
  - Replaced generic card content in `modules/module19.md` with:
    - capability target
    - ethics and peer-review concept set grounded in connectomics workflows
    - structured review/ethics workflow
    - review-board simulation activity
    - assessment rubric
    - evidence anchors (papers + datasets + competency checks)
  - Fixed metadata mismatch (`short_title`, `pipeline_stage`, `summary`) to match module topic.

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `ruby scripts/validate_technical_evidence.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Deep Rewrite: Module 20)

- **Module 20 topic realignment and rewrite**
  - Replaced `modules/module20.md` grant-writing placeholder content with a full connectomics-focused module:
    - new title: "Statistical Models and Inference for Connectomics"
    - capability target, concept set, and misconception guardrails
    - null-model and multiplicity-aware inference workflow
    - studio activity and rubric
    - evidence anchors (papers + datasets + competency checks)
  - Resolved prior metadata mismatch between `short_title` and page title/topic.

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `ruby scripts/validate_technical_evidence.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (60-Minute Tutorial Format + Module 21 Rewrite)

- **60-minute tutorial run-of-show blocks added**
  - Added instructor-ready, minute-by-minute tutorial sections to:
    - `technical-training/05-neuronal-ultrastructure.md`
    - `modules/module18.md`
  - New blocks include:
    - pre-class prep
    - timed delivery sequence
    - instructor cue language
    - formative checkpoints
    - post-class assignment expectations

- **Module 21 rewritten to match normalized topic**
  - Replaced generic mentorship placeholder with:
    - title/topic aligned to `Reproducibility and FAIR Principles`
    - capability target + concept set
    - hidden-curriculum scaffold section (explicit norms and expectations)
    - workflow, studio activity, rubric, and evidence anchors

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `ruby scripts/validate_technical_evidence.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Deep Rewrite: Module 22)

- **Module 22 rewritten for competency-based delivery**
  - Replaced public-engagement placeholder cards with a full scientific presentation module:
    - capability target
    - concept set with misconception guardrails
    - hidden curriculum scaffold (conference/talk norms made explicit)
    - 60-minute run-of-show
    - studio activity and rubric
  - Metadata retained/aligned with normalized `short_title` focus on writing + presentation.

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `ruby scripts/validate_technical_evidence.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Deep Rewrites: Modules 23-25)

- **Module 23 rewritten and aligned**
  - Replaced career-placeholder content in `modules/module23.md` with:
    - topic-aligned "Posters, Abstracts, and Conferences" capability module
    - hidden-curriculum scaffold for conference norms/networking
    - 60-minute run-of-show, studio activity, and rubric
  - Metadata now aligns with normalized `short_title`.

- **Module 24 rewritten and aligned**
  - Replaced systems-thinking placeholder in `modules/module24.md` with:
    - "Career Pathways and Graduate School Preparation" capability module
    - explicit hidden-curriculum norms (outreach, recommendations, fit language)
    - 60-minute run-of-show, activity outputs, and rubric
  - Metadata now aligns with normalized `short_title`.

- **Module 25 deepened**
  - Replaced generic portfolio cards in `modules/module25.md` with:
    - competency-evidence architecture for capstone portfolios
    - hidden-curriculum scaffold for reviewer expectations
    - 60-minute run-of-show, studio activity, and assessment rubric

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `ruby scripts/validate_technical_evidence.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Deep Rewrites: Modules 12-13)

- **Module 12 rewritten and aligned**
  - Replaced mismatched "functional annotation" placeholder in `modules/module12.md` with a full `Big Data in Connectomics` capability module.
  - Added:
    - concept set with misconception guardrails
    - hidden-curriculum scaffold for data-engineering norms
    - 60-minute run-of-show
    - studio activity, rubric, and resource links
  - Metadata now aligned to normalized `short_title` and analysis-stage infrastructure focus.

- **Module 13 deepened**
  - Replaced generic data-science cards in `modules/module13.md` with a full `Machine Learning in Neuroscience` capability module.
  - Added:
    - leakage-aware ML concepts
    - hidden-curriculum scaffold for responsible model reporting
    - 60-minute run-of-show
    - studio activity, rubric, and resource links

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `ruby scripts/validate_technical_evidence.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Full Module Rewrite Completion + Site Polish)

- **Completed full module rewrite (`01-25`)**
  - Rewrote remaining shallow modules:
    - `modules/module01.md` through `modules/module11.md`
    - `modules/module14.md` through `modules/module16.md`
  - All module pages now follow the same capability/tutorial pattern:
    - capability target
    - concept/workflow scaffold
    - 60-minute run-of-show
    - studio activity and rubric
    - teaching resources and quick practice prompt

- **Navigation and module library polish**
  - Updated `_data/navigation.yml` to relabel `Legacy Modules` as `Modules`.
  - Updated `modules/index.md` copy to position modules as an active tutorial library (not legacy archive).
  - Corrected module naming inconsistencies in matrix text and shared module metadata.
  - Updated `_data/modules.yml` entry for module 19 to align with rewritten topic.

- **Global copy-edit pass (high-traffic pages)**
  - Refined `start-here.md` section headings for cleaner, more consistent instructional tone.
  - Preserved structure and links while reducing stylistic noise in headings.

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `ruby scripts/validate_technical_evidence.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Teaching Materials System + Slide Production Layer)

- **Generated teaching materials for all modules**
  - Added `scripts/generate_module_teaching_materials.rb`.
  - Script-generated assets for all `module01`-`module25`:
    - `modules/slides/moduleNN.md` (browsable deck pages)
    - `course/decks/marp/modules/moduleNN.marp.md` (slide source)
    - `assets/worksheets/moduleNN/moduleNN-activity.md` (activity worksheets)
  - Added slide hub page:
    - `modules/slides/index.md`

- **Module page integration**
  - Added `_includes/ui/module-teaching-materials.html`.
  - Updated `_layouts/module.html` to render teaching links on every module page:
    - slide deck page
    - activity worksheet
    - Marp source path

- **Navigation and render tooling**
  - Updated `_data/navigation.yml` to include `Module Slides` in primary nav.
  - Updated `scripts/render_marp.sh` to recursively render nested `*.marp.md` files (including `course/decks/marp/modules/`).

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `ruby scripts/validate_technical_evidence.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Delivery-Ready Lesson UX + Rendered Deck Outputs)

- **Lesson-flow UI for modules**
  - Added `_includes/ui/module-lesson-map.html` and integrated it in `_layouts/module.html`.
  - Each module now opens with a consistent instructional path:
    - Learn -> Practice -> Check -> Teach
  - Added supporting style rules in `assets/css/site-styles.css`.

- **Rendered deck links in teaching pages**
  - Updated `scripts/generate_module_teaching_materials.rb` template so each `modules/slides/moduleNN.md` includes:
    - Marp source path
    - rendered HTML deck path
    - worksheet path
  - Regenerated all module slide pages (`modules/slides/module01.md` ... `module25.md`).

- **Marp rendering verified**
  - Updated `scripts/render_marp.sh` to avoid stdin inheritance issues during `find` loop and to support nested paths.
  - Rendered all available decks to:
    - `course/decks/marp/out/*.html` (technical track decks)
    - `course/decks/marp/out/modules/moduleNN.html` (module decks)

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `ruby scripts/validate_technical_evidence.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Teaching Hub + Browseability Pass)

- **New teaching landing area**
  - Added `teaching/index.md` (`/teaching/`) as a centralized instructor hub.
  - Added `_includes/cards/teaching-module-card.html` for module-level teaching kit cards.
  - Each card links directly to:
    - module lesson page
    - module slide page
    - rendered HTML deck
    - Marp source
    - worksheet

- **Navigation and entry-point updates**
  - Updated `_data/navigation.yml`:
    - added first-class `Teaching` menu with `Teaching Hub` and `Module Slides`.
  - Updated:
    - `index.html` (home resource card for Teaching Hub)
    - `modules/index.md` (teaching-kit callout)
    - `modules/slides/index.md` (link back to Teaching Hub)
    - `technical-training/index.md` (Teaching Hub CTA)

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `ruby scripts/validate_technical_evidence.rb` passes.
  - `bundle exec jekyll build` passes.

### Changes (Facilitator Layer + Copy Cleanup)

- **Facilitator guide**
  - Added `teaching/facilitator-guide.md` (`/teaching/facilitator-guide/`) with:
    - 60-minute delivery template
    - quality checks for instructors
    - material-location map
  - Linked from `teaching/index.md` and teaching navigation dropdown.

- **Instructional copy normalization**
  - Replaced residual draft wording in technical training pages:
    - `Visual context/training set (draft)` -> `Visual context/training set`
    - `Draft lecture deck` -> `Teaching slide deck`
  - Updated `technical-training/slides/index.md` language and title to production wording.
  - Added explicit links from technical slide pages to teaching hub and rendered deck outputs.

- **Checks**
  - `ruby scripts/validate_frontmatter.rb` passes.
  - `ruby scripts/validate_technical_evidence.rb` passes.
  - `bundle exec jekyll build` passes.
