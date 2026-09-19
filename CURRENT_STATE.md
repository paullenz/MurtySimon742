# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_T1_FIXED_FOOT_TARGET_INJECTIVITY_SHARED_CORE_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `14948a7cb4944ba8aea58cde306e2dee2abd0f78`

LAST VERIFIED RESULT: `The t=1 exceptional matched foot is graph-fixed strongly enough to make wrong-head traffic target-injective: for a target h, every wrong-head edge would require the same fixed pair (h,q_e) to have singleton common-neighbour set equal to its selected source, so one target head receives at most one selected wrong-head witness. The predecessor support-only J<=2k shared-core count therefore tightens to J<=k. In the corrected shared-core R2+R2 core-target orientation, z_* cannot meet any H_M head, so A=g exactly. The exceptional-pair X-edge localization then forces every X-edge to have a core endpoint; the two radius-two defects are isolated because they are nonadjacent to q_e; every remaining X-edge joins a core head to a nondefect radius-one H_M head, has Hamming length two, and each core head has X-degree at most one. Thus G[X] is a star forest and wrong-head targets compete with X-edge leaves for the same physical core heads: J+e(X)<=k. Retaining exact pair-local sigma_P gives p^2+M+e+[D+2(Emax-e)]_+<=C0-sigma_P, Emax=binom(g,2)+kg. Eliminating e yields F_k(R)=0 for R<=0, ceil(R/2) for 0<R<=2k, and R-k for R>=2k, R=D+2Emax. The audited local slot inequality strengthens in this star forest to r>=a+y+2+e+c_X, hence safely r>=a+y+2+e+1_{e>0}. Independent replay of the existing bounded t=1 no-E1 diagnostic reproduces 933 states, 509 with k>=3; 477 have an A=g row, only 147 retain a compatible star-forest e-range, and zero satisfy the new exact pair-local shared-core gate (minimum failure margin 9). This is an abstract parameter diagnostic, not graph-realizability evidence or a global closure.`

UNPRESERVED WORK: `None at this checkpoint. The theorem note and independent arithmetic replay are preserved under project/research/post_ms/2026-09-19-fixed-foot-target-injectivity-v1/. The predecessor exceptional-gamma theorem remains load-bearing; its support-only J<=2k hierarchy is explicitly superseded by fixed-foot target injectivity, while its matched-foot localization remains retained.`

DEFERRED ADMIN: `README remains synchronized to the 19 September daily audit trust boundary and need not be rewritten for every mathematical checkpoint. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires earlier repair.`

