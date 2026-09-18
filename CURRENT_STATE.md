# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `PAIR_HALL_DENSITY_CUT_STABILITY_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The mixed `{4,5}` selected-excess ladder is closed. The active branch is the triangle-containing unmatched/errorful antipode regime. No global eventual second-extremal theorem is claimed.

The current structural spine is

`rooted witness-slot residual -> local A-coordinate Hamming budget -> complementary-pair Hall demand -> exact cut decomposition -> capacity-density majorization -> beta/source localization or near-equality cut rigidity`.

## 1. Mandatory hostile control

The published Radosavljevic--Stanic--Zivkovic (2024) graph is exactly the project's `X_3`:

- `n=12`, `m=32>M(12)=31`;
- rooted data `p=4,b=8,a=3,u=0,lambda=4`;
- `q=s=f=r=0`, `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`;
- `G[B]=Q_3`, with the three A-vertices equal to the three coordinate-zero faces.

It is an exact rooted witness-slot saturation model: its 12 rooted B-edges consume all 12 B--A nonedge slots. The new Hall-density results do not exclude it: `u=0`, A is independent, and the A--U cross-deficit/beta bridge is inactive.

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

Define

> `Omega={(x,z) in B x A : xz notin E(G)}`.

Every rooted B-edge has a distinct criticality certificate slot in `Omega`. If `Upsilon` is the unused slot set, then

> `|Omega|=L_A+2f=Q+r`,
>
> `|Upsilon|=r`,
>
> `delta=|Upsilon|-f`.                                   `(SLOT)`

For each `z in A`, put `r_z=|{(x,z) in Upsilon}|`. The local directional collision identity gives

> `sum_{y in N_A(z)} d_H(c(y),c(z))<=r_z d_A(z)`.        `(LH)`

If `d_D(z)` is the direct A-edge degree at `z`,

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

Write `T0=a-p=p+u-lambda-1`. For a pair family `X`, use additive subscripts and put `x=a_X`.

Choose one criticality certificate for every non-direct A-edge. Let `t_P=P_P+C_P` be actual chosen non-direct certificate traffic sourced in pair `P`. The pair-local capacity is

> `Ccap_P=R_code(S_P)[g_P+2S_P/(lambda+1)]+2h_P`,
>
> `2t_P<=Ccap_P`.                                        `(CAP)`

The preserved Hall theorem is

> `[x(x-T0)-L_X+Z_X-R_X/p]_+<=sum_{P in X}Ccap_P`         `(HALL-P)`

for every pair family `X`.

## 5. Exact Hall-cut decomposition — new frontier

Let

> `c_X=e(A_X,A\A_X)`,
>
> `M_X=x(a-x)-c_X`                                        `(MCUT)`

be the missing A-cut mass. Let `N_X` be internal non-direct A-edges and define

> `E_X=t_X-N_X>=0`,                                      `(EXPORT)`

which is exactly the number of crossing A-edges whose chosen source lies in `X`.

Direct edges never cross a complementary-pair family cut. Put

> `J_X=R_X/p-2D_X>=0`.                                   `(J)`

The exact A-degree identity is

> `2e(A_X)=x(x-T0)-L_X+Z_X+M_X`.                         `(DEG-CUT)`

Define the actual Hall weight

> `w_P=2t_P+L_P-Z_P+R_P/p`.

Then, exactly,

> `w_X-x(x-T0)=2E_X+M_X+J_X`.                            `(EXACT-HALL)`

For the capacity weight

> `W_P=Ccap_P+L_P-Z_P+R_P/p`,
>
> `kappa_P=Ccap_P-2t_P>=0`,

we have

> `W_X-x(x-T0)=2E_X+M_X+J_X+kappa_X`.                    `(CAP-EXACT)`

This is a structural decomposition of Hall slack, not merely an inequality.

## 6. Hall density / majorization theorem

For active pairs define capacity density

> `rho_P^cap=W_P/a_P`.

For any real `tau`, let `X_<tau={P:rho_P^cap<tau}` and `A_tau=a_{X_<tau}`. Then

> `A_tau<T0+tau`.                                        `(HD)`

For `0<=tau<=p`, more than `p-tau` A-vertices therefore lie in pair classes of capacity density at least `tau`.

If a family `X` of mass `x` is entirely below density `tau`, then the stronger stability estimate holds:

> `2E_X+M_X+J_X+kappa_X<x(T0+tau-x)`.                    `(STAB)`

If the right side is `<1`, integrality forces

> `E_X=M_X=0`.                                           `(RIGID)`

So the A-cut is complete and every crossing A-edge chooses its source endpoint outside `X`; simultaneously `J_X+kappa_X<1`.

## 7. Cut conservation, polarization and forced complementary capacity

For the complementary family `bar X`:

> `E_X+E_barX=c_X`,
>
> `M_barX=M_X`.

