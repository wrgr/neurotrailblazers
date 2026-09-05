# NeuroTrailblazers brand guide

*Version 1, September 2026. Files referenced here live in `assets/brand/` and
`course/decks/marp/theme/`. The decisions below replace the three palettes currently in
use on the site (see the migration table at the end).*

---

## 1. What the brand has to do

NeuroTrailblazers is a workforce-development program: it trains the people who will build
and use synapse-resolution brain maps, and it publishes the training openly under
NIH BRAIN CONNECTS. The identity therefore has to read as **serious, open and
teachable**: credible next to a Nature Methods figure, warm enough for a first-generation
undergraduate, and clean enough to print on a worksheet or project in a lecture hall.

The existing banner already says this well: silhouetted people walking along dendrites,
in a restrained teal monochrome, under a condensed capital wordmark. Everything below is
derived from that image so the site, decks, worksheets and social cards look like one
thing. What it retires: the neural-blue / cerebral-purple / axon-cyan palette in
`_config.yml`, the purple-and-orange gradient favicon, and the emoji icon set.

## 2. Name, line, voice

**Name.** *NeuroTrailblazers*, one word, capital N and T, in running text. The all-caps
wordmark is for the logo only. Never "Neuro Trailblazers", "NeuroTrailBlazers" or "NTB"
in public copy; "NT" is acceptable as a file prefix.

**Line.** Recommended: **"Mapping connections. Making connections."**
The double meaning is exact: the field maps synaptic connections; the program makes
connections between people and research. Four words, and it says both halves of the
mission. Keep "Training the people who map the brain" as the one-sentence description
beneath it where a longer line is needed. The current line, "Illuminating Pathways for
Trailblazing Neuroscience Research(ers)", should be retired: the parenthetical is a hedge,
and the site currently carries eleven different one-line descriptions of itself.

Alternatives considered:

| Line | Why not first |
|---|---|
| Activating connections, in brains and between people. | Closest to the brief; "activating" is what neurons do, so it reads as jargon to outsiders |
| Every connection counts. | Catchy, but generic enough to belong to a bank |
| Connecting people to the connectome. | True, but the object is the map rather than the people |
| Where connections form. | Quiet; works as a section eyebrow, not a tagline |

Positioning sentence for About and funders, already on the site: *"IC3 and APEX organize
and expose the science. NeuroTrailblazers organizes the learning."*

**Voice.** The content standard in `docs/CONTENT_REVIEW.md` is also the brand voice:

- Numbers over adjectives. "About 2 PB per mm³" beats "very large".
- State what a thing does not show. Boundaries are a feature, not a disclaimer.
- Plain verbs, short sentences, no hype. No "audacious", "revolutionary", "unlock".
- Address the reader as a colleague who has not done this yet, never as a novice.
- Headings state the claim, not the topic.

## 3. Colour

Derived from the banner. Contrast ratios are WCAG 2.1 against the surface named.

| Token | Hex | Role | Contrast |
|---|---|---|---|
| `--nt-ink` Trail Ink | `#10303F` | Text, dark surfaces, the wordmark | 13.9:1 on white |
| `--nt-ink-2` | `#1E4656` | Secondary headings on light, panels on dark | 10.1:1 on white |
| `--nt-teal` Trail Teal | `#0F6B73` | Primary action, links, active state, big numbers | 6.2:1 on white, 5.5:1 on mist |
| `--nt-teal-deep` | `#0B5259` | Hover and pressed | 8.9:1 on white |
| `--nt-teal-light` | `#BFE3E4` | Tints, chips, table header on dark | 10.1:1 for ink text |
| `--nt-mist` | `#E6F2F3` | Pale panel and quiet-slide background (the banner sky) | 12.1:1 for ink text |
| `--nt-amber` Signal Amber | `#E8820C` | **One accent per surface, fills only.** The postsynaptic density on the mark. | 2.8:1 on white: **not for text on light** |
| `--nt-amber-deep` | `#B4600A` | Amber when it must be text on light | 4.6:1 on white |
| `--nt-amber-light` | `#FDECD6` | Warning callout tint | — |
| `--nt-paper` / `--nt-surface` | `#FFFFFF` / `#F5F8F8` | Page and card backgrounds | — |
| `--nt-border` | `#D8E1E3` | Rules and table lines | — |
| `--nt-muted` | `#55697A` | Captions, sources, secondary text | 5.7:1 on white |
| `--nt-good` / `--nt-warn` | `#1C6B43` / `#A8410A` | Semantic only | 6.5:1 / 6.1:1 on white |

**Proportions.** Ink and the neutrals carry 70% of any surface, teal 20%, amber under 5%
and usually a single element: the postsynaptic density on the mark, a pill, one callout. If
two things on a page are amber, one of them is wrong.

**Dark surfaces** (title slides, section dividers, footer, social card) are ink with mist
text and teal-light for secondary text. Amber is allowed as text on ink (5.0:1).

