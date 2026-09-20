# Daily adversarial audit — 21 September 2026

## Scope and verdict

This audit reviewed the preceding 24-hour eventual-D2C work at pre-audit head `4a7cf5ab4b94451a9e502cd901c906ab9890b048`, including the 20 September audit handoff, the raw same-code criticality package, the corrected H–U B-layer package, capacity-deficit/residual-slot arguments, the latest corrected global superconstant-deficit candidate, repository state, CI and every session telemetry record present under `project/research/session_logs/` for the audited period.

**Verdict:** no fatal contradiction was found in the final corrected local one-code/H–U/superconstant chain under its stated upstream hypotheses. That is not a graph-level eventual theorem. The live result remains a conditional necessary-condition programme, because the bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`, and this audit did not independently reconstruct every `Delta=h` equality-face exclusion from raw graph criticality.

The audit found a material **process** problem: session telemetry is largely absent, one record is incomplete, and two records point at the same scheduled 23:00:38 trigger. The pre-audit head also had a failing Status synchronization action. These are preserved as audit findings rather than rationalized away.

## Mathematical audit

### 1. Raw same-code theorem — VERIFIED AT STATED SCOPE

`project/research/post_ms/2026-09-20-same-code-raw-criticality-audit-v1/SAME_CODE_RAW_CRITICALITY_AUDIT.md` independently rederived from D2C edge-criticality that a same-code edge in the coded layer has the required triangle-criticality orientation, complementary-code witness location and fixed ordered `(source,witness)` injectivity. In particular, a fixed ordered physical source/witness pair cannot certify two distinct selected same-code edges. The audit found no use of a forbidden B-source/B-witness non-root singleton-head configuration in the corrected package.

### 2. H–U B-layer correction — VERIFIED AS A REAL REPAIR

The old `HU-PRIVATE/HU-QI/HU-IHOLE` route is invalid: a U source and a matched witness both lie in `B=N(v)`, so the root is already a common neighbour and the claimed non-root singleton-private-foot equation cannot hold. The corrected theorem in `ONE_CODE_R1_K2_HALF_RAY_HU_B_LAYER_CORRECTION_AND_SLACK_THEOREM.md` replaces that route with layer-correct witness placement and physical-source capacity. The invalid chain remains superseded and must not be reused.

### 3. Capacity-deficit decomposition / residual-slot collapse — TARGETED REPLAY PASSED

The exact decomposition `e(H,U)=R_q+R_j+S`, its deficits, endpoint-indexed H-anticompleteness and residual-column carrier/independence arguments are internally consistent under the same conditional one-code/rigid setup. The resulting predecessor lower bound `Delta>=h` survives targeted replay. This is still a conditional branch theorem, not a statement that a corresponding graph exists.

### 4. Corrected global superconstant-deficit theorem — PROVISIONALLY SUPPORTED

The current file is:

`project/research/post_ms/2026-09-20-rigid-interface-direct-audit-v1/ONE_CODE_R1_K2_HALF_RAY_GLOBAL_SUPERCONSTANT_DEFICIT.md`.

The same session first overcharged reverse-private/self-head capacity and then repaired it. The corrected local bills are consistent in targeted replay:

- B1 touched-row accounting allows one self-head recovery and uses `a_i >= m_i-1`;
- exceptional residual-bar H-neighbourhoods use `d(d-2)<=a`;
- outside-P H-positive vertices use `(d_H-1)(d_H-3)<=a` after at most one d-bit H-neighbour and one self-head recovery are charged correctly;
- shared U-resource use remains physically injected in the corrected H–U package.

Writing `s=Delta-h`, `R(s)=(3+sqrt(9+8s))/2`, `D=s+R(s)`, `tau(D)=1+sqrt(1+D)`, and `kappa(D)=2+sqrt(1+D)`, the corrected global inequality

`t <= 1 + 2D + 3 tau(D) + D kappa(D)`

has leading order `t <= (1+o(1)) s^(3/2)`, hence `s >= (1-o(1)) t^(2/3)`. The asymptotic conversion is arithmetically sound.

**Audit boundary:** this audit did not reconstruct every small equality-face exclusion (`N=0,1,2,3`) from first principles. The theorem is therefore labeled **provisionally supported**, not independently verified. Commit `945dc220...` remains superseded by the self-head correction beginning at `99cd7367...`.

### 5. Dominant graph-level risk — UNRESOLVED

The actual-D2C regression remains valuable as a negative control, but has still produced **zero positive rigid complete Hall-cut fixtures with `x>=3`** in the bounded corpus. This can mean the configuration is rare, outside the search range, or impossible. It does not justify choosing among those alternatives. The next graph-level step should therefore attack realizability/non-realizability directly rather than stacking another conditional scalar inequality.

## Repository / CI audit

Pre-audit head: `4a7cf5ab4b94451a9e502cd901c906ab9890b048`.

The interval from the previous daily checkpoint `c8d98aa4ba061f66e1bb94e3f5cdb58651261c93` to the pre-audit head contains **271 commits**. Several late commits are direct corrections of the same-session global theorem and its handoff. That density is not itself mathematical evidence, but it increases the chance of stale status, unreviewed dependency drift and accidental promotion.

The pre-audit Status synchronization action failed:

- workflow run: `35543011012`;
- job: `106163951722`;
- failed step: `Check every new commit`.

The repository policy in `scripts/check_status_sync.py` requires the live status block to contain the exact handoff fields `CHECKPOINT CLASS`, `WORK MODE`, `INSPECTED PREDECESSOR`, `LAST VERIFIED RESULT`, `UNPRESERVED WORK`, `DEFERRED ADMIN`, and `NEXT ACTION`. The pre-audit `CURRENT_STATE.md` had drifted to an older field vocabulary. This audit restores the required schema and updates README/public handoff without rewriting history.

## Mandatory session-utilisation audit

Hourly forward research is scheduled at `HH:00:38` for 01 through 23, with the midnight hour reserved for red-team audit. The repository contains only two telemetry records in the audited period, both under `project/research/session_logs/2026-09-20/` and both naming the same scheduled 23:00:38 trigger.

| Scheduled trigger | Actual start | Forward stop | Preservation complete | Wall span | Forward span | Units | Early-stop result | Stop reason | >=50m target | Status |
|---|---|---|---|---:|---:|---:|---|---|---|---|
| 01:00:38–22:00:38 (22 windows) | missing | missing | missing | — | — | — | missing | missing | unverified | **UNVERIFIED/NONCOMPLIANT** |
| 23:00:38, `230244_BST.md` | 23:02:44 (+2:06) | PENDING | PENDING | unverified | unverified | 19 | PENDING | PENDING | unverified | **UNVERIFIED/NONCOMPLIANT** |
| 23:00:38, `2026-09-20T23-30-28+01-00.md` | 23:30:28 (+29:50) | 23:51:58 | 23:52:21 | 21m53s to preservation | **21m30s** | 14 | 23:47:43 check recorded; preservation-stage audit resumed a material repair | late start left 25m10s to cutoff; preservation priority | **N/A** (<55m available) | **VERIFIED telemetry** |

### Verified aggregate only

- scheduled forward windows: **23**;
- missing-telemetry scheduled windows: **22**;
- incomplete additional telemetry record: **1**;
- fully verified run records: **1**;
- verified available window: **25m10s = 25.1667 min**;
- verified forward-research span: **21m30s = 21.5 min**;
- verified-only utilisation: **85.4%**;
- fully verified timing-compliant records: **1**;
- verified short runs under an applicable >=50-minute target: **0**;
- unverified/noncompliant windows/records: **23**;
- observed late starts in logged records: **2** (+2m06s, +29m50s);
- unexplained idle gaps: **none asserted from the available evidence**.

**Interpretation:** the 85.4% figure is not a day-wide utilisation estimate. It is the fraction for the one run with verified available-time and forward-span fields. The other scheduled windows remain unknown. Commit count, theorem count, prose volume and unit count were not used to infer durations.

### Telemetry repair

A durable schema is added at `project/research/session_logs/SESSION_LOG_SCHEMA.md`. Future runs must emit one finalized record per scheduled trigger, with unique run-instance identity for retries/re-entry, exact required timestamps, substantive-unit count, early-stop result, stop reason and >=50-minute applicability/compliance. Incomplete or missing fields remain explicitly unverified/noncompliant; historical timestamps are never reconstructed from commits.

## Confidence change

- **Up:** raw same-code criticality / ordered witness injection; corrected H–U layer logic; targeted capacity-deficit/residual-slot mechanics.
- **Flat / conditional:** corrected global superconstant-deficit theorem.
- **Down:** process confidence in day-wide utilisation evidence and repository synchronization, because most telemetry is absent and the pre-audit head failed Status synchronization.
- **Unchanged:** confidence in a complete eventual theorem. There is still no justified `n_0`, and the rigid-cut realizability gap remains open.

## Prioritized next-hours programme

1. **Equality-face hostile reconstruction.** Re-prove the `N=0,1,2,3` exclusions feeding `Delta>=h+1` directly from the corrected physical variables. **Stop/pivot:** any face that needs an unproved reuse/injectivity assumption blocks the global superconstant theorem.
2. **Rigid-cut realizability/non-realizability.** Search for an actual D2C positive fixture while simultaneously deriving raw-criticality obstructions. **Stop/pivot:** a positive fixture triggers direct downstream replay; an unbounded abstract family without graph realizability sends the programme back to structural criticality rather than looser inequalities.
3. **Rooted-ledger feedback only after 1–2.** Feed verified superconstant H-slack into `Q,E_U,r,f,delta` and seek a graph-level threshold/contradiction. **Stop/pivot:** if the rooted ledger absorbs the slack without superlinear cost, characterize the absorbing family rather than claiming closure.
4. Keep larger-reservoir, `z=2` and four-exception gates subordinate until one becomes genuinely load-bearing.

## Bottom line

The preceding 24 hours produced a meaningful conditional strengthening and repaired a real H–U layer error. The local mathematics is stronger than it was at the previous audit, but the project is still separated from an eventual theorem by a graph-interface realizability gap and by incomplete independent replay of the latest equality-face chain. The process audit is less favorable: the session-utilisation record is not sufficient to substantiate day-wide full-hour use, and that deficiency is now made explicit and mechanically guarded for future runs.
