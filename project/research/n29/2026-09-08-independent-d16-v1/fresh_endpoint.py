#!/usr/bin/env python3
"""Independent strongest endpoint LP and exact integer Farkas checker for N=29 D16.
No inherited project modules are imported. Requires SciPy only for proposing duals.
"""
from collections import defaultdict
from scipy.optimize import linprog
from scipy.sparse import coo_matrix,hstack,vstack,csr_matrix
import numpy as np

class Model:
    def __init__(self):self.map={};self.names=[];self.ub=[];self.eq=[];self.bound_start=None
    def var(self,n):
        n=tuple(n)
        if n not in self.map:self.map[n]=len(self.names);self.names.append(n)
        return self.map[n]
    def row(self,label,terms,rhs,eq=False):
        d={}
        for k,v in terms.items():
            j=k if isinstance(k,int) else self.var(k)
            if v:d[j]=d.get(j,0)+int(v)
        (self.eq if eq else self.ub).append((label,{j:v for j,v in d.items() if v},int(rhs)))
    def matrices(self):
        def mk(rows):
            rr=[];cc=[];vv=[];bb=[]
            for i,(_,d,b) in enumerate(rows):
                bb.append(float(b))
                for j,v in d.items():rr.append(i);cc.append(j);vv.append(float(v))
            return coo_matrix((vv,(rr,cc)),shape=(len(rows),len(self.names))).tocsr(),np.array(bb)
        A,b=mk(self.ub);E,f=mk(self.eq);return A,b,E,f
    def solve(self):
        A,b,E,f=self.matrices();return linprog(np.zeros(len(self.names)),A_ub=A,b_ub=b,A_eq=E,b_eq=f,bounds=(0,None),method='highs')
    def bounds(self):
        self.bound_start=len(self.ub)
        for j,n in enumerate(list(self.names)):self.row('B:'+repr(n),{j:1},1)

def add(*parts):
    z={}
    for c,d in parts:
        for k,v in d.items():z[k]=z.get(k,0)+c*v
    return {k:v for k,v in z.items() if v}
def sc(d,c):return {k:c*v for k,v in d.items()}
def groups(keys):
    out=[]
    for i,k in enumerate(keys):
        for old,ids in out:
            if old==k:ids.append(i);break
        else:out.append((k,[i]))
    return [x for _,x in out]
def partition(s,rho,st):
    L=groups([(s[i],tuple(st['domains'][i]),st['forced'][i]) for i in range(len(s))])
    B=groups([(rho[u],st['c'][u],tuple(f>>u&1 for f in st['forced'])) for u in range(len(rho))])
    return L,B

