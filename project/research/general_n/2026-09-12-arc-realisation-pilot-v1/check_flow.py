#!/usr/bin/env python3
"""Independent exhaustive tiny-object challenge; direct B-side conditions."""
from itertools import product,combinations
from pathlib import Path
import json
from flow import solve
HERE=Path(__file__).resolve().parent

def direct(a,b,selected,residual,arcs,capacities):
    if len(arcs)!=len(selected) or {(u,i) for u,i,v in arcs}!=set(selected):return False
    if len({tuple(sorted((u,v))) for u,i,v in arcs})!=len(arcs):return False
    if any(sum(w==v for u,i,w in arcs)>capacities[v] for v in range(b)):return False
    N=[{i for w,i in set(selected)|set(residual) if w==v} for v in range(b)]
    for u,i,v in arcs:
        if i in N[v]:return False
        missing={w for t,k,w in arcs if t==u}|{t for t,k,w in arcs if w==u}
        if any(i not in N[w] for w in missing-{v}):return False
    return True

def verify_certificate(a,b,selected,residual,capacities,result):
    if result['status']=='ROUTING':
        assert direct(a,b,selected,residual,result['arcs'],capacities)
    else:
        T=list(map(tuple,result['obligations']));assert len(T)==len(set(T)) and set(T)<=set(selected)
        N=[{i for w,i in set(selected)|set(residual) if w==v} for v in range(b)]
        S=[{i for w,i in selected if w==v} for v in range(b)];U=set()
        for u,i in T:
            for v in range(b):
                # Test individual memberships, not the implementation's set-difference expression.
                if u==v or i in N[v]:continue
                if any(k not in N[v] for k in S[u] if k!=i):continue
                if any(k not in N[u] for k in S[v]):continue
                U.add(v)
        assert sorted(U)==result['destinations']
        cap=sum(capacities[v] for v in U)
        assert cap==result['destination_capacity'] and len(T)-cap==result['deficit']>0
    return True

def main():
    count=0;assignments=0;yes=0;no=0
    a=2;b=3;positions=list(product(range(b),range(a)))
    for pattern in product(range(3),repeat=a*b):
        selected={p for p,c in zip(positions,pattern) if c==1};residual={p for p,c in zip(positions,pattern) if c==2}
        obligations=sorted(selected);caps=[sum(w==v for w,i in residual) for v in range(b)]
        feasible=False
        for ends in product(*[[v for v in range(b) if v!=u] for u,i in obligations]):
            assignments+=1;arcs=[(u,i,v) for (u,i),v in zip(obligations,ends)]
            if direct(a,b,selected,residual,arcs,caps):feasible=True
        result=solve(a,b,selected,residual,caps)
        assert (result['status']=='ROUTING')==feasible,(pattern,result)
        verify_certificate(a,b,selected,residual,caps,result);count+=1
        if feasible:yes+=1
        else:no+=1
    assert count==729
    a=3;b=3;pairs=list(combinations(range(b),2));labelled=0;injective=0;cross=0;demands=0;thresholds=0
    for options in product(range(1+2*a),repeat=len(pairs)):
        labelled+=1;arcs=[]
        for (u,v),choice in zip(pairs,options):
            if choice:
                i=(choice-1)%a
                arcs.append((u,i,v) if choice<=a else (v,i,u))
        selected={(u,i) for u,i,v in arcs}
        if len(selected)!=len(arcs):continue
        injective+=1;S=[{i for w,i in selected if w==v} for v in range(b)]
        required=[s.copy() for s in S];forbidden=[set() for _ in range(b)]
        for u,i,v in arcs:
            forbidden[v].add(i)
            missing={w for t,k,w in arcs if t==u}|{t for t,k,w in arcs if w==u}
            for w in missing-{v}:required[w].add(i)
        if any(x&y for x,y in zip(required,forbidden)):continue
        free=[(u,i) for u in range(b) for i in range(a) if i not in required[u]|forbidden[u]]
        for bits in product(range(2),repeat=len(free)):
            N=[x.copy() for x in required]
            for (u,i),bit in zip(free,bits):
                if bit:N[u].add(i)
            residual={(u,i) for u in range(b) for i in N[u]-S[u]};rho=[len(N[u]-S[u]) for u in range(b)]
            p=[sum(w==v for u,i,w in arcs) for v in range(b)];q=list(map(len,S));cross+=1
            assert direct(a,b,selected,residual,arcs,p)
            for u,i,v in arcs:
                assert S[u]-N[v]=={i} and S[v]<=N[u]
                assert rho[v]+q[v]>=q[u]-1
                assert sum(i in Ns for Ns in N)>=q[u]+p[u]
            for v in range(b):
                I={i for u,i,w in arcs if w==v}
                assert not I&N[v] and len(I)<=a-rho[v]-q[v]
                assert all(S[u]&I=={i} for u,i,w in arcs if w==v)
            bounds=[]
            for i in range(a):
                sources=[u for u in range(b) if i in S[u]]
                bounds.append(min([len(sources)]+[rho[u] for u in sources]))
            for s in product(*[range(k+1) for k in bounds]):
                demands+=1
                for h in range(1,max(s,default=0)+1):
                    thresholds+=1;H=[sum(s[i]>=h for i in labels) for labels in S]
                    assert all(rho[v]>=h for u,i,v in arcs if s[i]>=h and H[u]>h)
    report=dict(status='PASS',fixed_cross_patterns=count,brute_destination_assignments=assignments,
        routable_patterns=yes,certified_unroutable_patterns=no,labelled_oriented_graphs=labelled,
        distinct_source_label_graphs=injective,compatible_cross_patterns=cross,
        eligible_demand_vectors=demands,heavy_threshold_checks=thresholds,
        scope='Exhaustive finite abstract objects, not positive-surplus D2C graphs; general proof is separate.')
    (HERE/'flow_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
