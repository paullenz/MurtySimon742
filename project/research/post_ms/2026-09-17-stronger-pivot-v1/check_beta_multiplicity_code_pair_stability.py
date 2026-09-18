import itertools
import json
import math
from collections import Counter

import networkx as nx


def is_d2c(G):
    if len(G) < 3 or not nx.is_connected(G):
        return False
    if nx.diameter(G) != 2:
        return False
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def antipode_data(G, v):
    B = set(G.neighbors(v))
    antipodes = {}
    for u, w in itertools.combinations(sorted(B), 2):
        if G.has_edge(u, w):
            continue
        if set(nx.common_neighbors(G, u, w)) == {v}:
            holes = {
                z
                for z in G.nodes()
                if z not in {v, u, w}
                and not G.has_edge(z, u)
                and not G.has_edge(z, w)
            }
            antipodes[frozenset((u, w))] = len(holes)
    return B, antipodes


def partial_code(G, z, pairs):
    bits = []
    for a, b in pairs:
        aa = G.has_edge(z, a)
        bb = G.has_edge(z, b)
        if aa == bb:
            raise AssertionError(("not a transversal", z, (a, b), aa, bb))
        bits.append(1 if bb else 0)
    return tuple(bits)


def check_matched_hub_baf():
    atlas = [G.copy() for G in nx.graph_atlas_g() if len(G) >= 3 and is_d2c(G)]
    counts = Counter()
    min_margin = None
    violations = []
    code_violations = []

    for gi, G in enumerate(atlas):
        for v in G.nodes():
            counts["root_instances"] += 1
            B, antipodes = antipode_data(G, v)
            tight = [
                tuple(sorted(tuple(e)))
                for e, eta in antipodes.items()
                if eta == 0
            ]
            if not tight:
                continue
            counts["roots_with_tight_pair"] += 1

            flat = [x for e in tight for x in e]
            if len(set(flat)) != len(flat):
                violations.append(("tight-not-matching", gi, v, tight))
                continue

            pairs = sorted(tight)
            P = set(flat)
            U = B - P

            for q in P:
                Y = []
                etas = {}
                for y in U:
                    key = frozenset((q, y))
                    if key in antipodes:
                        Y.append(y)
                        etas[y] = antipodes[key]
                if not Y:
                    continue

                counts["matched_hubs_with_unmatched_antipodes"] += 1
                counts["matched_hub_partner_incidences"] += len(Y)
                if len(Y) >= 2:
                    counts["matched_hub_branching_centres"] += 1

                codes = [partial_code(G, y, pairs) for y in Y]
                if len(set(codes)) != 1:
                    code_violations.append((gi, v, q, Y, codes))

                d = len(Y)
                nonedges = sum(
                    1
                    for y, z in itertools.combinations(Y, 2)
                    if not G.has_edge(y, z)
                )
                lhs = sum(etas.values())
                rhs = math.comb(d, 2) + nonedges
                margin = lhs - rhs
                min_margin = margin if min_margin is None else min(min_margin, margin)
                if margin < 0:
                    violations.append(
                        ("matched-hub-baf", gi, v, q, Y, etas, nonedges, lhs, rhs)
                    )

    return {
        "d2c_atlas_classes": len(atlas),
        **dict(counts),
        "matched_hub_min_margin": min_margin,
        "matched_hub_baf_violations": len(violations),
        "matched_hub_code_violations": len(code_violations),
    }


def complement(x, p):
    return ((1 << p) - 1) ^ x


def beta_pool(c, p):
    bc = complement(c, p)
    return {bc ^ (1 << i) for i in range(p)}


def check_beta_pair_incidence():
    checked_pairs = 0
    checked_code_incidences = 0
    violations = []

    for p in range(3, 11):
        reps = []
        seen = set()
        for c in range(1 << p):
            cc = complement(c, p)
            rep = min(c, cc)
            if rep in seen:
                continue
            seen.add(rep)
            reps.append((c, cc))

        unions = []
        for c, cc in reps:
            Bc = beta_pool(c, p)
            Bcc = beta_pool(cc, p)
            checked_pairs += 1
            if Bc & Bcc:
                violations.append(("complement-pools-not-disjoint", p, c, sorted(Bc & Bcc)))
            if len(Bc) != p or len(Bcc) != p or len(Bc | Bcc) != 2 * p:
                violations.append(("wrong-pool-size", p, c))
            unions.append(Bc | Bcc)

        for d in range(1 << p):
            incidence = sum(d in U for U in unions)
            checked_code_incidences += 1
            if incidence != p:
                violations.append(("wrong-pair-incidence", p, d, incidence))

    return {
        "hypercube_p_min": 3,
        "hypercube_p_max": 10,
        "complement_pairs_checked": checked_pairs,
        "code_pair_incidences_checked": checked_code_incidences,
        "hypercube_violations": len(violations),
    }


def check_generic_pair_rounding():
    checked = 0
    violations = []
    for t in range(41):
        for s in range(41):
            checked += 1
            best = None
            for ec in range(81):
                for eb in range(81):
                    if t <= ec + 3 * eb and s <= 3 * ec + eb:
                        val = ec + eb
                        if best is None or val < best:
                            best = val
            lower = math.ceil(max((t + s) / 4, t / 3, s / 3))
            if best is None or best < lower:
                violations.append((t, s, best, lower))
    return {
        "generic_pair_integer_cases_checked": checked,
        "generic_pair_rounding_violations": len(violations),
    }


def main():
    out = {}
    out.update(check_matched_hub_baf())
    out.update(check_beta_pair_incidence())
    out.update(check_generic_pair_rounding())
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
