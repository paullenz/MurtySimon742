# q-layer threshold normal form

14 September 2026. **Candidate exact structural theorem for the q-stratified target-Hall reduction. External mathematical review remains OPEN.**

The q-stratified minimum-cut theorem reduces exact target-Hall failure to the q-only receiver quantity

```text
U_q(S)=sum_q sum_{k>=1} min(alpha_{q,k},beta_{q,k}).
```

This note removes the remaining target-by-target incoming geometry from `beta`. For each fixed target demand `q`, every incoming layer is controlled by one order statistic of selected-source demands and one cross-degree threshold.

## 1. Setup

Fix an arbitrary labelled source set `S`. For every vertex `u` write

```text
q_u,
c_u=q_u+rho_u,
P_u.
```

Directed numerical compatibility is

```text
D(u,w)
 iff u!=w,
     q_u<=c_w+1,
     q_w<=c_u.
```

For a target `w`, before deleting the forbidden diagonal define

```text
m_w(S)
 = #{u in S : q_u<=c_w+1 and q_w<=c_u}.
```

The actual incoming count is

```text
y_w(S)=m_w(S)-1_{w in S}.
```

For fixed target demand `q`, define the active selected-source multiset

```text
A_q(S)={q_u : u in S and c_u>=q},
```

with multiplicity, and write its elements in nondecreasing order

```text
r_{q,1}<=r_{q,2}<=...<=r_{q,N_q}.
```

Set `r_{q,k}=+infinity` for `k>N_q`.

## 2. Exact preincoming threshold

For any target `w` with `q_w=q`,

```text
m_w(S)
 = #{u in S : c_u>=q and q_u<=c_w+1}.
```

Therefore the following are equivalent:

```text
m_w(S)>=k,
r_{q,k}<=c_w+1,
c_w>=r_{q,k}-1.
```

Hence:

> **Preincoming order-statistic threshold.** For every `q,k>=1` and every target `w` with `q_w=q`,
>
> ```text
> m_w(S)>=k
> iff
> c_w>=r_{q,k}-1.                                      (1)
> ```

This is exact and uses no cap information.

## 3. Exact actual-incoming layer count

Let

```text
T^O_q(t;S)=#{w notin S : q_w=q and c_w>=t},
T^S_q(t;S)=#{w in S    : q_w=q and c_w>=t}.
```

For an unselected target, `y_w=m_w`, so by (1)

```text
y_w>=k iff c_w>=r_{q,k}-1.
```

For a selected target, `y_w=m_w-1`, so

```text
y_w>=k
 iff m_w>=k+1
 iff c_w>=r_{q,k+1}-1.
```

Consequently:

> **Exact beta-layer formula.**
>
> ```text
> beta_{q,k}(S)
> = T^O_q(r_{q,k}-1;S)
>   + T^S_q(r_{q,k+1}-1;S).                            (2)
> ```

Thus the entire incoming side of the q-stratified receiver formula is determined by:

```text
selected-source demand order statistics r_{q,k},
and selected/unselected c-tail counts at target demand q.
```

No target-by-target compatibility matrix remains.

## 4. Rectangle-count inverse form

Define the selected-source rectangle count

```text
R_S(q,t)
 = #{u in S : c_u>=q and q_u<=t}.                      (3)
```

Then

```text
r_{q,k}=min{t:R_S(q,t)>=k},                            (4)
```

with `+infinity` if the set is empty.

So the order statistics themselves are just inverse cumulative counts in the `(q,c)` source histogram. Equation (2) is therefore an exact two-dimensional histogram formula, not a flow statement.

## 5. Cap-side threshold

Assume fixed-q cap monotonicity:

```text
q_x=q_y,
c_x<=c_y
 => P_x<=P_y.
```

For every `q,k`, define

```text
theta_{q,k}
 = min{c_w : q_w=q and P_w>=k},                        (5)
```

with `+infinity` if no such target exists.

Because `P` is nondecreasing in `c` at fixed `q`, the set `P_w>=k` is a c-suffix. Writing

```text
T_q(t)=#{w:q_w=q and c_w>=t},
```

we have the exact cap-layer formula

```text
alpha_{q,k}=T_q(theta_{q,k}).                          (6)
```

Combining (2) and (6):

