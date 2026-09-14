#!/usr/bin/env python3
"""Exact finite verifier for row 471, eta=2, e_L=41 high-block closure.

This checks only the stated selected-incidence/common-pressure relaxation. It is
integer enumeration, not a graph-realizability or unrestricted-conjecture claim.
"""
from itertools import product
import json

HIGH_SOURCES=[5,9,10,11,12,13,16,19,23]
Q=[6,2,6,7,7,4,5,5,3]
CAP=[2,4,2,1,1,4,3,3,4]
HIGH_EXCESS=6
LOW_SLOTS=3
TOTAL_PRESSURE_REQUIRED=74
LOW_SOURCE_PRESSURE_CAPACITY=64
HIGH_PRESSURE_REQUIRED=TOTAL_PRESSURE_REQUIRED-LOW_SOURCE_PRESSURE_CAPACITY


def gamma(q,d):
    return 0 if d==0 else max(0,q-HIGH_EXCESS//d)


def allocations():
    out=[]
    def rec(i,remaining,cur):
        if i==len(Q):
            if remaining==0:out.append(tuple(cur))
            return
        for k in range(min(Q[i],remaining)+1):
            cur.append(k);rec(i+1,remaining-k,cur);cur.pop()
    rec(0,LOW_SLOTS,[])
    return out


def nested_excess(high_counts,pressures):
    return sum(max([d for h,d in zip(high_counts,pressures) if h>=j]+[0])
               for j in range(1,max(high_counts,default=0)+1))


def main():
    low_allocations=allocations()
    assert len(low_allocations)==164
    pressure_vectors=gamma_survivors=pair_survivors=0
    surviving_vectors=set();minimum_active_high=10**9;examples=[]
    for pressures in product(*[range(c+1) for c in CAP]):
        if sum(pressures)<HIGH_PRESSURE_REQUIRED:continue
        pressure_vectors+=1
        required=tuple(gamma(q,d) for q,d in zip(Q,pressures))
        if sum(required)>LOW_SLOTS:continue
        gamma_survivors+=1
        for low in low_allocations:
            if any(k<r for k,r in zip(low,required)):continue
            high=[q-k for q,k in zip(Q,low)]
            if nested_excess(high,pressures)>HIGH_EXCESS:continue
            pair_survivors+=1;surviving_vectors.add(pressures)
            active=sum(h for h,d in zip(high,pressures) if d>0)
            if active<minimum_active_high:
                minimum_active_high=active;examples=[dict(pressure=list(pressures),low=list(low),high=high)]
            elif active==minimum_active_high and len(examples)<8:
                examples.append(dict(pressure=list(pressures),low=list(low),high=high))
    max_positive_high_capacity=3*HIGH_EXCESS+HIGH_EXCESS
    assert pressure_vectors==55992
    assert gamma_survivors==1311
    assert pair_survivors==25
    assert len(surviving_vectors)==18
    assert minimum_active_high==28
    assert max_positive_high_capacity==24
    assert minimum_active_high>max_positive_high_capacity
    out=dict(schema='row471-e41-highblock-v1',row=471,eta=2,e_low=41,
             high_sources=HIGH_SOURCES,high_excess=HIGH_EXCESS,low_slots=LOW_SLOTS,
             total_pressure_required=TOTAL_PRESSURE_REQUIRED,
             low_source_pressure_capacity=LOW_SOURCE_PRESSURE_CAPACITY,
             high_pressure_required=HIGH_PRESSURE_REQUIRED,
             low_slot_allocations=len(low_allocations),pressure_vectors=pressure_vectors,
             gamma_survivors=gamma_survivors,pair_survivors=pair_survivors,
             surviving_pressure_vectors=len(surviving_vectors),
             minimum_active_high_selections=minimum_active_high,
             maximum_positive_high_label_capacity=max_positive_high_capacity,
             contradiction='28>24',examples=examples,
             conclusion='conditioned branch eta=2,e_L=41 excluded in stated selected-incidence/common-pressure relaxation; row471 not fully excluded')
    print(json.dumps(out,sort_keys=True,indent=2))

if __name__=='__main__':main()
