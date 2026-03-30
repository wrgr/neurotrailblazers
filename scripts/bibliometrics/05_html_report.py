#!/usr/bin/env python3
"""
Step 5: Generate standalone interactive HTML visualization.

Creates a self-contained HTML page with:
  - D3 force-directed graph (citation + co-authorship toggle)
  - Ranked tables (papers by citation + PageRank, authors)
  - Community coloring
  - Validation summary panel

Input:  output/*.json
Output: output/field_map.html

Usage:
  python 05_html_report.py
  python 05_html_report.py --max-nodes 300  # limit graph size
"""
import argparse
import json
from pathlib import Path

from config import OUTPUT_DIR


def load_json(filename):
    """Load a JSON file from output directory."""
    path = OUTPUT_DIR / filename
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)


def prune_graph(graph_data, max_nodes, rankings):
    """
    Prune graph to top N nodes by composite score.
    Returns pruned graph data in node-link format.
    """
    if not graph_data or not rankings:
        return graph_data

    # Get top node IDs by ranking
    top_ids = set()
    for p in rankings[:max_nodes]:
        top_ids.add(p.get("openalex_id", ""))

    # Filter nodes
    nodes = [n for n in graph_data.get("nodes", []) if n.get("id") in top_ids]
    node_ids = {n["id"] for n in nodes}

    # Filter edges
    links = [
        l for l in graph_data.get("links", [])
        if l.get("source") in node_ids and l.get("target") in node_ids
    ]

    return {"nodes": nodes, "links": links}


def generate_html(citation_graph, coauthorship_graph, paper_rankings,
                  author_rankings, communities, validation, stats,
                  citation_baseline):
    """
    Generate self-contained HTML with D3 visualization.
    All CSS and JS are inlined.
    """
    # Prepare data for embedding
    citation_json = json.dumps(citation_graph or {"nodes": [], "links": []})
    coauthorship_json = json.dumps(coauthorship_graph or {"nodes": [], "links": []})
    papers_json = json.dumps(paper_rankings[:100] if paper_rankings else [])
    authors_json = json.dumps(author_rankings[:100] if author_rankings else [])
    communities_json = json.dumps(communities or [])
    validation_json = json.dumps(validation or {})
    stats_json = json.dumps(stats or {})
    baseline_json = json.dumps(citation_baseline[:50] if citation_baseline else [])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Connectomics Field Map — Bibliometric Analysis</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: #0a0a1a; color: #e0e0e0; display: flex; height: 100vh; }}
#sidebar {{ width: 380px; background: #111128; overflow-y: auto; padding: 16px;
            border-right: 1px solid #2a2a4a; flex-shrink: 0; }}
