# N32, Delta=17, m=258: hand exclusion of the `3^14` demand profile

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate hand proof component. Independent mathematical review OPEN.** This note uses only the canonical selected/residual bridge and the equality case of threshold capacity. No LP or proof-critical computation is used.

## 1. Parameters

Take

\[
n=32,\qquad \Delta=b=17,\qquad a=n-1-\Delta=14,
\]

and suppose

\[
m=258.
\]

Relative to the complete-bipartite benchmark `b(a+1)=255`, the surplus is

\[
t=3.
\]

The fourteen-label hand theorem gives `Q<=23`, while the bridge gives

\[
Q\ge b+2t=23.
\]

Hence equality holds. One of the three possible equality demand profiles is

\[
s=(3,3,\ldots,3)=3^{14}.
\]

This note excludes that profile.

## 2. Equality fixes the residual tail

Here

\[
S=42,
\qquad W_2=W_3=42,
\]

and

\[
\gamma_2(42)=10,
\qquad
\gamma_3(42)=9.
\]

Since

\[
S\ge r+2t=r+6,
\]

we have `r<=36`. On the other hand residual activity and the tail identity give

\[
r=b+\sum_{h\ge2}z_h
\ge17+10+9=36.
\]

Therefore every inequality is equality:

\[
r=36,
\qquad z_2=10,
\qquad z_3=9,
\qquad z_h=0\ (h\ge4).
\]

Thus the seventeen residual source degrees are exactly

\[
3^9,\;2^1,\;1^7.
\tag{2.1}
\]

Let `Z` be the set of the nine residual-degree-three sources.

Every selected incidence has a label of demand three. Selected-incidence forcing therefore gives

\[
s_i=3\le\rho_u
\]

at every selected source `u`. Hence **all selected incidences originate in `Z`**. In particular the unique degree-two source and the seven degree-one sources have selected outdegree zero.

## 3. Exact threshold capacity at h=3

At threshold `h=3`,

\[
W_3=42,
\qquad z_3=9,
\qquad C_3(9)=42.
\]

Thus the threshold-capacity chain is exact.

Let

\[
J=\{u\in Z:q_u>3\},
\qquad j=|J|,
\qquad K=Z\setminus J.
\]

The scalar capacity bound is

\[
42\le (9-j)3+9j-\frac{j(j+1)}2\le42.
\]

Subtracting from 42 gives

\[
42-\left((9-j)3+9j-\frac{j(j+1)}2\right)
=\frac{(6-j)(5-j)}2.
\]

Hence

\[
j\in\{5,6\}.
\tag{3.1}
\]

Equality throughout the threshold-capacity proof has two consequences.

First, every source in `K` has exactly

\[
q_u=3.
\tag{3.2}
\]

Second, every selected missing pair sourced in `J` has its supplement again in `Z`, and the injective pair count is saturated. Therefore the arcs sourced in `J` use **every unordered pair inside `Z` incident with `J`**.

Their number is

\[
j(9-j)+\binom j2
=9j-\frac{j(j+1)}2,
\]

namely 30 when `j=5` and 33 when `j=6`.

Consequently every `J-K` pair is already oriented from its `J` endpoint. No selected pair sourced in `K` can use a supplement in `J`.

## 4. The remaining K sources have nowhere to send three arcs each

Take `u in K`. By (3.2), `q_u=3`.

For any selected pair `u->w`, supplement forcing gives

\[
\rho_w+q_w\ge q_u-1=2.
\tag{4.1}
\]

Outside `Z`, all selected outdegrees are zero. By (2.1), the seven residual-degree-one sources therefore have

\[
\rho_w+q_w=1
\]

and cannot be supplements of a `K` arc. The unique residual-degree-two source has value two and is the **only** possible supplement outside `Z`.

Inside `Z`, no `K` source can point to `J`, because all `J-K` unordered pairs were already used in the opposite orientation by the saturated `J` arcs. Thus the only unordered pairs available to source the arcs from `K` are

- pairs entirely inside `K`; and
- the one pair from each `K` source to the unique residual-degree-two source.

If `j=5`, then `|K|=4`. The total available pair capacity is therefore

\[
\binom42+4=10,
\]

but the four sources in `K` require

\[
4\cdot3=12
\]

outgoing selected pairs. Contradiction.

If `j=6`, then `|K|=3`. The available pair capacity is

\[
\binom32+3=6,
\]

while the required number is

\[
3\cdot3=9.
\]

Again a contradiction.

Hence the equality demand profile

\[
\boxed{s=3^{14}}
\]

cannot occur for `n=32, Delta=17, m=258`.
