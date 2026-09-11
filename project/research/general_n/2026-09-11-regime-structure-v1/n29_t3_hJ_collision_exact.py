#!/usr/bin/env python3
"""Produce exact non-circular collision witnesses for t=3 validity masks.

The target is the independently recomputed set of exact rational templates with
positive gap, never a chosen assignment label.  We preserve the lexicographically
first pair with equal (h,J) but different masks, and test stronger same-source /
same-demand collisions.
"""
from __future__ import annotations
from argparse import ArgumentParser
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import importlib.util,json


def load_module(path):
    spec=importlib.util.spec_from_file_location('cover',path)
    m=importlib.util.module_from_spec(spec); assert spec.loader is not None
    spec.loader.exec_module(m); return m

def h_res(rho):
    h=0
    for k,x in enumerate(sorted(rho,reverse=True),1):
        if x>=k:h=k
        else:break
    return h

def rat(x): return [x.numerator,x.denominator]

def profile_record(i,p,names,gaps):
    rho=p['rho'];s=p['s'];z2=sum(x>=2 for x in rho);D1=s.count(1)
    mask=[n for n in names if gaps[n][i]>0]
    return {
      'index':i,'demand_id':p['demand_id'],'s':s,'rho':rho,
      's_hist':dict(sorted(Counter(s).items())),'rho_hist':dict(sorted(Counter(rho).items())),
      'h':h_res(rho),'D1':D1,'rho1':rho.count(1),'z2':z2,'J':2*z2-D1,
      'r':sum(rho),'S':sum(s),'mask':mask,
      'gaps':{n:rat(gaps[n][i]) for n in names},
    }

def first_collision(records,keyfn):
    cells=defaultdict(list)
    for r in records:cells[keyfn(r)].append(r)
    candidates=[]
    for key,rs in cells.items():
        rs=sorted(rs,key=lambda x:x['index'])
        for a in range(len(rs)):
            for b in range(a+1,len(rs)):
                if rs[a]['mask']!=rs[b]['mask']:
                    candidates.append((rs[a]['index'],rs[b]['index'],key,rs[a],rs[b]))
    if not candidates:return None
    a,b,key,x,y=min(candidates,key=lambda z:(z[1],z[0]))
    return {'key':list(key) if isinstance(key,tuple) else key,'profile_a':x,'profile_b':y}

def main():
    ap=ArgumentParser();ap.add_argument('--cover-script',type=Path,required=True);ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    m=load_module(z.cover_script);P=m.load(z.demands_json,z.rows)
    if len(P)!=94:raise SystemExit(f'expected 94 profiles, got {len(P)}')
    names=sorted(m.TEMPLATES);gaps={n:m.gaps_for(P,m.TEMPLATES[n]) for n in names}
    records=[profile_record(i,p,names,gaps) for i,p in enumerate(P)]
    hj=first_collision(records,lambda r:(r['h'],r['J']))
    same_rho=first_collision(records,lambda r:tuple(r['rho']))
    same_s=first_collision(records,lambda r:tuple(r['s']))
    same_source_summary=first_collision(records,lambda r:(r['h'],r['rho1'],r['z2'],r['r']))
    if hj is None:raise AssertionError('expected (h,J) collision')
    out={'schema':'n29-t3-hJ-validity-mask-collision-exact-v1','status':'PASS','profiles':94,'templates':names,
         'first_hJ_collision':hj,'first_identical_rho_collision':same_rho,'first_identical_s_collision':same_s,
         'first_source_summary_collision':same_source_summary,
         'acceptance':'template masks and gaps recomputed by exact Fraction arithmetic from preserved four-template cover; no assignment labels used',
         'conclusion':'(h,J) is not sufficient to determine exact t=3 template-validity geometry.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    def brief(c):
        if c is None:return None
        return {'key':c['key'],'indices':[c['profile_a']['index'],c['profile_b']['index']],
                'masks':[c['profile_a']['mask'],c['profile_b']['mask']],
                's_hist':[c['profile_a']['s_hist'],c['profile_b']['s_hist']],
                'rho_hist':[c['profile_a']['rho_hist'],c['profile_b']['rho_hist']]}
    print(json.dumps({'status':'PASS','hJ':brief(hj),'same_rho':brief(same_rho),'same_s':brief(same_s),'same_source_summary':brief(same_source_summary)},indent=2,sort_keys=True))
if __name__=='__main__':main()
