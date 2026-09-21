# Selected-signature union rigidity

21 September 2026.

**Status:** candidate general lemma inside the inherited canonical
selected/residual bridge.  The proof is a direct set-containment/double-count;
the bridge itself retains its internal-review trust boundary.

## 1. Physical source signatures

For an `A`-label `i`, define

```text
X_i = {u in B : ui is a selected incidence},
Y_i = {u in B : i belongs to N_u=S_u disjoint-union R_u}.
```

Then

```text
|X_i|=x_i,
|Y_i|=x_i+R_i=C_i.
```

The raw A-side domination statement says that whenever `ui` is selected,

\[
N_F(i)\subseteq N_u.
\]

Therefore every edge `ij` of `F` gives the **directed signature
containments**

\[
X_i\subseteq Y_j,
\qquad
X_j\subseteq Y_i.
\tag{SU1}
\]

This information is lost by the full selected-incidence Hall theorem, which
checks eligibility one label at a time.

## 2. Union and overlap consequences

For every label `j`, (SU1) gives

\[
\boxed{\left|\bigcup_{i\in N_F(j)}X_i\right|\le C_j.}
\tag{SU2}
\]

In particular, for any two labels `i,k` with a common F-neighbour `j`,

\[
\boxed{|X_i\cap X_k|\ge x_i+x_k-C_j.}
\tag{SU3}
\]

The positive part may be taken on the right when used as a lower bound.

Define

\[
\lambda_{j,u}=|N_F(j)\cap S_u|.
\]

Its support in the `u` coordinate is contained in `Y_j`, and

\[
\sum_u\lambda_{j,u}=\sum_{i\in N_F(j)}x_i=:M_j.
\]

Cauchy--Schwarz therefore gives the exact second-moment inequality

\[
\sum_u\binom{\lambda_{j,u}}2
\ge
\frac12\left(\frac{M_j^2}{C_j}-M_j\right),
\tag{SU4}
\]

with the right side interpreted as zero when `C_j=0`.

Summing over `j` and double-counting yields the global signature/codegree
constraint

\[
\boxed{
\frac12\sum_j\left(\frac{M_j^2}{C_j}-M_j\right)
\le
\sum_u\sum_{\{i,k\}\subseteq S_u} c_F(i,k),
}
\tag{SU5}
\]

where `c_F(i,k)=|N_F(i) intersect N_F(k)|`.  Indeed both sides count, with the
appropriate inequality at each `j`, triples `(u,{i,k},j)` such that `u`
selects both `i,k` and `j` is a common F-neighbour.

This is a graph-realizability condition: it retains physical selected-source
identity and actual F-codegrees.  It is not implied by row/column Hall margins.

## 3. Consequence for the rational plateau

In the uniform plateau from `FULL_HALL_PLATEAU_OBSTRUCTION.md`, write

```text
x=1/4,
C=x+Phi,
gamma=sqrt(2x-x^2)=sqrt(7)/4.
```

At quadratic scale the symmetric margins are

```text
d_F(i)=C*a,
|X_i|=x*a,
gamma*a selected sources,
q_u=(x/gamma)*a on those sources.
```

Then (SU5) says that the average F-codegree of a pair of labels co-selected at
a high source is at least

\[
C\gamma a-o(a).
\tag{SU6}
\]

The exact coarse bounds already certified in the plateau package give

\[
C>27/64,
\qquad
\gamma>529/800,
\]

and hence

\[
\boxed{
\operatorname{avg}_{u,\{i,k\}\subseteq S_u}c_F(i,k)
>\frac{14283}{51200}a-o(a)
>0.2789a-o(a).
}
\tag{SU7}
\]

Since the plateau degree is only approximately `C*a = 0.422a`, co-selected
pairs must share asymptotically at least an approximately `gamma = 0.661`
fraction of an entire
F-neighbourhood on average.

## 4. Rigidity interpretation and next target

The abstract plateau survives Hall only by making its selected-source
signatures highly clustered.  Any graph-realizable survivor must now exhibit
one of two equivalent pathologies:

1. many large families `N_F(j)` whose selected signatures have union at most
   `C_j`; or
2. a positive-density collection of selected row-pairs with linear F-codegree.

This materially narrows the realizability question.  A closure theorem need
not attack arbitrary profile vectors: it is enough to show that D2C raw
criticality cannot support average co-selected-pair F-codegree as large as
`0.2789a` in the near-uniform plateau regime, or else classify the resulting
cluster geometry.  Balanced complete bipartite equality remains outside this
positive-demand plateau (`s_i=0`) and is not excluded.
