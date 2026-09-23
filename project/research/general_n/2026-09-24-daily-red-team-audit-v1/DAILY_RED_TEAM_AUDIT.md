# Daily adversarial audit - 24 September 2026

Status: `AUDIT_COMPLETE_INTERNAL_NOT_EXTERNAL_VERIFICATION`.

Audited predecessor: `083dc162be599fe102274c4ce23f4f99ba5c7476`.
Previous audited baseline: `f2f951e538c297243b4dbb02140fc8f96df97f5b`.
Window: the complete Europe/London research day of 23 September 2026, comprising 23 forward triggers and this separate audit.

## Disposition

The day produced real mathematical progress, but not an independent proof of Erdős #742. The internally checked maximum-degree implication remains

`Delta(G)>=250n/429 => e(G)<floor(n^2/4)` for `n>=6`,

with unresolved strip `n/2<Delta<250n/429`. No lower threshold was claimed or found. The day's attempted promotion from `S<=13` to `S<=14` is **frozen**. The r=12 source count was successfully repaired and replayed, but the load-bearing support-ten helper screen did not reproduce: the same script SHA, with the same 180-second per-row limit, returned 32 solver timeouts and zero proved infeasibilities. The saved earlier run claims 32 infeasibilities; this audit does not declare it false, but it cannot carry promotion until independently reproduced or certificate-backed. Equality remains supported only through `S<=8`.

The most important red-team correction is negative: unrestricted crossed-supplement injectivity is false on actual D2C graphs. `CROSS_SOURCE_COLLISION.md` gives explicit bounded collisions. Later work correctly retreats to demand-restricted Hall eligibility and congestion charging. A separate same-session mistake, `x_i<=n-Delta-1`, swapped the root-neighbour and root-nonneighbour sides. `EXACT_D2C18_AND_SUPPLEMENT_CAP.md` withdraws it; only `x_i<=Delta` follows. Neither invalid claim is used by the final n=18 chain.

## Evidentiary status

### Established background used

- The definition of diameter-two-criticality and elementary degree/deficit identities.
- Exact local characterization of edge criticality in a diameter-two graph. The independent NetworkX replay compared it with literal edge deletion on 457 connected diameter-at-most-two atlas graphs and 5,553 edges, with zero mismatches.

### Internal candidate mathematics retained

- `RAW_PROFILE_BRIDGE.md` and its 757-graph / 2,722-selection regression remain the graph-to-profile interface. This audit found no new counterexample, but did not repeat the full prior regression.
- `HALL_ENVELOPE_EXACTNESS.md`: for the graph-level certificate assignment interface,
  `S*=max_L(2|union C_i|-sum h_i)`. The inclusion-minimal maximizer argument and attainment assignment were checked directly.
- `ASSIGNED_WITNESS_OBSTRUCTION.md` and `STAR_CRITICALITY_SLACK.md`: an exact-H assignment produces a simple assigned-witness graph; D2C criticality forces quadratic star slack. The source-distinctness step is valid because distinct assigned `B`-edges with a fixed supplement endpoint have distinct other endpoints.
- `DEMAND_15_16_NORMAL_FORM.md`: deletion minimality reduces every `H>=15` obstruction to total demand 15 or 16. This is a finite-dimensional obstruction with a credible closure path, not a general theorem.
- `R12_INTERNAL_CLOSURE_REVIEW.md` records a same-day attempted r=12 promotion, but this audit freezes it because the support-ten helper solve did not reproduce. The retained audited bound is through `S<=13`.
- The strengthened n=18, `Delta=10` row is an abstract necessary-condition scan. Exact stable-index closure reaches 39,250, apart from the separately graph-excluded `(5,5,5)` tuple at index 20,851. Full row closure remains open.

### Exact computations replayed in this audit

