#!/usr/bin/env python3
"""Render the neuroanatomy and segmentation figures used across the content library.

Companion to render_h01_figures.py, which does the H01 pipeline walkthrough. This
one produces the structure-level figures the neuroanatomy, cell-type and
proofreading entries need: a myelinated axon, an asymmetric vs symmetric synapse
pair, a soma, an astrocyte, a blood vessel, the six-class subcompartment overlay,
and -- the one worth the whole script -- a real case where the aggressive `c2`
agglomeration merges two objects that the conservative `c3` keeps apart.

Structures are not eyeballed. They are located by querying H01's own annotation
layers (`masking` for myelin/vessel/nucleus, `c2/subcompartments` for
astrocyte/dendrite/soma/axon-initial-segment, the synapse annotations for
excitatory vs inhibitory), so a figure captioned "myelinated axon" is one the
dataset itself labels as such.

Data: the H01 release from the Lichtman Laboratory (Harvard) and the
Connectomics at Google team, licensed CC BY 4.0. Cite Shapson-Coe, A. et al.,
Science 384, eadk4858 (2024). doi:10.1126/science.adk4858

Requires:  pip install tensorstore pillow numpy scipy
Usage:     python3 scripts/render_em_figures.py [output_dir]
"""

import json
import struct
import sys
import urllib.request
from pathlib import Path

import numpy as np
import tensorstore as ts
from PIL import Image, ImageDraw, ImageFont

BASE = 'https://storage.googleapis.com/h01-release/data/20210601/'
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO_ROOT / 'assets' / 'images' / 'content-library' / 'em'

# Class ids, from each layer's own segment_properties.
MASK_MYELIN, MASK_NUCLEUS, MASK_VESSEL = 5, 3, 4
SUB_AXON, SUB_DENDRITE, SUB_ASTRO, SUB_SOMA, SUB_CILIUM, SUB_AIS = 100, 101, 102, 103, 104, 105
SUB_MYELINATED = (1100, 1101)

SUB_COLOURS = {
    SUB_AXON: (70, 150, 235), SUB_DENDRITE: (95, 190, 110), SUB_ASTRO: (240, 160, 60),
    SUB_SOMA: (150, 110, 225), SUB_CILIUM: (238, 214, 70), SUB_AIS: (233, 90, 90),
}
SUB_NAMES = {
    SUB_AXON: 'axon', SUB_DENDRITE: 'dendrite', SUB_ASTRO: 'astrocyte',
    SUB_SOMA: 'soma', SUB_CILIUM: 'cilium', SUB_AIS: 'axon initial segment',
}

_cache = {}


def layer(name, key):
    if (name, key) not in _cache:
        _cache[(name, key)] = ts.open({
            'driver': 'neuroglancer_precomputed',
            'kvstore': {'driver': 'http', 'base_url': BASE + name + '/'},
            'scale_metadata': {'key': key},
        }).result()
    return _cache[(name, key)]


def font(size):
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
              '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'):
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def stretch(a, gamma=0.9):
    """Percentile stretch over tissue pixels only, then gamma. See
    render_h01_figures.stretch for why the resin background is masked out."""
    a = a.astype(np.float32)
    bg = a >= 235
    s = a[~bg] if (bg.mean() > 0.02 and (~bg).sum() > 1000) else a
    p1, p2 = np.percentile(s, 1), np.percentile(s, 99)
    if p2 <= p1:
        return np.clip(a, 0, 255).astype(np.uint8)
    return (np.power(np.clip((a - p1) / (p2 - p1), 0, 1), gamma) * 255).astype(np.uint8)


EM_SCALES = {4: '4.0x4.0x33.0', 8: '8.0x8.0x33.0', 16: '16.0x16.0x33.0', 32: '32.0x32.0x33.0'}


def em(cx, cy, cz, nm_per_px, npx):
    d = layer('4nm_raw', EM_SCALES[nm_per_px])
    x0, y0 = int(cx / nm_per_px) - npx // 2, int(cy / nm_per_px) - npx // 2
    return d[x0:x0 + npx, y0:y0 + npx, int(cz / 33), 0].read().result()


def _bar(nm_per_px, npx):
    for v in (100, 200, 500, 1e3, 2e3, 5e3, 1e4, 2e4):
        if v >= nm_per_px * npx * 0.22:
            return v
    return 2e4


