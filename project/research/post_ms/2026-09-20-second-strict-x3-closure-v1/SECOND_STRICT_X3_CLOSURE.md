# Exact second-strict mixed y=1 — x=3 finite-order closure

Date: 2026-09-20

Status: **same-session internal structural/algebraic reduction**, conditional on the audited rigid one-code complete-cut interface and on the predecessor second-strict chain. It is deliberately not promoted to README. The 20 September red-team caveat remains binding: bounded graph-level regression still has no positive actual-D2C rigid complete Hall-cut fixture with `x>=3`.

This note resolves the last unbounded-in-scope head count left by `SMALL_HEAD_TAIL_SCOPE.md`. It also strengthens the mixed-hole exceptional-capacity theorem: singleton support is forced for *every* exact mixed second-strict configuration with `x>=3`, not merely for the previously treated large-head cases.

## 1. Audit reconciliation and setup

Before forward work, reread `CURRENT_STATE.md`, root `README.md`, the 20 September daily red-team audit, the latest commits, `SECOND_STRICT_INITIAL_REDUCTION.md`, `SECOND_STRICT_MIXED_Y1_CLASSIFICATION.md`, `SECOND_STRICT_Y1_HOSTILE_EXTENSION.md`, the physical-bills package, and the orientation-polarization note.

The binding upstream facts used here are:

- exact mixed second-strict geometry: `epsilon_b=p-g+2`, `h_X=h_o=1`;
- unique buffer--X hole `a_0` and unique buffer--outside hole `z_0`;
- every ordinary outside vertex is a buffer neighbour and itself certifies some buffer head;
- every outside-certified buffer head is Type R;
- there are `H>=x-2>=1` such heads;
- for every Type-R head `x` and every `j in S_0`, the matched edge `xq_j` must be certified by the sole physical exception `z_0`;
- at most one buffer edge can use the reverse channel through `(b,z_0)`;
- the raw same-code theorem and ordered `(source,witness)` injection have independently passed the daily audit.

As before, `S_0={i:c(a_0)_i!=d_i}` is nonempty, `s=|S_0|`, `k=x-g>=1`, and `omega=|U_o|`.

## 2. New strengthening: singleton support is universal in the mixed exact-second-strict layer

### Lemma 2.1 — if the exceptional reverse buffer channel is used, then `s=1`

Suppose one buffer head `t` is reverse-certified by `z_0`. Then

`N(b) cap N(z_0)={t}`.

Every outside-certified Type-R head `x` is a different buffer neighbour, so necessarily

`z_0x notin E`.                                             `(X3-REV-MISS)`

Fix any such head `x` and any `j in S_0`. The initial reduction proves that the matched edge `xq_j` must use `z_0`. There are only two raw orientations:

1. `q_j -> x` through `z_0`. This would require `z_0x in E`, because the claimed singleton is `N(q_j) cap N(z_0)={x}`. This contradicts `(X3-REV-MISS)`.
2. `x -> q_j` through `z_0`. This uses the fixed physical pair `(x,z_0)` and would require `N(x) cap N(z_0)={q_j}`.

For fixed `(x,z_0)` the common-neighbour set is graph-fixed, so orientation 2 can hold for at most one coordinate `j`.

Since `S_0` is nonempty,

> **if the reverse buffer channel is used, then `|S_0|=1`.** `(MIX-S1-REV)`

This is stronger than the old aggregate capacity inequality in the one-head case.

### Lemma 2.2 — if the reverse channel is unused, then `s=1`

If the reverse channel is unused, all `x-1` actual buffer heads are outside-certified, so `H=x-1>=2` because `x>=3`.

The already-preserved coordinate-orientation polarization theorem then applies: for each `j in S_0`, the physical adjacency `z_0q_j` fixes the same orientation for every head. A reverse coordinate cannot serve two different heads through the one graph-fixed pair `(q_j,z_0)`, while if all coordinates are forward then each fixed `(x,z_0)` can support at most one coordinate. Hence `|S_0|=1`.

Combining the two cases gives the structural strengthening