- `verify_r12_closure_manifest.py`: PASS as a **saved-manifest consistency check**. It trusts `R12_SUPPORT10_HELPER_SCREEN_RESULT.json`; it is not a solver replay and therefore does not cure the nonreproduction.
- `screen_r12_support67_helpers.py`: 5/5 infeasible, zero unknowns.
- `screen_r12_support89_helpers.py`: 44/44 infeasible, zero unknowns.
- `check_support10_case1_aggregate.py`: correctly reproduces the historical discrepancy, 32 distinct saved survivors rather than the old 42. The 42 was a double-count of shard 0, not ten missing kernels.
- `screen_support10_case1_helpers.py`: **NONREPRODUCTION**; 32/32 rows reached HiGHS status 1/time limit, hence 0 infeasible and 32 unknown. Exact summary: `SUPPORT10_HELPER_REPLAY_FAILURE.json`.
- `star_certificate_cover.py 8 6 5 dense8`: 1,264 dense extensions tested; 488 certificate-feasible; minimum star slack 40.
- `check_n18_555_d2c_z3.py`: UNSAT for the fixed `(5,5,5)` geometry.
- `validate_d2c_local_criterion.py`: zero local/brute-force criticality mismatches; the diameter-stage 82-edge model is not D2C and has 61 noncritical edges.

The fresh r=12 source replay covers all 6,386 strict support-ten kernels with per-shard survivor counts `[10,11,0,0,6,5,0,0]`, 32 distinct survivors and zero solver unknowns. It reuses the committed source encoding. The helper-aware screens for supports 6--9 reproduced; the support-ten screen did not. A solver timeout is neither feasibility nor infeasibility.

### Conjectural or incomplete interpretation

- `250/429` is not externally established and does not settle the live strip.
- `S<=14` is frozen. The retained audited finite edge bound is through `S<=13`.
- No rigidity theorem near `Delta=n/2` was completed. Balanced `K(floor(n/2),ceil(n/2))` graphs remain mandatory positive controls, including the odd-order examples inside the strip.
- The n=18 row is a bounded diagnostic inside the finite obstruction, not a threshold theorem. Its many abstract exclusions cannot be read as counts of D2C graphs.
- Bounded collision searches and nonappearance of an `H>=15` actual fixture prove neither nonrealizability nor asymptotic closure.

## Corrections and failures

1. **Unrestricted crossed-supplement injectivity is invalid.** Six collisions occur in the first bounded actual-D2C population; 13 in the larger live-strip check. Use pair Hall eligibility and congestion, not injectivity.
2. **The supplement-endpoint cap was invalid.** Assigned witnesses lie in `B=N(v)`, of size `Delta`, not in the outside set of size `n-Delta-1`. The false cap is preserved in the 13:00 telemetry but explicitly superseded by `EXACT_D2C18_AND_SUPPLEMENT_CAP.md`.
3. **The old 42-survivor count was wrong.** The correct saved and freshly replayed total is 32. The error was bookkeeping; the fresh source replay restores that part of the finite ledger.
4. **The support-ten helper solve did not reproduce.** All 32 fresh rows timed out under the committed script's 180-second limit. The saved 32-infeasible result remains evidence, but not adequate promotion evidence. `S<=14` is frozen.
5. **Telemetry records are not schema-uniform.** Closed intervals used `seconds`, `duration_seconds`, `duration`, and `end`. The schema now mandates `start`, `stop`, `seconds`, `unit`. This audit normalized historical variants explicitly.
6. **One proof note was text-corrupted.** `PAIR_ELIGIBILITY_HALL_FILTER.md` contained tab/form-feed substitutions for LaTeX escapes. It is repaired without changing the claim.
7. **Launch recovery is still unreliable.** Four triggers delivered zero research, one lacked any canonical record, and six useful records were never finalized. Two watchdog configurations improved recovery coverage but did not establish reliable primary launches.

No dependency on the external `Erdos742/Erdos742` `e+disj+X` proof core was found in the new files. References to it are trust-boundary statements only.

## Canonical launch and utilisation table

`+5` reports durable STARTED publication; `+10` reports the first substantive checkpoint relative to actual entry. `PASS` means the evidenced timestamp met the applicable aim. A PENDING/absent final boundary makes the record unverified even when useful research was preserved.

