# Research outcome assessment — 12 September 2026

**Status: subjective planning judgment. This is not mathematical evidence, external review, a novelty determination, or a statistically calibrated forecast.**

Baseline: public `main` at `f9ffe629dd35ddbaaae3cf8d8542e775984d531f`. Paul requested a considered reassessment after inconsistent conversational probability estimates. This note defines a reproducible baseline for future comparisons. The arithmetic makes the assumptions inspectable; it does not make the judgments objective.

## Scope and assumptions

The horizon is **12 September 2027**, assuming regular active research sessions, willingness to change methods, and substantive review by at least one suitably qualified external graph theorist. Review must reach the shared foundations and a proposed main result; decisive computations need external reproduction where relevant. These are forecasting assumptions, not claims that a reviewer has agreed or a commitment to background work. No capability breakthrough or unlimited compute is assumed.

Corrections and revisions are allowed. The subject is this programme's contribution, rather than the chance that someone else solves the conjecture. A paper-worthy result means a specialist judges it correct, original and mathematically substantial enough for a research paper. Journal acceptance within twelve months is a separate logistical and editorial event and is not estimated here.

The review for this assessment read the current mathematical sources, reviewer entry points and audit/correction records listed below. It did **not** rerun the full proof archive, formally verify the arguments, or constitute a fresh independent mathematical audit. Earlier recorded verification results remain evidence with their original scope.

## Comparable outcomes

These are **nested milestones**: achieving a later milestone includes achieving the earlier ones. Their probabilities must not be added. Existing candidate general theorems are eligible for the third row; another discovery is not required just to have useful general theory.

| Milestone within the stated horizon | Central planning estimate | Cautious scenario | Favourable scenario |
|---|---:|---:|---:|
| At least one substantial graph-theoretic result from the programme survives specialist scrutiny, allowing repairs | about 90% | 80% | 95% |
| At least one original result or proof method is substantial enough for a research paper | about 75% | 60% | 90% |
| That original contribution includes useful general theory for infinitely many orders or a parameter-uniform mechanism | about 65% | 45% | 85% |
| A material general advance beyond the present candidate results | about 40% | 20% | 65% |
| A complete original proof of the all-order bound and equality classification passes detailed specialist review | about 10% | 3% | 25% |

The displayed figures are deliberately rounded. The last two columns are sensitivity scenarios, **not confidence intervals, credible intervals or hard bounds**. Different informed judgments could lie outside them. No reliable empirical reference class has been identified for this particular human–AI research programme.

The first row is not the probability that all current fixed-order claims are correct simultaneously, or that every present statement survives unchanged. The fourth row needs more than another isolated order or an improved scalar decimal. A concrete qualifying example would be a reviewed maximum-degree theorem with threshold at most `0.57n`, with its small-order scope made explicit, or a uniform structural theorem covering a growing family in the intermediate-degree region still missed by the present reductions. A small simplification that only rediscovers old exclusions does not meet that milestone.

## Evidence supporting useful outcomes

**There are explicit candidates to review.** The current [7/12 package](../../../releases/general-7-12-reviewer-v1/README.md) contains a parameter-uniform argument and explicit finite assembly. The [step-back package](../../../releases/general-stepback-v1/README.md) contains the balanced-degree theorem, a fixed-label infinite family and tail theorems. The [heavy-load](../../../releases/general-heavy-load-reviewer-v1/README.md), [joint-routing](../../../releases/general-joint-routing-reviewer-v1/README.md) and [routing-tail](../../../releases/general-routing-tail-reviewer-v1/README.md) packages state general lemmas with hypotheses. Treating all general theory as a wholly future discovery would understate the current position.

**Computational findings have led to structural explanations.** The final N34 heavy certificate was replaced by a [short hand argument](../../reviews/n34/2026-09-12-heavy-independent-v1/HAND_PROOF.md). The joint-routing study added 729 exact exclusions after reapplying the union of previous hand rules. Its destination term added information that aggregate receiving capacity lost. This is concrete evidence that inspecting certificates can expose useful graph structure. It is not a measured success rate for future research attempts.

