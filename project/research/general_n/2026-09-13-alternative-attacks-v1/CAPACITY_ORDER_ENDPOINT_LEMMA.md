# Capacity-order endpoint lemma

13 September 2026. **Candidate general lemma inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

This note turns the exact-demand endpoint-order lemma into a source-capacity statement that can be evaluated **before choosing the incoming allocation** `p`. Its purpose is twofold: it gives a reusable symbolic availability theorem, and it removes the need to enumerate candidate endpoint pairs in the adjacent-family scan.

It is a necessary-condition relaxation, not a graph-existence theorem.

## 1. Setup

Fix a residual/scalar state and a selected-outgoing vector `q`. Let `Q=sum_u p_u` be the required total incoming load. Suppose a valid relaxation supplies, for each source `u`, an integral upper cap

```text
0 <= p_u <= M_u.                                      (1)
```

The `h_2` relaxation used in the N=34 adjacent-family scanner is the special case

```text
M_u(h_2)
 = min( (q_u>h_2 ? rho_u : rho_u+b-a-1),
        b-1-q_u ),                                    (2)
```

with negative values truncated to zero. Nothing in the theorem below depends on this particular formula: any simultaneously valid source caps `M_u` may be substituted.

For a zero-excess exact-demand label of demand `d`, the endpoint-order lemma says that every selected source belongs to

```text
A_d={u: rho_u>=d, q_u>0, p_u<=rho_u-1},              (3)
```

and, writing `L_u=q_u+p_u` on `A_d`,

```text
C_i >= max(d,L_(d)),                                  (4)
```

where `L_(d)` is the `d`-th smallest eligible endpoint load.

The difficulty is that both `A_d` and `L_(d)` depend on the unknown incoming allocation `p`. The next statement removes that dependence.

## 2. Capacity loss at an endpoint threshold

Fix an integer threshold `lambda`. A source can count among `d` eligible endpoints with load at most `lambda` only if

```text
rho_u>=d,
q_u>0,
q_u<=lambda.                                          (5)
```

For such a candidate source, imposing both exact-demand eligibility and endpoint load at most `lambda` changes its incoming cap from `M_u` to

```text
m_u(lambda)
 = min(M_u, rho_u-1, lambda-q_u).                     (6)
```

Define its capacity loss

```text
delta_u(lambda)=M_u-m_u(lambda) >= 0.                 (7)
```

Let

```text
U=sum_u M_u.                                          (8)
```

If fewer than `d` sources satisfy (5), put

```text
D_d(lambda)=infinity.
```

Otherwise let `D_d(lambda)` be the sum of the `d` smallest values `delta_u(lambda)` among sources satisfying (5).

Thus `D_d(lambda)` is the least total incoming capacity that must be sacrificed in order to force **some `d` distinct sources** to be eligible exact-demand endpoints of load at most `lambda`.

## 3. Capacity-order theorem

**Theorem.** If a feasible incoming allocation `p` of total load `Q` has

```text
L_(d) <= lambda,                                      (9)
```

then necessarily

```text
Q <= U-D_d(lambda).                                   (10)
```

Consequently define

```text
Lambda_d
 = min { lambda : D_d(lambda)<infinity
                  and Q<=U-D_d(lambda) }.             (11)
```

If the set in (11) is nonempty, every feasible incoming allocation containing a zero-excess demand-`d` label satisfies

```text
L_(d) >= Lambda_d,                                    (12)
C_i >= max(d,Lambda_d).                               (13)
```

If the set in (11) is empty throughout the permitted endpoint range, then the zero-excess demand-`d` branch is impossible in this relaxation.

### Proof

Assume `L_(d)<=lambda`. Then at least `d` sources in `A_d` have `q_u+p_u<=lambda`. Call any `d` of them `K`.

Every `u in K` satisfies (5), and its incoming value obeys all three bounds

```text
p_u<=M_u,
p_u<=rho_u-1,
p_u<=lambda-q_u.
```

Hence

```text
p_u<=m_u(lambda).
```

All sources outside `K` remain bounded by `M_u`. Therefore

```text
Q=sum_u p_u
 <= sum_{u notin K} M_u + sum_{u in K} m_u(lambda)
 = U-sum_{u in K} delta_u(lambda).
```

