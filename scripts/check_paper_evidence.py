#!/usr/bin/env python3
"""Dependency-free source/schema checks; not a substitute for a rendered-site test.

Run: python3 scripts/check_paper_evidence.py
Records must be DOI-specific and source-located. A broad method/category is
never a lookup key. This checker does not establish scientific truth.
"""
from __future__ import annotations
import datetime as dt
import json
import hashlib
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ('contribution', 'result', 'context', 'limitation', 'source_url',
            'source_locator', 'evidence_basis', 'checked_by', 'checked_on')


def eligible(doi: str, record: object) -> bool:
    """Schema eligibility only. Source review is a separate editorial action."""
    if not isinstance(record, dict):
        return False
    key = doi.strip().lower()
    url = urlparse(record.get('source_url', '')) if isinstance(record.get('source_url'), str) else None
    return bool(key.startswith('10.') and '/' in key and record.get('doi') == key
                and record.get('status') == 'source_checked'
                and all(isinstance(record.get(k), str) and record[k].strip() for k in REQUIRED)
                and url and url.scheme == 'https' and url.netloc and not url.username and not url.password)


def check() -> int:
    records = json.loads((ROOT / '_data/paper_evidence.json').read_text())
    assert isinstance(records, dict), 'Evidence must be a DOI-keyed object'
    for key, record in records.items():
        assert key.startswith('10.') and key == key.strip().lower(), key
        assert eligible(key, record), f'Incomplete or mismatched evidence: {key}'
        url = urlparse(record['source_url'])
        assert url.netloc and not url.username and not url.password, key
        dt.date.fromisoformat(record['checked_on'])

    relationships = json.loads((ROOT / '_data/paper_publication_links.json').read_text())
    for key, pair in relationships.items():
        assert key == pair['doi'] == key.strip().lower(), key
        assert pair['kind'] in ('original', 'correction'), key
        assert pair[pair['kind']]['doi'] == key, key
        assert pair['original']['doi'] != pair['correction']['doi'], key
        dt.date.fromisoformat(pair['checked_on'])
        assert pair['correction_note'].strip() and pair['source_locator'].strip(), key
        source = urlparse(pair['relationship_source_url'])
        assert source.scheme == 'https' and source.netloc and not source.username and not source.password, key
        for role in ('original', 'correction'):
            publication = pair[role]
            assert publication['title'].strip(), key
            assert publication['url'] == 'https://doi.org/' + publication['doi'], key
            for field in ('url', 'full_text_url'):
                if publication.get(field):
                    url = urlparse(publication[field])
                    assert url.scheme == 'https' and url.netloc and not url.username and not url.password, key
            pdf = publication.get('pdf_url')
            if pdf and pdf.startswith('/'):
                assert re.fullmatch(r'/assets/papers/[A-Za-z0-9_-][A-Za-z0-9._-]*\.pdf', pdf), key
                payload = (ROOT / pdf.lstrip('/')).read_bytes()
                assert payload.startswith(b'%PDF-'), key
                assert hashlib.sha256(payload).hexdigest() == publication['pdf_sha256'], key
                assert publication['pdf_license'].strip(), key
            elif pdf:
                url = urlparse(pdf)
                assert url.scheme == 'https' and url.netloc and not url.username and not url.password, key
            reciprocal = relationships[publication['doi']]
            assert reciprocal['kind'] == role, key
            assert reciprocal['original'] == pair['original'] and reciprocal['correction'] == pair['correction'], key

    card = (ROOT / '_includes/cards/journal-paper-card.html').read_text()
    graph = (ROOT / 'technical-training/journal-club/graph-data.json').read_text()
    gate = (ROOT / '_includes/papers/evidence-gate.html').read_text()
    for path, source in [('card', card), ('graph', graph)]:
        assert 'include papers/evidence-gate.html paper=p' in source, path
        for raw in ('p.ocar', 'p.summaries', 'p.plain_language_summary',
                    'p.streams', 'p.key_figures', 'p.discussion_prompts'):
            assert raw not in source, f'{path} publishes legacy field {raw}'
    for field in ('ocar', 'summaries', 'discussion_prompts'):
        assert f'"{field}":null' in graph, field
    assert '"summary":{{ evidence_summary | jsonify }}' in graph
    assert 'evidence_summary | escape' in graph, 'Legacy graph renders summary as HTML'
    assert 'checked_paper_evidence = nil' in gate, 'Reset evidence between papers'
    assert gate.index('checked_paper_evidence = nil') < gate.index('evidence_candidate =')
    assert 'evidence_candidate.doi == evidence_key' in gate
    assert "evidence_scheme == 'https://'" in gate
    for field in REQUIRED:
        assert field in gate, f'Gate omits {field}'
    for attribute in ('data-dataset=', 'data-method=', 'data-axis='):
        assert attribute not in card, attribute

    export = (ROOT / '_includes/papers/corpus-export.json').read_text()
    assert 'include papers/evidence-gate.html paper=p' in export
    assert '"evidence":{{ checked_paper_evidence | jsonify }}' in export
    for raw in ('p.ocar', 'p.summaries', 'p.plain_language_summary', 'p.streams'):
        assert raw not in export, raw
    page = (ROOT / 'technical-training/journal-club/graph.md').read_text()
    for raw in ('p.ocar', 'd.ocar', 'p.summaries', 'Ground-Truth', 'curated milestone publications'):
        assert raw not in page, raw
    assert 'evidenceApi.reviewPrompt' in page and 'evidenceApi.render' in page
    assert 'd.summary' not in page, 'Generated annotations must not be searched'
    config = (ROOT / '_config.yml').read_text()
    for tier in (500, 1000, 2000):
        assert f'  - data/corpus_{tier}.json' in config
        endpoint = ROOT / f'technical-training/journal-club/exports/corpus_{tier}.json'
        assert f'permalink: /data/corpus_{tier}.json' in endpoint.read_text()
    for generator in ('fast_ocar_generator.py', 'generate_ocar_all_2000.py', 'generate_ocar_corpus_500.py'):
        source = (ROOT / 'scripts/corpus_curation' / generator).read_text()
        assert 'raise SystemExit(' in source and 'RETIRED' in source and len(source) < 1000

    first_key, first = next(iter(records.items()))
    assert eligible(first_key, first)
    assert not eligible('10.9999/unrelated-sem-paper', first)
    assert not eligible(first_key, {'classification': 'imaging', 'method': 'SEM'})
    assert not eligible(first_key, dict(first, status='generated'))
    assert not eligible(first_key, dict(first, source_url='javascript:alert(1)'))
    for field in REQUIRED:
        bad = dict(first)
        bad[field] = ''
        assert not eligible(first_key, bad), field
    assert not eligible(first_key, None)
    print(f'PASS: {len(records)} evidence record; cards, graph, prompts, exports and retired generators; '
          f'{len(REQUIRED) + 6} eligibility fixtures. '
          'These are source/schema checks, not rendered-site or scientific validation.')
    print(f'PASS: {len(relationships)} DOI-scoped reciprocal publication links; safe URLs and unchanged local PDF checksums.')
    return 0


if __name__ == '__main__':
    raise SystemExit(check())
