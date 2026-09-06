#!/usr/bin/env python3
"""Check archive bytes and compare the smaller checkpoint with the larger one.
No uploaded code is executed; no SAT proof or mathematical result is checked.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import stat
from collections import Counter
from pathlib import Path, PurePosixPath
from zipfile import ZipFile


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_digest(path: Path) -> str:
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def inspect_structure(z: ZipFile):
    seen = set()
    for info in z.infolist():
        name = info.filename.rstrip('/')
        p = PurePosixPath(name)
        if (not name or '\\' in name or '\x00' in name or p.is_absolute()
                or '..' in p.parts or p.as_posix() != name or ':' in p.parts[0]):
            raise ValueError(f'unsafe member: {info.filename!r}')
        if info.filename in seen:
            raise ValueError(f'duplicate member: {info.filename}')
        seen.add(info.filename)
        if info.flag_bits & 1 or stat.S_ISLNK(info.external_attr >> 16):
            raise ValueError(f'encrypted/symlink member refused: {info.filename}')
    project = {i.filename: i for i in z.infolist()
               if not i.is_dir() and not i.filename.startswith('__MACOSX/')}
    manifests = [n for n in project if PurePosixPath(n).name == 'ARCHIVE_MANIFEST.json']
    if len(manifests) != 1:
        raise ValueError('expected one archive manifest')
    manifest_name = manifests[0]
    prefix = manifest_name[:-len('ARCHIVE_MANIFEST.json')]
    raw = z.read(manifest_name)
    manifest = json.loads(raw)
    if not isinstance(manifest.get('files'), list) or not manifest['files']:
        raise ValueError('manifest must contain a nonempty files array')
    rows = {}
    for row in manifest['files']:
        name = row['path']
        p = PurePosixPath(name)
        if (not name or '\\' in name or p.is_absolute() or '..' in p.parts
                or p.as_posix() != name or name in rows):
            raise ValueError('unsafe or duplicate manifest path')
        rows[name] = row
    expected = {prefix + name for name in rows} | {manifest_name}
    if expected != set(project):
        raise ValueError('project member list differs from manifest')
    return prefix, raw, manifest, rows


def compare(current: Path, previous: Path) -> dict:
    with ZipFile(current) as a, ZipFile(previous) as b:
        ap, am, manifest, rows = inspect_structure(a)
        bp, bm, old_manifest, old_rows = inspect_structure(b)
        checks = []
        for name, row in sorted(rows.items()):
            data = a.read(ap + name)
            actual_hash = digest(data)
            matches_manifest = len(data) == row['bytes'] and actual_hash == row['sha256']
            previous_present = name in old_rows
            previous_data = b.read(bp + name) if previous_present else None
            same = previous_data == data if previous_present else False
            checks.append({'path': name, 'bytes': len(data), 'sha256': actual_hash,
                           'matches_manifest': matches_manifest,
                           'present_in_previous': previous_present,
                           'byte_identical_to_previous': same})
        bad_crc = a.testzip()
        current_hash = file_digest(current)
        pinned_compact = '503a5cfbae2a4c25bd074086a4f30cbe19915be967475ec40fc10f6a3dc4ac39'
        result = {
            'intake': '2026-09-06-upload-03',
            'current_archive': {'filename': current.name, 'bytes': current.stat().st_size,
                                'sha256': current_hash, 'project_prefix': ap,
                                'manifest_sha256': digest(am),
                                'includes_full_proof_files': manifest.get('includes_full_proof_files'),
                                'expected_original_compact_zip_sha256': pinned_compact,
                                'matches_original_compact_zip_pin': current_hash == pinned_compact},
            'previous_archive': {'filename': previous.name, 'bytes': previous.stat().st_size,
                                 'sha256': file_digest(previous), 'project_prefix': bp,
                                 'manifest_sha256': digest(bm)},
            'zip_crc_passed': bad_crc is None,
            'first_crc_failure': bad_crc,
            'unsafe_or_duplicate_zip_members': 0,
            'unexpected_or_missing_project_members': 0,
            'project_file_count_including_manifest': len(rows) + 1,
            'payload_count': len(rows),
            'payload_bytes': sum(r['bytes'] for r in rows.values()),
            'payloads_matching_manifest': sum(c['matches_manifest'] for c in checks),
            'payloads_byte_identical_to_previous': sum(c['byte_identical_to_previous'] for c in checks),
            'payloads_new_relative_to_previous': [c['path'] for c in checks if not c['present_in_previous']],
            'payloads_changed_relative_to_previous': [c['path'] for c in checks if c['present_in_previous'] and not c['byte_identical_to_previous']],
            'manifest_bytes_identical_to_previous': am == bm,
            'payload_directory_counts': dict(Counter(n.split('/')[0] if '/' in n else '[root]' for n in rows)),
            'macos_metadata_file_count': sum(not i.is_dir() and i.filename.startswith('__MACOSX/') for i in a.infolist()),
            'omitted_previous_payloads_count': len(set(old_rows) - set(rows)),
            'omitted_previous_payloads': sorted(set(old_rows) - set(rows)),
            'new_mathematical_evidence_relative_to_previous': False,
            'project_code_executed': False,
            'sat_proof_replay_performed': False,
            'theorem_status_changed': False,
            'checks': checks,
        }
        if bad_crc or not all(c['matches_manifest'] for c in checks):
            result['status'] = 'INVALID'
        elif all(c['byte_identical_to_previous'] for c in checks):
            result['status'] = 'VERIFIED_COMPACT_SUBSET_OF_PREVIOUS_CHECKPOINT'
        else:
            result['status'] = 'CONTENT_DIFFERENCE_REQUIRES_REVIEW'
        return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('current', type=Path)
    parser.add_argument('previous', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = compare(args.current, args.previous)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k not in ('checks','omitted_previous_payloads')}, indent=2))
    return 3 if report['status'] == 'INVALID' else 0


if __name__ == '__main__':
    raise SystemExit(main())
