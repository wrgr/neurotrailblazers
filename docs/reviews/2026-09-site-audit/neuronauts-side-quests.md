# Site audit: Neuronauts and Side Quests

Area: `neuronauts/**`, `side-quests/**`. No `_data` file is used only by this area
(`_data/navigation.yml` and `_data/open_problems.yml` link here but are shared).
Branch `compass-workshops`, 2026-09-26. Nothing committed.

## Summary

| Type | Fixes |
|---|---|
| Accuracy | 27 |
| Polish | 8 |
| Voice | 10 |
| Missing | 1 |
| **Total** | **46** |

Files edited: `neuronauts/kids.md`, `neuronauts/index.html`, `side-quests/index.md`,
`side-quests/proofreading.md`, `side-quests/neuroanatomy-for-proofreaders.md`.

I did not change any 3D-print asset, README or generator. In `neuronauts/index.html`, the
character `<g id="nn-*">` SVG groups are unchanged. `neuronauts/3d-print/generate_stl.py`
hashes those groups and refuses to run if they drift. The print CSS (`nn-coverpage`) is
also unchanged. Every internal `relative_url` link in the area resolves to an existing
permalink, anchor or file.

Validators: `validate_frontmatter`, `validate_code_span_paths`, `validate_toggled_classes`
and `validate_paper_counts` all pass.

## Findings and fixes

