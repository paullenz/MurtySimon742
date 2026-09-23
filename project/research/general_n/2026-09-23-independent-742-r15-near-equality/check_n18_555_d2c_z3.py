"""Exact D2C realizability check for the n=18 d=x=h=(5,5,5) tuple.

The fixed labelled geometry follows from equality in the strengthened deficit
model plus exact-source injection: three degree-five labels have a common
five-set C as their neighbourhood; five common witnesses T meet C in a
perfect matching; four witnesses have degree ten and one degree nine; every
other vertex has degree ten.  Remaining adjacencies are solved exactly.
"""
import json
from z3 import Bool, If, Implies, Or, And, Not, Solver, Sum, sat

N = 18
L = range(0, 3)
T = range(3, 8)
C = range(8, 13)
U = range(13, 18)

E = {(i, j): Bool(f"e_{i}_{j}") for i in range(N) for j in range(i + 1, N)}


def edge(i, j):
    if i == j:
        return False
    return E[min(i, j), max(i, j)]


def unique_common(x, y, u):
    terms = [edge(x, u), edge(y, u)]
    for w in range(N):
        if w not in (x, y, u):
            terms.append(Not(And(edge(x, w), edge(y, w))))
    return And(*terms)


s = Solver()

# Exact degrees forced by total deficit 16.
degrees = [5, 5, 5, 10, 10, 10, 10, 9] + [10] * 10
for v in range(N):
    s.add(Sum([If(edge(v, w), 1, 0) for w in range(N) if w != v]) == degrees[v])

# The three labels have exactly the common C-neighbourhood.
for i in L:
    for c in C:
        s.add(edge(i, c))
    for v in list(L) + list(T) + list(U):
        if v != i:
            s.add(Not(edge(i, v)))

# Exact-source injection and common-source forcing give a T-C perfect matching.
for k, t in enumerate(T):
    for j, c in enumerate(C):
        s.add(edge(t, c) if j == k else Not(edge(t, c)))

# Diameter at most two.
for i in range(N):
    for j in range(i + 1, N):
        s.add(Or(edge(i, j), *[And(edge(i, w), edge(j, w))
                               for w in range(N) if w not in (i, j)]))

# Exact edge-criticality criterion.  Deleting ij can only destroy a length <=2
# path for ij itself, or for x-j through i, or for i-y through j.
for i in range(N):
    for j in range(i + 1, N):
        endpoint = And(*[Not(And(edge(i, w), edge(j, w)))
                         for w in range(N) if w not in (i, j)])
        certs = [endpoint]
        for x in range(N):
            if x not in (i, j):
                certs.append(And(Not(edge(x, j)), unique_common(x, j, i)))
                certs.append(And(Not(edge(i, x)), unique_common(i, x, j)))
        s.add(Implies(edge(i, j), Or(*certs)))

status = s.check()
out = {"status": str(status), "n": N, "degrees": degrees,
       "fixed_partition": {"L": list(L), "T": list(T), "C": list(C), "U": list(U)}}
if status == sat:
    m = s.model()
    edges = [[i, j] for (i, j), var in E.items() if bool(m.eval(var))]
    out["edges"] = edges
    out["edge_count"] = len(edges)
print(json.dumps(out, indent=2))
