#!/usr/bin/env python3
"""Restore the v3 package from hash-pinned base64/xz parts; standard library only."""
from __future__ import annotations
import argparse, base64, hashlib, json, lzma, sys
from pathlib import Path

def check(data:bytes,expected:str,label:str)->None:
    if hashlib.sha256(data).hexdigest()!=expected:
        raise ValueError('Checksum mismatch: '+label)

def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output',type=Path,help='New directory; existing paths are never overwritten')
    args=parser.parse_args();root=Path(__file__).resolve().parent
    meta=json.loads((root/'PRESERVATION.json').read_text(encoding='utf-8'))
    chunks=[]
    for row in meta['parts']:
        data=(root/row['path']).read_bytes()
        if len(data)!=row['bytes']:raise ValueError('Size mismatch: '+row['path'])
        check(data,row['sha256'],row['path']);chunks.append(data.strip())
    packed=base64.b64decode(b''.join(chunks),validate=True)
    check(packed,meta['decoded_xz_sha256'],'xz payload')
    raw=lzma.decompress(packed,memlimit=256*1024*1024)
    check(raw,meta['json_sha256'],'decoded JSON')
    bundle=json.loads(raw)
    if bundle['format']!='murty-simon-v3-files-v2':raise ValueError('Unknown package format')
    files={}
    for name,item in bundle['files'].items():
        path=Path(name)
        if path.is_absolute() or '..' in path.parts or len(path.parts)!=1:
            raise ValueError('Unsafe file path')
        if set(item)=={'text'}:text=item['text']
        elif set(item)=={'json'}:text=json.dumps(item['json'],sort_keys=True,indent=2)
        else:raise ValueError('Unknown file encoding')
        files[name]=text.encode('utf-8')
    check(files['MANIFEST.json'],meta['manifest_sha256'],'manifest')
    manifest=json.loads(files['MANIFEST.json'])
    for row in manifest['files']:
        data=files[row['path']]
        if len(data)!=row['bytes']:raise ValueError('Restored size mismatch')
        check(data,row['sha256'],row['path'])
    output=args.output.resolve()
    if output.exists():raise ValueError('Output path already exists')
    output.mkdir(parents=True)
    for name,data in files.items():(output/name).write_bytes(data)
    print(f'Restored {len(files)} files; all transport and manifest hashes passed.')
    print('Mathematical validity and independent review remain separate from these checks.')
if __name__=='__main__':
    try:main()
    except (OSError,ValueError,KeyError,lzma.LZMAError) as exc:
        print('ERROR:',exc,file=sys.stderr);sys.exit(1)
