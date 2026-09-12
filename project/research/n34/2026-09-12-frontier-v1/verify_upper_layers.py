#!/usr/bin/env python3
"""Solver-free verification of every local envelope and full state coverage.

Does not import the LP/model builder. Uses only standard-library integer sums.
"""
import json
from collections import Counter
from pathlib import Path
from check_frontier import expand

HERE=Path(__file__).resolve().parent
A,B,DMAX=15,18,13


def potential(d,h):
    return (4*(d>=2)+2*(d>=2 and h<=11)+(d>=2 and h<=9)
            +(d>=2 and h<=7)+(d>=2 and h<=4)+(d>=2 and h<=3)
            +(d>=3 and h<=8)+(d>=3 and h<=6)+(d>=3 and h<=5))


def main():
    data=json.loads((HERE/'upper_layer_certificates.json').read_text())
    assert (data['a'],data['b'],data['dmax'])==(A,B,DMAX)
    report={}
    for t in (3,4):
        layer=data['layers'][str(t)]
        expected,_=expand(t)
        covered=set()
        local_checks=0
        gaps=[]
        for cert in layer['certificates']:
            s,rho=tuple(cert['s']),tuple(cert['rho'])
            assert (s,rho) not in covered
            covered.add((s,rho))
            assert len(s)==A and len(rho)==B and min(s)>0
            assert all(isinstance(x,int) for x in cert['numerators'])
            den=cert['denominator'];assert isinstance(den,int) and den>0
            names=[tuple(n) if isinstance(n,list) else n for n in cert['names']]
            assert len(names)==len(set(names))==len(cert['numerators'])
            X=dict(zip(names,cert['numerators']))
            lam,c=X['lambda'],X['c']
            mu=X['mu+']-X['mu-']
            assert min(lam,c,X['mu+'],X['mu-'])>=0
            assert all(X['tau',j]>=0 for j in range(1,A+1))
            for demand in set(s):
                for R in range(DMAX-demand+1):
                    for x in range(demand,B-R+1):
                        assert X['ell',demand]<=lam*R+c*x+den*x*potential(R+demand,R+x)
                        local_checks+=1
            for residual in set(rho):
                qmax=min(A-residual,sum(demand<=residual for demand in s))
                for q in range(qmax+1):
                    for p in range(min(residual+B-A-1,B-1-q)+1):
                        transport=sum(X['tau',j]*((q if q>=j+1 else 0)
                                      -(p if residual+q>=j else 0)) for j in range(1,A+1))
                        assert X['sig',residual]<=mu*(q-p)-c*q+transport-den*q*potential(residual+q-1,q+p)
                        local_checks+=1
            gap=lam*sum(rho)-sum(n*X['ell',d] for d,n in Counter(s).items())-sum(n*X['sig',r] for r,n in Counter(rho).items())
            assert gap==cert['gap'] and gap<0
            gaps.append(gap)
        unresolved={(tuple(x['s']),tuple(x['rho'])) for x in layer['unresolved']}
        assert not covered & unresolved
        assert covered | unresolved == set(expected)
        hand=[]
        for s,rho in sorted(unresolved):
            S=sum(s)
            assert S>=sum(rho)+2*t
            # Tight total-demand threshold lemma, proved in the sibling
            # general_n/2026-09-12-joint-clipping-v1 review package.
            possible=[]
            for h in range(2,min(s)+1):
                z=sum(r>=h for r in rho)
                if z>=h and 2*S==z*(z-1)+h*(h+1) and B+2*t>h*(h+1):
                    possible.append(dict(h=h,z=z,S=S,r=sum(rho),
                                         incoming_lower=S-h*(h+1),
                                         incoming_upper=sum(rho)-B))
            assert possible, (s,rho)
            hand.append(dict(s=s,rho=rho,contradiction=possible[0]))
        assert len(covered)+len(hand)==len(expected)
        report[str(t)]=dict(expected_states=len(expected),exact_exclusions=len(covered),
                            hand_exclusions=len(hand),unresolved=0,hand=hand,
                            local_integer_checks=local_checks,
                            worst_gap=max(gaps) if gaps else None)
        print('t',t,report[str(t)],flush=True)
    (HERE/'upper_layer_verification.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
