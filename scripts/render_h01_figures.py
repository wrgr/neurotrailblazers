#!/usr/bin/env python3
"""Regenerate the figures for /content-library/case-studies/h01-pipeline/.

Every EM figure on that page is rendered here directly from the public H01
volume -- nothing is copied from a publication. The same approach works on any
Neuroglancer `precomputed` dataset (MICrONS, FlyWire, ...), which is half the
point of keeping this script in the repo: it is a worked example, not just a
build step.

Data: the H01 release from the Lichtman Laboratory (Harvard) and the
Connectomics at Google team. Cite Shapson-Coe, A. et al., "A petavoxel fragment
of human cerebral cortex reconstructed at nanoscale resolution," Science 384,
eadk4858 (2024). doi:10.1126/science.adk4858
Check https://h01-release.storage.googleapis.com/landing.html for current terms
before reusing the output.

Requires:  pip install tensorstore pillow numpy

Usage:     python3 scripts/render_h01_figures.py [output_dir]
           (default output dir: assets/images/content-library/case-studies/h01)
"""

import os
import struct
import sys
import urllib.request
from pathlib import Path

import numpy as np
import tensorstore as ts
from PIL import Image, ImageDraw, ImageFont

BASE = 'https://storage.googleapis.com/h01-release/data/20210601/'
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO_ROOT / 'assets' / 'images' / 'content-library' / 'case-studies' / 'h01'

N = 900  # standard figure edge, px

# Anchors, in nanometres, chosen once by surveying the volume (see the page).
SOMA = (2433280, 1292800, 84480)   # a neuronal cell body with a clear nucleolus
SYN_E = (2420856, 1279360, 82269)  # released excitatory synapse, id 43323838
SYN_I = (2451264, 1270712, 82599)  # released inhibitory synapse, id 132910682

# (nm/px in x&y, nm/px in z, precomputed scale key) for the raw EM layer.
SCALES = [
    (4, 33, '4.0x4.0x33.0'), (8, 33, '8.0x8.0x33.0'), (16, 33, '16.0x16.0x33.0'),
    (32, 33, '32.0x32.0x33.0'), (64, 66, '64.0x64.0x66.0'),
    (128, 132, '128.0x128.0x132.0_hp_q60'), (256, 264, '256.0x256.0x264.0_hp_q60'),
    (512, 528, '512.0x512.0x528.0_hp_q60'), (1024, 1056, '1024.0x1024.0x1056.0_hp_q60'),
    (2048, 2112, '2048.0x2048.0x2112.0_hp_q60'), (4096, 4224, '4096.0x4096.0x4224.0_hp_q60'),
    (8192, 8448, '8192.0x8192.0x8448.0_hp_q60'), (16384, 16896, '16384.0x16384.0x16896.0_hp_q60'),
]
KEY = {s[0]: s for s in SCALES}
_cache = {}


def vol(nm_per_px, layer='4nm_raw', key=None):
    ck = (nm_per_px, layer, key)
    if ck not in _cache:
        _cache[ck] = ts.open({
            'driver': 'neuroglancer_precomputed',
            'kvstore': {'driver': 'http', 'base_url': BASE + layer + '/'},
            'scale_metadata': {'key': key or KEY[nm_per_px][2]},
        }).result()
    return _cache[ck]


def read_nm(cx, cy, cz, nm_per_px, npx, layer='4nm_raw', key=None, z_res=None):
    """Read an npx x npx window centred on physical (cx, cy, cz) in nanometres."""
    d = vol(nm_per_px, layer, key)
    zr = z_res or KEY[nm_per_px][1]
    x0, y0 = int(cx / nm_per_px) - npx // 2, int(cy / nm_per_px) - npx // 2
    sx, sy, sz = d.domain.shape[0], d.domain.shape[1], d.domain.shape[2]
    x0 = max(0, min(x0, sx - npx))
    y0 = max(0, min(y0, sy - npx))
    z = max(0, min(int(cz / zr), sz - 1))
    return d[x0:x0 + npx, y0:y0 + npx, z, 0].read().result()


def font(size):
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
              '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def stretch(a, gamma):
    """Contrast-stretch over TISSUE pixels only, then gamma-correct.

    Sections sit in bright empty resin. Including that background in the
    percentiles drags the upper percentile up and crushes the tissue to black,
    so it is masked out first. The gamma then lifts midtones, because the
    neuropil occupies a narrow dark band while cell bodies and vessels form a
    long bright tail -- without it the neuropil reads as featureless black.
    """
    a = a.astype(np.float32)
    bg = a >= 235
    sample = a[~bg] if (bg.mean() > 0.02 and (~bg).sum() > 1000) else a
    p1, p2 = np.percentile(sample, 1), np.percentile(sample, 99)
    if p2 <= p1:
        return np.clip(a, 0, 255).astype(np.uint8)
    return (np.power(np.clip((a - p1) / (p2 - p1), 0, 1), gamma) * 255).astype(np.uint8)


