#!/usr/bin/env python3
"""Regenerate both finite test families and check pinned counts and stream hashes."""
import json
import pathlib
import subprocess
import sys
ROOT = pathlib.Path(__file__).resolve().parent
TASKS = (
    ('check_star_forest.py', 'evidence', 'CHECK_SUMMARY.json'),
    ('check_hole_budget.py', 'hole_evidence', 'HOLE_CHECK_SUMMARY.json'),
)
FIELDS = ('records', 'eligible_records', 'input_sha256', 'decision_sha256', 'cpp_decision_sha256')
def main():
    verified = []
    for source, directory, expected_name in TASKS:
        subprocess.run([sys.executable, str(ROOT / source)], check=True, stdout=subprocess.DEVNULL)
        actual = json.loads((ROOT / directory / 'CHECK_SUMMARY.json').read_text())
        expected = json.loads((ROOT / expected_name).read_text())
        mismatches = {k: [expected.get(k), actual.get(k)] for k in FIELDS if actual.get(k) != expected.get(k)}
        if mismatches:
            raise RuntimeError(f'{source}: pinned evidence mismatch: {mismatches}')
        verified.append({'source': source, 'records': actual['records'], 'decision_sha256': actual['decision_sha256']})
    print(json.dumps({'status': 'PASS_PINNED_REGENERATION', 'families': verified}, indent=2))
if __name__ == '__main__':
    main()
