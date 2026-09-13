# Endpoint class-packing lemma

13 September 2026. **Candidate general lemma inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

This note strengthens the single-label endpoint order-statistic argument by retaining competition between several labels for the same low-load selected sources. It is a direct consequence of simplicity of the selected incidence graph and endpoint load.

## 1. Setup

Fix a class `J` of `z` selected labels having the same selected degree `x` and the same source-compatibility condition. For example, the zero-excess demand-`d` class has

```text
x=d,
e_i=0,
s_i=d.
```

For every source `u` that is compatible with this class and has `q_u>0`, put

```text
L_u=q_u+p_u.
```

Endpoint load says that every selected incidence `ui` with `i in J` satisfies

```text
L_u <= C_i.                                           (1)
```

A source can be used at most once by a fixed label, because the selected incidence graph is simple, and at most `q_u` times over all labels.

## 2. Threshold packing bound

Fix an integer threshold `lambda`. Let

```text
A_lambda={u : u is compatible with J,
                 q_u>0,
                 L_u<lambda}.                         (2)
```

Suppose exactly `k` labels of `J` have `C_i<lambda`. Every selected source of each such label must lie in `A_lambda` by (1). Those `k` labels require exactly `x k` selected incidences from `A_lambda`.

For a fixed source `u in A_lambda`, simplicity permits at most one incidence to each of the `k` labels, while the row degree permits at most `q_u` incidences in total. Hence `u` contributes at most

```text
min(q_u,k)                                            (3)
```

of the required incidences. Therefore necessarily

```text
x k <= sum_{u in A_lambda} min(q_u,k).                (4)
```

Define

```text
kappa_lambda
 = max {0<=k<=z : x k <= sum_{u in A_lambda} min(q_u,k)}.  (5)
```

Then at most `kappa_lambda` labels in `J` can satisfy `C_i<lambda`; equivalently

```text
#{i in J : C_i>=lambda} >= z-kappa_lambda.            (6)
```

This is the **endpoint class-packing bound**.

### Proof

If `k` labels had `C_i<lambda`, all `xk` of their selected incidences would have to originate in `A_lambda`. Each source `u` can supply at most `min(q_u,k)` incidences to those labels. Summing gives (4). Thus any feasible `k` must be at most the largest `k` satisfying (4), namely `kappa_lambda`. QED.

## 3. Aggregate endpoint-mass lower bound

Since every label in the class has `C_i>=x`, threshold decomposition gives

```text
sum_{i in J} C_i
 = x z + sum_{lambda=x+1}^infinity
             #{i in J:C_i>=lambda}.                  (7)
```

Combining (6) and (7),

```text
sum_{i in J} C_i
 >= x z + sum_{lambda=x+1}^infinity
              (z-kappa_lambda).                      (8)
```

Only finitely many summands are nonzero, because once `lambda` exceeds every compatible `L_u`, the threshold source set stabilizes.

For `z=1`, (8) reduces to the ordinary endpoint lower order statistic. Thus the zero-excess endpoint-order lemma is the one-label shadow of this multi-label statement.

## 4. Why total incidence capacity alone is weaker

A coarser estimate would replace (4) by

```text
x k <= sum_{u in A_lambda} q_u.                       (9)
```

That loses the one-edge-per-source-per-label restriction. For example, three labels each needing degree three cannot be supported below a threshold by only two low-load sources, no matter how large those two row degrees are. Equation (4) detects this immediately because for every `k>0`,

```text
min(q_1,k)+min(q_2,k) <= 2k < 3k.
```

This distinct-source effect is exactly what the previous individual endpoint-order relaxation was missing.

## 5. Zero-excess demand classes

For a zero-excess demand-`d` label, selected-excess and selected-edge forcing require every selected source to satisfy

```text
rho_u>=d,
p_u<=rho_u-1,
q_u>0.                                                (10)
```

Thus the compatible set used in (2) is

```text
A_lambda(d)
 ={u:rho_u>=d,
     q_u>0,
     p_u<=rho_u-1,
     q_u+p_u<lambda}.                                 (11)
```

For `z_d` zero-excess demand-`d` labels, equations (5)-(8) give a selection-free lower bound on their **total** endpoint mass, not merely the same individual order statistic repeated `z_d` times.

## 6. Interaction with the global endpoint budget

The canonical bridge gives the exact identity

```text
sum_i C_i=r+Q.                                        (12)
```

Therefore class-packing lower bounds for disjoint label classes can be added. If

```text
sum_classes LB(class)
 + sum_remaining trivial lower bounds
 > r+Q,                                               (13)
```

the scalar branch is impossible.

Conversely, upper selected-source order statistics on the complementary labels give

```text
sum_{i in J} C_i
 = r+Q-sum_{i notin J}C_i
 >= r+Q-sum_{i notin J}UB_i.                         (14)
```

