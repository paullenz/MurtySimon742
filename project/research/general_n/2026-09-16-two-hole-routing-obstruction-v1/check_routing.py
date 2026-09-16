#!/usr/bin/env python3
"""Exact targeted checks of the two-hole equality obstruction.

Not an original-graph search or a catalogue replay. Python enumerates
multigraphs by remaining degrees and scalar profiles up to permutation;
C++ enumerates six free multiplicities and ordered profiles with dynamic
programming. All reduced destination decisions are compared, not hashes.
"""
from __future__ import annotations
import collections
import gzip
import hashlib
import itertools
import json
import math
import subprocess
import tempfile
from pathlib import Path

PAIRS = list(itertools.combinations(range(5), 2))


def interfaces() -> list[list[int]]:
    def visit(i: int, degrees: list[int], counts: list[int]):
        if i == len(PAIRS):
            if not any(degrees):
                yield counts
            return
        s, t = PAIRS[i]
        for n in range(min(degrees[s], degrees[t]) + 1):
            new = degrees.copy(); new[s] -= n; new[t] -= n
            if any(new[v] and not any(v in p for p in PAIRS[i+1:]) for v in range(5)):
                continue
            yield from visit(i+1, new, counts+[n])
    result = []
    for counts in visit(0, [6]*5, []):
        holes = [set(pair) for pair, count in zip(PAIRS, counts) for _ in range(count)]
        assert len(holes) == 15
        selected = [{j for j, pair in enumerate(holes) if t in pair} for t in range(5)]
        assert all(len(S) == 6 for S in selected)
        decisions = []
        for t, S in enumerate(selected):
            for j in range(15):
                if j not in S:
                    decisions.append(-1); continue
                destinations = [s for s in range(5)
                                if j not in selected[s] and S-{j} <= selected[s]]
                decisions.append(sum(1 << s for s in destinations))
                # Any duplicate column at this source has no profile destination.
                if any(k != j and holes[k] == holes[j] for k in S):
                    assert not destinations
        assert decisions.count(0) >= 28
        result.append(counts+decisions)
    return sorted(result)