**Layer colours** for the site map (core / path / delivery / quest) are re-tokenised as
`--nt-layer-*` in `assets/brand/brand-tokens.css`, replacing the purple used for
"delivery" with ink-2 so the map stays inside the palette.

## 4. Type

| Role | Face | Weights | Fallback |
|---|---|---|---|
| Display: wordmark, page and slide H1, big numbers | **Barlow Condensed** (OFL, Google Fonts) | 600, 700 | Arial Narrow, Roboto Condensed |
| Body and UI | **Source Sans 3** (already in use) | 400, 600, 700 | Segoe UI, Helvetica |
| Code, IDs, coordinates | **IBM Plex Mono** (already in use) | 400, 500 | Menlo, Consolas |

Barlow Condensed matches the letterforms of the banner wordmark and gives headings a
distinct silhouette without a second body face. Use it at 28 px and above only; below
that, Source Sans 3 semibold. Drop Plus Jakarta Sans from the font request: it is loaded
on every page and used nowhere.

In PowerPoint, where installed fonts cannot be assumed, the template uses **Arial Bold**
for display and **Calibri** for body. Install Barlow Condensed and Source Sans 3 and swap
them in the slide master when the audience will see the deck on your machine.

Sizes: body 17–18 px on the web, 22–24 px on slides; nothing below 15 px on a slide.
Line height 1.4–1.65. Headings tight (1.02–1.1), letter-spacing normal; the wordmark
alone is tracked +1%.

## 5. The mark

**Concept.** A synapse, drawn the way it appears in an electron micrograph. A spiny
dendrite runs along the bottom of the tile; an axon arrives from the top-left and swells
into a bouton filled with vesicles; across a narrow cleft, the spine head it contacts
carries a postsynaptic density. Every element is in the cell colour except the
postsynaptic density, which is amber: the one place on the mark where the connection is
actually made. Anyone who has looked at EM reads it at once; anyone who has not still sees
a path arriving at a bright point of contact. At 16 px it reads as a terminal meeting a
branch.

Colour logic, in the field's own terms: neurites and bouton are cytoplasm (cell colour),
vesicles are the tile colour, the PSD is the accent. Do not colour the bouton amber; that
was tried and it makes the terminal, not the contact, the subject.

Three earlier directions were retired: a branching path with a node (generic), a
convergent wiring diagram (correct about networks, but it looked like every other network
icon), and a set of alternatives (serial sections, segmented mosaic, connectivity matrix,
N monogram, imaged volume) that are documented in the working files for reference.

| File | Use |
|---|---|
| `nt-mark.svg` | Primary: mist cell, ink vesicles, amber PSD on ink tile. Favicon, app icon, avatars, slide footer |
| `nt-mark-reversed.svg` | Ink cell on mist tile, for dark backgrounds |
| `nt-mark-mono.svg` | One colour for print: paper cell, ink vesicles and PSD |
| `nt-wordmark.svg` / `-reversed.svg` | Outlined Barlow Condensed Bold with kerning, no font dependency |
| `nt-lockup-horizontal.svg` / `-reversed.svg` | Mark + wordmark, for headers and title slides |
| `nt-lockup-stacked.svg` / `-reversed.svg` | Square-ish contexts: social avatars, posters |
| `nt-favicon.svg` | Same as the mark; add a 32 px PNG for old browsers |
| `nt-social-card.svg` | 1200 × 630 Open Graph image, carries the motif and the tagline |
| `nt-motif-synapse.svg` | 1280 × 720 background scene for title and closing slides |

**The motif.** The larger scene behind title slides, closing slides and the social card
extends the mark: one dendrite with four spines crossing the frame, two axons arriving,
teal boutons, and a single amber postsynaptic density on the spine that is being
contacted. It is a ground, not an illustration: keep it at the shipped opacity and put
text over the quiet regions.

**Rules.**

- Clear space around any lockup is the diameter of the bouton on all sides.
- Minimum size: mark 16 px; horizontal lockup 120 px wide; stacked lockup 72 px wide.
- The mark always sits on its tile. Do not place the bare neurites on a photograph.
- Do not recolour the postsynaptic density. Amber is the one place amber is guaranteed to appear.
- Do not rotate, outline, add a drop shadow, or set the wordmark in any other face.
- The banner illustration (`assets/images/neurotrailblazers-banner.jpg`) stays as the
  hero image; it is not a logo and should not appear on every page's header.

## 6. Imagery and iconography

**Photography and illustration.** The banner sets the direction: silhouettes at human
scale against neural structure, teal monochrome, one warm accent at most. Electron
micrographs are shown as they are, greyscale, with a scale bar; segmentation overlays use
teal, ink-2 and amber before any other hue. No stock brains, no glowing networks, no
purple-to-orange gradients.

