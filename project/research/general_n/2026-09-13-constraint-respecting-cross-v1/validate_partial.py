#!/usr/bin/env python3
"""Directly validate the preserved positive partial compatibility pattern."""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
p = json.loads((HERE / "BEST_PARTIAL_PATTERN.json").read_text())
r = p["record"]
a, b = r["a"], r["b"]
S = list(map(set, p["selected"]))
R = list(map(set, p["residual"]))

assert len(S) == len(R) == b
assert [len(x) for x in R] == r["rho"]
assert all(not S[u] & R[u] for u in range(b))

X = [sum(i in S[u] for u in range(b)) for i in range(a)]
assert X == r["s"]
Ri = [sum(i in R[u] for u in range(b)) for i in range(a)]
q = list(map(len, S))
N = [S[u] | R[u] for u in range(b)]

endpoint = []
nonempty = []
empty = []
pair_count = 0
for u in range(b):
    for i in sorted(S[u]):
        if Ri[i] + X[i] < q[u]:
            endpoint.append([u, i, Ri[i] + X[i], q[u]])
        D = [
            v for v in range(b)
            if v != u and S[u] - N[v] == {i} and S[v] <= N[u]
        ]
        pair_count += len(D)
        if D:
            nonempty.append([u, i, D])
        else:
            empty.append([u, i])

claimed = p["claimed"]
assert sum(q) == claimed["selected_incidence_count"] == 37
assert len(nonempty) == claimed["obligations_with_nonempty_compatible_destination_set"] == 19
assert len(empty) == claimed["empty_obligations"] == 18
assert pair_count == claimed["eligible_ordered_pairs"] == 20
assert not endpoint and claimed["minimum_endpoint_load_violations"] == 0

out = {
    "status": "PASS",
    "selected_degrees": X,
    "residual_label_degrees": Ri,
    "source_selected_degrees": q,
    "nonempty": nonempty,
    "empty": empty,
    "eligible_ordered_pairs": pair_count,
    "scope": "Direct validation of one partial pattern only; no optimality or state exclusion."
}
(HERE / "PARTIAL_VALIDATION.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
