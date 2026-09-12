#!/usr/bin/env python3
"""Losslessly archive all original streams with exact recovery metadata."""
from pathlib import Path
import base64,gzip,hashlib,json,textwrap
HERE=Path(__file__).resolve().parent
FILES=['pool_inputs.jsonl','engine_input.txt','frontier_results.jsonl','survivors.json','template_coverage.json']

def main():
    files={}
    for name in FILES:
        raw=(HERE/name).read_bytes();encoded=('\n'.join(textwrap.wrap(base64.b64encode(gzip.compress(raw,mtime=0)).decode(),76))+'\n').encode()
        stored=name+'.gz.b64';(HERE/stored).write_bytes(encoded)
        assert gzip.decompress(base64.b64decode(encoded))==raw
        files[name]=dict(stored_file=stored,original_bytes=len(raw),original_sha256=hashlib.sha256(raw).hexdigest(),
            stored_bytes=len(encoded),stored_sha256=hashlib.sha256(encoded).hexdigest(),lines=len(raw.splitlines()))
    report=dict(schema='compatible-routing-catalogue-evidence-v1',encoding='gzip mtime=0, base64 wrapped at 76 characters',files=files,
        note='All inputs, evaluated gaps, stop points, survivors and template coverage are recoverable exactly. Original runtime and logs are preserved separately.')
    (HERE/'EVIDENCE_STORAGE.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
