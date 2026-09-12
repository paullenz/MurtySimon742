#!/usr/bin/env python3
"""Independent audit: literal lower multisets and tail-count terminal domains.

No import from joint_clipping.py; no memoized minimization or square-root
capacity inverse. Finite tables are checked with standard-library integers.
"""
from itertools import combinations_with_replacement
from math import comb
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent


def inv(h,w):
    if w==0:
        return 0
    z=h
    while (z*(z-1)+h*(h+1))//2<w:
        z+=1
    return z


def value(s):
    result=0
    for h in range(2,max(s,default=0)+1):
        n=sum(x>=h for x in s)
        w=sum(x for x in s if x>=h)
        result+=n-inv(h,w)
    return result


def main():
    data=json.loads((HERE/'results.json').read_text())
    rows={(r['a'],r['M'],r['k']):r for r in data['rows']}
    local=0
    expected_keys=set()
    for a in range(17,24):
        for M in range(6,a):
            for k in range(1,a+1):
                loss=k-inv(M,M*k)
                if loss<=0:
                    continue
                safe=sum(min(inv(h,w)-inv(h,w-k)
                             for w in range(M*k,M*k+(M-1)*(a-k)+1))
                         for h in range(2,M))
                if safe>=loss:
                    continue
                key=(a,M,k);expected_keys.add(key)
                r=rows[key]
                best=10**9
                for lower in combinations_with_replacement(range(M),a-k):
                    s=lower+(M,)*k
                    after=lower+(M-1,)*k
                    best=min(best,value(after)-value(s))
                    local+=1
                assert best==r['net_gain']
                assert r['joint_gain']==best+loss and r['independent_gain']==safe
    assert set(rows)==expected_keys
    assert all(r['net_gain']>=0 for r in rows.values() if r['a']<=22)
    assert all(r['net_gain']>=0 for r in rows.values() if r['a']==23 and r['M']>=7)
    assert value([6]*23)==31 and value([5]*23)==30

    bounds=[]
    for a,cap in [(a,5) for a in range(17,23)]+[(23,6)]:
        best=-999;num=0
        # N2 >= N3 >= ... >= Ncap; tail weight h*N_h+sum_{j>h}N_j.
        for rev in combinations_with_replacement(range(a+1),cap-1):
            tails=tuple(reversed(rev))
            score=sum(tails)-sum(inv(h,h*tails[h-2]+sum(tails[h-1:]))
                                  for h in range(2,cap+1))
            best=max(best,score);num+=1
        assert num==comb(a+cap-1,cap-1)
        target=next((r for r in data['terminal'] if r['a']==a),None)
        if a==23:
            target=json.loads((HERE/'adaptive_cap_23.json').read_text())
        assert best==target['Dmax']
        bounds.append(dict(a=a,cap=cap,terminal_states=num,Dmax=best,Qmax=a+best))
    assert [x['Qmax'] for x in bounds]==[32,35,39,42,46,49,54]
    result=dict(status='PASS',joint_rows=len(rows),literal_lower_multisets=local,
                independently_verified_bounds=bounds,
                known_23_label_failure=dict(before=31,after=30))
    (HERE/'independent_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
