# Threshold incidence-capacity lemma

13 September 2026. **Candidate general lemma inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

The demand-compatible excess-order cap is pointwise: it asks whether one source can find enough compatible labels above its required excess threshold. This note retains the next piece of structure: **different sources compete for the finite selected-incidence capacity of those labels**.

The resulting inequalities are Hall-type necessary conditions. They do not fix selected representative identities and they do not assert sufficiency for a selected incidence graph.

## 1. Setup

For every positive-demand label `i`, write

```text
e_i=x_i-s_i>=0.
```

For an active source `u`, put

```text
L_u=max(0,p_u-rho_u+1).                               (1)
```

At every selected positive-demand incidence `ui`, the established bridge lemmas give

```text
s_i<=rho_u,                                            (2)
e_i>=L_u.                                              (3)
```

The selected degree of label `i` is exactly `x_i`, so label `i` can support exactly `x_i` selected source-label incidences in total.

## 2. Threshold-capacity theorem

Fix integers `ell>=0` and `R>=1`. Define the source set

```text
U_(ell,R)
 ={u : q_u>0, rho_u<=R, L_u>=ell}.                    (4)
```

For `ell=0`, this is simply every active source with `rho_u<=R`.

Define the compatible label capacity

```text
X_(ell,R)
 =sum_{i: 0<s_i<=R, e_i>=ell} x_i.                   (5)
```

**Theorem.** Every legal selected/residual representative system satisfies

```text
sum_{u in U_(ell,R)} q_u <= X_(ell,R).                (6)
```

### Proof

Every selected incidence from a source `u in U_(ell,R)` ends at a positive-demand label `i`. By (2),

```text
s_i<=rho_u<=R,
```

and by (3),

```text
e_i>=L_u>=ell.
```

Thus every such incidence lands in the label class counted by (5). The sources in `U_(ell,R)` contribute exactly

```text
sum_{u in U_(ell,R)} q_u
```

distinct source-label incidences. A label `i` can receive only its selected degree `x_i` incidences, so the whole compatible class supplies at most `X_(ell,R)` incidences. This proves (6). QED.

No global representative geometry has been chosen in deriving the inequality.

## 3. Global and demand-class forms

If `R` is at least every source residual degree, (6) reduces to the global threshold-capacity inequality

```text
sum_{u:q_u>0, L_u>=ell} q_u
 <= sum_{i:e_i>=ell} x_i.                             (7)
```

For the current adjacent N34 family, where

```text
s_i in {2,3},
rho_u in {1,2,3},
```

the two useful cutoffs are

```text
R=2:
  sum_{u:rho_u=2, L_u>=ell} q_u
  <= sum_{i:s_i=2,e_i>=ell} x_i,                      (8)

R=3:
  sum_{u:rho_u in {2,3}, L_u>=ell} q_u
  <= sum_{i:e_i>=ell} x_i.                            (9)
```

The `ell=0` member of (8) is especially simple:

```text
sum_{u:rho_u=2} q_u
 <= sum_{i:s_i=2} x_i.                                (10)
```

It says that all selected incidences emitted by `rho=2` sources must fit into the total selected-degree capacity of demand-two labels.

## 4. Relation to the order-statistic source cap

The demand-compatible excess-order theorem says that one source with outgoing degree `q_u` must have at least `q_u` compatible labels at the required excess threshold. Equation (6) is different: it counts the **multiplicity capacity `x_i` of those labels across many sources**.

Neither implies the other in general.

A useful hierarchy is therefore

```text
pointwise compatible label count
    -> pointwise source incoming cap
    -> threshold incidence-capacity competition
    -> exact selected-incidence matching if still needed.
```

The first two can hold while (6) fails because several sources are all trying to use the same small high-excess capacity.

## 5. Incoming-ledger formulation

For a fixed excess profile and fixed outgoing margins `q`, the quantities `X_(ell,R)` are constants. An integer incoming allocation `p` is admissible only if

```text
sum_u p_u = Q,                                        (11)
```

all previously established pointwise source caps hold, and all inequalities (6) hold.

Since increasing `p_u` increases `L_u` only through discrete thresholds, this can be checked by an exact finite dynamic programme. Each source option `p_u` contributes

- `p_u` to the incoming total;
- `q_u p_u` to the source cost;
- `q_u` units of threshold workload at every `ell<=L_u`, in each applicable residual-degree cutoff.

Pruning whenever a threshold capacity (5) is exceeded gives an exact minimum of `sum q_u p_u` inside this relaxation.

This is proof-producing finite arithmetic: no numerical solver or floating-point infeasibility is required.

## 6. Adjacent-family consequences found in the frozen scan

The first applications explain the remaining low-excess obstructions left by the demand-compatible order-statistic scan.

### State 230

The only non-strict layers after the order-statistic screen were

```text
E=0,3,6.
```

Their extremal profiles have all four demand-two labels at zero excess while the `rho=2` source outgoing totals exceed the total demand-two selected capacity. The `ell=0, R=2` inequality (10) detects the obstruction directly.

A whole-layer replay is required before promoting this observation to a whole-state closure; the extremal witness alone is not the certificate.

### State 385

The order-statistic screen left

```text
E=6,7,8,9,11.
```

For the extremal profiles at `E=6,7,8`, the incoming allocation minimizing `sum q_u p_u` overloads the high-excess selected-incidence capacity. Enforcing (8)-(9) raises the exact source-cost minima for those witnesses from

```text
74 -> 98,
82 -> 106,
88 -> 100,
```

respectively, making those witness gaps strictly positive.

The equality witnesses at `E=9` and `E=11` survive this threshold-capacity refinement and therefore require the next incidence-rigidity step.

These witness calculations are diagnostic until the corresponding whole-layer exact replay is preserved.

## 7. Generalisation

Equation (6) applies to every residual-degree cutoff `R`, not only `R=2,3`, and to every excess threshold. More generally, any source class whose selected incidences are known to lie in a specified label class yields the same counting principle: total required selected incidences cannot exceed total selected degree in that class.

The mechanism is therefore a capacity version of Hall's condition naturally exposed by the canonical bridge.

## Trust boundary

This lemma uses only selected-edge forcing, selected-excess and the exact selected degrees `x_i` inside the canonical selected/residual bridge. It makes no switching assumption and does not fix quasi-edge representatives. External checking of the bridge and this derivation remains open.
