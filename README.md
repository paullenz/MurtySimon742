# Murty–Simon / Erdős Problem #742 — research archive and eventual D2C programme

<!-- Keep the live overview and status tables here. Put dated updates below them, never above them. -->
<!-- CURRENT-STATUS:START -->
## Current status

### Active mathematical target

The live problem is the **sufficiently-large / eventual second-extremal classification for diameter-2-critical graphs** around

`M(n)=floor((n-1)^2/4)+1`.

The stronger all-order 2019 Dailly–Foucaud–Hansberg conjecture is false: Radosavljević, Stanić and Živković (2024) give a 12-vertex D2C graph with 32 edges, while `M(12)=31`. That graph is a mandatory hostile control. Murty–Simon / Erdős #742 work remains preserved, but first-proof priority is not the active objective after discovery of the earlier `Erdos742/Erdos742` formalization.

**Live handoff:** [`CURRENT_STATE.md`](CURRENT_STATE.md).

### Current post-pivot frontier — internal, not promoted

The earlier exact zero-residual boundary gave an internally checked cutoff `n<=294` at `m>=M(n)`. The 18 September work advanced beyond that boundary. The present load-bearing spine is

`rooted witness-slot residual -> local A-code Hamming budget -> complementary-pair Hall demand -> exact Hall-cut decomposition -> Hall-density rigidity -> beta/source-tuple localization -> rigid-cut code collapse -> U-witness deficit/slack -> one-code pair-capacity/crowding trap`.

For a rigid Hall cut, outside-code diversity is now charged to actual U-witness population, A–U nonedges and unmatched slack. If the outside layer collapses to one code pair, it must satisfy the explicit bill

`Ccap_P + L_Y >= y(p+x+k)`,

with the aligned same-code crowding lower bound available simultaneously. These are strong internal structural advances, **not** a completed eventual theorem.

Key packages:

- [Rooted witness-slot saturation and Hamming defect](project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/)
- [Hall density / exact-cut stability](project/research/post_ms/2026-09-18-hall-density-cut-stability-v1/)
- [Same-code complementary-pair localization](project/research/post_ms/2026-09-18-large-code-pair-v1/)
- [Rigid Hall witness deficit and one-code trap](project/research/post_ms/2026-09-18-rigid-hall-witness-deficit-v1/)
- [Bounded-surplus four-exception gate](project/research/post_ms/2026-09-18-combined-channel-four-exception-v1/)

### 19 September 2026 adversarial checkpoint

The [daily red-team audit](project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md) reviewed the preceding 24-hour research interval, using `f2e85599491d9804084e9739e1cfcdc6cc088a29` as the last pre-window comparison point and `0060acd80a376074486563bc537386fe130459d2` as the pre-audit head. GitHub reports 216 intervening commits.

**Finding:** no fatal contradiction was found in the current load-bearing rooted-witness / Hall / rigid-U-witness spine. The trust boundary is nevertheless narrower than same-project CI alone would suggest. The finite source-tuple capacity theorem has now been independently re-derived from its two explicit shared premises — distinct physical sources in each source set and global selected-representative uniqueness for each source-coordinate obligation — including the arbitrary-subset layer-cake deficit formula. Those two graph-to-selected-system premises, and the wider graph-to-constraint interface, remain to be independently certified end-to-end.

The audit independently reconstructed the project’s `X_3` order-12 graph and confirmed diameter 2 and edge-criticality for all 32 edges. The repository’s direct identification with the published Figure 1 remains an **internal figure-based certification**; this audit did not independently compare against a machine-readable author adjacency list.

The audit also exposed repository-process defects in the audit checkpoint itself. Commit `03356bf3203fdc9bbd35fad97c6574eb16f3dcaa` failed Status synchronization because the guard did not parse the repository’s Markdown-bold `WORK MODE` field, and failed the N30 navigation checker because valid README directory links were treated as invalid. Follow-up commit `3d17a816eb4f95b149a5f02ef1fc36bc298b6bae` repaired both issues and its Status synchronization run `35406192884` passed. Commit `bfadbd7eca55475ea1ca92e36e781f074bfae3bb` restored direct fixed-order PDF links but the dedicated README guard then showed that the compression had also removed five current general-theory reviewer links and protected red-team detail. This checkpoint restores those surfaces rather than weakening the guard.

### Trust boundary

The newest theorem packages are **internal candidate mathematics**. Hand derivation, same-project checker replay, GitHub CI, independent implementation, external specialist review and publication acceptance are distinct. No finite abstract parameter scan is a count of realizable D2C graphs. No global eventual second-extremal theorem is claimed.

