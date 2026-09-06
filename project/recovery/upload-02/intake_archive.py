#!/usr/bin/env python3
"""Non-executing ZIP intake; original archive and files remain unchanged."""
from pathlib import Path, PurePosixPath
from collections import Counter
import zipfile, hashlib, stat, json, shutil
BASE=Path('/mnt/data/n25_recovery_02')
p=Path('/mnt/data/delta14_checkpoint-2.zip')
sha=lambda b:hashlib.sha256(b).hexdigest()
expected='3c53614d1a229bf6cf411703547919c874c544ac2c0f1e911a867c51d7de9e2e'
with p.open('rb') as f: archive_sha=hashlib.file_digest(f,'sha256').hexdigest()
with zipfile.ZipFile(p) as z:
    infos=z.infolist(); names=[i.filename for i in infos]
    if len(names)!=len(set(names)): raise ValueError('duplicate ZIP member')
    if sum(i.file_size for i in infos)>2_000_000_000: raise ValueError('expansion limit')
    for i in infos:
        q=PurePosixPath(i.filename)
        if q.is_absolute() or '..' in q.parts or '\\' in i.filename or '\x00' in i.filename: raise ValueError('unsafe path')
        if stat.S_ISLNK(i.external_attr>>16): raise ValueError('symlink')
        if i.flag_bits&1: raise ValueError('encrypted member')
    bad_crc=z.testzip()
    if bad_crc: raise ValueError('ZIP CRC failure '+bad_crc)
    manifest_name='delta14_checkpoint-2/ARCHIVE_MANIFEST.json'
    mbytes=z.read(manifest_name); manifest=json.loads(mbytes)
    known=Path('/mnt/data/ARCHIVE_MANIFEST.json').read_bytes()
    prefix='delta14_checkpoint-2/'
    rows=[]; declared=set(); output=BASE/'payload'
    output.mkdir(exist_ok=True)
    for rec in manifest['files']:
        rel=rec['path']; q=PurePosixPath(rel)
        if q.is_absolute() or '..' in q.parts or '\\' in rel or str(q)!=rel: raise ValueError('unsafe manifest')
        if rel in declared: raise ValueError('duplicate manifest path')
        declared.add(rel)
        if prefix+rel not in names:
            rows.append(rec|{'status':'MISSING'}); continue
        b=z.read(prefix+rel)
        row=rec|{'actual_bytes':len(b),'actual_sha256':sha(b)}
        row['status']='MATCH' if len(b)==rec['bytes'] and sha(b)==rec['sha256'] else 'MISMATCH'
        rows.append(row)
        dest=output/rel; dest.parent.mkdir(parents=True,exist_ok=True)
        with dest.open('xb') as f: f.write(b)
    (output/'ARCHIVE_MANIFEST.json').write_bytes(mbytes)
    extra=[i.filename for i in infos if not i.is_dir() and i.filename.startswith(prefix) and i.filename[len(prefix):] not in declared and i.filename!=manifest_name]
    metadata=[i.filename for i in infos if not i.is_dir() and i.filename.startswith('__MACOSX/')]
    result={'archive_name':p.name,'archive_bytes':p.stat().st_size,'archive_sha256':archive_sha,
            'expected_original_archive_sha256':expected,'original_container_hash_matches':archive_sha==expected,
            'zip_entries':len(infos),'zip_crc_all_members_passed':True,'zip_uncompressed_bytes':sum(i.file_size for i in infos),
            'manifest_sha256':sha(mbytes),'manifest_matches_prior_upload':mbytes==known,
            'declared_entries':len(rows),'declared_bytes':sum(x['bytes'] for x in rows),'payload_status_counts':dict(Counter(x['status'] for x in rows)),
            'metadata_members':len(metadata),'metadata_uncompressed_bytes':sum(i.file_size for i in infos if i.filename in metadata),
            'unexpected_project_members':extra,'unexpected_other_members':[i.filename for i in infos if not i.is_dir() and not i.filename.startswith((prefix,'__MACOSX/'))],
            'proof_replay_performed':False,'theorem_status_changed':False,
            'github_payload_published':False}
    (BASE/'intake_results.json').write_text(json.dumps(result,indent=2)+'\n')
    (BASE/'payload_hash_verification.json').write_text(json.dumps(rows,indent=2)+'\n')
    (BASE/'zip_member_inventory.json').write_text(json.dumps([{'path':i.filename,'bytes':i.file_size,'compressed_bytes':i.compress_size,'crc':i.CRC,'directory':i.is_dir()} for i in infos],indent=2)+'\n')
    print(json.dumps(result,indent=2))
