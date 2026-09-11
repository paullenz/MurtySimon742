#!/usr/bin/env python3
"""Exact regime-wise margin census for the non-circular t=1,2,3 assignments.

The templates and profile frontiers are the preserved exact objects.  The rules
below depend only on J for t=1,2 and on (h,J) for t=3.  Every assigned gap is
recomputed using fractions.Fraction through the original exact checker.  The
output records the exact minimum gap and extremal profile indices in each cell.
"""
from __future__ import annotations
from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path
from fractions import Fraction
import importlib.util,json


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);assert spec.loader is not None
    spec.loader.exec_module(m);return m

def h_res(rho):
    h=0
    for k,x in enumerate(sorted(rho,reverse=True),1):
        if x>=k:h=k
        else:break
    return h

def features(p):
    rho=p['rho'];s=p['s'];z2=sum(x>=2 for x in rho);D1=s.count(1)
    return h_res(rho),2*z2-D1

def choose(lab,h,J):
    if lab=='t1':return 'A' if J in (14,16) else 'B'
    if lab=='t2':
        if J==12:return 'T0'
        if J%2:return 'T1'
        return 'T2'
    if lab=='t3':
        if h==5:return 'A38'
        if (h,J)==(4,13):return 'A0'
        if (h,J)==(4,14):return 'A1'
        return 'A530'
    raise ValueError(lab)
def rat(x):return [x.numerator,x.denominator]

def audit_lab(lab,P,gaps):
    cells=defaultdict(list);allrows=[]
    for i,p in enumerate(P):
        h,J=features(p);name=choose(lab,h,J);g=gaps[name][i]
        if g<=0:raise AssertionError((lab,i,h,J,name,g))
        key=(J,) if lab in ('t1','t2') else (h,J)
        cells[key].append((i,name,g));allrows.append((i,h,J,name,g))
    out=[]
    for key in sorted(cells):
        rows=cells[key];mn=min(g for _,_,g in rows);mx=max(g for _,_,g in rows)
        names=sorted(set(n for _,n,_ in rows));assert len(names)==1
        out.append({'key':list(key),'profiles':len(rows),'template':names[0],
                    'minimum_gap':rat(mn),'minimum_gap_indices':[i for i,n,g in rows if g==mn],
                    'maximum_gap':rat(mx)})
    overall=min(g for *_,g in allrows)
    return {'profiles':len(P),'cells':out,'cell_count':len(out),'minimum_assigned_gap':rat(overall),
            'minimum_assigned_gap_indices':[i for i,h,J,n,g in allrows if g==overall]}

def main():
    ap=ArgumentParser();ap.add_argument('--t1-script',type=Path,required=True);ap.add_argument('--t2-script',type=Path,required=True);ap.add_argument('--t3-script',type=Path,required=True);ap.add_argument('--t2-demands-json',type=Path,required=True);ap.add_argument('--t2-rows',type=Path,required=True);ap.add_argument('--t3-demands-json',type=Path,required=True);ap.add_argument('--t3-rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    t1=load_module('t1',z.t1_script);t2=load_module('t2',z.t2_script);t3=load_module('t3',z.t3_script)
    P1=[{'s':list(p['s']),'rho':list(p['rho'])} for p in t1.PROFILES]
    G1={name:[t1.certificate_gap(p,th)[0] for p in t1.PROFILES] for name,th in t1.TEMPLATES.items()}
    P2=t2.load(z.t2_demands_json,z.t2_rows);G2={name:t2.gaps(P2,th) for name,th in t2.TEMPLATES.items()}
    P3=t3.load(z.t3_demands_json,z.t3_rows);G3={name:t3.gaps_for(P3,th) for name,th in t3.TEMPLATES.items()}
    labs={'t1':audit_lab('t1',P1,G1),'t2':audit_lab('t2',P2,G2),'t3':audit_lab('t3',P3,G3)}
    out={'schema':'adjacent-t123-regime-margin-exact-v1','status':'PASS','labs':labs,
         'arithmetic':'fractions.Fraction exact rational','solver_used':False,
         'interpretation':'Exact positive margins for the post-mask, non-circular finite regime rules. Cell minima are the natural extremal targets for symbolic generalization.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
