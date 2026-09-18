# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `RIGID_HALL_WITNESS_DEFICIT_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The mixed `{4,5}` selected-excess ladder is closed. The active branch is the triangle-containing unmatched/errorful antipode regime. No global eventual second-extremal theorem is claimed.

The current structural spine is

`rooted witness-slot residual -> local A-coordinate Hamming budget -> complementary-pair Hall demand -> exact cut decomposition -> capacity-density majorization -> beta expulsion / source-tuple obstruction -> rigid-cut code collapse -> singleton U-witness deficit/slack -> one-code outside pair-capacity trap`.

## 1. Mandatory hostile control

The published Radosavljevic--Stanic--Zivkovic (2024) graph is exactly the project's `X_3`:

- `n=12`, `m=32>M(12)=31`;
- rooted data `p=4,b=8,a=3,u=0,lambda=4`;
- `q=s=f=r=0`, `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`;
- `G[B]=Q_3`, with the three A-vertices equal to the three coordinate-zero faces.

It is an exact rooted witness-slot saturation model: its 12 rooted B-edges consume all 12 B--A nonedge slots. The Hall/beta/U-witness results do not exclude it: `u=0`, A is independent, and every new rigid U-witness penalty below vanishes.

Certification:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

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

we have

> `S=2delta+lambda(p+u)-p`,
>
> `m<=M(n) iff delta>=D_M`,
>
> `D_M=b(n-b)-M(n)`,
>
> `delta+Q=L_A+f`,
>
> `f=(p-lambda)(p+u)+q+E_U-delta`.                       `(RSF)`

Thus above `M(n)` unmatched slack itself raises the forced A-edge mass.

## 3. Exact rooted witness-slot residual

Define `Omega={(x,z) in B x A : xz notin E(G)}`. Every rooted B-edge has a distinct criticality certificate slot in `Omega`. If `Upsilon` is the unused slot set, then

> `|Omega|=L_A+2f=Q+r`,
>
> `|Upsilon|=r`,
>
> `delta=|Upsilon|-f`.                                   `(SLOT)`

For each `z in A`, put `r_z=|{(x,z) in Upsilon}|`. The local directional collision identity gives

> `sum_{y in N_A(z)} d_H(c(y),c(z))<=r_z d_A(z)`.        `(LH)`

If `d_D(z)` is direct A-edge degree,

> `p d_D(z)<=r_z d_A(z)`.                                `(LDF)`