#graph-container {{ flex: 1; position: relative; }}
svg {{ width: 100%; height: 100%; }}
h1 {{ font-size: 18px; color: #8888ff; margin-bottom: 8px; }}
h2 {{ font-size: 14px; color: #aaaadd; margin: 16px 0 8px; cursor: pointer; }}
h2:hover {{ color: #ccccff; }}
.section {{ margin-bottom: 12px; }}
.section-content {{ display: none; }}
.section-content.open {{ display: block; }}
table {{ width: 100%; border-collapse: collapse; font-size: 11px; }}
th, td {{ padding: 4px 6px; text-align: left; border-bottom: 1px solid #222244; }}
th {{ color: #8888cc; font-weight: 600; }}
tr:hover {{ background: #1a1a3a; }}
.rank {{ color: #666688; width: 30px; }}
.score {{ color: #88cc88; font-family: monospace; }}
.citations {{ color: #ccaa44; font-family: monospace; }}
.controls {{ margin: 12px 0; }}
.controls button {{ background: #2a2a5a; color: #ccccff; border: 1px solid #4a4a7a;
                    padding: 6px 12px; border-radius: 4px; cursor: pointer; margin: 2px; }}
.controls button:hover {{ background: #3a3a7a; }}
.controls button.active {{ background: #4a4aaa; border-color: #6a6acc; }}
.stat {{ display: inline-block; background: #1a1a3a; padding: 4px 8px;
         border-radius: 4px; margin: 2px; font-size: 11px; }}
.stat .value {{ color: #88cc88; font-weight: 600; }}
.node {{ cursor: pointer; }}
.link {{ stroke: #333366; stroke-opacity: 0.3; }}
#tooltip {{ position: absolute; background: #1a1a3a; border: 1px solid #4a4a7a;
            padding: 8px 12px; border-radius: 4px; font-size: 12px;
            pointer-events: none; display: none; max-width: 350px; z-index: 100; }}
#detail-panel {{ background: #0d0d2a; border: 1px solid #2a2a4a;
                 border-radius: 4px; padding: 12px; margin-top: 12px; display: none; }}
#detail-panel h3 {{ color: #aaaaff; font-size: 13px; margin-bottom: 4px; }}
#detail-panel .meta {{ font-size: 11px; color: #888; }}
</style>
</head>
<body>
<div id="sidebar">
  <h1>Connectomics Field Map</h1>
  <p style="font-size:11px;color:#888;margin-bottom:12px;">
    Data-driven bibliometric analysis via OpenAlex
  </p>

  <div class="controls">
    <button id="btn-citation" class="active" onclick="switchGraph('citation')">Citations</button>
    <button id="btn-coauthor" onclick="switchGraph('coauthor')">Co-authorship</button>
  </div>

  <div class="section">
    <div class="stat">Papers: <span class="value" id="stat-papers">-</span></div>
    <div class="stat">Authors: <span class="value" id="stat-authors">-</span></div>
    <div class="stat">Communities: <span class="value" id="stat-communities">-</span></div>
  </div>

  <div id="detail-panel">
    <h3 id="detail-title"></h3>
    <div class="meta" id="detail-meta"></div>
  </div>

  <div class="section">
    <h2 onclick="toggleSection(this)">Top Papers (Composite Score) [+]</h2>
    <div class="section-content" id="papers-table"></div>
  </div>

  <div class="section">
    <h2 onclick="toggleSection(this)">Top Papers (Citations Only) [+]</h2>
    <div class="section-content" id="baseline-table"></div>
  </div>

  <div class="section">
    <h2 onclick="toggleSection(this)">Top Authors [+]</h2>
    <div class="section-content" id="authors-table"></div>
  </div>

  <div class="section">
    <h2 onclick="toggleSection(this)">Communities [+]</h2>
    <div class="section-content" id="communities-list"></div>
  </div>

  <div class="section">
    <h2 onclick="toggleSection(this)">Validation [+]</h2>
    <div class="section-content" id="validation-panel"></div>
  </div>
</div>

<div id="graph-container">
  <div id="tooltip"></div>
  <svg id="graph-svg"></svg>
</div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
// Data (embedded)
const citationData = {citation_json};
const coauthorData = {coauthorship_json};
const paperRankings = {papers_json};
const authorRankings = {authors_json};
const communities = {communities_json};
const validation = {validation_json};
const stats = {stats_json};
const baseline = {baseline_json};

// State
let currentGraph = 'citation';
let simulation = null;

// Init stats
document.getElementById('stat-papers').textContent = stats.total_papers || '-';
document.getElementById('stat-authors').textContent = stats.total_authors || '-';
document.getElementById('stat-communities').textContent = stats.communities || '-';

// Toggle sections
function toggleSection(el) {{
  const content = el.nextElementSibling;
  content.classList.toggle('open');
  el.textContent = el.textContent.replace(/[+-]/, content.classList.contains('open') ? '-' : '+');
}}

// Build ranking tables
function buildPapersTable(papers, containerId) {{
  const container = document.getElementById(containerId);
  let html = '<table><tr><th class="rank">#</th><th>Paper</th><th>Year</th><th class="score">Score</th></tr>';
  papers.forEach((p, i) => {{
    const score = p.composite_score ? p.composite_score.toFixed(3) : p.total_citations;
    html += `<tr><td class="rank">${{i+1}}</td><td>${{(p.title||'').substring(0,60)}}...</td>
             <td>${{p.year||''}}</td><td class="score">${{score}}</td></tr>`;
  }});
  html += '</table>';
  container.innerHTML = html;
}}
buildPapersTable(paperRankings, 'papers-table');
buildPapersTable(baseline, 'baseline-table');

// Authors table
(function() {{
  const container = document.getElementById('authors-table');
  let html = '<table><tr><th class="rank">#</th><th>Author</th><th>Papers</th><th class="score">Score</th></tr>';
  authorRankings.forEach((a, i) => {{
    html += `<tr><td class="rank">${{i+1}}</td><td>${{a.name||''}}</td>
             <td>${{a.paper_count||0}}</td><td class="score">${{(a.composite_score||0).toFixed(3)}}</td></tr>`;
  }});
  html += '</table>';
  container.innerHTML = html;
}})();

// Communities list
(function() {{
  const container = document.getElementById('communities-list');
  let html = '';
  communities.forEach(c => {{
    const concepts = (c.top_concepts||[]).map(x => x.name).join(', ');
    html += `<div style="margin:4px 0;font-size:11px;padding:4px;background:#1a1a3a;border-radius:3px">
      <strong>${{c.label}}</strong> (${{c.size}} papers)<br>
      <span style="color:#888">${{concepts}}</span></div>`;
  }});
  container.innerHTML = html;
}})();

// Validation panel
(function() {{
  const container = document.getElementById('validation-panel');
  const v = validation;
  let html = '<div style="font-size:11px">';
  if (v.triangulation) {{
    html += '<strong>Triangulation:</strong><br>';
    for (const [k, val] of Object.entries(v.triangulation)) {{
      if (val.jaccard !== undefined) {{
        html += `${{k}}: Jaccard=${{val.jaccard}}<br>`;
      }}
    }}
  }}
  if (v.expert_validation) {{
    html += `<br><strong>Expert Recall:</strong> ${{(v.expert_validation.recall*100).toFixed(1)}}%<br>`;
    html += `Novel discoveries: ${{v.expert_validation.novel_in_data_driven}}<br>`;
  }}
  if (v.author_check) {{
    html += `<br><strong>Expert Authors Found:</strong> ${{v.author_check.found_in_corpus}}/${{v.author_check.total_experts}}<br>`;
  }}
  html += '</div>';
  container.innerHTML = html;
}})();

// Graph visualization
const svg = d3.select('#graph-svg');
const tooltip = d3.select('#tooltip');
const width = document.getElementById('graph-container').clientWidth;
const height = document.getElementById('graph-container').clientHeight;

// Community colors
const colorScale = d3.scaleOrdinal(d3.schemeTableau10);

function switchGraph(type) {{
  currentGraph = type;
  document.getElementById('btn-citation').classList.toggle('active', type === 'citation');
  document.getElementById('btn-coauthor').classList.toggle('active', type === 'coauthor');
  renderGraph(type === 'citation' ? citationData : coauthorData);
}}

function renderGraph(data) {{
  svg.selectAll('*').remove();
  if (!data || !data.nodes || data.nodes.length === 0) {{
    svg.append('text').attr('x', width/2).attr('y', height/2)
      .attr('text-anchor', 'middle').attr('fill', '#666')
      .text('No graph data available. Run the pipeline first.');
    return;
  }}

  const g = svg.append('g');

  // Zoom
  svg.call(d3.zoom().scaleExtent([0.1, 10]).on('zoom', (e) => {{
    g.attr('transform', e.transform);
  }}));

  const links = data.links.map(d => ({{...d}}));
  const nodes = data.nodes.map(d => ({{...d}}));

  if (simulation) simulation.stop();
  simulation = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d => d.id).distance(30))
    .force('charge', d3.forceManyBody().strength(-50))
    .force('center', d3.forceCenter(width / 2, height / 2));

  const link = g.append('g').selectAll('line')
    .data(links).join('line').attr('class', 'link');

  const node = g.append('g').selectAll('circle')
    .data(nodes).join('circle').attr('class', 'node')
    .attr('r', d => Math.max(3, Math.min(15, Math.sqrt(d.cited_by_count || 1) * 0.5)))
    .attr('fill', d => colorScale(d.community || 0))
    .attr('stroke', '#222').attr('stroke-width', 0.5)
    .call(d3.drag().on('start', dragStart).on('drag', dragging).on('end', dragEnd));

  node.on('mouseover', (e, d) => {{
    tooltip.style('display', 'block')
      .html(`<strong>${{d.title || d.name || d.id}}</strong><br>
             ${{d.year ? 'Year: ' + d.year + '<br>' : ''}}
             ${{d.cited_by_count ? 'Citations: ' + d.cited_by_count : ''}}`);
  }}).on('mousemove', (e) => {{
    tooltip.style('left', (e.pageX + 10) + 'px').style('top', (e.pageY - 10) + 'px');
  }}).on('mouseout', () => {{
    tooltip.style('display', 'none');
  }}).on('click', (e, d) => {{
    const panel = document.getElementById('detail-panel');
    panel.style.display = 'block';
    document.getElementById('detail-title').textContent = d.title || d.name || d.id;
    document.getElementById('detail-meta').innerHTML =
      `${{d.year ? 'Year: ' + d.year + '<br>' : ''}}
       ${{d.doi ? 'DOI: ' + d.doi + '<br>' : ''}}
       ${{d.cited_by_count ? 'Citations: ' + d.cited_by_count + '<br>' : ''}}
       ${{d.journal ? 'Journal: ' + d.journal : ''}}`;
  }});

  simulation.on('tick', () => {{
    link.attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
    node.attr('cx', d => d.x).attr('cy', d => d.y);
  }});

  function dragStart(e) {{ if (!e.active) simulation.alphaTarget(0.3).restart(); e.subject.fx = e.subject.x; e.subject.fy = e.subject.y; }}
  function dragging(e) {{ e.subject.fx = e.x; e.subject.fy = e.y; }}
  function dragEnd(e) {{ if (!e.active) simulation.alphaTarget(0); e.subject.fx = null; e.subject.fy = null; }}
}}

// Initial render
switchGraph('citation');
</script>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-nodes", type=int, default=300,
                        help="Maximum nodes in graph visualization")
    args = parser.parse_args()

    print("Loading data...")
    citation_graph = load_json("graphs/citation_graph.json")
    coauthorship_graph = load_json("graphs/coauthorship_graph.json")
    paper_rankings = load_json("paper_rankings.json") or []
    author_rankings = load_json("author_rankings.json") or []
    communities_data = load_json("communities.json") or []
    validation = load_json("validation_report.json")
    stats = load_json("corpus_stats.json")
    baseline = load_json("citation_baseline.json") or []

    # Prune graphs for visualization
    print(f"Pruning graphs to top {args.max_nodes} nodes...")
    citation_graph = prune_graph(citation_graph, args.max_nodes, paper_rankings)
    coauthorship_graph = prune_graph(coauthorship_graph, args.max_nodes, author_rankings)

    print("Generating HTML...")
    html = generate_html(
        citation_graph, coauthorship_graph,
        paper_rankings, author_rankings,
        communities_data, validation, stats, baseline
    )

    output_path = OUTPUT_DIR / "field_map.html"
    with open(output_path, "w") as f:
        f.write(html)
    print(f"Saved to {output_path}")
    print("Done. Open field_map.html in a browser to view.")


if __name__ == "__main__":
    main()