> **UNIVERSAL MIXED SINGLETON-SUPPORT THEOREM.**
>
> In the exact mixed second-strict branch `(h_X,h_o)=(1,1)` with `x>=3`,
>
> **`|S_0|=1`.**                                           `(MIX-S1-ALL)`

No finite scan and no pair-capacity relaxation is used.

## 3. Scope audit: the R/Fx/Fz y=1 classification transfers to x=3

Now specialize to the last live head count `x=3`, with `p>=2` (the `p=1` rigid-code case is already impossible). By `(MIX-S1-ALL)`, write `S_0={j}`, `C=c(a_0)` and `D=bar C`.

The proof of the `a_0y` trichotomy needs only singleton support, at least one Type-R head, and `p>=2`; it does not need `x>=5`:

- ordinary outside vertices miss `y` and no ordinary outside vertex has code `bar d`;
- common core and buffer miss `y`, while `a_0` misses the common core;
- the d-side matched endpoint in the unique differing fibre has a Type-R outside witness as an extra common neighbour with `a_0`;
- the bar-d-side matched endpoint has a Type-R head as an extra common neighbour with `y`;
- a forward A-witness must have complementary code `D`, giving either `z_0` or the unique possible exceptional X-head;
- a reverse witness must have code `bar d`, leaving only `z_0` after the core/buffer exclusions.

Thus exactly the same three cases remain:

- **R:** `c(z_0)=bar d`, `z_0a_0 in E`, `z_0y notin E`;
- **Fz:** `c(z_0)=D`, `z_0a_0 notin E`, `z_0y in E`, `N(a_0) cap N(z_0)={y}`;
- **Fx:** a unique `D`-coded X-head `t` witnesses `a_0 -> y`; then `c(z_0)=d` and `N(b) cap N(z_0)={t}`.

The downstream structural proofs also transfer at `x=3`:

### R

The pair `(b,z_0)` shares the tight `bar d` matched support, so no reverse buffer edge is possible and both buffer heads are Type R. A radius-`>=2` head would force `z_0` to certify its `j`-matched edge; one orientation is killed by `z_0q_j in E`, and the other has at least two matched common neighbours. Hence all X has code C. The inherited Type-R `a_0--X'` nonedges plus the same-code theorem eliminate the remaining possible X-edge, so

`G[X]=emptyset`.

### Fx

The complementary head `t` cannot be Type R because its difference support omits `j`, and Type F is globally impossible. Therefore `t` is exactly the unique reverse-buffer head and the other buffer head is the sole Type-R head. The singleton `N(b) cap N(z_0)={t}` kills the reverse orientation needed by any higher-radius Type-R head at coordinate `j`, so that sole R-head has code C. The raw two-orientation argument for a hypothetical `t--C` edge uses only `p>=2` (matched/core common neighbours, `y`, `b`, and the fixed singleton), not a large C-class. Thus again

`G[X]=emptyset`.

### Fz

Since `p>=2`, `b` and the D-coded `z_0` already share `p-1>=1` tight matched neighbours, so no reverse buffer edge exists and both buffer heads are Type R. The fixed pair `(q_j,z_0)` allows at most one higher-radius head. If such a head h exists, the other buffer head is radius-one C, so the hostile-extension proof of `h--C=emptyset` still has a genuine C-head available. Together with Type-R `a_0--X'` nonedges this gives `G[X]=emptyset`.

In exceptional Fz, both ordinary outside witness classes are nonempty: one certifies the radius-one C-head and one certifies h. The cross-class U-edge exclusion therefore transfers unchanged, so `G[U_o]=emptyset`; the isolation and rooted-slot bounds also transfer:

`epsilon_{z_0}>=p+k+omega-2`, `r>=x+2=5`.

Therefore every physical bill used in the large-head scalar formulas is valid at x=3 once singleton support is supplied.

## 4. Exact rooted-margin formulas at x=3

For `x=3`, `g in {1,2}` and `k=3-g in {2,1}`. Let `eps in {0,1}` be the parity remainder in the exact rooted identity.

The predecessor's omega-completed-square formulas now become finite symbolic alternatives.

### 4.1 R and no-exception Fz

The exact maximum over real omega is