def build(s,rho,st,t):
    a=len(s);b=len(rho);r=sum(rho);L,B=partition(s,rho,st);m=Model()
    Y={};D={};R={};F={};S={};T={};IF={};ARC={};INC={}
    for g,G in enumerate(L):
        i=G[0];D[g]={};R[g]={};norm={}
        for o,(d,rr,z) in enumerate(st['domains'][i]):
            n=('y',g,o);m.var(n);Y[g,o]=n;norm[n]=1;D[g][n]=d;R[g][n]=rr
        m.row(f'yn:{g}',norm,1,True)
    m.row('Rsum',add(*[(len(L[g]),R[g]) for g in range(len(L))]),r,True)
    m.row('Dsum',add(*[(len(L[g]),D[g]) for g in range(len(L))]),2*(r+t),True)
    for g in range(len(L)):
        for h in range(g,len(L)):
            if g==h and len(L[g])<2:continue
            n=('F',g,h);m.var(n);F[g,h]=n;m.row(f'Fb:{g}:{h}',{n:1},1)
    for g in range(len(L)):
        e=sc(D[g],-1)
        for h in range(len(L)):
            if g==h and len(L[g])<2:continue
            n=F[min(g,h),max(g,h)];e[n]=e.get(n,0)+len(L[h])-(g==h)
        m.row(f'Fd:{g}',e,0,True)
    for k,U in enumerate(B):
        u=U[0];f=sum(x>>u&1 for x in st['forced'])
        for g,G in enumerate(L):
            i=G[0];S[k,g]={};T[k,g]={};mand=bool(st['forced'][i]>>u&1)
            for o,(d,rr,z) in enumerate(st['domains'][i]):
                q=max(1,f,d-rho[u]+1);supp=any(w!=u and not(st['forced'][i]>>w&1) and d<=rho[u]+rho[w] and rho[w]+st['c'][w]>=q-1 for w in range(b))
                ps=rho[u]>=s[i] and st['c'][u]>=q and supp and rr+max(1,s[i])<=b;pr=not mand and rr>0;pn=not mand and d+f<=a-1 and rr+s[i]<=b-1
                e={Y[g,o]:-1}
                if ps:n=('sel',k,g,o);m.var(n);S[k,g][n]=1;e[n]=1
                if pr:n=('res',k,g,o);m.var(n);T[k,g][n]=1;e[n]=1
                m.row(f'st:{k}:{g}:{o}',e,0,not pn)
            if mand:m.row(f'mand:{k}:{g}',S[k,g],1,True)
        m.row(f'rr:{k}',add(*[(len(L[g]),T[k,g]) for g in range(len(L))]),rho[u],True)
        m.row(f'qc:{k}',add(*[(len(L[g]),S[k,g]) for g in range(len(L))]),st['c'][u])
    for g,G in enumerate(L):
        e=dict(R[g])
        for k in range(len(B)):
            for n,v in T[k,g].items():e[n]=e.get(n,0)-len(B[k])*v
        m.row(f'Rc:{g}',e,0,True)
        m.row(f'xs:{g}',add(*[(-len(B[k]),S[k,g]) for k in range(len(B))]),-s[G[0]])
    for (g,h),ff in F.items():
        for k in range(len(B)):
            m.row(f'Fsel:{g}:{h}:{k}:0',add((1,{ff:1}),(1,S[k,g]),(-1,S[k,h]),(-1,T[k,h])),1)
            if g!=h:m.row(f'Fsel:{g}:{h}:{k}:1',add((1,{ff:1}),(1,S[k,h]),(-1,S[k,g]),(-1,T[k,g])),1)
    for k,U in enumerate(B):
        u=U[0];q=add(*[(len(L[g]),S[k,g]) for g in range(len(L))])
        for g,G in enumerate(L):
            md=max(x[0] for x in st['domains'][G[0]]);M=max(0,md-rho[u]+1);m.row(f'ql:{k}:{g}',add((1,D[g]),(-1,q),(M,S[k,g])),rho[u]-1+M)
            M=max(0,md+st['c'][u]-a+1);m.row(f'md:{k}:{g}',add((1,D[g]),(1,q),(-M,S[k,g]),(-M,T[k,g])),a-1)
    m.row('Qcap',add(*[(len(B[k])*len(L[g]),S[k,g]) for k in range(len(B)) for g in range(len(L))]),r+(b-a-1)*b)
    for k in range(len(B)):
        for (g,h),ff in F.items():
            n=('if',k,g,h);m.var(n);IF[k,g,h]=n;m.row(f'ifd:{k}:{g}:{h}',add((1,{ff:1}),(-1,{n:1}),(1,S[k,g]),(1,S[k,h])),2)
        for g in range(len(L)):
            e=sc(R[g],-1)
            for h in range(len(L)):
                if g==h and len(L[g])<2:continue
                n=IF[k,min(g,h),max(g,h)];e[n]=e.get(n,0)+len(L[h])-(g==h)
            m.row(f'ifR:{k}:{g}',e,0)
    for k,U in enumerate(B):
        u=U[0];f=sum(x>>u&1 for x in st['forced'])
        for l,V in enumerate(B):
            w=V[0]
            if k==l and len(U)<2:continue
            for g,G in enumerate(L):
                i=G[0];dm=min(x[0] for x in st['domains'][i]);q=max(1,f,dm-rho[u]+1)
                if s[i]>rho[u] or dm>rho[u]+rho[w] or st['forced'][i]>>w&1 or q>st['c'][u] or q-1>rho[w]+st['c'][w]:continue
                n=('arc',k,l,g);m.var(n);ARC[k,l,g]=n
    for k in range(len(B)):
        for g in range(len(L)):
            e=sc(S[k,g],-1)
            for l in range(len(B)):
                if (k,l,g) in ARC:e[ARC[k,l,g]]=e.get(ARC[k,l,g],0)+len(B[l])-(k==l)
            m.row(f'ao:{k}:{g}',e,0,True)
    for k,U in enumerate(B):
        e={}
        for l in range(len(B)):
            for g in range(len(L)):
                if (l,k,g) in ARC:e[ARC[l,k,g]]=e.get(ARC[l,k,g],0)+(len(B[l])-(k==l))*len(L[g])
        INC[k]=e;m.row(f'inc:{k}',e,rho[U[0]]+b-a-1)
    for k in range(len(B)):
        for l in range(k,len(B)):
            if k==l and len(B[k])<2:continue
            e={}
            for g in range(len(L)):
                if (k,l,g) in ARC:e[ARC[k,l,g]]=e.get(ARC[k,l,g],0)+len(L[g])
                if (l,k,g) in ARC:e[ARC[l,k,g]]=e.get(ARC[l,k,g],0)+len(L[g])
            m.row(f'pi:{k}:{l}',e,1)
    for (k,l,g),v in ARC.items():
        m.row(f'ae:{k}:{l}:{g}',add((1,{v:1}),(1,S[l,g]),(1,T[l,g])),1)
        for h in range(len(L)):
            if h==g and len(L[h])<2:continue
            m.row(f'an:{k}:{l}:{g}:{h}',add((1,{v:1}),(1,S[k,h]),(-1,S[l,h]),(-1,T[l,h])),1)
            m.row(f'af:{k}:{l}:{g}:{h}',add((1,{v:1}),(1,{F[min(g,h),max(g,h)]:1}),(1,S[k,h]),(-1,T[l,h])),2)
    for k in range(len(B)):
        q=add(*[(len(L[g]),S[k,g]) for g in range(len(L))])
        for g in range(len(L)):
            m.row(f'el:{k}:{g}',add((1,q),(1,INC[k]),(b-1,S[k,g]),(-1,R[g]),*[(-len(B[l]),S[l,g]) for l in range(len(B))]),b-1)
    DEG={};RNG={}
    for k,U in enumerate(B):
        u=U[0];lo=sum(x>>u&1 for x in st['forced']);RNG[k]=range(lo,st['c'][u]+1)
        for q in RNG[k]:n=('deg',k,q);m.var(n);DEG[k,q]=n
        m.row(f'dn:{k}',{DEG[k,q]:1 for q in RNG[k]},1,True)
        for g,G in enumerate(L):
            i=G[0];mand=bool(st['forced'][i]>>u&1)
            for q in RNG[k]:
                e={DEG[k,q]:-1}
                for o,(d,rr,z) in enumerate(st['domains'][i]):
                    sup=sum(1 for w in range(b) if w!=u and not(st['forced'][i]>>w&1) and d<=rho[u]+rho[w] and q<=rho[w]+st['c'][w]+1)
                    al={'ts':q>=1 and s[i]<=rho[u] and d+1<=rho[u]+q and sup>0 and rr+max(1,s[i])<=b,'tr':not mand and rr>=1,'tm':not mand and d+q<=a-1 and rr+s[i]<=b-1}
                    for kind,ok in al.items():
                        if ok:n=(kind,k,g,o,q);m.var(n);e[n]=1
                m.row(f'tc:{k}:{g}:{q}',e,0,True)
            for o in range(len(st['domains'][i])):
                e={Y[g,o]:-1}
                for q in RNG[k]:
                    for kind in ('ts','tr','tm'):
                        n=(kind,k,g,o,q)
                        if n in m.map:e[n]=e.get(n,0)+1
                m.row(f'to:{k}:{g}:{o}',e,0,True)
                for kind,old in [('ts','sel'),('tr','res')]:
                    e={};oldn=(old,k,g,o)
                    if oldn in m.map:e[oldn]=-1
                    for q in RNG[k]:
                        n=(kind,k,g,o,q)
                        if n in m.map:e[n]=e.get(n,0)+1
                    m.row(f'tm:{kind}:{k}:{g}:{o}',e,0,True)
        for q in RNG[k]:
            for kind,target in [('ts',q),('tr',rho[u])]:
                e={DEG[k,q]:-target}
                for g,G in enumerate(L):
                    for o in range(len(st['domains'][G[0]])):
                        n=(kind,k,g,o,q)
                        if n in m.map:e[n]=e.get(n,0)+len(G)
                m.row(f'tn:{kind}:{k}:{q}',e,0,True)
    PAIR={}
    for k,U in enumerate(B):
        for l,V in enumerate(B):
            if k==l and len(U)<2:continue
            for q in RNG[k]:
                if not q:continue
                for v in RNG[l]:
                    if q-1<=rho[V[0]]+v:n=('pt',k,l,q,v);m.var(n);PAIR[k,l,q,v]=n
    for k,U in enumerate(B):
        for l,V in enumerate(B):
            if k==l and len(U)<2:continue
            e={n:1 for (kk,ll,q,v),n in PAIR.items() if (kk,ll)==(k,l)}
            for g in range(len(L)):
                n=('arc',k,l,g)
                if n in m.map:e[n]=e.get(n,0)-len(L[g])
            m.row(f'pa:{k}:{l}',e,0,True)
        for q in RNG[k]:
            e={DEG[k,q]:-q}
            for (kk,l,qq,v),n in PAIR.items():
                if kk==k and qq==q:e[n]=e.get(n,0)+len(B[l])-(k==l)
            m.row(f'po:{k}:{q}',e,0,True)
            e={DEG[k,q]:-(rho[U[0]]+b-a-1)}
            for (l,kk,v,qq),n in PAIR.items():
                if kk==k and qq==q:e[n]=e.get(n,0)+len(B[l])-(k==l)
            m.row(f'pn:{k}:{q}',e,0)
    for (k,q),w in DEG.items():
        u=B[k][0];rd={w:-r};dd={w:-2*(r+t)};rs={w:-(r-rho[u])};ds={w:-(rho[u]*(2*a-rho[u]-3+q)-2*t)}
        for n in list(m.map):
            if n and n[0] in ('ts','tr','tm') and n[1]==k and n[4]==q:
                _,_,g,o,_=n;d,rr,z=st['domains'][L[g][0]][o];N=len(L[g]);rd[n]=rd.get(n,0)+N*rr;dd[n]=dd.get(n,0)+N*d
                if n[0]=='ts':rs[n]=rs.get(n,0)+N*rr;ds[n]=ds.get(n,0)+N*d
        m.row(f'cr:{k}:{q}',rd,0,True);m.row(f'cd:{k}:{q}',dd,0,True);m.row(f'csr:{k}:{q}',rs,0);m.row(f'csd:{k}:{q}',ds,0)
    CX={};QP={};Z={}
    for g,G in enumerate(L):
        i=G[0];fc=st['forced'][i].bit_count()
        for o,(d,rr,z) in enumerate(st['domains'][i]):
            e={Y[g,o]:-1}
            for x in range(max(s[i],fc),b-rr+1):n=('cx',g,o,x);m.var(n);CX[g,o,x]=n;e[n]=1
            m.row(f'cx:{g}:{o}',e,0,True)
    for (k,q),dn in DEG.items():
        u=B[k][0];P=min(rho[u]+b-a-1,b-1-q);e={dn:-1}
        for p in range(P+1):n=('qp',k,q,p);m.var(n);QP[k,q,p]=n;e[n]=1
        m.row(f'qp:{k}:{q}',e,0,True);e={QP[k,q,p]:-p for p in range(P+1)}
        for (kk,l,qq,v),n in PAIR.items():
            if l==k and v==q:e[n]=e.get(n,0)+len(B[kk])-(kk==k)
        m.row(f'qi:{k}:{q}',e,0,True)
    sa=defaultdict(list);la=defaultdict(list)
    for k,q,p in QP:sa[k,q].append(p)
    for g,o,x in CX:la[g,o].append(x)
    for n in list(m.map):
        if n and n[0]=='ts':
            _,k,g,o,q=n;rr=st['domains'][L[g][0]][o][1];e={n:-1}
            for p in sa[k,q]:
                for x in la[g,o]:
                    if x and rr+x>=q+p:z=('z',k,g,o,q,p,x);m.var(z);Z[k,g,o,q,p,x]=z;e[z]=1
            m.row('zp:'+':'.join(map(str,n[1:])),e,0,True)
    bs=defaultdict(dict);bl=defaultdict(dict)
    for key,n in Z.items():k,g,o,q,p,x=key;bs[k,q,p,g][n]=1;bl[g,o,x,k][n]=1
    for (k,q,p),w in QP.items():
        cnt={w:-q}
        for g,G in enumerate(L):
            e={w:-1};e.update(bs[k,q,p,g]);m.row(f'sc:{k}:{q}:{p}:{g}',e,0)
            for n in bs[k,q,p,g]:cnt[n]=cnt.get(n,0)+len(G)
        m.row(f'sn:{k}:{q}:{p}',cnt,0,True)
    for (g,o,x),v in CX.items():
        tot={v:-x}
        for k,U in enumerate(B):
            e={v:-1};e.update(bl[g,o,x,k]);m.row(f'lc:{g}:{o}:{x}:{k}',e,0)
            for n in bl[g,o,x,k]:tot[n]=tot.get(n,0)+len(U)
        m.row(f'ln:{g}:{o}:{x}',tot,0,True)
    m.bounds();return m

