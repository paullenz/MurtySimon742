#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
manifest=json.loads((HERE/'MANIFEST.json').read_text())
for path,meta in manifest['artifacts'].items():
    data=(ROOT/path).read_bytes()
    assert len(data)==meta['bytes'] and hashlib.sha256(data).hexdigest()==meta['sha256'],path
print('PASS',len(manifest['artifacts']),'artifact hashes; external review OPEN')
