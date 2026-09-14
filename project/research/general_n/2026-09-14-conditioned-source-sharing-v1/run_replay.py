#!/usr/bin/env python3
"""Offline complete replay for conditioned source sharing on original row 108."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
REMAINDER = HERE.parent / '2026-09-14-block-pressure-v1' / 'REMAINDER_12.json'
SHARED = HERE.parent / '2026-09-14-joint-blocks-v1' / 'SHARED_SLACK_FULL.json'
EXPECTED_CANONICAL = '5ea860b79516d9a34e73a67fafdb7875cd3c9c99b01594b4bf3aab2c3e8a7629'


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':')).encode()


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: assertions are part of the verifier.')
    proc = subprocess.run([
        sys.executable, str(HERE / 'verify_row108.py'),
        '--remainder', str(REMAINDER),
        '--shared-result', str(SHARED),
    ], text=True, capture_output=True, check=True)
    actual = json.loads(proc.stdout)
    digest = hashlib.sha256(canonical(actual)).hexdigest()
    if digest != EXPECTED_CANONICAL:
        raise ValueError(f'canonical result hash mismatch: {digest}')
    assert actual['old_multiblock'] == {'inherited_rejected': 8, 'survivors': 32}
    assert actual['source_price']['closed'] == 24
    cp = actual['common_pressure']
    assert (cp['closed_tuples'], cp['total_histograms'], cp['incidence_feasible'],
            cp['incidence_charge_below'], cp['common_pressure_proofs'], cp['branch_nodes']) == (8,46662,1201,1124,77,57867)
    print('PASS: conditioned source sharing row 108 canonical-output replay')
    print('PASS: 32 prior tuples -> 24 fixed-price closures + 8 exact common-pressure closures')
    print('PASS: 46,662 histograms; 1,201 incidence-feasible; 77 common-pressure branch proofs')
    print('Scope: one original synthetic profile only; canonical whole-state frontier unchanged.')


if __name__ == '__main__':
    main()
