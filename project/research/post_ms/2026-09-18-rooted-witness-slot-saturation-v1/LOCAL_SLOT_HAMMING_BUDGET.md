# Local witness-slot Hamming budget

Date: 2026-09-18

Status: companion structural lemma to `ROOTED_WITNESS_SLOT_SATURATION_AND_HAMMING_DEFECT.md`.

The global identity

`H_A=sum_{(x,z) in Upsilon} c_A(x,z)`

has a stronger source-local form. This matters because the live obstruction is precisely the loss of locality when all slack/residual mass is summed before the A-edge witness channels are priced.

## 1. Local unused-slot count

Keep one chosen rooted B-edge witness-slot injection

`E(G[B]) -> Omega={(x,z) in B x A:xz notin E}`

and write `Upsilon` for the unused slots.

For `z in A`, put

> `Upsilon_z={(x,z) in Upsilon}`,                         `(L0)`
>
> `r_z=|Upsilon_z|`.                                      `(L1)`

Then

> `sum_{z in A} r_z=r`.                                   `(L2)`

Define the directed B-neighbourhood boundary of the A-edges incident with `z` by

> `H_A^+(z)=sum_{y in N_A(z)} |N_B(y)\N_B(z)|`.          `(L3)`

## 2. Exact local collision identity

### Theorem 2.1

For every `z in A`,

> `H_A^+(z)`
> ` =sum_{(x,z) in Upsilon_z} c_A(x,z)`.                 `(L4)`

#### Proof

Count ordered triples `(x,y,z)` with

- `yz in E(G[A])`;
- `x in N_B(y)\N_B(z)`.

For fixed `z`, these are exactly the terms counted on the left side of `(L4)`. On the other hand, `xz` is a B--A nonedge slot and `y` is a common A-neighbour of `x,z`, so the same triples are counted by `c_A(x,z)` over slots `(x,z)`.

Every used rooted B-edge slot has `c_A=0`, because its source and witness have a unique common neighbour and that neighbour lies in `B`. Hence only unused slots remain. `square`

Since every common A-neighbour of `(x,z)` is an A-neighbour of `z`,

> `c_A(x,z)<=d_A(z)`.                                    `(L5)`

Therefore

> `H_A^+(z)<=r_z d_A(z)`.                                `(L6)`

## 3. Local tight-code Hamming budget

Let `c(z) in {0,1}^p` be the preserved tight-fibre Boolean code on `A`.

For every A-edge `zy`, if the tight codes differ in `h` coordinates, then in each differing tight fibre the matched endpoint chosen by `y` is in `N_B(y)\N_B(z)`. Thus

> `|N_B(y)\N_B(z)|>=d_H(c(y),c(z))`.                     `(L7)`

Combining `(L4)--(L7)` gives the local theorem.

### Theorem 3.1 — local witness-slot Hamming budget

For every `z in A`,

> `sum_{y in N_A(z)} d_H(c(y),c(z))`
> ` <= r_z d_A(z)`.                                      `(LH)`

If `d_A(z)>0`, equivalently

> `average_{y in N_A(z)} d_H(c(y),c(z)) <= r_z`.         `(LH-avg)`

Thus the number of unused rooted witness slots attached to one A-coordinate controls the average tight-cube length of **all A-edges incident with that same vertex**.

This is strictly more local information than the global inequality

`2J_A<=rK_A`.

### Corollary 3.2 — zero-local-residual vertices

If `r_z=0`, then every A-neighbour of `z` has the **same** tight Boolean code as `z`.

In particular `z` is incident with no direct A-edge.

### Corollary 3.3 — local direct-fan price

Let `d_D(z)` be the number of direct A-edges incident with `z`. Direct endpoints have complementary tight codes, so each such edge has Hamming length `p`. Therefore

> `p d_D(z)<=r_z d_A(z)`.                                `(LDF)`

Equivalently, if `d_A(z)>0`,

> `d_D(z)/d_A(z)<=r_z/p`.                                `(LDF-frac)`

So a vertex whose incident A-edges are an `alpha` fraction direct must carry at least `alpha p` unused rooted B-edge witness slots locally.

Summing `(LDF)` over `z` and using `d_A(z)<=K_A` recovers

> `2pD<=rK_A`,

but `(LDF)` is the form that should be retained for the next pair/source-local synthesis.

## 4. Structural use

The new local picture is:

- low `r_z`: A-edges from `z` stay in a small Hamming neighbourhood of `c(z)`;
- high direct/complementary traffic at `z`: the same vertex must absorb a proportionally large local unused-slot budget;
- `sum r_z=r=f+delta`, so these local budgets cannot be assigned independently of the residual target.

This is a natural interface with the existing code-pair and source/Hall machinery. Instead of bounding the total direct channel and then summing pair slack, the next step should route each source's direct/non-direct split against `r_z` before complementary-pair aggregation.

The order-12 `X_3` hostile control has `r_z=0` for all three A-vertices and `d_A(z)=0`, exactly matching the theorem.