def certificate(m):
    A,b,E,f=m.matrices();N=len(m.names);nu=len(m.ub);ne=len(m.eq);D=hstack([-A.T,-E.T,E.T],format='csr');D=vstack([D,csr_matrix(np.r_[b,f,-f].reshape(1,-1))]);rhs=np.r_[np.zeros(N),-1.]
    r=linprog(np.ones(nu+2*ne),A_ub=D,b_ub=rhs,bounds=(0,None),method='highs')
    if not r.success:return None
    for s in (10**3,10**6,10**9,10**12):
        la=[max(0,round(float(x)*s)) for x in r.x[:nu]];mu=[round(float(x-y)*s) for x,y in zip(r.x[nu:nu+ne],r.x[nu+ne:])];co=[0]*N;R=0
        for rows,W in ((m.ub,la),(m.eq,mu)):
            for (_,d,bv),w in zip(rows,W):
                if w:R+=w*bv
                for j,a in d.items():co[j]+=w*a
        for j,x in enumerate(co):
            if x<0:la[m.bound_start+j]-=x;R-=x;co[j]=0
        if R<0:
            from math import gcd
            from functools import reduce
            g=reduce(gcd,[x for x in la if x]+[abs(x) for x in mu if x]) or 1
            return {'rhs':R//g,'ub':[(m.ub[i][0],w//g) for i,w in enumerate(la) if w],'eq':[(m.eq[i][0],w//g) for i,w in enumerate(mu) if w]}
    return None

def verify(m,c):
    U={x:(d,b) for x,d,b in m.ub};E={x:(d,b) for x,d,b in m.eq};co=defaultdict(int);R=0
    for x,w in c['ub']:
        assert x in U and type(w) is int and w>=0;d,b=U[x];R+=w*b
        for j,a in d.items():co[j]+=w*a
    for x,w in c['eq']:
        assert x in E and type(w) is int;d,b=E[x];R+=w*b
        for j,a in d.items():co[j]+=w*a
    assert R==c['rhs']<0 and all(x>=0 for x in co.values());return R
