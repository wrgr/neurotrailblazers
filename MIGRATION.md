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

- Extend normalized front matter to personas, datasets, and tools.
- Introduce type-specific layouts and includes (e.g., module/persona/dataset cards and listings) while keeping existing HTML content intact.
- Add a small validation script under `scripts/` to check front matter consistency across content types.
- Define and document conventions for slide and notebook assets (e.g., `assets/slides/moduleNN/`, `assets/notebooks/moduleNN/`) and gradually align modules to them.

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
    - Slides: `assets/slides/moduleNN/moduleNN-<slug>.{pptx,pdf}`
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
  - Added canonical `slides` entries (PPTX/PDF) and canonical `notebook` entries.
  - Preserved existing notebook links by keeping them in `notebook` and mirroring them under `downloads` for backward compatibility during transition.

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
