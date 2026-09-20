# Second-strict mixed y=1 tail — hostile extension and Fz internal-X closure

Date: 2026-09-20

Status: **same-session internal structural mathematics**, conditional on the audited rigid one-code complete-cut interface. This note audits and strengthens `SECOND_STRICT_MIXED_Y1_CLASSIFICATION.md`; it does not repair the independent zero-positive-rigid-cut fixture gap. `X_3` remains the mandatory negative control and is outside this unmatched branch.

## 1. Audit reconciliation

The binding daily audit remains `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Before forward work I reread `CURRENT_STATE.md`, root `README.md`, the daily audit, and the three newer second-strict commits beyond the stale handoff:

- `c4c117686614c37d70eea8775a2dc151eb373ede` — mixed `(1,1)` closure for `y>=2`;
- `3d06a2b7b0d558681fd8d72a37abca507580d78b` — two-X-hole two-foot/core-saturation normal form;
- `114c050f1e409633f66d7b24089c1397450d21d5` — large-head `y=1` mixed classification.

The first of these was independently checked at its most algebraically fragile point. Substituting

`u=x+omega`, `lambda=2p+omega-1-y`, `n=1+(x+y)+(2p+u)`

into its definitions of `C0`, `A`, and `B` reproduces exactly

`4B+A=-(F+2P)/2`.

A separate direct integer replay of the exceptional `p=2`, `omega=2,3,4` positivity cases agrees with the note. No algebraic mismatch was found. This does not by itself audit every preceding witness-location exclusion, but it removes an arithmetic-risk point from the `y>=2` closure.

The `y=1` trichotomy for the edge `a_0y` was also reread location by location. No missing obvious root/core/ordinary-outside channel was found. The three live cases remain:

- `R`: `c(z_0)=bar d`, `z_0a_0 in E`, `z_0y notin E`;
- `Fx`: a unique complementary X-head `t` witnesses `a_0 -> y`, with `c(z_0)=d` and `N(b) cap N(z_0)={t}`;
- `Fz`: `z_0` itself witnesses `a_0 -> y`, with `c(z_0)=D=bar C`, `z_0a_0 notin E`, `z_0y in E`, and `N(a_0) cap N(z_0)={y}`.

Throughout the large-head tail `p>=2`, `x>=5`, and the earlier exceptional-capacity theorem gives `S_0={j}`. Put `C=c(a_0)` and `D=bar C`.

## 2. Failed attack that must be preserved — the Fz exceptional head self-certifies

The predecessor leaves at most one higher-radius Type-R head `h` in case Fz. If it exists, `|S_h|>=2` and the matched edge at the unique coordinate `j in S_0` forces

`z_0h in E`,

`N(q_j) cap N(z_0)={h}`,

where `q_j` is the `bar d` endpoint in fibre `j`.

A tempting next attack is to reapply raw criticality to the edge `z_0h`. That does **not** create a contradiction: the same matched vertex `q_j` immediately certifies the orientation

`z_0 -> h`,

because `z_0q_j notin E` and the already-forced singleton is exactly `N(z_0) cap N(q_j)={h}`.

Likewise the edge `z_0y` in Fz recycles `a_0` as its raw certificate because `z_0a_0 notin E` and `N(z_0) cap N(a_0)={y}`.

Thus iterating criticality on either of these two certificate edges is a dead route. This is structurally the same “certificate recycling” obstruction seen earlier in the project and must not be counted as a new obligation.

## 3. Exceptional Fz geometry — exact isolation of z_0

Assume the higher-radius head `h` exists.

The singleton

`N(q_j) cap N(z_0)={h}`

has immediate physical consequences.

1. Every Type-R buffer head has `j in S_x`, hence is adjacent to `q_j`. Therefore `z_0` is nonadjacent to every X-head except `h`.
2. Every common-core vertex has code `bar d` and is adjacent to `q_j`. Therefore `z_0` is anticomplete to `W_0`.
3. `z_0b notin E` by the mixed-hole hypothesis.
4. Every ordinary outside vertex is itself a Type-R outside certificate and is adjacent to `a_0`. Since `N(a_0) cap N(z_0)={y}`, `z_0` is anticomplete to `U_o^*=U_o\{z_0}`.
5. `z_0a_0 notin E` and `z_0y in E` by Fz.

Hence in the exceptional Fz geometry

> `N_X(z_0)={h}`, `N_Y(z_0)={y}`, and `N_U(z_0)=emptyset`. `(FZ-Z0-ISO)`

Writing `omega=|U_o|` and `k=|W_0|`, the U-vertex slack formula gives the exact lower bound

> `epsilon_{z_0} >= p+k+omega-2`.                         `(FZ-Z0-PAY)`

No finite scan is involved.

## 4. The C-class is independent in every Fz geometry

All ordinary radius-one X-vertices have code `C`. Consider a hypothetical edge between two such C-vertices.

By the independently re-derived same-code theorem, any certificate must have complementary code `D`.

- An ordinary `D`-coded outside witness is adjacent to `b`, while both buffer-head endpoints are also adjacent to `b`; this gives an extra common neighbour.
- The exceptional vertex `z_0` has code `D`, but it is adjacent to `y`, and every C-source is adjacent to `y`; if `z_0` is used as the complementary witness, `y` is an extra common neighbour.
- There is no other A-vertex of code `D` in the Fz classification.

Therefore

> the radius-one C-class induces no edges.                `(FZ-C-INDEP)`

This covers both the no-exception and one-higher-radius Fz subcases.

## 5. New raw-criticality closure — the exceptional h has no C-neighbour

Assume again that the unique higher-radius head `h` exists, and let `x` be any radius-one C-vertex. Suppose `hx in E`.

The codes satisfy `S_C={j}` and `S_h={j} union T` with nonempty `T`. We exhaust both raw orientations of the triangle edge `hx`.

### Orientation `x -> h`

A witness must be adjacent to `h`, nonadjacent to `x`, and have singleton common neighbourhood `{h}` with `x`.

- Any X- or Y-witness shares `y` with `x`.
- `z_0` is adjacent to `h` and nonadjacent to `x`, but `z_0y,x y in E`, so `y` is an extra common neighbour.
- Any ordinary outside vertex is adjacent to `b`; since `xb in E`, `b` is an extra common neighbour whenever such a vertex is adjacent to `h`.
- A common-core vertex with head `h` has code `bar d`; it shares the tight endpoint `q_j` with the C-source `x`, so the common neighbourhood is not singleton.
- A tight matched vertex distinguishing `h` from `C` occurs at some `i in T`; the `bar d` endpoint `q_i` is adjacent to `b`, again giving the extra common neighbour `b` with the source `x`.
- The root is not an admissible witness for an A-source/head edge.

Thus this orientation is impossible.

### Orientation `h -> x`

Now a witness must be adjacent to `x`, nonadjacent to `h`, and have singleton common neighbourhood `{x}` with `h`.

- X/Y witnesses again share `y` with `h`.
- `z_0` is not adjacent to `x`.
- An ordinary outside witness adjacent to `x` is a b-neighbour, while `hb in E`, giving extra common neighbour `b`.
- The common-core vertex whose head is `x` has code `bar d`; it shares every tight `bar d` endpoint indexed by `S_h`, in particular at least the coordinates `j` and one element of `T`, with `h`.
- A matched endpoint adjacent to `x` and not `h` occurs at an `i in T` on the d-side; it is adjacent to `y`, and `hy in E`, so `y` is an extra common neighbour.

Thus the reverse orientation is impossible as well.

Contradiction. Therefore

> `E({h}, X_C)=emptyset`.                                 `(FZ-H-C0)`

Together with `(FZ-C-INDEP)` and the inherited Type-R relation `a_0--X'=emptyset`, this proves the new global conclusion

