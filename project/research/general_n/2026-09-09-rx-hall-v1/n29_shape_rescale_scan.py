#!/usr/bin/env python3
"""Reconnaissance for natural d-coordinate adaptation of the n30 BC shapes to n29.

Tests only the preserved 38 profiles surviving the first dmax boundary trim.
Every transformed generator set still defines a valid BC upper set; the test
changes the finite dictionary, not the underlying pairwise dominance theorem.
Floating feasibility remains proposal/reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
from fractions import Fraction
import argparse,json,math
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('gp',HERE/'shared_greedy_prune.py');gp=module_from_spec(sp);sp.loader.exec_module(gp)

def leq(a,b):return all(x<=y for x,y in zip(a,b))
def min_gens(g):
    pts=sorted(set(tuple(p) for p in g))
    return tuple(p for p in pts if not any(q!=p and leq(q,p) for q in pts))

def tx_shape(g,mode,target,ref):
    out=[]
    for D,mH in g:
        if mode=='trim':
            if D>target:continue
            D2=D
        elif mode=='clip':D2=min(D,target)
        elif mode=='floor':D2=max(1,(D*target)//ref)
        elif mode=='ceil':D2=max(1,(D*target+ref-1)//ref)
        elif mode=='round':D2=max(1,int(math.floor(D*target/ref+0.5)))
        else:raise ValueError(mode)
        out.append((D2,mH))
    z=min_gens(out)
    if not z:raise ValueError((mode,g))
    return z

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--reference-dmax',type=int,default=11);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text());J=json.loads(z.support_json.read_text());base=[tuple(tuple(p) for p in x['generators']) for x in J['active_BC']];sh=[tuple(tuple(p) for p in x['generators']) for x in J['active_SH']]
    modes=['trim','clip','floor','round','ceil'];records=[];summary={}
    for mode in modes:
        bc=[tx_shape(g,mode,z.dmax,z.reference_dmax) for g in base];rr=[]
        for old in B['trimmed_survivor_records']:
            P=[{'s':old['s'],'rho':old['rho'],'demand_id':old['demand_id']}]
            M,res=gp.solve(P,bc,sh,z.a,z.b,z.dmax)
            rr.append({'hard_position':old['hard_position'],'demand_id':old['demand_id'],'separated':bool(res.success),'objective':float(res.fun) if res.success else None})
        summary[mode]={'tested':len(rr),'separated':sum(r['separated'] for r in rr),'survivors':sum(not r['separated'] for r in rr),'survivor_positions':[r['hard_position'] for r in rr if not r['separated']],'BC_shapes':[[list(p) for p in g] for g in bc]}
    out={'schema':'n29-nine-shape-d-coordinate-rescale-v1','source_boundary_checkpoint':str(z.boundary_json),'source_support':str(z.support_json),'reference_dmax':z.reference_dmax,'target_dmax':z.dmax,'floating_point_reconnaissance_only':True,'summary':summary,'interpretation':'All modes use the same six BC / three SH shape slots. Only BC generator D coordinates are adapted. Each result remains a valid pairwise upper-set dictionary; numerical feasibility is reconnaissance only.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({m:{k:v for k,v in q.items() if k!='BC_shapes'} for m,q in summary.items()},indent=2,sort_keys=True))
if __name__=='__main__':main()
