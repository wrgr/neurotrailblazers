---
layout: page
title: "EM Figure Library"
permalink: /content-library/em-figures/
description: >
  Every electron-microscopy figure on this site in one place, with its caption,
  attribution, and a ready-to-paste Marp slide line — rendered from the public
  H01 human cortex volume and free to reuse under CC BY 4.0.
topics:
  - electron microscopy
  - teaching resources
difficulty: "Any"
tags:
  - imaging:electron-microscopy
  - methodology:reproducibility
use_layout_hero: false
content_type: core
---

# EM Figure Library

Every electron micrograph on this site, in one place, so you can pull them into
a deck without hunting through content pages.

All of them are rendered from the **public H01 human cortex volume** — not
copied from a publication, and not illustrations. Where a figure names a
structure, that structure was located by querying H01's own label layers, so
"astrocytic process" means the dataset labels it an astrocyte.

<div class="callout-box callout-note">
  <p><strong>Reuse:</strong> the H01 release states that "all released datasets
  are licensed under a
  <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">Creative Commons Attribution 4.0 License</a>."
  These renderings inherit that. Attribute as: <em>H01 dataset, Lichtman
  Laboratory (Harvard University) and Connectomics at Google; Shapson-Coe et
  al., </em>Science<em> 384, eadk4858 (2024)</em>.</p>
  <p><strong>Regenerate:</strong> <code>scripts/render_h01_figures.py</code> and
  <code>scripts/render_em_figures.py</code> rebuild every figure here from
  scratch. Both work on any Neuroglancer <code>precomputed</code> dataset, so
  the same code points at MICrONS or FlyWire.</p>
</div>

{% for group in site.data.em_figures.groups %}
## {{ group.title }}

{{ group.note }}

{% for f in group.figures %}
### {{ f.title }}

{% include figure.html
   src=f.src
   alt=f.title
   caption=f.detail
   credit="H01 human cortex, Lichtman Lab (Harvard) &amp; Connectomics at Google, CC BY 4.0. Shapson-Coe et al., <em>Science</em> 384, eadk4858 (2024)." %}

<details class="jc-card-details">
  <summary>Slide line and file path</summary>
  <div class="jc-details-body">
    <p><strong>Marp:</strong></p>
    <pre class="jc-citation-bib"><code>{{ f.marp }}</code></pre>
    <p><strong>File:</strong> <code>{{ f.src }}</code> &middot;
       <a href="{{ f.src | relative_url }}" target="_blank" rel="noopener">open full size</a></p>
  </div>
</details>

{% endfor %}
{% endfor %}

---

## Using these in a deck

The lesson decks under `course/decks/marp/` already carry a selection of these.
To add another, paste its Marp line above into the deck source and re-render:

```bash
npm install --no-save @marp-team/marp-cli   # if you don't have it
./scripts/render_marp.sh
```

The render step is not optional: `scripts/check_deck_freshness.rb` records a
hash of every deck source at render time and fails CI if a source was edited
without re-rendering. That gate exists because 29 of 35 decks had silently gone
stale before it did.

## What these figures deliberately do not show

Some things the pages describe are simply below this volume's resolution, and a
figure claiming otherwise would teach a measurement error. At 4 nm per pixel
with 33 nm sections:

| Structure | Size | At 4 nm | Showable? |
|---|---|---|---|
| Synaptic vesicle | ~40 nm | 10 px | Yes |
| Type I PSD thickness | 30–50 nm | 8–12 px | Yes, but subtle |
| Spine neck | 100–200 nm | 25–50 px | Yes |
| Polyribosome rosette | ~100 nm cluster | ~25 px | Yes, as a cluster |
| Myelin period | 12 nm | 3 px | **No** — lamellae cannot be counted |
| Synaptic cleft width | 12 vs 20 nm | 3 vs 5 px | **No** — at the noise floor |
| AIS dense undercoat | 5–10 nm | 1–2.5 px | **No** |
| Gap junction gap | 2–3 nm | <1 px | **No** |

Anything needing a whole-cell shape — apical dendrites, interneuron
morphologies, branching angles — needs a 3D mesh view rather than a single
plane, and is not in this set.
