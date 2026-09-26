"""Export one closed, textured surface per figure for service upload.

Usage: python export_service.py [output-directory]
Uses the existing character generator; keeps face colors through Manifold's
boolean union using RGB vertex properties. No nearest-color approximation.
"""
from pathlib import Path
import argparse
import io
import json
import zipfile

import manifold3d
import numpy as np
from PIL import Image
import trimesh

import generate_color3d as source


def compact_parts(name):
    """Broaden small relief details and Axon's antenna before miniaturizing."""
    colors = getattr(source, name.upper())
    hair = getattr(source, f"{name}_hair")
    # Rounded outlines avoid needle-like emblem tips; deeper extrusion embeds
    # the relief farther into the torso instead of increasing its projection.
    if name == "cortex":
        badge = source.Polygon(source.CORTEX_STAR).buffer(0.35)
        mouth = source.CORTEX_MOUTH.buffer(0.15)
        badge_z = 34
    elif name == "axon":
        badge = source.Polygon(source.AXON_BOLT).buffer(0.35)
        mouth = source.AXON_MOUTH
        badge_z = 32
    elif name == "dendra":
        badge = source.unary_union([source.stroke_polygon(s, 1.8) for s in source.DENDRA_TWIG])
        mouth = source.DENDRA_MOUTH.buffer(0.325)
        badge_z = 36
    elif name == "syn":
        badge = source.Polygon(source.sparkle_points(r_out=6.0, r_in=1.6)).buffer(0.35)
        mouth = source.SYN_MOUTH
        badge_z = 34
    else:
        badge = source.GLIA_WRENCH_POLY.buffer(0.2)
        mouth = source.GLIA_MOUTH.buffer(0.275)
        badge_z = 33

    def emblem(parts, c):
        shape = source.emblem_from_shapely(badge, 2.2, c["accent"])
        shape.apply_translation([0, 8.5, badge_z])
        parts.append(shape)

    def extra(parts, c):
        if name == "axon":
            parts.append(source.capsule_between((0, 0, 61.5), (0, 0, 68), 1.65, c["suit_dark"]))
            parts.append(source.sphere((0, 0, 68.6), 1.7, c["accent"]))
        if name == "glia":
            source.glia_extra(parts, c)

    return source.build_character(
        colors, hair, emblem, source.mouth_shape(mouth, thickness=1.5),
        eye_z=55 if name == "syn" else 54.5,
        mouth_z=52.5 if name == "syn" else 51.5, extra_fn=extra)


def build_solid(name, height_mm=None, compact=False):
    # Original glow sphere reached 1.1 mm below the stand. Lift just that
    # sphere to the base plane so the figure can rest on its flat disc.
    original_glow = source.DEFAULT_TAIL_GLOW
    try:
        source.DEFAULT_TAIL_GLOW = (original_glow[0], original_glow[1], 3.3)
        parts = compact_parts(name) if compact else source.CHARACTERS_3D[name]()
    finally:
        source.DEFAULT_TAIL_GLOW = original_glow
    solids = []
    for part in parts:
        if not part.is_watertight or not part.is_volume:
            raise ValueError(f"{name}: invalid source solid")
        props = np.column_stack([
            part.vertices,
            np.tile(part.visual.vertex_colors[0, :3], (len(part.vertices), 1)),
        ]).astype(np.float32)
        solid = manifold3d.Manifold(manifold3d.Mesh(
            props, part.faces.astype(np.uint32)))
        if solid.status() != manifold3d.Error.NoError:
            raise ValueError(f"{name}: {solid.status()}")
        solids.append(solid)
    union = manifold3d.Manifold.batch_boolean(solids, manifold3d.OpType.Add)
    if union.status() != manifold3d.Error.NoError:
        raise ValueError(f"{name}: union failed: {union.status()}")
    raw = union.to_mesh()
    props, faces = np.asarray(raw.vert_properties), np.asarray(raw.tri_verts)
    face_rgb = props[faces, 3:6]
    if not np.allclose(face_rgb, face_rgb[:, :1], atol=1e-4):
        raise ValueError(f"{name}: unexpected color interpolation")
    colors = np.rint(face_rgb[:, 0]).astype(np.uint8)
    # Manifold duplicates property vertices at color seams. Weld only XYZ;
    # retain one RGB per triangle, preserving crisp boundaries.
    vertices, inverse = np.unique(props[:, :3], axis=0, return_inverse=True)
    mesh = trimesh.Trimesh(vertices, inverse[faces], process=False)
    mesh.visual.face_colors = np.column_stack([colors, np.full(len(colors), 255)])
    if height_mm is not None:
        mesh.apply_scale(height_mm / mesh.extents[2])
    check_geometry(mesh)
    return mesh, colors


def check_geometry(mesh):
    if not mesh.is_watertight or not mesh.is_volume or len(mesh.split()) != 1:
        raise ValueError("Export must be one watertight, consistently oriented solid")
    if mesh.bounds[0, 2] < -1e-5 or not np.isfinite(mesh.vertices).all():
        raise ValueError("Invalid coordinates or geometry below the base")
    if np.any(mesh.area_faces < 1e-12):
        raise ValueError("Degenerate triangle")


