# Hostile replay: half-ray Delta-three barrier

Date: 2026-09-20

Status: **same-session independent replay passed at stated conditional scope**. This replay is narrower than the daily adversarial audit and does not promote the rigid interface to graph-level reachability.

Target: `ONE_CODE_R1_K2_HALF_RAY_DELTA_THREE_BARRIER.md`.

## Checks performed

### 1. No reuse of the superseded H--U private-foot premise

The proof uses only:

- corrected B-layer H--U capacity decomposition;
- residual-column resource localization;
- rooted B-layer separation;
- preserved H--H private-foot/U certificate split;
- raw criticality of actual B-edge spokes `z p_i`.

It does not invoke the invalid claim that a U-source on an H--U edge can use a B-layer matched endpoint as witness.

### 2. The `(0,1,1)` P-exhaustion is exact

With `c0=1`, `g=1`,

`|P\W_s|=(u-g)-2=t-2=S`.

The shared-resource injection is global over all S assigned mechanisms, so every vertex of `P\W_s` is used once as a physical shared resource. The T saturated-row reverse-U witnesses are pairwise distinct and H-anticomplete because their source rows have `m_i=0`. Hence only the remaining `S-T=s0<=3` P-vertices can serve as the unique P-neighbours of the T saturated source rows. No hidden unused P-reservoir remains.

### 3. Why the saturated source rows have `m_i=0`

For a saturated row in `(0,1,1)`, `a_i=0`, so its private reverse-certificate count is `r_i^q=m_i`. It already has one residual-slot edge and, if counted in T, one shared edge to the unique outside head. Since `g=1`, a saturated row has at most two U-neighbours. Therefore

`m_i + 1 + 1 <= 2`,

so `m_i=0`. The T source rows are consequently pairwise adjacent in H.

### 4. Raw carrier code classification does not assume universality

For an H-positive `z in P`, let `D(z)` be the private coordinates where z sees the d-endpoint `p_i`. For each `i in D(z)`, reverse criticality of `z p_i` is impossible regardless of whether `z h_i` is present: if absent the required A-witness h_i cannot contain the singleton head z; if present every Y-vertex is an extra common neighbour.

Forward criticality cannot use Y (an H-neighbour of z is extra) or K (`q_j` is extra). It must use `h_l`, and matched-fibre comparison forces `D(z)={i,l}`. Repeating on `z p_l` forces z to miss both `h_i,h_l`. Therefore every H-row actually touched by z has an index outside `D(z)` and z sees that row's private foot.

This is the exact fact needed for the carrier bound; H-universality is not assumed.

### 5. H--H U-capacity is not double-counted

For one carrier z, every pair of touched T-rows is an H-edge because both rows have missing H-degree zero. Since z sees both associated private feet, z spoils both private-foot singleton orientations. The preserved H--H split therefore forces that physical H-edge to be U-certified.

The proof only concludes

`binom(d_T(z),2)<= total number of U-certified H--H edges <=u`.

It does **not** add U-certified edge counts over different carriers. Overlap between carriers can only reduce the union of rows covered relative to the sum of individual capacities, so the subsequent cover bound

`T<=s0 R(t)`

is safe.

### 6. Threshold arithmetic

`R(t)=floor((1+sqrt(8t+9))/2)`.

The most permissive case is `s0=3`, requiring

`t-5<=3R(t)`.

At `t=30`, `R=8`, so `25<=24` fails. For real t,

`t-5 > (3/2)(1+sqrt(8t+9))`

once `t>(31+3sqrt(97))/2 = 30.273...`; hence every integer `t>=31` also fails. The stated threshold `t>=30` is correct.

### 7. Other Delta-two allocations

- `(2,0,0)`: placement impossible because `g=b=0` but `S>0`.
- `(1,1,0)`: one unsaturated row, `s<=4`; impossible for `t>=6`.
- `(0,2,0)`: two unsaturated rows, total `s<=6`; impossible for `t>=8`.
- `(1,0,1)`: exact P-exhaustion gives `h<=2M_H`; the residual-slot row bound gives `2M_H<=t+2`; impossible for `t>=4`, and parity excludes `t=3`.
- `(0,1,1)`: carrier argument above excludes `t>=30`.

All six nonnegative triples summing to two are covered.

## Replay conclusion

No hidden use of the invalidated private-foot H--U chain, no resource double counting, and no missing Delta-two allocation was found.

> **Replay verdict:** the conditional theorem `Delta>=3` (hence `L_H>=3t+2`) for the corrected half-ray and `t>=30` survives this independent same-session hostile replay.

This remains conditional downstream mathematics. The daily audit's principal upstream caveat is unchanged: bounded actual-D2C regression has zero positive rigid complete Hall-cut fixtures with `x>=3`, with `X_3` mandatory.