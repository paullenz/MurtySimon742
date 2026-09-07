# Murty–Simon / Erdős Problem #742

**Candidate proofs at n=25, n=27 and n=28; active general-order research.**

**Status updated: 7 September 2026. Independent mathematical review remains OPEN.** The new [direct197 v8 route](project/research/general_n/2026-09-07-direct-197-v8/README.md) excludes every freshly generated numerical state for **(n,Delta,m)=(28,15,197)**. Other maximum degrees at 197 are ruled out explicitly; Fan's strict 197.2075 bound rules out 198 or more edges. Combined with the separately preserved complete 196-edge equality route, this gives a complete **candidate** order-28 chain: **at most 196 edges, with equality only K(14,14)**.

This is not independent acceptance, formal verification or a solution of the general conjecture. A candidate mathematical argument, exact arithmetic reproduction, binary-evidence availability and independent expert review are distinct status questions.

## Current position

| Workstream | Candidate result | Outstanding review or preservation |
|---|---|---|
| n=25 | At most 156 edges; equality only K(12,13) | Independent mathematical review and external reproduction OPEN |
| n=27 | At most 182 edges; equality only K(13,14) | Independent review and external reproduction OPEN |
| n=28, direct v8 | All 197-edge maximum degrees excluded; prior 196-edge equality chain gives K(14,14) | Independent review; complete v6/v7/v8 binary attachment remains separately tracked |
| n=28, degree-load v7 | Alternative complete candidate using a weak-core density reduction | Independent review, especially core scope; its own audit ZIP attachment |
| General order | Candidate high-degree result and coupled degree/label/activation constraints | Middle-degree region open; no all-order proof or improved v8 coefficient |

The frozen n=25/n=27 editions and governed theorem ledger are unchanged.

## Direct order-28 route: start here

Read the [direct197 summary](project/research/general_n/2026-09-07-direct-197-v8/DIRECT_197_SUMMARY.md), [exact results](project/research/general_n/2026-09-07-direct-197-v8/RESULTS.json), [complete direct checking report](project/research/general_n/2026-09-07-direct-197-v8/EXACT_CHECK_REPORT.json), and [fresh-copy replay report](project/research/general_n/2026-09-07-direct-197-v8/FULL_REPLAY_REPORT.json).

The input domain is generated at **t=2**, not copied from the 196-edge/t=1 survivor list. There are **12,012 charging demand tuples**, of which 1,229 retained intervals expand to **8,216,928 residual rows**. The successive exact row, projected and joint-column screens leave 5,154, 2,959 and 1,584 rows. Final shared, source-degree-type and endpoint-type models exclude **787+790+7**, leaving **zero**. Every final rejection has an exact integer certificate reconstructed separately. No integer branching or optimisation status alone is counted as proof.

The Delta=16 case at 197 also has a short hand contradiction: the charging sum must be at least 26, but 11 labels supply at most 176/7. The h-index bound excludes Delta=17 through 26, degree sum excludes Delta<=14, and Delta=27 forces a star. Thus the new direct route covers every maximum degree at 197 without a weak-core reduction or deletion-preserves-criticality assumption. Full mathematics, code, exact input/output files and replay instructions are in the original v8 archive pinned in its directory guide.

The complete original v6 and LocalIncidence-v7 separate checking routes were rerun in fresh copies. V6 again leaves 388 equality-level rows; LocalIncidence v7 again excludes them in a **22/19/347** partition. The original v3 n28/Delta=16 equality scope also rechecked all 39 demand tuples and 604 residual rows. This session does not assert a fresh full replay of every earlier v3/v4/v5 equality-level stage; their complete-domain and structural arguments remain explicit dependencies.

## Two different v7 workstreams

**LocalIncidence v7** originally closed only the 196-edge branch. The new direct197 v8 result supplies its previously missing density scope. The separate [degree-load-v7 candidate](project/research/general_n/2026-09-07-degree-load-v7/N28_CANDIDATE.md) closes the same equality frontier in a different **173/215** partition and adds a weak-core density-reduction argument. Read its [proof](project/research/general_n/2026-09-07-degree-load-v7/PROOF.md) and [core-scope audit](project/research/general_n/2026-09-07-degree-load-v7/CORE_SCOPE_AUDIT.md).

The routes share lemmas, ancestors and authorship; they are not independent researcher endorsements. The alternative 388-row exclusions must not be added together or used interchangeably as evidence for different models. V8 does not rely on the weak-core reduction: its source-local residual lemma is applied to the original 197-edge critical graph. See the [V6/V7 reconciliation](project/research/general_n/2026-09-07-v6-v7-intake/README.md).

## Evidence availability and replay

**The newest fully archived repository research checkpoint verified at intake remains [v5](project/research/general_n/2026-09-07-column-propagation-v5/README.md).** Readable summaries and exact reports are not substitutes for full binary evidence.

