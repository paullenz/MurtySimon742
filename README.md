# Murty–Simon / Erdős Problem #742

**Candidate proofs at n=25 and n=27; order-28 candidate and direct-scope research.**

**Status updated: 7 September 2026. Independent mathematical review remains OPEN.** The [degree-load v7 order-28 route](project/research/general_n/2026-09-07-degree-load-v7/N28_CANDIDATE.md) proposes at most **196 edges**, with equality exactly for **K(14,14)**. It combines exact 196-edge exclusions with a candidate weak-core density reduction. This is a complete candidate route, not independent acceptance or a proof of the general conjecture.

**There are two distinct v7 workstreams.** The separately prepared **LocalIncidence v7** closes the 196-edge branch through different final models, but explicitly leaves **(n,Delta,m)=(28,15,197)** open in its own route. A direct t=2 investigation is being developed to avoid relying on the weak-core scope reduction. Do not count the alternative 388-row exclusions twice or substitute one v7 evidence bundle for the other. See the [V6/V7 intake and scope reconciliation](project/research/general_n/2026-09-07-v6-v7-intake/README.md).

## Current position

| Workstream | Candidate result or recorded frontier | Outstanding obligation |
|---|---|---|
| n=25 | At most 156 edges; equality only K(12,13) | Independent mathematical review and external reproduction OPEN |
| n=27 | At most 182 edges; equality only K(13,14) | Independent review and external reproduction OPEN |
| n=28, degree-load v7 | At most 196 edges; equality only K(14,14), using the weak-core reduction | Independent review, especially density scope; complete audit ZIP attachment |
| n=28, LocalIncidence v7 | All 388 final 196-edge rows excluded in a 22/19/347 partition | Direct 197-edge domain and exclusion; full archive attachment |
| General order | Candidate high-degree result, coupled degree/label and activation constraints | Middle-degree region open; no full all-order proof or improved v7 uniform coefficient |

Frozen n25/n27 editions and the governed theorem ledger are unchanged. Mathematical validity, exact arithmetic, file availability and independent review are separate status questions.

## Evidence availability

The latest fully archived research entry verified before this intake remains [column-propagation v5](project/research/general_n/2026-09-07-column-propagation-v5/README.md). The separate degree-load v7 readable proof, scope audit and reports are committed; its **21,975,757-byte complete audit ZIP** is still identified as pending in [PUBLICATION_SCOPE.json](project/research/general_n/2026-09-07-degree-load-v7/PUBLICATION_SCOPE.json).

Paul reported uploading **SharedAdjacency v6** and **LocalIncidence v7**. Their local originals pass all **88 and 87 payload checksums** respectively. However, the repository read-back at `239eee18aa05a21e2265b8fcd34bd6553a38ef6a` did not expose those archive files, and referencing the verified v6 blob returned HTTP 422. Accordingly this README does **not** claim completed binary publication or relocation of either archive. The [intake record](project/research/general_n/2026-09-07-v6-v7-intake/README.md) pins exact names, sizes, hashes and intended destinations. They are different from the degree-load audit ZIP. No loss of GitHub permission is inferred.

## Order-28 review entry points

Read the [degree-load candidate assembly](project/research/general_n/2026-09-07-degree-load-v7/N28_CANDIDATE.md), [model and density-reduction proofs](project/research/general_n/2026-09-07-degree-load-v7/PROOF.md), [core-scope audit](project/research/general_n/2026-09-07-degree-load-v7/CORE_SCOPE_AUDIT.md), and [directory guide](project/research/general_n/2026-09-07-degree-load-v7/README.md).

The degree-load route excludes the final 388 rows in stages of **173 and 215**. The LocalIncidence route excludes those same inputs in stages of **22, 19 and 347**. These are numerical necessary-condition rows, not graphs. The former route adds edges within the complement's A-part to obtain a weaker active B-quasi-edge core at the tested density. It does not claim that deleting edges preserves diameter-two criticality. Whether every model and upstream cut remains necessary for those weaker cores is an explicit mathematical review obligation. The direct 197-edge continuation is separate from that reduction.

Each archive documents its replay entry point. Integrity-only verification is not arithmetic replay. The exact v6 and LocalIncidence v7 checking routes use Python's standard library; inherited v5 full checks require a C++17 compiler with Boost headers. Discovery solvers are not substitutes for exact rejection certificates. No new complete-chain replay is asserted by this intake documentation.