def decorate(img, nm_per_px, note=''):
    d = ImageDraw.Draw(img)
    w, h = img.size
    length = _bar(nm_per_px, w)
    px = length / nm_per_px
    lab = f"{length / 1e3:g} µm" if length >= 1e3 else f"{length:g} nm"
    x0, y0 = int(w * 0.05), int(h * 0.94)
    d.rectangle([x0 - 8, y0 - 30, x0 + px + 8, y0 + 12], fill=(0, 0, 0))
    d.rectangle([x0, y0, x0 + px, y0 + 5], fill=(255, 255, 255))
    d.text((x0, y0 - 26), lab, fill=(255, 255, 255), font=font(19))
    if note:
        f = font(18)
        tw = d.textlength(note, font=f)
        d.rectangle([w - tw - 18, 8, w - 6, 36], fill=(0, 0, 0))
        d.text((w - tw - 12, 11), note, fill=(255, 255, 255), font=f)
    return img


def save(img, out_dir, name, quality=88):
    p = Path(out_dir) / name
    img.save(p, quality=quality, optimize=True)
    print(f"  {name:36s} {str(img.size):12s} {p.stat().st_size // 1024:>4} KB")


# --------------------------------------------------------------------------
# locating structures from the dataset's own labels
# --------------------------------------------------------------------------

def find_structures(centre_nm, half_vox=1200):
    """Return {structure: (x_nm, y_nm, z_nm)} for the densest instance of each
    labelled class near `centre_nm`, read from the masking and subcompartment
    layers rather than chosen by eye."""
    from scipy.ndimage import uniform_filter

    nm, zr = 64, 66
    mask = layer('masking', '64.0x64.0x66.0')
    sub = layer('c2/subcompartments', '64x64x66')
    x0 = int(centre_nm[0] / nm) - half_vox
    y0 = int(centre_nm[1] / nm) - half_vox
    z = int(centre_nm[2] / zr)
    n = 2 * half_vox
    m = mask[x0:x0 + n, y0:y0 + n, z, 0].read().result()
    s = sub[x0:x0 + n, y0:y0 + n, z, 0].read().result()

    def peak(binary, box, margin=140):
        # mode='constant' so padding outside the tile counts as empty; otherwise
        # every edge pixel reads as maximally dense and all peaks land on the rim.
        dens = uniform_filter(binary.astype(np.float32), size=box, mode='constant', cval=0.0)
        dens[:margin, :] = 0; dens[-margin:, :] = 0
        dens[:, :margin] = 0; dens[:, -margin:] = 0
        i = int(np.argmax(dens))
        ix, iy = np.unravel_index(i, dens.shape)
        return ix, iy

    targets = {
        'myelin': (m == MASK_MYELIN, 12), 'blood_vessel': (m == MASK_VESSEL, 24),
        'nucleus': (m == MASK_NUCLEUS, 24), 'astrocyte': (s == SUB_ASTRO, 16),
        'AIS': (s == SUB_AIS, 8), 'dendrite': (s == SUB_DENDRITE, 12),
        'soma': (s == SUB_SOMA, 24), 'myelinated_axon': (np.isin(s, SUB_MYELINATED), 10),
    }
    found = {}
    for name, (b, box) in targets.items():
        if not b.any():
            continue
        ix, iy = peak(b, box)
        found[name] = (int((x0 + ix) * nm), int((y0 + iy) * nm), int(z * zr))
    return found


def load_synapses():
    """Volume-wide sample of synapse annotations (see render_h01_figures)."""
    with urllib.request.urlopen(BASE + 'c2/synapses/precomputed/spatial0/0_0_0', timeout=120) as r:
        b = r.read()
    count = struct.unpack('<Q', b[:8])[0]
    geom = np.frombuffer(b, dtype='<f4', count=count * 7, offset=8).reshape(count, 7)
    typ = np.frombuffer(b, dtype='<u4', count=count * 7, offset=8).reshape(count, 7)[:, 6]
    ids = np.frombuffer(b, dtype='<u8', count=count, offset=8 + count * 28)
    return geom[:, :6], typ, ids


# --------------------------------------------------------------------------
# figures
# --------------------------------------------------------------------------

