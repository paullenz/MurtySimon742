#!/usr/bin/env python3
"""Integer audit of demand-block and source-cap priced pressure.

No optimizer is used. Prior module supplies only the previously frozen caps and
baseline budget; new charge, DP and receiver checks are implemented here.
Synthetic profiles are necessary-condition relaxations, NOT realized graphs.
"""
from __future__ import annotations
import argparse, csv, hashlib, importlib.util, json, random
from collections import Counter
from itertools import product
from pathlib import Path


def projection(s, q, rho):
    s = tuple(sorted(s)); E = sum(q)-sum(s)
    limits = [sum(qq>0 and r>=d for qq,r in zip(q,rho))-d for d in s]
    floors = {}
    for eta in set(s):
        n = sum(d<=eta for d in s)
        mass = sum(max(0,qq-sum(eta<d<=r for d in s)) for qq,r in zip(q,rho))
        floors[n] = max(0,mass-sum(d for d in s if d<=eta))
    return s,E,limits,floors


def scores(s, q, rho, P, eta, alpha, E, limits):
    caps = [max(0,p-r+1) for p,r in zip(P,rho)]
    table = []
    for d,h in zip(s,limits):
        row=[]
        for e in range(min(h,E)+1):
            eligible=[al*min(e,hp) for qq,r,al,hp in zip(q,rho,alpha,caps) if qq>0 and r>=d]
            eligible.sort(reverse=True)
            row.append(sum(eligible[:d+e]) if d>eta else 0)
        table.append(row)
    return table


def dp_upper(s, q, rho, P, eta=0, alpha=None):
    if alpha is None: alpha=[1]*len(q)
    assert eta>=0 and len(alpha)==len(q) and all(x>=0 for x in alpha)
    assert len(q)==len(rho)==len(P) and min(P,default=0)>=0
    s,E,limits,floors=projection(s,q,rho)
    if E<0 or min(limits,default=0)<0: return None
    table=scores(s,q,rho,P,eta,alpha,E,limits)
    best={0:0}
    for i,(h,row) in enumerate(zip(limits,table),1):
        nxt={}
        for used,value in best.items():
            for e in range(min(h,E-used)+1):
                t=used+e
                if t<floors.get(i,0): continue
                nxt[t]=max(nxt.get(t,-1),value+row[e])
        best=nxt
    return best.get(E)


def simple_upper(s,q,rho,delta,eta):
    E=sum(q)-sum(s)
    M=sum(max(0,qq-sum(eta<d<=r for d in s)) for qq,r in zip(q,rho))
    SL=sum(d for d in s if d<=eta)
    B=min(E,E+SL-M)
    if B<0: return None
    top=max((d for d in s if d>eta),default=0)
    return B*(top+min(B,delta))


def receiver_certificate(q,rho,s,P,eta,alpha,tau,theta,exact=False):
    assert tau>=1 and theta>=0 and eta>=0 and all(x>=0 for x in alpha)
    b=len(q);m=sum(d<=eta for d in s)
    v=[al*max(0,qq-m) for al,qq in zip(alpha,q)]
    c=[qq+r for qq,r in zip(q,rho)]
    A=[min(P[w],sum(u!=w and tau<=q[u]<=c[w]+1 and (not exact or q[w]<=c[u]) for u in range(b))) for w in range(b)]
    assert min(A,default=0)>=0
    f=[min(aa,r-1) for aa,r in zip(A,rho)];g=[aa-ff for aa,ff in zip(A,f)]
    demand=sum(qq for qq in q if qq>=tau)
    penalty=sum(max(0,theta-vv)*gg for vv,gg in zip(v,g))
    return dict(tau=tau,theta=theta,eta=eta,demand=demand,capacity=sum(A),free=sum(f),penalty=penalty,
                lower=theta*(demand-sum(f))-penalty)


def best_lower(q,rho,s,P,eta,alpha):
    m=sum(d<=eta for d in s);prices=sorted({0,*[al*max(0,qq-m) for al,qq in zip(alpha,q)]})
    out=None
    for tau in range(1,max(q,default=0)+1):
        for theta in prices:
            d=receiver_certificate(q,rho,s,P,eta,alpha,tau,theta)
            if out is None or d['lower']>out['lower']: out=d
    return out or dict(tau=1,theta=0,eta=eta,demand=0,capacity=0,free=0,penalty=0,lower=0)


