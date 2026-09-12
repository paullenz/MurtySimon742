#!/usr/bin/env python3
"""N34 equality v2: preserved envelope replay plus the hand replacement.

Imports the historical exact local formula checks. Its heavy model is never
built, and neither Farkas certificate is read by this proof replay.
"""
from collections import Counter
from pathlib import Path
import json
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT/'project/research/n34/2026-09-12-equality-v1'))
from verify import envelope,hand
from certificate_io import read_stage
from check_frontier import expand


def main():
    states,stats=expand(1);assert len(states)==13546
    expected=set(range(len(states)));covered=set();counts=Counter();checks=0;zero=Counter()
    for stage in ('fixed','adaptive'):
        seen=set()
        for rec in read_stage(stage):
            i=rec['state_id'];assert type(i) is int and i in expected and i not in seen
            assert (tuple(rec['s']),tuple(rec['rho']))==states[i];seen.add(i)
            method=rec['method']
            if method=='unresolved':continue
            assert i not in covered;covered.add(i);counts[method]+=1
            if min(rec['s'])==0:zero[method]+=1
            if method in ('fixed9','fixed13','adaptive'):checks+=envelope(rec)[0]
            else:hand(rec)
        assert seen==expected;expected=seen-covered
    assert len(expected)==1
    i=next(iter(expected));s,rho=states[i]
    assert s==(1,1)+(2,)*13 and rho==(1,)*10+(2,)*8
    k=sum(v>=2 for v in s);z=sum(v>=2 for v in rho);r=sum(rho)
    assert max(v+18-15-1 for v in rho if v>=2)<=4
    assert 6*k>r+6*z
    counts['heavy_load_hand']=1;covered.add(i)
    assert len(covered)==len(states) and sum(counts.values())==13546
    report=dict(status='PASS_COMPLETE',frontier=stats,exclusions=dict(counts),
        zero_demand_exclusions=dict(zero),envelope_local_integer_checks=checks,
        hand_accounting_exclusions=sum(v for k,v in counts.items() if k not in ('fixed9','fixed13','adaptive')),
        integer_envelope_certificates=sum(counts[k] for k in ('fixed9','fixed13','adaptive')),
        proof_critical_heavy_farkas_certificates=0,covered_states=len(covered),unresolved=[],external_review='OPEN')
    (HERE/'v2_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
