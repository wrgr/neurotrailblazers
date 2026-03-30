#!/usr/bin/env python3
"""
Step 7: Generate an interactive evolution-of-research timeline.

Shows:
  - Papers per year per community (stacked area chart)
  - Key milestone papers annotated on the timeline
  - Cross-community citation flows by decade (chord diagram)
  - Technique family emergence dates
  - Author career arcs for top researchers

Output: output/evolution_graph.html (standalone, no server needed)

Usage:
  python 07_evolution_graph.py
"""
import json
from collections import defaultdict
from pathlib import Path

from config import OUTPUT_DIR, TECHNIQUE_FAMILIES

# Which communities to show (filter noise)
NOISE_LABELS = {
    "geology", "seismology", "chromatography", "mass spectrometry",
    "apoptosis", "autophagy", "biochemistry",
}

# Milestone papers to annotate (openalex_id or doi → label)
MILESTONE_DOIS = {
    "10.1016/j.cub.2004.12.001":    "Denk SBEM (2004)",
    "10.1038/nature09802":           "Bock: physiology+EM (2011)",
    "10.1038/nn.2868":               "Briggman retina (2011)",
    "10.1038/nature12346":           "Kasthuri cortex (2015)",
    "10.1016/j.cell.2018.06.019":   "FAFB (2018)",
    "10.1038/s41592-018-0049-4":    "Flood-filling nets (2018)",
    "10.7554/eLife.57443":           "Hemibrain (2020)",
    "10.1126/science.add9330":      "Larval Drosophila (2023)",
    "10.1038/s41586-024-07558-y":   "FlyWire (2024)",
    "10.1126/science.adk4858":      "H01 human (2024)",
    "10.1038/s41592-024-02426-z":   "CAVE infra (2024)",
    "10.1371/journal.pcbi.0010042": "Sporns connectome (2005)",
    "10.1038/nmeth.4331":            "webKnossos (2017)",
    "10.1093/bioinformatics/btp266": "CATMAID (2009)",
}

COMMUNITY_COLORS = [
    "#4e79a7","#f28e2b","#e15759","#76b7b2","#59a14f",
    "#edc948","#b07aa1","#ff9da7","#9c755f","#bab0ac",
    "#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd",
    "#8c564b","#e377c2","#7f7f7f","#bcbd22","#17becf",
]


def load_data():
    def load(f):
        with open(OUTPUT_DIR / f) as fh:
            return json.load(fh)
    return load("communities.json"), load("corpus_merged.json"), load("paper_rankings.json")


def label_community(community):
    top = [c["name"].lower() for c in community.get("top_concepts", [])[:3]]
    is_noise = any(noise in " ".join(top) for noise in NOISE_LABELS)
    label = " / ".join(c["name"] for c in community.get("top_concepts", [])[:2])
    top_authors = [a["name"].split()[-1] for a in community.get("top_authors", [])[:2]]
    return label, top_authors, is_noise