**The preservation and checking reduce specific risks.** Numerical proposals are accepted only after exact arithmetic. Complete domains and surviving cases are retained. Separately structured implementations, original outputs and normalization audits make implementation mistakes easier to detect. These practices support the prospect of correcting a result even when its first implementation or exposition needs repair.

## Evidence limiting the forecast

**Common assumptions create correlated risk.** Much of the work depends on the [canonical bridge](../../research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md): quasi-edge selection, unique exceptions, injective residual charging and threshold capacity. Thousands of checked inequalities are not thousands of independent confirmations of those implications. One invalid graph-to-model step could invalidate many downstream certificates together. The balanced-degree witness argument provides some methodological diversity, but no part has received the external review assumed in this forecast.

**Real errors have occurred.** The [N29 audit](../../reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md) records a duplicated label multiplicity in an auxiliary model. The affected certificates were invalidated and a corrected route replayed. The [foundations audit](../../reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md) and latest [routing-tail audit](../../research/general_n/2026-09-12-routing-tail-projection-v1/AUDIT.md) preserve further corrections. Finding and fixing mistakes is evidence of an effective audit process and evidence that unreviewed mistakes remain possible; it should not be counted only as reassurance.

**The main remaining difficulty is structural.** The [scalar ceiling analysis](../../research/general_n/2026-09-09-profile-integral-7-12-v1/PROFILE_INTEGRAL_CEILING.md) places the current scalar-uniform architecture near a degree ratio of `0.582066`, already close to `7/12`. This is an architecture-specific limit with numerical reconnaissance in its evaluation, not a universal impossibility theorem. It nevertheless argues against expecting progressively sharper versions of the same scalar bound to reach the balanced-degree boundary. A growing intermediate-degree regime remains.

**Some proposed extensions actually fail.** The [step-back audit](../../reviews/general-theory/2026-09-12-stepback-v1/HOSTILE_AUDIT.md) records genuine clipping counterexamples by `a=23`. The latest projection supplied 114 additional whole-profile exclusions, but none among the 5,578 states surviving the preceding joint-routing catalogue. The scalar equality exclusions are a subset of those 114 and cannot be added again.

Those **5,578 are not unresolved cases in the current fixed-order candidate proofs**: their canonical envelope arguments already exclude them. They are survivors of the proposed general simplification. Their number is neither a count of actual graphs nor a percentage measure of distance to the unrestricted theorem. The zero result lowers expectations for further tuning of that tested refinement; it does not by itself justify a sharp project-wide downgrade.

## Published context and novelty limits

A bounded primary-source check supplies context, not a complete novelty review:

- [Haynes, Henning, van der Merwe and Yeo (2014)](https://link.springer.com/article/10.2478/s11533-014-0449-3) give maximum-degree conditions `0.7n`, and `0.6789n` for large enough order. Their abstract also records Fan's small-order results and Füredi's sufficiently-large-order result.
- [Bahjati et al., arXiv v2 (2016), Theorem 3.5](https://arxiv.org/html/1610.00360v2) states the condition `0.6756n`. Its abstract says `0.6755n`; this note uses the theorem's displayed constant and does not claim to audit that paper.
- [Dailly, Foucaud and Hansberg (2019)](https://arxiv.org/abs/1812.08420) provide structural results for graphs with a dominating edge and maximum degree `n-2`. Their [Theorem 4](https://arxiv.org/html/1812.08420v1) includes the exceptional graph H5, already accounted for in our foundations audit.
- [Loh and Ma](https://arxiv.org/abs/1406.6736) disprove a stronger average-edge-degree conjecture that had offered a route to Murty–Simon. This is a concrete warning that an attractive strengthening can fail while the original conjecture survives.

**Inference:** a correct and original `7/12 ≈ 0.5833` theorem would be a meaningful improvement over the explicit maximum-degree conditions just inspected. This is why a useful general contribution has a materially higher forecast than a further major advance. The inference is conditional: it does not certify that no later or differently formulated result subsumes it.

Direct retrieval of the Erdős Problems #742 page and the 2025 Lin–Wang publisher page returned HTTP 403. Indexed excerpts were available, but were not treated as a fresh full-page status check or a full-text audit. No comprehensive search, priority determination or claim of absence of competing work is made. The sufficiently-large-order theorem in the inspected literature also means that simply obtaining *some* infinite family is not automatically new or significant.

## How the numerical assessment was constructed

The central conditional judgments are:

| Step | Probability conditional on the preceding milestone | Judgment behind it |
|---|---:|---|
| Substantial correct mathematics | 90% initially | Explicit proofs and extensive exact checking, discounted for shared assumptions and external review still being open |
| Original and paper-worthy | 85% | Strong-looking candidate advances, discounted for unknown overlap with the literature and specialist significance judgment |
| Useful general theory | 85% | Several existing general candidates, allowing the possibility that only narrower results survive |
| Material further general advance | 60% | A productive extraction process and omitted compatibility information, balanced against demonstrated limits |
| Complete proof | 25% | Even after a further substantial advance, the whole remaining regime may resist this programme |

The conditional probability chain gives approximately `90%, 76.5%, 65.0%, 39.0%, 9.8%`. These become the rounded central estimates in the main table. **The conditional inputs are subjective choices, not frequencies inferred from certificates or fitted to research data.** This is an elicitation structure, not a trained forecasting model. Multiplication uses conditional probabilities and makes no independence assumption.

The cautious conditional inputs are `80%, 75%, 75%, 45%, 15%`; the favourable inputs are `95%, 95%, 95%, 75%, 35%`. They produce complete-proof estimates of roughly 3% and 23%, displayed coarsely as 3% and 25%. Both sets change several uncertain assumptions together. They are scenarios, not measured quantiles.

This also locates the dominant uncertainty. In the central model, granting substantial correct mathematics raises the complete-proof estimate only to about 11%. Granting a reviewed, original general contribution raises it to about 15%. Granting a material further advance raises it to 25%. Passing review of the foundations is essential, but would not establish the missing route to all orders.

Inputs are preserved in [forecast.json](forecast.json); exact chain arithmetic and a sum-to-one cross-check are in [arithmetic.json](arithmetic.json), regenerated with:

```sh
python project/assessments/2026-09-12-outcome-forecast-v1/evaluate_forecast.py
```

No statistical precision is claimed by the extra digits in that machine-readable output.

## Reconciliation of the earlier answers

The first answer in this conversation assigned exclusive outcomes of 5% complete proof, 25% substantial further general theorem, 55% useful partial work, and 15% mainly exploratory value. That implied 30% at least a substantial further theorem and 85% at least useful partial work. It gave no operational horizon and blurred the distinction between validating existing general candidates and discovering further theory.

The next answer withdrew 5% as a justified update from the previous day's estimate. That withdrawal did not establish a higher probability. Attempts to retrieve the exact 11 September numerical estimates failed; no replacement historical numbers are invented here.

This note supersedes those conversational estimates **for its explicitly defined scenario**. Its approximately 10% full-proof midpoint is a revised judgment, not evidence that the project doubled its prospects during this assessment. The 5% figure lies within the broad sensitivity scenarios. Likewise, the 75% paper-worthy estimate is not an evidenced fall from the earlier 85% generic partial-work figure: the event, deadline and standard are now more specific. Comparisons to yesterday remain incomplete until its actual wording and conditions are available.

## Rules for future updates

1. Keep the event definitions and horizon fixed when reporting a change. If the workload, review assumption or horizon changes, label a new scenario rather than a gain or loss in mathematical confidence.
2. Identify the new evidence and the particular conditional step it affects. Do not revise all outcomes because one pilot succeeds or fails.
3. Independent review of the shared bridge mainly changes correctness confidence. Specialist comparison with prior work changes originality confidence. A uniform theorem in the intermediate-degree regime changes the later progress and complete-proof estimates.
4. A repairable local bug and a false shared implication have different consequences. Trace dependencies before changing probabilities. A failed refinement is not a failed conjecture.
5. Repeated exact replays, more commits and more exclusions from an already covered finite pool are not independent probability updates. Count novel information and retain negative experiments.
6. Do not turn three successful lemmas into three independent chances of solving the problem. Do not extrapolate from orders 25–35 to arbitrary order or treat the surviving-state count as distance to completion.

The most informative next evidence remains a substantive external foundations review and a bounded compatibility experiment that adds information beyond the current joint-routing model. No new research pilot, external message or review request was undertaken during this assessment.
