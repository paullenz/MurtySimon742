#!/usr/bin/env python3
"""Greedy exact minimisation of the exceptional-state BC staircase prototype.

Starts from the 21 proof-active BC cuts in the unique minimum three-SH-cut
certificate, fixes those three indispensable SH corrections, and tries many
deterministic deletion orders. A BC cut is deleted only when the remaining
model still receives an independently verified exact integer-Farkas
certificate. This is an IIS-style research minimisation, not a proof that the
returned subset is globally minimum.
"""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,json,random
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('cg',HERE/'rz_hall_cutgen.py');cg=module_from_spec(spec);spec.loader.exec_module(cg);ex=cg.ex

def leq(a,b):return all(x<=y for x,y in zip(a,b))
def bc_point(z):return (z['R']+z['s'],-(z['R']+z['x']))
def minimal_generators(points):
    pts=sorted(set(tuple(x) for x in points))
    return [list(p) for p in pts if not any(q!=p and leq(q,p) for q in pts)]
def sh_label(v):return (v['s'],-(v['R']+v['x']))
def sh_source(u):return (u['rho'],-(u['q']+u['p']))

def row_from_bc(cut,sources,labels):
    lm={(v['g'],v['s'],v['R'],v['x']):v for v in labels};sm={(u['k'],u['rho'],u['q'],u['p']):u for u in sources};row={}
    for z in cut['label_states']:
        v=lm[(z['g'],z['s'],z['R'],z['x'])];row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for z in cut['source_states']:
        u=sm[(z['k'],z['rho'],z['q'],z['p'])];row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    return row

def row_from_sh(gens,sources,labels):
    gs=[tuple(x) for x in gens];row={}
    for v in labels:
        if any(leq(g,sh_label(v)) for g in gs):row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for u in sources:
        if u['q'] and any(leq(g,sh_source(u)) for g in gs):row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    return row

def solve(old,bc_indices,sh_cuts,a,b,dmax):
    m,sources,labels=cg.build_master(a,b,dmax,old['s'],old['rho']);bc_start=len(m.ub)
    ordered=sorted(bc_indices)
    for i in ordered:m.le(row_from_bc(old['cuts'][i],sources,labels),0)
    bc_end=len(m.ub);sh_start=len(m.ub)
    for c in sh_cuts:m.le(row_from_sh(c['generators'],sources,labels),0)
    sh_end=len(m.ub);ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m)
    detail=None
    if cert:
        active_bc=[];active_sh=[]
        for row_i,w in cert['ub']:
            if bc_start<=row_i<bc_end:
                j=ordered[row_i-bc_start];cut=old['cuts'][j]
                active_bc.append({'cut_index':j,'weight':w,'generator_size':cut.get('generator_size'),'generators':minimal_generators(bc_point(z) for z in cut['label_states'])})
            elif sh_start<=row_i<sh_end:
                j=row_i-sh_start;c=sh_cuts[j]
                active_sh.append({'slot':j,'source_cut_index':c['index'],'weight':w,'generator_size':c['generator_size'],'generators':c['generators']})
        detail={'rhs':cert['rhs'],'active_bc':active_bc,'active_sh':active_sh}
    return cert is not None,detail

def main():
    p=argparse.ArgumentParser();p.add_argument('--bc-json',type=Path,required=True);p.add_argument('--subset-json',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--trials',type=int,default=24);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    B=json.loads(a.bc_json.read_text());S=json.loads(a.subset_json.read_text());old=next(r for r in B['records'] if not r['rejected_exactly'])
    mc=S['minimum_certificates'][0];assert mc['subset']==[1,2,3]
    start=sorted(x['cut_index'] for x in mc['active_bc']);weights={x['cut_index']:x['weight'] for x in mc['active_bc']}
    sh_cuts=[S['sh_cuts'][i] for i in mc['subset']]
    ok,detail=solve(old,start,sh_cuts,a.a,a.b,a.dmax);assert ok
    orders=[]
    orders.append(('index_up',start[:]))
    orders.append(('index_down',list(reversed(start))))
    orders.append(('weight_up',sorted(start,key=lambda i:(weights[i],i))))
    orders.append(('weight_down',sorted(start,key=lambda i:(-weights[i],i))))
    for seed in range(max(0,a.trials-len(orders))):
        z=start[:];random.Random(seed).shuffle(z);orders.append((f'random_{seed}',z))
    trials=[];best=None
    for name,order in orders:
        keep=set(start);tests=0
        for i in order:
            if i not in keep:continue
            cand=keep-{i};tests+=1
            good,_=solve(old,cand,sh_cuts,a.a,a.b,a.dmax)
            if good:keep=cand
        good,fin=solve(old,keep,sh_cuts,a.a,a.b,a.dmax);assert good
        rec={'order':name,'size':len(keep),'bc_indices':sorted(keep),'tests':tests,'certificate':fin};trials.append(rec)
        if best is None or rec['size']<best['size'] or (rec['size']==best['size'] and rec['bc_indices']<best['bc_indices']):best=rec
    out={'schema':'n30-exception-bc-greedy-minimization-v1','hard_position':old['hard_position'],'demand_id':old['demand_id'],'starting_active_bc_count':len(start),'fixed_sh_subset':[1,2,3],'trials':trials,'best':best,'interpretation':'Greedy deletion from the 21 proof-active BC rows with the unique minimum three-SH correction fixed. Every accepted deletion preserves an exact integer-Farkas contradiction. The best subset is irreducible for its tested order, not certified globally minimum.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'starting':len(start),'best_size':best['size'],'best_indices':best['bc_indices'],'best_rhs':best['certificate']['rhs']},indent=2))
if __name__=='__main__':main()
