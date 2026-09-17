# Receiver inflation beyond h-index saturation

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal hand theorem with exact arithmetic audit; not promoted; external review and novelty open.** This result was chosen after stepping back from the recorded `u>0` next action. It uses destination structure that is invisible in the scalar h-index bound and is intended as a bridge between the h-index saturation theorem, the older heavy-routing family, and the exact-block receiver pools.

## 1. Setup

Use the positive-surplus residual setup of `project/research/general_n/2026-09-07-residual-hindex-v1/README.md` and the selected-representative bridge used by the current structural treatment. Thus `A` has size `a`, `B` has size `b`, `t>0`, every B-source has residual degree `rho_x>=1`, and each A-label has demand

    s_i=max(0,d_i-R_i).

Let `h` be the residual h-index and write

    H={x in B:rho_x>=h},     |H|=h+u=:N,
    T={i in A:s_i=h},        |T|=k.

The selected-edge injection gives `s_i<=h`. Every `i in T` has at least `h` selected occurrences and can be selected only from `H`.

For `x in H`, let

    r_x=#{i in T : i is selected at x}.

Then

    sum_(x in H) r_x >= kh.                              (1)

Because the complete `H x T` rectangle has `Nk` incidences, (1) also gives the omission budget

    sum_(x in H)(k-r_x) <= ku.                           (2)

## 2. Receiver-inflation theorem

Fix an integer `q` with

    1<=q<=min(h-1,k-1).

Call a high source `q`-light when `r_x<=q`. Put

    ell_q=min(N, floor(ku/(k-q))),                       (3)
    X_q=kh-q ell_q,                                      (4)
    Y_q=max(0, X_q-binomial(N,2)),                       (5)
    z_q=ceil(Y_q/N).                                     (6)

Then every actual realization satisfies

    r >= b+h(h-1)+u(h-1)+(q-1)z_q,                      (RI-r)

where `r=sum rho_x` is the total residual cross count. Consequently

    b+2t <= (a-h-u)(h-1)+k-(q-1)z_q.                    (RI)

The best bound is obtained by maximizing `(q-1)z_q` over the allowed `q`.

This is a genuine extra penalty beyond the preceding h-index saturation theorem. It uses only selected-pair uniqueness, forward containment, compatibility and residual activity; it has no supplement-indegree cap and no exact-block hypothesis.

## 3. Proof

### 3.1 Few light rows

Every q-light source omits at least `k-q` maximum-demand labels. By the total omission budget (2), the number of q-light sources is at most

    floor(ku/(k-q)),

and of course at most `N`. This proves (3).

The q-light rows together contain at most `q ell_q` selected T-incidences. Since the total is at least `kh`, the q-heavy rows `r_x>=q+1` contain at least

    kh-q ell_q=X_q                                      (7)

selected T-incidences.

### 3.2 High destinations have pair capacity

A selected cross-edge represents one unordered B-pair, and distinct selected cross-edges represent distinct B-pairs. Therefore at most

    binomial(N,2)

of the incidences counted in (7) can have their destination also in `H`. Hence at least `Y_q` of them have low destinations outside `H`.

A fixed low destination `v` can receive at most one such selected representative from each source `x in H`, because there is only one unordered B-pair `{x,v}`. Thus it receives at most `N` of the incidences. At least

    z_q=ceil(Y_q/N)                                     (8)

distinct low destinations are therefore forced.

### 3.3 Each forced low receiver has residual degree at least q

Take one of the low-destination incidences, say `(x,i)->v`, from a q-heavy source. The source `x` selects at least `q+1` labels of `T`. Forward containment for a selected representative puts every other selected T-label at `x` into the J-neighbourhood of `v`.

Because `v` is low, `rho_v<h`. It cannot select a label `j in T`: the selected-edge compatibility inequality would give

    h=s_j<=rho_v,

a contradiction. Hence all the other selected T-labels at `x` are residual at `v`. There are at least `q` of them, so

    rho_v>=q.                                          (9)

The ordinary h-index lower bound already counts every low vertex with residual degree one, using positive-surplus activity. Each of the `z_q` distinct receivers in (8) therefore contributes at least `q-1` additional residual units. The `N=h+u` high sources contribute at least h each. Thus

    r>=hN+(b-N)+(q-1)z_q
     =b+h(h-1)+u(h-1)+(q-1)z_q,

