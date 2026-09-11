#!/usr/bin/env python3
"""Solver-free verification of four n=30, Delta=16, m=225 zero-demand R-core certificates.

The mathematical input is ledger tightness: when S=r+2t and s_i=max(0,d_i-R_i),
all d_i-R_i are nonnegative. Hence d_i=R_i+s_i even for s_i=0, so the same
(R,y) label-state model used in the positive-demand residual-budget Hall core
is valid for the four zero-demand tight profiles.

This checker reconstructs each grouped necessary-condition model using integer
coefficients only and verifies a preserved nonnegative integer Farkas ray.
No LP/MIP solver and no floating point are used.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from pathlib import Path
import argparse, json

A=13; B=16; DMAX=11

class LP:
    def __init__(self):
        self.names=[]; self.ub=[]; self.bu=[]; self.eq=[]; self.be=[]
    def var(self,name):
        self.names.append(name); return len(self.names)-1
    def le(self,row,rhs):
        self.ub.append({j:int(v) for j,v in row.items() if v}); self.bu.append(int(rhs))
    def equal(self,row,rhs=0):
        self.eq.append({j:int(v) for j,v in row.items() if v}); self.be.append(int(rhs))

def groups(vals): return sorted(Counter(vals).items())

def build(s,rho):
    assert len(s)==A and len(rho)==B and sum(s)==sum(rho)+2
    SG=groups(rho); LG=groups(s); r=sum(rho); m=LP(); ST=defaultdict(list); SA=[]
    for k,(rh,nk) in enumerate(SG):
        qmax=min(A-rh,sum(si<=rh for si in s)); norm={}
        for q in range(qmax+1):
            for p in range(min(rh+B-A-1,B-1-q)+1):
                w=m.var(('W',k,q,p)); ST[k].append((q,p,w)); norm[w]=1
                if q: SA.append((w,rh,q,p,nk))
        m.equal(norm,1)
    m.equal({w:nk*(q-p) for k,(rh,nk) in enumerate(SG) for q,p,w in ST[k]},0)
    for th in range(1,A+1):
        row={}
        for k,(rh,nk) in enumerate(SG):
            for q,p,w in ST[k]:
                c=(nk*q if q>=th+1 else 0)-(nk*p if rh+q>=th else 0)
                if c: row[w]=c
        m.le(row,0)

    LT=defaultdict(list); LA=[]
    for g,(sg,ng) in enumerate(LG):
        norm={}
        # Ledger tightness gives d=R+s for s=0 as well as s>0.
        for R in range(DMAX-sg+1):
            for y in range(B-R-sg+1):
                x=sg+y; z=m.var(('L',g,R,y)); LT[g].append((R,y,x,z))
                LA.append((z,sg,R,y,ng,x)); norm[z]=1
        m.equal(norm,1)

    m.equal({z:ng*R for g,(sg,ng) in enumerate(LG) for R,y,x,z in LT[g]},r)
    total={}
    for k,(rh,nk) in enumerate(SG):
        for q,p,w in ST[k]: total[w]=total.get(w,0)+nk*q
    for g,(sg,ng) in enumerate(LG):
        for R,y,x,z in LT[g]: total[z]=total.get(z,0)-ng*x
    m.equal(total,0)

    def neigh(rh,q,p):
        return frozenset(i for i,(_,sg,R,y,_,x) in enumerate(LA)
                         if sg<=rh and R+sg<=rh+q-1 and R+x>=q+p)
    attrs=sorted(set((rh,q,p) for _,rh,q,p,_ in SA)); masks={u:neigh(*u) for u in attrs}
    domains=set(masks.values())
    for i,u in enumerate(attrs):
        for v in attrs[i:]: domains.add(masks[u]|masks[v])
    domains=sorted(domains,key=lambda D:(len(D),tuple(sorted(D))))
    for D in domains:
        row={}; used=False
        for w,rh,q,p,nk in SA:
            if masks[(rh,q,p)]<=D:
                row[w]=row.get(w,0)+nk*q; used=True
        if not used: continue
        for i in D:
            z,sg,R,y,ng,x=LA[i]; row[z]=row.get(z,0)-ng*x
        m.le(row,0)

    # Unit-density bounds x<=1 are valid for the grouped density variables.
    for j in range(len(m.names)): m.le({j:1},1)
    return m,{'attrs':len(attrs),'domains':len(domains),'labels':len(LA)}

def verify(m,cert):
    assert cert['variables']==len(m.names)
    assert cert['inequalities']==len(m.ub)
    assert cert['equalities']==len(m.eq)
    coef=[0]*len(m.names); rhs=0; seen=set()
    for i,w in cert['ub']:
        assert i not in seen and 0<=i<len(m.ub) and isinstance(w,int) and w>=0; seen.add(i)
        rhs += w*m.bu[i]
        for j,a in m.ub[i].items(): coef[j]+=w*a
    seen=set()
    for i,w in cert['eq']:
        assert i not in seen and 0<=i<len(m.eq) and isinstance(w,int); seen.add(i)
        rhs += w*m.be[i]
        for j,a in m.eq[i].items(): coef[j]+=w*a
    assert min(coef)>=0
    assert rhs==cert['rhs'] and rhs<0
    return rhs

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--certificates',type=Path,default=Path(__file__).with_name('N30_M225_ZERO_DEMAND_RCORE_CERTS.json'))
    ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    records=json.loads(a.certificates.read_text()); assert len(records)==4
    rows=[]
    for rec in records:
        m,meta=build(rec['s'],rec['rho']); assert meta==rec['meta']; rhs=verify(m,rec['cert'])
        rows.append({'s':rec['s'],'rho':rec['rho'],'variables':len(m.names),'inequalities':len(m.ub),'equalities':len(m.eq),'certificate_rhs':rhs,'certificate_support':len(rec['cert']['ub'])+len(rec['cert']['eq']),'metadata':meta})
    out={'schema':'n30-m225-zero-demand-r-core-exact-v1','status':'PASS','solver_used':False,'floating_point_used':False,'rows':rows,'conclusion':'Ledger tightness extends d=R+s to the zero-demand labels, and all four zero-demand tight rows are exactly Farkas-rejected by the residual-budget two-neighborhood Hall core.'}
    text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if a.output:a.output.write_text(text)
    print(text,end='')
if __name__=='__main__':main()
