# EN.585.781 — Frontiers in Neuroengineering: connectomics block

Lecture decks for modules 7–9, the three-module connectomics block (instructor: Will
Gray Roncal). These are presentation decks, not lecture *plans* — unlike
`technical-training/slides/`, which are build plans for an instructor assembling a
lecture.

| Source | Slides | Parts |
|---|---|---|
| `module07-introduction-to-connectomics.marp.md` | 58 | The case for mapping · Three scales · The field as it stands |
| `module08-tools-and-methods.marp.md` | 55 | Tissue to voxels · Storage and infrastructure · Reproducible pipelines |
| `module09-algorithms-and-applications.marp.md` | 57 | Segmentation, error and labor · Graph construction and nulls · Applications and NeuroAI |

Rendered HTML is committed under `course/decks/marp/out/en585781/`.

## How these are put together

**One discovery pipeline runs through all three decks** — question → specimen → image →
reconstruction → graph → claim. Each deck opens with the same diagram, marked to show
which columns it owns. Module 7 takes the two ends, Module 8 the middle, Module 9 the
conversion of measurements into claims.

**Eight progression streams** (scale; throughput and automation; segmentation quality;
modality integration; organism and lifespan coverage; structure → function; openness and
community; translation and people) are introduced in Module 7, tagged into the milestone
table, and revisited as a scorecard at the end of Module 9. They come from the
field-progression axes in the
[connectomics-survey](https://github.com/wrgr/connectomics-survey) evidence map.

**Macroscale methods are a contrast case, not a topic.** Diffusion MRI and X-ray
microtomography appear on one slide, as the example that different questions need
different instruments. Modules 10–12 cover human non-invasive methods properly.

**Sources.** Content is drawn from the `technical-training/` units (01–04, 08, 09) and
from the survey repository's verified milestone, dataset, and methods registries, so
citations are DOI-pinned and current through 2025.

## Rendering

Use the repository script, which registers the custom theme automatically:

```bash
npm install --no-save @marp-team/marp-cli   # if marp is not on PATH
./scripts/render_marp.sh                    # HTML — committed, and what CI checks
./scripts/render_marp.sh --pptx             # PowerPoint — gitignored, render on demand
```

PPTX is what to use for Google Slides: export, then **File → Import slides** in Google
Slides. The exports are not committed (see `.gitignore`).

**A caveat on PPTX.** The default export renders each slide as an image, so the text is
not editable in PowerPoint or Google Slides — treat those files as handouts, and treat
the `.marp.md` source as the thing you edit. Marp's `--pptx-editable` produces real text
boxes, but it converts through LibreOffice and needs a working `soffice` headless
conversion path; it fails in a bare container (`source file could not be loaded`) and is
marked experimental upstream. If you have LibreOffice locally, it is worth trying:

```bash
marp <deck>.marp.md --pptx --pptx-editable --allow-local-files \
  --theme-set course/decks/marp/en585781/theme/ -o <deck>.pptx
```

Editing a source without re-rendering fails `scripts/check_deck_freshness.rb` in CI. Run
the script; do not hand-edit `out/.render-manifest.json`.

## The theme

`theme/frontiers.css` is a Marp theme for a projected lecture hall: 1280×720, nothing
below about 14px, high contrast, and no reliance on colour alone to carry meaning.

Slide classes, set with `<!-- _class: ... -->`:

| Class | Use |
|---|---|
| `cover` | Deck title slide |
| `part` | Part divider |
| `claim` | A single centred claim, for a beat in the argument |
| `dense` | Tables with many rows |
| `tight` | Extra density where a slide still overruns; combines with the others |
| `refs` | Reference slides — many short citations |

Inline helpers: `.cols` (two columns), `.box` / `.box--warn` / `.box--good` (callouts),
`.ask` (a question to put to the room), `.src` (attribution).

**Do not re-wrap prose in the sources.** Marp Core sets markdown-it `breaks: true`, so a
newline inside a paragraph renders as a `<br>`. Prose paragraphs and list items are
therefore written as one long line each, and text reflows normally inside the slide and
inside `.cols` columns. Wrapping a paragraph at 80 or 90 columns -- which is what an
editor's fill command will do -- turns every wrap point into a hard line break and
sentences start breaking mid-phrase. Tables, code fences, headings, HTML, and the
speaker-note comments are unaffected either way.

**Every slide must fit inside 720px.** Overflow is silent in Marp — content is simply cut
off in the rendered HTML and in PPTX export. A checker is worth running after edits:
render to HTML, then measure `scrollHeight - clientHeight` on each
`svg[data-marpit-svg] section` in a headless browser. All 170 slides currently fit.

## Related material

- Proposed CDM revisions and an email draft: `course/en585781/`
- Source units: `technical-training/01`–`04`, `08`, `09`
- Instructor lecture plans for those units: `technical-training/slides/`

## Licence

**CC BY-SA 4.0** — see [`LICENSE`](LICENSE). Teach from these decks, adapt them, and
distribute the result; credit the original, say what you changed, and license your
version the same way. They contain no third-party figures, so adapting them raises no
image-licensing questions.

The learner- and instructor-facing pages are at
[`/teaching/lectures/`](../../../../teaching/lectures/).
