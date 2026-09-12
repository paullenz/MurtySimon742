#!/usr/bin/env python3
"""Complete N35 coverage and local integer checks; standard library only."""
from collections import Counter
import json
import exact_checks as exact
from frontier import HERE,expand


def main():
    report=dict(schema='n35-exact-replay-v1',status='PASS_COMPLETE',layers={},external_review='OPEN')
    for t,expected in ((3,19),(2,466)):
        exact.T=t;states,stats=expand(t);assert len(states)==expected
        seen=set();counts=Counter();zero=Counter();checks=0;gaps={};remaining=[]
        for line in (HERE/f't{t}.jsonl').read_text().splitlines():
            rec=json.loads(line);i=rec['state_id'];assert type(i) is int and 0<=i<len(states) and i not in seen
            assert rec['t']==t and (tuple(rec['s']),tuple(rec['rho']))==states[i]
            seen.add(i);method=rec['method'];counts[method]+=1
            if min(rec['s'])==0:zero[method]+=1
            if method in ('fixed9','fixed13','adaptive'):
                n,gap=exact.envelope(rec);checks+=n;gaps[method]=max(gaps.get(method,gap),gap)
            elif method=='unresolved':remaining.append(rec)
            else:exact.hand(rec)
        assert seen==set(range(len(states)))
        if remaining:report['status']='PASS_PARTIAL'
        report['layers'][str(t)]=dict(frontier=stats,exclusions=dict(counts),zero_demand_exclusions=dict(zero),
            local_integer_checks=checks,worst_gap_numerators=gaps,unresolved=remaining)
    (HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
