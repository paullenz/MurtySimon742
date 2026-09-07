#!/usr/bin/env python3
"""An infinite test-pattern family; not a family of actual graphs."""
import json
from pathlib import Path
from pair_engine import prepare,support_certificate,check_support,legacy_tests


def balanced_list(length,total):
    q,rem=divmod(total,length)
    return [q]*(length-rem)+[q+1]*rem


def profile(s):
    if type(s) is not int or s<2:raise ValueError('s>=2 is required')
    a=30*s;b=30*s+3;r=140*s*s+6*s
    return dict(name=f'family_s{s}',a=a,b=b,t=2,
        d=balanced_list(a,2*r+4),R=balanced_list(a,r),rho=[2*s]*(10*s+3)+[6*s]*(20*s))


def scalar_record(s):
    r=140*s*s+6*s;n=60*s+4
    return dict(s=s,n=n,delta=30*s+3,edges=n*n//4+1,residual=r,
        required=r+4,available=120*s*s+40*s,gap=20*s*s-34*s+4)


def main():
    rows=[]
    # Explicit triple universes grow cubically; use these small representatives.
    for s in [2,3,4]:
        p=profile(s);data=prepare(p);cert=support_certificate(data)
        assert cert and check_support(p,cert)
        old=legacy_tests(data)
        assert all(old.values())
        row=scalar_record(s)
        assert (cert['lhs'],cert['rhs'])==(row['required'],row['available'])
        row.update(legacy_tests=old,exact_support_certificate_pass=True)
        rows.append(row)
        print(row,flush=True)
    out=dict(status='PASS',scope='Explicit representatives s=2,3,4. Universal family rejection has a symbolic proof in PROOF.md.',
             rows=rows,meaning='Residual patterns only, NOT completed graph orders')
    Path(__file__).with_name('FAMILY_TESTS.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()


def degree_family(s):
    if type(s) is not int or s<1:raise ValueError('s>=1 required')
    a=20*s;b=20*s+3;r=56*s*s+6*s+3
    return dict(name=f'degree_family_s{s}',a=a,b=b,t=2,
       d=balanced_list(a,2*r+4),R=balanced_list(a,r),rho=[1]*(6*s+3)+[4*s]*(14*s))
