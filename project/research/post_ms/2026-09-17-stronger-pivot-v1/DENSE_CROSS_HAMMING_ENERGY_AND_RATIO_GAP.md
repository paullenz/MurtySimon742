# Dense-cross Hamming energy and an explicit unmatched-ratio gap

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal candidate structural theorems; external review open. This note continues `BETA_WITNESS_REUSE_GEOMETRY.md` in the near-full partial-Boolean branch. It does not assume the false all-order 2019 second-extremal conjecture. The published order-12/32 `X_3` control has `u=0` and is outside every argument below.

The purpose is to carry the beta-reuse geometry through the dense `A--U` layer. The main outputs are:

1. an exact beta/central partition of the `A--U` edges;
2. an injection of beta-central triples into Boolean Hamming-disagreement energy of `U`;
3. an exact stability budget coupling beta reuse, coordinate imbalance, `q=e(U)` and unmatched slack;
4. a stronger side-occupancy lemma for every beta-loaded A-vertex;
5. an explicit asymptotic gap from the previously possible ratio `u/p=4`: for fixed `lambda`, a sufficiently large above-`M(n)` candidate in the linear-unmatched regime must satisfy

> `u < (63/16) p`.

No global eventual second-extremal theorem is claimed.

---

## 1. Setup and one source-distinctness point

Use the notation of `CURRENT_STATE.md`:

- `p` tight antipode fibres;
- `U` the unmatched part of `B=N(v)`, `|U|=u`;
- `A=V\N[v]`, `|A|=a`;
- `lambda=2b-n=b-a-1`;
- `q=e(G[U])`, `s=e_G(A,U)`;
- `E_U=sum_{y in U}(b-d(y))`.

Thus

> `a=2p+u-lambda-1`,                                      (1.1)
>
> `s=u(p+u-1)-2q-E_U`.                                   (1.2)

For `x in A`, let `ell_x` be its beta load and `I_x` its set of beta target fibres as in `BETA_WITNESS_REUSE_GEOMETRY.md`.

For each `i in I_x`, write `y_i` for the unmatched source of the selected beta obligation witnessed by the physical edge `xy_i`.

There is a small injectivity point worth making explicit. The preserved selected/Hall rule says that, for a **fixed unmatched source** `y`, distinct beta-oriented P--U obligations use distinct selected cross edges `yx`. Therefore one physical cross edge `xy` cannot be the selected representative of two different beta obligations from the same source. Since the fibres in `I_x` are already distinct, it follows that

> the sources `y_i`, `i in I_x`, are pairwise distinct.       (1.3)

This justifies literally the one-coordinate-deviation language used in the predecessor note.

Put

> `Y_x={y_i:i in I_x}`,
>
> `C_x=N_U(x)\Y_x`,
>
> `c_x=|C_x|`.

Then `|Y_x|=ell_x`, and hence

> `d_U(x)=ell_x+c_x`.                                     (1.4)

Every beta-oriented P--U obligation has exactly one selected cross edge, and every selected cross edge occurring this way is one of the edges `xy_i`. Consequently, writing

> `B=sum_x ell_x=B_beta`,
>
> `C=sum_x c_x`,

we have the **exact partition**

> `s=B+C`.                                                (1.5)

This is stronger than using only the lower bound `B>=pu-mu_alpha a`.

---

## 2. Central triples inject into U-code Hamming disagreements

Fix any consistent `0/1` labelling of the endpoints of the `p` tight fibres. Write `c(y) in {0,1}^p` for the partial Boolean code of `y in U`.

Consider the set of **central triples**

> `(x,z,i)` with `x in A`, `z in C_x`, and `i in I_x`.

Its cardinality is

> `T=sum_x ell_x c_x`.                                    (2.1)

Map such a triple to

> `(y_i,z,i)`.                                            (2.2)

This map is injective. Indeed the selected system fixes the selected beta witness for the physical obligation at source `y_i` and fibre `i`, so `(y_i,i)` recovers `x`; then `z` is unchanged.

By beta-reuse criticality, `y_i` chooses the beta target in fibre `i`, whereas every other U-neighbour of `x`, in particular every `z in C_x`, chooses its tight mate. Thus

> `c(y_i)_i != c(z)_i`.                                   (2.3)

For coordinate `i`, let

