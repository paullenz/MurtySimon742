#!/usr/bin/env python3
"""Separate direct integer enumeration of the local inequalities and maxima.

Finite regression; the unbounded parameter statements require the hand proof.
"""
from pathlib import Path
import json
from bounds import capped,uniform_cap

HERE=Path(__file__).resolve().parent


def direct(h,T,H,p):
    f=sum(H+p<=j for j in range(h,T))
    return h*(H+p)-h*H*(H>h)+H*f


def main():
    options=0;caps=0;labels=0;uniform=0
    for h in range(1,13):
        for T in range(h,6*h+1):
            for P in range(5*h+1):
                running=0
                for H in range(T+2):
                    running=max(running,max(direct(h,T,H,p) for p in range(P+1)))
                    options+=P+1
                    assert running==capped(h,T,P,H),(h,T,P,H,running,capped(h,T,P,H))
                    caps+=1
                # Beyond H=T, the ramp vanishes and the cost is h*p.
                assert running==uniform_cap(h,T,P),(h,T,P,running,uniform_cap(h,T,P))
                uniform+=1
            for s in range(h,2*T+2):
                for R in range(T+2):
                    for x in (s,s+1,s+T):
                        f=sum(R+x<=j for j in range(h,T))
                        assert h*(R+x)+x*f>=h*max(T,s)
                        labels+=1
    failed=[]
    for h in range(1,13):
        # T=4h+1 fails a naive C=hT assertion even with p=0.
        T=4*h+1;H=2*h;value=direct(h,T,H,0)
        assert value>h*T
        failed.append(dict(attempt='extend cutoff beyond 4h with C=hT',h=h,T=T,H=H,p=0,cost=value,claimed_cap=h*T))
        # P=3h+1 fails the zero-penalty theorem at H=h.
        T=4*h;P=3*h+1;value=direct(h,T,h,P)
        assert value>h*T
        failed.append(dict(attempt='omit incoming penalty beyond p=3h',h=h,T=T,H=h,p=P,cost=value,claimed_cap=h*T))
    assert direct(2,6,2,5)==14>12
    report=dict(status='PASS',ranges=dict(h=[1,12],T='h..6h',P='0..5h',H='0..T+1'),
        direct_source_options=options,exact_capped_maxima=caps,exact_uniform_maxima=uniform,label_checks=labels,
        failed_extensions=failed,old_N34_p5_counterexample=dict(h=2,T=6,H=2,p=5,cost=14,claimed_cap=12),
        scope='Local-domain counterexamples are not graphs or counterexamples to Murty-Simon.',external_review='OPEN')
    (HERE/'local_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='failed_extensions'},indent=2))


if __name__=='__main__':main()
