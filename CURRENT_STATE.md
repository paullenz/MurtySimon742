# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_SLOT_PAIR_CROSS_DEFICIT_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The mixed `{4,5}` selected-excess ladder is closed. The active branch is the triangle-containing unmatched/errorful antipode regime.

The current structural spine is

`rooted B-edge criticality -> exact unused-slot residual -> local A-coordinate Hamming budget -> complementary-pair internal non-direct demand -> local matched-B/A-U capacity -> residual threshold`.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory hostile control

The published Radosavljevic--Stanic--Zivkovic (2024) graph is exactly the project's `X_3`:

- `n=12`, `m=32>M(12)=31`;
- rooted data `p=4,b=8,a=3,u=0,lambda=4`;
- `q=s=f=r=0`, `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`;
- `G[B]=Q_3`, with the three A-vertices equal to the three coordinate-zero faces.

Certification:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

It is now also the exact witness-slot saturation model: its 12 rooted B-edges consume all 12 B--A nonedge slots.

## 2. Rooted residual spine

Around a maximum-degree root `v`, write `B=N(v)`, `A=V\N[v]`, with `p` tight antipode pairs and unmatched set `U`, `u=|U|`:

> `b=2p+u`,
>
> `a=2p+u-lambda-1`.

Put `q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`. Then

> `Q=e(G[B])=p(p+u-1)+q`,
>
> `delta=b(n-b)-m=r-f`.

With

> `E_U=u(p+u-1)-2q-s`,
>
> `L_A=a(p+u)-s-2f`,
>
> `S=E_U+L_A`,

the preserved target identities are

> `S=2delta+lambda(p+u)-p`,
>
> `m<=M(n) iff delta>=D_M`,

where

> `D_M=b(n-b)-M(n)`.

Rooted triangles satisfy

> `r+Q=L_A+2f`,
>
> `delta+Q=L_A+f`,
>
> `f=(p-lambda)(p+u)+q+E_U-delta`.                       `(RSF)`

Thus above `M(n)` (`delta<=D_M-1`), unmatched slack itself raises the forced A-edge mass.

## 3. Exact rooted witness-slot residual

Define

> `Omega={(x,z) in B x A : xz notin E(G)}`.

Then

> `|Omega|=L_A+2f=Q+r`.

Every rooted B-edge `xy` lies in triangle `vxy`. Triangle-edge criticality gives an orientation and `z in A` with

> `N(x) cap N(z)={y}`.

A fixed `(x,z)` can certify only one head, so choosing one certificate per B-edge injects `E(G[B])` into `Omega`.

Let `Upsilon` be the unused slots. Then exactly

> `|Upsilon|=r`,
>
> `delta=|Upsilon|-f`.                                   `(SLOT)`

Therefore the second-extremal target is exactly `|Upsilon|>=f+D_M`.