def texture_files(mesh, colors, stem):
    palette, color_index = np.unique(colors, axis=0, return_inverse=True)
    # One 4K RGB atlas and one material. UV triangles sit well inside each
    # swatch; they have nonzero area even though each region is a flat color.
    atlas = Image.new("RGB", (4096, 4096), "white")
    uv = []
    for i, color in enumerate(palette):
        x, y = (i % 4) * 1024, (i // 4) * 1024
        if y >= 4096:
            raise ValueError("Palette exceeds atlas capacity")
        atlas.paste(tuple(map(int, color)), (x, y, x + 1024, y + 1024))
        for dx, dy in [(384, 384), (640, 384), (512, 640)]:
            uv.append(((x + dx) / 4096, 1 - (y + dy) / 4096))
    lines = [f"# Units: millimeters; Z up; height {mesh.extents[2]:.4f} mm",
             f"mtllib {stem}.mtl", f"o {stem}"]
    lines.extend("v %.9g %.9g %.9g" % tuple(v) for v in mesh.vertices)
    lines.extend("vt %.9g %.9g" % p for p in uv)
    lines.append("usemtl neuronaut_palette")
    for face, idx in zip(mesh.faces, color_index):
        lines.append("f " + " ".join(f"{v+1}/{int(idx)*3+k+1}" for k, v in enumerate(face)))
    buf = io.BytesIO()
    atlas.save(buf, format="PNG")
    return {
        f"{stem}.obj": ("\n".join(lines) + "\n").encode(),
        f"{stem}.mtl": ("newmtl neuronaut_palette\nKa 1 1 1\nKd 1 1 1\n"
                        "Ks 0 0 0\nd 1\nillum 1\n"
                        f"map_Kd {stem}.png\n").encode(),
        f"{stem}.png": buf.getvalue(),
    }


def verify_archive(path, expected, expected_colors):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        if len(names) != 3 or any("/" in n for n in names):
            raise ValueError("Upload archive must contain only OBJ, MTL, PNG at root")
        obj = next(n for n in names if n.endswith(".obj"))
        resolver = trimesh.resolvers.ZipResolver({n: z.read(n) for n in names})
        loaded = trimesh.load(io.BytesIO(z.read(obj)), file_type="obj", resolver=resolver,
                              force="mesh", process=False)
        # Check imported texture samples, not just that PNG is present.
        samples = trimesh.visual.color.uv_to_color(
            loaded.visual.uv[loaded.faces].mean(axis=1), loaded.visual.material.image)
        expected_palette = np.unique(expected_colors, axis=0)
        if not np.array_equal(np.unique(samples[:, :3], axis=0), expected_palette):
            raise ValueError("Texture roundtrip changed palette")
        # This single-object, single-material importer preserves face order.
        # Allow decimal serialization error in positions; RGB must be exact.
        if (loaded.triangles.shape != expected.triangles.shape
                or not np.allclose(loaded.triangles, expected.triangles, atol=1e-6, rtol=0)
                or not np.array_equal(samples[:, :3], expected_colors)):
            raise ValueError("Texture roundtrip changed per-triangle colors")
        loaded.visual = trimesh.visual.ColorVisuals()
        loaded.merge_vertices()
        check_geometry(loaded)
        if not np.allclose(loaded.extents, expected.extents, atol=1e-4):
            raise ValueError("Roundtrip changed dimensions")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("out_dir", nargs="?", type=Path,
                        default=Path(__file__).parent / "service-exports")
    parser.add_argument("--height-mm", type=float, help="Uniform target height including the base")
    parser.add_argument("--compact", action="store_true", help="Broaden details for the 2-inch edition")
    args = parser.parse_args()
    if args.height_mm is not None and (not np.isfinite(args.height_mm) or args.height_mm <= 0):
        parser.error("height must be a positive finite number")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for name in source.CHARACTERS_3D:
        mesh, colors = build_solid(name, args.height_mm, args.compact)
        stem = f"neuronaut-{name}"
        upload = args.out_dir / f"{stem}-color-upload.zip"
        with zipfile.ZipFile(upload, "w", zipfile.ZIP_DEFLATED) as z:
            for filename, data in texture_files(mesh, colors, stem).items():
                z.writestr(filename, data)
        verify_archive(upload, mesh, colors)
        mesh.export(args.out_dir / f"{stem}-monochrome.stl")
        # glTF uses meters and Y-up; printable OBJ/STL use mm and Z-up.
        preview = mesh.copy()
        preview.apply_scale(0.001)
        preview.apply_transform(trimesh.transformations.rotation_matrix(-np.pi / 2, [1, 0, 0]))
        preview.export(args.out_dir / f"{stem}-preview.glb")
        result = dict(character=name, dimensions_mm=mesh.extents.round(3).tolist(),
                      compact_details=args.compact, target_height_mm=args.height_mm,
                      volume_cm3=round(mesh.volume / 1000, 3), triangles=len(mesh.faces),
                      colors=len(np.unique(colors, axis=0)), connected_solids=1,
                      watertight=True, texture_roundtrip=True,
                      upload_zip_bytes=upload.stat().st_size)
        results.append(result)
        print(json.dumps(result), flush=True)
    (args.out_dir / "validation.json").write_text(json.dumps(results, indent=2) + "\n")


if __name__ == "__main__":
    main()
