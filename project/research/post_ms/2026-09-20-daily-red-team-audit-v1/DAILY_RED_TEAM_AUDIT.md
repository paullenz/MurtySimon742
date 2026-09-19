# Daily adversarial audit — 20 September 2026

**Repository:** `paullenz/MurtySimon742`  
**Audited comparison anchor:** `0060acd80a376074486563bc537386fe130459d2`  
**Audited head:** `1b31449427c81b76b3da9140e61dd55b18a739f0`  
**Commits in comparison:** 114  
**Mode:** adversarial audit only; no forward theorem development.

## Executive result

No fatal contradiction was found in the final, repaired one-code / first-strict / one-witness / all-R equality-pinch chain that existed at the audited head. The strongest defensible conclusion is narrower: the latest local package is a coherent **conditional necessary-condition package** whose arithmetic replay and several load-bearing hand steps survive independent reconstruction, but it is not an eventual second-extremal theorem, does not produce a threshold `n_0`, and still has no positive actual-D2C fixture realizing the rigid complete-cut hypotheses.

The audit did find two material process/handoff defects at the audited head and one minor diagnostic-hygiene issue:

1. `CURRENT_STATE.md` was stale: it stopped at the first-strict exact-core pinch while the repository had advanced through the all-R local-feedback package.
2. `README.md` still described graph-level regression / premise verification as the next priority even though that work had been completed and the active frontier had moved to the literal all-R equality pinch.
3. In `check_all_r_pinch_local_feedback.py`, the loop variable `t` is no longer used in any feasibility inequality after the purified `d`-based rewrite. The final count is unaffected, but the emitted `minimizing_t_distribution` is mechanically non-informative and must not be treated as evidence.

The audited head's Status synchronization run `35473850313` failed at job `105979551184`. This is deterministic, not transient infrastructure: the head commit changed the theorem note while leaving the `CURRENT_STATE.md` status block unchanged, exactly what `scripts/check_status_sync.py` is designed to reject.

## What materially changed in the preceding 24 hours

### 1. Source-tuple interface: repaired and materially strengthened

The first graph-level source-premise checker had tested the matched-source/alpha orientation while labelling it beta. That evidence was explicitly withdrawn and corrected. The repaired package proves the distinct physical beta-source premise directly: one fixed pair `(x,y)` cannot have `N(x)∩N(y)` equal to two different tight-fibre singletons. It also correctly narrows P2 to **selected-representative uniqueness** for one physical `(source,coordinate)` obligation rather than claiming raw witness uniqueness.

The repaired checker permanently installs `X_3` and reconstructs the selected P--U ledger and selected/residual Hall ledger. The key repair commits include:

- `86e4b8ffec96d79272dcbd9b17e31f8e20e3cdd0` — repair source-tuple premises and beta counting semantics;
- `6822988686fb6ea9b62ce8e312ebcbdea43f33a4` — correct beta regression and install `X_3`.

**Audit status:** verified at the stated selected-system semantics. The broader graph-to-constraint bridge remains the relevant trust boundary, not P1/P2 themselves.

### 2. Actual-graph Hall/pair-capacity regression: useful, but with a decisive coverage gap

The independent rigid graph-level regression reports 21 atlas D2C classes, 700 generated D2C graphs, 3 certificate policies, 3,540 root-policy instances, 114 qualified roots, 147 pair-capacity checks, 36 exact Hall-cut checks, and zero graph/formula mismatches. The mandatory `X_3` control remains non-excluded for the correct reason.

However, the regression found **zero actual rigid complete Hall cuts with `x>=3`** despite the bounded corpus and targeted searches. Consequently every later rigid one-code theorem is still conditional hand mathematics rather than an empirically exercised graph configuration. This is the largest remaining interface risk.

**Audit status:** regression evidence verified as correctly scoped; the zero-positive-fixture gap remains unresolved and must not be softened in future summaries.

### 3. Common-buffer criticality: one real theorem error was found and repaired

`COMMON_BUFFER_X_EDGE_CRITICALITY_REPAIR.md` explicitly invalidates Sections 4, 6 and 7 of the preceding anticomplete-buffer trichotomy in their matched-only form. The bad orientation required `bz` to be a nonedge while simultaneously putting `b` in `N(x)∩N(z)`, which is impossible. The repaired theorem replaces matched-only localization by a matched-or-outside dichotomy and reverses the zero-buffer conclusion: in that subbranch the forced certificates are outside unmatched witnesses, not gamma-aligned matched feet.

