# Second positive-residual full-tight layer: a Hamming-support defect bound

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not promoted. External mathematical and novelty review open.**

The active target is the sufficiently-large/eventual second-extremal D2C problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The false all-order 2019 strengthening is not assumed. The published order-12, size-32 obstruction remains a mandatory hostile control.

This note continues `FIRST_POSITIVE_RESIDUAL_TIGHT_COVER_GAP.md`. That predecessor proves that in a full tight-antipode Boolean cover with `k>=5`, the residual-zero layer and the first positive layer are absent, and in particular

\[
a\ge k+1,\qquad r=k(a-k+1)\ge2k.
\]

The present unit attacks the first surviving algebraic layer

\[
\boxed{a=k+1,\qquad r=2k.}
\]

The key point is that at this layer the Boolean witness-cover theorem forces every A-label to have a distinct code. The preserved F-separation rule then converts each label's residual-coordinate count directly into a Hamming-ball bound on its F-degree. This is enough to rule out the layer above `M(n)` once `k>=17`.

---

## 1. Entry point: the full-tight Boolean normal form

Assume the tight antipodes at a maximum-degree root `v` cover

\[
B=N_G(v)=P_1\dot\cup\cdots\dot\cup P_k,
\qquad |P_i|=2,
\qquad b=2k.
\]

Every `A`-vertex `x` is a Boolean transversal of the fibres and therefore has a code

\[
c(x)\in\{0,1\}^k.
\]

The exact full-cover identities are

\[
Q=k(k-1),
\qquad
r=k(a-k+1),
\qquad
\delta=r-e(F),
\]

where `F=G[A]`.

Now impose

\[
a=k+1.
\]

Then

\[
\boxed{r=2k.} \tag{1.1}
\]

The Boolean witness-cover theorem from the predecessor gives at least `k+1` **distinct** A-codes for `k>=5`. Since there are exactly `a=k+1` labels here, we obtain:

> **DISTINCT-CODE FACT.** Every A-label has a different Boolean code.   \(\tag{1.2}\)

This removes the principal obstruction to turning F-separation into a degree bound: there are no same-code multiplicities.

---

## 2. Residual coordinates contain every F-code difference

For `x in A`, let

\[
D_x\subseteq[k]
\]

be the set of fibre coordinates at which the unique H-cross incidence of `x` is residual. Thus

\[
|D_x|=R_x,
\]

and the complementary `k-R_x` coordinates are selected at `x`.

The preserved selected-incidence F-separation rule says:

> if coordinate `j` is selected at label `x`, every F-neighbour `y` of `x` agrees with `x` at coordinate `j`.

Consequently, for every edge `xy in E(F)`,

\[
\{j:c_j(x)\ne c_j(y)\}\subseteq D_x.                \tag{2.1}
\]

By symmetry it is also contained in `D_y`, but the one-sided inclusion is already enough here.

By (1.2), `c(y) != c(x)`. Hence the difference set in (2.1) is nonempty. There are only

\[
2^{R_x}-1
\]

nonempty subsets of `D_x`, and each determines at most one other A-code because all A-codes are distinct. Therefore

\[
d_F(x)\le2^{R_x}-1.                                  \tag{2.2}
\]

There is also the independent maximum-degree cap. Every A-vertex has exactly one G-neighbour in each antipode fibre, hence exactly `k` B-neighbours. Since the maximum degree is `b=2k`,

\[
d_F(x)\le k.                                         \tag{2.3}
\]

Combining:

> **HAMMING DEGREE BOUND.**
>
> \[
> \boxed{d_F(x)\le g_k(R_x):=\min\{k,2^{R_x}-1\}.}   \tag{HD}
> \]

Finally,

\[
\sum_{x\in A}R_x=r=2k.                               \tag{2.4}
\]

Thus a global F-edge bound follows from a one-variable majorant for `g_k`.

---

## 3. Uniform linear majorants

### 3.1 All `k>=19`

For every integer `R>=0` and `k>=19`,

\[
\boxed{g_k(R)\le\frac{k}{5}R.}                       \tag{3.1}
\]

For `R=0` this is trivial. For `R=1,2,3,4`, it is the four inequalities

\[
1\le k/5,
\quad 3\le2k/5,
\quad 7\le3k/5,
\quad 15\le4k/5,
\]

whose strongest requirement is `k>=75/4`, hence `k>=19`. For `R>=5`,

\[
g_k(R)\le k\le(k/5)R.
\]

Summing `(HD)`, using (2.4), and applying the handshake lemma gives

