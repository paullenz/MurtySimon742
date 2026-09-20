# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-20  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ALL_R_GRID_RESIDUAL_MAXIMIZER_2026_09_20`

WORK MODE: `MATH_AFTER_AUDIT_GATE`

INSPECTED PREDECESSOR: `c3a82e10a89406770d71ed613671296ee7f0f302`

LAST VERIFIED RESULT: `The 20 September daily red-team audit remains binding. Its mandatory same-code raw-criticality / ordered (source,witness) audit passed independently at c3a82e10.... Inside the literal all-R equality pinch this run proves g=x-k>=1; exact m-sensitive internal-witness score/hole bills; fixed-head C/D classification of every X--Y certificate for y>=2; a residual g-by-y certificate-grid dichotomy s_D>=g OR s_C>=y; full independence of the entire outside cross-witness population; d>=m+min(g,y); epsilon_z+epsilon_{a_0}>=2p+k+u-y+m+min(g,y)-2; and a q surcharge of at least binom(min(g,y),2) physical U--U holes. Type-aware cross loads give Z_X>=Z_X^0+NJ+e+m+R_C+s_D(x-1) and Z>=Z_0+NJ+e+m(y+1)+gy+s_C(y-1)+s_D(x-1). In y=1, the edge a_0y cannot use the special matched foot and forces one outside bar-C witness. The grid structure compresses the rooted residual condition to a one-dimensional d-gate R_grid(d,m)>=a. Its exact first differences show the maximum occurs only at the score-switch neighbours and d=T-2,T-1 (with clipped endpoints), reducing the d-search to a constant-size candidate set independent of u. This maximizer-location algebra was independently brute-force checked over T<60, all lower endpoints, -10<=A<100 and 0<=phi<50 with zero mismatches; a repository checker is preserved.`

UNPRESERVED WORK: `None. Live package: project/research/post_ms/2026-09-20-all-r-exact-local-optimization-v1/. Key files: ALL_R_EXACT_LOCAL_OPTIMIZATION.md; CROSS_EDGE_RESERVOIR_SHARPENING.md; TYPED_CROSS_HOLE_LEDGER.md; CROSS_GRID_COVER_DICHOTOMY.md; CROSS_WITNESS_INDEPENDENCE.md; CROSS_WITNESS_FULL_INDEPENDENCE.md; GRID_CONSERVATION_COROLLARY.md; Y1_SPECIAL_FOOT_OBSTRUCTION.md; GRID_RESIDUAL_GATE.md; GRID_RESIDUAL_MAXIMIZER.md; check_grid_residual_maximizer.py; plus exact-local/cross-reservoir diagnostics.`

DEFERRED ADMIN: `README intentionally remains at the independently audited 20 September checkpoint; do not promote same-hour conditional sharpenings before independent replay/adversarial review. The inherited dead t-choice output in check_all_r_pinch_local_feedback.py remains low-priority reviewer-facing cleanup.`

NEXT_ACTION: `First independently replay the new committed exact-local/cross-reservoir diagnostics and build a total typed checker retaining (d,m,e,s_C,s_D,R_C,R_D), ZX-TYPED/Z-TYPED and full CROSS-INDEP. Analytically substitute the constant-size d-maximizer candidates from GRID_RESIDUAL_MAXIMIZER.md into R-GRID and classify any unbounded parameter families rather than scanning d. Structurally split row-saturated and column-saturated residual-grid regimes and seek genuinely new multi-witness interactions; do not reuse the dead witness--head iteration because it recycles the original source certificate. Keep y=1 separate. After this local arm reaches a natural closure, return to the audit's zero-positive-fixture rigid complete-cut interface. Exact pair-local Ccap_P, ONE-P and CROWD remain local. No bounded scan may be promoted to an asymptotic threshold. Larger reservoirs, loaded-buffer, z=2 and four-exception work stay subordinate.`
<!-- CURRENT-STATUS:END -->

---

## Binding audit gate

