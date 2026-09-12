#!/usr/bin/env python3
"""N35 direct tail arithmetic and recursive residual reconstruction.

Reuses the complete a=15 demand CSV, but not its residual expansion program.
"""
from collections import Counter
import csv
from pathlib import Path

HERE=Path(__file__).resolve().parent
CSV=HERE.parents[1]/'n34/2026-09-12-frontier-v1/FRONTIER.csv'
A,B=15,19


def expand(t):
    assert t in (2,3)
    states=[];stats=Counter()
    for row in csv.DictReader(CSV.open()):
        s=tuple(int(row[f's{i}']) for i in range(A))
        assert len(s)==A and tuple(sorted(s))==s and 0<=min(s)<=max(s)<A
        tails={}
        for h in range(2,A):
            w=sum(v for v in s if v>=h)
            tails[h]=next(z for z in range(h,A+B+1)
                          if z*(z-1)+h*(h+1)>=2*w) if w else 0
        score=sum(s)-sum(tails.values())
        assert score==int(row['Q'])
        closed={h:max(tails[k] for k in range(h,A)) for h in range(2,A)}
        score2=sum(s)-sum(closed.values())
        assert score2==int(row['Q_monotone'])
        if score2<B+2*t:continue
        stats['profiles']+=1
        base=tuple(sorted(1+sum(j<closed[h] for h in range(2,A)) for j in range(B)))
        slack=sum(s)-2*t-sum(base)
        assert slack>=0

        def visit(prefix,budget):
            i=len(prefix)
            if i==B:
                rho=tuple(prefix)
                assert all(sum(v>=h for v in rho)>=tails[h] for h in tails)
                if sum(rho)>A*(A-1)//2-t-(A+1)//2:
                    stats['isolated_C_excluded_states']+=1;return
                states.append((s,rho));stats['states']+=1
                stats['zero_demand_states' if s[0]==0 else 'positive_demand_states']+=1
                return
            for v in range(max(base[i],prefix[-1] if prefix else 1),min(A,base[i]+budget)+1):
                visit(prefix+[v],budget-v+base[i])
        visit([],slack)
    assert len(states)==len(set(states))
    return sorted(states),dict(stats)
