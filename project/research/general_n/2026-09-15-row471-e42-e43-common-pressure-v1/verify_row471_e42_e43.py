#!/usr/bin/env python3
"""Exact standard-library verifier for row-471 branches e_L=41,42,43; new closures 42,43.

Scope: selected-incidence/common-pressure relaxation only.  This does not prove
row 471 as a whole (e_L=47 remains), graph nonrealizability beyond the stated
bridge projection, or the unrestricted Murty-Simon conjecture.
"""
from __future__ import annotations
import argparse, json
from itertools import combinations
from pathlib import Path

SOURCE_SHA256 = '157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572'
TARGET_ROW = 471
BRANCHES = (41,42,43)
ETA = 2


def conditional_caps(s,q,rho,P,eta,e_low):
    E=sum(q)-sum(s)
    assert 0 <= e_low <= E
    low=[i for i,d in enumerate(s) if d<=eta]
    SL=sum(s[i] for i in low)
    forced=[max(0,qq-sum(eta<d<=r for d in s)) for qq,r in zip(q,rho)]
    slack=e_low+SL-sum(forced)
    assert slack >= 0
    out=list(P)
    for u,(qq,r) in enumerate(zip(q,rho)):
        m=sum(s[i]<=r for i in low)
        kmax=min(qq,m,forced[u]+slack)
        if qq>kmax:
            out[u]=min(out[u],r-1+(E-e_low)//(qq-kmax))
    return out


def receiver_certificate(q,rho,pc):
    # Existing block-pressure receiver certificate: charge_eta=0, alpha=1,
    # tau=1, theta=5.  Since all labels are positive-demand, v_u=q_u.
    tau=1; theta=5
    c=[qq+r for qq,r in zip(q,rho)]
    A=[min(pc[w],sum(u!=w and tau<=q[u]<=c[w]+1 for u in range(len(q))))
       for w in range(len(q))]
    free=[min(a,r-1) for a,r in zip(A,rho)]
    g=[a-f for a,f in zip(A,free)]
    penalty=sum(max(0,theta-qq)*gg for qq,gg in zip(q,g))
    lower=theta*(sum(q)-sum(free))-penalty
    return dict(tau=tau,theta=theta,demand=sum(q),capacity=sum(A),
                free=sum(free),penalty=penalty,lower=lower)


def rho2_upper(q,rho,D,L):
    """Exact symmetry DP for the four rho=2 low sources.

    We track only the four demand-two labels.  A source of row sum q can put at
    most five selections on the five demand-one labels, so it must use between
    max(0,q-5) and min(q,4) distinct demand-two labels.  A demand-two label with
    low-source degree l and maximum selected-source pressure m requires at least
    (2+m-l)_+ selections from the rho=3 sources.  Their total low-block count is L.
    """
    src=sorted([(u,q[u],D[u]) for u,r in enumerate(rho) if r==2],
               key=lambda z:(-z[1],z[0]))
    assert [qq for _,qq,_ in src]==[7,4,4,3]
    assert all(dd==4 for _,_,dd in src)
    state={((0,0),)*4:(0,())}
    counts=[]
    for u,qq,Du in src:
        nxt={}
        for st,(score,witness) in state.items():
            for d in range(Du+1):
                for r in range(max(0,qq-5),min(qq,4)+1):
                    for inds in combinations(range(4),r):
                        b=[list(x) for x in st]
                        for i in inds:
                            b[i][0]+=1
                            b[i][1]=max(b[i][1],d)
                        key=tuple(sorted(map(tuple,b)))
                        val=score+qq*d
                        old=nxt.get(key)
                        if old is None or val>old[0]:
                            nxt[key]=(val,witness+((u,qq,d,r),))
        state=nxt; counts.append(len(state))
    feasible=[]
    for st,(score,witness) in state.items():
        req=sum(max(0,2+m-l) for l,m in st)
        if req<=L:
            feasible.append((score,st,witness,req))
    assert feasible
    best=max(feasible,key=lambda z:(z[0],-z[3],z[1]))
    return dict(upper=best[0],demand2_state=[list(x) for x in best[1]],
                witness=[list(x) for x in best[2]],required_high_slots=best[3],
                state_counts=counts,terminal_states=len(state),
                admissible_terminal_states=len(feasible))


def high_upper(q,rho,D,L,H):
    """Exact DP for the nine rho=3 sources under maximally nested high labels.

    If source u has h_u selected demand-three labels at pressure d_u, sorting the
    twelve high-label excesses decreasingly forces e_(j)>=max_{h_u>=j} d_u.
    Hence H is at least the sum of those layer maxima.  We optimize charge over
    all low-slot allocations and pressures satisfying this necessary condition.
    """
    src=[(u,q[u],D[u]) for u,r in enumerate(rho) if r==3]
    assert len(src)==9 and sum(qq for _,qq,_ in src)==45
    maxq=max(qq for _,qq,_ in src)
    state={(0,(0,)*maxq):(0,())}
    counts=[]
    for u,qq,Du in src:
        nxt={}
        for (used,layers),(score,witness) in state.items():
            for k in range(qq+1):
                if used+k>L: break
                h=qq-k
                for d in range(Du+1):
                    nl=list(layers)
                    for j in range(h): nl[j]=max(nl[j],d)
                    if sum(nl)>H: continue
                    key=(used+k,tuple(nl))
                    val=score+qq*d
                    old=nxt.get(key)
                    if old is None or val>old[0]:
                        nxt[key]=(val,witness+((u,qq,k,h,d),))
        state=nxt; counts.append(len(state))
    feasible=[(score,key,witness) for key,(score,witness) in state.items() if key[0]==L]
    assert feasible
    best=max(feasible,key=lambda z:(z[0],z[1]))
    return dict(upper=best[0],low_slots=best[1][0],layer_maxima=list(best[1][1]),
                witness=[list(x) for x in best[2]],state_counts=counts,
                terminal_states=len(state),admissible_terminal_states=len(feasible))


def verify(data):
    assert data['source_sha256']==SOURCE_SHA256
    p=next(x for x in data['rows'] if x['row']==TARGET_ROW)
    assert p['a']==21 and p['b']==25 and p['t']==1 and p['D0']==0 and p['Esel']==47
    assert p['s']==[1]*5+[2]*4+[3]*12
    q=p['q']; rho=p['rho']; P=p['P']; s=p['s']
    assert sum(q)==96 and sum(s)==49 and sum(rho)==47
    assert sum(q)==sum(rho)+2*p['t']+p['D0']+p['Esel']
    low1=[u for u,r in enumerate(rho) if r==1]
    low2=[u for u,r in enumerate(rho) if r==2]
    high=[u for u,r in enumerate(rho) if r==3]
    assert (len(low1),len(low2),len(high))==(12,4,9)
    assert (sum(q[u] for u in low1),sum(q[u] for u in low2),sum(q[u] for u in high))==(33,18,45)

    reports={}
    for eL in BRANCHES:
        L=eL-38
        H=p['Esel']-eL
        pc=conditional_caps(s,q,rho,P,ETA,eL)
        D=[max(0,pp-r+1) for pp,r in zip(pc,rho)]
        assert all(D[u]==4 for u in low1+low2)
        recv=receiver_certificate(q,rho,pc)
        assert recv['lower']==222 and recv['free']==22 and recv['penalty']==148
        r1=4*sum(q[u] for u in low1)
        assert r1==132
        r2=rho2_upper(q,rho,D,L)
        hi=high_upper(q,rho,D,L,H)
        total=r1+r2['upper']+hi['upper']
        assert total < recv['lower']
        reports[str(eL)]=dict(low_high_slots=L,high_excess=H,
                              receiver_lower=recv['lower'],rho1_upper=r1,
                              rho2_upper=r2['upper'],rho2_state_counts=r2['state_counts'],
                              rho2_admissible_terminal_states=r2['admissible_terminal_states'],
                              high_upper=hi['upper'],high_terminal_states=hi['terminal_states'],
                              high_admissible_terminal_states=hi['admissible_terminal_states'],
                              total_charge_upper=total,
                              contradiction=f"{total}<{recv['lower']}")
    assert [reports[str(e)]['rho2_upper'] for e in BRANCHES]==[36,44,54]
    assert [reports[str(e)]['high_upper'] for e in BRANCHES]==[45,38,29]
    assert [reports[str(e)]['total_charge_upper'] for e in BRANCHES]==[213,214,215]
    return dict(schema='row471-e42-e43-common-pressure-v1',row=471,
                independent_regression_e_low=[41],newly_closed_e_low=[42,43],remaining_e_low=[47],reports=reports,
                scope=('exact necessary-condition argument inside the conditioned selected-incidence/common-pressure '
                       'relaxation; e_L=47 remains; no unrestricted or whole-state claim'))


def main():
    if not __debug__: raise SystemExit('Assertions disabled: do not run with -O')
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--remainder',type=Path,required=True)
    args=ap.parse_args()
    out=verify(json.loads(args.remainder.read_text()))
    print(json.dumps(out,sort_keys=True,indent=2))

if __name__=='__main__': main()
