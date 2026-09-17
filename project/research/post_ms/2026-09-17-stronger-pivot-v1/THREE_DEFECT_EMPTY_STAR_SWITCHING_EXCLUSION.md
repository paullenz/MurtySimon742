# Three-defect empty-core star switching state: exact cover and eventual exclusion

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical and novelty review open.**

The live target is the sufficiently-large/eventual second-extremal D2C problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 Dailly--Foucaud--Hansberg strengthening is not assumed. The published order-12, size-32 obstruction remains a mandatory hostile control.

This note treats the second low-cover three-defect normal form found by exact exploration. It is distinct from the triangle-star state: the three exceptional coordinates are independent, two are isolated, and every ordinary leaf is attached to the third exceptional coordinate.

---

## 1. Normal form

Let the exceptional coordinates be `a,b,c`, and let

\[
D=\{d_1,\ldots,d_{k-3}\}.
\]

Take as zero switched state

\[
L=K_{1,k-3}\text{ centred at }c\quad\dot\cup\quad K_1(a)\quad\dot\cup\quad K_1(b). \tag{1.1}
\]

Thus `a,b` are isolated, `c` is adjacent to every `d in D`, and there are no other edges.

For `k>=6` the general forced witness-code formula gives the exact orientation-code decomposition

\[
\boxed{
\Omega_\sigma
\cong
2K_{k-3}
\dot\cup 2K_{1,k-3}
\dot\cup 2K_{2,k-2}
\dot\cup 2K_2.
} \tag{1.2}
\]

The small case `k=5` has accidental code collisions and is deliberately outside the uniform decomposition statement.

The minimum-cover contribution is therefore

\[
2(k-4)+2+4+2=2k,
\]
so

\[
\boxed{\tau(\Omega_\sigma)=2k\qquad(k>=6).} \tag{1.3}
\]

This is exactly the same component signature as the previously closed adjacent-lopsided two-defect state, although the switched graph itself is different.

---

## 2. Density consequence

In the full tight-antipode branch, every above-`M(n)` graph satisfies the preserved density window

\[
a\le2k.
\]

Since the actual distinct A-code support is a vertex cover of `Omega_sigma`, (1.3) forces

\[
a=2k,
\qquad
\lambda=2k-a-1=-1,
\qquad
r=k(k+1). \tag{2.1}
\]

Moreover the support is a minimum cover of (1.2).

---

## 3. Clean clique layers

The two `K_{k-3}` components have ordinary Boolean labels

\[
x_d=\{c,d\},
\qquad
\bar x_d=[k]\setminus\{c,d\},
\qquad d\in D. \tag{3.1}
\]

A minimum cover selects `k-4` labels from each clique. The remaining non-clique part of a minimum cover consists of

- four labels from the two `K_{2,k-2}` components;
- two star centres from the two `K_{1,k-3}` components;
- one endpoint from each of the two `K_2` components.

Mark these eight labels exceptional. Every selected clique label is then a clean singleton code.

### Same-layer independence

Distinct selected labels in one clique are joined by an `Omega` edge corresponding to a physical rooted-B edge selected at one endpoint at a coordinate where their codes disagree. The selected-incidence F-separation rule therefore forbids an F-edge between two clean labels in the same clique layer.

### Cross-layer residual forcing

For distinct `d,e in D`, the codes

\[
x_d=\{c,d\},
\qquad
\bar x_e=[k]\setminus\{c,e\}
\]

agree only at coordinates `d,e`.

Switching (1.1) by `x_d` gives leaf set

\[
D\setminus\{d\}. \tag{3.2}
\]

Thus, among the two agreement coordinates, only `e` can be selected at `x_d`. If

\[
x_d\bar x_e\in E(F),
\]

F-separation allows at most one selected coordinate at each endpoint, hence

\[
R_{x_d},R_{\bar x_e}\ge k-1. \tag{3.3}
\]

When `d=e`, the two codes are complementary and the residual requirement is `k`, which is stronger.

Let `h` be the number of high-residual clean labels. From (2.1),

\[
h(k-1)\le r=k(k+1),
\qquad
h\le k+2. \tag{3.4}
\]

The clean-clean F graph is bipartite between the two clique layers, so

\[
e_F(\mathrm{clean},\mathrm{clean})
\le\left\lfloor\frac{h^2}{4}\right\rfloor.
\]

All F-edges incident with the eight exceptional labels are bounded conservatively by `8k`. Therefore

\[
\boxed{
e(F)
\le
\left\lfloor\frac{(k+2)^2}{4}\right\rfloor+8k.
} \tag{3.5}
\]

---

## 4. Eventual exclusion

Using the full-tight identity

\[
\delta=r-e(F),
\]

(2.1) and (3.5) give

\[
\delta
\ge
k(k+1)-\left\lfloor\frac{(k+2)^2}{4}\right\rfloor-8k. \tag{4.1}
\]

At `a=2k`, one has `n=4k+1`, and the exact comparison with `M(n)` requires

\[
\delta\ge2k-1. \tag{4.2}
\]

The lower bound (4.1) reaches (4.2) for every

\[
\boxed{k\ge14}. \tag{4.3}
\]

Hence:

> **EMPTY-CORE THREE-DEFECT STAR EXCLUSION — internal candidate.**  
> In the full tight-antipode branch, if the switching class contains the state (1.1) and `k>=14`, then
> \[
> m\le M(n).
> \]

Together with the triangle-star theorem, both currently known three-defect states with orientation-code cover at most `2k` are now eventually excluded.

---

## 5. Trust boundary

- The order-12/32 `k=4,r=0` hostile control is a different residual-zero perfect-matching mechanism and is unaffected.
- The complete three-defect cover classification is not yet proved; this note closes only the explicit empty-core star normal form.
- The exact decomposition (1.2) and the arithmetic threshold are independently replayable in the accompanying checker.
- External mathematical review and novelty assessment remain open.