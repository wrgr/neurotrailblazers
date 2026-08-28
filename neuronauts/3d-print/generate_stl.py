"""
Generate flat 3D-print STLs for the five Neuronauts characters,
reconstructed from the exact coordinates used in the site's inline SVG
(neuronauts/index.html, <g id="nn-cortex/axon/dendra/syn/glia">).

Design: a two-piece standee.
  - Figure panel: a two-layer relief.
      Layer A ("base"): the full body silhouette (legs, boots, torso, arms,
      gloves, helmet, head, hair, axon-cable tail + bouton, tools/belt),
      extruded to BASE_MM thickness, with a small rectangular TAB fused
      below the boots so the flat panel can slot into a stand.
      Layer B ("detail"): the chest emblem + eyes + mouth, raised an extra
      DETAIL_MM on top of layer A, for a painted-relief look.
    Prints flat (no supports) but does NOT stand up on its own: a bare
    BASE_MM-thick panel balanced on its edge is not stable. Use the base
    below to display it upright.
  - Stand base (`neuronaut-stand-base.stl`, shared by all five figures):
    a squat block with a through-slot sized to the tab (plus clearance)
    so any figure panel presses into it and stands vertically. Also
    prints flat, no supports. Print one base per figure you want
    displayed at once.

Units: SVG coordinates are the original character-local units (as used in
neuronauts/index.html); XY is scaled by SCALE to millimeters, Z is set
directly in millimeters.

Sync with neuronauts/index.html: the shapely geometry below is a manual
transcription of each character's <g id="nn-*"> markup, not a live parse
of it, so editing the SVG in index.html does NOT automatically update
these shapes. To catch that drift, EXPECTED_SVG_HASHES below records a
hash of each character's exact <g> markup as of the last time this
geometry was updated; running this script re-hashes the live file and
refuses to generate stale STLs if they no longer match. After
intentionally changing a character's SVG, update the corresponding
shape function(s) in this file to match, then run
`python generate_stl.py --freeze-hashes` to print the new hashes to
paste into EXPECTED_SVG_HASHES.
"""
import hashlib
import math
import re
from pathlib import Path

from shapely.geometry import Polygon, LineString, box, Point
from shapely.ops import unary_union
import shapely.affinity as aff
import trimesh

SCALE = 0.8          # mm per SVG unit (XY)
BASE_MM = 3.2         # base layer thickness
DETAIL_MM = 1.3        # extra height for raised emblem/eyes/mouth

TAB = (-11, 54, 11, 67)   # x0, y0, x1, y1 in SVG units: tab fused below the boots
TAB_R = 2

STAND_LENGTH_MM = 46.0    # base block footprint
STAND_WIDTH_MM = 26.0
STAND_HEIGHT_MM = 12.0
STAND_R_MM = 4.0
SLOT_CLEARANCE_MM = 0.4   # extra width/depth added to the tab's own size for a friction fit

SOURCE_HTML = Path(__file__).resolve().parent.parent / "index.html"

# sha256 of each character's exact "<g id=\"nn-<name>\">...</g>" markup in
# neuronauts/index.html, as of the last time the shapes below were updated
# to match it. Regenerate with `python generate_stl.py --freeze-hashes`
# after intentionally changing both the SVG and this file together.
EXPECTED_SVG_HASHES = {
    "cortex": "9a84c49651be9daa8f5a9b9d0dda1b92249b93de22b8be39f7be3876ce512ce5",
    "axon": "b17083b69035c0638f383c59a6f964c39685b90f0e542e37e681ae4fae6d9ad9",
    "dendra": "ff814881b398cecd1dee952c8c7dc07be4e30d0b29679c60d9b1157b767c32dc",
    "syn": "934caf4386f27d62ff2a4a0de7f08859c9c0065740bdd2f52d642be8fe23e318",
    "glia": "c917f4e86b4f3479688a58ff6b04a160b7b828127e626164d701771460bd8632",
}


