# All-R one-witness equality pinch: located holes, exact outside-neighbour tradeoff, and Hall feedback

Date: 2026-09-19

Status: **internal conditional structural theorem package** inside the independently repaired first-strict unloaded one-code common-buffer branch. This note starts from the one-witness equality pinch in `ONE_WITNESS_POLARIZATION_PINCH.md`. It does not assert graph realizability or a global eventual theorem. The order-12 hostile control `X_3` remains outside these positive-U hypotheses.

## 1. Audit reconciliation and equality-pinch setup

The live 19 September adversarial-audit boundary remains binding: raw physical-source distinctness and selected `(source,coordinate)` uniqueness retain their repaired meanings; `X_3` remains mandatory; exact pair-local `Ccap_P`, `(ONE-P)`, and `(CROWD)` remain active; finite scans are diagnostics only.

Work in the unique `m=1` all-R model that can avoid the previously proved `r>=a+y` surcharge. Thus:

- `A=X dotcup Y`, `|X|=x>=3`, `|Y|=y>0`, and `X--Y` is complete;
- every vertex of `X` has one common tight code `C`, every vertex of `Y` has code `d), and `d_H(C,d)=1`;
- write `a_0` for the unique buffer non-neighbour in X and `X'=X\{a_0}`, `N=x-1`;
- `a_0` is isolated in `G[X]`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`, every vertex of `U_-` has code `bar d`, and `b` is adjacent to every vertex of `X'`;
- the unique selected outside witness is `z in U_o`, with `c(z)=bar C`, `N_A(z)={a_0}`, and for every `x in X'`,
  `N(x) cap N(z)={b}`;
- let `S_0={j_*}` be the unique coordinate where C differs from d, and `I_0=[p]\{j_*}`;
- for every `i in I_0`, if `q_i` is the matched endpoint selected by `bar d`, the reverse funnel gives
  `N(q_i) cap N(a_0)={z}`.

Put `u_o=u-k-1=|U_o|`. The branch requires `u_o>=1`.

## 2. Unit I — the unique hole misses the entire common core

### Theorem 2.1 — core exclusion at a_0

`a_0` is nonadjacent to every vertex of `W_0`.

### Proof

Fix `w in W_0` and any `i in I_0`. Since `c(w)=bar d`, the vertex w is adjacent to the matched endpoint `q_i`. If `a_0w` were also an edge, w would lie in `N(q_i) cap N(a_0)`, contradicting the graph-fixed singleton identity

`N(q_i) cap N(a_0)={z}`.

Hence `a_0--W_0` is empty. `square`

Because `ba_0` is already the unique buffer-X hole and `a_0` has no X-neighbour, direct degree counting gives the stronger slack floor

> `epsilon_{a_0} >= p-y+k+1`.                         `(A0+K)`

This improves the inherited `p-y+1` floor by exactly k.

## 3. Unit II — U-neighbours of a_0 have only two possible codes

### Theorem 3.1 — a_0 neighbour-code localization

If `w in U\{z}` and `a_0w in E`, then

> `c(w) in {d,C}`.                                     `(A0-CODE)`

### Proof

For every `i in I_0`, the singleton relation
`N(q_i) cap N(a_0)={z}`
forbids w from being adjacent to `q_i`. Therefore `c(w)_i=d_i` for every `i in I_0). At the single remaining coordinate `j_*`, w may choose either endpoint. These are exactly the codes d and C. `square`

In particular every `bar d)-coded core vertex and every `bar C)-coded U-vertex other than z is nonadjacent to `a_0`.

## 4. Unit III — z misses all k core vertices

The common-core head map `h:W_0->X` is injective and every core vertex has exactly one X-neighbour. By Theorem 2.1, no core head equals `a_0`; hence every core head lies in `X'`.

For each `w in W_0`, let `x=h(w) in X'`. Since z is the selected outside witness for every buffer neighbour,

`N(x) cap N(z)={b}`.

If `wz` were an edge, w would be a second common neighbour of x and z. Therefore:

> `z--W_0` is empty.                                   `(Z-CORE)`

Consequences:

1. the common-core hole count satisfies
   > `H_core=e_bar(W_0,U_o) >= k`;
2. the exact common-core slack identity sharpens to
   > `E_core >= k(p+k)`;                               `(CORE+)`
3. since `N_A(z)={a_0}`, the exact number of U-nonneighbours of z is
   `epsilon_z-(p-1)`, so
   > `epsilon_z>=p+k-1`;
4. the rooted triangle ceiling improves to
   > `q <= binom(u,2)-binom(k+1,2)-k`
   before any further z--U_o holes are counted.

This removes the weak historical `chi=1` option from the literal equality pinch.

