# Murty–Simon / Erdős #742 — current state handoff

<!-- CURRENT-STATUS:START -->
**14 September 2026 — checkpoint `conditioned-source-pricing-v1`.** Inspected predecessor: `b2110c7e4c96483bc2aa9931777f9aac9956dcdd`. This commit preserves both preceding source-price packages and their negative/witness evidence, adds the planned same-block conditioned source-price scan, tests the seven fresh shared-slack non-rejections separately, and repairs the original source-price replay's format-sensitive JSON hash check. Both live status surfaces are updated atomically. **Fixed-order, general 7/12 and canonical-frontier mathematical status unchanged; no new profile closure.**

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Every commit must update the CURRENT-STATUS blocks in BOTH this file and README.md atomically. Read [CANONICAL_REPOSITORY.md](CANONICAL_REPOSITORY.md), [AGENTS.md](AGENTS.md), [RESEARCH_EVIDENCE_INDEX.md](RESEARCH_EVIDENCE_INDEX.md), and commits newer than this predecessor before continuing.

## Canonical status — unchanged

```text
whole-state closures:             977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered relational candidates: 2,655 — UNPROMOTED
```

Fixed-order n25/n27-through-n35 and general7/12 candidates remain preserved with external mathematical review, novelty assessment and third-party reproduction OPEN. No unrestricted proof or newly realized graph is claimed.

The [shared block-slack pressure](project/research/general_n/2026-09-14-joint-blocks-v1/README.md) sample results remain: original707/713 rejected, leaving108,160,338,347,471,586; fresh708/715 rejected, leaving20,91,391,490,528,562,677 in its separate namespace. These are synthetic profiles, not remaining cases of the conjecture. The simultaneous multiblock extension left454/597 tuples across all six original profiles, hence no extra profile closure.

## Source-price results now preserved in three distinct scopes

The [original source-sharing package](project/research/general_n/2026-09-14-source-sharing-v1/README.md) proves the elementary exact-row source-price inequality and preserves its deterministic unconditioned six-profile experiment. Its576 finite price evaluations produced four weighted improvements but no profile closure.

The [stronger search / joint-witness package](project/research/general_n/2026-09-14-source-pricing-witnesses-v1/README.md) uses sharper receiver lower bounds and a bounded price search. Twenty-one of24 frozen comparisons improve against their same-domain zero-price baselines but none gives lower>upper. Exact joint-incidence/orientation witnesses for original160,338,347 show the explicitly listed uncoupled relaxation is feasible for those three profiles. Those PARTICULAR witnesses violate stronger selected-label/destination and shared residual-neighbourhood conditions, so they are not graph-derived realizations.

The new [conditioned source-price continuation](project/research/general_n/2026-09-14-conditioned-source-pricing-v1/README.md) couples the same row-price identity to the SAME fixed low-block excess and branch-specific legitimate caps used by the conditioned/shared-slack pipeline. Local deterministic audit checks9,293 actual selected-incidence configurations and24,063 priced inequalities;150 strictly improve on zero price. It applies inherited branch rejections first, then source-prices every remaining branch at the best targeted eta for all six original and all seven fresh boundary profiles. **No profile is newly excluded.**

The strongest new information is original row471 at eta2. For `e_L=39`, zero-price upper232 improves to225 against receiver lower224, leaving gap -1. For `e_L=40`, upper230 improves to225 against lower223, leaving gap -2. The retained best integer price puts1 on source indices9 and23 and0 elsewhere. Fresh row391 improves by4,3,2,1 across its four tested branches but remains well away from contradiction; fresh528 gains one unit on one branch. All other tested branches are zero-price optimal in this finite search. Full local output SHA256 is `1aec5dc47102ec24f64cc9776c624b32d025112b06fb643f306a0768e091639a`.

## Immediate next target: row 471 plus destination-label coupling

Do not broaden blind price search. Row471 is now a priority because exact row budgets remove nearly all of the conditioned relaxation gap and the stronger joint model did not produce an accepted witness there. Focus on eta2,e_L39/40 with ONE selected-incidence matrix, exact row/column sums, destination compatibility and the bridge's one-common-residual-neighbourhood constraint. Seek a Hall/saturation or forced-incidence contradiction that can be extracted as a hand lemma. Equality branches such as original338 remain rigidity targets, but its known uncoupled witness warns that selected-incidence/orientation constraints alone are insufficient.

For a canonical arc u->w and selected-label sets S_u,S_w, retain

