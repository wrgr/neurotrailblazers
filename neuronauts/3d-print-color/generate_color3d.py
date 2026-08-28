"""
Prototype v2: full-volume, full-color 3D Neuronaut figures (not the flat
relief standee) for services like Shapeways full-color printing.
"""
import numpy as np
import trimesh
from shapely.geometry import Polygon, LineString, Point
from shapely.ops import unary_union
import trimesh.creation as tc


def rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return [int(hex_color[i:i + 2], 16) for i in (0, 2, 4)] + [255]


def colored(mesh, hexcolor):
    mesh.visual = trimesh.visual.ColorVisuals(mesh, vertex_colors=np.tile(rgb(hexcolor), (len(mesh.vertices), 1)))
    return mesh


def ellipsoid(center, rx, ry, rz, hexcolor, subdivisions=3):
    m = tc.icosphere(subdivisions=subdivisions, radius=1.0)
    m.apply_scale([rx, ry, rz])
    m.apply_translation(center)
    return colored(m, hexcolor)


def sphere(center, r, hexcolor, subdivisions=3):
    return ellipsoid(center, r, r, r, hexcolor, subdivisions)


def capsule_between(p0, p1, radius, hexcolor):
    p0 = np.array(p0, dtype=float)
    p1 = np.array(p1, dtype=float)
    height = np.linalg.norm(p1 - p0)
    # trimesh.creation.capsule() is already centered at the origin along Z,
    # with hemisphere centers at z=-height/2 and z=+height/2 -- no extra
    # recentering translation needed before the rotate+translate below.
    m = tc.capsule(height=height, radius=radius, count=[8, 12])
    axis = (p1 - p0) / height
    z = np.array([0, 0, 1.0])
    if np.allclose(axis, z):
        rot = np.eye(4)
    elif np.allclose(axis, -z):
        rot = trimesh.transformations.rotation_matrix(np.pi, [1, 0, 0])
    else:
        v = np.cross(z, axis)
        s = np.linalg.norm(v)
        cth = np.dot(z, axis)
        vx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
        R3 = np.eye(3) + vx + vx.dot(vx) * ((1 - cth) / (s ** 2))
        rot = np.eye(4)
        rot[:3, :3] = R3
    m.apply_transform(rot)
    m.apply_translation(p0 + (p1 - p0) / 2.0)
    return colored(m, hexcolor)


def torus_ring(center, major_r, minor_r, hexcolor):
    m = tc.torus(major_radius=major_r, minor_radius=minor_r)
    m.apply_translation(center)
    return colored(m, hexcolor)


def stroke_polygon(points, width):
    """A 2D 'thick line' shape through points, local (x=right, y=up)."""
    return LineString(points).buffer(width / 2.0, quad_segs=12, cap_style=1, join_style=1)


def emblem_from_shapely(poly, thickness, hexcolor):
    """poly: shapely (Multi)Polygon in local (x=right, y=up) coords, apex/
    shape drawn upright. Extrudes forward (+Y in world) once translated to
    the torso front."""
    geoms = list(poly.geoms) if poly.geom_type == "MultiPolygon" else [poly]
    meshes = [tc.extrude_polygon(g, height=thickness) for g in geoms if not g.is_empty]
    m = trimesh.util.concatenate(meshes)
    R = trimesh.transformations.rotation_matrix(np.pi / 2, [1, 0, 0])
    m.apply_transform(R)
    return colored(m, hexcolor)


def emblem_mesh(points_xy_up, thickness, hexcolor):
    """points_xy_up: (x=right, y=up) local coords, apex/shape drawn upright.
    Extrudes forward (+Y in world) once placed at the torso front."""
    return emblem_from_shapely(Polygon(points_xy_up), thickness, hexcolor)


def tail_mesh(path_points, radius, hexcolor, bead_points=(), bead_r=2.6, glow_point=None, glow_r=4.2, glow_hex=None):
    path = np.array(path_points, dtype=float)
    n = max(len(path) * 6, 48)
    smooth = trimesh.path.simplify.resample_spline(path, smooth=0.15, count=n)
    circle = Polygon([(radius * np.cos(t), radius * np.sin(t)) for t in np.linspace(0, 2 * np.pi, 12)])
    tube = tc.sweep_polygon(circle, smooth)
    parts = [colored(tube, hexcolor)]
    for bp in bead_points:
        parts.append(sphere(bp, bead_r, hexcolor, subdivisions=2))
    if glow_point is not None:
        parts.append(sphere(glow_point, glow_r, glow_hex or hexcolor, subdivisions=2))
    return parts


