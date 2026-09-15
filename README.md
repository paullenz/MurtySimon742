# Murty–Simon / Erdős Problem #742

**Reviewers — start here:** [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) and [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). GitHub Issues/comments are preferred for counterexamples, corrections and reproducibility reports.

Open, reproducible research on the Murty–Simon conjecture / Erdős Problem #742. **The unrestricted conjecture is not claimed proved.** External mathematical review, novelty assessment and independent third-party reproduction remain OPEN. The project actively welcomes hostile review, counterexamples, literature corrections and independent reproduction.

<!-- CURRENT-STATUS:START -->
## Current status: fixed-order candidates

| Scope | Preserved candidate result; external review open |
|---|---|
| n=25 | e(G)<=156, equality exactly K(12,13); reviewer-v2 |
| n=27 | e(G)<=182, equality exactly K(13,14); reviewer-v2 |
| n=28 | e(G)<=196, equality exactly K(14,14); reviewer-v2 plus analytic hardening |
| n=29 | e(G)<=210, equality exactly K(14,15); reviewer-v4; difficult Delta=16 branch hand-closed |
| n=30 | e(G)<=225, equality exactly K(15,15); reviewer-v3 |
| n=31 | e(G)<=240, equality exactly K(15,16); source-first reviewer-v1 |
| n=32 | e(G)<=256, equality exactly K(16,16); source-first reviewer-v1 |
| n=33 | e(G)<=272, equality exactly K(16,17); source-first reviewer-v1 |
| n=34 | e(G)<=289, equality exactly K(17,17); reviewer-v2; final heavy certificate hand-replaced |
| n=35 | e(G)<=306, equality exactly K(17,18); reviewer-v1 |

## Current status: general research

| Workstream | Latest established or recorded position |
|---|---|
| General maximum-degree candidate | For n>=6, Delta(G)>=(7/12)n implies e(G)<floor(n^2/4); external review and novelty assessment open |
| Canonical finite frontier | **4,626 exclusions / 952 survivors; 3,632 quantified whole-state closures** after reviewed promotion of the fully audited relational family |
| Relational audit/promotion | **2,655/2,655 audited keys promoted** after run **34854911792 SUCCESS** and reviewed ledger reconciliation: 2,580 N34 + 75 N35 closures; 949 N34 + 3 N35 survivors remain |
| Forced-core routing capacity | [`forced-core-capacity-v1`](project/research/general_n/2026-09-15-forced-core-capacity-v1/README.md) closes original rows160 and338; dedicated remote replay **34944185174 SUCCESS** |
| Fresh forced-core/high squeeze | [`fresh-forced-core-high-squeeze-v1`](project/research/general_n/2026-09-15-fresh-forced-core-high-squeeze-v1/README.md): six fresh survivors fail total receiver capacity; row490 fails `43<45` after all six receivers are forced used |
| Original synthetic sample | **713/713 rejected.** Sample-level necessary-condition closure; canonical finite frontier unchanged |
| Fresh synthetic sample | **715/715 rejected.** Separate seed `74220260919`; sample-level necessary-condition closure; canonical finite frontier unchanged |
| Singleton-destination theorem | [`singleton-destination-trap-v1`](project/research/general_n/2026-09-15-singleton-destination-trap-v1/README.md) independently excludes original rows347,471,586; workflow **34910561258 SUCCESS** |
| Row471 branch history | Exact branch packages for `e_L=39,40,41,42,43` remain preserved as independent evidence. The whole-profile singleton-destination obstruction superseded the need to attack `e_L=47` |
| Row108 source sharing | [`conditioned-source-sharing-v1`](project/research/general_n/2026-09-14-conditioned-source-sharing-v1/README.md) excludes original row108; workflow **34906766833 / job104185160249 SUCCESS** |
| Fresh verification | Exact standard-library replay closes all seven retained rows. Frozen parsed-result SHA256 `7357a5139417a1b48f94d8ddbb6122c57363ce70ab0c4586673a290a25c51464`; research-branch replay **34946294672 SUCCESS** |
| Canonical forced-core discovery | Authoritative run **34950746007 SUCCESS** with exact 306-key coverage: **170 candidate whole-state exclusions / 136 rescanned survivors**; all 170 candidates N34, all three N35 targets survive. Discovery only; canonical frontier unchanged |
| Canonical forced-core audit reconciliation | All **124** locally certified rescues reappear among the 136 exhaustive survivors; the remaining **12** are states `2454,3145,4453,4618,5163,5672,5972,7664,7851,7927,9014,9849`. The predecessor's **24** independently audited closures are all in the final 170 and their stage counts reconcile with the completed primary aggregate |
| Full forced-core independent audit | [`forced-core-canonical-full-audit-v1`](project/research/general_n/2026-09-15-forced-core-canonical-full-audit-v1/README.md) freezes the exact 170/136 classification and installs a 170-state independent type-multiplicity replay with exact stage-count and key-coverage gates. Initial run **34985326400** failed before reconciliation because `download-artifact@v4` could not resolve the still-extant historical artifact by name; a pinned-artifact-ID REST download repair is now installed. No mathematical audit stage ran in the failed attempt and no promotion is implied |
| Documentation/process guards | Every commit must pair README/CURRENT_STATE updates. Historical N30 navigation failure, red-team-history guard failure and standalone row471 paired-status process failure remain visible rather than repainted green |
| Active continuation | Run the repaired full 170-state independent audit; preserve every mismatch or clean aggregate; only then consider a separate reviewed ledger promotion and continue the aggregate-inequality/general-theory attack |

