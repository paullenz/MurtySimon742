#!/usr/bin/env python3
"""Preserve exact raw study streams using deterministic gzip/base64 storage."""
from pathlib import Path
import base64
import gzip
import hashlib
import json

HERE=Path(__file__).resolve().parent


def main():
    files={}
    for name in ('pilot_results.jsonl','frontier_results.jsonl'):
        original=(HERE/name).read_bytes();encoded=base64.encodebytes(gzip.compress(original,mtime=0))
        stored=name+'.gz.b64';(HERE/stored).write_bytes(encoded)
        assert gzip.decompress(base64.b64decode(encoded))==original
        fmt='jsonl' if name.endswith('.jsonl') else 'json'
        count=len(original.splitlines()) if fmt=='jsonl' else len(json.loads(original))
        files[name]=dict(stored_file=stored,format=fmt,records=count,
            original_bytes=len(original),original_sha256=hashlib.sha256(original).hexdigest(),
            stored_bytes=len(encoded),stored_sha256=hashlib.sha256(encoded).hexdigest())
    report=dict(schema='joint-routing-evidence-storage-v1',encoding='base64(gzip(original)); mtime=0',files=files)
    (HERE/'EVIDENCE_STORAGE.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
