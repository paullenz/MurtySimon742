#!/usr/bin/env python3
"""Second constants check: rational enclosures only; imports no other project code."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json

def check(eta=F(1,5000),bad=F(9,125),zcap=F(17,30),a0=25):
    lo=F(1414213562373095048801688724209,10**30)
    hi=lo+F(1,10**30)
    if not (0<lo<hi):raise ValueError('root interval')
    if not lo*lo<2<hi*hi:raise ValueError('root enclosure')
    c_hi=F(3,2)-lo;c1lo=F(3,2)-hi-eta;c1hi=F(3,2)-lo-eta
    lamlo=1-hi/2;L=F(6,25)
    if not lamlo>L or not eta/(lamlo-L)**2<bad:raise ValueError('bad-label margin')
    # sqrt(eta)=sqrt(2)/100 for the stated eta, verified by squaring.
    if F(2,10000)!=eta:raise ValueError('eta identity')
    rhi=-2+2*eta+F(151,100)*hi
    if not rhi<F(17,125) or not F(17,125)/L<=zcap:raise ValueError('source bound')
    T=L+bad+F(1,a0);gap=L*(1-bad)-(zcap*zcap+T*T)/2
    if not gap>0:raise ValueError('pair contradiction')
    blo=F(613168,10**6);bhi=F(613169,10**6)
    if not ((blo-F(1,2))/(1-blo))**2<c1lo<c1hi<((bhi-F(1,2))/(1-bhi))**2:
        raise ValueError('beta interval')
    if not c1lo>F(1,12):raise ValueError('odd rounding')
    cases=[]
    for a in range(1,a0):
        v=blo*(a+1)/(1-blo);b=-((-v.numerator)//v.denominator)
        d=b-a-1;t=d*d//4
        if d<=0 or not t>c_hi*a*a:raise ValueError('small-a contradiction')
        cases.append([a,b,t])
    return dict(all_checks_pass=True,sqrt2_interval=[str(lo),str(hi)],
      final_gap=str(gap),small_a_cases=cases,uses_other_project_implementations=False)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    result=check();rejected=[]
    for name,kw in [('bad_fraction_too_small',{'bad':F(1,100)}),
                    ('invalid_source_cap',{'zcap':F(1,2)}),
                    ('unsupported_small_cutoff',{'a0':10})]:
        try:check(**kw)
        except ValueError:rejected.append(name)
        else:raise RuntimeError('Damaged constants passed: '+name)
    result['negative_controls_rejected']=rejected
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
