# Neuronauts — full-volume, full-color 3D figures

Genuinely sculpted 3D figures of the five Neuronauts (Captain Cortex, Axon,
Dendra, Syn, Glia) — not the flat relief standees in `../3d-print/`. Built
from primitives (spheres, capsules, a torus, a swept tube) matching each
character's palette and details from `neuronauts/index.html`: chest
emblem, hair, and the axon-cable tail with myelin beads and a glowing
synaptic bouton.

This is a separate, hand-modeled interpretation of the character art, not
a 3D extrusion of the flat SVG paths — it does not attempt byte-for-byte
geometric fidelity to `index.html` the way `../3d-print/` does. If the
site's character designs change meaningfully, this needs a manual re-look,
not just a re-run.

## Files

For each character (`cortex`, `axon`, `dendra`, `syn`, `glia`):

- `neuronaut3d-<name>-fullcolor.zip` — the print-ready deliverable: an
  OBJ + MTL pair (multi-material, one material per colored part — no
  texture maps needed since every part is a flat solid color) in its own
  zip, matching the format Shapeways documents for full-color uploads
  ([self-service upload guide](https://www.shapeways.com/blog/self-service-upload-3d-printing)).
- `neuronaut3d-all-five-fullcolor.zip` — all five characters' OBJ+MTL
  pairs together, each in its own subfolder (so their materials don't
  collide — see below); upload one character's subfolder at a time.
- `neuronaut3d-<name>.glb` — the same figure as glTF binary, for quick
  preview in any glTF viewer (e.g. https://gltf-viewer.donmccurdy.com) —
  not intended for print upload.
- `generate_color3d.py` — the generator script (Python + shapely +
  trimesh + manifold3d for the boolean-verification step below).

Each figure is about 70mm tall on a 30mm-diameter base, ~23-27 parts,
~2 petabytes less impressive than the connectome the rest of this site is
about but hopefully cuter.

## Why OBJ+MTL, not a single vertex-colored mesh

trimesh's default OBJ export for a vertex-colored mesh writes color as
extra columns on each vertex line (`v x y z r g b`) — a real but
less-universally-supported OBJ extension. Shapeways' documented format
expects proper per-face materials (`usemtl` + a companion `.mtl` with
`Kd` diffuse colors), so `generate_color3d.py` converts each part to a
named `SimpleMaterial` before export. One consequence worth knowing if
you extend this script: trimesh's OBJ exporter always names the material
file exactly `material.mtl`, regardless of the `.obj` filename — export
two characters into the same flat folder and the second silently
overwrites the first's materials. `export_full_color()` avoids this by
giving each character its own subfolder before zipping.

## Why each part is a separate solid, and how "connected" is verified

Each colored region (torso, arm, glove, hair puff, tail bead, ...) is its
own watertight mesh, deliberately overlapping its neighbors rather than
one boolean-unioned shell — booleaning parts of different colors together
loses which faces belonged to which color. That means print-worthiness
depends on every part actually sharing real volume with its neighbors, not
just looking close in a render.

`verify_connected()` checks this for real: for every pair of parts whose
bounding boxes are within 0.5mm of touching, it computes their actual
boolean intersection volume (via the `manifold3d` engine) and builds an
adjacency graph from pairs that share more than a trace of volume. The
generator refuses to consider a figure done unless every part is in that
graph and the whole graph is one connected component — i.e. the figure
prints as a single physically joined object, not a pile of parts that
happen to touch on screen. This caught a real bug during development: an
extra recentering translation on every capsule (legs, arms, tail-tube
supports) that silently left limbs floating with almost no material
actually overlapping their joints.

## Regenerating

```
python generate_color3d.py .
```

Rebuilds all five characters' `.obj`/`.mtl`/`.zip`/`.glb` in place and
prints each figure's part count, watertightness, and connectivity report.
A build only prints `[OK]` when every part is both watertight and
connected; investigate before printing if you see `[FAIL]`.

## Print settings

Full-color printing is a service process (binder jetting / photopolymer
full-color), not something you run on a desktop FDM printer. Upload the
`-fullcolor.zip` for the character you want directly to your print
service of choice. For Shapeways specifically: their self-service uploader
accepts a zip containing the OBJ and its MTL; pick a full-color material
(e.g. their full-color sandstone or full-color plastic options) once
you've uploaded and reviewed the color preview they generate. No
supports needed — the base is a flat disc already.
