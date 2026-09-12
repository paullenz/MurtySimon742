#!/usr/bin/env python3
"""Exhaustive finite checks of tail budgets and equality-rigidity arithmetic."""
from itertools import combinations_with_replacement
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent


def main():
    tail_checks=0;plateaus=0;forced=0
    for a in range(2,8):
        for b in range(1,7):
            for rho in combinations_with_replacement(range(1,a+1),b):
                actual=[sum(v>=h for v in rho) for h in range(a+2)]
                for kind in ('zero','half','exact'):
                    L=[0]*(a+2);L[1]=b
                    for h in range(2,a+1):L[h]=0 if kind=='zero' else actual[h]//2 if kind=='half' else actual[h]
                    for extra in range(3):
                        M=sum(rho)+extra;D=M-b-sum(L[2:]);d=max(i for i,v in enumerate(L) if v)
                        assert D>=0 and max(rho)<=min(a,d+D)
                        if D==0:
                            assert all(actual[h]==L[h] for h in range(1,a+1));forced+=1
                        for h in range(1,d+1):
                            z=actual[h];beta=sum(max(0,z-L[l]) for l in range(2,h+1))
                            E=sum(L[h+1:])+D-beta
                            assert beta<=D and sum(rv-h for rv in rho if rv>=h)<=E
                            assert all(rv<=min(a,d+D-beta) for rv in rho if rv>=h)
                            if h>=2:
                                m=1
                                while h-m>=2 and L[h-m]==L[h]:m+=1
                                assert z<=L[h]+D//m;plateaus+=1
                            tail_checks+=1
    local=0;extrema=0
    for h in range(1,13):
        for H in range(6*h+1):
            for p in range(3*h+1):
                cost=h*H+h*p+H*sum(H+p<=cutoff for cutoff in range(h,4*h))-h*H*int(H>h)
                assert cost<=4*h*h
                assert (cost==4*h*h)==(H==h or (H==2*h and p==0))
                local+=1;extrema+=cost==4*h*h
    routing=0
    for h in range(1,13):
        for P in range(3*h+1):
            for z in range(41):
                limit=max(0,min(z-2*h,P*z//(P+2*h)))
                for j in range(z+1):
                    if j and (z-j<2*h or 2*h*j>P*(z-j)):continue
                    assert j<=limit;routing+=1
    invalid=[
        dict(claim='Subtract all higher lower tails when bounding one residual degree',a=3,b=3,rho=[1,3,3],L=[3,2,2],h=2,E=2,
             wrong_Rmax=2,correct_Rmax=3,explanation='The distinguished source itself contributes to higher tails; other sources need only (L_l-1)_+.'),
        dict(claim='Charge (h-1)(z-L_h) for every tail increase',a=3,b=5,rho=[1,2,2,3,3],L=[5,4,1],M=11,D=1,h=3,z=2,
             wrong_charge=2,correct_charge=1,explanation='A lower tail already above z need not rise. The positive-part sum is necessary.'),
        dict(claim='Infer a positive number of 2h-senders from local maximality alone',h=2,z=2,H=[2,2],p=[0,0],heavy_sum=4,high_senders=0,
             explanation='This is only a local counterexample. Full nontrivial load equality implies G<=4W<=4h(z+j) and r>0, so j>=ceil(r/(4h))>=1. The first draft overstated the need for a separate j=0 exception; corrected before publication.'),
        dict(claim='Allow p>3h while retaining source cost <=4h^2',h=2,H=2,p=7,source_cost=18,claimed_upper=16,
             explanation='The incoming-degree hypothesis is essential; this is a local inequality counterexample, not a graph.')]
    report=dict(status='PASS',tail_checks=tail_checks,plateau_checks=plateaus,zero_slack_forced_tail_checks=forced,
                local_source_options=local,local_equality_options=extrema,routing_integer_checks=routing,
                domains=dict(tails='2<=a<=7, 1<=b<=6, all sorted positive residual tuples; zero/half/exact lower tails; M=r,r+1,r+2',
                             local='1<=h<=12, 0<=H<=6h, 0<=p<=3h',routing='1<=h<=12, 0<=P<=3h, 0<=z<=40, all admissible j'),
                invalid_extensions=invalid,scope='Finite corroboration of the hand proofs; abstract integer data are not claimed graph realizations.',external_review='OPEN')
    (HERE/'budget_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
