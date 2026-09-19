# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-20  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C hostile control `X_3` has 12 vertices and 32 edges while `M(12)=31`; it remains mandatory. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `DAILY_RED_TEAM_ALL_R_PINCH_AUDIT_2026_09_20`

WORK MODE: `AUDIT`

INSPECTED PREDECESSOR: `1b31449427c81b76b3da9140e61dd55b18a739f0`

LAST VERIFIED RESULT: `The 20 September daily adversarial audit found no fatal contradiction in the final repaired one-code / first-strict / one-witness / all-R equality-pinch chain, but it keeps the entire chain conditional on the rigid complete-cut hypotheses. Independent replays reproduced the source-premise atlas counts (21 D2C classes, 126 roots, 2 beta and 1 alpha raw certificates, zero P1/raw-P2 collisions), X_3 as a 12-vertex 32-edge D2C hostile control, the exact-core diagnostic (248,798 coarse; 208,684 pair; 174,769 final), and the latest all-R diagnostic (173,347 predecessor final; 124,528 new final; 48,819 rejected). The latest hand package survives spot-checking of z-neighbour purification, e(X)<=Nd, witness self-pricing, the piecewise e_req formula, and z/a0 score conservation. A major coverage gap remains: the actual-graph regression has zero positive rigid complete Hall cuts with x>=3. The audit also confirms that the earlier alpha/beta checker evidence, matched-only common-buffer orientation theorem, 188,912 first-strict count, 179,735 intermediate count, and 178,572 weak-core one-witness count are superseded and must not be revived.`

UNPRESERVED WORK: `None known. The daily audit is preserved at project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md. The audited head was 1b31449427c81b76b3da9140e61dd55b18a739f0. Invalidated and superseded results remain preserved in their native packages and git history.`

DEFERRED ADMIN: `The root README is refreshed at this audit checkpoint and the pre-audit README is preserved under archive/status-snapshots/2026-09-20/. One minor checker-hygiene item remains: the t loop / t-choice distribution in check_all_r_pinch_local_feedback.py is dead after the purified d-based rewrite and should be cleaned before reviewer-facing release; it does not affect the 124,528 final count.`

NEXT ACTION: `First independently re-derive the full coded-layer same-code criticality theorem and ordered (source,witness) injectivity used by all-R Units VI/XII/XIII directly from raw D2C edge criticality. Any missing witness location or reuse pattern blocks X-d-CAP and X-WIT-PAY. Only after that audit passes, solve the literal all-R local optimization with d, per-witness loads, z/a0 conservation, exact pair-local Ccap_P, ONE-P and CROWD retained simultaneously. In parallel or immediately after, attack the zero-positive-fixture rigid-cut coverage gap: construct an actual D2C rigid-cut fixture or prove the rigid singleton-head implication independently at publication standard; if repeated constructions yield none, test whether nonrealizability itself is the closure. Feed survivors into the exact rooted residual ledger using physical U-holes/slack. Do not infer a threshold from a bounded scan. Keep m>=2, loaded-buffer, z=2 and the four-exception route subordinate until this audited arm closes or proves insufficient.`
<!-- CURRENT-STATUS:END -->

---

## 1. Binding 20 September adversarial-audit gate

The latest daily red-team audit supersedes earlier handoff priorities where they conflict.

### Verified or independently reproduced

- Raw P1 distinct physical beta-source identity is a direct singleton-common-neighbour consequence.
- P2 is selected-representative uniqueness for one physical `(source,coordinate)` obligation, not raw-witness uniqueness.
- The corrected source-premise atlas replay gives 21 D2C classes through order seven, 126 roots, 2 raw beta certificates, 1 raw alpha certificate and zero P1/raw-P2 collisions.
- `X_3` independently replays as D2C with `n=12`, `m=32>M(12)=31`; `X_4` and `X_5` also replay as D2C but lie below their corresponding `M(n)` values.
- The exact-core first-strict diagnostic independently replays as `248,798 / 208,684 / 174,769` for coarse / pair / final rows.
- The all-R diagnostic independently replays as `173,347` predecessor final rows and `124,528` new final rows, rejecting `48,819`.
- The piecewise `e_req(d)` formula was brute-force checked against its defining inequality with zero off-by-one mismatches on a broad integer test range.

### Superseded or invalidated evidence

Do not reuse as current evidence:

- the pre-repair alpha-labelled-as-beta graph checker result;
- the matched-only common-buffer Orientation-A theorem invalidated and replaced at `14af481cf888c6cb3a8c22f5a51a01c75474a281`;
- the first-strict 188,912 count that omitted `m<=|U_o|`;
- the 179,735 intermediate diagnostic once exact common-core pricing is restored;
- the 178,572 one-witness count using the obsolete weak core floor;
- any abstract survivor count as a graph count or realizability statement.

### Unresolved high-risk interfaces