def synapse_pair(out_dir, exc_id=76490072, inh_id=72511046, npx=460, nm_per_px=4):
    """Asymmetric (excitatory) beside symmetric (inhibitory), matched scale.

    Deliberately NO marker over the synapse: the postsynaptic density is the
    thing the reader is being taught to look at, so drawing an annotation across
    it hides the evidence. The corner tick marks the edge of the frame the
    annotation sits at the centre of instead.
    """
    pts, typ, ids = load_synapses()
    panels = []
    for sid, title, colour in ((exc_id, 'Excitatory · asymmetric', (255, 120, 120)),
                               (inh_id, 'Inhibitory · symmetric', (120, 180, 255))):
        i = int(np.where(ids == sid)[0][0])
        cx, cy, cz = pts[i, 0] * 8, pts[i, 1] * 8, pts[i, 2] * 33
        # No upscaling: at 4 nm a Type I PSD is only ~8-12 px thick, and
        # interpolating it larger amplifies shot noise instead of revealing
        # structure. Native pixels, displayed at native size.
        img = Image.fromarray(stretch(em(cx, cy, cz, nm_per_px, npx)).T).convert('RGB')
        d = ImageDraw.Draw(img)
        # ticks at the frame edges pointing at centre, so the synapse itself
        # stays completely unobstructed
        c = npx // 2
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            x1, y1 = c + dx * (c - 4), c + dy * (c - 4)
            x2, y2 = c + dx * (c - 22), c + dy * (c - 22)
            d.line([(x1, y1), (x2, y2)], fill=colour, width=2)
        decorate(img, nm_per_px)
        f = font(16)
        d.rectangle([0, 0, npx, 26], fill=(0, 0, 0))
        d.text((8, 5), f"{title} · id {sid}", fill=colour, font=f)
        panels.append(np.array(img))
    gap = np.full((panels[0].shape[0], 10, 3), 255, np.uint8)
    save(Image.fromarray(np.hstack([panels[0], gap, panels[1]])), out_dir,
         'synapse-asymmetric-vs-symmetric.jpg')


def raw_vs_overlay(out_dir, centre, nm_per_px=8, npx=700):
    """Raw neuropil beside the six-class subcompartment answer key.

    Raw first, deliberately: the reader classifies the profiles themselves, then
    checks. That is the exercise the classification pages describe in prose.
    """
    sub = layer('c2/subcompartments', '64x64x66')
    grey = stretch(em(centre[0], centre[1], centre[2], nm_per_px, npx)).T
    n64 = int(npx * nm_per_px / 64)
    x0, y0 = int(centre[0] / 64) - n64 // 2, int(centre[1] / 64) - n64 // 2
    s = sub[x0:x0 + n64, y0:y0 + n64, int(centre[2] / 66), 0].read().result().T
    s = np.array(Image.fromarray(s.astype(np.int32), mode='I').resize((npx, npx), Image.NEAREST))

    rgb = np.stack([grey] * 3, -1).astype(np.float32)
    overlay = np.zeros_like(rgb)
    m = np.zeros(s.shape, bool)
    present = []
    for cid, col in SUB_COLOURS.items():
        sel = s == cid
        if sel.sum() > 60:
            overlay[sel] = col; m |= sel; present.append(cid)
    blended = np.where(m[..., None], rgb * 0.5 + overlay * 0.5, rgb).astype(np.uint8)

    panels = []
    for arr, title in ((np.stack([grey] * 3, -1).astype(np.uint8), 'Raw EM — what is each profile?'),
                       (blended, 'The model\'s answer')):
        img = Image.fromarray(arr)
        d = ImageDraw.Draw(img)
        decorate(img, nm_per_px)
        d.rectangle([0, 0, npx, 30], fill=(0, 0, 0))
        d.text((8, 6), title, fill=(255, 255, 255), font=font(18))
        if title.startswith('The model'):
            f = font(16)
            labels = [SUB_NAMES[c] for c in present]
            bw = int(max(d.textlength(t, font=f) for t in labels)) + 44
            d.rectangle([6, 36, 12 + bw, 44 + len(present) * 23], fill=(0, 0, 0))
            for i, cid in enumerate(present):
                y = 40 + i * 23
                d.rectangle([12, y + 4, 28, y + 18], fill=SUB_COLOURS[cid])
                d.text((36, y + 2), SUB_NAMES[cid], fill=(255, 255, 255), font=f)
        panels.append(np.array(img))
    gap = np.full((panels[0].shape[0], 10, 3), 255, np.uint8)
    save(Image.fromarray(np.hstack([panels[0], gap, panels[1]])), out_dir,
         'neuropil-raw-vs-subcompartments.jpg')