def extract_character_svg(name, html_text=None):
    """Return the exact "<g id=\"nn-<name>\">...</g>" markup from index.html,
    including its nested <g> children (shoulder etches, tail, helmet
    spines, ...) up to the matching closing tag."""
    text = html_text if html_text is not None else SOURCE_HTML.read_text()
    start_tag = f'<g id="nn-{name}">'
    start = text.find(start_tag)
    if start == -1:
        raise RuntimeError(f'Could not find {start_tag!r} in {SOURCE_HTML}')
    depth = 0
    pos = start
    for m in re.finditer(r"<g[ >]|</g>", text[start:]):
        depth += 1 if m.group().startswith("<g") else -1
        if depth == 0:
            pos = start + m.end()
            break
    else:
        raise RuntimeError(f'Unbalanced <g> tags scanning nn-{name} in {SOURCE_HTML}')
    return text[start:pos]


def check_svg_in_sync():
    """Fail loudly if index.html's character markup no longer matches the
    markup EXPECTED_SVG_HASHES was recorded from, instead of silently
    generating STLs that no longer match the published artwork."""
    html_text = SOURCE_HTML.read_text()
    mismatches = []
    for name, expected in EXPECTED_SVG_HASHES.items():
        actual = hashlib.sha256(extract_character_svg(name, html_text).encode()).hexdigest()
        if actual != expected:
            mismatches.append((name, actual))
    if mismatches:
        lines = [
            "neuronauts/3d-print/generate_stl.py is out of sync with neuronauts/index.html.",
            "The SVG markup for these characters has changed since the shapely geometry",
            "below was last written, so the STLs would no longer match the published art:",
        ]
        for name, actual in mismatches:
            lines.append(f'  - nn-{name}: expected hash {EXPECTED_SVG_HASHES[name]!r}, got {actual!r}')
        lines.append(
            "Update the corresponding shape function(s) in this file to match the new SVG, "
            "then run `python generate_stl.py --freeze-hashes` and paste the printed hashes "
            "into EXPECTED_SVG_HASHES."
        )
        raise SystemExit("\n".join(lines))


def freeze_hashes():
    html_text = SOURCE_HTML.read_text()
    print("EXPECTED_SVG_HASHES = {")
    for name in EXPECTED_SVG_HASHES:
        h = hashlib.sha256(extract_character_svg(name, html_text).encode()).hexdigest()
        print(f'    "{name}": "{h}",')
    print("}")


def circle(cx, cy, r, res=48):
    return Point(cx, cy).buffer(r, quad_segs=res)


def ellipse(cx, cy, rx, ry, res=48):
    c = Point(0, 0).buffer(1, quad_segs=res)
    e = aff.scale(c, rx, ry, origin=(0, 0))
    return aff.translate(e, cx, cy)


def rounded_rect(x, y, w, h, r, res=16):
    if r <= 0:
        return box(x, y, x + w, y + h)
    inset = box(x + r, y + r, x + w - r, y + h - r)
    return inset.buffer(r, quad_segs=res)


def polygon(pts):
    return Polygon(pts)


def capsule(points, width, res=16):
    return LineString(points).buffer(width / 2, quad_segs=res, cap_style=1, join_style=1)


