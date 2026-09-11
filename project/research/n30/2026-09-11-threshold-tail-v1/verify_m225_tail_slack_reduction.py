#!/usr/bin/env python3
"""Solver-free exact audit of the n=30, Delta=16, m=225 tail-slack reduction.

Input is the preserved exact 100-profile Q>=18 frontier. For each profile the
checker reconstructs every monotone residual tail compatible with threshold
capacity and the at-most-three-unit slack identity. It produces exactly the
272 historical row-threshold survivors and verifies their normalized SHA-256.

This does not prove the 100-profile classification itself; it proves that once
that frontier is known, the historical 150-million-state residual-row scan is
unnecessary for obtaining the 272 endpoint rows.
"""
from __future__ import annotations
from collections import Counter
from hashlib import sha256
from pathlib import Path
import argparse,json

B=16
HISTORICAL_NORMALIZED_SHA256='ac02b654d672062421a67e0b07a4f1cbebbc688e83ad4723ea37af2b0542f16e'
EXPECTED={(18,0):64,(19,0):96,(19,1):29,(20,0):42,(20,1):18,(20,2):6,(21,0):9,(21,1):5,(21,2):2,(21,3):1}
HIST_IDS=[1121,1324,1500,1574,2094,2309,2555,2596,2701,2812,2821,2984,2994,3073,3181,3256,3262,3266,3271,3281,3359,3410,3473,3550,3640,3644,3648,3654,3690,3733,3816,3825,3957,3963,3967,4051,4099,4160,4170,4175,4185,4201,4228,4266,4317,4380,4457,4463,4467,4473,4485,4504,4534,4575,4628,4642,4693,4771,4786,4792,4799,4849,4861,4864,4867,4871,4878,4893,4915,4947,4990,5044,5059,5065,5110,5125,5131,5138,5146,5165,5176,5188,5198,5203,5209,5216,5243,5266,5278,5284,5288,5293,5299,5306,5314,5323,5333,5344,5356,5368]

def C(h,z): return (z*(z-1)+h*(h+1))//2

def g(h,W):
    if W==0:return 0
    for z in range(h,B+1):
        if W<=C(h,z):return z
    raise ValueError((h,W))

def weak_comps(total,n,prefix=()):
    if n==1:
        yield prefix+(total,); return
    for x in range(total+1):
        yield from weak_comps(total-x,n-1,prefix+(x,))

def parse_profiles(path):
    out=[]
    for line in Path(path).read_text().splitlines():
        if not line or line.startswith('#'): continue
        lhs,rhs=line.split('|')
        s=tuple(map(int,lhs.split()))
        q=int(rhs.strip().split('=')[1])
        assert len(s)==13 and tuple(sorted(s))==s and 18<=q<=21
        out.append((s,q))
    return out

def score(s):
    gs={}
    for h in range(2,13):
        W=sum(x for x in s if x>=h)
        gs[h]=g(h,W)
    return sum(s)-sum(gs.values()),gs

def hist_from_tails(z):
    # z indexed h=2..13 inclusive
    ns=[B-z[2]]
    for h in range(2,13): ns.append(z[h]-z[h+1])
    ns.append(z[13])
    assert len(ns)==13 and min(ns)>=0 and sum(ns)==B
    rho=[]
    for deg,count in enumerate(ns,1):rho += [deg]*count
    return tuple(rho)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--profiles',required=True);ap.add_argument('--output');a=ap.parse_args()
    profiles=parse_profiles(a.profiles)
    assert len(profiles)==100 and len(set(s for s,q in profiles))==100
    qcount=Counter()
    rows=[]
    for s,q_decl in profiles:
        q,gs=score(s);assert q==q_decl
        qcount[q]+=1
        k=q-18
        base={h:gs[h] for h in range(2,13)};base[13]=0
        for used in range(k+1):
            for inc in weak_comps(used,12):
                z={h:base[h]+inc[h-2] for h in range(2,14)}
                if any(z[h]<z[h+1] for h in range(2,13)):continue
                if z[2]>B:continue
                rho=hist_from_tails(z)
                lam=k-used
                r=sum(rho)
                assert sum(s)==r+2+lam
                rows.append((s,rho,q,lam))
    assert qcount==Counter({18:64,19:29,20:6,21:1})
    assert len(rows)==272 and len(set((s,rho) for s,rho,q,lam in rows))==272
    split=Counter((q,lam) for s,rho,q,lam in rows)
    assert dict(split)==EXPECTED
    assert len(HIST_IDS)==len(profiles)
    s_to_id={s:i for (s,q),i in zip(profiles,HIST_IDS)}
    normalized=[]
    for s,rho,q,lam in rows:
        normalized.append((s_to_id[s],sum(rho),rho))
    text='\n'.join(' '.join(map(str,(i,r,*rho))) for i,r,rho in sorted(normalized))+'\n'
    reconstructed_hash=sha256(text.encode()).hexdigest()
    assert reconstructed_hash==HISTORICAL_NORMALIZED_SHA256
    positive_slack=sum(1 for s,rho,q,lam in rows if lam>0)
    assert positive_slack==61
    assert all(all(x>0 for x in s) for s,rho,q,lam in rows if lam>0)
    tight=sum(1 for x in rows if x[3]==0);assert tight==211
    out={'schema':'n30-m225-threshold-slack-reduction-v1','status':'PASS','solver_used':False,'floating_point_used':False,
         'profiles':len(profiles),'profile_Q_counts':dict(sorted(qcount.items())),'rows':len(rows),
         'Q_lambda_counts':{f'{q},{lam}':n for (q,lam),n in sorted(split.items())},
         'positive_ledger_slack_rows':positive_slack,'ledger_tight_rows':tight,
         'reconstructed_historical_row_sha256':reconstructed_hash,
         'historical_row_artifact_normalized_sha256':HISTORICAL_NORMALIZED_SHA256,
         'conclusion':'The 100 Q>=18 demand profiles generate exactly 272 monotone residual-tail rows from at most three units of threshold/ledger slack; 61 have positive ledger slack and are analytically impossible because all their demands are positive, leaving 211 tight rows.'}
    t=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if a.output:Path(a.output).write_text(t)
    print(t,end='')
if __name__=='__main__':main()
