# Second-strict mixed y=1 tail — case-specific physical U-side bills

Date: 2026-09-20

Status: **same-session internal structural continuation** of `SECOND_STRICT_Y1_HOSTILE_EXTENSION.md`. All statements remain conditional on the audited rigid one-code complete-cut interface and on the large-head hypotheses `p>=2,x>=5`.

Use the mixed second-strict notation `k=x-g`, `omega=|U_o|`, `U_o^*=U_o\{z_0}`, and `u=k+1+omega`. In every large-head `y=1` case established so far, `G[X]=emptyset`.

## 1. R case — ordinary outside independence and at most one z_0--U_o^* edge

In case R all X has one radius-one code `C`, every ordinary outside vertex certifies a C-head and hence has code `D=bar C`, while `c(z_0)=bar d`, `N_X(z_0)={a_0}`, and `z_0y notin E`.

### Ordinary outside vertices are independent

A hypothetical same-code edge `ww'` in `U_o^*` must, by the independently audited same-code theorem, use a complementary C-coded A-witness.

- `a_0` is adjacent to every ordinary Type-R outside witness and cannot distinguish the U-edge;
- every C-coded buffer head is adjacent to `b`, while the U-source is also adjacent to b, so b is an extra common neighbour.

Hence `G[U_o^*]` is edgeless.

### z_0 has at most one ordinary outside neighbour

Suppose `z_0w in E`, `w in U_o^*`. The codes `bar d` and D differ only in the unique coordinate `j=S_0`.

For orientation `w -> z_0`, the only matched endpoint capable of distinguishing the codes is `q_j`; but both `w` and `q_j` are adjacent to `a_0`, so `a_0` is an extra common neighbour. A U-witness is impossible for a U-source because the root would be an extra common neighbour, and the remaining A/root locations fail by adjacency or tight-code common neighbours.

For orientation `z_0 -> w`, the only surviving matched possibility is the d-side endpoint `r_j`. Every A-witness of code C shares the tight `q_j` endpoint with z_0, and U-witnesses again fail through the root. Consequently any such edge must satisfy

`N(z_0) cap N(r_j)={w}`.

The pair `(z_0,r_j)` is graph-fixed, so this can hold for at most one ordinary outside head. Therefore

> `d_{U_o^*}(z_0)<=1`.                                    `(R-ZU1)`

Since `U_-` and `U_o^*` are independent, `bz_0` is absent, and the only possible internal U_o edge is this single z_0-edge,

> `q<= (k+1)omega`.                                       `(R-Q)`

For ordinary outside slack, at most one w can see z_0. Thus at least `omega-2` ordinary vertices have all `omega-1` other U_o vertices as U-nonneighbours, while a possible exceptional neighbour still misses the other `omega-2` ordinary vertices. Since every ordinary witness has A-degree at most `x-1`,

> `E(U_o^*) >= (omega-2)[p-x+omega]_+ + [p-x+omega-1]_+`. `(R-UO-PAY)`

Also `epsilon_{z_0}>=p+omega-2`.

## 2. Fz with no higher-radius head — the entire U_o layer is independent

Here all X has code C and every vertex of `U_o`, including z_0, has code D. The defining Fz singleton is

`N(a_0) cap N(z_0)={y}`.

A same-code U-U edge must use a C-coded A-witness. For an edge involving two ordinary vertices, `a_0` sees both while every buffer-head witness has b as an extra common neighbour. For an edge `z_0w`, the candidate `a_0` has the wrong singleton (`{y}` rather than `{w}`); a buffer-head C-witness either shares y with z_0 or b with the ordinary U-source. Hence

> `G[U_o]=emptyset`.                                      `(FZ0-UO0)`

A direct raw-criticality check of a hypothetical edge `z_0x`, `x in X\{a_0}`, shows that orientation `x -> z_0` is impossible, while orientation `z_0 -> x` can only use the unique matched endpoint `q_j`. Therefore the graph-fixed pair `(z_0,q_j)` gives

> `d_X(z_0)<=1`.                                          `(FZ0-ZX1)`

Consequently

