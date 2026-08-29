#!/usr/bin/env python3
"""Split the two categories the ratio analysis proved are mis-binned.

Evidence, not preference. Sorting each category by in-corpus degree showed:

  `other` (1138) is not a residual bucket. It holds White 1986 (in_degree 975, the single
  most-cited paper in the corpus and the founding connectome), "Highly Nonrandom Features of
  Synaptic Connectivity in Local Cortical Circuits" (835), "Dense inhibitory connectivity in
  neocortex" (143) and "Cortex: Statistics and Geometry of Neuronal Connectivity" (130).
  These are the corpus's heart, filed as leftovers -- classify_v2's own docstring predicted
  it ("papers predating the word connectome") but not the magnitude.

  `biological-application` (2280) is the broad-vocabulary fallback, and its top-cited members
  are not applications at all: "Functional specificity of local synaptic connections in
  neocortical networks" (526), "Network anatomy and in vivo physiology of visual cortical
  neurons" (389), "Functional organization of excitatory synaptic strength in primary visual
  cortex" (346). These MEASURE CONNECTIVITY; they are the same kind of paper as White 1986.

So one new primary category is warranted, drawn from both:

  circuit-structure -- papers that measure or map connectivity between identified neurons,
                       at any scale or modality. Distinct from `neuroanatomy` (morphology and
                       ultrastructure without a connectivity claim) and from `dataset`
                       (which RELEASES a reconstruction rather than analysing one).

and `biological-application` splits into what remains:

  behaviour  -- circuit-to-behaviour work (motor control, courtship, feeding, navigation)
  physiology -- synaptic/cellular physiology and coding without a connectivity map

`connectomics` remains deliberately absent as a category: it is the corpus, not a bin in it.
`circuit-structure` is not a synonym for it -- a segmentation paper is connectomics and
belongs in `pipeline`.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

S = Path(__file__).resolve().parent
r = json.loads((S / "classification_v2.json").read_text())
v = json.loads((S / "llm_verdicts.json").read_text())
m = json.loads((S / "universe_meta.json").read_text())

# measuring who connects to whom
STRUCT = re.compile(
    r"synaptic (connectivity|connection|partner|input|target|contact|circuit)"
    r"|connectivity (of|between|matrix|map|pattern|rule|motif|structure)"
    r"|wiring (diagram|pattern|rule|specificity|optimi)"
    r"|circuit (diagram|architecture|structure|reconstruction|motif)"
    r"|connectome|monosynaptic|polysynaptic|presynaptic partner|postsynaptic partner"
    r"|structure of the nervous system|neural connectivity|anatomical connectivity"
    r"|synapses (onto|between|made by)|innervat|projectome"
    r"|nonrandom (features|connectivity)|local (circuit|network) (connectivity|structure)"
    r"|inhibitory connectivity|excitatory (network|connections)|network anatomy", re.I)
# circuit -> behaviour
BEHAV = re.compile(
    r"behavio(u)?r|locomot|walking|flight|courtship|mating|feeding|foraging|grooming"
    r"|aggression|arousal|sleep|navigation|decision|learning and memory|memory formation"
    r"|choice|escape|orientation to|taste|olfactory behavio|motor (control|program|initiation)"
    r"|action selection", re.I)

out = {}
n_struct = n_behav = n_phys = 0
for d, rec in r.items():
    if d in v["out"]:
        out[d] = rec
        continue
    cls = rec["classification"]
    x = m.get(d) or {}
    t, a = x.get("title") or "", (x.get("abstract") or "")[:900]
    txt = f"{t} {t} {a}"
    new = dict(rec)
    if cls in ("other", "biological-application", "neuroanatomy"):
        if STRUCT.search(txt):
            new["classification"] = "circuit-structure"
            new["subclassification"] = None
            n_struct += 1
        elif cls == "biological-application":
            if BEHAV.search(txt):
                new["classification"] = "behaviour"; n_behav += 1
            else:
                new["classification"] = "physiology"; n_phys += 1
            new["subclassification"] = None
    if new["classification"] != rec["classification"]:
        sec = list(new.get("secondary_classifications") or [])
        if rec["classification"] not in sec and rec["classification"] != "other":
            sec.append(rec["classification"])
        new["secondary_classifications"] = sec[:3]
    out[d] = new

(S / "classification_v3.json").write_text(json.dumps(out, ensure_ascii=False))
surv = [d for d in out if d not in v["out"]]
print(f"reassigned -> circuit-structure {n_struct}, behaviour {n_behav}, physiology {n_phys}\n",
      file=sys.stderr)
for k, n in Counter(out[d]["classification"] for d in surv).most_common():
    print(f"  {k:22s} {n:5d}", file=sys.stderr)
