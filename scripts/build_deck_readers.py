#!/usr/bin/env python3
"""Create reflowing HTML companions from the same rendered Marp slide bodies.
No rasterization, web requests, model calls, or JavaScript is required by readers.
"""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'course/decks/marp'
OUT = SRC / 'out'

class Slides(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.slides = []
        self.current = None
        self.skip = 0
        self.in_heading = False
        self.title = ''
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'section' and 'data-marpit-pagination' in a:
            self.current, self.title = [], ''
            return
        if self.current is None:
            return
        if tag in {'script','style','footer','header'}:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in {'h1','h2'}:
            self.in_heading = True
        tag = 'h2' if tag == 'h1' else tag
        allowed = {'id','class','href','src','alt','title','scope','colspan','rowspan','role','aria-label','aria-hidden'}
        clean = [(k,v) for k,v in attrs if k in allowed and v is not None]
        if tag == 'a':
            clean = [(k,v) for k,v in clean if not (k=='href' and v.lower().strip().startswith(('javascript:','data:')))]
        if tag == 'img':
            clean += [('loading','lazy'),('decoding','async')]
        self.current.append('<' + tag + ''.join(f' {k}="{escape(v,quote=True)}"' for k,v in clean) + '>')
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in {'img','br','hr','input','meta','link'}:
            self.handle_endtag(tag)
    def handle_endtag(self, tag):
        if self.current is None:
            return
        if tag == 'section':
            self.slides.append((''.join(self.current), self.title.strip()))
            self.current = None
            return
        if tag in {'script','style','footer','header'}:
            self.skip = max(0,self.skip-1)
            return
        if self.skip:
            return
        if tag in {'h1','h2'}:
            self.in_heading = False
        if tag not in {'img','br','hr','input','meta','link'}:
            self.current.append('</' + ('h2' if tag == 'h1' else tag) + '>')
    def handle_data(self, data):
        if self.current is not None and not self.skip:
            self.current.append(escape(data))
            if self.in_heading:
                self.title += data

def write_reader(source: Path):
    html_path = OUT / source.relative_to(SRC).with_suffix('').with_suffix('.html')
    if not html_path.exists():
        raise RuntimeError(f'Missing rendered deck: {html_path}')
    rendered = html_path.read_text(encoding='utf-8')
    slides = Slides(); slides.feed(rendered)
    if not slides.slides:
        raise RuntimeError(f'No slide sections: {html_path}')
    raw = re.sub(r'\A---\n.*?\n---\n','',source.read_text(encoding='utf-8'),count=1,flags=re.S)
    chunks = [s for s in re.split(r'^---\s*$',raw,flags=re.M) if s.strip()]
    if len(chunks) != len(slides.slides):
        raise RuntimeError(f'Source/render slide-count mismatch: {source}')
    reader = html_path.with_suffix('.reader.html')
    import os
    css = os.path.relpath(ROOT/'assets/css/deck-reader.css',reader.parent)
    title = slides.slides[0][1] or source.stem
    toc, sections = [], []
    for i,((body,heading),chunk) in enumerate(zip(slides.slides,chunks),1):
        label = heading or f'Slide {i}'
        toc.append(f'<li><a href="#slide-{i}">{i}. {escape(label)}</a></li>')
        notes = []
        for note in re.findall(r'<!--(.*?)-->',chunk,re.S):
            text = note.strip()
            if text and not re.match(r'^_?[\w-]+\s*:',text):
                notes.append(text)
        note_html = ''
        if notes:
            paragraphs = ''.join('<p>'+escape(n).replace('\n','<br>')+'</p>' for n in notes)
            note_html = '<details class="teaching-notes"><summary>Figure description and teaching notes</summary>'+paragraphs+'</details>'
        sections.append(f'<section class="reader-slide" id="slide-{i}" aria-label="Slide {i}: {escape(label,quote=True)}"><p class="slide-number">Slide {i} of {len(slides.slides)}</p>{body}{note_html}</section>')
    reader.write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} | Reading version</title><link rel="stylesheet" href="{escape(css,quote=True)}"></head>
<body><a class="reader-skip" href="#reading-content">Skip to slides</a><header class="reader-header"><p>NEUROTRAILBLAZERS · TEACHING MATERIALS</p><h1>{escape(title)}</h1><p>Reading version. Text reflows with your screen and zoom. Figures retain their available captions. Expand teaching notes for additional context and, where supplied, visual descriptions.</p><nav aria-label="Deck formats"><a href="{html_path.name}">Present slides</a><a href="https://www.neurotrailblazers.org/teaching/sessions/">Session kits</a></nav><details><summary>Contents · {len(slides.slides)} slides</summary><ol>{''.join(toc)}</ol></details></header>
<main id="reading-content" tabindex="-1">{''.join(sections)}</main><footer class="reader-footer">NeuroTrailblazers text: CC BY 4.0. Figures retain their individual credits. <a href="#top">Return to top</a></footer></body></html>'''.replace('<body>','<body id="top">'),encoding='utf-8')
    # Keyboard-accessible entry before the presentation UI, visible on focus.
    nav=f'<a class="nt-reader-link" href="{reader.name}">Read slides as a page</a>'
    nav_css='<style id="nt-reader-entry">.nt-reader-link{position:fixed;z-index:9999;left:12px;top:12px;transform:translateY(-150%);padding:12px 18px;background:#fff;color:#10303f;font:18px Arial,sans-serif;border:3px solid #0f6b73}.nt-reader-link:focus{transform:none}</style>'
    rendered=re.sub(r'<style id="nt-reader-entry">.*?</style>','',rendered,flags=re.S)
    rendered=re.sub(r'<a class="nt-reader-link"[^>]*>.*?</a>','',rendered,flags=re.S)
    rendered=rendered.replace('</head>',nav_css+'</head>').replace('<body>','<body>'+nav,1)
    html_path.write_text(rendered,encoding='utf-8')
    return len(slides.slides)

if __name__=='__main__':
    sources=sorted(SRC.rglob('*.marp.md'))
    count=sum(write_reader(source) for source in sources)
    print(f'Generated {len(sources)} reflowing readers from {count} rendered slides.')
