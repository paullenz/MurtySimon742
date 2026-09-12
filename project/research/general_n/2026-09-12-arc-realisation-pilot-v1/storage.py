#!/usr/bin/env python3
from pathlib import Path
import base64,gzip,hashlib,json,textwrap

def sha(raw):return hashlib.sha256(raw).hexdigest()

def write_model(path,model):
    raw=(json.dumps(model,sort_keys=True,separators=(',',':'))+'\n').encode()
    stored=('\n'.join(textwrap.wrap(base64.b64encode(gzip.compress(raw,mtime=0)).decode(),76))+'\n').encode()
    Path(path).write_bytes(stored)
    return dict(stored_file=Path(path).name,original_bytes=len(raw),original_sha256=sha(raw),stored_bytes=len(stored),stored_sha256=sha(stored))

def read_model(path,meta=None):
    stored=Path(path).read_bytes();raw=gzip.decompress(base64.b64decode(stored))
    if meta:
        assert len(stored)==meta['stored_bytes'] and sha(stored)==meta['stored_sha256']
        assert len(raw)==meta['original_bytes'] and sha(raw)==meta['original_sha256']
    return json.loads(raw)
