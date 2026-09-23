# n=18 realizability attack: exact D2C formulation and supplement-endpoint cap

23 September 2026. Status: internal research checkpoint. The exact MILP formulation below has not yet closed the row; the supplement-endpoint cap is a direct graph-level necessary condition at the already audited assigned-witness interface.

## 1. Exact D2C feasibility formulation: first bounded attempt

For an n=18 graph with maximum degree at most 10, use binary edge variables x_ab. For every unordered pair {a,b} and third vertex k, introduce y_abk = x_ak AND x_bk. Diameter at most two is encoded by

    x_ab + sum_{k != a,b} y_abk >= 1.

For an edge ij in a diameter-two graph, deletion of ij destroys diameter two iff at least one of the following holds:

1. i and j have no common neighbour;
2. there is z nonadjacent to i and adjacent to j such that N(i) intersect N(z) = {j};
3. symmetrically, there is z nonadjacent to j and adjacent to i such that N(j) intersect N(z) = {i}.

This characterization is exact because a length-at-most-two path using ij has i or j as an endpoint. Binary witness variables encode these alternatives, together with degree <=10 and a symmetry-fixed degree-10 root 0 with neighbours 1,...,10. (For the strict n=18 counterexample search, e>=82 forces average degree >9, hence some degree-10 vertex exists, so this root normalization is WLOG.)

The first optimization model had 7,650 variables and 27,575 constraints; HiGHS presolved it to 5,237 binary variables and 17,940 rows. A bounded ~40-second optimization run found only a 49-edge incumbent with bound 90 before termination. This is inconclusive: it neither realizes nor excludes an 82-edge D2C graph. The exact formulation is retained as a fallback feasibility route; the next run should impose e>=82 directly rather than optimize from a weak incumbent.

## 2. New graph-level supplement-endpoint capacity

In the assigned-witness construction, the right part of W* is exactly

    B = V(G) \ (N(v) union {v}),

for a maximum-degree root v. Therefore

    |B| = n - Delta - 1.

The construction already proves W* is simple and deg_W*(i)=x_i for every assigned label i. Consequently every graph-level assignment satisfies the additional necessary condition

    x_i <= |B| = n - Delta - 1.          (SUPPLEMENT CAP)

This is independent of the earlier source-capacity inequality

    x_i <= (Delta-h_i)(Delta-2).

### Immediate effect on the first n=18, Delta=10 abstract survivor

Here |B|=18-10-1=7. The first corrected abstract survivor from the preceding session has

    d=(8,7), x=(8,7), h=(8,7).

Its first label requires x_0=8 distinct supplement endpoints in B, but B has only seven vertices. Hence this particular survivor is **not graph-realizable**.

This does not by itself close the entire n=18, Delta=10 row: the abstract screen stopped after its first survivor. The next exact step is to rerun the complete row with x_i<=7 added and determine whether another abstract survivor exists.

## Trust boundary

The supplement cap is a direct consequence of the already preserved graph-level assigned-witness construction. It does not strengthen the upstream strict-counterexample-to-interface bridge, does not establish actual graph realizability of any surviving abstract point, and does not alter the existing equality scope (currently through S<=8).