## 5. Unit IV — exact outside-neighbour / z-slack tradeoff

Because z is adjacent to b, nonadjacent to all k core vertices, and has no other possible U-locations outside `W_0 dotcup {b} dotcup U_o`, there is a unique integer

> `0<=d<=u_o-1`

such that z is nonadjacent to exactly d vertices of `U_o\{z}`.

Equivalently,

> `epsilon_z=p+k-1+d`,                                 `(Z-EPS)`
>
> `J:=|N_U(z) cap (U_o\{z})|=u_o-1-d`.                `(J-EXACT)`

The k+d nonedges incident with z are disjoint from the internal nonedges of the independent set `U_-=W_0 dotcup {b}`, so

> `q <= q_max(d):=binom(u,2)-binom(k+1,2)-k-d`.        `(Q-d)`

Thus every unit of relief from the outside-neighbour fanout below is paid simultaneously by one extra unit of `epsilon_z` and one additional physical U--U nonedge.

## 6. Unit V — every other U-neighbour of z creates an X' hole rectangle

### Theorem 6.1 — outside-neighbour rectangle

If `w in U\{b,z}` and `zw in E`, then w is nonadjacent to every vertex of `X'`.

### Proof

For each `x in X'`, the fixed certificate relation is

`N(x) cap N(z)={b}`.

If xw were an edge while zw is an edge and `w!=b`, then w would be a second common neighbour of x and z. `square`

Restricting to the J vertices of `N_U(z) cap (U_o\{z})` gives J disjoint outside-U columns, each missing all N vertices of `X'`.

The already-forced A--U nonedges from the core, buffer and z themselves are disjoint from these columns. Hence

> `Z >= Z_0+NJ`,                                       `(Z-RECT)`
>
> `Z_0=(k+1)(a-1)+y+1`.

On the X-side alone,

> `Z_X >= Z_X^0+NJ`,                                   `(ZX-RECT)`
>
> `Z_X^0=(k+1)N+1`.

The extra `+1` in both baselines is the physical hole `ba_0`.

Every one of the J outside vertices misses N=x-1 A-vertices. For a U-vertex,
`d_{A union U}=p+u-1-epsilon`; therefore each such vertex has

> `epsilon_w >= g_1:=[p-y-1]_+`.                       `(J-SLACK)`

So the rectangle is not merely an incidence count: unless `p-y=1`, it also produces U-slack.

## 7. Unit VI — internal X-edges require new bar-C witnesses

All X-vertices have code C and `a_0` is isolated in `G[X]`, so every internal X-edge lies in `G[X']`.

The full coded-layer same-code criticality theorem says that each such edge has a complementary-code witness. Here `A_{bar C}=emptyset` (for `p>=2`), so the witness lies in `U_{bar C}`.

The distinguished witness z cannot certify any edge of `G[X']`: for every source `x in X'` its common neighbourhood with z is the fixed singleton `{b}`, whereas an internal-X edge certificate would require the other X-endpoint as singleton head.

Let

> `t=|U_{bar C}\{z}|`.

Mapping each internal X-edge to its ordered `(source,witness)` pair is injective, and every possible source lies in `X'`. Therefore

> `e(X) <= Nt`.                                        `(X-CAP)`

In particular

> `t >= ceil(e(X)/N)` whenever `e(X)>0`.              `(TBAR)`

### Theorem 7.1 — an adjacent additional bar-C vertex is A-anticomplete

If `w in U_{bar C}\{z}` and `zw in E`, then `N_A(w)=emptyset`, hence

> `epsilon_w>=p`.                                      `(BAR-PAY)`

### Proof

By Theorem 3.1, w is nonadjacent to `a_0`; by Theorem 6.1 it is nonadjacent to all of `X'`. Thus w is anticomplete to X.

The edge zw is a same-code U--U edge. The same-code criticality theorem requires its witness to lie in `A_C=X`.

An orientation with source z is impossible: the witness must be nonadjacent to z, hence lie in `X'`, but w has no X'-neighbour and therefore cannot be the singleton head.

In the opposite orientation the singleton head is z. The witness must be an X-vertex adjacent to z; the only such vertex is `a_0`. Hence necessarily

`N(w) cap N(a_0)={z}`.

Since `a_0` is adjacent to every vertex of Y, w is anticomplete to Y as well. Thus w is anticomplete to all A, and a U-vertex with no A-neighbours has slack at least p. `square`

