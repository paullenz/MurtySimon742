#!/usr/bin/env python3
"""Mine semantic row-family support from exact R+Z Farkas certificates.

This reconstructs the residual-budget + source-label-incidence relaxation with
semantic tags on every equality/inequality, proposes and exactly verifies the
same integer Farkas certificates, then aggregates nonzero multiplier support by
constraint family. It is a research diagnostic, not a new theorem.
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
    eqtags=[]; ubtags=[]
    def EQ(row,bv,tag): m.equal(row,bv); eqtags.append(tag)
    def LE(row,bv,tag): m.le(row,bv); ubtags.append(tag)
    for k,(rh,nk) in enumerate(SG):
        qmax=min(a-rh,sum(si<=rh for si in s)); norm={}
        for q in range(qmax+1):
            for p in range(min(rh+b-a-1,b-1-q)+1):
                w=m.var(('W',k,q,p)); ST[k].append((q,p,w)); norm[w]=1
        EQ(norm,1,('source_norm',rh,nk))
    EQ({w:nk*(q-p) for k,(rh,nk) in enumerate(SG) for q,p,w in ST[k]},0,('qp_balance',))
    for th in range(1,a+1):
        row={}
        for k,(rh,nk) in enumerate(SG):
            for q,p,w in ST[k]:
                c=(nk*q if q>=th+1 else 0)-(nk*p if rh+q>=th else 0)
                if c: row[w]=c
        LE(row,0,('transport_threshold',th))
    LT=defaultdict(list)
    for g,(sg,ng) in enumerate(LG):
        norm={}
        for R in range(dmax-sg+1):
            for x in range(sg,b-R+1):
                z=m.var(('L',g,R,x)); LT[g].append((R,x,z)); norm[z]=1
        EQ(norm,1,('label_norm',sg,ng))
    residual={}
    for g,(sg,ng) in enumerate(LG):
        for R,x,z in LT[g]: residual[z]=ng*R
    EQ(residual,r,('residual_budget',r))
    by_source=defaultdict(list); by_label=defaultdict(list)
    for k,(rh,nk) in enumerate(SG):
        for g,(sg,ng) in enumerate(LG):
            if sg>rh: continue
            for q,p,w in ST[k]:
                if q==0: continue
                for R,x,lvar in LT[g]:
                    if R+sg>rh+q-1 or R+x<q+p: continue
                    z=m.var(('Z',k,g,q,p,R,x)); by_source[k,q,p,g].append(z); by_label[g,R,x].append((k,z))
    for k,(rh,nk) in enumerate(SG):
        for q,p,w in ST[k]:
            total={w:-q}
            for g,(sg,ng) in enumerate(LG):
                cap={w:-1}
                for z in by_source[k,q,p,g]:
                    cap[z]=cap.get(z,0)+1; total[z]=total.get(z,0)+ng
                LE(cap,0,('source_group_cap',rh,nk,q,p,sg,ng))
            EQ(total,0,('source_total',rh,nk,q,p))
    for g,(sg,ng) in enumerate(LG):
        for R,x,lvar in LT[g]:
            row={lvar:-x}
            for k,z in by_label[g,R,x]: row[z]=row.get(z,0)+SG[k][1]
            EQ(row,0,('label_incidence',sg,ng,R,x))
    bound_start=len(m.ub)
    ex.add_unit_density_bounds(m)
    for j in range(len(m.names)): ubtags.append(('unit_bound',m.names[j][0] if isinstance(m.names[j],tuple) else 'var'))
    assert len(eqtags)==len(m.eq) and len(ubtags)==len(m.ub)
    m.semantic_eqtags=eqtags; m.semantic_ubtags=ubtags; m.bound_start=bound_start
    return m

def load(dp,rp,t):
    D=json.loads(Path(dp).read_text()); out=[]
    for pos,line in enumerate(Path(rp).read_text().splitlines()):
        if not line.strip(): continue
        z=list(map(int,line.split())); did,total,rho=z[0],z[1],z[2:]; s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t: out.append((pos,did,total,s,rho))
    return out

def fam(tag): return tag[0]

def main():
    p=argparse.ArgumentParser(); p.add_argument('--demands-json',type=Path,required=True); p.add_argument('--rows',type=Path,required=True); p.add_argument('--a',type=int,required=True); p.add_argument('--b',type=int,required=True); p.add_argument('--dmax',type=int,required=True); p.add_argument('--t',type=int,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    records=[]; aggregate=defaultdict(lambda:{'certificates_using':0,'nonzero_rows':0,'abs_weight':0})
    for hp,(pos,did,total,s,rho) in enumerate(load(a.demands_json,a.rows,a.t)):
        m=build(a.a,a.b,a.dmax,s,rho); cert=ex.exact_certificate(m)
        if cert is None: raise SystemExit(f'no exact R+Z certificate for hard row {hp}')
        per=defaultdict(lambda:{'rows':0,'abs_weight':0,'tags':[]})
        for i,w in cert['ub']:
            tag=m.semantic_ubtags[i]; f=fam(tag); per[f]['rows']+=1; per[f]['abs_weight']+=abs(w); per[f]['tags'].append({'tag':list(tag),'weight':w})
        for i,w in cert['eq']:
            tag=m.semantic_eqtags[i]; f=fam(tag); per[f]['rows']+=1; per[f]['abs_weight']+=abs(w); per[f]['tags'].append({'tag':list(tag),'weight':w})
        for f,z in per.items(): aggregate[f]['certificates_using']+=1; aggregate[f]['nonzero_rows']+=z['rows']; aggregate[f]['abs_weight']+=z['abs_weight']
        records.append({'hard_position':hp,'demand_id':did,'s':s,'rho':rho,'rhs':cert['rhs'],'families':dict(per)})
    out={'schema':'rz-certificate-semantic-mining-v1','hard_rows':len(records),'aggregate':dict(aggregate),'records':records,'interpretation':'Nonzero exact Farkas multiplier support by semantic constraint family. Large weights are scale-dependent; repeated family/tag support is the useful signal.'}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({'hard_rows':len(records),'aggregate':dict(aggregate)},indent=2,sort_keys=True))
if __name__=='__main__': main()
