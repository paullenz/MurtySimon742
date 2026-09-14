# Row 471 common-pressure split: new closures `e_L=42,43`

15 September 2026. Successor to the independently verified [`e_L=41` high-block closure](../2026-09-15-row471-e41-v1/README.md) and the earlier [`e_L=39,40` rigidity package](../2026-09-14-conditioned-source-pricing-v1/ROW471_RIGIDITY.md). **Exact integer necessary-condition argument; external mathematical review OPEN.**

This package gives a uniform source-group charge bound for `e_L=41,42,43`. Its `41` contradiction is an independent regression only; the **new mathematical closures are `e_L=42` and `43`**. Thus the conditioned row-471 analysis now leaves only

```text
e_L = 47
```

open. Row 471 is **not** excluded as a whole. The original synthetic sample remains `708/713`; the promoted canonical frontier remains `4,626 exclusions / 952 survivors / 3,632 whole-state closures`.

## Setup and receiver lower bound

For original synthetic row 471,

```text
a=21, b=25, t=1, D0=0, Esel=47,
label demands = 1^5, 2^4, 3^12,
sum q_u = 96.
```

Use the conditioned low block `{i:s_i<=2}`, of base demand `13`. The sources split as

```text
rho=1: 12 sources, total row sum 33;
rho=2:  4 sources, row sums 7,4,4,3, total 18;
rho=3:  9 sources, total row sum 45.
```

All `rho<=2` selections lie in the low block, so if its excess is `e_L`, the nine `rho=3` sources use exactly

```text
L = e_L-38
```

low-block selections, while the twelve demand-three labels have total excess

```text
H = 47-e_L.
```

For `e_L=41,42,43`, `(L,H)=(3,6),(4,5),(5,4)`.

All labels have positive demand. With common source pressure `d_u=(p_u-rho_u+1)_+`, unit charge is `C=sum q_ud_u`. The inherited exact receiver certificate (`tau=1`, `theta=5`, uniform weight, `charge_eta=0`) gives on all three branches

```text
free = 22,
penalty = 148,
C >= 5*(96-22)-148 = 222.                         (R)
```

## `rho=1` contribution

Every `rho=1` source has conditioned pressure ceiling `4` on these branches. Their total row sum is `33`, hence

```text
C_{rho=1} <= 132.                                  (A)
```

## Four-source exact DP for `rho=2`

The four `rho=2` sources have row sums `7,4,4,3` and pressure ceiling `4`. Let `ell_i` be their selected-incidence degree at one of the four demand-two labels, and `m_i` the largest selected-source pressure there. If `h_i` high-source selections also hit that label, its excess is `ell_i+h_i-2`; pressure feasibility therefore forces

```text
h_i >= (2+m_i-ell_i)_+.
```

Because only `L` high-source low-block selections exist,

```text
sum_i (2+m_i-ell_i)_+ <= L.                        (B)
```

An exact symmetry DP processes only these four sources. A row-`q` source can use at most five demand-one labels, so it selects between `max(0,q-5)` and `min(q,4)` distinct demand-two labels. Trying every pressure `0..4` and every such subset produces exactly

```text
15, 210, 1,225, 4,325
```

canonical states after source rows `7,4,4,3`. Filtering by (B) gives

| `e_L` | `L` | max `C_{rho=2}` |
|---:|---:|---:|
| 41 | 3 | 36 |
| 42 | 4 | 44 |
| 43 | 5 | 54 |

Demand-one congestion is intentionally relaxed, so these are safe upper bounds.

## Nine-source nested-excess DP for `rho=3`

Let high source `u` use `k_u` low-block selections and `h_u=q_u-k_u` demand-three selections. Then `sum k_u=L`. Sort the twelve high-label excesses as `e_(1)>=...>=e_(12)`. If source `u` selects `h_u` distinct high labels at pressure `d_u`, then `e_(h_u)>=d_u`, hence necessarily

```text
H >= sum_j max { d_u : h_u >= j }.                 (C)
```

This is the most favourable possible nesting of high-label pressure requirements. An exact DP enumerates integer `k_u,d_u`, the conditioned pressure ceilings, total low slots `L`, and the layer maxima in (C). It gives

| `e_L` | `L` | `H` | max `C_{rho=3}` |
|---:|---:|---:|---:|
| 41 | 3 | 6 | 45 |
| 42 | 4 | 5 | 38 |
| 43 | 5 | 4 | 29 |

The final state sets contain only `85,75,63` states respectively.

## Contradictions

Adding the independently relaxed group maxima from (A), (B), and (C):

| `e_L` | `rho=1` | `rho=2` | `rho=3` | charge upper | receiver lower |
|---:|---:|---:|---:|---:|---:|
| 41 | 132 | 36 | 45 | **213** | **222** |
| 42 | 132 | 44 | 38 | **214** | **222** |
| 43 | 132 | 54 | 29 | **215** | **222** |

Thus `41` is independently reconfirmed, while the new closures are

```text
214 < 222  (e_L=42),
215 < 222  (e_L=43).
```

Together with the earlier exact `39,40,41` work, **only `e_L=47` remains for row 471 at this conditioned threshold**.

## Exact replay and scope

[`verify_row471_e42_e43.py`](verify_row471_e42_e43.py) uses Python standard library only, reads the preserved original profile corpus, reconstructs the conditioned caps, rechecks (R), and executes both exact DPs. The compact frozen result is [`RESULT.json`](RESULT.json), canonical parsed-JSON SHA-256

```text
b2f2b8f1f714eb11225c07d9a9595154a7c53523b5d8da74be8a2028c170cc15
```

Run [`run_replay.py`](run_replay.py) from repository root. Remote CI is a separate verification event and must not be called successful until inspected.

This is a necessary-condition contradiction inside the stated conditioned selected-incidence/common-pressure relaxation. It does not promote a whole canonical state, does not close row 471 while `e_L=47` remains, and does not prove the unrestricted conjecture.

## Next target

`e_L=47` is structurally different: all selected excess lies in the low block and the inherited best charge system uses `charge_eta=2`, so the `C>=222` lower bound above is unavailable. The next attack should use selected-label/destination compatibility and the bridge's **one shared residual neighbourhood per source**, rather than extrapolating the charge split beyond its valid domain.
