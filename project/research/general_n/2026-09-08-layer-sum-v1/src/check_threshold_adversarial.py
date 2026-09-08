#!/usr/bin/env python3
from itertools import combinations, product
import json


def require(cond, msg):
    if not cond:
        raise AssertionError(msg)


def exact_identity(z, h, j):
    q = z - h
    lhs = h*z + q*(q-1)//2
    rhs = (z-j)*h + j*z - j*(j+1)//2
    gap2 = 2*(lhs-rhs)
    require(gap2 == (q-j)*(q-j-1), (z,h,j,gap2))
    require(gap2 >= 0, (z,h,j,gap2))
    return gap2


def arithmetic_sweep(limit=250):
    cases = equalities = 0
    for z in range(limit+1):
        for h in range(z+1):
            q = z-h
            for j in range(z+1):
                gap2 = exact_identity(z,h,j)
                cases += 1
                if gap2 == 0:
                    require(j in {q-1,q}, (z,h,j,q))
                    equalities += 1
    return {"cases": cases, "equality_cases": equalities, "limit": limit}


def enumerate_marked_orientations(max_n=6):
    # Enumerate each partial orientation once. For every initial segment Z and
    # every h<=|Z|, count arcs sourced in Z. If such a source has load > h,
    # require all of its counted endpoints to remain in Z. This directly
    # models the two graph consequences used by the threshold proof.
    admitted = checks = orientation_states = 0
    worst_gap = None
    equality_hits = 0
    for n in range(1, max_n+1):
        pairs = list(combinations(range(n),2))
        for choice_vec in product(range(3), repeat=len(pairs)):
            orientation_states += 1
            out = [set() for _ in range(n)]
            for (u,v), c in zip(pairs, choice_vec):
                if c == 1:
                    out[u].add(v)
                elif c == 2:
                    out[v].add(u)
            for z in range(1,n+1):
                Z = set(range(z))
                load = [len(out[u]) for u in range(z)]
                total = sum(load)
                for h in range(z+1):
                    checks += 1
                    if any(load[u] > h and not out[u].issubset(Z) for u in range(z)):
                        continue
                    admitted += 1
                    j = sum(load[u] > h for u in range(z))
                    pair_count = j*z - j*(j+1)//2
                    direct = (z-j)*h + pair_count
                    bound = h*z + (z-h)*(z-h-1)//2
                    require(total <= direct, ('direct',n,z,h,j,total,direct,load))
                    require(direct <= bound, ('quadratic',n,z,h,j,direct,bound))
                    gap = bound-total
                    worst_gap = gap if worst_gap is None else min(worst_gap,gap)
                    equality_hits += (gap == 0)
    return {"max_n":max_n,"orientation_states":orientation_states,
            "checks":checks,"admitted":admitted,
            "minimum_bound_gap":worst_gap,"equality_hits":equality_hits}


def negative_controls():
    z,h = 4,1
    illegal_total = 12
    bound = h*z + (z-h)*(z-h-1)//2
    require(illegal_total > bound, (illegal_total,bound))
    z,h = 2,1
    illegal_total = 4
    bound = h*z + (z-h)*(z-h-1)//2
    require(illegal_total > bound, (illegal_total,bound))
    return {"opposite_orientations":"violate as expected",
            "high_source_outside_Z":"violate as expected"}


def main():
    out = {
        "schema":"threshold-capacity-adversarial-v2",
        "arithmetic": arithmetic_sweep(),
        "marked_orientation_model": enumerate_marked_orientations(),
        "negative_controls": negative_controls(),
        "status":"PASS",
        "claim_scope":"abstract pair-capacity lemma only; not a proof of the graph-to-model reduction"
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
