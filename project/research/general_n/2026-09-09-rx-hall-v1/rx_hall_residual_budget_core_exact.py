#!/usr/bin/env python3
"""Exact RX-Hall core restoring residual-column budget but eliminating Z incidence.

Source types retain only nested source/supplement transport cuts. Label types
are (R,y) with x=s+y. The exact residual budget sum R=r is restored, and
source/label compatibility uses RX1-RX3 directly. Selected incidence variables
Z are replaced by Hall capacity inequalities for unions of at most two source
neighborhoods. P transport variables, cumulative tails and unordered-pair
aggregate capacity remain absent.
"""
from collections import Counter,defaultdict
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,gzip,hashlib,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('rx_hall_exact',HERE/'rx_hall_exact.py'); ex=module_from_spec(spec); spec.loader.exec_module(ex); rx=ex.rx

def groups(v): return sorted(Counter(v).items())

def build(a,b,dmax,s,rho):
    SG=groups(rho); LG=groups(s); r=sum(rho); m=rx.LP(); ST=defaultdict(list); SA=[]
    for k,(rh,nk) in enumerate(SG):
        qmax=min(a-rh,sum(si<=rh for si in s)); norm={}
        for q in range(qmax+1):
            for p in range(min(rh+b-a-1,b-1-q)+1):
                w=m.var(('W',k,q,p)); ST[k].append((q,p,w)); norm[w]=1
                if q: SA.append((w,rh,q,p,nk))
        m.equal(norm,1)
    # Weakened nested source/supplement transport remains sufficient as a necessary condition.
    m.equal({w:nk*(q-p) for k,(rh,nk) in enumerate(SG) for q,p,w in ST[k]},0)
    for th in range(1,a+1):
        row={}
        for k,(rh,nk) in enumerate(SG):
            for q,p,w in ST[k]:
                c=(nk*q if q>=th+1 else 0)-(nk*p if rh+q>=th else 0)
                if c: row[w]=c
        m.le(row,0)
    # Label types retain R and y=x-s. Exact local feasible box from the full model.
    LT=defaultdict(list); LA=[]
    for g,(sg,ng) in enumerate(LG):
        norm={}
        for R in range(dmax-sg+1):
            for y in range(b-R-sg+1):
                x=sg+y; z=m.var(('L',g,R,y)); LT[g].append((R,y,x,z)); LA.append((z,sg,R,y,ng,x)); norm[z]=1
        m.equal(norm,1)
    residual={}
    for g,(sg,ng) in enumerate(LG):
        for R,y,x,z in LT[g]: residual[z]=residual.get(z,0)+ng*R
    m.equal(residual,r)
    total={}
    for k,(rh,nk) in enumerate(SG):
        for q,p,w in ST[k]: total[w]=total.get(w,0)+nk*q
    for g,(sg,ng) in enumerate(LG):
        for R,y,x,z in LT[g]: total[z]=total.get(z,0)-ng*x
    m.equal(total,0)
    # Exact RX1-RX3 compatibility neighborhood in (s,R,y) label-type space.
    def neigh(rh,q,p):
        return frozenset(i for i,(_,sg,R,y,_,x) in enumerate(LA)
                         if sg<=rh and R+sg<=rh+q-1 and R+x>=q+p)
    attrs=sorted(set((rh,q,p) for _,rh,q,p,_ in SA)); masks={u:neigh(*u) for u in attrs}; domains=set(masks.values())
    for i,u in enumerate(attrs):
        for v in attrs[i:]: domains.add(masks[u]|masks[v])
    domains=sorted(domains,key=lambda D:(len(D),tuple(sorted(D))))
    for D in domains:
        row={}; used=False
        for w,rh,q,p,nk in SA:
            if masks[(rh,q,p)]<=D: row[w]=row.get(w,0)+nk*q; used=True
        if not used: continue
        for i in D:
            z,sg,R,y,ng,x=LA[i]; row[z]=row.get(z,0)-ng*x
        m.le(row,0)
    ex.add_unit_density_bounds(m); m.meta={'source_attribute_types':len(attrs),'one_or_two_neighborhood_domains':len(domains)}; return m

def hard(dp,rp,t):
    D=json.loads(Path(dp).read_text()); out=[]
    for pos,line in enumerate(Path(rp).read_text().splitlines()):
        if not line.strip(): continue
        z=list(map(int,line.split())); did,total,rho=z[0],z[1],z[2:]; s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t: out.append((pos,did,total,s,rho))
    return out

def main():
    p=argparse.ArgumentParser(); p.add_argument('--demands-json',type=Path,required=True); p.add_argument('--rows',type=Path,required=True); p.add_argument('--a',type=int,required=True); p.add_argument('--b',type=int,required=True); p.add_argument('--dmax',type=int,required=True); p.add_argument('--t',type=int,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    H=hard(a.demands_json,a.rows,a.t); rec=[]; unr=[]; dc=[]
    for hp,(pos,did,total,s,rho) in enumerate(H):
        M=build(a.a,a.b,a.dmax,s,rho); cert=ex.exact_certificate(M); dc.append(M.meta['one_or_two_neighborhood_domains']); z={'hard_position':hp,'position':pos,'demand_id':did,'total':total,'s':s,'rho':rho,'metadata':M.meta,'certificate':cert}; rec.append(z)
        if cert is None: unr.append({k:z[k] for k in ('hard_position','position','demand_id','s','rho')})
    raw=(json.dumps(rec,separators=(',',':'),sort_keys=True)+'\n').encode(); gz=gzip.compress(raw,mtime=0); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_bytes(gz); rhs=[z['certificate']['rhs'] for z in rec if z['certificate']]
    R={'schema':'general-rx-hall-residual-budget-core-exact-v1','scope':{'a':a.a,'b':a.b,'dmax':a.dmax,'t':a.t},'hard_rows':len(H),'exact_integer_farkas_rejections':len(H)-len(unr),'unresolved':unr,'hall_domains_min':min(dc) if dc else None,'hall_domains_max':max(dc) if dc else None,'rhs_min':min(rhs) if rhs else None,'rhs_max':max(rhs) if rhs else None,'uses_exact_residual_budget':True,'uses_rx1_rx2_rx3_compatibility':True,'removes_Z_incidence_variables':True,'removes_P_transport_variables':True,'uses_two_neighborhood_hall':True,'uses_unordered_pair_aggregate_capacity':False,'uses_cumulative_tail_variables':False,'floating_point_is_proposal_only':True,'integer_farkas_is_acceptance':True,'json_sha256':hashlib.sha256(raw).hexdigest(),'gzip_sha256':hashlib.sha256(gz).hexdigest()}
    a.output.with_suffix(a.output.suffix+'.report.json').write_text(json.dumps(R,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in R.items() if k!='unresolved'},sort_keys=True))
    if unr: raise SystemExit(f'{len(unr)} residual-budget core rows lack exact certificates')
if __name__=='__main__': main()
