#!/usr/bin/env python3
"""Exact ablation: BC staircases plus pairwise third-coordinate dominance.

Starting from the W/L master and the preserved 2D BC upper-set library, test
whether the exceptional n=30 state can be closed by either of the two pairwise
projections of the full 3D order:
  SD: (s, R+s) <= (rho, rho+q-1)
  SH: (s, -(R+x)) <= (rho, -(q+p))
or by both families together.

Pairwise upper-set cuts are separated by max-flow/min-cut and strengthened to
the ambient upward closure in the chosen two coordinates. Final rejection is
accepted only through exact integer-Farkas verification.
"""
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('cg',HERE/'rz_hall_cutgen.py');cg=module_from_spec(spec);spec.loader.exec_module(cg);ex=cg.ex

def leq(a,b): return all(x<=y for x,y in zip(a,b))

def coords(v_or_u,fam,is_source=False):
    if fam=='SD':
        return ((v_or_u['rho'],v_or_u['rho']+v_or_u['q']-1) if is_source
                else (v_or_u['s'],v_or_u['R']+v_or_u['s']))
    if fam=='SH':
        return ((v_or_u['rho'],-(v_or_u['q']+v_or_u['p'])) if is_source
                else (v_or_u['s'],-(v_or_u['R']+v_or_u['x'])))
    raise ValueError(fam)

def compat(u,v,fam): return leq(coords(v,fam),coords(u,fam,True))

def row_from_bc(cut,sources,labels):
    lm={(v['g'],v['s'],v['R'],v['x']):v for v in labels}
    sm={(u['k'],u['rho'],u['q'],u['p']):u for u in sources}
    row={}
    for z in cut['label_states']:
        v=lm[(z['g'],z['s'],z['R'],z['x'])]
        row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for z in cut['source_states']:
        u=sm[(z['k'],z['rho'],z['q'],z['p'])]
        row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    return row

def separate(sol,sources,labels,fam):
    activeL=[v for v in labels if v['n']*v['x']*sol[v['var']]>1e-9]
    activeS=[u for u in sources if u['n']*u['q']*sol[u['var']]>1e-9]
    nl,ns=len(activeL),len(activeS);S=0;lo=1;so=lo+nl;T=so+ns
    D=cg.Dinic(T+1);total=0.0
    for i,v in enumerate(activeL):
        z=v['n']*v['x']*sol[v['var']];total+=z;D.add(S,lo+i,z)
    for j,u in enumerate(activeS):D.add(so+j,T,u['n']*u['q']*sol[u['var']])
    INF=max(1.0,total+1.0)
    for i,v in enumerate(activeL):
        for j,u in enumerate(activeS):
            if compat(u,v,fam):D.add(lo+i,so+j,INF)
    val,seen=D.flow(S,T)
    if total-val<=1e-7:return None
    U=[v for i,v in enumerate(activeL) if seen[lo+i]]
    mins=[coords(v,fam) for v in U]
    UA=[v for v in labels if any(leq(y,coords(v,fam)) for y in mins)]
    N=[u for u in sources if u['q'] and any(compat(u,v,fam) for v in UA)]
    row={}
    for v in UA:row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for u in N:row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    lhs=sum(c*sol[j] for j,c in row.items())
    if lhs<=1e-7:raise RuntimeError(f'{fam} upper-set row not violated: {lhs}')
    sig=(fam,tuple(sorted((v['g'],v['R'],v['x']) for v in UA)),tuple(sorted((u['k'],u['q'],u['p']) for u in N)))
    return row,lhs,sig,UA,N

def generator_size(U,fam):
    pts=sorted(set(coords(v,fam) for v in U))
    return len([p for p in pts if not any(q!=p and leq(q,p) for q in pts)])

def solve(old,a,b,dmax,families,maxcuts):
    m,sources,labels=cg.build_master(a,b,dmax,old['s'],old['rho'])
    for c in old['cuts']:m.le(row_from_bc(c,sources,labels),0)
    pair_start=len(m.ub); cuts=[]; sigs=set(); numerical_status=None
    for it in range(maxcuts):
        res=m.solve();numerical_status=res.status
        if not res.success:break
        found=None
        for fam in families:
            sep=separate(res.x,sources,labels,fam)
            if sep is not None:
                found=(fam,sep);break
        if found is None:break
        fam,(row,lhs,sig,U,N)=found
        if sig in sigs:raise RuntimeError(f'duplicate {fam} pairwise upper-set cut')
        sigs.add(sig);m.le(row,0)
        cuts.append({'family':fam,'iteration':it,'violation':lhs,'generator_size':generator_size(U,fam)})
    pair_end=len(m.ub);ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m)
    active=[]
    if cert:
        for i,w in cert['ub']:
            if pair_start<=i<pair_end:
                c=cuts[i-pair_start];active.append({'cut_index':i-pair_start,'weight':w,'family':c['family'],'generator_size':c['generator_size']})
    return {'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs'],'pairwise_cuts_added':len(cuts),'pairwise_cut_counts':{f:sum(c['family']==f for c in cuts) for f in families},'proof_active_pairwise':active,'numerical_status_before_exact':numerical_status}

def main():
    p=argparse.ArgumentParser();p.add_argument('--bc-json',type=Path,required=True);p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True);p.add_argument('--dmax',type=int,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--max-cuts',type=int,default=1000);a=p.parse_args();H=json.loads(a.bc_json.read_text());records=[]
    modes={'BC':(), 'BC+SD':('SD',), 'BC+SH':('SH',), 'BC+SD+SH':('SD','SH')}
    for old in H['records']:
        rec={'hard_position':old['hard_position'],'demand_id':old['demand_id'],'modes':{}}
        for name,fams in modes.items():
            if not fams:
                # Reuse known exact BC status from source checkpoint.
                rec['modes'][name]={'rejected_exactly':bool(old['rejected_exactly']),'pairwise_cuts_added':0}
            else:
                rec['modes'][name]=solve(old,a.a,a.b,a.dmax,fams,a.max_cuts)
        records.append(rec)
    summary={name:{'exact_rejections':sum(r['modes'][name]['rejected_exactly'] for r in records),'rejected_positions':[r['hard_position'] for r in records if r['modes'][name]['rejected_exactly']]} for name in modes}
    out={'schema':'rz-bc-plus-pairwise-dominance-v1','source_checkpoint':str(a.bc_json),'summary':summary,'records':records,'interpretation':'Exact ablation of whether BC 2D staircases plus SD and/or SH pairwise upper-set dominance suffice. No full 3D upper sets are added.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,indent=2,sort_keys=True))
if __name__=='__main__':main()
