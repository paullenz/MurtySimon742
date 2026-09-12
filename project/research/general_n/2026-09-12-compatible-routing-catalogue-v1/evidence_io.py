#!/usr/bin/env python3
"""Prefer hash-verified encoded evidence; raw files are discovery fallbacks."""
from pathlib import Path
import base64,gzip,hashlib,json
HERE=Path(__file__).resolve().parent

def read_bytes(name):
    path=HERE/'EVIDENCE_STORAGE.json'
    entries=json.loads(path.read_text())['files'] if path.exists() else {}
    if name not in entries:return (HERE/name).read_bytes()
    meta=entries[name];stored=(HERE/meta['stored_file']).read_bytes()
    assert len(stored)==meta['stored_bytes'] and hashlib.sha256(stored).hexdigest()==meta['stored_sha256']
    raw=gzip.decompress(base64.b64decode(stored))
    assert len(raw)==meta['original_bytes'] and hashlib.sha256(raw).hexdigest()==meta['original_sha256']
    assert len(raw.splitlines())==meta['lines']
    return raw

def records(name):return [json.loads(line) for line in read_bytes(name).splitlines()]
