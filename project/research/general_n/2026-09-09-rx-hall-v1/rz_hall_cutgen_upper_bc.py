#!/usr/bin/env python3
"""Two-dimensional ambient upper-set Hall separation for the BC transport slice.

The inherited W/L master, source q-domain, residual budget and source threshold
constraints are unchanged. Only source-label transport compatibility uses
  d=R+s <= alpha=rho+q-1
  h=R+x >= beta=q+p
so in coordinates Y=(d,-h), X=(alpha,-beta) the transport relation is Y<=X.
This intentionally omits the edge condition s<=rho, matching the earlier BC
compatibility ablation. Final rejection is accepted only by exact integer
Farkas verification.
"""
from collections import deque
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('cg',HERE/'rz_hall_cutgen.py');cg=module_from_spec(spec);spec.loader.exec_module(cg);ex=cg.ex

def ycoord(v):return (v['R']+v['s'],-(v['R']+v['x']))
def xcoord(u):return (u['rho']+u['q']-1,-(u['q']+u['p']))
def leq(a,b):return all(x<=y for x,y in zip(a,b))
def compat(u,v):return leq(ycoord(v),xcoord(u))

def separate(sol,sources,labels):
    activeL=[v for v in labels if v['n']*v['x']*sol[v['var']]>1e-9]
    activeS=[u for u in sources if u['n']*u['q']*sol[u['var']]>1e-9]
    nl,ns=len(activeL),len(activeS);S=0;lo=1;so=lo+nl;T=so+ns;D=cg.Dinic(T+1);total=0.0
    for i,v in enumerate(activeL):
        z=v['n']*v['x']*sol[v['var']];total+=z;D.add(S,lo+i,z)
    for j,u in enumerate(activeS):D.add(so+j,T,u['n']*u['q']*sol[u['var']])
    INF=max(1.0,total+1.0)
    for i,v in enumerate(activeL):
        for j,u in enumerate(activeS):
            if compat(u,v):D.add(lo+i,so+j,INF)
    val,seen=D.flow(S,T)
    if total-val<=1e-7:return None
    U=[v for i,v in enumerate(activeL) if seen[lo+i]]
    N=[u for u in sources if u['q'] and any(compat(u,v) for v in U)]
    return U,N

def generator_size(U):
    pts=sorted(set(ycoord(v) for v in U))
    return len([p for p in pts if not any(q!=p and leq(q,p) for q in pts)])

def upward_separate(sol,sources,labels):
    raw=separate(sol,sources,labels)
    if raw is None:return None
    U,N=raw;mins=[ycoord(v) for v in U];UA=[v for v in labels if any(leq(y,ycoord(v)) for y in mins)]
    row={}
    for v in UA:row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for u in N:row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    lhs=sum(c*sol[j] for j,c in row.items())
    if lhs<=1e-7:raise RuntimeError(f'BC upper-set row not violated: {lhs}')
    sig=(tuple(sorted((v['g'],v['R'],v['x']) for v in UA)),tuple(sorted((u['k'],u['q'],u['p']) for u in N)))
    return row,lhs,sig,UA,N

def main():
    p=argparse.ArgumentParser();p.add_argument('--demands-json',type=Path,required=True);p.add_argument('--rows',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--t',type=int,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--max-cuts',type=int,default=1000);a=p.parse_args();records=[]
    for hp,(did,total,s,rho) in enumerate(cg.load(a.demands_json,a.rows,a.t)):
        m,sources,labels=cg.build_master(a.a,a.b,a.dmax,s,rho);cuts=[];sigs=set();hall_start=len(m.ub);numerical_status=None
        for it in range(a.max_cuts):
            res=m.solve();numerical_status=res.status
            if not res.success:break
            sep=upward_separate(res.x,sources,labels)
            if sep is None:break
            row,lhs,sig,U,N=sep
            if sig in sigs:raise RuntimeError('duplicate BC upper-set cut')
            sigs.add(sig);m.le(row,0);cuts.append({'iteration':it,'violation':lhs,'generator_size':generator_size(U),'label_states':[{'g':v['g'],'s':v['s'],'R':v['R'],'x':v['x']} for v in U],'source_states':[{'k':u['k'],'rho':u['rho'],'q':u['q'],'p':u['p']} for u in N]})
        hall_end=len(m.ub);ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m);active=[]
        if cert:active=[{'cut_index':i-hall_start,'weight':w,'generator_size':cuts[i-hall_start]['generator_size']} for i,w in cert['ub'] if hall_start<=i<hall_end]
        records.append({'hard_position':hp,'demand_id':did,'s':s,'rho':rho,'bc_upper_cuts_added':len(cuts),'proof_active_bc_upper_count':len(active),'proof_active_bc_upper_cuts':active,'cuts':cuts,'numerical_status_before_exact':numerical_status,'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs']})
    out={'schema':'rz-bc-ambient-upper-cut-generation-v1','hard_rows':len(records),'exact_rejections':sum(r['rejected_exactly'] for r in records),'survivors':sum(not r['rejected_exactly'] for r in records),'rejected_positions':[r['hard_position'] for r in records if r['rejected_exactly']],'cut_counts':[r['bc_upper_cuts_added'] for r in records],'proof_active_cut_counts':[r['proof_active_bc_upper_count'] for r in records],'records':records,'interpretation':'2D ambient upper-set/stochastic-dominance projection for B+C transport only; inherited source q-domain is retained. Exact integer-Farkas acceptance only.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:out[k] for k in ('exact_rejections','survivors','rejected_positions','cut_counts','proof_active_cut_counts')},indent=2))
if __name__=='__main__':main()
