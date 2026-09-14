#!/usr/bin/env python3
"""Offline replay for the original-sample singleton-destination exclusions."""
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
GN=HERE.parent
INPUT=GN/'2026-09-14-block-pressure-v1'/'REMAINDER_12.json'
VERIFY=HERE/'verify_singleton_destination.py'
FROZEN=HERE/'RESULT.json'
EXPECTED='9a89c420f82a0bd89eb8e99a34dd3109ace9c1829879e62e819d452f408313f7'
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
    if not __debug__:raise RuntimeError('Run without -O: assertions are audit checks.')
    proc=subprocess.run([sys.executable,str(VERIFY),'--remainder',str(INPUT)],text=True,capture_output=True,check=True)
    actual=json.loads(proc.stdout);frozen=json.loads(FROZEN.read_text())
    assert actual==frozen
    digest=hashlib.sha256(canonical(actual)).hexdigest();assert digest==EXPECTED
    assert actual['newly_excluded']==[347,471,586]
    assert actual['remaining']==[160,338]
    assert actual['original_sample']=={'not_rejected':[160,338],'rejected':711,'total':713}
    print('PASS: singleton-destination exclusions 347,471,586')
    print('PASS: all-source cardinality arc-slot flow independently rejects the same three profiles')
    print('PASS: rows160,338 retained as non-rejections under both relaxations')
    print('PASS: canonical result',digest)
    print('SCOPE: original synthetic namespace only; canonical finite frontier unchanged')
if __name__=='__main__':main()
