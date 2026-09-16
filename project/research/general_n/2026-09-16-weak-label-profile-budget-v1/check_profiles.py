#!/usr/bin/env python3
"""Weak-label profile bounds: relaxed checks, NOT original-graph enumeration.
Run beside verify_minima.cpp; uses only Python stdlib and a C++17 compiler.
"""
from __future__ import annotations
import csv, hashlib, itertools, json, subprocess, tempfile
from pathlib import Path

def ceildiv(a: int, b: int) -> int:
    assert b > 0
    return -(-a // b)

def domain() -> list[tuple[int,int]]:
    return [(d,z) for d in range(3,21) for z in range(1,min(d,4)+1)] + [(d,z) for d in range(21,51) for z in (1,2)]

def minimum(d: int, z: int) -> dict:
    k0=1+z*(d-1); h0=ceildiv(2*k0,d-2)
    best=d*h0; winners=[]; feasible=0
    for h in range(h0+1):
        k=k0+h
        for L in range(d*h//(d-1)+1):
            q=d*h-(d-1)*L; f=max(0,d-1-z-L)
            for n0 in range(max(0,k-q),k+1):
                lo=max(0,2*(k-n0)-q); hi=k-n0
                assert lo<=hi
                feasible+=hi-lo+1
                val=d*h+(d-2)*L+(d-1)*n0+f*lo
                if val>best: continue
                if val<best: best=val; winners=[]
                for n1 in range(lo,hi+1 if f==0 else lo+1):
                    winners.append([h,L,n0,n1,k-n0-n1])
    assert best>=d*(z+1)-1
    return dict(d=d,z=z,h_cutoff=h0,minimum=best,feasible_tuples=feasible,minimizers=winners)

def profile_checks() -> dict:
    counts={}; cases=0
    for d,max_b in ((3,8),(4,6),(5,4)):
        full=(1<<d)-1
        # Nonempty proper residual subsets of T: positive activity, low sources.
        choices=list(range(1,full))
        n=0
        for b in range(max_b+1):
            for residuals in itertools.combinations_with_replacement(choices,b):
                pools=[sum(r==(full^(1<<t)) for r in residuals) for t in range(d)]
                m=sum(pools)
                R=[sum(bool(r&(1<<t)) for r in residuals) for t in range(d)]
                beta=[R[t]-(m-pools[t]) for t in range(d)]
                assert min(beta)>=0
                outside=[r for r in residuals if r.bit_count()!=d-1]
                assert sum(beta)==sum(r.bit_count() for r in outside)
                for t in range(d):
                    needed=full^(1<<t)
                    directly_eligible=sum((r&needed)==needed for r in residuals)
                    assert directly_eligible==pools[t]
                assert not any((r&full)==full for r in residuals)
                n+=1
        counts[str(d)]=n; cases+=n
    return dict(cases=cases,by_d=counts,scope='T-residual multisets and A-side eligibility only; not selected-system realizations')

def interface_checks(mins: dict[tuple[int,int],int]) -> dict:
    scenarios=[(3,1,k) for k in range(3,7)]+[(3,2,k) for k in range(5,8)]+[(4,1,k) for k in range(4,6)]
    rows=[]; all_cases=0
    for d,z,k in scenarios:
        h=k-1-z*(d-1); full=(1<<k)-1; count=0
        pairs=list(itertools.combinations(range(d),2))
        for u in itertools.product((0,1),repeat=d):
            L=sum(u); p=[z+v for v in u]; m=sum(p)
            for internal_missing in range(1<<len(pairs)):
                nu=[0]*d
                for bit,(i,j) in enumerate(pairs):
                    if internal_missing&(1<<bit): nu[i]+=1; nu[j]+=1
                allowance=[h-L+u[t]-nu[t] for t in range(d)]
                if min(allowance)<0: continue
                choices=[[mask for mask in range(1<<k) if mask.bit_count()<=allowance[t]] for t in range(d)]
                for holes in itertools.product(*choices):
                    all_missing=full
                    for row in holes: all_missing &= row
                    if all_missing: continue # Every K label has a tight neighbour.
                    sizes=[sum(bool(row&(1<<j)) for row in holes) for j in range(k)]
                    n0=sizes.count(0); n1=sizes.count(1); n2=k-n0-n1
                    Q=sum(sizes); mu=internal_missing.bit_count()
                    R=[k-1-nu[t]-holes[t].bit_count() for t in range(d)]
                    beta=[R[t]-(m-p[t]) for t in range(d)]
                    assert min(beta)>=0
                    assert 2*mu+Q+sum(beta)==d*h-(d-1)*L
                    eta=(d-1)*n0
                    for j in range(k):
                        if sizes[j]==1:
                            t=next(t for t in range(d) if holes[t]&(1<<j))
                            eta+=max(0,d-1-p[t])
                    f=max(0,d-1-z-L)
                    assert eta >= (d-1)*n0+f*n1
                    assert n1+2*n2<=Q<=d*h-(d-1)*L
                    assert d*h+(d-2)*L+eta>=mins[d,z]
                    count+=1
        rows.append(dict(d=d,z=z,kappa=k,cases=count)); all_cases+=count
    return dict(cases=all_cases,rows=rows,scope='Relaxed binary tight interfaces with profile counts; not original graphs')

def controls() -> list:
    # A source with the correct profile need not be used by a tight obligation.
    d=5; c=[2]*d; p=[3,2,2,2,2]
    needed=[sum(p)-p[t] for t in range(d)]
    old=[sum(c)-c[t] for t in range(d)]
    assert [needed[t]-old[t] for t in range(d)]==[0,1,1,1,1]
    # Labels with >=2 missing tight neighbours can use non-full residual profiles.
    d=4; neighbors=0b0011; residual=0b0011
    assert neighbors&residual==neighbors and residual.bit_count()<d-1
    # Zero demand alone does not prove unselection.
    assert max(0,2-2)==0 and 1>=max(0,2-2)
    return [dict(kind='used_pool_is_not_full_profile_pool',d=5,used=c,full=p,
                 tight_residual_increment=[0,1,1,1,1],extra_residual_cost=4,
                 scope='Local capacity control, not canonical realization'),
            dict(kind='one_hole_eligibility_does_not_extend_to_two_holes',d=4,
                 tight_neighbours='0011',possible_residual_profile='0011'),
            dict(kind='zero_demand_not_zero_selected_degree',degree=2,residual_degree=2,selected_degree=1),
            dict(kind='relaxed_minimum_not_graph_realization',d=5,z=2,h=4,L=2,n0=1,n1=12,n2=0,
                 note='The scalar minimizer allows all weak labels the largest profile; individual pool caps are not imposed.')]

def main() -> None:
    root=Path(__file__).resolve().parent
    py=[minimum(d,z) for d,z in domain()]
    with tempfile.TemporaryDirectory(prefix='weak-profiles-') as tmp:
        exe=Path(tmp)/'verify'
        subprocess.run(['g++','-std=c++17','-O2','-Wall','-Wextra',str(root/'verify_minima.cpp'),'-o',str(exe)],check=True,timeout=30)
        out=subprocess.run([str(exe)],text=True,stdout=subprocess.PIPE,check=True,timeout=40)
    cpp=json.loads(out.stdout)
    assert py==cpp, 'Python/C++ minima, feasible counts or full minimizer lists disagree'
    text=json.dumps(py,separators=(',',':'))+'\n'
    (root/'MINIMIZERS.json').write_text(text)
    mins={(r['d'],r['z']):r['minimum'] for r in py}
    thresholds=[]
    for d in range(3,13):
        B=mins[d,2]; anyB=mins[d,1]
        old=4*d+4+ceildiv(11,d-2)
        new=ceildiv(2*d*(2*d-3)+B-d+4,d-2)
        any_new=ceildiv(d*(2*d-3)+anyB-d+4,d-2)
        assert new>=old
        thresholds.append(dict(d=d,tau=1,B_extras=B,old_min_a_extras=old,new_min_a_extras=new,new_min_a_any_block=any_new))
    result=dict(status='PASS_TARGETED_PROFILE_AND_RELAXATION_CHECKS_ONLY',
                scalar_domain='d=3..20,z=1..min(d,4); d=21..50,z=1,2',
                scalar_pairs=len(py),feasible_scalar_tuples=sum(r['feasible_tuples'] for r in py),
                exact_minima_counts_and_all_minimizers_match=True,
                minimizers_sha256=hashlib.sha256(text.encode()).hexdigest(),
                profile_checks=profile_checks(),interface_checks=interface_checks(mins),
                thresholds=thresholds,negative_controls=controls(),
                scope='Necessary-condition relaxations only; both implementations by same assistant',
                original_graph_enumeration='NOT_RUN',catalogue_replay='NOT_RUN',
                canonical_bridge_validation='NOT_ASSERTED',independent_expert_review='OPEN')
    (root/'CHECK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
