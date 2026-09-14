#!/usr/bin/env python3
"""Offline exact replay, input provenance and full frozen-output comparisons.

JSON evidence is hashed canonically because pretty-print formatting is not
mathematical evidence. Complete parsed-object equality is still required below.
Python source files retain byte-for-byte hashes.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CANONICAL = HERE.parent / '2026-09-14-block-pressure-v1/REMAINDER_12.json'
RAW_HASHES = {
    'source_prices.py': '0edaf844b1bafa1bebaebb5e06384b6a643ea4de9bb74f0cdd4c0a6ac8ad2587',
    'verify_source_prices.py': '7cb18968e8cf0cf65e3553ef97aab555449aa31676c3275b9b0b520aacf3c3f7',
}
JSON_HASHES = {
    'ORIGINAL_SIX_INPUT.json': 'a65e2181b836af9b7265ab1cc1ac03b290acc24160eb35558144123138861e37',
    'ORIGINAL_SIX_RESULTS.json': '1953c61d26c68dc2bcbb9aeddbe0d18336e05b118541f4d9ca3f9528c808caae',
    'VERIFICATION.json': '64e906fcfeae534c01008ac36263333518608d5e1339ce171d70f102406c3dcc',
}

def canonical_json_hash(path):
    value=json.loads(path.read_text())
    payload=json.dumps(value,sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(payload).hexdigest()

def main():
    if not __debug__:
        raise RuntimeError('Run without -O: assertions are part of the verifier.')
    for name, expected in RAW_HASHES.items():
        actual=hashlib.sha256((HERE/name).read_bytes()).hexdigest()
        if actual!=expected:
            raise ValueError(f'Frozen source hash mismatch: {name}: {actual}')
    for name,expected in JSON_HASHES.items():
        actual=canonical_json_hash(HERE/name)
        if actual!=expected:
            raise ValueError(f'Frozen canonical-JSON hash mismatch: {name}: {actual}')
    raw=CANONICAL.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(raw)).encode('ascii')+b'\0'+raw).hexdigest()
    if blob!='70b6fb160c82179c52ef8d88be673a4a729016a4':
        raise ValueError(f'Canonical original-input Git blob mismatch: {blob}')
    canonical_rows={row['row']:row for row in json.loads(raw)['rows']}
    for subset in json.loads((HERE/'ORIGINAL_SIX_INPUT.json').read_text())['rows']:
        canonical=canonical_rows[subset['row']]
        if any(canonical[key]!=value for key,value in subset.items()):
            raise ValueError(f'Local transcription differs at original row {subset["row"]}')
    for program,expected_file in [('verify_source_prices.py','VERIFICATION.json'),('source_prices.py','ORIGINAL_SIX_RESULTS.json')]:
        process=subprocess.run([sys.executable,str(HERE/program)],text=True,capture_output=True,check=True)
        actual=json.loads(process.stdout)
        expected=json.loads((HERE/expected_file).read_text())
        if actual!=expected:
            raise ValueError(f'Complete parsed JSON differs: {expected_file}')
        print(f'PASS: {program}; complete {expected_file} equality')
    print('PASS: pinned source bytes, canonical JSON evidence, canonical input, copied six-row arrays, finite soundness and 576 exact price evaluations.')
    print('New profile exclusions: 0. No fresh-seed, graph-realization or whole-state coverage claim.')

if __name__=='__main__':
    main()
