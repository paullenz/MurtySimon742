# Murty–Simon / Erdős #742 — current state handoff

<!-- CURRENT-STATUS:START -->
<!-- FORCED-CORE-AUDIT-V2-STAGING -->
**15 September 2026 — independent forced-core audit v2 launch checkpoint.** The completed 306-state forced-core discovery remains discovery-only: 170 N34-derived candidate exclusions and 136 rescanned survivors, with 646 stored-witness survivors for 782 route survivors. The independently structured type-multiplicity scanner now has **29/170 exact field-for-field candidate matches** (the original 24 plus states `9858,10296,10507,10858,10898`). A direct replay through the independent acceptance semantics validates **136/136 survivor witnesses** and exactly reproduces witness `E`, target-flow cost and envelope; an initial 26-failure replay was traced solely to misreading the canonical `envelope=-1` sentinel and is recorded in the audit-v2 package. The full one-state-per-job 170-candidate audit is installed on `research/forced-core-canonical-audit-v2`; its final gate also requires the 136-witness replay. In parallel, `RECEIVER_PRICE_LEMMA.md` proves scalar receiver-capacity and fractional receiver-price inequalities as necessary conditions; eight audited closures currently have zero partition-only rejections, but completeness is **not** claimed. **Canonical/promoted status unchanged: 4,626 exclusions / 952 survivors / 3,632 whole-state closures. External review remains OPEN.**

**15 September 2026 — completed forced-core canonical discovery; audit/promotion pending.** The authoritative resumed-enumeration workflow **34950746007** completed successfully on `25fd9044e9d8ef52326d27f9a97732916aef5dc4`. Of the 306 canonical states whose stored witnesses failed the forced-core theorem, exhaustive enumeration returns **170 candidate whole-state exclusions and 136 survivors**. Together with the 646 stored witnesses that already survive the theorem, this leaves **782 definite survivors of the forced-core route**. The final aggregate contains **170 N34-derived candidate exclusions and 0 N35 candidate exclusions**. The earlier 124 locally certified replacement witnesses all reappear among the 136 final survivors; the other 12 survivor state IDs are `2454,3145,4453,4618,5163,5672,5972,7664,7851,7927,9014,9849`. The initial **24** independently reimplemented complete exclusions all occur among the final 170 and still agree field-for-field with the primary scanner. Final artifact **10396963173**, `canonical-forced-core-discovery-final`, digest `sha256:60409b6049e9436aeaaaf898509f7022abb3b3ade030359174379ba22e238705`, records `promotion_status=DISCOVERY_ONLY_NOT_PROMOTED`. **Canonical/promoted mathematical status is unchanged: 4,626 exclusions / 952 survivors / 3,632 whole-state closures. No forced-core closure is ledger-promoted by this checkpoint.** External review remains OPEN.

**Repository-root archival cleanup — 15 September 2026.** Six historical `README_*` snapshots and eight historical `CURRENT_STATE_*` snapshots from 14 September are preserved byte-for-byte under [`archive/status-snapshots/2026-09-14/`](archive/status-snapshots/2026-09-14/), leaving `README.md` and `CURRENT_STATE.md` as the only live root status surfaces. No historical evidence is deleted. **Canonical mathematical status unchanged.**

**Maintenance provenance correction — 15 September 2026.** Historical commit `aa6c41fcede3bf2e7e935a00840030ef0b9ee1df` came from successful restoration run `34905883642`; GitHub records `paullenz` as both actor and triggering actor. The restoration script set synthetic author/committer `Research verification <verification@users.noreply.github.com>`, which GitHub mapped to account `verification` (display name Bill Wang). This is an attribution error, not evidence that that account triggered the workflow. The commit is retained without rewriting the audited chain; the one-off workflow is now manual-only, completed replays make no repository mutation, and future workflow-created commits use canonical `github-actions[bot]`. **Mathematical/canonical status unchanged.**
<!-- RELATIONAL-FULL-PROMOTION:PROMOTED -->

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Every commit must update the CURRENT-STATUS blocks in BOTH this file and README.md atomically. Read [`AGENTS.md`](AGENTS.md), [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md), [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md), and newer commits before continuing.

## Canonical status — unchanged by the completed forced-core discovery

```text
whole-state closures:             3,632
canonical exclusions:             4,626
canonical survivors:                952
  N34-derived survivors:             949
  N35-derived survivors:               3
recovered relational candidates:  2,655 — AUDITED AND PROMOTED
```

The reviewed relational promotion remains the current canonical finite frontier. Fixed-order n25/n27-through-n35 and general7/12 candidates remain preserved with external review, novelty assessment and third-party reproduction OPEN. No unrestricted proof or newly realized graph is claimed.

If and only if the 170 forced-core candidates clear complete independent audit and the separate reviewed promotion gate, the finite ledger would become:

```text
whole-state closures:             3,802
canonical exclusions:             4,796
canonical survivors:                782
  N34-derived survivors:             779
  N35-derived survivors:               3
```

Those numbers are **provisional promotion consequences, not current canonical counts**.

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

## Canonical forced-core discovery — completed, not promoted

[`canonical-forced-core-scan-v1`](project/research/general_n/2026-09-15-forced-core-canonical-scan-v1/README.md) pins the exact promoted relational discovery result SHA256 `2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970`. The stored-witness pre-screen was used only as an optimization:

```text
canonical relational survivors:          952
stored witnesses surviving new theorem:  646
stored witnesses rejected by new theorem:306
rescanned survivors after exhaustive run:136
candidate whole-state exclusions:        170
route survivors after completed scan:    782
candidate exclusions by source:      N34=170, N35=0
```

The authoritative remote workflow is GitHub Actions run **34950746007**, head `25fd9044e9d8ef52326d27f9a97732916aef5dc4`. It completed **SUCCESS** on 15 September 2026. Its final aggregate artifact is:

```text
artifact id: 10396963173
name: canonical-forced-core-discovery-final
size: 19,778 bytes
digest: sha256:60409b6049e9436aeaaaf898509f7022abb3b3ade030359174379ba22e238705
promotion_status: DISCOVERY_ONLY_NOT_PROMOTED
```

The 646 stored-witness survivors are definite non-exclusions for this route because their existing `q` witnesses satisfy both the promoted relational relaxation and the new theorem. The full enumeration supplies explicit accepted witness profiles for the other 136 survivors. Therefore search failure is no longer being used to infer any of the 170 candidates: each candidate is a completed whole-state exhaustive exclusion under the exact scanner's acceptance conditions. That still does **not** make the 170 canonical until independent implementation checks and a reviewed promotion gate succeed.

## Canonical forced-core reconciliation and independent audit — incomplete

[`forced-core-canonical-audit-v1`](project/research/general_n/2026-09-15-forced-core-canonical-audit-v1/README.md) preserved **124 explicit replacement witnesses** before the full run finished. All 124 reappear among the final 136 rescanned survivors. The **12 additional survivors found only by the complete enumeration** are:

```text
2454, 3145, 4453, 4618, 5163, 5672,
5972, 7664, 7851, 7927, 9014, 9849
```

The same audit package preserves an independently structured type-multiplicity implementation. Its initial 24 complete whole-state exclusions agree with the primary implementation field-for-field on `profiles_tested` and every rejection/pass stage count; all 24 are contained in the final 170 exclusion candidates.

This is strong internal reconciliation, but it is not yet the promotion gate. The independent type-multiplicity scanner must be expanded substantially — preferably to all 170 candidate closures — and the survivor side should receive an independent witness replay so the audit is not one-sided.

All three N35 canonical survivors remain definite survivors of this route. Any promotion from the completed forced-core discovery would therefore remove only N34-derived states.

## Preserved predecessor evidence

- Singleton-destination theorem: original rows347,471,586 excluded; remote workflow34910561258 SUCCESS.
- Row471 branches `e_L=39,40`: conditioned rigidity, run34906169745 SUCCESS.
- Row471 `e_L=41`: independent high-block/common-pressure contradiction.
- Row471 `e_L=42,43`: source-group totals `214,215<222`, run34909572352 SUCCESS.
- Row108 source-sharing: remote workflow34906766833/job104185160249 SUCCESS.
- Historical failed runs and process/audit failures remain failures; nothing here repaints them green.

## Immediate next target

1. freeze the completed 306-state aggregate and its provenance in a permanent research package;
2. run the independently structured type-multiplicity scanner across the final 170 candidate exclusions and require exact field-by-field agreement;
3. independently replay all 136 rescanned survivor witnesses, preserving the 124 pre-certified rescues and the 12 complete-enumeration-only survivors separately;
4. build a promotion gate that requires exactly 306 expected keys, no duplicates or missing keys, exactly 170 exclusions +136 rescanned survivors, exact independent exclusion agreement, successful survivor witness replay, preservation of the initial 24 audit matches and 124 rescue reconciliation, and zero N35 exclusions;
5. promote the finite ledger only if every gate succeeds; otherwise preserve and diagnose every discrepancy without weakening acceptance criteria;
6. turn repeated receiver-count/high-threshold patterns into an aggregate inequality that does not require per-profile enumeration;
7. continue external review of the graph-to-selected/residual bridge and fixed-neighbourhood routing theorem.
<!-- CURRENT-STATUS:END -->

## Preservation, failures and audit gates

The complete pre-row108 handoff remains preserved byte-for-byte in [`archive/status-snapshots/2026-09-14/CURRENT_STATE_PRE_ROW108_2026-09-14.md`](archive/status-snapshots/2026-09-14/CURRENT_STATE_PRE_ROW108_2026-09-14.md); the other historical root README/CURRENT_STATE snapshots are indexed in [`archive/status-snapshots/2026-09-14/`](archive/status-snapshots/2026-09-14/). Earlier archives, reviewer packages, counterexamples and negative experiments remain intact.

Historical failures remain failures: source-price transfer run34904353492, N30 navigation run34906766832, the red-team-history guard failure34908428824, and standalone row471 process commit `2667a909...` are not repainted by later repairs. The branch-specific charge route did not itself finish row471; the singleton-destination theorem is a distinct stronger structural argument. The forced-core/high-squeeze theorem is another distinct successor and does not retrospectively turn earlier uncoupled witnesses or solver statuses into graph realizations.

The 2,655 relational candidates have cleared complete coverage, dual agreement, zero unresolved cases, successful aggregate and the separate reviewed-ledger step. Their promotion changes the canonical finite frontier. Synthetic sample exclusions, including the 713/713 original and 715/715 fresh closures, **do not** change it. The completed canonical forced-core discovery likewise remains discovery-only until its independent audit and reviewed promotion gates are satisfied.

Internal proof checks, successful CI and durable publication do not replace external specialist review of the canonical graph-to-selected/residual bridge, selected-incidence eligibility, destination capacities and the fixed-neighbourhood labelled-routing criterion.
