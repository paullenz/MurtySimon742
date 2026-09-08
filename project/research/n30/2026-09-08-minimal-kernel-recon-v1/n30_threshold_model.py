"""Standalone cumulative-threshold/source-flow relaxation for n=30, Delta=16.

Fresh parameterisation of the corrected n=29 v2 model at a=13,b=16.  It does
not import the historical n=29 v1/v2 builders.  Every actual graph satisfying
the standalone bridge maps to a feasible point of this relaxation.
"""
from collections import defaultdict
from functools import reduce
from math import gcd
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix,vstack,hstack,csr_matrix

A=13;B=16;DMAX=11

class Model:
    def __init__(self):self.names=[];self.eq=[];self.ub=[];self.bound_start=None
    def var(self,n):self.names.append(n);return len(self.names)-1
    def equal(self,d,b=0):self.eq.append(({j:c for j,c in d.items() if c},b))
    def le(self,d,b):self.ub.append(({j:c for j,c in d.items() if c},b))
    def arrays(self):
        def mat(rows):
            rr=[];cc=[];vv=[]
            for i,(d,b) in enumerate(rows):
                for j,x in d.items():rr.append(i);cc.append(j);vv.append(x)
            return coo_matrix((vv,(rr,cc)),shape=(len(rows),len(self.names))).tocsr(),np.array([b for d,b in rows],float)
        X,b=mat(self.ub);E,f=mat(self.eq);return X,b,E,f
    def solve(self):
        X,b,E,f=self.arrays();return linprog(np.zeros(len(self.names)),A_ub=X,b_ub=b,A_eq=E,b_eq=f,bounds=(0,None),method='highs')

def add(d,j,c=1):d[j]=d.get(j,0)+c
def groups(vals):
    d=defaultdict(int)
    for x in vals:d[x]+=1
    return sorted(d.items())

def build(s,rho,t):
    assert len(s)==A and len(rho)==B
    r=sum(rho);LG=groups(s);SG=groups(rho);m=Model()
    Y={};T={};label_opts=defaultdict(list)
    W={};source_types=defaultdict(list)

    # Label option fractions and cumulative selected-degree tails.  T is a
    # fraction of the whole equal-demand group, exactly as in corrected n29 v2.
    for g,(sg,ng) in enumerate(LG):
        norm={}
        for d in range(DMAX+1):
            for R in range(B+1):
                if sg>0 and d-R!=sg:continue
                if sg==0 and d>R:continue
                U=B-R
                if U<sg or d>R+U:continue
                y=m.var(('Y',g,d,R));Y[g,d,R]=y;label_opts[g].append((d,R,y,U));norm[y]=1
                prev=y
                for h in range(1,U+1):
                    th=m.var(('T',g,d,R,h));T[g,d,R,h]=th
                    m.le({th:1,prev:-1},0)
                    if h<=sg:m.equal({th:1,y:-1},0)
                    prev=th
        m.equal(norm,1)
    ed={};er={}
    for (g,d,R),y in Y.items():
        ng=LG[g][1];add(ed,y,ng*d);add(er,y,ng*R)
    m.equal(ed,2*(r+t));m.equal(er,r)

    # Actual source types. General bounds specialise to p<=rho+B-A-1=rho+2.
    for k,(rh,nk) in enumerate(SG):
        norm={}
        for q in range(A-rh+1):
            for p in range(min(rh+B-A-1,B-1-q)+1):
                w=m.var(('W',k,q,p));W[k,q,p]=w;source_types[k].append((q,p,w));norm[w]=1
        m.equal(norm,1)

    # Averaged selected source->supplement flow.
    P_out=defaultdict(list);P_in=defaultdict(list);P_pair=defaultdict(list)
    for k,(rhk,nk) in enumerate(SG):
        qks=sorted({q for q,p,w in source_types[k] if q>0})
        for l,(rhl,nl) in enumerate(SG):
            if k==l and nk<2:continue
            qls=sorted({q for q,p,w in source_types[l]})
            for q in qks:
                for q2 in qls:
                    if rhl+q2<q-1:continue
                    z=m.var(('P',k,l,q,q2))
                    P_out[k,q].append((l,z));P_in[l,q2].append((k,z));P_pair[min(k,l),max(k,l)].append((k,l,z))
    for k,(rh,nk) in enumerate(SG):
        for q in sorted({qq for qq,p,w in source_types[k] if qq>0}):
            e={}
            for qq,p,w in source_types[k]:
                if qq==q:add(e,w,-q)
            for l,z in P_out[k,q]:add(e,z,SG[l][1]-(k==l))
            m.equal(e,0)
    for l,(rh,nl) in enumerate(SG):
        for q2 in sorted({qq for qq,p,w in source_types[l]}):
            e={}
            for qq,p,w in source_types[l]:
                if qq==q2:add(e,w,-p)
            for k,z in P_in[l,q2]:add(e,z,SG[k][1]-(k==l))
            m.equal(e,0)
    for key,items in P_pair.items():
        e={}
        for kk,ll,z in items:add(e,z,1)
        m.le(e,1)  # same-group exact graph bound is <=1/2; <=1 is a safe relaxation

    # Selected source-label incidence density.
    by_source=defaultdict(list);by_label=defaultdict(list)
    for k,(rh,nk) in enumerate(SG):
        for g,(sg,ng) in enumerate(LG):
            for q,p,w in source_types[k]:
                if q==0:continue
                for d,R,y,U in label_opts[g]:
                    req=max(1,q+p-R)
                    if sg>rh or d>rh+R or d>rh+q-1 or req>U:continue
                    z=m.var(('Z',k,g,q,p,d,R))
                    by_source[k,q,p,g].append((d,R,z));by_label[g,d,R].append((k,q,p,z))
    for k,(rh,nk) in enumerate(SG):
        for q,p,w in source_types[k]:
            e={w:-q}
            for g,(sg,ng) in enumerate(LG):
                cap={w:-1}
                for d,R,z in by_source[k,q,p,g]:add(cap,z,1);add(e,z,ng)
                m.le(cap,0)
            m.equal(e,0)

    for g,(sg,ng) in enumerate(LG):
        for d,R,y,U in label_opts[g]:
            items=by_label[g,d,R]
            total={}
            for k,q,p,z in items:add(total,z,SG[k][1])
            e=dict(total)
            # Correct per-label identity: sum_k n_k Z = E[x] = sum_h T_h.
            for h in range(1,U+1):add(e,T[g,d,R,h],-1)
            m.equal(e,0)
            # Nested capacity for selected incidences requiring x>=h.
            for h in range(1,U+1):
                e={}
                for k,q,p,z in items:
                    if max(1,q+p-R)>=h:add(e,z,SG[k][1])
                add(e,T[g,d,R,h],-(h-1))
                for hh in range(h,U+1):add(e,T[g,d,R,hh],-1)
                m.le(e,0)

    m.bound_start=len(m.ub)
    for j in range(len(m.names)):m.le({j:1},1)
    return m

