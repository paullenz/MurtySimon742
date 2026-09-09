#!/usr/bin/env python3
"""Exact elimination of redundant unit-bound rows from the minimized certificate.

For W/L distribution variables, z<=1 follows from the relevant group
normalisation sum z_j=1 and z_j>=0. Given a Farkas certificate that uses a unit
row w*z<=w, replace it by adding weight w to that group's normalisation
equality. The target variable receives the same coefficient; every other
variable in the group receives an additional nonnegative coefficient; the RHS
is unchanged. This script performs that transformation and verifies the result
exactly on a model containing no explicit unit upper bounds.
"""
from ast import literal_eval
from collections import Counter
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('cg',HERE/'rz_hall_cutgen.py');cg=module_from_spec(spec);spec.loader.exec_module(cg);ex=cg.ex

def leq(a,b):return all(x<=y for x,y in zip(a,b))
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

def main():
    p=argparse.ArgumentParser();p.add_argument('--bc-json',type=Path,required=True);p.add_argument('--subset-json',type=Path,required=True);p.add_argument('--min-json',type=Path,required=True);p.add_argument('--semantic-json',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    B=json.loads(a.bc_json.read_text());S=json.loads(a.subset_json.read_text());M=json.loads(a.min_json.read_text());Z=json.loads(a.semantic_json.read_text())
    old=next(r for r in B['records'] if not r['rejected_exactly']);bc_indices=M['best']['bc_indices'];mc=S['minimum_certificates'][0];sh=[S['sh_cuts'][i] for i in mc['subset']]
    m,sources,labels=cg.build_master(a.a,a.b,a.dmax,old['s'],old['rho'])
    for i in bc_indices:m.le(row_from_bc(old['cuts'][i],sources,labels),0)
    for c in sh:m.le(row_from_sh(c['generators'],sources,labels),0)
    # No unit upper bounds are added.
    SG=sorted(Counter(old['rho']).items());LG=sorted(Counter(old['s']).items())
    eqw={x['row']:x['weight'] for x in Z['active_equalities']}
    replacements=[]
    for x in Z['active_inequalities']:
        if x['family']!='unit_bound':continue
        name=literal_eval(x['variable_name']);w=x['weight']
        if name[0]=='W':
            row=name[1]
        elif name[0]=='L':
            row=len(SG)+1+name[1]
        else:raise AssertionError(name)
        eqw[row]=eqw.get(row,0)+w
        replacements.append({'variable':name,'weight':w,'normalisation_row':row})
    ubw={x['row']:x['weight'] for x in Z['active_inequalities'] if x['family']!='unit_bound'}
    cert={'ub':sorted(ubw.items()),'eq':sorted(eqw.items()),'rhs':Z['certificate_rhs'],'variables':len(m.names),'inequalities':len(m.ub),'equalities':len(m.eq),'rounding_scale':'derived-exact-unit-elimination'}
    rhs=ex.verify_certificate(m,cert);assert rhs==Z['certificate_rhs']==-881
    coef=[0]*len(m.names)
    for i,w in cert['ub']:
        for j,c in m.ub[i].items():coef[j]+=w*c
    for i,w in cert['eq']:
        for j,c in m.eq[i].items():coef[j]+=w*c
    out={'schema':'n30-exception-unit-bound-free-certificate-v1','certificate':cert,'replacements':replacements,'adjusted_equalities':[{'row':i,'weight':w} for i,w in sorted(eqw.items())],'min_variable_coefficient':min(coef),'zero_variable_coefficients':sum(c==0 for c in coef),'positive_variable_coefficients':sum(c>0 for c in coef),'rhs':rhs,'interpretation':'Exact certificate on the minimized 6-BC + 3-SH W/L master with no explicit z<=1 rows. Unit-bound multipliers are absorbed into group normalisation equalities; nonnegativity of all variables completes the contradiction.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:out[k] for k in ('rhs','min_variable_coefficient','zero_variable_coefficients','positive_variable_coefficients')},indent=2))
if __name__=='__main__':main()