NEXT ACTION: `Stay on m=g+1,t=1,k>=3,E=2. First try to turn the new closed pair gate p^2+M+F_k(D+2Emax)<=C0-sigma_P, together with y>0 and the exact definitions of D,Emax,C0,sigma_P, into a compact analytic exclusion of the shared-core core-target family over the full parameter range. If a residual analytic family survives, intersect it with the exact star-forest slot floor r>=a+y+2+e+c_X and the rooted q/E_U ceiling; do not add another loose scalar relaxation. Only after the shared-core family is analytically closed or sharply parameterized should the now-tied J<=k one-core R2+R2 and core-containing R3 alternatives be opened. Keep k=2,k=1,m=g+2,loaded buffer,z=2,and the four-exception gate deferred. Keep X_3 and the graph-level audit boundary explicit.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

This run began by rereading `CURRENT_STATE.md`, root `README.md`, the latest commits, the 19 September daily adversarial audit, `SOURCE_PREMISE_REPAIR.md`, the actual-D2C graph-level regression status, and the latest exceptional-gamma-foot handoff before doing forward mathematics.

Binding trust boundary:

- distinct physical beta-source identity: raw-criticality proved;
- `(source,coordinate)` uniqueness: selected representative only;
- finite source-tuple theorem: not unconditional graph-level closure;
- actual-D2C regression: 3,540 root-policy instances, 147 exact pair-capacity checks, 36 Hall decompositions, zero recorded mismatches, `X_3` retained;
- no bounded actual D2C fixture realizes the full rigid complete-cut hypotheses, so the live branch remains conditional hand mathematics;
- exact pair-local `S_P/Ccap_P` remains mandatory;
- four-exception gate remains subordinate.

There is no departure from the audit priority order. The current work strengthens the raw-criticality matched-foot line identified by the predecessor and then feeds it directly into pair-local and rooted-slot quantities.

---

## 2. Fixed-foot target injectivity

The predecessor proved that in the `t=1` minimal-reservoir layer every selected outside-witness wrong-head edge `z_s h` uses the same exceptional matched foot `q_e` and satisfies

`N(h) cap N(q_e)={z_s}`.

Therefore a fixed target head cannot receive two distinct selected wrong-head witnesses: the fixed common-neighbour set for `(h,q_e)` cannot be two different singletons.

Hence every target head receives at most one wrong-head incidence. In particular, when the unique target code is the repeated core code,

`J<=k`.

The predecessor's support-only `J<=2k` shared-core envelope is superseded. Its matched-foot localization is retained.

---

## 3. Corrected shared-core `R2+R2` geometry

Retain core support `{r}`, defect supports `{r,i}` and `{r,j}`, with the unique exceptional coordinate `e=r` and target code equal to the core code.

The common core witness `z_*` cannot have any wrong-head neighbour in `H_M`, because every wrong-head target code is the core code. Therefore

`A=g`.

Every X-edge is covered by the exceptional gamma pair, and in this orientation the represented exceptional code is the core code. Hence every X-edge has a core endpoint. The fixed matched-foot singleton argument gives core X-degree at most one.

Both radius-two defects are nonadjacent to the `d`-selected exceptional foot `q_e` because their supports contain `r`. Therefore neither can be the non-core endpoint of a core X-edge. They are isolated in `G[X]`.

Thus every actual X-edge joins a core vertex of support `{r}` to a nondefect radius-one singleton support `{s}`, `s!=r`, and has Hamming distance two. `G[X]` is a star forest with core leaves and nondefect `H_M` centers.

---

## 4. Core-head conservation

A core head targeted by a wrong-head witness has singleton common-neighbour set with `q_e` equal to that outside witness. A core head incident with an X-edge has the same fixed pair `(core,q_e)` with singleton common neighbour equal to its X-neighbour. These cannot both occur.

Target injectivity makes the wrong-head targets distinct, and core X-degree at most one makes X-edge leaves distinct. Hence

`J+e(X)<=k`.

If `J>0`, an active defect witness must be nonadjacent to `z_*` by the core witness singleton certificate, so `M>=1`. No stronger multiplicity in M is currently claimed.

---

## 5. Exact pair-local V-gate

At `t=1`, selected outside-witness slack obeys

`sum epsilon_selected >= p^2+k+M-J >= p^2+M+e`,

where `e=e(X)`.

With `A=g`, put

`Emax=binom(g,2)+kg`,

`R=D+2Emax`.

Then

`L_X >= [R-2e]_+`.

Retaining exact pair-local `sigma_P`, every shared-core survivor satisfies

`p^2+M+e+[R-2e]_+ <= C0-sigma_P`, `0<=e<=k`.

The exact elimination is

`F_k(R)=min_{0<=e<=k}{e+[R-2e]_+}`

with

- `F_k(R)=0` for `R<=0`;
- `F_k(R)=ceil(R/2)` for `0<R<=2k`;
- `F_k(R)=R-k` for `R>=2k`.

Hence

`p^2+M+F_k(R)<=C0-sigma_P`.

If M=0, then J=0 and the stronger special gate is

`p^2+k+[D+2(Emax-k)]_+<=C0-sigma_P`.

---

## 6. Star-forest rooted-slot floor

The audited local inequality is

`sum_{w in N_A(z)} d_H(c(w),c(z)) <= r_z d_A(z)`.

In shared-core E2:

- every Y vertex sees X-to-d total Hamming length `x+2`, so costs at least two slots;
- each isolated core head costs one, while each core X-leaf costs two;
- both radius-two defects cost two despite being X-isolated;
- each nondefect H_M star center costs two, while an isolated radius-one H_M head costs one.

If `c_X` is the number of nonisolated H_M star centers,

`r>=a+y+2+e+c_X`.

Safely,

`r>=a+y+2+e+1_{e>0}`.

This is a physical local-slot statement, not an abstract density relaxation.

---

## 7. Diagnostic status

The independent checker under

`project/research/post_ms/2026-09-19-fixed-foot-target-injectivity-v1/`

replays the same bounded abstract box as the predecessor and first reproduces the known `t=1` no-E1 distribution exactly:

`933` total, with `509` at `k>=3`.

For those 509 states:

- 477 have at least one predecessor row with `A=g`;
- 147 have a nonempty star-forest X-edge range after the predecessor density floor;
- 0 pass the new exact pair-local shared-core gate;
- the smallest pair-budget failure margin among those 147 is 9.

No graph-realizability conclusion is drawn from this scan. The zero count is evidence that the analytic shared-core gate is worth trying to close exactly before broadening topology.

---

## 8. Preserved package

`project/research/post_ms/2026-09-19-fixed-foot-target-injectivity-v1/T1_EXCEPTIONAL_TARGET_INJECTIVITY_SHARED_CORE.md`

`project/research/post_ms/2026-09-19-fixed-foot-target-injectivity-v1/check_fixed_foot_target_injectivity.py`

The checker is an arithmetic/parameter diagnostic only. The fixed-foot injectivity, star-forest classification, conservation law, pair gate, and local-slot floor are hand deductions from the preserved criticality and slot lemmas.

---

## 9. Next work

Do not return to the superseded `d0=2` endpoint or its old 39-row ledger as a live route.

Stay on the corrected shared-core family long enough to seek a compact analytic exclusion from the closed pair gate. If that leaves a real asymptotic family, use the star-forest slot floor and exact rooted residual ceiling on that family. If shared-core closes, move immediately to the tied `J<=k` alternatives: one-core `R2+R2` and core-containing `R3`, retaining the same fixed-foot target injectivity and exact pair-local accounting.
