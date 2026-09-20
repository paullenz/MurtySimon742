# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-20  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ALL_R_FULL_CROSS_WITNESS_INDEPENDENCE_2026_09_20`

WORK MODE: `MATH_AFTER_AUDIT_GATE`

INSPECTED PREDECESSOR: `c3a82e10a89406770d71ed613671296ee7f0f302`

LAST VERIFIED RESULT: `The 20 September daily red-team audit remains binding. Its mandatory same-code raw-criticality / ordered (source,witness) gate has passed independently at c3a82e10..., including head reserve and strengthened witness pricing. In the literal all-R equality pinch the current run proves: g=x-k>=1; exact m-sensitive internal-witness score/hole bills; for y>=2 every X--Y certificate is a fixed-head bar-C column witness or fixed-head bar-d row witness; after maximal core credit the remaining g-by-y certificate grid satisfies s_D>=g OR s_C>=y, hence d>=m+min(g,y); the entire outside cross-witness population (not only each type separately) is independent in U; therefore q loses binom(s_C+s_D,2) physical pairs and in particular at least binom(min(g,y),2); epsilon_z+epsilon_{a_0}>=2p+k+u-y+m+min(g,y)-2; type-aware cross loads force Z_X>=Z_X^0+NJ+e+m+R_C+s_D(x-1) and Z>=Z_0+NJ+e+m(y+1)+gy+s_C(y-1)+s_D(x-1). In y=1 the edge a_0y cannot use the special matched foot because z is a second common neighbour, so at least one outside bar-C witness is still mandatory.`

UNPRESERVED WORK: `None. The live package is project/research/post_ms/2026-09-20-all-r-exact-local-optimization-v1/. It contains ALL_R_EXACT_LOCAL_OPTIMIZATION.md, CROSS_EDGE_RESERVOIR_SHARPENING.md, TYPED_CROSS_HOLE_LEDGER.md, CROSS_GRID_COVER_DICHOTOMY.md, CROSS_WITNESS_INDEPENDENCE.md, CROSS_WITNESS_FULL_INDEPENDENCE.md, GRID_CONSERVATION_COROLLARY.md, Y1_SPECIAL_FOOT_OBSTRUCTION.md, and committed diagnostic scripts. Same-hour diagnostic counts remain provisional until independent replay.`

DEFERRED ADMIN: `README intentionally remains at the independently audited 20 September checkpoint. Do not promote same-hour sharpenings there before replay/adversarial review. The inherited dead t-choice output in check_all_r_pinch_local_feedback.py is still a low-priority reviewer-facing cleanup item.`

NEXT_ACTION: `Remain in the literal all-R equality pinch. Build and independently replay a total typed checker retaining (d,m,e,s_C,s_D,R_C,R_D), ZX-TYPED/Z-TYPED and full CROSS-INDEP; do not infer a total count from the e=0 slice. Structurally split the residual grid into row-saturated and column-saturated regimes and seek a genuinely new interaction between multiple fixed-head witnesses. The naive witness--head-edge criticality iteration is a dead end because the original source recycles as the certificate. Keep y=1 separate. After this local arm reaches a natural closure, return to the audit's unresolved zero-positive-fixture rigid complete-cut interface. Exact pair-local Ccap_P, ONE-P and CROWD remain local. No bounded scan may be promoted to an asymptotic threshold. Larger reservoirs, loaded-buffer, z=2 and four-exception work stay subordinate.`
<!-- CURRENT-STATUS:END -->

---

## Binding audit gate

