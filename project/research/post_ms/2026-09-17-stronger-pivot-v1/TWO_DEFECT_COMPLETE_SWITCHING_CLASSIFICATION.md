# Complete two-defect switching classification and eventual exclusion

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical and novelty review open.**

The live target is the sufficiently-large/eventual second-extremal D2C problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 Dailly--Foucaud--Hansberg Conjecture 3 is not assumed. The order-12, size-32 D2C obstruction remains a mandatory hostile control.

This note completes the two-defect switching problem left open in `TWO_DEFECT_ISOLATED_STAR_SWITCHING_EXCLUSION.md`. The key point is stronger than the previous exploratory bound: the orientation-code cover number can be computed exactly for every four-parameter two-defect state. Combining that formula with the preserved above-threshold density window `a<=2k` leaves only two lopsided normal forms. One is the already closed isolated-star state; the other is an adjacent lopsided state with cover number exactly `2k`, and it can be closed by the same F-separation mechanism.

---

## 1. Full-tight Boolean setup

Assume a maximum-degree root `v` has a full tight-antipode cover

\[
B=P_1\dot\cup\cdots\dot\cup P_k,
\qquad |P_i|=2,
\qquad b=2k.
\]

The B-layer is a signed 2-lift of `K_k`. Every `A`-vertex has a Boolean code in `{0,1}^k`, and the orientation-code graph `Omega_sigma` has one code vertex per Boolean code and one edge per physical rooted B-edge. The actual distinct A-code support is a vertex cover of `Omega_sigma`.

The exact full-tight identities are

\[
Q=k(k-1),
\qquad
r=k(a-k+1),
\qquad
\delta=r-e(F).
\]

The preserved density window says that any full-tight graph with `m>M(n)` satisfies

\[
\boxed{a\le2k}. \tag{1.1}
\]

Thus a structural lower bound on `tau(Omega_sigma)` near `2k` directly constrains the eventual problem.

---

## 2. Every two-defect switched state has four parameters

Suppose a switched graph `L` has exactly `k-2` leaves, hence exactly two non-leaf coordinates `a,b`.

Every other vertex has degree one, so it is either

- attached to `a`;
- attached to `b`; or
- paired with another leaf in an isolated `K_2`.

The edge `ab` may or may not be present. Write

- `P` for the `p` leaves attached to `a`;
- `Q` for the `q` leaves attached to `b`;
- `R_1,...,R_t` for the `t` isolated leaf-leaf pairs;
- `epsilon in {0,1}` for the indicator of `ab`.

Then

\[
p+q+2t=k-2, \tag{2.1}
\]

and the two exceptional degrees

\[
p+\epsilon,\qquad q+\epsilon
\]

must both differ from one.

This is the complete two-defect parameter family `(p,q,t,epsilon)`.

---

## 3. Orientation-code formula

Choose the two-defect state itself as the zero switching state, so its edge indicator is the signing `sigma`.

For a physical B-edge from source fibre `j`, source endpoint bit `s`, to target fibre `i`, the forced witness code is

\[
\begin{aligned}
c_j&=1-s,\\
c_i&=s\oplus\sigma_{ij},\\
c_h&=1\oplus s\oplus\sigma_{jh}\qquad(h\ne i,j).
\end{aligned} \tag{3.1}
\]

The other physical edge over the same quotient pair gives the complementary code. Formula (3.1) is therefore enough to determine `Omega_sigma` by direct equality comparison of code vectors.

The component accounting below is obtained solely from (3.1). It is useful to record it because it converts the exploratory four-parameter scan into a hand-checkable finite family.

---

## 4. Exact cover formula when `t=0`

### 4.1 `epsilon=0`

If one of `p,q` is zero, validity forces the other to equal `k-2`; this is the isolated-star state already treated in the predecessor note. Its orientation-code graph is

\[
2K_{k-2}\ \dot\cup\ 4K_{1,k-2}\ \dot\cup\ K_2,
\]

with the final physical edge doubled. Hence

\[
\boxed{\tau=2k-1}. \tag{4.1}
\]

If both `p,q` are nonzero, validity forces `p,q>=2`. Formula (3.1) groups the quotient-pair families into

\[
2K_p,\qquad 2K_q,\qquad 2K_{p,q},\qquad 4K_{1,k-2},\qquad K_2,
\]

again with the final physical edge possibly carrying multiplicity but with the same simple vertex-cover problem. Thus

\[
\tau
=2(p-1)+2(q-1)+2\min(p,q)+4+1.
\]

Using `p+q=k-2`,

\[
\boxed{\tau=2k-3+2\min(p,q)}. \tag{4.2}
\]

Since `min(p,q)>=2`, this gives