If `J=R/p-2D`, then

> `sigma_X+sigma_barX=2x(a-x)+J`,                        `(CONS)`

where `sigma_X=w_X-x(x-T0)`.

Hence

> `x(x-T0)<=w_X<=x(a+p-x)+J`.                            `(SAND)`

Moreover

> `Ccap_barX>=2x(a-x)-2(M_X+E_X)`.                       `(COMP-CAP)`

Thus a capacity-low-density family with `B=x(T0+tau-x)` forces

> `Ccap_barX>2x(a-x)-2B`;                                `(COMP-FORCE)`

and in the rigid `<1` case,

> `Ccap_barX>=2x(a-x)`.

Define the capacity Hall reserve

> `Sigma_X=W_X-x(x-T0)`.

For disjoint families `X,Y`, with masses `x,y`,

> `Sigma_{X union Y}=Sigma_X+Sigma_Y-2xy`.                `(POL)`

Therefore Hall feasibility forces

> `Sigma_X+Sigma_Y>=2xy`.                                `(POL+)`

Two disjoint macroscopic pair blocks cannot both be close to Hall equality.

## 8. Cross-deficit localization

Because

> `W_P=Ccap_P+L_P-Z_P+R_P/p`,

low capacity density `<tau` is equivalent to

> `Z_P>Ccap_P+L_P+R_P/p-tau a_P`.                        `(OVER)`

The density theorem therefore gives, for `0<=tau<=p`:

> the total A-mass of pairs satisfying `(OVER)` is `<T0+tau`.

Equivalently, more than `p-tau` A-vertices lie in pair classes satisfying

> `Z_P<=Ccap_P+L_P+R_P/p-tau a_P`.                       `(CROSS-LOC)`

This is the new bridge to the preserved beta/source-tuple stack: `Z_P` is the local A--U nonincidence deficit, while source-tuple beta support constrains which A-vertices can carry or avoid U-source obligations.

Package:

`project/research/post_ms/2026-09-18-hall-density-cut-stability-v1/`.

## 9. Preserved beta/source stack

The exact integrated source-tuple theorem remains active. For positive beta support `A_+`, `N_+=|A_+|`, every fixed `r>=3` gives

> `B_beta<=N_+p-Phi_r(N_+)`.

Hence `N_+>=N_sup(B_beta)`, shrinking the zero-beta cross-edge reservoir and giving preserved lower bounds on `E_U` and `r`. The previous global scalar collapses are known to be too lossy; do not collapse `(CROSS-LOC)` to total `S` before exploiting this support information.

Reference:

`project/research/post_ms/2026-09-18-rooted-residual-supply-v1/SOURCE_TUPLE_SUPPORT_AND_ZERO_BETA_CAPACITY.md`.

## 10. Direct-fan stability remains active

The bounded-surplus direct theorem remains available. For `n>=23`, a direct fan of order `d`, total hole surplus `eta<=d-2`, and at most four external exceptions is triangle-free or already satisfies `m<=M(n)`. Thus every live triangle-containing above-`M(n)` survivor has

> `eta>=d-1` or `z>=5`.

This is supporting structure; the current primary attack is the Hall-density/source-localization line.

## 11. Audit

The new Hall-density package includes an independent abstract algebra checker. Frozen audit:

- random graph/partition trials: 50,000;
- pair-class instances: 156,014;
- family/subset checks: 834,948;
- failures: 0.

A separate development stress run completed 200,000 random trials with zero failures. These are audit support only; promoted statements are hand derived.

## 12. Live frontier

The previous request for a pair-allocation/majorization theorem has now produced an exact density/stability theorem. The next highest-value move is to combine `(CROSS-LOC)` with the beta/source-support decomposition **before summing over pair classes**.

Two coherent routes are live:

1. **Beta/local-deficit coupling.** Show that beta-forced A--U nonincidence cannot be concentrated entirely in the `<T0+tau` exceptional A-mass while the remaining `>p-tau` mass pays `Ccap_P+L_P+R_P/p-tau a_P`.
2. **Near-equality classification.** Exploit `(RIGID)` plus `(COMP-FORCE)`: a nearly maximal low-capacity family has a complete A-cut, all crossing sources oriented from the complement, near-saturated direct/Hamming credit and near-saturated certificate capacity. Classify or exclude this geometry in the triangle-containing above-`M(n)` branch.

A useful exact reserve form for any family is

> `Sigma_X=sum_{P in X}Sigma_P-2sum_{P<Q in X}a_Pa_Q`.

This identifies the cross-pair quadratic bill that singleton pair inequalities miss.

Do not return to the closed mixed `{4,5}` ladder. Do not optimize for first-proof priority on Erdős #742. Keep `X_3` as the mandatory hostile control.
<!-- CURRENT-STATUS:END -->
