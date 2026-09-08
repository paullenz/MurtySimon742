#!/usr/bin/env python3
"""Standard-library arithmetic checks for the n=30 candidate assembly.

This script deliberately excludes the Delta=16/17 finite kernels, which have
separate exact replay workflows.  It checks the published-bound arithmetic,
degree-sum reductions, and exact emptiness of the charging demand domain for
Delta=18,...,28 at m=225 and 226.
"""
from fractions import Fraction
import json

N=30
TARGET=N*N//4


def demand_count(a,b,t):
    """Count complete sorted integer demand profiles satisfying charging."""
    need=Fraction(b+2*t)
    vals=[Fraction(s*(a+1-2*s),a-s) for s in range(a)]
    tail=[max(vals[i:]) for i in range(a)] if a else []
    count=0
    def rec(left,lo,score):
        nonlocal count
        if left==0:
            if score>=need:
                count+=1
            return
        if score+left*tail[lo] < need:
            return
        for s in range(lo,a):
            if score+vals[s]+(left-1)*tail[s] < need:
                continue
            rec(left-1,s,score+vals[s])
    if a==0:
        return int(Fraction(0)>=need)
    rec(a,0,Fraction())
    return count


def main():
    # Fan strict bound as used in the project:
    # m < n^2/4 + [n^2-(81/5)n+56]/320.
    fan = Fraction(N*N,4) + Fraction(N*N-Fraction(81,5)*N+56,320)
    assert fan == Fraction(7247,32)
    assert 226 < fan < 227

    # Degree-sum reductions.
    assert Fraction(N*15,2) == 225
    assert Fraction(N*14,2) == 210

    rows=[]
    for m in (225,226):
        for delta in range(18,29):
            a=N-1-delta
            b=delta
            t=m-b*(N-b)
            c=demand_count(a,b,t)
            assert c==0
            rows.append({"m":m,"Delta":delta,"a":a,"b":b,"t":t,"charging_profiles":c})

    report={
        "schema":"n30-outer-arithmetic-v1",
        "status":"PASS",
        "n":N,
        "target":TARGET,
        "fan_bound":{"numerator":fan.numerator,"denominator":fan.denominator},
        "degree_sum":{"max_edges_Delta15":225,"max_edges_Delta14":210},
        "charging_empty_scopes":rows,
        "all_Delta18_to_28_empty_at_225_226":True,
    }
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