def exact_certificate(m):
    X,b,E,f=m.arrays();N=len(m.names);nu=len(m.ub);ne=len(m.eq)
    D=hstack([-X.T,-E.T,E.T],format='csr')
    D=vstack([D,csr_matrix(np.r_[b,f,-f].reshape(1,-1))],format='csr')
    rhs=np.r_[np.zeros(N),-1.0]
    res=linprog(np.ones(nu+2*ne),A_ub=D,b_ub=rhs,bounds=(0,None),method='highs')
    if not res.success:return None
    for scale in (1000,1000000,1000000000):
        lam=[max(0,round(float(x)*scale)) for x in res.x[:nu]]
        mu=[round(float(x-y)*scale) for x,y in zip(res.x[nu:nu+ne],res.x[nu+ne:])]
        coef=[0]*N;rhsval=0
        for rows,weights in ((m.ub,lam),(m.eq,mu)):
            for (row,rhs0),w in zip(rows,weights):
                if not w:continue
                rhsval+=w*rhs0
                for j,c in row.items():coef[j]+=w*c
        for j,c in enumerate(coef):
            if c<0:
                lam[m.bound_start+j]-=c;rhsval-=c;coef[j]=0
        if rhsval<0:
            factor=reduce(gcd,lam+[abs(x) for x in mu]) or 1
            cert={'ub':[(i,w//factor) for i,w in enumerate(lam) if w],
                  'eq':[(i,w//factor) for i,w in enumerate(mu) if w],
                  'rhs':rhsval//factor,'variables':N,'inequalities':nu,'equalities':ne}
            verify_certificate(m,cert);return cert
    return None

def verify_certificate(m,c):
    assert c['variables']==len(m.names) and c['inequalities']==len(m.ub) and c['equalities']==len(m.eq)
    coef=[0]*len(m.names);rhs=0
    for rows,weights,nonneg in ((m.ub,c['ub'],True),(m.eq,c['eq'],False)):
        seen=set()
        for i,w in weights:
            assert i not in seen and 0<=i<len(rows) and isinstance(w,int) and (not nonneg or w>=0)
            seen.add(i);row,b=rows[i];rhs+=w*b
            for j,a in row.items():coef[j]+=w*a
    assert min(coef)>=0 and rhs==c['rhs'] and rhs<0
    return rhs
