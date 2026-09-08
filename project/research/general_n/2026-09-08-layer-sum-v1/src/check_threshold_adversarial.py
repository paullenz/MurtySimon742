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
    # Vertices 0..z-1 are Z_h. A counted arc is an oriented unordered pair
    # whose source lies in Z_h. If a source has load > h, every endpoint of
    # its counted arcs must also lie in Z_h. This is exactly the abstract
    # consequence used in the pair-capacity proof; outside-source arcs are
    # irrelevant and omitted.
    admitted = states = 0
    worst_gap = None
    equality_hits = 0
    for n in range(1, max_n+1):
        pairs = list(combinations(range(n),2))
        for z in range(1,n+1):
            for h in range(z+1):
                opts = []
                for u,v in pairs:
                    choices = [0]
                    if u < z:
                        choices.append(1)  # u -> v
                    if v < z:
                        choices.append(2)  # v -> u
                    opts.append(choices)
                for choice_vec in product(*opts):
                    states += 1
                    load = [0]*z
                    endpoints = [[] for _ in range(z)]
                    used = set()
                    for (u,v),c in zip(pairs,choice_vec):
                        if c == 1:
                            require((u,v) not in used, 'pair reuse')
                            used.add((u,v)); load[u] += 1; endpoints[u].append(v)
                        elif c == 2:
                            require((u,v) not in used, 'pair reuse')
                            used.add((u,v)); load[v] += 1; endpoints[v].append(u)
                    if any(load[u] > h and any(v >= z for v in endpoints[u]) for u in range(z)):
                        continue
                    admitted += 1
                    j = sum(load[u] > h for u in range(z))
                    total = sum(load)
                    pair_count = j*z - j*(j+1)//2
                    direct = (z-j)*h + pair_count
                    bound = h*z + (z-h)*(z-h-1)//2
                    require(total <= direct, ('direct',n,z,h,j,total,direct,load,endpoints))
                    require(direct <= bound, ('quadratic',n,z,h,j,direct,bound))
                    gap = bound-total
                    worst_gap = gap if worst_gap is None else min(worst_gap,gap)
                    equality_hits += (gap == 0)
    return {"max_n":max_n,"states":states,"admitted":admitted,
            "minimum_bound_gap":worst_gap,"equality_hits":equality_hits}


def negative_controls():
    # Allowing both orientations of an unordered pair destroys the premise.
    z,h = 4,1
    illegal_total = 12  # complete bidirected graph on four sources
    bound = h*z + (z-h)*(z-h-1)//2
    require(illegal_total > bound, (illegal_total,bound))
    # Allowing a >h source to spend arcs outside Z also destroys the proof.
    z,h = 2,1
    illegal_total = 4
    bound = h*z + (z-h)*(z-h-1)//2
    require(illegal_total > bound, (illegal_total,bound))
    return {"opposite_orientations":"violate as expected",
            "high_source_outside_Z":"violate as expected"}


def main():
    out = {
        "schema":"threshold-capacity-adversarial-v1",
        "arithmetic": arithmetic_sweep(),
        "marked_orientation_model": enumerate_marked_orientations(),
        "negative_controls": negative_controls(),
        "status":"PASS",
        "claim_scope":"abstract pair-capacity lemma only; not a proof of the graph-to-model reduction"
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
