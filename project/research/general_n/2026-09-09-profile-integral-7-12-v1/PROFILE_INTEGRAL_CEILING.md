# Intrinsic scalar ceiling of the current profile-integral route

9 September 2026. Strategic research note; **not a theorem statement and not needed by the 7/12 candidate proof**.

The strengthened 7/12 argument passes from the exact profile-integral inequality

\[
r\ge a\sum_i\Phi(s_i/a)-a/4,
\qquad
\Phi(x)=\int_0^x\sqrt{2x-y^2}\,dy,
\]

to a uniform scalar upper bound on

\[
g(x)=x-\Phi(x),\qquad 0\le x\le1.
\]

It is useful to know the best possible constant obtainable from this *scalar-uniform* reduction before investing further effort in polynomial minorants.

## Exact calculus reduction

Elementary integration gives

\[
\Phi(x)=\frac{x}{2}\sqrt{x(2-x)}+x\arcsin\sqrt{x/2}.
\]

Differentiating under the integral sign gives the simpler identity

\[
\Phi'(x)=\sqrt{x(2-x)}+\arcsin\sqrt{x/2}.
\]

Hence

\[
g'(x)=1-\sqrt{x(2-x)}-\arcsin\sqrt{x/2}.
\]

Write

\[
\theta=\arcsin\sqrt{x/2},\qquad 0\le\theta\le\pi/4.
\]

Then

\[
x=2\sin^2\theta,
\qquad
\sqrt{x(2-x)}=\sin2\theta,
\]

so a stationary point satisfies

\[
\boxed{\theta+\sin2\theta=1.}
\tag{C1}
\]

The left side is strictly increasing on `[0,pi/4]`, since its derivative is

\[
1+2\cos2\theta>0.
\]

Thus there is a unique interior stationary point, and it is the unique maximum of `g`. At (C1),

\[
g_{\max}=\sin^2\theta\,(1-\theta).
\tag{C2}
\]

High-precision numerical evaluation gives

```text
theta  ~= 0.35228845646087296396
x_max  ~= 0.23811434167182176710
g_max  ~= 0.07711470389152937783
```

These decimals are reconnaissance values, not exact certificates.

## Consequence for this proof architecture

If the only information retained from the profile is the uniform scalar inequality

\[
x-\Phi(x)\le M,
\]

then asymptotically the best possible surplus coefficient is

\[
t\lesssim \frac{M}{2}a^2.
\]

For a degree ratio `lambda=b/n`, the Turan-side surplus is asymptotically

\[
\left(\frac{\lambda-1/2}{1-\lambda}\right)^2a^2.
\]

Therefore the limiting degree ratio obtainable from this scalar-uniform route is

\[
\lambda_*=\frac{1/2+\sqrt{M/2}}{1+\sqrt{M/2}}.
\]

Using the numerical value in (C2) gives

```text
lambda_* ~= 0.5820657.
```

The clean 7/12 candidate threshold is

```text
7/12 = 0.5833333333...
```

so it is already relatively close to the intrinsic asymptotic ceiling of the present scalar-uniform profile-integral method.

## Strategic implication

Further sharpening of the elementary square-root minorant can improve 7/12 modestly, but **cannot by itself drive the degree threshold anywhere near 1/2**. A substantial advance must retain more joint profile information than the single constant `max_x(x-Phi(x))`.

This supports prioritising the current pairwise staircase / monotone-coupling programme, which retains the joint `(d,h)` and `(s,h)` distributions rather than collapsing them to a scalar loss.
