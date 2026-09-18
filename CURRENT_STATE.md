# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_WITNESS_SLOT_LOCAL_HAMMING_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The mixed `{4,5}` selected-excess ladder is closed and is not a live branch. The active branch is the triangle-containing unmatched/errorful antipode regime.

The live structural spine is now

`rooted B-edge criticality -> exact unused witness-slot residual -> local A-coordinate Hamming budgets -> forced non-direct A-edge demand -> complementary-pair matched/A-U capacity -> residual threshold`.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 graph is exactly the project's `X_3`:

- `n=12`, `m=32>M(12)=31`;
- rooted data `p=4,b=8,a=3,u=0,lambda=4`;
- `q=s=f=r=0`, `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`;
- `G[B]=Q_3`, with three A-vertices equal to the three coordinate-zero faces.

Certification:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

The new witness-slot language identifies `X_3` as an **exact saturation model**: its 12 rooted B-edges consume all 12 B--A nonedge slots.

## 2. Rooted residual / triangle spine

Around a maximum-degree root `v`, write

`B=N(v)`, `A=V\N[v]`, `lambda=2b-n=b-a-1`.

There are `p` tight antipode pairs in `B` and an unmatched set `U`, `u=|U|`, so

> `b=2p+u`,
>
> `a=2p+u-lambda-1`.

Put

`q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`.

Then

> `Q=e(G[B])=p(p+u-1)+q`,
>
> `r=(p+u)(a-p)+p-s-q`,
>
> `delta=b(n-b)-m=r-f`.                                  `(DEF)`

With `epsilon_z=b-d(z)`, put

> `E_U=u(p+u-1)-2q-s`,
>
> `L_A=a(p+u)-s-2f`,
>
> `S=E_U+L_A`.

Let

`c_lambda=ceil(lambda(lambda+2)/2)`,

`D_M=ceil((4p+2u-c_lambda-2)/2)`.

Then

> `S=2delta+lambda(p+u)-p`,                               `(RS)`
>
> `D_M=b(n-b)-M(n)`,
>
> `m<=M(n) iff delta>=D_M`.                               `(RT)`

The exact rooted-transfer identities remain

> `r+Q=L_A+2f`,                                           `(RQ1)`
>
> `delta+Q=L_A+f`,                                        `(RQ2)`
>
> `f=(p-lambda)(p+u)+q+E_U-delta`.                        `(RSF)`

Thus above `M(n)` (`delta<=D_M-1`),

> `f>=F_0+q+E_U`,                                         `(RSF+)`

where `F_0=(p-lambda)(p+u)-D_M+1`.

## 3. Rooted witness slots: exact meaning of `r`

Define

> `Omega={(x,z) in B x A : xz notin E(G)}`.              `(WS0)`

Counting B--A nonedges gives

> `|Omega|=L_A+2f=Q+r`.                                   `(WS1)`

Every `xy in E(G[B])` lies in the triangle `vxy`. Triangle-edge criticality gives an orientation, say source `x`, head `y`, and `z in A` such that

> `N(x) cap N(z)={y}`.                                    `(WS2)`

The witness cannot lie in `B`, since `v` would be a second common neighbour. A fixed ordered pair `(x,z)` can certify only one head, so choosing one certificate per B-edge injects

> `E(G[B]) -> Omega`.                                     `(WS3)`

Let `Upsilon` be the unused slots. Then exactly

> `|Upsilon|=r`,                                          `(WS4)`
>
> `delta=|Upsilon|-f`.                                    `(WS5)`

Therefore the second-extremal target is precisely

> `|Upsilon|>=f+D_M`.                                     `(WS6)`

