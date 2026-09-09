---
title: "A strengthened profile-integral maximum-degree bound for diameter-2 edge-critical graphs"
subtitle: "Reviewer edition 1 - current strongest profile-integral candidate"
author: "Paul Lenz research project; mathematical development and drafting with ChatGPT/Geeps"
date: "9 September 2026"
documentclass: article
fontsize: 11pt
geometry: [a4paper, margin=25mm]
colorlinks: true
linkcolor: "black"
urlcolor: "blue"
---

\begin{abstract}
We present a strengthened candidate profile-integral argument. A sharper elementary square-root minorant improves the universal surplus estimate, and an exact finite threshold certificate completes the degree assembly at the rational threshold 7/12. Two separately written standard-library checkers agree on the scalar arithmetic and every finite exception. The argument remains candidate mathematics: independent specialist review, novelty assessment and external computational reproduction are open.
\end{abstract}

**Reviewer status.** complete candidate hand argument; internal exact audits green; independent review and novelty assessment OPEN. This reviewer edition is an editorial rendering of the canonical source proof listed below. It does not convert same-assistant checking into external independence, does not make a novelty or priority claim, and does not claim the unrestricted Murty-Simon conjecture unless the source proof itself proves such a statement.

**Canonical claim.** `n >= 6 and Delta(G) >= (7/12)n imply e(G) < floor(n^2/4)`.

**Canonical proof source.** `project/research/general_n/2026-09-09-profile-integral-7-12-v1/PROOF.md`. The source is reproduced in full below; substantive mathematical changes must be made in the canonical proof first and then rebuilt into this edition.

---

# A strengthened profile-integral bound and a 7/12 maximum-degree candidate

9 September 2026. Paul Lenz: research direction. ChatGPT/Geeps: derivation, drafting and internal checking.

**Status: complete candidate hand proof; internal exact audits green. Independent mathematical review, novelty assessment and external computational reproduction remain OPEN. This is not an unrestricted solution of Murty–Simon.**

## Statement

Let `G` be a finite simple diameter-two edge-critical graph on `n>=6` vertices, with `m` edges and maximum degree `b`. Put

```text
a = n-1-b,
t = m-b(n-b).
```

The argument proves the strengthened universal surplus bound

\[
\boxed{t<\frac{5a^2}{128}+\frac a8.}
\tag{P+}
\]

Together with an exact finite threshold certificate, it gives the candidate implication

\[
\boxed{b\ge \frac{7}{12}n\quad\Longrightarrow\quad m<\left\lfloor\frac{n^2}{4}\right\rfloor.}
\tag{T+}
\]

The proof uses the same graph-to-demand and exact threshold-capacity lemmas as the earlier `293/500` profile-integral candidate. The new mathematical ingredient is a sharper elementary scalar estimate; no new graph bridge is assumed.

## 1. Shared graph-to-profile lemma

Let `H` be the complement of `G`. Choose a minimum-degree vertex `v` of `H`, put

```text
A=N_H(v), |A|=a,
B=V(H)\N_H[v], |B|=b.
```

Use the selected quasi-edge construction for missing pairs of `H[B]`, with residual source degrees `rho_u`, residual label degrees `R_i`, selected label degrees `x_i`, and common residual total `r`. Let `F` be the complement of `H[A]`, with `d_i=deg_F(i)`, and define

\[
s_i=\max(0,d_i-R_i),\qquad S=\sum_i s_i.
\]

The established exact ledger and minimum-degree argument give

\[
e(F)=r+t,\qquad \sum_i d_i=2(r+t),\qquad S\ge r+2t.
\tag{1}
\]

For a selected incidence from source `u` to label `i`, the quasi-edge covering argument gives

\[
s_i\le \rho_u.
\tag{2}
\]

For each integer `h>=1`, define

\[
I_h=\{i:s_i\ge h\},\quad W_h=\sum_{i\in I_h}s_i,
\]

\[
Z_h=\{u:\rho_u\ge h\},\quad z_h=|Z_h|.
\]

Counting selected orientations and their supplements gives the exact threshold-capacity inequality

\[
2W_h\le z_h^2-z_h+h(h+1).
\tag{3}
\]

If `H0=max_i s_i>0`, then a label of demand `H0` needs `H0` distinct sources of residual degree at least `H0`, and the nested source sets satisfy

\[
z_h\ge H0\ge h\quad(1\le h\le H0),
\qquad
\sum_{h=1}^{H0}z_h\le r.
\tag{4}
\]

These are graph-derived necessary conditions, not empirical observations.

## 2. The profile integral

For `h<=H0`, let `ell=|I_h|` and `p=ell/a`. Cauchy--Schwarz gives

\[
\left[\frac1a\sum_{i\in I_h}\sqrt{2as_i-h^2}\right]^2
\le 2pW_h-p^2h^2.
\]

Using (3), `0<=p<=1`, and `z_h>=h`,

\[
2pW_h-p^2h^2
\le pz_h^2+p(1-p)h^2
\le z_h^2.
\]

