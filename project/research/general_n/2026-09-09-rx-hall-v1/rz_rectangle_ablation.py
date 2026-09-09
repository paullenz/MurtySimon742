#!/usr/bin/env python3
"""Exact rectangle-only ablation for the two pairwise dominance orders.

Adds all single-generator upper-set inequalities of the forms
  BC rectangle: d>=D and h<=H versus alpha>=D and beta<=H
  SH rectangle: s>=S and h<=H versus rho>=S and beta<=H
on top of the Z-free W/L master. Tests BC rectangles alone, SH rectangles alone,
and both families together on the seven preserved n=30 hard states.

This asks whether multistep staircase unions are genuinely necessary. Final
rejection is accepted only through exact integer-Farkas verification.
"""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('cg',HERE/'rz_hall_cutgen.py');cg=module_from_spec(spec);spec.loader.exec_module(cg);ex=cg.ex

def add_rectangles(m,sources,labels,fam):
    if fam=='BC':
        avals=sorted(set([v['R']+v['s'] for v in labels]+[u['rho']+u['q']-1 for u in sources if u['q']]))
    elif fam=='SH':
        avals=sorted(set([v['s'] for v in labels]+[u['rho'] for u in sources if u['q']]))
    else: raise ValueError(fam)
    hvals=sorted(set([v['R']+v['x'] for v in labels]+[u['q']+u['p'] for u in sources if u['q']]))
    added=0
    for A in avals:
        for H in hvals:
            row={}
            for v in labels:
                av=(v['R']+v['s']) if fam=='BC' else v['s']; hv=v['R']+v['x']
                if av>=A and hv<=H: row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
            for u in sources:
                if not u['q']: continue
                av=(u['rho']+u['q']-1) if fam=='BC' else u['rho']; hv=u['q']+u['p']
                if av>=A and hv<=H: row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
            if row:
                m.le(row,0);added+=1
    return added

def main():
    p=argparse.ArgumentParser();p.add_argument('--demands-json',type=Path,required=True);p.add_argument('--rows',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--t',type=int,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();hard=cg.load(a.demands_json,a.rows,a.t)
    modes={'NONE':(), 'BC':('BC',), 'SH':('SH',), 'BCSH':('BC','SH')};records=[]
    for hp,(did,total,s,rho) in enumerate(hard):
        rr={'hard_position':hp,'demand_id':did,'modes':{}}
        for name,fams in modes.items():
            m,sources,labels=cg.build_master(a.a,a.b,a.dmax,s,rho);counts={}
            for fam in fams:counts[fam]=add_rectangles(m,sources,labels,fam)
            ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m)
            rr['modes'][name]={'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs'],'rectangles_added':counts}
        records.append(rr)
    summary={name:{'exact_rejections':sum(r['modes'][name]['rejected_exactly'] for r in records),'rejected_positions':[r['hard_position'] for r in records if r['modes'][name]['rejected_exactly']]} for name in modes}
    out={'schema':'n30-pairwise-rectangle-ablation-v1','summary':summary,'records':records,'interpretation':'All ambient single-generator rectangle upper sets are present. Failure therefore demonstrates need for genuinely multistep staircase unions within this relaxation.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,indent=2,sort_keys=True))
if __name__=='__main__':main()
