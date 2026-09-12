#!/usr/bin/env python3
"""Lossless portable text storage for the two full JSONL certificate streams."""
import base64
import gzip
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
out=dict(schema='n34-equality-certificate-storage-v1',encoding='base64(gzip(JSONL)); gzip mtime=0',files={})
for stage in ('fixed','adaptive'):
    source=HERE/(stage+'.jsonl')
    raw=source.read_bytes()
    rows=[json.loads(line) for line in raw.splitlines() if line.strip()]
    compressed=gzip.compress(raw,compresslevel=9,mtime=0)
    encoded=base64.encodebytes(compressed)
    assert gzip.decompress(base64.b64decode(encoded))==raw
    target=HERE/(stage+'.jsonl.gz.b64')
    target.write_bytes(encoded)
    out['files'][stage]=dict(original_file=source.name,stored_file=target.name,
        original_bytes=len(raw),original_sha256=hashlib.sha256(raw).hexdigest(),
        stored_bytes=len(encoded),stored_sha256=hashlib.sha256(encoded).hexdigest(),records=len(rows))
(HERE/'CERTIFICATE_STORAGE.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
