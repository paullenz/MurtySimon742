#!/usr/bin/env python3
"""Exact replay of BAND_INTERVAL_CUT_COUNTEREXAMPLE.md."""
import json
from pathlib import Path

TYPES=[(0,2,4),(3,3,1),(3,3,4),(3,5,3),(4,6,2),(4,7,3)]
COUNTS=[1]*6
SELECTED={1,2,3,4}
GENS=[1,3,4]
M=[2,1,1]
D=[6,3,4]
EXPECTED={1:0,2:2,3:1,4:0,5:-1,6:1,7:0}


def compat(a,b):
    qa,ca,_=a; qb,cb,_=b
    return qa<=cb+1 and qb<=ca


def band_of_type(t):
    if t not in SELECTED:
        return None
    c=TYPES[t][1]
    for i,g in enumerate(GENS):
        if c<=TYPES[g][1]:
            return i
    raise AssertionError("unassigned selected type")


def margin(mask):
    demand=sum(D[i] for i in range(3) if mask>>i&1)
    cap=0
    for s,sigma in enumerate(TYPES):
        u=sum(M[i] for i,g in enumerate(GENS) if (mask>>i)&1 and compat(TYPES[g],sigma))
        b=band_of_type(s)
        if b is not None and (mask>>b)&1:
            u-=1
        assert u>=0
        cap+=min(sigma[2],u)
    return cap-demand


def main():
    got={m:margin(m) for m in range(1,8)}
    assert got==EXPECTED,(got,EXPECTED)
    contiguous={1,2,4,3,6,7}
    assert min(got[m] for m in contiguous)>=0
    assert got[5]==-1
    report={
        "schema":"band-interval-cut-counterexample-verification-v1",
        "result":"PASS",
        "types":[list(x) for x in TYPES],
        "selected_types":sorted(SELECTED),
        "generator_types":GENS,
        "band_counts":M,
        "band_demands":D,
        "margins":{str(k):v for k,v in got.items()},
        "contiguous_masks":[1,2,4,3,6,7],
        "noncontiguous_deficient_mask":5,
        "noncontiguous_deficiency":1,
        "external_review":"OPEN",
    }
    Path(__file__).with_name("BAND_INTERVAL_CUT_COUNTEREXAMPLE_VERIFICATION.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
