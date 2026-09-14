#!/usr/bin/env python3
"""Independent integer audit of high-q interval/bridge-budget identities.

Standard library only. This checks identities and one-sided bounds, NOT universal
q-tail sufficiency or realizability by diameter-two-critical graphs.
"""
from __future__ import annotations
import argparse, collections, hashlib, itertools, json, random
from pathlib import Path
from typing import Sequence


def directed(q: Sequence[int], rho: Sequence[int]) -> list[list[bool]]:
    c = [x+y for x,y in zip(q,rho)]
    return [[u != w and q[u] <= c[w]+1 and q[w] <= c[u]
             for w in range(len(q))] for u in range(len(q))]


def target_caps(a: int, q: list[int], rho: list[int], Esel: int, z: int) -> list[int]:
    """All four current caps. Negative values are infeasibility, never clipped."""
    b = len(q); D = directed(q,rho)
    deg = [sum(D[u][w] or D[w][u] for w in range(b)) for u in range(b)]
    out = []
    for u in range(b):
        caps = [rho[u]+b-a-1, b-1-q[u], deg[u]-q[u]]
        kstar = min(z, q[u], Esel)
        if q[u] > kstar:
            caps.append(rho[u]-1+(Esel-kstar)//(q[u]-kstar))
        P = min(caps)
        if q[u]+rho[u] <= a:
            losses = [0, q[u]+rho[u]+b-a-1-deg[u]]
            if q[u] > kstar:
                losses.append(b-a-(Esel-kstar)//(q[u]-kstar))
            assert rho[u]+b-a-1-P == max(losses)
        if q[u]+rho[u] <= a and b-a >= 0:
            thresholds=[min(Esel,z)+max(Esel-z,0)//j+1 for j in range(1,b-a+1)]
            ell=sum(q[u]>=v for v in thresholds)
            eta=max(0,q[u]+rho[u]+b-a-1-deg[u]-ell)
            assert P==rho[u]+b-a-1-ell-eta
        out.append(P)
    return out


def check(q: Sequence[int], rho: Sequence[int], P: Sequence[int],
          a: int | None = None, t: int | None = None,
          D0: int | None = None, Esel: int | None = None,
          weights: Sequence[int] | None = None) -> dict:
    b=len(q)
    assert b and len(rho)==b and len(P)==b
    assert all(isinstance(x,int) and x>=0 for v in (q,rho,P) for x in v)
    c=[q[u]+rho[u] for u in range(b)]; K=max(q)
    D=directed(q,rho)
    hist=collections.Counter(q)
    # A histogram implementation independent of the direct labelled counts.
    def N(j: int) -> int:
        return sum(count for value,count in hist.items() if value>=j)
    if weights is None:
        weights=[1+(j%3) for j in range(K)]
    assert len(weights)==K and all(isinstance(x,int) and x>=0 for x in weights)
    phi=[0]
    for weight in weights: phi.append(phi[-1]+weight)
    out=[]
    for tau in range(1,K+2):
        chosen=[u for u in range(b) if q[u]>=tau]
        demand=sum(q[u] for u in chosen)
        y=[sum(D[u][w] for u in chosen) for w in range(b)]
        J=[max(0,N(tau)-N(c[w]+2))-int(q[w]>=tau) for w in range(b)]
        bruteJ=[sum(u!=w and q[u]<=c[w]+1 for u in chosen) for w in range(b)]
        assert J==bruteJ and all(J[w]>=y[w]>=0 for w in range(b))
        H=sum(min(P[w],y[w]) for w in range(b))
        U=sum(min(P[w],J[w]) for w in range(b))
        blocked=[sum(u!=w and q[u]<=c[w]+1 and c[u]<q[w] for u in chosen) for w in range(b)]
        assert blocked == [sum(q[u]>=tau and c[u]<q[w] for u in range(b)) for w in range(b)]
        assert all(J[w]-blocked[w]==y[w] for w in range(b))
        assert all(blocked[w]==0 for w in range(b) if q[w]<=tau+min(rho))
        Xi=sum(max(0,blocked[w]-max(0,J[w]-P[w])) for w in range(b))
        Omega=sum(max(0,P[w]-J[w]) for w in range(b))
        assert Xi==U-H and U==sum(P)-Omega and demand-U<=demand-H
        row=dict(tau=tau,demand=demand,H=H,U=U,Omega=Omega,Xi=Xi,
                 deficiency=demand-H,interval_lower=demand-U)
        if a is not None:
            assert None not in (t,D0,Esel)
            r=sum(rho); Q=sum(q); B=2*t+D0+Esel
            assert Q==r+B and D0>=0 and Esel>=0 and t>=0
            assert all(cw<=a for cw in c)
            h=[rho[w]+b-a-1 for w in range(b)]
            G=b*(b-a-1)-B
            assert G>=0 and all(h[w]>=P[w] for w in range(b))
            cap_loss=sum(h[w]-P[w] for w in range(b))
            low=sum(q[u] for u in range(b) if q[u]<tau)
            assert demand-U==cap_loss+Omega-low-G
            assert demand-H==cap_loss+Omega+Xi-low-G
            row.update(G=G,cap_loss=cap_loss,low_demand=low)
        out.append(row)
    # Independently check both exact and interval weighted top-compatible sums.
    lhs=sum(q[u]*phi[q[u]] for u in range(b))
    receiver=0; interval_receiver=0
    for w in range(b):
        values=sorted((q[u] for u in range(b) if D[u][w]),reverse=True)
        ivals=sorted((q[u] for u in range(b) if u!=w and q[u]<=c[w]+1),reverse=True)
        receiver+=sum(phi[x] for x in values[:P[w]])
        interval_receiver+=sum(phi[x] for x in ivals[:P[w]])
    assert lhs-receiver==sum(weights[j]*out[j]['deficiency'] for j in range(K))
    assert lhs-interval_receiver==sum(weights[j]*out[j]['interval_lower'] for j in range(K))
    assert receiver<=interval_receiver
    if sum(weights[j]*out[j]['interval_lower'] for j in range(K))>0:
        assert any(row['deficiency']>0 for row in out)
    return dict(rows=out,weighted_deficiency=lhs-receiver,
                weighted_interval_lower=lhs-interval_receiver)


def brute_minimum(q: Sequence[int],rho: Sequence[int],P: Sequence[int]) -> int:
    b=len(q); D=directed(q,rho); best=0
    for mask in range(1<<b):
        ids=[u for u in range(b) if mask>>u&1]
        margin=sum(min(P[w],sum(D[u][w] for u in ids)) for w in range(b))-sum(q[u] for u in ids)
        best=min(best,margin)
    return best


def self_test(random_trials: int) -> dict:
    types=list(itertools.product(range(3),range(2),range(3)))
    exhaustive=0; positive_reverse=0; strict_interval_misses=0; first_reverse=None; first_miss=None
    for b in range(1,5):
        for profile in itertools.combinations_with_replacement(types,b):
            q,rho,P=map(list,zip(*profile)); result=check(q,rho,P); exhaustive+=1
            if any(r['Xi']>0 for r in result['rows']):
                positive_reverse+=1
                if first_reverse is None: first_reverse=dict(q=q,rho=rho,P=P,**result)
            if max(r['deficiency'] for r in result['rows'])>0 and max(r['interval_lower'] for r in result['rows'])<=0:
                strict_interval_misses+=1
                if first_miss is None: first_miss=dict(q=q,rho=rho,P=P,**result)
    rng=random.Random(7420914)
    random_reverse=0
    for _ in range(random_trials):
        b=rng.randint(1,12)
        q=[rng.randrange(9) for _ in range(b)];rho=[rng.randrange(9) for _ in range(b)];P=[rng.randrange(b+1) for _ in range(b)]
        result=check(q,rho,P,weights=[rng.randrange(5) for _ in range(max(q))])
        random_reverse+=any(r['Xi']>0 for r in result['rows'])
    scalar_cases=0
    for delta,q,E,z in itertools.product(range(7),range(25),range(41),range(25)):
        kstar=min(z,q,E)
        direct=max(0,delta-(E-kstar)//(q-kstar)) if q>kstar else 0
        tails=sum(q>=min(E,z)+max(E-z,0)//j+1 for j in range(1,delta+1))
        assert direct==tails
        scalar_cases+=1
    hostile=[]
    fixtures=[('arbitrary_monotone',[0,1,3,3,1,3,2],[2,1,1,1,1,1,1],[2,1,3,3,1,3,0],None,None),
              ('cap_formula_only',[1]+[3]*6,[1]*7,[3]*7,5,2),
              ('all_zero_demands',[1]+[3]*6,[1]*7,[3]*7,19,4)]
    for name,q,rho,P,E,z in fixtures:
        if E is not None: assert target_caps(4,q,rho,E,z)==P
        result=check(q,rho,P);minimum=brute_minimum(q,rho,P)
        assert minimum==-1 and max(r['deficiency'] for r in result['rows'])==0
        hostile.append(dict(name=name,q=q,rho=rho,P=P,Esel=E,z=z,
                            minimum_Hall_margin=minimum,maximum_tail_deficiency=0))
    return dict(exhaustive_profiles=exhaustive,exhaustive_positive_reverse_profiles=positive_reverse,
                exhaustive_interval_detection_misses=strict_interval_misses,
                first_abstract_reverse_gap=first_reverse,first_abstract_interval_miss=first_miss,
                scalar_selected_tail_loss_cases=scalar_cases,random_seed=7420914,random_trials=random_trials,random_positive_reverse_profiles=random_reverse,
                hostile=hostile,status='PASS',scope='identities and upper bounds only; no universal tail sufficiency')


def main() -> None:
    ap=argparse.ArgumentParser();ap.add_argument('--random-trials',type=int,default=5000);ap.add_argument('--output',type=Path);ap.add_argument('--obstruction',type=Path)
    args=ap.parse_args();result=self_test(args.random_trials)
    if args.obstruction:
        cert=json.loads(args.obstruction.read_text());K=cert['K'];total=[0]*K
        for p in cert['profiles']:
            assert target_caps(p['a'],p['q'],p['rho'],p['Esel'],p['s'].count(0))==p['P']
            checked=check(p['q'],p['rho'],p['P'],p['a'],p['t'],p['D0'],p['Esel'])
            ds=[next((r['deficiency'] for r in checked['rows'] if r['tau']==tau),0) for tau in range(1,K+1)]
            assert ds==p['deficiencies'] and p['weight']>0 and max(ds)>0
            total=[x+p['weight']*y for x,y in zip(total,ds)]
        assert total==cert['weighted_sum_deficiencies'] and all(x<=0 for x in total)
        result['fixed_weight_obstruction']='PASS: exact integer combination, no optimization solver used'

    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(text)
    print(text,end='')

if __name__=='__main__':main()