At most d of the t additional `bar C)-vertices can be nonadjacent to z. Therefore at least

> `[t-d]_+`

of them pay the p-slack floor. Since those vertices are already among the J rectangle vertices, whose generic floor is `g_1`, the additional U-slack surcharge is

> `(p-g_1)[t-d]_+`.                                    `(BAR-UPGRADE)`

## 8. Unit VII — exact Hall feedback on the C-code block

The family `A_C=X` has complete cut to Y, so its missing-cut term is zero. The exact Hall-density identity therefore reduces to

> `2e(X)=x(p-y)-L_X+Z_X`.                              `(H-X)`

Let `C_0` be the above-threshold total score cap. Since

`E_U+L_A<=C_0`

and `L_X<=L_A`,

> `L_X<=C_0-E_U`.

For fixed d and t define

`J=u_o-1-d`,

`E_base(d)=k(p+k)+(p-g+1)+(p+k-1+d)+J g_1`,

and

> `E_min(d,t)=E_base(d)+(p-g_1)[t-d]_+`.               `(EU-min)`

This counts disjoint U-vertex slack contributions from:

- the exact common core;
- the first-strict buffer;
- z;
- the J outside-neighbour rectangle vertices;
- the extra upgrade for adjacent additional `bar C)-vertices.

Combining `(H-X)`, `(ZX-RECT)`, and `L_X<=C_0-E_U` gives the necessary internal-edge demand

> `2e(X) >= x(p-y)+Z_X^0+NJ-C_0+E_min(d,t)`.           `(H-demand)`

But simultaneously

> `e(X)<=min{binom(N,2),Nt}`.                           `(H-cap)`

Therefore every equality-pinch survivor must admit integers

> `0<=d<=u_o-1`, `0<=t<=u_o-1`

such that

> `2 min{binom(N,2),Nt}`
> ` >= x(p-y)+Z_X^0+NJ-C_0+E_min(d,t)`.                `(H-PINCH)`

This is the desired local feedback loop:

`z-U adjacency -> X'-U hole rectangle -> Hall-forced e(X) -> extra bar-C witnesses -> U-slack`.

## 9. Unit VIII — adjacent additional bar-C witnesses form an independent set

Let

> `B={w in U_{bar C}\{z}: zw in E}`, `r_B=|B|`.

By the preceding argument every vertex of B is anticomplete to A.

### Theorem 9.1 — bar-C star leaves are independent

> `G[B]` is edgeless.                                   `(B-INDEP)`

### Proof

Suppose `w_1w_2` were an edge in B. It is a same-code U--U edge, so the full coded-layer criticality theorem requires a witness in the complementary A-class `A_C=X`, regardless of which endpoint is chosen as source. But the singleton head is the other endpoint, and both `w_1,w_2` are anticomplete to X. Hence no orientation can place the other endpoint in the required common neighbourhood. Contradiction. `square`

For a fixed d and a total of t additional `bar C)-vertices, at least

> `r_B>=[t-d]_+`

are adjacent to z. Their pairwise nonedges are disjoint from:

- the internal nonedges of `U_-`;
- the k edges missing between z and `W_0`;
- the d edges missing between z and the remaining outside vertices.

Therefore the triangle ceiling strengthens to

> `q <= binom(u,2)-binom(k+1,2)-k-d-binom([t-d]_+,2)`. `(Q-BAR)`

This is a physical U-edge exclusion, not a witness-incidence count.

## 10. Unit IX — criticality bounds the U-degree of a_0 through the bar-C reservoir

The neighbour-code localization `(A0-CODE)` says that every U-neighbour of `a_0` other than z has code d or C. The same extra `bar C)-population that supports internal X-edges also limits both possibilities.

Let again

> `t=|U_{bar C}\{z}|`.

### Lemma 10.1 — C-coded U-neighbours of a_0

> `|N_U(a_0) cap U_C| <= t`.                            `(A0-C-CAP)`

### Proof

For `w in U_C` with `a_0w in E`, the edge has equal-code endpoints. If w is chosen as source, the full coded-layer same-code theorem requires its witness to lie in `A_{bar C}`, but that A-class is empty. Hence the source must be `a_0`.

Because `a_0` and w have the same tight code, no matched endpoint can be adjacent to w while nonadjacent to `a_0). Any A/U witness must have code `bar C`. The distinguished z is adjacent to `a_0` and therefore cannot be the nonadjacent source-witness partner. Thus the witness lies in `U_{bar C}\{z}`.

For fixed source `a_0` and fixed witness, the singleton common neighbourhood determines at most one head w. Therefore the t available witnesses certify at most t such neighbours. `square`

### Lemma 10.2 — d-coded U-neighbours of a_0

> `|N_U(a_0) cap U_d| <= t+1`.                          `(A0-d-CAP)`

### Proof

Let `w in U_d` be adjacent to `a_0`. The codes C and d differ only at the special coordinate `j_*`.

An orientation with U-source w cannot use a U or matched-B witness because both would share the root with w. An A-witness would have to avoid every matched neighbour of w and therefore have code `bar d), but `A_{bar d}=emptyset`. So the U-source orientation is impossible.