**Icons.** Replace emoji with a single line-icon set (Lucide or Phosphor, 1.75 px stroke,
24 px grid) in ink or teal. Pathway cards on the home page get an icon in a mist circle;
headings get none. Emoji that remain must be `aria-hidden="true"`.

**Module art.** The 25 generated SVG banners in `assets/images/modules/` should be
regenerated from the palette above (`scripts/generate_module_art.rb` takes the colours
as constants).

## 7. Components

Shared across web, decks and worksheets:

- **Callouts.** Note (mist), Good (green tint), Warn (amber tint), Key (ink with mist
  text). 10 px radius, no left border stripe, bold lead-in word. One per slide, two per
  web section.
- **Pills.** Barlow Condensed 600, uppercase, +8% tracking, teal-light background with
  teal-deep text; amber background with ink text for the single highlighted label.
- **Source line.** Every figure and every number carries one: muted, 15 px, pinned to the
  bottom of the slide or the end of the figure caption. "Source: Author et al. (year),
  DOI. Licence if not CC BY."
- **Tables.** Header row mist, 1 px border rows, zebra on surface. Rubrics are always
  three rows: Not yet / Proficient / Strong.
- **Radius** 10 px; large cards 18 px. **Shadows** ink at 8% and 12%.

## 8. Slides

Two implementations of the same system, both shipped:

**Marp** (the repository's native deck format).
`course/decks/marp/theme/neurotrailblazers.css` registers automatically through
`scripts/render_marp.sh`. Fonts are embedded as data URIs so decks render identically
offline and in PPTX export. Set `theme: neurotrailblazers` in the front matter.
`course/decks/marp/neurotrailblazers-template.marp.md` demonstrates every slide class
(`title`, `section`, content, `mist`, `figure`, `stat`, `dark`, `closing`) and the
`.cols`, `.note/.warn/.good/.key`, `.pill` and `.source` blocks; its render is at
`course/decks/marp/out/neurotrailblazers-template.html`.

**PowerPoint.** `assets/brand/NeuroTrailblazers-slide-template.pptx`: twelve slides,
one per type, 16:9, with usage notes in the speaker notes of every slide and five slide
masters (light, mist, dark, title, closing). Duplicate a slide of the right type rather
than restyling a blank one.

Deck rules, in both:

1. Heading states the claim. One idea per slide.
2. Four bullets is the ceiling; split rather than shrink.
3. Every figure and number slide has a source line.
4. Dark slides for the opener, section dividers, the one turn in the argument, and the
   close. Everything else on paper or mist.
5. Amber once per slide, as a fill.
6. Speaker notes carry the third level of detail; the slide does not.
7. Close with the licence line.

## 9. Web migration

`assets/brand/brand-tokens.css` is the single source of truth. To move the site onto it:

| Legacy | Replace with |
|---|---|
| `--neural-blue #2563eb` (31 uses) | `--nt-teal` |
| `--cerebral-purple #7c3aed` (7) and `--layer-delivery` | `--nt-ink-2` |
| `--axon-cyan #06b6d4` (12) | `--nt-teal-light` for fills, `--nt-teal` for strokes |
| `--brain-gray #f3f4f6` (16) | `--nt-surface` |
| `--synapse-black #1f2937` (4), `--ink #0d1117` | `--nt-ink` |
| `--teal #006d6b`, `--teal-mid`, `--teal-lt` | `--nt-teal`, `--nt-teal-deep`, `--nt-teal-light` |
| `--amber`, `--amber-lt` | `--nt-amber`, `--nt-amber-light` |
| Hardcoded Tailwind hex (`#1e40af`, `#5b21b6`, `#dbeafe`, `#ede9fe`, `#eff6ff`, `#f3e8ff`, `#f97316`…) | The nearest `--nt-*` token; there are about 60 |
| `colors:` block in `_config.yml` | Delete; nothing should read colours from config |
| `frontiers.css` deck theme | Retire, or re-point its variables at the tokens above |
| Plus Jakarta Sans in the font request | Delete; add Barlow Condensed 600/700 |

Do the migration in one pass and delete the legacy `:root` blocks in the same commit, so
there is never a period with two live systems. Verify with a grep for `#2563eb`,
`#7c3aed` and `#06b6d4` returning nothing outside `docs/`.

## 10. File inventory

```
assets/brand/
  brand-tokens.css                      CSS custom properties (colour, type, radius, shadow)
  nt-mark.svg  nt-mark-reversed.svg  nt-mark-mono.svg  nt-favicon.svg
  nt-wordmark.svg  nt-wordmark-reversed.svg
  nt-lockup-horizontal.svg  nt-lockup-horizontal-reversed.svg
  nt-lockup-stacked.svg  nt-lockup-stacked-reversed.svg
  nt-social-card.svg  nt-motif-synapse.svg
  NeuroTrailblazers-slide-template.pptx
course/decks/marp/theme/neurotrailblazers.css
course/decks/marp/neurotrailblazers-template.marp.md
course/decks/marp/out/neurotrailblazers-template.html
```
