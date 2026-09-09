#!/usr/bin/env python3
"""Semantic mining of the minimized 6-BC + 3-SH exceptional certificate.

Reconstructs the exceptional n=30 W/L master, adds the six BC staircase rows
from the best greedy minimisation checkpoint and the unique minimum three SH
corrections, then obtains an independently verified exact integer-Farkas
certificate. All equality and inequality multipliers are labelled by semantic
family so the finite contradiction can be translated into a symbolic bound.
"""
from collections import Counter
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
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

def row_from_sh(gens,sources,labels):
    gs=[tuple(x) for x in gens];row={}
    for v in labels:
        if any(leq(g,sh_label(v)) for g in gs):row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for u in sources:
        if u['q'] and any(leq(g,sh_source(u)) for g in gs):row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    return row

def main():
    p=argparse.ArgumentParser();p.add_argument('--bc-json',type=Path,required=True);p.add_argument('--subset-json',type=Path,required=True);p.add_argument('--min-json',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    B=json.loads(a.bc_json.read_text());S=json.loads(a.subset_json.read_text());M=json.loads(a.min_json.read_text())
    old=next(r for r in B['records'] if not r['rejected_exactly']); best=M['best']; bc_indices=best['bc_indices']
    mc=S['minimum_certificates'][0]; assert mc['subset']==[1,2,3]; sh=[S['sh_cuts'][i] for i in mc['subset']]
    m,sources,labels=cg.build_master(a.a,a.b,a.dmax,old['s'],old['rho'])
    SG=sorted(Counter(old['rho']).items());LG=sorted(Counter(old['s']).items())
    # build_master equality order: source norms, qp balance, label norms, residual budget, total incidence.
    eq_tags=[]
    for k,(rho,nk) in enumerate(SG):eq_tags.append({'family':'source_norm','k':k,'rho':rho,'multiplicity':nk})
    eq_tags.append({'family':'qp_balance'})
    for g,(s,ng) in enumerate(LG):eq_tags.append({'family':'label_norm','g':g,'s':s,'multiplicity':ng})
    eq_tags.append({'family':'residual_budget'})
    eq_tags.append({'family':'incidence_mass'})
    assert len(eq_tags)==len(m.eq),(len(eq_tags),len(m.eq))
    # build_master inequality order is threshold transport th=1..a.
    ub_tags=[{'family':'transport_threshold','threshold':th} for th in range(1,a.a+1)]
    assert len(ub_tags)==len(m.ub),(len(ub_tags),len(m.ub))
    for i in bc_indices:
        m.le(row_from_bc(old['cuts'][i],sources,labels),0)
        ub_tags.append({'family':'BC_staircase','source_cut_index':i,'generator_size':old['cuts'][i].get('generator_size')})
    for c in sh:
        m.le(row_from_sh(c['generators'],sources,labels),0)
        ub_tags.append({'family':'SH_staircase','source_cut_index':c['index'],'generator_size':c['generator_size'],'generators':c['generators']})
    bound_start=len(m.ub); ex.add_unit_density_bounds(m)
    for j,name in enumerate(m.names):ub_tags.append({'family':'unit_bound','variable_index':j,'variable_name':repr(name)})
    assert len(ub_tags)==len(m.ub)
    cert=ex.exact_certificate(m); assert cert is not None; ex.verify_certificate(m,cert)
    active_ub=[];active_eq=[];family_weight={};family_count={}
    for i,w in cert['ub']:
        tag=dict(ub_tags[i]);tag.update({'row':i,'weight':w});active_ub.append(tag)
        f=tag['family'];family_weight[f]=family_weight.get(f,0)+w;family_count[f]=family_count.get(f,0)+1
    for i,w in cert['eq']:
        tag=dict(eq_tags[i]);tag.update({'row':i,'weight':w});active_eq.append(tag)
        f=tag['family'];family_weight[f]=family_weight.get(f,0)+abs(w);family_count[f]=family_count.get(f,0)+1
    out={'schema':'n30-exception-minimal-pairwise-certificate-semantic-v1','hard_position':old['hard_position'],'demand_id':old['demand_id'],'s':old['s'],'rho':old['rho'],'bc_indices':bc_indices,'sh_indices':[c['index'] for c in sh],'certificate_rhs':cert['rhs'],'certificate_rounding_scale':cert['rounding_scale'],'active_inequalities':active_ub,'active_equalities':active_eq,'family_abs_weight':family_weight,'family_active_rows':family_count,'unit_bound_active_count':sum(x['family']=='unit_bound' for x in active_ub),'interpretation':'Exact semantic decomposition of the minimized 6-BC + 3-SH certificate. Floating point proposes the ray only; integer multiplier arithmetic is independently verified.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'rhs':out['certificate_rhs'],'family_active_rows':family_count,'unit_bound_active_count':out['unit_bound_active_count'],'active_equalities':active_eq,'active_nonunit_inequalities':[x for x in active_ub if x['family']!='unit_bound']},indent=2,sort_keys=True))
if __name__=='__main__':main()
