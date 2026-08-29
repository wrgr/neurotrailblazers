#!/usr/bin/env python3
"""Generates a high-resolution, self-clustered SVG network graph with weighted directed citation edges."""
import json
import math
import random
import xml.sax.saxutils as saxutils
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

def escape_xml(s: str) -> str:
    if not s: return ""
    return saxutils.escape(s)

def main():
    c500_path = PROJECT_ROOT / "_data/corpus_500.json"
    data = json.loads(c500_path.read_text())
    papers = data["papers"]
    doi_map = {p["doi"].lower(): p for p in papers}

    # Load edges
    edge_path = SCRIPT_DIR / "corpus_citation_edges.json"
    edge_data = json.loads(edge_path.read_text()) if edge_path.exists() else {"edges": []}
    
    # Filter edges where both source and target are in Top 500
    top500_edges = []
    for e in edge_data.get("edges", []):
        s_doi = e["source"].lower()
        t_doi = e["target"].lower()
        if s_doi in doi_map and t_doi in doi_map and s_doi != t_doi:
            top500_edges.append((s_doi, t_doi))

    print(f"Generating Self-Clustered SVG Graph with {len(papers)} nodes and {len(top500_edges)} directed edges...")

    CATEGORIES = [
        "circuit-structure", "pipeline", "physiology", "behaviour",
        "imaging", "cell-types", "neuroanatomy", "synthesis",
        "dataset", "neuroai", "health", "training-outreach"
    ]
    
    CATEGORY_COLORS = {
        "circuit-structure": "#2563eb",
        "pipeline": "#0891b2",
        "physiology": "#059669",
        "behaviour": "#d97706",
        "imaging": "#7c3aed",
        "cell-types": "#db2777",
        "neuroanatomy": "#4f46e5",
        "synthesis": "#4b5563",
        "dataset": "#0284c7",
        "neuroai": "#9333ea",
        "health": "#dc2626",
        "training-outreach": "#16a34a"
    }

    width = 1200
    height = 900
    cx = width / 2
    cy = height / 2

    # Initialize nodes with radial category layout
    nodes = {}
    random.seed(42)
    for idx, p in enumerate(papers):
        cat = p.get("classification", "circuit-structure")
        cat_idx = CATEGORIES.index(cat) if cat in CATEGORIES else 0
        angle = (cat_idx / len(CATEGORIES)) * 2 * math.pi - math.pi / 2
        r = 280 + random.gauss(0, 45)
        
        in_deg = p.get("in_degree", 0)
        out_deg = p.get("out_degree", 0)
        tot_deg = in_deg + out_deg
        radius = max(3.5, min(14.0, 3.5 + math.sqrt(tot_deg) * 1.3))

        nodes[p["doi"].lower()] = {
            "doi": p["doi"].lower(),
            "title": p.get("title", ""),
            "authors": p.get("authors", ""),
            "year": p.get("year", 2024),
            "cat": cat,
            "color": CATEGORY_COLORS.get(cat, "#64748b"),
            "x": cx + math.cos(angle) * r,
            "y": cy + math.sin(angle) * r,
            "vx": 0.0,
            "vy": 0.0,
            "radius": radius,
            "tot_deg": tot_deg
        }

    # Run Force Simulation (Self-Clustering physics)
    node_list = list(nodes.values())
    iterations = 120
    for it in range(iterations):
        alpha = (1.0 - it / iterations)
        
        # 1. Spring attraction along citation edges
        for s_doi, t_doi in top500_edges:
            s = nodes[s_doi]
            t = nodes[t_doi]
            dx = t["x"] - s["x"]
            dy = t["y"] - s["y"]
            dist = math.hypot(dx, dy) or 1.0
            desired_dist = 80.0
            force = (dist - desired_dist) * 0.03 * alpha
            fx = (dx / dist) * force
            fy = (dy / dist) * force
            s["vx"] += fx
            s["vy"] += fy
            t["vx"] -= fx
            t["vy"] -= fy

        # 2. Coulomb Repulsion
        for i in range(len(node_list)):
            n1 = node_list[i]
            # Center gravity
            n1["vx"] -= (n1["x"] - cx) * 0.003 * alpha
            n1["vy"] -= (n1["y"] - cy) * 0.003 * alpha

            for j in range(i + 1, len(node_list)):
                n2 = node_list[j]
                rx = n2["x"] - n1["x"]
                ry = n2["y"] - n1["y"]
                r2 = rx * rx + ry * ry + 80.0
                if r2 < 35000.0:
                    rep_force = (2400.0 / r2) * alpha
                    r = math.sqrt(r2)
                    rfx = (rx / r) * rep_force
                    rfy = (ry / r) * rep_force
                    n1["vx"] -= rfx
                    n1["vy"] -= rfy
                    n2["vx"] += rfx
                    n2["vy"] += rfy

        # Update positions
        for n in node_list:
            n["vx"] *= 0.85
            n["vy"] *= 0.85
            n["x"] += n["vx"]
            n["y"] += n["vy"]

    # Build SVG
    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background:#ffffff; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif;">')
    
    svg_lines.append(f'''
    <defs>
      <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
        <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.18"/>
      </filter>
      <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#94a3b8" fill-opacity="0.6"/>
      </marker>
    </defs>
    
    <!-- Background grid & Header -->
    <rect width="{width}" height="{height}" fill="#ffffff"/>
    <text x="{cx}" y="42" text-anchor="middle" font-size="22" font-weight="700" fill="#0f172a">Top 500 Connectomics Self-Clustered Citation Network</text>
    <text x="{cx}" y="66" text-anchor="middle" font-size="13" fill="#64748b">Self-Organizing Force Physics &#8226; Directed Citation Edges (N = {len(top500_edges)}) &#8226; 12 Domain Color Cues</text>
    ''')

    # Draw Directed Citation Edges
    for s_doi, t_doi in top500_edges:
        s = nodes[s_doi]
        t = nodes[t_doi]
        svg_lines.append(f'<line x1="{s["x"]:.1f}" y1="{s["y"]:.1f}" x2="{t["x"]:.1f}" y2="{t["y"]:.1f}" stroke="#94a3b8" stroke-opacity="0.22" stroke-width="0.75" marker-end="url(#arrow)"/>')

    # Sort nodes so larger landmark nodes draw on top
    sorted_nodes = sorted(node_list, key=lambda n: n["radius"])

    # Draw Nodes
    for n in sorted_nodes:
        clean_title = escape_xml(n["title"])
        clean_cat = escape_xml(n["cat"])
        svg_lines.append(f'<circle cx="{n["x"]:.1f}" cy="{n["y"]:.1f}" r="{n["radius"]:.1f}" fill="{n["color"]}" fill-opacity="0.88" stroke="#ffffff" stroke-width="1.2" filter="url(#shadow)">')
        svg_lines.append(f'  <title>{clean_title} ({n["year"]}) - {clean_cat} (Degree: {n["tot_deg"]})</title>')
        svg_lines.append(f'</circle>')

    # Landmark labels for top cited papers
    landmarks = sorted(node_list, key=lambda x: -x["tot_deg"])[:16]
    for lm in landmarks:
        title_short = lm["title"]
        if len(title_short) > 28:
            title_short = title_short[:27] + "…"
        author_last = lm["authors"].split(";")[0].split(",")[0].strip() if lm["authors"] else ""
        label_text = f"{author_last} ({lm['year']})" if author_last else f"{lm['year']}"
        label_clean = escape_xml(label_text)
        
        svg_lines.append(f'<text x="{lm["x"] + lm["radius"] + 4:.1f}" y="{lm["y"] + 3:.1f}" font-size="9" font-weight="600" fill="#1e293b" stroke="#ffffff" stroke-width="2.5" paint-order="stroke fill">{label_clean}</text>')

    # Footer Legend
    svg_lines.append(f'''
    <rect x="40" y="{height - 48}" width="{width - 80}" height="32" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
    <text x="{cx}" y="{height - 28}" text-anchor="middle" font-size="11" fill="#475569">
      Arrows Point from Citing Paper &#8594; Cited Paper &#8226; Spring Force Pulls Citing Papers Together &#8226; Colors = 12 Domain Categories
    </text>
    </svg>
    ''')

    out_svg = SCRIPT_DIR / "corpus_500_network_graph.svg"
    out_svg.write_text("\n".join(svg_lines))
    print(f"Successfully generated self-clustered SVG network graph: {out_svg} ({out_svg.stat().st_size} bytes).")

if __name__ == "__main__":
    main()
