# Exact q-stratified crossing-gap identity

14 September 2026. **Candidate exact structural theorem inside the current post-pair target-Hall model. External mathematical review and novelty assessment remain OPEN.**

The global receiver-layer rearrangement forgets all target identity. Splitting targets by `q` is much sharper. This note identifies **exactly** what information is still lost after that split.

The loss is not a general high-dimensional correlation term. It is a count of one specific self-deletion/saturation crossing inside equal-`q`, equal-preincoming blocks.

## 1. Setup

Fix an arbitrary labelled Hall source set `S`. For each labelled target copy `w`, write

```text
q_w = target demand parameter,
c_w = q_w + rho_w,
P_w = current post-pair target cap,
epsilon_w = 1_{w in S}.
```

Before deleting the forbidden diagonal, define

```text
m_w(S)
 = #{u in S : q_u <= c_w+1 and q_w <= c_u}.             (1)
```

The actual compatible selected-source count is

```text
y_w(S) = m_w(S) - epsilon_w.                            (2)
```

The exact receiver capacity of `S` is

```text
H(S) = sum_w min(P_w,y_w).                              (3)
```

For each `q`, form the multiset of target caps `P_w` and incoming counts `y_w` over target copies with `q_w=q`. Sort the two multisets in the same order and pair them comonotonically. Let the resulting q-stratified rearrangement upper bound be

```text
U_q(S).                                                  (4)
```

Equivalently, if

```text
alpha_{q,k}=#{w:q_w=q, P_w>=k},
beta_{q,k} =#{w:q_w=q, y_w>=k},
```

then

```text
U_q(S)=sum_q sum_{k>=1} min(alpha_{q,k},beta_{q,k}).     (5)
```

Always

```text
H(S) <= U_q(S) <= U_global(S).                          (6)
```

The second inequality is immediate because splitting a rearrangement problem into strata can only reduce its maximum overlap.

## 2. Fixed-q comonotonicity before diagonal deletion

In the current post-pair cap model, at fixed `q`, increasing `c` makes `P` nondecreasing. This is the fixed-q target-cap monotonicity already used in [`Q_SELECTED_STRATIFIED_RECEIVER_EXACTNESS.md`](Q_SELECTED_STRATIFIED_RECEIVER_EXACTNESS.md).

For an arbitrary fixed source set `S`, `m_w(S)` is also nondecreasing with `c_w` at fixed `q_w=q`: the condition

```text
q_u <= c_w+1
```

only becomes easier as `c_w` increases, while the other condition `q_w<=c_u` is unchanged.

Therefore, within each fixed-q stratum, target copies may be ordered by increasing `c` so that both

```text
P_1 <= P_2 <= ...,
m_1 <= m_2 <= ...                                      (7)
```

hold simultaneously.

The only possible failure of comonotonicity for the **actual** incoming counts

```text
y_i=m_i-epsilon_i                                      (8)
```

comes from the one-unit self-deletion term.

Because the `m_i` are integers, if `m_i<m_j` for `i<j`, then

```text
y_i <= m_i <= m_j-1 <= y_j.                            (9)
```

Thus sorting the `y_i` can only reorder copies **inside blocks having the same pre-diagonal incoming value `m`**.

## 3. The crossing statistic

For each pair `(q,m)`, let

```text
B_{q,m}={w:q_w=q, m_w=m}.                               (10)
```

Inside `B_{q,m}`, define

```text
H^S_{q,m}
 = #{w in B_{q,m}: epsilon_w=1 and P_w>=m},             (11)

L^O_{q,m}
 = #{w in B_{q,m}: epsilon_w=0 and P_w<=m-1}.           (12)
```

These are, respectively:

- selected targets whose cap is high enough to benefit from an incoming value `m`, but which receive only `m-1` after self-deletion;
- unselected targets whose cap is too low to benefit from their incoming value `m`.

Define the total q-crossing count

```text
C_q(S)
 = sum_{q,m} min(H^S_{q,m},L^O_{q,m}).                  (13)
```

## 4. Exact identity

> **q-stratified crossing-gap theorem.** In the current post-pair target-cap model, for every labelled source set `S`,
>
> ```text
> U_q(S) - H(S) = C_q(S).                               (14)
> ```

### Proof inside one `(q,m)` block

All copies in the block have actual incoming value

```text
m-1  if selected,
m    if unselected.                                    (15)
```

Let `u` be the number of unselected copies and let

```text
H = #{w in B_{q,m}:P_w>=m}.                             (16)
```

Write every target contribution with the common base

```text
min(P_w,m-1).                                           (17)
```

Assigning incoming value `m` rather than `m-1` adds exactly one further unit iff `P_w>=m`.

In the exact assignment, the `u` copies receiving value `m` are precisely the unselected copies. Hence the exact bonus is

```text
H^O_{q,m}
 = #{unselected w:P_w>=m}.                              (18)
```

In the q-stratified comonotone rearrangement, the `u` copies receiving value `m` are paired with the `u` largest target caps. The rearranged bonus is therefore

```text
min(u,H).                                               (19)
```

So the block gap is

```text
min(u,H)-H^O_{q,m}.                                     (20)
```

Now

```text
H = H^O_{q,m}+H^S_{q,m},
u = H^O_{q,m}+L^O_{q,m}.                                     (21)
```

Substitution gives

```text
min(u,H)-H^O_{q,m}
 = min(H^S_{q,m},L^O_{q,m}).                            (22)
```

By (9), different `m` blocks never need to cross when the incoming sequence is sorted. Summing (22) over all `(q,m)` proves (14).

## 5. Consequences

The q-stratified receiver formula is exact **iff**

```text
C_q(S)=0.                                               (23)
```

Equivalently, every equal-`q`, equal-preincoming block avoids the simultaneous presence of

```text
selected target with P>=m
and
unselected target with P<m.                             (24)
```

For a deficient Hall witness of demand `D(S)`, the q-stratified upper bound fails to detect the obstruction exactly when

```text
C_q(S) >= D(S)-H(S).                                    (25)
```

Thus the entire target-correlation problem beyond q-stratified layers has collapsed to a single explicit integer statistic `C_q`.

This is the smallest missing statistic sought after the global receiver-layer pilot: no arbitrary target matching remains.

## 6. Relation to the selected-bit stratification theorem

[`Q_SELECTED_STRATIFIED_RECEIVER_EXACTNESS.md`](Q_SELECTED_STRATIFIED_RECEIVER_EXACTNESS.md) obtains exactness by splitting each q-stratum according to `epsilon` before rearrangement.

Equation (14) quantifies exactly why that split is sufficient and exactly how much is lost if it is omitted. The only obstruction is the one-unit diagonal deletion crossing described by (11)-(13).

## 7. Important nonclaim

This theorem does **not** say that q-only stratification is always exact. Mixed selected/unselected saturation crossings can occur, and then `C_q>0`.

A preserved counterexample should therefore accompany any use of the theorem. The Murty-specific task is not to assert `C_q=0` abstractly, but to bound or exclude `C_q` using the bridge, residual/excess budgets, canonical maximality, and the earlier relational constraints.

## 8. Trust boundary

The identity uses the fixed-q monotonicity of the **current post-pair target cap** `P` and the exact directed numerical compatibility relation. It is exact within that target-Hall model once those ingredients are accepted.

It does not assert graph realizability, does not by itself exclude any whole scalar state, and does not prove the unrestricted Murty-Simon conjecture. External mathematical review and genuinely independent reproduction remain open.
