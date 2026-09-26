# Neuronauts — 2-inch edition

All five figures are **50.8 mm (2 inches) tall including their base**.
They are approximately 34–38 mm wide, on 22–24 mm diameter bases.
Original larger models are preserved in the neighboring `service-exports` folder.

## Full-color uploads

Upload each ZIP intact, separately. Set units to **millimeters**, scale to
**100%**, and verify **50.8 mm height**. These packages contain only one OBJ,
one MTL, and one 4K PNG texture at the root, with a single closed surface.

- [Captain Cortex](neuronaut-cortex-color-upload.zip)
- [Axon](neuronaut-axon-color-upload.zip)
- [Dendra](neuronaut-dendra-color-upload.zip)
- [Syn](neuronaut-syn-color-upload.zip)
- [Glia](neuronaut-glia-color-upload.zip)

For JLC3DP, select **Full-Color Resin / WJP**. Its
[ordering instructions](https://jlc3dp.com/help/article/instructions-for-placing-full-color-printing-orders)
accept this file combination and require engineering review.

## Plain resin / paint-your-own uploads

Use these STL files for an unpainted resin quote. They have identical geometry
to the color figures but no color information. Again, use mm and 100% scale.

- [Captain Cortex](neuronaut-cortex-monochrome.stl)
- [Axon](neuronaut-axon-monochrome.stl)
- [Dendra](neuronaut-dendra-monochrome.stl)
- [Syn](neuronaut-syn-monochrome.stl)
- [Glia](neuronaut-glia-monochrome.stl)

The `-preview.glb` files are for viewing, not the recommended service upload.
They use meters and Y-up as expected by glTF viewers.

If you downloaded `neuronauts-2inch-download-unpack-first.zip`, unpack it
first, then upload the individual `-color-upload.zip` files inside it.
The outer download bundle is not a print-service upload.

## Changes for this size

- Broadened Cortex, Dendra, and Glia's smiles and embedded all mouths deeper.
- Rounded pointed emblems, broadened Dendra's branches and Glia's emblem,
  and increased the relief depth into the torso.
- Increased Axon's antenna shaft diameter by 50% before scaling; its final
  nominal diameter is about 2.4 mm.
- Retained the corrected flat base and unified solid geometry.
- Scaled each figure individually to exactly 50.8 mm overall height.

All five were re-imported from the final ZIP files and verified for one
watertight, consistently oriented solid, exact per-triangle texture colors,
and dimensions. The STLs and GLB sizes were also checked. Numerical results
are in `validation.json`; `crew-preview.png` renders the actual ZIP contents.

This is local file validation, not a completed physical print test or vendor
approval. The service still needs to review small features, joints, and
support removal. No complete minimum-wall-thickness certification is claimed.
Do not shrink further without another design review. No order has been placed.

## Regenerate

From the parent `3d-print-color` directory, using `requirements-service.txt`:

```sh
python export_service.py service-exports-2inch --height-mm 50.8 --compact
python render_service_preview.py service-exports-2inch --title 'Neuronauts · 2-inch edition'
```
