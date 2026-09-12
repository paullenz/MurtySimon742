#!/usr/bin/env python3
"""Exhaust every oriented, light/heavy-coloured pair system on up to 4 vertices."""
from itertools import combinations,product
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent

def main():
    systems=0;configurations=0;cuts=0
    for b in range(1,5):
        pairs=list(combinations(range(b),2))
        # absent; forward light; backward light; forward heavy; backward heavy
        for pattern in product(range(5),repeat=len(pairs)):
            arcs=[]
            for (u,v),code in zip(pairs,pattern):
                if code:arcs.append((u,v,code>=3) if code in (1,3) else (v,u,code>=3))
            systems+=1
            q=[sum(u==x for u,v,c in arcs) for x in range(b)]
            p=[sum(v==x for u,v,c in arcs) for x in range(b)]
            H=[sum(u==x and c for u,v,c in arcs) for x in range(b)]
            for h in range(1,4):
                e=[int(x>h) for x in H];j=sum(e);F=[x*y for x,y in zip(H,e)];O=[x-y for x,y in zip(q,F)]
                required=[1]*b
                for u,v,c in arcs:
                    required[v]=max(required[v],q[u]-1-q[v],h if c and e[u] else 1)
                for spare in (0,1):
                    rho=[x+spare for x in required];a=max(x+y for x,y in zip(rho,q))
                    m=[min(pv,j-ev) for pv,ev in zip(p,e)]
                    incoming=[sum(v==x and c and e[u] for u,v,c in arcs) for x in range(b)]
                    assert all(incoming[x]<=m[x] and (rho[x]>=h or incoming[x]==0) for x in range(b))
                    ot=[sum(O[x] for x in range(b) if q[x]>k) for k in range(a+2)]
                    ft=[sum(F[x] for x in range(b) if q[x]>k) for k in range(a+2)]
                    for k,l in product(range(a+2),repeat=2):
                        upper=sum(p[x] if rho[x]+q[x]>=k else (m[x] if rho[x]>=h and rho[x]+q[x]>=l else 0) for x in range(b))
                        assert ot[k]+ft[l]<=upper,(b,pattern,h,rho,k,l)
                        cuts+=1
                    configurations+=1
    counterexamples=[
        dict(invalid_claim='Destination score must be at least q_origin rather than q_origin-1',
             arcs=[[0,1],[0,2]],q=[2,0,0],p=[0,1,1],rho=[1,1,1],h=1,H=[2,0,0],
             explanation='Both receiving scores are 1. The valid eligibility threshold is q_origin-1=1, not 2.'),
        dict(invalid_claim='Use min(p,j-1) for every destination, including destinations outside the high-sender set',
             arcs=[[0,1],[0,2]],q=[2,0,0],p=[0,1,1],rho=[1,1,1],h=1,H=[2,0,0],j=1,
             explanation='The two non-senders each receive one forced arc; subtracting one from j there incorrectly leaves zero capacity.'),
        dict(invalid_claim='Use the forced-arc cap m instead of p on destinations eligible for ordinary traffic',
             arcs=[[0,1]],q=[1,0],p=[0,1],rho=[1,1],h=1,H=[0,0],j=0,
             explanation='There is one ordinary arc and every forced-arc cap is zero. Ordinary destinations require their total indegree capacity.')]
    report=dict(status='PASS',coloured_partial_orientations=systems,routing_configurations=configurations,mixed_cuts_checked=cuts,
        scope='b=1..4; h=1..3; minimal valid residual scores and those scores plus one; all cutoffs 0..a+1',
        counterexamples=counterexamples,examples_are='Abstract routing systems, not asserted D2C graphs',external_review='OPEN')
    (HERE/'routing_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
