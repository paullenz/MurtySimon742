# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-20  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `FIRST_STRICT_MAXIMAL_M2_FR_RAW_EDGE_COLLAPSE_2026_09_20`

WORK MODE: `MATH_AFTER_AUDIT_GATE`

INSPECTED_PREDECESSOR_HEAD: `d981985a7f1acecfd45e27ceb517436b206f580c`

LATEST_NEW_COMMITS: `401247423e04c1180a9d4401f7a26f9a9887af80` (raw-edge collapse theorem package), `13d83c51ac7a4e093fd2e7998da7a70db0101efb` (companion diagnostic).

LAST VERIFIED/AUDITED BASE: `The 20 September daily red-team audit remains binding. P1/P2 semantics are repaired; the raw same-code criticality theorem and ordered (source,witness) injection were independently re-derived and passed; X_3 remains mandatory; exact pair-local Ccap_P/(ONE-P)/(CROWD) remain load-bearing; finite scans remain diagnostics only; and bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with x>=3.`

PREDECESSOR CORRECTION: `The m=2 bulk-block proof at MAXIMAL_SELECTION_MATCHING_AND_M1_CLOSURE.md Section 11 had a radius-one scope omission. M2_BULK_BLOCK_SCOPE_CORRECTION.md repairs it. The final large-X normal form survives: for maximal m=2, p>=3, x>=4 there are exactly two complementary X' code classes, one F and one R, |S_0|=1, I_F=S_0 and I_R=I_0. Future work must cite the correction rather than the unqualified Section 11 argument.`

NEW INTERNAL CANDIDATE RESULT: `In the corrected maximal-m=2, p>=3, x>=4, omega=|U_o|>2 F/R normal form, let f be the unique F-head, R_X the x-2 R-heads, z_R the unique R-witness and Z_F=U_o\{z_R}. Raw same-code criticality plus the fixed certificate identities N(f)∩N(z)={b} for z in Z_F and N(r)∩N(z_R)={b} for r in R_X force: (i) Z_F--R_X empty; (ii) z_R--Z_F empty; (iii) z_R f absent and hence N_A(z_R)={a_0}; (iv) every z in Z_F is A-anticomplete; therefore G[U_o] is edgeless. This gives epsilon_z>=p+omega-1 for z in Z_F, epsilon_zR>=p+omega-2 and E_Uo>=omega^2+(p-1)omega-1, together with q<=C(u,2)-C(k+1,2)-C(omega,2)-(k-1). A second raw criticality exhaustion forces f--R_X empty, then G[R_X] empty, and finally a_0f absent. Since Type R already gives a_0--R_X empty, G[X] is entirely edgeless in this branch.`

PAIR_LOCAL CONSEQUENCE: `Let Sigma_P(omega) be the exact pair-local threshold incorporating exact core floor, buffer slack, physical Y-price L_Y=y(p-g+1+omega), CROWD and Ccap_P. Since U_o has neither d nor bar d code for p>=3, every omega>2 survivor obeys Sigma_P(omega)+omega^2+(p-1)omega-1<=C0. Do not replace Sigma_P by total score.`

DIAGNOSTIC STATUS: `A same-session independent implementation of the strengthened physical-reservoir gate over the historical broad box gives omega>2 base 182396, pair survivors 171981, score survivors 103860 and conservative rooted-residual survivors 73663. The committed checker check_m2_fr_raw_edge_collapse.py records these expected values. They are abstract necessary-condition rows, not graph counts, and must be independently replayed before reviewer-facing use. The diagnostic deliberately does NOT scalarize the new e(X)=0 theorem.`

UNPRESERVED_WORK: `None from this invocation. New theorem and checker are committed. The strongest unused consequence is e(X)=0 itself: it has not yet been reinserted into the exact Hall-density identity / rooted residual ledger.`

DEFERRED_ADMIN: `README intentionally remains at the independently audited 20 September public checkpoint. Same-hour m=2 closures are provisional until adversarial replay. Historical m=1 and all-R d/J/grid work remains preserved with its original trust boundaries.`

