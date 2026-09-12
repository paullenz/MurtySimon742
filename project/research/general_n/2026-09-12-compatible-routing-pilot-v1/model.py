#!/usr/bin/env python3
"""Integer whole-source-count necessary conditions; no solver dependency."""
from collections import Counter
import hashlib,json
MODES=('catalogue_free','selected_balance','separate_transport','joint_transport')

def capacity(rec,h):
    a,s,rho=rec['a'],rec['s'],rec['rho']
    caps=[min(a-v,sum(h<=x<=v for x in s)) for v in rho if v>=h]
    hi=sorted((c for c in caps if c>h),reverse=True)
    z=len(caps);low=sum(min(h,c) for c in caps)
    return [low-j*h+min(sum(hi[:j]),j*z-j*(j+1)//2) for j in range(len(hi)+1)]

def build(rec,h,j,mode):
    assert mode in MODES and rec['t']>0 and min(rec['rho'])>=1
    a,b,s,rho=rec['a'],rec['b'],rec['s'],rec['rho'];sizes=Counter(rho)
    z=sum(v>=h for v in rho);W=sum(v for v in s if v>=h)
    G=sum(max(4*h,v) for v in s if v>=h);target=h*(G-sum(rho))
    names=[];bounds=[]
    for rv,n in sorted(sizes.items()):
        heavy=sum(h<=sv<=rv for sv in s);light=sum(sv<h and sv<=rv for sv in s)
        if mode=='catalogue_free':
            if rv<h:continue
            for H in range(min(a-rv,heavy)+1):
                if j==0 and H>h:continue
                for p in range(min(rv+b-a-1,b-1-H)+1):
                    names.append((rv,-1,p,H));bounds.append(n)
        else:
            for q in range(min(a-rv,heavy+light)+1):
                for H in range(max(0,q-light),min(q,heavy)+1):
                    if j==0 and H>h:continue
                    for p in range(min(rv+b-a-1,b-1-q)+1):
                        names.append((rv,q,p,H));bounds.append(n)
    eq=[];ub=[]
    def row(kind,name,coeff,rhs=0):
        (eq if kind=='eq' else ub).append(dict(name=name,coefficients={i:c for i,c in enumerate(coeff) if c},rhs=rhs))
    for rv,n in sorted(sizes.items()):
        if mode=='catalogue_free' and rv<h:continue
        row('eq',['source_count',rv],[int(v==rv) for v,q,p,H in names],n)
    row('eq',['high_sender_count'],[int(H>h) for v,q,p,H in names],j)
    row('ub',['heavy_mass'],[-H for v,q,p,H in names],-W)
    row('ub',['load'],[-H*(h+max(0,4*h-max(h,(H if mode=='catalogue_free' else q)+p))) for v,q,p,H in names],-target)
    row('ub',['pair_capacity'],[H*int(H>h) for v,q,p,H in names],j*z-j*(j+1)//2)
    row('ub',['heavy_receiving'],[H*int(H>h)-(min(p,j-int(H>h)) if v>=h else 0) for v,q,p,H in names])
    if mode!='catalogue_free':
        row('eq',['selected_balance'],[q-p for v,q,p,H in names])
    if mode in ('separate_transport','joint_transport'):
        for k in range(a+2):
            row('ub',['all_transport',k],[q*int(q>k)-p*int(v+q>=k) for v,q,p,H in names])
            row('ub',['forced_transport',k],[H*int(H>h and q>k)-(min(p,j-int(H>h)) if v>=h and v+q>=k else 0) for v,q,p,H in names])
    if mode=='joint_transport':
        for k in range(1,a+2):
            for ell in range(k):
                coeff=[]
                for v,q,p,H in names:
                    F=H*int(H>h);m=min(p,j-int(H>h))
                    incoming=p if v+q>=k else (m if v>=h and v+q>=ell else 0)
                    coeff.append((q-F)*int(q>k)+F*int(q>ell)-incoming)
                row('ub',['mixed_transport',k,ell],coeff)
    bound_start=len(ub)
    for i,cap in enumerate(bounds):ub.append(dict(name=['count_cap',i],coefficients={i:1},rhs=cap))
    return dict(names=names,bounds=bounds,eq=eq,ub=ub,bound_start=bound_start,h=h,j=j,mode=mode,target=target)

def digest(model):
    return hashlib.sha256(json.dumps(model,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def verify(model,certificate):
    totals=[0]*len(model['names']);rhs=0
    for kind in ('eq','ub'):
        seen=set()
        for i,w in certificate[kind]:
            assert type(i) is int and 0<=i<len(model[kind]) and i not in seen
            assert type(w) is int and (kind=='eq' or w>=0)
            seen.add(i);row=model[kind][i];rhs+=w*row['rhs']
            for col,c in row['coefficients'].items():totals[col]+=w*c
    assert min(totals,default=0)>=0 and rhs==certificate['rhs']<0
    return dict(columns=len(totals),rhs=rhs)
