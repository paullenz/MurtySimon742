# N34 states 13518 and 13519 — whole-state pair-capacity closure

13 September 2026. **Candidate whole-state closures inside the canonical selected/residual bridge. External mathematical review and independent third-party computational reproduction remain OPEN.**

These two N34 frozen scalar states are excluded by a short combination of:

1. source selected-degree availability;
2. the all-positive-demand [`TOTAL_EXCESS_SOURCE_CAP.md`](TOTAL_EXCESS_SOURCE_CAP.md); and
3. the orientation-independent potential-pair graph extracted in [`ORIENTATION_FLOW_HALL.md`](ORIENTATION_FLOW_HALL.md).

The final replay does **not** need selected-incidence max flow, orientation prefix cuts, pair Hall flow, target Hall flow, or the weighted min-cost theorem. Those stronger tools were useful in discovering the closure, but the preserved proof certificate is deliberately simpler.

## 1. The two scalar states

Both states have

```text
a=15,
b=18,
t=1,
s=(5,6^14),
S=sum_i s_i=89.
```

State 13518 has

```text
rho=(1^4,4,5,6^11,8),
R=sum rho=87.
```

State 13519 has

```text
rho=(1^4,4,5,6^10,7^2),
R=sum rho=87.
```

Every demand is positive.

Write

```text
x_i=s_i+e_i,
E=sum_i e_i,
Q=sum_i x_i=sum_u q_u=sum_u p_u=S+E.
```

## 2. A deliberately enlarged q-universe

On every selected source-label incidence the canonical bridge gives

```text
s_i<=rho_u.
```

A source uses distinct selected labels, and always

```text
q_u+rho_u<=a.
```

Therefore every legal source degree satisfies

```text
0<=q_u<=qmax(rho_u)
       :=min(a-rho_u, #{i:s_i<=rho_u}).               (1)
```

For the present demand profile this already forces

```text
rho=1 or 4  => q=0,
rho=5       => q<=1,
rho>=6      => q<=a-rho.
```

For either state

```text
sum_u qmax(rho_u)=107.
```

Since `Q=89+E`, every legal branch therefore has

```text
0<=E<=18.                                             (2)
```

The independent verifier enumerates **every** q-multiset satisfying only (1), `sum q=89+E`, and equality-rho permutation symmetry. It deliberately does not impose the stronger global selected-incidence Hall conditions or the nested demand-prefix restrictions. Hence its search space is a superset of the legal selected-incidence q-profiles.

## 3. Incoming caps before orientation geometry

Here

```text
b-a-1=2.
```

The canonical incoming and simple missing-degree inequalities give

```text
p_u<=rho_u+2,                                         (3)
p_u<=17-q_u.                                          (4)
```

Because every `s_i>0`, the total-excess source cap gives, for every `q_u>0`,

```text
p_u<=rho_u+floor(E/q_u)-1.                            (5)
```

Let `P_u^(0)` be the minimum of the applicable right sides of (3)-(5).

The independent replay records how many q-profiles already satisfy

```text
P_u^(0)>=0 for every u,
sum_u P_u^(0)>=Q.                                     (6)
```

Many do: for example at `E=0`, 109 profiles in state 13518 and 214 in state 13519 pass (6). Thus the final exclusion is genuinely supplied by the new orientation geometry rather than by the older aggregate capacity bound alone.

## 4. Potential-pair graph

Put

```text
c_u=q_u+rho_u.
```

For an actual selected orientation `u->w`, [`ORIENTATION_FLOW_HALL.md`](ORIENTATION_FLOW_HALL.md) gives

```text
q_u<=c_w+1,
q_w<=c_u.                                             (7)
```

Define the directed compatibility relation

```text
D(u,w)
 iff u!=w,
     q_u<=c_w+1,
     q_w<=c_u.                                        (8)
```

and define the undirected potential-pair graph `K_D` by

```text
uw in E(K_D)
 iff D(u,w) or D(w,u).                                (9)
```

Every actual missing B-edge receives one of the two selected orientations, so its direction satisfies (8). Consequently

```text
J=overline{H[B]} subseteq K_D.                        (10)
```

At vertex `u`,

```text
d_J(u)=q_u+p_u.
```

Therefore

```text
p_u<=d_KD(u)-q_u.                                    (11)
```

This is an orientation-independent degree cap: no choice of orientation can create a missing neighbour outside `K_D`.

Define

```text
P_u=min(P_u^(0), d_KD(u)-q_u).                        (12)
```

Every legal branch must have

```text
P_u>=0 for every u,
Q=sum_u p_u<=sum_u P_u.                               (13)
```

Thus a q-profile is excluded whenever any `P_u<0` or

```text
sum_u P_u-Q<0.                                       (14)
```

## 5. Independent exhaustive replay

[`verify_pair_capacity_states_13518_13519.py`](verify_pair_capacity_states_13518_13519.py) independently enumerates the enlarged q-universe described above. It does not call the C++ scanner and does not use its recursion or pruning logic.

