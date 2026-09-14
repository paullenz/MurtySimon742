#!/usr/bin/env python3
import itertools,json,random
from collections import defaultdict

SEED=7420916


def D(q,c,u,w):
    return u!=w and q[u]<=c[w]+1 and q[w]<=c[u]


def stats(q,c,P,S):
    S=set(S); H=0; groups=defaultdict(lambda:[[],[]]); blocks=defaultdict(lambda:[[],[]]); y=[]
    for w in range(len(q)):
        yw=sum(1 for u in S if D(q,c,u,w)); y.append(yw); H+=min(P[w],yw)
        groups[q[w]][0].append(P[w]); groups[q[w]][1].append(yw)
        m=yw+(1 if w in S else 0)
        if w in S and P[w]>=m: blocks[(q[w],m)][0].append(w)
        if w not in S and P[w]<m: blocks[(q[w],m)][1].append(w)
    U=0
    for ps,ys in groups.values():
        ps=sorted(ps,reverse=True);ys=sorted(ys,reverse=True)
        U+=sum(min(a,b) for a,b in zip(ps,ys))
    C=sum(min(len(Hs),len(Ls)) for Hs,Ls in blocks.values())
    demand=sum(q[u] for u in S)
    return H-demand,U-demand,C,y,blocks


def monotone(q,c,P):
    n=len(q)
    for i in range(n):
        for j in range(n):
            if q[i]==q[j] and c[i]<=c[j] and P[i]>P[j]: return False
    return True


def analyze(q,c,P):
    n=len(q); exact_min=None;q_min=None;mins=[]
    for mask in range(1<<n):
        S={i for i in range(n) if mask>>i&1}
        f,g,C,_,_=stats(q,c,P,S)
        assert g-f==C
        if exact_min is None or f<exact_min: exact_min=f;mins=[S]
        elif f==exact_min: mins.append(S)
        q_min=g if q_min is None else min(q_min,g)
    assert exact_min==q_min
    M=set().union(*mins) if mins else set(); S=set(M); removed=[]
    while True:
        f,g,C,y,blocks=stats(q,c,P,S)
        assert f==exact_min
        if C==0:
            assert g==exact_min
            break
        pair=None
        for (qq,m),(Hs,Ls) in blocks.items():
            if not Hs or not Ls: continue
            for x in Ls:
                for yy in Hs:
                    if c[x]<c[yy]: pair=(x,yy,m);break
                if pair:break
            if pair:break
        assert pair is not None
        x,yy,m=pair
        assert x not in M
        f2,_,_,_,_=stats(q,c,P,S-{yy})
        assert f2==exact_min
        removed.append((yy,P[yy],m));S.remove(yy)
        for r,Pr,mr in removed:
            yr=sum(1 for u in S if D(q,c,u,r))
            current_m=yr
            assert Pr>=current_m
    return exact_min,M,S,removed


def hostile():
    q=[0,3,3,3,0]; c=[4,4,4,4,2]; P=[4,1,1,1,2]
    mn,M,S,removed=analyze(q,c,P)
    fm,gm,Cm,_,_=stats(q,c,P,M)
    fs,gs,Cs,_,_=stats(q,c,P,S)
    assert mn==-1 and Cm==1 and fm==-1 and gm==0
    assert fs==gs==-1 and Cs==0 and S=={1,2,3}
    return {'minimum_margin':mn,'Mplus_crossing':Cm,'Mplus_q_margin':gm,'final_crossing':Cs,'final_q_margin':gs,'final_witness':sorted(S),'deletions':len(removed)}


def exhaustive():
    tested=positive=deletions=0
    for n in range(1,5):
        for q in itertools.product(range(2),repeat=n):
            for rho in itertools.product(range(2),repeat=n):
                c=tuple(q[i]+rho[i] for i in range(n))
                for P in itertools.product(range(3),repeat=n):
                    if not monotone(q,c,P): continue
                    tested+=1
                    mn,M,S,rem=analyze(q,c,P)
                    if stats(q,c,P,M)[2]: positive+=1
                    deletions+=len(rem)
    return {'profiles':tested,'Mplus_positive_crossing_profiles':positive,'deletions':deletions,'n_max':4,'q_values':[0,1],'rho_values':[0,1],'P_values':[0,1,2]}


def random_monotone_P(q,c,rng):
    n=len(q);P=[0]*n
    for qq in sorted(set(q)):
        vals={}; level=0
        for cc in sorted({c[i] for i in range(n) if q[i]==qq}):
            level=min(n-1,level+rng.randint(0,2));vals[cc]=level
        for i in range(n):
            if q[i]==qq:P[i]=vals[c[i]]
    return P


def random_phase(trials=30000):
    rng=random.Random(SEED);positive=deletions=0
    for _ in range(trials):
        n=rng.randint(2,8)
        q=[rng.randint(0,4) for _ in range(n)]
        rho=[rng.randint(0,4) for _ in range(n)]
        c=[q[i]+rho[i] for i in range(n)]
        P=random_monotone_P(q,c,rng)
        mn,M,S,rem=analyze(q,c,P)
        if stats(q,c,P,M)[2]:positive+=1
        deletions+=len(rem)
    return {'trials':trials,'seed':SEED,'Mplus_positive_crossing_profiles':positive,'deletions':deletions}


def main():
    out={
      'schema':'q-stratified-mincut-exactness-verification-v1',
      'hostile_counterexample':hostile(),
      'exhaustive':exhaustive(),
      'random':random_phase(),
      'result':'PASS',
      'trust_boundary':'Finite verification supports the hand proof; it does not replace external mathematical review.'
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