| Trigger | Actual start | +5 / +10 | Segments / closed intervals | Forward stop / preservation | Verified forward | Units | Target | Canonical class |
|---|---|---|---:|---|---:|---:|---|---|
| 01:00 | 01:01:57 | late 27s / PASS | 1 / 7 | 01:47:42 / 01:51:19 | 18m10s | 7 | 40m NO | SHORT/NONCOMPLIANT |
| 02:00 | 02:01:19 | PASS / PASS | 1 / 7 | 02:50:56 / 02:54:28 | 40m10s | 3 | YES | COMPLIANT |
| 03:00 | 03:02:45 | PASS / PASS | 1 / closed | 03:53:29 / 03:58:11 | 40m02s | 5 | YES | SHORT/NONCOMPLIANT: final report crossed 04:00 trigger |
| 04:00 | 04:59:32 | no / no | late delivery / 0 | none / after hard close | 0 | 0 | N/A | MISSED/NO-FORWARD-RESEARCH |
| 05:00 | UNVERIFIED | no / no | 0 / 0 | UNVERIFIED | 0 verified | 0 | UNVERIFIED | UNVERIFIED/MISSING-TELEMETRY |
| 06:00 | 06:03:18 | PASS / PASS | 1 / closed | 06:51:31 / 06:53:06 | 17m13s | 10 | NO | SHORT/NONCOMPLIANT |
| 07:00 | 07:59:51 | no / no | late delivery / 0 | none / after hard close | 0 | 0 | N/A | MISSED/NO-FORWARD-RESEARCH |
| 08:00 | 08:58:34 | no / no | late delivery / 0 | none / 08:59:46 | 0 | 0 | N/A | MISSED/NO-FORWARD-RESEARCH |
| 09:00 | 09:26:51 | late / PASS | 1 unclosed / 3 | UNVERIFIED / UNVERIFIED | 7m13s lower bound | 3 | N/A | LATE-START/N/A-TARGET; unfinalized |
| 10:00 | 10:00:51 | PASS / PASS | 1 / closed | 10:50:48 / 10:52:51 | 31m00s | 10 | NO | SHORT/NONCOMPLIANT |
| 11:00 | 11:04:13 | late 1s / PASS | 1 unclosed / 1 | UNVERIFIED / UNVERIFIED | 3m08s lower bound | 1 | UNVERIFIED | UNVERIFIED/MISSING-TELEMETRY |
| 12:00 | 12:02:29 | PASS / PASS | re-entry / closed | 12:48:37 / 12:50:12 | 31m37s | 6 | NO | SHORT/NONCOMPLIANT |
| 13:00 | 13:08:53 | late / PASS | 1 unclosed / 2 | UNVERIFIED / UNVERIFIED | 1m07s lower bound | 2 | UNVERIFIED | UNVERIFIED/MISSING-TELEMETRY |
| 14:00 | 14:00:30 | PASS / PASS | 1 / closed | 14:53:19 / 14:54:20 | 41m28s | 5 | YES | COMPLIANT |
| 15:00 | 15:00:47 | PASS / PASS | 1 / closed | 15:53:38 / 15:56:19 | 37m43s | 7 | NO | SHORT/NONCOMPLIANT; workers terminated 35s after cutoff, uncredited |
| 16:00 | 16:06:11 | late / PASS | 1 unclosed / 1 | UNVERIFIED / UNVERIFIED | 0m50.31s lower bound | 1 | UNVERIFIED | UNVERIFIED/MISSING-TELEMETRY |
| 17:00 | 17:07:58 | late / PASS | 1 unclosed / 1 | UNVERIFIED / UNVERIFIED | 4m56s lower bound | 1 | UNVERIFIED | UNVERIFIED/MISSING-TELEMETRY |
| 18:00 | 18:03:44 | late 35s / PASS | 1 / closed | 18:50:04 / 18:51:43 | 31m21s | 7 | NO | SHORT/NONCOMPLIANT |
| 19:00 | 19:00:47 | PASS / PASS | 1 / closed | 19:47:37 / 19:49:08 | 40m36s | 5 | YES | COMPLIANT |
| 20:00 | 20:01:26 | PASS / PASS | 1 / closed | 20:48:14 / 20:49:34 | 41m00s | 5 | YES | COMPLIANT |
| 21:00 | 21:09:54 | late / PASS | 1 unclosed / 4 | UNVERIFIED / UNVERIFIED | 12m30s lower bound | 3 | UNVERIFIED | UNVERIFIED/MISSING-TELEMETRY |
| 22:00 | 22:01:42 | PASS / PASS | re-entry / closed | 22:50:01 / 22:51:35 | 32m05s | 4 | NO | SHORT/NONCOMPLIANT |
| 23:00 | 23:04:21 | durable STARTED late / none | 1 unclosed / 0 | none / none | 0 | 0 | UNVERIFIED | MISSED/NO-FORWARD-RESEARCH |

### Aggregate

