# Murty–Simon / Erdős Problem #742

**Candidate proofs at n=25, n=27 and now n=28; active general-order research.**

**Status updated: 7 September 2026. Independent mathematical review remains OPEN.** The new [order-28 candidate](project/research/general_n/2026-09-07-degree-load-v7/N28_CANDIDATE.md) proposes **at most 196 edges, with equality exactly for K(14,14)**. The final 388 numerical rows are excluded with exact checked certificates; a new weak-core reduction supplies the higher-edge-count scope. This is a complete candidate route, not an announcement of independent acceptance or a solution of the full conjecture.

**Evidence availability:** the readable v7 proof, scope audit, results and check reports are recorded here. The complete **21,975,757-byte audit ZIP**, containing the original v3–v6 archives and the full v7 code/certificates, was supplied separately in the research chat and **is not yet attached to this repository**. Its filename and SHA-256 are pinned in the [v7 publication-scope record](project/research/general_n/2026-09-07-degree-load-v7/PUBLICATION_SCOPE.json). Readable-document publication must not be confused with complete binary-evidence publication. The latest fully archived repository research checkpoint remains [v5](project/research/general_n/2026-09-07-column-propagation-v5/README.md).

## Current position

| Workstream | Candidate result | Review or preservation obligation |
|---|---|---|
| n=25 | At most 156 edges; equality only K(12,13) | Independent mathematical review and external reproduction OPEN |
| n=27 | At most 182 edges; equality only K(13,14) | Independent mathematical review and external reproduction OPEN |
| n=28 | At most 196 edges; equality only K(14,14) | Independent review OPEN; complete audit ZIP awaits repository attachment |
| General order | Candidate high-degree result, coupled degree/label constraints and weak-core density reduction | No complete all-order proof or new uniform coefficient |

The frozen n=25/n=27 editions and governed theorem ledger are unchanged. A candidate mathematical proof, exact arithmetic reproduction, evidence availability and independent review are separate status questions.

## Start here: n=28 candidate

Read the [assembled candidate theorem](project/research/general_n/2026-09-07-degree-load-v7/N28_CANDIDATE.md), the [new model and density-reduction proofs](project/research/general_n/2026-09-07-degree-load-v7/PROOF.md), and especially the [core-scope audit](project/research/general_n/2026-09-07-degree-load-v7/CORE_SCOPE_AUDIT.md). The [v7 directory guide](project/research/general_n/2026-09-07-degree-load-v7/README.md) explains the separately supplied complete replay bundle.

The new degree-15 calculation at 196 edges closes the v6 frontier:

| Stage | Inputs | Exact exclusions | Remaining |
|---|---:|---:|---:|
| Joint arc / column-option / endpoint-degree events | 388 | 173 | 215 |
| Source incoming/outgoing degree and actual label-load consistency | 215 | 215 | **0** |

These are necessary-condition rows, not graphs. Every row has an exact integer contradiction checked against separately reconstructed constraints. The v4 full arithmetic and v5/v6 full separate-checking routes were rerun, their handoff bytes compared, and v3's complete n28/Delta16 scope rechecked. The new v7 checker and graph/core tests also passed in a fresh copy. Both implementations are by the same assistant, not independent research authors.

The upper-bound and equality claims need more than a zero equality-level frontier. The new proof weakens critical graphs to **active B-quasi-edge cores**, a class preserved by adding edges inside the complement's A-part. This lowers the surplus to the tested level while preserving exactly the structural premises of the finite route. The reduced complement need not have diameter two. **No deletion-preserves-criticality assertion and no unproved monotonicity of the old column tests is used.** The scope audit is therefore a central external-review target.

The complete audit bundle's `replay_chain.py --check --output ...` reruns all required numerical stages from the original archives. Its default `--verify-only` checks integrity and stage identity, not arithmetic. Full-chain checking needs Python and a C++17 compiler with Boost headers for the inherited v5 program; v7's exact checker itself uses only Python's standard library. The bundle records which component checks were executed and distinguishes these from testing the new combined wrapper in integrity mode.

## Frozen n=25 review entry points

