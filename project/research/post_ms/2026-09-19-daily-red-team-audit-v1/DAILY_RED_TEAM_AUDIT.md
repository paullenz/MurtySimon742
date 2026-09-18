# Daily red-team audit - 19 September 2026

## Scope and audit window

This audit reviews the dense diameter-2-critical (D2C) work added to `paullenz/MurtySimon742` during the preceding 24 hours, using the last pre-window checkpoint `f2e85599491d9804084e9739e1cfcdc6cc088a29` and the pre-audit head `0060acd80a376074486563bc537386fe130459d2` as the principal comparison points. GitHub reports 216 commits between those endpoints. Because that volume is too large for independent line-by-line recertification in one audit session, this report audits the current load-bearing theorem spine, the mandatory hostile control, the finite/checker trust boundaries, and repository/status consistency. Superseded side branches are preserved but are not individually re-certified here.

This is an adversarial audit, not a forward-research session. The question is not whether a line is promising, but whether the claims currently relied upon survive attempts to break their assumptions, quantifiers, algebra, certificate semantics, and negative controls.

## Executive finding

No fatal mathematical contradiction was found in the load-bearing current spine. The strongest new advance is therefore retained, but with a narrower and more explicit trust boundary: the recent Hall-density, rigid-cut, U-witness-deficit and one-code capacity inequalities are internally hand-derived and arithmetically checked, while their graph-theoretic premises have not yet been independently re-derived end-to-end on an independent implementation of realizable D2C graphs.

The audit did find a genuine repository/process defect. The current `CURRENT_STATE.md` used `WORK MODE: EVENTUAL_D2C_MATH`, whereas `scripts/check_status_sync.py` accepts only `MATH`, `ADMIN`, `AUDIT`, `STATUS`, or `RECOVERY`; the file also omitted required synchronization fields. The latest status-synchronization workflow therefore failed. This is a deterministic policy mismatch, not a transient infrastructure event. The live status and README are corrected by the audit checkpoint, and future mathematical commits should be atomic with their status update (or otherwise update `CURRENT_STATE.md` in every commit checked by the policy).

No global eventual second-extremal theorem is claimed.

## Material claims audited

### 1. Published 12-vertex hostile control - VERIFIED as a D2C graph; publication isomorphism remains internally certified

The repository's `X_3` construction has 12 vertices and 32 edges, exceeding `M(12)=31`. An independent reconstruction during this audit confirms diameter 2; deletion of each of the 32 edges raises the diameter to 3; the degree multiset is `[4,4,4,4,5,5,5,6,6,6,7,8]`; and the root-cube vertex edge is the unique dominating edge. This validates the graph itself as the required hostile control.

The repository also contains a direct figure-based identification with Figure 1 of Radosavljevic-Stanic-Zivkovic (2024). That identification is retained as an internal certification, but this audit did not obtain a machine-readable author adjacency list and did not independently reproduce the visual figure comparison from the publisher PDF. Consequently the publication-isomorphism statement remains internally rather than externally certified.

