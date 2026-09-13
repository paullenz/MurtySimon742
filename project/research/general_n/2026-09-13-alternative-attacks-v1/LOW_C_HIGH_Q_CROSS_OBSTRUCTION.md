# Low-c / high-q cross obstruction

13 September 2026. **Candidate general theorem inside the canonical selected/residual bridge. External mathematical review and novelty assessment remain OPEN.**

This is a compact symbolic consequence of [`POTENTIAL_PAIR_CAPACITY.md`](POTENTIAL_PAIR_CAPACITY.md). It converts the two-dimensional potential-pair restriction into a one-parameter product inequality and may be more useful for an all-order argument than explicit pair-capacity enumeration.

## 1. Setup

For each `u in B`, write

```text
q_u = selected outdegree,
rho_u = residual A-cross degree,
c_u = q_u+rho_u,
Q = sum_u q_u = |E(overline{H[B]})|.
```

The directed compatibility theorem implies that if an unordered pair `{u,w}` is a missing B-edge, then necessarily

```text
c_w>=q_u-1.                                           (1)
```

Indeed either orientation of the missing pair forces this weak inequality; see [`POTENTIAL_PAIR_CAPACITY.md`](POTENTIAL_PAIR_CAPACITY.md).

## 2. Threshold sets

For any integer `r`, define

```text
L_r={w:c_w<=r},
U_r={u:q_u>=r+2}.                                     (2)
```

Write their cardinalities as

```text
ell_r=|L_r|,
u_r=|U_r|.                              (3)
```

If `u in U_r` and `w in L_r`, then

```text
q_u>=r+2>c_w+1,                                      (4)
```

contradicting the necessary missing-pair condition (1). Therefore **no pair between `U_r` and `L_r` can be a missing B-edge**.

Moreover `U_r` and `L_r` are disjoint: if `u in U_r`, then

```text
c_u=q_u+rho_u>=q_u>=r+2>r,                            (5)
```

using only `rho_u>=0`. Thus the forbidden cross pairs are exactly `ell_r u_r` distinct unordered pairs.

## 3. Product inequality

There are `binom(b,2)` unordered pairs in `B`. Since every pair between `U_r` and `L_r` is forbidden from the missing graph,

```text
Q
 <= binom(b,2)-ell_r u_r.                             (6)
```

Equivalently:

> **Low-c / high-q cross obstruction.** For every integer `r`, every legal branch satisfies
>
> ```text
> Q + ell_r u_r <= binom(b,2).                        (7)
> ```

This is a selection-orientation-free consequence once the scalar margins `(q,rho)` are fixed.

## 4. Slack interpretation

Define the missing-pair slack

```text
sigma=binom(b,2)-Q.                                   (8)
```

Then (7) is simply

```text
ell_r u_r<=sigma.                                     (9)
```

Hence any threshold with many low-`c` vertices immediately limits the number of high-`q` sources:

```text
u_r<=floor(sigma/ell_r)                               (10)
```

when `ell_r>0`.

Conversely, many high-`q` sources force

```text
ell_r<=floor(sigma/u_r).                              (11)
```

Thus a dense missing graph cannot simultaneously contain a substantial low-cross-neighbourhood reservoir and many large selected-load sources.

## 5. Source-demand specialization

Selected-edge forcing gives

```text
s_i<=rho_u                                            (12)
```

on every selected incidence. If

```text
d=min_i{s_i:s_i>0},                                   (13)
```

then every source with

```text
rho_u<d                                               (14)
```

has no selected positive-demand incidence. In all-positive-demand states this forces

```text
q_u=0,
c_u=rho_u.                                           (15)
```

Therefore any known mass of low residual degrees automatically contributes to `ell_r` for suitable `r`. Equation (10) then bounds how many remaining sources may have selected load at least `r+2`.

This is precisely the qualitative mechanism visible in the pair-capacity closures of states 13518 and 13519: several low-rho vertices become unusable as missing neighbours of high-q sources.

## 6. Layer-cake relation

Summing the forbidden cross-pair incidences over thresholds is not directly valid because one pair can be counted at several `r`. However, each ordered inversion

```text
q_u>=c_w+2                                             (16)
```

corresponds to the interval of thresholds

```text
c_w<=r<=q_u-2.                                        (17)
```

Thus

```text
sum_r ell_r u_r
 = sum_{u,w} max(0,q_u-c_w-1).                        (18)
```

Equation (18) is a useful weighted inversion identity. The unweighted incompatibility count from [`POTENTIAL_PAIR_GLOBAL_BOUNDS.md`](POTENTIAL_PAIR_GLOBAL_BOUNDS.md) is

```text
I_1=#{(u,w):q_u>=c_w+2}.                              (19)
```

while (18) records the total inversion depth.

The product inequality (7) holds separately at every threshold; (18) suggests a possible route to combine those inequalities with convexity or majorization without double-counting pairs naively.

## 7. Relation to residual h-index ideas

Earlier residual h-index arguments classified how many residual degrees exceed a threshold. Here the natural threshold object is

```text
ell_r=#{w:q_w+rho_w<=r},                              (20)
```

paired with

```text
u_r=#{u:q_u>=r+2}.                                    (21)
```

The obstruction

```text
ell_r u_r<=binom(b,2)-Q                               (22)
```

therefore has an h-index-like character but couples the selected outdegree distribution to the combined cross-neighbourhood distribution. It may supply the missing bridge between the earlier scalar residual theory and the newer orientation geometry.

## 8. Immediate research targets

Natural next steps are:

1. combine (22) with `q_u+rho_u<=a` to bound possible q tails;
2. combine it with selected-demand forcing to obtain lower bounds on `ell_r` from the rho distribution;
3. optimize `sum q=Q` under the family (22) to derive a selection-free scalar upper bound on Q;
4. incorporate total-excess source caps so high-q vertices also have reduced incoming capacity;
5. test whether the resulting symbolic relaxation subsumes a substantial fraction of the exact pair-capacity frontier closures.

## Trust boundary

The proof of (7) is elementary once the potential-pair condition is accepted. Its Murty-Simon application therefore inherits the canonical bridge trust boundary. It is a necessary condition only; satisfying it does not imply graph feasibility or prove the unrestricted conjecture.
