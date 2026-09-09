# Pairwise staircase potentials

9 September 2026. Research reduction inside the selected/residual necessary-condition framework. This is **not** an unrestricted Murty--Simon theorem.

## 1. Incidence-weighted measures

In the positive-demand zero-slack W/L master, a label state is

\[
v=(s,R,x),
\qquad d=R+s,
\qquad h=R+x,
\]

with incidence mass proportional to `x`, while a source state is

\[
u=(\rho,q,p),
\qquad \alpha=\rho+q-1,
\qquad \beta=q+p,
\]

with incidence mass proportional to `q`.

For grouped densities `L_v` and `W_u`, write

\[
\mu_L(v)=n_v x_v L_v,
\qquad
\mu_S(u)=n_u q_u W_u.
\]

The explicit total-incidence equation in the projected master is

\[
\sum_v \mu_L(v)=\sum_u\mu_S(u).
\tag{P0}
\]

## 2. BC staircase family

The dominant two-coordinate compatibility is

\[
d\le \alpha,
\qquad
h\ge \beta.
\tag{BC}
\]

Equivalently, in product-order coordinates `(d,-h)` and `(alpha,-beta)`, a transported incidence moves upward coordinatewise.

Let `H` be any nondecreasing integer-valued step function on the finite `d` support, allowing empty values below its first step. Then

\[
U_H=\{(d,h): h\le H(d)\}
\]

is an upper set for `(d,-h)`. Every finite upper set in this two-dimensional order is represented by such a monotone staircase after deleting redundant boundary points.

Therefore every valid BC coupling satisfies

\[
\boxed{
\sum_v \mu_L(v)\,\mathbf 1\{h_v\le H(d_v)\}
\le
\sum_u \mu_S(u)\,\mathbf 1\{\beta_u\le H(\alpha_u)\}.
}
\tag{BC-H}
\]

Conversely, on finite supports the full family `(BC-H)`, together with equal total mass, is equivalent to the Hall/Strassen upper-set condition for existence of a monotone BC coupling.

A staircase with minimal generators

\[
(D_1,-H_1),\ldots,(D_k,-H_k),
\]

where the `D_j` and `H_j` increase, is exactly the step function taking threshold `H_j` after `D_j` until the next jump.

## 3. SH staircase family

The second pairwise compatibility retained by the n=30 reduction is

\[
s\le\rho,
\qquad
h\ge\beta.
\tag{SH}
\]

Thus for any nondecreasing step function `K`, every valid coupling satisfies

\[
\boxed{
\sum_v \mu_L(v)\,\mathbf 1\{h_v\le K(s_v)\}
\le
\sum_u \mu_S(u)\,\mathbf 1\{\beta_u\le K(\rho_u)\}.
}
\tag{SH-K}
\]

Again, all finite `(s,-h)` upper sets are of this staircase form.

## 4. Weighted potential formulation

Take nonnegative weights `lambda_j`, `gamma_l` and staircase functions `H_j`, `K_l`. Define

\[
F(d,h)=\sum_j\lambda_j\mathbf 1\{h\le H_j(d)\},
\]

\[
G(s,h)=\sum_l\gamma_l\mathbf 1\{h\le K_l(s)\}.
\]

Summing `(BC-H)` and `(SH-K)` gives the single valid potential inequality

\[
\boxed{
\sum_v \mu_L(v)\,[F(d_v,h_v)+G(s_v,h_v)]
\le
\sum_u \mu_S(u)\,[F(\alpha_u,\beta_u)+G(\rho_u,\beta_u)].
}
\tag{P}
\]

This is the precise sense in which the current symbolic target has the form

\[
\Phi(s,d,h)=F(d,h)+G(s,h).
\]

The remaining theorem problem is not validity of `(P)`--that follows directly from pairwise monotone transport--but finding parameterised `F,G` for which the label side has a useful universal lower bound and the source side has a sufficiently strong universal upper bound from the source constraints, residual budget and threshold transport.

## 5. Exact n=30 exceptional-state G prototype

The exhaustive subset run

`checkpoints/N30_EXCEPTION_SH_SUBSETS_RUN_34349585850.json`

shows that, on top of the full BC staircase library, the unique minimum rejecting subset of the four generated SH corrections is `{1,2,3}`. The instrumented exact rerun gives Farkas weights

\[
420,\quad 525,\quad 713.
\]

The three required SH staircases have minimal generators

\[
\{(1,-1),(2,-5),(3,-6)\},
\]

\[
\{(1,-1),(2,-7)\},
\]

\[
\{(1,-1),(2,-2),(3,-11)\}.
\]

Equivalently, their threshold functions are

\[
K_1(1)=1,\ K_1(2)=5,\ K_1(s\ge3)=6,
\]

\[
K_2(1)=1,\ K_2(s\ge2)=7,
\]

\[
K_3(1)=1,\ K_3(2)=2,\ K_3(s\ge3)=11.
\]

Hence the finite correction potential is

\[
G=420\,1_{h\le K_1(s)}+525\,1_{h\le K_2(s)}+713\,1_{h\le K_3(s)}.
\tag{G30}
\]

On the exceptional profile (`s` takes values 1,2,3), this gives the step table

```text
s=1:  G=1658 for h<=1, then 0.
s=2:  G=1658 for h<=2; 945 for 3<=h<=5; 525 for 6<=h<=7; then 0.
s>=3: G=1658 for h<=6; 1238 at h=7; 713 for 8<=h<=11; then 0.
```

The companion exact certificate uses 21 BC staircase rows together with these three SH rows and has negative exact Farkas right-hand side. The BC part is being minimised next; the 21-row representation should not be interpreted as canonical.

## 6. Natural subfamilies and falsification programme

Several analytically simpler subfamilies follow immediately:

- **rectangles:** `H(d)=C` after one threshold `d>=D`;
- **BC diagonal:** `H(d)=d+c`, which is the one-dimensional dominance
  \[
  x-s\ge p-\rho+1;
  \]
- **SH diagonal:** `K(s)=s+c`, which is
  \[
  R+x-s\ge q+p-\rho;
  \]
- **first moments:** affine increasing potentials, yielding the three scalar moment inequalities in the dedicated ablation.

The exact first-moment ablation shows that all three scalar moments together reject 0/7 of the n=30 hard states, so affine potentials are far too weak. Rectangle-only and diagonal-CDF ablations are being run separately; their outcomes should determine how much genuinely multistep staircase geometry must survive into a general argument.

## 7. Status boundary

This note proves only the finite-order transport reductions and the validity of the staircase potential family inside the candidate graph-to-model framework. It does not prove that a bounded number of staircase steps suffices for arbitrary `n`, nor that the displayed n=30 coefficients generalise. The n=29 and n=30 complete candidate proofs are independent of this post-hoc generalisation route.