Start with the [reviewer manuscript](releases/n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf), [review guide](releases/n25-reviewer-v1/REVIEW_GUIDE.md), [frozen candidate proof](project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md), and [exact result tables](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RESULTS.md). The [reviewer package](releases/n25-reviewer-v1/README.md) contains the unchanged evidence, sources, checksums and replay wrapper.

The candidate includes the degree-13 witness proof, degree-14/15/16 residual arguments, the published complement minimum-degree reduction for Delta>=17, and 1,959 checked final equality-column certificates. See the [reconciliation](project/reviews/n25/2026-09-06-full-chain-candidate-v1/RECONCILIATION.md), [literature/attribution note](releases/n25-reviewer-v1/LITERATURE_AND_ATTRIBUTION.md) and [internal red-team report](project/reviews/n25/2026-09-06-redteam-v1/N25_Red_Team_Report_2026-09-06.md).

The [external review register](releases/n25-reviewer-v1/REVIEW_REGISTER.json) remains OPEN. Paul [reported sending a review invitation to Dr Florent Foucaud](project/reviews/n25/outreach/2026-09-07-foucaud-sent-user-report.md). No completed external assessment is asserted here.

## Frozen n=27 review entry points

The [n=27 candidate proof](project/reviews/n27/2026-09-07-candidate-v1/README.md) proposes 182 edges with equality only K(13,14). Its [full evidence package](releases/n27-candidate-v1/README.md) provides the complete numerical route and replay instructions. Independent mathematical review and external computational reproduction remain OPEN.

## General-order research

The [coupled-resource v2 derivation](project/research/general_n/2026-09-07-coupled-resource-v2/PROOF.md) gives the candidate implication, for n>=4,

```text
Delta(G) >= ((10-sqrt(2))/14)*n  ==>  e(G) < floor(n^2/4),
(10-sqrt(2))/14 = 0.6132704598...
```

The v7 work does not improve that coefficient. The middle-degree region remains open in general. The [residual h-index v1](project/research/general_n/2026-09-07-residual-hindex-v1/README.md), [pair budgets v2](project/research/general_n/2026-09-07-pair-budgets-v2/README.md), [demand-support v3](project/research/general_n/2026-09-07-demand-support-v3/PROOF.md), [overlapping demand-stability v3](project/research/general_n/2026-09-07-demand-stability-v3/README.md), [label-tail v4](project/research/general_n/2026-09-07-label-tail-v4/README.md), and [column-propagation v5](project/research/general_n/2026-09-07-column-propagation-v5/README.md) remain preserved unchanged.

The two v3 workstreams cover the same three degree cases and are not counted twice. Their exclusions at (n,Delta)=(30,17) and (33,19) do not complete those orders. Their (28,16) exclusion is one branch of the new order-28 assembly. The v4/v5 historical frontiers of 13,196 and 6,918 rows were superseded in the new research; their original reports are not rewritten. Excluded infinite profile families are not whole-order theorems.

**No complete order above 28, proof through n=1,000, full general conjecture, novelty/priority determination, independent endorsement or formal-kernel verification is claimed.** Actual-graph samples contain no positive-surplus example. Universal correctness rests on the structural proofs and finite-domain exclusion, not extrapolation from those samples.

## Historical work and governed status

The parked historical Delta=15 proof, Audit v5 and legacy SAT/reproduction tasks remain preserved; replacement routes do not retroactively certify unresolved historical arguments. The [README immediately before this update](project/reviews/history/README_before_n28_candidate_v7.md) is retained byte-for-byte, including its earlier v5 scope and detailed replay notes.

- [Project standing orders](project/N25_PROJECT_STANDING_ORDERS.md)
- [Repository synchronization and commit-completion policy](project/REPO_SYNC_POLICY.md)
- [Canonical n=25 review](project/CANONICAL_N25_REVIEW_2026-09-06.md)
- [Governed theorem ledger](repro-v1/ledger/theorem_ledger.json)
- [Historical task backlog](project/CANONICAL_TASKS.json)
- [Evidence-recovery manifest](project/EVIDENCE_RECOVERY_MANIFEST.json)

The theorem ledger is not promoted by research or document publication. Keep code, exact inputs/outputs, provenance, corrections and review reports; preserve each edition and label later changes separately. Branch attachment and read-back verification are required before any commit is called complete.
