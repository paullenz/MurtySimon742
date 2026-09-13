# State 227: exact-demand exclusion for every source-margin vector

13 September 2026. **Candidate hand reduction with finite exact arithmetic; external mathematical review OPEN.** This note strengthens `MARGIN_CLASS_EXAMPLE.md`. It proves that N34 state 227 has no selected-incidence realization with `x=s` for **any** source selected-degree vector `q`. It does **not** exclude `x>s`, so it is not yet a whole-state exclusion.

## 1. State data

For N34 state 227,

```text
a=15, b=18, t=1,
s = 2^4,3^11,
rho = 1^7,2,3^10.
```

Hence `S=sum s_i=41` and `r=sum rho_u=39`. Assume exact demand `x_i=s_i` for every label. Then

```text
Q=sum_i x_i=sum_u q_u=sum_u p_u=41.
```

All fifteen labels have positive demand.

## 2. A geometry-independent upper bound

For a selected incidence `ui`, endpoint load gives

```text
q_u+p_u <= R_i+x_i.
```

Under exact demand put `C_i=R_i+s_i`. Summing over all selected incidences gives

```text
sum_u q_u(q_u+p_u) <= sum_i s_i C_i.                 (2.1)
```

Let `D_2` be the four demand-two labels and put `R_2=sum_(i in D_2) R_i`. Since `sum_i C_i=r+S=80` and `sum_(i in D_2) C_i=8+R_2`,

```text
sum_i s_i C_i
 =2(8+R_2)+3(80-8-R_2)
 =232-R_2.
```

Therefore every exact-demand realization must satisfy

```text
A := sum_u q_u(q_u+p_u)+R_2 <= 232.                  (2.2)
```

## 3. Source restrictions independent of selected geometry

The selected-edge forcing says `s_i<=rho_u` at every selected incidence.

- All seven `rho=1` sources have `q_u=0`. Their ordinary incoming bound is `p_u<=3`, so together they absorb at most 21 incoming units.
- The unique `rho=2` source, call it `u_*`, can select only the four demand-two labels, hence `q_*<=4`. If active, exact demand gives `p_*<=1`; if inactive, the ordinary bound gives `p_*<=4`.
- An active `rho=3` source has `p_u<=2`; an inactive one has `p_u<=5`.

An active `rho=3` source also satisfies

```text
q_u<=7.                                               (3.1)
```

Indeed, on every selected label (2.1) gives `C_i>=q_u`; since `s_i<=3`, `R_i=C_i-s_i>=q_u-3`. The selected labels are distinct, so `39=r>=q_u(q_u-3)`. The value `q_u=8` would require `40<=39`.

## 4. Active incoming load forced by inactive capacity

Let `k` be the number of active sources among the unique `rho=2` source and the ten `rho=3` sources. Let `z=1` if the `rho=2` source is active and `z=0` otherwise.

Because `sum p_u=41`, maximizing incoming load on inactive sources still leaves the following minimum active incoming load.

If `z=0`, inactive capacity is

```text
7*3 + 4 + (10-k)*5 = 75-5k,
```

so active `rho=3` sources carry at least

```text
P_0(k)=max(0,5k-34).                                  (4.1)
```

The feasible active counts are `k=6,...,10`.

If `z=1`, inactive capacity is

```text
7*3 + (11-k)*5 = 76-5k,
```

so the active sources carry at least

```text
P_1(k)=max(0,5k-35).                                  (4.2)
```

The feasible active counts are `k=7,...,11`.

Any additional active incoming unit increases `sum q_u(q_u+p_u)`, so the minimum lower bound occurs at equality in (4.1) or (4.2).

## 5. Exact finite minimization

For `m` active `rho=3` sources define

```text
F_m(Q,P)=min sum_j q_j(q_j+p_j),
```

over integers `1<=q_j<=7`, `0<=p_j<=2`, `sum q_j=Q`, `sum p_j=P`. The exact recurrence is

```text
F_0(0,0)=0,
F_m(Q,P)=min_[1<=q<=7,0<=p<=2]
          {q(q+p)+F_(m-1)(Q-q,P-p)}.
```

`verify_exact_demand_all_q.py` evaluates this recurrence with integer arithmetic only.

### rho=2 inactive

Here `A>=sum q(q+p)`. The exact minima are:

| active sources k | forced active P | minimum A |
|---:|---:|---:|
| 6 | 0 | 281 |
| 7 | 1 | 246 |
| 8 | 6 | 241 |
| 9 | 11 | 236 |
| 10 | 16 | 233 |

Every value exceeds 232.

### rho=2 active

Write its parameters as `(q_*,p_*)`. It selects `q_*` distinct demand-two labels. For each one, endpoint load gives

```text
R_i=C_i-2 >= q_*+p_*-2,
```

hence

```text
R_2 >= q_* max(0,q_*+p_*-2).                          (5.1)
```

The exact quantity minimized is

```text
q_*(q_*+p_*)
+q_* max(0,q_*+p_*-2)
+F_(k-1)(41-q_*,P_1(k)-p_*),
```

with `1<=q_*<=4` and `0<=p_*<=1`. The exact minima are:

| active sources k | forced active P | minimum A |
|---:|---:|---:|
| 7 | 0 | 253 |
| 8 | 5 | 245 |
| 9 | 10 | 240 |
| 10 | 15 | 235 |
| 11 | 20 | 234 |

Again every value exceeds 232. The smallest lower bound in all cases is 233.

## 6. Conclusion

Equation (2.2) requires `A<=232`, whereas the complete active-source split proves `A>=233` for every possible exact-demand source-margin vector and every selected-incidence geometry.

Therefore N34 state 227 has **no realization with `x=s`**, for any `q`-vector. This closes level G2 of the geometry hierarchy for this state:

```text
variable q, fixed x=s: excluded.
```

It is stronger than the earlier fixed-margin result but remains short of a whole-state exclusion. The remaining escape is `x>s`. No claim about that branch is made here. Solver timeouts encountered while exploring `x>s` are preserved as non-results and are not used in this proof.
