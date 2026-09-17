#!/usr/bin/env python3
"""Exact arithmetic checker for the zero-residual boundary cutoff.

The hand proof reduces any non-bipartite high-density boundary graph to integers
a>=1, lambda>=1 and some z in [ceil(a/2),a] satisfying

    z! <= b * lambda^z,

where b=a+1+lambda and

    b(a+1) >= floor((2a+1+lambda)^2/4)+1.

A separate hand estimate in ZERO_RESIDUAL_BOUNDARY.md rules out a>=1296.
This checker exhausts the remaining range exactly.
"""

from math import factorial


def threshold(a, lam):
    b = a + 1 + lam
    n = 2*a + 2 + lam
    M = ((n-1)*(n-1))//4 + 1
    return b, n, M


def density_ok(a, lam):
    b, _, M = threshold(a, lam)
    return b*(a+1) >= M


def factorial_possible(a, lam):
    b, _, _ = threshold(a, lam)
    lo = (a+1)//2
    # f(z)=z!/lam^z decreases while z+1<lam and increases afterwards.
    # Hence one of these interval/break-point candidates minimizes f.
    cand = {lo, a}
    for z in (lam-1, lam):
        if lo <= z <= a:
            cand.add(z)
    return [z for z in sorted(cand) if factorial(z) <= b*(lam**z)]


def main():
    feasible = []
    for a in range(1, 1296):
        # The density inequality is quadratic in lambda and, past its small
        # initial range, fails monotonically. The generous 2a+2 ceiling is
        # only a deterministic finite guard.
        for lam in range(1, 2*a+3):
            if not density_ok(a, lam):
                if lam > 2:
                    break
                continue
            good = factorial_possible(a, lam)
            if good:
                b, n, M = threshold(a, lam)
                feasible.append((a, lam, good[0], n, b, M))

    assert feasible
    max_a = max(x[0] for x in feasible)
    max_n = max(x[3] for x in feasible)
    top_a = [x for x in feasible if x[0] == max_a]
    top_n = [x for x in feasible if x[3] == max_n]

    assert max_a == 134
    assert max_n == 294
    assert top_a == [(134, 24, 67, 294, 159, 21463)]
    assert top_n == top_a

    print("PASS_ZERO_RESIDUAL_BOUNDARY_FINITE_ARITHMETIC")
    print("max_a=134 max_n=294 witness_parameters=(a,lambda,z,b)=(134,24,67,159)")


if __name__ == "__main__":
    main()
