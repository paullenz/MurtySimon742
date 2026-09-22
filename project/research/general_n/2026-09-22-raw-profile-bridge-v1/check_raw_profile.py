#!/usr/bin/env python3
"""Exact graph-to-profile regression; standard library only.

Starts with adjacency data, verifies D2C using deletion and independent BFS,
then reconstructs EVERY bridge object. Irrational profile sums are certified
with integer square-root upper bounds, never floating-point tolerances.
"""
import argparse
from collections import Counter, deque
from itertools import combinations, product
import hashlib
import json
from math import isqrt, prod
from pathlib import Path
import random
import time


def edges(rows):
    return [(i,j) for i in range(len(rows)) for j in range(i+1,len(rows)) if rows[i] >> j & 1]


def from_edges(n, es):
    rows = [0]*n
    for i,j in es:
        rows[i] |= 1 << j
        rows[j] |= 1 << i
    return tuple(rows)


def diameter_at_most_two(rows):
    return all((rows[i] >> j & 1) or (rows[i] & rows[j]) for i in range(len(rows)) for j in range(i+1,len(rows)))


def is_d2c(rows):
    n=len(rows)
    es=edges(rows)
    if n<3 or len(es)==n*(n-1)//2 or not diameter_at_most_two(rows):
        return False
    for i,j in es:
        changed=list(rows)
        changed[i] ^= 1 << j
        changed[j] ^= 1 << i
        if diameter_at_most_two(changed):
            return False
    return True


def bfs_diameter_status(rows, removed=None):
    """Separate path-based implementation: no common-neighbour test."""
    n=len(rows)
    greatest=0
    for source in range(n):
        distances={source:0}
        queue=deque([source])
        while queue:
            u=queue.popleft()
            for w in range(n):
                if not(rows[u] >> w & 1) or (removed is not None and {u,w}==set(removed)):
                    continue
                if w not in distances:
                    distances[w]=distances[u]+1
                    queue.append(w)
        if len(distances)!=n:
            return None
        greatest=max(greatest,max(distances.values()))
    return greatest


def certify_d2c_bfs(rows):
    assert bfs_diameter_status(rows)==2
    for e in edges(rows):
        value=bfs_diameter_status(rows,e)
        assert value is None or value>2, ('noncritical',e)


def cube_face(k):
    # Root 0, face vertices 1..k, then binary cube vertices.
    offset=k+1
    es=[]
    for s in range(1<<k):
        es.append((0,offset+s))
        for j in range(k):
            if not(s >> j & 1):
                es.append((1+j,offset+s))
                es.append((offset+s,offset+(s^(1<<j))))
    return from_edges(offset+(1<<k),es)


def greedy_critical(n, seed):
    rows=[((1<<n)-1)^(1<<i) for i in range(n)]
    order=list(combinations(range(n),2))
    random.Random(seed).shuffle(order)
    for i,j in order:
        rows[i] ^= 1 << j
        rows[j] ^= 1 << i
        if not diameter_at_most_two(rows):
            rows[i] ^= 1 << j
            rows[j] ^= 1 << i
    assert is_d2c(rows)
    return tuple(rows)


def legal_choices(rows,v):
    n=len(rows)
    mask=(1<<n)-1
    H=[mask ^ (1<<i) ^ rows[i] for i in range(n)]
    B=[u for u in range(n) if rows[v] >> u & 1]
    A=[i for i in range(n) if H[v] >> i & 1]
    pairs=[]
    options=[]
    for u,w in combinations(B,2):
        if not(rows[u] >> w & 1):
            continue
        cs=[]
        dual=[]
        for source,supplement in ((u,w),(w,u)):
            for label in A:
                if (H[source] >> label & 1) and (H[source] | H[label]) == mask ^ (1<<supplement):
                    cs.append((source,label,supplement))
                if not(rows[source] >> label & 1) and rows[source] & rows[label] == 1<<supplement:
                    dual.append((source,label,supplement))
        assert sorted(cs)==sorted(dual), ('complement/G witness disagreement',v,u,w)
        assert cs, ('missing quasi-edge',v,u,w)
        pairs.append((u,w))
        options.append(cs)
    return A,B,H,pairs,options


def sqrt_upper(n, scale):
    lo=isqrt(n*scale*scale)
    return lo+(lo*lo != n*scale*scale)


