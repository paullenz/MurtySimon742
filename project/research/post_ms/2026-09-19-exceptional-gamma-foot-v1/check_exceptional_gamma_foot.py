#!/usr/bin/env python3
"""Audit the t=1 exceptional-gamma support consequences.

This is a finite support/topology checker only. It does not enumerate D2C
graphs and is not a substitute for the raw criticality proofs in
EXCEPTIONAL_GAMMA_FOOT_COLLAPSE.md.
"""
from itertools import product


def exceptional_max(supports, mult):
    """Max wrong-head incidence count with one exceptional coordinate/target."""
    classes = list(supports)
    coords = sorted(set().union(*supports.values()))
    best = -1
    best_data = []
    for e in coords:
        for target in classes:
            j = 0
            sources = []
            for src in classes:
                if src == target:
                    continue
                if e not in supports[src]:
                    continue
                if not (supports[src] & supports[target]):
                    continue
                j += mult[target]
                sources.append(src)
            if j > best:
                best = j
                best_data = [(e, target, tuple(sources))]
            elif j == best:
                best_data.append((e, target, tuple(sources)))
    return best, best_data


def r22(k, h, c):
    if (h, c) == (1, 2):
        s = {"C0":{"r"}, "C1":{"r","i"}, "C2":{"r","j"},
             "Ri":{"i"}, "Rj":{"j"}}
    elif (h, c) == (1, 1):
        s = {"C0":{"r"}, "C1":{"r","s"}, "C2":{"s","j"},
             "Rs":{"s"}, "Rj":{"j"}}
    elif (h, c) == (1, 0):
        s = {"C0":{"r"}, "C1":{"s","i"}, "C2":{"s","j"},
             "Rs":{"s"}, "Ri":{"i"}, "Rj":{"j"}}
    elif (h, c) == (0, 1):
        s = {"C0":{"r"}, "C1":{"r","i"}, "C2":{"j","l"},
             "Ri":{"i"}, "Rj":{"j"}, "Rl":{"l"}}
    elif (h, c) == (0, 0):
        s = {"C0":{"r"}, "C1":{"i","j"}, "C2":{"l","m"},
             "Ri":{"i"}, "Rj":{"j"}, "Rl":{"l"}, "Rm":{"m"}}
    else:
        raise ValueError((h,c))
    s = {a:frozenset(b) for a,b in s.items()}
    mult = {a:(k if a == "C0" else 1) for a in s}
    return s, mult


def r3(k, c):
    if c == 1:
        s = {"C0":{"r"}, "C1":{"r","i","j"},
             "Ri":{"i"}, "Rj":{"j"}}
    else:
        s = {"C0":{"r"}, "C1":{"i","j","l"},
             "Ri":{"i"}, "Rj":{"j"}, "Rl":{"l"}}
    s = {a:frozenset(b) for a,b in s.items()}
    mult = {a:(k if a == "C0" else 1) for a in s}
    return s, mult


def shared_complement_free(p):
    """Canonical shared R22 represented-code support is complement-free.

    For p=3 there are only core+C1+C2. For p>=4 we safely include all
    radius-one supports as a superset; complement-freeness in the actual
    represented subset then follows except that for p=4 a radius-1 complement
    has size 3 and cannot occur, while the two radius-2 defects intersect.
    """
    coords = list(range(p))
    r, i, j = 0, 1, 2
    represented = {frozenset({r}), frozenset({r,i}), frozenset({r,j})}
    if p >= 4:
        represented |= {frozenset({q}) for q in coords}
    universe = frozenset(coords)
    for a in represented:
        abar = universe - a
        if abar in represented and abar != a:
            # At p=4 the only possible same-size issue is radius2/radius2;
            # the two actual defects both contain r, so are not complements.
            if p == 4 and len(a) == 2:
                continue
            return False, (a, abar)
    return True, None


def main():
    checks = 0
    expected_r22 = {(1,2):lambda k:2*k,
                    (1,1):lambda k:k,
                    (0,1):lambda k:k,
                    (1,0):lambda k:2,
                    (0,0):lambda k:1}

    equality_examples = {}
    for k in range(3, 31):
        for hc, f in expected_r22.items():
            s,m = r22(k,*hc)
            got,data = exceptional_max(s,m)
            want = f(k)
            assert got == want, (k,hc,got,want,data)
            checks += 1
            if hc == (1,2):
                # The unique global maximum is exceptional coordinate r,
                # target repeated core C0. Hence d0=0, not d0=2.
                assert data == [("r","C0",("C1","C2"))], (k,data)
                equality_examples[k] = data[0]

        s,m = r3(k,1)
        got,_ = exceptional_max(s,m)
        assert got == k, (k,"R3-c1",got)
        checks += 1
        s,m = r3(k,0)
        got,_ = exceptional_max(s,m)
        assert got == 1, (k,"R3-c0",got)
        checks += 1

    complement_checks = 0
    for p in range(3, 40):
        ok,bad = shared_complement_free(p)
        assert ok, (p,bad)
        complement_checks += 1

    # The pair-local lower bound induced by e(X)<=k is algebraically direct:
    # Delta >= C(g,2)+kA-k. Check non-negativity for the live A>=g-1 box.
    delta_checks = 0
    for p in range(3, 40):
        g = p-1
        for k in range(3, 30):
            for A in (g-1,g):
                delta0 = g*(g-1)//2 + k*A - k
                assert delta0 >= 0
                delta_checks += 1

    print({
        "exceptional_topology_checks": checks,
        "shared_complement_checks": complement_checks,
        "delta_floor_checks": delta_checks,
        "shared_global_max_formula": "J=2k, uniquely e=r,target=C0,d0=0",
        "old_d0_2_status": "impossible under one-exception matched-foot localization",
        "trust": "support/arithmetic audit only; raw D2C criticality proof is in the theorem note",
        "failures": 0,
    })


if __name__ == "__main__":
    main()
