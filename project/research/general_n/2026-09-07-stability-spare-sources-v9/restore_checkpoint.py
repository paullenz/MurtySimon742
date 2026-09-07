#!/usr/bin/env python3
"""Recover hash-pinned v9 authored sources; never performs mathematical checking."""
from pathlib import Path, PurePosixPath
import base64
import hashlib
import io
import json
import lzma
import tarfile

ROOT = Path(__file__).resolve().parent

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def safe_name(name: str) -> bool:
    p = PurePosixPath(name)
    return bool(name) and not p.is_absolute() and '..' not in p.parts and '\\' not in name and str(p) == name

def main() -> None:
    meta = json.loads((ROOT / 'PUBLICATION_CAPSULE.json').read_text())
    texts = []
    seen = set()
    for entry in meta['parts']:
        name = entry['path']
        if not safe_name(name) or name in seen:
            raise ValueError('Unsafe or duplicate part')
        seen.add(name)
        data = (ROOT / name).read_bytes()
        if len(data) != entry['bytes'] or digest(data) != entry['sha256']:
            raise ValueError('Part mismatch: ' + name)
        texts.append(''.join(data.decode('ascii').split()))
    packed = base64.b64decode(''.join(texts), validate=True)
    if len(packed) != meta['compressed_bytes'] or digest(packed) != meta['compressed_sha256']:
        raise ValueError('Compressed capsule mismatch')
    files = {}
    with tarfile.open(fileobj=io.BytesIO(lzma.decompress(packed)), mode='r:') as archive:
        for member in archive.getmembers():
            if not member.isfile() or not safe_name(member.name) or member.name in files:
                raise ValueError('Unsafe or duplicate member')
            stream = archive.extractfile(member)
            if stream is None:
                raise ValueError('Unreadable member')
            files[member.name] = stream.read()
    if digest(files['SOURCE_MANIFEST.json']) != meta['source_manifest_sha256']:
        raise ValueError('Source manifest mismatch')
    expected = json.loads(files['SOURCE_MANIFEST.json'])['files']
    if set(files) != set(expected) | {'SOURCE_MANIFEST.json'} or len(files) != meta['source_files_including_manifest']:
        raise ValueError('Member coverage mismatch')
    for name, entry in expected.items():
        data = files[name]
        if len(data) != entry['bytes'] or digest(data) != entry['sha256']:
            raise ValueError('Source mismatch: ' + name)
    for name, data in files.items():
        path = ROOT / name
        if path.is_symlink() or any(parent.is_symlink() for parent in path.parents):
            raise ValueError('Symlink destination: ' + name)
        if path.exists() and (not path.is_file() or path.read_bytes() != data):
            raise ValueError('Refusing to overwrite changed source: ' + name)
    for name, data in files.items():
        path = ROOT / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    print(json.dumps({'recovered_source_files': len(files), 'all_hashes_match': True,
                      'mathematical_calculation_performed': False}))

if __name__ == '__main__':
    main()