The result is strict in every excess layer.

### State 13518

| E | q-profiles | profiles passing pre-pair capacity (6) | best `sum P-Q` after pair cap |
|---:|---:|---:|---:|
| 0 | 2,147 | 109 | -14 |
| 1 | 1,697 | 75 | -16 |
| 2 | 1,327 | 8 | -17 |
| 3 | 1,025 | 4 | -19 |
| 4 | 782 | 1 | -21 |
| 5 | 589 | 0 | -23 |
| 6 | 437 | 0 | -25 |
| 7 | 319 | 0 | -28 |
| 8 | 229 | 4 | -30 |
| 9 | 161 | 161 | -33 |
| 10 | 111 | 111 | -35 |
| 11 | 75 | 48 | -38 |
| 12 | 49 | 24 | -40 |
| 13 | 31 | 0 | -44 |
| 14 | 19 | 0 | -46 |
| 15 | 11 | 0 | -50 |
| 16 | 6 | 0 | -52 |
| 17 | 3 | 0 | -56 |
| 18 | 1 | 1 | -58 |

Total q-profiles checked: **9,019**.

### State 13519

| E | q-profiles | profiles passing pre-pair capacity (6) | best `sum P-Q` after pair cap |
|---:|---:|---:|---:|
| 0 | 4,939 | 214 | -14 |
| 1 | 3,813 | 142 | -16 |
| 2 | 2,908 | 10 | -17 |
| 3 | 2,188 | 4 | -19 |
| 4 | 1,624 | 1 | -21 |
| 5 | 1,187 | 0 | -24 |
| 6 | 854 | 0 | -26 |
| 7 | 603 | 0 | -29 |
| 8 | 418 | 11 | -31 |
| 9 | 283 | 283 | -34 |
| 10 | 187 | 187 | -35 |
| 11 | 120 | 63 | -38 |
| 12 | 75 | 26 | -40 |
| 13 | 45 | 0 | -44 |
| 14 | 26 | 0 | -46 |
| 15 | 14 | 0 | -50 |
| 16 | 7 | 0 | -52 |
| 17 | 3 | 0 | -56 |
| 18 | 1 | 1 | -60 |

Total q-profiles checked: **19,295**.

In both states the closest layer is `E=0`, and even there every enlarged q-profile is at least **14 incoming incidences short** after (11). There is no equality or near-zero exceptional case to resolve.

## 6. Independent implementations

Two separate implementations agree.

### Discovery / exact coupled C++ scan

[`scan_excess_budget_orientation.cpp`](scan_excess_budget_orientation.cpp) was run in GitHub Actions run `34788648942`. It scanned all `E=0,...,18` layers and reported:

```text
state 13518: 9,019 profiles, every layer excluded
state 13519: 19,295 profiles, every layer excluded
```

Every profile failed already at the pointwise/total incoming-cap stage; no Hall or min-cost conclusion was needed for the final closure.

### Independent enlarged-universe Python replay

[`verify_pair_capacity_states_13518_13519.py`](verify_pair_capacity_states_13518_13519.py) was run in GitHub Actions run `34788751909`, which completed successfully. It omitted the C++ scanner's incidence-flow and prefix machinery and independently reproduced all profile counts and the strict deficits in the tables above.

The independent replay therefore verifies a simpler statement than the discovery scanner: **even a superset of legal q-profiles is impossible under (3)-(5) and (11).**

## 7. Whole-state conclusion

For either state, every legal branch must have `0<=E<=18` by (1)-(2). For every such `E`, every q-profile satisfying the universal source bounds is excluded by (13)-(14). Therefore no scalar branch represented by state 13518 or state 13519 can occur.

Hence these are quantified whole-state exclusions in the frozen N34 generalisation catalogue.

They change the catalogue accounting from

```text
1,010 exclusions / 4,568 survivors
```

to

```text
1,012 exclusions / 4,566 survivors.
```

These are scalar-state exclusions in the generalisation experiment. They are not additional obligations in the already complete fixed-order N34 candidate proof, and they do not prove the unrestricted Murty–Simon conjecture.

## 8. Structural lesson

The useful new mechanism is not the full max-flow machinery but the simpler potential-pair degree projection:

```text
selected orientation compatibility
        => actual missing graph J is a subgraph of K_D
        => p_u+q_u<=d_KD(u)
        => p_u<=d_KD(u)-q_u.
```

When combined with total-excess source caps, this can destroy an entire scalar state with a large margin before any Hall cut is needed. The natural next scan is therefore to apply this **pair-capacity screen** across all remaining frozen survivors before paying for exact orientation flow.

## Trust boundary

The finite enumeration is exact integer arithmetic and has two independent implementations. The mathematical application still depends on the canonical graph-to-constraint bridge, especially selected-edge forcing, the selected-excess incidence bound underlying the total-excess cap, and the directed orientation compatibility lemma. Those remain open to external specialist review and novelty assessment. Same-assistant derivation plus green CI is not external acceptance.
