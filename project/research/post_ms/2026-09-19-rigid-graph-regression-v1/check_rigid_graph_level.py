#!/usr/bin/env python3
"""Independent graph-level regression for the rigid Hall / pair-capacity interface.

The checker starts from actual graphs.  It does not import the earlier source-
premise checker and does not treat abstract incidence data as graph evidence.

It reconstructs:
  * D2C status and the rooted A/B partition;
  * tight antipode fibres, unmatched B vertices, and A/U Boolean codes;
  * an independent rooted B-edge witness-slot injection and unused slots;
  * direct/non-direct A-edges and fixed criticality certificates;
  * matched-foot gamma codes and A/U complement localization;
  * complementary-pair L,S,Z,R,g,h,Ccap data;
  * the exact Hall-cut decomposition;
  * rigid singleton-head / U-deficit quantities whenever a rigid cut occurs;
  * one-sided-pair h_P=0 and matched traffic localization.

The mandatory X_3 negative control is explicit.  X_4 and X_5 in the same
cube-face family are included as exact-saturation controls outside the tight-
fibre branch.
"""

from collections import Counter, defaultdict
from fractions import Fraction
import itertools
import math
import random

import networkx as nx


SEED_TAG = 20260919
POLICIES = ("lex", "matched_first", "au_first")


def M(n):
    return ((n - 1) ** 2) // 4 + 1


def is_d2c(G):
    if len(G) < 3 or not nx.is_connected(G) or nx.diameter(G) != 2:
        return False
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def tight_pair(G, v, u, w):
    if u not in G[v] or w not in G[v] or G.has_edge(u, w):
        return False
    if set(nx.common_neighbors(G, u, w)) != {v}:
        return False
    for z in G:
        if z in (v, u, w):
            continue
        if int(G.has_edge(z, u)) + int(G.has_edge(z, w)) != 1:
            return False
    return True


def rooted_partition(G, v):
    B = set(G.neighbors(v))
    A = set(G) - B - {v}
    pairs = []
    for u, w in itertools.combinations(sorted(B), 2):
        if tight_pair(G, v, u, w):
            pairs.append((u, w))
    flat = [z for pair in pairs for z in pair]
    assert len(flat) == len(set(flat)), ("overlapping tight pairs", v, pairs)
    U = B - set(flat)
    return A, B, U, pairs


def complement(code):
    return tuple(1 - bit for bit in code)


def pair_key(code):
    code = tuple(code)
    return min(code, complement(code))


def boolean_codes(G, v):
    A, B, U, pairs = rooted_partition(G, v)
    codes = {}
    for z in A | U:
        bits = []
        for q0, q1 in pairs:
            b0 = G.has_edge(z, q0)
            b1 = G.has_edge(z, q1)
            assert b0 != b1, ("non-transversal coded vertex", v, z, q0, q1)
            bits.append(0 if b0 else 1)
        codes[z] = tuple(bits)
    return codes


def rooted_B_selection(G, v):
    """Choose one independent criticality slot for each rooted B-edge."""
    A, B, U, pairs = rooted_partition(G, v)
    selected = []
    for u, w in G.subgraph(B).edges():
        candidates = []
        for source, head in ((u, w), (w, u)):
            for z in A:
                if G.has_edge(source, z) or not G.has_edge(z, head):
                    continue
                if set(nx.common_neighbors(G, source, z)) == {head}:
                    candidates.append((source, z, head))
        assert candidates, ("rooted B-edge has no A witness", v, u, w)
        candidates.sort(key=lambda t: tuple(map(repr, t)))
        selected.append(candidates[0])
    assert len({(s, z) for s, z, _ in selected}) == len(selected), (
        "selected rooted slot not injective",
        v,
    )
    return selected


