#!/usr/bin/env python3
"""Exact RX-Hall ablation retaining residual budget R and incidence Z, omitting P.

Keeps source-type W distributions, global/nested necessary transport cuts,
label (R,x) distributions with exact residual budget, and the original grouped
source-label Z incidence equations including per-demand-group unit capacity.
Exact source/supplement P transport, cumulative tails and unordered-pair
aggregate capacity are omitted. Thus this is a relaxation of the full stripped
RX-Hall model and is suitable for sound rejection tests.
"""
from collections import Counter,defaultdict
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,gzip,hashlib,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('rx_hall_exact',HERE/'rx_hall_exact.py'); ex=module_from_spec(spec); spec.loader.exec_module(ex); rx=ex.rx

def groups(v): return sorted(Counter(v).items())

def build(a,b,dmax,s,rho):
    SG=groups(rho); LG=groups(s); r=sum(rho); m=rx.LP(); ST=defaultdict(list)
    # Source types.
    for k,(rh,nk) in enumerate(SG):
        qmax=min(a-rh,sum(si<=rh for si in s)); norm={}
        for q in range(qmax+1):
            pmax=min(rh+b-a-1,b-1-q)
            for p in range(pmax+1):
                w=m.var(('W',k,q,p)); ST[k].append((q,p,w)); norm[w]=1
        m.equal(norm,1)
    # Necessary transport projection only; exact P variables omitted.
    m.equal({w:nk*(q-p) for k,(rh,nk) in enumerate(SG) for q,p,w in ST[k]},0)
    for th in range(1,a+1):
        row={}
        for k,(rh,nk) in enumerate(SG):
            for q,p,w in ST[k]:
                c=(nk*q if q>=th+1 else 0)-(nk*p if rh+q>=th else 0)
                if c: row[w]=c
        m.le(row,0)

    # Label types (R,x), positive demand fixes d=R+s.
    LT=defaultdict(list)
    for g,(sg,ng) in enumerate(LG):
        norm={}
        for R in range(dmax-sg+1):
            for x in range(sg,b-R+1):
                z=m.var(('L',g,R,x)); LT[g].append((R,x,z)); norm[z]=1
        m.equal(norm,1)
    residual={}
    for g,(sg,ng) in enumerate(LG):
        for R,x,z in LT[g]: residual[z]=ng*R
    m.equal(residual,r)

    # Original grouped selected source-label incidence Z.
    by_source=defaultdict(list); by_label=defaultdict(list)
    for k,(rh,nk) in enumerate(SG):
        for g,(sg,ng) in enumerate(LG):
            if sg>rh: continue
            for q,p,w in ST[k]:
                if q==0: continue
                for R,x,lvar in LT[g]:
                    if R+sg>rh+q-1: continue
                    if R+x<q+p: continue
                    z=m.var(('Z',k,g,q,p,R,x))
                    by_source[k,q,p,g].append(z); by_label[g,R,x].append((k,z))
    for k,(rh,nk) in enumerate(SG):
        for q,p,w in ST[k]:
            total={w:-q}
            for g,(sg,ng) in enumerate(LG):
                cap={w:-1}
                for z in by_source[k,q,p,g]:
                    cap[z]=cap.get(z,0)+1
                    total[z]=total.get(z,0)+ng
                m.le(cap,0)
            m.equal(total,0)
    for g,(sg,ng) in enumerate(LG):
        for R,x,lvar in LT[g]:
            row={lvar:-x}
            for k,z in by_label[g,R,x]: row[z]=row.get(z,0)+SG[k][1]
            m.equal(row,0)
    ex.add_unit_density_bounds(m)
    m.meta={'uses_exact_residual_budget':True,'uses_Z_incidence':True,'uses_exact_P_transport':False}
    return m

def hard(dp,rp,t):
    D=json.loads(Path(dp).read_text()); out=[]
    for pos,line in enumerate(Path(rp).read_text().splitlines()):
        if not line.strip(): continue
        z=list(map(int,line.split())); did,total,rho=z[0],z[1],z[2:]; s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t: out.append((pos,did,total,s,rho))
    return out

def main():
    p=argparse.ArgumentParser(); p.add_argument('--demands-json',type=Path,required=True); p.add_argument('--rows',type=Path,required=True); p.add_argument('--a',type=int,required=True); p.add_argument('--b',type=int,required=True); p.add_argument('--dmax',type=int,required=True); p.add_argument('--t',type=int,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    H=hard(a.demands_json,a.rows,a.t); rec=[]; unr=[]
    for hp,(pos,did,total,s,rho) in enumerate(H):
        M=build(a.a,a.b,a.dmax,s,rho); cert=ex.exact_certificate(M)
        z={'hard_position':hp,'position':pos,'demand_id':did,'total':total,'s':s,'rho':rho,'certificate':cert}; rec.append(z)
        if cert is None: unr.append({k:z[k] for k in ('hard_position','position','demand_id','s','rho')})
    raw=(json.dumps(rec,separators=(',',':'),sort_keys=True)+'\n').encode(); gz=gzip.compress(raw,mtime=0); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_bytes(gz)
    rhs=[z['certificate']['rhs'] for z in rec if z['certificate']]
    R={'schema':'general-rx-hall-rz-core-exact-v1','scope':{'a':a.a,'b':a.b,'dmax':a.dmax,'t':a.t},'hard_rows':len(H),'exact_integer_farkas_rejections':len(H)-len(unr),'unresolved':unr,'rhs_min':min(rhs) if rhs else None,'rhs_max':max(rhs) if rhs else None,'uses_exact_residual_budget':True,'uses_Z_incidence':True,'removes_P_transport_variables':True,'uses_unordered_pair_aggregate_capacity':False,'uses_cumulative_tail_variables':False,'floating_point_is_proposal_only':True,'integer_farkas_is_acceptance':True,'json_sha256':hashlib.sha256(raw).hexdigest(),'gzip_sha256':hashlib.sha256(gz).hexdigest()}
    a.output.with_suffix(a.output.suffix+'.report.json').write_text(json.dumps(R,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in R.items() if k!='unresolved'},sort_keys=True))
    if unr: raise SystemExit(f'{len(unr)} R+Z rows lack exact certificates')
if __name__=='__main__': main()
