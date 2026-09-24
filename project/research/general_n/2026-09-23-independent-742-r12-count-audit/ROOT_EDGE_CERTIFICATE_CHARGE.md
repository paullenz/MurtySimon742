# Root-edge certificate charge for assigned-witness endpoints

24 September 2026. Status: internally proved graph-level necessary condition at the assigned-certificate interface. It is not a complete realizability theorem and does not close the demand-15/16 obstruction.

Let `v` be a maximum-degree root, `B=N(v)`, `A=V(G)\(B union {v})`, `|B|=Delta`, `|A|=a=n-1-Delta`, and `rho=2Delta-n`. In an assigned-witness graph let `I_t` be the labels incident with a right endpoint `t in B`, let `r_t=|I_t|>0`, and let `U_t` be the `r_t` distinct physical B-sources of those incidences.

## Lemma

For every right endpoint `t`, criticality of the root edge `vt` has one of two forms.

1. There is an A-vertex `x_t` with `N(x_t) intersect B={t}`. Then

       delta_{x_t} >= rho+1+r_t.

2. There is a B-vertex `b_t` with `N(b_t) intersect N(t)={v}`.

If several endpoints use the same B-witness `b`, write `T_b={t:b_t=b}`. Then

       delta_b >= max(0, |T_b union (union_{t in T_b} U_t)|-a).

The A-witnesses belonging to distinct endpoints are distinct. Consequently, after choosing one root-edge certificate for every right endpoint,

    D >= sum_{t in S} (rho+1+r_t)
         + sum_b max(0, |T_b union (union_{t in T_b} U_t)|-a),

where `S` is the set of endpoints using the A-singleton branch and the second sum is over the distinct B-witness vertices. Each graph vertex is charged at most once in this inequality.

### Proof

Because `r_t>0`, endpoint `t` has a B-neighbour (indeed every source in `U_t`), so deleting `vt` cannot make the endpoints `v,t` themselves farther than two. The standard edge-criticality alternative therefore supplies either an A-vertex whose unique B-neighbour is `t`, or a B-vertex whose only common neighbour with `t` is `v`.

In the first branch, every `i in I_t` is nonadjacent to `t` and has a unique common neighbour with `t`, namely its assigned source. If `x_t` were adjacent to `i`, it would be a second common neighbour of `i,t`. Hence `x_t` misses all `r_t` labels in `I_t`. It has only one B-neighbour and at most `a-1-r_t` A-neighbours, so

    d(x_t) <= 1+(a-1-r_t)=a-r_t,
    delta_{x_t} >= Delta-a+r_t=rho+1+r_t.

Different singleton B-neighbourhoods `{t}` give different A-vertices.

In the second branch, `b` is nonadjacent to every `t in T_b`. It is also nonadjacent to every source in every `U_t`, since those sources are neighbours of `t` and `b,t` have no common neighbour other than `v`. Thus `b` has at least `|T_b union union U_t|` nonneighbours among the other `n-1` vertices, giving

    d(b) <= n-1-|T_b union union U_t|,
    delta_b >= |T_b union union U_t|-a.

Taking the nonnegative part and summing over distinct A-witnesses and distinct B-witnesses proves the claim. QED.

## Exact interpretation and present limitation

This packages the root-edge mechanism used in the fixed saturated `(8,7)` closure. Its singleton branch explains the charge `delta_{x_p}>=4` there: `rho=2` and `r_p=1`.

At profile-only resolution the B-witness branch can still be almost free: without retaining physical source identities, one knows only weak lower bounds on the union across different endpoints, and these are usually at most `a`. Therefore the lemma does not honestly improve the existing scalar demand-15/16 screen by itself. Its theorem-facing use is to add root-certificate choice variables to the explicit-source model, with the exact source union in the B-witness branch. Treating every right endpoint as if it necessarily used the singleton branch would be invalid.

The next bounded test is to insert these two certificate branches into the explicit-source realizability model and determine whether the remaining leading profiles can route all right endpoints through low-charge B-witness classes.
