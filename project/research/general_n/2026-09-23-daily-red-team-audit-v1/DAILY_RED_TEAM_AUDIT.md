# Independent Erdos #742 daily adversarial audit - 23 September 2026

Audited head: `320ff91c4b3b1c64e98349788f9f971f65a9ef01`.  Audit scope: the complete Europe/London research day of 22 September, plus the midnight audit.  This report separates graph-theoretic proof, finite necessary-condition computation, actual-graph regression and process evidence.

## Executive disposition

The day made material mathematical progress, but not a proof of Erdős #742.  The independently reconstructed raw graph-to-profile bridge in `2026-09-22-raw-profile-bridge-v1/RAW_PROFILE_BRIDGE.md` survived line review and an exact rerun of `check_raw_profile.py`: 757 D2C graphs, 1,256 maximum-degree roots, 2,722 legal selections, 153 positive-demand selections and both supplement branches, with no discrepancy.  This substantially reduces yesterday's principal bridge risk, but is same-project internal verification, not external review.

The zero-demand equality theorem in `ZERO_DEMAND_EQUALITY.md` survived quantifier, parity and balanced-complete-bipartite checks.  The finite residual pipeline supports the edge bound through total demand `S<=13` and balanced-complete-bipartite equality through `S<=8`, subject to its stated computer-assisted trust boundary.  The general positive-demand strip and full equality characterization remain open.  The candidate maximum-degree threshold remains exactly `250/429`; no lower threshold was obtained.

Two saved evidence files were corrupt at audited head because truncated tool output, including warning and ellipsis markers, had been committed as if complete: `R8_EQUALITY_CORE_SCREEN.json` and `r11_support9_masks.txt`.  Consequently the advertised replay initially crashed.  The corrupt originals are preserved with `.corrupted-at-320ff91` names.  Both files were regenerated directly from their saved source programs; `verify_r8_pipeline.py` and `audit_r11_pipeline.py` then passed.  This is a real repository/evidence failure and a completed repair, not a mathematical counterexample.

## Material claims and hostile tests

### 1. Raw criticality to profile

The note proves, for every maximum-degree root and every legal quasi-edge selection, the exact ledger `e(F)=r+t`, the source-demand injection, supplement forcing, threshold capacity and radical profile inequality.  The separate `a=0` star case correctly repairs the earlier strict `0<0` display defect.  The proof does not import the external `e+disj+X` inequality.  Repository dependency search found no hidden invocation of that proof core in the new chain.

Rerun identifier: `check_raw_profile.py`, source SHA-256 `138ef5194f134e1902685692285af1f816a18792dbd337439634bfdc3dfbf2d4`.  Exact result: PASS with 8,374 independent BFS edge-deletion checks.  Limit: there are no positive-surplus actual-graph fixtures, and only two high-load threshold checks.

### 2. Equality geometry near Delta=n/2

`ZERO_DEMAND_EQUALITY.md` proves internally that `S=0` implies the Murty-Simon bound, with equality exactly the balanced complete bipartite graph.  The odd case explicitly gives `K(k,k+1)` and therefore does not exclude the equality family lying in the unresolved degree strip.  The Boolean orientation argument permits repeated codes and uses maximum degree only where stated.  No flaw was found in the even/odd split, sink argument or `a=1` endpoint.

The exact positive-residual equality pipeline replays through `r=8`: 11,350 strict labelled rows / 68 strict orbits and 26,838 equality labelled rows / 203 equality orbits; 39 equality source-feasible orbits yield 2,103 source populations and zero supplement survivors.  This supports, internally, equality through `S<=8`; it is not a proof for arbitrary demand.

### 3. Bounded positive demand

The analytic residual-support lemmas and finite quotient/source/supplement screens give strict closure through `r=11`, hence the edge bound through `S<=13` because a strict counterexample has `S>=r+2`.  The repaired `audit_r11_pipeline.py` reports 2,496, 3,273 and 280 strict rows at supports 8, 9 and 10; 16, 8 and 3 source survivors; and zero supplement survivors.

A hostile dependency comparison found that the `r=8` equality checker admits residual-free helper sources while later `r=10/r=11` supplement scripts omit them.  The omission was tested rather than waved away:

- exact helper-aware replay of all four `r=10` surviving kernels leaves zero supplement-feasible populations;
- an optimistic helper-aware MILP makes 24 of the 27 `r=11` kernels infeasible;
- the remaining three time out, but each has only the all-zero residual-free type and that type discharges no supplement obligation, so their original exhaustive DFS is unaffected;
- none of the 27 stored witness populations reopens.

The audit therefore retains `S<=13` at internal computer-assisted status.  It does not promote it to external verification: the cross-file audit does not independently reimplement the orbit quotient or source/supplement algorithms.

The `r=12` support-ten partition `(2,2,1^8)` remains open.  Its exact source screen leaves 42 of 6,386 strict kernels; the repaired supplement wrapper did not finish before cutoff.  No `S<=14` conclusion is authorized.  Solver interruption is not mathematical evidence.

### 4. Degree threshold and realizability

No claim below `250/429` was made.  The threshold retains candidate/internal-review status, now with a substantially better audited graph bridge.  The plateau and finite quotient systems are constraints, not constructed D2C graphs.  Negative necessary-condition screens can exclude a graph only through the proved bridge; surviving abstract rows are not graph realizations.

## Repository findings and repairs

- Preserved the two corrupt files as historical evidence and regenerated clean canonical outputs from `screen_r8_equality.py` and `r11_support9_orbits.cpp`.
- Added `check_r10_residual_free_helpers.py`, `check_residual_free_helper_gap.py` and `check_r11_optimistic_free_helpers_milp.py` as hostile audit checkers.
- Created one canonical audit-reconciliation record for every previously omitted scheduled trigger.  No timestamps or duration were inferred from commits.
- `CURRENT_STATE.md` and `README.md` are updated to the audited mathematical and operational frontier.  Earlier eventual-D2C work remains historical/reusable.