**Checkpoint — 15 September 2026, `forced-core-canonical-full-audit-v1` transport repair.** Authoritative forced-core discovery run `34950746007` has completed successfully with exact coverage of all 306 witness-killed states, giving 170 candidate whole-state exclusions and 136 rescanned survivors. All 170 candidates are N34-derived; all three N35 targets survive. The 124 locally certified replacement witnesses all reappear, with exactly 12 additional survivors found by exhaustive enumeration. The original 24 independently audited exclusions are all contained in the final 170 and reconcile field-for-field with the completed primary stage counts. Initial full-audit run `34985326400` failed before reconciliation at the cross-run artifact name-download step; no reconciliation code or independent scanner ran. That failed run is preserved as failed. The repaired workflow downloads the two pinned source artifacts by immutable artifact ID through the GitHub REST endpoint before applying the same 170-state audit gates. **Mathematical/canonical status is unchanged: 4,626 exclusions / 952 survivors / 3,632 whole-state closures. No forced-core closure is promoted by this checkpoint.** External mathematical review remains OPEN.
<!-- RELATIONAL-FULL-PROMOTION:PROMOTED -->

**Standing order:** every commit must update the current-status blocks in BOTH this README and [`CURRENT_STATE.md`](CURRENT_STATE.md), in the same atomic commit, including an explicit unchanged-mathematics statement when appropriate. Keep these fixed-order and general summaries near the top. README changes must be additive/reconciliatory: do not silently delete or materially compress substantive historical content, especially protected audit history, failures/corrections and reviewer navigation. See [`AGENTS.md`](AGENTS.md) and [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md).
<!-- CURRENT-STATUS:END -->

**Canonical repository:** `paullenz/MurtySimon742`. For a restart read [`CURRENT_STATE.md`](CURRENT_STATE.md), [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md), and newer commits. The complete pre-row108 root overview is preserved byte-for-byte in [`README_PRE_ROW108_2026-09-14.md`](README_PRE_ROW108_2026-09-14.md).

<!-- REDTEAM-HISTORY:START -->
## Hostile / red-team audit history and resulting proof hardening

**Protected project history.** This section records what adversarial review actually changed, including defects that invalidated evidence, non-blocking errors, and proof dependencies that were removed after challenge. It is intentionally cumulative. Routine status rewrites must not delete or materially compress it; new hostile-audit results should be appended or reconciled while preserving earlier findings and links.

The repository intentionally preserves failed approaches and audit findings rather than silently rewriting them. Several important proof improvements exist specifically because hostile review attacked earlier versions.

### n=29 — a real defect was found, corrected, and then the computational dependency was largely removed

During the restarted hostile audit of the additional n=29 `Delta=16` cumulative-threshold verifier, a **real normalization bug** was found in its first version: a label-group multiplicity was counted twice. The v1 cumulative-threshold certificates are therefore **invalid as proof evidence** and the historical v1 source remains retained only for auditability. This defect did **not** affect the original n=29 direct route or the separate fully fresh implementation.

A corrected `v2` model was replayed cleanly and again produced zero survivors. The audit then reduced the proof-critical `Delta=16` computation to a smaller trusted kernel, whose clean replay also produced zero survivors with every late exclusion rechecked by exact integer Farkas arithmetic. See the [public-release audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md) and [minimal-kernel report](project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json).

On 11 September, a separate ChatGPT instance with no project background performed a hostile n=29 review supplied by the user. It independently attacked the graph-to-model bridge, residual activity, threshold capacity, isolated-C treatment, corrected LP normalization, exact Farkas semantics and the hand assembly, and reported **no fatal flaw**. It independently recovered the complete n=29 charging-domain counts and a NetworkX graph-atlas bridge regression through order 7; both were reproduced again inside this project. Crucially, the review also found a new pointwise charging bound that removed substantial upper-range computation from the logical proof chain. See the [blind external red-team follow-up](project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md), [reviewer-v4 proof](project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md), [reviewer-v4 release package](releases/n29-reviewer-v4/README.md), and [cross-order analytic caps](project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md).