> **`G[X]` is edgeless in case Fz, even when the unique higher-radius head exists.** `(FZ-X0)`

The predecessor had already proved `G[X]=emptyset` in cases R and Fx. Hence:

> **Every large-head (`p>=2,x>=5`) mixed second-strict y=1 geometry has `G[X]=emptyset`.** `(Y1-X0-ALL)`

## 6. Rooted-slot consequence

Because `Y={y}`, every X-vertex is adjacent to y and has code different from d. With `G[X]=emptyset`, each X-vertex has at least one unused rooted slot.

- In R and in Fz with no higher-radius head, all X-codes have radius one, and `r_y>=1`; hence `r>=x+1`.
- In Fx, the predecessor's sharper bound remains

  `r>=x+p-2+ceil((x+p-2)/x)`.

- In exceptional Fz, if `s=|S_h|>=2`, the Y-source Hamming load is `(x-1)+s>x`, so `r_y>=2`; hence

> `r>=x+2`.                                                `(FZ-RLOW+)`

This is a genuine one-unit jump over the no-exception Fz arm.

## 7. Additional physical normalization of the ordinary outside layer

In cases R and Fz without a higher-radius head, every ordinary outside vertex has code D because every buffer head has code C. The ordinary outside layer is independent: a same-code U-U edge would require a C-coded A-witness; `a_0` is adjacent to every ordinary Type-R witness and cannot distinguish the edge, while every buffer-head C-witness has `b` as an extra common neighbour with the U-source.

In Fx the same conclusion holds for `U_o^*`: all outside-certified heads have code C, so every ordinary outside witness has code D. Moreover `N(b) cap N(z_0)={t}` and every ordinary outside vertex is adjacent to b, hence `z_0` is anticomplete to `U_o^*`.

Thus the R/Fx/no-exception-Fz tails have much smaller U-side edge capacity than an unrestricted outside reservoir. The exceptional-Fz tail may contain two outside code classes (`D` and `bar c(h)`), so only the within-class independence and the complete `z_0--U_o^*` nonadjacency from `(FZ-Z0-ISO)` are asserted here.

## 8. Live frontier

After this hostile extension, the large-head mixed y=1 tail has no internal X density left to exploit: **all three cases have `e(X)=0`**.

The remaining work is therefore arithmetic/physical rather than another X-edge classification:

1. substitute `e(X)=0`, the case-specific z_0 slack, and the reduced U-edge capacity into the exact rooted identity and score cap;
2. first try to close the exceptional-Fz arm using `(FZ-Z0-PAY)` and `(FZ-RLOW+)`;
3. then treat the all-radius-one R/Fz arms together where possible;
4. keep `x=3,4` as explicit small-head tails rather than contaminating the large-head algebra.

The separate exact-second-strict two-X-hole branch remains live and is governed by `SECOND_STRICT_TWO_X_HOLE_NORMAL_FORM.md`.