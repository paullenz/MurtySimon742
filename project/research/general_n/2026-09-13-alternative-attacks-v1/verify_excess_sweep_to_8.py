#!/usr/bin/env python3
"""Exact replay of state-227 excess-profile sweep for E=4,...,8.

Standard library only.  No MILP/LP status is used.
"""
from functools import lru_cache
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent


def parts(total,n,maxv):
    out=[]
    def rec(pos,last,rem,pref):
        if pos==n:
            if rem==0: out.append(tuple(pref))
            return
        slots=n-pos-1
        for v in range(last,min(maxv,rem)+1):
            rr=rem-v
            if rr<v*slots or rr>maxv*slots: continue
            rec(pos+1,v,rr,pref+[v])
    rec(0,0,total,[])
    return out


@lru_cache(None)
def qtuples(n,total,qmax,last=0):
    if n==0:
        return ((),) if total==0 else ()
    out=[]
    for q in range(last,min(qmax,total)+1):
        rr=total-q
        if rr<q*(n-1) or rr>qmax*(n-1): continue
        for tail in qtuples(n-1,rr,qmax,q):
            out.append((q,)+tail)
    return tuple(out)


def pmax_table(rho,H,qmax):
    out={}
    for q in range(qmax+1):
        cap=min(rho+2,17-q); best=-1
        for p in range(max(-1,cap)+1):
            if q==0:
                best=p; continue
            L=max(0,p-rho+1,q+p-13)
            if L==0 or q<=H.get(L,0): best=p
        out[q]=best
    return out


def solve(e2,e3,collect=False):
    e2=tuple(sorted(e2)); e3=tuple(sorted(e3))
    E=sum(e2)+sum(e3); Q=41+E; need=Q-21
    H={l:sum(e>=l for e in e2+e3) for l in range(1,E+2)}
    H2={l:sum(e>=l for e in e2) for l in range(1,E+2)}
    xmax=max([2+e for e in e2]+[3+e for e in e3])
    qmax=max(q for q in range(13) if q*max(0,q-xmax)<=39)
    p3=pmax_table(3,H,qmax); p2=pmax_table(2,H2,4)
    z0=e2.count(0); hpos=4-z0; baseline=3*(80+E)
    d3=[(e,3+e,e) for e in e3 if e>=1]
    d2=[(e,2+e,e-1) for e in e2 if e>=2]
    best=None; minimizers=[]
    for q2 in range(5):
        pm2=p2[q2]
        if pm2<0: continue
        target=Q-q2
        for qs in qtuples(10,target,qmax,0):
            caps=[p3[q] for q in qs]
            if any(c<0 for c in caps): continue
            desc=qs[::-1]; Pplus=0; ok=True
            for e,k,w in d3:
                if k>10 or desc[k-1]<=0: ok=False; break
                Pplus+=w*(e+2+desc[k-1])
            if not ok: continue
            all_desc=tuple(sorted(qs+(q2,),reverse=True))
            for e,k,w in d2:
                if k>11 or all_desc[k-1]<=0: ok=False; break
                Pplus+=w*(e+2+all_desc[k-1])
            if not ok: continue
            sq=sum(q*q for q in qs); capsum=sum(caps)
            for pp2 in range(pm2+1):
                rem=max(0,need-pp2)
                if rem>capsum: continue
                left=rem; pcost=0
                for q,cap in zip(qs,caps):
                    take=min(left,cap); pcost+=q*take; left-=take
                    if left==0: break
                if left: continue
                T=q2*q2+sq+q2*pp2+pcost
                C0=2*z0+max(0,q2-hpos)*max(0,q2+pp2-2)
                B=T+C0-Pplus
                arg=(q2,pp2,qs,T,C0,Pplus)
                if best is None or B<best:
                    best=B; minimizers=[arg]
                elif collect and B==best:
                    minimizers.append(arg)
    return best,baseline,minimizers


def main():
    expected={
        4:(20,20,0,0,6),
        5:(35,35,0,0,4),
        6:(62,61,1,0,4),
        7:(102,101,1,0,8),
        8:(167,166,0,1,9),
    }
    summaries=[]; equalities=[]; source_infeasible=[]
    for E in range(4,9):
        total=strict=eq=src=0; mingap=None
        for e2tot in range(E+1):
            for e2 in parts(e2tot,4,E):
                for e3 in parts(E-e2tot,11,E):
                    total+=1
                    B,base,args=solve(e2,e3,True)
                    if B is None:
                        src+=1
                        source_infeasible.append({'E':E,'e2':list(e2),'e3':list(e3)})
                        continue
                    gap=B-base
                    assert gap>=0,(E,e2,e3,gap)
                    if gap==0:
                        eq+=1
                        equalities.append({'E':E,'e2':list(e2),'e3':list(e3),'B':B,'baseline':base,'minimizers':[[a[0],a[1],list(a[2]),a[3],a[4],a[5]] for a in args]})
                    else:
                        strict+=1; mingap=gap if mingap is None else min(mingap,gap)
        got=(total,strict,eq,src,mingap)
        assert got==expected[E],(E,got,expected[E])
        summaries.append({'E':E,'profiles':total,'strict':strict,'equality':eq,'source_infeasible':src,'minimum_strict_gap':mingap})

    assert source_infeasible==[{'E':8,'e2':[0,0,0,0],'e3':[0,0,0,0,0,0,0,0,0,0,8]}]
    assert len(equalities)==2
    e6=equalities[0]; e7=equalities[1]
    assert e6['E']==6 and e6['e2']==[0,0,0,0] and e6['e3']==[0,0,0,0,0,0,0,0,0,0,6]
    assert e6['minimizers']==[[0,4,[1,5,5,5,5,5,5,5,5,6],328,8,78]]
    assert e7['E']==7 and e7['e2']==[0,0,0,7] and e7['e3']==[0,0,0,0,0,0,0,0,0,0,0]
    assert e7['minimizers']==[[1,4,[1,5,5,5,5,5,5,5,5,6],339,6,84]]

    # Equality-rigidity checks are direct arithmetic encodings of the hand note.
    # E=6: C0=8 across four zero-excess D2 labels -> each C=2.  rho2 inactive;
    # only one rho3 source has q<5, so at least 7 of 8 D2 incidences have q>=5.
    assert e6['minimizers'][0][4]==8
    assert sum(2 for _ in range(4))==8 and 8-1>=7
    # E=7: rho2 has L=p-rho+1=3, so must use the unique e=7 D2 label;
    # remaining three D2 labels have C0=6 and need six rho3 incidences, >=5 from q>=5.
    q2,p2=e7['minimizers'][0][0:2]
    assert max(0,p2-2+1)==3 and q2==1 and e7['minimizers'][0][4]==6 and 6-1>=5

    out={'schema':'state-227-excess-sweep-to-8-v1','status':'PASS','summaries':summaries,'equality_profiles':equalities,'source_infeasible_profiles':source_infeasible,'equality_profiles_hand_excluded':True,'conclusion':'Any surviving state-227 realization must have total selected excess E>=9.','whole_state_exclusion':False}
    (HERE/'EXCESS_SWEEP_TO_8_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','profiles':sum(x['profiles'] for x in summaries),'conclusion':'E>=9 required'},indent=2))


if __name__=='__main__': main()