Among all candidate `d`-sets, the smallest possible loss is `D_d(lambda)`, so

```text
Q<=U-D_d(lambda),
```

which proves (10).

If `lambda<Lambda_d`, condition (10) fails (or fewer than `d` candidates exist), so `L_(d)<=lambda` is impossible. Since all quantities are integral, (12) follows. Equation (13) then follows from the corrected endpoint-order lemma `C_i>=max(d,L_(d))`. QED.

## 4. Exactness inside the pure capacity relaxation

When the only constraints on `p` are the independent integral intervals (1) plus `sum p_u=Q`, condition (10) is not merely necessary for the existence of `d` endpoints at threshold `lambda`: it is sufficient.

Choose the `d` candidates attaining `D_d(lambda)`, cap them by (6), leave every other source at cap `M_u`, and distribute `Q` indistinguishable incoming units among the resulting integer intervals. Every integer total from zero through the total capacity is attainable. Hence `Lambda_d` is the **exact minimum possible `d`-th eligible endpoint load in the source-cap relaxation**.

Additional graph or incidence constraints can only increase the true endpoint order statistic.

## 5. Demand-two corollary for the baseline-three inequality

For a zero-excess demand-two label define

```text
mu_2=max(2,Lambda_2).                                 (14)
```

If

```text
z_0=#{i:s_i=2,e_i=0},
```

then every one of those labels satisfies `C_i>=mu_2`, even if different labels reuse the same eligible sources. Therefore their aggregate negative baseline-three correction is at most

```text
-z_0 mu_2.                                            (15)
```

This is safe because the endpoint bound is global: any selected pair of eligible sources has maximum load at least the second-smallest eligible load, and (12) lower-bounds that statistic for every feasible `p`.

## 6. Combination with the incoming-cost lower bound

For fixed `q`, threshold count `h_2` and total incoming load `Q`, let

```text
P_min(q,h_2,Q)
```

be the usual greedy minimum of

```text
sum_u q_u p_u
```

under the source caps (2).

Independently, the capacity-order theorem gives `mu_2`. Hence every feasible `p` in a branch with `z_0` zero-excess demand-two labels satisfies

```text
sum_u q_u p_u + z_0 max(2,L_(2))
 >= P_min(q,h_2,Q) + z_0 mu_2.                        (16)
```

No joint-attainment assumption is required: the two lower bounds hold simultaneously for every feasible allocation. This is the key computational simplification. The scanner need not enumerate endpoint pairs or condition the greedy incoming allocation on a chosen pair.

## 7. Relation to state 519 and the adjacent family

The dedicated state-519 replay minimized incoming cost jointly with an explicitly chosen eligible source pair and closed the exceptional layers `E=6,8,9`. The theorem above abstracts the same source-availability phenomenon into a selection-free capacity calculation.

For the remaining adjacent-family states `230,282,385`, the old refined scan already closes the high-excess tails. The capacity-order bound therefore only needs to be evaluated on their non-strict low/mid-excess layers. It should be used as a cheap screen before any further exact incidence replay.

The theorem does **not** claim that any of those three states is newly closed. That conclusion requires an exact integer scan with the strengthened correction and subsequent treatment of any surviving equality/non-strict profiles.

## 8. Generalisation

The argument is not specific to `d=2`, baseline three, N=34, or the particular `h_2` cap. For any demand `d` and any valid simultaneous source caps `M_u`, it converts a requirement for `d` low-load eligible sources into the scalar capacity loss `D_d(lambda)`.

This exposes a reusable duality:

- threshold/excess arguments reduce **incoming capacity** of high-`q` sources;
- exact-demand labels require **availability** of low-`p` sources;
- forcing low endpoint load consumes a quantifiable amount of the same incoming capacity;
- the `d` smallest capacity losses determine the best possible endpoint order statistic in the relaxed ledger.

That is the structural content behind the state-519 pair calculation.

## Trust boundary

This note depends on the canonical selected/residual bridge, the selected-excess lemma and the corrected exact-demand endpoint-order lemma. It makes no graph-level switching assumption and does not choose quasi-edge representatives. External review and independent computational reproduction remain open.