With source `a_0`, an A/U witness must have complementary code `bar C) and be nonadjacent to `a_0), giving at most the t vertices of `U_{bar C}\{z}`. There is exactly one additional matched-B possibility: the endpoint in the special fibre selected by d and not by C. Every other matched endpoint is adjacent to both source and head and cannot be the nonadjacent witness.

Again a fixed source-witness pair can determine at most one singleton head. Thus there are at most t+1 d-coded U-neighbours. `square`

Since z itself is one U-neighbour of `a_0`, these two lemmas give

> `d_U(a_0)<=2t+2`.                                     `(A0-UDEG)`

As `a_0` has no X-neighbour and is complete to Y,

> `epsilon_{a_0}>=p+u-y-2t-2`.                         `(A0-t)`

Together with `(A0+K)`, every survivor must use the dynamic floor

> `epsilon_{a_0}>=A_0(t):=max{p-y+k+1, p+u-y-2t-2}`.   `(A0-DYN)`

This is a second conservation law: a small complementary witness reservoir forces `a_0) to lose U-degree directly.

## 10. Unit X — pair, triangle and residual gates retained simultaneously

The exact pair-local threshold must be recomputed using the strengthened core floor `E_core>=k(p+k)`, not the old weak `k(p+k)-1`.

Let `Sigma_P^+(1)` be the least pair score satisfying:

1. `S_P>=k(p+k)+(p-g+1)+y(p-g+2)`;
2. `(CROWD)`;
3. exact `Ccap_P(S_P)>=2xy`.

The outside-pair score then gives

> `Sigma_P^+(1)+epsilon_z+epsilon_{a_0}<=C_0`.         `(PAIR+)`

Also put

`L_Y=y(p-g+2)`,

`A_min=max{phi(g),L_Y+(p-y+k+1)}`,

so

> `E_U<=E_U^max:=C_0-A_min`.                            `(EU-max)`

For a chosen d, retain all three necessary checks:

> `E_min(d,t)<=E_U^max`;                                `(EU-feas)`
>
> `2q_max(d)+E_U^max >= Z_0+NJ-u(p-lambda)`;           `(Z-feas)`
>
> `(p-lambda)(p+u)+q_max(d)+E_U^max>=a`.               `(R-feas)`

The last condition is the inherited equality-pinch rooted-slot requirement `r>=a`.

No total-score substitution is made for the pair-local crossing threshold.

## 12. Diagnostic replay

A companion checker evaluates only the necessary system above on the same abstract box used by the predecessor pinch diagnostic:

`3<=p<=18`, `1<=u<=18`, `lambda>=0`.

It first exactly reproduces the predecessor corrected one-witness count:

- coarse rows: **248,798**;
- predecessor equality-pinch final rows: **173,347**.

It then applies the hand theorems in this note, including the strengthened `a_0--W_0` and `z--W_0` exclusions, exact d/J tradeoff, same-code complementary-witness capacity, and Hall feedback.

The resulting abstract final count is:

> **133,317**.

Thus **40,030** predecessor abstract pinch rows fail the new necessary system.

These are parameter rows, not graphs. The zero-survivor question is not answered by this scan; the value of the replay is to identify which literal resource geometry remains after the local hand deductions.

## 13. Trust boundary and next move

Promoted conditionally inside the audited equality pinch:

1. `a_0--W_0` is empty;
2. `N_U(a_0)\{z}` uses only codes d or C;
3. `z--W_0` is empty, hence `H_core>=k`;
4. the d/J outside-neighbour tradeoff is exact;
5. every z-neighbour in `U_o\{z}` is anticomplete to `X'`;
6. additional adjacent `bar C)-vertices are anticomplete to all A and pay `epsilon>=p`;
7. internal X-edge mass requires additional `bar C) witnesses;
8. adjacent additional `bar C` witnesses form an independent U-set and strengthen the q ceiling by `(Q-BAR)`;\n9. `(H-PINCH)` is an exact Hall/criticality necessary condition when combined with the stated score floors.

The next hand target should stay inside the remaining equality-pinch rows and classify near equality in `(H-PINCH)`. In particular:

- first analyze the dominant `d=0` branch, where z is adjacent to every other outside-U vertex and the full `N x (u_o-1)` hole rectangle is present;
- determine whether `H-PINCH` near equality forces most internal X-edges to saturate a very small `U_{bar C}\{z}` witness population;
- feed the resulting same-code U--U criticality back through the fixed witness `a_0`;
- only if that literal geometry survives should `d>0` or `m>=2` be promoted.

Loaded-buffer, `m=g+2`, `z=2`, and the four-exception route remain subordinate.
