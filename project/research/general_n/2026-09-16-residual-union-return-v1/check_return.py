#!/usr/bin/env python3
"""Internal necessary-condition tests; not original graph enumeration."""
from __future__ import annotations
import base64, gzip, hashlib, itertools, json, subprocess, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def block_cost(block: tuple[int, ...], flags: int, a: int, lam: int,
               use_reverse: bool = True) -> int | None:
    if len({i // 2 for i in block}) != len(block):
        return None
    bits = [(flags >> i) & 1 for i in block]
    if use_reverse and len(block) > 1 and any(bits):
        return None
    core = sum(1-b for b in bits)
    reserve = max(a+b-((flags >> (i^1)) & 1) for i,b in zip(block,bits))
    degree = max(core+reserve, lam if any(bits) else 0)
    return degree-1 if degree <= a+1 else None

def direct_partitions(p: int, flags: int, a: int, lam: int,
                      use_reverse: bool = True) -> tuple[int,int,int]:
    # Enumerate actual set partitions, not a subset-cost dynamic program.
    costs: list[int] = []
    def visit(rem: tuple[int,...], accumulated: int) -> None:
        if not rem:
            costs.append(accumulated); return
        first, rest = rem[0], rem[1:]
        for size in range(min(p-1,len(rest))+1):
            for other in itertools.combinations(rest,size):
                block=(first,)+other
                cost=block_cost(block,flags,a,lam,use_reverse)
                if cost is not None:
                    chosen=set(block)
                    visit(tuple(x for x in rest if x not in chosen),accumulated+cost)
    visit(tuple(range(2*p)),0)
    low=min(costs)
    return low,len(costs),costs.count(low)

def closed_cost(p: int, flags: int, a: int, lam: int) -> int:
    n00=n11=mix=0
    for t in range(p):
        state=(flags>>(2*t))&3
        n00 += state==0; n11 += state==3; mix += state in (1,2)
    return 2*a*n00+2*(max(a,lam)-1)*n11+a*mix+a*(mix//2)+(a-1)*(mix%2)

def receiver_presence_checks() -> dict:
    cases=eligible_cases=shared_cases=0
    for sizes in [(2,),(3,),(4,),(2,2),(2,3),(3,3),(2,2,2),(2,2,3)]:
        groups=[]; start=0
        for g in sizes:
            groups.append(set(range(start,start+g))); start+=g
        for pattern in itertools.product(range(3),repeat=start):
            selected={i for i,x in enumerate(pattern) if x==2}
            present={i for i,x in enumerate(pattern) if x}
            arrivals=[]
            for t,group in enumerate(groups):
                missing=group-present
                if len(missing)==1 and selected<=group:
                    arrivals.append((t,next(iter(missing))))
            cases+=1
            if arrivals: eligible_cases+=1
            if len(arrivals)>=2:
                shared_cases+=1; assert not selected
            if selected and arrivals:
                assert len(arrivals)==1
    return dict(ternary_neighbourhoods=cases,with_eligible_arrival=eligible_cases,
                with_multiple_eligible_bundles=shared_cases)

def matrix_checks() -> dict:
    matrix_cases=endpoint_cases=0
    for g in range(2,5):
        off=[(i,j) for i in range(g) for j in range(g) if i!=j]
        for mask in range(1<<len(off)):
            selected=[set() for _ in range(g)]
            for bit,(i,j) in enumerate(off):
                if mask>>bit&1: selected[i].add(j)
            residual=[set(range(g))-{i}-selected[i] for i in range(g)]
            b=[len(s) for s in selected]
            d=[sum(i in row for row in selected) for i in range(g)]
            assert sum(b)==sum(d)
            for i in range(g):
                assert sum(i in row for row in residual)==g-1-d[i]
            matrix_cases+=1
        for h,s,C,b,d in itertools.product(range(6),range(1,4),range(6),range(g),range(g)):
            R=h+g-1-d; delta=R+s
            for f in range(g-b):
                forced=max(0,delta-C-f)
                required=max(0,h+s-C-d+b)
                assert forced>=required
                endpoint_cases+=1
    return dict(companion_selection_matrices=matrix_cases,
                positive_demand_endpoint_arrays=endpoint_cases)

def controls() -> list[dict]:
    # Without reverse containment a receiver can select mates from several bundles.
    good=direct_partitions(2,15,3,2)[0]
    bad=direct_partitions(2,15,3,2,False)[0]
    assert good==8 and bad==4
    # A stronger selected-mate degree floor is not supplied by demand two alone.
    assert direct_partitions(1,3,3,2)[0]==4
    assert direct_partitions(1,3,3,4)[0]==6
    # Two different bundles may share non-family residual labels.
    assert block_cost((0,2),10,3,4)==3
    # One shared label breaks the disjoint-bundle intersection conclusion.
    left={0,2}; right={1,2}; selected={2}; present={2}
    assert selected<=left and selected<=right
    assert len(left-present)==len(right-present)==1
    # s=0 does not imply delta=R+s.
    assert max(0,0-5)==0 and 0!=5+0
    return [dict(kind='reverse_containment_required',p=2,flags=15,
                 full_relaxation_cost=good,without_reverse_cost=bad),
            dict(kind='selected_mate_floor_requires_proof',p=1,flags=3,
                 natural_floor_2_cost=4,extra_floor_4_cost=6),
            dict(kind='nonfamily_reserves_overlap',mixed_residual_types=2,
                 distinct_family_mates=2,shared_external_labels=2,rho=4),
            dict(kind='overlapping_bundles_do_not_force_empty_intersection',
                 groups=[[0,2],[1,2]],receiver_selected=[2]),
            dict(kind='positive_demand_required',delta=0,R=5,s=0),
            dict(kind='monitor_copies_must_not_multiply_cost',
                 statement='The theorem selects one source per bundle; additional copies may reuse destinations.'),
            dict(kind='receiver_budget_is_not_sigma_O',
                 statement='Receivers may be internal; count W once outside H and all intact monitors, not automatically outside V.')]

def main() -> None:
    rows=[]
    for p in range(1,5):
        for a in range(2,7):
            for lam in (1,a,a+1):
                for flags in range(1<<(2*p)):
                    value,total,opt=direct_partitions(p,flags,a,lam)
                    assert value==closed_cost(p,flags,a,lam)
                    if a==3:
                        assert value>=4*p
                        if lam==4: assert value>=(9*p+1)//2
                    rows.append([p,a,lam,flags,value,total,opt])
    with tempfile.TemporaryDirectory() as td:
        binary=Path(td)/'verify'
        subprocess.run(['g++','-O2','-std=c++17','-Wall','-Wextra',
                        str(ROOT/'verify_return.cpp'),'-o',str(binary)],check=True,timeout=25)
        cp=subprocess.run([str(binary)],check=True,text=True,stdout=subprocess.PIPE,timeout=25)
    cpp=[list(map(int,line.split())) for line in cp.stdout.splitlines()]
    assert rows==cpp
    raw=json.dumps(rows,separators=(',',':')).encode()
    (ROOT/'EXACT_ROWS.json.gz').write_bytes(gzip.compress(raw,mtime=0))
    # A compact symmetry-reduced record retains every observed cost/count triple.
    index={}
    for p,a,lam,flags,value,total,opt in rows:
        states=[(flags>>(2*t))&3 for t in range(p)]
        key=(p,a,lam,states.count(0),states.count(3),sum(x in (1,2) for x in states))
        result=(value,total,opt)
        assert key not in index or index[key]==result
        index[key]=result
    compact={'columns':['p','A','lambda','n00','n11','mixed','cost','partitions','optimal_partitions'],
             'rows':[list(k)+list(v) for k,v in sorted(index.items())],
             'full_domain_sha256':hashlib.sha256(raw).hexdigest()}
    (ROOT/'SYMMETRY_ROWS.json').write_text(json.dumps(compact,separators=(',',':'))+'\n')
    summary=dict(status='PASS_TARGETED_MIXED_RETURN_CHECKS_ONLY',
                 exact_python_cpp_rows=len(rows),symmetry_rows=len(index),
                 compatible_partitions_total=sum(r[5] for r in rows),
                 full_table_sha256=hashlib.sha256(raw).hexdigest(),
                 presence=receiver_presence_checks(),return_matrices=matrix_checks(),
                 controls=controls(),
                 five_pairs=dict(A=3,receiver_ceiling=4,
                                 bound_with_selected_floor_at_most_3=20,
                                 bound_with_selected_floor_4=23,
                                 no_selected_mates_bound=30),
                 scope='Necessary receiver-resource and local incidence models; not original graphs or catalogue replay',
                 independent_expert_review='OPEN',both_implementations='same assistant')
    (ROOT/'CHECK_RESULTS.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
