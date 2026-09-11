#!/usr/bin/env python3
"""Exact audit of the hand D1=2 elimination in the n=29,t=3 A1 regime.

Uses only Python standard library and integer arithmetic.  Two layers:
1. verify the symbolic case bounds in N29_T3_A1_D1_2_HAND_ELIMINATION.md;
2. independently enumerate the tiny post-one-label residual histogram space and
   confirm that the largest-eight Hall inequality rejects every state under the
   exact scalar-cutoff definition.

This is an audit of the hand lemma, not a graph-realisability search.
"""
from itertools import combinations_with_replacement
import json
from pathlib import Path

A=12; B=16
HERE=Path(__file__).resolve().parent

def h_res(rho):
    h=0
    for k,x in enumerate(sorted(rho,reverse=True),1):
        if x>=k:h=k
        else:break
    return h

def cutoff(s,rho):
    C=[min(A-r,sum(x<=r for x in s)) for r in rho]
    K=max(C)
    score=[r+c for r,c in zip(rho,C)]
    good=[k for k in range(1,K+1) if sum(z>=k-1 for z in score)>=k+1]
    L=max(good) if good else 0
    return L,[min(c,L) for c in C]

def top8(s):
    return sorted(s)[-8:]

def hall_supply(P,rho,cap):
    return sum(min(cap[u],sum(x<=rho[u] for x in P)) for u in range(B))

def symbolic_pairs():
    return [(d2,d3,10-d2-d3) for d2 in range(3) for d3 in range(5)
            if 2*d2+d3<=4]

def largest8_need(d2,d3,d4):
    s=[1,1]+[2]*d2+[3]*d3+[4]*d4
    return sum(top8(s))

def max_linear_supply(C,k,L):
    # maximize kY+LM subject to Y,M>=0 integers and Y+2M<=C.
    return max(k*y+L*m for y in range(C+1) for m in range(C//2+1)
               if y+2*m<=C)

def check_symbolic_bounds():
    pairs=symbolic_pairs()
    assert pairs==[(0,0,10),(0,1,9),(0,2,8),(0,3,7),(0,4,6),
                   (1,0,9),(1,1,8),(1,2,7),(2,0,8)]
    rows=[]
    for d2,d3,d4 in pairs:
        C=12-2*d2-d3
        need=largest8_need(d2,d3,d4)
        k=max(0,8-d4)  # number of demand-3 labels in top eight; <=2 here
        assert 0<=k<=2 and need>=30

        # L<=5: 2Q <=5C.
        q5=(5*C)//2
        assert q5<need

        # L=6: generic bound, except (0,0), whose gate argument lowers M to <=5.
        if (d2,d3)==(0,0):
            q6=30
        else:
            q6=max_linear_supply(C,k,6)
        assert q6<need,(d2,d3,d4,C,k,q6,need)

        rows.append({'D2':d2,'D3':d3,'D4':d4,'budget_C':C,
                     'top8_demand3':k,'top8_need':need,
                     'L_le_5_bound':q5,'L_6_bound':q6})

    # L=7 hand gate: the only surviving demand histogram can be (2,0,8),
    # and then N=24 plus h=4 forces exactly four rho>=4 sources.
    d2,d3,d4=2,0,8
    assert 2*d2+d3==4
    assert largest8_need(d2,d3,d4)==32
    assert 4*7<32
    return rows

def enumerate_post_one_label():
    total=0; byL={}; worst_gap=999; witness=None
    for d2,d3,d4 in symbolic_pairs():
        s=(1,1)+(2,)*d2+(3,)*d3+(4,)*d4
        r=36-2*d2-d3
        nonunit_sum=r-8
        for vals in combinations_with_replacement(range(2,A+1),8):
            if sum(vals)!=nonunit_sum:continue
            rho=(1,)*8+vals
            if h_res(rho)!=4:continue
            total+=1
            L,cap=cutoff(s,rho)
            P=top8(s);need=sum(P);supply=hall_supply(P,rho,cap)
            byL[L]=byL.get(L,0)+1
            gap=need-supply
            if gap<worst_gap:
                worst_gap=gap;witness=(d2,d3,d4,list(vals),L,need,supply)
            assert L<=7
            assert supply<need,(d2,d3,d4,vals,L,need,supply)
    assert total==43,total
    return {'states':total,'cutoff_census':dict(sorted(byL.items())),
            'minimum_Hall_deficit':worst_gap,'minimum_gap_witness':witness}

def main():
    report={'schema':'n29-t3-a1-d1-2-hand-check-v1','status':'PASS',
            'symbolic_case_rows':check_symbolic_bounds(),
            'post_one_label_exact_audit':enumerate_post_one_label(),
            'solver_used':False,'floating_point_used':False,
            'interpretation':'The previously unresolved D1=2 A1 branch is eliminated by the hand L<=5/L=6/L=7 argument; the tiny 43-state post-one-label enumeration is retained only as an independent exact audit of that derivation.'}
    out=HERE/'N29_T3_A1_D1_2_HAND_CHECK.json'
    out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(report,indent=2,sort_keys=True))
if __name__=='__main__':main()
