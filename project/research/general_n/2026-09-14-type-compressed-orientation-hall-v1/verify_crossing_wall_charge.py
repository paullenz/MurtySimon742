#!/usr/bin/env python3
import json, random
from collections import defaultdict

SEED=7420915
rng=random.Random(SEED)


def D(q,c,u,w):
    return u!=w and q[u] <= c[w]+1 and q[w] <= c[u]


def potential(q,c,u,w):
    return D(q,c,u,w) or D(q,c,w,u)


def degree(q,c,u):
    return sum(1 for w in range(len(q)) if w!=u and potential(q,c,u,w))


def margin_and_y(q,c,P,S):
    S=set(S)
    y=[]
    H=0
    for w in range(len(q)):
        yw=sum(1 for u in S if D(q,c,u,w))
        y.append(yw)
        H += min(P[w],yw)
    return H-sum(q[u] for u in S), y


def all_minimizers(q,c,P):
    n=len(q)
    best=None; mins=[]
    for mask in range(1<<n):
        S={i for i in range(n) if (mask>>i)&1}
        v,_=margin_and_y(q,c,P,S)
        if best is None or v<best:
            best=v; mins=[S]
        elif v==best:
            mins.append(S)
    M=set().union(*mins) if mins else set()
    return best,mins,M


def m_pre(q,c,S,w):
    return sum(1 for u in S if q[u] <= c[w]+1 and q[w] <= c[u])


def crossing_blocks(q,c,P,S):
    blocks=defaultdict(lambda:[[],[]])
    for w in range(len(q)):
        m=m_pre(q,c,S,w)
        if w in S and P[w]>=m:
            blocks[(q[w],m)][0].append(w)
        if w not in S and P[w]<=m-1:
            blocks[(q[w],m)][1].append(w)
    return blocks


def hostile_counterexample():
    q=[0,3,3,3,0]
    c=[4,4,4,4,2]
    P=[4,1,1,1,2]
    best,mins,M=all_minimizers(q,c,P)
    assert best==-1
    assert M=={0,1,2,3}
    _,y=margin_and_y(q,c,P,M)
    blocks=crossing_blocks(q,c,P,M)
    C=sum(min(len(H),len(L)) for H,L in blocks.values())
    assert C==1
    x=4; yy=0
    Z={w for w in range(5) if y[w]<P[w]}
    A={w for w in range(5) if D(q,c,x,w)} & Z
    T={w for w in range(5) if y[w]<=P[w]}
    R={w for w in range(5) if D(q,c,yy,w)} & T
    assert len(A)==q[x]+1==1
    assert len(R)==q[yy]==0
    rem,_=margin_and_y(q,c,P,M-{yy})
    assert rem==best
    return {
        'minimum_margin':best,
        'minimizer_count':len(mins),
        'C_q':C,
        'selected_slack_A':P[0]-y[0],
        'exterior_oversaturation_C':y[4]-P[4],
        'tight_slack_neighbors':len(A),
        'removal_margin':rem,
    }


def random_double_tightness(trials=20000):
    pairs=0; profiles_with_pairs=0
    for _ in range(trials):
        n=rng.randint(3,7)
        q=[rng.randint(0,3) for _ in range(n)]
        rho=[rng.randint(1,3) for _ in range(n)]
        c=[q[i]+rho[i] for i in range(n)]
        P=[rng.randint(0,n-1) for _ in range(n)]
        best,mins,M=all_minimizers(q,c,P)
        _,yv=margin_and_y(q,c,P,M)
        seen=False
        for x in range(n):
            if x in M: continue
            mx=m_pre(q,c,M,x)
            for yy in range(n):
                if yy not in M or yy==x: continue
                if q[x]!=q[yy] or not c[x]<c[yy]: continue
                if m_pre(q,c,M,yy)!=mx: continue
                m=mx
                if not (P[x]<=m-1 and P[yy]>=m): continue
                seen=True; pairs+=1
                Z={w for w in range(n) if yv[w]<P[w]}
                A={w for w in range(n) if D(q,c,x,w)} & Z
                T={w for w in range(n) if yv[w]<=P[w]}
                R={w for w in range(n) if D(q,c,yy,w)} & T
                assert len(A)==q[x]+1
                assert len(R)==q[yy]
                assert R==A-{yy}
                rem,_=margin_and_y(q,c,P,M-{yy})
                assert rem==best
                for w in range(n):
                    if D(q,c,yy,w) and w not in R:
                        assert yv[w]>=P[w]+1
        if seen: profiles_with_pairs+=1
    return {'trials':trials,'profiles_with_crossing_pairs':profiles_with_pairs,'crossing_pairs_checked':pairs}


def random_desert_degree_jump(trials=50000):
    equal_m_pairs=0
    for _ in range(trials):
        n=rng.randint(3,10)
        q=[rng.randint(0,6) for _ in range(n)]
        rho=[rng.randint(1,4) for _ in range(n)]
        c=[q[i]+rho[i] for i in range(n)]
        S={i for i in range(n) if rng.random()<0.5}
        for x in range(n):
            if x in S: continue
            for yy in range(n):
                if yy not in S or yy==x: continue
                if q[x]!=q[yy] or not c[x]<c[yy]: continue
                if m_pre(q,c,S,x)!=m_pre(q,c,S,yy): continue
                equal_m_pairs+=1
                I=[w for w in range(n) if c[x]+2<=q[w]<=c[yy]+1]
                assert all(w not in S for w in I)
                assert degree(q,c,yy)-degree(q,c,x)==len(I)
    return {'trials':trials,'equal_m_pairs_checked':equal_m_pairs}


def random_weighted_charge(trials=30000):
    positive=0; blocks_checked=0
    for _ in range(trials):
        b=rng.randint(4,8)
        a=rng.randint(max(2,b-3),b+1)
        rho=[rng.randint(1,a) for _ in range(b)]
        q=[rng.randint(0,max(0,a-rho[i])) for i in range(b)]
        c=[q[i]+rho[i] for i in range(b)]
        dk=[degree(q,c,i) for i in range(b)]
        caps=[]; ok=True
        for i in range(b):
            cap=min(rho[i]+b-a-1,b-1-q[i],dk[i]-q[i])
            if cap<0:
                ok=False; break
            caps.append(cap)
        if not ok: continue
        P=caps
        best,mins,M=all_minimizers(q,c,P)
        blocks=crossing_blocks(q,c,P,M)
        C=sum(min(len(H),len(L)) for H,L in blocks.values())
        if not C: continue
        positive+=1
        W=0
        _,yv=margin_and_y(q,c,P,M)
        for (qq,m),(H,L) in blocks.items():
            cc=min(len(H),len(L)); blocks_checked+=int(cc>0)
            W += cc*max(0,m+a-b)
        selected_slack=sum(max(0,P[w]-yv[w]) for w in M)
        exterior_over=sum(max(0,yv[w]-P[w]) for w in range(b) if w not in M)
        assert C<=selected_slack
        assert C<=exterior_over
        assert W<=sum(rho)-b
    return {'trials':trials,'positive_crossing_profiles':positive,'positive_blocks_checked':blocks_checked}


def main():
    result={
        'schema':'crossing-wall-charge-verification-v1',
        'seed':SEED,
        'hostile_counterexample':hostile_counterexample(),
        'random_double_tightness':random_double_tightness(),
        'random_desert_degree_jump':random_desert_degree_jump(),
        'random_weighted_charge':random_weighted_charge(),
        'result':'PASS',
        'trust_boundary':'Finite deterministic testing supports but does not replace the hand proofs; external mathematical review remains open.'
    }
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