def build_timeline_data(communities, corpus):
    """Build year × community paper counts and milestone annotations."""
    paper_to_community = {}
    community_meta = {}

    for c in communities:
        cid = c["community_id"]
        label, authors, is_noise = label_community(c)
        community_meta[cid] = {
            "id": cid,
            "label": label,
            "authors": authors,
            "size": c["size"],
            "is_noise": is_noise,
            "color": COMMUNITY_COLORS[cid % len(COMMUNITY_COLORS)],
        }
        for pid in c.get("members", []):
            paper_to_community[pid] = cid

    # Filter to non-noise communities
    valid_communities = {
        cid: m for cid, m in community_meta.items() if not m["is_noise"]
    }

    # Year × community counts
    year_community = defaultdict(lambda: defaultdict(int))
    paper_details = {}  # pid → {year, cid, title, doi, citations}

    doi_to_pid = {}
    for paper in corpus:
        pid = paper.get("openalex_id", "")
        doi = (paper.get("doi") or "").lower()
        year = paper.get("year")
        cid = paper_to_community.get(pid)

        if doi:
            doi_to_pid[doi] = pid

        if year and 2000 <= year <= 2026 and cid in valid_communities:
            year_community[year][cid] += 1
            paper_details[pid] = {
                "pid": pid,
                "title": paper.get("title", ""),
                "doi": doi,
                "year": year,
                "community": cid,
                "citations": paper.get("cited_by_count", 0),
            }

    # Technique family first-appearance years
    technique_first = {}
    for paper in sorted(corpus, key=lambda x: x.get("year") or 9999):
        title = (paper.get("title") or "").lower()
        year = paper.get("year")
        if not year:
            continue
        for family, keywords in TECHNIQUE_FAMILIES.items():
            if family not in technique_first:
                if any(kw.lower() in title for kw in keywords):
                    technique_first[family] = year

    # Milestone annotations
    milestones = []
    for doi, label in MILESTONE_DOIS.items():
        pid = doi_to_pid.get(doi.lower())
        if pid and pid in paper_details:
            d = paper_details[pid]
            milestones.append({
                "year": d["year"],
                "label": label,
                "doi": doi,
                "citations": d["citations"],
                "community": d["community"],
                "community_label": valid_communities.get(d["community"], {}).get("label", ""),
            })
        else:
            # Find by scanning corpus
            for paper in corpus:
                pdoi = (paper.get("doi") or "").lower()
                if pdoi == doi.lower() and paper.get("year"):
                    cid = paper_to_community.get(paper.get("openalex_id", ""), -1)
                    milestones.append({
                        "year": paper["year"],
                        "label": label,
                        "doi": doi,
                        "citations": paper.get("cited_by_count", 0),
                        "community": cid,
                        "community_label": valid_communities.get(cid, {}).get("label", ""),
                    })
                    break

    milestones.sort(key=lambda x: x["year"])

    # Build year series
    all_years = list(range(2000, 2026))
    valid_cids = sorted(valid_communities.keys(),
                        key=lambda c: -valid_communities[c]["size"])[:12]  # top 12

    series = []
    for cid in valid_cids:
        meta = valid_communities[cid]
        values = [year_community[y][cid] for y in all_years]
        series.append({
            "community_id": cid,
            "label": meta["label"],
            "authors": meta["authors"],
            "color": meta["color"],
            "values": values,
            "total": sum(values),
        })

    return {
        "years": all_years,
        "series": series,
        "milestones": milestones,
        "technique_first": technique_first,
        "community_meta": {k: v for k, v in valid_communities.items() if k in valid_cids},
    }


def generate_html(data):
    data_json = json.dumps(data)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>EM Connectomics — Research Evolution</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background:#0a0a1a; color:#e0e0e0; padding:20px; }}