\[
\tau\ge2k+1. \tag{4.3}
\]

### 4.2 `epsilon=1`

Validity now forces `p,q>=1`. Direct use of (3.1) gives the component decomposition

\[
2K_p\ \dot\cup\ 2K_q\ \dot\cup\ 2K_{p+1,q+1}
\ \dot\cup\ 2K_{1,p}\ \dot\cup\ 2K_{1,q}.
\]

Therefore

\[
\begin{aligned}
\tau
&=2(p-1)+2(q-1)
 +2(\min(p,q)+1)+4\\
&=\boxed{2k-2+2\min(p,q)}. \tag{4.4}
\end{aligned}
\]

In particular:

- if `min(p,q)=1`, then `tau=2k`;
- if `min(p,q)>=2`, then `tau>=2k+2`.

---

## 5. Exact cover formula when `t>=1`

The leaf-pair family produces many extra orientation-code components. The cleanest proof is to group quotient pairs before simplifying code equalities.

For `p+q>0`, formula (3.1) gives the following disjoint cover contributions.

| Quotient-pair package | minimum-cover contribution |
|---|---:|
| pairs internal to `P` | `2(p-1)_+` |
| pairs internal to `Q` | `2(q-1)_+` |
| the `P-Q` package together with its two exceptional spine incidences | `2 min(p,q)+2` |
| the two cross-exception star packages | `2` |
| the `a-b` package | `2` |
| incidences between each `R_s` and `{a,b} union P union Q` | `8t` |
| incidences between distinct `R_s,R_u` | `2t(t-1)` |

Here `(x)_+=max(x,0)`. For `epsilon=0` the `P-Q` package visibly splits into two `K_{p,q}` components plus a two-centre double-star. For `epsilon=1` some of those pieces merge, but an explicit cover and an equally large disjoint matching/clique certificate give the same total contribution `2 min(p,q)+2`. The other rows are unions of cliques, stars, doubled edges, or two-centre trees directly read from (3.1).

Summing yields

\[
\boxed{
\tau
=2(p-1)_+ +2(q-1)_+ +2\min(p,q)
 +2t^2+6t+6.
} \tag{5.1}
\]

This formula is independent of `epsilon` whenever the tuple is valid and `p+q>0`.

There is one special family: `p=q=0`, necessarily `epsilon=0`. Then `k=2t+2`, and formula (3.1) gives exactly

- `4t` path components `P_3`;
- `2t^2-2t+3` isolated `K_2` components.

Hence

\[
\boxed{\tau=2t^2+2t+3}. \tag{5.2}
\]

### Consequence

Every valid `t>=1` tuple satisfies

\[
\boxed{\tau>2k}. \tag{5.3}
\]

Indeed:

- if `p=q=0`, then `t>=2` and
  \[
  \tau-2k=2t^2-2t-1>0;
  \]
- if one of `p,q` is zero, validity gives the other at least two and (5.1) gives
  \[
  \tau-2k=2t^2+2t>0;
  \]
- if both are positive, the same difference is even larger.

Thus every two-defect state containing at least one isolated leaf-leaf pair is already incompatible with (1.1) in an above-`M(n)` full-tight graph.

---

## 6. Exact density reduction: only two lopsided normal forms survive

Combine Sections 4--5 with the above-threshold density condition `a<=2k` and the fact that the A-code support has size at least `tau(Omega_sigma)`.

Every two-defect state except the following two forms has

\[
\tau>2k
\]

and is therefore impossible before any F-analysis:

### Type I: isolated-star

\[
(p,q,t,\epsilon)=(0,k-2,0,0)
\]

or its symmetric copy. Here

\[
\tau=2k-1.
\]

This type was already excluded above `M(n)` for `k>=12` in `TWO_DEFECT_ISOLATED_STAR_SWITCHING_EXCLUSION.md`.

### Type II: adjacent lopsided

\[
(p,q,t,\epsilon)=(1,k-3,0,1)
\]

or its symmetric copy. Here

\[
\boxed{\tau=2k}. \tag{6.1}
\]

Therefore an above-threshold graph in Type II must have exactly

\[
a=2k,
\qquad
\lambda=2k-a-1=-1. \tag{6.2}
\]

It remains only to close this single normal form.

---

## 7. Orientation-code normal form for the adjacent-lopsided survivor

Let `u` be the unique leaf attached to exceptional coordinate `a`, and let

\[
D=\{d_1,\ldots,d_{k-3}\}
\]

be the leaves attached to `b`; also `ab` is present.

Formula (3.1) gives

\[
\boxed{
\Omega_\sigma
\cong
2K_{k-3}
\dot\cup 2K_{2,k-2}
\dot\cup 2K_{1,k-3}
\dot\cup 2K_2.
} \tag{7.1}
\]