Main package:

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/`.

## 4. Complementary-pair Hall system

For an unordered complementary tight-code pair `P={c,bar c}`, let

> `A_P=A_c union A_bar c`, `a_P=|A_P|`,
>
> `L_P=L_c+L_bar c`, `S_P=S_c+S_bar c`,
>
> `R_P=sum_{z in A_P}r_z d_A(z)`,
>
> `Z_P=a_Pu-e(A_P,U)`.

The total cross deficit is exact:

> `sum_P Z_P=au-s=u(p-lambda)+2q+E_U`.                   `(ZSUM)`

Write `T0=a-p=p+u-lambda-1`. Choose one criticality certificate for every non-direct A-edge and let `t_P=P_P+C_P` be actual chosen non-direct traffic sourced in pair `P`. The pair-local capacity is

> `Ccap_P=R_code(S_P)[g_P+2S_P/(lambda+1)]+2h_P`,
>
> `2t_P<=Ccap_P`.                                        `(CAP)`

For every pair family `X`, with `x=a_X`, the preserved Hall theorem is

> `[x(x-T0)-L_X+Z_X-R_X/p]_+<=Ccap_X`.                   `(HALL-P)`

## 5. Exact Hall-cut decomposition

Let

> `c_X=e(A_X,A\A_X)`,
>
> `M_X=x(a-x)-c_X`,
>
> `E_X=t_X-N_X`,
>
> `J_X=R_X/p-2D_X`.

Here `N_X,D_X` are internal non-direct/direct A-edge counts. Then

> `2e(A_X)=x(x-T0)-L_X+Z_X+M_X`.                         `(DEG-CUT)`

Define

> `w_P=2t_P+L_P-Z_P+R_P/p`.

Exactly,

> `w_X-x(x-T0)=2E_X+M_X+J_X`.                            `(EXACT-HALL)`

For

> `W_P=Ccap_P+L_P-Z_P+R_P/p`,
>
> `kappa_P=Ccap_P-2t_P>=0`,

we likewise have

> `W_X-x(x-T0)=2E_X+M_X+J_X+kappa_X`.                    `(CAP-EXACT)`

Thus Hall slack decomposes into selected-source export, missing-cut mass, unused direct/Hamming credit, and unused non-direct certificate capacity.

## 6. Hall density / majorization

For active pairs define

> `rho_P^cap=W_P/a_P`.

For any real `tau`, let `X_<tau={P:rho_P^cap<tau}` and `A_tau=a_{X_<tau}`. Then

> `A_tau<T0+tau`.                                        `(HD)`

For `0<=tau<=p`, more than `p-tau` A-vertices therefore lie in pair classes with capacity density at least `tau`.

If a family `X` of mass `x` lies entirely below density `tau`, then

> `2E_X+M_X+J_X+kappa_X<x(T0+tau-x)`.                    `(STAB)`

If the right side is `<1`, then

> `E_X=M_X=0`.                                           `(RIGID)`

Hence the A-cut is complete and every crossing A-edge chooses its source outside `X`.

For the complement `bar X`, if `J=R/p-2D`,

> `sigma_X+sigma_barX=2x(a-x)+J`,                        `(CONS)`
>
> `x(x-T0)<=w_X<=x(a+p-x)+J`,                            `(SAND)`
>
> `Ccap_barX>=2x(a-x)-2(M_X+E_X)`.                       `(COMP-CAP)`

Thus a rigid low-density family forces `Ccap_barX>=2x(a-x)`.

## 7. Hall reserve polarization

Put

> `Sigma_X=W_X-x(x-T0)`.

For disjoint pair families `X,Y`, masses `x,y`,

> `Sigma_{X union Y}=Sigma_X+Sigma_Y-2xy`.                `(POL)`

Therefore Hall feasibility forces

> `Sigma_X+Sigma_Y>=2xy`.                                `(POL+)`

More generally

> `Sigma_X=sum_{P in X}Sigma_P-2sum_{P<Q in X}a_Pa_Q`.

This exposes the exact quadratic cross-pair bill omitted by singleton pair inequalities: two disjoint macroscopic blocks cannot both sit close to Hall equality.

## 8. Hall density couples directly to beta/source support

For `z in A`, its pairwise-distinct designated beta sources are U-neighbours, so

> `ell_z<=d_U(z)`.

For a pair family `X`, define local beta load `B_X=sum_{z in A_X}ell_z`. Since `s_X=e(A_X,U)=xu-Z_X`,

> `B_X<=xu-Z_X`.                                         `(BLOCAL)`

If `X` lies below Hall-capacity density `tau`, then `W_X<tau x`, hence

> `B_X<x(u+tau)-Ccap_X-L_X-R_X/p`.                       `(BE)`

The integrated source-tuple theorem on the complement gives

> `B_barX<=(a-x)p-Phi_r(a-x)`.

Thus

> `B_beta`
> `<x(u+tau)+(a-x)p-Phi_r(a-x)`
> ` -Ccap_X-L_X-R_X/p`.                                  `(HBL)`

In particular

> `B_beta<x(u+tau)+(a-x)p-Phi_r(a-x)`.                   `(HBL0)`

Reference:

`project/research/post_ms/2026-09-18-hall-density-cut-stability-v1/HALL_BETA_LOCALIZATION.md`.

## 9. Rigid Hall cuts force Boolean-code collapse

Assume `E_X=M_X=0`, `X` nonempty proper and `x=a_X>=3`; put `Y=A\A_X`, `y=|Y|`. Every crossing edge is sourced in Y. Let `mu_X` be the number of matched B-endpoints having exactly one neighbour in `A_X`; then `mu_X<=p`. Define

> `k=(x-mu_X)_+`.

For every outside source, at least k singleton-head witnesses lie in U, all in the U-code class complementary to that source code. If `h_Y` distinct tight codes occur in Y, then

> `h_Y k<=u`,
>
> `h_Y(x-p)_+<=u`.                                       `(COLL)`

In particular `x<=p+u`; large rigid families force very few outside codes.

Reference:

`project/research/post_ms/2026-09-18-hall-density-cut-stability-v1/RIGID_HALL_WITNESS_GEOMETRY.md`.

## 10. New: rigid U-witness deficit, slack and residual pricing

Keep the rigid notation above and write `h=h_Y`, `g=x-T0=p-y`.

For each outside code d, collect all U-witnesses used by its sources. Every used witness has exactly one X-neighbour. If it is reused by `t` outside sources, then it misses all those sources and satisfies

> `epsilon_w >= [g+t-1]_+`.                               `(RWI)`

This yields two new exact resource floors.

### A--U nonedge / beta floor

> `Z_X>=hk(x-1)`,
>
> `Z_Y>=yk`,
>
> `Z>=k[y+h(x-1)]`.                                      `(RZ)`

Hence

> `B_beta<=au-k[y+h(x-1)]`.                              `(RB)`

Keeping source-tuple capacity local gives the stronger box

> `B_X<=min{x u-hk(x-1),xp-Phi_r(x)}`,
>
> `B_Y<=min{y(u-k),yp-Phi_r(y)}`.                        `(RBOX)`

### Multiplicity-sensitive U-slack

If `g>=1`,

> `E_U>=k[y+h(g-1)]`
> `   =k[p-1+(h-1)(g-1)]`.                               `(RE+)`

If `g<=1`,

> `E_U>=[yk-(1-g)u]_+`.                                  `(RE-)`

Thus for `g>=1`, even a one-code outside block costs `k(p-1)` unmatched slack; every additional outside code costs another `k(g-1)`.

### Residual/A-edge bridge

Let

> `Z_rig=k[y+h(x-1)]`,
>
> `D=Z_rig-u(p-lambda)`,
>
> `E_rig=` the right side of `(RE+)` or `(RE-)`.

Because `Z=u(p-lambda)+2q+E_U`,

> `q+E_U>=E_rig+ceil((D-E_rig)_+/2)`.                    `(RQE)`

Therefore every above-`M(n)` rigid-cut survivor satisfies

> `f >= (p-lambda)(p+u)-D_M+1`
> `     +E_rig+ceil((D-E_rig)_+/2)`.                     `(RF)`

This is the direct local-Hall-to-rooted-residual bridge that was missing from the previous checkpoint.

### Feasibility/code-collapse envelope

With

> `C0=2(D_M-1)+lambda(p+u)-p`

and any valid independent beta lower bound `B_*`, every rigid above-M candidate must satisfy

> `hk<=u`,
>
> `E_rig<=C0`,
>
> `B_*+k[y+h(x-1)]<=au`.                                 `(RFEAS)`

For `g>=1`, `k(p-1)>C0` kills the rigid cut outright. For `g>=2`, either

> `k(p+g-2)<=C0`

or the entire outside A-layer has one code (`h=1`). The beta inequality gives an independent one-code trigger.

### One-code outside pair-capacity trap

If `h=1`, write the unique outside code as d and `P={d,bar d}`. Direct A-edges join complementary codes, so there are no direct edges inside Y. Every crossing edge and every internal Y-edge is non-direct traffic sourced in P. The exact complete-cut degree identity and `Z_Y>=yk` give

> `Ccap_P+L_Y >= y(p+x+k)`.                               `(ONE)`

Thus code collapse is not an equality escape: the single outside pair must pay an explicit certificate/slack bill. The preserved aligned-code crowding theorem adds, whenever `3y>=D0=5p+5u-3lambda-2`,

> `S_P>=y(3y-D0)`.                                       `(CROWD)`

Package:

`project/research/post_ms/2026-09-18-rigid-hall-witness-deficit-v1/`.

## 11. Preserved supporting stacks

The integrated source-tuple theorem and beta-support inverse remain active:

> `B_beta<=N_+p-Phi_r(N_+)`,
>
> `N_+>=N_sup(B_beta)`.

The bounded-surplus direct theorem also remains active: for `n>=23`, a direct fan of order `d`, total hole surplus `eta<=d-2`, and at most four external exceptions is triangle-free or already satisfies `m<=M(n)`. Thus every live triangle-containing above-`M(n)` survivor has `eta>=d-1` or `z>=5`.

Do not collapse pair-local information to total `S` before using it; previous global scalar syntheses were audited and found too lossy.

## 12. Audit

The Hall-density package frozen audit remains clean:

- random graph/partition trials: 50,000;
- pair-class instances: 156,014;
- family/subset checks: 834,948;
- failures: 0.

The new rigid-witness package adds:

- 12,841 random abstract witness-incidence systems: zero failures;
- 100,000 exact integer minimization checks for `(RQE)`: zero failures;
- 1,910,960 abstract rigid parameter/code-count instances for `3<=p<=18`, `1<=u<=18` after imposing the older population condition `hk<=u`;
- 39,902 of those abstract instances are newly rejected by the U-slack/beta-deficit filters (28,102 by U-slack and 11,800 by beta deficit in this diagnostic box);
- failures: 0.

These computations are audit/diagnostic support only; the promoted statements are hand derived. The parameter scan is not a count of realizable D2C graphs.

## 13. Live frontier

The Hall allocation problem is now sharply split.

1. **Non-rigid low-density families:** continue to use `(HBL)/(HBL0)` with the strongest preserved switching beta lower bound and local resource terms. The conservative root-imbalance-only scan was too weak, so do not globalize away the local data.
2. **Rigid families:** the old population collapse `hk<=u` is now supplemented by actual beta-deficit and U-slack bills `(RB)/(RE+)`; these either kill the rigid cut or force the outside to one code. Once `h=1`, the immediate target is the explicit one-sided pair inequality `(ONE)` together with the actual `Ccap_P` formula and aligned-code crowding. This is the most compact route to closing the rigid Hall branch.
3. If the one-code inequality leaves an asymptotic equality family, classify that geometry directly and feed its forced `q,E_U,f` back through `(RF)` and `delta+Q=L_A+f`.

Do not return to the closed mixed `{4,5}` ladder. Do not optimize for first-proof priority on Erdős #742. Keep `X_3` as the mandatory hostile control.
<!-- CURRENT-STATUS:END -->
