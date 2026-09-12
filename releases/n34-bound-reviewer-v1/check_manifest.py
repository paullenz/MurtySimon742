#!/usr/bin/env python3
"""Check the exact release artifact bytes, using only the standard library."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
data = json.loads((HERE/'MANIFEST.json').read_text())
for path,expected in data['artifacts'].items():
    raw = (ROOT/path).read_bytes()
    assert len(raw)==expected['bytes'],path
    assert hashlib.sha256(raw).hexdigest()==expected['sha256'],path
print('PASS:',len(data['artifacts']),'artifact hashes')