> `u_i^0=|{y in U:c(y)_i=0}|`,`
>
> `u_i^1=|{y in U:c(y)_i=1}|`,
>
> `d_i=u_i^0-u_i^1`.

The number of **ordered** U-pairs disagreeing at coordinate `i` is `2u_i^0u_i^1`. Therefore the total ordered Hamming-disagreement energy is

> `D_U=sum_{y!=z} dist_H(c(y),c(z))`
>
> `   =2 sum_i u_i^0u_i^1`
>
> `   =p u^2/2 - (1/2) sum_i d_i^2`.                     (2.4)

The injection (2.2) proves

> **CENTRAL-TRIPLE HAMMING THEOREM**
>
> `T=sum_x ell_x c_x <= D_U <= p u^2/2`.                 (2.5)

Put

> `H=sum_i d_i^2`.                                        (2.6)

Then the sharp form is

> `T + H/2 <= p u^2/2`.                                  (2.7)

This is a hand injection, not a finite-scan inference.

---

## 3. Exact beta-reuse stability budget

For every `x in A`, since `ell_x<=p` and `c_x<=u`,

> `(p-ell_x)(u-c_x)>=0`.

Expanding gives the exact identity

> `ell_x c_x`
>
> `=u ell_x+p c_x-pu+(p-ell_x)(u-c_x)`.                  (3.1)

Define

> `Z=sum_x (p-ell_x)(u-c_x)>=0`.                         (3.2)

Summing (3.1), using `C=s-B` and (1.5), gives

> `T=(u-p)B+p s-pua+Z`.                                  (3.3)

Let

> `h_alpha=pu-B`                                         (3.4)

be the number of P--U obligations selected on the alpha side. The preserved alpha-capacity theorem gives

> `0<=h_alpha<=W_alpha<=mu_alpha a`.                     (3.5)

Substitute `B=pu-h_alpha`, (1.1) and (1.2) into (3.3). A direct simplification gives

> `T=p u(u-2p+lambda)`
>
> `  -(u-p)h_alpha-2p q-p E_U+Z`.                        (3.6)

Combining (3.6) with the sharp Hamming bound (2.7) yields the exact **stability budget**

> **DENSE-CROSS HAMMING BUDGET**
>
> `Z+H/2`
>
> `<=p u(2p-lambda-u/2)`
>
> `  +(u-p)h_alpha+2p q+p E_U`.                          (3.7)

When `u>=p`, use (3.5) to obtain the parameter-level necessary inequality

> `Z+H/2`
>
> `<=p u(2p-lambda-u/2)`
>
> `  +(u-p)mu_alpha a+2p q+p E_U`.                       (3.8)

Dropping `Z,H>=0` gives the simpler necessary condition

> **DENSE-CROSS HAMMING NECESSARY INEQUALITY**
>
> `u(u/2-2p+lambda)`
>
> `<=((u-p)/p) mu_alpha a+2q+E_U`.                       (3.9)

For fixed `lambda` and `u=O(p)`, the preserved bounds

- `mu_alpha=O(sqrt(p))`;
- `q=O(p^(3/2))`;
- `E_U<=S_req-2=O(p)`

make the right side `O(p^(3/2))`. Hence (3.9) already gives

> `u <= 4p-2lambda+O(sqrt(p))`.                          (3.10)

The more important information is retained in (3.8), not in the coarse corollary (3.10).

---

## 4. Side occupancy is stronger than the central-set bound

The predecessor beta-reuse theorem says more than `C_x` lies on one side of every target fibre.

Fix `x` with `ell_x>0` and `i in I_x`. Every U-neighbour of `x` **except the one designated source `y_i`** chooses the same endpoint of fibre `i` as `x`. Therefore one side of coordinate `i` contains all `d_U(x)-1` vertices in `N_U(x)\{y_i}`.

Thus

> **LOADED-WITNESS SIDE-OCCUPANCY LEMMA**
>
> `d_U(x)-1 <= max(u_i^0,u_i^1)`
>
> `          =(u+|d_i|)/2`                               (4.1)

for every `i in I_x`.

Equivalently,

> `|d_i| >= (2d_U(x)-u-2)_+` for every `i in I_x`.       (4.2)

This is stronger than merely bounding `c_x`, because the other `ell_x-1` designated beta sources also lie on the central side at coordinate `i`.

A useful threshold form follows. For `theta>0`, define

> `J_theta={i:|d_i|>=theta p}`.                           (4.3)

If

> `ell_x>|J_theta|`,                                     (4.4)

then `I_x` contains a coordinate outside `J_theta`; hence (4.1) gives

> `d_U(x) <= (u+theta p)/2+1`.                           (4.5)

So a beta witness whose load is larger than the number of strongly imbalanced coordinates cannot itself be highly U-dense.

---

## 5. An explicit gap below u/p=4

We now combine the exact budget with side occupancy. This is an asymptotic theorem in the currently active **linear-unmatched, fixed-`lambda` regime**.

Assume for contradiction that there is a sequence of above-`M(n)` near-full candidates with

> `p -> infinity`, `lambda` fixed, `u=Theta(p)`,

and with a subsequential ratio

> `rho=u/p >= 63/16`.                                    (5.1)

The coarse inequality (3.10) allows us to restrict to `rho<=4+o(1)`.

The preserved bounds and (3.8) imply, uniformly along such a sequence,

> `H <= rho(4-rho)p^3+O(p^(5/2))`.                       (5.2)

Indeed the leading term in twice (3.8) is

`2p u(2p-u/2)=(4rho-rho^2)p^3`,

while the `lambda`, alpha, `q` and `E_U` terms are `O(p^(5/2))` or smaller.

Choose the fixed imbalance threshold

> `theta=5/4`.                                           (5.3)

Let `J=J_theta` and write `j=|J|/p`. From (5.2),

> `j <= (16/25)rho(4-rho)+o(1)`.                        (5.4)

Now let

> `L={x in A:ell_x>|J|}`.

Vertices outside `L` contribute at most `|J|` beta obligations each. Since

> `B>=pu-mu_alpha a=rho p^2-o(p^2)`                     (5.5)

and `a=(rho+2)p+o(p)`, the crude but sufficient count gives

> `|L|/p`
>
> `>=rho-(rho+2)j-o(1)`.                                (5.6)

Every `x in L` uses at least one coordinate outside `J`, so by (4.5)

> `d_U(x)/p <= (rho+5/4)/2+o(1)`.                       (5.7)

All other A-vertices satisfy only the trivial `d_U(x)<=u=rho p`.

Therefore

> `s/p^2`
>
> `<=rho(rho+2)`
>
> ` -(rho-5/4)/2 * [rho-(rho+2)j]+o(1)`.                (5.8)

On the other hand, `q=O(p^(3/2))` and `E_U=O(p)` in this regime, so the exact slack identity (1.2) gives

> `s/p^2=rho(1+rho)+o(1)`.                              (5.9)

Using the upper bound for `j` from (5.4), (5.8)--(5.9) require

> `(rho-5/4)/2`
>
> ` * [rho-(rho+2)(16/25)rho(4-rho)]`
>
> `<=rho+o(1)`.                                         (5.10)

Subtracting `rho`, the left-minus-right polynomial is

> `F(rho)`
>
> `=rho(64rho^3-208rho^2-252rho+315)/200`.              (5.11)

At the clean rational endpoint `rho=63/16=3.9375`,

> `F(63/16)=3969/40960>0`.                              (5.12)

Moreover

> `F'(63/16)=1071/50>0`,
>
> `F''(rho)=3(32rho^2-52rho-21)/25>0`

