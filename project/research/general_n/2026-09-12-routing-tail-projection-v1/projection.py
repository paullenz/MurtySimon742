#!/usr/bin/env python3
"""Pure integer demand/tail projection of the joint-routing inequality."""
from functools import lru_cache


def baseline(rec):
    L={1:rec['b'],rec['a']+1:0}
    L.update({row['h']:row['closed_tail'] for row in rec['tails']})
    L[rec['a']]=0
    return L


def context(rec,L,h,z):
    a,b,t,s=rec['a'],rec['b'],rec['t'],tuple(rec['s'])
    M=sum(s)-2*t;W=sum(v for v in s if v>=h);G=sum(max(4*h,v) for v in s if v>=h)
    lower_cost=b+sum(max(L[l],z) for l in range(2,h))+z if h>=2 else b
    E=M-lower_cost
    other=sum(max(0,L[l]-1) for l in range(h+1,a+1))
    Rmax=min(a,h+E-other)
    options=[[],[]];types=[]
    if E>=sum(L[l] for l in range(h+1,a+1)):
        for rv in range(h,Rmax+1):
            c=min(a-rv,sum(h<=v<=rv for v in s));P=rv+b-a-1
            if P>=0:types.append((rv,c,P))
            for H in range(c+1):
                for p in range(min(P,b-1-H)+1):
                    B=h*H+H*max(0,4*h-max(h,H+p))
                    options[int(H>h)].append((rv,H,p,B))
    C=max((o[1] for group in options for o in group),default=0)
    K=lambda j:j*(z-j)+j*(j-1)//2
    jbounds=[(z-j)*min(h,C)+min(j*C,K(j)) for j in range(z+1 if C>h else 1)]
    return dict(a=a,b=b,h=h,z=z,M=M,W=W,G=G,E=E,Rmax=Rmax,C=C,options=options,types=types,jbounds=jbounds)


def evaluate(ctx,j,lam,mu,eta,kappa,den=1):
    h,z=ctx['h'],ctx['z'];A=[]
    for e in (0,1):
        vals=[den*B+eta*H-(lam+mu)*e*H+lam*min(p,j-e)-kappa*(rv-h)
              for rv,H,p,B in ctx['options'][e]]
        A.append(max(vals) if vals else None)
    assert A[0] is not None and (j==0 or A[1] is not None)
    lhs=den*h*ctx['G']
    rhs=den*h*ctx['M']+kappa*ctx['E']+(z-j)*A[0]+(j*A[1] if j else 0)+mu*(j*(z-j)+j*(j-1)//2)-eta*ctx['W']
    return dict(j=j,denominator=den,lam=lam,mu=mu,eta=eta,kappa=kappa,lhs=lhs,rhs=rhs,gap=lhs-rhs,local_maxima=A)
