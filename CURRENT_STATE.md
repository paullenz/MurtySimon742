# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-20  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `RIGID_DISTINCT_HEAD_NEAR_RIGID_2026_09_20`

WORK MODE: `MATH_AFTER_AUDIT_GATE`

LATEST_RECONCILED_PREDECESSOR_HEAD: `40a1df1b8ab8afdac2e22636e24997a42eb83ec0`.

LATEST_THIS_RUN_COMMITS: `3c49980579ff94c15b75b4db4de3853ebc1808f3` / `8a8cce8db61f5b39a974d82a6e9f48795f31ed7b` (distinct singleton-head support refinement and scope correction), `36912e58fd3973be78d865016a6d3d963fea44c0` (one-code U-occupancy corollary, explicitly scoped as a corollary of predecessor `92d1808`), `baa166a8ad54995081970ca195450b8c599e7fba` (near-rigid distinct-head refinement).

LAST VERIFIED/AUDITED BASE: `The 20 September daily red-team audit remains binding. P1/P2 semantics are repaired; raw same-code criticality and ordered (source,witness) injection independently passed; X_3 remains mandatory; exact pair-local Ccap_P/(ONE-P)/(CROWD) remain load-bearing whenever invoked; finite scans remain diagnostics only; and bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with x>=3. The zero-positive-fixture interface remains the dominant global risk.`

SECOND_STRICT_STATUS: `Same-session candidate chain now closes the exact unloaded second-strict layer to finite order: mixed y=1 x=3 closure gives n<=16; together with x=4 n<=19 and x>=5 n<=33, all mixed-y1 survivors have n<=33; the two-X-hole arm has n<=816; (0,2) is empty and mixed y>=2 is internally closed. Conditional on the rigid one-code interface and predecessor closures, the exact unloaded second-strict layer has no survivor for n>=817. These remain provisional pending daily hostile replay.`

RIGID_INTERFACE_AUDIT: `317867d... independently rederived from raw criticality that M_X=E_X=0 implies a complete A-cut, all selected crossing sources in Y, x distinct physical singleton-head witnesses per source, witnesses only in tight matched endpoints or U, x<=p+u, and complementary U-code concentration. This reduces trust risk in the implication but does not solve reachability; regression still has zero positive fixtures.`

RIGID_SINGLETON_BUDGET: `92d1808... is the predecessor sharp theorem: only physically singleton matched endpoints can relieve rigid crossing demand; one tight fibre contributes at most one such endpoint, so u>=[hx-p]_+, hx<=u+p, and (h-1)x+g0<=lambda+1. Hence any rigid cut requires g0<=lambda+1 and h>=2 requires lambda+1-g0>=x. Do not attribute this p-budget to the later same-session files.`

DISTINCT_HEAD_REFINEMENT: `The new refinement replaces endpoint multiplicity by distinct singleton-head support. For source code d let rho_d be the number of distinct A_X heads among gamma-d tight matched endpoints with singleton A_X-neighbourhood. Then rho_d<=mu_d and sum rho_d<=p, but every d-coded source can matched-certify at most rho_d distinct crossing heads. Therefore k_d>=[x-rho_d]_+, u>=sum k_d, Z_X>=(x-1)sum k_d, Z_Y>=sum y_d k_d, and Z_Y>=[xy-p(y-h+1)]_+. This can be strictly stronger than the predecessor when several private coordinates repeat one head.`

NEAR_RIGID_REPLAY: `The hand chain in ONE_CODE_NEAR_RIGID_SLOT_PRICE.md survived same-session hostile replay at its stated scope. For one minimum-U source with actual k_*, if m=x-k_*>=3 then selected matched heads have private coordinates, no two are complementary, J_X<1 forces e(H)<p/4, and exact X-degree bookkeeping gives L_X>xg0-k_*(x-k_*)-p/2. The physical lower endpoint should be k_*>=[x-rho]_+ rather than merely [x-g_P]_+, while phi(g_P) remains a separate pair-local collision price.`

ONE_CODE_U_OCCUPANCY: `Let c=lambda+1-g0>=0. The predecessor rooted collapse gives c<x => h=1. In the one-code case, u=x-p+c and mandatory complementary U-witness population K>=[x-p]_+=[u-c]_+ when x>p. Thus at most c U vertices can escape that population, and Z_X>=(x-1)[u-c]_+. This is a corollary/interpretation of the predecessor p-budget, not a new collapse theorem.`

