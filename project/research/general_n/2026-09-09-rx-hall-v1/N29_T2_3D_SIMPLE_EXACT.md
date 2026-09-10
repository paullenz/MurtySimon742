# n=29, t=2: exact 11-term 3-D potential

## Status

**Exact finite RX-Hall certificate, conditional on the 3-D potential-certificate lemma and the graph-to-profile bridge.**

This is a simplification of the finite `t=2` RX-Hall frontier certificate. It is not an unrestricted Murty-Simon proof and does not supersede the existing fixed-order `n=29` reviewer proof chain unless that chain is deliberately rewritten to use it.

## Scope

Parameters: `n=29`, `Delta=16`, `m=210`, `a=12`, `b=16`, `t=2`.

The regenerated frontier contains 902 RX-Hall profiles. The exact checker verifies 334,159 inequalities in 20,518 variables.

## Primitive global potential

Using 3-D monotone coordinates `(s,d,v)` and the notation

- `B(D,V) = 1[d >= D and v >= V]`,
- `J_c = 1[d+v >= b-c]`, so `J_2` is `K=14` and `J_0` is `K=16`,
- `SH3 = 1[s >= 3]`,

the fixed primitive potential is

```
3 B(3,6) + 3 B(3,7) + 3 B(3,8) + 3 B(3,9)
+ 4 B(3,10) + 4 B(3,11) + 4 B(3,12) + 4 B(3,13)
+ 8 J_2 + 7 J_0 + 29 SH3.
```

There are 11 nonzero generators and the primitive weight sum is 72.

This support is the cleanest full-frontier survivor discovered after restoring the first Hall coordinate. It uses only the joint `D3` layer, two diagonal slack thresholds, and one first-coordinate threshold. No `D2` or `D4` rectangle family remains.

## Exact run

Workflow run: **34510208273**

Head commit: `5334076a3f3f16e62fb35d374aa7bc8de1d94df9`

Artifact id: **10165483726**

Artifact SHA-256:

`ef54da1daf46d23e4be39c5e982a4e4b9b042538a6833099e560b107733ff8c1`

Exactification details:

- scale: `1,000,000`;
- proposal margin: `1.0001`;
- proof target: original normalized margin `<= -1`;
- 902 strict profile rows;
- 334,159 total inequalities;
- 20,518 variables;
- zero row violations;
- zero bound violations;
- zero maximum homogeneous-row residual;
- worst strict-margin numerator: `-1,000,000`;
- required strict-margin numerator: `-1,000,000`;
- 1,088 envelope-rounding repairs, total correction 2,407, maximum correction 12.

The rounding repairs alter only the unique free envelope variable in homogeneous envelope rows; proof acceptance is exact integer arithmetic under the corrected scaled-RHS rule.

## Independent replay

The same workflow then ran

`n29_common_potential_verify_3d.py`

under `/usr/bin/python3` with standard-library imports only. The replay does not import NumPy, SciPy, the LP builder, or the exactifier. It reconstructs all 20,518 variables and every envelope/profile inequality from the regenerated frontier.

Independent replay result:

- status: `PASS`;
- name-order hash: matched;
- row violations: 0;
- bound violations: 0;
- homogeneous maximum LHS: 0;
- strict profile rows: 902;
- worst strict margin: `-1,000,000 / 1,000,000 = -1`.

## Interpretation

This result materially simplifies the finite `t=2` Hall-potential picture. The earlier proof-grade 16-generator potential demonstrated exact feasibility in two projected coordinates. Restoring the first Hall coordinate allows the certificate to be written with only 11 generators and removes the entire `D2` and `D4` families.

The current certificate is tight at the normalized margin boundary. That is acceptable mathematically, but further coefficient optimisation/support pruning may produce a cleaner interior certificate. A separate integer-weight minimisation is therefore retained as a discovery task; it must not be confused with the exact result above.

## Trust boundary

Exact replay establishes the finite RX-Hall contradiction conditional on the symbolic 3-D transport/potential lemma and the graph-to-RX-Hall/profile bridge. Independent human audit of those universal graph-theoretic steps remains open.
