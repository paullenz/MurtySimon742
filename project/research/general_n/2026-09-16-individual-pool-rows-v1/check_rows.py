#!/usr/bin/env python3
"""Row-specific one-hole demand prices. Internal necessary-condition tests only.
Python uses sorted pool vectors and greedy unit prices; C++ uses ordered
pool compositions and bounded-allocation dynamic programming. No original
critical graphs or catalogue states are enumerated. Run beside verify_rows.cpp.
"""
from __future__ import annotations
import collections
import itertools
import json
import math
from pathlib import Path
import subprocess
import tempfile

DOMAIN = [(d,z) for d in range(3,11) for z in (1,2)]


def partitions(total: int, length: int, lower: int=0):
    """Nondecreasing nonnegative vectors of specified sum and length."""
    if length == 0:
        if total == 0:
            yield ()
        return
    for x in range(lower, total//length+1):
        for tail in partitions(total-x, length-1, x):
            yield (x,)+tail


def compositions(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for x in range(total+1):
        for tail in compositions(total-x, length-1):
            yield (x,)+tail


def row_minimum(d: int, z: int) -> dict:
    if d < 3 or z < 1:
        raise ValueError('Requires d>=3 and z>=1')
    k0=1+z*(d-1)
    h0=(2*k0+d-3)//(d-2)
    best=d*h0
    winners=[]
    feasible=0
    by_h=[10**9]*(h0+1)
    for h in range(h0+1):
        k=k0+h
        for L in range(d*h//(d-1)+1):
            Q=d*h-(d-1)*L
            for u in partitions(L,d):
                caps=[h-L+x for x in u]
                if min(caps) < 0:
                    continue
                orbit=math.factorial(d)
                for count in collections.Counter(u).values():
                    orbit//=math.factorial(count)
                # Unit prices for up to k one-hole labels, sorted cheapest first.
                prices=sorted(max(0,d-1-z-x)
                              for x,cap in zip(u,caps)
                              for _ in range(min(cap,k)))
                prefix=[0]
                for price in prices:
                    prefix.append(prefix[-1]+price)
                for n0 in range(k+1):
                    for N in range(min(k-n0,len(prices))+1):
                        n2=k-n0-N
                        if N+2*n2 > Q:
                            continue
                        feasible+=orbit
                        val=d*h+(d-2)*L+(d-1)*n0+prefix[N]
                        by_h[h]=min(by_h[h],val)
                        key=[h,L,*u,n0,N,n2]
                        if val < best:
                            best=val
                            winners=[]
                        if val == best:
                            winners.append(key)
    return dict(d=d,z=z,h_cutoff=h0,minimum=best,
                ordered_pool_and_type_tuples=feasible,
                minima_by_h=by_h,minimizers=sorted(winners))


def coarse_d5() -> dict:
    # Fresh full-composition replay of just the predecessor's d=5,z=2 scalar case.
    d,z=5,2
    k0=9
    best=10**9
    winners=[]
    feasible=0
    for h in range(7):
        k=k0+h
        for L in range(5*h//4+1):
            for n0 in range(k+1):
                for N in range(k-n0+1):
                    n2=k-n0-N
                    if N+2*n2>5*h-4*L:
                        continue
                    feasible+=1
                    val=5*h+3*L+4*n0+max(0,2-L)*N
                    if val<best:
                        best=val;winners=[]
                    if val==best:
                        winners.append([h,L,n0,N,n2])
    assert best==30
    assert winners==[[4,2,1,12,0],[6,0,0,0,15]]
    return dict(minimum=best,feasible_tuples=feasible,minimizers=winners)


def targeted_patterns() -> dict:
    rows=[]
    for u in compositions(2,5):
        pools=[2+x for x in u]
        n=[2+x for x in u]  # Sum is 12, so every row capacity is saturated.
        deficit=sum(nt*max(0,4-p) for nt,p in zip(n,pools))
        assert deficit in (16,18)
        assert sum(n)==12
        rows.append(dict(u=list(u),pools=pools,one_hole_counts=n,
                         additional_deficit=deficit,total_slack=30+deficit))
    assert collections.Counter(r['additional_deficit'] for r in rows)=={16:5,18:10}
    # Alternative attaining the ROW MODEL minimum: not an original graph.
    holes=list(itertools.combinations(range(5),2))
    holes += [(0,1),(1,2),(2,3),(3,4),(0,4)]
    q=[sum(t in pair for pair in holes) for t in range(5)]
    assert len(holes)==15 and q==[6]*5
    delta_T=[4+15-qt for qt in q]
    R_T=[dt-5 for dt in delta_T]
    assert R_T==[8]*5
    assert R_T==[10-2]*5
    return dict(targeted_distributions=rows,
                minimum_additional_deficit=16,
                surviving_two_hole_interface=dict(
                    d=5,z=2,h=6,L=0,kappa=15,pools=[2]*5,
                    holes=[list(pair) for pair in holes],q=q,delta_T=delta_T,
                    R_T=R_T,mu=0,beta=[0]*5,n0=0,n1=0,n2=15,
                    row_model_slack=30,canonical_realization='NOT_ASSERTED'))


def relaxed_interface_checks() -> dict:
    # Small exact T/K binary interfaces. Only row/price algebra is being tested.
    cases=0
    for d,z,k in ((3,1,3),(3,1,4),(3,2,5),(3,2,6),(4,1,4)):
        h=k-1-z*(d-1)
        internal=list(itertools.combinations(range(d),2))
        for u in itertools.product((0,1),repeat=d):
            L=sum(u)
            caps=[h-L+x for x in u]
            if min(caps)<0:
                continue
            for tm in range(1<<len(internal)):
                nu=[0]*d
                for bit,(s,t) in enumerate(internal):
                    if tm>>bit&1:
                        nu[s]+=1;nu[t]+=1
                allowed=[caps[t]-nu[t] for t in range(d)]
                if min(allowed)<0:
                    continue
                choices=[[v for v in range(1<<k) if v.bit_count()<=c]
                         for c in allowed]
                for missing in itertools.product(*choices):
                    # A K-label must be adjacent to at least one tight label.
                    all_missing=(1<<k)-1
                    for row in missing:
                        all_missing &= row
                    if all_missing:
                        continue
                    n=[0]*d;n0=n2=0
                    for j in range(k):
                        col=[t for t in range(d) if missing[t]>>j&1]
                        if len(col)==0:n0+=1
                        elif len(col)==1:n[col[0]]+=1
                        else:n2+=1
                    q=[v.bit_count() for v in missing]
                    beta=[caps[t]-nu[t]-q[t] for t in range(d)]
                    assert min(beta)>=0
                    assert all(n[t]<=q[t]<=caps[t] for t in range(d))
                    assert sum(n)+2*n2<=sum(q)<=d*h-(d-1)*L
                    eta=(d-1)*n0+sum(n[t]*max(0,d-1-z-u[t]) for t in range(d))
                    coarse=(d-1)*n0+max(0,d-1-z-L)*sum(n)
                    assert eta>=coarse
                    cases+=1
    return dict(cases=cases,scope='Small binary tight interfaces; not full selected systems')


def main() -> None:
    root=Path(__file__).resolve().parent
    py=[row_minimum(d,z) for d,z in DOMAIN]
    with tempfile.TemporaryDirectory(prefix='pool-rows-') as tmp:
        exe=Path(tmp)/'verify'
        subprocess.run(['g++','-std=c++17','-O2','-Wall','-Wextra',
                        str(root/'verify_rows.cpp'),'-o',str(exe)],check=True,timeout=30)
        out=subprocess.run([str(exe)],check=True,text=True,
                           stdout=subprocess.PIPE,timeout=40)
    cpp=json.loads(out.stdout)
    assert py==cpp, {'python':py,'cpp':cpp}
    (root/'ROW_MINIMIZERS.json').write_text(json.dumps(py,indent=2)+'\n')
    table=[]
    old_B2={3:8,4:17,5:30,6:35,7:39,8:40,9:45,10:50}
    for row in py:
        if row['z']!=2:continue
        d=row['d'];B=row['minimum']
        threshold=(2*d*(2*d-3)+B-d+4+d-3)//(d-2)
        table.append(dict(d=d,previous_B=old_B2[d],row_B=B,
                          minimum_a_for_extras_tau1=threshold))
    result=dict(status='PASS_TARGETED_ROW_MODEL_CHECKS_ONLY',
        python_cpp_exact_agreement=True,parameter_pairs=len(py),
        ordered_pool_and_type_tuples=sum(r['ordered_pool_and_type_tuples'] for r in py),
        tuple_count_definition='(h,L,ordered u,n0,total one-hole count,n2); not every n_t allocation',
        comparison='Exact minima, all h-slice minima, feasible tuple counts, complete symmetry-reduced minimizing keys; greedy versus dynamic programming',
        fresh_predecessor_d5_replay=coarse_d5(),
        patterns=targeted_patterns(),interfaces=relaxed_interface_checks(),thresholds=table,
        negative_controls=[
            'Giving all twelve one-hole labels the cheapest pool price misses at least sixteen units.',
            'Deleting one coarse minimizer does not delete the two-hole minimizer.',
            'The explicit attaining object is a T/K incidence interface, not an original critical graph.',
            'One-hole prices are not imposed on multi-hole labels without a separate source lemma.'
        ],
        scope='Conditional row and price relaxation only; both implementations by the same assistant',
        original_graph_enumeration='NOT_RUN',catalogue_replay='NOT_RUN',
        canonical_bridge_validation='NOT_ASSERTED',independent_expert_review='OPEN')
    (root/'CHECK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
