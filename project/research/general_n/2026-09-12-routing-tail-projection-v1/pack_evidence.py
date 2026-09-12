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
    for name in ('pilot_results.jsonl','profile_results.jsonl','state_comparison.json','boundary_results.jsonl','boundary_state_comparison.json'):
        original=(HERE/name).read_bytes();encoded=base64.encodebytes(gzip.compress(original,mtime=0))
        stored=name+'.gz.b64';(HERE/stored).write_bytes(encoded)
        assert gzip.decompress(base64.b64decode(encoded))==original
        fmt='jsonl' if name.endswith('.jsonl') else 'json'
        obj=json.loads(original) if fmt=='json' else None
        count=len(original.splitlines()) if fmt=='jsonl' else len(obj['records']) if isinstance(obj,dict) else len(obj)
        files[name]=dict(stored_file=stored,format=fmt,records=count,
            original_bytes=len(original),original_sha256=hashlib.sha256(original).hexdigest(),
            stored_bytes=len(encoded),stored_sha256=hashlib.sha256(encoded).hexdigest())
        if isinstance(obj,dict):files[name]['records_key']='records'
    report=dict(schema='routing-tail-projection-evidence-storage-v1',encoding='base64(gzip(original)); mtime=0',files=files)
    (HERE/'EVIDENCE_STORAGE.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
