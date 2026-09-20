# One-code rigid cut — residual-one beta-witness multiplicity tradeoff

Date: 2026-09-20

Status: **same-session structural continuation** of `ONE_CODE_R1_RESIDUAL_HUB_CRITICALITY.md`, conditional on the same rigid one-code near-equality interface. No finite scan is used as proof. The zero-positive actual-D2C rigid-fixture caveat remains binding.

The predecessor hub theorem supplies, for every `h in K`, a beta witness

> `f(h)=a_h in K\{h}`
>
> with `h a_h notin E` and `N(z_h) cap N(a_h)={q_j}`.      `(BM-0)`

This note retains the multiplicity pattern of `f` instead of collapsing immediately to the minimum-degree-one bound on `bar G[K]`.

## 1. Image-size interpolation for missing K-edges

For `a in K`, put

`r_a=|f^{-1}(a)|`,

and let

`s=|im(f)|`.

Then

`sum_a r_a=k`,

`r_a>=1` on the s image vertices, and `f` has no fixed point.

Every directed arc `h -> f(h)` lies on a missing edge of `G[K]`. One undirected missing edge can support at most two arcs, and it supports two exactly when its endpoints form a directed 2-cycle. Every such 2-cycle consumes two vertices of `im(f)`, so there are at most `floor(s/2)` doubled arc-pairs.

Therefore the k directed obligations use at least

> **`k-floor(s/2)` distinct missing K-edges.**             `(BM-KMISS)`

Hence

> **`e(K)<=binom(k,2)-k+floor(s/2)`.**                    `(BM-EK)`

Since `f` is fixed-point-free, `s>=2`. At the other extreme `s<=k`; minimizing `(BM-KMISS)` over s recovers exactly the predecessor `ceil(k/2)` bound.

Keeping s is useful because small witness image forces many K-holes, whereas large image creates a different rooted-Q price below.

## 2. Repeated beta witnesses force extra W--escape nonedges

Let

`t_a=d_U(a)`

be the number of U-neighbours of `a in K`, and let `epsilon_a=(2p+u)-d(a)` be its maximum-degree slack.

The hub theorem proved `K--H` empty. Therefore for `a in K`,

`d(a)=p+y+e_K(a)+t_a`,

so

> `epsilon_a=g0+u-e_K(a)-t_a`.                            `(BM-DEG)`

If `r_a>0`, the `r_a` preimages of a are distinct K-nonneighbours of a. Thus

`e_K(a)<=k-1-r_a`.

Using the residual-one identity `k=u-c+1`, equivalently `u-k+1=c`, and `g0+c=lambda+1`, `(BM-DEG)` gives

> **`t_a>=lambda+1+r_a-epsilon_a`.**                      `(BM-T)`

Now fix `h` with `f(h)=a`. From `(BM-0)`, every U-neighbour of a must be a nonneighbour of `z_h`, or it would be a second common neighbour of `z_h,a` besides `q_j`.

Among `W_s`, the vertex a is adjacent only to its own selected witness `z_a`, because every `z_b` has the unique X-neighbour b. Thus at least `t_a-1` of the forced nonneighbours of `z_h` lie in the escape set

`E=U\W_s`, `|E|=d_U=c-1`.

Different h have different first endpoints `z_h`, so these W--E missing pairs do not overlap across different h. If P denotes the number of W--E nonedges forced in this way, then

> **`P>=sum_a r_a(t_a-1)`.**                              `(BM-P1)`

Combining with `(BM-T)`,

> **`P>=sum_{a:r_a>0} r_a[lambda+r_a-epsilon_a]_+`.**    `(BM-P2)`

This is the first exact price for *repeated* use of one A-witness by many distinct beta sources at the unique residual coordinate.

## 3. A clean slack-versus-U-hole conservation law

For fixed integer `r>=1`, consider

`F_r(epsilon)=epsilon+2r[lambda+r-epsilon]_+`.

For `0<=epsilon<=lambda+r`, its slope is `1-2r<0`; beyond `lambda+r` it equals epsilon. Hence its minimum is attained exactly at `epsilon=lambda+r` and equals `lambda+r`.

Summing over the s active beta witnesses and using that `L_A` contains their A-slacks gives

> **`L_A+2P >= lambda s+k`.**                             `(BM-CONS)`

This is a physical conservation law: avoiding the extra W--escape holes requires paying enough A-slack at the repeatedly used beta witnesses, and vice versa.

Since `s>=2`, the coarse corollary is

> `L_A+2P>=2lambda+k`,

but the s-dependent form should be retained.

## 4. Rooted triangle capacity with multiplicity retained

The selected witness set `W_s` is independent. Without the new beta constraints one has

`q<=k d_U+binom(d_U,2)`.

The P additional missing W--E edges from `(BM-P1)` sharpen this to

> **`q<=k d_U+binom(d_U,2)-P`.**                          `(BM-Q)`

Equivalently, with `d_U=c-1`,

`q<=(c-1)u-c(c-1)/2-P`.

Use the exact rooted identity and score ceiling as in the predecessor Q-feedback note:

`Z+L_A <= u(p-lambda)+2q+C0`.

Together with `Z>=k(x+y-1)`, `(BM-Q)`, and `(BM-CONS)`, every residual-one survivor satisfies

> **`k(x+y-1)+lambda s+k`**
> **`<=u(p-lambda)+2(c-1)u-c(c-1)+C0`.**                 `(BM-QF)`

This is a new s-sensitive rooted-Q necessary condition derived before collapsing the beta-witness multiplicities.

## 5. The same image parameter sharpens the X-slack bill

For `p>=4`, the near-rigid private-coordinate theorem still gives

`e(H)<p/4`,

and the hub theorem gives `K--H` empty. Combining `(BM-EK)` with the exact X-degree identity and `Z_X>=k(x-1)` yields

> **`L_X > x g0-p/2 + k(p+1)-2floor(s/2)`.**              `(BM-LX1)`

The independent complement-code capacity `e(K)<=k(c-1)` gives in parallel

> `L_X > x g0-p/2+k(p+k-2c)`.                             `(BM-LX2)`

Therefore

> **`L_X > x g0-p/2 +`**
> **`max{k(p+1)-2floor(s/2), k(p+k-2c)}`.**               `(BM-LX)`

Minimizing the first term over `2<=s<=k` recovers the s-free floor in the predecessor hub note. The value of retaining s is the tradeoff:

- small s makes `(BM-LX)` stronger because many beta arcs collapse onto few witnesses and therefore force many K-nonedges;
- large s makes `(BM-QF)` stronger through the `lambda s` term.

This is the first direct interpolation between those two physical effects.

## 6. Stress-test interpretation

The exact residual-one escape family from `aa9f246...` is not closed merely by taking the two s-sensitive inequalities separately: its previous s-free `L_X` floor already dominates the coarse `lambda s+k` conservation term for the natural scaling range. Thus this package should not be advertised as a branch closure.

Its value is structural. The surviving freedom has been reduced to an explicit finite-dimensional object:

- a fixed-point-free beta-witness map `f:K->K`;
- image size s and indegrees `r_a`;
- A-slacks `epsilon_a` on the image;
- forced W--escape holes P satisfying `(BM-P2)`;
- the exact competing inequalities `(BM-QF)` and `(BM-LX)`.

The next attack should optimize these quantities **jointly**, not replace s by either endpoint prematurely. In particular, a proof that the singleton equations prohibit near-permutation witness maps (large s), or that small-s maps force additional same-code/U-hole structure beyond `(BM-P2)`, would attack the remaining unbounded direction at its actual physical bottleneck.
