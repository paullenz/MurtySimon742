#!/usr/bin/env python3
"""Build a new compact recovery companion; never impersonate an original ZIP."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent
PAYLOAD = ROOT / 'payload'
FULL_ARCHIVE_SHA256 = '27d4a632dc8bc2262def45b0a3ea0650adb8fb5d7e831e19839d14a3f8af9dfe'
OUTPUT = ROOT.parent / 'N25_Recovery_02_Source_Results_and_Audit_2026-09-06.zip'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    original = json.loads((PAYLOAD/'ARCHIVE_MANIFEST.json').read_text())
    selected, omitted = [], []
    for item in original['files']:
        name = item['path']
        if name.startswith('certificates/') and name.endswith('.rup.gz'):
            omitted.append(item)
            continue
        data = (PAYLOAD/name).read_bytes()
        if len(data) != item['bytes'] or digest(data) != item['sha256']:
            raise ValueError('Payload no longer matches the original manifest: '+name)
        selected.append((PAYLOAD/name, 'payload/'+name))
    selected.append((PAYLOAD/'ARCHIVE_MANIFEST.json', 'payload/ARCHIVE_MANIFEST.json'))
    for name in ('2026-09-06-upload-02.md', '2026-09-06-upload-02-check-results.json',
                 'README_RECOVERY_02.md', 'intake_archive.py', 'intake_results.json',
                 'payload_hash_verification.json', 'zip_member_inventory.json',
                 'run_recovery_checks.py', 'source_publication_plan.json', 'build_companion.py'):
        selected.append((ROOT/name, name))
    for folder in ('checks', 'logs', 'tools', 'tests'):
        for path in sorted((ROOT/folder).rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts:
                selected.append((path, path.relative_to(ROOT).as_posix()))
    names = [name for _, name in selected]
    if len(names) != len(set(names)):
        raise ValueError('Duplicate companion path')
    rows = []
    def write(archive, name, data):
        info = zipfile.ZipInfo(name, date_time=(2026, 9, 6, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, data, compresslevel=6)
    with zipfile.ZipFile(OUTPUT, 'w') as archive:
        for path, name in sorted(selected, key=lambda x: x[1]):
            data = path.read_bytes()
            write(archive, name, data)
            rows.append({'path':name, 'bytes':len(data), 'sha256':digest(data)})
        meta = {'kind':'NEW_COMPACT_COMPANION', 'included_files':rows,
                'omitted_from_payload':omitted, 'full_archive_sha256':FULL_ARCHIVE_SHA256}
        write(archive, 'BUNDLE_MANIFEST.json', (json.dumps(meta, indent=2)+'\n').encode())
    with zipfile.ZipFile(OUTPUT) as archive:
        if archive.testzip() is not None:
            raise ValueError('Companion ZIP CRC failure')
        for row in rows:
            data = archive.read(row['path'])
            if len(data) != row['bytes'] or digest(data) != row['sha256']:
                raise ValueError('Companion readback mismatch: '+row['path'])
    print(json.dumps({'archive':str(OUTPUT), 'bytes':OUTPUT.stat().st_size,
                      'sha256':digest(OUTPUT.read_bytes()), 'files_plus_manifest':len(rows)+1,
                      'proof_files_explicitly_omitted':len(omitted)}, indent=2))

if __name__ == '__main__':
    main()
