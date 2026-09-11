#!/usr/bin/env python3
"""Non-circular exact validity-mask audit across the t=1,2,3 laboratories.

For each lab, recompute the exact rational gap of *every* preserved scalar
template before constructing any feature labels.  Then test h,J only against
the resulting complete validity masks.  This deliberately avoids chosen
assignment rules.
"""
from __future__ import annotations
from argparse import ArgumentParser
from collections import Counter,defaultdict
from pathlib import Path
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

def feat(p):
    rho=p['rho'];s=p['s'];z2=sum(x>=2 for x in rho);D1=s.count(1)
    return {'h':h_res(rho),'J':2*z2-D1,'D1':D1,'rho1':rho.count(1),'z2':z2}

def summarize(P,masks):
    records=[];mc=Counter();mult=Counter()
    for i,p in enumerate(P):
        mask=tuple(k for k in sorted(masks) if masks[k][i])
        if not mask:raise AssertionError(('uncovered',i))
        mid='+'.join(mask);f=feat(p);records.append((i,mid,f));mc[mid]+=1;mult[len(mask)]+=1
    def census(fields):
        d=defaultdict(Counter)
        for i,mid,f in records:d[tuple(f[x] for x in fields)][mid]+=1
        mixed=[(k,v) for k,v in d.items() if len(v)>1]
        return {'occupied_cells':len(d),'mixed_cells':len(mixed),'profiles_in_mixed_cells':sum(sum(v.values()) for _,v in mixed)}
    return {'profiles':len(P),'mask_counts':dict(sorted(mc.items())),'coverage_multiplicity':dict(sorted(mult.items())),
            'h_J':census(('h','J')),'h_J_D1_rho1':census(('h','J','D1','rho1')),
            'records':[{'index':i,'mask':mid,**f} for i,mid,f in records]}

def main():
    ap=ArgumentParser();ap.add_argument('--t1-script',type=Path,required=True);ap.add_argument('--t2-script',type=Path,required=True);ap.add_argument('--t3-script',type=Path,required=True);ap.add_argument('--t2-demands-json',type=Path,required=True);ap.add_argument('--t2-rows',type=Path,required=True);ap.add_argument('--t3-demands-json',type=Path,required=True);ap.add_argument('--t3-rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    t1=load_module('t1',z.t1_script);t2=load_module('t2',z.t2_script);t3=load_module('t3',z.t3_script)
    P1=[{'s':list(p['s']),'rho':list(p['rho'])} for p in t1.PROFILES]
    M1={name:[t1.certificate_gap(p,th)[0]>0 for p in t1.PROFILES] for name,th in t1.TEMPLATES.items()}
    P2=t2.load(z.t2_demands_json,z.t2_rows);M2={name:[g>0 for g in t2.gaps(P2,th)] for name,th in t2.TEMPLATES.items()}
    P3=t3.load(z.t3_demands_json,z.t3_rows);M3={name:[g>0 for g in t3.gaps_for(P3,th)] for name,th in t3.TEMPLATES.items()}
    if (len(P1),len(P2),len(P3))!=(7,902,94):raise AssertionError((len(P1),len(P2),len(P3)))
    labs={'t1':summarize(P1,M1),'t2':summarize(P2,M2),'t3':summarize(P3,M3)}
    out={'schema':'adjacent-t123-validity-mask-audit-exact-v1','status':'PASS','labs':labs,
         'acceptance':'every template gap is recomputed exactly before masks/features; no assignment labels are used',
         'conclusion':'h,J is assessed only as a classifier of complete exact validity masks, not chosen sufficient assignments.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','labs':{k:{'profiles':v['profiles'],'mask_counts':v['mask_counts'],'coverage_multiplicity':v['coverage_multiplicity'],'h_J':v['h_J'],'h_J_D1_rho1':v['h_J_D1_rho1']} for k,v in labs.items()}},indent=2,sort_keys=True))
if __name__=='__main__':main()
