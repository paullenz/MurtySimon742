#!/usr/bin/env python3
from pathlib import Path
import json,hashlib
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
data=json.loads((HERE/'MANIFEST.json').read_text())
for path,meta in data['artifacts'].items():
    raw=(ROOT/path).read_bytes()
    assert len(raw)==meta['bytes'] and hashlib.sha256(raw).hexdigest()==meta['sha256'],path
print('PASS',len(data['artifacts']),'artifact hashes; external review OPEN')
