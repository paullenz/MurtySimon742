# n=18 realizability attack: exact D2C formulation; mistaken supplement-cap route invalidated

23 September 2026. Status: internal research checkpoint. The exact MILP formulation below remains a valid fallback. The initially proposed `x_i<=n-Delta-1` supplement-endpoint cap was **incorrect and is explicitly invalidated here**; it arose from swapping the project notation for the root-neighbour and root-nonneighbour sides.

## 1. Exact D2C feasibility formulation: first bounded attempt

For an n=18 graph with maximum degree at most 10, use binary edge variables x_ab. For every unordered pair {a,b} and third vertex k, introduce y_abk = x_ak AND x_bk. Diameter at most two is encoded by

    x_ab + sum_{k != a,b} y_abk >= 1.

For an edge ij in a diameter-two graph, deletion of ij destroys diameter two iff at least one of the following holds:

1. i and j have no common neighbour;
2. there is z nonadjacent to i and adjacent to j such that N(i) intersect N(z) = {j};
3. symmetrically, there is z nonadjacent to j and adjacent to i such that N(j) intersect N(z) = {i}.

This characterization is exact because a length-at-most-two path using ij has i or j as an endpoint. Binary witness variables encode these alternatives, together with degree <=10 and a symmetry-fixed degree-10 root 0 with neighbours 1,...,10. For an n=18 strict counterexample with e>=82, average degree exceeds 9, so a degree-10 vertex exists and this root normalization is WLOG.

The first optimization model had 7,650 variables and 27,575 constraints; HiGHS presolved it to 5,237 binary variables and 17,940 rows. A bounded ~40-second optimization run found only a 49-edge incumbent with bound 90 before termination. This is inconclusive: it neither realizes nor excludes an 82-edge D2C graph. The exact formulation is retained as a fallback feasibility route; the next run should impose e>=82 directly rather than optimize from a weak incumbent.

## 2. Invalidated route: the supposed supplement-endpoint cap

The first checkpoint mistakenly read the right part of the assigned-witness graph as the root-nonneighbour side of size `n-Delta-1`. The project's actual notation in `STAR_CRITICALITY_SLACK.md` is:

- `B=N(v)`, so `|B|=Delta`;
- `A=V\(B union {v})`, so `|A|=n-Delta-1`;
- demand-positive labels lie in `A`;
- witness endpoints `T_i=N_{W*}(i)` lie in `B`.

Therefore simplicity of `W*` yields only

    x_i <= |B| = Delta,

which is weaker than the already known `x_i<=h_i<=Delta-1` for a positive assigned label. It does **not** rule out the n=18, Delta=10 survivor `x=(8,7)`.

A bounded rerun with the incorrect cap `x_i<=7` was also diagnostic only and must not be used: it found several nominal survivors, but the screen itself was based on the invalid cap. No mathematical conclusion is taken from that rerun.

## 3. Trust boundary and next step

The n=18, Delta=10 abstract survivor remains open for actual graph realizability. The next useful step is to retain the exact source and witness geometry from `STAR_CRITICALITY_SLACK.md` and either derive an additional graph-level obstruction for the specific `d=(8,7), x=(8,7), h=(8,7)` configuration or solve the exact `e>=82` D2C feasibility model. The invalidated cap is preserved here as a failed route rather than silently deleted.