def A_edge_certificates(G, v, policy="lex"):
    """Fix one certificate for every non-direct A-edge.

    Direct means the A-edge lies in no triangle.  For a non-direct edge, the
    standard triangle-edge criticality certificate is reconstructed directly.
    """
    A, B, U, pairs = rooted_partition(G, v)
    matched = {z for pair in pairs for z in pair}
    out = {}
    for a, b in G.subgraph(A).edges():
        edge = frozenset((a, b))
        if not set(nx.common_neighbors(G, a, b)):
            out[edge] = ("direct", None, None, None)
            continue
        candidates = []
        for source, head in ((a, b), (b, a)):
            for w in G:
                if w in (source, head):
                    continue
                if G.has_edge(source, w) or not G.has_edge(w, head):
                    continue
                if set(nx.common_neighbors(G, source, w)) == {head}:
                    channel = 0 if w in matched else 1
                    candidates.append((source, w, head, channel))
        assert candidates, ("non-direct A-edge has no certificate", v, a, b)
        if policy == "matched_first":
            candidates.sort(key=lambda t: (t[3], repr(t[0]), repr(t[1]), repr(t[2])))
        elif policy == "au_first":
            candidates.sort(key=lambda t: (1 - t[3], repr(t[0]), repr(t[1]), repr(t[2])))
        else:
            candidates.sort(key=lambda t: (repr(t[0]), repr(t[1]), repr(t[2])))
        source, w, head, _ = candidates[0]
        out[edge] = ("non-direct", source, w, head)
    return out


def gamma_codes(G, v, pairs):
    """Graph-theoretic row-complement gamma code for matched endpoints."""
    gamma = {}
    index = {}
    for i, (q0, q1) in enumerate(pairs):
        index[q0] = (i, 0)
        index[q1] = (i, 1)
    for w, (i, side) in index.items():
        bits = []
        for j, (q0, q1) in enumerate(pairs):
            if i == j:
                bits.append(1 - side)
                continue
            b0 = G.has_edge(w, q0)
            b1 = G.has_edge(w, q1)
            assert b0 != b1, ("matched endpoint not transversal", v, w, j)
            # gamma chooses the endpoint opposite w's matched-B neighbour.
            bits.append(1 if b0 else 0)
        gamma[w] = tuple(bits)
    for q0, q1 in pairs:
        assert gamma[q1] == complement(gamma[q0])
    return gamma, index


def root_data(G, v, policy="lex"):
    assert is_d2c(G), ("fixture is not D2C", len(G), G.number_of_edges())
    A, B, U, pairs = rooted_partition(G, v)
    codes = boolean_codes(G, v)
    gamma, matched_index = gamma_codes(G, v, pairs)
    matched = set(matched_index)

    a, b, p, u = len(A), len(B), len(pairs), len(U)
    lam = 2 * p + u - a - 1
    L = lam + 1
    D0 = 5 * p + 5 * u - 3 * lam - 2
    eps = {z: b - G.degree(z) for z in A | U | matched}

    selected_B = rooted_B_selection(G, v)
    selected_slots = {(source, z) for source, z, _ in selected_B}
    r_z = {
        z: sum(
            1
            for q in B
            if not G.has_edge(q, z) and (q, z) not in selected_slots
        )
        for z in A
    }

    A_certs = A_edge_certificates(G, v, policy)

    keys = {pair_key(codes[z]) for z in A}
    keys |= {pair_key(gamma[w]) for w in matched}
    pstats = {}
    for P in keys:
        Aset = {z for z in A if pair_key(codes[z]) == P}
        AUset = {z for z in A | U if pair_key(codes[z]) == P}
        pstats[P] = {
            "Aset": Aset,
            "a": len(Aset),
            "L": sum(eps[z] for z in Aset),
            "S": sum(eps[z] for z in AUset),
            "Z": sum(1 for z in Aset for w in U if not G.has_edge(z, w)),
            "R": sum(r_z[z] * G.subgraph(A).degree(z) for z in Aset),
            "D": 0,
            "t": 0,
            "C": 0,
            "PB": 0,
            "g": 0,
            "h": 0,
        }

    matched_load = Counter()
    for edge, rec in A_certs.items():
        x, y = tuple(edge)
        if rec[0] == "direct":
            P = pair_key(codes[x])
            assert P == pair_key(codes[y])
            assert codes[y] == complement(codes[x])
            pstats[P]["D"] += 1
            continue

        _, source, witness, head = rec
        P = pair_key(codes[source])
        pstats[P]["t"] += 1
        if witness in matched:
            assert codes[source] == gamma[witness], (
                "matched gamma localization failed",
                v,
                source,
                witness,
            )
            pstats[P]["PB"] += 1
            matched_load[witness] += 1
        elif witness in A | U:
            assert codes[witness] == complement(codes[source]), (
                "A/U complement localization failed",
                v,
                source,
                witness,
            )
            pstats[P]["C"] += 1
        else:
            raise AssertionError(("unexpected A-edge witness channel", v, edge, rec))

    for q0, q1 in pairs:
        P = pair_key(gamma[q0])
        pstats.setdefault(
            P,
            {
                "Aset": set(), "a": 0, "L": 0, "S": 0, "Z": 0, "R": 0,
                "D": 0, "t": 0, "C": 0, "PB": 0, "g": 0, "h": 0,
            },
        )
        pstats[P]["g"] += 1
        pstats[P]["h"] += min(matched_load[q0], matched_load[q1])

    if L > 0:
        for P, d in pstats.items():
            s = d["S"]
            Rcode = max(0, math.floor((D0 + math.sqrt(D0 * D0 + 12 * s)) / 3))
            d["Rcode"] = Rcode
            d["Ccap"] = Rcode * (d["g"] + Fraction(2 * s, L)) + 2 * d["h"]

    return {
        "A": A, "B": B, "U": U, "pairs": pairs, "codes": codes,
        "gamma": gamma, "matched": matched, "eps": eps,
        "a": a, "b": b, "p": p, "u": u, "lambda": lam, "L": L,
        "D0": D0, "selected_B": selected_B, "r_z": r_z,
        "A_certs": A_certs, "pstats": pstats,
    }


