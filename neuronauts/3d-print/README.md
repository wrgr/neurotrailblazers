# Neuronauts — 3D-printable standees

Flat relief standees of the five Neuronaut characters (Captain Cortex, Axon,
Dendra, Syn, Glia), generated directly from the character coordinates used
in `neuronauts/index.html`. Each figure includes the neuron-styled details
from the page art: the trailing axon-cable tail with myelin beads and a
glowing synaptic bouton, plus a raised chest emblem, eyes, and mouth.

## Files

- `neuronaut-cortex.stl`, `neuronaut-axon.stl`, `neuronaut-dendra.stl`,
  `neuronaut-syn.stl`, `neuronaut-glia.stl` — one figure panel each, ~38 mm
  wide × 79–88 mm tall × 4.5 mm thick, each with a small tab below the
  boots.
- `neuronaut-stand-base.stl` — a shared base block (46 × 26 × 12 mm) with a
  slot cut through it sized to any figure's tab. Print one per figure you
  want displayed at once.
- `neuronaut-all-five.stl` — all five figure panels plus one stand base,
  arranged on one plate (298 × 101 × 12 mm), ready to slice as a single
  print job.
- `generate_stl.py` — the generator script (Python + shapely + trimesh).
  See [Keeping this in sync](#keeping-this-in-sync-with-indexhtml) before
  editing character geometry in `neuronauts/index.html`.

## Assembly

A figure panel is only 4.5 mm thick — balanced on that edge it's not
stable on its own. Press each figure's tab into a stand base's slot (a
firm push fit; add a dot of glue if you want it permanent) to display it
upright. Both pieces print flat with no supports.

## Design

**Figure panel** — a two-layer relief, extruded from the flat SVG artwork:

- **Base layer** (3.2 mm): the full body silhouette — legs, boots, torso,
  arms, gloves, helmet, head, hair, and the axon-cable tail — fused to a
  rectangular tab below the boots.
- **Detail layer** (+1.3 mm on top): the chest emblem, eyes, and mouth, for
  a painted-relief look.

**Stand base** — a solid block with a through-slot boolean-cut to the tab's
size plus clearance, so any figure snaps into any base.

## Print settings

No supports or brim needed for either part — both have a flat bottom.
Suggested starting point for FDM:

- Layer height: 0.12–0.16 mm (captures the emblem and facial detail best)
- Infill: 15–20 % is plenty for the figure panels; 15% is fine for the
  base too since it's mostly a friction-fit shell
- Orientation: print both parts flat, as-is — figure panel face down or
  face up (doesn't matter), base block on its largest face
- Nozzle: 0.4 mm; hand-paint the raised details after printing for the
  full multi-color look from the page

For resin printers, either part can also print flat with no supports;
there's no need to print the figure panel on edge.

## Keeping this in sync with index.html

`generate_stl.py` reconstructs each character's geometry by hand in
Python — it does not parse `neuronauts/index.html`, so editing a
character's SVG there does not automatically change the generated STLs.
To catch that drift instead of silently generating stale models, the
script hashes each character's `<g id="nn-*">` markup in `index.html` and
compares it against `EXPECTED_SVG_HASHES` at the top of the file; if
they don't match, it refuses to run.

After intentionally changing a character's SVG in `index.html`:

1. Update the matching shape function in `generate_stl.py` (e.g.
   `cortex_shapes()`) to reflect the new geometry.
2. Run `python generate_stl.py --freeze-hashes` and paste the printed
   hashes into `EXPECTED_SVG_HASHES`.
3. Re-run `python generate_stl.py .` to regenerate the STLs.
