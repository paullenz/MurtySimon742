# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly-Foucaud-Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty-Simon / Erdos #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `DAILY_RED_TEAM_AUDIT_2026_09_19`.

**WORK MODE:** `AUDIT`.

**INSPECTED PREDECESSOR:** `0060acd80a376074486563bc537386fe130459d2`.

**LAST VERIFIED RESULT:** The current load-bearing rooted-witness/Hall/rigid-U-witness spine survived the 19 September adversarial audit at the stated internal trust boundary; the rigid witness-deficit inequalities remain conditional on the graph-theoretic premises and are not a global eventual theorem.

**UNPRESERVED WORK:** none.

**DEFERRED ADMIN:** none.

**NEXT ACTION:** Independently re-prove the finite source-tuple theorem, then attack the one-code rigid branch with the exact pair-capacity and crowding inequalities; in parallel build an independent graph-level regression of the rooted/Hall quantities on realizable small D2C graphs including `X_3`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The mixed `{4,5}` selected-excess ladder is closed. The active branch remains the triangle-containing unmatched/errorful antipode regime. No global eventual second-extremal theorem is claimed.

The current structural spine is

`rooted witness-slot residual -> local A-coordinate Hamming budget -> complementary-pair Hall demand -> exact cut decomposition -> capacity-density majorization -> beta expulsion / source-tuple obstruction -> rigid-cut code collapse -> singleton U-witness deficit/slack -> one-code outside pair-capacity/crowding trap`.

## 1. Daily red-team finding

The 19 September audit compared the last pre-window checkpoint `f2e85599491d9804084e9739e1cfcdc6cc088a29` with pre-audit head `0060acd80a376074486563bc537386fe130459d2` (216 intervening commits). The audit concentrated on the current load-bearing theorem spine rather than line-by-line recertifying every superseded side branch.

No fatal mathematical contradiction was found in the current spine. The trust boundary is important: the Hall-density and rigid-witness checkers validate algebraic/incidence consequences on generated abstract systems; they are not independent end-to-end verification that every premise holds for every realizable D2C graph. The finite source-tuple theorem remains a high-priority independent re-proof dependency.

Full audit:

