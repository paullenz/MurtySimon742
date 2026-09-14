#!/usr/bin/env python3
"""All-source spill and clipped positive-label charge: standard-library audit.

Actual incidence matrices check soundness; the DP maximizes a NECESSARY
projection, not graph realizability. Optional frozen/synthetic inputs are hashed.
No production scanner imports. Run without -O; assertions are proof checks.
"""
from __future__ import annotations
import argparse
from collections import Counter
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path
import random
import csv


def spill_data(s, q, rho, eta):
    low = [i for i, d in enumerate(s) if d <= eta]
    forced = [max(0, qq - sum(eta < d <= r for d in s)) for qq, r in zip(q, rho)]
    return low, sum(s[i] for i in low), forced


def spill_caps(s, q, rho, initial):
    E = sum(q) - sum(s)
    if E < 0: raise ValueError('Negative selected excess')
    P = list(initial)
    for eta in sorted({0, *s}):
        low, SL, forced = spill_data(s, q, rho, eta)
        M = sum(forced)
        if M > E + SL: raise ValueError('Impossible selected-incidence spill')
        for w, (qq, r) in enumerate(zip(q, rho)):
            C = E + SL - M + forced[w]  # Remove w before counting its actual k.
            m = sum(s[i] <= r for i in low)
            k = min(qq, m, C)
            if qq > k: P[w] = min(P[w], r - 1 + (C - k) // (qq - k))
    return P


def simple_envelope(s, q, rho, delta):
    E = sum(q) - sum(s)
    M0 = sum(spill_data(s, q, rho, 0)[2])
    B = E - M0
    if B < 0: raise ValueError('Forced zero-demand excess exceeds Esel')
    return B * (max(s, default=0) + min(B, delta))


def projection(s, q, rho):
    s = tuple(sorted(s)); E = sum(q) - sum(s)
    limits = tuple(sum(qq > 0 and r >= d for qq, r in zip(q, rho)) - d for d in s)
    floors = {}
    for eta in set(s):
        low, SL, forced = spill_data(s, q, rho, eta)
        floors[len(low)] = max(0, sum(forced) - SL)
    return s, E, limits, floors


def dp_maximum(s, E, limits, floors, delta):
    if E < 0 or any(h < 0 for h in limits): return None
    best = {0: 0}
    for i, (d, h) in enumerate(zip(s, limits), 1):
        nxt = {}
        for total, value in best.items():
            for e in range(min(h, E - total) + 1):
                if total + e < floors.get(i, 0): continue
                score = value + ((d + e) * min(e, delta) if d else 0)
                nxt[total + e] = max(nxt.get(total + e, -1), score)
        best = nxt
    return best.get(E)


def envelope(s, q, rho, delta):
    return dp_maximum(*projection(s, q, rho), delta)


def old_caps(a, s, q, rho):
    b = len(q); E = sum(q) - sum(s); z = s.count(0)
    c = [qq + r for qq, r in zip(q, rho)]
    D = [[u != w and q[u] <= c[w] + 1 and q[w] <= c[u] for w in range(b)] for u in range(b)]
    P = []
    for w, qq in enumerate(q):
        degree = sum(D[w][u] or D[u][w] for u in range(b))
        cap = min(rho[w] + b - a - 1, b - 1 - qq, degree - qq)
        k = min(z, qq, E)
        if qq > k: cap = min(cap, rho[w] - 1 + (E - k) // (qq - k))
        P.append(cap)
    return P


def prior_localized(s, q, rho, initial):
    E = sum(q) - sum(s); P = list(initial)
    for eta in sorted({0, *rho}):
        m = sum(d <= eta for d in s)
        C = E + sum(d for d in s if d <= eta) - sum(qq for qq, r in zip(q, rho) if r <= eta)
        if C < 0: raise ValueError('Prior prefix infeasible')
        for w, (qq, r) in enumerate(zip(q, rho)):
            if r <= eta: continue
            k = min(m, qq, C)
            if qq > k: P[w] = min(P[w], r - 1 + (C - k) // (qq - k))
    return P


def priced_lower(q, rho, s, P):
    """Max over finite price breakpoints; a Hall deficit is returned separately."""
    b = len(q); z = s.count(0); v = [max(0, qq - z) for qq in q]
    c = [qq + r for qq, r in zip(q, rho)]
    best = (0, 1, 0); hall = False; uniform = 0; first = None
    for tau in range(1, max(q, default=0) + 1):
        demand = sum(qq for qq in q if qq >= tau)
        A = [min(P[w], sum(u != w and tau <= q[u] <= c[w] + 1 for u in range(b))) for w in range(b)]
        deficit = demand - sum(A); hall |= deficit > 0; uniform += deficit
        if deficit > 0 and first is None: first = tau
        f = [min(aa, rr - 1) for aa, rr in zip(A, rho)]; g = [aa - ff for aa, ff in zip(A, f)]
        for theta in sorted({0, *v}):
            val = theta * (demand - sum(f)) - sum(max(0, theta - vv) * gg for vv, gg in zip(v, g))
            if val > best[0]: best = (val, tau, theta)
    return dict(hall=hall, lower=best[0], tau=best[1], theta=best[2], uniform=uniform, first=first)


def rejected(test, budget):
    return test['hall'] or test['lower'] > budget


def incidence_check(s, rho, X, delta):
    a = len(s); b = len(rho); q = [sum(row) for row in X]
    x = [sum(row[i] for row in X) for i in range(a)]; e = [xx - d for xx, d in zip(x, s)]
    assert min(e, default=0) >= 0
    assert all(not X[u][i] or s[i] <= rho[u] for u in range(b) for i in range(a))
    pressure = [min([delta] + [e[i] for i in range(a) if X[u][i] and s[i] > 0]) for u in range(b)]
    cap = spill_caps(s, q, rho, [r + delta - 1 for r in rho])
    assert all(r - 1 + p <= cc for r, p, cc in zip(rho, pressure, cap))
    for eta in sorted({0, *s}):
        low, SL, forced = spill_data(s, q, rho, eta)
        for w in range(b):
            k = sum(X[w][i] for i in low)
            C = sum(e) + SL - sum(forced) + forced[w]
            if pressure[w] >= 1: assert C >= k + (q[w] - k) * pressure[w]
    charge = sum(max(0, qq - s.count(0)) * p for qq, p in zip(q, pressure))
    true_upper = sum(xx * min(ee, delta) for xx, ee, d in zip(x, e, s) if d > 0)
    upper = envelope(s, q, rho, delta)
    assert charge <= true_upper <= upper <= simple_envelope(s, q, rho, delta)


def exhaustive():
    count = 0
    for a in range(1, 4):
        for b in range(1, 5):
            for masks in product(range(1 << a), repeat=b):
                X = [[(mask >> i) & 1 for i in range(a)] for mask in masks]
                q = [sum(row) for row in X]; x = [sum(row[i] for row in X) for i in range(a)]
                for s in product(*(range(xx + 1) for xx in x)):
                    ranges = [range(max([1] + [s[i] for i in range(a) if X[u][i]]), a - q[u] + 1) for u in range(b)]
                    for rho in product(*ranges):
                        for delta in (1, 2, 4): incidence_check(s, rho, X, delta)
                        count += 1
    return dict(incidence_configurations=count,delta_values=[1,2,4],checks=3*count)


def independent_dp_audit():
    rng = random.Random(74220260915); feasible = 0
    for _ in range(3000):
        n = rng.randrange(1, 6); s = sorted(rng.randrange(4) for _ in range(n))
        h = [rng.randrange(4) for _ in s]; E = rng.randrange(9); delta = rng.randrange(1, 7)
        floors = {i:rng.randrange(E+2) for i in range(1,n+1) if rng.randrange(3)==0}
        brute = []
        for e in product(*(range(x+1) for x in h)):
            if sum(e) != E or any(sum(e[:i])<v for i,v in floors.items()): continue
            brute.append(sum((d+x)*min(x,delta) for d,x in zip(s,e) if d>0))
        expected = max(brute) if brute else None
        assert dp_maximum(s,E,h,floors,delta)==expected
        feasible += expected is not None
    return dict(trials=3000,feasible=feasible,seed=74220260915)


def hostile():
    cases=[([0,1,3,3,1,3,2],[2,1,1,1,1,1,1],[2,1,3,3,1,3,0]),([1]+[3]*6,[1]*7,[3]*7)]
    margins=[]
    for q,rho,P in cases:
        c=[x+y for x,y in zip(q,rho)];b=len(q);best=0;tail=[]
        for mask in range(1<<b):
            T=[u for u in range(b) if (mask>>u)&1]
            demand=sum(q[u] for u in T)
            H=sum(min(P[w],sum(u!=w and q[u]<=c[w]+1 and q[w]<=c[u] for u in T)) for w in range(b))
            best=min(best,H-demand)
        for tau in range(1,max(q)+2):
            T=[u for u in range(b) if q[u]>=tau]
            tail.append(sum(min(P[w],sum(u!=w and q[u]<=c[w]+1 and q[w]<=c[u] for u in T)) for w in range(b))-sum(q[u] for u in T))
        assert best==-1 and min(tail)==0
        margins.append(dict(minimum=best,tail_margins=tail))
    # Last q/rho/P is shared by both E=5,z=2 and E=19,z=4 examples.
    assert 19-5>2  # Two positive labels forced at rho=1 cannot carry S=14.
    assert 0 < 7+2  # All-zero demands violate S >= r+2t at t>=1.
    return dict(examples=3,distinct_q_rho_cap_systems=margins,bridge_rejections=['residual total exceeds choose(a,2)','selected-demand forcing','positive-surplus ledger'])


def frozen(exc, pilot):
    states={}
    for line in pilot.read_text().splitlines()[1:]:
        v=list(map(int,line.split()));layer,i,a,b,t,ns=v[:6]
        states[i]=(a,b,t,v[6:6+ns],v[7+ns:])
    C=Counter();first=Counter();changed=[]
    for row,line in enumerate(exc.read_text().splitlines()):
        fields=dict(x.split('=',1) for x in line.split('\t')[1:]);state=int(fields['state']);a,b,t,s,rr=states[state]
        q=[];rho=[];P=[]
        for item in fields['types'].split(';'):
            qq,c,p,n,*_=map(int,item.split(','));q += [qq]*n;rho += [c-qq]*n;P += [p]*n
        assert sorted(rho)==rr and sum(s)==sum(rho)+2*t
        assert old_caps(a,s,q,rho)==P
        L=prior_localized(s,q,rho,P);new=spill_caps(s,q,rho,L)
        assert all(x<=y for x,y in zip(new,L))
        test=priced_lower(q,rho,s,new);E=sum(q)-sum(s)
        C['profiles']+=1;C['tighter_than_localized']+=new!=L;C['full_cap_rejections']+=sum(new)<sum(q)
        C['uniform_interval_detections']+=test['uniform']>0;C['interval_detections']+=test['hall'];first[test['first']]+=1
        if new!=L:changed.append(dict(row=row,state=state,q=q,rho=rho,s=s,localized=L,spill=new))
    return dict(counts=dict(C),first_threshold=dict(first),changed_profiles=changed,exceptions_sha256=sha(exc),pilot_sha256=sha(pilot))


def synthetic(path):
    C=Counter();newrows=[];survivors=[];certificate=None
    for row,raw in enumerate(csv.DictReader(path.open(),delimiter='\t')):
        p={k:([int(x) for x in v.split(',')] if k in ('s','q','rho','P') else int(v)) for k,v in raw.items()}
        s,q,rho=p['s'],p['q'],p['rho'];E=p['Esel'];delta=p['b']-p['a']
        assert sum(q)==sum(rho)+2*p['t']+p['D0']+E and sum(s)==sum(q)-E
        assert len(s)==p['a'] and len(q)==p['b'] and p['z']==s.count(0)
        assert all(qq+r<=p['a'] and r>=1 for qq,r in zip(q,rho))
        assert old_caps(p['a'],s,q,rho)==p['P']
        L=prior_localized(s,q,rho,p['P']);cap=spill_caps(s,q,rho,L)
        oldtest=priced_lower(q,rho,s,L);test=priced_lower(q,rho,s,cap)
        simple=simple_envelope(s,q,rho,delta);dp=envelope(s,q,rho,delta)
        assert dp is not None and dp<=simple<=E*(E+max(s))
        original=rejected(oldtest,E*(E+max(s)));sp=rejected(test,E*(E+max(s)))
        lin=rejected(test,simple);last=rejected(test,dp)
        for k,v in [('profiles',1),('prior_priced_rejected',original),('spill_old_envelope_rejected',sp),('spill_linear_rejected',lin),('spill_dp_rejected',last),('unrejected',not last),('cap_tightened',cap!=L)]: C[k]+=v
        if last and not original:newrows.append(row)
        if not last:survivors.append(row)
        if row==4:
            assert simple==48 and dp==46 and test['lower']==57 and test['tau']==1 and test['theta']==4 and not test['hall']
            certificate=dict(p,row=row,localized=L,spill=cap,forced_zero_mass=E-8,linear_upper=simple,dp_upper=dp,priced=test)
    return dict(counts=dict(C),newly_rejected_rows=newrows,unrejected_rows=survivors,certificate=certificate,input_sha256=sha(path),scope='713 fixed-seed scalar/incidence/pair-flow relaxations; not realized graphs or full scalar states')


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exceptions',type=Path);parser.add_argument('--pilot-input',type=Path);parser.add_argument('--synthetic',type=Path)
    args=parser.parse_args()
    if bool(args.exceptions)!=bool(args.pilot_input):parser.error('Both frozen inputs are required')
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    out=dict(schema='capped-positive-excess-and-all-source-spill-v1',external_review='OPEN',exhaustive=exhaustive(),independent_dp=independent_dp_audit(),hostile=hostile())
    if args.exceptions:out['frozen_812']=frozen(args.exceptions,args.pilot_input)
    if args.synthetic:out['synthetic_713']=synthetic(args.synthetic)
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
