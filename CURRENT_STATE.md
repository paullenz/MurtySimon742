# Murty–Simon / Erdős #742 — current state handoff

<!-- CURRENT-STATUS:START -->
**15 September 2026 — checkpoint `forced-core-canonical-full-audit-v1` installation.** Authoritative discovery workflow **34950746007** on `25fd9044e9d8ef52326d27f9a97732916aef5dc4` has completed **SUCCESS** with exact 306-key coverage: **170 candidate whole-state exclusions and 136 rescanned survivors**. All 170 candidates are N34-derived; all three N35 targets survive. All **124** locally certified replacement witnesses reappear among the exhaustive survivors, and the remaining **12** survivors are states `2454,3145,4453,4618,5163,5672,5972,7664,7851,7927,9014,9849`. The predecessor's **24** independently audited exclusions are all contained in the final 170 and their stored stage counts match the completed primary aggregate. A 170-state independently structured type-multiplicity replay is installed on research branch `research/forced-core-canonical-full-audit-v1`; it must match every deterministic stage count before any promotion is considered. **Mathematical/canonical status is unchanged: 4,626 exclusions / 952 survivors / 3,632 whole-state closures. No forced-core closure is promoted by this checkpoint.** External review remains OPEN.
<!-- RELATIONAL-FULL-PROMOTION:PROMOTED -->

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Every commit must update the CURRENT-STATUS blocks in BOTH this file and README.md atomically. Read [`AGENTS.md`](AGENTS.md), [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md), [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md), and newer commits before continuing.

## Canonical status — unchanged by the full forced-core audit installation

```text
whole-state closures:             3,632
canonical exclusions:             4,626
canonical survivors:                952
  N34-derived survivors:             949
  N35-derived survivors:               3
recovered relational candidates:  2,655 — AUDITED AND PROMOTED
```

The reviewed relational promotion remains the current canonical finite frontier. Fixed-order n25/n27-through-n35 and general7/12 candidates remain preserved with external review, novelty assessment and third-party reproduction OPEN. No unrestricted proof or newly realized graph is claimed.

## Original synthetic boundary sample — 713/713

The singleton-destination theorem excluded rows347,471,586 and [`forced-core-capacity-v1`](project/research/general_n/2026-09-15-forced-core-capacity-v1/README.md) excluded rows160 and338. Its standard-library proof package now has dedicated remote workflow **34944185174 SUCCESS**. The original 713-profile namespace is closed under the accumulated necessary conditions.

The forced-core mechanism is:

```text
A={i:s_i<=1}, h=|A|, U={u:rho_u=1 and q_u=h}.
```

Every `u in U` has `S_u=A`. For an obligation `(u,i)` to destination `v`, fixed-neighbourhood routing requires

```text
S_u minus N_v = {i},
S_v subset N_u,
```

and receiver capacity `c_v=rho_v+b-a-1`. A receiver can serve at most one core label. Row160 needs three capacity-10 bins from `5,5,5,4,4,4,4` (best minimum9); row338 needs20 obligations against capacity17.

## Fresh synthetic boundary sample — 715/715

The preserved fresh seed `74220260919` had seven non-rejections: rows20,91,391,490,528,562,677. [`fresh-forced-core-high-squeeze-v1`](project/research/general_n/2026-09-15-fresh-forced-core-high-squeeze-v1/README.md) explicitly scans only this fresh namespace. Its research-branch workflow **34946294672 SUCCESS** reproduces the closure.

At residual level `r=1`, six profiles fail even the total relaxed receiver-capacity inequality:

```text
row   h   |U|   receiver capacities   total / required
 20   3    10   7,6,6,5               24 / 30
 91   2    12   4                       4 / 24
391   2    10   8,4                    12 / 20
528   1    11   7                       7 / 11
562   1     9   none                    0 /  9
677   1    10   none                    0 / 10
```

Fresh row490 has core `A={0,1,2}` and eleven forced sources. Its six relaxed receivers have capacities `8,6,6,9,8,7`, so the raw partition is feasible. But each core label needs11 units while every receiver has capacity below11; since a receiver serves only one core label, all six receivers are forced used.

Every used receiver `v` satisfies `S_v subset A_r union R_u` for at least one forced source, and `|R_u|=1`; therefore it has at most one selected label outside A. At threshold3 the profile requires

```text
sum_{s_i>=3} s_i = 45
```

selected high-label incidences. Sources with `rho>=3` have only46 raw selected slots, and the forced use of receivers3 and17 removes respectively1 and2 high slots (receiver23 loses0), leaving

```text
43 < 45.
```

Thus row490 is excluded by an explicit integer inequality, not by a numerical solver status. Frozen canonical result SHA256:

```text
7357a5139417a1b48f94d8ddbb6122c57363ce70ab0c4586673a290a25c51464
```

## General structural form

For arbitrary residual level `r`, put `A_r={i:s_i<=r}`, `h=|A_r|`, `U_r={u:rho_u=r,q_u=h}`. Then every `u in U_r` has `S_u=A_r`. Any receiver of a forced-core obligation lies in the relaxed class

