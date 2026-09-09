#!/usr/bin/env python3
"""Exact RX4 Hall core using the full union-closure of compatibility rectangles.

This is the next ablation after the two-rectangle RX4 core. It still removes
all R, P and Z variables, the residual budget, cumulative tails and unordered-
pair aggregate capacity. The only change is that Hall domains are the complete
finite union-closure of source compatibility rectangles rather than unions of
at most two rectangles.
"""
from collections import Counter,defaultdict
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,gzip,hashlib,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('rx_hall_exact',HERE/'rx_hall_exact.py'); ex=module_from_spec(spec); spec.loader.exec_module(ex); rx=ex.rx

def groups(v): return sorted(Counter(v).items())

def build(a,b,dmax,s,rho):
    SG=groups(rho); LG=groups(s); m=rx.LP(); ST=defaultdict(list); SA=[]
    for k,(rh,nk) in enumerate(SG):
        qmax=min(a-rh,sum(si<=rh for si in s)); norm={}
        for q in range(qmax+1):
            for p in range(min(rh+b-a-1,b-1-q)+1):
                h=max(0,q+p-dmax,p-rh+1); w=m.var(('W',k,q,p)); ST[k].append((q,p,h,w)); norm[w]=1
                if q: SA.append((w,rh,h,nk,q))
        m.equal(norm,1)
    m.equal({w:nk*(q-p) for k,(rh,nk) in enumerate(SG) for q,p,h,w in ST[k]},0)
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
    tot={}
    for k,(rh,nk) in enumerate(SG):
        for q,p,h,w in ST[k]: tot[w]=tot.get(w,0)+nk*q
    for g,(sg,ng) in enumerate(LG):
        for y,x,z in LT[g]: tot[z]=tot.get(z,0)-ng*x
    m.equal(tot,0)
    def neigh(rh,h): return frozenset(i for i,(_,sg,y,_,_) in enumerate(LA) if sg<=rh and y>=h)
    attrs=sorted(set((rh,h) for _,rh,h,_,_ in SA)); masks={u:neigh(*u) for u in attrs}
    # Exact finite union-closure of all source neighborhoods.
    domains={frozenset()}
    for u in attrs:
        M=masks[u]; domains |= {D|M for D in list(domains)}
    domains.discard(frozenset()); domains=sorted(domains,key=lambda D:(len(D),tuple(sorted(D))))
    for D in domains:
        row={}; used=False
        for w,rh,h,nk,q in SA:
            if masks[(rh,h)]<=D: row[w]=row.get(w,0)+nk*q; used=True
        if not used: continue
        for i in D:
            z,sg,y,ng,x=LA[i]; row[z]=row.get(z,0)-ng*x
        m.le(row,0)
    ex.add_unit_density_bounds(m); m.meta={'source_attribute_pairs':len(attrs),'full_staircase_domains':len(domains)}; return m

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
        M=build(a.a,a.b,a.dmax,s,rho); cert=ex.exact_certificate(M); dc.append(M.meta['full_staircase_domains']); z={'hard_position':hp,'position':pos,'demand_id':did,'total':total,'s':s,'rho':rho,'hall_core_metadata':M.meta,'certificate':cert}; rec.append(z)
        if cert is None: unr.append({k:z[k] for k in ('hard_position','position','demand_id','s','rho')})
    raw=(json.dumps(rec,separators=(',',':'),sort_keys=True)+'\n').encode(); gz=gzip.compress(raw,mtime=0); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_bytes(gz); rhs=[z['certificate']['rhs'] for z in rec if z['certificate']]
    R={'schema':'general-rx-hall-rx4-staircase-exact-v1','scope':{'a':a.a,'b':a.b,'dmax':a.dmax,'t':a.t},'hard_rows':len(H),'exact_integer_farkas_rejections':len(H)-len(unr),'unresolved':unr,'hall_domains_min':min(dc) if dc else None,'hall_domains_max':max(dc) if dc else None,'rhs_min':min(rhs) if rhs else None,'rhs_max':max(rhs) if rhs else None,'uses_rx1':True,'uses_rx3':True,'uses_rx4':True,'uses_full_staircase_hall_closure':True,'removes_R_P_Z':True,'uses_unordered_pair_aggregate_capacity':False,'uses_cumulative_tail_variables':False,'floating_point_is_proposal_only':True,'integer_farkas_is_acceptance':True,'json_sha256':hashlib.sha256(raw).hexdigest(),'gzip_sha256':hashlib.sha256(gz).hexdigest()}
    a.output.with_suffix(a.output.suffix+'.report.json').write_text(json.dumps(R,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in R.items() if k!='unresolved'},sort_keys=True))
    if unr: raise SystemExit(f'{len(unr)} staircase-core rows lack exact certificates')
if __name__=='__main__': main()