Reference: `project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

### 2. Rooted witness-slot residual and local Hamming defect - VERIFIED at hand-derivation level, conditional on the rooted setup

The package `project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/` was re-read adversarially. The following steps survived review:

- each rooted B-edge receives a criticality witness slot in `Omega={(x,z) in B x A : xz notin E(G)}`;
- the certificate map is injective;
- `|Omega|=L_A+2f=Q+r`, so the unused-slot set has size `r` and `delta=|Upsilon|-f`;
- when `r=0`, A is independent and every slot is used;
- B-edges then have A-code Hamming distance exactly one, giving the Boolean-coordinate structure;
- the collision identities and `r K_A >= H_A >= 2J_A` are consistent with the exact code semantics.

No hidden duplicate-counting or endpoint-witness collision was found in these steps. The theorem remains conditional on the rooted identities and the criticality-certificate lemma rather than being a separately formalized end-to-end D2C proof.

### 3. Hall-density exact cut decomposition - ALGEBRA VERIFIED; structural premises remain conditional

The package `project/research/post_ms/2026-09-18-hall-density-cut-stability-v1/` was checked for sign errors, missing non-negativity hypotheses, and invalid integer/equality transitions. The identities

`2e(A_X)=x(x-T0)-L_X+Z_X+M_X`,

`w_X-x(x-T0)=2E_X+M_X+J_X`,

and the capacity-slack extension with `kappa_X` are algebraically consistent. The low-density implication `x<T0+tau`, the `<1` integer rigidity step, and reserve polarization also survive the audit.

The preserved checker reports 50,000 random graph/partition trials, 156,014 pair-class checks and 834,948 family/subset checks with zero failures. An independent replay of the checker logic reproduced those aggregate counts. This is useful arithmetic/regression evidence, but it does not independently establish that every abstract generated datum comes from a realizable D2C graph. The audit therefore classifies the algebra as verified and the D2C structural interface as conditional.

References: `HALL_DENSITY_STABILITY.md`, `HALL_BETA_LOCALIZATION.md`, `check_hall_cut_stability.py`, and `AUDIT_SUMMARY.md` in that package.

### 4. Rigid Hall witness geometry - VERIFIED conditionally

For a rigid Hall cut (`E_X=M_X=0`) the complete A-cut conclusion and outside-source localization were checked. The singleton-head U-witness argument giving

`h_Y (x-p)_+ <= u`

survives review. In particular, a large rigid family necessarily collapses the number of outside tight codes. No missing case was found in the use of `mu_X<=p` or in the distinct-code accounting.

Reference: `project/research/post_ms/2026-09-18-hall-density-cut-stability-v1/RIGID_HALL_WITNESS_GEOMETRY.md`.

### 5. Rigid U-witness deficit/slack and residual bridge - VERIFIED conditionally; checker is not a realizability proof

The latest package `project/research/post_ms/2026-09-18-rigid-hall-witness-deficit-v1/` was the principal audit target. The following deductions were re-derived and no sign or multiplicity error was found:

- each outside code needs at least `k=(x-mu_X)_+` singleton-head U-witnesses;
- a reused witness with multiplicity `t` satisfies `epsilon_w >= [g+t-1]_+`;
- `Z_X>=hk(x-1)`, `Z_Y>=yk`, hence `Z>=k[y+h(x-1)]`;
- for `g>=1`, `E_U>=k[y+h(g-1)]`;
- for `g<=1`, `E_U>=[yk-(1-g)u]_+`;
- the exact integer minimization bridge `q+E_U>=E_rig+ceil((D-E_rig)_+/2)` follows from `Z=u(p-lambda)+2q+E_U`;
- the resulting A-edge lower bound and cutoff conditions have the stated direction;
- in the one-code case, direct edges inside Y are impossible and the pair-capacity bill `Ccap_P+L_Y >= y(p+x+k)` follows from the complete cut and non-direct traffic count;
- the aligned same-code crowding inequality is consistent with the preserved crowding package.

The checker reports 12,841 witness systems, 100,000 exact integer minimization tests and 1,910,960 abstract rigid parameter/code-count instances, with zero invariant failures; 39,902 abstract instances are rejected by the new U-slack/beta-deficit filters. Independent arithmetic replay reproduced these counts. The checker constructs abstract incidence/parameter systems and therefore does not by itself certify that the premises hold for every actual D2C graph. The theorem is retained as a strong internal structural advance, not promoted to an external theorem.

### 6. Same-code crowding and source-tuple support - PROVISIONALLY SUPPORTED, with targeted re-audit still required

The same-code crowding/complementary-pair localization proof was inspected at the points used by the one-code trap: witness localization, injection into U capacity, and the aligned-code self-pricing lower bound. No local contradiction was found.

The finite source-tuple theorem and beta-support inverse were checked at the algebraic substitution level and remain coherent with the Hall-beta localization argument. However the continuum/asymptotic refinements of the source-tuple package were not re-audited line-by-line tonight. Because the latest rigid-box argument invokes the finite source-tuple theorem for arbitrary subsets, an independent re-proof of that exact finite statement is a high-priority audit dependency before it is treated as stable external-review material.

### 7. Direct-fan bounded-surplus four-exception gate - STRONGLY SUPPORTED, not fully re-certified tonight

The theorem that, for `n>=23`, direct fan order `d>=2`, `eta<=d-2` and at most four external exceptions, a triangle-containing above-`M(n)` survivor is impossible was reviewed at its main load-bearing steps. Independent finite checks confirmed the safe-coordinate lower bound for the relevant four-vertex kernels and the final quadratic inequality. The audit did not re-derive every kernel-specific criticality subcase (notably the complete treatment of all four-vertex exception graphs). This package remains strongly supported rather than fully independently re-certified.

Reference: `project/research/post_ms/2026-09-18-combined-channel-four-exception-v1/DIRECT_FAN_BOUNDED_SURPLUS_FOUR_EXCEPTION_GATE.md`.

## What the previous 24 hours actually achieved

The main mathematical progress is a transition from a broad rooted residual/Boolean-flow picture to a considerably sharper local rigidity mechanism. The chain now connects an exact rooted witness-slot residual to Hamming-coordinate control, Hall-cut exactness, low-density rigidity, code collapse on the opposite side of a rigid cut, a multiplicity-sensitive unmatched-slack bill, and finally an explicit one-code pair-capacity/crowding obstruction.

This is significant because it moves a difficult branch from a qualitative statement ('a rigid Hall cut has few outside codes') to quantified resource inequalities that charge the collapse itself. In particular, code collapse is no longer an apparent equality escape: a one-code outside layer must pay both certificate capacity and same-code crowding. This is a meaningful narrowing of the prospective eventual proof architecture.

What has *not* been achieved is equally important: there is still no theorem excluding every triangle-containing above-`M(n)` graph for all sufficiently large n, no proved global threshold n0, and no independent formalization or second implementation of the entire graph-to-Hall-to-rigid-witness chain. The latest finite parameter rejections are diagnostic counts of abstract systems, not counts of D2C graphs.

## Repository and CI audit

The repository is logically organized and preserves failed approaches, negative controls and audit history. The current-status surfaces were not synchronized with the newest mathematics: README still presented the `n<=294` zero-residual result as the current post-pivot frontier and still described the autonomous programme as a three-day window ending 20 September. `CURRENT_STATE.md` was mathematically newer but violated the repository's status-synchronization schema.

The pre-audit head `0060acd80a376074486563bc537386fe130459d2` triggered Status synchronization run `35402717100`; job `105785888407` failed at 'Check every new commit'. Inspection of `.github/workflows/status-synchronization.yml` and `scripts/check_status_sync.py` shows why: the parser accepts work modes `MATH`, `ADMIN`, `AUDIT`, `STATUS`, `RECOVERY`, while the file used `EVENTUAL_D2C_MATH`, and the required fields `INSPECTED PREDECESSOR`, `LAST VERIFIED RESULT`, `UNPRESERVED WORK`, `DEFERRED ADMIN`, and `NEXT ACTION` were absent.

This audit checkpoint repairs those status fields, updates the README live overview/current chain, records this red-team report, and explicitly marks the audit trust boundaries. The failure is preserved as historical evidence rather than repainted as a transient CI issue.

## Confidence change

The audit does not justify a numerical probability revision. Qualitatively, confidence in the *local algebraic and combinatorial deductions* is slightly higher because their key steps survived hostile re-derivation and independent arithmetic replay. Confidence in the *overall eventual theorem* should not rise by the same amount: the main residual risk has shifted toward shared graph-theoretic premises and end-to-end completeness rather than arithmetic mistakes inside the newest inequalities.

The correct interpretation is therefore: stronger local structure, narrower live frontier, but still a substantial integration/completeness gap.

## Recommended next 24-hour programme

1. **Independent finite source-tuple re-proof.** Re-derive the finite source-tuple theorem and beta-support inverse from definitions without importing the current proof text. Stop and repair immediately if any subset quantifier, source distinctness condition or capacity term differs. If it survives, freeze a compact lemma with an independent checker.
2. **One-code rigid branch as the primary forward target.** Combine `(ONE)` with the exact `Ccap_P` formula and `(CROWD)` before introducing any new global scalar relaxation. The objective is either a clean contradiction for a broad asymptotic range or a sharply parameterized equality family. Stop/pivot if two consecutive relaxations erase pair-local information without reducing the feasible asymptotic family.
3. **End-to-end premise audit on small realizable D2C graphs.** Build an independent graph-level regression that computes the rooted partition, slots, codes, pair families, Hall quantities and rigid-witness quantities directly from actual small D2C graphs, including `X_3`. This should verify that every implemented quantity satisfies the claimed structural identities. Pivot to proof repair on the first mismatch; do not 'tune' the checker around a discrepancy.
4. **Finish independent four-exception kernel audit if that theorem remains load-bearing.** Re-derive the omitted kernel-specific cases rather than relying on the existing narrative. If it is not needed by the emerging one-code route, demote it to supporting rather than load-bearing status.
5. **Repository discipline.** Mathematical file(s), checker evidence and `CURRENT_STATE.md` should be committed atomically where possible; every commit subject to status synchronization must satisfy the required handoff fields. README should be refreshed at reviewer-facing milestones and in each daily red-team checkpoint.

## Stop/pivot criteria

- Any actual D2C counterexample to a claimed structural identity invalidates that identity immediately, regardless of abstract checker success.
- Any checker that only generates algebraically consistent abstract data must not be described as independent graph-level verification.
- If the one-code branch leaves an asymptotic family after the exact pair-capacity and crowding terms are both used, classify that geometry directly and feed its forced `q,E_U,f` back through the rooted residual identities; do not keep adding scalar inequalities indefinitely.
- If a proposed simplification removes the 12-vertex `X_3` hostile control for a reason that would also apply at `n=12`, treat that as a red flag unless the theorem's size hypothesis is explicitly used.
- No global eventual theorem should be promoted until the triangle-containing live branch is closed with an explicit quantified range and the graph-to-constraint chain has received independent end-to-end review.

## Traceability

- Pre-window comparison base: `f2e85599491d9804084e9739e1cfcdc6cc088a29`.
- Pre-audit head: `0060acd80a376074486563bc537386fe130459d2`.
- Pre-audit tree: `f0fd7bf2a46c03400668d915bca97408b1c45484`.
- Latest status-sync failure: workflow run `35402717100`, job `105785888407`.
- Latest load-bearing packages:
  - `project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/`
  - `project/research/post_ms/2026-09-18-hall-density-cut-stability-v1/`
  - `project/research/post_ms/2026-09-18-large-code-pair-v1/`
  - `project/research/post_ms/2026-09-18-rigid-hall-witness-deficit-v1/`
  - `project/research/post_ms/2026-09-18-combined-channel-four-exception-v1/`
- Latest rigid package commits: theorem `fd34b21...`, checker `82e979b...`, audit summary `da99891...`, live-state handoff `0060acd...`.

This report is an internal red-team checkpoint. It is evidence of attempted falsification and repository reconciliation, not external peer review.
