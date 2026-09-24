# Saturated (5,5,5) exclusion from one-use sources and the degree budget

24 September 2026. Status: internal finite graph-interface proof. It removes the need for the full D2C SAT model for the exact-H one-use realization of this fixed tuple, but it does not close any other n=18 profile or the general theorem.

## Strict star slack

For an assigned star with `x>=3`, the quadratic star proof can be made strict:

    sum_{t in T} epsilon_t >= binom(x,2)+1.

If equality held at `binom(x,2)`, the proof's inequalities force `G[T]=K_x` and exactly `binom(x,2)` missing T--Z incidences. In a clique, a Z-vertex certifying a T-edge must have exactly one neighbour in T; otherwise the nonadjacent endpoint has more than one common neighbour with it. The singleton neighbour sets used by the certificates must cover every edge of `K_x`, so at least `x-1` such Z-vertices are needed. Each has `x-1` missing T-incidences, giving at least `(x-1)^2>binom(x,2)` for `x>=3`, contradiction.

This supplies the `+1` used by the strengthened witness-deficit code for ordinary stars of size at least three.

## Deficit-budget rigidity at n=18, Delta=10

Take three labels with `d=x=h=5`, and suppose the strict-counterexample budget `D<=16`. Put `C=sum_i delta_i`. Summing the three strict star inequalities gives

    78 <= 5C + sum_t r_t delta_t.

There are only three labels, so `r_t<=3`, while all deficits outside the centres total at most `D-C`. Hence

    78 <= 5C+3(D-C) <= 48+2C.

Each centre has `delta_i<=h_i=5`, so `C<=15`. Every inequality is therefore equality:

- `D=16`;
- all three centre deficits equal five;
- exactly one noncentre vertex has deficit one;
- that vertex is a right endpoint incident with all three labels;
- every other vertex has deficit zero.

In particular an empty membership type occurs.

## Four remaining membership geometries

Saturation says every vertex outside `C_i` is an assigned endpoint for label i. The one-use membership-step lemma and the three cardinalities `|C_i|=5` leave five labelled count vectors. The deficit-one common endpoint removes the vector with no empty type, leaving four (three are label permutations):

    (1,1,1,2,2,1,1,1)
    (1,1,2,1,1,2,1,1)
    (1,2,1,1,1,1,2,1)
    (2,1,1,1,1,1,1,2).

The committed checker exhausts every one-use Boolean-step source skeleton for these vectors. Each has eight valid skeletons. In every skeleton the unique-common-neighbour constraints forbid exactly 28 of the 45 possible B-edges, so at most 17 B-edges can occur.

## Degree-sum contradiction

Let U be the four inactive A-vertices. The three active labels have degree five and no A-neighbours; the B-degree targets are nine at the unique deficit-one empty-type vertex and ten at every other B-vertex. Summing degrees over B gives

    99 = 10 (root edges) + 15 (active-label edges)
             + 2e(B) + e(B,U).

The four U-vertices have total degree 40 and at most six internal edges, so `e(B,U)>=28`. Therefore `e(B)<=23`; more importantly, eliminating `e(B,U)` with

    40 = e(B,U)+2e(U)

gives `e(B)=17+e(U)>=17`.

Since only 17 B-edges are allowed, all allowed B-edges must occur, `e(U)=0`, and every U--B edge must occur. Hence an empty-type B-vertex needs B-degree four if its deficit is one, and B-degree five if its deficit is zero.

The exact source-skeleton enumeration now gives:

- in each vector with one empty vertex, that vertex has only three allowed B-neighbours, below the required four;
- in the vector with two empty vertices, each has only four allowed B-neighbours, but one is the deficit-zero vertex and requires five.

All four geometries are impossible. Combined with the private-source contradiction for the previously recorded common-C geometry, this excludes the saturated exact-H `(5,5,5)` tuple at the graph interface without appealing to full diameter/D2C SAT.

Reproduction:

    python exclude_saturated_555_degree.py

The enumeration is finite internal verification, not external mathematical acceptance. Equality remains controlled only through the separate `S<=8` theorem.
