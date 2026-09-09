#!/usr/bin/env python3
"""Exact compatibility-edge ablation for the stripped n=30 R+Z transport core.

The source-group-cap inequalities are absent throughout.  The only changes
between modes are which of the three graph-derived conditions are required for
a Z transport edge:
  A: s <= rho
  B: R+s <= rho+q-1       (RX2-type upper threshold)
  C: R+x >= q+p           (RX3-type lower threshold)
All other constraints, including the inherited source-state q-domain, exact
residual budget, q/p balance, threshold transport and unit bounds, are fixed.
"""
from collections import Counter,defaultdict
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('rx_hall_exact',HERE/'rx_hall_exact.py'); ex=module_from_spec(spec); spec.loader.exec_module(ex); rx=ex.rx
MODES={
 'ABC':(1,1,1),'BC':(0,1,1),'AC':(1,0,1),'AB':(1,1,0),
 'A':(1,0,0),'B':(0,1,0),'C':(0,0,1),'NONE':(0,0,0)
}
def groups(v): return sorted(Counter(v).items())
def build(a,b,dmax,s,rho,mode):
    useA,useB,useC=MODES[mode]; SG=groups(rho); LG=groups(s); r=sum(rho); m=rx.LP(); ST=defaultdict(list)
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
            if useA and sg>rh: continue
            for q,p,w in ST[k]:
                if q==0: continue
                for R,x,lvar in LT[g]:
                    if useB and R+sg>rh+q-1: continue
                    if useC and R+x<q+p: continue
                    z=m.var(('Z',k,g,q,p,R,x)); by_source[k,q,p,g].append(z); by_label[g,R,x].append((k,z))
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
    ex.add_unit_density_bounds(m); return m

def load(dp,rp,t):
    D=json.loads(Path(dp).read_text()); out=[]
    for line in Path(rp).read_text().splitlines():
        if not line.strip(): continue
        z=list(map(int,line.split())); did,total,rho=z[0],z[1],z[2:]; s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t: out.append((did,total,s,rho))
    return out

def main():
    p=argparse.ArgumentParser(); p.add_argument('--demands-json',type=Path,required=True); p.add_argument('--rows',type=Path,required=True); p.add_argument('--a',type=int,required=True); p.add_argument('--b',type=int,required=True); p.add_argument('--dmax',type=int,required=True); p.add_argument('--t',type=int,required=True); p.add_argument('--mode',choices=MODES,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    rec=[]
    for hp,(did,total,s,rho) in enumerate(load(a.demands_json,a.rows,a.t)):
        m=build(a.a,a.b,a.dmax,s,rho,a.mode); cert=ex.exact_certificate(m)
        rec.append({'hard_position':hp,'demand_id':did,'rejected_exactly':cert is not None,'certificate_rhs':None if cert is None else cert['rhs']})
    out={'schema':'rz-compatibility-edge-ablation-v1','mode':a.mode,'conditions':{'A_s_le_rho':bool(MODES[a.mode][0]),'B_R_plus_s_upper':bool(MODES[a.mode][1]),'C_R_plus_x_lower':bool(MODES[a.mode][2])},'hard_rows':len(rec),'exact_rejections':sum(x['rejected_exactly'] for x in rec),'survivors':sum(not x['rejected_exactly'] for x in rec),'records':rec,'interpretation':'Only Z-edge compatibility conditions are ablated. Source-group caps remain deleted. Survivors are relaxation states, not graphs.'}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
