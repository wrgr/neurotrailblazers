#!/usr/bin/env python3
"""One-time, guarded source migration. Removed before the review commit."""
from pathlib import Path

def edit(path, old, new):
    p=Path(path); text=p.read_text(encoding='utf-8')
    if old not in text: raise RuntimeError('Source changed: '+path)
    p.write_text(text.replace(old,new),encoding='utf-8')

edit('_layouts/default.html', '    <link rel="stylesheet" href="{{ \'/assets/css/usability.css\' | relative_url }}?v={{ site.time | date: \'%s\' }}">', '    <link rel="stylesheet" href="{{ \'/assets/css/usability.css\' | relative_url }}?v={{ site.time | date: \'%s\' }}">\n    <link rel="stylesheet" href="{{ \'/assets/css/visual-refresh.css\' | relative_url }}?v={{ site.time | date: \'%s\' }}">')
edit('scripts/generate_module_teaching_materials.rb', "require 'date'", "require 'date'\nrequire_relative 'lib/deck_design'")
edit('scripts/generate_module_teaching_materials.rb', '  # ---- Ready-to-run session kit', '  DeckDesign.apply(marp_path, num)\n\n  # ---- Ready-to-run session kit')
edit('scripts/generate_module_teaching_materials.rb', '>Open slides</a>', '>Present slides</a>\n        <a class="resource-link" href="{{ \'/course/decks/marp/out/modules/module#{num}.reader.html\' | relative_url }}">Read slides as a page</a>')
p=Path('scripts/generate_module_teaching_materials.rb'); s=p.read_text(encoding='utf-8'); a=s.index("sessions_index = File.join(SESSION_DIR, 'index.md')"); b=s.index('\nMD',a)+3; p.write_text(s[:a]+'# Preserve the hand-maintained, searchable session catalog from PR 188.\n'+s[b:],encoding='utf-8')
edit('scripts/render_marp.sh', '# Only an HTML render refreshes the manifest:', '# Build reflowing text/figure companions from the same rendered slide bodies.\nif [ "$DO_HTML" -eq 1 ]; then\n  python3 "$ROOT_DIR/scripts/build_deck_readers.py"\nfi\n\n# Only an HTML render refreshes the manifest:')
edit('scripts/render_marp.sh', '"sources": sources, "themes": themes}', '"sources": sources, "themes": themes,\n                "reader_generator": hashlib.sha256((src_dir.parents[2] / "scripts/build_deck_readers.py").read_bytes()).hexdigest()}')
edit('scripts/check_deck_freshness.rb', 'problems = []', 'problems = []\nreader_generator = ROOT.join("scripts/build_deck_readers.py")\nproblems << "reader generator changed since last render" unless manifest["reader_generator"] == Digest::SHA256.hexdigest(reader_generator.binread)')
edit('.github/workflows/validate.yml', '      - name: Site paths in code spans', '      - name: Visual teaching data and reading versions\n        run: ruby scripts/check_visual_design.rb\n\n      - name: Site paths in code spans')
edit('.github/workflows/validate.yml', '      - name: Internal link audit', '      - name: Card geometry and slide reading accessibility\n        run: NODE_PATH="$RUNNER_TEMP/research-browser/node_modules" node scripts/check_visual_design.cjs\n\n      - name: Internal link audit')
p=Path('course/decks/marp/theme/neurotrailblazers.css')
p.write_text(p.read_text(encoding='utf-8')+'''
/* Teaching figures are content, not decoration. One question beside each visual. */
section.visual-lesson { font-size:28px; padding:38px 52px 90px; }
section.visual-lesson h2 { font-size:40px; margin-bottom:12px; }
.visual-lead { font-size:25px; margin-bottom:16px; }
.visual-images { display:flex; gap:24px; justify-content:center; align-items:flex-start; }
.visual-images figure { flex:1 1 0; min-width:0; text-align:center; }
.visual-images img { height:345px; max-width:100%; object-fit:contain; }
.visual-images figcaption { font-size:18px; margin-top:6px; }
.visual-question { margin-top:18px; padding:10px 16px; background:var(--nt-mist); border-left:4px solid var(--nt-teal); font-size:24px; line-height:1.3; }
.visual-steps { display:flex; gap:20px; padding:0; margin:24px 0 32px; list-style:none; }
.visual-steps li { flex:1 1 0; min-width:0; border-top:4px solid var(--nt-teal); padding:20px 18px; background:var(--nt-mist); }
.visual-steps h3 { font-size:27px; margin:12px 0; }
.visual-steps p { font-size:25px; margin:0; }
.step-number { display:block; font-size:42px; line-height:1; color:var(--nt-teal-deep); font-weight:700; }
.visual-code { display:grid; grid-template-columns:3fr 2fr; gap:24px; margin:26px 0; }
.visual-code pre { font-size:23px; white-space:pre-wrap; }
.visual-code .output { background:var(--nt-mist); color:var(--nt-ink); font-family:var(--font-body); font-size:30px; }
.visual-lesson table { margin:32px 0; font-size:28px; }
.visual-lesson td, .visual-lesson th { padding:18px; }
.visual-tree { text-align:center; font-size:25px; margin:20px 0; }
.visual-tree p { margin:0 auto; }
.tree-root, .tree-fork { background:var(--nt-mist); width:320px; border:2px solid var(--nt-teal); padding:8px; }
.tree-stem { padding:8px; }
.tree-children { display:flex; width:760px; margin:0 auto; gap:32px; padding-top:16px; }
.tree-children p { flex:1; border-top:3px solid var(--nt-teal); padding:8px; }
section p.source { font-size:16px; }
section.title.nanoscale p.source { font-size:16px; }
section footer, section header, section::after { font-size:16px; }
''',encoding='utf-8')