Repair commit:

- `14af481cf888c6cb3a8c22f5a51a01c75474a281` — repair common-buffer X-edge criticality orientation.

**Audit status:** the invalid matched-only claim remains withdrawn. The later first-strict / one-witness chain is built on the repaired route rather than the invalidated sections.

### 4. First-strict funnel: interrupted arithmetic was reconstructed, then physically corrected

The first-strict funnel theorem prose was committed without its claimed checker. The reconstruction reproduced the legacy arithmetic but exposed a genuine omitted physical condition:

`1 <= m <= |U_o| = u-k-1`.

The legacy 188,912-survivor diagnostic was therefore superseded. Restoring the exact common-core identity and the weakest forced core-hole floor gives the current broad abstract replay:

- coarse rows: 248,798;
- exact-core pair survivors: 208,684;
- exact-core pair rejects: 40,114;
- exact-core final survivors: 174,769;
- residual rejects after the pair gate: 33,915.

This audit independently reimplemented `check_first_strict_exact_core.py` from its formulas and reproduced all five counts exactly.

**Audit status:** arithmetic verified; graph-realizability is not implied.

### 5. One-witness polarization: a genuine structural compression

Inside the repaired first-strict branch, `m=1` polarizes to all-F or all-R. Rechecking the Hamming bills confirms that every one-witness geometry except one literal all-R equality arm pays `r>=a+y`. The unique cheap arm has

- `s=1`;
- `I=I_0`;
- all of `X` in one code class `C` with `d_H(C,d)=1`;
- `a_0` isolated in `G[X]`;
- the unique selected outside witness `z` with `N_A(z)={a_0}`;
- full-class capacity `x<=R_A`.

The corrected one-witness abstract diagnostic has 206,935 pair survivors and 173,347 final rows.

**Audit status:** hand compression is internally coherent and remains conditional on the repaired rigid/first-strict hypotheses.

### 6. All-R equality pinch: latest local structural advance survives this audit

At the audited head, `ALL_R_PINCH_LOCAL_FEEDBACK.md` adds a sequence of located-hole and criticality consequences. The most important independently spot-checked steps are:

- `a_0--W_0` and `z--W_0` are empty;
- the `d/J` tradeoff for `z` is exact;
- every `z`-neighbour in `U_o\{z}` has code `bar C`, is A-anticomplete and belongs to an independent set;
- an internal X-edge cannot use those `z`-neighbours as complementary witnesses, giving `e(X)<=Nd`;
- witness load on the at-most-`d` remaining complementary vertices gives
  `E_D >= [e(X)-d(x-p)_+]_+`;
- the exact Hall lower bound therefore becomes
  `2e(X)>=B_d+[e(X)-d(x-p)_+]_+`;
- the piecewise `e_req(d)` formula is algebraically exact;
- `epsilon_z+epsilon_{a_0}>=2p+k+u-y-2` is a genuine conservation law.

The audit independently reimplemented the companion diagnostic and exactly reproduced:

- coarse rows: 248,798;
- predecessor equality-pinch final rows: 173,347;
- new final rows: 124,528;
- newly rejected rows: 48,819.

The piecewise `e_req` formula was separately brute-force checked over `-20<=B<=200` and `0<=c<=100`; there were zero off-by-one mismatches with the defining inequality `2e>=B+[e-c]_+`.

**Audit status:** no fatal flaw found in the final purified `d`-based package. The count is an abstract necessary-condition diagnostic, not a graph count or a proof of nonrealizability.

## Independent negative-control replay

The audit independently reconstructed the cube-face family for `k=3,4,5` and checked D2C directly:

- `X_3`: `n=12`, `m=32`, D2C, and `M(12)=31`;
- `X_4`: `n=21`, `m=80`, D2C, below `M(21)=101`;
- `X_5`: `n=38`, `m=192`, D2C, below `M(38)=343`.

The source-premise atlas logic was also independently reimplemented and reproduced the repository's small-corpus counts: 21 unlabeled D2C classes through order seven, 126 rooted instances, 2 raw beta certificates, 1 raw alpha certificate, and zero P1/raw-P2 collisions.

## Superseded or weakened evidence that must stay superseded

The following must not re-enter the live proof narrative as current evidence:

- the first source-premise checker result before the alpha/beta orientation correction;
- the matched-only common-buffer Orientation-A theorem invalidated by `14af481c...`;
- the 188,912 first-strict survivor count, which omitted physical outside-reservoir capacity;
- the 179,735 intermediate count once the stronger exact-core identity is in force;
- the 178,572 one-witness count using the obsolete weak core floor;
- any finite survivor count interpreted as a count of realizable D2C graphs;
- any claim that bounded graph regression has exercised a positive rigid complete-cut fixture.

## Current risk register

### High — conditional rigid-cut interface

No actual D2C fixture in the bounded corpus realizes the full rigid complete-cut hypotheses. A scope error in the hand implication could therefore survive every present graph regression. This is the dominant mathematical audit risk.

### High — same-code criticality / selected witness injection is now load-bearing

The all-R Units VI/XII/XIII repeatedly use the full coded-layer same-code criticality theorem and graph-fixed ordered `(source,witness)` injectivity. The spot checks in this audit found the uses plausible and internally consistent, but the next independent proof audit should re-derive that theorem directly from raw edge criticality and check every location/type case without importing downstream code language.

### Medium — theorem velocity and repair churn

The 24-hour interval contained several real corrections: alpha/beta mislabelling, a wrong common-buffer orientation, a missing physical reservoir condition, and an interrupted checker that had to be reconstructed. This is evidence that same-hour theorem packages should remain provisional until the next adversarial checkpoint even when their arithmetic passes.

### Medium — exact pair-local dependency

`Ccap_P`, `(ONE-P)` and `(CROWD)` remain load-bearing. The graph regression exercises the upstream pair quantities, but later scalar diagnostics must continue to keep pair-local score separate from total score.

### Low — latest checker dead variable

The `t` loop in `check_all_r_pinch_local_feedback.py` no longer changes feasibility after the purified rewrite. The final count is correct, but `t_choice` output is not meaningful. Clean it before any reviewer-facing release of that checker.

## Confidence change from this audit

Confidence increased in the repaired source-premise semantics and in the arithmetic correctness of the exact-core and all-R diagnostics because both were independently reconstructed. Confidence did **not** materially increase in a complete eventual theorem: the main remaining obstacle is structural closure of a conditional branch that still lacks a positive realizable fixture, and the preceding day exposed enough genuine local mistakes to justify keeping all new branch closures below publication-grade confidence until independently re-derived.

## Mandatory next-hours programme

1. **Independent raw-criticality audit of same-code criticality and ordered witness injection.** Re-derive the full theorem used by all-R Units VI/XII/XIII without importing the coded-layer package. Check A-A, U-U and A/U witness locations and both edge orientations. **Stop/pivot:** any missing witness location or reuse pattern is a blocker; repair before using `X-d-CAP` or `X-WIT-PAY` again.
2. **Only after item 1 passes, solve the literal all-R local optimization exactly.** Keep `d`, the per-witness internal-X loads `r_w`, the `z/a_0` conservation law, exact `Ccap_P`, `(ONE-P)` and `(CROWD)` simultaneously. **Stop/pivot:** if exact local optimization leaves an unbounded scaling family, characterize that family rather than adding another weak scalar inequality.
3. **Attack the rigid-cut coverage gap.** Either construct a positive actual D2C rigid-cut fixture for regression or give an independent publication-standard proof of the rigid singleton-head implication. **Stop/pivot:** if systematic constructions continue to produce zero fixtures, investigate whether nonrealizability itself can be proved and used as the structural closure.
4. **Feed any surviving all-R geometry back into the exact rooted residual ledger.** Use physical U-nonedges and U-slack, not abstract survivor counts, to seek an asymptotic contradiction or a finite threshold. **Stop/pivot:** do not promote a threshold from a bounded parameter box.
5. Keep `m>=2`, loaded-buffer, `z=2` and the four-exception gate subordinate unless the audited all-R arm closes or becomes provably insufficient.

## Repository hygiene actions required by this audit

This audit checkpoint must:

- advance `CURRENT_STATE.md` to the all-R local-feedback frontier and embed this audit gate;
- refresh `README.md` so the public status no longer says graph-level premise verification is the next task;
- preserve the pre-audit README as a dated status snapshot;
- retain all invalidated/superseded claims and counts in their native history;
- leave the latest audit note discoverable from both `CURRENT_STATE.md` and `README.md`.

No theorem file is silently rewritten by this audit. Corrections to theorem content should remain explicit follow-up commits with their own audit trail.