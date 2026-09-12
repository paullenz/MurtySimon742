#!/usr/bin/env python3
from pathlib import Path
import base64,gzip,hashlib,json,textwrap
HERE=Path(__file__).resolve().parent
FILES=['pool_inputs.jsonl','engine_input.txt','frontier_results.jsonl','reference_results.jsonl','survivors.json']

def main():
    files={};byhash={}
    for name in FILES:
        raw=(HERE/name).read_bytes();digest=hashlib.sha256(raw).hexdigest()
        if digest in byhash:stored,encoded=byhash[digest]
        else:
            stored=name+'.gz.b64';encoded=('\n'.join(textwrap.wrap(base64.b64encode(gzip.compress(raw,mtime=0)).decode(),76))+'\n').encode()
            (HERE/stored).write_bytes(encoded);byhash[digest]=stored,encoded
        assert gzip.decompress(base64.b64decode(encoded))==raw
        files[name]=dict(stored_file=stored,original_bytes=len(raw),original_sha256=digest,stored_bytes=len(encoded),stored_sha256=hashlib.sha256(encoded).hexdigest(),lines=len(raw.splitlines()))
    assert files['frontier_results.jsonl']['stored_file']==files['reference_results.jsonl']['stored_file']
    report=dict(schema='closed-compatible-potential-evidence-v1',encoding='gzip mtime=0, base64 wrapped at 76 characters',files=files,
        note='Five logical streams, four unique stored streams. The independently generated result streams are byte-identical and share storage. Separate original logs and timings are preserved.')
    (HERE/'EVIDENCE_STORAGE.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