1. No actual D2C fixture in the bounded regression realizes a rigid complete Hall cut with `x>=3`; later rigid one-code mathematics therefore remains a conditional hand implication.
2. The full coded-layer same-code criticality theorem and ordered `(source,witness)` injectivity are now repeatedly load-bearing in the all-R package and should receive a fresh raw-criticality proof audit before more deductions are stacked on them.
3. Exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` must remain local; total-score substitutions are not allowed in the live branch.

Reference: `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

---

## 2. Current live mathematical frontier

The active conditional branch is the literal `m=1` all-R equality pinch produced by the independently repaired first-strict funnel.

Its fixed geometry is:

- `A=X dotcup Y`, `X--Y` complete, `|X|=x>=3`, `|Y|=y>0`;
- all of `X` has one tight code `C`, all of `Y` code `d`, and `d_H(C,d)=1`;
- `a_0` is the unique buffer non-neighbour in `X` and is isolated in `G[X]`;
- the unique selected outside witness `z` satisfies `N_A(z)={a_0}`;
- `W_0` is the common core and both `a_0--W_0` and `z--W_0` are empty.

For `d` equal to the number of `z`-nonneighbours in `U_o\{z}` and `J=u_o-1-d`, the latest local package proves conditionally:

- every `z`-neighbour in `U_o\{z}` has code `bar C`, is A-anticomplete, and the J-set is independent;
- internal X-edge witnesses must come from at most d `z`-nonneighbour complementary vertices, so `e(X)<=N d`, `N=x-1`;
- their selected load gives `E_D >= [e(X)-d(x-p)_+]_+`;
- exact Hall feedback gives `2e(X)>=B_d+[e(X)-d(x-p)_+]_+` and the corresponding piecewise `e_req(d)`;
- `epsilon_z+epsilon_{a_0}>=2p+k+u-y-2` is independent of d.

The current broad-box diagnostic leaves **124,528 abstract rows**. This is a diagnostic of necessary conditions only. There is no eventual theorem, no realizability classification, and no justified threshold `n_0`.

Key package: `project/research/post_ms/2026-09-19-all-r-pinch-local-feedback-v1/ALL_R_PINCH_LOCAL_FEEDBACK.md`.

---

## 3. Important repaired dependency chain

The current branch must be read through the repaired artifacts, not the invalidated intermediate claims:

1. `2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md` — fixes alpha/beta semantics and P1/P2 trust boundary.
2. `2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md` — actual-graph regression through Hall/pair capacity; zero positive rigid cuts is an explicit coverage gap.
3. `2026-09-19-common-buffer-criticality-repair-v1/COMMON_BUFFER_X_EDGE_CRITICALITY_REPAIR.md` — invalidates the matched-only orientation theorem and replaces it with matched-or-outside criticality.
4. `2026-09-19-first-strict-funnel-reservoir-v1/FIRST_STRICT_FUNNEL_REPAIR_AUDIT.md` — reconstructs the interrupted checker, adds physical `m<=|U_o|`, and re-audits support-block lemmas.
5. `2026-09-19-first-strict-funnel-reservoir-v1/ONE_WITNESS_POLARIZATION_PINCH.md` — compresses `m=1` to the unique cheap all-R equality arm.
6. `2026-09-19-all-r-pinch-local-feedback-v1/ALL_R_PINCH_LOCAL_FEEDBACK.md` — current local feedback package.

The 24-hour comparison from `0060acd80a376074486563bc537386fe130459d2` to the audited head contains 114 commits. The high repair density is itself a reason not to promote same-hour closures beyond their stated conditional scope before the next daily audit.

---

## 4. Repository / CI audit

At the audited head `1b31449427c81b76b3da9140e61dd55b18a739f0`, GitHub Actions Status synchronization run `35473850313`, job `105979551184`, failed in `Check every new commit`.

This was not an infrastructure failure. The commit advanced `ALL_R_PINCH_LOCAL_FEEDBACK.md` while `CURRENT_STATE.md` still described the earlier first-strict frontier. The daily checkpoint repairs that handoff gap and refreshes the README.

The status guard remains a process guard, not a proof checker. A passing guard means the handoff changed when the repository changed; it does not validate the mathematics.

---

## 5. Mandatory next-hours programme

1. Re-prove same-code criticality / ordered source-witness injection directly from raw D2C criticality. Stop immediately on any extra witness location or reusable ordered pair.
2. If item 1 survives, perform the exact local all-R optimization retaining `d`, per-witness loads, `ZA0-CONS`, exact `Ccap_P`, `(ONE-P)` and `(CROWD)`. If an unbounded family survives, classify it instead of adding weak scalar cuts.
3. Resolve the rigid-cut coverage gap by finding a positive actual fixture or independently proving the rigid implication at publication standard. If fixtures remain absent, test direct nonrealizability.
4. Feed surviving geometry to `Q=e(G[U])`, `E_U`, `r`, `f` and `delta=r-e(F)` using physical holes/slack. Never promote a bounded scan to an asymptotic threshold.
5. Keep larger reservoirs / loaded buffers / `z=2` / four-exception work subordinate until this arm closes or is shown insufficient.