#!/usr/bin/env python3
"""Test whether bounded-size canonical Hall staircases suffice exactly.

Consumes a preserved Z-free Hall cut-generation checkpoint. For each hard row,
rebuilds the W/L master and retains only generated Hall cuts whose label set has
at most K inclusion-maximal neighbourhoods. Rejection is accepted only through
the exact integer-Farkas checker. This tests the generated cut library; failure
at a given K does not prove that no other K-frontier Hall cut could help.
"""
from collections import defaultdict
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('cutgen',HERE/'rz_hall_cutgen.py'); cg=module_from_spec(spec); spec.loader.exec_module(cg)
ex=cg.ex

def frontier_size(cut,sources):
    neigh=[]
    for vd in cut['label_states']:
        v={'g':vd['g'],'s':vd['s'],'R':vd['R'],'x':vd['x']}
        neigh.append(frozenset(i for i,u in enumerate(sources) if u['q'] and cg.compat(u,v)))
    uniq=set(neigh)
    maximal=[n for n in uniq if not any(n < m for m in uniq)]
    return len(maximal)

def row_from_cut(cut,sources,labels):
    lm={(v['g'],v['s'],v['R'],v['x']):v for v in labels}; sm={(u['k'],u['rho'],u['q'],u['p']):u for u in sources}; row={}
    for z in cut['label_states']:
        v=lm[(z['g'],z['s'],z['R'],z['x'])]; row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for z in cut['source_states']:
        u=sm[(z['k'],z['rho'],z['q'],z['p'])]; row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    return row

def main():
    p=argparse.ArgumentParser();p.add_argument('--hall-json',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--t',type=int,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--ks',default='1,2,3,4,5,6,7,8,10');a=p.parse_args();ks=[int(x) for x in a.ks.split(',')]
    H=json.loads(a.hall_json.read_text()); records=[]
    for old in H['records']:
        m0,sources,labels=cg.build_master(a.a,a.b,a.dmax,old['s'],old['rho'])
        decorated=[]
        for i,c in enumerate(old['cuts']): decorated.append((i,frontier_size(c,sources),c))
        tests={}
        for K in ks:
            m,s2,l2=cg.build_master(a.a,a.b,a.dmax,old['s'],old['rho']); kept=[]
            for i,f,c in decorated:
                if f<=K: m.le(row_from_cut(c,s2,l2),0);kept.append(i)
            ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m)
            tests[str(K)]={'cuts_kept':len(kept),'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs']}
        records.append({'hard_position':old['hard_position'],'demand_id':old['demand_id'],'generated_cuts':len(old['cuts']),'frontier_histogram':{str(k):sum(f==k for _,f,_ in decorated) for k in sorted(set(f for _,f,_ in decorated))},'tests':tests})
    summary={str(K):{'exact_rejections':sum(r['tests'][str(K)]['rejected_exactly'] for r in records),'survivors':sum(not r['tests'][str(K)]['rejected_exactly'] for r in records),'rejected_positions':[r['hard_position'] for r in records if r['tests'][str(K)]['rejected_exactly']]} for K in ks}
    out={'schema':'rz-hall-bounded-frontier-test-v1','source_checkpoint':str(a.hall_json),'summary':summary,'records':records,'interpretation':'Exact test using only already-generated Hall cuts with canonical maximal-neighbourhood frontier size <=K. Non-rejection does not exclude undiscovered K-frontier cuts.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,indent=2,sort_keys=True))
if __name__=='__main__':main()