Paul reported uploading SharedAdjacency v6 and LocalIncidence v7. Their local originals passed all 88 and 87 payload checksums, but repository read-back did not expose the ZIPs and the v6 object reference returned HTTP 422. They have therefore **not been claimed moved or attached**. Exact names, hashes and intended destinations are in the [intake record](project/research/general_n/2026-09-07-v6-v7-intake/README.md). The separate degree-load-v7 **21,975,757-byte audit bundle** is still independently identified as pending by its [publication-scope record](project/research/general_n/2026-09-07-degree-load-v7/PUBLICATION_SCOPE.json).

The new **MurtySimon_N28_197_Direct_v8.zip** is supplied in the research chat: **5,677,524 bytes**, SHA-256 `b753076ffc755066a0c57756be91cc5b265c163d869244d3aa65e3943799347b`, containing 90 payload files plus the manifest. This README update publishes its summary and reports, **not that binary ZIP**. Its full direct197 replay is self-contained once extracted; no earlier ZIP is needed for that new calculation.

From the extracted v8 package, `python3 -I -B replay.py --verify-only` checks integrity only. `python3 -I -B replay.py --check --output /absolute/new/path` performs the complete fresh direct197 checking route. Checking uses Python's standard library and a C++17 compiler with Boost headers, no optimisation solver or network. Both the clean replay and the final ZIP/member checks passed. The directory guide distinguishes the tested checking wrapper from optional rediscovery.

## Frozen n=25 and n=27 review entry points

For n=25, start with the [reviewer manuscript](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf), [review guide](releases/n25-reviewer-v1/REVIEW_GUIDE.md), [frozen proof](project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md), [exact results](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RESULTS.md), and [reviewer package](releases/n25-reviewer-v1/README.md). The candidate includes degree 13 witness counting, degree 14/15/16 residual arguments, the published Delta>=17 reduction, and 1,959 checked final equality-column certificates. See the [reconciliation](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RECONCILIATION.md), [literature note](releases/n25-reviewer-v1/LITERATURE_AND_ATTRIBUTION.md), and [internal red-team report](project/reviews/n25/2026-09-06-redteam-v1/N25_Red_Team_Report_2026-09-06.md).

For n=27, the [candidate proof](project/reviews/n27/2026-09-07-candidate-v1/README.md) proposes 182 edges with equality only K(13,14). Its [complete evidence package](releases/n27-candidate-v1/README.md) provides the numerical route and replay instructions.

The [external review register](releases/n25-reviewer-v1/REVIEW_REGISTER.json) remains OPEN. Paul [reported sending a review invitation to Dr Florent Foucaud](project/reviews/n25/outreach/2026-09-07-foucaud-sent-user-report.md); no completed external assessment is asserted.

## General-order research and limits

The [coupled-resource v2 derivation](project/research/general_n/2026-09-07-coupled-resource-v2/PROOF.md) gives the candidate implication for n>=4:

```text
Delta(G) >= ((10-sqrt(2))/14)*n  ==>  e(G) < floor(n^2/4),
(10-sqrt(2))/14 = 0.6132704598...
```

V8 does not improve that coefficient. The [h-index v1](project/research/general_n/2026-09-07-residual-hindex-v1/README.md), [pair-budgets v2](project/research/general_n/2026-09-07-pair-budgets-v2/README.md), [demand-support v3](project/research/general_n/2026-09-07-demand-support-v3/PROOF.md), [overlapping demand-stability v3](project/research/general_n/2026-09-07-demand-stability-v3/README.md), [label-tail v4](project/research/general_n/2026-09-07-label-tail-v4/README.md), and [column-propagation v5](project/research/general_n/2026-09-07-column-propagation-v5/README.md) remain unchanged. V3's (30,17) and (33,19) degree-case exclusions do not complete those orders. Historical frontiers are retained, not rewritten. Infinite excluded profile families are not whole-order theorems.

**No complete order above 28, proof through n=1,000, full general conjecture, priority determination, independent endorsement or formal-kernel verification is claimed.** Actual-graph samples contain no positive-surplus example. Universal correctness rests on the structural proofs and full finite-domain coverage, not those samples or floating-point solver statuses.

## Governance and preservation

The [README preceding this direct197 update](project/reviews/history/README_before_direct197_v8_2026-09-07.md) is retained verbatim, alongside earlier historical versions. Historical Delta=15, Audit v5 and legacy SAT/reproduction obligations are not retrospectively certified by replacement routes.

- [Project standing orders](project/N25_PROJECT_STANDING_ORDERS.md)
- [Repository synchronization and commit-completion policy](project/REPO_SYNC_POLICY.md)
- [Canonical n25 review](project/CANONICAL_N25_REVIEW_2026-09-06.md)
- [Governed theorem ledger](repro-v1/ledger/theorem_ledger.json)
- [Historical task backlog](project/CANONICAL_TASKS.json)
- [Evidence-recovery manifest](project/EVIDENCE_RECOVERY_MANIFEST.json)

Preserve code, exact data, provenance, corrections and review reports. Branch attachment and read-back are required before a commit is called complete. Documentation publication, binary publication and mathematical certification remain separate.
