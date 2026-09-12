#!/usr/bin/env python3
"""Preserve concrete failures of two tempting local-maximization shortcuts."""
from itertools import product
from pathlib import Path
import json
from check_local import enumerate_maxima
HERE=Path(__file__).resolve().parent

def options(case,e):
    a,b,h,k,j,rho,hi,lo=case;out=[]
    for H,q,p in product(range(a+1),range(a+1),range(b)):
        if H>hi or H>q or q-H>lo or q+rho>a or q+p>=b or p>rho+b-a-1 or int(H>h)!=e or e>j:continue
        f=sum(q+p<=cut for cut in range(h,4*h))
        m=min(p,j-e) if rho>=h else 0
        value=H*(h+f)+H-2*(e*H-m)-4*((q if q>k else 0)-(p if rho+q>=k else 0))
        out.append((value,H,q,p))
    return out

def main():
    jump=(15,18,4,2,5,1,0,1);rows=options(jump,0)
    correct=max(r[0] for r in rows);shortcut=max(v for v,H,q,p in rows if q==H)
    assert (correct,shortcut)==(12,0)
    vertex=(15,18,4,2,5,4,10,2);rows=options(vertex,1);Hs={r[1] for r in rows};ends={min(Hs),max(Hs)}
    correct2=max(r[0] for r in rows);shortcut2=max(v for v,H,q,p in rows if H in ends)
    assert (correct2,shortcut2)==(56,54)
    report=dict(status='PASS',scope='Abstract local source domains, not asserted diameter-two critical graphs',
        examples=[dict(invalid_shortcut='Always replace q by H across the destination-eligibility jump',parameters=jump,sender_class=0,true_maximum=correct,shortcut_maximum=shortcut),
                  dict(invalid_shortcut='Check only the endpoints of the H interval',parameters=vertex,sender_class=1,H_endpoints=sorted(ends),true_maximum=correct2,shortcut_maximum=shortcut2)],external_review='OPEN')
    (HERE/'shortcut_counterexamples.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