Latest daily audit: `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Still binding:

- repaired P1/P2 semantics;
- `X_3` hostile control;
- no positive actual-D2C rigid complete Hall cut with `x>=3` in the bounded regression;
- exact pair-local `Ccap_P`, `(ONE-P)`, `(CROWD)`;
- finite parameter rows are diagnostics, not graph counts;
- superseded alpha/beta evidence, invalid matched-only common-buffer orientation, and historical 188,912 / 179,735 / 178,572 counts must not be revived.

The audit-mandated same-code raw-criticality proof is preserved at `project/research/post_ms/2026-09-20-same-code-raw-criticality-audit-v1/SAME_CODE_RAW_CRITICALITY_AUDIT.md` and passed.

## Live all-R formulas

Let d count z-nonneighbours in `U_o\{z}`, `J=u_o-1-d`, m be actually used internal-X witnesses, e=`e(X)`, and for `y>=2` let `s_C,s_D,R_C,R_D` describe outside cross witnesses and their selected residual-grid loads.

Internal witness constraints:

`m<=d`, `m<=e<=m(x-2)` for `m>0`,

`P_int(e,m)=[e-m(x-p-2)]_+`,

`Z_X>=Z_X^0+NJ+e+m`,

`Z>=Z_0+NJ+e+m(y+1)`.

Residual cross grid:

`R_C+R_D=gy`,

`s_C<=R_C<=s_C g`,

`s_D<=R_D<=s_D y`,

`s_D>=g OR s_C>=y`,

`m+s_C+s_D<=d`.

Type-aware bills:

`P_cross >= [R_C-s_C[x-p+1]_+]_+ + R_D+s_D(p-y-1)`,

`epsilon_{a_0}>=p+u-y-d+m+s_C+s_D-1`,

`Z_X>=Z_X^0+NJ+e+m+R_C+s_D(x-1)`,

`Z>=Z_0+NJ+e+m(y+1)+gy+s_C(y-1)+s_D(x-1)`,

`q<=binom(u,2)-binom(k+1,2)-k-d-binom(J,2)-binom(s_C+s_D,2)`.

Compact consequences for `y>=2`:

`d>=m+min(g,y)`,

`epsilon_z+epsilon_{a_0}>=2p+k+u-y+m+min(g,y)-2`,

`q<=binom(u,2)-binom(k+1,2)-k-d-binom(J,2)-binom(min(g,y),2)`.

For `y=1`, the full residual-grid theorem is not asserted, but `a_0y` still forces one outside bar-C witness among the d z-nonneighbours.

## Diagnostic labels

Independently audited predecessor: `173,347` equality-pinch rows; `124,528` after the d-based local package.

Same-hour provisional diagnostics:

- `78,582` total rows under exact `(d,m,e)` plus crude cross capacity;
- `71,996` total rows under type-relaxed cross population/score;
- focused typed `e=0` slice: `62,800` after typed physical holes;
- `60,552` after residual grid cover;
- `58,999` after same-type independence (`54,392` for `y>=2`, `4,607` for `y=1`);
- y=1 mandatory outside witness reduces its disjoint slice to `4,523`, giving a combined focused current `e=0` slice of `58,915` rows.

No total typed count stronger than `71,996` is promoted yet.

## Session ledger

**Invocation start:** ~01:29 BST.  
**Preservation cutoff:** ~01:55 BST.

Substantive units completed this run:

1. audit/raw-criticality reconciliation;
2. `g>=1` core-head gate;
3. m-sensitive z/a0 conservation;
4. internal-witness `Z_X/Z` ledger;
5. exact fixed-m load price and Hall gate;
6. raw complete-cut C/D witness-star classification;
7. cross/internal witness disjointness and cross slack bill;
8. typed `R_C/R_D,s_C/s_D` hole ledger;
9. residual grid-cover dichotomy;
10. same-type witness independence;
11. parameter-only grid conservation synthesis;
12. y=1 special-foot obstruction;
13. certificate-recycling obstruction for the naive witness--head iteration;
14. full C--D cross-type independence, so the entire outside cross population is independent.

**Live unfinished line:** total typed checker plus structural interaction of multiple fixed-head witnesses in row-saturated / column-saturated regimes.

**Stop reason:** preservation phase before the next invocation; no mathematical blocker.