PROCESS_CORRECTION_THIS_RUN: `During the shortened invocation the latest commit 92d1808 was initially not inspected before independently rediscovering hx<=u+p and the rooted collapse. The duplicate claim was then explicitly corrected: RIGID_SINGLETON_GAMMA_BUDGET_SHARPENING.md now preserves only the genuinely new distinct-head rho_d refinement, and RIGID_SINGLETON_BUDGET_ROOTED_COLLAPSE.md now preserves only the one-code U-occupancy corollary. Do not double-count these as independent theorems.`

NEXT_ACTION: `Keep the rigid-interface zero-fixture problem in front. In the one-code near-rigid regime retain c=lambda+1-g0, rho, actual k_*, g_P, L_X, E_U, Z_X, R_X, and exact pair-local Ccap_P/(ONE-P)/(CROWD) simultaneously. First determine whether k_*>=[x-rho]_+ plus at-most-c escaping U vertices forces a stronger local pair-capacity or rooted-slot contradiction; do not collapse rho into g_P. In the multi-code regime use predecessor (h-1)x+g0<=lambda+1 and the rho_d code-specific deficits. If an unbounded family remains after exact local optimization, characterize it rather than adding another weak scalar inequality. Maintain X_3 and the zero-positive-fixture caveat.`
<!-- CURRENT-STATUS:END -->

---

## Binding audit gate

Latest daily audit: `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Binding constraints:

- repaired P1/P2 semantics;
- raw same-code criticality / ordered `(source,witness)` injection independently passed;
- `X_3` mandatory negative control;
- zero positive actual-D2C rigid complete Hall cuts with `x>=3` in bounded regression;
- exact pair-local `Ccap_P`, `(ONE-P)`, `(CROWD)` whenever invoked;
- finite scans are diagnostics only;
- superseded evidence stays superseded;
- same-session closures stay provisional until independent adversarial replay.

## Live structural chain

`audited rooted/Hall setup`
`-> independently rederived rigid singleton-head implication`
`-> provisional exact unloaded second-strict finite-order closure (n<817 branch threshold)`
`-> sharpened physical singleton matched budget (predecessor 92d1808)`
`-> rooted strip (h-1)x+g0<=lambda+1`
`-> one-code near-rigid private-coordinate versus U-defect tradeoff`
`-> new distinct-head support rho prevents repeated private coordinates on one head from acting as multiple matched heads`.

The public README remains deliberately at the independently audited checkpoint. Do not promote these same-session rigid-interface refinements there before the daily red-team replay.

## Session ledger — current invocation

**Invocation start:** 09:26:11 BST.  
**Planned preservation cutoff:** 09:55:38 BST.

Substantive units completed:

1. reread `CURRENT_STATE.md`, README, the 20 September daily red-team audit and latest commits; reconciled the stale handoff against the x=3 closure and the newer rigid-interface direct-audit / gamma / private-coordinate / near-rigid packages;
2. hostile-replayed the near-rigid Hamming-slot chain and found its key inequalities internally consistent at the stated conditional scope;
3. isolated the physically sharper matched-capacity object `rho_d`, the number of distinct singleton heads rather than singleton endpoints;
4. derived `k_d>=[x-rho_d]_+` and the corresponding code-specific U population, located X--U/Y--U deficit and U-slack bills;
5. derived the multiplicity-sensitive physical bound `Z_Y>=[xy-p(y-h+1)]_+` from the distinct-head budget;
6. translated the one-code rooted gap `c=lambda+1-g0` into the physical occupancy statement `K>=[u-c]_+` and `Z_X>=(x-1)[u-c]_+`;
7. discovered that predecessor commit `92d1808` had already proved the global `p` singleton budget and rooted collapse, then corrected the same-session notes so only the genuinely new `rho_d` refinement and U-occupancy corollary remain claimed.

**Live unfinished line:** exact one-code near-rigid optimization with `(c,rho,k_*,g_P)` kept separate, then pair-local `Ccap_P/(ONE-P)/(CROWD)` and rooted residual feedback. The main global question remains whether the rigid event is realizable at all.

**Stop reason:** preservation phase reached in a shortened invocation after seven tightly connected substantive units, including a same-session attribution/scope correction. No mathematical blocker and no clean-checkpoint early stop.
