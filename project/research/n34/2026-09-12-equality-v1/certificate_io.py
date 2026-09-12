#!/usr/bin/env python3
"""Read the exact stored JSONL bytes using only the Python standard library."""
import base64
import gzip
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent


def read_stage(stage):
    assert stage in ('fixed','adaptive')
    index=HERE/'CERTIFICATE_STORAGE.json'
    if index.exists():
        meta=json.loads(index.read_text())['files'][stage]
        encoded=(HERE/meta['stored_file']).read_bytes()
        assert hashlib.sha256(encoded).hexdigest()==meta['stored_sha256']
        raw=gzip.decompress(base64.b64decode(encoded,validate=False))
        assert len(raw)==meta['original_bytes']
        assert hashlib.sha256(raw).hexdigest()==meta['original_sha256']
        rows=[json.loads(line) for line in raw.splitlines() if line.strip()]
        assert len(rows)==meta['records']
        return rows
    # Discovery-time input, before the immutable storage package is created.
    return [json.loads(line) for line in (HERE/(stage+'.jsonl')).read_text().splitlines() if line.strip()]
