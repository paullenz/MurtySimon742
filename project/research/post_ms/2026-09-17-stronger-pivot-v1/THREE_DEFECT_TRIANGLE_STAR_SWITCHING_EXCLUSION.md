# Three-defect triangle-star switching state: exact cover and eventual exclusion

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical and novelty review open.**

This note is the first continuation beyond the completed two-defect regime. It studies the lowest-cover three-defect state found by exact finite exploration: three exceptional coordinates spanning a triangle, with all `k-3` leaves attached to one triangle vertex.

The striking feature is that its orientation-code graph has exactly the same simple component signature as the previously solved isolated-star two-defect state. The Boolean clique labels differ slightly, but the same F-separation mechanism gives an eventual exclusion.

The false all-order 2019 second-extremal conjecture is not assumed. The order-12/32 `X_3` hostile control remains mandatory and lies outside the present regime.

---

## 1. Three-defect normal form

A switched graph with exactly `k-3` leaves has three non-leaf coordinates. Every leaf is either

- attached to one of the three exceptional coordinates; or
- paired with another leaf in an isolated `K_2`.

The graph induced by the three exceptional coordinates is arbitrary. Thus the complete three-defect family can be parameterised by

- attachment counts `(p_1,p_2,p_3)`;
- a number `t` of isolated leaf-leaf pairs;
- one of the eight graphs on the three exceptional coordinates;

subject to

\[
p_1+p_2+p_3+2t=k-3
\]

and the requirement that each exceptional coordinate have degree different from one.

This is again a finite-parameter structural family rather than an arbitrary signing problem.

The present note treats the exact state

\[
L=K_3\text{ on }\{a,b,c\}
\quad\text{plus }k-3\text{ leaves }D
\text{ attached to }c. \tag{1.1}
\]

Call this the **triangle-star three-defect state**.

---

## 2. Exact orientation-code decomposition

Use (1.1) as the zero switched state. The general forced witness-code formula is

\[
\begin{aligned}
c_j&=1-s,\\
c_i&=s\oplus\sigma_{ij},\\
c_h&=1\oplus s\oplus\sigma_{jh}\qquad(h\ne i,j).
\end{aligned}
\]

Direct equality comparison of these code vectors over all quotient pairs gives

> **TRIANGLE-STAR ORIENTATION-CODE NORMAL FORM — internal candidate**
>
> \[
> \boxed{
> \Omega_\sigma
> \cong
> 2K_{k-2}\ \dot\cup\ 4K_{1,k-2}\ \dot\cup\ K_2,
> }
> \tag{2.1}
> \]
>
> where the final simple `K_2` carries two physical rooted-B edges.

Therefore

\[
\boxed{\tau(\Omega_\sigma)=2(k-3)+4+1=2k-1.} \tag{2.2}
\]

So an above-`M(n)` full-tight graph containing this switching state can only have

\[
a\in\{2k-1,2k\},
\qquad
\lambda=2k-a-1\in\{0,-1\}. \tag{2.3}
\]

This already pushes the state into the same near-balanced window as the isolated-star two-defect mechanism.

---

## 3. Clique codes

After gauge, one `K_{k-2}` component has code vertices

\[
\varnothing
\quad\text{and}\quad
x_d=\{c,d\},\qquad d\in D,
\]

while the other clique is its complement.

Thus each clique contains

- one **special** code (`emptyset` or the all-one code), and
- `k-3` ordinary codes `x_d` or `bar x_d` indexed by `D`.

A minimum clique cover omits one code from each clique. We therefore mark as exceptional any selected special clique code; at most two such labels occur.

The four star centres and the chosen endpoint of the doubled `K_2` are also exceptional. Hence a canonical minimum cover has at most

\[
7
\]

exceptional core labels.

If the actual A-layer has

\[
q_0=a-(2k-1)=-\lambda\in\{0,1\}
\]

additional labels, mark every outside-core label and every label in a duplicated core class exceptional. As in the predecessor arguments, each surplus label creates at most two newly exceptional labels. Therefore

