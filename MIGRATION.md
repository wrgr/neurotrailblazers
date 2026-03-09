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