def verify_selection(rows,v,data,selection,counts):
    A,B,H,pairs,_=data
    n=len(rows); a=len(A); b=len(B)
    assert b==max(x.bit_count() for x in rows)
    sel={(u,i):w for u,i,w in selection}
    assert len(sel)==len(selection)==len(pairs)
    assert {tuple(sorted((u,w))) for u,i,w in selection}==set(pairs)
    residual={(u,i) for u in B for i in A if H[u] >> i & 1 and (u,i) not in sel}
    rho={u:sum((u,i) in residual for i in A) for u in B}
    R={i:sum((u,i) in residual for u in B) for i in A}
    x={i:sum((u,i) in sel for u in B) for i in A}
    d={i:sum(rows[i] >> j & 1 for j in A) for i in A}
    s={i:max(0,d[i]-R[i]) for i in A}
    S=sum(s.values()); r=len(residual); f=sum(d.values())//2
    t=len(edges(rows))-b*(n-b)
    assert f==r+t and sum(R.values())==sum(rho.values())==r
    assert all(H[i].bit_count()==a-d[i]+R[i]+x[i] for i in A)
    assert all(x[i]>=s[i] and 0<=s[i]<=a-1 for i in A)
    assert S>=r+2*t
    counts['selections']+=1
    counts['positive_demand_selections']+=int(S>0)
    counts['positive_surplus_selections']+=int(t>0)
    counts['zero_demand_selections']+=int(S==0)
    for u,i,w in selection:
        direct=[]; indirect=[]
        for j in A:
            if not(rows[i] >> j & 1):
                continue
            assert H[u] >> j & 1
            if (u,j) in residual:
                direct.append(j)
            else:
                wj=sel[u,j]
                assert wj!=w and (wj,i) in residual
                assert not(H[i] >> j & 1) and not(H[wj] >> j & 1)
                indirect.append(wj)
        assert len(indirect)==len(set(indirect))<=R[i]
        assert len(direct)<=rho[u]
        assert d[i]==len(direct)+len(indirect)<=rho[u]+R[i]
        assert s[i]<=rho[u]
        counts['selected_injection_checks']+=1
        counts['nonempty_injection_checks']+=int(d[i]>0)
    # Selected-signature union, checked separately from the injection.
    for j in A:
        incoming={u for i in A if rows[i] >> j & 1 for u in B if (u,i) in sel}
        total={u for u in B if H[u] >> j & 1}
        assert incoming<=total
        counts['signature_union_checks']+=1
    H0=max(s.values(),default=0)
    zs=[]; all_radicals=[]
    scale=10**40
    for h in range(1,H0+1):
        I=[i for i in A if s[i]>=h]
        W=sum(s[i] for i in I)
        Z={u for u in B if rho[u]>=h}; z=len(Z)
        loads={u:[i for i in I if (u,i) in sel] for u in B}
        J={u for u in B if len(loads[u])>h}; j=len(J)
        assert all(not loads[u] or u in Z for u in B)
        high_pairs=[]
        for u in J:
            for i in loads[u]:
                w=sel[u,i]
                others=[k for k in loads[u] if k!=i]
                assert all(H[w] >> k & 1 for k in others)
                selected_others=[k for k in others if (w,k) in sel]
                if selected_others:
                    assert rho[w]>=s[selected_others[0]]>=h
                    counts['supplement_selected_cases']+=1
                else:
                    assert all((w,k) in residual for k in others)
                    assert len(others)>=h and rho[w]>=h
                    counts['supplement_residual_cases']+=1
                assert w in Z
                high_pairs.append(tuple(sorted((u,w))))
        assert len(high_pairs)==len(set(high_pairs))<=j*(z-j)+j*(j-1)//2
        assert W<=sum(map(len,loads.values()))<=(z-j)*h+j*z-j*(j+1)//2
        assert 2*W<=z*z-z+h*(h+1)
        assert z>=H0>=h
        q=z-h
        assert (q-j)*(q-j-1)>=0
        assert sum(sqrt_upper(2*a*s[i]-h*h,scale) for i in I)<=a*z*scale
        all_radicals.extend(2*a*s[i]-h*h for i in I)
        zs.append(z)
        counts['threshold_checks']+=1
        counts['high_load_threshold_checks']+=int(bool(J))
    assert sum(zs)==sum(min(rho[u],H0) for u in B)<=r
    if a:
        assert sum(sqrt_upper(q,scale) for q in all_radicals)<=a*r*scale
    else:
        assert len(edges(rows))==n-1 and t==0
        counts['star_zero_a_controls']+=1
    return {'a':a,'b':b,'r':r,'t':t,'S':S,'H0':H0,'demands':[s[i] for i in A],'residual_source_degrees':[rho[u] for u in B]}