def svg_arc_points(p0, rx, ry, x_rot_deg, large_arc, sweep, p1, n=24):
    """Sample an SVG elliptical arc (endpoint parameterization) into points.
    p0, p1: (x, y) start/end. Returns list including both endpoints."""
    x1, y1 = p0
    x2, y2 = p1
    if (x1, y1) == (x2, y2):
        return [p0]
    phi = math.radians(x_rot_deg)
    cphi, sphi = math.cos(phi), math.sin(phi)
    dx2, dy2 = (x1 - x2) / 2.0, (y1 - y2) / 2.0
    x1p = cphi * dx2 + sphi * dy2
    y1p = -sphi * dx2 + cphi * dy2
    rx, ry = abs(rx), abs(ry)
    lam = (x1p ** 2) / (rx ** 2) + (y1p ** 2) / (ry ** 2)
    if lam > 1:
        s = math.sqrt(lam)
        rx *= s
        ry *= s
    sign = -1 if large_arc == sweep else 1
    num = (rx ** 2 * ry ** 2 - rx ** 2 * y1p ** 2 - ry ** 2 * x1p ** 2)
    den = (rx ** 2 * y1p ** 2 + ry ** 2 * x1p ** 2)
    co = sign * math.sqrt(max(num / den, 0.0))
    cxp = co * (rx * y1p) / ry
    cyp = -co * (ry * x1p) / rx
    cx = cphi * cxp - sphi * cyp + (x1 + x2) / 2.0
    cy = sphi * cxp + cphi * cyp + (y1 + y2) / 2.0

    def ang(ux, uy, vx, vy):
        d = math.hypot(ux, uy) * math.hypot(vx, vy)
        a = math.acos(max(-1, min(1, (ux * vx + uy * vy) / d)))
        return a if (ux * vy - uy * vx) >= 0 else -a

    theta1 = ang(1, 0, (x1p - cxp) / rx, (y1p - cyp) / ry)
    dtheta = ang((x1p - cxp) / rx, (y1p - cyp) / ry, (-x1p - cxp) / rx, (-y1p - cyp) / ry)
    if sweep == 0 and dtheta > 0:
        dtheta -= 2 * math.pi
    if sweep == 1 and dtheta < 0:
        dtheta += 2 * math.pi

    pts = []
    for i in range(n + 1):
        t = theta1 + dtheta * i / n
        ex = cx + rx * math.cos(t) * cphi - ry * math.sin(t) * sphi
        ey = cy + rx * math.cos(t) * sphi + ry * math.sin(t) * cphi
        pts.append((ex, ey))
    return pts


def quad_bezier(p0, p1, p2, n=12):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


# ---- shared body parts (identical across all 5 characters) ----
def legs():
    return unary_union([
        rounded_rect(-10, 30, 8, 18, 4),
        rounded_rect(2, 30, 8, 18, 4),
    ])


def boots():
    return unary_union([ellipse(-6, 50, 7, 4), ellipse(6, 50, 7, 4)])


def torso():
    return rounded_rect(-14, -2, 28, 36, 12)


def arms():
    return unary_union([rounded_rect(-22, 2, 9, 22, 4.5), rounded_rect(13, 2, 9, 22, 4.5)])


def gloves():
    return unary_union([circle(-17.5, 25, 4.5), circle(17.5, 25, 4.5)])


def helmet():
    return circle(0, -16, 15.5)


def head():
    return circle(0, -15, 11.5)


def tail():
    cable = capsule([(3, 32), (10, 35), (17, 40), (22, 46), (22, 50), (19, 54), (14, 58), (7, 56)], 6)
    beads = unary_union([circle(10, 36, 2.2), circle(18, 43, 2.2), circle(21, 50, 2.2)])
    bouton = circle(6, 57, 3.6)
    return unary_union([cable, beads, bouton])


def tab():
    x0, y0, x1, y1 = TAB
    return rounded_rect(x0, y0, x1 - x0, y1 - y0, TAB_R)


def mouth_smile(cy_offset=0):
    pts = quad_bezier((-4, -10 + cy_offset), (0, -6.5 + cy_offset), (4, -10 + cy_offset))
    return capsule(pts, 1.3)


def eyes(cy=-16, r=1.9, dx=4.5):
    return unary_union([circle(-dx, cy, r), circle(dx, cy, r)])