The main remaining shared-risk interface is the graph-to-constraint chain: rooted criticality certificates, distinct-source/selected-obligation uniqueness, Hall pair localization, and their integration on realizable D2C graphs. The next audit priority is graph-level regression and independent premise verification, not additional confidence by repetition of the same abstractions.

### Canonical preserved finite ledger

**4,626 exclusions / 952 survivors / 3,632 whole-state closures.** The fixed-order candidate proofs, audits, exact-block work, h-index/receiver theory, selected-incidence Hall machinery and mixed `{4,5}` all-excess closure remain preserved with their original trust boundaries. The discovery of earlier external #742 work changes priority/novelty, not the internal logical status of those artifacts.

### Standalone-paper programme

Two internal candidate paper packages remain under development:

1. [Stratified Hall / minimum-cut exactness](project/papers/stratified-hall-mincut/MANUSCRIPT.md) — abstract two-sided crossing-dominance / Hall-margin exactness.
2. [Boolean-flow / D2C stability](project/papers/boolean-flow-d2c/MANUSCRIPT.md) — zero-residual Boolean-coordinate structure, the `n<=294` boundary cutoff, and root-edge stability.

See the [standalone paper index](project/papers/README.md) and claim ledgers before citing any result as established or new.

### Current fixed-order candidate packages

| Scope | Preserved candidate result; external review open |
|---|---|
| n=25 | `e(G)<=156`, equality exactly `K(12,13)`; reviewer-v2 |
| n=27 | `e(G)<=182`, equality exactly `K(13,14)`; reviewer-v2 |
| n=28 | `e(G)<=196`, equality exactly `K(14,14)`; reviewer-v2 plus analytic hardening |
| n=29 | `e(G)<=210`, equality exactly `K(14,15)`; reviewer-v4; difficult `Delta=16` branch hand-closed |
| n=30 | `e(G)<=225`, equality exactly `K(15,15)`; reviewer-v3 |
| n=31 | `e(G)<=240`, equality exactly `K(15,16)`; source-first reviewer-v1 |
| n=32 | `e(G)<=256`, equality exactly `K(16,16)`; source-first reviewer-v1 |
| n=33 | `e(G)<=272`, equality exactly `K(16,17)`; source-first reviewer-v1 |
| n=34 | `e(G)<=289`, equality exactly `K(17,17)`; reviewer-v2; final heavy certificate hand-replaced |
| n=35 | `e(G)<=306`, equality exactly `K(17,18)`; reviewer-v1 |

### Operational programme

The eventual-D2C programme is continuing through **27 September 2026**, with a dedicated daily adversarial audit and repository-hygiene checkpoint. Daily audit work is reserved for attempted falsification, independent replay, README/CURRENT_STATE reconciliation and a dated 24-hour report rather than forward research. Autonomous work must not revert to the false all-order 2019 conjecture, must retain `X_3` as a regression test, and must not optimize for first-proof priority on Erdős #742.

