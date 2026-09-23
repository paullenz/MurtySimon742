# n=18, Delta=10: first abstract survivor excluded by star-equality rigidity

23 September 2026. Status: **internal graph-level obstruction**, conditional on the already preserved assigned-witness interface and `STAR_CRITICALITY_SLACK.md`. It excludes the specific first abstract survivor from `WITNESS_DEFICIT_ROWS_17_18.md`; it does not yet close the entire n=18, Delta=10 row.

## Survivor data

The first abstract survivor has

    demand d=(8,7),
    assigned witness counts x=(8,7),
    missed-root-neighbour counts h=(8,7),
    centre deficits (7,6),

and its minimum-deficit realization has seven witness endpoints shared by both labels plus one endpoint used only by the first label, all with endpoint deficit zero.

Use the project notation of `STAR_CRITICALITY_SLACK.md`: for a maximum-degree root v, `B=N(v)` has size Delta=10 and the demand-positive labels lie in `A=V\(B union {v})`, where |A|=7.

Focus on the second label i. Here

    x=h=7, delta_i=6, rho=2.

Its witness set T has seven vertices. Every t in T has delta_t=0 in the minimum-deficit survivor. Hence every pair-deficit slack is

    epsilon_t = delta_i + delta_t - (rho+1) = 6-3 = 3,

so

    sum_{t in T} epsilon_t = 21 = binom(7,2).

Thus the quadratic star-slack theorem is attained with equality.

## Equality consequences

Write C=binom(7,2)=21, e=e(G[T]),

    alpha = 2(C-e)

for the ordered missing incidences inside T, and

    beta = sum_{z in Z} l_z,

where `S_z=N(z) intersect T`, `k_z=|S_z|`, and `l_z=7-k_z`.

The proof of the star-slack theorem gives

    sum epsilon_t >= alpha+beta,
    e <= beta.

Therefore

    21 >= 2(21-e)+beta >= 42-e >= 21.

Every inequality is equality. In particular

1. `e=21`, so `G[T]=K_7`;
2. `beta=e=21`;
3. the total Z-certificate capacity is used with no slack.

For this label, `|R|=h-delta_i=1`, so `|Z|=|A|-1-|R|=5`.

## Certificate-capacity contradiction

Fix `z in Z`. If `0<k_z<7`, then every `t in T minus S_z` is adjacent in the clique `G[T]` to **all** `k_z` vertices of `S_z`. For z to certify an oriented T-edge with nonadjacent endpoint t, the adjacent endpoint must be the **unique** common neighbour of t and z inside T. Hence z can certify a T-edge only when `k_z=1` (the cases `k_z=0` and `k_z=7` certify none).

But equality `e=beta=21` means the total upper capacity `sum l_z` is completely used to certify all 21 T-edges. Consequently every z with `l_z>0` must actually realize its full `l_z` capacity. The only possible positive-capacity type is therefore `k_z=1`, giving `l_z=6`; vertices with `k_z=7` contribute `l_z=0`.

Thus `beta=sum l_z` must be a multiple of 6. It cannot equal 21. Contradiction.

Hence the first `d=(8,7), x=(8,7), h=(8,7)` abstract survivor is **not realizable by a diameter-two-critical graph** at the assigned-witness interface.

## Scope and next action

This is a realizability exclusion of one optimizer, not a proof that the full n=18, Delta=10 abstract row is empty. The next step is to continue the row search past this survivor and test subsequent minimum-deficit configurations against the same equality/near-equality certificate geometry, or encode the certificate-capacity refinement directly in the abstract optimizer.