\[
2e(F)=\sum_x d_F(x)
\le\frac{k}{5}\sum_xR_x
=\frac{2k^2}{5}.
\]

Hence

\[
\boxed{e(F)\le\frac{k^2}{5}.}                        \tag{3.2}
\]

### 3.2 The two boundary values `k=17,18`

For `k in {17,18}` one instead has, for every `R>=0`,

\[
\boxed{g_k(R)\le\frac{15}{4}R.}                      \tag{3.3}
\]

For `R<=4`, the largest ratio `(2^R-1)/R` is `15/4`. For `R>=5`,

\[
g_k(R)\le k\le18<75/4\le(15/4)R.
\]

Therefore

\[
e(F)\le\frac{15k}{4}.                               \tag{3.4}
\]

Since `e(F)` is integral this gives

\[
e(F)\le63\quad(k=17),
\qquad
e(F)\le67\quad(k=18).                            \tag{3.5}
\]

---

## 4. Conversion to the second-extremal comparison level

At `a=k+1`,

\[
n=1+b+a=3k+2.
\]

Also

\[
\delta=r-e(F)=2k-e(F),
\]

and

\[
b(n-b)=2k(k+2).
\]

Therefore

\[
\boxed{m=2k^2+2k+e(F).}                              \tag{4.1}
\]

### 4.1 `k>=19`

By (3.2),

\[
m\le2k^2+2k+\frac{k^2}{5}.
\]

For `n=3k+2`,

\[
M(n)=\left\lfloor\frac{(3k+1)^2}{4}\right\rfloor+1
\ge\frac{9k^2+6k+4}{4}.
\]

The difference between this lower bound and the displayed upper bound for `m` is

\[
\frac{k^2-10k+20}{20},
\]

which is positive for every `k>=19`. Hence

\[
\boxed{m<M(n)\qquad(k>=19).}                          \tag{4.2}
\]

### 4.2 `k=17,18`

Using (3.5):

- `k=17`: `m<=2(17)^2+2(17)+63=675`, while `M(53)=677`;
- `k=18`: `m<=2(18)^2+2(18)+67=751`, while `M(56)=757`.

So again

\[
m<M(n).
\]

We obtain:

> **SECOND POSITIVE-RESIDUAL FULL-TIGHT DEFECT THEOREM — internal candidate.**  
> In a full tight-antipode Boolean cover with
>
> \[
> a=k+1,\qquad r=2k,
> \]
>
> and `k>=17`, one has
>
> \[
> \boxed{m<M(n).}
> \]
>
> Therefore an above-`M(n)` full-tight counterexample with `k>=17` cannot occupy this layer. It must satisfy
>
> \[
> \boxed{a\ge k+2,\qquad r=k(a-k+1)\ge3k.}           \tag{4.3}
> \]

This is a theorem only inside the full tight-antipode normal form. It does not address unmatched or errorful antipodes, and it is not an eventual second-extremal theorem by itself.

---

## 5. Interpretation

The residual-zero classification isolates `H5` and the order-12 `X_3` cube mechanism. The first positive-residual Boolean cover theorem then removes `r=k`. The present Hamming theorem shows that, once `k>=17`, the next algebraic layer `r=2k` is already too sparse in F to reach the second-extremal comparison level.

The mechanism is simple and reusable:

1. selected coordinates freeze Boolean coordinates along F-edges;
2. residual coordinates are therefore the only coordinates in which an F-neighbour may differ;
3. distinct Boolean codes turn `R_x` residual coordinates into at most `2^{R_x}-1` possible F-neighbours;
4. the exact residual ledger controls the sum of all `R_x`.

So residual mass is now doing two jobs simultaneously: it pays directly in `delta=r-e(F)` and it limits how dense `F` can become.

The mandatory `k=4`, `n=12`, `m=32` hostile control is untouched: it lies at the previously classified `r=0` boundary, far outside the present `k>=17` statement.

---

## 6. Next target

The next full-tight layer is

\[
a=k+2,\qquad r=3k.
\]

The witness-cover theorem still guarantees at least `k+1` distinct codes, so there can be at most one duplicated code class. The natural continuation is therefore to extend the Hamming-degree argument to **bounded code multiplicity**: quantify the extra F-degree made possible by that one duplicate class and determine whether the `r=3k` layer is also below `M(n)` for all sufficiently large `k`.

Separately, `(AMC)` remains the correct accounting tool when returning to near-full covers with unmatched or errorful antipodes. No return to Q0, the closed mixed `{4,5}` ladder, or first-proof optimization for Erdős #742 is warranted.