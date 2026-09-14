# Staircase-threshold form of sharp Hall up-sets

14 September 2026. **Candidate exact structural corollary for the directed target-capacity Hall relaxation. External mathematical review and novelty assessment remain OPEN.**

This note turns the antichain boundary from [`CANONICAL_ANTICHAIN_CERTIFICATE.md`](CANONICAL_ANTICHAIN_CERTIFICATE.md) into an explicit moving threshold in cross degree `c`.

## 1. Sharp hardness order

Recall

```text
x >=_* y
iff c_x<=c_y
    and [q_x>q_y or (q_x=q_y and P_x>=P_y)].            (1)
```

Let `S` be any up-set under this order, not necessarily a Hall minimizer. Let its minimal generators be

```text
A={g_1,...,g_h}.
```

Because `A` is an antichain, its generators have distinct cross degrees. Order them so that

```text
c_1 < c_2 < ... < c_h.                                 (2)
```

Write `g_i=(q_i,c_i,P_i)`.

## 2. Monotone staircase lemma

For `i<j`, antichain incomparability forces

```text
q_i <= q_j.                                             (3)
```

Indeed, if `q_i>q_j`, then `c_i<c_j` and hence `g_i>=_*g_j`, contradiction.

If in addition

```text
q_i=q_j,
```

then necessarily

```text
P_i<P_j.                                                (4)
```

Otherwise `c_i<c_j` and `P_i>=P_j` would again give `g_i>=_*g_j`.

Thus the generator sequence is a staircase:

```text
c strictly increases,
q weakly increases,
P strictly increases along every equal-q plateau.       (5)
```

## 3. Exact moving-threshold representation

Take any available type

```text
x=(q,c,P).
```

If

```text
c>c_h,
```

then `x` cannot dominate any generator, so

```text
x notin S.                                              (6)
```

Otherwise define

```text
i(c)=min{i : c<=c_i}.                                  (7)
```

Then:

> **Staircase-threshold theorem.** For every available type with `c<=c_h`,
>
> ```text
> x in S
> iff q>q_{i(c)}
>     or [q=q_{i(c)} and P>=P_{i(c)}].                 (8)
> ```

### Proof

The reverse implication is immediate: `c<=c_i` together with the condition on `(q,P)` says exactly that `x>=_*g_i`.

For the forward implication, suppose `x in S`. Since `S=up_*(A)`, there is some generator `g_j` with `x>=_*g_j`. Thus `c<=c_j`, so `j>=i(c)`. By (3), `q_j>=q_i`.

If `q>q_j`, then `q>q_i`. If `q=q_j>q_i`, again `q>q_i`. The only remaining case is `q=q_j=q_i`; along that equal-demand generator plateau, (4) gives `P_j>=P_i`, and `x>=_*g_j` gives `P>=P_j>=P_i`. This is exactly (8). QED.

## 4. Piecewise threshold function

Put `c_0=-infinity` symbolically. On each cross-degree band

```text
c_{i-1} < c <= c_i,                                    (9)
```

membership in `S` is governed by the single pair

```text
(q_i,P_i):

q>q_i,
or q=q_i and P>=P_i.                                  (10)
```

After `c_h` the selected set is empty.

So an arbitrary sharp-hardness up-set is exactly a **monotone threshold staircase** in the three coordinates `(c,q,P)`. No exponential family of arbitrary type subsets is needed to describe the source side once its generator staircase is known.

This does **not** reinstate the disproved one-dimensional Ferrers-prefix claim. That false claim sought one fixed linear ordering of individual sources. Here the `(q,P)` threshold changes at the generator cross-degree breakpoints `c_i` and multiple incomparable generators can be essential.

## 5. Exact Hall margin in staircase form

Let the type table have multiplicities `n_tau`. For a target type `sigma=(q_sigma,c_sigma,P_sigma)`, numerical directed compatibility with a source type `tau` is

```text
q_tau <= c_sigma+1,
c_tau >= q_sigma.                                      (11)
```

Let `selected(tau)` be the staircase rule (8). The number of selected compatible source copies before deleting the target's own source copy is therefore

```text
m_sigma =
  sum_{tau:
        selected(tau),
        c_tau>=q_sigma,
        q_tau<=c_sigma+1}
      n_tau.                                            (12)
```

The exact complete-type Hall margin is

```text
F(S)=
 sum_sigma n_sigma
   min(P_sigma, m_sigma-1_{sigma in S})
 -sum_{tau in S} n_tau q_tau.                          (13)
```

Equations (8), (12) and (13) express the target-Hall obstruction as rectangle counts against a moving staircase boundary.

## 6. Canonical Hall failure

For the canonical maximal minimizer `M+` from [`CANONICAL_ANTICHAIN_CERTIFICATE.md`](CANONICAL_ANTICHAIN_CERTIFICATE.md), the generator staircase is unique. Thus a target-Hall failure has the preferred certificate

```text
(c_i,q_i,P_i,n_i data for the generator staircase,
 full type table,
 F(M+)<0).                                              (14)
```

The full selected type set can be reconstructed deterministically from (8).

## 7. Murty-Simon-specific finite height

In the current canonical/post-pair source universe,

```text
c=q+rho
```

and the source cap used by the frontier scanners includes

```text
q<=a-rho.
```

Hence

```text
0<=c<=a.                                                (15)
```

Because distinct generators have distinct integer `c`, their number satisfies the immediate Murty-specific bound

```text
h<=a+1.                                                 (16)
```

This is not expected to be the final useful bound—it is linear rather than constant—but it turns the exact antichain into a staircase with at most one breakpoint per cross-degree level. Any stronger all-order theorem should exploit the additional relations among `q`, `rho`, `P`, demand and excess to constrain which of those breakpoints can actually occur.

## 8. Verification

[`verify_staircase_threshold_hall.py`](verify_staircase_threshold_hall.py) independently checks on exhaustive small type tables and a deterministic broad challenge that every sharp up-set:

1. has distinct generator cross degrees;
2. has the monotone generator ordering (5);
3. is reconstructed exactly by the moving threshold (8);
4. gives the same Hall margin through the staircase rectangle-count formula (12)-(13).

The verifier is arithmetic support for the hand proof, not a substitute for external review.

## 9. Trust boundary

This is an order-theoretic consequence of the sharp target-Hall relaxation. The Murty-Simon application inherits the canonical bridge and the validity of the target capacities `P`. The bound (16) uses the current canonical source cap `q<=a-rho`; it is not asserted outside settings where that cap has been established.

The unrestricted Murty-Simon conjecture is not proved by this result.
