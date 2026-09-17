#!/usr/bin/env python3
from math import comb
import json

def require(cond, msg):
    if not cond:
        raise AssertionError(msg)

def k_star(h, a, M):
    c = comb(M - h + 1, 2)
    return min(a, M - 1 + c // (h - 1))

def non_square_bound(h, a, M):
    return a * (h - 2) - 1 + k_star(h, a, M) - (h - 2) * M

cases = 0
flat = 0
for h in range(3, 16):
    for a in range(h, 61):
        for M in range(h, min(3 * a, 100) + 1):
            cap = (h - 1) * M + comb(M - h + 1, 2)

            brute = -10**18
            arg = None
            for k in range(h):  # non-square: k <= h-1
                for K in range(k, a + 1):
                    if (h - 1) * K + k <= cap:
                        value = K + k
                        if value > brute:
                            brute = value
                            arg = (K, k)

            closed = (h - 1) + k_star(h, a, M)
            require(
                brute == closed,
                f"objective mismatch h={h} a={a} M={M}: brute={brute} closed={closed} arg={arg}",
            )

            direct = a * (h - 2) + brute - (h - 2) * M - h
            require(
                direct == non_square_bound(h, a, M),
                f"bound mismatch h={h} a={a} M={M}: direct={direct}",
            )
            cases += 1

        require(
            non_square_bound(h, a, h) == (h - 2) * (a - h + 1),
            f"flat-tail mismatch h={h} a={a}",
        )
        flat += 1

print(json.dumps({
    "status": "PASS",
    "scope": "exact integer audit of the staircase-capacity elimination only; graph-theoretic threshold capacity remains a hand theorem",
    "h_range": [3, 15],
    "a_range": "h..60",
    "M_range": "h..min(3a,100)",
    "parameter_cases": cases,
    "flat_tail_cases": flat
}, indent=2))
