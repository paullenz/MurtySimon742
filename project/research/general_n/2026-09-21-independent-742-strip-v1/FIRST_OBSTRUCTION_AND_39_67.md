# First profile obstruction and a `39/67` threshold improvement

21 September 2026.

**Status:** internally derived candidate mathematics.  The rational certificate is
exactly checkable, but the inherited graph-to-profile lemma remains at the same
candidate/internal-review trust level as the `7/12` package.

The scalar ceiling and its stationary-point calculation were already preserved
in `2026-09-09-profile-integral-7-12-v1/PROFILE_INTEGRAL_CEILING.md`; Section 2
independently rederives that boundary for continuity.  The new work here is the
exact `121/1569` certificate, the threshold/order ladder, and the subsequent
graph-realizability obstruction/rigidity analysis in this package.

## 1. Inherited ledger

Use the notation of the canonical profile-integral proof:

```text
a = n-1-b,  b = Delta(G),  t = e(G)-b(n-b).
```

The graph-derived profile inequalities give

\[
r\ge a\sum_{i=1}^a\Phi(s_i/a)-a/4,
\qquad
2t\le S-r,
\]

where `S=sum_i s_i` and

\[
\Phi(x)=\int_0^x\sqrt{2x-y^2}\,dy.
\]

Thus any uniform upper bound on

\[
f(x):=x-\Phi(x)
\]

immediately gives a universal surplus bound.

## 2. Exact first scalar obstruction

The closed form and derivatives are

\[
\Phi(x)=\frac{x}{2}\sqrt{x(2-x)}
        +x\arcsin\sqrt{x/2},
\]

\[
f'(x)=1-\sqrt{x(2-x)}-\arcsin\sqrt{x/2},
\qquad
f''(x)=-\frac{3/2-x}{\sqrt{x(2-x)}}<0
\]

for `0<x<=1`.  Hence `f` has a unique interior maximizer `xi`, determined by

\[
\sqrt{\xi(2-\xi)}+\arcsin\sqrt{\xi/2}=1.
\]

Numerically (diagnostic only),

```text
xi = 0.2381143384...
M  = f(xi) = 0.07711470389...
```

This is not merely a loose pointwise artifact.  At continuum scale the uniform
demand profile

```text
s_i = xi*a for every label i,
z(eta) = a*sqrt(2*xi-eta^2),  0 <= eta <= xi,
r = a^2*Phi(xi)
```

saturates the Cauchy/threshold inequality and the nested source budget to
leading order:

\[
z(\eta)^2+(\eta a)^2=2\xi a^2=2W_{\eta a},
\qquad
\int_0^\xi z(\eta)a\,d\eta=a^2\Phi(\xi).
\]

The remaining exact ledger is scalar-compatible: take total residual label
degree `sum R_i=r`, total demand `S=xi*a^2`, and
`t=(S-r)/2`.  Average `d_i=s_i+R_i` is
`(xi+Phi(xi))*a<a`, so even the elementary degree ceiling does not eliminate
the profile.

Consequently the decoupled scalar/profile argument alone cannot approach
`b/n=1/2`.  Its limiting ratio is

\[
\alpha_*=
\frac{1/2+\sqrt{M/2}}{1+\sqrt{M/2}}
=0.5820656900\ldots.
\]

Any further movement below `alpha_*` must use a graph-realizability condition
that couples the nearly uniform demand plateau to physical sources, selected
incidences, or the residual graph.  This is the exact first obstruction to the
requested push toward `1/2`.

## 3. Rational sharpening of the scalar certificate

The canonical square-root minorant gives

\[
f(x)\le P(q),\qquad q=\sqrt{x/2},
\]

\[
P(q)=2q^2-4q^3+\frac23q^5+\frac1{10}q^7+\frac3{56}q^9.
\]

Write `P'(q)=qQ(q)`, where

\[
Q(q)=4-12q+\frac{10}{3}q^3+\frac7{10}q^5+\frac{27}{56}q^7.
\]

On `0<=q<=1/sqrt(2)`,

