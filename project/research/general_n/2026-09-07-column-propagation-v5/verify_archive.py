#!/usr/bin/env python3
"""Verify the original v5 archive and optionally extract it to a NEW directory.

This verifies evidence integrity only; it does not certify the mathematics.
No network, compiler, solver or third-party package is required.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile

ARCHIVE = 'MurtySimon_GeneralN_ColumnPropagation_v5.zip'
PREFIX = 'MurtySimon_GeneralN_ColumnPropagation_v5/'
SHA256 = '79bdbdf02b23b9eef38e964b54eb300921b24d539014f07b476655d1575e63b6'
BYTES = 1035233


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='New extraction directory; existing paths are refused.')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    raw = (root / ARCHIVE).read_bytes()
    require(len(raw) == BYTES, 'Archive byte count mismatch.')
    require(hashlib.sha256(raw).hexdigest() == SHA256, 'Archive SHA-256 mismatch.')
    with zipfile.ZipFile(root / ARCHIVE) as archive:
        infos = archive.infolist()
        names = [i.filename for i in infos]
        require(len(names) == len(set(names)), 'Duplicate archive entry.')
        for info in infos:
            path = PurePosixPath(info.filename)
            require(info.filename.startswith(PREFIX) and not path.is_absolute()
                    and '..' not in path.parts and '\\' not in info.filename,
                    'Unsafe archive path.')
            require(not info.is_dir() and not stat.S_ISLNK(info.external_attr >> 16),
                    'Expected ordinary file entries only.')
        require(archive.testzip() is None, 'ZIP CRC failure.')
        manifest = json.loads(archive.read(PREFIX + 'MANIFEST.json'))
        require(manifest.get('schema') == 'murty-simon-file-manifest-v1', 'Unknown manifest schema.')
        records = manifest['files']
        require(len(records) == 54, 'Unexpected payload count.')
        expected = {PREFIX + 'MANIFEST.json'} | {PREFIX + r['path'] for r in records}
        require(len(expected) == 55 and set(names) == expected, 'Manifest coverage mismatch.')
        for record in records:
            data = archive.read(PREFIX + record['path'])
            require(len(data) == record['bytes'], 'Size mismatch: ' + record['path'])
            require(hashlib.sha256(data).hexdigest() == record['sha256'],
                    'Hash mismatch: ' + record['path'])
        for name in ('PROOF.md', 'REVIEW_AND_HANDOFF.md', 'RESULTS.json'):
            require((root / name).read_bytes() == archive.read(PREFIX + name),
                    'Readable mirror differs from original: ' + name)
        if args.output is not None:
            target = args.output.expanduser().resolve()
            require(not target.exists(), 'Refusing to overwrite an existing output path.')
            target.mkdir(parents=True, exist_ok=False)
            archive.extractall(target)
    report = {'archive_sha256': SHA256, 'archive_bytes': BYTES,
              'payload_files_verified': 54, 'all_payload_hashes_match': True,
              'readable_mirrors_match': True, 'mathematical_review': 'OPEN',
              'full_arithmetic_replay_performed': False}
    if args.output is not None:
        report['extracted_checkpoint'] = str(target / PREFIX.rstrip('/'))
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