def myelin_field(out_dir, centre, nm_per_px=32, npx=760):
    """Every myelinated axon in a grey-matter field, lit up against the rest.

    The point is the ratio: unmyelinated axons vastly outnumber myelinated ones
    in cortex, which is easy to assert and hard to believe until you see it.
    """
    mask = layer('masking', '64.0x64.0x66.0')
    grey = stretch(em(centre[0], centre[1], centre[2], nm_per_px, npx), 0.8).T
    n64 = int(npx * nm_per_px / 64)
    x0, y0 = int(centre[0] / 64) - n64 // 2, int(centre[1] / 64) - n64 // 2
    m = mask[x0:x0 + n64, y0:y0 + n64, int(centre[2] / 66), 0].read().result().T
    m = np.array(Image.fromarray(m.astype(np.int32), mode='I').resize((npx, npx), Image.NEAREST))
    sel = m == MASK_MYELIN
    rgb = np.stack([grey] * 3, -1).astype(np.float32)
    overlay = np.zeros_like(rgb); overlay[sel] = (240, 160, 60)
    blended = np.where(sel[..., None], rgb * 0.4 + overlay * 0.6, rgb).astype(np.uint8)
    img = Image.fromarray(blended)
    d = ImageDraw.Draw(img)
    pct = 100.0 * sel.mean()
    decorate(img, nm_per_px)
    note = f'myelin: {pct:.1f}% of this field'
    f = font(18); tw = d.textlength(note, font=f)
    d.rectangle([6, 6, 18 + tw, 36], fill=(0, 0, 0))
    d.text((12, 10), note, fill=(240, 160, 60), font=f)
    save(img, out_dir, 'myelin-in-grey-matter.jpg')


def merge_split_figure(out_dir, centre=(2420856, 1279360, 82269), nm_per_px=8, npx=700):
    """The c2/c3 trade-off, on a real object: find a c2 segment that c3 splits."""
    c2 = layer('c2', '8.0x8.0x33.0')
    c3 = layer('c3', '8.0x8.0x33.0')
    x0, y0 = int(centre[0] / nm_per_px) - npx // 2, int(centre[1] / nm_per_px) - npx // 2
    z = int(centre[2] / 33)
    A = c2[x0:x0 + npx, y0:y0 + npx, z, 0].read().result()
    B = c3[x0:x0 + npx, y0:y0 + npx, z, 0].read().result()
    grey = stretch(em(centre[0], centre[1], centre[2], nm_per_px, npx)).T

    # a c2 object that c3 divides into >=2 substantial parts
    pick, parts = None, []
    for sid in np.unique(A):
        if sid == 0:
            continue
        m = A == sid
        if m.sum() < 3000:
            continue
        sub = B[m]; sub = sub[sub != 0]
        if not sub.size:
            continue
        vals, counts = np.unique(sub, return_counts=True)
        order = np.argsort(-counts); vals, counts = vals[order], counts[order]
        keep = counts > max(800, 0.12 * counts.sum())
        if keep.sum() >= 2:
            pick, parts = sid, list(vals[keep])
            break
    if pick is None:
        print("  (no c2/c3 disagreement found in this field; skipping)")
        return

    # Re-centre on the disputed object and re-read: the search field is wherever
    # we happened to start, so the object is usually off to one side, and a
    # figure whose whole point is one object should have it in the middle.
    ys, xs = np.nonzero((A == pick).T)
    off_x = int((xs.mean() - npx / 2) * nm_per_px)
    off_y = int((ys.mean() - npx / 2) * nm_per_px)
    centre = (centre[0] + off_x, centre[1] + off_y, centre[2])
    x0, y0 = int(centre[0] / nm_per_px) - npx // 2, int(centre[1] / nm_per_px) - npx // 2
    A = c2[x0:x0 + npx, y0:y0 + npx, z, 0].read().result()
    B = c3[x0:x0 + npx, y0:y0 + npx, z, 0].read().result()
    grey = stretch(em(centre[0], centre[1], centre[2], nm_per_px, npx)).T

    part_cols = [(233, 90, 90), (70, 150, 235), (95, 190, 110), (240, 160, 60)]
    panels = []
    for arr, title, mode in ((A.T, 'c2 — aggressive: one object', 'single'),
                             (B.T, 'c3 — conservative: two objects', 'parts')):
        rgb = np.stack([grey] * 3, -1).astype(np.float32)
        overlay = np.zeros_like(rgb)
        if mode == 'single':
            overlay[arr == pick] = (150, 110, 225)
            m = (arr == pick)
        else:
            m = np.zeros(arr.shape, bool)
            for j, pid in enumerate(parts):
                sel = arr == pid
                overlay[sel] = part_cols[j % len(part_cols)]
                m |= sel
        blended = np.where(m[..., None], rgb * 0.42 + overlay * 0.58, rgb * 0.75).astype(np.uint8)
        img = Image.fromarray(blended)
        decorate(img, nm_per_px)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, npx, 30], fill=(0, 0, 0))
        d.text((8, 6), title, fill=(255, 255, 255), font=font(18))
        panels.append(np.array(img))
    gap = np.full((panels[0].shape[0], 8, 3), 255, np.uint8)
    save(Image.fromarray(np.hstack([panels[0], gap, panels[1]])), out_dir,
         'segmentation-c2-vs-c3.jpg')
    print(f"    (c2 segment {pick} -> {len(parts)} c3 parts)")


