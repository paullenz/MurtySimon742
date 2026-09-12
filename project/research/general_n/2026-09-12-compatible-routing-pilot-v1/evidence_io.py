#!/usr/bin/env python3
"""Read the original losslessly encoded solver stream with both hash checks."""
from pathlib import Path
import base64,gzip,hashlib,json
HERE=Path(__file__).resolve().parent

def read_bytes(name):
    catalog=HERE/'EVIDENCE_STORAGE.json'
    entries=json.loads(catalog.read_text())['files'] if catalog.exists() else {}
    if name not in entries:return (HERE/name).read_bytes()
    meta=entries[name];stored=(HERE/meta['stored_file']).read_bytes()
    assert len(stored)==meta['stored_bytes'] and hashlib.sha256(stored).hexdigest()==meta['stored_sha256']
    raw=gzip.decompress(base64.b64decode(stored))
    assert len(raw)==meta['original_bytes'] and hashlib.sha256(raw).hexdigest()==meta['original_sha256']
    assert len(raw.splitlines())==meta['records']
    return raw

def read_records(name):return [json.loads(line) for line in read_bytes(name).splitlines()]
