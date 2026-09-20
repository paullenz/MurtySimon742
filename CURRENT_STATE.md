# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-20  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The published 2024 hostile control `X_3` has 12 vertices and 32 edges while `M(12)=31`; it remains mandatory. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ALL_R_CROSS_GRID_COVER_2026_09_20`

WORK MODE: `MATH_AFTER_AUDIT_GATE`

INSPECTED PREDECESSOR: `c3a82e10a89406770d71ed613671296ee7f0f302`

LAST VERIFIED RESULT: `The binding 20 September daily red-team audit remains in force. Its mandatory raw same-code criticality / ordered (source,witness) audit has now passed independently at c3a82e10..., including witness locations, graph-fixed ordered-pair injectivity, head reserve r_w<=x-2, and epsilon_w>=[p-x+r_w+2]_+. Building only after that gate, the current run has sharpened the literal all-R equality pinch. The injective core-head map into X\{a_0} forces g=x-k>=1. For m actually used internal-X witnesses, epsilon_{a_0}>=p+u-y-d+m-1, Z_X>=Z_X^0+NJ+e+m, Z>=Z_0+NJ+e+m(y+1), and the exact internal witness load price is P_int(e,m)=[e-m(x-p-2)]_+, giving e>=B_d+m+P_int. For y>=2, raw criticality of the complete X--Y cut localizes every outside certificate to a bar-C witness with one fixed Y-head or a bar-d witness with one fixed X-head. Granting the k core rows for free leaves a g-by-y residual certificate grid. Its outside witness cover satisfies the sharp dichotomy s_D>=g OR s_C>=y, hence s_C+s_D>=min(g,y) and d>=m+min(g,y). The two same-type outside witness families are each independent in U, so the q ceiling loses at least min{binom(g,2),binom(y,2)} additional physical U--U pairs. The compact conservation consequence is epsilon_z+epsilon_{a_0}>=2p+k+u-y+m+min(g,y)-2. Type-aware certificate loads further force Z_X>=Z_X^0+NJ+e+m+R_C+s_D(x-1) and Z>=Z_0+NJ+e+m(y+1)+gy+s_C(y-1)+s_D(x-1). In the exceptional y=1 slice, the edge a_0y still cannot use the special matched foot because z is a second common neighbour; it therefore forces at least one outside bar-C witness among the d z-nonneighbours.`

UNPRESERVED WORK: `None. New packages in project/research/post_ms/2026-09-20-all-r-exact-local-optimization-v1/: ALL_R_EXACT_LOCAL_OPTIMIZATION.md, CROSS_EDGE_RESERVOIR_SHARPENING.md, TYPED_CROSS_HOLE_LEDGER.md, CROSS_GRID_COVER_DICHOTOMY.md, CROSS_WITNESS_INDEPENDENCE.md, GRID_CONSERVATION_COROLLARY.md, Y1_SPECIAL_FOOT_OBSTRUCTION.md, plus committed exact-local and cross-reservoir diagnostic scripts. Same-hour diagnostics remain provisional until independent replay.`

DEFERRED ADMIN: `README remains at the independently audited 20 September checkpoint; do not promote same-hour conditional sharpenings to the public overview before replay/adversarial review. The inherited dead t-choice output in check_all_r_pinch_local_feedback.py remains a low-priority reviewer-facing cleanup item.`

NEXT_ACTION: `Remain in the all-R equality pinch. First build/replay a total typed checker retaining (d,m,e,s_C,s_D,R_C,R_D) together with ZX-TYPED/Z-TYPED and Q-CROSS-INDEP; do not extrapolate a total count from e=0 slices. Structurally treat the two residual-grid cover regimes separately: row-saturated (s_D>=g) and column-saturated (s_C>=y). Search for genuinely new interaction between distinct fixed-head witnesses; merely applying criticality to a witness--head edge recycles the original source and yields no new obligation. Keep y=1 separate and inspect the fixed special matched foot across X'. Once this local arm reaches a natural closure, return to the audit's other high-risk interface: zero positive actual-D2C rigid complete Hall cuts with x>=3. Exact pair-local Ccap_P, ONE-P and CROWD stay local; no threshold may be inferred from bounded scans; m>=2 / loaded-buffer / z=2 / four-exception work remains subordinate.`
<!-- CURRENT-STATUS:END -->

---

## Binding daily audit

The latest adversarial audit is `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`. It independently reproduced the repaired source-premise semantics, `X_3`, the exact-core diagnostic, and the audited 124,528-row all-R d-based diagnostic; it also retained the zero-positive-fixture rigid-cut gap as the dominant graph-to-hand interface risk. Superseded alpha/beta evidence, the invalid matched-only common-buffer theorem, and the 188,912 / 179,735 / 178,572 historical diagnostic counts must not be revived.