Hence

\[
z_h\ge \frac1a\sum_{i:s_i\ge h}\sqrt{2as_i-h^2}.
\tag{5}
\]

Summing over `h` and using (4),

\[
r\ge \frac1a\sum_i D_a(s_i),
\qquad
D_a(s)=\sum_{h=1}^s\sqrt{2as-h^2}.
\tag{6}
\]

Define

\[
\Phi(x)=\int_0^x\sqrt{2x-y^2}\,dy,
\qquad 0\le x\le1.
\]

The shifted-midpoint concavity argument from the profile-integral proof gives, for every integer `0<=s<=a-1`,

\[
D_a(s)\ge a^2\Phi(s/a)-a/4.
\tag{7}
\]

For completeness, if `s>0`, put `f(y)=sqrt(2as-y^2)`. On `[0,s+1/2]` it is decreasing and concave; midpoint concavity gives

\[
\sum_{h=1}^sf(h)\ge\int_{1/2}^{s+1/2}f(y)\,dy.
\]

The difference from the integral over `[0,s]` is at most

\[
\frac{f(0)-f(s+1/2)}2
\le \frac{\sqrt{2as}-s}{2}\le a/4,
\]

because `(s+a/2)^2>=2as`. Rescaling the integral gives (7).

Combining (6) and (7),

\[
r\ge a\sum_i\Phi(s_i/a)-a/4.
\tag{8}
\]

Everything from (1) through (8) is shared with the previous profile-integral route.

## 3. Sharper scalar estimate

We now prove

\[
\boxed{x-\Phi(x)<\frac5{64}\qquad(0\le x\le1).}
\tag{9}
\]

### 3.1 A sharper square-root minorant on the actual domain

For `0<=u<=1/2`, put

\[
B(u)=1-\frac u2-\frac{u^2}{8}-\frac{3u^3}{32}.
\]

Direct expansion gives

\[
1-u-B(u)^2
=
\frac{u^3}{1024}\left(64-112u-24u^2-9u^3\right).
\tag{10}
\]

Both `B(u)` and the cubic in parentheses are decreasing on `[0,1/2]`, while

\[
B(1/2)=181/256>0,
\]

\[
64-112(1/2)-24(1/2)^2-9(1/2)^3=7/8>0.
\]

Therefore `B(u)>=0` and `B(u)^2<=1-u`, so

\[
\sqrt{1-u}\ge B(u)\qquad(0\le u\le1/2).
\tag{11}
\]

For `x>0`, in the integral for `Phi(x)` take

\[
u=y^2/(2x).
\]

Since `0<=y<=x<=1`, one has `0<=u<=x/2<=1/2`; this restricted range is what allows the improvement over the previous `1/12` estimate. Integrating (11) gives

\[
\Phi(x)
\ge
\sqrt{2x}\left(
 x-\frac{x^2}{12}-\frac{x^3}{160}-\frac{3x^4}{1792}
\right).
\tag{12}
\]

### 3.2 Exact polynomial bound

Put

\[
q=\sqrt{x/2},\qquad 0\le q\le1/\sqrt2.
\]

Then (12) gives

\[
x-\Phi(x)\le P(q),
\]

where

\[
P(q)=2q^2-4q^3+\frac23q^5+\frac1{10}q^7+\frac3{56}q^9.
\tag{13}
\]

Write

\[
P'(q)=qQ(q),
\]

\[
Q(q)=4-12q+\frac{10}{3}q^3+\frac7{10}q^5+\frac{27}{56}q^7.
\]

On `0<=q<=1/3`, `Q(q)>=4-12q>=0`, so `P` is increasing.

On `7/20<=q<=1/sqrt2`,

\[
Q'(q)
=-12+10q^2+\frac72q^4+\frac{27}{8}q^6
\le -\frac{365}{64}<0.
\]

Moreover exact arithmetic gives

\[
Q(7/20)=-\frac{1631127391}{30720000000}<0.
\]

Thus `P` is decreasing from `7/20` onward.

It remains only the short interval `1/3<=q<=7/20`. There

\[
2q^2-4q^3\le 2/27
\]

because this cubic is decreasing for `q>=1/3`, while the positive tail is increasing and

\[
\frac23(7/20)^5+\frac1{10}(7/20)^7+\frac3{56}(7/20)^9
=
\frac{43868404489}{12288000000000}
<\frac1{250}.
\]

Consequently, throughout all three intervals,

\[
P(q)<\frac2{27}+\frac1{250}<\frac5{64},
\]

with exact margin

\[
\frac5{64}-\left(\frac2{27}+\frac1{250}\right)=\frac{11}{216000}>0.
\]

This proves (9), including `x=0` directly.

## 4. Strengthened universal surplus bound

Apply (9) to every `s_i/a` in (8):

\[
r
>
S-\frac{5a^2}{64}-\frac a4.
\]

Since (1) gives `2t<=S-r`,