def base_disc(radius=15, height=2.2, hexcolor="#111827"):
    m = tc.cylinder(radius=radius, height=height, sections=56)
    m.apply_translation([0, 0, height / 2.0])
    return colored(m, hexcolor)


DEFAULT_TAIL_PATH = [(0, -8, 32), (9, -11, 26), (14, -11, 18), (15, -8, 10), (12, -5, 4.5), (7, -3, 2.2)]
DEFAULT_TAIL_BEADS = [(10, -11, 23), (14.5, -9.5, 13), (13, -6, 7)]
DEFAULT_TAIL_GLOW = (7, -3, 2.2)


# ---------------------------------------------------------------------
def build_character(colors, hair_fn, emblem_fn, mouth_fn, eye_z=54.5, mouth_z=51.5, extra_fn=None):
    c = colors
    parts = [base_disc()]

    # legs + boots (front-offset so boots peek past the torso silhouette)
    for sx in (-5.5, 5.5):
        parts.append(capsule_between((sx, 0, 5.5), (sx, 0.5, 17), 3.1, c["suit_dark"]))
        parts.append(ellipsoid((sx, 2.5, 3.4), 4.6, 6.2, 3.2, c["boot"]))

    # torso: taller than wide, not a ball
    parts.append(ellipsoid((0, 0, 30), 10.5, 8.5, 13.5, c["suit"]))

    # arms + gloves, angled out and slightly forward
    for sx in (-1, 1):
        shoulder = (sx * 9.5, 1, 38)
        hand = (sx * 20, 4, 30)
        parts.append(capsule_between(shoulder, hand, 3.0, c["suit"]))
        parts.append(sphere(hand, 3.6, c["glove"]))

    # neck: an explicit bridge from torso to head so the two are always
    # solidly connected regardless of how the ellipsoid/sphere surfaces
    # happen to line up (verified with build_color3d.check_connectivity)
    parts.append(capsule_between((0, 0, 39), (0, 0, 50), 5.2, c["suit_dark"]))
    # neck collar (decorative, wraps the neck)
    parts.append(torus_ring((0, 0, 45), 6.4, 2.1, c["helmet_ring"]))

    # head
    parts.append(sphere((0, 0, 53), 8.6, c["skin"]))
    hair_fn(parts, c)

    # eyes + mouth (on the head's front hemisphere)
    for sx in (-2.5, 2.5):
        parts.append(sphere((sx, 8.0, eye_z), 1.05, "#111827"))
    mouth_fn(parts, c, mouth_z)

    # chest emblem, centered on the torso front at world (0, 9.4, 34)
    emblem_fn(parts, c)

    # axon-cable tail
    parts += tail_mesh(
        path_points=DEFAULT_TAIL_PATH, radius=2.1, hexcolor=c["boot"],
        bead_points=DEFAULT_TAIL_BEADS, bead_r=1.9,
        glow_point=DEFAULT_TAIL_GLOW, glow_r=3.3, glow_hex=c["accent"],
    )

    if extra_fn:
        extra_fn(parts, c)

    return [p for p in parts if p is not None]


def polygon_emblem(points_xy_up, thickness=1.6, at=(0, 8.5, 34)):
    def fn(parts, c):
        m = emblem_mesh(points_xy_up, thickness, c["accent"])
        m.apply_translation(list(at))
        parts.append(m)
    return fn


def stroke_emblem(strokes, width=1.6, thickness=1.6, at=(0, 8.5, 34)):
    """strokes: list of point-lists, each a polyline in local (x=right,
    y=up) coords; unioned into one filled badge shape (a crisper look than
    mounting separate thin 3D capsule sticks)."""
    poly = unary_union([stroke_polygon(pts, width) for pts in strokes])

    def fn(parts, c):
        m = emblem_from_shapely(poly, thickness, c["accent"])
        m.apply_translation(list(at))
        parts.append(m)
    return fn