| File | Issue | Type | Fix |
|---|---|---|---|
| side-quests/proofreading.md | NEURD cited as "Dorkenwald et al., *Nature Methods*, 2024, 10.1038/s41592-024-02515-z". That DOI is a 4Pi-SIM microscopy paper. NEURD is Celii et al., *Nature* 640, 487–496 (2025) | accuracy | Corrected the author, journal, year and DOI (10.1038/s41586-025-08660-5, checked on Crossref). Changed "the reference implementation" to "one published example; it automates the correction of merge errors", which is what the abstract says |
| side-quests/index.md | "Around 17,000 words of reference material". The five proofreading library pages total about 14,650 words, front matter included | accuracy | "About 14,000 words" |
| side-quests/neuroanatomy-for-proofreaders.md | "all six library entries". The quest sequences eight (6 neuroanatomy + 2 cell-types) | accuracy | "all eight" |
| neuronauts/kids.md | EyeWire "over 250,000 people from 145 countries … mapped dozens of new retinal ganglion cells". The 2014 paper had about 120,000 players from nearly 150 countries (EyeWire blog, May 2014). It reconstructed starburst amacrine cells, not new ganglion cells | accuracy | Rewrote the story around what Kim et al. 2014 actually found |
| neuronauts/kids.md | "reconstructed over 10 meters of retinal circuitry": unsourced | accuracy | Replaced with a verifiable fact: EyeWire II reports more than 25,000 complete neurons as of May 2026 (eyewire.ai) |
| neuronauts/kids.md | "including thousands of students and kids": unsourced | accuracy | Removed |
| neuronauts/kids.md | FlyWire "discovered" ring-shaped compass circuits. That circuit was known before FlyWire | accuracy | "Their map includes the fly's ring-shaped compass circuit" |
| neuronauts/kids.md | Fly "computes an escape route in just 5 milliseconds": unsourced number | accuracy | Removed the number |
| neuronauts/kids.md | Fly wiring "about 150 meters" | accuracy | 149 m, the figure in Dorkenwald et al. 2024 |
| neuronauts/kids.md | H01 "5,000 sheets … 1,000 times thinner than a hair". The paper reports 5,019 sections at 33.9 nm, about 2,000× thinner than a hair | accuracy | "about 5,000 … roughly 2,000 times thinner". Added that imaging took almost a year (326 days) |
| neuronauts/kids.md | "10,000 years doing it by hand": invented number | accuracy | "lifetimes" |
| neuronauts/kids.md | Worm: "In 1986, Sydney Brenner and his team spent over 15 years … with colored pens"; "first creature whose entire brain … completely mapped"; worm "navigate mazes" | accuracy | Credited White and Brenner's team with "more than ten years" of work published in 1986. Removed the pens and the mazes claims. Changed "completely mapped" to "whole nervous system mapped". Replaced "remember temperatures" with thermotaxis stated precisely |
| neuronauts/kids.md | "AI robots" (×4). The software is not a robot | accuracy | "computer programs" |
| neuronauts/kids.md | "over 86 billion", "100 trillion" stated as exact | accuracy | "about", "roughly" |
| neuronauts/kids.md | "25-minute lesson with a worksheet". The lesson is 25–40 minutes and has no worksheet | accuracy | "25–40 minute lesson" |
| neuronauts/kids.md | "open-access 2,000-paper collection". The collection is free to use, but not every paper in it is open access | accuracy | "free" |
| neuronauts/kids.md | Teacher card sent students to eyewire.org, now superseded by EyeWire II | polish | Pointed to connectome.quest, the Seung Lab hub for EyeWire II, FlyWire and other projects, with a note to check each project's age rules |
| neuronauts/kids.md | "colour" (×3) | polish | "color" |
| neuronauts/kids.md | "Let's Explore…", "Brain Mapping Revolution", "proving that anyone can be a real neuroscientist" | voice | Rewrote these headings and lines at the same kid register |
| neuronauts/index.html | "a new inhibitory wiring rule" cited to Ding et al. 2025. Ding reports a like-to-like rule among excitatory neurons (the inhibitory work is Schneider-Mizell et al., not cited here) | accuracy | "like-to-like wiring rule", in the Leg 7 notes and the future card |
| neuronauts/index.html | EyeWire "more than 200,000 players from 150 countries" (the kids page said 250,000/145) | accuracy | About 120,000 players from nearly 150 countries at the 2014 paper. Added the EyeWire blog to source 13 |
| neuronauts/index.html | "287 proofreader co-authors". 287 is the Princeton press figure for researchers. FlyWire names 292 contributors, including citizen scientists, on its website. The paper has 46 named authors | accuracy | "292 people credited by FlyWire". Added provenance to source 14 |
| neuronauts/index.html | Mouse brain "~1,000×" a cubic millimeter (×2), next to "about 500 mm³" | accuracy | "about 500 times" / "roughly 500-fold" |
| neuronauts/index.html | Human brain "~1,000× a mouse brain" (by volume it is about 2,400×) | accuracy | "roughly 1,000 times as many neurons" |
| neuronauts/index.html | Data ladder: mouse "~10⁷ neurons". A mouse has about 7×10⁷ | accuracy | "~10⁸" |
| neuronauts/index.html | "slicing a blueberry into 25,000 sheets". At 40 nm, 25,000 sheets is 1 mm; a blueberry would need about 250,000 | accuracy | "a poppy seed, about a millimeter across" |
| neuronauts/index.html | Hua et al. 2015 "pushed staining … to whole-brain-scale blocks". The paper reports blocks at least 1 mm in diameter | accuracy | Corrected |
| neuronauts/index.html | 2015: Kasthuri volume "about 0.0002% of a mouse brain", cited to lecture notes. This did not match either the 1,500 µm³ saturated sub-volume or the 660 GB image set | accuracy | Replaced with the verifiable 660 GB (neurodata.io), compared with the 2 PB per mm³ (division labeled as ours). Removed "Every leg … industrialized" |
| neuronauts/index.html | "eighteen days of human effort per neuron". The division uses project calendar time, not effort | accuracy | "project time"; "minutes" is now "about twenty minutes" |
| neuronauts/index.html | "one person with colored pencils": unverified | accuracy | "by hand on photographic prints" |
| neuronauts/index.html | BRAIN spend "about the cost of a single new aircraft carrier's air wing": unsourced comparison | accuracy | Removed. Dated the $3B/1,300 figure to 2023, the year of the cited NIH release |
| neuronauts/index.html | Cajal "ink drawings in 1900"; timeline "1900" (the work spans the late 1880s–1900s) | accuracy | "more than a century ago"; "Around 1900" |
| neuronauts/index.html | Axons "tenths of a micrometer … far below what a light microscope can separate" | accuracy | "as thin as a tenth of a micrometer, below what an ordinary light microscope can separate" |
| neuronauts/index.html | Cover caption "Maps available: none — yet". This contradicts MICrONS and H01 later on the same page | accuracy | "one cubic millimeter of mouse brain … about 200,000 cells, joined by about half a billion synapses" |
| neuronauts/index.html | Glossary: "a cubic millimeter of cortex holds about half a billion" synapses (true for mouse; H01 human is 150M) | accuracy | "of mouse cortex" |
| neuronauts/index.html | "A skill you can learn in an afternoon" (proofreading) | accuracy | "You can start learning it in an afternoon" |
| neuronauts/index.html | Junior Lab banner emoji not hidden from screen readers | polish | Wrapped in `aria-hidden` span |
| neuronauts/index.html | Junior Lab banner promised "mini-games" and "decoders" (there is one quiz and one decoder) | polish | Described what exists |
| neuronauts/index.html | "journey"; "the scorekeeper of how science gets done"; "something that used to be impossible has quietly become an industry"; "not decoration; it is the machine"; "thinking machine"; "It is destiny"; "Read that again"; "the field has receipts"; "That is not a footnote … That is the plot" | voice | Cut these or replaced them with plain statements |