\[
Q'(q)\le-12+5+7/8+27/64=-365/64<0.
\]

Set

```text
l = 345053/1000000,
u = 345054/1000000.
```

Exact rational arithmetic gives `Q(l)>0>Q(u)`.  Therefore the unique maximum
of `P` lies in `[l,u]`.  On that interval, monotonicity of the monomials gives

\[
P(q)\le
2u^2-4l^3+\frac23u^5+\frac1{10}u^7+\frac3{56}u^9
<\frac{121}{1569}.
\]

Hence

\[
\boxed{t<\frac{121}{3138}a^2+\frac a8.}
\tag{S39}
\]

## 4. Degree assembly

Assume `b>=39n/67`.  Since `n=a+b+1`,

\[
28b\ge39(a+1),
\qquad
b-n/2=\frac{b-a-1}{2}\ge\frac{11(a+1)}{56}.
\]

If `e(G)>=floor(n^2/4)`, parity gives

\[
t\ge\left\lfloor\frac{(b-a-1)^2}{4}\right\rfloor
\ge\frac{121(a+1)^2}{3136}-\frac14.
\]

Subtracting (S39), define

\[
D(a)=\frac{121(a+1)^2}{3136}-\frac14
     -\frac{121a^2}{3138}-\frac a8.
\]

Exact arithmetic gives

```text
D(1949) = -26669/1230096,
D(1950) = 43251/1640128 > 0,
D(1951)-D(1950) = 236671/4920384 > 0.
```

The quadratic coefficient of `D` is positive, so all later forward
differences increase.  Thus `D(a)>0` for every integer `a>=1950`.

Combine this with the preserved `7/12` candidate.  If `n>=4681` and
`b>=39n/67`, either `b>=7n/12`, already closed by that candidate, or
`b<7n/12`, in which case

\[
a=n-1-b>5n/12-1>1949,
\]

so `a>=1950` and the preceding contradiction applies.

Therefore, at the inherited candidate trust level,

\[
\boxed{
n\ge4681,\quad \Delta(G)\ge\frac{39}{67}n
\quad\Longrightarrow\quad
e(G)<\left\lfloor\frac{n^2}{4}\right\rfloor .
}
\]

This is a strict threshold improvement because
`39/67 = 0.58208955... < 7/12 = 0.58333333...`.

### A threshold/order tradeoff ladder

The same calculation gives more practical corollaries.  For a rational
threshold `alpha=p/q`, put

\[
\eta(\alpha)=\frac{2p-q}{2(q-p)}.
\]

If `eta(alpha)^2>121/3138`, define

\[
D_\alpha(a)=\eta(\alpha)^2(a+1)^2-\frac14
             -\frac{121a^2}{3138}-\frac a8.
\]

Once `D_alpha(A)>0` and its forward difference is positive, convexity closes
all `a>=A`.  Combining below `7/12` as above needs only
`n>12A/5`.  Exact arithmetic gives:

| improved threshold | decimal | first `A` | sufficient `n` |
|---:|---:|---:|---:|
| `116/199` | 0.58291457... | 53 | 128 |
| `88/151` | 0.58278146... | 62 | 149 |
| `46/79` | 0.58227848... | 204 | 490 |
| `85/146` | 0.58219178... | 346 | 831 |
| `39/67` | 0.58208955... | 1950 | 4681 |

Thus the first focused session yields both a near-ceiling asymptotic
improvement and a smaller-order usable form, for example

\[
n\ge149,\quad\Delta(G)\ge\frac{88}{151}n
\Longrightarrow e(G)<\lfloor n^2/4\rfloor.
\]

All rows retain the inherited candidate trust boundary.

## 5. What remains graph-theoretic

The new threshold is still bounded below by the uniform plateau obstruction.
The next high-value question is therefore not another scalar Taylor
coefficient.  It is whether a near-uniform demand plateau can be realized by
the raw selected quasi-edge system of an actual D2C graph.  A useful rigidity
theorem would show that near-saturation of the threshold capacity forces a
design-like source geometry, then compare that geometry with physical-source
injectivity and residual graph degrees.