# ---- per-character extras ----
def cortex_shapes():
    hair = unary_union([circle(-9, -24, 4.5), circle(0, -26.5, 4.5), circle(9, -24, 4.5)])
    star = polygon([
        (0, 3), (1.8, 8), (7, 8.2), (3, 11.5), (4.3, 16.5),
        (0, 13.6), (-4.3, 16.5), (-3, 11.5), (-7, 8.2), (-1.8, 8),
    ])
    base = unary_union([legs(), boots(), tail(), torso(), arms(), gloves(), helmet(), head(), hair])
    detail = unary_union([star, eyes(), mouth_smile()])
    return base, detail


def axon_shapes():
    hair_dome = ellipse(0.5, -19, 11.5, 9).intersection(box(-30, -40, 30, -19))
    antenna = unary_union([capsule([(0, -31), (0, -38)], 2.5), circle(0, -40, 3)])
    bolt = polygon([(1, 3), (-4, 11), (0, 11), (-2, 18), (5, 9), (1, 9), (4, 3)])
    base = unary_union([legs(), boots(), tail(), torso(), arms(), gloves(), antenna, helmet(), head(), hair_dome])
    detail = unary_union([bolt, eyes(), mouth_smile(-0.3)])
    return base, detail


def dendra_shapes():
    hair = unary_union([circle(-10, -27, 5), circle(10, -27, 5)])
    branch = unary_union([
        capsule([(0, 16), (0, 8)], 2), capsule([(0, 10), (-5, 5)], 2), capsule([(0, 10), (5, 5)], 2),
        capsule([(0, 14), (-4, 11)], 2), capsule([(0, 14), (4, 11)], 2),
    ])
    base = unary_union([legs(), boots(), tail(), torso(), arms(), gloves(), helmet(), head(), hair])
    detail = unary_union([branch, eyes(), mouth_smile()])
    return base, detail


def syn_shapes():
    dome_start, dome_end = (-11, -17), (12, -17)
    dome_arc = svg_arc_points(dome_start, 11.5, 10.5, 0, 0, 1, dome_end, n=20)
    hair_pts = dome_arc + [(8, -21), (0, -26), (-8, -21)]
    hair = polygon(hair_pts)
    spark = unary_union([
        circle(0, 9, 4),
        capsule([(0, 1), (0, 3.5)], 1.8), capsule([(0, 14.5), (0, 17)], 1.8),
        capsule([(-8, 9), (-5.5, 9)], 1.8), capsule([(5.5, 9), (8, 9)], 1.8),
    ])
    base = unary_union([legs(), boots(), tail(), torso(), arms(), gloves(), helmet(), head(), hair])
    detail = unary_union([spark, eyes(-15), mouth_smile(1)])
    return base, detail


def glia_shapes():
    hair_dome = ellipse(0.5, -18, 11.5, 9.5).intersection(box(-30, -40, 30, -18))
    belt = rounded_rect(-14, 18, 28, 6, 3)
    pouch1 = rounded_rect(-6, 16.5, 5, 9, 1.5)
    pouch2 = rounded_rect(2, 16.5, 5, 9, 1.5)
    wrench_arc = svg_arc_points((-2, 4), 4, 4, 0, 1, 0, (2, 4), n=24)
    wrench_pts = wrench_arc + [(2, 12), (-2, 12)]
    wrench = polygon(wrench_pts).buffer(0)
    base = unary_union([legs(), boots(), tail(), torso(), arms(), gloves(), belt, pouch1, pouch2,
                         helmet(), head(), hair_dome])
    detail = unary_union([wrench, eyes(), mouth_smile()])
    return base, detail


CHARACTERS = {
    "cortex": cortex_shapes,
    "axon": axon_shapes,
    "dendra": dendra_shapes,
    "syn": syn_shapes,
    "glia": glia_shapes,
}


def extrude(poly, height, z0=0.0):
    if poly.is_empty:
        return None
    tf = trimesh.transformations.translation_matrix([0, 0, z0])
    geoms = list(poly.geoms) if poly.geom_type == "MultiPolygon" else [poly]
    meshes = [trimesh.creation.extrude_polygon(g, height=height, transform=tf) for g in geoms if not g.is_empty]
    if not meshes:
        return None
    return trimesh.util.concatenate(meshes)