def subcompartment_figure(out_dir, centre, nm_per_px=32, npx=760):
    """The six-class subcompartment model over raw EM."""
    sub = layer('c2/subcompartments', '64x64x66')
    grey = stretch(em(centre[0], centre[1], centre[2], nm_per_px, npx), 0.75).T
    # subcompartments live at 64 nm; read the matching window and upsample
    n64 = int(npx * nm_per_px / 64)
    x0, y0 = int(centre[0] / 64) - n64 // 2, int(centre[1] / 64) - n64 // 2
    s = sub[x0:x0 + n64, y0:y0 + n64, int(centre[2] / 66), 0].read().result().T
    s = np.array(Image.fromarray(s.astype(np.int32), mode='I').resize((npx, npx), Image.NEAREST))

    rgb = np.stack([grey] * 3, -1).astype(np.float32)
    overlay = np.zeros_like(rgb)
    m = np.zeros(s.shape, bool)
    present = []
    for cid, col in SUB_COLOURS.items():
        sel = s == cid
        if sel.sum() > 40:
            overlay[sel] = col
            m |= sel
            present.append(cid)
    blended = np.where(m[..., None], rgb * 0.5 + overlay * 0.5, rgb).astype(np.uint8)
    img = Image.fromarray(blended)
    d = ImageDraw.Draw(img)
    f = font(17)
    labels = [SUB_NAMES[c] for c in present]
    if labels:
        bw = int(max(d.textlength(t, font=f) for t in labels)) + 44
        d.rectangle([6, 6, 12 + bw, 19 + len(present) * 25], fill=(0, 0, 0))
        for i, cid in enumerate(present):
            y = 12 + i * 25
            d.rectangle([12, y + 4, 30, y + 19], fill=SUB_COLOURS[cid])
            d.text((38, y + 2), SUB_NAMES[cid], fill=(255, 255, 255), font=f)
    decorate(img, nm_per_px)
    save(img, out_dir, 'subcompartment-classes.jpg')


