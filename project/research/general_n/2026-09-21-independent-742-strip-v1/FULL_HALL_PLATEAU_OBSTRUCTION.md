# A plateau surviving full selected-incidence Hall and pair orientation

21 September 2026.

**Status:** exact obstruction inside an asymptotic aggregated relaxation.  It is
not a graph construction and not a counterexample to Murty--Simon.  Its purpose
is to identify which newer realizability information can and cannot eliminate
the profile-integral barrier.

## 1. Rational plateau above the Turan requirement

Take the uniform demand height

\[
x=1/4,
\qquad
\Phi=\Phi(1/4),
\qquad
f=x-\Phi.
\]

The closed form is

\[
\Phi=\frac{\sqrt7}{32}
     +\frac14\arcsin\frac1{2\sqrt2}.
\]

The exact rational estimates

```text
sqrt(7) < 1323/500 = 2.646,
arcsin(1/(2sqrt(2))) < 181/500 = 0.362
```

give

\[
f>\frac14-\frac{1323}{16000}-\frac{181}{2000}
  =\frac{1229}{16000}
  =0.0768125.
\]

The arcsine estimate follows from its positive power series: use the first four
terms, bound every later coefficient by one, use
`1/(2sqrt(2))<177/500`, and sum the geometric tail in powers of `1/8`.

Set the source/label ratio

\[
\beta=b/a=139/100.
\]

The Turan-side required asymptotic surplus is

\[
\frac{(\beta-1)^2}{4}a^2=0.038025a^2,
\]

whereas the plateau permits

\[
t=\frac f2a^2>0.03840625a^2.
\]

Thus this profile lies genuinely on the counterexample side of the degree
assembly, not merely at a harmless below-Turan point.

## 2. Threshold-capacity saturation

Give all `a` labels demand `s_i=xa`.  At normalized threshold `y=h/a`, put

\[
z(y)=a\sqrt{2x-y^2}
\qquad(0<y\le x).
\]

Then

\[
z(y)^2+(ya)^2=2xa^2=2W_h,
\]

and

\[
\int_0^xz(y)a\,dy=a^2\Phi.
\]

So the threshold capacity and nested residual budget are both saturated to
leading order.  The extra `b-z(0+)` sources have residual degree `O(1)` and do
not change the quadratic-scale integral.

## 3. Full selected-incidence Hall also survives

At the top demand threshold let

\[
\gamma=\sqrt{2x-x^2}=\sqrt7/4.
\]

Use `gamma*a` high sources.  Give every label selected degree `xa`, and every
high source selected row degree

\[
q=\frac{x}{\gamma}a.
\]

All high sources are eligible for all labels at the aggregated level:

- `s_i<=rho_u` at the top interface;
- put incoming load `p=0` on high sources, so `g_u=0`;
- give each label residual degree `Phi*a`, hence endpoint mass
  `C_i=(x+Phi)a=(1/2-f)a`;
- the exact bounds below give `q<C_i`.

The complete high-source/label eligibility graph therefore admits the required
biregular selected-incidence matrix.  Equivalently, for every subset `S` of
high sources,

\[
\sum_{u\in S}q_u
\le\sum_i\min(xa,|S|),
\]

so the complete full selected-incidence Hall family holds, not only singleton
row packing or threshold projections.

## 4. Global orientation and pair uniqueness also survive

Put all incoming orientation load on the low-source pool of normalized size

\[
\ell=\beta-\gamma.
\]

Give every low source incoming degree

\[
p=\frac{x}{\ell}a
\]

and no selected outgoing degree.  The selected missing-pair orientation is then
a simple bipartite orientation from the high pool to the low pool.  It has
equal total out- and indegree `xa^2`, and distinct high--low pairs realize pair
uniqueness.

The following deliberately coarse exact bounds show positive margins:

```text
2.645 < sqrt(7) < 2.646,
0.66125 < gamma < 0.6615,
ell > 0.7285,
q/a < 100/264.5 < 0.379,
p/a < 0.25/0.7285 < 0.344,
C_i/a = 1/2-f > 27/64 = 0.421875,
beta-1 = 0.39.
```

Hence `q<C_i`, `p<beta-1`, `q<ell`, `p<gamma`, and
`x+q/a<1`.  These are exactly the margins needed for endpoint eligibility,
the local incoming cap on the low pool, a simple high--low orientation graph,
and disjoint selected/residual rows at the aggregated matrix level.

The residual row-tail sequence is also compatible with uniform residual
column degree `Phi*a`: for normalized `k`, Gale--Ryser reduces to

\[
k\Phi\le\int_0^k z(y)\,dy,
\]

which holds because `z` is decreasing, supported in `[0,x]`, and its total
integral is `Phi` (the prefix average dominates the whole-interval average).

There is also enough room to realize the selected and residual matrices
**disjointly**, so separate graphicality is not hiding an immediate collision.
All `gamma*a` top sources have residual row degree `x*a`.  Their normalized
residual mass per label is `gamma*x`, while their selected mass per label is
`x`.  The certified bounds give

```text
x+gamma*x < 1/4 + (2646/4000)/4 < 0.416 < gamma,
Phi-gamma*x > (1/4-5/64) - (2646/4000)/4 > 0.006.
```

Thus on the high-source/label complete bipartite graph one may take two
edge-disjoint biregular layers, of row degrees `q*a` and `x*a`, using disjoint
cyclic offset sets after a rational blow-up.  The remaining positive residual
column mass `Phi-gamma*x` is supplied by the low-source tail, which has no
selected A-incidences.  Every row and column retains a fixed positive unused
margin.  Rational approximations to `gamma,Phi` then realize the continuum
system with `o(a^2)` rounding.

## 5. Consequence for the live proof search

The uniform plateau is not eliminated by any combination of:

1. the exact threshold-capacity family;
2. the nested residual budget;
3. graphical residual row/column degrees;
4. simultaneous disjoint selected/residual incidence margins;
5. the full selected-incidence Hall inequalities;
6. endpoint eligibility `C_i>=p_u+q_u`;
7. global orientation balance; or
8. uniqueness of the unordered source--supplement pair.

Therefore applying full Hall as a black-box capacity constraint cannot close
the `1/2`--`7/12` strip.  The first missing information is genuinely joint:
the same physical residual sets must simultaneously contain the appropriate
`F`-neighbourhoods for every selected incidence, while the oriented supplement
pairs must arise from raw criticality.  A successful next theorem must couple
those set inclusions across many nearly identical label demands; another
one-dimensional threshold sum cannot suffice.
