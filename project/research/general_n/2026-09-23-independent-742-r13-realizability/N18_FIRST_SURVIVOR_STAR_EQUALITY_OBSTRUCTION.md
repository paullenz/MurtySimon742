# n=18, Delta=10: minimum-deficit optimizer excluded; star-slack is strict for x>=3

23 September 2026. Status: **internal graph-level refinement**, conditional on the already preserved assigned-witness interface and `STAR_CRITICALITY_SLACK.md`.

Important correction: the argument below excludes the **13-deficit optimizer** of the first abstract tuple; it does **not** exclude the whole tuple `d=(8,7), x=(8,7), h=(8,7)`. After adding the strict star refinement to the abstract MILP, the same tuple remains feasible with minimum total deficit 14, still below the strict-counterexample budget 16. The earlier broader wording is therefore superseded here.

## The 13-deficit optimizer

The preceding minimum-deficit realization has

    demand d=(8,7),
    x=(8,7),
    h=(8,7),
    centre deficits (7,6),

with seven witness endpoints shared by both labels plus one endpoint used only by the first label, all endpoint deficits zero.

Use the project notation of `STAR_CRITICALITY_SLACK.md`: for a maximum-degree root v, `B=N(v)` has size Delta=10 and demand-positive labels lie in `A=V\(B union {v})`, where |A|=7.

For the second label i,

    x=h=7, delta_i=6, rho=2,

and every t in its witness set T has delta_t=0. Hence

    epsilon_t = delta_i + delta_t - (rho+1) = 3,
    sum epsilon_t = 21 = binom(7,2).

### Equality contradiction

Write C=binom(7,2), e=e(G[T]), alpha=2(C-e), and beta=sum_z l_z as in the star-slack proof. Then

    C = sum epsilon_t >= alpha+beta >= 2C-e >= C.

Thus equality holds throughout: `G[T]=K_7`, `beta=e=C`, and total Z-certificate capacity is used with no slack.

For any `z in Z`, let `S_z=N(z) intersect T`, `k_z=|S_z|`, `l_z=x-k_z`. In a clique T, a vertex t outside S_z is adjacent to every member of S_z. Therefore z can certify an oriented T-edge from t only when `k_z=1`; `k_z=0` has no adjacent endpoint, while `k_z=x` has `l_z=0`.

If equality capacity is fully used, each positive-capacity z must therefore have a singleton S_z and must use all x-1 star edges incident with its singleton centre. Since total certificate capacity equals the number of T-edges, these singleton stars would have to partition E(K_x): every edge would need exactly one endpoint among the chosen singleton centres. For x>=3 this is impossible, because either the chosen-centre set or its complement contains an internal edge (indeed both cannot have size at most one).

Hence equality in the quadratic star-slack theorem is impossible for every x>=3.

## Strict star-slack corollary

Because all quantities are integral, for any assigned-witness star with x>=3,

    sum_{t in T} epsilon_t >= binom(x,2)+1.

Equivalently,

    x delta_i + sum_{t in T} delta_t
      >= x(rho+1) + binom(x,2) + 1.      (STRICT-STAR)

This is a genuine graph-realizability strengthening of the existing quadratic star-slack inequality, still conditional on the same assigned-witness interface.

## Effect on the first tuple

Re-solving the preserved aggregated incidence model with `+1` in each star inequality for x>=3 gives for `d=(8,7), x=(8,7), h=(8,7)`:

    minimum total deficit = 14,
    centre deficits = (7,6),
    right types = one label-0-only endpoint of deficit 0,
                  six shared endpoints of deficit 0,
                  one shared endpoint of deficit 1.

Thus STRICT-STAR invalidates the old 13-deficit optimizer but **does not yet close** this tuple under Dmax=16.

## Next action

Use the resulting near-equality structure together with the exact source geometry (`x=h` for both labels, so every missed root-neighbour is an assigned witness) or test it directly in the exact n=18 D2C feasibility model. Do not promote the tuple exclusion until every realization with total deficit at most 16 is ruled out.
