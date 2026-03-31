#!/usr/bin/env python3
"""
K-Core Decomposition Visualization.

Creates D3.js interactive visualization showing:
- Citation network colored by k-core shell (innermost to outermost)
- K-core shells as concentric regions
- Emphasis on EM connectomics zone (k=25–30)
- Interactive filtering by k-core range

This complements field_map.html with structural topology view.

Usage:
    python 06b_kcore_visualization.py

Output:
    output/kcore_map.html  (~3 MB)
"""
import json
from pathlib import Path
import networkx as nx
from networkx.readwrite import json_graph

OUT = Path("output")


def create_kcore_visualization():
    """Generate k-core visualization HTML."""

    print("Loading citation graph...")
    with open(OUT / "graphs" / "citation_graph.json") as f:
        graph_data = json.load(f)
    graph = json_graph.node_link_graph(graph_data, directed=True)

    print("Loading enriched reading list with k-core data...")
    with open(OUT / "reading_list_enriched.json") as f:
        enriched = json.load(f)

    kcore_lookup = {p['openalex_id']: p.get('core_number', 0) for p in enriched}

    # Group papers by k-core shell
    kcore_groups = {}
    for node_id, node_data in graph.nodes(data=True):
        paper_id = node_data.get('id')
        kcore = kcore_lookup.get(paper_id, 0)
        if kcore not in kcore_groups:
            kcore_groups[kcore] = []
        kcore_groups[kcore].append({
            'id': node_id,
            'title': node_data.get('title', ''),
            'kcore': kcore,
            'year': node_data.get('year', 0),
        })

    # Color scheme: k-core shells
    # k=32 (innermost) -> red
    # k=25–29 (EM zone) -> orange
    # k=20–24 (bridge) -> yellow
    # k=15–19 (peripheral) -> light green
    # k<15 (very peripheral) -> gray

    def kcore_color(k):
        """Map k-core number to color."""
        if k >= 30:
            return "#d62728"  # Dark red
        elif k >= 25:
            return "#ff7f0e"  # Orange
        elif k >= 20:
            return "#2ca02c"  # Green
        elif k >= 15:
            return "#9467bd"  # Purple
        elif k >= 10:
            return "#8c564b"  # Brown
        else:
            return "#7f7f7f"  # Gray

    # Build D3 data structure
    nodes = []
    links = []

    node_map = {}  # Original graph node -> D3 node index

    for i, (node_id, node_data) in enumerate(graph.nodes(data=True)):
        paper_id = node_data.get('id')
        kcore = kcore_lookup.get(paper_id, 0)

        node_map[node_id] = i

        nodes.append({
            'id': i,
            'name': node_data.get('title', 'Unknown')[:60],
            'paper_id': paper_id,
            'year': node_data.get('year', 0),
            'kcore': kcore,
            'color': kcore_color(kcore),
            'cited_by_count': node_data.get('cited_by_count', 0),
        })

    # Build edges (sample for visualization)
    edge_count = 0
    max_edges = 3000  # Keep visualization manageable

    for src, tgt in graph.edges():
        if edge_count >= max_edges:
            break
        if src in node_map and tgt in node_map:
            links.append({
                'source': node_map[src],
                'target': node_map[tgt],
                'value': 1,
            })
            edge_count += 1

    print(f"  {len(nodes)} nodes, {len(links)} edges (sampled)")

    # Generate HTML
    html = f"""<!DOCTYPE html>
<meta charset="utf-8">
<title>Citation Network by K-Core Shell</title>
<style>
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    margin: 0;
    padding: 20px;
    background: #0a0a1a;
    color: #e0e0e0;
  }}
  h1 {{
    margin-top: 0;
  }}
  #viz {{
    border: 1px solid #2a2a4a;
    border-radius: 6px;
    background: #0a0a1a;
    width: 100%;
    height: 800px;
  }}
  .legend {{
    margin: 20px 0;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 10px;
  }}
  .legend-item {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .legend-color {{
    width: 16px;
    height: 16px;
    border-radius: 3px;
  }}
  .info {{
    position: absolute;
    top: 20px;
    right: 20px;
    background: rgba(10, 10, 26, 0.9);
    padding: 12px 16px;
    border: 1px solid #2a2a4a;
    border-radius: 6px;
    max-width: 300px;
    font-size: 12px;
    z-index: 10;
  }}
  .controls {{
    margin: 20px 0;
  }}
  input[type="range"] {{
    width: 200px;
    vertical-align: middle;
  }}
</style>

<h1>Citation Network: K-Core Decomposition</h1>

<div class="legend">
  <div class="legend-item">
    <div class="legend-color" style="background: #d62728;"></div>
    <span>k ≥ 30: Inner core (highest centrality)</span>
  </div>
  <div class="legend-item">
    <div class="legend-color" style="background: #ff7f0e;"></div>
    <span>k = 25–29: EM connectomics zone</span>
  </div>
  <div class="legend-item">
    <div class="legend-color" style="background: #2ca02c;"></div>
    <span>k = 20–24: Bridge papers</span>
  </div>
  <div class="legend-item">
    <div class="legend-color" style="background: #9467bd;"></div>
    <span>k = 15–19: Moderately peripheral</span>
  </div>
  <div class="legend-item">
    <div class="legend-color" style="background: #8c564b;"></div>
    <span>k = 10–14: Peripheral</span>
  </div>
  <div class="legend-item">
    <div class="legend-color" style="background: #7f7f7f;"></div>
    <span>k < 10: Very new/niche</span>
  </div>
</div>

<div class="controls">
  <label>Filter by k-core:
    <input type="range" id="kcore-filter" min="0" max="32" value="0" step="1">
    <span id="kcore-value">Show all</span>
  </label>
</div>

<svg id="viz"></svg>

<div class="info">
  <strong>Hover:</strong> Paper details<br>
  <strong>Drag:</strong> Reposition nodes<br>
  <strong>Zoom:</strong> Scroll wheel<br>
  <br>
  <strong>EM connectomics zone:</strong> k=25–29<br>
  Papers here are structurally central.
</div>

<script src="https://d3js.org/d3.v7.min.js"><\/script>
<script>
const data = {{
  nodes: {json.dumps(nodes)},
  links: {json.dumps(links)}
}};

const width = document.getElementById('viz').clientWidth;
const height = document.getElementById('viz').clientHeight;

const svg = d3.select('#viz')
  .attr('width', width)
  .attr('height', height);

// Add zoom
const g = svg.append('g');
svg.call(d3.zoom().on('zoom', e => {{
  g.attr('transform', e.transform);
}}));

// Force simulation
const simulation = d3.forceSimulation(data.nodes)
  .force('link', d3.forceLink(data.links).id(d => d.id).distance(30))
  .force('charge', d3.forceManyBody().strength(-300))
  .force('center', d3.forceCenter(width / 2, height / 2))
  .force('collision', d3.forceCollide(5));

// Links
const link = g.selectAll('line')
  .data(data.links)
  .enter()
  .append('line')
  .style('stroke', '#4a4a6a')
  .style('stroke-opacity', 0.3)
  .style('stroke-width', 0.5);

// Nodes
const node = g.selectAll('circle')
  .data(data.nodes)
  .enter()
  .append('circle')
  .attr('r', d => Math.sqrt(d.cited_by_count) / 4 + 2)
  .style('fill', d => d.color)
  .style('stroke', '#fff')
  .style('stroke-width', 0.5)
  .call(d3.drag()
    .on('start', dragstarted)
    .on('drag', dragged)
    .on('end', dragended));

// Tooltips
node.append('title')
  .text(d =>
    d.name + '\\n' +
    'Year: ' + d.year + '\\n' +
    'K-core: ' + d.kcore + '\\n' +
    'Citations: ' + d.cited_by_count
  );

// Update simulation
simulation.on('tick', () => {{
  link
    .attr('x1', d => d.source.x)
    .attr('y1', d => d.source.y)
    .attr('x2', d => d.target.x)
    .attr('y2', d => d.target.y);

  node
    .attr('cx', d => d.x)
    .attr('cy', d => d.y);
}});

// K-core filter
document.getElementById('kcore-filter').addEventListener('change', e => {{
  const min_kcore = parseInt(e.target.value);
  const label = min_kcore === 0 ? 'Show all' : 'k ≥ ' + min_kcore;
  document.getElementById('kcore-value').textContent = label;

  node.style('opacity', d => d.kcore >= min_kcore ? 1 : 0.1);
  link.style('opacity', d =>
    (d.source.kcore >= min_kcore && d.target.kcore >= min_kcore) ? 1 : 0.05
  );
}});

function dragstarted(event, d) {{
  if (!event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}}

function dragged(event, d) {{
  d.fx = event.x;
  d.fy = event.y;
}}

function dragended(event, d) {{
  if (!event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}}
</script>
"""

    with open(OUT / "kcore_map.html", 'w') as f:
        f.write(html)

    print("Saved → output/kcore_map.html")

    # Print summary by k-core shell
    print("\nK-Core Distribution:")
    for k in sorted(kcore_groups.keys(), reverse=True):
        count = len(kcore_groups[k])
        print(f"  k = {k:2d}: {count:4d} papers", end="")
        if k >= 30:
            print("  (inner core)")
        elif k >= 25:
            print("  (EM connectomics zone)")
        elif k >= 20:
            print("  (bridge)")
        elif k >= 15:
            print("  (moderately peripheral)")
        else:
            print()


if __name__ == "__main__":
    create_kcore_visualization()
