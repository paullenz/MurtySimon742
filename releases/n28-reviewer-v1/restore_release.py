#!/usr/bin/env python3
"""Recover exact authored reviewer sources; no proof search or compilation."""
from pathlib import Path,PurePosixPath
import base64,hashlib,io,json,lzma,tarfile
ROOT=Path(__file__).resolve().parent
def digest(b):return hashlib.sha256(b).hexdigest()
def main():
    m=json.loads((ROOT/'PUBLICATION_CAPSULE.json').read_text());texts=[]
    for e in m['parts']:
        b=(ROOT/e['path']).read_bytes()
        if len(b)!=e['bytes'] or digest(b)!=e['sha256']:raise ValueError('Part mismatch')
        texts.append(''.join(b.decode('ascii').split()))
    raw=base64.b64decode(''.join(texts),validate=True)
    if len(raw)!=m['compressed_bytes'] or digest(raw)!=m['compressed_sha256']:raise ValueError('Capsule mismatch')
    files={}
    with tarfile.open(fileobj=io.BytesIO(lzma.decompress(raw)),mode='r:') as tf:
        for x in tf.getmembers():
            p=PurePosixPath(x.name)
            if not x.isfile() or p.is_absolute() or '..' in p.parts or x.name in files:raise ValueError('Unsafe member')
            files[x.name]=tf.extractfile(x).read()
    if digest(files['SOURCE_MANIFEST.json'])!=m['source_manifest_sha256']:raise ValueError('Source manifest mismatch')
    expected=json.loads(files['SOURCE_MANIFEST.json'])['files']
    if set(files)!=set(expected)|{'SOURCE_MANIFEST.json'} or len(files)!=m['source_files_including_manifest']:raise ValueError('Member coverage')
    for name,e in expected.items():
        b=files[name]
        if len(b)!=e['bytes'] or digest(b)!=e['sha256']:raise ValueError('Member mismatch: '+name)
    for name,b in files.items():
        p=ROOT/name
        if p.exists() and (not p.is_file() or p.is_symlink() or p.read_bytes()!=b):raise ValueError('Refusing to overwrite changed source: '+name)
        if any(q.is_symlink() for q in p.parents):raise ValueError('Symlink parent')
    for name,b in files.items():
        p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
    print(json.dumps({'recovered_source_files':len(files),'all_hashes_match':True,'proof_calculation_performed':False}))
if __name__=='__main__':main()