## Canonical launch and utilisation audit

All 23 scheduled forward triggers are enumerated below.  `RAN` means durable substantive scheduled research occurred; it does not mean the 50-minute target was met.  Times and durations are based only on closed intervals.  The separate manual recovery at 09:14:26 has 11m10s and three units but receives no scheduled-session or focused-session credit.

| Trigger BST | Earliest start | Verified forward | Units | Classification | Evidence / note |
|---|---:|---:|---:|---|---|
| 01:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | audit-created canonical record |
| 02:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | audit-created canonical record |
| 03:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | audit-created canonical record |
| 04:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | audit-created canonical record |
| 05:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | audit-created canonical record |
| 06:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | audit-created canonical record |
| 07:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | audit-created canonical record |
| 08:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | audit-created canonical record |
| 09:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | 09:14 manual recovery kept separate |
| 10:00:38 | 10:02:42 | 35m40s | 11 | SHORT/NONCOMPLIANT | RAN; finalized |
| 11:00:38 | 11:01:19 | 33m21s | 20 | SHORT/NONCOMPLIANT | RAN; finalized |
| 12:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | audit-created canonical record |
| 13:00:38 | 13:58:57 | 0m00s | 0 | MISSED/NO FORWARD | late zero-research delivery; closure incomplete |
| 14:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | audit-created canonical record |
| 15:00:38 | 15:04:10 | 32m39s | 9 | LATE-START/TARGET N/A | RAN; 49m28s available |
| 16:00:38 | 16:03:51 | 28m36s | 11 | LATE-START/TARGET N/A | RAN; 49m47s available; checkpoint 19s late |
| 17:00:38 | 17:00:58 | 26m37s | 13 | SHORT/NONCOMPLIANT | RAN; finalized |
| 18:00:38 | 18:04:09 | 17m33s | 16 | LATE-START/TARGET N/A | RAN; closed intervals only |
| 19:00:38 | 19:58:31 | 0m00s | 0 | MISSED/NO FORWARD | late zero-research delivery |
| 20:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | audit-created canonical record |
| 21:00:38 | 21:02:43 | 28m28s | 11 | SHORT/NONCOMPLIANT | RAN; finalized |
| 22:00:38 | 22:00:33 | 31m02s | 9 | SHORT/NONCOMPLIANT | RAN; unfinished r=12 solve preserved |
| 23:00:38 | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED/MISSING | 23:11/23:14 changes were administration only |

Aggregate: 23 scheduled; 23 canonical records after audit reconciliation (9 existed before audit); 9 fully evidenced deliveries, of which 8 contained scheduled research and one was a finalized zero-research delivery; 0 met the applicable 50-minute target; 5 short/noncompliant; 3 late-start/target-N/A; 2 missed/zero-forward; 13 missing/unverified.  The eight evidenced research windows provide 408m39s of verified available time and 233m56s of closed forward intervals, or 57.25% utilisation over those evidenced windows only.  The same 233m56s is the scheduled-day lower bound; adding the separate manual recovery gives 245m06s.  Scheduled substantive units: 100; manual units: 3.

Separate counts: one midnight audit; one manual-recovery research run; three administrative/configuration episodes.  None is counted as a scheduled forward session.  No prior preservation segment is evidenced as displacing a later trigger; the principal failure is absent or late launch evidence, not proven overrun.

The prospective 40-minute standalone policy begins at 23 September 01:00:38.  Its first three triggers were future at this audit and are not credited.  The next audit must review each individually for durable STARTED by trigger+5 minutes and first substantive checkpoint within ten minutes of entry.

## Focused-session gate and recommendation

Focused-session count remains `1/24`.  Eight useful scheduled runs occurred today, but none met the historical 50-minute qualification, and short research is not relabelled as no work.  The formal gate is not due.  Its mathematical success condition has already been met provisionally by the strict `250/429` improvement; the day also produced a credible finite-dimensional bounded-demand obstruction.  Recommendation: continue, while refusing to equate run count, useful short work and focused-session credit.

## Mandatory next-hours programme

1. Finish the exact helper-aware supplement screen for the 42 `r=12`, support-ten `(2,2,1^8)` kernels.  Stop with an explicit survivor list or full infeasibility certificate; do not claim closure from interruption.
2. Independently reimplement one load-bearing orbit/source stage (prefer `r=11` support nine) rather than adding another demand layer.  Any count mismatch freezes `S<=13`.
3. Seek actual D2C positive-demand/high-load fixtures and replay the full bridge on them.  Bounded nonappearance is not nonrealizability.
4. Return to the residual degree strip only after those gates: combine the validated bridge with the high-codegree cluster or derive a near-zero-demand stability theorem that preserves every balanced complete-bipartite control.
5. Operationally, judge the new standalone cadence by observed artifacts: all 23 daily triggers, first three launches individually, 40-minute target separate from RAN, and no inferred credit.

Stop/pivot criteria: freeze a finite conclusion on any orbit/source mismatch; freeze `250/429` on any raw bridge counterexample; reject any equality lemma that excludes odd balanced complete bipartite graphs; after 24 genuinely credited focused sessions make the explicit continue/pivot decision from the gate evidence.

## Deferred items

The audit did not independently reimplement every orbit canonicalizer or exhaustively repeat the unfinished `r=12` supplement solve.  It did not externally verify the `250/429` scalar package again because no threshold change occurred and yesterday's exact replay remains current.  These omissions are explicit; the audit is complete at the stated scope.
