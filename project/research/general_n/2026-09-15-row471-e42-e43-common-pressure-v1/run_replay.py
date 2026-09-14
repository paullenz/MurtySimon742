#!/usr/bin/env python3
"""Offline replay for the exact row471 e_L=42,43 common-pressure closures."""
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
GN=HERE.parent
INPUT=GN/'2026-09-14-block-pressure-v1'/'REMAINDER_12.json'
VERIFY=HERE/'verify_row471_e42_e43.py'
FROZEN=HERE/'RESULT.json'
EXPECTED='b2f2b8f1f714eb11225c07d9a9595154a7c53523b5d8da74be8a2028c170cc15'
def canonical(x): return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
    if not __debug__: raise RuntimeError('Run without -O: assertions are audit checks.')
    out=json.loads(subprocess.run([sys.executable,str(VERIFY),'--remainder',str(INPUT)],text=True,capture_output=True,check=True).stdout)
    frozen=json.loads(FROZEN.read_text())
    assert out==frozen
    digest=hashlib.sha256(canonical(out)).hexdigest(); assert digest==EXPECTED
    assert out['independent_regression_e_low']==[41]
    assert out['newly_closed_e_low']==[42,43] and out['remaining_e_low']==[47]
    assert [out['reports'][str(e)]['total_charge_upper'] for e in (41,42,43)]==[213,214,215]
    assert all(out['reports'][str(e)]['receiver_lower']==222 for e in (41,42,43))
    print('PASS: row471 e_L=41 independent regression 213<222')
    print('PASS: row471 e_L=42,43 new exact closures 214<222 and 215<222')
    print('PASS: canonical result',digest)
    print('SCOPE: e_L=47 remains; row471 as a whole is not excluded')
if __name__=='__main__': main()
