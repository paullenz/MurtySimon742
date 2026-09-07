#!/usr/bin/env python3
"""Reassemble the exact n=27 candidate archive from checked GitHub parts."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()

def main():
    manifest=json.loads((ROOT/'PARTS.json').read_text());out=ROOT/manifest['archive']
    if out.exists():
        if out.stat().st_size==manifest['bytes'] and sha(out)==manifest['sha256']:
            print('Existing archive verified:',out);return
        raise ValueError('A different file already exists at the output path.')
    for part in manifest['parts']:
        path=ROOT/part['name']
        assert path.is_file() and path.stat().st_size==part['bytes'] and sha(path)==part['sha256'],part['name']
    with out.open('xb') as target:
        for part in manifest['parts']:
            with (ROOT/part['name']).open('rb') as source:
                for block in iter(lambda:source.read(1024*1024),b''):target.write(block)
    assert out.stat().st_size==manifest['bytes'] and sha(out)==manifest['sha256']
    print('Complete archive verified:',out)

if __name__=='__main__':main()
