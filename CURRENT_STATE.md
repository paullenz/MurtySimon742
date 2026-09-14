# Murty–Simon / Erdős #742 — current state handoff

<!-- CURRENT-STATUS:START -->
<!-- SOURCE-PRICE-PUBLICATION:START -->
**Maintenance checkpoint — 14 September 2026, `source-price-publication-repair-v1`.** Inspected predecessor: `7504cfa5f9899b9e2b088fc07142e4445ca049bc`. This preserves all newer conditioned-price and joint-witness research. The original replay failure was an extra zero in row338's price vector, NOT merely JSON formatting. This commit restores the original byte-hash replay harness and installs deterministic restoration of that exact data error. The original full expected hash and unchanged full replay must pass before corrected raw JSON and BOTH status receipts are atomically published without force. Local diagnosis, restoration and full six-profile replay passed. **Remote restoration is not yet claimed complete. Mathematical status unchanged; no new profile closure.** See [repair audit](project/research/general_n/2026-09-14-source-sharing-v1/CI_AUDIT.md). The next mathematical target remains row471 and selected-label/destination/common-residual-neighbourhood coupling.
<!-- SOURCE-PRICE-PUBLICATION:END -->

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Every commit must update CURRENT-STATUS blocks in BOTH README.md and this file atomically, including an explicit unchanged-mathematics statement for maintenance. Read [CANONICAL_REPOSITORY.md](CANONICAL_REPOSITORY.md), [AGENTS.md](AGENTS.md), [RESEARCH_EVIDENCE_INDEX.md](RESEARCH_EVIDENCE_INDEX.md), and newer commits before continuing. The research checkpoint retained below is `7504cfa5f9899b9e2b088fc07142e4445ca049bc`.

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

## Three separate source-price scopes

The [original package](project/research/general_n/2026-09-14-source-sharing-v1/README.md) retains its elementary exact-row pricing proof, deterministic 576-price experiment and finite checks:9,043 incidence/demand configurations,371 brute-force DP comparisons and three hostile fixtures. Four weighted bounds improve against the same zero-price baseline, but none excludes a profile. All unit-weight trials retain zero. Complete non-improving traces are retained; the transferred extra-zero error and its exact restoration are documented separately, without changing any expected mathematical hash. Zero/uncharged columns, signed scores, exact cardinality and row restoration are essential.

The [stronger search / joint-witness package](project/research/general_n/2026-09-14-source-pricing-witnesses-v1/README.md) attains21 improvements in24 frozen comparisons, with no contradiction. Exact incidence/orientation witnesses for original160,338,347 establish feasibility only of the LISTED uncoupled model; they do not assign labels to arcs or construct graph residual neighbourhoods. Their81,101,129 arcs/incidences pass the package's integer checker, but the PARTICULAR witnesses violate stronger pair conditions58,71,95 times and common residual-union limits8,8,15 times. Row338 source4 would need15 residual labels with rho3. This is not an exclusion of all realizations of any profile. Original108/471 timeouts and586 numerical infeasibility remain non-certificates. Its distinct local scope includes9,043 incidence/gauge cases,626 column enumerations,1,000 valid lower-bound checks,24 frozen bound replays and18 rejected witness corruptions. The original workflow does not verify it.

The [conditioned continuation](project/research/general_n/2026-09-14-conditioned-source-pricing-v1/README.md) uses the SAME exact low-block excess and branch-specific legitimate caps as the conditioned/shared-slack route. Recorded local audit:9,293 incidence configurations,24,063 priced inequalities,150 strict improvements over zero prices. Inherited branch rejections are applied first, then every remaining branch at the targeted eta is priced for all six originals and all seven fresh profiles, separately. **No new profile exclusion.** Full frozen output SHA256: `1aec5dc47102ec24f64cc9776c624b32d025112b06fb643f306a0768e091639a`.

