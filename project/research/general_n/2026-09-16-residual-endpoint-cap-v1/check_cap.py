#!/usr/bin/env python3
"""Targeted arithmetic and row-relaxation checks; NOT original-graph enumeration.

Run beside verify_cap.cpp with Python 3 and a C++17 compiler. Both enumerators
are by the same assistant. The symbolic endpoint-cap proof is separate.
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


def pool_vectors(total: int):
    for u in itertools.combinations_with_replacement(range(total + 1), 5):
        if sum(u) == total:
            yield u


def python_rows() -> list[list[int]]:
    rows = []
    # The exhibited value 34 implies h>=7 cannot minimize (5h>=35).
    for h in range(7):
        kappa = 9 + h
        for L in range(5*h//4 + 1):
            for u in pool_vectors(L):
                capacities = [h-L+x for x in u]
                if min(capacities) < 0:
                    continue
                prices = [max(1, 2-x) for x in u]
                slots = sorted(p for p,c in zip(prices, capacities) for _ in range(c))
                prefix = [0] + list(itertools.accumulate(slots))
                weight = math.factorial(5)
                for v in collections.Counter(u).values():
                    weight //= math.factorial(v)
                for n0 in range(kappa+1):
                    for n1 in range(kappa-n0+1):
                        n2 = kappa-n0-n1
                        if n1 + 2*n2 > 5*h-4*L or n1 > len(slots):
                            continue
                        eta = 4*n0+n2+prefix[n1]
                        omega = 5*h+3*L+eta
                        assert eta >= kappa
                        assert omega >= 36-h+(11-h)*L
                        assert omega >= 27+3*h+(7-h)*L
                        assert omega >= 9+6*h+3*L
                        assert omega >= 34
                        rows.append([h,L,*u,n0,n1,n2,omega,weight])
    return sorted(rows)


def cap_checks() -> dict:
    cases = 0
    by_d = []
    for d in range(2,17):
        count = 0
        for source in range(d):
            for destination in range(d):
                for delta in range(source+destination+1):
                    for residual in range(d,2*d+3):
                        s = max(0, delta-residual)
                        assert s <= d-2
                        assert delta <= 2*d-2
                        count += 1
        cases += count
        by_d.append(dict(d=d,cases=count))
    return dict(cases=cases,by_d=by_d,
                scope='Selected-label necessary scalar arrays only, not graph realizations')


def injection_masks() -> dict:
    total = 0
    for n in range(1,7):
        for source in range(1<<n):
            for dest in range(1<<n):
                union = source|dest
                D = union
                while True:
                    # Neighbours not charged residually at the source must be
                    # residual at the destination; overlaps are allowed.
                    assert (D & ~source) & ~dest == 0
                    assert D.bit_count() <= source.bit_count()+dest.bit_count()
                    total += 1
                    if D == 0:
                        break
                    D = (D-1)&union
    assert total == sum(7**n for n in range(1,7))
    return dict(cases=total,scope='Local residual-incidence masks; canonical forcing is proved symbolically')


def hand_envelope() -> dict:
    cases = 0
    minimizers = []
    for h in range(51):
        for L in range(5*h//4+1):
            lo = max(36-h+(11-h)*L,27+3*h+(7-h)*L,9+6*h+3*L)
            assert lo >= 34
            if lo == 34:
                minimizers.append([h,L,lo-5*h-3*L])
            cases += 1
    assert minimizers == [[2,0,24]]
    # Local endpoint table for a completely residual set of r sources, with
    # every other endpoint bounded by c: s<=max(0,2c-r).
    generalized = 0
    for c in range(9):
        for r in range(1,13):
            for delta in range(2*c+1):
                for R in range(r,r+6):
                    assert max(0,delta-R) <= max(0,2*c-r)
                    generalized += 1
    return dict(envelope_cases=cases,minimizers=minimizers,
                generalized_endpoint_arrays=generalized,
                scope='Finite support only; hand proof has no finite h cutoff')


def controls() -> list[dict]:
    # None of these scalar/local controls is asserted to be a canonical graph.
    assert max(0,8-4) == 4 > 3
    assert 9 <= 4+5 and max(0,9-5) == 4 > 3
    assert max(0,9-9) == 0 and 9 > 2*5-2
    assert 6 < 9+5 and 1 < 9+6
    return [
        dict(kind='residual_at_all_high_sources_cannot_be_dropped',d=5,
             source=4,destination=4,delta=8,R=4,s=4,canonical_realization=False),
        dict(kind='both_endpoints_must_be_low',d=5,source=4,destination=5,
             delta=9,R=5,s=4,canonical_realization=False),
        dict(kind='degree_cap_requires_a_selected_incidence',d=5,delta=9,R=9,
             x=0,s=0,degree_cap_applies=False,canonical_realization=False),
        dict(kind='old_interface_not_a_canonical_system',d=5,h=6,L=0,eta=0,
             kappa=15,violates_new_eta_floor=True,old_row_minimum_still=30),
        dict(kind='Omega31_branches',branches=[dict(h=5,eta=6,required_eta=14),
                                              dict(h=6,eta=1,required_eta=15)],
             branches_rejected=2),
        dict(kind='relaxed_Omega34_is_not_a_realizability_claim',h=2,L=0,
             n0=1,n1=10,n2=0,omega=34,canonical_realization='NOT_ASSERTED')]


def main() -> None:
    root = Path(__file__).resolve().parent
    rows = python_rows()
    with tempfile.TemporaryDirectory(prefix='endpoint-cap-') as tmp:
        exe = Path(tmp)/'verify_cap'
        subprocess.run(['g++','-std=c++17','-O2','-Wall','-Wextra',
                        str(root/'verify_cap.cpp'),'-o',str(exe)],check=True,timeout=30)
        run = subprocess.run([str(exe)],check=True,text=True,stdout=subprocess.PIPE,timeout=30)
    independent = json.loads(run.stdout)
    assert rows == independent, 'Python/C++ complete symmetry-reduced outer cost tables differ'
    data = (json.dumps(rows,separators=(',',':'))+'\n').encode()
    (root/'EXACT_ROW_COSTS.json.gz').write_bytes(gzip.compress(data,mtime=0))
    minimum = min(r[-2] for r in rows)
    minima = [r for r in rows if r[-2] == minimum]
    h_slices = [min(r[-2] for r in rows if r[0] == h) for h in range(7)]
    assert minimum == 34
    assert [r[:10] for r in minima] == [[2,0,0,0,0,0,0,1,10,0]]
    result = dict(status='PASS_TARGETED_ENDPOINT_CAP_AND_ROW_CHECKS_ONLY',
                  python_cpp_complete_outer_cost_table_agreement=True,
                  row_relaxation=dict(d=5,z=2,minimum=minimum,
                      minima_by_h=h_slices,minimizing_rows=minima,
                      symmetry_reduced_outer_rows=len(rows),
                      ordered_outer_tuples=sum(r[-1] for r in rows),
                      count_is_not_all_one_hole_allocations=True,
                      exact_rows_sha256=hashlib.sha256(data).hexdigest(),
                      row_fields=['h','L','u0','u1','u2','u3','u4','n0','n1','n2','cost','ordered_multiplicity']),
                  endpoint_arrays=cap_checks(),injection_masks=injection_masks(),
                  hand_envelope=hand_envelope(),negative_controls=controls(),
                  symbolic_consequence='s_k<=d-2 for every k in K; d=5,E>0 implies Omega>=34 and 4a+5>=b+2tau+104',
                  integer_tau_one_minimum_a_for_extras=35,
                  original_graph_enumeration='NOT_RUN',catalogue_replay='NOT_RUN',
                  independent_expert_review='OPEN',canonical_bridge_validation='NOT_ASSERTED',
                  independence='Different algorithms by the same assistant; not independent expert acceptance')
    (root/'CHECK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
