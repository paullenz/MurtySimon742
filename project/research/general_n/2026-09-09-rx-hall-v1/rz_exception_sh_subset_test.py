#!/usr/bin/env python3
"""Exact subset minimization for the four SH correction staircases.

Consumes the preserved BC checkpoint and v2 BC+pairwise checkpoint. For the
unique BC-surviving n=30 state, reconstruct each ambient (s,-h) upper-set row
from its minimal generator antichain and test every subset of the generated SH
cuts. Rejection is accepted only through exact integer-Farkas verification.

v2 additionally records the exact Farkas weights on the BC and SH staircase
rows for every rejecting subset, so the unique minimum certificate can be used
as a finite prototype for a symbolic F(d,h)+G(s,h) potential.
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
def bc_point(z): return (z['R']+z['s'],-(z['R']+z['x']))

def minimal_generators(points):
    pts=sorted(set(tuple(x) for x in points))
    return [list(p) for p in pts if not any(q!=p and leq(q,p) for q in pts)]

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
    bc_meta=[{'index':i,'generator_size':c.get('generator_size'), 'generators':minimal_generators(bc_point(z) for z in c['label_states'])} for i,c in enumerate(old['cuts'])]
    tests=[]
    for k in range(len(cuts)+1):
        for sub in combinations(range(len(cuts)),k):
            m,sources,labels=cg.build_master(a.a,a.b,a.dmax,old['s'],old['rho'])
            bc_start=len(m.ub)
            for c in old['cuts']:m.le(row_from_bc(c,sources,labels),0)
            bc_end=len(m.ub)
            sh_start=len(m.ub)
            for i in sub:m.le(row_from_generators(cuts[i]['generators'],sources,labels),0)
            sh_end=len(m.ub)
            ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m)
            rec={'subset':list(sub),'size':k,'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs']}
            if cert is not None:
                active_bc=[];active_sh=[]
                for row_i,w in cert['ub']:
                    if bc_start<=row_i<bc_end:
                        j=row_i-bc_start; meta=bc_meta[j]
                        active_bc.append({'cut_index':j,'weight':w,'generator_size':meta['generator_size'],'generators':meta['generators']})
                    elif sh_start<=row_i<sh_end:
                        local=row_i-sh_start; actual=sub[local]; c=cuts[actual]
                        active_sh.append({'cut_index':actual,'weight':w,'generator_size':c['generator_size'],'generators':c['generators']})
                rec['active_bc']=active_bc;rec['active_sh']=active_sh
                rec['active_bc_count']=len(active_bc);rec['active_sh_count']=len(active_sh)
            tests.append(rec)
    rejecting=[x for x in tests if x['rejected_exactly']];minsize=min((x['size'] for x in rejecting),default=None)
    minimal=[x for x in rejecting if x['size']==minsize]
    out={'schema':'n30-exception-sh-subset-minimization-v2','hard_position':pos,'demand_id':old['demand_id'],'sh_cuts':[{'index':i,'generator_size':c['generator_size'],'generators':c['generators']} for i,c in enumerate(cuts)],'tests':tests,'minimum_rejecting_subset_size':minsize,'minimum_rejecting_subsets':[x['subset'] for x in minimal],'minimum_certificates':minimal,'interpretation':'All subsets of the four generated ambient SH correction cuts are tested on top of the full preserved BC library. Exact integer-Farkas acceptance only; v2 records proof-active BC/SH staircase weights.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'minimum_rejecting_subset_size':minsize,'minimum_rejecting_subsets':out['minimum_rejecting_subsets'],'minimum_certificates':[{'subset':x['subset'],'rhs':x['certificate_rhs'],'active_bc_count':x.get('active_bc_count'),'active_sh':x.get('active_sh')} for x in minimal]},indent=2))
if __name__=='__main__':main()
