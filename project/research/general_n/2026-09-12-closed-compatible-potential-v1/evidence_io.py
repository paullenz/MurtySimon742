#!/usr/bin/env python3
from pathlib import Path
import base64,gzip,hashlib,json
HERE=Path(__file__).resolve().parent

def read_bytes(name):
    p=HERE/'EVIDENCE_STORAGE.json';catalog=json.loads(p.read_text())['files'] if p.exists() else {}
    if name not in catalog:return (HERE/name).read_bytes()
    m=catalog[name];stored=(HERE/m['stored_file']).read_bytes()
    assert len(stored)==m['stored_bytes'] and hashlib.sha256(stored).hexdigest()==m['stored_sha256']
    raw=gzip.decompress(base64.b64decode(stored))
    assert len(raw)==m['original_bytes'] and hashlib.sha256(raw).hexdigest()==m['original_sha256']
    assert len(raw.splitlines())==m['lines']
    return raw

def records(name):return [json.loads(line) for line in read_bytes(name).splitlines()]
