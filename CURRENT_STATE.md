# Murty–Simon / Erdős #742 — current state handoff

<!-- CURRENT-STATUS:START -->
<!-- SOURCE-PRICE-PUBLICATION:START -->
**Publication verification — 2026-09-14 22:48:27 UTC; run 34905883642.** The original source-price result file is restored to its pre-existing SHA256 `1953c61d26c68dc2bcbb9aeddbe0d18336e05b118541f4d9ca3f9528c808caae`. The UNCHANGED offline harness passed all source/input hashes, the canonical twelve-row input, the six-row transcription, 9,043 incidence/demand checks, 371 brute-force comparisons, three hostile/boundary fixtures and complete output equality for all 576 price evaluations. The failed run 34904353492 remains recorded. **Mathematical status unchanged: zero new profile exclusions.** This receipt covers the original source-sharing package, NOT the separate stronger price/witness package. Validated checkout: `e6c9915826173b7b4ab8f76dc9b944b710128b0b`; this atomic commit publishes the repaired data and paired status receipt. See [repair audit](project/research/general_n/2026-09-14-source-sharing-v1/CI_AUDIT.md).
<!-- SOURCE-PRICE-PUBLICATION:END -->

**14 September 2026 — research checkpoint `row471-rigidity-v1`.** Inspected predecessor: `aa6c41fcede3bf2e7e935a00840030ef0b9ee1df`. Two conditioned branches of original synthetic row471 are now hand-closed. At eta2,e_L39 the receiver/source-price squeeze forces pressures `d_9>=4,d_23>=4,d_13>=2`; the twelve demand-three labels then need at least12 high excess although only8 is available. At e_L40 it forces `d_9>=4,d_23>=3,d_13>=2`, requiring at least10 high excess with only7 available. Exact integer recheck is in [ROW471_RIGIDITY.md](project/research/general_n/2026-09-14-conditioned-source-pricing-v1/ROW471_RIGIDITY.md) and `verify_row471_rigidity.py`. **This closes branches 39 and40, not the row471 profile. Original sample remains707/713; fixed-order, general7/12 and canonical-frontier status are unchanged.**

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Every commit must update CURRENT-STATUS blocks in BOTH README.md and this file atomically. Read [CANONICAL_REPOSITORY.md](CANONICAL_REPOSITORY.md), [AGENTS.md](AGENTS.md), [RESEARCH_EVIDENCE_INDEX.md](RESEARCH_EVIDENCE_INDEX.md), and newer commits before continuing.

## Canonical status — unchanged

```text
whole-state closures:             977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered relational candidates: 2,655 — UNPROMOTED
```

Fixed-order n25/n27-through-n35 and general7/12 candidates remain preserved; external mathematical review, novelty assessment and third-party reproduction OPEN. No unrestricted proof or newly realized graph is claimed.

The [shared-slack](project/research/general_n/2026-09-14-joint-blocks-v1/README.md) sample remains original707/713 rejected, leaving108,160,338,347,471,586; fresh708/715 rejected, leaving20,91,391,490,528,562,677 in a distinct namespace. These are synthetic profiles, not remaining cases of the conjecture. The simultaneous multiblock experiment left454/597 tuples across all six originals; no extra closure.

## Three source-price scopes plus row471 rigidity

The [original package](project/research/general_n/2026-09-14-source-sharing-v1/README.md) retains its elementary exact-row pricing proof, deterministic576-price experiment and finite checks:9,043 incidence/demand configurations,371 brute-force DP comparisons and three hostile fixtures. Four weighted bounds improve against the same zero-price baseline, but none excludes a profile. All unit-weight trials retain zero. The transferred extra-zero error and its exact restoration are documented separately; restored full replay34905883642 passed without weakening the original expected hash.

The [stronger search / joint-witness package](project/research/general_n/2026-09-14-source-pricing-witnesses-v1/README.md) attains21 improvements in24 frozen comparisons, with no contradiction. Exact incidence/orientation witnesses for original160,338,347 establish feasibility only of the LISTED uncoupled model; they do not assign labels to arcs or construct graph residual neighbourhoods. The particular witnesses violate stronger pair/common-residual conditions, so they are not graph realizations and do not exclude or realize the profiles generally.

The [conditioned continuation](project/research/general_n/2026-09-14-conditioned-source-pricing-v1/README.md) uses the SAME exact low-block excess and branch-specific legitimate caps as the conditioned/shared-slack route. Recorded audit:9,293 incidence configurations,24,063 priced inequalities,150 strict improvements over zero prices. Inherited branch rejections are applied first, then every remaining branch at the targeted eta is priced for all six originals and all seven fresh profiles separately. Its exact remote replay **34905354792 completed SUCCESS** on checkpoint7504cfa5, matching the frozen full-output SHA256 `1aec5dc47102ec24f64cc9776c624b32d025112b06fb643f306a0768e091639a` and the headline row471 near-miss values.