\[
\boxed{|E|\le7+2q_0=7-2\lambda.} \tag{3.1}
\]

All remaining labels are clean singleton ordinary clique codes.

---

## 4. F-separation on the clean clique layers

### Same-layer independence

Distinct ordinary codes in one clique are joined by an Omega edge. The corresponding physical rooted B-edge is selected at one endpoint, at a coordinate where the two codes disagree. The selected-incidence F-separation rule therefore gives

\[
F[\text{clean clique layer}]=\varnothing. \tag{4.1}
\]

This holds in both complementary layers.

### Cross-layer edges force high residual degree

For distinct `d,e in D`,

\[
x_d=\{c,d\},
\qquad
\bar x_e=[k]\setminus\{c,e\}
\]

agree only at the two coordinates `d,e`.

The switched graph at `x_d` has leaf set

\[
\{c\}\cup(D\setminus\{d\}). \tag{4.2}
\]

Among the two agreement coordinates, only `e` is a leaf. Hence if

\[
x_d\bar x_e\in E(F),
\]

F-separation allows at most one selected coordinate at `x_d`. Thus

\[
R_{x_d}\ge k-1.
\]

The complementary endpoint satisfies the same inequality. When `d=e`, the codes are complementary and the residual requirement is `k`.

Let `h` be the number of high-residual clean labels. Then

\[
h(k-1)\le r. \tag{4.3}
\]

The clean-clean F graph is bipartite between the two clique layers, so

\[
e_F(\text{clean,clean})
\le\left\lfloor\frac{h^2}{4}\right\rfloor. \tag{4.4}
\]

All edges incident with the exceptional set are bounded conservatively by `|E|k`. Therefore

\[
\boxed{
e(F)
\le
\left\lfloor\frac{h^2}{4}\right\rfloor
 +(7-2\lambda)k,
\qquad
h\le\left\lfloor\frac{r}{k-1}\right\rfloor.
} \tag{4.5}
\]

---

## 5. Eventual exclusion

In the full-tight normal form

\[
r=k(a-k+1)=k(k-\lambda). \tag{5.1}
\]

### `lambda=0`: `a=2k-1`

Then

\[
r=k^2,
\qquad
h\le k+1,
\]

and

\[
e(F)\le
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor+7k.
\]

The resulting lower bound on `delta=r-e(F)` reaches the exact second-extremal requirement for every

\[
\boxed{k\ge13}. \tag{5.2}
\]

### `lambda=-1`: `a=2k`

Then

\[
r=k(k+1),
\qquad
h\le k+2,
\]

and

\[
e(F)\le
\left\lfloor\frac{(k+2)^2}{4}\right\rfloor+9k.
\]

The resulting defect reaches the required threshold for every

\[
\boxed{k\ge15}. \tag{5.3}
\]

Therefore:

> **TRIANGLE-STAR THREE-DEFECT SWITCHING EXCLUSION — internal candidate.**  
> In the full tight-antipode branch, if the switching class contains the triangle-star state (1.1) and `k>=15`, then
> \[
> m\le M(n).
> \]

---

## 6. Why this matters

The complete two-defect regime has now been closed eventually. The triangle-star state is the first three-defect mechanism identified by exact finite exploration as having cover number only `2k-1`; all other tested three-defect parameter states through the current finite range have cover number at least `2k` or substantially larger.

Thus this state was the correct first target beyond two defects. Its exclusion shows that another low-cover Boolean obstruction does not generate an eventual counterexample family.

The next structural target should be the complete three-defect parameter family. The conjectural finite-family statement suggested by the current exact scan is

\[
\tau(\Omega_\sigma)\ge2k-1,
\]

with equality only for the triangle-star state and its relabellings. This is not yet proved and is not promoted.

---

## 7. Negative control and trust boundary

The order-12/32 hostile control is the `k=4` residual-zero perfect-matching Boolean/cube mechanism. It is not a three-defect triangle-star state and is unaffected by this theorem.

All universal statements above are internal hand mathematics backed by finite replay. External mathematical review and novelty assessment remain open. No all-order second-extremal theorem is claimed.