Checked and left unchanged, because they are correct as written: Method of the Year 2025
(*Nature Methods*), the Helmstaedter commentary (22, 2490–2492), BRAIN CONNECTS (11 awards,
~$150M over 5 years, 40+ institutions), HI-MC partners (Google Research blog lists Harvard,
the Allen Institute, MIT, Cambridge, Princeton and JHU APL, with a 10–15 mm³ hippocampal
target), the 2023 cell census (32 million cells, 5,300+ types), and FlyWire (139,255 neurons,
~50M synapses, citizen-scientist co-authors). Also H01 (57,000 cells, 150M synapses, 1.4 PB,
~33.9 nm sections), GBD 2021 (3.4 billion people, 43%), the 2025 adaptive DBS approval and
speech BCI, Battelle's HGP estimate, the "free to read" labels on the kids page (Unpaywall),
and the SynapseWeb, connectome.quest and EyeWire II descriptions.

## Needs owner decision

1. **Which full-color print file the public pages link to.** `neuronauts/kids.md` and the
   expedition CTA both link to `neuronauts/3d-print-color/neuronaut3d-all-five-fullcolor.zip`.
   `service-exports/README.md` says that combined ZIP has subfolders, which go against Shapeways'
   upload limits, and that this may explain an earlier import failure. The folder README says
   to use the September 2026 per-figure ZIPs, and there is also a 2-inch bundle
   (`neuronauts-2inch-download-unpack-first.zip`). I left the links alone because changing the
   public download is your call. The options are the 2-inch bundle, the full-size per-figure
   ZIPs, or keeping the old ZIP with a caveat.
2. **Remaining rhetoric on the expedition page.** It still has a lot of em-dashes and
   storybook lines ("the fly inside is a library", "Suit up", "the greatest unexplored
   territory" in the cover art). They fit an outreach narrative, so I cut only the clearest
   tics. A full voice pass would be a rewrite.
3. **Source 35 (lecture notes) as evidence.** Several briefing claims and the data ladder
   cite the owner's unpublished lecture notes. That is labeled, but the ladder's
   order-of-magnitude rows are not checkable by a reader. Consider citing Berger's
   estimate directly if it is published.
4. **The kids quiz item "wires … around the entire Earth 4 times".** It is consistent with
   Marner et al. 2003 (about 150,000–180,000 km of myelinated fibers), but it has no source.
   Add a source or keep it as quiz flavor.

## Outside my area

- `_data/journal_papers.yml` (around line 21821) lists the NEURD paper's citation as
  "Schneider-Mizell et al. (2025)". The first author is Celii, B.
  (10.1038/s41586-025-08660-5). `content-library/connectomics/open-problems-undergrad.md`
  already cites it correctly.
- Untracked junk sits in the working tree: `neuronauts/.DS_Store`,
  `neuronauts/3d-print-color/.DS_Store` and `neuronauts/3d-print-color/__pycache__/`. Nothing
  tracked is affected, but `.gitignore` should cover `.DS_Store` and `__pycache__/` if it
  does not already.