def _bar_len(nm_per_px, npx):
    target = nm_per_px * npx * 0.22
    for v in (100, 200, 500, 1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6, 2e6):
        if v >= target:
            return v
    return 2e6


def _bar_label(nm):
    if nm >= 1e6:
        return f"{nm / 1e6:g} mm"
    if nm >= 1e3:
        return f"{nm / 1e3:g} µm"
    return f"{nm:g} nm"


def decorate(img, nm_per_px, note=''):
    d = ImageDraw.Draw(img)
    w, h = img.size
    length = _bar_len(nm_per_px, w)
    px = length / nm_per_px
    x0, y0 = int(w * 0.05), int(h * 0.94)
    d.rectangle([x0 - 8, y0 - 32, x0 + px + 8, y0 + 14], fill=(0, 0, 0))
    d.rectangle([x0, y0, x0 + px, y0 + 6], fill=(255, 255, 255))
    d.text((x0, y0 - 28), _bar_label(length), fill=(255, 255, 255), font=font(21))
    if note:
        f = font(19)
        tw = d.textlength(note, font=f)
        d.rectangle([w - tw - 20, 8, w - 6, 38], fill=(0, 0, 0))
        d.text((w - tw - 14, 12), note, fill=(255, 255, 255), font=f)
    return img


def em_image(centre, nm_per_px, npx=N):
    gamma = 0.55 if nm_per_px >= 128 else 0.9
    return Image.fromarray(stretch(read_nm(*centre, nm_per_px, npx), gamma).T).convert('RGB')


def save(img, out_dir, name, quality=86):
    path = Path(out_dir) / name
    img.save(path, quality=quality, optimize=True)
    print(f"  {name:32s} {str(img.size):12s} {path.stat().st_size // 1024:>4} KB")


def load_synapses():
    """The spatial0 index holds a volume-wide sample of synapse annotations.

    Neuroglancer 'multiple annotation encoding': a uint64 count, then per
    annotation the geometry (LINE = 6 float32: pre xyz, post xyz) plus its
    properties (here one uint32 excitatory/inhibitory enum), then the ids.
    Coordinates are in the annotation layer's own 8 x 8 x 33 nm units.
    """
    url = BASE + 'c2/synapses/precomputed/spatial0/0_0_0'
    with urllib.request.urlopen(url, timeout=120) as r:
        b = r.read()
    count = struct.unpack('<Q', b[:8])[0]
    rec = np.frombuffer(b, dtype='<f4', count=count * 7, offset=8).reshape(count, 7)
    typ = np.frombuffer(b, dtype='<u4', count=count * 7, offset=8).reshape(count, 7)[:, 6]
    ids = np.frombuffer(b, dtype='<u8', count=count, offset=8 + count * 28)
    return rec[:, :6], typ, ids


def synapse_panel(centre, syn_id, out_dir, name, note):
    """4 nm EM centred on a released synapse, with the dataset's own annotation."""
    pts, typ, ids = load_synapses()
    npx, nm_per_px = 560, 4
    img = em_image(centre, nm_per_px, npx)
    d = ImageDraw.Draw(img)
    i = int(np.where(ids == syn_id)[0][0])
    pre = (pts[i, 0] * 8, pts[i, 1] * 8)
    post = (pts[i, 3] * 8, pts[i, 4] * 8)
    to_px = lambda p: (npx / 2 + (p[0] - centre[0]) / nm_per_px,
                       npx / 2 + (p[1] - centre[1]) / nm_per_px)
    a, b_ = to_px(pre), to_px(post)
    colour = (255, 90, 90) if typ[i] == 2 else (90, 170, 255)  # 2 = excitatory
    d.line([a, b_], fill=colour, width=3)
    for p in (a, b_):
        d.ellipse([p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7], outline=colour, width=3)
    save(decorate(img, nm_per_px, note), out_dir, name)


