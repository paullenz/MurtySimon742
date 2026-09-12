#!/usr/bin/env python3
"""Lossless study evidence reader; checks both stored and original hashes."""
from pathlib import Path
import base64
import gzip
import hashlib
import json
import sys

HERE=Path(__file__).resolve().parent


def read_bytes(name):
    catalog=HERE/'EVIDENCE_STORAGE.json'
    entries=json.loads(catalog.read_text())['files'] if catalog.exists() else {}
    if name not in entries:return (HERE/name).read_bytes()
    item=entries[name];data=(HERE/item['stored_file']).read_bytes()
    assert len(data)==item['stored_bytes'] and hashlib.sha256(data).hexdigest()==item['stored_sha256']
    original=gzip.decompress(base64.b64decode(data))
    assert len(original)==item['original_bytes'] and hashlib.sha256(original).hexdigest()==item['original_sha256']
    count=len(original.splitlines()) if item['format']=='jsonl' else len(json.loads(original))
    assert count==item['records']
    return original


def read_records(name):
    return [json.loads(line) for line in read_bytes(name).splitlines()]


if __name__=='__main__':
    assert len(sys.argv)==3,'usage: evidence_io.py ORIGINAL_NAME OUTPUT_PATH'
    Path(sys.argv[2]).write_bytes(read_bytes(sys.argv[1]))
