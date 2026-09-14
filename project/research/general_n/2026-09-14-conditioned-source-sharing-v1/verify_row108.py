#!/usr/bin/env python3
"""Exact standard-library replay for the first source-sharing closure (row 108).

This verifier works only in the explicitly stated selected-incidence relaxation.
It does not claim graph realization, whole-state closure, or a general theorem.
Run without -O: assertions are audit checks.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, deque
from functools import lru_cache
from itertools import product
from pathlib import Path

SHARED_HASH = "35d4c3c05595102b2a568d986d8bab753059da4a2c59b31689a550aaddb23ce6"
CORPUS_HASH = "157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572"
TARGET_ROW = 108
TARGET_CHARGE = 211
PRICE_LAMBDA = [0,-4,0,0,0,0,0,0,0,0,0,0,-4,0,0,0,0,0,0,0,0,-4,0,0,0,0,0,0]
PRESSURE_TUPLES = {
    (26,33),(26,35),(26,36),(26,37),(27,33),(27,36),(27,37),(28,37)
}


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def old_caps(a, s, q, rho):
    b=len(q); E=sum(q)-sum(s); z=s.count(0)
    c=[qq+r for qq,r in zip(q,rho)]
    D=[[u!=w and q[u]<=c[w]+1 and q[w]<=c[u] for w in range(b)] for u in range(b)]
    P=[]
    for w,qq in enumerate(q):
        degree=sum(D[w][u] or D[u][w] for u in range(b))
        cap=min(rho[w]+b-a-1,b-1-qq,degree-qq)
        k=min(z,qq,E)
        if qq>k:
            cap=min(cap,rho[w]-1+(E-k)//(qq-k))
        P.append(cap)
    return P


def prior_localized(s,q,rho,initial):
    E=sum(q)-sum(s); P=list(initial)
    for eta in sorted({0,*rho}):
        m=sum(d<=eta for d in s)
        C=E+sum(d for d in s if d<=eta)-sum(qq for qq,r in zip(q,rho) if r<=eta)
        if C<0: raise ValueError("prior prefix infeasible")
        for w,(qq,r) in enumerate(zip(q,rho)):
            if r<=eta: continue
            k=min(m,qq,C)
            if qq>k:
                P[w]=min(P[w],r-1+(C-k)//(qq-k))
    return P


def spill_data(s,q,rho,eta):
    low=[i for i,d in enumerate(s) if d<=eta]
    forced=[max(0,qq-sum(eta<d<=r for d in s)) for qq,r in zip(q,rho)]
    return low,sum(s[i] for i in low),forced


def spill_caps(s,q,rho,initial):
    E=sum(q)-sum(s); P=list(initial)
    for eta in sorted({0,*s}):
        low,SL,forced=spill_data(s,q,rho,eta); M=sum(forced)
        if M>E+SL: raise ValueError("spill infeasible")
        for w,(qq,r) in enumerate(zip(q,rho)):
            C=E+SL-M+forced[w]
            m=sum(s[i]<=r for i in low)
            k=min(qq,m,C)
            if qq>k:
                P[w]=min(P[w],r-1+(C-k)//(qq-k))
    return P


def baseline(p):
    raw=old_caps(p['a'],p['s'],p['q'],p['rho'])
    assert raw==p['P']
    return spill_caps(p['s'],p['q'],p['rho'],prior_localized(p['s'],p['q'],p['rho'],raw))


def fullcap(p,levels,nums,es,P):
    q,r=p['q'],p['rho']; D=[max(0,pp-rr+1) for pp,rr in zip(P,r)]; out=[]
    for u,qq in enumerate(q):
        ok=[]
        for d in range(D[u]+1):
            count=sum((nn if not v or not d else min(nn,e//d))
                      for v,nn,e in zip(levels,nums,es) if v<=r[u])
            if count>=qq: ok.append(d)
        if not ok: return None
        out.append(min(P[u],r[u]-1+max(ok)))
    return out


def receiver_certificate(q,rho,s,P,eta,alpha,tau,theta):
    b=len(q); m=sum(d<=eta for d in s)
    v=[al*max(0,qq-m) for al,qq in zip(alpha,q)]
    c=[qq+r for qq,r in zip(q,rho)]
    A=[min(P[w],sum(u!=w and tau<=q[u]<=c[w]+1 for u in range(b))) for w in range(b)]
    f=[min(aa,r-1) for aa,r in zip(A,rho)]; g=[aa-ff for aa,ff in zip(A,f)]
    demand=sum(qq for qq in q if qq>=tau)
    penalty=sum(max(0,theta-vv)*gg for vv,gg in zip(v,g))
    return dict(tau=tau,theta=theta,eta=eta,demand=demand,capacity=sum(A),free=sum(f),penalty=penalty,
                lower=theta*(demand-sum(f))-penalty)


def best_lower(q,rho,s,P,eta,alpha):
    m=sum(d<=eta for d in s)
    prices=sorted({0,*[al*max(0,qq-m) for al,qq in zip(alpha,q)]})
    out=None
    for tau in range(1,max(q,default=0)+1):
        for theta in prices:
            d=receiver_certificate(q,rho,s,P,eta,alpha,tau,theta)
            if out is None or d['lower']>out['lower']: out=d
    return out or dict(tau=1,theta=0,eta=eta,demand=0,capacity=0,free=0,penalty=0,lower=0)


def exact_blocks_upper(p,P,levels,nums,es,eta,alpha):
    q,r=p['q'],p['rho'];D=[max(0,pp-rr+1) for pp,rr in zip(P,r)];total=0
    for v,n,E in zip(levels,nums,es):
        eligible=[u for u in range(len(q)) if q[u] and r[u]>=v];hi=len(eligible)-v
        if hi<0:return None
        score=[sum(sorted((alpha[u]*min(e,D[u]) for u in eligible),reverse=True)[:v+e]) if v>eta else 0
               for e in range(min(hi,E)+1)]
        dp={0:0}
        for _ in range(n):
            nd={}
            for used,val in dp.items():
                for e in range(min(hi,E-used)+1):
                    t=used+e; nv=val+score[e]
                    if nv>nd.get(t,-10**18): nd[t]=nv
            dp=nd
        if E not in dp:return None
        total+=dp[E]
    return total


def old_multiblock_screen(p,cum,P):
    levels=sorted(set(p['s']));nums=[p['s'].count(v) for v in levels]
    full=(0,)+tuple(cum)+(p['Esel'],);es=[full[i+1]-full[i] for i in range(len(levels))]
    if min(es)<0:return 'invalid',es,None,None
    pc=fullcap(p,levels,nums,es,P)
    if pc is None:return 'empty_source',es,None,None
    if sum(pc)<sum(p['q']):return 'sumcap',es,pc,None
    best=None
    for eta in sorted({0,*levels[:-1]}):
        for alpha in ([1]*len(p['q']),[1 if qq<=2 else 3 for qq in p['q']]):
            up=exact_blocks_upper(p,pc,levels,nums,es,eta,alpha)
            if up is None:return 'empty',es,pc,None
            low=best_lower(p['q'],p['rho'],p['s'],pc,eta,alpha)
            cand=dict(low);cand.update(gap=low['lower']-up,upper=up,
                                       weight_rule='uniform' if max(alpha)==1 else 'three_above_q2')
            if best is None or cand['gap']>best['gap']:best=cand
            if cand['gap']>0:break
        if best['gap']>0:break
    return ('price' if best['gap']>0 else 'unrejected'),es,pc,best


def source_priced_upper(p,pc,levels,nums,es,eta,alpha,lambdas):
    """Lagrange row-price upper; exact row sums restore sum lambda_u q_u."""
    q,r=p['q'],p['rho'];D=[max(0,pp-rr+1) for pp,rr in zip(pc,r)];total=0
    assert len(lambdas)==len(q)
    for d,n,E in zip(levels,nums,es):
        eligible=[u for u in range(len(q)) if q[u] and r[u]>=d];hi=len(eligible)-d
        if hi<0:return None
        score=[]
        for e in range(min(hi,E)+1):
            vals=[]
            for u in eligible:
                base=alpha[u]*min(e,D[u]) if d>eta else 0
                vals.append(base-lambdas[u])
            vals.sort(reverse=True)
            score.append(sum(vals[:d+e]))
        dp={0:0}
        for _ in range(n):
            nd={}
            for used,val in dp.items():
                for e in range(min(hi,E-used)+1):
                    t=used+e;nv=val+score[e]
                    if nv>nd.get(t,-10**18):nd[t]=nv
            dp=nd
        if E not in dp:return None
        total+=dp[E]
    return total+sum(l*qq for l,qq in zip(lambdas,q))


@lru_cache(None)
def partitions(n,E,hi,lo=0):
    """Nondecreasing excess tuples, quotienting identical-label permutations."""
    if n==0:return ((),) if E==0 else ()
    if E<n*lo or E>n*hi:return ()
    out=[]
    for x in range(lo,min(hi,E//n)+1):
        for tail in partitions(n-1,E-x,hi,x):out.append((x,)+tail)
    return tuple(out)


def hist_from_tuple(d,t):
    return [(d,e,m) for e,m in sorted(Counter(t).items())]


def histogram_blocks(p,levels,nums,es):
    blocks=[]
    for d,n,E in zip(levels,nums,es):
        eligible=sum(qq>0 and r>=d for qq,r in zip(p['q'],p['rho']))
        hi=eligible-d
        blocks.append([hist_from_tuple(d,t) for t in partitions(n,E,hi,0)])
    return blocks


class FEdge:
    __slots__=('to','rev','cap')
    def __init__(self,to,rev,cap):self.to=to;self.rev=rev;self.cap=cap

def fadd(g,u,v,c):
    g[u].append(FEdge(v,len(g[v]),c));g[v].append(FEdge(u,len(g[u])-1,0))


def maxflow_feasible(p,hist,pressures=None):
    nsrc=len(p['q']);nt=len(hist);S=0;so=1;to=1+nsrc;T=to+nt;N=T+1
    g=[[] for _ in range(N)];total=sum(p['q']);dem=0
    if pressures is None:pressures=[0]*nsrc
    for u,q in enumerate(p['q']):
        if q:fadd(g,S,so+u,q)
    for j,(d,e,m) in enumerate(hist):
        req=m*(d+e);dem+=req;fadd(g,to+j,T,req)
        for u,(q,r,pr) in enumerate(zip(p['q'],p['rho'],pressures)):
            if q and r>=d and (d==0 or e>=pr):fadd(g,so+u,to+j,m)
    if dem!=total:return False
    flow=0
    while True:
        level=[-1]*N;level[S]=0;dq=deque([S])
        while dq:
            v=dq.popleft()
            for e in g[v]:
                if e.cap and level[e.to]<0:level[e.to]=level[v]+1;dq.append(e.to)
        if level[T]<0:break
        it=[0]*N
        def dfs(v,f):
            if v==T:return f
            while it[v]<len(g[v]):
                e=g[v][it[v]]
                if e.cap and level[e.to]==level[v]+1:
                    z=dfs(e.to,min(f,e.cap))
                    if z:
                        e.cap-=z;g[e.to][e.rev].cap+=z;return z
                it[v]+=1
            return 0
        while True:
            z=dfs(S,10**9)
            if not z:break
            flow+=z
    return flow==total


class CEdge:
    __slots__=('to','rev','cap','cost')
    def __init__(self,to,rev,cap,cost):self.to=to;self.rev=rev;self.cap=cap;self.cost=cost

def cadd(g,u,v,cap,cost):
    g[u].append(CEdge(v,len(g[v]),cap,cost));g[v].append(CEdge(u,len(g[u])-1,0,-cost))


def max_incidence_charge(p,pc,hist,eta=0,alpha=None):
    """Exact max charge for a FIXED histogram, retaining row sums but not common pressure."""
    if alpha is None:alpha=[1]*len(p['q'])
    nsrc=len(p['q']);nt=len(hist);S=0;so=1;to=1+nsrc;T=to+nt;N=T+1
    g=[[] for _ in range(N)];total=sum(p['q']);dem=0
    D=[max(0,pp-r+1) for pp,r in zip(pc,p['rho'])]
    for u,q in enumerate(p['q']):
        if q:cadd(g,S,so+u,q,0)
    for j,(d,e,m) in enumerate(hist):
        req=m*(d+e);dem+=req;cadd(g,to+j,T,req,0)
        for u,(q,r) in enumerate(zip(p['q'],p['rho'])):
            if q and r>=d:
                reward=alpha[u]*min(e,D[u]) if d>eta else 0
                cadd(g,so+u,to+j,m,-reward)
    if dem!=total:return None
    flow=0;cost=0;INF=10**18
    while flow<total:
        dist=[INF]*N;pv=[-1]*N;pe=[-1]*N;inq=[False]*N
        dist[S]=0;dq=deque([S]);inq[S]=True
        while dq:
            v=dq.popleft();inq[v]=False
            for k,e in enumerate(g[v]):
                if e.cap and dist[e.to]>dist[v]+e.cost:
                    dist[e.to]=dist[v]+e.cost;pv[e.to]=v;pe[e.to]=k
                    if not inq[e.to]:dq.append(e.to);inq[e.to]=True
        if dist[T]==INF:return None
        f=total-flow;v=T
        while v!=S:
            if pv[v]<0:return None
            f=min(f,g[pv[v]][pe[v]].cap);v=pv[v]
        v=T
        while v!=S:
            u=pv[v];e=g[u][pe[v]];e.cap-=f;g[v][e.rev].cap+=f;v=u
        flow+=f;cost+=f*dist[T]
    return -cost


def prove_no_common_pressure_at_least(p,pc,hist,target,eta=0,alpha=None,node_limit=500000):
    """Exact branch proof that no feasible pressure vector reaches target."""
    if alpha is None:alpha=[1]*len(p['q'])
    q=p['q'];rho=p['rho'];D=[max(0,pp-r+1) for pp,r in zip(pc,rho)]
    mlow=sum(1 for d in p['s'] if d<=eta)
    value=[alpha[u]*max(0,q[u]-mlow) for u in range(len(q))]
    labels=[]
    for d,e,m in hist:labels += [(d,e)]*m
    local=[]
    for qq,r,Du in zip(q,rho,D):
        if qq==0:local.append(0);continue
        ex=[(10**9 if d==0 else e) for d,e in labels if d<=r]
        ex.sort(reverse=True)
        if len(ex)<qq:return True,0
        local.append(min(Du,ex[qq-1]))
    order=sorted(range(len(q)),key=lambda u:value[u]*local[u],reverse=True)
    suffix=[0]*(len(order)+1)
    for k in range(len(order)-1,-1,-1):
        u=order[k];suffix[k]=suffix[k+1]+value[u]*local[u]
    pressure=[0]*len(q);nodes=0
    def rec(k,score):
        nonlocal nodes
        nodes+=1
        if nodes>node_limit:raise RuntimeError('branch node limit')
        if score+suffix[k]<target:return False
        if not maxflow_feasible(p,hist,pressure):return False
        if k==len(order):return score>=target
        u=order[k];old=pressure[u]
        for d in range(local[u],-1,-1):
            pressure[u]=d
            if rec(k+1,score+value[u]*d):pressure[u]=old;return True
        pressure[u]=old
        return False
    exists=rec(0,0)
    return (not exists),nodes


def replay(remainder,shared):
    assert remainder['source_sha256']==CORPUS_HASH
    assert hashlib.sha256(canonical(shared)).hexdigest()==SHARED_HASH
    p=next(x for x in remainder['rows'] if x['row']==TARGET_ROW)
    assert p['a']==24 and p['b']==28 and p['Esel']==45 and p['D0']==0
    assert sum(p['q'])==sum(p['rho'])+2*p['t']+p['D0']+p['Esel']
    P=baseline(p)
    shared_row=next(x for x in shared['replay']['reports'] if x['row']==TARGET_ROW)
    assert [x['remaining'] for x in shared_row['splits']]==[list(range(26,34)),list(range(33,38))]
    levels=sorted(set(p['s']));nums=[p['s'].count(v) for v in levels]
    assert levels==[1,2,3] and nums==[2,3,19]

    inherited=[]; survivors=[]
    for cum in product(*[x['remaining'] for x in shared_row['splits']]):
        if list(cum)!=sorted(cum):continue
        kind,es,pc,best=old_multiblock_screen(p,cum,P)
        if kind=='unrejected':survivors.append((tuple(cum),es,pc,best))
        else:inherited.append(dict(cum=list(cum),reason=kind,best=best))
    assert len(inherited)==8 and len(survivors)==32

    source_price=[];pressure_cases=[]
    for cum,es,pc,oldbest in survivors:
        lower=best_lower(p['q'],p['rho'],p['s'],pc,0,[1]*len(p['q']))
        up=source_priced_upper(p,pc,levels,nums,es,0,[1]*len(p['q']),PRICE_LAMBDA)
        if up<lower['lower']:
            source_price.append(dict(cum=list(cum),excess=es,upper=up,lower=lower['lower'],gap=lower['lower']-up))
        else:
            pressure_cases.append((cum,es,pc,lower,up))
    assert len(source_price)==24
    assert {x[0] for x in pressure_cases}==PRESSURE_TUPLES

    pressure_reports=[];tot_hist=tot_feas=tot_charge=tot_common=tot_nodes=0
    for cum,es,pc,lower,priced_up in pressure_cases:
        assert lower['lower']==TARGET_CHARGE
        blocks=histogram_blocks(p,levels,nums,es)
        hist_total=1
        for b in blocks:hist_total*=len(b)
        feasible=charge_below=common=nodes=0
        for combo in product(*blocks):
            hist=[x for block in combo for x in block]
            if not maxflow_feasible(p,hist):continue
            feasible+=1
            charge=max_incidence_charge(p,pc,hist,0,[1]*len(p['q']))
            assert charge is not None
            if charge<TARGET_CHARGE:
                charge_below+=1;continue
            ok,nodes_here=prove_no_common_pressure_at_least(p,pc,hist,TARGET_CHARGE,0,[1]*len(p['q']))
            assert ok
            common+=1;nodes+=nodes_here
        assert feasible==charge_below+common
        pressure_reports.append(dict(cum=list(cum),excess=es,priced_upper=priced_up,
                                     histograms=hist_total,incidence_feasible=feasible,
                                     incidence_charge_below=charge_below,common_pressure_proofs=common,
                                     branch_nodes=nodes))
        tot_hist+=hist_total;tot_feas+=feasible;tot_charge+=charge_below;tot_common+=common;tot_nodes+=nodes
    assert (tot_hist,tot_feas,tot_charge,tot_common)==(46662,1201,1124,77)
    assert tot_nodes==57867

    return dict(schema='source-sharing-row108-v1',external_review='OPEN',row=TARGET_ROW,
                old_multiblock=dict(inherited_rejected=len(inherited),survivors=len(survivors)),
                source_price=dict(price_vector=PRICE_LAMBDA,closed=len(source_price),certificates=source_price),
                common_pressure=dict(closed_tuples=len(pressure_reports),target_charge=TARGET_CHARGE,
                                     total_histograms=tot_hist,incidence_feasible=tot_feas,
                                     incidence_charge_below=tot_charge,common_pressure_proofs=tot_common,
                                     branch_nodes=tot_nodes,reports=pressure_reports),
                conclusion='row 108 excluded in the stated selected-incidence relaxation; no whole-state promotion')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--remainder',type=Path,required=True)
    ap.add_argument('--shared-result',type=Path,required=True)
    args=ap.parse_args()
    remainder=json.loads(args.remainder.read_text())
    shared=json.loads(args.shared_result.read_text())
    print(json.dumps(replay(remainder,shared),sort_keys=True,indent=2))

if __name__=='__main__':main()