Core package:

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/`.

## 4. Saturation theorem and `X_3`

Define the rooted A-incidence code on B by

> `phi(x)=(1_{xz in E})_{z in A} in {0,1}^A`.

If `r=0`, then:

- `A` is independent, hence `f=delta=0`;
- every B--A nonedge slot is used by a rooted B-edge certificate;
- every edge `xy in G[B]` satisfies `d_H(phi(x),phi(y))=1`;
- `G[B]` is bipartite under parity of `phi`;
- for each `z in A`, writing `S_z=N_B(z)`, every `x in B\S_z` has exactly one neighbour in `S_z` inside `B`.

Thus exact residual saturation is a hypercube-type representation. `X_3` is the canonical small hostile model: `phi(B)={0,1}^3`, `G[B]=Q_3`, and A consists of the three coordinate faces.

## 5. Near-saturation collision identities

For an unused or used slot `(x,z)`, put

`c_B(x,z)=|N(x) cap N(z) cap B|`,

`c_A(x,z)=|N(x) cap N(z) cap A|`.

Used slots have `c_B=1,c_A=0`.

Define

> `H_B=sum_{xy in E(B)} |N_A(x) triangle N_A(y)|`,
>
> `H_A=sum_{yz in E(A)} |N_B(y) triangle N_B(z)|`.

Exact double counting gives

> `H_B=Q+sum_{Upsilon} c_B(x,z)`,                         `(HB)`
>
> `H_A=  sum_{Upsilon} c_A(x,z)`.                         `(HA)`

Hence

> `H_B-Q<=r(p+u)`.                                        `(HB+)`

Small `r` therefore forces the rooted B-edge representation toward the saturated `d_H=1` model.

## 6. Global and local A-edge Hamming budgets

Let `c(z) in {0,1}^p` be the preserved tight-fibre Boolean code on A and put

> `J_A=sum_{yz in E(A)} d_H(c(y),c(z))`.

Since `d_A(z)<=K_A:=min(p+u,a-1)`, the collision identity gives

> `rK_A>=H_A>=2J_A`.                                      `(HAM)`

In particular, if `D` is direct A-edge traffic, direct endpoints have complementary tight codes and

> `2pD<=rK_A`.                                            `(DIR)`

The stronger source-local form is now the preferred one. For `z in A`, let

> `r_z=|{(x,z) in Upsilon}|`,                             `(L1)`

so `sum_z r_z=r`. Then the directed collision count is exact:

> `sum_{y in N_A(z)} |N_B(y)\N_B(z)|`
> ` =sum_{(x,z) in Upsilon} c_A(x,z)`.                   `(L2)`

Therefore

> `sum_{y in N_A(z)} d_H(c(y),c(z))<=r_z d_A(z)`.        `(LH)`

If `d_A(z)>0`, the average tight-code length of A-edges incident with `z` is at most `r_z`.

For the direct fan at `z`,

> `p d_D(z)<=r_z d_A(z)`.                                `(LDF)`

So an `alpha` fraction of direct incident A-edges forces at least `alpha p` unused rooted witness slots **at the same A-coordinate**. This is the locality that the preceding global scalar envelopes were missing.

Companion note:

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/LOCAL_SLOT_HAMMING_BUDGET.md`.

## 7. Forced non-direct demand

With the exact channel decomposition

> `f=D+P_B+C`,                                             `(CH)`

where `P_B` is matched-B traffic and `C` is A/U UCN traffic, `(DIR)` and `r=f+delta` give

> `P_B+C >= [((2p-K_A)f-K_A delta)/(2p)]_+`.             `(ND1)`

Writing

> `G=(p-lambda)(p+u)+q+E_U`,

so `f=G-delta`, gives the cleaner form

> `P_B+C >= [(1-K_A/(2p))G-delta]_+`.                    `(ND2)`

Above `M(n)`,

> `P_B+C`
> ` >= [(1-K_A/(2p))((p-lambda)(p+u)+q+E_U)`
> `      -(D_M-1)]_+`.                                    `(ND3)`

Thus whenever `K_A<2p`, a definite part of the rooted-transfer A-edge demand must enter the already self-priced non-direct witness channels rather than being hidden in direct/complementary edges.

## 8. Preserved source/Hall and q/E stack