h1 {{ color:#8888ff; font-size:22px; margin-bottom:4px; }}
.subtitle {{ color:#888; font-size:13px; margin-bottom:20px; }}
.panel {{ background:#111128; border:1px solid #2a2a4a; border-radius:6px;
          padding:16px; margin-bottom:16px; }}
h2 {{ color:#aaaadd; font-size:15px; margin-bottom:12px; }}
.legend {{ display:flex; flex-wrap:wrap; gap:8px; margin-bottom:12px; font-size:11px; }}
.legend-item {{ display:flex; align-items:center; gap:5px; cursor:pointer; padding:3px 6px;
                border-radius:3px; border:1px solid transparent; }}
.legend-item:hover {{ border-color:#444; }}
.legend-dot {{ width:10px; height:10px; border-radius:50%; flex-shrink:0; }}
svg text {{ font-family: -apple-system, sans-serif; }}
.tooltip {{ position:fixed; background:#1a1a3a; border:1px solid #4a4a7a;
            padding:8px 12px; border-radius:4px; font-size:12px;
            pointer-events:none; display:none; max-width:320px; z-index:100; }}
.milestone-label {{ font-size:10px; fill:#ffcc44; }}
.axis text {{ fill:#888; font-size:11px; }}
.axis line, .axis path {{ stroke:#333; }}
.grid line {{ stroke:#1a1a3a; stroke-dasharray:2,3; }}
.technique-badge {{ display:inline-block; background:#1a2a3a; border:1px solid #2a4a6a;
                    padding:2px 8px; border-radius:10px; font-size:11px; margin:2px; }}
.technique-year {{ color:#88aaff; font-weight:600; }}
#controls {{ margin-bottom:10px; }}
button {{ background:#2a2a5a; color:#ccccff; border:1px solid #4a4a7a;
          padding:5px 12px; border-radius:4px; cursor:pointer; margin:2px; font-size:12px; }}
button:hover {{ background:#3a3a7a; }}
button.active {{ background:#4a4aaa; }}
</style>
</head>
<body>
<h1>EM Connectomics — Evolution of Research (2000–2025)</h1>
<p class="subtitle">Data-driven bibliometric analysis · 7,925 papers · OpenAlex</p>

<div class="panel">
  <h2>Research Communities Over Time</h2>
  <div id="controls">
    <button class="active" onclick="setMode('stacked')">Stacked</button>
    <button onclick="setMode('stream')">Streamgraph</button>
    <button onclick="setMode('lines')">Lines</button>
  </div>
  <div class="legend" id="legend"></div>
  <svg id="area-chart" width="100%" height="380"></svg>
</div>

<div class="panel">
  <h2>Technique Family First Appearance</h2>
  <div id="technique-timeline"></div>
</div>

<div class="panel">
  <h2>Milestone Papers Timeline</h2>
  <svg id="milestone-chart" width="100%" height="180"></svg>
</div>

<div class="tooltip" id="tooltip"></div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
const DATA = {data_json};
const years = DATA.years;
const series = DATA.series;
const milestones = DATA.milestones;
const techniqeFirst = DATA.technique_first;

// Colour visible/hidden state
const hidden = new Set();
let mode = 'stacked';

// ── Legend ────────────────────────────────────────────────────────────
const legend = document.getElementById('legend');
series.forEach(s => {{
  const el = document.createElement('div');
  el.className = 'legend-item';
  el.id = 'leg-' + s.community_id;
  el.innerHTML = `<div class="legend-dot" style="background:${{s.color}}"></div>
    <span>${{s.label}} <span style="color:#888">(${{s.total}})</span></span>`;
  el.onclick = () => toggleSeries(s.community_id);
  legend.appendChild(el);
}});

function toggleSeries(cid) {{
  if (hidden.has(cid)) {{ hidden.delete(cid); }}
  else {{ hidden.add(cid); }}
  document.getElementById('leg-' + cid).style.opacity = hidden.has(cid) ? 0.3 : 1;
  drawAreaChart();
}}

function setMode(m) {{
  mode = m;
  document.querySelectorAll('#controls button').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
  drawAreaChart();
}}

// ── Stacked area chart ────────────────────────────────────────────────
function drawAreaChart() {{
  const svgEl = document.getElementById('area-chart');
  const W = svgEl.clientWidth || 900;
  const H = 380;
  const margin = {{top:20, right:20, bottom:40, left:55}};
  const w = W - margin.left - margin.right;
  const h = H - margin.top - margin.bottom;

  const svg = d3.select('#area-chart');
  svg.attr('height', H).selectAll('*').remove();
  const g = svg.append('g').attr('transform', `translate(${{margin.left}},${{margin.top}})`);

  const visibleSeries = series.filter(s => !hidden.has(s.community_id));
  const keys = visibleSeries.map(s => s.community_id);
  const colorMap = Object.fromEntries(series.map(s => [s.community_id, s.color]));
  const labelMap = Object.fromEntries(series.map(s => [s.community_id, s.label]));

  const rowData = years.map((yr, i) => {{
    const row = {{year: yr}};
    visibleSeries.forEach(s => {{ row[s.community_id] = s.values[i]; }});
    return row;
  }});

  const stack = d3.stack()
    .keys(keys)
    .offset(mode === 'stream' ? d3.stackOffsetWiggle : d3.stackOffsetNone);

  const stacked = stack(rowData);

  const x = d3.scaleLinear().domain(d3.extent(years)).range([0, w]);
  const yExt = [
    d3.min(stacked, layer => d3.min(layer, d => d[0])),
    d3.max(stacked, layer => d3.max(layer, d => d[1]))
  ];
  const y = d3.scaleLinear().domain(yExt).nice().range([h, 0]);

  // Grid
  g.append('g').attr('class','grid')
    .call(d3.axisLeft(y).tickSize(-w).tickFormat(''))
    .select('.domain').remove();

  const area = d3.area()
    .x((d,i) => x(years[i]))
    .y0(d => y(d[0]))
    .y1(d => y(d[1]))
    .curve(d3.curveCatmullRom);

  g.selectAll('.area')
    .data(stacked)
    .join('path')
    .attr('class','area')
    .attr('fill', d => colorMap[d.key] + 'cc')
    .attr('stroke', d => colorMap[d.key])
    .attr('stroke-width', 0.5)
    .attr('d', area)
    .on('mouseover', (e,d) => {{
      const yr = Math.round(x.invert(d3.pointer(e,g.node())[0]));
      const idx = years.indexOf(yr);
      const val = idx >= 0 ? d[idx][1] - d[idx][0] : '?';
      showTip(e, `<strong>${{labelMap[d.key]}}</strong><br>Year: ${{yr}}<br>Papers: ${{val}}`);
    }})
    .on('mousemove', e => moveTip(e))
    .on('mouseout', hideTip);

  // Milestone lines
  milestones.forEach(m => {{
    const mx = x(m.year);
    if (mx < 0 || mx > w) return;
    g.append('line')
      .attr('x1', mx).attr('x2', mx).attr('y1', 0).attr('y2', h)
      .attr('stroke', '#ffcc44').attr('stroke-width', 1)
      .attr('stroke-dasharray', '3,3').attr('opacity', 0.6);
    g.append('text')
      .attr('class','milestone-label')
      .attr('x', mx + 3).attr('y', 10)
      .attr('transform', `rotate(90,${{mx+3}},10)`)
      .text(m.label);
  }});

  // Axes
  g.append('g').attr('class','axis').attr('transform',`translate(0,${{h}})`)
    .call(d3.axisBottom(x).tickFormat(d3.format('d')));
  g.append('g').attr('class','axis').call(d3.axisLeft(y).ticks(6));
  g.append('text').attr('x', w/2).attr('y', h+35)
    .attr('text-anchor','middle').attr('fill','#666').attr('font-size',11)
    .text('Year');
  g.append('text').attr('transform','rotate(-90)')
    .attr('x',-h/2).attr('y',-42)
    .attr('text-anchor','middle').attr('fill','#666').attr('font-size',11)
    .text('Papers per year');
}}

// ── Technique timeline ────────────────────────────────────────────────
(function() {{
  const container = document.getElementById('technique-timeline');
  const techniqueNames = {{
    volume_em: 'Volume EM (SEM/TEM/FIB-SEM)',
    atum_gridtape: 'ATUM / GridTape',
    barcoding: 'Barcoding (MAPseq/BARseq)',
    expansion_microscopy: 'Expansion Microscopy',
    xray: 'X-ray Nanotomography',
    array_tomography: 'Array Tomography',
    graph_theory: 'Graph Theory / Networks',
  }};
  let html = '';
  Object.entries(techniqeFirst)
    .sort((a,b) => a[1] - b[1])
    .forEach(([key, year]) => {{
      html += `<span class="technique-badge">
        ${{techniqueNames[key] || key}}: <span class="technique-year">${{year}}</span>
      </span>`;
    }});
  container.innerHTML = html;
}})();

// ── Milestone bubble chart ────────────────────────────────────────────
(function() {{
  const svgEl = document.getElementById('milestone-chart');
  const W = svgEl.clientWidth || 900;
  const H = 180;
  const margin = {{top:30, right:20, bottom:35, left:20}};
  const w = W - margin.left - margin.right;
  const h = H - margin.top - margin.bottom;

  const svg = d3.select('#milestone-chart').attr('height', H);
  svg.selectAll('*').remove();
  const g = svg.append('g').attr('transform', `translate(${{margin.left}},${{margin.top}})`);

  const x = d3.scaleLinear().domain([2000, 2025]).range([0, w]);
  const r = d3.scaleSqrt()
    .domain([0, d3.max(milestones, d => d.citations)])
    .range([4, 20]);

  const colorMap = Object.fromEntries(series.map(s => [s.community_id, s.color]));

  // Grid years
  g.append('g').attr('class','axis').attr('transform',`translate(0,${{h/2+10}})`)
    .call(d3.axisBottom(x).tickFormat(d3.format('d')).ticks(10))
    .select('.domain').attr('stroke','#333');

  g.append('line').attr('x1',0).attr('x2',w).attr('y1',h/2).attr('y2',h/2)
    .attr('stroke','#2a2a4a').attr('stroke-width',1);

  // Place bubbles with simple collision avoidance (alternate above/below)
  const sorted = [...milestones].sort((a,b)=>a.year-b.year);
  sorted.forEach((m, i) => {{
    const cx = x(m.year);
    const above = i % 2 === 0;
    const cy = above ? h/2 - r(m.citations) - 8 : h/2 + r(m.citations) + 8;
    const color = colorMap[m.community] || '#8888ff';

    g.append('line')
      .attr('x1',cx).attr('x2',cx)
      .attr('y1',h/2).attr('y2',cy)
      .attr('stroke',color).attr('stroke-width',1).attr('opacity',0.5);

    g.append('circle')
      .attr('cx',cx).attr('cy',cy).attr('r',r(m.citations))
      .attr('fill',color+'88').attr('stroke',color).attr('stroke-width',1)
      .style('cursor','pointer')
      .on('mouseover', e => showTip(e,
        `<strong>${{m.label}}</strong><br>Year: ${{m.year}}<br>Citations: ${{m.citations.toLocaleString()}}<br>${{m.community_label}}`
      ))
      .on('mousemove', e => moveTip(e))
      .on('mouseout', hideTip);

    // label
    const labelY = above ? cy - r(m.citations) - 4 : cy + r(m.citations) + 11;
    g.append('text')
      .attr('x', cx).attr('y', labelY)
      .attr('text-anchor','middle')
      .attr('font-size', 9).attr('fill','#aaa')
      .text(m.label.split('(')[0].trim());
  }});
}})();

// ── Tooltip helpers ───────────────────────────────────────────────────
const tip = document.getElementById('tooltip');
function showTip(e, html) {{ tip.style.display='block'; tip.innerHTML=html; moveTip(e); }}
function moveTip(e) {{ tip.style.left=(e.clientX+12)+'px'; tip.style.top=(e.clientY-10)+'px'; }}
function hideTip() {{ tip.style.display='none'; }}

// Initial render
drawAreaChart();
window.addEventListener('resize', drawAreaChart);
</script>
</body>
</html>"""


def main():
    print("Loading data...")
    communities, corpus, rankings = load_data()

    print("Building timeline data...")
    data = build_timeline_data(communities, corpus)

    print(f"  {len(data['series'])} communities")
    print(f"  {len(data['milestones'])} milestones found")
    print(f"  Technique first appearances:")
    for tech, year in sorted(data["technique_first"].items(), key=lambda x: x[1]):
        print(f"    {tech}: {year}")

    print("Generating HTML...")
    html = generate_html(data)
    out_path = OUTPUT_DIR / "evolution_graph.html"
    with open(out_path, "w") as f:
        f.write(html)
    print(f"Saved → {out_path}")
    print("Done. Open evolution_graph.html in a browser.")


if __name__ == "__main__":
    main()