## Frozen n=25 review

Start with the [reviewer manuscript](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf), [review guide](releases/n25-reviewer-v1/REVIEW_GUIDE.md), [frozen proof](project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md), [exact results](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RESULTS.md), and [reviewer package](releases/n25-reviewer-v1/README.md).

The candidate includes degree-13 witness counting, degree-14/15/16 residual arguments, the published complement minimum-degree reduction for Delta>=17, and 1,959 checked final equality-column certificates. See the [reconciliation](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RECONCILIATION.md), [literature/attribution note](releases/n25-reviewer-v1/LITERATURE_AND_ATTRIBUTION.md), and [internal red-team report](project/reviews/n25/2026-09-06-redteam-v1/N25_Red_Team_Report_2026-09-06.md).

The [external review register](releases/n25-reviewer-v1/REVIEW_REGISTER.json) remains OPEN. Paul [reported sending a review invitation to Dr Florent Foucaud](project/reviews/n25/outreach/2026-09-07-foucaud-sent-user-report.md); no completed external assessment is asserted.

## Frozen n=27 review

The [n27 candidate proof](project/reviews/n27/2026-09-07-candidate-v1/README.md) proposes 182 edges with equality only K(13,14). Its [complete evidence package](releases/n27-candidate-v1/README.md) provides the numerical route and replay instructions. Independent mathematical review and external computational reproduction remain OPEN.

## General-order research

The [coupled-resource v2 derivation](project/research/general_n/2026-09-07-coupled-resource-v2/PROOF.md) gives the candidate implication for n>=4:

```text
Delta(G) >= ((10-sqrt(2))/14)*n  ==>  e(G) < floor(n^2/4),
(10-sqrt(2))/14 = 0.6132704598...
```

This is a mathematical argument under its stated structural premises, not extrapolation from finite tests. The v7 routes do not improve the coefficient. The [h-index v1](project/research/general_n/2026-09-07-residual-hindex-v1/README.md), [pair-budgets v2](project/research/general_n/2026-09-07-pair-budgets-v2/README.md), [demand-support v3](project/research/general_n/2026-09-07-demand-support-v3/PROOF.md), [overlapping demand-stability v3](project/research/general_n/2026-09-07-demand-stability-v3/README.md), [label-tail v4](project/research/general_n/2026-09-07-label-tail-v4/README.md), and [column-propagation v5](project/research/general_n/2026-09-07-column-propagation-v5/README.md) are preserved unchanged.

The v3 degree-case exclusions at (30,17) and (33,19) do not complete those orders; (28,16) supplies one branch of order-28 assembly. V4's 13,196-row and v5's 6,918-row equality frontiers are historical stages. SharedAdjacency v6 leaves 388 rows; both v7 routes exclude those rows using different arguments. Infinite excluded profile families are not whole-order theorems.

**No complete order above 28, proof through n=1,000, full general conjecture, novelty/priority determination, independent endorsement or formal-kernel verification is claimed.** Saved actual-graph samples contain no positive-surplus example. Universal correctness depends on structural proofs and complete finite domains, not those samples alone.

## Governance and preservation

Historical Delta=15, Audit v5 and legacy SAT/reproduction obligations remain preserved; replacement routes do not retroactively certify them. The [README preceding this reconciliation](project/reviews/history/README_before_v6_v7_intake_2026-09-07.md) is retained byte-for-byte, as is the [earlier pre-order28 README](project/reviews/history/README_before_n28_candidate_v7.md).

- [Project standing orders](project/N25_PROJECT_STANDING_ORDERS.md)
- [Repository synchronization and commit-completion policy](project/REPO_SYNC_POLICY.md)
- [Canonical n25 review](project/CANONICAL_N25_REVIEW_2026-09-06.md)
- [Governed theorem ledger](repro-v1/ledger/theorem_ledger.json)
- [Historical task backlog](project/CANONICAL_TASKS.json)
- [Evidence-recovery manifest](project/EVIDENCE_RECOVERY_MANIFEST.json)

Preserve code, exact inputs/outputs, provenance, corrections, survivor lists and review reports. Branch attachment and read-back are required before any commit is called complete. Documentation publication is not binary-evidence publication or mathematical certification.