- Scheduled research triggers: 23; separate audits: 1; manual research: 0; admin/configuration tasks: separate and not credited.
- Canonical records present after audit reconciliation: 23/23; present before audit: 22/23.
- Scheduled sessions with any evidenced substantive research: 18.
- Fully finalized records: 15, including three zero-research late deliveries.
- Completed, evidenced 40-minute target sessions: 5 (`02`, `03`, `14`, `19`, `20`).
- Canonical classes: 4 COMPLIANT; 8 SHORT/NONCOMPLIANT; 1 LATE-START/N/A-TARGET; 4 MISSED/NO-FORWARD-RESEARCH; 6 UNVERIFIED/MISSING-TELEMETRY.
- Durable STARTED by trigger+5: 10/23. Every one of the 18 sessions with evidenced substantive research preserved its first checkpoint within ten minutes of actual entry.
- Substantive-unit ledger total: 85.
- Fully finalized records: 622m01s evidenced available research windows and 402m25s verified forward work, giving 64.70% over those evidenced windows only.
- All closed forward intervals, including partial/unfinalized records: 432m09.31s. This is a lower bound on scheduled research time, not full-day utilisation.

The 03:00 final report crossed the 04:00 trigger; the 04:00 delivery was missed. This is an evidenced overlap, but it does not prove that the 42-second report overrun caused the later 58-minute launch delay. Cause remains unknown. No other prior-session preservation is evidenced as displacing the next trigger.

## First three post-cutover triggers

1. `01:00`: research ran and checkpointed promptly, but durable STARTED was 27 seconds late and only 18m10s is verified. No focus credit.
2. `02:00`: durable STARTED and first checkpoint met their aims; 40m10s verified; finalized; compliant; focus credit.
3. `03:00`: durable STARTED and first checkpoint met their aims; 40m02s verified; focus credit, but the final user report crossed the next trigger and the process record is noncompliant.

Configuration, enabled state and `last_run_time` are not counted as execution evidence. The standalone task was observed enabled with the correct independent-#742 prompt; the retired chat-bound task and old health checker were observed paused. Two enabled recovery watchdogs explain several recovered starts but do not cure missing primary launches or unfinished telemetry.

## Focused-session gate

The focused-session count is `6/24`: the original threshold-improvement session plus five complete evidenced 40-minute sessions on 23 September. The gate is not due. Its mathematical success condition has already been met provisionally by the strict improvement from `7/12` to `250/429`; the demand-15/16 normal form also supplies a credible finite-dimensional obstruction. Recommendation: continue until the first audit after 24 credited sessions, while freezing `S<=14` and enforcing the stop criteria below. This recommendation is not based on sunk cost.

## Prioritized next-hours programme

1. **Resolve the r=12 nonreproduction.** Produce independently checkable infeasibility certificates or reimplement the 32 support-ten helper systems with a second solver/encoding. `S<=14` stays frozen until every row is decisively classified and the saved result is reproduced.
2. **Complete the n=18 row only as a bounded validation target.** Continue stable index 39,251 onward; stop at the next distinct abstract survivor and test it with the staged exact D2C model. Do not mistake row closure for strip closure.
3. **Return to graph-level demand 15/16.** Use actual source/supplement geometry to exclude or realize the remaining normal forms. Prioritize high-demand star overlap and demand-restricted collisions; unrestricted injectivity is forbidden.
4. **Protect equality.** Develop the near-zero-demand rigidity branch with even and odd balanced complete bipartite graphs as positive controls at every lemma. Equality remains only `S<=8`.
5. **Launch reliability.** Require one canonical writer, STARTED by +5, checkpoint by +10, exact interval keys, and finalization before hard close. Do not count watchdog configuration as recovery.

### Stop/pivot criteria

- Keep `S<=14` frozen until the support-ten timeout discrepancy is resolved by decisive, reproducible evidence.
- Freeze `250/429` on any raw bridge counterexample under a legal selection.
- Reject any equality lemma that excludes `K(floor(n/2),ceil(n/2))`, especially odd order.
- If demand-15/16 remains only an abstract scan after 24 credited sessions, pivot from further scalar enumeration to a direct graph-realizability theorem or abandon this route.
- At the first audit after 24 credited sessions, make an explicit continue/pivot decision from the achieved threshold/rigidity/finite-obstruction evidence.

## Deferred items

This audit did not independently reimplement the r=12 source or helper MILPs, exhaustively replay all 39,250 n=18 stable indices, or repeat the unchanged 250/429 scalar package. It reran the listed load-bearing checkers and exposed the support-ten timeout discrepancy. These deferred items remain explicit trust risks; no unperformed review is described as complete.
