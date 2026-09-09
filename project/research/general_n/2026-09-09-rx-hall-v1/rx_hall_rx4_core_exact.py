#!/usr/bin/env python3
"""Exact RX-Hall Hall core strengthened only by the graph-level RX4 consequence.

Relative to rx_hall_t3_hall_core_exact.py this keeps the same tiny model but
replaces the selected-incidence extra-load threshold

    y >= max(0, q+p-dmax)

by the conjunction of RX3 and RX4,

    y >= max(0, q+p-dmax, p-rho+1).

No R, P or Z variables are restored. No residual budget, cumulative tails,
unordered-pair aggregate capacity, or full staircase Hall family is used.
Floating point proposes Farkas multipliers; exact integer arithmetic accepts.
"""
from collections import Counter, defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import argparse,gzip,hashlib,json

HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('rx_hall_exact',HERE/'rx_hall_exact.py')
if spec is None or spec.loader is None: raise SystemExit('cannot load rx_hall_exact.py')
ex=module_from_spec(spec); spec.loader.exec_module(ex); rx=ex.rx

def groups(vals): return sorted(Counter(vals).items())

def build(a,b,dmax,s,rho):
    assert len(s)==a and len(rho)==b and min(s)>0
    SG=groups(rho); LG=groups(s); m=rx.LP(); ST=defaultdict(list); SA=[]
    for k,(rh,nk) in enumerate(SG):
        nlabels=sum(si<=rh for si in s); norm={}; qmax=min(a-rh,nlabels)
        for q in range(qmax+1):
            pmax=min(rh+b-a-1,b-1-q)
            for p in range(pmax+1):
                # RX3: y>=q+p-dmax. RX4: y>=p-rho+1.
                h=max(0,q+p-dmax,p-rh+1)
                w=m.var(('W',k,q,p)); ST[k].append((q,p,h,w)); norm[w]=1
                if q>0: SA.append((w,rh,h,nk,q))
        m.equal(norm,1)
    bal={}
    for k,(rh,nk) in enumerate(SG):
        for q,p,h,w in ST[k]: bal[w]=nk*(q-p)
    m.equal(bal,0)
    for th in range(1,a+1):
        row={}
        for k,(rh,nk) in enumerate(SG):
            for q,p,h,w in ST[k]:
                c=(nk*q if q>=th+1 else 0)-(nk*p if rh+q>=th else 0)
                if c: row[w]=c
        m.le(row,0)
    LT=defaultdict(list); LA=[]
    for g,(sg,ng) in enumerate(LG):
        norm={}
        for y in range(b-sg+1):
            x=sg+y; z=m.var(('L',g,y)); LT[g].append((y,x,z)); LA.append((z,sg,y,ng,x)); norm[z]=1
        m.equal(norm,1)
    total={}
    for k,(rh,nk) in enumerate(SG):
        for q,p,h,w in ST[k]: total[w]=total.get(w,0)+nk*q
    for g,(sg,ng) in enumerate(LG):
        for y,x,z in LT[g]: total[z]=total.get(z,0)-ng*x
    m.equal(total,0)
    def neigh(rh,h):
        return frozenset(i for i,(_,sg,y,_,_) in enumerate(LA) if sg<=rh and y>=h)
    attrs=sorted(set((rh,h) for _,rh,h,_,_ in SA)); masks={u:neigh(*u) for u in attrs}; domains=set(masks.values())
    for i,u in enumerate(attrs):
        for v in attrs[i:]: domains.add(masks[u]|masks[v])
    domains=sorted(domains,key=lambda D:(len(D),tuple(sorted(D))))
    for D in domains:
        row={}; used=False
        for w,rh,h,nk,q in SA:
            if masks[(rh,h)]<=D: row[w]=row.get(w,0)+nk*q; used=True
        if not used: continue
        for i in D:
            z,sg,y,ng,x=LA[i]; row[z]=row.get(z,0)-ng*x
        m.le(row,0)
    ex.add_unit_density_bounds(m)
    m.meta={'source_attribute_pairs':len(attrs),'one_or_two_rectangle_domains':len(domains)}
    return m

def load_hard(dp,rp,t):
    D=json.loads(Path(dp).read_text()); out=[]
    for pos,line in enumerate(Path(rp).read_text().splitlines()):
        if not line.strip(): continue
        z=list(map(int,line.split())); did,total,rho=z[0],z[1],z[2:]; s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t: out.append((pos,did,total,s,rho))
    return out

def main():
    p=argparse.ArgumentParser(); p.add_argument('--demands-json',type=Path,required=True); p.add_argument('--rows',type=Path,required=True)
    p.add_argument('--a',type=int,required=True); p.add_argument('--b',type=int,required=True); p.add_argument('--dmax',type=int,required=True); p.add_argument('--t',type=int,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    hard=load_hard(a.demands_json,a.rows,a.t); recs=[]; unresolved=[]; nd=[]
    for hp,(pos,did,total,s,rho) in enumerate(hard):
        model=build(a.a,a.b,a.dmax,s,rho); cert=ex.exact_certificate(model); nd.append(model.meta['one_or_two_rectangle_domains'])
        r={'hard_position':hp,'position':pos,'demand_id':did,'total':total,'s':s,'rho':rho,'hall_core_metadata':model.meta,'certificate':cert}; recs.append(r)
        if cert is None: unresolved.append({k:r[k] for k in ('hard_position','position','demand_id','s','rho')})
    raw=(json.dumps(recs,separators=(',',':'),sort_keys=True)+'\n').encode(); gz=gzip.compress(raw,mtime=0); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_bytes(gz)
    rhs=[r['certificate']['rhs'] for r in recs if r['certificate']]
    report={'schema':'general-rx-hall-rx4-core-exact-v1','scope':{'a':a.a,'b':a.b,'dmax':a.dmax,'t':a.t},'hard_rows':len(hard),'exact_integer_farkas_rejections':len(hard)-len(unresolved),'unresolved':unresolved,'hall_domains_min':min(nd) if nd else None,'hall_domains_max':max(nd) if nd else None,'rhs_min':min(rhs) if rhs else None,'rhs_max':max(rhs) if rhs else None,'uses_rx1':True,'uses_rx3':True,'uses_rx4':True,'uses_rx2_via_rx4_elimination':True,'removes_R_residual_variables_and_budget':True,'removes_P_transport_variables':True,'removes_Z_incidence_variables':True,'uses_hall_unions_of_at_most_two_rectangles':True,'uses_all_staircase_hall_cuts':False,'uses_unordered_pair_aggregate_capacity':False,'uses_cumulative_tail_variables':False,'floating_point_is_proposal_only':True,'integer_farkas_is_acceptance':True,'json_sha256':hashlib.sha256(raw).hexdigest(),'gzip_sha256':hashlib.sha256(gz).hexdigest()}
    a.output.with_suffix(a.output.suffix+'.report.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in report.items() if k!='unresolved'},sort_keys=True))
    if unresolved: raise SystemExit(f'{len(unresolved)} RX4-core rows lack exact certificates')
if __name__=='__main__': main()