> `q<= (k+1)omega-1`,                                     `(FZ0-Q)`
>
> `epsilon_{z_0}>=p+omega-2`,                             `(FZ0-ZPAY)`
>
> `E(U_o^*) >= (omega-1)[p-x+omega]_+`.                  `(FZ0-UOPAY)`

The first inequality subtracts the physical b--z_0 hole from the complete `U_-`--`U_o` bipartite maximum.

## 3. Fx — U_o is independent and the exceptional D-head is physically expensive

In Fx the unique complementary X-vertex `t` witnesses `a_0 -> y`, so

`N(a_0) cap N(t)={y}`.

It is also the unique reverse buffer head, with

`c(z_0)=d`, `N(b) cap N(z_0)={t}`.

All ordinary outside vertices certify C-heads and have code D. They form an independent set by the same same-code/b-extra-neighbour argument as above. The singleton `N(b) cap N(z_0)={t}` forces `z_0` to miss every ordinary outside vertex because each is adjacent to b. Therefore

> `G[U_o]=emptyset`, and `q<=(k+1)omega-1`.               `(FX-UO0)`

Moreover every ordinary outside vertex is adjacent to a_0 (Type R). Since `N(a_0) cap N(t)={y}`, the exceptional head t must be anticomplete to all of `U_o^*`. This gives a much stronger t-price than the naive X-degree count:

> `epsilon_t >= p+k+omega-3`.                             `(FX-T-PAY)`

Together with

- `epsilon_{a_0}>=p+k+1`,
- every ordinary C-head `x` satisfying `epsilon_x>=p+k`,

we obtain

> `L_X >= x(p+k)+omega-2`.                                `(FX-LX)`

For the outside layer,

> `epsilon_{z_0}>=p+omega-2`,
>
> `E(U_o^*) >= (omega-1)[p-x+omega]_+`.                  `(FX-UOPAY)`

## 4. Exceptional Fz — two outside code classes and convex self-pricing

If the unique higher-radius Fz head h exists, the previous hostile extension proves

`N_X(z_0)={h}`, `N_Y(z_0)={y}`, `N_U(z_0)=emptyset`,

so

`epsilon_{z_0}>=p+k+omega-2`.

The ordinary outside vertices split into exactly two possible code classes:

- D-witnesses certifying radius-one C-heads;
- E=`bar c(h)` witnesses certifying h.

Both classes are nonempty: at least one C-head exists because `x>=5`, and h itself requires an outside certificate. Put their physical sizes `alpha,beta>=1`, with

`alpha+beta=omega-1`.

Within each code class, U-U edges are impossible by the same-code theorem and the buffer/source singleton obstruction. In addition z_0 is anticomplete to all ordinary outside vertices. Hence an alpha-class vertex has at least alpha U_o nonneighbours (z_0 plus its `alpha-1` class-mates), and a beta-class vertex has at least beta. Each ordinary outside certificate has A-degree at most `x-1`. Therefore

> `E(U_o^*) >= alpha[p-x+1+alpha]_+ + beta[p-x+1+beta]_+`. `(FZ1-UOPAY)`

All possible internal U_o edges run between the two classes, so

> `q <= (k+1)(omega-1)+alpha beta`.                       `(FZ1-Q)`

In particular `omega>=3` and the outside-reservoir price is convex/quadratic once either class becomes large.

## 5. Consequence for the next exact optimization

The large-head mixed y=1 problem has now been reduced to case-specific integer resource systems with `e(X)=0`:

- R: `(R-Q)` and `(R-UO-PAY)`;
- no-exception Fz: `(FZ0-Q)`, `(FZ0-ZPAY)`, `(FZ0-UOPAY)`;
- Fx: `(FX-UO0)`, `(FX-T-PAY)`, `(FX-LX)`, `(FX-UOPAY)`;
- exceptional Fz: the explicit two-class variables `alpha,beta` with `(FZ1-UOPAY)` and `(FZ1-Q)` plus the stronger rooted floor `r>=x+2`.

The next step should solve these necessary systems exactly against the standard score cap and rooted identity, preserving `alpha,beta` in the exceptional Fz arm rather than replacing them immediately by a balanced relaxation. Finite checks may be used to locate the surviving scaling regime, but not as proof of nonrealizability.