def mouth_shape(poly, thickness=1.0, y=8.7, hexcolor="#111827"):
    """A flat mouth badge (same technique as the chest emblems) mounted on
    the head's front hemisphere at world (0, y, mouth_z) -- mouth_z comes
    from build_character's per-character parameter at call time."""
    def fn(parts, c, mouth_z):
        m = emblem_from_shapely(poly, thickness, hexcolor)
        m.apply_translation([0, y, mouth_z])
        parts.append(m)
    return fn


def sparkle_points(r_out=6.5, r_in=1.8, n=4):
    pts = []
    for i in range(n * 2):
        ang = np.pi / 2 - i * np.pi / n
        r = r_out if i % 2 == 0 else r_in
        pts.append((r * np.cos(ang), r * np.sin(ang)))
    return pts


# ---------------------------------------------------------------------
CORTEX = dict(
    skin="#5b3a29", suit="#7c3aed", suit_dark="#5b21b6", boot="#312e81",
    glove="#ede9fe", helmet_ring="#7c3aed", accent="#fde047", hair="#1c1917",
)
CORTEX_STAR = [
    (0, 7.5), (1.8, 2.5), (7, 2.3), (3, -0.9), (4.3, -6),
    (0, -3.3), (-4.3, -6), (-3, -0.9), (-7, 2.3), (-1.8, 2.5),
]


def cortex_hair(parts, c):
    for hx, hz in ((-5.2, 58.5), (0, 61), (5.2, 58.5)):
        parts.append(sphere((hx, 1, hz), 4.3, c["hair"]))


# confident, warm closed smile -- the mission lead
CORTEX_MOUTH = stroke_polygon([(-3.4, 0.4), (-1.7, -0.9), (0, -1.3), (1.7, -0.9), (3.4, 0.4)], width=1.1)


def build_cortex():
    return build_character(CORTEX, cortex_hair, polygon_emblem(CORTEX_STAR), mouth_shape(CORTEX_MOUTH))


# ---------------------------------------------------------------------
AXON = dict(
    skin="#f3c19f", suit="#06b6d4", suit_dark="#0e7490", boot="#164e63",
    glove="#cffafe", helmet_ring="#0891b2", accent="#fbbf24", hair="#7c2d12",
)
# lightning bolt: SVG y-down pts (1,3)(-4,11)(0,11)(-2,18)(5,9)(1,9)(4,3), remapped to y-up (12 - origY)
AXON_BOLT = [(1, 9), (-4, 1), (0, 1), (-2, -6), (5, 3), (1, 3), (4, 9)]


def axon_hair(parts, c):
    parts.append(ellipsoid((0, 1, 60), 7.4, 6.6, 4.6, c["hair"]))


def axon_extra(parts, c):
    parts.append(capsule_between((0, 0, 61.5), (0, 0, 68), 1.1, c["suit_dark"]))
    parts.append(sphere((0, 0, 68.6), 1.7, c["accent"]))


# excited, wide-open grin -- the fast scout
AXON_MOUTH = stroke_polygon([(-2.3, 0), (2.3, 0)], width=2.0)


def build_axon():
    return build_character(
        AXON, axon_hair, polygon_emblem(AXON_BOLT, at=(0, 8.5, 32)), mouth_shape(AXON_MOUTH), extra_fn=axon_extra,
    )


# ---------------------------------------------------------------------
DENDRA = dict(
    skin="#8d5524", suit="#059669", suit_dark="#065f46", boot="#064e3b",
    glove="#d1fae5", helmet_ring="#059669", accent="#a7f3d0", hair="#111827",
)


def dendra_hair(parts, c):
    for hx in (-6.2, 6.2):
        parts.append(sphere((hx, 0.5, 59.5), 4.4, c["hair"]))


DENDRA_TWIG = [
    [(0, -6), (0, 5)],
    [(0, 1), (-4.5, 5)],
    [(0, 1), (4.5, 5)],
    [(0, -2), (-3, 1)],
    [(0, -2), (3, 1)],
]


# soft, gentle closed smile -- the attentive listener
DENDRA_MOUTH = stroke_polygon([(-2.4, 0.15), (-1.2, -0.4), (0, -0.55), (1.2, -0.4), (2.4, 0.15)], width=0.75)