def verify_graph(rows,name,counts,coverage,limit,samples,seed):
    assert is_d2c(rows),name
    certify_d2c_bfs(rows)
    counts['graphs']+=1
    counts['independent_bfs_edge_deletions']+=len(edges(rows))
    deg=max(x.bit_count() for x in rows)
    root_results=[]
    for v,row in enumerate(rows):
        if row.bit_count()!=deg:
            continue
        data=legal_choices(rows,v)
        options=data[-1]
        size=prod(map(len,options))
        counts['maximum_degree_roots']+=1
        if size<=limit:
            assignments=product(*options)
            kind='EXHAUSTIVE'
            counts['roots_all_selections_exhausted']+=1
        else:
            rng=random.Random(seed+v)
            chosen={tuple(cs[0] for cs in options),tuple(cs[-1] for cs in options)}
            for _ in range(samples):
                chosen.add(tuple(rng.choice(cs) for cs in options))
            assignments=sorted(chosen)
            kind='SAMPLED'
            counts['roots_sampled_selections']+=1
        checked=0; positives=0; demands=set()
        for selection in assignments:
            result=verify_selection(rows,v,data,selection,counts)
            checked+=1; positives+=int(result['S']>0)
            demands.add(tuple(result['demands']))
            if result['S']>0 and len(coverage['positive_demand_examples'])<12:
                coverage['positive_demand_examples'].append({'name':name,'n':len(rows),'root':v,'edges':edges(rows),'selection':selection,**result})
        root_results.append({'root':v,'selection_space_size':size,'selection_mode':kind,'checked':checked,'positive_demand_assignments':positives,'distinct_demand_profiles':len(demands)})
        counts['roots_with_choice_dependent_profile']+=int(len(demands)>1)
    return {'name':name,'n':len(rows),'m':len(edges(rows)),'maximum_degree':deg,'roots':root_results}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-exhaustive-n',type=int,default=6)
    ap.add_argument('--random-seeds',type=int,default=12)
    ap.add_argument('--max-random-n',type=int,default=16)
    ap.add_argument('--selection-limit',type=int,default=1024)
    ap.add_argument('--samples',type=int,default=24)
    ap.add_argument('--output',default='RESULTS.json')
    args=ap.parse_args()
    begin=time.monotonic(); counts=Counter(); coverage={'positive_demand_examples':[]}; fixtures=[]
    seen=set()
    def check(rows,name):
        if rows in seen: return
        seen.add(rows)
        fixtures.append(verify_graph(rows,name,counts,coverage,args.selection_limit,args.samples,20260922+len(fixtures)))
    for n in range(3,args.max_exhaustive_n+1):
        es=list(combinations(range(n),2))
        for mask in range(1<<len(es)):
            counts['labelled_graphs_enumerated']+=1
            rows=from_edges(n,[e for i,e in enumerate(es) if mask>>i&1])
            if is_d2c(rows): check(rows,f'exhaustive_n{n}_mask{mask}')
    for n in range(4,21):
        lo=n//2
        rows=from_edges(n,[(i,j) for i in range(lo) for j in range(lo,n)])
        assert len(edges(rows))==n*n//4
        check(rows,f'balanced_K_{lo}_{n-lo}')
        check(from_edges(n,[(0,i) for i in range(1,n)]),f'star_n{n}')
    for k in (3,4,5):
        rows=cube_face(k)
        if k==3: assert len(rows)==12 and len(edges(rows))==32 and ((len(rows)-1)**2)//4+1==31
        check(rows,f'X_{k}')
    for n in range(7,args.max_random_n+1):
        for seed in range(args.random_seeds):
            check(greedy_critical(n,20260922+1000*n+seed),f'greedy_n{n}_seed{seed}')
    output={'status':'PASS','scope':'actual D2C graphs; finite diagnostic, not proof of all graphs','parameters':vars(args),'counts':dict(sorted(counts.items())),'coverage':coverage,'fixtures':fixtures,'elapsed_seconds':round(time.monotonic()-begin,4),'exact_arithmetic':'integers; profile radical bounds certified using isqrt at scale 10^40','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(args.output).write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ('fixtures','coverage')},indent=2))


if __name__=='__main__':
    main()
