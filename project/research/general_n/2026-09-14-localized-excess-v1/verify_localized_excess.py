#!/usr/bin/env python3
"""Independent finite checks of the localized selected-excess cap.

The exhaustive/random inputs are incidence systems, NOT realized Murty graphs.
No imports from either production C++ verifier. Python standard library only.
Optional --exceptions and --pilot-input replay the frozen 812 diagnostic.
"""
from __future__ import annotations
import argparse
from collections import Counter, deque
import hashlib
from itertools import product
import json
from pathlib import Path
import random
from typing import Sequence

SEED = 7420914
SURVIVORS = [
    dict(id=1626,a=15,b=18,t=1,s=[1,2,2,3,3,3,3,3,3,4,4,4,4,4,4],
         rho=[1]*8+[3]*4+[4]*5+[5],q=[0,0,0,1,1,1,1,1,3,3,6,7,2,3,6,6,7,3]),
    dict(id=2984,a=15,b=18,t=1,s=[1,3,3,3]+[4]*11,
         rho=[1]*6+[3]*2+[4]*10,q=[0,0,1,1,1,1,3,3,1,1,3,6,6,6,6,6,6,6])]

def localized(s: Sequence[int], q: Sequence[int], rho: Sequence[int], initial: Sequence[int]):
    E = sum(q)-sum(s)
    if E < 0: raise ValueError('Negative selected excess')
    P = list(initial)
    for eta in sorted({0,*rho}):
        m = sum(d<=eta for d in s)
        C = E + sum(d for d in s if d<=eta) - sum(qq for qq,r in zip(q,rho) if r<=eta)
        if C < 0: raise ValueError('Infeasible selected-incidence prefix')
        for u,(qq,r) in enumerate(zip(q,rho)):
            if r<=eta or qq==0: continue
            k = min(m,qq,C)
            if k<qq: P[u] = min(P[u],r-1+(C-k)//(qq-k))
    return P

def network_flow(n, edges, source, sink):
    # Dense-residual Edmonds--Karp, independently structured from C++ Dinic.
    residual = [[0]*n for _ in range(n)]
    original = [[0]*n for _ in range(n)]
    for u,v,cap in edges:
        assert cap>=0
        residual[u][v]+=cap; original[u][v]+=cap
    total=0
    while True:
        prev=[-1]*n;prev[source]=source;todo=deque([source])
        while todo and prev[sink]<0:
            u=todo.popleft()
            for v,cap in enumerate(residual[u]):
                if cap>0 and prev[v]<0:prev[v]=u;todo.append(v)
        if prev[sink]<0:break
        v=sink;aug=10**9
        while v!=source:aug=min(aug,residual[prev[v]][v]);v=prev[v]
        v=sink
        while v!=source:
            u=prev[v];residual[u][v]-=aug;residual[v][u]+=aug;v=u
        total+=aug
    return total,[[original[u][v]-residual[u][v] for v in range(n)] for u in range(n)]

def selected_matrix(s,q,rho):
    b,a=len(q),len(s);src=b+a;dst=src+1;ss=src+2;tt=src+3
    edges=[];bal=[0]*(tt+1)
    def lower(u,v,lo,hi):
        assert 0<=lo<=hi
        edges.append((u,v,hi-lo));bal[u]-=lo;bal[v]+=lo
    for u,qq in enumerate(q):lower(src,u,qq,qq)
    for u,r in enumerate(rho):
        for i,d in enumerate(s):
            if d<=r:lower(u,b+i,0,1)
    for i,d in enumerate(s):
        hi=sum(d<=r for r in rho)
        if d>hi:return None
        lower(b+i,dst,d,hi)
    lower(dst,src,0,sum(q))
    need=0
    for v,z in enumerate(bal):
        if z>0:edges.append((ss,v,z));need+=z
        elif z<0:edges.append((v,tt,-z))
    f,flow=network_flow(tt+1,edges,ss,tt)
    if f!=need:return None
    X=[[flow[u][b+i] for i in range(a)] for u in range(b)]
    assert [sum(row) for row in X]==list(q)
    assert all(sum(row[i] for row in X)>=s[i] for i in range(a))
    return X

def compatibility(q,rho):
    c=[x+y for x,y in zip(q,rho)]
    return [[int(u!=v and q[u]<=c[v]+1 and q[v]<=c[u]) for v in range(len(q))] for u in range(len(q))]

def old_caps(a,s,q,rho):
    b=len(q);E=sum(q)-sum(s);z=s.count(0);D=compatibility(q,rho);P=[]
    for u,qq in enumerate(q):
        degree=sum(bool(D[u][v] or D[v][u]) for v in range(b))
        cap=min(rho[u]+b-a-1,b-1-qq,degree-qq)
        k=min(z,qq,E)
        if qq>k:cap=min(cap,rho[u]-1+(E-k)//(qq-k))
        P.append(cap)
    return P

def target_flow(q,rho,P):
    if min(P)<0:return -1
    b=len(q);D=compatibility(q,rho);edges=[]
    for u,qq in enumerate(q):edges.append((2*b,u,qq))
    for u in range(b):
        for v in range(b):
            if D[u][v]:edges.append((u,b+v,1))
    for v,p in enumerate(P):edges.append((b+v,2*b+1,p))
    return network_flow(2*b+2,edges,2*b,2*b+1)[0]

def tails(a,q,rho,P):
    b=len(q);D=compatibility(q,rho);c=[qq+r for qq,r in zip(q,rho)];h=b-a-1
    out=[]
    for tau in range(1,max(q,default=0)+2):
        T=[u for u,qq in enumerate(q) if qq>=tau];dem=sum(q[u] for u in T)
        y=[sum(D[u][v] for u in T) for v in range(b)]
        exact=dem-sum(min(p,yy) for p,yy in zip(P,y))
        lost=sum(max(rho[v]+h-P[v],rho[v]+h-y[v]) for v in range(b))
        # Exact signed cap-loss identity. Positivity of bridge defects is separate.
        assert exact==sum(q)-sum(rho)-b*h+lost-sum(qq for qq in q if qq<tau)
        activation=dem-sum(P[v] for v in range(b) if c[v]>=tau-1)
        marginal_cap=0;gap=0
        for v in range(b):
            n=len(T)-int(v in T)
            upper=sum(q[u]>c[v]+1 for u in T)
            lower=sum(c[u]<q[v] for u in T)
            assert y[v]==n-upper-lower
            marginal_cap+=min(P[v],n-upper,n-lower)
            gap+=min(upper,lower,max(P[v]-y[v],0))
        assert marginal_cap-sum(min(p,yy) for p,yy in zip(P,y))==gap
        out.append(dict(tau=tau,deficiency=exact,activation=activation,marginal=dem-marginal_cap,gap=gap))
    return out

def check_incidence(s,rho,X):
    b=len(X);a=len(s);q=[sum(row) for row in X];x=[sum(row[i] for row in X) for i in range(a)]
    assert all(x[i]>=s[i] for i in range(a))
    assert all(not X[u][i] or s[i]<=rho[u] for u in range(b) for i in range(a))
    e=[x[i]-s[i] for i in range(a)];E=sum(e)
    bound=localized(s,q,rho,[10**6]*b)
    for u in range(b):
        positive=[e[i] for i in range(a) if X[u][i] and s[i]>0]
        actual=rho[u]-1+min(positive) if positive else 10**6
        assert actual<=bound[u],dict(s=s,rho=rho,X=X,u=u,actual=actual,bound=bound[u])
        d=max(0,actual-rho[u]+1)
        for eta in sorted({0,*rho}):
            if rho[u]<=eta:continue
            k=sum(X[u][i] for i in range(a) if s[i]<=eta)
            C=E+sum(si for si in s if si<=eta)-sum(q[v] for v in range(b) if rho[v]<=eta)
            assert C>=k+(q[u]-k)*d
    return q

def exhaustive():
    count=0
    for a in range(1,4):
        for b in range(1,5):
            for masks in product(range(1<<a),repeat=b):
                X=[[(mask>>i)&1 for i in range(a)] for mask in masks]
                q=[sum(row) for row in X];x=[sum(row[i] for row in X) for i in range(a)]
                for s in product(*(range(v+1) for v in x)):
                    ranges=[]
                    for u in range(b):
                        lo=max([1]+[s[i] for i in range(a) if X[u][i]])
                        ranges.append(range(lo,a-q[u]+1))
                    for rho in product(*ranges):check_incidence(s,rho,X);count+=1
    return count

def algebraic_floor_check():
    count=0
    for m in range(16):
        for C in range(31):
            for q in range(1,21):
                kstar=min(m,q,C)
                if kstar==q:continue
                bound=(C-kstar)//(q-kstar)
                brute=max((C-k)//(q-k) for k in range(min(m,q-1,C)+1))
                assert bound==brute
                count+=1
    return count

def mutation_checks(n=3000):
    rng=random.Random(SEED);bases=[];count=0;positive_ledger=0
    for d in SURVIVORS:
        X=selected_matrix(d['s'],d['q'],d['rho']);assert X is not None
        bases.append((d,X))
    for j in range(n):
        d,X=bases[j%len(bases)];a,b=d['a'],d['b'];s,rho=d['s'],d['rho']
        for _ in range(8):
            i=rng.randrange(a);u=rng.randrange(b);v=rng.randrange(b)
            if X[u][i] and not X[v][i] and s[i]<=rho[v] and sum(X[v])<a-rho[v]:
                X[u][i]=0;X[v][i]=1
        q=check_incidence(s,rho,X);assert sum(s)==sum(rho)+2*d['t']
        assert all(qq+r<=a for qq,r in zip(q,rho))
        E=sum(q)-sum(s);assert sum(q)==sum(rho)+2*d['t']+E
        count+=1;positive_ledger+=1
    return dict(seed=SEED,incidence_mutations=count,positive_scalar_ledger_profiles=positive_ledger,
                domain='selected-incidence/source-cap/two-defect projection; NOT realized graphs')

def hostile_checks():
    cases=[dict(name='arbitrary_monotone_caps',a=4,q=[0,1,3,3,1,3,2],rho=[2,1,1,1,1,1,1],P=[2,1,3,3,1,3,0]),
           dict(name='cap_formula_only_E5_z2',a=4,q=[1]+[3]*6,rho=[1]*7,P=[3]*7),
           dict(name='all_zero_demand_E19_z4',a=4,q=[1]+[3]*6,rho=[1]*7,P=[3]*7)]
    out=[]
    for d in cases:
        tt=tails(d['a'],d['q'],d['rho'],d['P']);f=target_flow(d['q'],d['rho'],d['P'])
        assert f<sum(d['q']) and all(x['deficiency']<=0 for x in tt)
        out.append(dict(name=d['name'],target_flow=f,Q=sum(d['q']),tail_margins=[-x['deficiency'] for x in tt]))
    assert selected_matrix([0]*4,[1]+[3]*6,[1]*7) is not None
    assert 0<7+2 # all-zero demand cannot satisfy S>=r+2t at t>=1
    # With rho=1 and two zero demands, each remaining demanded label has s<=1;
    # hence S<=2, contradicting the cap-only example's S=Q-E=14.
    assert 19-5>2
    return out

def survivor_checks():
    out=[]
    for d in SURVIVORS:
        a,b,s,q,rho=d['a'],d['b'],d['s'],d['q'],d['rho'];P=old_caps(a,s,q,rho)
        X=selected_matrix(s,q,rho);assert X is not None;check_incidence(s,rho,X)
        f=target_flow(q,rho,P);assert f==sum(q)
        new=localized(s,q,rho,P);tt=tails(a,q,rho,new);old=tails(a,q,rho,P)
        assert sum(new)<sum(q)
        out.append(dict(id=d['id'],r=sum(rho),S=sum(s),Q=sum(q),t=d['t'],D0=0,Esel=sum(q)-sum(s),
                        original_target_flow=f,original_P=P,localized_P=new,localized_cap_sum=sum(new),
                        original_tail_margins=[-v['deficiency'] for v in old],localized_tail_margins=[-v['deficiency'] for v in tt]))
    return out

def frozen_checks(exceptions:Path,pilot_input:Path):
    states={}
    for line in pilot_input.read_text().splitlines()[1:]:
        v=list(map(int,line.split()));layer,i,a,b,t,ns=v[:6]
        states[i]=dict(a=a,b=b,t=t,s=v[6:6+ns],rho=v[7+ns:])
    ct=Counter();first=Counter();newfirst=Counter()
    for line in exceptions.read_text().splitlines():
        fields=dict(x.split('=',1) for x in line.split('\t')[1:]);st=states[int(fields['state'])]
        q=[];rho=[];P=[]
        for item in fields['types'].split(';'):
            qq,c,p,n,*_=map(int,item.split(','));q +=[qq]*n;rho +=[c-qq]*n;P +=[p]*n
        assert sorted(rho)==st['rho'];assert P==old_caps(st['a'],st['s'],q,rho)
        assert sum(st['s'])==sum(rho)+2*st['t']
        assert sum(q)-sum(st['s'])==int(fields['E'])
        new=localized(st['s'],q,rho,P);oldtt=tails(st['a'],q,rho,P);newtt=tails(st['a'],q,rho,new)
        ct['profiles']+=1;ct['tightened']+=new!=P
        ct['original_uniform']+=sum(v['deficiency'] for v in oldtt)>0
        ct['localized_uniform']+=sum(v['deficiency'] for v in newtt)>0
        ct['original_activation']+=max(v['activation'] for v in oldtt)>0
        ct['localized_activation']+=max(v['activation'] for v in newtt)>0
        ct['localized_full_source']+=newtt[0]['deficiency']>0
        ct['original_marginal']+=max(v['marginal'] for v in oldtt)>0
        ct['localized_marginal']+=max(v['marginal'] for v in newtt)>0
        ct['localized_exact']+=max(v['deficiency'] for v in newtt)>0
        first[next(v['tau'] for v in oldtt if v['deficiency']>0)]+=1
        newfirst[next(v['tau'] for v in newtt if v['deficiency']>0)]+=1
    assert ct['profiles']==812 and ct['localized_exact']==812
    return dict(counts=dict(ct),first_deficient_threshold=dict(first),localized_first_deficient_threshold=dict(newfirst),
                exceptions_sha256=hashlib.sha256(exceptions.read_bytes()).hexdigest(),
                pilot_input_sha256=hashlib.sha256(pilot_input.read_bytes()).hexdigest())

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--exceptions',type=Path);p.add_argument('--pilot-input',type=Path)
    args=p.parse_args()
    if bool(args.exceptions)!=bool(args.pilot_input):p.error('Supply both frozen inputs')
    out=dict(schema='localized-selected-excess-v1',external_review='OPEN',floor_cases=algebraic_floor_check(),
             exhaustive_incidence_profiles=exhaustive(),mutations=mutation_checks(),hostile=hostile_checks(),survivors=survivor_checks())
    if args.exceptions:out['frozen_812']=frozen_checks(args.exceptions,args.pilot_input)
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