throughout `[63/16,4]`. Hence `F` is strictly increasing there. Equation (5.10) is therefore impossible for all sufficiently large `p` whenever the limiting ratio lies in `[63/16,4]`.

Together with (3.10), this proves:

> **EXPLICIT LINEAR-UNMATCHED RATIO GAP — internal candidate.**
>
> For every fixed `lambda`, every sufficiently large above-`M(n)` near-full partial-Boolean candidate in the linear-unmatched regime satisfies
>
> `u < (63/16)p`.                                       (5.13)

Equivalently, the previously admissible asymptotic endpoint `u/p=4` is separated from the surviving region by the explicit constant gap `1/16`.

The constant is not optimized. A numerical optimization of the threshold argument gives a modestly better boundary, but `63/16` is deliberately retained because the proof is exact and compact.

---

## 6. Near-boundary stability information retained for later use

Even before the explicit gap, (3.8) gives a useful structural description of any sequence attempting to approach the old `rho=4` boundary.

If

> `u=4p-2lambda+O(sqrt(p))`,

then the right side of (3.8) is `O(p^(5/2))`, and hence

> `H=sum_i d_i^2=O(p^(5/2))`,                            (6.1)
>
> `Z=sum_x(p-ell_x)(u-c_x)=O(p^(5/2))`.                 (6.2)

Consequently:

1. for every fixed `epsilon>0`, at most `O(sqrt(p))` tight coordinates satisfy `|d_i|>=epsilon p`;
2. for every fixed `epsilon>0`, all but `O(sqrt(p))` A-vertices satisfy at least one of
   
   `ell_x >= (1-epsilon)p`
   
   or
   
   `c_x >= u-epsilon p`.

The side-occupancy lemma then shows why this old boundary cannot actually be attained: a heavily beta-loaded A-vertex must meet a nearly balanced fibre, forcing its total U-degree close to at most `u/2`, while a highly U-central vertex can beta-load only through the very small set of strongly imbalanced fibres. The quantitative threshold count in Section 5 packages exactly this incompatibility.

---

## 7. Strategic consequence

The dense-cross branch has now moved from a qualitative shape

> sparse `U`, dense `A--U`, large beta reuse

to a quantitative incompatibility between three exact ledgers:

1. selected/Hall forces `B_beta` close to `pu`;
2. unmatched slack forces `s` close to `u(p+u)`;
3. beta-reuse side occupancy can realise both only if the U-code coordinates carry substantial imbalance, but the central-triple Hamming budget limits the total squared imbalance.

The next useful refinement is not another row classification. It is to optimize or sharpen this **load / U-degree / coordinate-imbalance tradeoff**, preferably without fixing `lambda`, and then couple the resulting bound back into `E_U+L_A` rather than only into the ratio `u/p`.

The order-12/32 `X_3` graph remains untouched: there `u=0`, whereas every theorem above concerns the unmatched layer.