> **q-layer threshold normal form.** For every source set `S`,
>
> ```text
> U_q(S)
> = sum_q sum_{k>=1}
>     min(
>       T_q(theta_{q,k}),
>       T^O_q(r_{q,k}-1;S)
>       + T^S_q(r_{q,k+1}-1;S)
>     ).                                                (7)
> ```

Every term is a one-dimensional tail count in cross degree `c`, plus the inverse rectangle statistic `r_{q,k}` from the selected-source histogram.

## 6. Current Murty cap specialisation

In the current post-pair Murty model,

```text
P_w=min(
  rho_w+b-a-1,
  b-1-q_w,
  rho_w+lambda(q_w,E,z)   [when applicable],
  d_K(w)-q_w
).
```

Hence for `q_w=q`, the condition `P_w>=k` is equivalent to all applicable inequalities

```text
q<=b-1-k,                                              (8)
rho_w>=k+a-b+1,                                       (9)
rho_w>=k-lambda(q,E,z)  [when that cap is present],  (10)
d_K(w)>=q+k.                                         (11)
```

Since `rho=c-q`, the first three conditions are explicit lower thresholds on `c`.

For the potential-pair term, fixed-q potential degree is nondecreasing in `c`. In the positive-surplus source universe (`c>=q`), the closed form is

```text
d_K(q,c)
 = #{v : c_v>=q-1 and q_v<=c+1}
   -1
   -#{v : c_v=q-1 and q_v=c+1}.                       (12)
```

Define

```text
kappa_{q,k}
 = min{c>=q : d_K(q,c)>=q+k}.                          (13)
```

Then the cap threshold in (5) is the maximum of the applicable c-thresholds from (9)-(11), subject to the gate (8). Thus `alpha` is also a direct histogram tail count.

This makes the exact q-stratified minimum problem depend only on:

```text
global (q,c) histogram,
cap thresholds theta_{q,k},
selected-source rectangle counts R_S(q,t),
selected/unselected target c-tails,
source demand sum D(S).
```

No max-flow variable survives.

## 7. Combination with q-stratified minimum-cut exactness

[`Q_STRATIFIED_MINCUT_EXACTNESS.md`](Q_STRATIFIED_MINCUT_EXACTNESS.md) proves

```text
min_S [H(S)-D(S)]
=
min_S [U_q(S)-D(S)].                                  (14)
```

[`Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md`](Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md) further permits the minimization on the right to be restricted to unions of complete `(q,c,P)` types.

Therefore exact target-Hall failure is equivalent to the existence of a type-complete source set `S` for which the purely threshold-count expression

```text
sum_q sum_k
 min(
   T_q(theta_{q,k}),
   T^O_q(r_{q,k}-1;S)+T^S_q(r_{q,k+1}-1;S)
 )
-
sum_{u in S}q_u                                       (15)
```

is negative.

This is the current preferred all-order target.

## 8. Verification

A separately written verifier compares the direct q-layer definition against (7).

Frozen local verification totals:

```text
exhaustive labelled profiles: 46,800
exhaustive source sets:       666,600
q values:                     0,1
c values:                     q..2
P values:                     0..2 with fixed-q monotonicity
random trials:                30,000
random maximum n:             10
result:                       PASS
```

The verifier computes `alpha` and `beta` directly from target capacities and actual incoming counts, and independently through the cap thresholds and source order statistics. It requires exact equality term-by-term and in the final q-layer sum.

## 9. Research consequence

The remaining hand-proof problem is no longer a target-flow problem and no longer a target-correlation problem. It is a histogram inequality:

```text
for every admissible type-complete S,
threshold receiver capacity >= selected demand.        (16)
```

The natural next attacks are:

1. lower-bound the cap tails `T_q(theta_{q,k})` from the residual and potential-pair budgets;
2. express the source thresholds `r_{q,k}` via `R_S(q,t)` and the source cap `q+rho<=a`;
3. pair the demand layer-cake identity for `D(S)` with the `(q,k)` receiver layers;
4. identify which threshold rectangles can be simultaneously sparse enough to violate (16).

## Trust boundary

Equations (1)-(7) are elementary consequences of directed compatibility, self-deletion and fixed-q cap monotonicity. The Murty specialisation additionally uses the current post-pair cap formula and the potential-pair degree theorem. The reduction is exact for the target-Hall relaxation; it does not prove graph realizability or the unrestricted Murty-Simon conjecture.