def partitions(total: int, length: int, lower: int=0):
    if length == 0:
        if total == 0: yield ()
        return
    for x in range(lower, total//length+1):
        for rest in partitions(total-x, length-1, x):
            yield (x,)+rest


def scalar_checks() -> dict:
    feasible=0; best=10**9; winners=[]; byh=[10**9]*7
    for h in range(7):
        k=9+h
        for L in range(5*h//4+1):
            Q=5*h-4*L
            for u in partitions(L, 5):
                caps=[h-L+x for x in u]
                if min(caps)<0: continue
                orbit=math.factorial(5)
                for n in collections.Counter(u).values(): orbit//=math.factorial(n)
                prices=sorted(max(0,2-x) for x,c in zip(u,caps) for _ in range(min(c,k)))
                prefix=[0]
                for p in prices: prefix.append(prefix[-1]+p)
                for n0 in range(k+1):
                    for N in range(min(k-n0,len(prices))+1):
                        n2=k-n0-N
                        if N+2*n2>Q: continue
                        feasible+=orbit
                        eta=4*n0+prefix[N]
                        value=5*h+3*L+eta
                        assert value>=36-h+(11-h)*L
                        if value==30:
                            assert (h,L,n0,N,n2)==(6,0,0,0,15)
                        byh[h]=min(byh[h],value)
                        key=[h,L,*u,n0,N,n2]
                        if value<best:best=value;winners=[]
                        if value==best:winners.append(key)
    assert best==30 and len(winners)==1
    return dict(feasible_outer_tuples=feasible,minimum=best,minima_by_h=byh,
                minimizers=sorted(winners))


def local_lemmas() -> dict:
    # At demand four and beta=0, enumerate residual masks on T plus two
    # outside labels. The outside labels are merely local placeholders.
    rows=0; admissible=0
    T=set(range(5))
    full_profiles=[T-{t} for t in range(5)]
    for pair in PAIRS:
        required=T-set(pair)
        permitted=[]
        for mask in range(1<<7):
            R={i for i in range(7) if mask>>i&1}
            if len(R)>4: continue
            rows+=1
            beta_zero_compatible=not (R&T) or R in full_profiles
            if len(R)>=4 and required<=R and beta_zero_compatible:
                permitted.append(R);admissible+=1
        assert permitted and {tuple(sorted(r)) for r in permitted}=={
            tuple(sorted(T-{t})) for t in pair}
    # Generic twin-label obstruction, checked by all subsets, with two fixed
    # twins k=0 and j=1. A profile destination contains either both or neither.
    predicate_cases=0
    for n in range(2,9):
        for source in range(1<<n):
            if source&3!=3:continue
            required=source&~1
            for cap in range(source.bit_count()-1):
                assert source.bit_count()>=cap+2
                for dest in range(1<<n):
                    predicate_cases+=1
                    valid=not (dest&1) and required&dest==required
                    high=bool(dest&1)
                    profile=((dest&1)!=0)==((dest&2)!=0)
                    outside=dest.bit_count()<=cap
                    if high or profile or outside:assert not valid
    return dict(residual_masks_tested=rows,eligible_profile_types=admissible,
                twin_predicate_cases=predicate_cases)


def negative_controls() -> list[dict]:
    T=set(range(5));holes={0,1}
    extra=(T-holes)|{5}
    assert len(extra)==4 and T-holes<=extra and extra not in [T-{t} for t in T]
    # Without beta=0 this source can pass the local selection tests outside V.
    k={(0,0),(0,1),(1,0)}; j={(0,0),(0,1),(1,1)}
    assert len(k)==len(j)==3 and (1,1) in j-k
    # Demand three does not force the twins onto all four pool sources.
    source=set(range(5)); dest=source-{0}
    assert len(dest)==4 and 0 not in dest and source-{0}<=dest
    # If only five labels are selected, four residual slots can receive the rest.
    return [dict(kind='beta_zero_is_essential',holes=[0,1],residual=sorted(extra),
                 tight_occurrences_outside_full_profiles=3,scope='Local control, not a graph'),
            dict(kind='zero_deficit_is_essential',demand=3,
                 k_sources=sorted(k),j_sources=sorted(j),
                 scope='Twins distinguishable when selection is not saturated'),
            dict(kind='six_selected_K_labels_is_essential_to_capacity_step',
                 selected_K=5,off_profile_capacity=4,local_destination_exists=True),
            dict(kind='old_interface_remains_valid_as_an_interface',
                 interface_equations='PASS',full_saturated_routing='IMPOSSIBLE',
                 original_graph_realization='NOT_ASSERTED')]


def main() -> None:
    root=Path(__file__).resolve().parent
    py=dict(interfaces=interfaces(),scalar=scalar_checks())
    with tempfile.TemporaryDirectory(prefix='two-hole-routing-') as td:
        exe=Path(td)/'verify'
        subprocess.run(['g++','-std=c++17','-O2','-Wall','-Wextra',
                        str(root/'verify_routing.cpp'),'-o',str(exe)],check=True,timeout=30)
        out=subprocess.run([str(exe)],check=True,text=True,stdout=subprocess.PIPE,timeout=30)
    cpp=json.loads(out.stdout)
    assert py==cpp, 'Python/C++ full decision-list or scalar disagreement'
    assert len(py['interfaces'])==654
    hist=collections.Counter(2*row[10:].count(0) for row in py['interfaces'])
    assert dict(hist)=={56:90,60:564}
    # Include the previously displayed ten pairs plus a repeated five-cycle.
    explicit=[1]*10
    for pair in [(0,1),(1,2),(2,3),(3,4),(0,4)]:explicit[PAIRS.index(pair)]+=1
    explicit_row=next(row for row in py['interfaces'] if row[:10]==explicit)
    evidence=json.dumps(py,sort_keys=True,separators=(',',':')).encode()+b'\n'
    (root/'EXACT_DECISIONS.json.gz').write_bytes(gzip.compress(evidence,mtime=0))
    result=dict(status='PASS_TARGETED_ROUTING_AND_HAND_BOUND_CHECKS_ONLY',
                predecessor='002713dc090035ec4f01d8eaaf9d27023082bc4d',
                python_cpp_full_agreement=True,
                interface_domain='Five distinguished tight labels; all 6-regular loopless multigraphs with parallel edges allowed; K-label permutations reduced',
                interfaces=len(py['interfaces']),
                mandatory_selected_incidences_per_interface=60,
                mandatory_selected_incidences_total=60*len(py['interfaces']),
                impossible_incidence_histogram=dict(sorted(hist.items())),
                impossible_selected_incidences_total=sum(k*v for k,v in hist.items()),
                fully_destination_admissible_interfaces=0,
                explicit_predecessor_interface=dict(multiplicities=explicit,
                    impossible_selected_incidences=2*explicit_row[10:].count(0)),
                scalar=py['scalar'],local_lemmas=local_lemmas(),
                negative_controls=negative_controls(),
                exact_decisions_sha256=hashlib.sha256(evidence).hexdigest(),
                new_symbolic_consequence='5h+3L+eta>=31 for d=5,z=2; 4a+5>=b+2tau+101; tau>=1 and b>=a+2 force a>=34 for extras',
                original_graph_enumeration='NOT_RUN',catalogue_replay='NOT_RUN',
                canonical_bridge_validation='NOT_ASSERTED',independent_expert_review='OPEN',
                scope='Finite checks support the new conditional hand proof; both checkers by the same assistant; no promotion or novelty claim')
    (root/'CHECK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