**Reviewers:** [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) · [`REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md) · [papers and review materials](#papers-and-review-materials).
<!-- CURRENT-STATUS:END -->

## Dated research updates — current and preserved history

**19 September 2026 — daily adversarial audit and live-state reconciliation.** No fatal contradiction was found in the current load-bearing rooted-witness/Hall/rigid-U-witness spine. The audit distinguishes hand-derived structural claims from abstract checker support, independently re-derives the finite source-tuple capacity theorem conditional on its two named shared premises, confirms `X_3` as a D2C hostile control, and records/repairs deterministic status/navigation/index failures rather than classing them as transient. See the [full audit](project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md), [independent source-tuple re-proof](project/research/post_ms/2026-09-19-daily-red-team-audit-v1/INDEPENDENT_SOURCE_TUPLE_REPROOF.md), [process repair note](project/research/post_ms/2026-09-19-daily-red-team-audit-v1/FOLLOW_UP_PROCESS_REPAIR.md), and [`CURRENT_STATE.md`](CURRENT_STATE.md).

**17 September 2026 — programme reset.** External work in `Erdos742/Erdos742` changed the priority interpretation of the Murty–Simon project, while the 2024 order-12 counterexample falsified the contemplated all-order second-extremal strengthening. The active programme therefore became the sufficiently-large/eventual D2C problem. The dependency audit found no inspected fixed-order proof using the false conjecture as a premise. See [literature correction](project/research/post_ms/2026-09-17-stronger-pivot-v1/LITERATURE_CORRECTION_2024_EXCEPTION.md) and [dependency audit](project/research/post_ms/2026-09-17-stronger-pivot-v1/DEPENDENCY_AUDIT_2019_FALSE_CONJECTURE.md).

### Preserved pre-audit README

The complete root README immediately before the 19 September daily reconciliation is preserved byte-for-byte at [`archive/status-snapshots/2026-09-19/README_before_daily_red_team.md`](archive/status-snapshots/2026-09-19/README_before_daily_red_team.md). That snapshot contains the full dated 14–17 September status chronology, the historical general-research workstream register, prior audit/promotion details, workflow provenance notes, and earlier next-action lists. Those records remain part of the project evidence; this live README is intentionally status-first rather than silently deleting them.

Earlier status snapshots are preserved under [`archive/status-snapshots/`](archive/status-snapshots/).

<!-- REDTEAM-HISTORY:START -->
## Hostile / red-team audit history and resulting proof hardening

**19 September 2026 — daily eventual-D2C audit.** The [full report](project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md) found no fatal contradiction in the current rooted-witness/Hall/rigid-U-witness spine, but tightened the evidence labels: abstract checker success is not graph-level realizability verification; the source-tuple capacity theorem is now independently re-derived conditional on its graph-to-selected-system premises; the four-exception direct-fan gate is strongly supported rather than fully re-certified in this audit; and the one-code exact pair-capacity/crowding branch remains the primary forward target. The audit also found and preserved deterministic repository-process regressions.

**n=29 — real normalization bug found and corrected.** Hostile review established that a label-group multiplicity was counted twice. The v1 cumulative-threshold certificates are therefore **invalid as proof evidence**. A corrected v2 replay, smaller exact kernel and later hand clipping argument removed the defect and much of the computational dependency. See [public-release audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md), [minimal kernel](project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json), and [reviewer-v4](project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md).

**Blind external red-team follow-up.** The [blind external red-team follow-up](project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md) preserved a non-blocking sign/order typo while distinguishing it from the corrected normalization defect; the point of the record is that even non-fatal criticism remains visible rather than being erased by a later clean proof.

**Fan dependency removed from the fixed-order logical spine.** The direct reduction in [FAN_FREE_REDUCTION.md](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md) and its companion [FAN_FREE_AUDIT.md](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md) replaced the historical Fan-density dependency for the preserved fixed-order packages. The external-feedback audit that prompted the hardening remains at [REPORT.md](project/reviews/cross-cutting/2026-09-09-external-ai-feedback-audit-v1/REPORT.md).

**Hostile coverage/integrity audit surfaces remain first-class evidence.** Preserved packages include the [n=25 re-audit](project/reviews/n25/2026-09-08-reaudit-v1/README.md), [n=27 red-team audit](project/reviews/n27/2026-09-08-redteam-v1/REPORT.md), [n=28 red-team report](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md), [n=30 assembly audit](project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md), and [general 7/12 hostile audit](project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md).

**Preservation rule:** a hostile audit may strengthen, weaken, invalidate or redirect a claim. All four outcomes are evidence. Invalidated and superseded computations remain visible; failed audits, counterexamples and reviewer-triggered proof changes are not to be removed because a later route is cleaner. The complete pre-audit red-team chronology is preserved in the archived README linked above.
<!-- REDTEAM-HISTORY:END -->

## Current research chain

The active chain is the **eventual dense D2C programme**:

- [Literature correction / 12-vertex exception](project/research/post_ms/2026-09-17-stronger-pivot-v1/LITERATURE_CORRECTION_2024_EXCEPTION.md)
- [Published-figure hostile-control certification](project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md)
- [False-2019-conjecture dependency audit](project/research/post_ms/2026-09-17-stronger-pivot-v1/DEPENDENCY_AUDIT_2019_FALSE_CONJECTURE.md)
- [Signed-surplus pivot](project/research/post_ms/2026-09-17-stronger-pivot-v1/SIGNED_SURPLUS_PIVOT.md)
- [Zero-residual Boolean-flow boundary](project/research/post_ms/2026-09-17-stronger-pivot-v1/ZERO_RESIDUAL_BOUNDARY.md)
- [Rooted witness-slot saturation](project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/)
- [Hall density / cut stability](project/research/post_ms/2026-09-18-hall-density-cut-stability-v1/)
- [Same-code complementary-pair localization](project/research/post_ms/2026-09-18-large-code-pair-v1/)
- [Rigid Hall witness deficit and one-code trap](project/research/post_ms/2026-09-18-rigid-hall-witness-deficit-v1/)
- [19 September daily adversarial audit](project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md)
- [Independent finite source-tuple re-proof](project/research/post_ms/2026-09-19-daily-red-team-audit-v1/INDEPENDENT_SOURCE_TUPLE_REPROOF.md)

The immediate priority is to verify the two remaining graph-to-selected-system premises behind the source-tuple theorem directly from rooted criticality, then combine the **exact** one-code `Ccap_P` formula with `(ONE)` and `(CROWD)` before introducing any further global scalar relaxation. In parallel, build an independent graph-level regression of the rooted/Hall quantities on realizable small D2C graphs including `X_3`.

## Failures and audit gates remain first-class evidence

Do not quietly delete, relabel or retrospectively clean up a failed lemma, non-closing experiment, counterexample or CI event. The pre-audit Status synchronization failure `35402717100` / `105785888407`, audit-head failures `35405621026` / `105794668021` and `35405621004` / `105794668117`, first-repair N30 failure `35406193034` / `105796333427`, and README guard failure `35406504877` / `105797249965` are preserved as deterministic process findings, not transient infrastructure. Historical failures and non-promoted discovery results remain documented in the preserved pre-audit README and their native packages.

Finite discovery, audit, ledger promotion and external mathematical acceptance remain separate gates. Synthetic or abstract-system rejections do not alter the canonical graph frontier by themselves.

<!-- REVIEW-MATERIALS:START -->
## Papers and review materials

**Reviewer entry:** start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md), then [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md).

### Active standalone paper candidates

- [Stratified Hall / minimum-cut manuscript](project/papers/stratified-hall-mincut/MANUSCRIPT.md) · [claim ledger](project/papers/stratified-hall-mincut/CLAIM_LEDGER.md) · [abstract theorem](project/papers/stratified-hall-mincut/ABSTRACT_CROSSING_DOMINANCE.md)
- [Boolean-flow D2C manuscript](project/papers/boolean-flow-d2c/MANUSCRIPT.md) · [claim ledger](project/papers/boolean-flow-d2c/CLAIM_LEDGER.md) · [all-private stability theorem](project/research/post_ms/2026-09-17-stronger-pivot-v1/ALL_PRIVATE_STABILITY.md)

### Fixed-order reviewer packages

- [`n=25 reviewer-v2`](releases/n25-reviewer-v2/README.md) · [manuscript](releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) · [verification companion](releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf)
- [`n=27 reviewer-v2`](releases/n27-reviewer-v2/README.md) · [manuscript](releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) · [verification companion](releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf)
- [`n=28 reviewer-v2`](releases/n28-reviewer-v2/README.md) · [manuscript](releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) · [verification companion](releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf)
- [`n=29 reviewer-v4`](releases/n29-reviewer-v4/README.md) · [manuscript](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) · [verification companion](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf)
- [`n=30 reviewer-v3`](releases/n30-reviewer-v3/README.md) · [manuscript](releases/n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf) · [verification companion](releases/n30-reviewer-v3/N30_Verification_Companion_v3.pdf)
- [`n=31 reviewer-v1`](releases/n31-reviewer-v1/README.md)
- [`n=32 reviewer-v1`](releases/n32-reviewer-v1/README.md)
- [`n=33 reviewer-v1`](releases/n33-reviewer-v1/README.md)
- [`n=34 reviewer-v2`](releases/n34-reviewer-v2/README.md)
- [`n=35 reviewer-v1`](releases/n35-reviewer-v1/README.md)

### General-theory reviewer packages

- [`7/12` maximum-degree reviewer-v1](releases/general-7-12-reviewer-v1/README.md)
- [`13/22` retained maximum-degree reviewer-v1](releases/general-13-22-reviewer-v1/README.md)
- [`293/500` retained maximum-degree reviewer-v1](releases/general-293-500-reviewer-v1/README.md)
- [General step-back structural package](releases/general-stepback-v1/README.md)
- [Joint-clipping reviewer-v1](releases/general-joint-clipping-reviewer-v1/README.md)
- [Heavy-load / routing reviewer-v1](releases/general-heavy-load-reviewer-v1/README.md)
- [Joint-routing reviewer-v1](releases/general-joint-routing-reviewer-v1/README.md)
- [Routing-tail reviewer-v1](releases/general-routing-tail-reviewer-v1/README.md)
- [Compatible-routing reviewer-v1](releases/general-compatible-routing-reviewer-v1/README.md)
- [Compatible-routing full-catalogue reviewer-v1](releases/general-compatible-catalogue-reviewer-v1/README.md)
- [Closed-compatible reviewer-v1](releases/general-closed-compatible-reviewer-v1/README.md)
- [Arc-realisation reviewer-v1](releases/general-arc-realisation-reviewer-v1/README.md)
<!-- REVIEW-MATERIALS:END -->

## Repository policy and provenance

The canonical repository is `paullenz/MurtySimon742`. Every active research transaction must leave `CURRENT_STATE.md` parseable by `scripts/check_status_sync.py`, including the required checkpoint and handoff fields. README is refreshed at substantive reviewer-facing milestones and at the daily adversarial audit. Mathematical files, checker evidence and status should be committed atomically where practical because status synchronization checks every new commit.

Historical status and audit material must remain discoverable. The 19 September archived pre-audit README is the complete preservation point for the material compressed from this live status-first surface.
