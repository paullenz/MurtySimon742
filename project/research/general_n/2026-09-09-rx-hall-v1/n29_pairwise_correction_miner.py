#!/usr/bin/env python3
"""Mine BC/SH upper-set corrections atop the boundary-specialised n30 dictionary.

Scope: the 38 n29 t=2 profiles preserved after deleting unreachable d=11 BC
generators. Build the same W/L source-threshold/residual-budget master used by
the pairwise programme, add the specialised 6 BC + 3 SH Hall inequalities,
then separate violated ambient upper sets in either BC=(d,-h) or SH=(s,-h)
coordinates. At each iteration add the more violated available family.

Final rejection is accepted only through the existing exact integer-Farkas
checker (with explicit unit-density bounds at the acceptance step). The mined
shapes are finite research evidence, not a universal theorem.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cg',HERE/'rz_hall_cutgen.py');cg=module_from_spec(sp);sp.loader.exec_module(cg);ex=cg.ex

def leq(a,b):return all(x<=y for x,y in zip(a,b))
def min_gens(points):
    pts=sorted(set(tuple(p) for p in points))
    return tuple(p for p in pts if not any(q!=p and leq(q,p) for q in pts))
def inside(pt,gens):return any(leq(g,pt) for g in gens)
def coords_label(v,fam):
    h=v['R']+v['x']
    return (v['R']+v['s'],-h) if fam=='BC' else (v['s'],-h)
def coords_source(u,fam):
    beta=u['q']+u['p']
    return (u['rho']+u['q']-1,-beta) if fam=='BC' else (u['rho'],-beta)
def compat(u,v,fam):return leq(coords_label(v,fam),coords_source(u,fam))

def shape_row(sources,labels,gens,fam):
    row={}
    for v in labels:
        if inside(coords_label(v,fam),gens):row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for u in sources:
        if u['q'] and inside(coords_source(u,fam),gens):row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    return row

def separate(sol,sources,labels,fam):
    activeL=[v for v in labels if v['n']*v['x']*sol[v['var']]>1e-9]
    activeS=[u for u in sources if u['n']*u['q']*sol[u['var']]>1e-9]
    nl,ns=len(activeL),len(activeS);S=0;lo=1;so=lo+nl;T=so+ns;D=cg.Dinic(T+1);total=0.0
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
    raw=min_gens(coords_label(v,fam) for v in U)
    UA=[v for v in labels if inside(coords_label(v,fam),raw)]
    N=[u for u in sources if u['q'] and any(compat(u,v,fam) for v in UA)]
    row={}
    for v in UA:row[v['var']]=row.get(v['var'],0)+v['n']*v['x']
    for u in N:row[u['var']]=row.get(u['var'],0)-u['n']*u['q']
    lhs=sum(c*sol[j] for j,c in row.items())
    if lhs<=1e-7:raise RuntimeError((fam,'nonpositive strengthened violation',lhs))
    return {'family':fam,'row':row,'violation':lhs,'generators':raw}

def trim_bc(g,dmax):return min_gens(p for p in g if p[0]<=dmax)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--max-cuts',type=int,default=300);z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text());J=json.loads(z.support_json.read_text());targets=B['trimmed_survivor_records'];base_bc=[trim_bc(tuple(tuple(p) for p in x['generators']),z.dmax) for x in J['active_BC']];base_sh=[tuple(tuple(p) for p in x['generators']) for x in J['active_SH']]
    rec=[];all_new=set()
    for old in targets:
        m,sources,labels=cg.build_master(z.a,z.b,z.dmax,old['s'],old['rho'])
        for g in base_bc:m.le(shape_row(sources,labels,g,'BC'),0)
        for g in base_sh:m.le(shape_row(sources,labels,g,'SH'),0)
        new_start=len(m.ub);cuts=[];sigs=set();termination=None
        for it in range(z.max_cuts):
            sol=m.solve()
            if not sol.success:termination='numerically_infeasible';break
            opts=[x for x in (separate(sol.x,sources,labels,'BC'),separate(sol.x,sources,labels,'SH')) if x is not None]
            if not opts:termination='pairwise_feasible_no_violated_upper_set';break
            q=max(opts,key=lambda x:x['violation']);sig=(q['family'],q['generators'])
            if sig in sigs:raise RuntimeError(('duplicate cut',sig))
            sigs.add(sig);m.le(q['row'],0);cuts.append({'iteration':it,'family':q['family'],'violation':q['violation'],'generators':[list(p) for p in q['generators']]});all_new.add(sig)
        else:termination='cut_limit'
        new_end=len(m.ub);ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m);active=[]
        if cert:
            for i,w in cert['ub']:
                if new_start<=i<new_end:
                    c=cuts[i-new_start];active.append({'cut_index':i-new_start,'weight':w,'family':c['family'],'generators':c['generators']})
        rec.append({'hard_position':old['hard_position'],'demand_id':old['demand_id'],'s':old['s'],'rho':old['rho'],'termination':termination,'new_cuts_added':len(cuts),'new_BC':sum(c['family']=='BC' for c in cuts),'new_SH':sum(c['family']=='SH' for c in cuts),'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs'],'proof_active_new':active,'cuts':cuts})
    pooled={}
    for r in rec:
        for c in r['proof_active_new']:
            key=(c['family'],tuple(tuple(p) for p in c['generators']))
            pooled.setdefault(key,{'family':c['family'],'generators':c['generators'],'profiles':0,'total_weight':0})
            pooled[key]['profiles']+=1;pooled[key]['total_weight']+=c['weight']
    pool=sorted(pooled.values(),key=lambda x:(-x['profiles'],-x['total_weight'],x['family'],x['generators']))
    out={'schema':'n29-pairwise-correction-miner-v1','scope':{'a':z.a,'b':z.b,'dmax':z.dmax,'profiles':len(rec)},'base_support':{'BC':[[list(p) for p in g] for g in base_bc],'SH':[[list(p) for p in g] for g in base_sh]},'exact_rejections':sum(r['rejected_exactly'] for r in rec),'pairwise_survivors':sum(not r['rejected_exactly'] for r in rec),'termination_counts':{k:sum(r['termination']==k for r in rec) for k in sorted(set(r['termination'] for r in rec))},'distinct_proof_active_new_shapes':len(pool),'pooled_proof_active_new_shapes':pool,'records':rec,'integer_farkas_acceptance':True,'floating_separation_proposal_only':True,'interpretation':'Mines BC/SH ambient upper-set corrections atop the boundary-specialised nine-shape dictionary on the 38 n29 transfer survivors. Exact Farkas acceptance only; finite evidence, not a theorem.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('records','pooled_proof_active_new_shapes','base_support')},indent=2,sort_keys=True));print('top pooled',json.dumps(pool[:20],indent=2,sort_keys=True))
if __name__=='__main__':main()
