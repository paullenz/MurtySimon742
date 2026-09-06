#!/usr/bin/env python3
"""Check archive-manifest bytes without executing project code.

Exit 0: all declared payloads present and matched; 2: payloads missing;
3: mismatch, unsafe input, or invalid manifest. No mathematical claim is made.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def validate_rows(manifest: Any) -> list[dict[str, Any]]:
    if not isinstance(manifest, dict) or not isinstance(manifest.get('files'), list):
        raise ValueError('manifest must contain a files array')
    if not manifest['files']:
        raise ValueError('empty manifest cannot establish recovery completeness')
    seen: set[str] = set()
    for row in manifest['files']:
        if not isinstance(row, dict):
            raise ValueError('manifest entry is not an object')
        name = row.get('path')
        if not isinstance(name, str) or not name or '\\' in name or '\x00' in name:
            raise ValueError('invalid path')
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or path.as_posix() != name:
            raise ValueError(f'unsafe or noncanonical path: {name!r}')
        if name == '.' or ':' in path.parts[0]:
            raise ValueError(f'unsafe path: {name!r}')
        if name in seen:
            raise ValueError(f'duplicate path: {name}')
        seen.add(name)
        if type(row.get('bytes')) is not int or row['bytes'] < 0:
            raise ValueError(f'invalid size: {name}')
        if not isinstance(row.get('sha256'), str) or not re.fullmatch(r'[0-9a-f]{64}', row['sha256']):
            raise ValueError(f'invalid SHA-256: {name}')
    return manifest['files']


def inspect(manifest_path: Path, payload_root: Path) -> dict[str, Any]:
    if manifest_path.is_symlink():
        raise ValueError('manifest must not be a symlink')
    raw = manifest_path.read_bytes()
    manifest = json.loads(raw)
    rows = validate_rows(manifest)
    root = payload_root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError('payload root must be a directory')
    checks = []
    for row in rows:
        p = root
        for part in PurePosixPath(row['path']).parts:
            p = p / part
            if p.is_symlink():
                raise ValueError(f'symlink refused: {row["path"]}')
        result = dict(row)
        if not p.exists():
            result['intake_status'] = 'MISSING'
        elif not p.is_file():
            result['intake_status'] = 'MISMATCH'
            result['error'] = 'not a regular file'
        else:
            result['actual_bytes'] = p.stat().st_size
            result['actual_sha256'] = digest(p)
            result['intake_status'] = ('MATCH' if result['actual_bytes'] == row['bytes']
                                       and result['actual_sha256'] == row['sha256'] else 'MISMATCH')
        checks.append(result)
    counts = {s.lower(): sum(x['intake_status'] == s for x in checks)
              for s in ('MATCH', 'MISMATCH', 'MISSING')}
    state = ('INVALID' if counts['mismatch'] else 'PARTIAL' if counts['missing'] else 'COMPLETE')
    return {'status': state, 'manifest_sha256': hashlib.sha256(raw).hexdigest(),
            'source_archive_claims_full_proof_files': manifest.get('includes_full_proof_files'),
            'declared_entries': len(rows), 'declared_bytes': sum(r['bytes'] for r in rows),
            'counts': counts, 'missing_declared_bytes': sum(x['bytes'] for x in checks if x['intake_status'] == 'MISSING'),
            'proof_replay_performed': False, 'original_archive_container_hash_verified': False,
            'checks': checks}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('payload_root', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = inspect(args.manifest, args.payload_root)
        code = {'COMPLETE': 0, 'PARTIAL': 2, 'INVALID': 3}[result['status']]
    except (ValueError, OSError) as error:
        result = {'status': 'INVALID', 'error': str(error), 'proof_replay_performed': False}
        code = 3
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'checks'}, sort_keys=True))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