A separate proof-text audit found a **non-blocking sign/order typo** in an intermediate explanatory sentence of the expanded threshold-capacity lemma. The corrected sign is exactly the direction needed for the already-used final inequality, so no numerical result or candidate status changed. The historical lemma records the correction rather than erasing it.

Later on 11 September, summing threshold capacity over residual-degree tails produced a stronger demand-only inequality. A hand clipping argument gives `Q(s)<=18`, while the bridge gives `Q(s)>=16+2t` for `Delta=16`, hence `t<=1`. This closes the `n=29, Delta=16, m>=210` branch without proof-critical computation. The corrected minimal-kernel/Farkas route remains frozen as independent corroboration and audit history rather than being discarded.

### Robustness milestone — Fan dependency removed after hostile challenge

A later external-AI critique raised three concrete objections: two possible collision/double-counting issues in the selected/residual construction, and the fact that the fixed-order papers then in scope used G. Fan's 1987 upper-density theorem to cap the edge search. The two local semantic objections did **not** survive re-audit: selection is one representative per missing **unordered** `B`-pair, and the forced cross-edges in the residual injection cannot themselves be selected because their endpoints miss an `A`-vertex. The current editions state those points explicitly. See the [cross-cutting feedback audit](project/reviews/cross-cutting/2026-09-09-external-ai-feedback-audit-v1/REPORT.md).

For the Fan point, the project deliberately went further than defending the citation. It constructed direct order-specific upper-range reductions for the five fixed-order candidates then in scope, `n=25,27,28,29,30`, so Fan's theorem became **historical attribution only**, not a logical dependency of those proofs. Every historical reviewer/proof source was retained unchanged. The replacement is documented in [`FAN_FREE_REDUCTION.md`](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md), with later analytic simplifications in [`POINTWISE_CAPS.md`](project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md).

The assembled replacement passed a fresh [hostile coverage/integrity audit](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md): required upper edge ranges were complete, every proof-event checkpoint had zero survivors under exact acceptance, reviewer surfaces contained no residual logical invocation of Fan, and frozen historical source hashes still matched their recorded provenance. This is internal robustness evidence, not external acceptance; graph-to-residual lemmas and short hand monotonicity arguments remain important review targets.

### Other fixed-order and general hostile audits retained

| Scope | Adversarial audit outcome and resulting hardening |
|---|---|
| `n=25` | The [8 September re-audit](project/reviews/n25/2026-09-08-reaudit-v1/README.md) replayed the complete finite domain in 16 disjoint clean-runner shards: 543,578 outer states, 3,442,212 labelled columns and 1,959 independently reconstructed final equality certificates. No blocking mathematical defect was found; terminal reconstruction was made more independent of the frozen verifier. |
| `n=27` | The [8 September red-team audit](project/reviews/n27/2026-09-08-redteam-v1/REPORT.md) hardened a replay covering 80,978,546 canonical columns and independently reconstructed all 35,435 terminal source-cap vectors. It found a raw C++ negative-token input-acceptance weakness and an initial audit-comparator gzip-timestamp mismatch; both were explicitly guarded/corrected without changing the mathematical candidate. |
| `n=28` | The [7 September red-team report](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md) added fresh replays, independent certificate checks and graph tests. No blocking defect was found in the direct candidate route. A non-blocking standalone-helper input-validation defect was recorded and guarded rather than hidden. |
| `n=30` | The [hostile assembly audit](project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md) attacked the stitching of the exact degree regimes and certificate branches. Later Fan-free/analytic hardening reduced several historically computational upper-range scopes while retaining the assembly evidence. |
| General `7/12` | The [hostile audit](project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md) used separately structured exact checkers against the scalar arithmetic, finite degree-assembly exceptions and threshold certificates. Large finite regressions are treated as consistency checks, not extrapolative proof; the shared graph-to-demand/profile-integral lemmas remain the central review target. |

### Preservation rule for adversarial findings

A hostile audit can strengthen confidence, weaken a claim, expose a defect, or force a different proof route. All four outcomes are useful evidence. Findings that invalidate evidence must stay visible as invalidated; superseded computations remain available as corroboration/history; failed audits, counterexamples and reviewer-triggered proof changes are not to be removed merely because a later route is cleaner. The automated README guard enforces the presence of this section and its core links, but the standing order is broader: substantive historical content elsewhere in the README must also be preserved unless the user explicitly requests removal or compression.
<!-- REDTEAM-HISTORY:END -->

