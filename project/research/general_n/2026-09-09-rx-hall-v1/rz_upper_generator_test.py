#!/usr/bin/env python3
"""Exact bounded-antichain test for ambient upper-set Hall cuts.

Consumes an ambient upper-set cut-generation checkpoint, rebuilds the W/L
master, and retains only generated upper-set inequalities whose minimal
coordinate generator antichain has size <=K. Final rejection is accepted only
through the exact integer-Farkas checker.
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

def main():
    p=argparse.ArgumentParser();p.add_argument('--upper-json',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--t',type=int,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--ks',default='1,2,3,4,5,6,7,8,9,10');a=p.parse_args();ks=[int(x) for x in a.ks.split(',')]
    H=json.loads(a.upper_json.read_text());records=[]
    for old in H['records']:
        tests={}
        for K in ks:
            m,sources,labels=cg.build_master(a.a,a.b,a.dmax,old['s'],old['rho']);kept=0
            for c in old['cuts']:
                if c['generator_size']<=K:
                    m.le(row_from_cut(c,sources,labels),0);kept+=1
            ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m)
            tests[str(K)]={'cuts_kept':kept,'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs']}
        hist={str(k):sum(c['generator_size']==k for c in old['cuts']) for k in sorted(set(c['generator_size'] for c in old['cuts']))}
        records.append({'hard_position':old['hard_position'],'demand_id':old['demand_id'],'generated_cuts':len(old['cuts']),'generator_histogram':hist,'tests':tests})
    summary={str(K):{'exact_rejections':sum(r['tests'][str(K)]['rejected_exactly'] for r in records),'survivors':sum(not r['tests'][str(K)]['rejected_exactly'] for r in records),'rejected_positions':[r['hard_position'] for r in records if r['tests'][str(K)]['rejected_exactly']]} for K in ks}
    out={'schema':'rz-ambient-upper-bounded-generator-test-v1','source_checkpoint':str(a.upper_json),'summary':summary,'records':records,'interpretation':'Exact test using only already-generated ambient upper-set cuts with minimal coordinate generator antichain size <=K. Non-rejection does not exclude undiscovered K-generator upper sets.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,indent=2,sort_keys=True))
if __name__=='__main__':main()
