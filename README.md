# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research, organised by graph order. **Updated 7 September 2026. Independent mathematical review and external computational reproduction remain OPEN.** A paper prepared for review, a successful internal replay and repository publication are not independent acceptance or a proof of the general conjecture.

## n=25 — candidate proof

**Proposed result:** every simple diameter-two edge-critical graph on 25 vertices has at most **156 edges**, with equality only for **K(12,13)**.

**Paper:** [reviewer manuscript (PDF)](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf) · [readable manuscript](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.md) · [review guide](releases/n25-reviewer-v1/REVIEW_GUIDE.md).

The [complete reviewer package](releases/n25-reviewer-v1/README.md), [frozen proof](project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md) and [exact results](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RESULTS.md) supply the evidence and replay instructions. The candidate includes degree-13 witness counting, degree-14/15/16 residual arguments, the published high-degree reduction, and 1,959 checked final equality-column certificates.

Read the [reconciliation](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RECONCILIATION.md), [literature and attribution note](releases/n25-reviewer-v1/LITERATURE_AND_ATTRIBUTION.md) and [internal red-team report](project/reviews/n25/2026-09-06-redteam-v1/N25_Red_Team_Report_2026-09-06.md). **Status:** complete candidate; internal arithmetic reproduced; independent review OPEN. The frozen edition is unchanged.

## n=27 — candidate proof

**Proposed result:** at most **182 edges**, with equality only for **K(13,14)**.

**Paper:** [complete readable proof manuscript](project/reviews/n27/2026-09-07-candidate-v1/PROOF.md) · [proof and review guide](project/reviews/n27/2026-09-07-candidate-v1/README.md).

The [complete evidence package](releases/n27-candidate-v1/README.md) supplies the source, ledgers, certificates and replay instructions. The manuscript link opens the full Markdown proof, not a PDF or an archive-only landing page. **Status:** complete candidate; internal arithmetic reproduced; independent review OPEN. No new n=27 mathematical replay is asserted by the n=28 editorial release.

## n=28 — candidate proof and reviewer release

**Proposed result:** at most **196 edges**, with equality only for **K(14,14)**.

**Papers:** [mathematical manuscript (PDF)](releases/n28-reviewer-v1/N28_Reviewer_Manuscript_v1.pdf) · [computational verification and reviewer guide (PDF)](releases/n28-reviewer-v1/N28_Verification_Companion_v1.pdf).

The [reviewer release](releases/n28-reviewer-v1/README.md) contains both editable LaTeX sources, the default hardened checking driver, immutable archive inventory, validation reports and a [review report template](releases/n28-reviewer-v1/REVIEW_REPORT_TEMPLATE.md). The [review register](releases/n28-reviewer-v1/REVIEW_REGISTER.json) distinguishes mathematical review from external reproduction. No review invitation is sent by this release.

### Direct route: equality, then upper bound

At **196 edges**, the degree-15 chain passes through v5, v6 and **LocalIncidence-v7**: 6,918 rows reduce to 388, then to zero in v7's 22/19/347 partition. At **197 edges**, direct197-v8 generates its own t=2 domain: 12,012 charging tuples, 1,229 retained intervals and 8,216,928 residual rows. Successive screens leave 5,154, 2,959 and 1,584 rows; exact final certificates exclude 787+790+7, leaving zero. These are necessary-condition rows, not graphs.

All other maximum-degree cases are handled explicitly. Fan's cited strict bound of 197.2075 rules out 198 or more edges; its original proof remains an external theorem input. The direct route uses neither deletion-preserves-criticality nor an unproved transfer of equality-level survivor lists. Full structural arguments, computation and degree-case assembly are consolidated in the new manuscript.

### Hardened checking is now the default

The reviewer driver verifies the six original archives and all 400 payloads, creates a separate v8 working copy and automatically applies the hash-pinned helper guard. The original source, manifests, archives and historical reports are unchanged. Full checking is the default; integrity-only mode must be requested explicitly.

```sh
python3 -I -B releases/n28-reviewer-v1/review_check.py \
  --archives-dir /absolute/path/to/original-zips \
  --output /absolute/path/to/new-n28-review --jobs 3
```

The [complete release validation](releases/n28-reviewer-v1/validation/REVIEW_CHECK_REPORT.json) records **all eight jobs passing**, both density scopes ending with zero survivors, all five handoffs matching byte-for-byte, and unchanged originals. All **13 malformed helper inputs** are rejected before output creation. The valid 8,216,928-row scope reproduces the original report, survivor bytes and per-demand bands. Checking requires Python 3.10+, C++17 and Boost headers, no optimisation solver or network. The companion explains how to obtain the original ZIPs and distinguishes the new engineering validation from the historical audit.

The [internal red-team audit](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md) found no blocking defect in the audited direct route. Its additional arithmetic kernel checked 8,983 certificate leaves but reuses preserved model constructors; it is not a third independent graph-to-model derivation. **Status:** complete candidate prepared for review; full internal replay reproduced; independent mathematical review OPEN.

### Alternative degree-load-v7 route