def verify_root(G, v, policy="lex", exhaustive_cuts=True):
    D = root_data(G, v, policy)
    A, B, U = set(D["A"]), set(D["B"]), set(D["U"])
    a, b, p, u, lam = D["a"], D["b"], D["p"], D["u"], D["lambda"]
    stats = Counter()
    stats["roots"] += 1

    # The pair/slack package is used only in the nonnegative-lambda branch.
    if p == 0 or lam < 0:
        return stats
    assert all(D["eps"][z] >= 0 for z in A | U)
    stats["qualified_roots"] += 1

    n, m = len(G), G.number_of_edges()
    f = G.subgraph(A).number_of_edges()
    Q = G.subgraph(B).number_of_edges()
    r = sum(D["r_z"].values())
    delta = b * (n - b) - m
    assert delta == r - f, ("delta != r-f", v, delta, r, f)

    q = Q - p * (p + u - 1)
    EU = sum(D["eps"][z] for z in U)
    Z = sum(1 for z in A for w in U if not G.has_edge(z, w))
    assert Z == u * (p - lam) + 2 * q + EU
    assert f == (p - lam) * (p + u) + q + EU - delta
    stats["rooted_residual_identities"] += 1

    # Local rooted-slot Hamming price on direct A-edges.
    dA = dict(G.subgraph(A).degree())
    dD = Counter()
    for edge, rec in D["A_certs"].items():
        if rec[0] == "direct":
            x, y = tuple(edge)
            dD[x] += 1
            dD[y] += 1
    for z in A:
        assert p * dD[z] <= D["r_z"][z] * dA[z]
        stats["local_slot_checks"] += 1

    # Exact pair-local capacities and one-sided pair purity.
    for P, d in D["pstats"].items():
        assert d["t"] == d["C"] + d["PB"]
        assert 2 * d["t"] <= d["Ccap"], ("Ccap failure", v, policy, P, d)
        stats["pair_capacity_checks"] += 1

        c, cb = P, complement(P)
        nc = sum(D["codes"][z] == c for z in A)
        nb = sum(D["codes"][z] == cb for z in A)
        if (nc == 0) ^ (nb == 0):
            assert d["h"] == 0, ("one-sided pair has h>0", v, policy, P, d)
            n_occ = max(nc, nb)
            assert d["PB"] <= d["g"] * n_occ
            stats["one_sided_pair_checks"] += 1

    stats["A_edges"] += len(D["A_certs"])
    stats["direct_A_edges"] += sum(rec[0] == "direct" for rec in D["A_certs"].values())
    stats["nondirect_A_edges"] += sum(rec[0] == "non-direct" for rec in D["A_certs"].values())
    stats["matched_A_certificates"] += sum(
        rec[0] == "non-direct" and rec[2] in D["matched"]
        for rec in D["A_certs"].values()
    )

    active = [P for P, d in D["pstats"].items() if d["a"] > 0]
    if len(active) < 2:
        return stats

    if exhaustive_cuts and len(active) <= 12:
        families = [
            {active[i] for i in range(len(active)) if (mask >> i) & 1}
            for mask in range(1, (1 << len(active)) - 1)
        ]
    else:
        families = [{P} for P in active]

    for keys in families:
        X = set().union(*(D["pstats"][P]["Aset"] for P in keys))
        Y = A - X
        x, y = len(X), len(Y)
        cross = sum(G.has_edge(z, w) for z in X for w in Y)
        missing = x * y - cross

        tX = sum(D["pstats"][P]["t"] for P in keys)
        N_X = 0
        D_X = 0
        crossing_source_X = 0
        for edge, rec in D["A_certs"].items():
            ends = set(edge)
            if ends <= X:
                if rec[0] == "direct":
                    D_X += 1
                else:
                    N_X += 1
            elif len(ends & X) == 1:
                assert rec[0] != "direct", ("direct edge crosses pair family", v, edge)
                if rec[1] in X:
                    crossing_source_X += 1

        E_X = tX - N_X
        assert E_X == crossing_source_X
        LX = sum(D["pstats"][P]["L"] for P in keys)
        ZX = sum(D["pstats"][P]["Z"] for P in keys)
        RX = sum(D["pstats"][P]["R"] for P in keys)
        JX = Fraction(RX, p) - 2 * D_X
        assert JX >= 0

        weight = 2 * tX + LX - ZX + Fraction(RX, p)
        lhs = weight - x * (x - (a - p))
        rhs = 2 * E_X + missing + JX
        assert lhs == rhs, ("exact Hall decomposition", v, policy, keys, lhs, rhs)
        stats["Hall_cut_checks"] += 1

        if x < 3 or y == 0 or E_X != 0 or missing != 0:
            continue

        # Rigid singleton-head regression.  This block is intentionally live
        # even though the current bounded corpus has no such realized cut.
        stats["rigid_cuts"] += 1
        mu_X = sum(sum(G.has_edge(w, z) for z in X) == 1 for w in D["matched"])
        k = max(0, x - mu_X)
        code_occ = defaultdict(list)

        for source in Y:
            witnesses = []
            for head in X:
                rec = D["A_certs"][frozenset((source, head))]
                assert rec[0] == "non-direct"
                _, actual_source, witness, actual_head = rec
                assert actual_source == source and actual_head == head
                assert {z for z in X if G.has_edge(witness, z)} == {head}
                witnesses.append(witness)
                if witness in U:
                    assert D["codes"][witness] == complement(D["codes"][source])
                    code_occ[D["codes"][source]].append((source, witness))
            assert len(witnesses) == len(set(witnesses))
            assert sum(w in U for w in witnesses) >= k

        h = len({D["codes"][z] for z in Y})
        assert h * k <= u
        g0 = x - (a - p)
        for code, occ in code_occ.items():
            sources = {z for z in Y if D["codes"][z] == code}
            W = {w for _, w in occ}
            assert len(W) >= k
            traffic = Counter(w for _, w in occ)
            assert sum(traffic.values()) >= len(sources) * k
            for w, tw in traffic.items():
                assert D["eps"][w] >= max(0, g0 + tw - 1)

        ZX_actual = sum(1 for z in X for w in U if not G.has_edge(z, w))
        ZY_actual = sum(1 for z in Y for w in U if not G.has_edge(z, w))
        assert ZX_actual >= h * k * (x - 1)
        assert ZY_actual >= y * k
        EU = sum(D["eps"][w] for w in U)
        if g0 >= 1:
            assert EU >= k * (y + h * (g0 - 1))
        else:
            assert EU >= max(0, y * k - (1 - g0) * u)
        stats["rigid_witness_checks"] += 1

    return stats