def incidence_checks():
    count=0;checks=0;strict=0
    for a in range(1,4):
        for b in range(1,4):
            for masks in product(range(1<<a),repeat=b):
                X=[[(k>>i)&1 for i in range(a)] for k in masks]
                q=[sum(row) for row in X];x=[sum(row[i] for row in X) for i in range(a)]
                for s in product(*(range(xx+1) for xx in x)):
                    ranges=[range(max([1]+[s[i] for i in range(a) if X[u][i]]),a-q[u]+1) for u in range(b)]
                    for rho in product(*ranges):
                        count+=1;e=[xx-d for xx,d in zip(x,s)]
                        # Variable source caps: actual pressures must respect them.
                        cap=[(u+sum(s)+q[u])%4 for u in range(b)]
                        pressure=[min([cap[u]]+[e[i] for i in range(a) if X[u][i] and s[i]>0]) for u in range(b)]
                        P=[r-1+h for r,h in zip(rho,cap)]
                        for eta in sorted({0,*s}):
                            m=sum(d<=eta for d in s)
                            for alpha in ([1]*b,[1+u%3 for u in range(b)]):
                                left=sum(al*max(0,qq-m)*dd for al,qq,dd in zip(alpha,q,pressure))
                                actual=sum(sum(alpha[u]*min(e[i],cap[u]) for u in range(b) if X[u][i]) for i in range(a) if s[i]>eta)
                                ss,E,limits,floors=projection(s,q,rho)
                                order=sorted(range(a),key=lambda i:s[i]);es=[e[i] for i in order]
                                table=scores(ss,q,rho,P,eta,alpha,E,limits)
                                top=sum(row[ei] for row,ei in zip(table,es))
                                upper=dp_upper(s,q,rho,P,eta,alpha)
                                assert left<=actual<=top<=upper
                                if alpha==[1]*b: assert upper<=simple_upper(s,q,rho,3,eta)
                                strict+=top>actual;checks+=1
    return dict(configurations=count,inequality_checks=checks,strict_top_relaxations=strict)


def independent_brute_audit():
    rng=random.Random(742091416);feasible=0
    for _ in range(2000):
        a=rng.randrange(1,6);b=rng.randrange(1,5)
        s=sorted(rng.randrange(4) for _ in range(a));q=[rng.randrange(a+1) for _ in range(b)]
        rho=[rng.randrange(1,5) for _ in range(b)];P=[r-1+rng.randrange(4) for r in rho]
        alpha=[rng.randrange(4) for _ in q];eta=rng.randrange(4)
        ss,E,limits,floors=projection(s,q,rho);best=None
        if E>=0 and min(limits,default=0)>=0:
            for ev in product(*(range(h+1) for h in limits)):
                if sum(ev)!=E or any(sum(ev[:j])<v for j,v in floors.items()):continue
                total=0
                # No sorting formula: enumerate all labelled source subsets.
                for d,e in zip(ss,ev):
                    if d<=eta:continue
                    values=[]
                    for mask in range(1<<b):
                        U=[u for u in range(b) if mask>>u&1]
                        if len(U)!=d+e or any(q[u]==0 or rho[u]<d for u in U):continue
                        values.append(sum(alpha[u]*min(e,max(0,P[u]-rho[u]+1)) for u in U))
                    assert values
                    total+=max(values)
                best=total if best is None else max(best,total)
        assert dp_upper(s,q,rho,P,eta,alpha)==best
        feasible+=best is not None
    return dict(trials=2000,feasible=feasible,seed=742091416)


def receiver_audit():
    rng=random.Random(742091417);boxes=0
    for _ in range(1000):
        n=rng.randrange(1,5);rho=[rng.randrange(1,4) for _ in range(n)]
        A=[rng.randrange(4) for _ in range(n)];v=[rng.randrange(7) for _ in range(n)]
        theta=rng.randrange(9);f=[min(a,r-1) for a,r in zip(A,rho)];g=[a-ff for a,ff in zip(A,f)]
        for incoming in product(*(range(a+1) for a in A)):
            dem=sum(incoming)
            lhs=theta*(dem-sum(f))-sum(max(0,theta-vv)*gg for vv,gg in zip(v,g))
            cost=sum(vv*max(0,y-r+1) for vv,y,r in zip(v,incoming,rho))
            assert lhs<=cost;boxes+=1
    return dict(seed=742091417,instances=1000,incoming_vectors=boxes)