```text
v not in U_r,
q_v <= h+r-1,
q_v+rho_v >= h-1,
```

and each receiver is dedicated to at most one core label. If such a receiver is forced used, then `S_v subset A_r union R_u`, so for every threshold `tau>r` it has at most `r` selected labels with `s_i>=tau`. This couples exact receiver usage to the existing threshold-demand machinery.

## Canonical forced-core discovery complete; full independent audit installed — not promoted

[`canonical-forced-core-scan-v1`](project/research/general_n/2026-09-15-forced-core-canonical-scan-v1/README.md) pins the promoted-relational discovery result SHA256 `2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970`. The stored-witness pre-screen was only an optimization; complete enumeration now gives:

```text
canonical relational survivors entering route: 952
stored witnesses surviving new theorem:          646
stored witnesses requiring resumed enumeration: 306
rescanned survivors:                             136
candidate whole-state exclusions:                170
survivors of this forced-core route:              782
candidate N34 exclusions:                        170
candidate N35 exclusions:                          0
```

The 646 stored witnesses are definite non-exclusions for this route. [`forced-core-canonical-audit-v1`](project/research/general_n/2026-09-15-forced-core-canonical-audit-v1/README.md) preserves 124 further explicit witnesses; every one reappears among the 136 exhaustive survivors. The exact set difference is the twelve later survivors `2454,3145,4453,4618,5163,5672,5972,7664,7851,7927,9014,9849`, all N34. Search failure was never used as exclusion evidence.

Authoritative remote workflow **34950746007** completed successfully with exact key coverage. Its completed aggregate classifies all 306 targets and yields the 170/136 split above. All three N35 targets survive, so every candidate new closure is N34-derived. This remains discovery evidence, not a ledger promotion.

The predecessor audit package preserves an independently structured type-multiplicity implementation. Its first 24 complete whole-state exclusions agree with the primary implementation field-for-field on `profiles_tested` and every rejection/pass stage count; all 24 are members of the final 170 and their stored counts reconcile with the completed primary aggregate.

[`forced-core-canonical-full-audit-v1`](project/research/general_n/2026-09-15-forced-core-canonical-full-audit-v1/README.md) durably freezes the exact 170 candidate keys and 136 survivor keys and installs a full 170-state independent replay. The workflow requires exact agreement on `S`, `Emax`, complete profile count, every pair-capacity/incidence/Hall/cost/core stage count and final status, followed by exact 170-key aggregate coverage. Any mismatch is preserved and fails the aggregate. **No candidate is promoted merely because the discovery or internal audit succeeds.**

## Preserved predecessor evidence

- Singleton-destination theorem: original rows347,471,586 excluded; remote workflow34910561258 SUCCESS.
- Row471 branches `e_L=39,40`: conditioned rigidity, run34906169745 SUCCESS.
- Row471 `e_L=41`: independent high-block/common-pressure contradiction.
- Row471 `e_L=42,43`: source-group totals `214,215<222`, run34909572352 SUCCESS.
- Row108 source-sharing: remote workflow34906766833/job104185160249 SUCCESS.
- Historical failed runs and process/audit failures remain failures; nothing here repaints them green.

## Immediate next target

1. complete the 170-state independent type-multiplicity audit and require exact stage-count/key agreement;
2. preserve every mismatch or, if clean, the complete audit aggregate and hashes;
3. only after a clean full audit perform a separate reviewed ledger/non-overlap promotion step;
4. turn repeated receiver-count/high-threshold patterns into an aggregate inequality that does not require per-profile enumeration;
5. continue external review of the graph-to-selected/residual bridge and fixed-neighbourhood routing theorem.
<!-- CURRENT-STATUS:END -->

## Preservation, failures and audit gates

The complete pre-row108 handoff remains preserved byte-for-byte in [`CURRENT_STATE_PRE_ROW108_2026-09-14.md`](CURRENT_STATE_PRE_ROW108_2026-09-14.md); earlier archives, reviewer packages, counterexamples and negative experiments remain intact.

Historical failures remain failures: source-price transfer run34904353492, N30 navigation run34906766832, the red-team-history guard failure34908428824, and standalone row471 process commit `2667a909...` are not repainted by later repairs. The branch-specific charge route did not itself finish row471; the singleton-destination theorem is a distinct stronger structural argument. The forced-core/high-squeeze theorem is another distinct successor and does not retrospectively turn earlier uncoupled witnesses or solver statuses into graph realizations.

The 2,655 relational candidates have cleared complete coverage, dual agreement, zero unresolved cases, successful aggregate and the separate reviewed-ledger step. Their promotion changes the canonical finite frontier. Synthetic sample exclusions, including the 713/713 original and 715/715 fresh closures, **do not** change it. The canonical forced-core discovery and audit remain discovery/audit-only until complete independent audit and a separate reviewed promotion gate are satisfied.

Internal proof checks, successful CI and durable publication do not replace external specialist review of the canonical graph-to-selected/residual bridge, selected-incidence eligibility, destination capacities and the fixed-neighbourhood labelled-routing criterion.