which is (RI-r).

Finally the demand side of the h-index argument gives

    r+2t<=sum_i s_i<=a(h-1)+k.

Subtracting (RI-r) proves (RI).

## 4. What the theorem says on the square face

When `u=0` and `k=h`, there are no light rows for any `q<h`, so `ell_q=0`. Taking `q=h-1` gives

    Y_q=h^2-binomial(h,2)=h(h+1)/2,
    z_q=ceil((h+1)/2),

and therefore the additional scalar loss

    (h-2)ceil((h+1)/2).                                (10)

For example this loss is 9 at h=5, 16 at h=6, 20 at h=7 and 30 at h=8.

The exact-block theory is stronger on this square face: it proves h labelled full receiver pools, each with residual degree h-1, rather than merely the `ceil((h+1)/2)` receivers forced by global B-pair capacity. Thus (10) is not a replacement for the exact-block theorem. Its purpose is to survive when the square face is perturbed.

## 5. Excess-source examples

For `k=h`, optimizing the receiver penalty over q gives the following illustrative additional losses beyond `a-k+u(h-1)` from the preceding saturation theorem:

| h | u=0 | u=1 | u=2 | u=3 |
|---:|---:|---:|---:|---:|
| 5 | 9 | 2 | 0 | 0 |
| 6 | 16 | 4 | 1 | 0 |
| 7 | 20 | 6 | 2 | 0 |
| 8 | 30 | 9 | 3 | 1 |
| 9 | 35 | 12 | 6 | 2 |
| 10 | 48 | 18 | 8 | 3 |
| 11 | 54 | 24 | 12 | 4 |
| 12 | 70 | 28 | 15 | 6 |

These are arithmetic consequences of (RI), not graph realizations and not sharpness claims. They show that the excess-high-source branch is not cost-free even before exact-block structure is reached.

## 6. Relation to the older heavy-load routing family

The 12 September heavy-load theorem in `project/research/general_n/2026-09-12-heavy-load-family-v1/HEAVY_LOAD_FAMILY.md` controls selected heavy load through supplement indegrees `p_u`, residual tails and ramp potentials. The present theorem uses a different resource:

- high-destination selected incidences consume distinct unordered pairs inside H;
- the overflow must go to low destinations;
- a low destination of a heavily loaded source must carry many maximum-demand labels residually.

Thus the two mechanisms are complementary. Receiver inflation has no incoming-degree hypothesis; the heavy-load theorem can still constrain profiles for which the coarse pair-capacity overflow `Y_q` vanishes.

## 7. Step-back assessment: the next obstruction is multi-level

The new bound addresses the recorded `u>0` scope gap, but a wider review shows that this is not the only escape from the exact square block. Even with `u=0`, a scalar optimizer can move mass from the top demand level `h` to the `h-1` level by taking `k<h`. In that regime the top receiver penalty weakens while the older h-index sum bound can remain large.

That means the next best move is **not** simply to keep increasing the `u>0` penalty in isolation. The more promising structural target is a multi-level or peeling theorem: after accounting for the top `h`-level selected/receiver structure, expose the forced `(h-1)`-level load and charge its receivers or supplement routing as well. The existing heavy-load tail inequalities are natural ingredients for that second layer.

This is the main strategic conclusion of this unit. It changes the next research priority from a single excess-source branch to a staircase of coupled demand levels.

## 8. Arithmetic audit and limits

`check_receiver_inflation.py` independently solves the finite row-load relaxation by dynamic programming. For every tested `(h,u,k,q)` it computes the exact maximum number of q-light rows and the exact minimum selected mass in q-heavy rows subject only to `sum r_x>=kh`, then checks the closed bounds (3)--(4). The published range is

    2<=h<=15, 0<=u<=5, 1<=k<=15,

with every admissible q, giving 6,090 parameter/threshold checks and no failure.

This audit verifies the arithmetic row relaxation, not the graph implications in Sections 3.2--3.3. Those are hand arguments from the representative system and still require independent mathematical review. No canonical graph census, fixed-order promotion or unrestricted Murty-Simon claim is made.