def cube_face_graph(k):
    """X_k: cube Q_k, universal root to cube, and k zero-face vertices."""
    G = nx.Graph()
    cube = [format(i, f"0{k}b") for i in range(2 ** k)]
    faces = [f"a{j}" for j in range(k)]
    G.add_nodes_from(["r"] + faces + cube)
    for s in cube:
        for j in range(k):
            t = s[:j] + ("1" if s[j] == "0" else "0") + s[j + 1 :]
            G.add_edge(s, t)
    for s in cube:
        G.add_edge("r", s)
    for j, a in enumerate(faces):
        for s in cube:
            if s[j] == "0":
                G.add_edge(a, s)
    return G


def verify_cube_face_family():
    out = {}
    for k in (3, 4, 5):
        G = cube_face_graph(k)
        assert is_d2c(G)
        A, B, U, pairs = rooted_partition(G, "r")
        selected = rooted_B_selection(G, "r")
        used = {(s, z) for s, z, _ in selected}
        r = sum(
            1
            for z in A
            for q in B
            if not G.has_edge(q, z) and (q, z) not in used
        )
        f = G.subgraph(A).number_of_edges()
        n, m = len(G), G.number_of_edges()
        assert r == 0 and f == 0
        assert m == (k + 1) * (2 ** k)
        assert n == (2 ** k) + k + 1
        assert m == len(B) * (n - len(B))
        if k == 3:
            assert len(pairs) == 4 and len(U) == 0
            assert m == 32 and M(n) == 31
        else:
            # For k>=4, 2k cube neighbours of a candidate pair cannot cover
            # the other 2^k-2 cube vertices, so no tight transversal pair.
            assert len(pairs) == 0 and U == B
            assert m < M(n)
        out[str(k)] = {
            "n": n,
            "m": m,
            "M": M(n),
            "p": len(pairs),
            "u": len(U),
            "Q": G.subgraph(B).number_of_edges(),
            "r": r,
            "f": f,
        }
    return out