That conditioned scan retained row471 eta2 branches `39,40,41,42,43,47`. The new [row471 rigidity argument](project/research/general_n/2026-09-14-conditioned-source-pricing-v1/ROW471_RIGIDITY.md) now removes39 and40 by combining the SAME source-price upper with the receiver pressure minimum and positive-label endpoint forcing. The remaining conditioned branches are therefore

```text
41,42,43,47.
```

The new verifier is self-contained integer arithmetic and is added to the conditioned workflow. A fresh remote run including this verifier is required before remote verification of the new branch closures is claimed.

## Immediate next target: row471 e_L=41 and destination-label coupling

Prioritize eta2,e_L41, then42,43,47. The simple near-equality pressure argument that closed39/40 no longer forces the same three sources once the source-price gap widens, so do not extend it by wishful analogy. Retain ONE selected-incidence matrix with exact row/column sums and impose destination compatibility plus one common residual neighbourhood. Seek a Hall/saturation or forced-incidence contradiction suitable for a reusable hand lemma. For canonical arc u->w and selected sets S_u,S_w, retain

```text
1 <= |S_u minus S_w| <= rho_w+1,
|S_w minus S_u| <= rho_u,
| (union_{w:u->w} S_w) minus S_u | <= rho_u.
```

Enforce these over ALL allowed realizations, not just existing witnesses. Keep full branch coverage and separate row namespaces. Retain multiresource shared slack, exact q-layer/mincut, crossing-wall/saturation and maximum-cut/stability alternatives.

## Verification history and corrections

Shared-slack run34898768799/job104159335270 on `de4cdce81db75301b622874fdfe6f5c792e89b7a` passed and complete downloaded outputs matched. Conditioned-source-pricing run34905354792 on7504cfa5 completed SUCCESS. Original source-price34904353492/job104177437867 FAILED before mathematics at the transferred result hash; the later diagnosis identified an extra vector entry rather than mere formatting. The original raw expected hash stayed authoritative, and restored replay34905883642 passed the unchanged full harness. The failed run remains a failure in history. [CI_AUDIT.md](project/research/general_n/2026-09-14-source-sharing-v1/CI_AUDIT.md) preserves the exact diagnosis and hashes.

The q-layer normal-form strategy correction remains: all subsets passing means Hall feasibility; exclusion requires a deficient subset. Its equations1–15 and recorded finite checks are unchanged; the old note is preserved byte-for-byte. No all-profile contradiction follows merely from that correction.
<!-- CURRENT-STATUS:END -->

## Preservation, dependencies and audit gates

The [shared-slack README archive](README_SHARED_SLACK_DETAILS_2026-09-14.md), [handoff archive](CURRENT_STATE_PRE_COMMIT_STATUS_2026-09-14.md), all subsequent checkpoints in Git history and all reviewer packages remain retained. The full failure-retention policy and reviewer-first invitation remain in the README. Read the [canonical bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md), [shared-slack proof](project/research/general_n/2026-09-14-joint-blocks-v1/README.md) and [offline guide](project/research/general_n/2026-09-14-joint-blocks-v1/REPRODUCE.md). Preserve Q=r+2t+D0+Esel; distinguish structural t, q-threshold tau and block eta. Zero-demand labels stay explicit. Keep legitimate caps, positive-label forcing d_u=(p_u-rho_u+1)_+<=e_i and y<=p for actual-tail receivers. Relaxed incidence/pressure feasibility is not graph realizability.

The2,655 candidates require complete coverage, dual agreement, zero unresolved states, successful aggregate and a separate reviewed ledger step. Keep N34/N35 provenance and closure validator. No live audit shard count is asserted. Fetch EVERY page or a complete diagnostic before reporting audit34854911792. Do not duplicate it, change budgets/concurrency or retry queued/running/successful jobs or computational timeouts; the existing narrow transient-infrastructure retry rule remains.

All16 earlier raw/derived evidence files are preserved at `b6a15db114d7b4f3b71d73da816daec563f11824`. Publication-only34895776658 succeeded; earlier34894544147 passed math/hash steps but failed Git rebase. Preserve both records and [publication audit](project/research/general_n/2026-09-14-evidence-preservation-v1/PUBLICATION_AUDIT.md). Internal checks, remote CI and preservation are distinct from external specialist acceptance of the graph-to-selected/residual bridge.
