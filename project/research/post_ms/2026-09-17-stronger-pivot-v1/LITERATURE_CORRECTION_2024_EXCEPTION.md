# Literature correction: the 2019 all-order second-extremal conjecture has a 12-vertex counterexample

17 September 2026. Literature audit and strategic correction for the `paullenz/MurtySimon742` programme.

**Status:** primary-source literature correction. This is not a new theorem of the project.

## 1. The collision

Dailly, Foucaud and Hansberg (Discrete Mathematics 342 (2019), 3142–3159, DOI `10.1016/j.disc.2019.06.023`) proposed in Conjecture 3 that a non-bipartite D2C graph other than `H5` has at most

`M(n)=floor((n-1)^2/4)+1`

edges, with equality only for their expanded-`C5` family `C5+` or thirteen listed small graphs.

That statement is no longer viable as an all-order target.

Radosavljević, Stanić and Živković, *Primitive diameter 2-critical graphs*, Publications de l'Institut Mathématique 115(129) (2024), 21–32, DOI `10.2298/PIM2429021R`, explicitly state that Radosavljević found another exception. Their Figure 1 is a D2C graph with

`n=12`,
`m=32`,

a dominating edge, and

`32 > floor(11^2/4)+1 = 31`.

Thus it is a counterexample to the 2019 Conjecture 3. It is not a counterexample to Murty–Simon, since `32<floor(12^2/4)=36`.

The same small-order work reports no analogous order-13 exception, but the project will not use that enumeration as a universal certificate; the published 12-vertex graph itself is enough to invalidate the old target.

## 2. The large-order problem survives

Lin and Wang, *Characterize all C5-free diameter-2-critical graphs with at least floor((n-1)^2/4)+1 edges*, Discrete Applied Mathematics 375 (2025), 332–337, formulate the large-order question directly:

> for sufficiently large order, if a D2C graph has at least `M(n)` edges, is it complete bipartite or one of the expanded 5-cycles?

Their paper proves a substantial `C5`-free case. This sufficiently-large formulation is compatible with finite counterexamples and is therefore the correct live second-extremal target.

For project purposes define the **eventual second-extremal problem** as:

> Determine whether there exists `n0` such that every non-bipartite D2C graph of order `n>=n0` satisfies `m<=M(n)`, with equality precisely for the expanded-`C5` family `C5+`.

No value of `n0` is assumed. No claim is made here that this eventual statement is new or presently unresolved in every equivalent formulation; the literature search establishes it as an active recent research question, not as a solved theorem.

## 3. Definition correction for `C5+`

The original 2019 paper is authoritative. Its Figure 1 and introductory definition say that three consecutive vertices `x1,x2,x3` of `C5` are replaced by independent twin sets `X1,X2,X3`, with

`|X2| in {floor((n-3)/2), ceil((n-3)/2)}`.

This is the form that gives the extremal edge count `M(n)`.

The 2024 paper, while referring to the same family, prints a different `(n-2)/3` expression. Since that conflicts with the original source and with the extremal count, the project will not propagate the secondary formula.

## 4. Consequences for our mathematics

The two post-pivot algebraic observations remain valid because they were derived from the canonical bridge, not from the truth of Conjecture 3:

1. the **residual defect**

   `delta=b(n-b)-m=r-e(F)`

   converts any edge target into a lower bound on residual surplus over `F`;

2. for a maximum-degree root `v`, the total selected count

   `Q=e(G[N(v)])`

   is exactly the number of triangles through `v`.

What changes is the quantifier. We are no longer trying to prove `delta>=b(n-b)-M(n)` for every non-bipartite D2C graph outside the old exceptional list. We seek a structural mechanism proving it **eventually**, while understanding and explicitly surviving finite counterexamples.

## 5. Why the triangle-bearing branch remains natural

The expanded-`C5` extremals are triangle-free. The non-bipartite triangle-free second-extremal bound is already known. Hence a route to the eventual classification is to prove that every sufficiently large **triangle-containing** non-bipartite D2C graph lies strictly below `M(n)`.

This is precisely where the project's selected-representative / Hall machinery is potentially relevant, because `Q` counts triangles through the chosen maximum-degree root.

The open scope issue remains: a triangle-containing graph need not a priori have a maximum-degree vertex in a triangle. The finite atlas diagnostic through order 7 found no counterexample to that root property, but it is only diagnostic.

## 6. Mandatory negative control

The 12-vertex graph must now be treated as a regression test for every proposed general structural statement.

The next bounded unit is therefore not another abstract inequality. It is to recover the exact graph (from a graph6 list, adjacency data, or a faithful reconstruction of the published figure), verify D2C directly, and calculate:

- maximum degree `b` and root choices;
- `delta=b(n-b)-32`;
- rooted triangle count `Q` for every maximum-degree root;
- canonical `A/B/F` decomposition;
- residual/source profiles under the selected representative system where feasible;
- whether the maximum-triangle-root property holds;
- which proposed defect/activity inequalities are tight or fail.

A theorem that accidentally excludes this graph without an explicit large-order or structural hypothesis is wrong and must be rejected.

## 7. Revised research objective

The active hierarchy is now:

1. **benchmark the 12-vertex exception** and understand its mechanism;
2. attack the sufficiently-large triangle-bearing branch using residual defect plus Hall routing;
3. retain the known triangle-free `C5+` extremals as the equality model;
4. use the 2025 `C5`-free theorem and the 2019 dominating-edge machinery as external structural inputs when they genuinely reduce scope;
5. preserve all finite exceptions rather than patching them away informally.

This is a stronger and safer research programme than continuing either the original #742 ladder or the false 2019 all-order strengthening.