Latest daily audit: `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Still binding: repaired P1/P2 semantics; `X_3`; zero positive actual-D2C rigid complete Hall cuts with `x>=3` in bounded regression; exact pair-local `Ccap_P`, `(ONE-P)`, `(CROWD)`; finite rows are diagnostics only; superseded alpha/beta evidence, invalid matched-only common-buffer orientation, and historical 188,912 / 179,735 / 178,572 counts stay superseded.

The audit-mandated same-code raw-criticality proof at `project/research/post_ms/2026-09-20-same-code-raw-criticality-audit-v1/SAME_CODE_RAW_CRITICALITY_AUDIT.md` passed.

## Live formulas

For y>=2 put `h=min(g,y)`, `T=u-k-2`, `J=T-d`. Internal witnesses: `m<=d`, `m<=e<=m(x-2)` for m>0, `P_int=[e-m(x-p-2)]_+`.

Residual certificate grid:

`R_C+R_D=gy`, `s_C<=R_C<=s_C g`, `s_D<=R_D<=s_D y`, `s_D>=g OR s_C>=y`, `m+s_C+s_D<=d`.

Type-aware bills:

`P_cross >= [R_C-s_C[x-p+1]_+]_+ + R_D+s_D(p-y-1)`,

`epsilon_{a_0}>=p+u-y-d+m+s_C+s_D-1`,

`Z_X>=Z_X^0+NJ+e+m+R_C+s_D(x-1)`,

`Z>=Z_0+NJ+e+m(y+1)+gy+s_C(y-1)+s_D(x-1)`,

`q<=binom(u,2)-binom(k+1,2)-k-d-binom(J,2)-binom(s_C+s_D,2)`.

Compact grid bills:

`d>=m+h`,

`epsilon_z+epsilon_{a_0}>=2p+k+u-y+m+h-2`,

`q<=Q_grid(d)=binom(u,2)-binom(k+1,2)-k-d-binom(T-d,2)-binom(h,2)`.

With `L_Y=y(p-g+2)`,

`E_U<=C0-max{phi(g),L_Y+p+u-y-d+m+h-1}`.

The rooted identity gives the one-dimensional necessary gate

`a<=R_grid(d,m)=(p-lambda)(p+u)+Q_grid(d)+C0-max{phi(g),L_Y+p+u-y-d+m+h-1}`

for some integer `m+h<=d<=T`.

Let `A=L_Y+p+u-y+m+h-1`. Then

`Q_grid(d+1)-Q_grid(d)=T-d-2`;

when `A-d>=phi(g)`, `R_grid(d+1)-R_grid(d)=T-d-1`;

when `A-d<=phi(g)`, the difference is `T-d-2`.

Hence the maximum needs checking only at clipped values among `floor(A-phi(g))`, `floor(A-phi(g))+1`, `T-2`, `T-1`, plus an endpoint if clipping removes its neighbour.

## Diagnostic evidence labels

Independently audited predecessor: 173,347 equality-pinch rows; 124,528 after the d-based package.

Same-hour provisional: 78,582 total under exact `(d,m,e)` plus crude cross capacity; 71,996 total under type-relaxed cross population/score; focused typed e=0 slice 62,800 after physical holes, 60,552 after grid cover, 58,999 after same-type independence; y=1 mandatory outside witness reduces its slice 4,607 -> 4,523, giving combined focused current e=0 slice 58,915. No total typed count stronger than 71,996 is promoted yet.

## Session ledger

**Invocation start:** ~01:29 BST.  
**Preservation cutoff:** ~01:55 BST.

Substantive units completed:

1. audit/raw-criticality reconciliation;
2. `g>=1` core-head gate;
3. m-sensitive z/a0 conservation;
4. internal-witness physical `Z_X/Z` ledger;
5. exact fixed-m load price and Hall gate;
6. raw complete-cut C/D witness-star classification;
7. cross/internal witness disjointness and cross slack bill;
8. typed cross physical-hole ledger;
9. residual grid-cover dichotomy;
10. same-type cross-witness independence;
11. parameter-only grid conservation synthesis;
12. y=1 special-foot obstruction;
13. certificate-recycling obstruction for naive witness--head iteration;
14. full C--D cross-type independence;
15. grid-compressed one-dimensional rooted residual gate;
16. exact constant-size candidate classification for the d-maximizer, independently brute-force checked with zero mismatches in the stated range.

**Live unfinished line:** total typed checker; substitution/classification of the explicit d-maximizer cases; structural interaction in row-saturated/column-saturated regimes.

**Stop reason:** preservation cutoff approached; no mathematical blocker.