```text
1 <= |S_u minus S_w| <= rho_w+1,
|S_w minus S_u| <= rho_u,
| (union_{w:u->w} S_w) minus S_u | <= rho_u.
```

The last line enforces one shared residual neighbourhood at each source. Full multiresource shared slack, exact q-layer/mincut, crossing-wall/saturation and maximum-cut/stability remain preserved alternatives.

## Verification history and explicit failure preservation

Last recorded shared-slack success is run34898768799,job104159335270,on `de4cdce81db75301b622874fdfe6f5c792e89b7a`; downloaded complete outputs were compared exactly. Status-synchronization run34902757136 passed on `8568b8c4bd631a80cd3f310644120a2ca0e323ff`.

Original source-price workflow run34904353492 on `788819f813e92d32470ff23783a9dc9faf7a4ce1` **FAILED before mathematical replay**. Job104177437867 stopped because `run_replay.py` compared `ORIGINAL_SIX_RESULTS.json` using a format-sensitive raw SHA256 and got `0705a7da14d49e81bd02f5442464b81b5796791454d5a3de8cace333bc74596c` instead of the stored serialization-independent value. This failure is not relabeled green. The repair hashes JSON canonically while retaining byte hashes for Python sources, canonical input provenance and complete parsed-object equality after rerunning both programs. A new run must be inspected before remote success is claimed.

The new conditioned-source-pricing workflow likewise checks the complete generated JSON against exact SHA256 `1aec5dc47102ec24f64cc9776c624b32d025112b06fb643f306a0768e091639a` and headline row471 values. At this checkpoint it is newly installed and **not yet claimed passed**.

The [q-layer normal-form note](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_LAYER_THRESHOLD_NORMAL_FORM.md) retains the corrected strategy paragraph: all subsets passing is Hall feasibility; excluding a profile requires some deficient subset. Equations(1)–(15) and recorded verifier counts are unchanged; the former note remains archived byte-for-byte.
<!-- CURRENT-STATUS:END -->

## Preserved details and proof dependencies

The shared-slack handoff is archived **byte-for-byte** in [CURRENT_STATE_PRE_COMMIT_STATUS_2026-09-14.md](CURRENT_STATE_PRE_COMMIT_STATUS_2026-09-14.md). Its preceding README is likewise retained in [README_SHARED_SLACK_DETAILS_2026-09-14.md](README_SHARED_SLACK_DETAILS_2026-09-14.md). Both retain the full theorem, branch tables, verification counts, hashes, unsuccessful experiments and publication history. All earlier archives and reviewer packages remain intact. Use dated observations as history, not live state. The failure-retention policy restored in commit5140548a and reviewer-first feedback invitation in e7a06e65 remain fully visible in the root README.

Read the [shared-slack proof package](project/research/general_n/2026-09-14-joint-blocks-v1/README.md), [original source-price package](project/research/general_n/2026-09-14-source-sharing-v1/README.md), [stronger price/witness package](project/research/general_n/2026-09-14-source-pricing-witnesses-v1/README.md), and [conditioned price continuation](project/research/general_n/2026-09-14-conditioned-source-pricing-v1/README.md). Keep Q=r+2t+D0+Esel; structural surplus t,q-threshold tau and demand-block threshold eta are distinct. Zero-demand labels must remain explicit. Retain legitimate caps, selected positive-label endpoint forcing d_u=(p_u-rho_u+1)_+<=e_i,and essential domination y<=p for actual-tail receiver vectors. Independent pressure/slack or source-price projections are not exact graph realizations.

## Audit and publication gates

The2,655 recovered relational candidates require complete coverage,both implementations agreeing,zero unresolved cases,successful aggregate and a separate reviewed ledger step. Preserve N34/N35 provenance and the closure-ledger validator. No fresh live shard count is asserted. Fetch EVERY job page or a newer complete diagnostic before reporting audit34854911792. Do not duplicate it,change budgets/concurrency,or retry queued/running/successful jobs or computational timeouts. A confirmed transient infrastructure failure remains subject to the existing narrowly scoped retry rule.

All16 preceding raw/derived evidence files were durably published at `b6a15db114d7b4f3b71d73da816daec563f11824`. Publication-only run34895776658 succeeded;original34894544147 passed its mathematical/hash steps but failed Git rebase. Preserve that distinction and [publication audit](project/research/general_n/2026-09-14-evidence-preservation-v1/PUBLICATION_AUDIT.md).

Internal proof checks,successful CI and durable publication do not replace external specialist review of the canonical graph-to-selected/residual bridge.
