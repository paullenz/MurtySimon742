#!/usr/bin/env python3
"""Exact ablation of the n=30 R+Z core with source-group caps removed.

Keeps source/label state normalisation, q/p balance, threshold transport,
exact residual budget, Z compatibility support, source-total incidence,
label-incidence equalities and unit bounds. Deletes ONLY the inequalities
limiting a source-state to at most one actual label from each demand group.

The output records exact integer-Farkas rejection versus genuine relaxation
survival for the seven residual-budget hard states. Research diagnostic only.
"""
from collections import Counter,defaultdict
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('rx_hall_exact',HERE/'rx_hall_exact.py'); ex=module_from_spec(spec); spec.loader.exec_module(ex); rx=ex.rx

def groups(v): return sorted(Counter(v).items())

def build(a,b,dmax,s,rho):
    SG=groups(rho); LG=groups(s); r=sum(rho); m=rx.LP(); ST=defaultdict(list)
    for k,(rh,nk) in enumerate(SG):
        qmax=min(a-rh,sum(si<=rh for si in s)); norm={}
        for q in range(qmax+1):
            for p in range(min(rh+b-a-1,b-1-q)+1):
                w=m.var(('W',k,q,p)); ST[k].append((q,p,w)); norm[w]=1
        m.equal(norm,1)
    m.equal({w:nk*(q-p) for k,(rh,nk) in enumerate(SG) for q,p,w in ST[k]},0)
    for th in range(1,a+1):
        row={}
        for k,(rh,nk) in enumerate(SG):
            for q,p,w in ST[k]:
                c=(nk*q if q>=th+1 else 0)-(nk*p if rh+q>=th else 0)
                if c: row[w]=c
        m.le(row,0)
    LT=defaultdict(list)
    for g,(sg,ng) in enumerate(LG):
        norm={}
        for R in range(dmax-sg+1):
            for x in range(sg,b-R+1):
                z=m.var(('L',g,R,x)); LT[g].append((R,x,z)); norm[z]=1
        m.equal(norm,1)
    m.equal({z:ng*R for g,(sg,ng) in enumerate(LG) for R,x,z in LT[g]},r)
    by_source=defaultdict(list); by_label=defaultdict(list)
    for k,(rh,nk) in enumerate(SG):
        for g,(sg,ng) in enumerate(LG):
            if sg>rh: continue
            for q,p,w in ST[k]:
                if q==0: continue
                for R,x,lvar in LT[g]:
                    if R+sg>rh+q-1 or R+x<q+p: continue
                    z=m.var(('Z',k,g,q,p,R,x)); by_source[k,q,p,g].append(z); by_label[g,R,x].append((k,z))
    # Deliberately NO per-demand-group source capacity inequalities here.
    for k,(rh,nk) in enumerate(SG):
        for q,p,w in ST[k]:
            total={w:-q}
            for g,(sg,ng) in enumerate(LG):
                for z in by_source[k,q,p,g]: total[z]=total.get(z,0)+ng
            m.equal(total,0)
    for g,(sg,ng) in enumerate(LG):
        for R,x,lvar in LT[g]:
            row={lvar:-x}
            for k,z in by_label[g,R,x]: row[z]=row.get(z,0)+SG[k][1]
            m.equal(row,0)
    ex.add_unit_density_bounds(m)
    return m

def load(dp,rp,t):
    D=json.loads(Path(dp).read_text()); out=[]
    for line in Path(rp).read_text().splitlines():
        if not line.strip(): continue
        z=list(map(int,line.split())); did,total,rho=z[0],z[1],z[2:]; s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t: out.append((did,total,s,rho))
    return out

def main():
    p=argparse.ArgumentParser(); p.add_argument('--demands-json',type=Path,required=True); p.add_argument('--rows',type=Path,required=True); p.add_argument('--a',type=int,required=True); p.add_argument('--b',type=int,required=True); p.add_argument('--dmax',type=int,required=True); p.add_argument('--t',type=int,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    rec=[]
    for hp,(did,total,s,rho) in enumerate(load(a.demands_json,a.rows,a.t)):
        m=build(a.a,a.b,a.dmax,s,rho); cert=ex.exact_certificate(m)
        rec.append({'hard_position':hp,'demand_id':did,'s':s,'rho':rho,'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs']})
    out={'schema':'rz-no-source-group-cap-ablation-v1','scope':{'a':a.a,'b':a.b,'dmax':a.dmax,'t':a.t},'hard_rows':len(rec),'exact_rejections':sum(x['rejected_exactly'] for x in rec),'survivors':sum(not x['rejected_exactly'] for x in rec),'records':rec,'interpretation':'Deletes only per-demand-group source capacity inequalities from the exact R+Z model. A survivor is a relaxation state, not a graph.'}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