Main package:

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/`.

## 4. Saturation and near-saturation

If `r=0`, the slot map is bijective. Then:

- `A` is independent, hence `f=delta=0`;
- with `phi(x)=(1_{xz in E})_{z in A}`, every B-edge has `d_H(phi(x),phi(y))=1`;
- `G[B]` is bipartite by parity of `phi`;
- each A-neighbourhood cut is one-sided perfectly dominated from its complement.

`X_3` is exactly the `a=3` saturated realization with `phi(B)={0,1}^3` and `G[B]=Q_3`.

For arbitrary `r`, exact collision identities are

> `H_B=Q+sum_{(x,z) in Upsilon}|N(x) cap N(z) cap B|`,
>
> `H_A=  sum_{(x,z) in Upsilon}|N(x) cap N(z) cap A|`,

where

`H_B=sum_{xy in E(B)}|N_A(x) triangle N_A(y)|`,

`H_A=sum_{yz in E(A)}|N_B(y) triangle N_B(z)|`.

Hence `H_B-Q<=r(p+u)`.

## 5. Local A-coordinate Hamming budget

Let `c(z) in {0,1}^p` be the tight-fibre Boolean code on A. For each `z in A`, let

> `r_z=|{(x,z) in Upsilon}|`,

so `sum_z r_z=r`.

The directional collision identity gives

> `sum_{y in N_A(z)} |N_B(y)\N_B(z)|`
> ` =sum_{(x,z) in Upsilon}|N(x) cap N(z) cap A|`.

Therefore

> `sum_{y in N_A(z)} d_H(c(y),c(z))<=r_z d_A(z)`.        `(LH)`

In particular, if `d_D(z)` is direct A-edge degree at `z`, direct endpoints have complementary codes and

> `p d_D(z)<=r_z d_A(z)`.                                `(LDF)`

So an `alpha` fraction of direct incident A-edges forces at least `alpha p` unused rooted witness slots at the same A-coordinate.

Summing recovers the global bound `2pD<=rK_A`, where `K_A=min(p+u,a-1)`.

## 6. Complementary-pair residual demand

For an unordered complementary tight-code pair `P={c,bar c}`, put

> `A_P=A_c union A_bar c`, `a_P=|A_P|`,
>
> `L_P=L_c+L_bar c`, `S_P=S_c+S_bar c`,
>
> `R_P=sum_{z in A_P} r_z d_A(z)`,

and

> `T=a-p=p+u-lambda-1`.

Let `s_P=e(A_P,U)` and define the local A--U nonedge deficit

> `Z_P=a_Pu-s_P>=0`.                                     `(ZP)`

Its total is exactly

> `sum_P Z_P=au-s=u(p-lambda)+2q+E_U`.                   `(ZSUM)`

Retaining the actual A--U split strengthens pair crowding to

> `2e(G[A_P])>=a_P(a_P-T)-L_P+Z_P`.                     `(PC)`

The local Hamming theorem gives `2pD_P<=R_P` for direct internal edges, so if `N_P` is the internal **non-direct** A-edge count,

> `2N_P>=`
> `[a_P(a_P-T)-L_P+Z_P-R_P/p]_+`.                        `(PRD)`

Crucially, an internal non-direct A-edge cannot export its source pair: whichever endpoint is the chosen source still has code in `P`.

## 7. Pair-local non-direct capacity

Let `C_P` be A/U UCN traffic sourced from pair `P`, and `P_P` matched-B traffic sourced from `P`.

The preserved aligned A/U theorem gives

> `(lambda+1)C_P<=R_code(S_P)S_P`.                       `(AU-P)`

For matched-B, let `g_P` be the number of tight fibres whose gamma pair is `P`, and

> `h_P=sum_{i in I_P}min(t_i^0,t_i^1)`.

Then

> `P_P<=g_P R_code(S_P)/2+h_P`.                          `(MB-P)`

The resources obey

> `sum_P g_P=p`,
>
> `(lambda+1)sum_P h_P<=R_A(L_A)L_A`,
>
> `sum_P R_P<=rK_A`.

Since `N_P<=P_P+C_P`, every pair satisfies the new live feasibility theorem

> `[a_P(a_P-T)-L_P+Z_P-R_P/p]_+`
> ` <=R_code(S_P)[g_P+2S_P/(lambda+1)]+2h_P`.            `(PAIR)`

This is the first theorem that simultaneously keeps pair population, pair slack, local residual/Hamming resource, local A--U cross deficit, matched-fibre multiplicity, and two-sided matched-foot resource. Forced internal demand cannot be paid from unrelated pairs.

Core notes:

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/COMPLEMENT_PAIR_RESIDUAL_DEMAND.md`,

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/PAIR_CROSS_DEFICIT_STRENGTHENING.md`.

## 8. Preserved source/Hall stack

The exact source-tuple hierarchy and integrated beta-support machinery remain active. They provide:

- beta-load floors and an integrated support floor;
- `E_U` lower bounds;
- `q>=ceil([u(lambda-p)-E_U]_+/2)`;
- beta-sensitive q ceilings with load-one compression.

These quantities now enter `(PAIR)` through two distinct mechanisms:

1. the residual split raises total forced A-edge demand;
2. `ZSUM=u(p-lambda)+2q+E_U` forces local A--U missing-incidence mass across the pairs.

Do not collapse these to total `S` before using the pair allocation.

## 9. C5 reassessment

Lin and Wang (Discrete Applied Mathematics 375 (2025), 332--337, DOI `10.1016/j.dam.2025.06.025`) prove that sufficiently-large C5-free D2C graphs at or above `M(n)` are complete bipartite.

This is not extra leverage in the live partial-Boolean triangle branch. If `p>=2` and `Q>0`, a rooted B-edge certificate `N(x) cap N(z)={y}` has `z in A` and `d_B(z)>=p>=2`; choosing another `w in N_B(z)\{y}` gives the 5-cycle

> `v-x-y-z-w-v`.

Thus `p>=2,Q>0` already implies `C5 subseteq G` locally.

Correction note:

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/C5_REASSESSMENT.md`.

## 10. Audit

The new finite audit is support only; promoted results are hand proofs.

- 21 D2C graph-atlas classes through order seven;
- 50 maximum-degree roots;
- 14 rooted B-edges checked for A-witness certificates;
- 91 B--A nonedge slots, 77 unused;
- 27 saturated roots;
- zero failures of the exact global collision identities or saturation consequences;
- `X_3`: `Q=12`, `|Omega|=12`, `r=0`, `H_B=12`, `H_A=0`;
- the local A-coordinate collision identity was independently checked on 87 root/coordinate instances, including 37 with `r_z=0`; failures: 0.

Audit files are in the rooted-witness-slot package.

## 11. Live frontier

The scalar route is retired as the main attack: its finite diagnostic left too much freedom because pair resources were globally interchangeable.

The next highest-value move is now a **pair-allocation/majorization theorem for `(PAIR)`**. The desired advance is to show that the fixed total

> `sum Z_P=u(p-lambda)+2q+E_U`

and the rooted-transfer forced A-edge mass cannot both be dispersed over complementary pairs while respecting the disjoint budgets

> `sum a_P=a`, `sum L_P=L_A`, `sum S_P=S`, `sum R_P<=rK_A`, `sum g_P=p`, and the global `h_P` budget.

In particular, investigate whether source/Hall beta support prevents `Z_P` from being anti-correlated with the large `a_P` pairs; that would make the positive part in `(PAIR)` unavoidable on a controlled family of pairs.

A secondary line is the stability/classification of near-saturated `phi(B)` representations, retaining `X_3` as the exact hostile equality model.

Do not return to the closed mixed `{4,5}` ladder, and do not optimize for first-proof priority on Erdős #742.
<!-- CURRENT-STATUS:END -->
