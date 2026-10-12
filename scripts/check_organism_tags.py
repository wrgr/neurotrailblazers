#!/usr/bin/env python3
"""Species must be named explicitly; cortical anatomy alone is not mouse evidence."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'corpus_curation'))
from classify_engine import extract_organisms, normalize_existing_organisms

cases = {
    'Rat visual cortex': ['rat'],
    'Somatosensory cortex': ['none'],
    'Barrel cortex': ['none'],
    'Mouse and rat visual cortex': ['mouse', 'rat'],
    'Macaque visual cortex': ['macaque'],
    'Drosophila visual cortex': ['fly'],
}
for text, expected in cases.items():
    assert extract_organisms(text) == expected, (text, extract_organisms(text), expected)
assert normalize_existing_organisms(['mouse', 'rat'], 'Rat visual cortex') == ['rat']
assert normalize_existing_organisms(['mouse'], 'Somatosensory cortex') == ['none']
assert normalize_existing_organisms(['mouse', 'rat'], 'Mouse and rat visual cortex') == ['mouse', 'rat']
print('PASS organism tags: cortical regions do not imply mouse; regeneration preserves corrected tags')