def build_dendra():
    return build_character(
        DENDRA, dendra_hair, stroke_emblem(DENDRA_TWIG, width=1.5, at=(0, 8.5, 36)), mouth_shape(DENDRA_MOUTH),
    )


# ---------------------------------------------------------------------
SYN = dict(
    skin="#e8b48c", suit="#ea580c", suit_dark="#9a3412", boot="#7c2d12",
    glove="#ffedd5", helmet_ring="#ea580c", accent="#fde047", hair="#292524",
)


def syn_hair(parts, c):
    parts.append(ellipsoid((0, -1, 61.5), 3.2, 6.8, 5.5, c["hair"]))


# excited, surprised little "o" -- the energetic connector
SYN_MOUTH = Point(0, -0.3).buffer(1.7, quad_segs=16)


def build_syn():
    return build_character(
        SYN, syn_hair, polygon_emblem(sparkle_points(r_out=6.0, r_in=1.6), at=(0, 8.5, 34)),
        mouth_shape(SYN_MOUTH), eye_z=55, mouth_z=52.5,
    )


# ---------------------------------------------------------------------
GLIA = dict(
    skin="#f3c19f", suit="#db2777", suit_dark="#9d174d", boot="#831843",
    glove="#fce7f3", helmet_ring="#db2777", accent="#a5f3fc", hair="#d6d3d1",
)


def glia_hair(parts, c):
    parts.append(ellipsoid((0, 1, 60.5), 7.2, 6.4, 4.4, c["hair"]))


def _hexagon(cx, cy, r):
    return Polygon([(cx + r * np.cos(np.pi / 2 + i * np.pi / 3), cy + r * np.sin(np.pi / 2 + i * np.pi / 3))
                    for i in range(6)])


GLIA_WRENCH_POLY = unary_union([
    _hexagon(0, 3.4, 2.7),
    Polygon([(-0.9, -5), (0.9, -5), (0.9, 3.0), (-0.9, 3.0)]),
])


def glia_emblem(parts, c):
    m = emblem_from_shapely(GLIA_WRENCH_POLY, 1.6, c["accent"])
    m.apply_translation([0, 8.5, 33])
    parts.append(m)


def glia_extra(parts, c):
    # two small tool pouches at the hip, mounted the same safe-embedding
    # way as the chest emblems rather than a full belt (a torus wide
    # enough to grip this ellipsoid torso's un-even cross-section looks
    # like an inner tube, not a belt -- not worth the trade-off).
    for sx, hexcolor in ((-6.0, "#fbbf24"), (6.0, "#a5f3fc")):
        parts.append(ellipsoid((sx, 6.4, 20), 2.2, 1.8, 3.0, hexcolor))
        parts.append(capsule_between((sx, 0.5, 20), (sx, 6.4, 20), 1.6, c["suit_dark"]))


# focused, one-sided smirk -- the engineer mid-repair
GLIA_MOUTH = stroke_polygon([(-2.6, -0.2), (-0.6, -0.5), (0.8, -0.35), (2.3, 0.9)], width=0.85)


def build_glia():
    return build_character(GLIA, glia_hair, glia_emblem, mouth_shape(GLIA_MOUTH), extra_fn=glia_extra)


def verify_connected(parts, margin=0.5, min_volume=0.15):
    """Confirm the whole figure prints as one physically joined object:
    every part must share real solid volume (not just a touching bbox)
    with at least one other part, and the part-adjacency graph must be a
    single connected component. Returns (ok, report_lines)."""
    n = len(parts)
    boxes = [p.bounds for p in parts]

    def boxes_close(a, b):
        return all(a[0][k] - margin <= b[1][k] and b[0][k] - margin <= a[1][k] for k in range(3))

    adj = [[] for _ in range(n)]
    thin = []
    for i in range(n):
        for j in range(i + 1, n):
            if not boxes_close(boxes[i], boxes[j]):
                continue
            try:
                inter = trimesh.boolean.intersection([parts[i], parts[j]], engine="manifold")
                vol = inter.volume if inter is not None and len(inter.vertices) > 0 else 0.0
            except Exception:
                vol = 0.0
            if vol > min_volume:
                adj[i].append(j)
                adj[j].append(i)
            elif vol > 0:
                thin.append((i, j, vol))

    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)

    isolated = [i for i in range(n) if not adj[i]]
    unreached = sorted(set(range(n)) - seen)
    lines = []
    if isolated:
        lines.append(f"parts with NO solid connection to anything: {isolated}")
    if unreached:
        lines.append(f"parts not reachable from part 0 (disconnected sub-cluster): {unreached}")
    for i, j, vol in thin:
        lines.append(f"thin joint parts {i}-{j}: only {vol:.3f} mm^3 overlap")
    ok = not isolated and not unreached
    return ok, lines


