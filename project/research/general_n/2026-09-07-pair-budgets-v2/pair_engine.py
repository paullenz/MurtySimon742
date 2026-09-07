#!/usr/bin/env python3
"""General-order selected-pair relaxation and exact certificate checking.

Search uses scipy optionally. Checkers use only Python exact integers.
No feasible profile is claimed to be a graph. No solver infeasibility is proof.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
from math import lcm
import json


def prepare(p: dict) -> dict:
    a,b,t = p['a'],p['b'],p['t']
    d,R,rho = p['d'],p['R'],p['rho']
    if not (len(d)==len(R)==a and len(rho)==b):
        raise ValueError('profile lengths')
    if not all(type(x) is int for x in [a,b,t]+d+R+rho):
        raise ValueError('integer data required')
    r=sum(rho)
    if sum(R)!=r or sum(d)!=2*(r+t):
        raise ValueError('ledger mismatch')
    if not (a>0 and b>0 and all(0<=x<a for x in d) and all(0<=x<=b for x in R)
            and all(1<=x<=a for x in rho) and t>0):
        raise ValueError('outside positive-surplus domain')
    demand=[max(0,di-ri) for di,ri in zip(d,R)]
    # Select q easiest eligible labels and match the strongest q suppliers.
    c=[]
    for u,ru in enumerate(rho):
        suppliers=sorted((ru+rw for w,rw in enumerate(rho) if w!=u),reverse=True)
        best=0
        for q in range(1,min(a-ru,b-1)+1):
            eligible=sorted(di for i,di in enumerate(d) if di<=ru+q-1 and di<=ru+R[i])
            if len(eligible)>=q and all(di<=rw for di,rw in zip(eligible[:q][::-1],suppliers[:q])):
                best=q
        c.append(best)
    # Refinement preserves c[u]>=q[u] by induction; never use partly updated caps.
    rounds=[c[:]]
    while True:
        new=[]
        for u,cu in enumerate(c):
            new.append(max(q for q in range(cu+1)
                if sum(w!=u and rho[w]+c[w]>=q-1 for w in range(b))>=q))
        if new==c: break
        c=new
        rounds.append(c[:])
    eligible=[[u for u in range(b) if d[i]<=rho[u]+c[u]-1 and d[i]<=rho[u]+R[i]] for i in range(a)]
    f=[0]*b
    for i in range(a):
        if demand[i]>len(eligible[i]):
            return dict(profile=p,early=dict(kind='label_capacity',i=i,lhs=demand[i],rhs=len(eligible[i])),caps=c)
        if demand[i] and demand[i]==len(eligible[i]):
            for u in eligible[i]: f[u]+=1
    for u in range(b):
        if f[u]>c[u]:
            return dict(profile=p,early=dict(kind='forced_source',u=u,lhs=f[u],rhs=c[u]),caps=c)
    ell=b-a-1
    inc=[min(b-1,rw+ell) for rw in rho]
    if min(inc)<0:
        return dict(profile=p,early=dict(kind='incoming_negative',u=inc.index(min(inc))),caps=c)
    # Keep cap-zero supplements too: this universe is the OLD permitted-pair
    # universe. The new incoming resource may then have capacity zero.
    triples=[]
    for i in range(a):
        for u in eligible[i]:
            lam=max(1,f[u],d[i]-rho[u]+1)
            if lam>c[u]: continue
            for w in range(b):
                if w!=u and d[i]<=rho[u]+rho[w] and rho[w]+c[w]>=lam-1:
                    triples.append((i,u,w))
    pairs=sorted({tuple(sorted((u,w))) for i,u,w in triples})
    return dict(profile=p,r=r,demand=demand,caps=c,cap_rounds=rounds,eligible=eligible,
                forced=f,incoming_caps=inc,triples=triples,pairs=pairs,ell=ell)


def support_certificate(data: dict, labels: list[int] | None=None) -> dict | None:
    if 'early' in data: return dict(kind='early',witness=data['early'])
    if labels is None: labels=list(range(data['profile']['a']))
    labelset=set(labels)
    W=sorted({w for i,u,w in data['triples'] if i in labelset})
    lhs=sum(data['demand'][i] for i in labels)
    rhs=sum(data['incoming_caps'][w] for w in W)
    if lhs>rhs:
        return dict(kind='supplement_support',labels=labels,W=W,lhs=lhs,rhs=rhs)
    return None


def check_support(p: dict, cert: dict) -> bool:
    data=prepare(p)
    if cert['kind']=='early':
        return 'early' in data and cert['witness']==data['early']
    if cert['kind']!='supplement_support' or 'early' in data: return False
    I=cert['labels']
    if len(set(I))!=len(I) or not all(0<=i<p['a'] for i in I): return False
    out=support_certificate(data,I)
    return out==cert


def resource_data(data: dict):
    a,b=data['profile']['a'],data['profile']['b']
    resources=[]; capacity=[]
    def add(name,cap):
        resources.append(name);capacity.append(cap)
    for u in range(b):add(('source',u),data['caps'][u])
    for w in range(b):add(('supplement',w),data['incoming_caps'][w])
    for i in range(a):
        for u in data['eligible'][i]:add(('source_label',i,u),1)
    for u,w in data['pairs']:add(('pair',u,w),1)
    lookup={name:j for j,name in enumerate(resources)}
    rows=[]
    for i,u,w in data['triples']:
        names=[('source',u),('supplement',w),('source_label',i,u),('pair',min(u,w),max(u,w))]
        rows.append([lookup[name] for name in names])
    return resources,capacity,rows


def find_weighted_certificate(data: dict) -> dict | None:
    """Floating point discovers weights; only check_weighted certifies them."""
    if 'early' in data:return None
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import lil_matrix
    resources,capacity,rows=resource_data(data)
    a=data['profile']['a']; nvars=a+len(resources)
    A=lil_matrix((len(rows),nvars),dtype=float)
    for k,((i,u,w),rs) in enumerate(zip(data['triples'],rows)):
        A[k,i]=1
        for j in rs:A[k,a+j]=-1
    obj=np.array([-x for x in data['demand']]+capacity,dtype=float)
    res=linprog(obj,A_ub=A.tocsr(),b_ub=np.zeros(len(rows)),
                bounds=[(0,1)]*a+[(0,None)]*len(resources),method='highs')
    if not res.success or res.fun>=-1e-7:return None
    for den in [1,10,100,1000,10000]:
        vals=[Fraction(float(x)).limit_denominator(den) for x in res.x]
        scale=lcm(*(v.denominator for v in vals))
        ints=[int(v*scale) for v in vals]
        cert=dict(kind='weighted_cover',label_weights=ints[:a],
            resource_weights=[dict(resource=list(name),weight=ints[a+j])
                              for j,name in enumerate(resources) if ints[a+j]],
            search_note='LP-discovered weights; claimed only after exact integer verification')
        if check_weighted(data['profile'],cert):return cert
    return None


def check_weighted(p: dict,cert: dict) -> bool:
    data=prepare(p)
    if 'early' in data or cert.get('kind')!='weighted_cover': return False
    weights=cert['label_weights']
    if len(weights)!=p['a'] or not all(type(x) is int and x>=0 for x in weights):return False
    resources,capacity,rows=resource_data(data)
    lookup={name:j for j,name in enumerate(resources)}
    alpha=[0]*len(resources); seen=set()
    for rec in cert['resource_weights']:
        name=tuple(rec['resource']);w=rec['weight']
        if name not in lookup or name in seen or type(w) is not int or w<0:return False
        seen.add(name);alpha[lookup[name]]=w
    for (i,u,w),rs in zip(data['triples'],rows):
        if weights[i]>sum(alpha[j] for j in rs):return False
    lhs=sum(x*y for x,y in zip(weights,data['demand']))
    rhs=sum(x*y for x,y in zip(alpha,capacity))
    return lhs>rhs


def find_integer_witness(data: dict,seconds: float=15) -> dict:
    """Find an integral witness to the relaxation, never an actual graph."""
    import numpy as np
    from scipy.optimize import milp,Bounds,LinearConstraint
    from scipy.sparse import lil_matrix
    resources,capacity,rows=resource_data(data)
    a=data['profile']['a']; nt=len(rows)
    A=lil_matrix((a+len(resources),nt),dtype=float)
    for k,((i,u,w),rs) in enumerate(zip(data['triples'],rows)):
        A[i,k]=1
        for j in rs:A[a+j,k]=1
    lb=np.array(data['demand']+[-np.inf]*len(resources),dtype=float)
    ub=np.array(data['demand']+capacity,dtype=float)
    res=milp(np.zeros(nt),integrality=np.ones(nt),bounds=Bounds(0,1),
             constraints=LinearConstraint(A.tocsc(),lb,ub),
             options={'time_limit':seconds})
    if res.x is None:
        return dict(status='NO_WITNESS_FOUND',solver_status=int(res.status),message=str(res.message),
                    meaning='No exclusion claimed; no infeasibility certificate produced')
    selected=[list(t) for t,x in zip(data['triples'],res.x) if x>0.5]
    ans=dict(status='RELAXATION_WITNESS',selected=selected,meaning='Not a graph or counterexample')
    if not check_integer_witness(data['profile'],ans):
        return dict(status='NO_EXACT_WITNESS',meaning='Floating candidate failed exact checks')
    return ans


def check_integer_witness(p:dict,witness:dict) -> bool:
    data=prepare(p)
    if 'early' in data:return False
    allowed=set(data['triples']); chosen=[tuple(t) for t in witness['selected']]
    if len(chosen)!=len(set(chosen)) or any(t not in allowed for t in chosen):return False
    resources,capacity,rows=resource_data(data)
    lut={t:rs for t,rs in zip(data['triples'],rows)}
    use=[0]*len(capacity); demand=[0]*p['a']
    for t in chosen:
        demand[t[0]]+=1
        for j in lut[t]:use[j]+=1
    return demand==data['demand'] and all(x<=y for x,y in zip(use,capacity))


def legacy_tests(data: dict) -> dict:
    """Earlier numerical cuts, with exact exhaustive subset check via maxflow.
    Supplement-support/weighted covers are deliberately NOT applied here.
    """
    if 'early' in data:return dict(early=data['early'])
    p=data['profile'];d,R,rho=p['d'],p['R'],p['rho'];a,b=p['a'],p['b']
    s=data['demand'];caps=data['caps']
    tests={}
    tests['source_total']=sum(caps)>=sum(s)
    tests['fixed_pair_threshold']=all(sum(s[i] for i in range(a) if d[i]>=j)<=
                sum(ru+rw>=j for ru,rw in combinations(rho,2)) for j in range(1,max(d)+1))
    tests['outer_pair_threshold']=all(sum(di for di in d if di>=j)-sum(min(ru,sum(di>=j for di in d)) for ru in rho)<=
                sum(ru+rw>=j for ru,rw in combinations(rho,2)) for j in range(1,max(d)+1))
    tests['global_permitted_pairs']=sum(s)<=len(data['pairs'])
    # integer augmenting paths (not a floating solver)
    n=a+b+2; S=a+b;T=S+1; adj=[[] for _ in range(n)]; cap={}
    def edge(u,v,c):
        adj[u].append(v);adj[v].append(u);cap[u,v]=c;cap[v,u]=0
    for i in range(a):
        edge(S,i,s[i])
        for u in data['eligible'][i]:edge(i,a+u,1)
    for u in range(b):edge(a+u,T,caps[u])
    flow=0
    while True:
        prev={S:None};todo=[S]
        for x in todo:
            for y in adj[x]:
                if y not in prev and cap[x,y]>0:prev[y]=x;todo.append(y)
            if T in prev:break
        if T not in prev:break
        val=10**9;x=T
        while prev[x] is not None:
            y=prev[x];val=min(val,cap[y,x]);x=y
        x=T
        while prev[x] is not None:
            y=prev[x];cap[y,x]-=val;cap[x,y]+=val;x=y
        flow+=val
    tests['all_source_label_subset_cuts']=flow==sum(s)
    tests['h_index']=sum(max(0,di-max([0]+[j for j in range(1,b+1) if sum(x>=j for x in rho)>=j])) for di in d)<=data['r']
    k=a-1-max(d);L=a*(a-1)//2-p['t']
    tests['local_k']=L>=b+k+(a-k-1)*(a-k-2)//2
    tests['minimum_C_degree']=L-data['r']>=(a*k+1)//2
    tests['incoming_total_only']=sum(s)<=sum(data['incoming_caps'])
    dd=sorted(d,reverse=True)
    tests['F_degree_graphical']=sum(dd)%2==0 and all(sum(dd[:k])<=k*(k-1)+sum(min(k,x) for x in dd[k:]) for k in range(1,a+1))
    rr=sorted(rho,reverse=True)
    tests['residual_degree_bigraphical']=all(sum(rr[:k])<=sum(min(k,x) for x in R) for k in range(1,b+1))
    return tests


def degree_budget_certificate(data: dict) -> dict | None:
    """Source pair-degree versus A-label neighbourhood sizes, all Q at once.

    Actual selected degree x_i >= s_i and sum(x_i-s_i)=Q-Qmin.
    If pair-degree sigma_u > D0, each of its q_u selected labels consumes
    at least sigma_u-D0 of this excess. Incoming degree <= pcap_u.
    Thus (sigma_u-pcap_u)*(sigma_u-D0)<=Q-Qmin when both factors >0.
    """
    if 'early' in data:return dict(kind='early',witness=data['early'])
    p=data['profile'];a,b=p['a'],p['b']
    qmin=sum(data['demand']);D0=max(max(d,R) for d,R in zip(p['d'],p['R']))
    incoming_support={w for i,u,w in data['triples']}
    inc=[data['incoming_caps'][u] if u in incoming_support else 0 for u in range(b)]
    pair_degree=[sum(u in pair for pair in data['pairs']) for u in range(b)]
    qmax=min(sum(data['caps']),len(data['pairs']),sum(inc),
             sum(min(b-p['R'][i],len(data['eligible'][i])) for i in range(a)))
    rows=[]
    for Q in range(qmin,qmax+1):
        excess=Q-qmin
        caps=[]
        for u in range(b):
            largest=min(pair_degree[u],data['caps'][u]+inc[u])
            keep=[]
            for sigma in range(largest+1):
                need_out=max(0,sigma-inc[u])
                if sigma>D0 and need_out*(sigma-D0)>excess:continue
                keep.append(sigma)
            caps.append(max(keep))
        upper=sum(caps)
        if 2*Q<=upper:return None
        rows.append(dict(Q=Q,excess=excess,degree_caps=caps,lhs=2*Q,rhs=upper))
    return dict(kind='source_pair_degree_budget',Qmin=qmin,Qmax=qmax,D0=D0,rows=rows)


def check_degree_budget(p:dict,cert:dict) -> bool:
    if cert.get('kind')=='early':return check_support(p,cert)
    data=prepare(p)
    if 'early' in data:return False
    return degree_budget_certificate(data)==cert and cert is not None


def degree_budget_closure(data: dict) -> dict | None:
    """Monotone Q-upper-bound refinement; exact, no column or graph search."""
    if 'early' in data:return dict(kind='early',witness=data['early'])
    p=data['profile'];a,b=p['a'],p['b']
    qmin=sum(data['demand']);D0=max(max(d,R) for d,R in zip(p['d'],p['R']))
    W={w for i,u,w in data['triples']}
    inc=[data['incoming_caps'][u] if u in W else 0 for u in range(b)]
    pairdeg=[sum(u in pair for pair in data['pairs']) for u in range(b)]
    qmax=min(sum(data['caps']),len(data['pairs']),sum(inc),
             sum(min(b-p['R'][i],len(data['eligible'][i])) for i in range(a)))
    initial=qmax;rounds=[]
    while qmax>=qmin:
        E=qmax-qmin;caps=[]
        for u in range(b):
            sigma=max(z for z in range(min(pairdeg[u],data['caps'][u]+inc[u])+1)
                      if max(0,z-inc[u])*max(0,z-D0)<=E)
            caps.append(sigma)
        new=min(qmax,sum(caps)//2)
        rounds.append(dict(Qupper_before=qmax,excess_upper=E,degree_caps=caps,Qupper_after=new))
        if new==qmax:return None
        qmax=new
    return dict(kind='source_pair_degree_closure',Qmin=qmin,Qupper_initial=initial,D0=D0,
                rounds=rounds,Qupper_final=qmax)


def check_degree_closure(p:dict,cert:dict) -> bool:
    return cert is not None and degree_budget_closure(prepare(p))==cert
