#!/usr/bin/env python3
"""Finite algebra audit for same-code crowding / complementary-pair localization.

This is diagnostic support only.  The promoted statements are the hand proofs
in SAME_CODE_CROWDING_COMPLEMENT_PAIR_LOCALIZATION.md.
"""
from math import ceil, floor, sqrt
import random, json

counts = {
    "crowding_complement_forcing": 0,
    "weighted_pair_payment": 0,
    "aligned_au_capacity": 0,
    "pair_traffic_localization": 0,
    "global_aligned_code_cap": 0,
}
failures = []

def fail(tag, data):
    failures.append({"tag": tag, "data": data})
    raise AssertionError((tag, data))

# 1. Primitive crowding + pure same-code edge capacity imply CF-A/CF-U/CF-V.
for T in range(-1, 4):
    for n in range(5):
        for t in range(5):
            N = n + t
            for nb in range(5):
                for tb in range(5):
                    M = nb + tb
                    for L in range(7):
                        eminA = max(0, ceil((n*(n-T)-L)/2))
                        if eminA <= n*M:
                            counts["crowding_complement_forcing"] += 1
                            if L < max(0, n*(n-T-2*M)):
                                fail("CF-A", (T,n,t,nb,tb,L))
                        for E in range(7):
                            S = L + E
                            eminV = max(0, ceil((N*(N-T)-t-S)/2))
                            if eminV <= N*M:
                                counts["crowding_complement_forcing"] += 1
                                if S < max(0, N*(N-T-2*M)-t):
                                    fail("CF-V", (T,n,t,nb,tb,L,E))
                    for E in range(7):
                        eminU = max(0, ceil((t*(t-T-1)-E)/2))
                        # U-source same-code witnesses must lie in A_bar.
                        if eminU <= t*nb:
                            counts["crowding_complement_forcing"] += 1
                            if E < max(0, t*(t-T-1-2*nb)):
                                fail("CF-U", (T,n,t,nb,tb,E))

# 2. Weighted same-code capacity + crowding imply code-pair scorecard bounds.
for T in range(-1, 2):
    for lam in range(3):
        lp1 = lam + 1
        for n in range(4):
            for t in range(4):
                N = n+t
                for nb in range(4):
                    for tb in range(4):
                        M = nb+tb
                        Lmax = max(N,M)
                        for Lc in range(4):
                            for Ec in range(4):
                                Sc=Lc+Ec
                                for Lb in range(4):
                                    for Eb in range(4):
                                        Sb=Lb+Eb
                                        SP=Sc+Sb
                                        D=N*(N-T)-t
                                        emin=max(0,ceil((D-Sc)/2))
                                        emax=min(N*M, floor((M*Sc+N*Sb)/lp1))
                                        if emin <= emax:
                                            counts["weighted_pair_payment"] += 1
                                            if SP*(2*Lmax+lp1) < lp1*max(0,D):
                                                fail("CPP-V", (T,lam,n,t,nb,tb,Lc,Ec,Lb,Eb))
                                        DU=t*(t-T-1)
                                        eminU=max(0,ceil((DU-Ec)/2))
                                        emaxU=min(t*nb, floor((nb*Ec+t*Lb)/lp1))
                                        if eminU <= emaxU:
                                            counts["weighted_pair_payment"] += 1
                                            if SP*(2*Lmax+lp1) < lp1*max(0,DU):
                                                fail("CPP-U", (T,lam,n,t,nb,tb,Lc,Ec,Lb,Eb))
                                        Db=M*(M-T)-tb
                                        eminb=max(0,ceil((Db-Sb)/2))
                                        emaxb=min(M*N, floor((N*Sb+M*Sc)/lp1))
                                        if emin <= emax and eminb <= emaxb:
                                            counts["weighted_pair_payment"] += 1
                                            if SP*(4*Lmax+lp1) < lp1*max(0,D+Db):
                                                fail("CPP-P", (T,lam,n,t,nb,tb,Lc,Ec,Lb,Eb))

# 3. Pair-summed A/U cylinder capacity has the aligned-code coefficient mu_*.
for lam in range(4):
    lp1=lam+1
    for n in range(5):
        for t in range(5):
            N=n+t
            for nb in range(5):
                for tb in range(5):
                    M=nb+tb
                    wc=N+n
                    wb=M+nb
                    mu=max(wc,wb)
                    for Lc in range(5):
                        for Ec in range(5):
                            Sc=Lc+Ec
                            for Lb in range(5):
                                for Eb in range(5):
                                    Sb=Lb+Eb
                                    SP=Sc+Sb
                                    Cc=floor((M*Lc+n*Sb)/lp1)
                                    Cb=floor((N*Lb+nb*Sc)/lp1)
                                    counts["aligned_au_capacity"] += 1
                                    if lp1*(Cc+Cb) > mu*SP:
                                        fail("AUC5+", (lam,n,t,nb,tb,Lc,Ec,Lb,Eb,Cc,Cb))

# 4. Cauchy pair-localization checked on deterministic pseudo-random pair tables.
rng=random.Random(74220260918)
for _ in range(20000):
    h=rng.randint(1,8)
    records=[]
    for __ in range(h):
        A=rng.randint(0,8)
        V=rng.randint(A,12)
        C=rng.randint(0,A*V)
        records.append((A,V,C))
    a=sum(x[0] for x in records)
    W=sum(x[1] for x in records)
    Mtot=sum(x[2] for x in records)
    Cmax=max(x[2] for x in records)
    counts["pair_traffic_localization"] += 1
    if Mtot*Mtot > Cmax*a*W:
        fail("PT2", records)

# 5. Eliminate the complement mass from CF-V and check the finite root cap.
for T in range(-2,4):
    for W in range(1,13):
        D0=T+2*W+1
        for n in range(W+1):
            for t in range(W-n+1):
                N=n+t
                wc=N+n
                for M in range(W-N+1):
                    for S in range(15):
                        emin=max(0,ceil((N*(N-T)-t-S)/2))
                        if emin <= N*M:
                            counts["global_aligned_code_cap"] += 1
                            lower=max(0,(wc/2)*(3*wc/2-D0))
                            if S + 1e-12 < lower:
                                fail("WC-global", (T,W,n,t,M,S,wc,lower))
                            root=(D0+sqrt(D0*D0+12*S))/3
                            if wc > floor(root+1e-12):
                                fail("R-code", (T,W,n,t,M,S,wc,root))

summary = {
    "status": "ok" if not failures else "failure",
    "checks": counts,
    "total_checks": sum(counts.values()),
    "failures": failures,
    "scope": "finite algebra audit only; does not replace D2C structural proofs",
}
print(json.dumps(summary, indent=2, sort_keys=True))
