#!/usr/bin/env python3
"""Freeze the first n=27 package after comparing its complete clean replay."""
from pathlib import Path
import gzip, hashlib, json, shutil, subprocess, sys, zipfile

ROOT = Path(__file__).resolve().parent
WORK = ROOT / 'n27_work'
REPLAY = ROOT / 'n27_clean_replay'
RELEASE = ROOT / 'n27_release'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write_json(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')

def main():
    log = ROOT / 'n27_full_replay.log'
    assert json.loads(log.read_text().splitlines()[-1])['status'] == 'COMPLETE_INTERNAL_REPLAY_PASS'
    compared = []
    for replay_file in sorted(REPLAY.rglob('*')):
        if not replay_file.is_file() or '__pycache__' in replay_file.parts:
            continue
        if replay_file.suffix == '.log' or replay_file.name in ('columns', 'survey', 'check_survey'):
            continue
        rel = replay_file.relative_to(REPLAY)
        original = WORK / rel
        assert original.is_file(), str(rel)
        a, b = original.read_bytes(), replay_file.read_bytes()
        aa, bb = (gzip.decompress(a), gzip.decompress(b)) if rel.suffix == '.gz' else (a, b)
        method = 'identical_decompressed_bytes' if rel.suffix == '.gz' else 'identical_bytes'
        if aa != bb:
            assert str(rel) == 'd15_182_supplement_certificates.json', str(rel)
            ja, jb = json.loads(aa), json.loads(bb)
            input_name = 'd15_182_pair_survivors.jsonl.gz'
            assert ja.pop('input_sha256') == sha((WORK / input_name).read_bytes())
            assert jb.pop('input_sha256') == sha((REPLAY / input_name).read_bytes())
            assert ja == jb
            aa = bb = json.dumps(ja, sort_keys=True, separators=(',', ':')).encode()
            method = 'identical_json_except_verified_input_archive_hash'
        compared.append({'path':str(rel), 'original_sha256':sha(a), 'replay_sha256':sha(b),
                         'comparison':method, 'content_sha256':sha(aa), 'status':'PASS'})
    assert compared
    logs = WORK / 'clean_replay_logs'
    logs.mkdir(exist_ok=True)
    shutil.copyfile(log, WORK / 'clean_replay.log')
    for source in REPLAY.rglob('*.log'):
        target = logs / source.relative_to(REPLAY)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    shutil.copyfile(REPLAY / 'd15_182_supplement_certificates.json', logs / 'reproduced_supplement_certificates.json')
    write_json(WORK / 'CLEAN_REPLAY_CHECK.json', {
        'date':'2026-09-07', 'status':'PASS', 'wrapper_status':'COMPLETE_INTERNAL_REPLAY_PASS',
        'independent_external_replay':False,
        'comparison_note':'Gzip timestamps can change archive bytes. All decompressed data agree; the supplement certificate records and correctly verifies its own input archive hash.',
        'source_note':'All production Python and C++ source files copied into the clean replay are byte-identical to this package. Documentation was finalized after the replay.',
        'wrapper_log_sha256':sha(log.read_bytes()), 'compared_files':compared})
    readme = WORK / 'README.md'
    body = readme.read_text()
    marker = '## Verify or reproduce\n'
    body = body.replace(marker, '## Distribution\n\nThe downloadable evidence ZIP contains the complete directory described below. The GitHub source folder provides the manuscript, code and smaller records for browsing; obtain the large ledgers and column files from [the archive distribution](https://github.com/paullenz/MurtySimon25/tree/main/releases/n27-candidate-v1) before running verification.\n\n'+marker, 1)
    body = body.replace('- `MANIFEST.json`:', '- `CLEAN_REPLAY_CHECK.json`, `clean_replay.log`, `clean_replay_logs/`: a full clean-directory rebuild and replay, with comparisons against all original generated data and source files.\n- `MANIFEST.json`:', 1)
    readme.write_text(body)
    payloads = [p for p in sorted(WORK.rglob('*')) if p.is_file() and '__pycache__' not in p.parts
                and p.name not in ('columns', 'survey', 'check_survey', 'MANIFEST.json')]
    write_json(WORK / 'MANIFEST.json', {'files':[{'path':str(p.relative_to(WORK)), 'bytes':p.stat().st_size,
                 'sha256':sha(p.read_bytes())} for p in payloads]})
    subprocess.run([sys.executable, '-I', '-B', str(WORK/'replay.py'), '--verify-only'], check=True)
    proof = ROOT / 'N27_Candidate_Proof_2026-09-07_v1.md'
    shutil.copyfile(WORK / 'PROOF.md', proof)
    archive = ROOT / 'N27_Candidate_Evidence_2026-09-07_v1.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as out:
        for p in payloads + [WORK / 'MANIFEST.json']:
            out.write(p, 'N27_Candidate_2026-09-07_v1/' + str(p.relative_to(WORK)))
    with zipfile.ZipFile(archive) as check:
        assert check.testzip() is None
        assert len(check.infolist()) == len(payloads)+1
    RELEASE.mkdir(exist_ok=True)
    data = archive.read_bytes()
    parts = []
    for i, offset in enumerate(range(0, len(data), 8*1024*1024), start=1):
        part = RELEASE / (archive.name + f'.part{i:02d}')
        content = data[offset:offset+8*1024*1024]
        part.write_bytes(content)
        parts.append({'name':part.name, 'bytes':len(content), 'sha256':sha(content),
                      'git_blob_sha1':hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()})
    receipt = {'archive':archive.name, 'bytes':len(data), 'sha256':sha(data),
               'archive_entries':len(payloads)+1, 'parts':parts}
    write_json(RELEASE / 'PARTS.json', receipt)
    shutil.copyfile(ROOT/'n27_assemble_archive.py', RELEASE/'assemble_archive.py')
    subprocess.run([sys.executable, '-I', '-B', str(RELEASE/'assemble_archive.py')], check=True)
    (RELEASE/'README.md').write_text(f'''# N=27 candidate evidence, edition 1

7 September 2026. Complete candidate argument; external mathematical review and external computational reproduction remain OPEN.

The proposed statement is e(G) <= 182 for every simple diameter-two edge-critical graph on 27 vertices, with equality exactly K13,14. The [proof and browsable source files](../../project/reviews/n27/2026-09-07-candidate-v1/README.md) describe the argument and its audit limits.

## Obtain the complete archive

Download or clone this repository with all files in this directory. Run:

```sh
python3 assemble_archive.py
```

This verifies each byte part, reconstructs `{archive.name}`, and verifies the complete archive. The parts are pieces of one archive and cannot be extracted individually.

- Complete ZIP: {len(data):,} bytes.
- SHA-256: `{sha(data)}`.
- Entries: {len(payloads)+1}; all ledgers, original outputs, source code, certificates, checks, clean replay logs and instructions are included.

Extract the complete ZIP. Inside `N27_Candidate_2026-09-07_v1`, run:

```sh
python3 -I -B replay.py --verify-only
python3 -I -B replay.py --replay --output /absolute/path/to/new-n27-replay
```

The first command verifies frozen files and final certificates. The second rebuilds and repeats the entire arithmetic in a new directory. Python 3.10+, a C++17 compiler (`g++`), zlib and OpenSSL libcrypto development headers/libraries are required. Executables are rebuilt from the preserved source.

A complete clean replay passed internally before this archive was frozen. Its data match the original outputs, including all 80,978,546 canonical residual columns representing 1,451,011,425 labelled columns. No final numerical cases remain. These are same-assistant checks and do not replace external mathematical assessment.

The frozen n=25 packages and governed theorem ledger are preserved unchanged.
''')
    print(json.dumps({'status':'PACKAGE_FROZEN_AND_ASSEMBLY_VERIFIED', **receipt, 'proof_sha256':sha(proof.read_bytes()), 'compared_files':len(compared)}))

if __name__ == '__main__':
    main()