Thus endpoint class packing and endpoint-budget complement are two sides of the same fixed-sum identity.

## 7. State-122 diagnostic

The current unique weak layer of state 122 is `E=0`, so all six demand-two labels and all nine demand-three labels are zero-excess. One near-extremal source pattern exposed by the strengthened scanner is

```text
q_(rho=2) = 4,4,4,
q_(rho=3) = 0,3,3,4,4,4,4,5.
```

The former single-label relaxation lets all six demand-two labels reuse the same two cheapest eligible sources. The class-packing bound forbids that simplification once the row degrees and distinct-source condition are retained. In the equality-like incoming allocations, the demand-three class also becomes rigid: if fewer than three rho-three sources lie below a threshold, no demand-three label can lie below that threshold at all.

This is the structural reason the remaining `-1` gap should be attacked by class packing rather than by another state-specific scalar inequality.

## 8. State-283 diagnostic

The unique weak layer of state 283 has

```text
E=7,
e_(demand 2)=(0,0,7),
e_(demand 3)=0^12,
q_(rho=2)=1,1,1,1,
q_(rho=3)=5^9.
```

Every rho-three source has five selected incidences but there is only one positive-excess label, so each such source must touch a zero-excess label and hence has `p_u<=2`. Combined with the incoming-capacity ledger, the extremal branch is highly constrained. The twelve zero-excess demand-three labels then compete for nine identical high-q sources; their aggregate endpoint mass is much larger than the individual-label relaxation records.

This makes state 283 a second natural test of (8), with a different demand class from state 122.

## 9. Relation to exact Hall flow

The selected-incidence Hall theorem asks whether all row and column degrees can be realized in an allowed bipartite graph. The class-packing inequality is a threshold projection of that same object after sources are filtered by endpoint load:

```text
source u may feed a label with C_i<lambda
 only when q_u+p_u<lambda.
```

For an identical label class, inequality (4) is the degree-sequence obstruction obtained by applying simplicity and row capacities to the low-endpoint subproblem. It is deliberately cheaper than a full max-flow replay and is therefore suitable for broad quantified scans.

## 10. Mixed demand-two / demand-three joint Hall projection

The separate class bounds remain valid when several zero-excess demand classes coexist, but they do not use the fact that those classes compete for the **same** selected-source incidences. In the low-demand N34 states the important pair is the zero-excess demand-two class `J_2` and zero-excess demand-three class `J_3`.

Fix a threshold `lambda`, and suppose `a` labels of `J_2` and `b` labels of `J_3` have endpoint mass below `lambda`. Put

```text
A_2(lambda)={u: rho_u=2,
                q_u>0,
                p_u<=1,
                q_u+p_u<lambda},

A_3(lambda)={u: rho_u>=3,
                q_u>0,
                p_u<=rho_u-1,
                q_u+p_u<lambda}.                     (15)
```

A source in `A_2` can feed only demand-two labels, whereas a source in `A_3` can feed either class. Consider any subcollection containing `i` of the `a` demand-two labels and `j` of the `b` demand-three labels. It needs exactly `2i+3j` selected incidences. Simplicity and the row-degree cap imply the necessary Hall inequality

```text
2i+3j
 <= sum_{u in A_2(lambda)} min(q_u,i)
  + sum_{u in A_3(lambda)} min(q_u,i+j)               (16)
```

for every

```text
0<=i<=a, 0<=j<=b, i+j>0.                              (17)
```

No sufficiency claim is needed here: (16) is used only as a necessary feasibility test, so retaining a pair `(a,b)` that satisfies it can only weaken the resulting lower bound, never invalidate it.

Define `K_lambda` to be the largest `a+b` over pairs within the available class sizes that satisfy all inequalities (16). Then at most `K_lambda` labels across `J_2 union J_3` can have endpoint mass below `lambda`, and therefore

```text
#{i in J_2 union J_3 : C_i>=lambda}
 >= |J_2|+|J_3|-K_lambda.                             (18)
```

Threshold summation gives the mixed-class endpoint lower bound. Because demand-two labels have baseline `2` and demand-three labels baseline `3`, the `lambda=3` contribution is applied only to `J_2`; from `lambda=4` onward equation (18) applies to both classes.

The implementation uses this mixed bound only as a **global endpoint-budget feasibility prune** against `sum_i C_i=r+Q`. The score objective continues to use the already-proved separate demand-two contribution. Thus the new test does not double-count endpoint mass in the objective.

## Trust boundary

The proof of the class-packing inequality and mixed-class Hall projection is finite bipartite counting. Their Murty–Simon application depends on the canonical selected/residual bridge, especially endpoint load, selected-excess, selected-edge forcing and the exact endpoint-sum identity. They do not assert that a scalar branch satisfying the bounds extends to a graph. External checking of those bridge implications remains open.
