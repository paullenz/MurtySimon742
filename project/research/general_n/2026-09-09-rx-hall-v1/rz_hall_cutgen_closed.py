#!/usr/bin/env python3
"""Canonical neighbourhood-closed Hall cut generation for the stripped R+Z core.

Every numerical min-cut label set U is strengthened immediately to
cl(U)={v:N(v) subset N(U)}. The source neighbourhood is unchanged, so this is
a valid stronger Hall inequality. Final contradictions are accepted only via
the exact integer-Farkas checker.
"""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('cg',HERE/'rz_hall_cutgen.py'); cg=module_from_spec(spec); spec.loader.exec_module(cg); ex=cg.ex

def closed_separate(sol,sources,labels):
    raw=cg.separate(sol,sources,labels)
    if raw is None:return None
    _,_,_,U,N=raw
    nkeys={(u['k'],u['rho'],u['q'],u['p']) for u in N}
    UC=[]
    for v in labels:
        nv={(u['k'],u['rho'],u['q'],u['p']) for u in sources if u['q'] and cg.compat(u,v)}
        if nv.issubset(nkeys):UC.append(v)
    row={}
    for v in UC:row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for u in N:row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    lhs=sum(c*sol[j] for j,c in row.items())
    if lhs<=1e-7:raise RuntimeError(f'closed Hall row not violated: {lhs}')
    sig=(tuple(sorted((v['g'],v['R'],v['x']) for v in UC)),tuple(sorted((u['k'],u['q'],u['p']) for u in N)))
    return row,lhs,sig,UC,N

def frontier_size(U,sources):
    ns=[]
    for v in U:ns.append(frozenset(i for i,u in enumerate(sources) if u['q'] and cg.compat(u,v)))
    uniq=set(ns);return len([n for n in uniq if not any(n<m for m in uniq)])

def main():
    p=argparse.ArgumentParser();p.add_argument('--demands-json',type=Path,required=True);p.add_argument('--rows',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--t',type=int,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--max-cuts',type=int,default=1000);a=p.parse_args();records=[]
    for hp,(did,total,s,rho) in enumerate(cg.load(a.demands_json,a.rows,a.t)):
        m,sources,labels=cg.build_master(a.a,a.b,a.dmax,s,rho);cuts=[];sigs=set();hall_start=len(m.ub);numerical_status=None
        for it in range(a.max_cuts):
            res=m.solve();numerical_status=res.status
            if not res.success:break
            sep=closed_separate(res.x,sources,labels)
            if sep is None:break
            row,lhs,sig,U,N=sep
            if sig in sigs:raise RuntimeError('duplicate closed Hall cut')
            sigs.add(sig);m.le(row,0);cuts.append({'iteration':it,'violation':lhs,'frontier_size':frontier_size(U,sources),'label_states':[{'g':v['g'],'s':v['s'],'R':v['R'],'x':v['x']} for v in U],'source_states':[{'k':u['k'],'rho':u['rho'],'q':u['q'],'p':u['p']} for u in N]})
        hall_end=len(m.ub);ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m);active=[]
        if cert:
            active=[{'cut_index':i-hall_start,'weight':w,'frontier_size':cuts[i-hall_start]['frontier_size']} for i,w in cert['ub'] if hall_start<=i<hall_end]
        records.append({'hard_position':hp,'demand_id':did,'s':s,'rho':rho,'closed_hall_cuts_added':len(cuts),'proof_active_closed_hall_count':len(active),'proof_active_closed_hall_cuts':active,'cuts':cuts,'numerical_status_before_exact':numerical_status,'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs']})
    out={'schema':'rz-closed-hall-cut-generation-v1','hard_rows':len(records),'exact_rejections':sum(r['rejected_exactly'] for r in records),'survivors':sum(not r['rejected_exactly'] for r in records),'cut_counts':[r['closed_hall_cuts_added'] for r in records],'proof_active_cut_counts':[r['proof_active_closed_hall_count'] for r in records],'records':records,'interpretation':'Z-free Hall projection using canonical neighbourhood-closed cuts. Exact integer-Farkas acceptance only.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:out[k] for k in ('exact_rejections','survivors','cut_counts','proof_active_cut_counts')},indent=2))
if __name__=='__main__':main()