def as_materialed(mesh, name):
    """Copy of `mesh` with its uniform vertex color converted into a small
    solid-color UV texture, so OBJ export writes real `vt` UV coordinates
    plus a `map_Kd <name>.png` in material.mtl -- not just a bare `Kd`
    value with no texture and no UV coordinates.

    Shapeways documents exactly two color paths for OBJ uploads: real
    per-vertex color, or a UV-mapped bitmap texture (JPG/PNG/GIF) -- see
    their self-service upload guide linked in README.md. A `usemtl` +
    flat `Kd` with no texture and no `vt` lines is valid OBJ but isn't
    either of those documented paths, and print services built around
    "vertex color or texture" can silently ignore it and import the
    model as plain grey. Since every part here really is one flat solid
    color, the texture is trivial: a single-pixel PNG, UV-mapped to its
    center for every vertex."""
    from PIL import Image

    m = mesh.copy()
    rgba = tuple(np.asarray(mesh.visual.vertex_colors[0], dtype=np.uint8))
    image = Image.new("RGB", (8, 8), rgba[:3])
    uv = np.full((len(m.vertices), 2), 0.5)
    mat = trimesh.visual.material.SimpleMaterial(image=image, diffuse=rgba, name=name)
    m.visual = trimesh.visual.TextureVisuals(uv=uv, image=image, material=mat)
    return m


def export_full_color(parts, name, out_dir):
    """Full-color OBJ+MTL, one self-contained folder (and zip) per
    character. trimesh's OBJ exporter always names the material file
    exactly `material.mtl` regardless of the .obj's own name, so two
    characters exported into the same flat directory would silently
    overwrite each other's materials -- hence the per-character subfolder,
    which also matches Shapeways' documented "upload a zip containing the
    model + its MTL" workflow."""
    import os
    import shutil
    import zipfile

    char_dir = os.path.join(out_dir, name)
    os.makedirs(char_dir, exist_ok=True)

    materialed = [as_materialed(p, f"{name}_{i:02d}") for i, p in enumerate(parts)]
    obj_path = os.path.join(char_dir, f"neuronaut3d-{name}.obj")
    trimesh.Scene(materialed).export(obj_path)

    glb_path = os.path.join(out_dir, f"neuronaut3d-{name}.glb")
    trimesh.Scene(parts).export(glb_path)

    zip_path = os.path.join(out_dir, f"neuronaut3d-{name}-fullcolor.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for fname in os.listdir(char_dir):
            zf.write(os.path.join(char_dir, fname), arcname=fname)

    return obj_path, glb_path, zip_path


CHARACTERS_3D = {
    "cortex": build_cortex,
    "axon": build_axon,
    "dendra": build_dendra,
    "syn": build_syn,
    "glia": build_glia,
}


if __name__ == "__main__":
    import os
    import sys
    import zipfile

    out_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    char_dirs = []
    for name, fn in CHARACTERS_3D.items():
        parts = fn()
        bad = [i for i, p in enumerate(parts) if not p.is_watertight]
        ok, report = verify_connected(parts)
        obj_path, glb_path, zip_path = export_full_color(parts, name, out_dir)
        char_dirs.append(os.path.dirname(obj_path))
        status = "OK" if ok and not bad else "FAIL"
        print(f"{name}: {len(parts)} parts, non-watertight={bad}, connected={ok} [{status}] -> {zip_path}")
        for line in report:
            print(f"    {line}")

    all_zip = os.path.join(out_dir, "neuronaut3d-all-five-fullcolor.zip")
    with zipfile.ZipFile(all_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for cdir in char_dirs:
            char_name = os.path.basename(cdir)
            for fname in os.listdir(cdir):
                zf.write(os.path.join(cdir, fname), arcname=f"{char_name}/{fname}")
    print(f"all-five: -> {all_zip}")
