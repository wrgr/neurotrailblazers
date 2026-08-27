# Neuronauts — 3D-printable standees

Flat relief standees of the five Neuronaut characters (Captain Cortex, Axon,
Dendra, Syn, Glia), generated directly from the character coordinates used
in `neuronauts/index.html`. Each figure includes the neuron-styled details
from the page art: the trailing axon-cable tail with myelin beads and a
glowing synaptic bouton, plus a raised chest emblem, eyes, and mouth.

## Files

- `neuronaut-cortex.stl`, `neuronaut-axon.stl`, `neuronaut-dendra.stl`,
  `neuronaut-syn.stl`, `neuronaut-glia.stl` — one figure each, ~45 mm wide ×
  84–94 mm tall × 4.5 mm thick, each on its own integrated base plaque.
- `neuronaut-all-five.stl` — all five arranged side by side on one plate
  (264.8 × 93.6 × 4.5 mm), ready to slice as a single print job.
- `generate_stl.py` — the generator script (Python + shapely + trimesh).
  Re-run it after editing the character geometry in `neuronauts/index.html`
  to regenerate matching STLs; see the constants at the top (`SCALE`,
  `BASE_MM`, `DETAIL_MM`, `PLAQUE`) to adjust size or proportions.

## Design

Two-layer relief, extruded from the flat SVG artwork:

- **Base layer** (3.2 mm): the full body silhouette — legs, boots, torso,
  arms, gloves, helmet, head, hair, and the axon-cable tail — fused to a
  rounded rectangular base plaque so each figure stands with no supports.
- **Detail layer** (+1.3 mm on top): the chest emblem, eyes, and mouth, for
  a painted-relief look.

## Print settings

No supports or brim needed — every figure has a flat bottom and a wide,
stable base plaque. Suggested starting point for FDM:

- Layer height: 0.12–0.16 mm (captures the emblem and facial detail best)
- Infill: 15–20 % is plenty at this thickness
- Orientation: print flat, base plaque down, as-is
- Nozzle: 0.4 mm; hand-paint the raised details after printing for the
  full multi-color look from the page

For resin printers, print upright (rotate 90° so the base plaque is a
vertical wall) for the cleanest surface finish on the face.
