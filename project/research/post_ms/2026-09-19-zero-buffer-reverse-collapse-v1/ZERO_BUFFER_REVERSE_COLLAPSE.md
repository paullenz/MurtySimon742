# Zero-buffer reverse-channel collapse

Date: 2026-09-19

Status: structural strengthening inside the repaired rigid one-code `z=1` common-buffer branch. This note does **not** claim the eventual second-extremal theorem. It closes the cheapest reverse-head geometry from the preceding handoff and replaces the scalar guess `d=0` by the graph-forced conclusion `d=p`.

## 1. Audit reconciliation

Before forward mathematics, `CURRENT_STATE.md`, `README.md`, the latest commits, the 19 September daily adversarial audit/handoff, the repaired source-premise note, and the independent actual-D2C rigid Hall/pair-capacity regression were reread.

The audit order is unchanged. The raw distinct-source premise is directly proved from the beta singleton common-neighbour certificate; selected `(source,coordinate)` uniqueness is a selected-representative convention for a unique physical P--U obligation; the `B_beta` lower bounds count those selected physical obligations. The independent actual-graph regression reaches rooted residual identities, A/U codes, Hall cuts and exact `Ccap_P`, has zero recorded graph/formula mismatches, and retains the published `X_3` (`n=12,m=32>M(12)=31`) hostile control. No actual rigid complete Hall cut with `x>=3` has yet been found, so the present result remains a hand implication conditional on the rigid one-code hypotheses. The four-exception gate remains subordinate.

The active branch is the repaired zero-buffer common-buffer subbranch:

- a complete rigid cut `X--Y`, `x=|X|>=3`, `y=|Y|>0`;
- all Y-sources have code `d`, while X contains neither code `d` nor `bar d`;
- `g=p`, `k=x-p>0`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`, `e(G[U_-])=0`;
- `epsilon_b=0`, hence `b--X` and `b--U_o` are complete;
- for each of the p tight fibres, the endpoint of gamma-code `d` is used in the matched crossing layer and has one graph-fixed X-head;
- `X=H_M dotcup H_0`, `|H_M|=p`, `|H_0|=k`, where `H_0` is the injective core-head image of `W_0`.

The corrected criticality alternatives for an edge `b x` are retained:

- Orientation A: `b z in E`, `x z notin E`, `N(x) cap N(z)={b}`;
- Orientation B: `x z in E`, `b z notin E`, `N(b) cap N(z)={x}`.

Orientation A is matched with `gamma(z)=c(x)` or outside unmatched with `c(z)=bar c(x)` and z anticomplete to Y. Orientation B, if it exists, uses a matched endpoint of gamma-code `bar d`.

---

## 2. Unit I: mate-degree amplification in every tight fibre

Fix a tight fibre `{q,q'}` with

`gamma(q)=d`, `gamma(q')=bar d`.

The matched crossing layer uses q for every Y-source. Since `X--Y` is complete, the singleton common-neighbour certificate for that crossing layer forces q to have exactly one X-neighbour; denote it by `h_M(q)`.

Thus

> `N_X(q)={h_M(q)}`.                                      `(2.1)`

Every vertex outside the tight pair and the root is adjacent to exactly one endpoint of the fibre. In particular every X-vertex other than `h_M(q)` is nonadjacent to q and therefore adjacent to q'. Hence

> `N_X(q')=X\{h_M(q)}`                                   `(2.2)`
>
> and `d_X(q')=x-1`.                                      `(2.3)`

This uses only tight-fibre transversality plus the already-established graph-fixed matched crossing head.

---

## 3. Unit II: the reverse Orientation-B channel is empty

Suppose some buffer edge `b x_0` used Orientation B with matched witness q'. Gamma localization forces `gamma(q')=bar d` and the criticality certificate requires

`N(b) cap N(q')={x_0}`.                                  `(3.1)`

But zero buffer slack makes b adjacent to every vertex of X. By `(2.2)`, q' is adjacent to the `x-1` vertices in `X\{h_M(q)}`. Therefore

`|N(b) cap N(q')| >= x-1 >= 2`,                           `(3.2)`

because the rigid cut has `x>=3`.

This contradicts `(3.1)`.

Therefore:

> **REVERSE-CHANNEL COLLAPSE.** No buffer--X edge admits Orientation B in the zero-buffer `g=p` branch. `(REV0)`

Equivalently the preceding reverse-head set is empty:

> `R_B=emptyset`, `r_B=0`, and `d=p`.                     `(3.3)`

This is the opposite end of the scalar range from the previous cheapest arithmetic possibility `d=0`. The scalar monotonicity result was correct, but its minimizer is not graph-realizable.

---

## 4. Unit III: every buffer--X edge is outside-U certified

By `(REV0)`, every one of the x buffer--X edges uses Orientation A.

At `g=p`, every matched gamma pair is `{d,bar d}`. A matched Orientation-A witness for source x would require

`gamma(z)=c(x)`.

But every X-code is different from both d and `bar d`. Hence the matched Orientation-A subchannel is also empty.

Consequently every `x in X` has an outside witness `z_x in U_o` such that

> `b z_x in E`, `x z_x notin E`,
>
> `N(x) cap N(z_x)={b}`,
>
> `c(z_x)=bar c(x)`,
>
> and `z_x` is anticomplete to Y.                         `(4.1)`

No physical-witness injectivity is asserted: different X-sources may choose the same z when their codes permit it. What is exact is the selected outside-source incidence count

> `ell=x=p+k`.                                            `(4.2)`

The predecessor lower bound `ell>=k+d` therefore becomes equality at the graph-forced value `d=p`.

---

## 5. Unit IV: every core head forces a physical core--outside hole

Let `w in W_0` and let `x=h(w) in H_0` be its unique X-neighbour. By Unit III, choose an outside witness z for the buffer edge `b x`.

The certificate has

`N(x) cap N(z)={b}`.

Since w is adjacent to x, w cannot also be adjacent to z, otherwise w would be a second common neighbour. Hence `wz` is a nonedge.

The k vertices w are distinct, so the resulting physical pairs `(w,z)` are distinct even if some witnesses z are reused. Therefore

> `H_core=e_bar(W_0,U_o)>=k`.                             `(5.1)`

Using the exact core identity

`E_core=k(p+k-1)+H_core`,

we obtain the sharpened unconditional zero-buffer floor

> `E_core>=k(p+k)`.                                       `(5.2)`

Thus the `H_core=0` equality geometry from the preceding handoff is not merely expensive: it is impossible. The first live stability layer starts at `H_core=k`.

---

## 6. Unit V: code-purity and distinct outside-witness demand

Let W be the set of distinct physical outside witnesses selected in Unit III, put `m=|W|`, and let `t_z` be the number of X-sources whose selected buffer-edge certificate uses z. Then

`sum_{z in W} t_z=x`.                                     `(6.1)`

If the same physical z serves x and x', `(4.1)` gives

`c(z)=bar c(x)=bar c(x')`,

hence `c(x)=c(x')`. Thus:

> one physical outside witness serves only one X-code class. `(6.2)`

For an above-threshold candidate, the preserved aligned-code self-pricing theorem gives

`n_c<=R_A=floor(R_code(C0)/2)`.

Therefore

> `t_z<=R_A`                                               `(6.3)`

and

> `m>=ceil(x/R_A)`.                                       `(6.4)`

This is strictly stronger than the preceding zero-buffer witness floor `ceil(k/R_A)`, because the reverse collapse forces outside certificates for all p matched-crossing heads as well as the k excess heads.

Every z is anticomplete to Y, so the physical Y--`U_o` hole count satisfies

> `H_Y>=ym`,                                               `(6.5)`

and the exact source-slack identity at `g=p` gives

> `L_Y=y+H_Y>=y(1+m)`.                                    `(6.6)`

---

## 7. Unit VI: outside-witness slack after full reverse collapse

For `z in W`, the U-vertex degree identity and `(4.1)` give the preserved bound

`epsilon_z >= [p-x+t_z]_+`.

Since `x=p+k`, this is

> `epsilon_z >= [t_z-k]_+`.                               `(7.1)`

Summing over W and using convex truncation,

> `E_W:=sum_{z in W}epsilon_z >= [x-km]_+`.               `(7.2)`

This is a genuine physical U-slack term on vertices outside the common core. It is disjoint from `E_core`.

The exact score obstruction can therefore retain m rather than prematurely eliminate it:

> `S >= k(p+k)+[x-km]_+`
> `     +max{phi(p), y(1+m)}`,                            `(7.3)`

where `m>=ceil(x/R_A)` and `phi(p)=p(p-1)` for `p>=3` (zero in the already-defined small-p convention).

For the distinguished one-code pair P itself, the core and Y-slack terms lie in the same pair-local ledger, so

> `S_P >= k(p+k)+y(1+m)`.                                 `(7.4)`

The audit-mandated exact local constraints remain simultaneous:

> `2xy <= Ccap_P`
>
> `Ccap_P=R_code(S_P) * (p + 2S_P/(lambda+1))`,           `(7.5)`

along with `(ONE-P)` and `(CROWD)`. Thus the reverse collapse strengthens the input to the exact pair bill rather than replacing it by a total-score scan.

---

## 8. Unit VII: strengthened rooted residual feedback

The repaired physical A--U hole count was

`Z>=k(a-1)+y+ym+ell`.

Unit III gives `ell=x=p+k`, hence

> `Z>=ka+p+y(1+m)`.                                       `(8.1)`

Relative to the previous scalar-cheapest `d=0` handoff this gains an exact additional p holes.

The U-slack floor is

> `E_U>=E0(m):=k(p+k)+[x-km]_+`.                          `(8.2)`

Using the exact rooted identity

`Z=u(p-lambda)+2q+E_U`,

put

`D(m)=ka+p+y(1+m)-u(p-lambda)`.                           `(8.3)`

Then exact integer minimization gives

> `q+E_U >= E0(m)+ceil([D(m)-E0(m)]_+/2)`.               `(8.4)`

This is the correct rooted residual ledger for the zero-buffer reverse-collapsed branch. It should be combined with `(7.4)--(7.5)` before any coarse total-score relaxation.

---

## 9. Unit VIII: the previous head-partition target disappears

The preceding handoff proposed attacking the scalar-cheapest configuration `d=0`, in which all p reverse gamma-`bar d` endpoints were imagined to carry singleton X-heads and `H_core=0` placed the k core heads inside that reverse-head set.

Units I--IV show that this configuration is impossible at the first physical adjacency check:

- each gamma-d crossing endpoint has exactly one X-neighbour;
- its tight mate of gamma-code `bar d` therefore has x-1 X-neighbours;
- the buffer is complete to X;
- hence no gamma-`bar d` mate can have a singleton common X-neighbour with the buffer;
- so the reverse-head set is empty, not saturated;
- all X buffer edges use outside witnesses;
- and every core head creates a core--outside hole.

Thus the live zero-buffer branch is forced to the **maximal reverse deficit** `d=p`, with `H_core>=k`, `ell=x`, and the strengthened pair/residual ledgers above.

This is a structural reduction, not a numerical diagnostic.

---

## 10. Trust boundary and next move

No new witness-incidence injectivity was assumed. Unit IV counts k distinct physical nonedges because their W_0 endpoints are distinct. Unit V permits arbitrary reuse of a physical outside witness inside one X-code class and prices only the already-proved aligned-code class capacity. The proof uses only the corrected buffer-edge orientations, tight-fibre transversality, the graph-fixed matched-crossing heads, and zero-buffer completeness.

The mandatory negative control remains untouched: `X_3` has `u=0` and never enters a branch requiring `U_-=W_0 dotcup {b}` with `k>0`.

Next work should stay in this branch long enough to exploit the new full outside load. In order:

1. combine the exact local `Ccap_P`, `(ONE-P)` and `(CROWD)` with `(7.4)` while retaining m;
2. optimize the one-dimensional physical tradeoff in `(7.3)` and `(8.4)` symbolically, not by blind scan;
3. test whether the simultaneous pair-capacity and rooted-residual inequalities already exclude the zero-buffer branch above an explicit parameter threshold;
4. if a thin strip survives, use the code-purity classes of Unit V and criticality of the forced `W_0--W` edges/nonedges to classify that strip;
5. only after this maximal-deficit branch is exhausted consider positive buffer slack or `z=2`.
