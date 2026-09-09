#!/usr/bin/env python3
"""Exact diagonal/CDF ablation inside the two pairwise dominance orders.

BC diagonal H(d)=d+c is equivalent to incidence-weighted one-dimensional
stochastic dominance
    y=x-s >= delta=p-rho+1.
SH diagonal K(s)=s+c is equivalent to
    z=R+x-s >= gamma=q+p-rho.

For each family this script adds every distinct integer lower-tail inequality
mass(label variable <= c) <= mass(source variable <= c), then exactifies all
seven preserved n=30 hard states. This tests whether arbitrary staircase shape
is needed beyond the natural diagonal subfamilies.
"""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('cg',HERE/'rz_hall_cutgen.py');cg=module_from_spec(spec);spec.loader.exec_module(cg);ex=cg.ex

def add_cdf(m,sources,labels,fam):
    if fam=='BCDIAG':
        lv=lambda v:v['x']-v['s']; sv=lambda u:u['p']-u['rho']+1
    elif fam=='SHDIAG':
        lv=lambda v:v['R']+v['x']-v['s']; sv=lambda u:u['q']+u['p']-u['rho']
    else: raise ValueError(fam)
    cuts=sorted(set([lv(v) for v in labels]+[sv(u) for u in sources if u['q']]))
    added=0
    for c in cuts:
        row={}
        for v in labels:
            if lv(v)<=c: row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
        for u in sources:
            if u['q'] and sv(u)<=c: row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
        m.le(row,0);added+=1
    return added

def main():
    p=argparse.ArgumentParser();p.add_argument('--demands-json',type=Path,required=True);p.add_argument('--rows',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--t',type=int,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();hard=cg.load(a.demands_json,a.rows,a.t)
    modes={'NONE':(), 'BCDIAG':('BCDIAG',), 'SHDIAG':('SHDIAG',), 'BOTH':('BCDIAG','SHDIAG')};records=[]
    for hp,(did,total,s,rho) in enumerate(hard):
        rr={'hard_position':hp,'demand_id':did,'modes':{}}
        for name,fams in modes.items():
            m,sources,labels=cg.build_master(a.a,a.b,a.dmax,s,rho);counts={}
            for fam in fams:counts[fam]=add_cdf(m,sources,labels,fam)
            ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m)
            rr['modes'][name]={'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs'],'cdf_cuts_added':counts}
        records.append(rr)
    summary={name:{'exact_rejections':sum(r['modes'][name]['rejected_exactly'] for r in records),'rejected_positions':[r['hard_position'] for r in records if r['modes'][name]['rejected_exactly']]} for name in modes}
    out={'schema':'n30-pairwise-diagonal-cdf-ablation-v1','summary':summary,'records':records,'interpretation':'Exact test of all lower-tail inequalities for y>=delta and z>=gamma. Failure shows general staircase geometry is stronger than these natural diagonal one-dimensional projections.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,indent=2,sort_keys=True))
if __name__=='__main__':main()