def proofread_before_after(out_dir, cell_id=3955003482, centre=(2487902, 1440845, 28512),
                           nm_per_px=8, npx=820):
    """Raw EM, the automated segmentation's answer, and the proofread answer.

    H01 ships 104 manually proofread cells alongside the automated segmentation,
    so "before and after a human fixed it" is directly renderable rather than
    reconstructed. Note where the errors are NOT: at a cell body the automated
    result is essentially perfect. The corrections live out in the thin neurites,
    which is exactly why proofreading is expensive.
    """
    pf = layer('proofread_104', '8.0x8.0x33.0')
    auto = layer('c2', '8.0x8.0x33.0')
    x0, y0 = int(centre[0] / nm_per_px) - npx // 2, int(centre[1] / nm_per_px) - npx // 2
    z = int(centre[2] / 33)
    P = pf[x0:x0 + npx, y0:y0 + npx, z, 0].read().result().T
    A = auto[x0:x0 + npx, y0:y0 + npx, z, 0].read().result().T
    grey = stretch(em(centre[0], centre[1], centre[2], nm_per_px, npx)).T

    truth = P == cell_id
    if truth.sum() < 500:
        print("  (proofread cell not in this field; skipping before/after)")
        return
    sub = A[truth]; sub = sub[sub != 0]
    vals, counts = np.unique(sub, return_counts=True)
    auto_seg = vals[counts.argmax()]
    predicted = A == auto_seg
    wrong = predicted & ~truth          # merged on by the algorithm, removed by hand
    right = predicted & truth

    # Re-centre on the correction itself. The starting coordinate is the cell's
    # soma, but the interesting thing is the boundary between what the algorithm
    # claimed and what a human kept -- put that in the middle of the frame.
    if wrong.any():
        wy, wx = np.nonzero(wrong)
        ry, rx = np.nonzero(right)
        tx, ty = (wx.mean() + rx.mean()) / 2, (wy.mean() + ry.mean()) / 2
        centre = (centre[0] + int((tx - npx / 2) * nm_per_px),
                  centre[1] + int((ty - npx / 2) * nm_per_px), centre[2])
        x0 = int(centre[0] / nm_per_px) - npx // 2
        y0 = int(centre[1] / nm_per_px) - npx // 2
        P = pf[x0:x0 + npx, y0:y0 + npx, z, 0].read().result().T
        A = auto[x0:x0 + npx, y0:y0 + npx, z, 0].read().result().T
        grey = stretch(em(centre[0], centre[1], centre[2], nm_per_px, npx)).T
        truth = P == cell_id
        predicted = A == auto_seg
        wrong = predicted & ~truth
        right = predicted & truth

    GREEN, RED = (95, 190, 110), (233, 90, 90)
    panels = []

    def compose(mask_colour_pairs, title):
        rgb = np.stack([grey] * 3, -1).astype(np.float32)
        overlay = np.zeros_like(rgb)
        any_m = np.zeros(grey.shape, bool)
        for msk, col in mask_colour_pairs:
            overlay[msk] = col
            any_m |= msk
        out = np.where(any_m[..., None], rgb * 0.45 + overlay * 0.55, rgb).astype(np.uint8)
        img = Image.fromarray(out)
        d = ImageDraw.Draw(img)
        decorate(img, nm_per_px)
        d.rectangle([0, 0, npx, 34], fill=(0, 0, 0))
        d.text((10, 8), title, fill=(255, 255, 255), font=font(20))
        return np.array(img)

    panels.append(compose([], 'Raw EM'))
    panels.append(compose([(right, GREEN), (wrong, RED)],
                          'Automated — one object'))
    panels.append(compose([(truth, GREEN)], 'After proofreading'))

    gap = np.full((panels[0].shape[0], 10, 3), 255, np.uint8)
    strip = Image.fromarray(np.hstack([panels[0], gap, panels[1], gap, panels[2]]))
    d = ImageDraw.Draw(strip)
    note = f'red = {wrong.sum():,} voxels the algorithm merged on; a human removed them'
    f = font(19)
    tw = d.textlength(note, font=f)
    d.rectangle([strip.width // 2 - tw // 2 - 12, strip.height - 40,
                 strip.width // 2 + tw // 2 + 12, strip.height - 8], fill=(0, 0, 0))
    d.text((strip.width // 2 - tw // 2, strip.height - 36), note, fill=RED, font=f)
    save(strip, out_dir, 'proofreading-before-after.jpg')
    print(f"    (cell {cell_id}; automated segment {auto_seg}; "
          f"{wrong.sum()} merged-on voxels)")


def main():
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"rendering EM figures into {out_dir}")

    anchor = (2433280, 1292800, 84480)
    print("  locating structures from the dataset's own labels...")
    found = find_structures(anchor)
    print("   ", ", ".join(sorted(found)))
    (out_dir / 'structure-coordinates.json').write_text(json.dumps(found, indent=1))

    plain = [
        ('myelinated_axon', 4, 620, 'myelinated-axon.jpg'),
        ('astrocyte', 8, 620, 'astrocyte-process.jpg'),
        ('blood_vessel', 32, 620, 'blood-vessel.jpg'),
        ('soma', 16, 760, 'soma-ultrastructure.jpg'),
        ('dendrite', 4, 620, 'dendrite-and-organelles.jpg'),
    ]
    for key, nmpp, npx, fname in plain:
        if key not in found:
            print(f"  ({key} not found; skipping {fname})")
            continue
        c = found[key]
        img = Image.fromarray(stretch(em(c[0], c[1], c[2], nmpp, npx)).T).convert('RGB')
        save(decorate(img, nmpp, f'{nmpp} nm/px'), out_dir, fname)

    synapse_pair(out_dir)
    subcompartment_figure(out_dir, found.get('soma', anchor))
    raw_vs_overlay(out_dir, found.get('dendrite', anchor))
    myelin_field(out_dir, found.get('myelin', anchor))
    merge_split_figure(out_dir)
    proofread_before_after(out_dir)
    print("done")


if __name__ == '__main__':
    main()
