#!/usr/bin/env python3
"""Exact first-moment ablation of the pairwise dominance reductions.

For the Z-free W/L master, add subsets of the three scalar inequalities implied
by the BC and SH coordinatewise couplings:
  D: sum label x*d <= sum source q*alpha
  H: sum label x*h >= sum source q*beta
  S: sum label x*s <= sum source q*rho
where d=R+s, h=R+x, alpha=rho+q-1 and beta=q+p.

Tests all seven preserved n=30 residual-budget hard states. Acceptance is only
through the exact integer-Farkas checker. This is a simplification/falsification
experiment, not a theorem claim.
"""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
from itertools import combinations
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('cg',HERE/'rz_hall_cutgen.py');cg=module_from_spec(spec);spec.loader.exec_module(cg);ex=cg.ex

def add_moment(m,sources,labels,kind):
    row={}
    if kind=='D':
        for v in labels:
            d=v['R']+v['s']; row[v['var']]=row.get(v['var'],0)+v['n']*v['x']*d
        for u in sources:
            if u['q']:
                alpha=u['rho']+u['q']-1; row[u['var']]=row.get(u['var'],0)-u['n']*u['q']*alpha
    elif kind=='H':
        for u in sources:
            if u['q']:
                beta=u['q']+u['p']; row[u['var']]=row.get(u['var'],0)+u['n']*u['q']*beta
        for v in labels:
            h=v['R']+v['x']; row[v['var']]=row.get(v['var'],0)-v['n']*v['x']*h
    elif kind=='S':
        for v in labels: row[v['var']]=row.get(v['var'],0)+v['n']*v['x']*v['s']
        for u in sources:
            if u['q']: row[u['var']]=row.get(u['var'],0)-u['n']*u['q']*u['rho']
    else: raise ValueError(kind)
    m.le(row,0)

def main():
    p=argparse.ArgumentParser();p.add_argument('--demands-json',type=Path,required=True);p.add_argument('--rows',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--t',type=int,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    hard=cg.load(a.demands_json,a.rows,a.t);families=('D','H','S');modes=[]
    for k in range(4):
        for sub in combinations(families,k):modes.append(sub)
    records=[]
    for hp,(did,total,s,rho) in enumerate(hard):
        rr={'hard_position':hp,'demand_id':did,'modes':{}}
        for sub in modes:
            m,sources,labels=cg.build_master(a.a,a.b,a.dmax,s,rho)
            for kind in sub:add_moment(m,sources,labels,kind)
            ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m)
            name=''.join(sub) if sub else 'NONE'
            rr['modes'][name]={'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs']}
        records.append(rr)
    summary={}
    for sub in modes:
        name=''.join(sub) if sub else 'NONE'
        summary[name]={'exact_rejections':sum(r['modes'][name]['rejected_exactly'] for r in records),'rejected_positions':[r['hard_position'] for r in records if r['modes'][name]['rejected_exactly']]}
    out={'schema':'n30-pairwise-first-moment-ablation-v1','summary':summary,'records':records,'interpretation':'Exact ablation of the three first-moment inequalities implied by BC/SH coordinatewise dominance. Non-rejection shows only that these scalar moments are too weak for this relaxation.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,indent=2,sort_keys=True))
if __name__=='__main__':main()
