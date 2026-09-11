#!/usr/bin/env python3
"""Exact microstate -> fresh n=30 grouped late-LP regression.

Independent graph-level aggregation into Y/T/W/P/Z, evaluated with Fraction
arithmetic against the separately written n30_threshold_model.py production
builder. Fixtures test the averaging layer, not existence of critical graphs.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import json, sys

HERE=Path(__file__).resolve().parent
PROD=HERE.parent.parent / '2026-09-08-minimal-kernel-recon-v1'
sys.path.insert(0,str(PROD))
import n30_threshold_model as prod  # noqa:E402

A,B=13,16

def balanced(rowdeg,avoid=frozenset(),offset=0):
    col=[0]*A; E=[]
    for u,deg in enumerate(rowdeg):
        cand=[i for i in range(A) if (u,i) not in avoid]
        cand.sort(key=lambda i:(col[i],(i-u-offset)%A))
        assert len(cand)>=deg
        for i in cand[:deg]: col[i]+=1;E.append((u,i))
    assert len(E)==len(set(E));return E

def fixture(kind):
    if kind=='uniform-rho':
        rho=[4]*B;qtar=[4]*B;s=[1]*12+[0]
    elif kind=='mixed':
        rho=[3]*8+[4]*8;qtar=[4]*8+[3]*8;s=[1]*6+[0]*7
    else: raise ValueError(kind)
    arcs=[];seen=set()
    for u,q in enumerate(qtar):
        for z in range(1,q+1):
            w=(u+z)%B
            assert (u,w) not in seen and (w,u) not in seen
            seen.add((u,w));arcs.append((u,w))
    q=[0]*B;p=[0]*B
    for u,w in arcs:q[u]+=1;p[w]+=1
    sel=balanced(q,offset=0);res=balanced(rho,frozenset(sel),5)
    assert not(set(sel)&set(res))
    x=[0]*A;R=[0]*A
    for _,i in sel:x[i]+=1
    for _,i in res:R[i]+=1
    d=[R[i]+s[i] for i in range(A)]
    assert all(0<=d[i]<=11 and x[i]<=B-R[i] for i in range(A))
    r=sum(rho);assert sum(d)%2==0;t=sum(d)//2-r
    assert sum(R)==r
    for u,w in arcs: assert rho[w]+q[w]>=q[u]-1
    for u in range(B):
        assert q[u]+rho[u]<=A
        assert p[u]<=rho[u]+2
        assert q[u]+p[u]<=B-1
    for u,i in sel:
        assert s[i]<=rho[u]
        assert d[i]<=rho[u]+R[i]
        assert d[i]<=rho[u]+q[u]-1
        assert R[i]+x[i]>=q[u]+p[u]
    return dict(kind=kind,rho=rho,q=q,p=p,s=s,R=R,x=x,d=d,selected=sel,pair_arcs=arcs,t=t)

def groups(vals):
    c=Counter(vals);vals2=sorted(c);idx={v:j for j,v in enumerate(vals2)}
    return idx,{idx[v]:c[v] for v in vals2}

def aggregate(f):
    go,ng=groups(f['s']);ko,nk=groups(f['rho']);v=defaultdict(Fraction)
    for i in range(A):
        g=go[f['s'][i]];d,R,x=f['d'][i],f['R'][i],f['x'][i]
        v[('Y',g,d,R)]+=Fraction(1,ng[g])
        for h in range(1,B-R+1):
            if x>=h:v[('T',g,d,R,h)]+=Fraction(1,ng[g])
    for u in range(B):
        k=ko[f['rho'][u]];v[('W',k,f['q'][u],f['p'][u])]+=Fraction(1,nk[k])
    for u,w in f['pair_arcs']:
        k,l=ko[f['rho'][u]],ko[f['rho'][w]];den=nk[k]*(nk[l]-(k==l));assert den>0
        v[('P',k,l,f['q'][u],f['q'][w])]+=Fraction(1,den)
    for u,i in f['selected']:
        k,g=ko[f['rho'][u]],go[f['s'][i]]
        v[('Z',k,g,f['q'][u],f['p'][u],f['d'][i],f['R'][i])]+=Fraction(1,nk[k]*ng[g])
    return dict(v)

def evaluate(m,a):
    names=set(m.names);missing=[(n,str(x)) for n,x in a.items() if x and n not in names]
    assert not missing,missing
    x=[a.get(n,Fraction(0)) for n in m.names];assert all(0<=z<=1 for z in x)
    eq=[];ub=[]
    for j,(row,rhs) in enumerate(m.eq):
        lhs=sum(Fraction(c)*x[i] for i,c in row.items())
        if lhs!=rhs:eq.append((j,str(lhs),str(rhs)))
    for j,(row,rhs) in enumerate(m.ub):
        lhs=sum(Fraction(c)*x[i] for i,c in row.items())
        if lhs>rhs:ub.append((j,str(lhs),str(rhs)))
    return dict(variables=len(m.names),equalities=len(m.eq),inequalities=len(m.ub),eq_bad=eq,ub_bad=ub)

def run(kind):
    f=fixture(kind);r=evaluate(prod.build(f['s'],f['rho'],f['t']),aggregate(f))
    assert not r['eq_bad'] and not r['ub_bad'],r
    return {'fixture':kind,'t':f['t'],'demand_groups':sorted(Counter(f['s']).items()),
      'residual_groups':sorted(Counter(f['rho']).items()),'selected_pair_arcs':len(f['pair_arcs']),
      'selected_cross_edges':len(f['selected']),'corrected_n30':{'variables':r['variables'],
      'equalities':r['equalities'],'inequalities':r['inequalities'],'violations':0}}

def main():
    R={'schema':'n30-late-lp-microstate-embedding-audit-v1','status':'PASS','fixtures':[run('uniform-rho'),run('mixed')],
       'all_production_rows_satisfied':True,'external_independence':False,
       'note':'Exact rational normalization regression only; fixtures are not asserted critical graphs.'}
    (HERE/'MICROSTATE_AUDIT_REPORT.json').write_text(json.dumps(R,indent=2)+'\n')
    print(json.dumps(R,indent=2))
if __name__=='__main__':main()
