"""Morphometry for the synthetic skeletons in the Module 09 and Module 16 kits.

All skeletons are synthetic teaching morphologies written by
scripts/generate_kit_materials.rb on neurotrailblazers.org; none is a
reconstruction of a real neuron. Python 3, standard library only.

    python3 morphometry.py                          # descriptor table, all cells
    python3 morphometry.py --cell cell07 --detail   # per-dendrite breakdown
    python3 morphometry.py --cell cell02 --sholl 10 # Sholl counts every 10 um
    python3 morphometry.py --swc neurons/basket.swc --sholl 10

Descriptors: cable length (um), branch points, tips, maximum Strahler order,
spine count and density (spines per um), and an arbor-volume proxy (the
axis-aligned bounding box of the dendrites, which overstates oblique arbors).
With volume.json present it also reports soma distance to the nearest face,
dendrites cut by a face, spine density on uncut dendrites only, and terminal
branches shorter than 2 um.
"""

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read_swc(path):
    nodes = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        i, t, x, y, z, r, p = line.split()
        nodes[int(i)] = (int(t), float(x), float(y), float(z), float(r), int(p))
    children = defaultdict(list)
    for i, n in nodes.items():
        if n[5] != -1:
            children[n[5]].append(i)
    return nodes, children


def seg_len(nodes, i):
    n, p = nodes[i], nodes[nodes[i][5]]
    return math.dist(n[1:4], p[1:4])


def subtree(children, root):
    out, stack = [], [root]
    while stack:
        i = stack.pop()
        out.append(i)
        stack.extend(children[i])
    return out


def strahler(children, i):
    kids = children[i]
    if not kids:
        return 1
    orders = sorted((strahler(children, k) for k in kids), reverse=True)
    return orders[0] + 1 if len(orders) > 1 and orders[0] == orders[1] else orders[0]


def load_spines():
    counts = defaultdict(lambda: defaultdict(int))
    path = HERE / "spines.csv"
    if path.exists():
        with open(path, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                counts[row["cell_id"]][int(row["node_id"])] += 1
    return counts


def load_bounds():
    path = HERE / "volume.json"
    if not path.exists():
        return None
    b = json.loads(path.read_text(encoding="utf-8"))["bounds_um"]
    return [b["x"], b["y"], b["z"]]


def on_face(n, bounds, tol=0.5):
    return any(abs(c - lo) <= tol or abs(c - hi) <= tol for c, (lo, hi) in zip(n[1:4], bounds))


def describe(name, nodes, children, spines, bounds):
    soma = next(i for i, n in nodes.items() if n[0] == 1)
    dend = [i for i, n in nodes.items() if n[0] != 1]
    cable = sum(seg_len(nodes, i) for i in dend)
    branch_points = sum(1 for i in dend if len(children[i]) >= 2)
    tips = sum(1 for i in dend if not children[i])
    xs = [[nodes[i][k] for i in dend] for k in (1, 2, 3)]
    bbox = math.prod(max(v) - min(v) for v in xs)
    n_spines = sum(spines.get(i, 0) for i in dend)
    row = {
        "cell": name,
        "cable_um": round(cable, 1),
        "branch_points": branch_points,
        "tips": tips,
        "max_strahler": max(strahler(children, k) for k in children[soma]),
        "spines": n_spines,
        "spine_density_per_um": round(n_spines / cable, 3) if cable else 0.0,
        "arbor_bbox_um3": round(bbox),
    }
    # Terminal branches: from a branch point (or the soma) to a tip.
    short = 0
    for i in dend:
        if children[i]:
            continue
        length, j = 0.0, i
        while nodes[j][5] != -1 and len(children[nodes[j][5]]) < 2 and nodes[nodes[j][5]][0] != 1:
            length += seg_len(nodes, j)
            j = nodes[j][5]
        length += seg_len(nodes, j)
        short += length < 2.0
    row["terminal_branches_under_2um"] = short
    detail = []
    for k in children[soma]:
        ids = subtree(children, k)
        c = sum(seg_len(nodes, i) for i in ids)
        s = sum(spines.get(i, 0) for i in ids)
        cut = bool(bounds) and any(on_face(nodes[i], bounds) for i in ids)
        detail.append({"dendrite_root_node": k, "type": "apical" if nodes[k][0] == 4 else "basal",
                       "cable_um": round(c, 1), "spines": s,
                       "spine_density_per_um": round(s / c, 3) if c else 0.0, "cut_by_face": cut})
    if bounds:
        sx = nodes[soma][1:4]
        row["soma_to_face_um"] = round(min(min(c - lo, hi - c) for c, (lo, hi) in zip(sx, bounds)), 1)
        row["dendrites_cut_by_face"] = sum(d["cut_by_face"] for d in detail)
        kept = [d for d in detail if not d["cut_by_face"]]
        kc = sum(d["cable_um"] for d in kept)
        row["spine_density_uncut_dendrites"] = round(sum(d["spines"] for d in kept) / kc, 3) if kc else None
    return row, detail


def sholl(nodes, step):
    soma = next(i for i, n in nodes.items() if n[0] == 1)
    centre = nodes[soma][1:4]
    radial = {i: math.dist(n[1:4], centre) for i, n in nodes.items()}
    rmax = max(radial.values())
    out = []
    r = step
    while r <= rmax + step:
        crossings = sum(1 for i, n in nodes.items()
                        if n[5] != -1 and nodes[n[5]][0] != 1
                        and (radial[n[5]] - r) * (radial[i] - r) < 0)
        out.append({"radius_um": r, "intersections": crossings})
        r += step
    return out


def main():
    ap = argparse.ArgumentParser(description="Morphometry for synthetic teaching skeletons.")
    ap.add_argument("--cell", help="cell ID, e.g. cell07 (reads skeletons/<cell>.swc)")
    ap.add_argument("--swc", help="path to any SWC file instead of --cell")
    ap.add_argument("--detail", action="store_true", help="per-dendrite breakdown")
    ap.add_argument("--sholl", type=float, help="Sholl step in um")
    args = ap.parse_args()

    spines = load_spines()
    bounds = load_bounds()
    if args.swc:
        targets = [(Path(args.swc).stem, Path(args.swc))]
    elif args.cell:
        targets = [(args.cell, HERE / "skeletons" / (args.cell + ".swc"))]
    else:
        targets = [(p.stem, p) for p in sorted((HERE / "skeletons").glob("*.swc"))]

    rows = []
    for name, path in targets:
        nodes, children = read_swc(path)
        if args.sholl:
            print(json.dumps({"cell": name, "sholl": sholl(nodes, args.sholl)}, indent=2))
            continue
        row, detail = describe(name, nodes, children, spines.get(name, {}), bounds)
        rows.append(row)
        if args.detail:
            print(json.dumps({"cell": name, "summary": row, "dendrites": detail}, indent=2))
    if rows and not args.detail:
        cols = list(rows[0])
        print("\t".join(cols))
        for row in rows:
            print("\t".join(str(row.get(c, "")) for c in cols))
        print("# synthetic teaching data; arbor_bbox_um3 is a bounding box, not a hull")


if __name__ == "__main__":
    main()
