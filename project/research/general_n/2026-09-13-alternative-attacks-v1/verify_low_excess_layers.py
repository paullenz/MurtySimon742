#!/usr/bin/env python3
"""Exact integer replay for state 227 selected-excess layers E=1,2,3.

No numerical optimizer is used.  The checker combines:
- excess-layer source restrictions;
- exact source-load dynamic programming;
- exact residual-budget support functions;
- top-k source-degree bounds for concentrated excess profiles.
"""
from functools import lru_cache
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent


def nondec_parts(total,n,maxv):
    out=[]
    def rec(pos,last,rem,pref):
        if pos==n:
            if rem==0:
                out.append(tuple(pref))
            return
        slots=n-pos-1
        for v in range(last,min(maxv,rem)+1):
            rr=rem-v
            if rr<v*slots or rr>maxv*slots:
                continue
            rec(pos+1,v,rr,pref+[v])
    rec(0,0,total,[])
    return out


def source_data(e2,e3):
    H={l:sum(e>=l for e in e2+e3) for l in range(1,10)}
    H2={l:sum(e>=l for e in e2) for l in range(1,10)}
    xmax=max([2+e for e in e2]+[3+e for e in e3])
    qmax=0
    for q in range(1,13):
        if q*max(0,q-xmax)<=39:
            qmax=q
    return H,H2,qmax


def source_options(e2,e3):
    H,H2,qmax=source_data(e2,e3)
    o2=[]
    for q in range(5):
        for p in range(min(4,17-q)+1):
            if q:
                L=max(0,p-1,q+p-13)
                if L and q>H2.get(L,0):
                    continue
            o2.append((q,p,q*(q+p)))
    o3=[]
    for q in range(qmax+1):
        for p in range(min(5,17-q)+1):
            if q:
                L=max(0,p-2,q+p-13)
                if L and q>H.get(L,0):
                    continue
            o3.append((q,p,q*(q+p)))
    return o2,o3,qmax


def coarse_bounds(e2,e3):
    E=sum(e2)+sum(e3); Q=41+E; need=Q-21
    o2,o3,_=source_options(e2,e3)
    dp={(0,0):0}
    for opts in [o2]+[o3]*10:
        nd={}
        for (qs,ps),cost in dp.items():
            for q,p,c in opts:
                nq=qs+q
                if nq>Q:
                    continue
                np_=min(need,ps+p)
                key=(nq,np_); value=cost+c
                if value<nd.get(key,10**9):
                    nd[key]=value
        dp=nd
    lower=dp[(Q,need)]

    xs=[2+e for e in e2]+[3+e for e in e3]
    caps=[11]*4+[10]*11
    upper=sum(x*x for x in xs)
    left=39
    for i in sorted(range(15),key=lambda j:(-xs[j],j)):
        take=min(left,caps[i]); upper+=xs[i]*take; left-=take
        if left==0:
            break
    assert left==0
    return lower,upper


def sharp_bound(e2,e3):
    E=sum(e2)+sum(e3); Q=41+E; need=Q-21
    o2,o3,_=source_options(e2,e3)
    orders=[3+e for e in e3 if e>=1]+[2+e for e in e2 if e>=2]
    K=max(orders) if orders else 1
    zero=(0,)*K
    dp={(0,0,zero):0}
    for _ in range(10):
        nd={}
        for (qs,ps,top),cost in dp.items():
            for q,p,c in o3:
                nq=qs+q
                if nq>Q:
                    continue
                np_=min(need,ps+p)
                nt=tuple(sorted(top+(q,),reverse=True)[:K])
                key=(nq,np_,nt); value=cost+c
                if value<nd.get(key,10**9):
                    nd[key]=value
        dp=nd

    z0=sum(e==0 for e in e2); hpos=4-z0
    baseline=3*(80+E)
    best=None
    for q2,p2,c2 in o2:
        C0=2*z0+max(0,q2-hpos)*max(0,q2+p2-2)
        for (qs,ps,top3),c3 in dp.items():
            if qs+q2!=Q or min(need,ps+p2)!=need:
                continue
            topall=tuple(sorted(top3+(q2,),reverse=True)[:K])
            pos=0; ok=True
            for e in e3:
                if e>=1:
                    k=3+e
                    if top3[k-1]<=0:
                        ok=False; break
                    pos+=e*(e+2+top3[k-1])
            if not ok:
                continue
            for e in e2:
                if e>=2:
                    k=2+e
                    if topall[k-1]<=0:
                        ok=False; break
                    pos+=(e-1)*(e+2+topall[k-1])
            if not ok:
                continue
            value=c2+c3+C0-pos
            if best is None or value<best:
                best=value
    assert best is not None
    return best,baseline


EXPECTED={
(1,(0,0,0,1),()):('coarse',242,237),
(1,(0,0,0,0),(1,)):('sharp',248,243),
(2,(0,0,0,0),(2,)):('sharp',255,246),
(2,(0,0,0,0),(1,1)):('sharp',257,246),
(2,(0,0,0,1),(1,)):('coarse',257,254),
(2,(0,0,0,2),()):('coarse',258,255),
(2,(0,0,1,1),()):('coarse',257,242),
(3,(0,0,0,0),(3,)):('sharp',256,249),
(3,(0,0,0,0),(1,2)):('sharp',263,249),
(3,(0,0,0,0),(1,1,1)):('sharp',262,249),
(3,(0,0,0,1),(2,)):('coarse',274,273),
(3,(0,0,0,1),(1,1)):('sharp',267,249),
(3,(0,0,0,2),(1,)):('coarse',274,272),
(3,(0,0,1,1),(1,)):('coarse',270,259),
(3,(0,0,0,3),()):('sharp',257,249),
(3,(0,0,1,2),()):('coarse',274,260),
(3,(0,1,1,1),()):('coarse',270,247),
}


def compact_nonzero(t):
    return tuple(x for x in t if x)


def main():
    records=[]
    seen=set()
    for E in (1,2,3):
        for e2tot in range(E+1):
            for e2 in nondec_parts(e2tot,4,9):
                for e3full in nondec_parts(E-e2tot,11,7):
                    e3=compact_nonzero(e3full)
                    key=(E,e2,e3)
                    assert key in EXPECTED, key
                    mode,elo,eup=EXPECTED[key]
                    if mode=='coarse':
                        lower,upper=coarse_bounds(e2,e3full)
                    else:
                        lower,upper=sharp_bound(e2,e3full)
                    assert (lower,upper)==(elo,eup),(key,lower,upper,elo,eup)
                    assert lower>upper
                    records.append({
                        'E':E,'demand2_excess':list(e2),'demand3_positive_excess':list(e3),
                        'method':mode,'lower':lower,'upper':upper,'gap':lower-upper,
                    })
                    seen.add(key)
    assert seen==set(EXPECTED)
    assert len(records)==17
    out={
        'schema':'state-227-low-excess-v1',
        'status':'PASS',
        'profiles_checked':17,
        'excluded_total_excess':[1,2,3],
        'minimum_required_total_excess':4,
        'whole_state_exclusion':False,
        'records':records,
    }
    (HERE/'LOW_EXCESS_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','profiles':17,'conclusion':'E>=4 required'},indent=2))

if __name__=='__main__':
    main()
