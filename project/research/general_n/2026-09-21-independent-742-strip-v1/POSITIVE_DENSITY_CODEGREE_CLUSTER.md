# Positive-density codegree cluster forced by a plateau survivor

21 September 2026.

**Status:** candidate quantitative consequence of the robust signature theorem,
within the inherited canonical bridge and the corrected joint plateau
hypotheses below.  The hypothesis list was narrowed by the 22 September audit.

## Statement (corrected audit scope)

Retain the exact rational plateau normalization, or a profile band satisfying
all of these hypotheses simultaneously:

```text
lambda=1,
x_i>=x*a for every endpoint used below, with x=1/4,
d_F(i)>=d*a where d=27/64,
d_F(i), C_i<=c*a with c=6771/16000,
Q=sum_u q_u satisfies x*a^2<=Q<=X*a^2 with x=X=1/4,
beta=b/a<=139/100,
```

Thus the selected-mass bounds force `Q=a^2/4` in this normalization.  The
original statement listed only `Q>=a^2/4` and omitted the lower-degree and
selected-endpoint assumptions.  Robust stability uses the upper bound on `Q`,
while the convexity step below uses the lower bound.  The correction narrows
the theorem to the hypotheses actually used; none of the arithmetic changes.

Let a **selected pair occurrence** be a triple `(u,{i,k})` with
`{i,k} subset S_u`.  The endpoint-cap version of robust signature stability
gives weighted average F-codegree at least

\[
\kappa a-K,
\qquad
\kappa=\frac{1265625}{5094049},
\quad
K=\frac{2250}{2257}.
\]

Call an occurrence **high-codegree** when

\[
c_F(i,k)\ge a/5.
\]

Since every pair has codegree at most `c*a`, if `H` is the number of high
occurrences and `D=sum_u binom(q_u,2)` is the total number of occurrences, then

\[
(\kappa a-K)D
\le Hca+(D-H)a/5.
\]

Therefore

\[
\boxed{
\frac HD\ge
\frac{(\kappa-1/5)a-K}{(c-1/5)a}.
}
\tag{PC1}

For `a>=21` this is positive, and asymptotically

\[
\frac HD\ge
\frac{3949043200}{18190848979}-o(1)
>0.2170-o(1).
\tag{PC2}

Thus more than 21.7% of all selected pair occurrences must have at least
`a/5` common F-neighbours.

## There are quadratically many distinct high-codegree pairs

Convexity of row degrees gives

\[
D=\sum_u\binom{q_u}{2}
\ge\frac{Q^2}{2b}-\frac Q2
\ge\frac{25}{1112}a^3-\frac18a^2
\tag{PC3}

for the stated normalization (the right side is increasing in `Q` once
`a>=3`).
Each unordered label pair can occur at no more than `b<=beta*a` physical
sources.  Combining (PC1)--(PC3), the number of **distinct** pairs with
`c_F(i,k)>=a/5` is at least

\[
\left(
\frac{1234076000000}{351465393123259}-o(1)
\right)a^2
> (0.00351-o(1))a^2.
\tag{PC4}

This converts an average constraint into a positive-density structural object:
an actual plateau survivor contains quadratically many pairs with linear
F-codegree, and those pairs are repeatedly co-selected by physical sources.

## Next closure target

The live problem is now finite-dimensional at density scale.  Either raw D2C
criticality forbids a positive density of pairs having simultaneously

1. at least `a/5` common F-neighbours, and
2. a common selected physical source,

or those pairs organize into a bounded cluster/blow-up geometry.  The latter
can be classified against the source/supplement pair injection.  Another
scalar profile inequality cannot see (PC4).
