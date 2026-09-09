#!/usr/bin/env python3
"""Exact test of 2D BC upper-set cuts plus 1D s/rho tail dominance.

The s-tail inequalities are the valid monotone-coupling marginals
  sum_{label s>=S} n_g x L <= sum_{source rho>=S} n_k q W.
We test whether these simple one-dimensional corrections, added to the preserved
2D BC staircase library, close the one n=30 hard state that BC alone leaves.
"""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('cg',HERE/'rz_hall_cutgen.py');cg=module_from_spec(spec);spec.loader.exec_module(cg);ex=cg.ex

def row_from_cut(cut,sources,labels):
    lm={(v['g'],v['s'],v['R'],v['x']):v for v in labels};sm={(u['k'],u['rho'],u['q'],u['p']):u for u in sources};row={}
    for z in cut['label_states']:
        v=lm[(z['g'],z['s'],z['R'],z['x'])];row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for z in cut['source_states']:
        u=sm[(z['k'],z['rho'],z['q'],z['p'])];row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    return row

def add_s_tails(m,sources,labels):
    maxv=max([v['s'] for v in labels]+[u['rho'] for u in sources]); added=[]
    for S in range(2,maxv+1):
        row={}
        for v in labels:
            if v['s']>=S: row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
        for u in sources:
            if u['q'] and u['rho']>=S: row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
        m.le(row,0);added.append(S)
    return added

def solve(old,a,b,dmax,use_bc,use_s):
    m,sources,labels=cg.build_master(a,b,dmax,old['s'],old['rho']);
    if use_bc:
        for c in old['cuts']:m.le(row_from_cut(c,sources,labels),0)
    tails=add_s_tails(m,sources,labels) if use_s else []
    ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m)
    return {'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs'],'bc_cuts':len(old['cuts']) if use_bc else 0,'s_tail_thresholds':tails}

def main():
    p=argparse.ArgumentParser();p.add_argument('--bc-json',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();H=json.loads(a.bc_json.read_text());records=[]
    for old in H['records']:
        modes={'S':solve(old,a.a,a.b,a.dmax,False,True),'BC':solve(old,a.a,a.b,a.dmax,True,False),'BCS':solve(old,a.a,a.b,a.dmax,True,True)}
        records.append({'hard_position':old['hard_position'],'demand_id':old['demand_id'],'modes':modes})
    summary={m:{'exact_rejections':sum(r['modes'][m]['rejected_exactly'] for r in records),'rejected_positions':[r['hard_position'] for r in records if r['modes'][m]['rejected_exactly']]} for m in ('S','BC','BCS')}
    out={'schema':'rz-bc-plus-s-tail-ablation-v1','source_checkpoint':str(a.bc_json),'summary':summary,'records':records,'interpretation':'Tests whether full 2D BC staircase library plus only 1D s/rho tail dominance closes the exceptional n30 hard state. Exact integer-Farkas acceptance only.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,indent=2,sort_keys=True))
if __name__=='__main__':main()