\[
2t<\frac{5a^2}{64}+\frac a4,
\]

hence

\[
\boxed{t<\frac{5a^2}{128}+\frac a8.}
\]

This proves (P+).

## 5. Degree assembly for 7/12

Assume now

\[
b\ge 7n/12,
\qquad n=a+b+1.
\]

Then

\[
5b\ge7(a+1),
\]

so

\[
b-n/2=\frac{b-a-1}{2}\ge\frac{a+1}{5}.
\tag{14}
\]

If, contrary to (T+),

\[
m\ge\lfloor n^2/4\rfloor,
\]

then

\[
t\ge\lfloor n^2/4\rfloor-b(n-b)
=\left\lfloor\frac{(b-a-1)^2}{4}\right\rfloor
\ge (b-n/2)^2-1/4.
\]

Using (14),

\[
t\ge \frac{(a+1)^2}{25}-\frac14.
\tag{15}
\]

Subtracting the upper bound (P+) from the right side of (15) gives

```text
D(a) = (a+1)^2/25 - 1/4 - 5a^2/128 - a/8.
```

Its quadratic coefficient is

\[
\frac1{25}-\frac5{128}=\frac3{3200}>0.
\]

Exact arithmetic gives

\[
D(53)=123/3200>0,
\]

and

\[
D(54)-D(53)=177/3200>0.
\]

Subsequent forward differences increase by `6/3200`. Hence `D(a)>0` for every integer `a>=53`, contradicting (P+).

## 6. Exact finite assembly for a<=52

For fixed `a`, the least integer `b` satisfying the degree premise is

\[
b_0=\left\lceil\frac{7(a+1)}5\right\rceil.
\]

Since `b_0>a+1`, the required surplus

\[
T_0=\left\lfloor\frac{(b_0-a-1)^2}{4}\right\rfloor
\]

is nondecreasing for larger eligible `b`.

For `2<=a<=52`, the strict bound (P+) immediately contradicts `t>=T_0` whenever

\[
128T_0\ge5a^2+16a.
\tag{16}
\]

Exact integer arithmetic shows that (16) fails only for

```text
 a = 4, 6, 9, 11, 14, 19, 24, 29, 34, 39, 44.
```

These eleven cases are closed by the same finite threshold certificate already used in the profile-integral programme. For fixed `a`, maximum demand `H>0`, and total demand `S`, define for `1<=h<=H`

\[
K_h=\max\left(1,
\left\lceil\frac{S-a(h-1)}{H-h+1}\right\rceil\right),
\]

\[
w_h=\max\{H,hK_h,S-(a-K_h)(h-1)\}.
\]

Any demand multiset with maximum `H` and total `S` has at least `K_h` entries at least `h`, hence `W_h>=w_h`. Let `L_h` be the least integer `z>=H` satisfying

\[
z^2-z+h(h+1)\ge2w_h.
\]

By (3)-(4), `z_h>=L_h` and therefore

\[
r\ge\sum_{h=1}^H L_h,
\]

so

\[
S-r\le S-\sum_{h=1}^H L_h.
\tag{17}
\]

The exact maxima of (17) over all integer `1<=H<=a-1`, `H<=S<=aH` are:

| a | least b | required T0 | max upper bound on S-r |
|---:|---:|---:|---:|
| 4 | 7 | 1 | 1 |
| 6 | 10 | 2 | 2 |
| 9 | 14 | 4 | 5 |
| 11 | 17 | 6 | 8 |
| 14 | 21 | 9 | 13 |
| 19 | 28 | 16 | 26 |
| 24 | 35 | 25 | 43 |
| 29 | 42 | 36 | 64 |
| 34 | 49 | 49 | 90 |
| 39 | 56 | 64 | 121 |
| 44 | 63 | 81 | 155 |

Every entry in the last column is strictly below `2T0`. Since `2t<=S-r`, each exception contradicts `t>=T0`. The zero-demand case `S=0` gives `t<=0` separately.

For `a=0`, edge-criticality plus a universal vertex forces a star, so `m=n-1<floor(n^2/4)` for `n>=6`. For `a=1`, `F` is edgeless and `t=-r<=0`, whereas the eligible degree premise requires positive surplus relative to the Turán threshold. Thus all cases are covered.

This proves the candidate implication (T+).

## 7. Exact checker and trust boundary

`src/check_7_12.py` verifies with standard-library rational/integer arithmetic:

1. the square-root minorant identity and endpoint signs;
2. the `5/64` scalar polynomial certificate;
3. the large-`a` quadratic margin and forward difference;
4. completeness of the eleven finite assembly exceptions;
5. the exact threshold certificate for all eleven exceptions;
6. a degree-pair regression through `n=5000`.

The regression is not proof by exhaustion; it is a consistency check on the hand assembly.

The principal mathematical trust boundary remains the shared graph-to-demand and threshold-capacity argument in Sections 1--2. A flaw there would affect both this strengthening and the earlier profile-integral candidate. Same-assistant checking is not external review.
