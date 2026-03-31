#!/usr/bin/env python3
"""
Generate full visualizations with ALL papers and authors (no pruning).

Creates:
  - field_map_full.html: Citation network with ALL 7,503 papers + ranked lists
  - coauthor_map_full.html: Co-authorship network with ALL 35,797 authors + ranked lists
  - journal_club_threshold_*.html: Journal club at different importance thresholds

Input:  output/paper_rankings_all.json, graphs/*.json, journal_club_*.json
Output: output/field_map_full.html, output/coauthor_map_full.html, output/journal_club_threshold_*.html
"""
import json
from pathlib import Path
from collections import defaultdict

OUTPUT_DIR = Path("output")


def load_json(filename):
    """Load a JSON file from output directory."""
    path = OUTPUT_DIR / filename
    if not path.exists():
        print(f"Warning: {filename} not found")
        return None
    with open(path) as f:
        return json.load(f)


def generate_field_map_full():
    """Generate field_map_full.html with ALL papers and no pruning."""
    print("Generating field_map_full.html...")

    citation_graph = load_json("graphs/citation_graph.json") or {"nodes": [], "links": []}
    coauthorship_graph = load_json("graphs/coauthorship_graph.json") or {"nodes": [], "links": []}
    paper_rankings = load_json("paper_rankings_all.json") or []
    author_rankings = load_json("author_rankings.json") or []
    communities_data = load_json("communities.json") or []
    stats = load_json("corpus_stats.json") or {}

    # Prepare data for embedding
    citation_json = json.dumps(citation_graph)
    coauthorship_json = json.dumps(coauthorship_graph)
    papers_json = json.dumps(paper_rankings[:200] if paper_rankings else [])
    authors_json = json.dumps(author_rankings[:200] if author_rankings else [])
    communities_json = json.dumps(communities_data or [])
    stats_json = json.dumps(stats or {})

    # Count stats
    num_papers = len(citation_graph.get("nodes", []))
    num_authors = len(coauthorship_graph.get("nodes", []))
    num_edges = len(citation_graph.get("links", []))

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EM Connectomics Field Map — Full Network</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: #0a0a1a; color: #e0e0e0; display: flex; height: 100vh; }}
#sidebar {{ width: 400px; background: #111128; overflow-y: auto; padding: 16px;
            border-right: 1px solid #2a2a4a; flex-shrink: 0; }}
