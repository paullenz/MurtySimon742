#!/usr/bin/env python3
"""Exact subset minimization for the four SH correction staircases.

Consumes the preserved BC checkpoint and v2 BC+pairwise checkpoint. For the
unique BC-surviving n=30 state, reconstruct each ambient (s,-h) upper-set row
from its minimal generator antichain and test every subset of the generated SH
cuts. Rejection is accepted only through exact integer-Farkas verification.
"""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
from itertools import combinations
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('cg',HERE/'rz_hall_cutgen.py');cg=module_from_spec(spec);spec.loader.exec_module(cg);ex=cg.ex

def leq(a,b): return all(x<=y for x,y in zip(a,b))
def sh_label(v): return (v['s'],-(v['R']+v['x']))
def sh_source(u): return (u['rho'],-(u['q']+u['p']))

def row_from_bc(cut,sources,labels):
    lm={(v['g'],v['s'],v['R'],v['x']):v for v in labels};sm={(u['k'],u['rho'],u['q'],u['p']):u for u in sources};row={}
    for z in cut['label_states']:
        v=lm[(z['g'],z['s'],z['R'],z['x'])];row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for z in cut['source_states']:
        u=sm[(z['k'],z['rho'],z['q'],z['p'])];row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    return row

def row_from_generators(gens,sources,labels):
    gens=[tuple(x) for x in gens];row={}
    for v in labels:
        if any(leq(g,sh_label(v)) for g in gens):row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for u in sources:
        if u['q'] and any(leq(g,sh_source(u)) for g in gens):row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    return row

def main():
    p=argparse.ArgumentParser();p.add_argument('--bc-json',type=Path,required=True);p.add_argument('--pair-json',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    B=json.loads(a.bc_json.read_text());P=json.loads(a.pair_json.read_text())
    old=next(r for r in B['records'] if not r['rejected_exactly']);pos=old['hard_position']
    pr=next(r for r in P['records'] if r['hard_position']==pos);cuts=pr['modes']['BC+SH']['pairwise_cuts']
    assert cuts and all(c['family']=='SH' for c in cuts)
    tests=[]
    for k in range(len(cuts)+1):
        for sub in combinations(range(len(cuts)),k):
            m,sources,labels=cg.build_master(a.a,a.b,a.dmax,old['s'],old['rho'])
            for c in old['cuts']:m.le(row_from_bc(c,sources,labels),0)
            for i in sub:m.le(row_from_generators(cuts[i]['generators'],sources,labels),0)
            ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m)
            tests.append({'subset':list(sub),'size':k,'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs']})
    rejecting=[x for x in tests if x['rejected_exactly']];minsize=min((x['size'] for x in rejecting),default=None)
    minimal=[x for x in rejecting if x['size']==minsize]
    out={'schema':'n30-exception-sh-subset-minimization-v1','hard_position':pos,'demand_id':old['demand_id'],'sh_cuts':[{'index':i,'generator_size':c['generator_size'],'generators':c['generators']} for i,c in enumerate(cuts)],'tests':tests,'minimum_rejecting_subset_size':minsize,'minimum_rejecting_subsets':[x['subset'] for x in minimal],'interpretation':'All subsets of the four generated ambient SH correction cuts are tested on top of the full preserved BC library. Exact integer-Farkas acceptance only.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'minimum_rejecting_subset_size':minsize,'minimum_rejecting_subsets':out['minimum_rejecting_subsets'],'sh_cuts':out['sh_cuts']},indent=2))
if __name__=='__main__':main()