The mandatory same-code raw-criticality re-proof requested by that audit is preserved at `project/research/post_ms/2026-09-20-same-code-raw-criticality-audit-v1/SAME_CODE_RAW_CRITICALITY_AUDIT.md` and passed.

## Current live geometry

Inside the still-conditional literal all-R equality pinch:

- `A=X dotcup Y`, `X--Y` complete, `|X|=x>=3`, `|Y|=y>0`;
- all X code C, all Y code d, `d_H(C,d)=1`;
- `a_0` is isolated in `G[X]`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`, core heads inject into `X\{a_0}`;
- `g=x-k>=1`;
- z has code `bar C`, `N_A(z)={a_0}`, and misses all core vertices;
- d counts z-nonneighbours in `U_o\{z}`; the J z-neighbours are `bar C`, A-anticomplete, and independent.

For internal-X witness population m and edge mass e:

`m<=d`, `m<=e<=m(x-2)` for `m>0`,

`P_int(e,m)=[e-m(x-p-2)]_+`,

`epsilon_{a_0}>=p+u-y-d+m-1`,

`Z_X>=Z_X^0+NJ+e+m`,

`Z>=Z_0+NJ+e+m(y+1)`,

`e>=B_d+m+P_int(e,m)`.

For `y>=2`, after maximal free credit to the k core-head rows, the residual `g x y` cross-certificate grid is covered by outside C-column witnesses and D-row witnesses. If `s_C,s_D` and `R_C,R_D` are populations and loads:

`R_C+R_D=gy`,

`s_C<=R_C<=s_C g`,

`s_D<=R_D<=s_D y`,

`s_D>=g OR s_C>=y`,

`m+s_C+s_D<=d`.

The type-aware bills are

`P_cross >= [R_C-s_C[x-p+1]_+]_+ + R_D+s_D(p-y-1)`,

`epsilon_{a_0}>=p+u-y-d+m+s_C+s_D-1`,

`Z_X>=Z_X^0+NJ+e+m+R_C+s_D(x-1)`,

`Z>=Z_0+NJ+e+m(y+1)+gy+s_C(y-1)+s_D(x-1)`,

and

`q<=binom(u,2)-binom(k+1,2)-k-d-binom(J,2)-binom(s_C,2)-binom(s_D,2)`.

The witness--head edge itself gives no new criticality obligation: the original source recycles as a valid certificate. Any next structural gain must come from multi-source or multi-witness interaction.

## Diagnostic evidence labels

Independently audited predecessor figures: `173,347` equality-pinch rows and `124,528` after the d-based local-feedback package.

Same-hour provisional diagnostics:

- exact `(d,m,e)` plus crude cross capacity: `78,582` total abstract rows;
- type-relaxed cross-witness population/score system: `71,996` total abstract rows;
- typed `e(X)=0` slice after physical `Z_X/Z` ledger: `62,800` rows;
- typed `e(X)=0` slice after grid cover: `60,552` rows;
- typed `e(X)=0` slice after same-type independence: `58,999` rows (`54,392` with `y>=2`, `4,607` with `y=1`);
- applying the y=1 mandatory outside witness reduces that disjoint slice from `4,607` to `4,523`, so the combined focused `e=0` slice under the current hand lemmas is `58,915` rows.

These are necessary-condition parameter diagnostics, not graphs. No total typed count is promoted beyond `71,996` until a total typed checker is independently replayed.

## Session ledger

**Invocation start:** approximately 01:29 BST.  
**Preservation cutoff:** approximately 01:55 BST, before the next research invocation.

Substantive units completed:

1. reconciled the raw same-code re-proof with the binding daily audit;
2. proved `g>=1` from core-head injection;
3. derived m-sensitive z/a0 conservation;
4. derived internal-witness physical `Z_X/Z` ledgers;
5. derived exact fixed-m load price and Hall gate;
6. classified `y>=2` X--Y raw certificates into fixed-head C/D witness stars;
7. proved internal and cross witness populations are disjoint and derived cross slack / a0 / Z bills;
8. refined to typed `R_C,R_D,s_C,s_D` physical hole ledgers;
9. proved the residual grid-cover dichotomy `s_D>=g OR s_C>=y`;
10. proved C-type and D-type cross witness families are each independent, giving quadratic q loss;
11. synthesized parameter-only `d`, q, and z/a0 conservation bills;
12. isolated the `y=1` special-foot obstruction at `a_0y`;
13. tested the natural witness--head criticality follow-on, found the certificate-recycling obstruction, preserved it, and redirected the next attack.

**Live unfinished line:** total typed checker and structural interaction of multiple fixed-head witnesses in the row-saturated / column-saturated regimes.

**Why stopping:** preservation phase before the next invocation; no mathematical blocker.
