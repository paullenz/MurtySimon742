#!/usr/bin/env python3
"""Conservative diagnostic for HBL0 using only the root-imbalance beta floor.

This is intentionally NOT a proof search.  It tests whether the new Hall/beta
localization theorem can gain anything if one discards the switching beta floor
and all positive local resource terms.  A zero-closure result diagnoses exactly
which information must be retained next.
"""

import math


def c_hat(p,u,r,K):
    return math.floor(((K+r)/r)*math.comb(u,r)/math.comb(p-K,r))


def phi(p,u,r,N):
    if p<r or u<r:
        return 0
    return sum(max(0,N-c_hat(p,u,r,K)) for K in range(p-r+1))


def main():
    stats={
        "param_tuples":0,
        "with_positive_root_floor":0,
        "source_feasible":0,
        "tau_mass_tests":0,
        "hbl_mass_exclusions":0,
        "tau_all_excluded":0,
    }

    for p in range(3,31):
        for u in range(3,2*p+1):
            for lam in range(0,2*p+u-1):
                a=2*p+u-lam-1
                if a<=0:
                    continue
                stats["param_tuples"]+=1

                # Deliberately use only the root-imbalance beta floor.
                B0=max(0,p*(lam+1-2*p))
                if B0<=0:
                    continue
                stats["with_positive_root_floor"]+=1

                # Retain only tuples not already killed by the r=3 global
                # integrated source-capacity inequality.
                if B0>a*p-phi(p,u,3,a):
                    continue
                stats["source_feasible"]+=1

                for tau in range(0,p+1):
                    admissible=[]
                    for x in range(1,a):
                        y=a-x
                        # Hamming-corrected low-density mass condition.
                        if y>p*(p-tau)/(p-1):
                            admissible.append(x)
                    if not admissible:
                        continue

                    all_bad=True
                    for x in admissible:
                        y=a-x
                        stats["tau_mass_tests"]+=1
                        F=x*(u+tau)+y*p-phi(p,u,3,y)
                        bad=(B0>=F)
                        if bad:
                            stats["hbl_mass_exclusions"]+=1
                        else:
                            all_bad=False
                    if all_bad:
                        stats["tau_all_excluded"]+=1

    for key,value in stats.items():
        print(f"{key}={value}")


if __name__=="__main__":
    main()
