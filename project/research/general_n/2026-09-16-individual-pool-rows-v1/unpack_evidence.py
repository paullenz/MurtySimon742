#!/usr/bin/env python3
"""Extract recorded evidence into recorded/; verify each file before writing."""
import base64, gzip, hashlib, json
from pathlib import Path
root=Path(__file__).resolve().parent
bundle=json.loads(gzip.decompress(base64.b64decode((root/'EVIDENCE.json.gz.b64').read_bytes())))
items=[]
for name,text in bundle['files'].items():
    if Path(name).name!=name or name in ('.','..'):
        raise ValueError('Unsafe evidence filename')
    data=text.encode('utf-8')
    if hashlib.sha256(data).hexdigest()!=bundle['sha256'][name]:
        raise ValueError('Evidence digest mismatch: '+name)
    items.append((name,data))
out=root/'recorded';out.mkdir(exist_ok=True)
for name,data in items:
    path=out/name
    if path.exists() and path.read_bytes()!=data:
        raise FileExistsError('Refusing to overwrite different evidence: '+name)
    path.write_bytes(data)
print('Verified and extracted',len(items),'recorded evidence files into',out)
