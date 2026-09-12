#!/usr/bin/env python3
"""Preserve the exact original solver vectors, failures and timing fields."""
from pathlib import Path
import base64,gzip,hashlib,json
HERE=Path(__file__).resolve().parent

if __name__=='__main__':
    name='pilot_results.jsonl';raw=(HERE/name).read_bytes();encoded=base64.encodebytes(gzip.compress(raw,mtime=0))
    stored=name+'.gz.b64';(HERE/stored).write_bytes(encoded)
    assert gzip.decompress(base64.b64decode(encoded))==raw
    meta=dict(stored_file=stored,format='jsonl',records=len(raw.splitlines()),original_bytes=len(raw),original_sha256=hashlib.sha256(raw).hexdigest(),
              stored_bytes=len(encoded),stored_sha256=hashlib.sha256(encoded).hexdigest())
    (HERE/'EVIDENCE_STORAGE.json').write_text(json.dumps(dict(schema='compatible-routing-evidence-v1',files={name:meta}),indent=2)+'\n')
    print(json.dumps(meta,indent=2))
