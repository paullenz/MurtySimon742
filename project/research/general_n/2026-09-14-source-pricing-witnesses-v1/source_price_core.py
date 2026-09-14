"""Exact source-priced envelopes. Standard library; rational data scaled to ints."""
from __future__ import annotations


def envelope(profile: dict, alpha: list[int], price: list[int], xi: int = 0):
    """Exact upper envelope, not joint incidence optimum. None means empty.

    Retains total excess and every sorted-label-prefix forced-selection bound.
    Zero/uncharged labels still pay incidence prices. Row budgets are dualized.
    """
    s, q, rho, P = (profile[k] for k in ('s', 'q', 'rho', 'P'))
    E, b = profile['Esel'], len(q)
    if len(alpha) != b or len(price) != b or any(v < 0 for v in alpha):
        raise ValueError('Require nonnegative alpha and one signed price per source')
    if xi < 0 or E < 0 or sum(q) != sum(s) + E:
        raise ValueError('Invalid threshold or excess ledger')
    if any(not isinstance(v, int) for v in alpha + price):
        raise TypeError('Scale rational coefficients to integers first')
    D = [max(0, P[u]-rho[u]+1) for u in range(b)]
    order = sorted(range(len(s)), key=lambda i: (s[i], i))
    eligible_total = [sum(v <= rho[u] for v in s) for u in range(b)]
    inside = [0]*b
    dp = {0: (0, (), ())}
    cache = {}
    S = 0
    for i in order:
        si = s[i]
        if si not in cache:
            eligible = [u for u in range(b) if q[u] > 0 and rho[u] >= si]
            options = []
            for e in range(min(E, len(eligible)-si)+1):
                weights = [(alpha[u]*min(e, D[u]) if si > xi else 0)-price[u]
                           for u in range(b)]
                chosen = tuple(sorted(eligible, key=lambda u: (-weights[u],u))[:si+e])
                options.append((e, sum(weights[u] for u in chosen), chosen))
            cache[si] = options
        S += si
        for u in range(b):
            inside[u] += int(si <= rho[u])
        forced = sum(max(0,q[u]-eligible_total[u]+inside[u]) for u in range(b))
        minimum = max(0,forced-S)
        nxt = {}
        for olde, (oldv, es, columns) in dp.items():
            for e, val, chosen in cache[si]:
                ee = olde+e
                if minimum <= ee <= E:
                    candidate = oldv+val
                    if ee not in nxt or candidate > nxt[ee][0]:
                        nxt[ee] = (candidate, es+(e,), columns+(chosen,))
        dp = nxt
        if not dp:
            return None
    if E not in dp:
        return None
    value, es, columns = dp[E]
    use = [0]*b
    for col in columns:
        for u in col:
            use[u] += 1
    return {'upper': value+sum(q[u]*price[u] for u in range(b)),
            'sorted_label_order': order, 'excess': list(es),
            'columns': [list(c) for c in columns], 'source_use': use}


def receiver_lower(profile: dict, alpha: list[int], xi: int = 0):
    """Exact finite receiver-price lower bound for SAME positive-label charge.

    Actual q-tail incoming vectors y are dominated by full incoming p.
    """
    s,q,rho,P = (profile[k] for k in ('s','q','rho','P'))
    b = len(q)
    h = [max(0,q[u]-sum(v <= xi and v <= rho[u] for v in s)) for u in range(b)]
    w = [alpha[u]*h[u] for u in range(b)]
    best = {'lower':0,'tau':0,'theta':0}
    for tau in sorted(set(q)):
        Q = sum(v for v in q if v >= tau)
        A = [min(P[u],sum(v != u and tau <= q[v] <= q[u]+rho[u]+1
                         for v in range(b))) for u in range(b)]
        free = [min(A[u],rho[u]-1) for u in range(b)]
        G = [A[u]-free[u] for u in range(b)]
        if Q > sum(A):
            return {'capacity_impossible':True,'tau':tau,'demand':Q,'capacity':sum(A)}
        for theta in sorted(set([0]+w)):
            lower = theta*(Q-sum(free))-sum(max(0,theta-w[u])*G[u] for u in range(b))
            if lower > best['lower']:
                best = {'lower':lower,'tau':tau,'theta':theta,
                        'demand':Q,'free':free,'G':G,'h':h}
    return best