def build(name, fn, out_dir):
    base_shape, detail_shape = fn()
    full_base = unary_union([base_shape, tab()])
    full_base = full_base.buffer(0)
    detail_shape = detail_shape.intersection(full_base.buffer(0.5))

    base_mesh = extrude(full_base, BASE_MM)
    meshes = [base_mesh]
    if not detail_shape.is_empty:
        detail_mesh = extrude(detail_shape, DETAIL_MM, z0=BASE_MM)
        if detail_mesh is not None:
            meshes.append(detail_mesh)

    combined = trimesh.util.concatenate(meshes)
    combined.apply_scale([SCALE, SCALE, 1.0])
    # flip Y (SVG y-down -> mm y-up) and sit flat on the print bed (z=0..)
    combined.apply_transform(trimesh.transformations.scale_matrix(-1, [0, 0, 0], [0, 1, 0]))
    combined.apply_translation([0, 0, 0])
    minb = combined.bounds[0]
    combined.apply_translation(-minb)

    out_path = f"{out_dir}/neuronaut-{name}.stl"
    combined.export(out_path)
    w, d, h = combined.extents
    print(f"{name}: watertight={combined.is_watertight} extents=({w:.1f}, {d:.1f}, {h:.1f}) mm -> {out_path}")
    return combined


def build_stand_base():
    """A squat block with a through-slot sized to fit any figure's tab, so
    the flat panel can be pressed in and stand upright. Boolean-cut with
    the manifold3d engine; both pieces still print flat, no supports."""
    block = trimesh.creation.box(extents=[STAND_LENGTH_MM, STAND_WIDTH_MM, STAND_HEIGHT_MM])

    tab_x0, tab_y0, tab_x1, tab_y1 = TAB
    tab_len_mm = (tab_x1 - tab_x0) * SCALE     # tab width becomes the slot's long axis
    tab_thick_mm = BASE_MM                     # tab thickness = the flat panel thickness

    slot = trimesh.creation.box(extents=[
        tab_len_mm + SLOT_CLEARANCE_MM,
        tab_thick_mm + SLOT_CLEARANCE_MM,
        STAND_HEIGHT_MM + 4.0,  # taller than the block for a clean through-cut
    ])
    stand = trimesh.boolean.difference([block, slot], engine="manifold")
    stand.apply_translation([0, 0, STAND_HEIGHT_MM / 2.0])
    return stand


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    if "--freeze-hashes" in args:
        freeze_hashes()
        raise SystemExit(0)

    check_svg_in_sync()

    out_dir = args[0] if args else "."
    meshes = []
    spacing = 55.0  # mm between figures on the shared plate
    for i, (name, fn) in enumerate(CHARACTERS.items()):
        m = build(name, fn, out_dir)
        plate_copy = m.copy()
        plate_copy.apply_translation([i * spacing, 0, 0])
        meshes.append(plate_copy)

    stand = build_stand_base()
    stand_path = f"{out_dir}/neuronaut-stand-base.stl"
    stand.export(stand_path)
    w, d, h = stand.extents
    print(f"stand-base: watertight={stand.is_watertight} extents=({w:.1f}, {d:.1f}, {h:.1f}) mm -> {stand_path}")

    plate_stand = stand.copy()
    plate_stand.apply_translation([len(CHARACTERS) * spacing, 0, 0])
    meshes.append(plate_stand)

    plate = trimesh.util.concatenate(meshes)
    plate_path = f"{out_dir}/neuronaut-all-five.stl"
    plate.export(plate_path)
    w, d, h = plate.extents
    print(f"all-five plate: watertight={plate.is_watertight} extents=({w:.1f}, {d:.1f}, {h:.1f}) mm -> {plate_path}")