`project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

## 2. Mandatory hostile control

The published Radosavljevic-Stanic-Zivkovic (2024) order-12, size-32 exception is represented by the project's `X_3` construction:

- `n=12`, `m=32>M(12)=31`;
- rooted data `p=4,b=8,a=3,u=0,lambda=4`;
- `q=s=f=r=0`, `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`;
- `G[B]=Q_3`, with the three A-vertices equal to the three coordinate-zero faces.

An independent audit reconstruction confirms that this graph has diameter 2 and that deletion of each of its 32 edges raises the diameter to 3. It remains the mandatory negative control. The repository's direct Figure-1 identification is an internal figure-based certification; a machine-readable author adjacency list has not been independently compared here.

Certification:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

## 3. Rooted residual and exact witness-slot spine

Around a maximum-degree root `v`, write `B=N(v)`, `A=V\N[v]`, with `p` tight antipode pairs and unmatched set `U`, `u=|U|`. Then

> `b=2p+u`,
>
> `a=2p+u-lambda-1`.

Put `q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`. Then

> `Q=e(G[B])=p(p+u-1)+q`,
>
> `delta=b(n-b)-m=r-f`,
>
> `E_U=u(p+u-1)-2q-s`,
>
> `L_A=a(p+u)-s-2f`,
>
> `S=E_U+L_A=2delta+lambda(p+u)-p`,
>
> `delta+Q=L_A+f`,
>
> `f=(p-lambda)(p+u)+q+E_U-delta`. `(RSF)`

For `Omega={(x,z) in B x A : xz notin E(G)}`, every rooted B-edge has a distinct criticality-certificate slot. If `Upsilon` is the unused-slot set, then

> `|Omega|=L_A+2f=Q+r`,
>
> `|Upsilon|=r`,
>
> `delta=|Upsilon|-f`. `(SLOT)`

For each `z in A`, put `r_z=|{(x,z) in Upsilon}|`. The local directional collision bounds remain

> `sum_{y in N_A(z)} d_H(c(y),c(z))<=r_z d_A(z)`, `(LH)`
>
> `p d_D(z)<=r_z d_A(z)`. `(LDF)`

Audit status: hand derivation rechecked; no collision/injection defect found. Still conditional on the rooted setup and criticality-certificate lemma.

Main package: `project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/`.

## 4. Complementary-pair Hall system and exact cut

For complementary pair `P={c,bar c}`, define the preserved pair quantities `a_P,L_P,S_P,R_P,Z_P` and actual chosen non-direct traffic `t_P`. The pair-local capacity remains

> `Ccap_P=R_code(S_P)[g_P+2S_P/(lambda+1)]+2h_P`,
>
> `2t_P<=Ccap_P`. `(CAP)`

For every pair family `X`, mass `x=a_X`,

> `[x(x-T0)-L_X+Z_X-R_X/p]_+<=Ccap_X`. `(HALL-P)`

With

> `M_X=x(a-x)-c_X`, `E_X=t_X-N_X`, `J_X=R_X/p-2D_X`,

we have the exact identities

> `2e(A_X)=x(x-T0)-L_X+Z_X+M_X`, `(DEG-CUT)`
>
> `w_X-x(x-T0)=2E_X+M_X+J_X`, `(EXACT-HALL)`
>
> `W_X-x(x-T0)=2E_X+M_X+J_X+kappa_X`. `(CAP-EXACT)`

Audit status: algebra and sign structure rechecked; random/checker evidence supports the identities, but the abstract checker is not a graph-realizability proof.

## 5. Hall density, rigidity and beta localization

For `rho_P^cap=W_P/a_P`, a low-density family satisfies

> `A_tau<T0+tau`. `(HD)`

and

> `2E_X+M_X+J_X+kappa_X<x(T0+tau-x)`. `(STAB)`

If the right side is `<1`, integrality gives

> `E_X=M_X=0`. `(RIGID)`

The reserve polarization identity remains

> `Sigma_{X union Y}=Sigma_X+Sigma_Y-2xy`. `(POL)`

For beta localization,

> `B_X<=xu-Z_X`, `(BLOCAL)`

and the source-tuple theorem on the complement yields the preserved `HBL/HBL0` bounds.

Audit status: Hall-density algebra verified. The exact finite source-tuple theorem is the next independent re-proof target before this interface is treated as externally stable.

Package: `project/research/post_ms/2026-09-18-hall-density-cut-stability-v1/`.

## 6. Rigid Hall cut code collapse

Assume `E_X=M_X=0`, `X` nonempty proper, `x=a_X>=3`, `Y=A\A_X`, `y=|Y|`. Let `mu_X<=p` count matched B-endpoints with exactly one neighbour in `A_X` and put

> `k=(x-mu_X)_+`.

If `h=h_Y` distinct tight codes occur in Y, the preserved singleton-head witness argument gives

> `hk<=u`,
>
> `h(x-p)_+<=u`. `(COLL)`

Audit status: re-derived; no missing multiplicity case found.

Reference: `project/research/post_ms/2026-09-18-hall-density-cut-stability-v1/RIGID_HALL_WITNESS_GEOMETRY.md`.

## 7. Rigid U-witness deficit, slack and residual pricing

Write `g=x-T0=p-y`. For each outside code, collect its U-witnesses. Reuse multiplicity `t` forces

> `epsilon_w >= [g+t-1]_+`. `(RWI)`

The exact resource floors are

> `Z_X>=hk(x-1)`,
>
> `Z_Y>=yk`,
>
> `Z>=k[y+h(x-1)]`, `(RZ)`
>
> `B_beta<=au-k[y+h(x-1)]`. `(RB)`

With local source-tuple capacity,

> `B_X<=min{x u-hk(x-1),xp-Phi_r(x)}`,
>
> `B_Y<=min{y(u-k),yp-Phi_r(y)}`. `(RBOX)`

For `g>=1`,

> `E_U>=k[y+h(g-1)] = k[p-1+(h-1)(g-1)]`. `(RE+)`

For `g<=1`,

> `E_U>=[yk-(1-g)u]_+`. `(RE-)`

If `Z_rig=k[y+h(x-1)]`, `D=Z_rig-u(p-lambda)`, and `E_rig` is the appropriate right side above, then

> `q+E_U>=E_rig+ceil((D-E_rig)_+/2)`. `(RQE)`

Therefore an above-`M(n)` rigid-cut survivor satisfies the preserved A-edge floor `(RF)` and feasibility envelope `(RFEAS)`.

Audit status: principal derivations rechecked and independent arithmetic replay consistent. The preserved checker is diagnostic support on abstract systems, not an independent realizability certificate.

## 8. One-code outside pair-capacity/crowding trap

If `h=1`, let `P={d,bar d}` be the unique outside code pair. Direct A-edges cannot lie inside Y. Every crossing and internal-Y edge is non-direct traffic sourced in P, giving

> `Ccap_P+L_Y >= y(p+x+k)`. `(ONE)`

When `3y>=D0=5p+5u-3lambda-2`, the aligned-code crowding theorem adds

> `S_P>=y(3y-D0)`. `(CROWD)`

Audit status: the degree/traffic derivation and same-code localization were rechecked without finding a local flaw. This is now the primary forward target: combine the *exact* `Ccap_P` expression with `(ONE)` and `(CROWD)` before relaxing to global scalars.

Package: `project/research/post_ms/2026-09-18-rigid-hall-witness-deficit-v1/`.

## 9. Supporting theorem status

The bounded-surplus direct theorem remains strongly supported: for `n>=23`, a direct fan of order `d>=2`, total hole surplus `eta<=d-2`, and at most four external exceptions is triangle-free or already satisfies `m<=M(n)`. Independent checks during the audit confirmed the safe-coordinate lower bound and final global quadratic inequality. Not every four-vertex kernel criticality subcase was re-derived tonight, so this theorem should be treated as strongly supported rather than fully independently re-certified until needed.

The integrated source-tuple theorem and beta-support inverse remain active but are singled out for independent re-proof before further promotion.

## 10. Checker and trust-boundary summary

Preserved Hall-density audit:

- 50,000 random graph/partition trials;
- 156,014 pair-class instances;
- 834,948 family/subset checks;
- zero reported failures.

Preserved rigid-witness audit:

- 12,841 random abstract witness-incidence systems;
- 100,000 exact integer minimization tests for `(RQE)`;
- 1,910,960 abstract rigid parameter/code-count instances in the recorded diagnostic box;
- 39,902 newly rejected abstract instances (28,102 U-slack, 11,800 beta deficit);
- zero invariant failures.

These are arithmetic/diagnostic checks. They do not count realizable D2C graphs and do not replace a graph-level independent implementation.

## 11. Repository/status audit

The pre-audit head `0060acd80a376074486563bc537386fe130459d2` triggered Status synchronization run `35402717100`, job `105785888407`, which failed at `Check every new commit`.

The failure is deterministic. `scripts/check_status_sync.py` accepts `WORK MODE` values `MATH`, `ADMIN`, `AUDIT`, `STATUS`, and `RECOVERY`; the predecessor used `EVENTUAL_D2C_MATH`. It also requires the exact fields `INSPECTED PREDECESSOR`, `LAST VERIFIED RESULT`, `UNPRESERVED WORK`, `DEFERRED ADMIN`, and `NEXT ACTION`, which were absent.

This checkpoint repairs those fields. Future proof/checker/state publication should be atomic where possible, because status synchronization checks every new commit rather than only final branch state.

README has also been refreshed at this daily reviewer-facing checkpoint: the live frontier is the rigid Hall witness-deficit / one-code trap rather than merely the earlier `n<=294` zero-residual result; the 12-vertex figure certification caveat is stated accurately; and the daily audit/report is linked.

The failed CI run remains part of audit history and is not relabelled as transient.

## 12. Next programme and stop/pivot criteria

1. Independently re-prove the finite source-tuple theorem and beta-support inverse from definitions. Any changed subset quantifier, distinct-source requirement, or capacity term is a blocker.
2. Attack the one-code rigid branch with exact pair-local quantities: `(ONE)` + actual `Ccap_P` + `(CROWD)`. Do not globalize away code-pair information before this combination is exhausted.
3. Build an independent graph-level regression that computes the rooted partition, witness slots, A-codes, Hall terms and rigid-witness quantities directly on realizable small D2C graphs, including `X_3`. The first mismatch is a proof/checker blocker, not a reason to tune the test.
4. Re-audit the remaining four-exception kernel subcases only if that theorem remains load-bearing; otherwise demote it to supporting status.
5. If exact one-code inequalities still leave an asymptotic family, classify that geometry directly and feed forced `q,E_U,f` through `(RF)` and `delta+Q=L_A+f`. Do not add indefinite scalar relaxations.

Keep `X_3` as the mandatory hostile control. Do not return to the closed mixed `{4,5}` ladder. Do not optimize for first-proof priority on Erdos #742.
<!-- CURRENT-STATUS:END -->