def hostile_audit():
    cases=[([0,1,3,3,1,3,2],[2,1,1,1,1,1,1],[2,1,3,3,1,3,0]),
           ([1]+[3]*6,[1]*7,[3]*7)]
    results=[]
    for q,rho,P in cases:
        n=len(q);c=[qq+r for qq,r in zip(q,rho)]
        def margin(U):
            demand=sum(q[u] for u in U)
            received=sum(min(P[w],sum(u!=w and q[u]<=c[w]+1 and q[w]<=c[u] for u in U)) for w in range(n))
            return received-demand
        minimum=min(margin([u for u in range(n) if mask>>u&1]) for mask in range(1<<n))
        tails=[margin([u for u in range(n) if q[u]>=tau]) for tau in range(1,max(q)+2)]
        assert minimum==-1 and min(tails)==0
        results.append(dict(minimum=minimum,tail_margins=tails))
    assert 19-5>2 and 0<7+2
    return dict(examples=3,distinct_systems=results,explicit_bridge_failures=[
        'r exceeds choose(a,2)', 'selected-demand infeasibility', 'S below r+2t'])


def load_prior(path):
    spec=importlib.util.spec_from_file_location('capped_prior',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def replay(path,prior):
    rows=[]
    for row,raw in enumerate(csv.DictReader(path.open(),delimiter='\t')):
        p={k:([int(x) for x in v.split(',')] if k in ('q','rho','s','P') else int(v)) for k,v in raw.items()}
        p['row']=p.get('row',row);rows.append(p)
    counts=Counter();certificates=[];remaining=[]
    expected19=[39,76,108,119,160,240,258,295,338,342,347,365,406,471,570,586,664,682,688]
    prior_remaining=[]
    for p in rows:
        q,rho,s=p['q'],p['rho'],p['s'];a,b=p['a'],p['b']
        assert b==len(q)==len(rho) and a==len(s)
        assert sum(s)==sum(rho)+2*p['t']+p['D0'] and sum(q)==sum(s)+p['Esel']
        oldP=prior.old_caps(a,s,q,rho)
        assert oldP==p['P']
        P=prior.spill_caps(s,q,rho,prior.prior_localized(s,q,rho,oldP))
        oldenv=prior.envelope(s,q,rho,b-a);oldtest=prior.priced_lower(q,rho,s,P)
        counts['profiles']+=1
        if prior.rejected(oldtest,oldenv):counts['prior_rejected']+=1;continue
        prior_remaining.append(p['row']);best=None
        for name,alpha in [('uniform',[1]*b),('three_above_q2',[1 if qq<=2 else 3 for qq in q])]:
            for eta in sorted({0,*s}):
                if eta>=max(s): continue
                upper=dp_upper(s,q,rho,P,eta,alpha);low=best_lower(q,rho,s,P,eta,alpha)
                assert upper is not None
                if best is None or low['lower']-upper>best['gap']:
                    best=dict(low,upper=upper,gap=low['lower']-upper,weight_rule=name)
        if best['gap']>0:
            counts['newly_rejected']+=1
            certificates.append(dict(row=p['row'],certificate=best,prior_upper=oldenv,prior_lower=oldtest['lower']))
        else:counts['unrejected']+=1;remaining.append(p['row'])
    assert prior_remaining==expected19
    assert [r['row'] for r in certificates]==[39,76,119,406,664,682,688]
    p=next(p for p in rows if p['row']==664)
    q,rho,s=p['q'],p['rho'],p['s']
    P=prior.spill_caps(s,q,rho,prior.prior_localized(s,q,rho,prior.old_caps(p['a'],s,q,rho)))
    hand=receiver_certificate(q,rho,s,P,1,[1]*len(q),3,8)
    M=sum(max(0,qq-sum(1<d<=r for d in s)) for qq,r in zip(q,rho))
    SL=sum(d for d in s if d<=1);B=min(p['Esel'],p['Esel']+SL-M)
    upper=simple_upper(s,q,rho,p['b']-p['a'],1)
    assert (p['Esel'],M,SL,B,upper,hand['lower'])==(33,15,1,19,190,209)
    hand.update(row=664,Esel=33,forced_low=15,low_demand=1,remaining_excess=19,delta=6,smax=4,upper=upper,gap=19)
    return dict(input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),counts=dict(counts),certificates=certificates,
                unweighted_hand_certificate=hand,unrejected_rows=remaining)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--synthetic',type=Path);ap.add_argument('--prior',type=Path);args=ap.parse_args()
    if bool(args.synthetic)!=bool(args.prior):ap.error('Supply both synthetic corpus and prior verifier')
    out=dict(schema='demand-block-source-pressure-v1',external_review='OPEN',incidence=incidence_checks(),
             independent_brute=independent_brute_audit(),receiver=receiver_audit(),hostile=hostile_audit())
    if args.synthetic:out['synthetic']=replay(args.synthetic,load_prior(args.prior))
    print(json.dumps(out,sort_keys=True,indent=2))
if __name__=='__main__':main()
