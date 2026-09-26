# Neuronauts: revised service upload files

Prepared September 25, 2026. Start with **Captain Cortex**, 65.3 mm tall.

## Upload the correct file

Each `neuronaut-NAME-color-upload.zip` is a complete, individual full-color
upload. Keep that ZIP intact: it contains exactly one OBJ, its MTL, and one
4096 × 4096 RGB PNG texture, all at the archive root. Upload each figure
separately. Set units to **millimeters** and scale to **100%**.

Heights: Cortex 65.3 mm; Axon 70.3 mm; Dendra 63.9 mm; Syn 67.0 mm;
Glia 64.9 mm. All are 47.2 mm wide, 30 mm deep, with a 30 mm base.

The `-monochrome.stl` files are optional unpainted resin prototype files;
STL does not carry these colors. The `-preview.glb` files are for viewing
and use meters as required by glTF. Use the color ZIP for full-color ordering.

## Recommended first quote

Try [JLC3DP's quote page](https://jlc3dp.com/3d-printing-quote), selecting
**Full-Color Resin / WJP**, quantity one, using the Cortex color ZIP.
Its [current ordering instructions](https://jlc3dp.com/help/article/instructions-for-placing-full-color-printing-orders)
explicitly accept OBJ + MTL + PNG in ZIP archives and require engineering
review. Its [material page](https://jlc3dp.com/help/article/full-color-resin)
advertises pricing **from $5**, which is a starting price, not a quote for
these models. Check the delivered total including shipping and applicable
taxes/duties. No model-specific quote or upload acceptance has been obtained.

Use [Craftcloud](https://craftcloud3d.com/) for a competing quote; its
[material guide](https://craftcloud3d.com/en/material-guide) lists
High Definition Full Color as well as standard and high-detail resin.
Confirm the actual offer includes the model's full surface colors.
For an unpainted shape prototype, quote the monochrome STL in standard resin.

Have the service check the antenna, thin emblem tips, facial details, and
tail during engineering review. These exports pass geometry checks, but
have not undergone a complete minimum-feature-thickness analysis or physical
print test. Do not reduce the scale before review. These are solid figures:
JLC3DP's [WJP guidelines](https://jlc3dp.com/help/article/wjp-products-design-guidelines)
say hollow designs are unsupported. The service chooses orientation and
support processing; a flat base does not eliminate overhang supports.

## What was corrected

- Unioned the overlapping colored primitives into one watertight solid per
  figure, removing internal intersecting surfaces while retaining the exact
  RGB of every surviving triangle.
- Replaced multiple separate materials/textures with one material and one
  atlas, with valid, nonzero-area UV triangles inside flat-color swatches.
- Lifted the tail's glow sphere by 1.1 mm so it no longer protrudes below
  the base. Other character geometry and original sizes are retained.
- Built one root-level upload ZIP per figure, with no unrelated files.

The old `neuronaut3d-all-five-fullcolor.zip` contains subfolders, contrary
to [Shapeways' current upload limitations](https://support.shapeways.com/hc/en-nl/articles/17001579812252-What-are-the-upload-limitations).
That is a possible explanation for the earlier import failure if the
combined ZIP was used. The original error has not been reproduced.

## Validation and regeneration

`validation.json` records dimensions, volume, triangle count, and checks
for each model. All five exports were re-imported: each is one watertight,
consistently oriented solid, with every triangle's geometry and sampled
texture color checked against the union result. This is local validation,
not service approval. `crew-preview.png` renders the actual upload ZIPs.

From the parent directory, in a Python environment with
`requirements-service.txt` installed:

```sh
python export_service.py
python render_service_preview.py
```
