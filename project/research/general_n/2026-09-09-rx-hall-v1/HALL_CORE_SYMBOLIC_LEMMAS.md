# Symbolic RX-Hall core lemmas

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: universal lemma extraction / candidate proof component. This file does not claim the unrestricted Murty-Simon conjecture. The finite n=29 t=3 Hall-core computation is evidence for usefulness, not a proof of any stronger all-order conclusion. Independent mathematical review remains OPEN.**

## 1. Purpose

The exact n=29 RX-Hall certificates have now been reduced much further than the original endpoint LP. On the hard positive-demand t=3 frontier, all 94 rows are rejected exactly by a Hall core which removes

- source/supplement transport variables `P`;
- residual-label variables `R` and the residual budget;
- selected-incidence variables `Z`;
- RX2;
- grouped source-label cap inequalities;
- cumulative-tail variables;
- unordered-pair aggregate capacity.

The surviving conceptual ingredients can be stated directly on an actual selected quasi-edge configuration. This note records those graph-level inequalities so that the next attack can target them symbolically rather than treating the LP as the mathematical object.

## 2. Setup

Use the existing complement / quasi-edge framework and notation. Let

- `A` be the label side;
- `B` be the source/supplement side;
- `s_i>0` be the demand of label `i in A`;
- `x_i` be its actual selected degree;
- `rho_u` be the residual degree of source `u in B`;
- `q_u` be its selected outdegree;
- `p_u` be its supplement indegree;
- `dmax` be the established upper bound on the residual column degree `R_i`.

Put

```text
y_i := x_i-s_i,
h_u := max(0,q_u+p_u-dmax).
```

In the positive-demand zero-slack sector the already established bridge gives

```text
s_i <= rho_u                                      (RX1)
```

for every selected source-label incidence `u -> i`, and RX3 gives

```text
R_i+x_i >= q_u+p_u.
```

Since `R_i <= dmax-s_i`, RX3 immediately implies

```text
y_i=x_i-s_i >= q_u+p_u-dmax,
```

hence

```text
y_i >= h_u.                                       (HC1)
```

Therefore every selected incidence from source `u` must land in the compatibility rectangle

```text
N(u) = {(s,y): s<=rho_u and y>=h_u}.              (HC2)
```

No use of RX2 is made in HC1-HC2.

## 3. Pointwise source-degree cap

Because the selected graph is simple, a source can use any actual label at most once. RX1 therefore gives the direct bound

```text
q_u <= #{i in A : s_i <= rho_u}.                  (HC3)
```

This is a graph-level counting inequality; no grouped-density model is needed.

## 4. Source/supplement threshold transport

Every selected missing B-pair has one source and one supplement. The established supplement compatibility says that for a selected source/supplement arc `u -> w`,

```text
rho_w+q_w >= q_u-1.                               (T0)
```

Fix an integer threshold `k>=1`. Every one of the `q_u` outgoing arcs from a source with `q_u>=k+1` must therefore terminate at a supplement `w` satisfying `rho_w+q_w>=k`.

Counting these arcs gives the nested transport inequality

```text
sum_{u: q_u>=k+1} q_u
    <=
sum_{w: rho_w+q_w>=k} p_w.                      (HC4_k)
```

This is the direct integer form of the nested transport cuts used by the Hall-core model. It uses no transport variables and deliberately allows every eligible target on the right; consequently it is a necessary condition and is safe as a relaxation.

The global source/supplement balance is simply

```text
sum_u q_u = sum_u p_u.                            (HC5)
```

## 5. Rectangle Hall inequality

For integers `R,H`, define the label rectangle

```text
D(R,H) = {i in A : s_i<=R and y_i>=H}.
```

If a source satisfies

```text
rho_u <= R  and  h_u >= H,
```

then its whole compatibility rectangle `N(u)` is contained in `D(R,H)`. Hence all `q_u` selected incidences of that source must use labels in `D(R,H)`.

Counting selected incidences into those labels yields

