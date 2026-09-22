#!/usr/bin/env python3
"""Actual-adjacency replay of Boolean orientation and equality controls.

No universal nonexistence is inferred from this finite test. All-selection
coverage and sampled coverage are reported separately.
"""
import argparse
from collections import Counter
from itertools import product
import hashlib
import json
from math import prod
from pathlib import Path
import random
import sys
import time
HERE=Path(__file__).resolve().parent
BRIDGE=HERE.parent/'2026-09-22-raw-profile-bridge-v1'
if not BRIDGE.is_dir(): BRIDGE=HERE
sys.path.insert(0,str(BRIDGE))
import check_raw_profile as C
from extract_supplement_witness import graph_from_fixture


def check(rows, root, selection, counts):
    n=len(rows); b=rows[root].bit_count(); a=n-b-1
    A=[i for i in range(n) if i!=root and not(rows[root]>>i&1)]
    B=[u for u in range(n) if rows[root]>>u&1]
    M={u:{i for i in A if not(rows[u]>>i&1)} for u in B}
    L={u:{i for x,i,w in selection if x==u} for u in B}
    R={u:M[u]-L[u] for u in B}
    indeg={u:sum(w==u for x,i,w in selection) for u in B}
    f=sum(bool(rows[i]>>j&1) for i,j in C.combinations(A,2))
    r=sum(map(len,R.values()))
    d={i:sum(bool(rows[i]>>j&1) for j in A) for i in A}
    residual={i:sum(i in R[u] for u in B) for i in A}
    s={i:max(0,d[i]-residual[i]) for i in A}
    S=sum(s.values()); m=len(C.edges(rows)); t=m-b*(n-b)
    deficit=n*n//4-b*(n-b)
    assert f==r+t and S>=r+2*t
    for u in B:
        assert len(L[u])==sum(x==u for x,i,w in selection)
        assert rows[u].bit_count()==a+1+indeg[u]-len(R[u])
        assert indeg[u]<=2*b-n+len(R[u])
        counts['degree_identity_checks']+=1
    for u,i,w in selection:
        assert i in M[u]-M[w]
        assert L[u]-{i}<=M[w]
        assert L[w]<=M[u]
        assert M[w]-M[u]<=R[w]
        assert M[u]-M[w]<={i}|R[u]
        counts['robust_arc_checks']+=1
        if r==0:
            assert M[w]==M[u]-{i}
            counts['exact_boolean_arcs']+=1
    if S==0:
        counts['zero_demand']+=1
        assert m<=n*n//4
    if S==0 and m==n*n//4:
        counts['zero_demand_equality']+=1
        counts['zero_demand_equality_odd' if n%2 else 'zero_demand_equality_even']+=1
        assert r==f==t==0
        assert not selection
        assert all(not(rows[i]>>j&1) for i,j in C.combinations(A+[root],2))
        assert all(not(rows[u]>>w&1) for u,w in C.combinations(B,2))
        assert all(rows[i]>>u&1 for i in A+[root] for u in B)
        assert abs(len(A)+1-len(B))<=1
    if r==0 and f==0 and selection:
        counts['nonempty_zero_residual_roots']+=1
        assert 2*b-n>=2
    if m>=n*n//4:
        assert r<=S-2*deficit
        assert f<=S-deficit
    counts['selections']+=1
    counts['S_'+str(S)]+=1
    return {'S':S,'r':r,'f':f,'t':t,'Q':len(selection),'lambda':2*b-n}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--extra-seeds',type=int,default=30)
    p.add_argument('--max-order',type=int,default=26)
    p.add_argument('--output',default='EQUALITY_RESULTS.json')
    args=p.parse_args()
    started=time.monotonic(); counts=Counter(); ledger=[]
    old=json.loads((BRIDGE/'RESULTS.json').read_text())
    fixtures=[(f['name'],graph_from_fixture(f)) for f in old['fixtures']]
    for n in range(7,args.max_order+1):
        for seed in range(args.extra_seeds):
            fixtures.append((f'extra_n{n}_seed{seed}',C.greedy_critical(n,742000+1000*n+seed)))
    for n in range(3,42):
        p=n//2; q=n-p
        fixtures.append((f'balanced_control_n{n}',C.from_edges(n,[(i,j) for i in range(p) for j in range(p,n)])))
    for name,rows in fixtures:
        assert C.is_d2c(rows)
        # Independent breadth-first deletion verification on every input.
        C.certify_d2c_bfs(rows)
        counts['graphs']+=1
        counts['bfs_deletion_checks']+=len(C.edges(rows))
        roots=[]; delta=max(x.bit_count() for x in rows)
        for v in range(len(rows)):
            if rows[v].bit_count()!=delta: continue
            data=C.legal_choices(rows,v); options=data[-1]; space=prod(map(len,options))
            if space<=1024:
                choices=list(product(*options)); counts['exhausted_roots']+=1
            else:
                rng=random.Random(27000+100*v+len(rows))
                choices=[tuple(x[0] for x in options)]
                choices += [tuple(rng.choice(x) for x in options) for _ in range(31)]
                choices=list(dict.fromkeys(choices)); counts['sampled_roots']+=1
            values=[check(rows,v,s,counts) for s in choices]
            roots.append({'root':v,'space':space,'tested':len(choices),'profiles':sorted({tuple(sorted(x.items())) for x in values})})
        ledger.append({'name':name,'n':len(rows),'m':len(C.edges(rows)),'roots':roots})
    # A dense near-equality impostor checks why root-edge criticality is essential.
    impostor=C.from_edges(5,[(0,2),(0,3),(0,4),(1,3),(1,4),(2,3)])
    assert C.diameter_at_most_two(impostor) and not C.is_d2c(impostor)
    assert C.bfs_diameter_status(impostor,(0,3))==2
    result={'status':'PASS','counts':dict(counts),'elapsed_seconds':time.monotonic()-started,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies':['check_raw_profile.py','extract_supplement_witness.py','RESULTS.json'],
            'noncritical_impostor':{'n':5,'m':6,'edges':C.edges(impostor),'deletable_edge':[0,3]},
            'fixtures':ledger}
    Path(args.output).write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='fixtures'},indent=2))


if __name__=='__main__':main()