For `k>=5`, every minimum cover therefore has the following structure:

- `k-4` labels from each `K_{k-3}` clique;
- the two size-2 sides of the two `K_{2,k-2}` components (four labels total);
- the centre of each `K_{1,k-3}` (two labels total);
- one endpoint from each `K_2` (two labels total).

The cover size is exactly `2k`, agreeing with (6.1).

Because `a=2k`, every A-label has a distinct code and the actual support is such a minimum cover.

---

## 8. F-separation closes the adjacent-lopsided form

The two clique layers in (7.1) have the same useful Boolean description as the predecessor isolated-star calculation. After endpoint gauge, their clean labels can be written

\[
x_d=\{b,d\},
\qquad
\bar x_d=[k]\setminus\{b,d\},
\qquad d\in D.
\]

Each clique cover omits one of its `k-3` labels, so all selected clique labels are clean singletons. Mark all eight non-clique labels in the minimum cover exceptional.

### Same-layer clean labels are F-independent

For distinct `d,e`, the Omega edge joining `x_d,x_e` represents a physical rooted B-edge and must be selected at one endpoint. Its source coordinate is one of `d,e`, where the two codes disagree. The selected-incidence F-separation rule therefore forbids

\[
x_dx_e\in E(F).
\]

The complementary clique layer is identical.

### A clean cross-layer F-edge forces high residual degree

For `d!=e`, the codes `x_d` and `bar x_e` agree only at coordinates `d,e`. The switched graph at `x_d` has leaf set

\[
D\setminus\{d\}.
\]

Thus among the two agreement coordinates only `e` can be selected. If

\[
x_d\bar x_e\in E(F),
\]

then F-separation allows at most one selected coordinate at each endpoint, so

\[
R_{x_d},R_{\bar x_e}\ge k-1. \tag{8.1}
\]

When `d=e`, the two codes are complements and the residual requirement is `k`, which is stronger.

Let `h` be the number of clean labels with residual degree at least `k-1`. Since

\[
r=k(k+1),
\]

we have

\[
h(k-1)\le r,
\qquad
h\le k+2. \tag{8.2}
\]

The clean-clean F graph is bipartite between the two clique layers, so

\[
e_F(\text{clean,clean})\le\left\lfloor\frac{h^2}{4}\right\rfloor.
\]

All F-edges incident with the eight exceptional labels are bounded conservatively by `8k`. Hence

\[
\boxed{
e(F)\le
\left\lfloor\frac{(k+2)^2}{4}\right\rfloor+8k.
} \tag{8.3}
\]

Therefore

\[
\delta=r-e(F)
\ge
k(k+1)-\left\lfloor\frac{(k+2)^2}{4}\right\rfloor-8k. \tag{8.4}
\]

At `a=2k`, we have `n=4k+1`, and the second-extremal comparison requires

\[
\delta\ge2k-1. \tag{8.5}
\]

The right side of (8.4) reaches (8.5) for every

\[
\boxed{k\ge14}. \tag{8.6}
\]

Thus Type II is eventually excluded.

---

## 9. Complete two-defect conclusion

Combining the exact cover classification with the isolated-star predecessor and Section 8 gives:

> **COMPLETE TWO-DEFECT SWITCHING EXCLUSION — internal candidate.**  
> In the full tight-antipode Boolean branch, if the switching class contains a state with exactly two non-leaf coordinates and `k>=14`, then
> \[
> m\le M(n).
> \]

More precisely:

- every two-defect parameter tuple except the isolated-star and adjacent-lopsided forms has `tau(Omega_sigma)>2k` and is incompatible with above-threshold density immediately;
- the isolated-star form is closed from `k>=12`;
- the adjacent-lopsided form is closed from `k>=14`.

So the **entire two-defect switching regime is eventually closed**.

Together with the one-defect results, any above-`M(n)` full-tight graph with sufficiently large `k` must have every switched graph containing at least three non-leaf coordinates.

---

## 10. Negative control and trust boundary

The order-12/32 hostile control remains outside the theorem: it is the `k=4,r=0` perfect-matching switching mechanism, not a two-defect state.

The exact cover formulas in this note are internal hand mathematics derived from (3.1) and backed by finite replay. External mathematical review and novelty assessment remain open. No all-order second-extremal theorem is claimed.

The natural next structural target is the **three-defect switching family**. A state with `k-3` leaves has three exceptional coordinates; every leaf is attached to one exceptional coordinate or paired with another leaf, while the induced graph on the three exceptional coordinates is arbitrary. This is again a finite-parameter normal form rather than an arbitrary signing problem.