```text
sum_{u: rho_u<=R, h_u>=H} q_u
    <=
sum_{i: s_i<=R, y_i>=H} x_i.                   (HC6)
```

This is ordinary Hall/capacity counting on the actual selected bipartite incidence graph.

## 6. Two-rectangle Hall inequality

More generally, let

```text
D = D(R1,H1) union D(R2,H2).
```

Every source whose compatibility rectangle is wholly contained in this union must send all of its selected incidences into labels in `D`. Therefore

```text
sum_{u: N(u) subseteq D} q_u
    <=
sum_{i in D} x_i.                              (HC7)
```

The containment test can be left in this set-theoretic form; for threshold rectangles it is finite and monotone. HC7 is again direct counting, not an LP artefact.

The exact t=3 Hall-core verifier uses only unions of at most two compatibility rectangles, not all staircase Hall domains.

## 7. Total selected incidence

Counting the same selected cross-edges by sources and labels gives

```text
sum_u q_u = sum_i x_i
            = sum_i (s_i+y_i).                    (HC8)
```

In the positive-demand zero-slack sector the existing ledger also gives

```text
sum_i s_i = r+2t.                                 (HC9)
```

Thus

```text
sum_u q_u = r+2t + sum_i y_i.                     (HC10)
```

HC10 exposes the remaining global resource: any source pattern requiring large `h_u` must consume extra label load `y_i`, while HC4 constrains how high-q source types can receive supplements.

## 8. What the exact t=3 computation establishes

For the n=29, Delta=16, m=211 scope `(a,b,t,dmax)=(12,16,3,10)`, the regenerated hard positive-demand zero-slack frontier has 94 rows.

The exact Hall-core model built from HC3-HC8 plus elementary density bounds rejects all 94 rows with exact integer Farkas certificates. A separate standard-library verifier, importing neither the generator nor SciPy, checks every certificate. The clean workflow is `General RX-Hall t3 Hall core`, run `34329608225` at commit `99d60f1a1096f44285fe25ed31f50c4d20f19d83`.

The preserved report records:

```text
hard rows:                         94
exact integer Farkas rejections:  94
unresolved:                         0
Hall domains per row:              6..40
RX2 used:                           no
R/residual budget used:             no
P transport variables used:         no
Z incidence variables used:         no
unordered-pair aggregate capacity:  no
cumulative tails:                   no
```

This is a finite exact statement about the relaxation. It does not itself prove a parameteric theorem.

## 9. Candidate symbolic target

The remaining all-order problem suggested by the exact certificates is now sharply stated:

> Combine HC3-HC8 with the existing demand/charging constraints to upper-bound the available label extra-load `sum y_i` or, equivalently, to show that the source mass forced into high `h_u` / high `q_u` types exceeds the Hall capacity of the demand profile whenever the edge surplus is positive in the unresolved near-balanced degree band.

A successful elimination would replace the final LP by one or a small family of explicit threshold inequalities.

Two promising routes are:

1. **single-threshold integration:** sum HC6 over a monotone sequence of `(R,H)` thresholds and telescope the right side into a weighted demand/extra-load profile;
2. **two-corner staircase compression:** prove that for the source neighborhoods arising from the bridge, any violating Hall staircase has an equally strong witness which is the union of at most two rectangles, explaining why the t=3 finite model needs no larger domains.

The second route is particularly valuable: if true parameterically, it turns the Hall component into a low-dimensional extremal inequality rather than an exponential family.

## 10. Trust boundary / falsification priorities

Before promoting any consequence beyond this lemma package:

1. rederive HC1-HC8 independently from the graph-to-demand bridge;
2. test the one/two-rectangle sufficiency conjecture on n=30 and then n=31 as a falsification laboratory;
3. if it survives, generate exact certificates and mine their threshold weights;
4. do not infer a theorem from numerical infeasibility;
5. any failure of the universal graph-to-demand bridge overrides this entire programme.

Same-assistant derivation and checking are not external mathematical review.