NEXT_ACTION: `First independently replay check_m2_fr_raw_edge_collapse.py and hostile-audit the new raw edge exclusions, especially cross-code f--R_X and a_0f. If they pass, exploit e(X)=0 exactly in the Hall-density / residual ledger rather than adding another weak scalar score inequality. Attempt an analytic contradiction or characterize any surviving scaling family. Only then split omega=2, x=3 and p<=2. Keep loaded-buffer, z=2 and four-exception routes subordinate. In parallel, retain the zero-positive-fixture rigid-cut interface as the dominant global audit risk.`
<!-- CURRENT-STATUS:END -->

---

## Binding audit gate

Latest daily audit: `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Still binding:

- repaired P1/P2 semantics;
- `X_3` mandatory negative control;
- zero positive actual-D2C rigid complete Hall cuts with `x>=3` in bounded regression;
- exact pair-local `Ccap_P`, `(ONE-P)`, `(CROWD)`;
- finite parameter rows are diagnostics only;
- superseded alpha/beta evidence, invalid matched-only common-buffer orientation and historical 188,912 / 179,735 / 178,572 counts stay superseded;
- same-hour closures remain provisional until independently re-derived.

Raw same-code audit: `project/research/post_ms/2026-09-20-same-code-raw-criticality-audit-v1/SAME_CODE_RAW_CRITICALITY_AUDIT.md` — passed.

## Live structural chain

`audited rigid first-strict unique-hole`
`-> raw outside eligibility graph H`
`-> maximal representative image m=nu(H)`
`-> maximal m=1 completely closed`
`-> maximal m=2, p>=3, x>=4 has two corrected complementary F/R code classes`
`-> omega>2: one F-head f, bulk R_X, unique R-witness z_R, F-star reservoir Z_F`
`-> full U_o independence + A-anticomplete Z_F + N_A(z_R)={a_0}`
`-> E_Uo>=omega^2+(p-1)omega-1 and full binom(omega,2) q loss`
`-> raw cross-code exhaustion gives G[X]=empty`
`-> exact Hall/residual reinsertion is the live unfinished line.`

Key files:

- `project/research/post_ms/2026-09-20-maximal-selection-matching-v1/MAXIMAL_SELECTION_MATCHING_AND_M1_CLOSURE.md`
- `project/research/post_ms/2026-09-20-maximal-selection-matching-v1/M2_BULK_BLOCK_SCOPE_CORRECTION.md`
- `project/research/post_ms/2026-09-20-maximal-selection-matching-v1/M2_FR_RESERVOIR.md`
- `project/research/post_ms/2026-09-20-maximal-selection-matching-v1/M2_FR_RAW_EDGE_COLLAPSE.md`
- `project/research/post_ms/2026-09-20-maximal-selection-matching-v1/check_m2_fr_raw_edge_collapse.py`

## Session ledger — current invocation

**Invocation start:** 03:27:23 BST.  
**Planned preservation cutoff:** 03:55:38 BST.

Substantive units completed:

1. reconciled the stale handoff against the newer maximal-m=2 commit chain and mandatory radius-one scope correction;
2. proved `Z_F--R_X` is empty from the raw same-code theorem plus fixed eligibility common-neighbour sets;
3. proved `z_R--Z_F` is empty, upgrading the previous `Z_F` independence to full `G[U_o]` independence;
4. proved `z_Rf` is absent and hence `N_A(z_R)={a_0}`;
5. proved every F-star witness is A-anticomplete and derived the sharp physical outside-reservoir bill `E_Uo>=omega^2+(p-1)omega-1` plus full `binom(omega,2)` rooted-triangle loss;
6. exhausted raw criticality for the complementary X-code edges, proving `f--R_X` empty, then `G[R_X]` empty, then `a_0f` absent, hence `G[X]=empty`;
7. combined the physical reservoir with the exact pair-local threshold and independently scanned the broad diagnostic box, reducing omega>2 residual rows from the predecessor 110759 to 73663 without yet using the full force of `e(X)=0`.

**Live unfinished line:** independently replay/audit the new edge-collapse theorem, then insert `e(X)=0` into the exact Hall-density and rooted residual identities to seek an analytic closure or explicit scaling family.

**Stop reason:** preservation cutoff approached after a shortened late-start window; no mathematical blocker and no early clean-checkpoint stop.