The exact source-tuple hierarchy remains

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`     `(FDPr)`

for every `r>=3`, with integrated deficit profile and beta-support floors. In particular the preserved machinery supplies:

- lower bounds on total beta load `B_beta`;
- the integrated beta-support floor `N_sup(B_beta)`;
- resulting `E_U` floors;
- the cross-edge q floor
  
  > `q>=ceil([u(lambda-p)-E_U]_+/2)`;
- the beta-sensitive q ceiling
  
  > `q<=au-B_beta+N_1`,
  
  together with load-one compression.

These quantities should now feed the **local** residual/witness-slot allocation rather than be collapsed immediately to one scalar `S`.

## 9. Preserved pair-local channel capacity

For Boolean code `c`, write `n_c=|A_c|`, `N_c=|(A union U)_c|`, `w_c=N_c+n_c`, and pair slack `S_P,L_P` on `P={c,bar c}`.

Aligned-code self-pricing gives the preserved radius

> `R_code(s)=max(0,floor((D_0+sqrt(D_0^2+12s))/3))`,

where `D_0=5p+5u-3lambda-2`.

Direct plus A/U traffic on a complementary pair satisfies

> `2(lambda+1)(D_P+C_P)`
> ` <=R_code(S_P)(2L_P+S_P)`.                            `(CCP)`

Matched-B traffic self-prices through

> `P_B<=aR_A(L_A)`,

with `R_A(L)=max(2,floor((1+sqrt(1+4L))/2))`, and the preserved fibre-polarization/complement-pair theorems give finer local information.

The previous one-dimensional global collapse, replacing pair slack by total `S`, was explicitly tested and gave no generic new closures. Do not return to that scalar optimization as the main line.

## 10. C5 reassessment

Lin and Wang (Discrete Applied Mathematics 375 (2025), 332--337, DOI `10.1016/j.dam.2025.06.025`) prove that sufficiently-large C5-free D2C graphs at or above `M(n)` are complete bipartite.

This is an external consistency boundary, but it is **not extra leverage in the live partial-Boolean triangle branch**. If `p>=2` and `Q>0`, choose a rooted B-edge certificate

> `N(x) cap N(z)={y}`, with `z in A`.

Every A-vertex has at least one B-neighbour in each tight pair, so `d_B(z)>=p>=2`. Choose `w in N_B(z)\{y}`. Since `xz` is a nonedge, the five distinct vertices

> `v-x-y-z-w-v`

form a `C5`.

Therefore

> `p>=2` and `Q>0` imply `C5 subseteq G`.                 `(C5)`

So the current branch already contains a C5 for a local reason; trying to exploit the Lin--Wang theorem would not advance it.

Correction note:

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/C5_REASSESSMENT.md`.

## 11. Audit

The new package contains finite audit support only; the promoted statements are hand arguments.

Main witness-slot audit:

- 21 D2C graph-atlas classes through order seven;
- 50 maximum-degree roots;
- 14 rooted B-edges checked for A-witness certificates;
- 91 B--A nonedge slots;
- 77 unused slots;
- 27 saturated roots;
- zero failures of `(HB)`, `(HA)`, saturation consequences, or the `X_3` reconstruction;
- `X_3`: `Q=12`, `|Omega|=12`, `r=0`, `H_B=12`, `H_A=0`.

The local identity `(L2)` was independently checked on 87 A-coordinate/root instances across the same 21 D2C atlas classes, including 37 coordinates with `r_z=0`; failures: 0.

Files:

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/check_rooted_witness_slot_saturation.py`,

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/ROOTED_WITNESS_SLOT_AUDIT_SUMMARY.json`,

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/LOCAL_SLOT_HAMMING_AUDIT_SUMMARY.json`.

## 12. Live frontier

The next highest-value move is to retain **both** local coordinates:

1. `r_z`, which prices the Hamming/direct share of A-edges incident with source `z`;
2. complementary tight-code pair slack, which prices the matched-B and A/U witness channels.

The aim is a source-to-pair transport inequality: after `(LDF)` removes the locally affordable direct traffic, route the remaining incident A-edge demand to its matched/A-U complementary pair and charge that pair before summing over sources. This would directly attack the information loss identified by the failed scalar synthesis.

A secondary line is to classify near-saturated `phi(B)` representations using `(HB+)`, with `X_3` retained as the exact hostile equality model.

Do not return to the closed mixed `{4,5}` ladder, and do not optimize for first-proof priority on Erdős #742.
<!-- CURRENT-STATUS:END -->
