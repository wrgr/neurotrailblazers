# Visual teaching and card-layout review

This change builds on deployed PR #188. It does not merge or deploy automatically and does not mark Modules 02-09 ready.

## Scope

The shared card stylesheet fills grid tracks instead of retaining a 260px card inside a wider column. It reduces nested gutters, retains 44px controls, preserves readable text, and explicitly retains the non-sticky paper filters.

Sixteen instructional visual examples are authored for Modules 02-09: help-seeking and support maps, a reproducible notebook chain and synthetic code output, credited H01 anatomy/EM/segmentation/proofreading panels, hypothesis-comparison diagrams, and a small verifiable synthetic skeleton. Scientific images retain original aspect ratios and scale bars; colors do not constitute ground truth. Each example has a visible caption or explanation, discussion question, source, and longer text description in the reading version. Descriptive labels and positional descriptions supplement color.

The module teaching-materials generator splits long simple lists across slides and retains further explanation in notes. It no longer overwrites the hand-maintained searchable session catalog. It produces the same lesson, worksheet, and session-kit routes, adding reading-version links to session kits.

Every rendered Marp deck gets a reflowing HTML companion generated from the same slide bodies and corresponding notes. Covers without page numbers are included. Readers are not scaled screenshots and do not require JavaScript. The first keyboard target in the presentation opens the companion; the session kit exposes both formats directly.

## Ownership and limits

Assessment workers continue to own their isolated draft JSON, fixtures, and review files under the assessment-fanout contract. The design coordinator owns `_data/module_deck_visuals.yml`, the shared generator/helper, reader generation, CSS, and rendering. Do not hand-edit generated decks or session pages. Propose additional validated figures through this same visual manifest.

This is an accessibility improvement, not a conformance certification. It does not supply missing alt text or domain descriptions for every historical figure, establish assessment validity, or substitute for screen-reader, projector, physical-device, and real-user review. The expanded figure authoring scope in this pass is Modules 02-09; the reader format extends to all existing decks.

## Verification

Run `ruby scripts/generate_module_teaching_materials.rb`, `bash scripts/render_marp.sh --html`, the full existing Validate suite, and the added visual-design validators. Source checks cover examples/credits, fixture arithmetic, reader coverage, slide-count correspondence and preservation of the session catalog. Browser checks cover grid geometry, narrow screens, 200% reader text, native keyboard entry, description disclosure, and new visual slide bounds. Keep #188 paper list/map and wrong-button tests enabled. Do not waive a failed check.

Primary guidance: W3C complex images tutorial (`https://www.w3.org/WAI/tutorials/images/complex/`) and Reflow understanding (`https://www.w3.org/WAI/WCAG21/Understanding/reflow.html`). Image provenance: H01 release (`https://h01-release.storage.googleapis.com/landing.html`), Shapson-Coe et al. (2024), doi:10.1126/science.adk4858, CC BY 4.0, as recorded in the repository's image catalog.
