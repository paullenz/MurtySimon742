# Refined baseline-3 order-statistic lemma

13 September 2026. **Candidate general lemma inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

This note extracts the state-382 tail refinement into a reusable statement. It is a necessary condition on scalar selected/residual margins; it is not by itself a whole-state exclusion and it inherits the trust boundary of `../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`.

## Setup

Use the canonical bridge notation and assume positive surplus `t>0`. Thus for each source `u in B` we have residual count `rho_u`, outgoing selected count `q_u`, incoming selected count `p_u`; for each label `i in A` we have positive demand `s_i`, selected degree `x_i`, residual degree `R_i`, and

```text
e_i = x_i-s_i >= 0,
C_i = R_i+x_i.
```

Assume throughout this lemma that every label has positive demand and

```text
s_i in {2,3}.
```

Put

```text
Q = sum_u q_u = sum_i x_i,
r = sum_u rho_u,
T = sum_u q_u(q_u+p_u).
```

The exact cross-edge ledger gives

```text
sum_i C_i = r+Q.                                      (1)
```

Because `s_i>0`, the definition of demand is exact:

```text
s_i=d_i-R_i,
C_i=d_i+e_i.                                          (2)
```

## 1. Exact source-score order statistic

For a source put

```text
v_u = rho_u+q_u-1.
```

At every selected incidence `ui`, the canonical bridge gives

```text
s_i <= rho_u,
d_i <= rho_u+q_u-1 = v_u.                            (3)
```

For `d in {2,3}`, list the values `v_u` over sources with `rho_u>=d` in nonincreasing order:

```text
v^(d)_1 >= v^(d)_2 >= ... .                           (4)
```

A label `i` of demand `d=s_i` has

```text
x_i=d+e_i
```

distinct selected sources, all with `rho_u>=d`. Equation (3) holds at every one of them. Therefore, provided such a selected label is possible,

```text
d_i <= v^(d)_(d+e_i),
C_i <= e_i + v^(d)_(d+e_i).                          (5)
```

This is stronger than replacing all eligible sources by the worst residual class. In particular, a `rho=2` source contributes the exact score `q_u+1`, not the relaxed `q_u+2` used in the first state-382 tail replay.

## 2. Baseline-3 decomposition

From the endpoint-load lemma, every selected incidence `ui` satisfies

```text
q_u+p_u <= C_i.
```

Summing over all selected incidences gives

```text
T <= sum_i x_i C_i.                                   (6)
```

Use `x_i=3+(x_i-3)` and (1):

```text
sum_i x_i C_i
 = 3(r+Q) + sum_i (x_i-3)C_i.                         (7)
```

For demand three, `x_i-3=e_i`, so the correction is nonnegative and (5) gives

```text
(x_i-3)C_i
 <= e_i [ e_i + v^(3)_(3+e_i) ]                      (8)
```

when `e_i>0`; it is zero when `e_i=0`.

For demand two,

```text
x_i-3=e_i-1.
```

If `e_i>=2`, (5) gives

```text
(x_i-3)C_i
 <= (e_i-1)[ e_i + v^(2)_(2+e_i) ].                  (9)
```

If `e_i=1`, the correction is zero. If `e_i=0`, then `x_i=2` and trivially `C_i>=x_i=2`, hence

```text
(x_i-3)C_i = -C_i <= -2.                              (10)
```

Let

```text
z_0 = #{i:s_i=2,e_i=0}.
```

Combining (6)-(10) yields the refined necessary inequality

```text
T + 2 z_0
<= 3(r+Q)
 + sum_(i:s_i=3,e_i>0) e_i [e_i+v^(3)_(3+e_i)]
 + sum_(i:s_i=2,e_i>=2) (e_i-1)[e_i+v^(2)_(2+e_i)].  (11)
```

Any term whose required order statistic does not exist corresponds to an impossible excess profile, because `x_i` distinct eligible selected sources are unavailable.

## 3. q-cap and h2 incoming cap

Two additional scalar consequences make (11) cheap to optimise.

First, selected labels at a fixed source are distinct. Since every selected label at source `u` must satisfy `s_i<=rho_u`, and also `q_u+rho_u<=a`,

```text
q_u <= min(a-rho_u, #{i:s_i<=rho_u}).                 (12)
```

Second, put

```text
h_2 = #{i:e_i>=2}.
```

If `q_u>h_2`, at least one selected label at source `u` has `e_i<=1`. The selected-excess inequality

```text
p_u-rho_u+1 <= e_i
```

then gives

```text
q_u>h_2  =>  p_u<=rho_u.                              (13)
```

Otherwise the universal source cap remains

```text
p_u<=rho_u+b-a-1,                                     (14)
```

and always

```text
q_u+p_u<=b-1.                                         (15)
```

For fixed `q` and `h_2`, the minimum possible `sum q_u p_u` under (13)-(15) is obtained by assigning the required incoming mass first to sources with smallest `q_u`. Thus (11)-(15) define an exact finite integer relaxation depending only on `(a,b,rho,s,E)` and the order statistics of `q` within residual classes.

## 4. Relation to state 382

For state 382,

```text
a=15, b=18,
s=2^2,3^13,
rho=1^6,2,3^11.
```

The original refined tail replay used the safe relaxation

```text
v^(2) <= q+2
```

also for the single `rho=2` source. Equation (5) retains its exact value `q+1`, so the present relaxation is at least as strong while requiring no extra graph data.

The separate state-382 proof already establishes the whole-state exclusion. This note changes no frontier count by itself.

## 5. Computational use

The companion files

- `prepare_refined_h2_family_scan.py`,
- `scan_refined_h2_family.cpp`,
- `.github/workflows/scan-refined-h2-adjacent-family.yml`

apply (11)-(15) to the adjacent N34 low-demand family and include the five already-closed states as regression tests. A positive minimum gap at a fixed excess `E` proves that the relaxation has no feasible margin profile at that layer. A nonpositive gap is only a survivor of the relaxation and is not evidence for a graph.

## 6. Trust boundary

- The derivation above is hand mathematics inside the candidate canonical bridge. Independent expert checking remains open.
- The order-statistic step uses only distinct selected sources, `s_i<=rho_u`, and source selected-degree forcing; it does not assume graph-level 2x2 switching.
- The scan is exact integer arithmetic for this relaxation but does not constitute external reproduction.
- No unrestricted Murty-Simon theorem is claimed here.