The separate [degree-load-v7 candidate](project/research/general_n/2026-09-07-degree-load-v7/N28_CANDIDATE.md) closes the same equality frontier in a different 173/215 partition and adds a weak-core density reduction. Its [scope audit](project/research/general_n/2026-09-07-degree-load-v7/CORE_SCOPE_AUDIT.md) identifies that extra obligation. It is not a dependency of the new reviewer manuscript. The two v7 archives are not interchangeable and their overlapping exclusions must not be counted twice. The alternative bundle's availability remains tracked by its own [publication-scope record](project/research/general_n/2026-09-07-degree-load-v7/PUBLICATION_SCOPE.json).

## Review-paper index

| Scope | Direct paper link | Companion material |
|---|---|---|
| n=25 | [Reviewer manuscript — PDF](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf) | [Review guide and evidence](releases/n25-reviewer-v1/REVIEW_GUIDE.md) |
| n=27 | [Full proof manuscript — Markdown](project/reviews/n27/2026-09-07-candidate-v1/PROOF.md) | [Evidence package](releases/n27-candidate-v1/README.md) |
| n=28 | [Mathematical manuscript — PDF](releases/n28-reviewer-v1/N28_Reviewer_Manuscript_v1.pdf) | [Verification companion — PDF](releases/n28-reviewer-v1/N28_Verification_Companion_v1.pdf) |

The new n=28 [manuscript source](releases/n28-reviewer-v1/N28_Reviewer_Manuscript_v1.tex) and [companion source](releases/n28-reviewer-v1/N28_Verification_Companion_v1.tex) are editable. Their [build report](releases/n28-reviewer-v1/PAPER_BUILD_REPORT.json) pins source and PDF hashes. Document compilation is not a mathematical check. All papers state their candidate status and review limits.

## General-order research

The [coupled-resource derivation](project/research/general_n/2026-09-07-coupled-resource-v2/PROOF.md) gives the candidate implication for n>=4:

```text
Delta(G) >= ((10-sqrt(2))/14)*n  ==>  e(G) < floor(n^2/4),
(10-sqrt(2))/14 = 0.6132704598...
```

The middle-degree region remains open. The reviewer release makes no improvement to that coefficient. Earlier [residual h-index v1](project/research/general_n/2026-09-07-residual-hindex-v1/README.md), [pair budgets v2](project/research/general_n/2026-09-07-pair-budgets-v2/README.md), [demand-support v3](project/research/general_n/2026-09-07-demand-support-v3/PROOF.md), [overlapping demand-stability v3](project/research/general_n/2026-09-07-demand-stability-v3/README.md) and [label-tail v4](project/research/general_n/2026-09-07-label-tail-v4/README.md) remain preserved.

The (30,17) and (33,19) degree-case exclusions do not complete those orders. Infinite excluded profile families are not whole-order theorems. **No complete order above 28, proof through n=1,000, all-order solution, priority determination or formal-kernel verification is claimed.**

## Original evidence and governance

The original [v5](project/research/general_n/2026-09-07-column-propagation-v5/README.md), [v6](project/research/general_n/2026-09-07-shared-adjacency-v6/README.md), [LocalIncidence-v7](project/research/general_n/2026-09-07-local-incidence-v7/README.md) and [v8](project/research/general_n/2026-09-07-direct-197-v8/README.md) archives are in their dated directories. V3/v4 recovery instructions and the exact six-archive inventory are linked from the reviewer release. The [audit package](project/reviews/n28/2026-09-07-redteam-v1/README.md) has separate recovery instructions. Historic missing-upload statements are superseded by verified publication receipts, not erased.

Paul Lenz directed the project; ChatGPT/Geeps supplied mathematical development, software, manuscripts and internal checks. The original implementations have the same assistant author. Saved actual-graph samples contain no positive-surplus graph. Universal correctness therefore rests on the structural proofs, necessary-model implication and complete domains, not extrapolation from samples. The [external review register](releases/n25-reviewer-v1/REVIEW_REGISTER.json) remains OPEN; Paul [reported an earlier invitation to Dr Florent Foucaud](project/reviews/n25/outreach/2026-09-07-foucaud-sent-user-report.md), not a completed endorsement.

The [README before this reviewer-release update](project/reviews/history/README_before_n28_reviewer_release_v1.md) is preserved verbatim. Frozen n25/n27 proofs, original n28 archives and the governed theorem ledger are untouched. Historical Delta=15, Audit v5 and SAT/reproduction obligations are not retrospectively certified by replacement routes.

See the [standing orders](project/N25_PROJECT_STANDING_ORDERS.md), [commit-completion policy](project/REPO_SYNC_POLICY.md), [canonical review](project/CANONICAL_N25_REVIEW_2026-09-06.md), [theorem ledger](repro-v1/ledger/theorem_ledger.json), [task backlog](project/CANONICAL_TASKS.json) and [evidence-recovery manifest](project/EVIDENCE_RECOVERY_MANIFEST.json). Publication preserves evidence; it does not promote mathematical status.
