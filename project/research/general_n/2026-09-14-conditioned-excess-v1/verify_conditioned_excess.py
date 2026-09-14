#!/usr/bin/env python3
"""Conditioned spill-slack caps, exact budget splits and row-295 hand audit.

Standard library only. Inputs are selected-incidence/bridge projections, not
realized Murty graphs. Prior modules provide frozen caps and price arithmetic;
the new conditional cap, conditional DP and independent brute audit live here.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, random
from collections import Counter
from itertools import product
from pathlib import Path

EXPECTED_ROWS = [108,160,240,258,295,338,342,347,365,471,570,586]
NEW_EXCLUSIONS = [295,365,570]


def conditional_caps(s, q, rho, P, eta, e_low):
    """None means the specified low-block total is infeasible, not a timeout."""
    assert eta >= 0 and len(q)==len(rho)==len(P)
    assert all(x>=0 for x in s+q+P) and all(r>=1 for r in rho)
    E=sum(q)-sum(s)
    if not 0<=e_low<=E:return None
    low=[i for i,d in enumerate(s) if d<=eta]
    if not low and e_low!=0:return None
    if len(low)==len(s) and e_low!=E:return None
    SL=sum(s[i] for i in low)
    forced=[max(0,qq-sum(eta<d<=r for d in s)) for qq,r in zip(q,rho)]
    slack=e_low+SL-sum(forced)
    if slack<0:return None
    result=list(P)
    for u,(qq,r) in enumerate(zip(q,rho)):
        m=sum(s[i]<=r for i in low)
        k_max=min(qq,m,forced[u]+slack)
        if qq>k_max:
            result[u]=min(result[u],r-1+(E-e_low)//(qq-k_max))
    return result


def conditional_upper(s,q,rho,P,eta,e_low,charge_eta,alpha):
    """Integer top-source envelope with exact excess total on one prefix."""
    assert len(alpha)==len(q) and min(alpha,default=0)>=0 and charge_eta>=0
    ss=sorted(s);E=sum(q)-sum(ss);n_low=sum(d<=eta for d in ss)
    if E<0 or not 0<=e_low<=E:return None
    if n_low==0 and e_low!=0:return None
    if n_low==len(ss) and e_low!=E:return None
    limits=[sum(qq>0 and r>=d for qq,r in zip(q,rho))-d for d in ss]
    if min(limits,default=0)<0:return None
    floors={}
    for t in set(ss):
        n=sum(d<=t for d in ss)
        spill=sum(max(0,qq-sum(t<d<=r for d in ss)) for qq,r in zip(q,rho))
        floors[n]=max(0,spill-sum(d for d in ss if d<=t))
    ceilings=[max(0,pp-r+1) for pp,r in zip(P,rho)]
    best={0:0}
    for i,(d,h) in enumerate(zip(ss,limits),1):
        score=[]
        for e in range(min(h,E)+1):
            values=sorted((al*min(e,D) for qq,r,al,D in zip(q,rho,alpha,ceilings) if qq>0 and r>=d),reverse=True)
            score.append(sum(values[:d+e]) if d>charge_eta else 0)
        nxt={}
        for used,value in best.items():
            for e in range(min(h,E-used)+1):
                total=used+e
                if total<floors.get(i,0):continue
                if i<n_low and total>e_low:continue
                if i==n_low and total!=e_low:continue
                value2=value+score[e]
                if total not in nxt or value2>nxt[total]:nxt[total]=value2
        best=nxt
    return best.get(E)


def check_incidence(s,rho,X,D):
    a=len(s);b=len(rho);q=[sum(row) for row in X]
    x=[sum(row[i] for row in X) for i in range(a)];ev=[xx-d for xx,d in zip(x,s)]
    assert min(ev,default=0)>=0
    assert all(not X[u][i] or s[i]<=rho[u] for u in range(b) for i in range(a))
    pressure=[min([D[u]]+[ev[i] for i in range(a) if X[u][i] and s[i]>0]) for u in range(b)]
    P=[r-1+d for r,d in zip(rho,D)];checks=0
    for eta in sorted({0,*s,max(s,default=0)+1}):
        e_low=sum(e for e,d in zip(ev,s) if d<=eta)
        cap=conditional_caps(s,q,rho,P,eta,e_low)
        assert cap is not None
        assert all(r-1+d<=p for r,d,p in zip(rho,pressure,cap))
        alpha=[1+u%3 for u in range(b)]
        for ce in sorted({0,eta}):
            left=sum(al*max(0,qq-sum(d<=ce for d in s))*dd for al,qq,dd in zip(alpha,q,pressure))
            upper=conditional_upper(s,q,rho,cap,eta,e_low,ce,alpha)
            assert upper is not None and left<=upper
            checks+=1
    return checks


def exhaustive_incidence():
    profiles=checks=0
    for a in range(1,4):
        for b in range(1,4):
            for masks in product(range(1<<a),repeat=b):
                X=[[(mask>>i)&1 for i in range(a)] for mask in masks]
                q=[sum(row) for row in X];x=[sum(row[i] for row in X) for i in range(a)]
                for s0 in product(*(range(xx+1) for xx in x)):
                    s=list(s0)
                    ranges=[range(max([1]+[s[i] for i in range(a) if X[u][i]]),a-q[u]+1) for u in range(b)]
                    for rho0 in product(*ranges):
                        rho=list(rho0);D=[(u+sum(s)+q[u])%5 for u in range(b)]
                        checks+=check_incidence(s,rho,X,D);profiles+=1
    return dict(configurations=profiles,conditioned_inequalities=checks,a_max=3,b_max=3)


def independent_brute_audit():
    rng=random.Random(742091418);nonempty=0
    for _ in range(2000):
        a=rng.randrange(1,6);b=rng.randrange(1,5)
        s=sorted(rng.randrange(4) for _ in range(a));q=[rng.randrange(a+1) for _ in range(b)]
        rho=[rng.randrange(1,5) for _ in range(b)];P=[r-1+rng.randrange(5) for r in rho]
        eta=rng.randrange(5);ce=rng.randrange(4);alpha=[rng.randrange(4) for _ in q]
        E=sum(q)-sum(s);e_low=rng.randrange(max(0,E)+2);answer=None
        limits=[sum(qq>0 and r>=d for qq,r in zip(q,rho))-d for d in s]
        if E>=0 and min(limits,default=0)>=0:
            for es in product(*(range(h+1) for h in limits)):
                if sum(es)!=E or sum(e for d,e in zip(s,es) if d<=eta)!=e_low:continue
                ok=True
                for t in set(s):
                    occupied=sum(d+e for d,e in zip(s,es) if d<=t)
                    forced=sum(max(0,qq-sum(t<d<=r for d in s)) for qq,r in zip(q,rho))
                    if occupied<forced:ok=False;break
                if not ok:continue
                total=0
                for d,e in zip(s,es):
                    if d<=ce:continue
                    vals=[]
                    for mask in range(1<<b):
                        U=[u for u in range(b) if mask>>u&1]
                        if len(U)!=d+e or any(q[u]==0 or rho[u]<d for u in U):continue
                        vals.append(sum(alpha[u]*min(e,max(0,P[u]-rho[u]+1)) for u in U))
                    assert vals
                    total+=max(vals)
                answer=total if answer is None else max(answer,total)
        got=conditional_upper(s,q,rho,P,eta,e_low,ce,alpha)
        assert got==answer,(s,q,rho,eta,e_low,ce,got,answer)
        nonempty+=answer is not None
    return dict(seed=742091418,trials=2000,nonempty=nonempty)


def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def old_caps(p,prior):
    s,q,rho=p['s'],p['q'],p['rho']
    return prior.spill_caps(s,q,rho,prior.prior_localized(s,q,rho,prior.old_caps(p['a'],s,q,rho)))


def hand295(p,prior):
    s,q,rho=p['s'],p['q'],p['rho'];P=old_caps(p,prior)
    D=[max(0,pp-r+1) for pp,r in zip(P,rho)]
    E=sum(q)-sum(s);low=[u for u,qq in enumerate(q) if qq==2]
    assert Counter(s)=={1:2,2:3,3:3,4:16}
    assert len(low)==12 and all(rho[u]==1 and D[u]==4 for u in low)
    assert all(qq>=2 for qq in q) and q.count(3)==4
    forced_low=12*2-2;high=E-forced_low
    assert (sum(q),sum(rho),E,forced_low,high)==(109,79,28,22,6)
    table={}
    for demand in (2,3,4):
        vals=[]
        for e in range(high+1):
            candidates=sorted((min(e,D[u]) for u in range(len(q)) if q[u]>0 and rho[u]>=demand),reverse=True)
            value=sum(candidates[:demand+e]);assert value<=5*e;vals.append(value)
        table[demand]=vals
    assert max(D)<=4
    # Lower charge: C >= 3*sum d - sum_{q=2}d >= 3*(Q-free)-48.
    free=sum(r-1 for r in rho);lower=3*(sum(q)-free)-12*4
    # Upper charge: 4*(2+E_low)+5*(E-E_low)<=126, equality forces E_low=22.
    upper=4*(2+forced_low)+5*high
    assert lower==upper==126
    required_q3_pressure=(sum(q)-free)-12*4
    allowed_q3_pressure=q.count(3)*(high//3)
    assert required_q3_pressure==10 and allowed_q3_pressure==8
    return dict(row=295,Q=sum(q),r=sum(rho),Esel=E,free=free,P=P,D=D,
                forced_low_excess=forced_low,remaining_high_excess=high,top_source_table=table,
                charge_lower=lower,charge_upper=upper,required_q3_pressure=10,maximum_q3_pressure=8,
                contradiction='equality would force 10 <= 8')


def replay(rows,prior,block):
    assert [p['row'] for p in rows]==EXPECTED_ROWS
    outputs=[]
    for p in rows:
        s,q,rho=p['s'],p['q'],p['rho'];E=p['Esel'];P=old_caps(p,prior)
        assert len(s)==p['a'] and len(q)==len(rho)==p['b']
        assert all(r>=1 and qq+r<=p['a'] for qq,r in zip(q,rho))
        assert sum(s)==sum(rho)+2*p['t']+p['D0'] and sum(q)==sum(s)+E
        assert prior.old_caps(p['a'],s,q,rho)==p['P']
        reports=[]
        for eta in sorted(set(s))[:-1]:
            M=sum(max(0,qq-sum(eta<d<=r for d in s)) for qq,r in zip(q,rho))
            SL=sum(d for d in s if d<=eta);branches=[];unrejected=[]
            for e_low in range(max(0,M-SL),E+1):
                pc=conditional_caps(s,q,rho,P,eta,e_low)
                if pc is None:
                    branches.append(dict(e_low=e_low,reason='infeasible_split'));continue
                if sum(pc)<sum(q):
                    branches.append(dict(e_low=e_low,reason='total_capacity',gap=sum(q)-sum(pc)));continue
                best=None
                for ce in sorted({0,eta}):
                    for weighted,alpha in [(False,[1]*len(q)),(True,[1 if qq<=2 else 3 for qq in q])]:
                        upper=conditional_upper(s,q,rho,pc,eta,e_low,ce,alpha)
                        if upper is None:best=dict(e_low=e_low,reason='empty_projection');break
                        low=block.best_lower(q,rho,s,pc,ce,alpha);gap=low['lower']-upper
                        if best is None or gap>best.get('gap',-10**9):
                            best=dict(e_low=e_low,reason='price',upper=upper,lower=low['lower'],gap=gap,
                                      charge_eta=ce,weighted=weighted,tau=low['tau'],theta=low['theta'])
                        if gap>0:break
                    if best['reason']=='empty_projection' or best.get('gap',0)>0:break
                if best['reason']!='empty_projection' and best.get('gap',0)<=0:unrejected.append(e_low)
                branches.append(best)
            reports.append(dict(eta=eta,admissible_e_low_min=max(0,M-SL),admissible_e_low_max=E,
                                branches=branches,unrejected_e_low=unrejected))
            if not unrejected:break
        outputs.append(dict(row=p['row'],excluded=not reports[-1]['unrejected_e_low'],splits=reports))
    new=[r['row'] for r in outputs if r['excluded']]
    assert new==NEW_EXCLUSIONS
    return dict(input_rows=EXPECTED_ROWS,newly_excluded=new,not_excluded=[r['row'] for r in outputs if not r['excluded']],
                reports=outputs,hand295=hand295(next(p for p in rows if p['row']==295),prior))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--prior',required=True,type=Path)
    ap.add_argument('--block',required=True,type=Path)
    ap.add_argument('--remainder',required=True,type=Path)
    args=ap.parse_args()
    prior=load_module(args.prior,'prior_caps');block=load_module(args.block,'prior_block')
    raw=json.loads(args.remainder.read_text());assert raw['source_sha256']=='157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572'
    result=dict(schema='conditioned-spill-slack-v1',external_review='OPEN',
                source_corpus_sha256=raw['source_sha256'],incidence=exhaustive_incidence(),
                independent_brute=independent_brute_audit(),hostile=block.hostile_audit(),
                replay=replay(raw['rows'],prior,block))
    print(json.dumps(result,sort_keys=True,indent=2))
if __name__=='__main__':main()