## Current research chain

Specific graph orders and explicitly defined relaxed profiles are laboratories for structural principles, not substitutes for an all-order proof. The [canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md) translates a hypothetical graph into selected quasi-edge representatives, residual incidences, label demands, missing-pair loads and incoming capacities.

- [Shared block slack](project/research/general_n/2026-09-14-joint-blocks-v1/README.md): one shared low-block slack budget; original707/713 and fresh708/715 at that checkpoint.
- [Source-priced selected incidence](project/research/general_n/2026-09-14-source-sharing-v1/README.md): exact source-row dualization; restored replay34905883642 passed while the earlier failure remains preserved.
- [Stronger source-price search / witnesses](project/research/general_n/2026-09-14-source-pricing-witnesses-v1/README.md): 21/24 tested bounds improve; uncoupled witnesses for original160,338,347 show why stronger destination/residual correlation is needed. This package supplies the local destination-coupling inequalities used by the singleton theorem.
- [Conditioned source pricing](project/research/general_n/2026-09-14-conditioned-source-pricing-v1/README.md): exact branch totals and legitimate caps. Its row471 rigidity successor closes `e_L=39,40`; run34906169745 passed the exact scan and rigidity verifier.
- [Row471 `e_L=41` high-block closure](project/research/general_n/2026-09-15-row471-e41-v1/README.md): receiver pressure plus one common high-excess budget forces at least28 high selections from positive-pressure sources, but positive-excess high labels can carry at most24.
- [Row471 `e_L=42,43` common-pressure split](project/research/general_n/2026-09-15-row471-e42-e43-common-pressure-v1/README.md): exact `rho=2` symmetry DP plus exact nested-high-excess DP gives source-group charge uppers `214,215<222`; remote run34909572352 passed. These branch results remain independent corroboration.
- [Singleton destination / arc-slot Hall theorem](project/research/general_n/2026-09-15-singleton-destination-trap-v1/README.md): a `(q,rho)=(1,1)` source can only point to `q<=1`; unordered-pair Hall deficiency excludes whole original profiles347,471,586. A broader cardinality-compatible pair-slot flow independently rejects the same three and retains160,338.
- [Forced-core receiver-capacity partition](project/research/general_n/2026-09-15-forced-core-capacity-v1/README.md): low eligibility makes the selected sets of ten `rho=1` sources identical in rows160 and338; exact labelled-routing receiver capacities cannot be partitioned across the forced labels, closing the original synthetic sample at713/713.
- [Fresh forced-core/high-demand squeeze](project/research/general_n/2026-09-15-fresh-forced-core-high-squeeze-v1/README.md): six fresh survivors fail total receiver capacity; the seventh forces all candidate receivers used and then violates high-label selected demand `43<45`, closing the fresh sample at715/715.
- [Canonical forced-core discovery scan](project/research/general_n/2026-09-15-forced-core-canonical-scan-v1/README.md): exact arbitrary-`r` theorem inserted into the promoted relational `q` enumeration; run34950746007 completed all 306 resumed targets with 170 candidate closures and 136 survivors. Discovery only; canonical frontier unchanged.
- [Canonical forced-core audit checkpoint](project/research/general_n/2026-09-15-forced-core-canonical-audit-v1/README.md): 124 certified replacement witnesses all reappear in the completed exhaustive survivor set; the independent type-multiplicity implementation's first 24 exclusions are contained in the final 170 and reconcile with the final primary counts.
- [Canonical forced-core full independent audit](project/research/general_n/2026-09-15-forced-core-canonical-full-audit-v1/README.md): exact 170 candidate and 136 survivor sets frozen; full 170-state type-multiplicity replay installed with field-by-field stage-count and exact-key aggregate gates. Initial run34985326400 failed before any mathematical audit stage because the historical artifact was not resolved by name; pinned-ID REST download is the repaired transport. No canonical promotion implied.
- [Conditioned source sharing / row108](project/research/general_n/2026-09-14-conditioned-source-sharing-v1/README.md): exact row/type incidence plus one common source pressure excludes row108 in the stated relaxation; remote replay34906766833 succeeded.

For row108, one fixed signed price vector closes24 of the32 block-total tuples surviving the older multiblock screen. The remaining eight require unit charge at least211. Exact row/type flow reduces46,662 excess histograms to1,201 feasible histograms;1,124 already have exact incidence-charge upper below211, and exact common-pressure branch-and-bound eliminates the remaining77. Complete verifier output canonical parsed-JSON SHA256: `5ea860b79516d9a34e73a67fafdb7875cd3c9c99b01594b4bf3aab2c3e8a7629`.