def cortical_layers(out_dir, z_nm=84480):
    """H01's released L1-L6 + white-matter segmentation over the EM.

    The layer volume is 1000 nm/px and the nearest EM level is 1024 nm/px, but
    both cover the same physical extent from the same origin, so resampling
    each to a common output width aligns them.
    """
    lay = vol(None, 'layers', key='1000.0x1000.0x528.0')
    em = vol(1024)
    layer_slice = lay[:, :, int(z_nm / 528), 0].read().result()
    em_slice = em[:, :, int(z_nm / 1056), 0].read().result()

    w = 900
    h = int(w * layer_slice.shape[1] / layer_slice.shape[0])
    em_img = Image.fromarray(stretch(em_slice, 0.55).T).resize((w, h), Image.LANCZOS)
    lay_img = Image.fromarray(layer_slice.T.astype(np.uint8)).resize((w, h), Image.NEAREST)
    lay_arr = np.array(lay_img)

    names = {1: 'L1', 2: 'L2', 3: 'L3', 4: 'L4', 5: 'L5', 6: 'L6', 7: 'WM'}
    cols = {1: (233, 90, 90), 2: (240, 160, 60), 3: (238, 214, 70), 4: (95, 190, 110),
            5: (70, 150, 235), 6: (150, 110, 225), 7: (140, 140, 150)}
    rgb = np.stack([np.array(em_img)] * 3, -1).astype(np.float32)
    colour = np.zeros_like(rgb)
    for k, c in cols.items():
        colour[lay_arr == k] = c
    blended = np.where((lay_arr > 0)[..., None], rgb * 0.55 + colour * 0.45, rgb).astype(np.uint8)

    img = Image.fromarray(blended)
    d = ImageDraw.Draw(img)
    f = font(17)
    labels = {k: (f"{n} — white matter" if k == 7 else f"{n} — cortical layer {k}")
              for k, n in names.items()}
    box_w = int(max(d.textlength(t, font=f) for t in labels.values())) + 40
    d.rectangle([6, 6, 12 + box_w, 19 + len(names) * 26], fill=(0, 0, 0))
    for i, k in enumerate(names):
        y = 12 + i * 26
        d.rectangle([12, y + 4, 30, y + 20], fill=cols[k])
        d.text((38, y + 2), labels[k], fill=(255, 255, 255), font=f)

    nm_per_px = layer_slice.shape[0] * 1000 / w
    decorate(img, nm_per_px)
    save(img, out_dir, '11-cortical-layers.jpg', quality=88)


def segmentation_pair(out_dir, centre=SYN_E, nm_per_px=8, npx=800):
    raw = vol(nm_per_px)
    seg = vol(nm_per_px, 'c2')
    x0, y0 = int(centre[0] / nm_per_px) - npx // 2, int(centre[1] / nm_per_px) - npx // 2
    z = int(centre[2] / 33)
    e = raw[x0:x0 + npx, y0:y0 + npx, z, 0].read().result()
    s = seg[x0:x0 + npx, y0:y0 + npx, z, 0].read().result()

    grey = stretch(e, 0.9).T
    save(decorate(Image.fromarray(grey).convert('RGB'), nm_per_px, 'raw EM  ·  8 nm/px'),
         out_dir, '10a-raw-em.jpg')

    seg_t = s.T
    rgb = np.stack([grey] * 3, -1).astype(np.float32)
    rng = np.random.default_rng(7)  # fixed seed so colours are stable across runs
    colour = np.zeros_like(rgb)
    for sid in np.unique(seg_t):
        if sid:
            colour[seg_t == sid] = rng.integers(60, 255, 3)
    blended = np.where((seg_t != 0)[..., None], rgb * 0.45 + colour * 0.55, rgb).astype(np.uint8)
    print(f"    ({len(np.unique(seg_t)) - 1} segments in this view)")
    save(decorate(Image.fromarray(blended), nm_per_px, 'FFN segmentation overlay'),
         out_dir, '10b-segmentation-overlay.jpg')


def main():
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"rendering H01 figures into {out_dir}")

    # 1. whole sample: one full section, not a crop
    d = vol(8192)
    a = d[:, :, 5, 0].read().result()
    img = Image.fromarray(stretch(a, 0.55).T).convert('RGB')
    img = img.resize((img.width * 3, img.height * 3), Image.LANCZOS)
    save(decorate(img, 8192 / 3, 'one 33 nm section'), out_dir, '01-whole-sample.jpg')

    # 2-7. the zoom ladder, each step ~4x closer
    for nm_per_px, name, centre, note in (
        (2048, '02-cortical-span', SOMA, '2048 nm/px'),
        (512, '03-cell-field', SOMA, '512 nm/px'),
        (128, '04-local-circuit', SOMA, '128 nm/px'),
        (32, '05-neuron-soma', SOMA, '32 nm/px'),
        (8, '06-neuropil', SYN_E, '8 nm/px'),
        (4, '07-synapse-level', SYN_E, '4 nm/px — full resolution'),
    ):
        save(decorate(em_image(centre, nm_per_px), nm_per_px, note), out_dir, name + '.jpg')

    # 8-9. released synapse annotations drawn on the EM they came from
    synapse_panel(SYN_E, 43323838, out_dir, '08-synapse-excitatory.jpg',
                  'excitatory · id 43323838')
    synapse_panel(SYN_I, 132910682, out_dir, '09-synapse-inhibitory.jpg',
                  'inhibitory · id 132910682')

    # 10. raw vs automated segmentation, same field
    segmentation_pair(out_dir)

    # 11. cortical layers
    cortical_layers(out_dir)
    print("done")


if __name__ == '__main__':
    main()
