# Forced-incidence source-score lemma

13 September 2026. **Candidate general lemma inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

The threshold incidence-capacity lemma can show that a class of sources collectively needs more compatible selected-incidence capacity. At an equality boundary one often needs a finer conclusion: a particular label is forced to receive an incidence from a low-score source. The selected-source degree bound then lowers that label's correction.

This note records the elementary pigeonhole step used to close the final state-385 equality profiles.

## 1. Setup

Let `U` be a set of active sources and `J` a set of positive-demand labels such that every selected incidence emitted by a source in `U` must land in `J`.

For `u in U`, the source emits exactly `q_u` selected incidences. For `j in J`, label `j` has selected degree exactly `x_j`. The selected source-label graph is simple, so a fixed label can receive at most one selected incidence from each source.

For a target label `i in J`, the labels in `J\{i}` can absorb at most

```text
A_(U,J\i)
 = sum_{j in J\{i}} min(x_j, |U|)                    (1)
```

incidences from `U`.

This is deliberately a safe upper bound; further compatibility restrictions can only reduce the true absorption capacity.

## 2. Forced-incidence theorem

**Theorem.** If

```text
sum_{u in U} q_u > A_(U,J\i),                         (2)
```

then the target label `i` must receive at least one selected incidence from a source in `U`.

### Proof

If `i` received no incidence from `U`, all

```text
sum_{u in U} q_u
```

selected incidences emitted by `U` would have to land in `J\{i}`. But each `j in J\{i}` can receive at most `min(x_j,|U|)` such incidences, because its total selected degree is `x_j` and there is at most one source-label edge from each source in `U`. Their total absorption capacity is therefore at most (1), contradicting (2). QED.

## 3. Source-score consequence

At every selected incidence `ui`, the canonical selected-source degree forcing gives

```text
d_i <= rho_u+q_u-1.                                   (3)
```

Suppose every source in `U` has score at most

```text
M=max_{u in U}(rho_u+q_u-1).                          (4)
```

If (2) forces target `i` to receive an incidence from `U`, then

```text
d_i<=M,                                                (5)
C_i=d_i+e_i<=M+e_i.                                   (6)
```

Thus any positive baseline correction whose coefficient multiplies `C_i` can be recomputed with the stronger upper bound (6).

This is stronger than merely knowing that enough high-score sources exist globally: the incidence demand of `U` forces a low-score source onto the particular label.

## 4. Demand-two specialization in the adjacent N34 family

In the current family,

```text
s_i in {2,3},
rho_u in {1,2,3}.
```

A `rho=2` source can select only demand-two labels. Hence take

```text
U={u:rho_u=2},
J={i:s_i=2}.                                          (7)
```

All selected incidences from `U` land in `J`, so the theorem applies immediately.

### State 385, E=7

The sole profile left after threshold-incidence refinement has

```text
q_(rho=2)=(1,1,1),
e_(s=2)=(0,7),
x_(s=2)=(2,9).
```

Let `i` be the excess-seven demand-two label. The other demand-two label can absorb at most

```text
min(2,3)=2
```

incidences from the three sources, whereas those sources emit

```text
1+1+1=3.
```

Thus `i` is forced to receive a `rho=2,q=1` incidence. Its source score is

```text
2+1-1=2,
```

so

```text
d_i<=2,
C_i<=2+7=9.                                           (8)
```

The old relaxed correction used `C_i<=14`, with coefficient `e_i-1=6`. Replacing 14 by 9 lowers the correction by

```text
6(14-9)=30.
```

The previous relaxed gap was `-1`, so the strengthened gap is at least

```text
-1+30=29>0.                                           (9)
```

### State 385, E=9

The unique remaining profile has

```text
q_(rho=2)=(2,2,2),
e_(s=2)=(3,6),
x_(s=2)=(5,8).
```

The three `rho=2` sources emit six incidences, all into the two demand-two labels. For either target label, the other label can receive at most three incidences from this three-source set, regardless of its larger total degree. Hence both targets are forced to receive a `rho=2,q=2` incidence.

Their source score is

```text
2+2-1=3.
```

Therefore their endpoint upper bounds improve from the relaxed values

```text
C<=10,13
```

to

```text
C<=6,9.
```

The demand-two correction falls from

```text
2*10 + 5*13 = 85
```

to at most

```text
2*6 + 5*9 = 57.
```

The old gap was zero, so the strengthened gap is at least

```text
28>0.                                                  (10)
```

### State 385, E=11

The unique remaining profile has

```text
q_(rho=2)=(2,2,2),
e_(s=2)=(4,4),
x_(s=2)=(6,6),
```

plus one demand-three label of excess three. Again each demand-two target is forced to receive a `rho=2,q=2` incidence, so

```text
d_i<=3,
C_i<=7
```

for both demand-two labels. Their combined correction therefore falls from

```text
2 * [3*12] = 72
```

to at most

```text
2 * [3*7] = 42.
```

The demand-three excess-three correction remains bounded by 33, so the total positive correction falls from 105 to at most 75. The old gap was zero; the strengthened gap is at least

```text
30>0.                                                  (11)
```

## 5. Generalisation

The theorem is not specific to demand two. Any source subset `U` whose selected labels are confined to a label class `J` can force incidences onto particular labels when the remaining class cannot absorb all row demand. Combining this with source-score bounds converts an incidence-capacity fact into a sharper endpoint-degree bound.

A still stronger version can replace the coarse `min(x_j,|U|)` term by the number of sources in `U` individually compatible with label `j`, yielding a genuine Hall-type neighbourhood capacity. The present form is enough for the state-385 boundary profiles and is easier to audit.

## Trust boundary

This lemma uses only the simplicity of the selected source-label graph, exact source/label selected degrees, demand compatibility, and canonical selected-source degree forcing. It makes no graph-switching assumption and does not choose quasi-edge representatives beyond the abstract legal representative system. External review remains open.
