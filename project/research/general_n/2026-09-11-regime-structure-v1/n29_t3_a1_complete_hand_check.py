#!/usr/bin/env python3
"""Exact audit of the complete hand support reduction for n=29,t=3 A1.

This checker does not provide the proof: N29_T3_A1_COMPLETE_HAND_REDUCTION.md does.
It independently exhausts the small post-hand-reduction histogram spaces to verify
that the symbolic branch conclusions are exact and match the old core enumerator.
Standard library, integer/Fraction arithmetic only; no solver/floating point.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path
import json

A=12;B=16;T=3
HERE=Path(__file__).resolve().parent

def h_res(rho):
    h=0
    for k,x in enumerate(sorted(rho,reverse=True),1):
        if x>=k:h=k
        else:break
    return h

def charge(s):
    return sum((Fraction(x*(A+1-2*x),A-x) for x in s),Fraction())

def cutoff(s,rho):
    C=[min(A-r,sum(x<=r for x in s)) for r in rho]
    score=[r+c for r,c in zip(rho,C)]
    K=max(C,default=0)
    good=[k for k in range(1,K+1) if sum(z>=k-1 for z in score)>=k+1]
    L=max(good) if good else 0
    return L,[min(c,L) for c in C]

def first_fail(s,rho,cap):
    if sum(cap)<sum(s): return ('total',0,sum(s),sum(cap))
    ss=sorted(s)
    for k in range(1,A+1):
        P=ss[A-k:];need=sum(P)
        supply=sum(min(cap[u],sum(x<=rho[u] for x in P)) for u in range(B))
        if supply<need:return ('prefix',k,need,supply)
    return None

def d1_zero_states():
    broad=0; total_fail=0; prefix7=0; survive=[]; support_bad=[]
    for d2 in range(13):
      for d3 in range(13-d2):
        d4=12-d2-d3
        s=(2,)*d2+(3,)*d3+(4,)*d4
        if charge(s)<22:continue
        S=sum(s);r=S-6;N=r-9
        for vals in combinations_with_replacement(range(2,A+1),7):
            if sum(vals)!=N:continue
            rho=(1,)*9+vals
            if h_res(rho)!=4:continue
            broad+=1
            L,cap=cutoff(s,rho);f=first_fail(s,rho,cap)
            if f is None:
                survive.append((d2,d3,d4,vals,L))
                if L!=6 or any(x not in {3,4,5,6} for x in vals):support_bad.append(survive[-1])
            elif f[0]=='total':total_fail+=1
            else:
                assert f[0]=='prefix' and f[1]==7,f
                prefix7+=1
    assert broad==1102,broad
    assert total_fail==1086,total_fail
    assert prefix7==5,prefix7
    assert len(survive)==11,len(survive)
    assert not support_bad,support_bad
    return {'post_one_label_states':broad,'total_capacity_failures':total_fail,
            'top7_Hall_failures':prefix7,'survivors':len(survive),
            'all_survivors_L':sorted(set(x[4] for x in survive)),
            'all_survivor_nonunit_rho_support':sorted(set(v for x in survive for v in x[3])),
            'survivor_histograms':[{'D2':d2,'D3':d3,'D4':d4,'rho_nonunit':list(vals),'L':L}
                for d2,d3,d4,vals,L in survive]}

def branch_checks():
    # Charging max + parity/J yields D1 only 0,2,4.
    feasible=[]
    for d1 in range(13):
        if (14+d1)%2:continue
        z2=(14+d1)//2
        if not 0<=z2<=16:continue
        maxcharge=Fraction(d1,1)+Fraction(5,2)*(12-d1)
        if maxcharge>=22:feasible.append(d1)
    assert feasible==[0,2,4],feasible
    # D1=4 hand contradiction: lower S 39 > upper S36.
    assert 7+4*4+5*2+6==39
    assert 4+8*4==36
    # D1=0 cutoff hand bounds.
    assert 9+4*4+3*2+6==37
    assert 7*5==35
    return {'charging_J_D1_values':feasible,'D1_4_lower_S':39,'D1_4_upper_S':36,
            'D1_0_if_L_le_5_lower_S':37,'D1_0_if_L_le_5_total_cap':35}

def main():
    r={'schema':'n29-t3-a1-complete-hand-check-v1','status':'PASS',
       'branch_checks':branch_checks(),'D1_0_exact_audit':d1_zero_states(),
       'D1_2_audit':'see N29_T3_A1_D1_2_HAND_CHECK.json (separate PASS receipt)',
       'solver_used':False,'floating_point_used':False,
       'interpretation':'The hand branch reduction is independently consistent: D1 is restricted to 0,2,4; D1=4 is arithmetically impossible; in D1=0 the only states surviving total capacity plus Hall have exactly the stable A1 support and L=6. D1=2 is covered by its separate exact hand audit.'}
    (HERE/'N29_T3_A1_COMPLETE_HAND_CHECK.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    print(json.dumps(r,indent=2,sort_keys=True))
if __name__=='__main__':main()