#graph-container {{ flex: 1; position: relative; }}
svg {{ width: 100%; height: 100%; }}
h1 {{ font-size: 18px; color: #8888ff; margin-bottom: 8px; }}
h2 {{ font-size: 13px; color: #aaaadd; margin: 14px 0 6px; cursor: pointer; }}
h2:hover {{ color: #ccccff; }}
.section {{ margin-bottom: 10px; }}
.section-content {{ display: none; font-size: 11px; }}
.section-content.open {{ display: block; }}
table {{ width: 100%; border-collapse: collapse; font-size: 10px; }}
th, td {{ padding: 3px 4px; text-align: left; border-bottom: 1px solid #222244; }}
th {{ color: #8888cc; font-weight: 600; }}
tr:hover {{ background: #1a1a3a; }}
.rank {{ color: #666688; width: 25px; }}
.score {{ color: #88cc88; font-family: monospace; font-size: 9px; }}
.controls {{ margin: 12px 0; }}
.controls button {{ background: #2a2a5a; color: #ccccff; border: 1px solid #4a4a7a;
                    padding: 6px 12px; border-radius: 4px; cursor: pointer; margin: 2px; font-size: 11px; }}
.controls button:hover {{ background: #3a3a7a; }}
.controls button.active {{ background: #4a4aaa; border-color: #6a6acc; }}
.stat {{ display: inline-block; background: #1a1a3a; padding: 4px 8px;
         border-radius: 4px; margin: 2px; font-size: 11px; }}
.stat .value {{ color: #88cc88; font-weight: 600; }}
.node {{ cursor: pointer; }}
.link {{ stroke: #333366; stroke-opacity: 0.2; }}
#tooltip {{ position: absolute; background: #1a1a3a; border: 1px solid #4a4a7a;
            padding: 6px 10px; border-radius: 4px; font-size: 11px;
            pointer-events: none; display: none; max-width: 320px; z-index: 100; }}
#detail-panel {{ background: #0d0d2a; border: 1px solid #2a2a4a;
                 border-radius: 4px; padding: 10px; margin-top: 10px; display: none; font-size: 10px; }}
#detail-panel h3 {{ color: #aaaaff; font-size: 12px; margin-bottom: 4px; }}
.meta {{ color: #888; line-height: 1.4; }}
.search-box {{ width: 100%; padding: 6px; background: #1a1a3a; border: 1px solid #2a2a4a;
               border-radius: 4px; color: #ccccff; font-size: 11px; margin-bottom: 8px; }}
</style>
</head>
<body>
<div id="sidebar">
  <h1>📊 EM Connectomics Field Map</h1>
  <p style="font-size:10px;color:#888;margin-bottom:12px;">
    Full network: All {{num_papers}} papers, {{num_edges}} citation edges
  </p>

  <div class="controls">
    <button id="btn-citation" class="active" onclick="switchGraph('citation')">Citations</button>
    <button id="btn-coauthor" onclick="switchGraph('coauthor')">Co-authorship</button>
  </div>

  <div class="section">
    <div class="stat">Papers: <span class="value">{{num_papers}}</span></div>
    <div class="stat">Authors: <span class="value">{{num_authors}}</span></div>
    <div class="stat">Edges: <span class="value">{{num_edges}}</span></div>
  </div>

  <div id="detail-panel">
    <h3 id="detail-title"></h3>
    <div class="meta" id="detail-meta"></div>
  </div>

  <input type="text" id="search-box" class="search-box" placeholder="Search papers...">

  <div class="section">
    <h2 onclick="toggleSection(this)">Top Papers ({{len(paper_rankings)}}) [+]</h2>
    <div class="section-content" id="papers-table"></div>
  </div>

  <div class="section">
    <h2 onclick="toggleSection(this)">Top Authors ({{len(author_rankings)}}) [+]</h2>
    <div class="section-content" id="authors-table"></div>
  </div>
</div>

<div id="graph-container">
  <div id="tooltip"></div>
  <svg id="graph-svg"></svg>
</div>

<script>
// Embedded data
const citationData = {citation_json};
const coauthorData = {coauthorship_json};
const paperRankings = {papers_json};
const authorRankings = {authors_json};
const communities = {communities_json};

let currentGraph = 'citation';

// Toggle section visibility
function toggleSection(el) {{
  const content = el.nextElementSibling;
  content.classList.toggle('open');
  el.textContent = el.textContent.replace(/[+-]/, content.classList.contains('open') ? '-' : '+');
}}

// Build paper rankings table
(function() {{
  const container = document.getElementById('papers-table');
  if (!paperRankings || paperRankings.length === 0) {{
    container.innerHTML = '<p style="color:#888">No papers loaded</p>';
    return;
  }}
  let html = '<table><tr><th class="rank">#</th><th>Paper</th><th class="score">Score</th></tr>';
  paperRankings.slice(0, 100).forEach((p, i) => {{
    const score = (p.composite_score || 0).toFixed(3);
    const title = (p.title || '').substring(0, 50);
    html += `<tr><td class="rank">${{i+1}}</td><td title="${{p.title}}">${{title}}</td><td class="score">${{score}}</td></tr>`;
  }});
  html += '</table>';
  container.innerHTML = html;
}})();

// Build author rankings table
(function() {{
  const container = document.getElementById('authors-table');
  if (!authorRankings || authorRankings.length === 0) {{
    container.innerHTML = '<p style="color:#888">No authors loaded</p>';
    return;
  }}
  let html = '<table><tr><th class="rank">#</th><th>Author</th><th class="score">Papers</th></tr>';
  authorRankings.slice(0, 100).forEach((a, i) => {{
    const papers = a.paper_count || 0;
    const name = (a.name || '').substring(0, 40);
    html += `<tr><td class="rank">${{i+1}}</td><td title="${{a.name}}">${{name}}</td><td class="score">${{papers}}</td></tr>`;
  }});
  html += '</table>';
  container.innerHTML = html;
}})();

// Graph visualization
const svg = d3.select('#graph-svg');
const tooltip = d3.select('#tooltip');
const width = document.getElementById('graph-container').clientWidth;
const height = document.getElementById('graph-container').clientHeight;

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
      .attr('text-anchor', 'middle').attr('fill', '#666').attr('font-size', 14)
      .text('No graph data available');
    return;
  }}

  const g = svg.append('g');

  // Zoom
  svg.call(d3.zoom().scaleExtent([0.1, 10]).on('zoom', (e) => {{
    g.attr('transform', e.transform);
  }}));

  // Simulation
  const simulation = d3.forceSimulation(data.nodes)
    .force('link', d3.forceLink(data.links).id(d => d.id).distance(30).strength(0.3))
    .force('charge', d3.forceManyBody().strength(-20))
    .force('center', d3.forceCenter(width/2, height/2))
    .force('collision', d3.forceCollide(5));

  const link = g.append('g')
    .selectAll('line')
    .data(data.links)
    .join('line')
    .attr('class', 'link')
    .attr('stroke-width', d => Math.sqrt(d.weight || 1));

  const node = g.append('g')
    .selectAll('circle')
    .data(data.nodes)
    .join('circle')
    .attr('class', 'node')
    .attr('r', d => Math.sqrt((d.cited_by_count || d.paper_count || 1) + 1) * 0.8)
    .attr('fill', d => colorScale(d.community || 0))
    .attr('stroke', '#fff')
    .attr('stroke-width', 0.5)
    .call(d3.drag()
      .on('start', dragstarted)
      .on('drag', dragged)
      .on('end', dragended));

  node.on('mouseover', function(e, d) {{
    tooltip.style('display', 'block')
      .html(`<strong>${{(d.title || d.name || 'Unknown').substring(0, 60)}}</strong><br>
             Year: ${{d.year || 'N/A'}}<br>
             Citations: ${{d.cited_by_count || d.paper_count || 0}}`);
  }})
  .on('mousemove', function(e) {{
    tooltip.style('left', (e.pageX + 10) + 'px')
      .style('top', (e.pageY - 28) + 'px');
  }})
  .on('mouseout', function() {{
    tooltip.style('display', 'none');
  }});

  simulation.on('tick', () => {{
    link.attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);
    node.attr('cx', d => d.x = Math.max(5, Math.min(width - 5, d.x)))
      .attr('cy', d => d.y = Math.max(5, Math.min(height - 5, d.y)));
  }});

  function dragstarted(e, d) {{
    if (!e.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }}
  function dragged(e, d) {{
    d.fx = e.x;
    d.fy = e.y;
  }}
  function dragended(e, d) {{
    if (!e.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }}
}}

// Initial render
renderGraph(citationData);

// Search functionality
document.getElementById('search-box').addEventListener('keyup', function(e) {{
  const query = e.target.value.toLowerCase();
  svg.selectAll('circle').style('opacity', d => {{
    const title = (d.title || '').toLowerCase();
    const name = (d.name || '').toLowerCase();
    return (title.includes(query) || name.includes(query)) ? 1 : 0.1;
  }});
}});
</script>
</body>
</html>"""

    # Write file
    output_path = OUTPUT_DIR / "field_map_full.html"
    with open(output_path, "w") as f:
        f.write(html)
    print(f"✓ Saved {output_path} ({num_papers} papers, {num_edges} edges)")
    return output_path


def generate_coauthor_map_full():
    """Generate coauthor_map_full.html with ALL authors and no pruning."""
    print("Generating coauthor_map_full.html...")

    coauthorship_graph = load_json("graphs/coauthorship_graph.json") or {"nodes": [], "links": []}
    author_rankings = load_json("author_rankings.json") or []

    # Prepare data for embedding
    coauthorship_json = json.dumps(coauthorship_graph)
    authors_json = json.dumps(author_rankings[:200] if author_rankings else [])

    # Count stats
    num_authors = len(coauthorship_graph.get("nodes", []))
    num_edges = len(coauthorship_graph.get("links", []))

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EM Connectomics Co-authorship Network</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: #0a0a1a; color: #e0e0e0; display: flex; height: 100vh; }}
#sidebar {{ width: 400px; background: #111128; overflow-y: auto; padding: 16px;
            border-right: 1px solid #2a2a4a; flex-shrink: 0; }}
#graph-container {{ flex: 1; position: relative; }}
svg {{ width: 100%; height: 100%; }}
h1 {{ font-size: 18px; color: #8888ff; margin-bottom: 8px; }}
h2 {{ font-size: 13px; color: #aaaadd; margin: 14px 0 6px; cursor: pointer; }}
h2:hover {{ color: #ccccff; }}
.section {{ margin-bottom: 10px; }}
.section-content {{ display: none; font-size: 11px; }}
.section-content.open {{ display: block; }}
table {{ width: 100%; border-collapse: collapse; font-size: 10px; }}
th, td {{ padding: 3px 4px; text-align: left; border-bottom: 1px solid #222244; }}
th {{ color: #8888cc; font-weight: 600; }}
tr:hover {{ background: #1a1a3a; }}
.rank {{ color: #666688; width: 25px; }}
.score {{ color: #88cc88; font-family: monospace; font-size: 9px; }}
.stat {{ display: inline-block; background: #1a1a3a; padding: 4px 8px;
         border-radius: 4px; margin: 2px; font-size: 11px; }}
.stat .value {{ color: #88cc88; font-weight: 600; }}
.node {{ cursor: pointer; }}
.link {{ stroke: #333366; stroke-opacity: 0.1; }}
#tooltip {{ position: absolute; background: #1a1a3a; border: 1px solid #4a4a7a;
            padding: 6px 10px; border-radius: 4px; font-size: 11px;
            pointer-events: none; display: none; max-width: 320px; z-index: 100; }}
#detail-panel {{ background: #0d0d2a; border: 1px solid #2a2a4a;
                 border-radius: 4px; padding: 10px; margin-top: 10px; display: none; font-size: 10px; }}
#detail-panel h3 {{ color: #aaaaff; font-size: 12px; margin-bottom: 4px; }}
.meta {{ color: #888; line-height: 1.4; }}
.search-box {{ width: 100%; padding: 6px; background: #1a1a3a; border: 1px solid #2a2a4a;
               border-radius: 4px; color: #ccccff; font-size: 11px; margin-bottom: 8px; }}
</style>
</head>
<body>
<div id="sidebar">
  <h1>👥 EM Connectomics Co-authorship</h1>
  <p style="font-size:10px;color:#888;margin-bottom:12px;">
    Full network: All {{num_authors}} authors, {{num_edges}} collaboration edges
  </p>

  <div class="section">
    <div class="stat">Authors: <span class="value">{{num_authors}}</span></div>
    <div class="stat">Collaborations: <span class="value">{{num_edges}}</span></div>
  </div>

  <div id="detail-panel">
    <h3 id="detail-title"></h3>
    <div class="meta" id="detail-meta"></div>
  </div>

  <input type="text" id="search-box" class="search-box" placeholder="Search authors...">

  <div class="section">
    <h2 onclick="toggleSection(this)">Top Authors ({{len(author_rankings)}}) [+]</h2>
    <div class="section-content" id="authors-table"></div>
  </div>
</div>

<div id="graph-container">
  <div id="tooltip"></div>
  <svg id="graph-svg"></svg>
</div>

<script>
// Embedded data
const networkData = {coauthorship_json};
const authorRankings = {authors_json};

// Toggle section visibility
function toggleSection(el) {{
  const content = el.nextElementSibling;
  content.classList.toggle('open');
  el.textContent = el.textContent.replace(/[+-]/, content.classList.contains('open') ? '-' : '+');
}}

// Build author rankings table
(function() {{
  const container = document.getElementById('authors-table');
  if (!authorRankings || authorRankings.length === 0) {{
    container.innerHTML = '<p style="color:#888">No authors loaded</p>';
    return;
  }}
  let html = '<table><tr><th class="rank">#</th><th>Author</th><th class="score">Papers</th></tr>';
  authorRankings.slice(0, 100).forEach((a, i) => {{
    const papers = a.paper_count || 0;
    const name = (a.name || '').substring(0, 40);
    html += `<tr><td class="rank">${{i+1}}</td><td title="${{a.name}}">${{name}}</td><td class="score">${{papers}}</td></tr>`;
  }});
  html += '</table>';
  container.innerHTML = html;
}})();

// Graph visualization
const svg = d3.select('#graph-svg');
const tooltip = d3.select('#tooltip');
const width = document.getElementById('graph-container').clientWidth;
const height = document.getElementById('graph-container').clientHeight;

const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

function renderGraph(data) {{
  svg.selectAll('*').remove();
  if (!data || !data.nodes || data.nodes.length === 0) {{
    svg.append('text').attr('x', width/2).attr('y', height/2)
      .attr('text-anchor', 'middle').attr('fill', '#666').attr('font-size', 14)
      .text('No graph data available');
    return;
  }}

  const g = svg.append('g');

  // Zoom
  svg.call(d3.zoom().scaleExtent([0.1, 10]).on('zoom', (e) => {{
    g.attr('transform', e.transform);
  }}));

  // Simulation - stronger repulsion for author networks
  const simulation = d3.forceSimulation(data.nodes)
    .force('link', d3.forceLink(data.links).id(d => d.id).distance(40).strength(0.2))
    .force('charge', d3.forceManyBody().strength(-30))
    .force('center', d3.forceCenter(width/2, height/2))
    .force('collision', d3.forceCollide(6));

  const link = g.append('g')
    .selectAll('line')
    .data(data.links)
    .join('line')
    .attr('class', 'link')
    .attr('stroke-width', d => Math.sqrt(d.weight || 1) * 0.5);

  const node = g.append('g')
    .selectAll('circle')
    .data(data.nodes)
    .join('circle')
    .attr('class', 'node')
    .attr('r', d => Math.sqrt((d.paper_count || 1) + 1) * 0.7)
    .attr('fill', d => colorScale(d.id.charCodeAt(0) % 10))
    .attr('stroke', '#fff')
    .attr('stroke-width', 0.5)
    .call(d3.drag()
      .on('start', dragstarted)
      .on('drag', dragged)
      .on('end', dragended));

  node.on('mouseover', function(e, d) {{
    tooltip.style('display', 'block')
      .html(`<strong>${{(d.name || 'Unknown').substring(0, 50)}}</strong><br>
             Papers: ${{d.paper_count || 0}}<br>
             Co-authors: ${{d.co_author_count || 0}}`);
  }})
  .on('mousemove', function(e) {{
    tooltip.style('left', (e.pageX + 10) + 'px')
      .style('top', (e.pageY - 28) + 'px');
  }})
  .on('mouseout', function() {{
    tooltip.style('display', 'none');
  }});

  simulation.on('tick', () => {{
    link.attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);
    node.attr('cx', d => d.x = Math.max(5, Math.min(width - 5, d.x)))
      .attr('cy', d => d.y = Math.max(5, Math.min(height - 5, d.y)));
  }});

  function dragstarted(e, d) {{
    if (!e.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }}
  function dragged(e, d) {{
    d.fx = e.x;
    d.fy = e.y;
  }}
  function dragended(e, d) {{
    if (!e.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }}
}}

// Initial render
renderGraph(networkData);

// Search functionality
document.getElementById('search-box').addEventListener('keyup', function(e) {{
  const query = e.target.value.toLowerCase();
  svg.selectAll('circle').style('opacity', d => {{
    const name = (d.name || '').toLowerCase();
    return name.includes(query) ? 1 : 0.1;
  }});
}});
</script>
</body>
</html>"""

    # Write file
    output_path = OUTPUT_DIR / "coauthor_map_full.html"
    with open(output_path, "w") as f:
        f.write(html)
    print(f"✓ Saved {output_path} ({num_authors} authors, {num_edges} edges)")
    return output_path


def generate_journal_club_visualizations():
    """Generate journal club visualizations at different thresholds."""
    print("\nGenerating journal club threshold visualizations...")

    # Load all journal club papers at different thresholds
    thresholds = {
        10: "Inclusive (≥0.10)",
        15: "Moderate (≥0.15)",
        20: "Core (≥0.20)",
        30: "Strict (≥0.30)"
    }

    for threshold, label in thresholds.items():
        filename = f"journal_club_threshold_{threshold}.json"
        papers = load_json(filename)

        if not papers:
            print(f"  Warning: {filename} not found, skipping threshold {threshold}")
            continue

        # Generate HTML
        papers_json = json.dumps(papers[:100])
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Journal Club — {label}</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: #0a0a1a; color: #e0e0e0; padding: 30px; max-width: 1200px; margin: 0 auto; }}
h1 {{ color: #8888ff; margin-bottom: 10px; }}
.subtitle {{ color: #888; margin-bottom: 30px; font-size: 14px; }}
.stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
          gap: 15px; margin-bottom: 40px; }}
.stat-box {{ background: #1a1a3a; border: 1px solid #2a2a4a; padding: 15px; border-radius: 6px; }}
.stat-number {{ font-size: 24px; font-weight: bold; color: #88cc88; }}
.stat-label {{ font-size: 12px; color: #888; margin-top: 5px; }}
.thresholds {{ display: flex; gap: 10px; margin-bottom: 30px; flex-wrap: wrap; }}
.btn {{ background: #2a2a5a; color: #ccccff; border: 1px solid #4a4a7a;
        padding: 10px 20px; border-radius: 4px; cursor: pointer; font-size: 13px; }}
.btn:hover {{ background: #3a3a7a; }}
.btn.active {{ background: #4a4aaa; border-color: #6a6acc; }}
table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
th, td {{ padding: 8px 12px; text-align: left; border-bottom: 1px solid #222244; }}
th {{ background: #1a1a3a; color: #8888cc; font-weight: 600; }}
tr:hover {{ background: #0f0f2a; }}
.rank {{ color: #666688; width: 30px; }}
.tier {{ padding: 2px 6px; border-radius: 3px; font-size: 11px; font-weight: 600; }}
.tier-platinum {{ background: #4a4a2a; color: #ffdd44; }}
.tier-gold {{ background: #3a3a2a; color: #ffaa44; }}
.tier-silver {{ background: #2a2a3a; color: #cccccc; }}
.tier-bronze {{ background: #2a2a2a; color: #8888aa; }}
</style>
</head>
<body>
<h1>📚 Journal Club — {label}</h1>
<div class="subtitle">
  {len(papers)} papers selected by network importance metrics
</div>

<div class="stats">
  <div class="stat-box">
    <div class="stat-number">{len(papers)}</div>
    <div class="stat-label">Papers</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">{sum(1 for p in papers if p.get('tier') == 'Platinum')}</div>
    <div class="stat-label">Platinum</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">{sum(1 for p in papers if p.get('tier') == 'Gold')}</div>
    <div class="stat-label">Gold</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">{sum(1 for p in papers if p.get('tier') == 'Silver')}</div>
    <div class="stat-label">Silver</div>
  </div>
</div>

<table>
<tr>
  <th class="rank">#</th>
  <th>Tier</th>
  <th>Paper</th>
  <th>Year</th>
  <th>Score</th>
  <th>Citations</th>
  <th>In/Out</th>
</tr>"""

        for i, p in enumerate(papers, 1):
            tier = p.get('tier', 'Bronze')
            tier_class = f"tier-{tier.lower()}"
            title = (p.get('title', 'Unknown'))[:70]
            score = f"{p.get('composite_score', 0):.3f}"
            citations = p.get('total_citations', 0)
            in_deg = p.get('in_degree', 0)
            out_deg = p.get('out_degree', 0)

            html += f"""<tr>
  <td class="rank">{i}</td>
  <td><span class="tier {tier_class}">{tier}</span></td>
  <td title="{p.get('title')}">{title}</td>
  <td>{p.get('year', 'N/A')}</td>
  <td>{score}</td>
  <td>{citations}</td>
  <td>{in_deg}/{out_deg}</td>
</tr>"""

        html += """</table>
</body>
</html>"""

        output_path = OUTPUT_DIR / f"journal_club_threshold_{threshold}.html"
        with open(output_path, "w") as f:
            f.write(html)
        print(f"✓ Saved journal_club_threshold_{threshold}.html ({len(papers)} papers)")


def main():
    print("=" * 60)
    print("Generating full corpus visualizations")
    print("=" * 60)

    generate_field_map_full()
    generate_coauthor_map_full()
    generate_journal_club_visualizations()

    print("\nDone! Generated files:")
    print("  - field_map_full.html (citation network + rankings)")
    print("  - coauthor_map_full.html (co-authorship network + rankings)")
    print("  - journal_club_threshold_*.html (4 versions)")


if __name__ == "__main__":
    main()
