#!/usr/bin/env python3
"""Shared block-slack pressure: exact, standard-library internal verifier.

The parent conditioned certificate is hash-pinned. New calculations extend its
branch coverage; they do not re-audit the graph-to-incidence bridge. No solver,
float, timeout, or surviving relaxed profile is a graph-realizability claim.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, random
from collections import Counter
from itertools import product
from pathlib import Path

PARENT_HASH='7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e'
CORPUS_HASH='157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572'
INPUT_ROWS=[108,160,240,258,338,342,347,471,586]


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':')).encode()


def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def options(q,forced,eligible_low,high_excess,ceilings):
    """Each (pressure,slack cost) uses one shared low-block excess total."""
    assert high_excess>=0 and len(q)==len(forced)==len(eligible_low)==len(ceilings)
    out=[]
    for qq,f,m,D in zip(q,forced,eligible_low,ceilings):
        assert 0<=f<=qq and D>=0
        row=[]
        for d in range(D+1):
            required=f if d==0 else max(f,qq-high_excess//d)
            if required<=min(m,qq):row.append((d,required-f))
        out.append(row)
    return out


def block_options(s,q,rho,P,low,e_low):
    """low may be arbitrary but MUST contain all zero-demand labels."""
    assert len(q)==len(rho)==len(P) and all(r>=1 for r in rho)
    assert min(s+q+P,default=0)>=0 and all(s[i]>0 or i in low for i in range(len(s)))
    E=sum(q)-sum(s)
    if not 0<=e_low<=E:return None
    if not low and e_low!=0:return None
    if len(low)==len(s) and e_low!=E:return None
    f=[max(0,qq-sum(i not in low and s[i]<=r for i in range(len(s)))) for qq,r in zip(q,rho)]
    m=[sum(s[i]<=r for i in low) for r in rho]
    J=sum(s[i] for i in low)+e_low-sum(f)
    if J<0:return None
    oo=options(q,f,m,E-e_low,[max(0,p-r+1) for p,r in zip(P,rho)])
    if any(not row for row in oo):return None
    return J,oo


def dp_pressure(oo,budget,limits=None):
    """Exact only for the one-budget independent-pressure projection."""
    assert budget>=0
    if limits is None:limits=[max((d for d,_ in row),default=-1) for row in oo]
    dp={0:0}
    for row,limit in zip(oo,limits):
        nxt={}
        for used,value in dp.items():
            for d,cost in row:
                if d>limit or used+cost>budget:continue
                t=used+cost;nxt[t]=max(nxt.get(t,-1),value+d)
        dp=nxt
    return dp


def tail_box(q,rho,P,tau):
    n=len(q);c=[qq+r for qq,r in zip(q,rho)]
    A=[min(P[w],sum(u!=w and tau<=q[u]<=c[w]+1 for u in range(n))) for w in range(n)]
    free=[min(aa,r-1) for aa,r in zip(A,rho)]
    return sum(qq for qq in q if qq>=tau),sum(free),[aa-ff for aa,ff in zip(A,free)]


def best_shared(q,rho,P,budget,oo):
    best=None
    for tau in range(1,max(q,default=0)+1):
        demand,free,limits=tail_box(q,rho,P,tau)
        dp=dp_pressure(oo,budget,limits)
        if not dp:return dict(kind='empty_pressure_projection',tau=tau)
        capacity=free+max(dp.values());gap=demand-capacity
        if best is None or gap>best['gap']:
            best=dict(kind='shared_slack',tau=tau,demand=demand,free=free,budget=budget,
                      capacity=capacity,gap=gap,final_dp=sorted(dp.items()))
    return best or dict(kind='shared_slack',tau=1,demand=0,free=0,budget=budget,capacity=0,gap=0,final_dp=[[0,0]])


def baseline(p,prior):
    s,q,rho=p['s'],p['q'],p['rho']
    return prior.spill_caps(s,q,rho,prior.prior_localized(s,q,rho,prior.old_caps(p['a'],s,q,rho)))


def check_incidence(s,rho,X,D,low):
    a=len(s);n=len(rho);q=[sum(row) for row in X]
    x=[sum(row[i] for row in X) for i in range(a)];e=[xx-d for xx,d in zip(x,s)]
    assert min(e,default=0)>=0
    assert all(not X[u][i] or s[i]<=rho[u] for u in range(n) for i in range(a))
    P=[r-1+d for r,d in zip(rho,D)]
    d=[min([D[u]]+[e[i] for i in range(a) if X[u][i] and s[i]>0]) for u in range(n)]
    k=[sum(X[u][i] for i in low) for u in range(n)]
    f=[max(0,q[u]-sum(i not in low and s[i]<=rho[u] for i in range(a))) for u in range(n)]
    got=block_options(list(s),q,list(rho),P,low,sum(e[i] for i in low))
    assert got is not None
    J,oo=got;costs=[dict(row)[dd] for row,dd in zip(oo,d)]
    assert all(cost<=kk-ff for cost,kk,ff in zip(costs,k,f))
    assert sum(costs)<=J and sum(d)<=max(dp_pressure(oo,J).values())
    # A simultaneous partition cap: all block totals must use the SAME e vector.
    levels=sorted(set(s));ns=[s.count(v) for v in levels]
    es=[sum(e[i] for i in range(a) if s[i]==v) for v in levels]
    for u,dd in enumerate(d):
        available=sum((nn if not v or not dd else min(nn,ee//dd))
                      for v,nn,ee in zip(levels,ns,es) if v<=rho[u])
        assert q[u]<=available
    return J


def incidence_audit():
    counts=Counter()
    for a in range(1,4):
        for n in range(1,4):
            for masks in product(range(1<<a),repeat=n):
                X=[[(m>>i)&1 for i in range(a)] for m in masks]
                q=[sum(row) for row in X];x=[sum(row[i] for row in X) for i in range(a)]
                for ss in product(*(range(xx+1) for xx in x)):
                    s=list(ss)
                    ranges=[range(max([1]+[s[i] for i in range(a) if X[u][i]]),a-q[u]+1) for u in range(n)]
                    for rr in product(*ranges):
                        rho=list(rr);counts['incidence_configurations']+=1
                        D=[(u+sum(q)+sum(s))%5 for u in range(n)]
                        for mask in range(1<<a):
                            low={i for i in range(a) if mask>>i&1}
                            if any(s[i]==0 and i not in low for i in range(a)):continue
                            J=check_incidence(s,rho,X,D,low)
                            counts['arbitrary_block_checks']+=1;counts['positive_slack_checks']+=J>0
    rng=random.Random(742091420)
    for trial in range(10000):
        a=rng.randrange(4,13);n=rng.randrange(3,16)
        X=[[int(rng.random()<0.25) for _ in range(a)] for _ in range(n)]
        x=[sum(row[i] for row in X) for i in range(a)];q=[sum(row) for row in X]
        s=[rng.randrange(xx+1) for xx in x]
        rho=[max([1]+[s[i] for i in range(a) if X[u][i]]) for u in range(n)]
        if any(qq+r>a for qq,r in zip(q,rho)):continue
        D=[rng.randrange(7) for _ in range(n)]
        low={i for i in range(a) if s[i]==0 or rng.random()<0.5}
        check_incidence(s,rho,X,D,low);counts['random_legal_incidence']+=1
    return dict(counts=dict(counts),seed=742091420,random_trials=10000,
                domain='actual selected incidence with source/label forcing; not necessarily positive-surplus graphs')


def independent_brute_audit():
    rng=random.Random(742091421);nonempty=0;vectors=0
    for trial in range(3000):
        n=rng.randrange(1,6);q=[rng.randrange(6) for _ in range(n)]
        f=[rng.randrange(qq+1) for qq in q];m=[rng.randrange(ff,qq+1) for ff,qq in zip(f,q)]
        D=[rng.randrange(5) for _ in range(n)];H=rng.randrange(9);J=rng.randrange(7)
        oo=options(q,f,m,H,D);brute=None
        for pressure in product(*(range(dd+1) for dd in D)):
            vectors+=1;needed=[]
            for qq,ff,mm,d in zip(q,f,m,pressure):
                possible=[k-ff for k in range(ff,mm+1) if (qq-k)*d<=H]
                if not possible:break
                needed.append(min(possible))
            if len(needed)!=n or sum(needed)>J:continue
            brute=sum(pressure) if brute is None else max(brute,sum(pressure))
        got=max(dp_pressure(oo,J).values(),default=None)
        assert got==brute
        nonempty+=brute is not None
    return dict(seed=742091421,trials=3000,pressure_vectors=vectors,nonempty=nonempty)


def retained_bad_shortcut():
    # Both sources use the SAME positive label. Its excess must not be counted
    # only once when summing all sources' high-label incidence charge.
    s=[1,0];rho=[1,1];X=[[1,0],[1,0]];d=[1,1]
    assert check_incidence(s,rho,X,d,{1})==0
    return dict(s=s,rho=rho,X=X,pressure=d,high_excess=1,summed_high_incidence_charge=2,
                rejected_claim='sum_u (q_u-k_u)*d_u <= E_high',
                scope='actual incidence counterexample; not a positive-surplus graph')


def replay(remainder,parent,prior):
    assert hashlib.sha256(canonical(parent)).hexdigest()==PARENT_HASH
    assert remainder['source_sha256']==CORPUS_HASH
    byrow={p['row']:p for p in remainder['rows']}
    reports=[]
    for old in parent['replay']['reports']:
        if old['row'] not in INPUT_ROWS:continue
        p=byrow[old['row']];s,q,rho=p['s'],p['q'],p['rho'];P=baseline(p,prior)
        assert sum(q)==sum(rho)+2*p['t']+p['D0']+p['Esel']
        assert all(qq+r<=p['a'] and r>=1 for qq,r in zip(q,rho))
        splits=[]
        for sp in old['splits']:
            eta=sp['eta'];new=[];remaining=[]
            for e_low in sp['unrejected_e_low']:
                data=block_options(s,q,rho,P,{i for i,d in enumerate(s) if d<=eta},e_low)
                cert=dict(kind='infeasible_block') if data is None else best_shared(q,rho,P,*data)
                if cert['kind']!='shared_slack' or cert['gap']>0:new.append(dict(e_low=e_low,certificate=cert))
                else:remaining.append(e_low)
            interval=list(range(sp['admissible_e_low_min'],sp['admissible_e_low_max']+1))
            inherited=[e for e in interval if e not in sp['unrejected_e_low']]
            assert set(inherited)|{r['e_low'] for r in new}|set(remaining)==set(interval)
            splits.append(dict(eta=eta,range=[interval[0],interval[-1]],inherited_rejected=inherited,
                               new_certificates=new,remaining=remaining))
        reports.append(dict(row=p['row'],excluded=any(not sp['remaining'] for sp in splits),splits=splits))
    rejected=[r['row'] for r in reports if r['excluded']]
    assert rejected==[240,258,342]
    return dict(input_rows=INPUT_ROWS,parent_full_hash=PARENT_HASH,newly_excluded=rejected,
                not_excluded=[r['row'] for r in reports if not r['excluded']],reports=reports,
                scope='nine inherited synthetic non-rejections; parent branch coverage retained; no whole-state promotion')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--prior',type=Path,required=True)
    ap.add_argument('--block',type=Path,required=True)
    ap.add_argument('--remainder',type=Path,required=True)
    ap.add_argument('--parent-output',type=Path,required=True)
    args=ap.parse_args()
    prior=load_module(args.prior,'slack_prior');block=load_module(args.block,'slack_block')
    result=dict(schema='shared-block-slack-v1',external_review='OPEN',incidence=incidence_audit(),
                brute=independent_brute_audit(),hostile=block.hostile_audit(),
                false_high_mass_sum=retained_bad_shortcut(),
                replay=replay(json.loads(args.remainder.read_text()),json.loads(args.parent_output.read_text()),prior))
    print(json.dumps(result,sort_keys=True,indent=2))
if __name__=='__main__':main()