Original row471 at eta2: e_L39 improves upper232 to225 against lower224, gap-1; e_L40 improves230 to225 against lower223, gap-2. Best integer prices put1 at source indices9 and23 and0 elsewhere. Fresh391 gains4,3,2,1 on its four branches; fresh528 gains1 on one branch, without contradiction. Other tested branches retain zero as best in the finite search, not a certificate of global price optimality. No new live remote conclusion for the conditioned workflow is asserted in this maintenance checkpoint.

## Immediate next target: row471 and destination-label coupling

Prioritize eta2,e_L39/40 with ONE selected-incidence matrix, exact row/column sums, destination compatibility and one common residual neighbourhood. Seek a Hall/saturation or forced-incidence contradiction suitable for a hand lemma, rather than broad blind price search. Original338 equality/rigidity remains interesting, but its uncoupled witness warns that incidence/orientation constraints alone are insufficient. For canonical arc u->w and selected sets S_u,S_w, retain

```text
1 <= |S_u minus S_w| <= rho_w+1,
|S_w minus S_u| <= rho_u,
| (union_{w:u->w} S_w) minus S_u | <= rho_u.
```

Enforce these over ALL allowed realizations, not just existing witnesses. Keep full branch coverage and separate row namespaces. Retain multiresource shared slack, exact q-layer/mincut, crossing-wall/saturation and maximum-cut/stability alternatives.

## Verification history and corrections

Shared-slack run34898768799/job104159335270 on `de4cdce81db75301b622874fdfe6f5c792e89b7a` passed and complete downloaded outputs matched. On788819f8, status34904353538, reviewer-navigation34904353444, N30 package34904353499 and all q-layer34904353463 job steps passed. Original source-price34904353492/job104177437867 FAILED before mathematics at the transferred result hash. The diagnosis in7504cfa5 that the mismatch was merely formatting is superseded: the additional vector entry changed data. The original raw expected hash remains authoritative. The guarded restoration receipt above distinguishes later success from this retained failure; [CI_AUDIT.md](project/research/general_n/2026-09-14-source-sharing-v1/CI_AUDIT.md) preserves exact hashes and diagnosis.

The q-layer normal-form strategy correction remains: all subsets passing means Hall feasibility; exclusion requires a deficient subset. Its equations1–15 and recorded finite checks are unchanged; the old note is preserved byte-for-byte. No all-profile contradiction follows merely from that correction.
<!-- CURRENT-STATUS:END -->

## Preservation, dependencies and audit gates

The [shared-slack README archive](README_SHARED_SLACK_DETAILS_2026-09-14.md), [handoff archive](CURRENT_STATE_PRE_COMMIT_STATUS_2026-09-14.md), all subsequent checkpoints in Git history and all reviewer packages remain retained. The full failure-retention policy and reviewer-first invitation remain in the README. Read the [canonical bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md), [shared-slack proof](project/research/general_n/2026-09-14-joint-blocks-v1/README.md) and [offline guide](project/research/general_n/2026-09-14-joint-blocks-v1/REPRODUCE.md). Preserve Q=r+2t+D0+Esel; distinguish structural t, q-threshold tau and block eta. Zero-demand labels stay explicit. Keep legitimate caps, positive-label forcing d_u=(p_u-rho_u+1)_+<=e_i and y<=p for actual-tail receivers. Relaxed incidence/pressure feasibility is not graph realizability.

The2,655 candidates require complete coverage, dual agreement, zero unresolved states, successful aggregate and a separate reviewed ledger step. Keep N34/N35 provenance and closure validator. No live audit shard count is asserted. Fetch EVERY page or a complete diagnostic before reporting audit34854911792. Do not duplicate it, change budgets/concurrency or retry queued/running/successful jobs or computational timeouts; the existing narrow transient-infrastructure retry rule remains.

All16 earlier raw/derived evidence files are preserved at `b6a15db114d7b4f3b71d73da816daec563f11824`. Publication-only34895776658 succeeded; earlier34894544147 passed math/hash steps but failed Git rebase. Preserve both records and [publication audit](project/research/general_n/2026-09-14-evidence-preservation-v1/PUBLICATION_AUDIT.md). Internal checks, remote CI and preservation are distinct from external specialist acceptance of the graph-to-selected/residual bridge.
