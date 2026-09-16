#!/usr/bin/env python3
"""Regenerate the source-complete checks and enforce the published full summary."""
import json
import pathlib
import subprocess
import sys
ROOT=pathlib.Path(__file__).resolve().parent

def main():
    expected=json.loads((ROOT/'CHECK_SUMMARY.json').read_text())
    subprocess.run([sys.executable,str(ROOT/'check_support_charge.py')],check=True,stdout=subprocess.DEVNULL)
    actual=json.loads((ROOT/'evidence'/'CHECK_SUMMARY.json').read_text())
    if actual!=expected:
        keys=set(expected)|set(actual)
        raise RuntimeError({k:[expected.get(k),actual.get(k)] for k in keys if expected.get(k)!=actual.get(k)})
    report={'status':'PASS_FRESH_SOURCE_ONLY_REGENERATION','records':actual['records'],
            'input_sha256':actual['input_sha256'],'decision_sha256':actual['decision_sha256']}
    print(json.dumps(report,indent=2))
if __name__=='__main__': main()