## Failures and audit gates remain first-class evidence

Do not quietly delete, relabel or retrospectively clean up a failed lemma, non-closing experiment, counterexample or CI event. The454/597 simultaneous-multiblock non-rejection remains a negative predecessor result. Source-price run34904353492 remains failed even though the exact restoration replay later succeeded. N30 run34906766832 remains failed because an earlier condensed README omitted explicit frozen PDF navigation; restoring the links does not repaint that run green. Red-team-history guard run34908428824 remains failed because the start-here link was outside the protected block; the later repair does not repaint it green. Standalone row471 research-note commit `2667a909...` violated the paired-status publication order; later checkpoints correct the live surfaces but do not rewrite that predecessor as compliant. Full forced-core independent-audit run34985326400 remains failed because its first cross-run artifact name lookup returned “Artifact not found”; reconciliation and audit jobs did not run, and the later pinned-ID transport repair does not repaint it green. The branch-specific charge route did not itself finish row471; the later destination theorem is a distinct stronger structural route. Synthetic-sample exclusions do not change the canonical finite frontier by themselves.

The 2,655 recovered relational candidates completed full discovery and two-implementation audit, then the separate reviewed ledger step. All 2,655 are now ledger-promoted with pinned hashes and zero unresolved states. This finite closure family remains conditional on the canonical bridge and does not replace external specialist review.

<!-- REVIEW-MATERIALS:START -->
## Papers and review materials

This reviewer-facing navigation surface is protected. Detailed canonical status remains [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md); new editions must update both surfaces rather than deleting this section.

**Reviewer entry:** start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md), then use the package index below.

### Fixed-order papers and packages

- [`n=25 reviewer-v2`](releases/n25-reviewer-v2/README.md) — [manuscript PDF](releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf).
- [`n=27 reviewer-v2`](releases/n27-reviewer-v2/README.md) — [manuscript PDF](releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf).
- [`n=28 reviewer-v2`](releases/n28-reviewer-v2/README.md) — [manuscript PDF](releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf).
- [`n=29 reviewer-v4`](releases/n29-reviewer-v4/README.md) — [manuscript PDF](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) and [verification companion PDF](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf).
- [`n=30 reviewer-v3`](releases/n30-reviewer-v3/README.md) — [manuscript PDF](releases/n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf) and [verification companion PDF](releases/n30-reviewer-v3/N30_Verification_Companion_v3.pdf).
- [`n=31 reviewer-v1`](releases/n31-reviewer-v1/README.md).
- [`n=32 reviewer-v1`](releases/n32-reviewer-v1/README.md).
- [`n=33 reviewer-v1`](releases/n33-reviewer-v1/README.md).
- [`n=34 reviewer-v2`](releases/n34-reviewer-v2/README.md).
- [`n=35 reviewer-v1`](releases/n35-reviewer-v1/README.md).

### General-theory papers and reviewer packages

- [`7/12` maximum-degree reviewer-v1](releases/general-7-12-reviewer-v1/README.md).
- [`13/22` retained maximum-degree reviewer-v1](releases/general-13-22-reviewer-v1/README.md).
- [`293/500` retained maximum-degree reviewer-v1](releases/general-293-500-reviewer-v1/README.md).
- [General step-back structural package](releases/general-stepback-v1/README.md).
- [Joint-clipping reviewer-v1](releases/general-joint-clipping-reviewer-v1/README.md).
- [Heavy-load / routing reviewer-v1](releases/general-heavy-load-reviewer-v1/README.md).
- [Joint heavy routing](releases/general-joint-routing-reviewer-v1/README.md).
- [Demand/tail projection reviewer-v1](releases/general-routing-tail-reviewer-v1/README.md).
- [Compatible-destination routing reviewer-v1](releases/general-compatible-routing-reviewer-v1/README.md).
- [Compatible-routing full-catalogue reviewer-v1](releases/general-compatible-catalogue-reviewer-v1/README.md).
- [Closed-compatible-potential reviewer-v1](releases/general-closed-compatible-reviewer-v1/README.md).
- [Fixed-neighbourhood / arc-realisation reviewer-v1](releases/general-arc-realisation-reviewer-v1/README.md).
<!-- REVIEW-MATERIALS:END -->

## Trust boundary

Hand derivation, same-assistant verification, remote CI, durable preservation and external acceptance are distinct. No timeout, missing output, unsuccessful search or floating infeasibility is proof. The canonical selected/residual bridge remains the principal correlated external-review dependency.
