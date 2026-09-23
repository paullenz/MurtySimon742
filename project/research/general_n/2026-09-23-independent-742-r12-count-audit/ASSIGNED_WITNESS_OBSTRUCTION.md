# Assigned-certificate witness obstruction

23 September 2026. Status: **proved internal reduction at the exact-H graph-level certificate-choice interface**. This uses the already proved exactness theorem `S*=H`; it does not strengthen the audited strict-counterexample-to-interface bridge and is not an externally accepted Murty--Simon proof.

## Construction

Let `L` be an inclusion-minimal subset attaining

`H = 2|union_{i in L} C_i| - sum_{i in L} h_i > 0`.

By `HALL_ENVELOPE_EXACTNESS.md`, assign every private physical B-edge to its unique label and assign every remaining physical edge of the union to any one incident label. Every physical edge is assigned exactly once, every `i in L` stays demand-positive, and, writing `x_i` for the number of physical edges assigned to `i`,

`H = sum_{i in L} (2x_i-h_i)`.

For each assigned physical edge choose one of its valid certificate orientations `u--t` for its assigned label `i`: `i` misses `t` and `N(i) intersect N(t)={u}`. Define the bipartite **assigned-witness graph** `W*` between `L` and `B` by joining `i` to this supplement endpoint `t`.

`W*` is simple. Indeed, for fixed `(i,t)` the unique-common-neighbour condition permits only one source `u`, so two different assigned physical edges cannot produce the same pair `(i,t)`. Consequently

`deg_{W*}(i)=x_i <= h_i`.

## Lemma 1: right-degree collision charge survives shared-edge assignment

Write `r_t=deg_{W*}(t)`. For every edge `i--t` of `W*`,

`h_i >= r_t`.

Proof. The assigned physical edges associated with the `r_t` incidences at `t` are pairwise distinct, because a physical edge is assigned to only one label. Hence their sources `u_1,...,u_r` are distinct. For the incidence `(i_j,t)`, `u_j` is the unique common neighbour. Therefore `i_j` misses `t` and misses every `u_k` with `k!=j`; these are `r_t` distinct B-vertices. QED.

This extends the private-witness collision charge to an exact-H attaining assignment and therefore absorbs the former shared-overlap term `2|Q|` into ordinary assigned-witness incidences.

## Lemma 2: pair-deficit charge on every assigned incidence

Put `rho=2Delta-n` and `delta_z=Delta-d(z)`. For every edge `i--t` of `W*`,

`delta_i+delta_t >= rho+1`.

Proof. `i,t` are nonadjacent and have exactly one common neighbour. Hence

`d(i)+d(t)-1 = |N(i) union N(t)| <= n-2`.

Substituting `d(z)=Delta-delta_z` gives the claim. QED.

Thus any matching of size `r` in `W*` consumes at least `r(rho+1)` total degree deficit on disjoint vertices. If `D=sum_z delta_z`, then

`nu(W*) <= floor(D/(rho+1))`.

For a strict counterexample in the current maximum-degree strip the already preserved density calculation gives `D<n rho/2` (with the sharper parity formulas retained in `DEFICIT_MATCHING_REDUCTION.md`). By Konig's theorem, `W*` has a vertex cover `X union Y`, `X subset L`, `Y subset B`, of size at most `floor(D/(rho+1))`.

## Lemma 3: whole-demand square bound off the label side of a cover

For any vertex cover `X union Y` of `W*`, put `U=L minus X` and `y=|Y|`. Then

`sum_{i in U} (2x_i-h_i) <= y^2`.

Proof. All neighbours of an `i in U` lie in `Y`, so `x_i<=y`. Lemma 1 gives `h_i>=r_t` on every incident edge, while simplicity gives `x_i<=h_i`. Therefore

`2x_i-h_i <= x_i^2/h_i
             = sum_{t in N(i)} x_i/h_i
             <= sum_{t in N(i)} x_i/r_t`.

After summing over `i in U`, each `t in Y` contributes at most `y`, because at most `r_t` uncovered labels are incident with `t` and every corresponding `x_i<=y`. There are at most `y` such vertices. QED.

## Consolidated obstruction

Every hypothetical exact-H obstruction `H>=15` can therefore be represented by an actual simple bipartite assigned-witness graph satisfying simultaneously:

1. every left vertex `i` has positive integer demand `d_i=2x_i-h_i>=1`;
2. `x_i=deg(i)<=h_i`;
3. on every edge `i--t`, `h_i>=deg(t)`;
4. on every edge, `delta_i+delta_t>=rho+1`;
5. `H=sum_i d_i`;
6. `nu(W*)<=floor(D/(rho+1))` under the strict-counterexample deficit budget;
7. for every cover `X union Y`, the demand on `L minus X` is at most `|Y|^2`.

This removes the separate `2|Q|` term from the concentrated-cover analysis. The unresolved obstruction is now genuinely star-like: a small label-side part `X` may still carry large demand through many distinct supplement endpoints even when the matching number is small.

No theorem excluding that star concentration is claimed here. An abstract star satisfying the listed inequalities is easy to write down, so these constraints alone do not prove `H<15`; the next step must use additional graph realizability/criticality information on high-demand label centres rather than merely re-optimizing the same deficit/matching inequalities.

## Exact next target

For a demand-positive label `i` with `x_i` assigned witnesses, exploit the full unique-common-neighbour geometry of the witness set `T_i`: every `t in T_i` has exactly one neighbour in `N(i)`. Derive a graph-realizability charge that grows with the star demand `2x_i-h_i`, or produce an actual D2C live-strip negative control with a large single-centre demand. This directly targets the only concentration left by the assigned-witness reduction.
