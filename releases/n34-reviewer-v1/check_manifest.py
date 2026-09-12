#!/usr/bin/env python3
"""Check current release artifact hashes using only the standard library."""
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
manifest=json.loads((HERE/'MANIFEST.json').read_text())
for path,meta in manifest['artifacts'].items():
    raw=(ROOT/path).read_bytes()
    assert len(raw)==meta['bytes'],path
    assert hashlib.sha256(raw).hexdigest()==meta['sha256'],path
print('PASS:',len(manifest['artifacts']),'artifact hashes')