`2B_max=eps+4g-k^2-2kp+6k-p^2+2p-4`.

If `(g,k)=(1,2)`,

`2B_max=eps-p^2-2p+8 <= 9-p^2-2p`,

so `B>=0` forces `p=2`.

If `(g,k)=(2,1)`,

`2B_max=eps-p^2+9 <= 10-p^2`,

so `B>=0` forces `p<=3`.

Thus

> **R/Fz0: `p<=3`.**                                      `(X3-R-P3)`

Moreover

`2B=2B_max-[omega-(5-p)]^2`.

For the surviving p/g choices this gives the uniform integer bound

> **R/Fz0: `omega<=5`.**                                  `(X3-R-W5)`

Since mixed y=1 has

`n=x+2p+k+omega+3`,

we obtain

> **R/Fz0: `n<=16`.**                                     `(X3-R-N16)`

### 4.2 Exceptional Fz

Here

`2B_max=eps+4g-k^2-2kp+4k-p^2+2p-6`.

For `(g,k)=(1,2)`,

`2B_max=eps-p^2-2p+2<0`

for every `p>=2`, so this alternative is impossible.

For `(g,k)=(2,1)`,

`2B_max=eps-p^2+5`,

so `B>=0` forces `p=2`. The completed square has the same centre `5-p=3`, and `2B_max<=2`, hence

> **exceptional Fz: `(g,k,p)=(2,1,2)`, `omega<=4`, and `n<=15`.** `(X3-FZ1-N15)`

(The physical exceptional-Fz geometry also has `omega>=3`; this is not needed for the upper bound.)

### 4.3 Fx

Using the same safe rooted-floor relaxation as the predecessor,

`2B_max<=eps+2g-k^2-2kp+4k-p^2+2p+1`.

For `(g,k)=(1,2)`, this is

`eps-p^2-2p+7`,

and for `(g,k)=(2,1)` it is

`eps-p^2+8`.

With `p>=2`, any survivor has `p<=3`; but when `p=3`, the square centre `x-p+1=1` lies below the physical `omega>=2`, and the maximum available at integer `omega>=2` is negative. Hence actually

> **Fx: `p=2`.**                                          `(X3-FX-P2)`

The completed-square centre is `4-p=2`, and the surviving alternatives give

> **Fx: `omega<=4`, hence `n<=15`.**                       `(X3-FX-N15)`

## 5. x=3 conclusion

Combining R, no-exception Fz, exceptional Fz and Fx:

> **X3 MIXED-y=1 FINITE-ORDER CLOSURE.**
>
> In the exact mixed second-strict branch with `p>=2`, `x=3`, every survivor satisfies
>
> **`n<=16`.**                                             `(X3-N16)`

This is analytic. The only finite evaluation is over the two exact possibilities `g=1,2`, not graph enumeration.

Together with the predecessor results:

- `x>=5`: `n<=33`;
- `x=4`: `n<=19`;
- `x=3`: `n<=16`;
- `p=1`: impossible;

we obtain the stronger mixed-y=1 synthesis

> **every exact mixed second-strict y=1 survivor has `n<=33`.** `(MIX-Y1-N33-ALL)`

Combined further with the already-internal `y>=2` mixed closure, the impossible `(0,2)` arm, and the two-X-hole bound `n<=816`, the current same-session chain yields:

> **conditional on the rigid one-code interface and the predecessor closures, the entire exact unloaded second-strict layer has no survivor for `n>=817`.** `(SECOND-STRICT-N817)`

This is a branch theorem, not a global D2C theorem. It remains subject to independent adversarial replay, and the zero-positive-rigid-cut fixture gap remains the dominant global risk.

## 6. What this changes strategically

The small-head mixed tail is no longer the asymptotic frontier. Before opening a third buffer-defect scalar programme, the daily audit's dominant interface obligation should regain priority: either produce an actual D2C graph realizing the rigid complete Hall-cut interface with `x>=3`, or prove a structural no-go theorem explaining why the bounded regression sees none. The new `(SECOND-STRICT-N817)` result is worth preserving because it says that *if* the rigid branch is reachable, exact unloaded buffer defect two is already finite-order.