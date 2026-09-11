#!/usr/bin/env python3
"""Exact audit of the hand D1=0 support reduction for the n=29,t=3 A1 regime.

This is a falsification checker, not a replacement for the written hand proof.
It enumerates the small post-one-label domain and verifies that every state
satisfying the stated necessary conditions either violates total/prefix Hall
or belongs to the hand-derived stable support class.
"""
from itertools import combinations_with_replacement
from collections import Counter

A=12; B=16; T=3

def h_res(rho):
    h=0
    for k,x in enumerate(sorted(rho,reverse=True),1):
        if x>=k: h=k
        else: break
    return h

def scalar_cutoff(s,rho):
    C=[min(A-r,sum(x<=r for x in s)) for r in rho]
    K=max(C,default=0)
    scores=[r+c for r,c in zip(rho,C)]
    good=[k for k in range(1,K+1) if sum(z>=k-1 for z in scores)>=k+1]
    L=max(good) if good else 0
    return L,[min(c,L) for c in C]

def first_hall_failure(s,rho,cap):
    if sum(cap)<sum(s): return ('total',0,sum(s),sum(cap))
    ss=sorted(s)
    for k in range(1,A+1):
        P=ss[A-k:]
        need=sum(P)
        supply=sum(min(cap[u],sum(x<=rho[u] for x in P)) for u in range(B))
        if supply<need: return ('prefix',k,need,supply)
    return None

def main():
    broad=0
    l_not_6=0
    high_ge7_total_pass=0
    rho2_total_pass=0
    rho2_prefix7_fail=0
    stable=0
    stable_bad_support=0
    survivors=[]

    # D1=0 and one-label Hall+h=4 already imply s in {2,3,4}.
    for s in combinations_with_replacement((2,3,4),A):
        D=Counter(s)
        # J=14 with D1=0 gives z2=7, hence nine residual ones.
        r=sum(s)-2*T
        nonunit_total=r-9
        for vals in combinations_with_replacement(range(2,A+1),7):
            if sum(vals)!=nonunit_total: continue
            rho=(1,)*9+vals
            if h_res(rho)!=4: continue
            broad+=1
            L,cap=scalar_cutoff(s,rho)
            fail=first_hall_failure(s,rho,cap)

            # Written proof says any state capable of passing total capacity has L=6.
            if sum(cap)>=sum(s) and L!=6:
                l_not_6+=1
                raise AssertionError(('total-pass with L!=6',s,rho,L,sum(cap),sum(s)))

            # Any rho>=7 should fail total capacity already.
            if max(rho)>=7 and sum(cap)>=sum(s):
                high_ge7_total_pass+=1
                raise AssertionError(('rho>=7 passes total',s,rho,L,sum(cap),sum(s)))

            if 2 in rho and sum(cap)>=sum(s):
                rho2_total_pass+=1
                # The hand proof reduces these to D2=3,4,5 and kills them by k=7 Hall.
                P=sorted(s)[-7:]
                need=sum(P)
                supply=sum(min(cap[u],sum(x<=rho[u] for x in P)) for u in range(B))
                if supply>=need:
                    raise AssertionError(('rho2 escapes largest7 Hall',s,rho,L,need,supply))
                rho2_prefix7_fail+=1

            if fail is None:
                stable+=1
                rc=Counter(rho)
                if set(rc)-{1,3,4,5,6} or L!=6 or rc[1]!=9:
                    stable_bad_support+=1
                    raise AssertionError(('survivor outside stable support',s,rho,L))
                survivors.append((tuple(sorted(Counter(s).items())),tuple(sorted(rc.items()))))

    assert l_not_6==0
    assert high_ge7_total_pass==0
    assert rho2_total_pass==rho2_prefix7_fail
    assert stable==11, stable
    assert stable_bad_support==0
    assert len(set(survivors))==11
    print({
        'status':'PASS',
        'broad_post_one_label_states':broad,
        'rho2_total_capacity_passers':rho2_total_pass,
        'rho2_largest7_hall_failures':rho2_prefix7_fail,
        'stable_support_survivors':stable,
        'all_stable_support_rho_subset':[1,3,4,5,6],
        'stable_scalar_cutoff':6,
    })

if __name__=='__main__':
    main()
