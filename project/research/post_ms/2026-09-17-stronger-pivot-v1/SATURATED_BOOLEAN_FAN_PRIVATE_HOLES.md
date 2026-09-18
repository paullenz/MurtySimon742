# Private-hole structure of saturated Boolean antipode fans

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal hand corollary of `BOOLEAN_ANTIPODE_FAN_PAYMENT.md`; not externally reviewed.

## 1. Setup

Use the near-full partial-Boolean setup of `BOOLEAN_ANTIPODE_FAN_PAYMENT.md`. Thus `p>=1`, `z in U` is an unmatched antipode centre, and `Y` is a set of `d` U-antipode partners of `z` all having the same antipode error

`eta(yz)=η>=1`.

Suppose the fan saturates the Boolean capacity bound

`d=2η+1`.

The predecessor theorem already implies:

- `G[Y]=K_d`;
- all holes of every target `y in Y` lie outside `Y`;
- every partner-partner edge is charged to an external hole;
- the charge orientation is a regular tournament on `Y`;
- every used hole has the partial Boolean code `c(z)`, complementary to the common code of `Y`.

This note extracts a stronger vertex-level consequence from equality.

## 2. A witness hole has exactly one neighbour in the partner clique

Orient an edge `xy` of the regular tournament as `x -> y`, and let `h` be the hole certifying criticality at target `y`. By construction,

`h~x`, `h not~y`,

and

`N(h) intersect N(y)={x}`.                                      (2.1)

Because `Y` is a clique, every vertex of `Y\{y}` is a neighbour of `y`. Hence (2.1) immediately implies

> `N(h) intersect Y={x}`.                                        (2.2)

So an external witness hole is not merely a hole for its target. Inside the entire saturated partner clique it is a **private foot of the source**.

## 3. Distinct sources require distinct private holes

Suppose one external vertex `h` certified an oriented edge from source `x` and another oriented edge from a different source `x'`. Equation (2.2) applied to the first edge gives

`N(h) intersect Y={x}`,

while applied to the second gives

`N(h) intersect Y={x'}`,

a contradiction.

Therefore a hole vertex can serve only one source in the regular tournament, although it may certify several outgoing edges of that same source.

Every vertex of a regular tournament on `d=2η+1>=3` vertices has positive outdegree `η`. Choose one certified outgoing edge for each source. The chosen witness holes are then pairwise distinct.

Hence:

> **SATURATED FAN PRIVATE-HOLE THEOREM.** A saturated fan with
>
> `d=2η+1`
>
> zero/error-homogeneous partners forces at least `d` distinct vertices outside `Y union {z}` whose neighbourhood in `Y` is a singleton. One can index them as
>
> `h_x`, `x in Y`,
>
> with
>
> `N(h_x) intersect Y={x}`.                                      (PH)

Moreover every `h_x` has partial Boolean code `c(z)`.

Thus the complementary code classes already contain at least

- `d` partner vertices of code `bar c(z)`;
- the hub `z` plus `d` distinct private holes of code `c(z)`.

In particular the population of `A union U` in the two complementary code classes is at least

> `2d+1`.                                                        (3.1)

## 4. If U is too small, A must absorb the private holes

Only vertices of `U\(Y union {z})` can host private holes while remaining on the B side. There are `u-d-1` such vertices. Since the saturated fan needs `d` distinct holes, at least

> `max(0, d-(u-d-1)) = max(0,2d+1-u)`                            (4.1)

of its private holes lie in `A`.

All those A-vertices have the single partial Boolean code `c(z)`.

Consequently, writing `n_c` for A-code multiplicity,

> `n_{c(z)} >= max(0,2d+1-u)`.                                  (4.2)

This is a direct bridge from equality in antipode-error payment to the A-code multiplicities that enter the preserved alpha/beta Hall-capacity inequalities.

### First saturated case

For `η=1`, one has `d=3`. A saturated fan therefore consists of

- a triangle of three antipode partners of code `bar c(z)`;
- a hub `z` of code `c(z)`;
- at least three distinct private holes of code `c(z)`, one private to each triangle vertex.

If `u<=6`, at least `7-u` of these holes lie in A. In the smallest possible four-vertex U-block (`u=4`), all three private holes lie in A and

`n_{c(z)}>=3`.

## 5. Relation to the unmatched slack floors

At `lambda=-1`, equality in the coarse bound

`E_U>=ceil(u/4)`

can only be approached by slack-one hubs saturated at `η=1`, each with three zero-slack partners. The present theorem says that every such local equality block carries an additional three-private-hole system in the complementary Boolean code class.

At `lambda=0`, a hub of slack `e` that saturates the unmatched floor has

`η=e-1`, `d=2e-1`.

It therefore forces `2e-1` distinct private holes of the hub code.

This is the first point where the strengthened fan theorem interfaces directly with the row/Hall programme: low error is possible only by creating large, highly organised complementary-code populations, and those populations are exactly what alpha multiplicity and disjoint beta-pool bounds can see.

## 6. Next use

The next compact target should combine (4.2) with the preserved projective-twin identity

`mu_alpha = max_c |alpha^{-1}(c)|`

and the per-source alpha capacity. Two possible outcomes are both useful:

1. large forced A-multiplicity in `c(z)` spills into beta obligations for the complementary zero-partner row; or
2. large alpha multiplicity implies a large true-twin clique in a switching state of the matched 2-lift, pushing the matched core back toward the already classified low switching-defect normal forms.

No such closure is claimed in this note.