def greedy_d2c_from_complete(n, seed):
    """Deterministically generate an actual D2C graph by edge minimization."""
    rng = random.Random(seed)
    G = nx.complete_graph(n)
    edges = list(G.edges())
    rng.shuffle(edges)
    # Deletability for diameter<=2 is monotone under later edge deletions, so
    # one randomized pass suffices for inclusion-minimality.
    for e in edges:
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            G = H
    assert is_d2c(G)
    return G


def main():
    total = Counter()

    # Entire unlabeled atlas through order 7.
    atlas_classes = 0
    atlas_max_roots = 0
    for G0 in nx.graph_atlas_g():
        if len(G0) < 3:
            continue
        G = nx.convert_node_labels_to_integers(G0)
        if not is_d2c(G):
            continue
        atlas_classes += 1
        maxdeg = max(dict(G.degree()).values())
        for v in G:
            if G.degree(v) != maxdeg:
                continue
            atlas_max_roots += 1
            for policy in POLICIES:
                total += verify_root(G, v, policy)

    # Two fixed larger fixtures: one exercises a nontrivial pair-family Hall
    # cut, the other has a real matched-B candidate for a non-direct A-edge.
    fixed = [
        ("hall_cut_n8", "GdJ@^O", 7),
        ("matched_candidate_n10", "INPCw[`gW", 6),
    ]
    fixed_results = {}
    for name, graph6, root in fixed:
        G = nx.from_graph6_bytes(graph6.encode("ascii"))
        assert is_d2c(G)
        fixed_results[name] = {
            "n": len(G),
            "m": G.number_of_edges(),
            "root": root,
        }
        for policy in POLICIES:
            total += verify_root(G, root, policy)

    # Deterministic generated actual-D2C corpus, n=8..14.
    generated = 0
    generated_max_roots = 0
    for n in range(8, 15):
        for s in range(100):
            G = greedy_d2c_from_complete(n, n * 10000 + s)
            generated += 1
            maxdeg = max(dict(G.degree()).values())
            for v in G:
                if G.degree(v) != maxdeg:
                    continue
                generated_max_roots += 1
                for policy in POLICIES:
                    total += verify_root(G, v, policy)

    cube_family = verify_cube_face_family()

    # Mandatory X_3 also passes the full pair/Hall regression at its cube root.
    X3 = cube_face_graph(3)
    for policy in POLICIES:
        total += verify_root(X3, "r", policy)

    # Explicitly require the matched-first fixed fixture to exercise the
    # matched-B A-edge channel at least once.
    Gm = nx.from_graph6_bytes("INPCw[`gW".encode("ascii"))
    Dm = root_data(Gm, 6, "matched_first")
    assert any(
        rec[0] == "non-direct" and rec[2] in Dm["matched"]
        for rec in Dm["A_certs"].values()
    )

    print(
        {
            "seed_tag": SEED_TAG,
            "certificate_policies": POLICIES,
            "atlas_D2C_classes_through_7": atlas_classes,
            "atlas_max_degree_roots": atlas_max_roots,
            "generated_actual_D2C_graphs": generated,
            "generated_max_degree_roots": generated_max_roots,
            "fixed_fixtures": fixed_results,
            "cube_face_family": cube_family,
            "regression_totals": dict(total),
            "failures": 0,
            "trust_boundary": (
                "actual-graph regression; bounded corpus and fixed certificate "
                "policies are not a proof of universal graph premises"
            ),
        }
    )


if __name__ == "__main__":
    main()
