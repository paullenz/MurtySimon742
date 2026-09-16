# Strategic reassessment: from exact boundary cases to shared residual budgets

16 September 2026. User-requested step back after the residual-endpoint cap.

**Status: STRATEGY_REASSESSMENT_NOT_A_NEW_PROOF.** Inspected main `da6d0dd04224cfaf4bf6212c02c5d9dc34851e23`. No proof, computational result, catalogue exclusion, promotion gate or reviewer package is changed. Proposed generalizations below are research targets, not established theorems. The existing mathematical checkpoint remains conditional and internally reviewed only.

## 1. Recommendation

Do not make another one-unit improvement of the d=5 threshold the default objective. Retain the Omega=34 pattern as a diagnostic example, while prioritizing a parameterized obstruction that accounts jointly for forced residual presence, label demand and shared destination capacity. It should survive a controlled loss of exact tightness and be tested against configurations outside the latest special family.

This is not abandonment of the canonical construction. It is a change in what the next unit must explain. A useful result should either establish a shared-budget inequality beyond one equality pattern or expose a precise feasible relaxed obstruction showing which graph property is still missing.

## 2. What the accumulated evidence supports

The latest local statement, s_k<=d-2 for k in K under |T|=|H|=d, is more strategically valuable than its d=5 threshold alone. Its proof uses two low endpoints and forced residual presence at all high sources. The more general form is already in the endpoint-cap proof: if a label is residual at r0 specified sources and every other source has residual degree at most c, then its demand is at most max(0,2c-r0). This is an existing conditional corollary, not a new claim of this review.

Earlier examples tell a consistent story. Independent aggregate capacities may all appear sufficient while their label identities and competing uses make simultaneous routing impossible. The forced-core receiver partition proof, one-hole source confinement, two-hole destination obstruction and endpoint cap preserve different parts of that coupling. The endpoint inequality itself was already in canonical bridge Section 6.2. Its later stronger application is a reason to inventory which proved constraints each relaxation discards before inventing further elaborate relaxations.

There is already an exact fixed-cross-neighbourhood B-side flow criterion. We should reuse it, not describe max-flow/Hall or a new flow implementation as the missing discovery. Its scope is crucial: it does not certify the A-side graph, A-side domination, or full edge-criticality, and rejection of one fixed cross pattern is not exclusion of all patterns with the same scalar data.

## 3. The three outstanding logical gaps

(1) **Coverage.** The recent numerical chain assumes exactly d demand-d labels and exactly d eligible high sources. There is no established theorem in the material reviewed here that every putative counterexample admits such a block. Solving every d=5 equality pattern would not remove this hypothesis.

(2) **Rigidity versus exclusion.** E=0 only forbids extra high-source selections. A proof still has to eliminate the rigid branch or use it to obtain the desired edge bound. This distinction applies even if an improved inequality covers many more values of a.

(3) **One shared budget.** For d=5 in the extra-selection branch, the exact identity is

    4a+5-b-2tau = 70+Omega+alpha+sigma_H+sigma_O.

Optimizing Omega while separately discarding the remaining nonnegative terms can conceal the actual obstruction: a configuration may lower one term only by increasing another. The next theorem should control a joint expression, not simply exclude the current Omega minimizer and restart at its successor. Local residual-incidence injections are not automatically disjoint across different labels. Any global charging argument must prove its reuse/congestion bound.

## 4. Keep the true counterexample surplus in the model

The canonical surplus is tau=e(G)-b(n-b), with n=a+b+1 and b=Delta(G). Define

    g(n,b)=floor(n^2/4)-b(n-b)=floor((b-a-1)^2/4).

The identity follows from n^2-4b(n-b)=(n-2b)^2 and the integrality of b(n-b). An upper-bound counterexample must satisfy

    tau>=g(n,b)+1,

not merely tau>=1. For example, b-a-1=8 gives g=16 and hence tau>=17. Equality at the Murty-Simon bound corresponds to tau=g, not necessarily tau=0.

Using tau>=1 in the earlier corollaries is valid; it is not a defect in those proofs. However, strategic comparisons and catalogue tests should retain the actual g and tau rather than comparing only the simplified threshold tables. Proving tau<=0 everywhere would be stronger than is needed for the conjectured upper bound. This review does not assert that stronger statement to be true or false.

## 5. Main mathematical target: a shared-capacity inequality with controlled defect

Start with the general residual-support endpoint cap and the existing labelled destination sets. Retain the actual source/destination residual degrees, not just the largest allowed degree. Couple the available destinations through their shared capacities. Seek an exact integer or rational certificate for the total cost, with an explicit bound on reuse of every charged residual incidence.

The first test is the Omega=34 pattern, but the theorem should be stated before specializing to h=2,L=0 or d=5. At a minimum it should explain what cost is forced when label selection is slightly unsaturated. Do not assume the destination sets or beta terms remain those of equality.

To make the loss of exact tightness measurable, fix a threshold d, put H_d={u:rho_u>=d}, and take a label set I with s_i>=d for every i in I. Define

    D(I)=|I|*|H_d|-sum_(i in I)s_i.

Every selected occurrence of a label in I belongs to H_d. Since x_i>=s_i, the total number of missing selected incidences in H_d x I is

    |I|*|H_d|-sum_(i in I)x_i <= D(I).

This elementary omission count is only a starting point. D=0 forces a full selected rectangle, while small D bounds the total number of omissions. It does NOT by itself reproduce the K-residual property, force a useful rectangle in every graph, or bound the number of all other labels. Those require proofs. In particular, one cannot export the exact-block endpoint cap to a defective block without recovering the requisite forced residual support.

The proposed general route is a structural alternative: either a sufficiently concentrated/near-tight family gives a quantitative residual/destination obstruction, or a sufficiently diffuse assignment contradicts a global capacity bound. No such exhaustive alternative has yet been established. Producing or falsifying it is more relevant to an unrestricted proof than another isolated threshold increment.

## 6. Use computation to choose and falsify the next theorem

The immediate diagnostic should classify the current candidate space by hypotheses, rather than infer coverage from the number of small scalar tests. Record which records force a tight block, which only admit one for a particular witness, which remain diffuse, and which already fall to an applicable endpoint or joint-capacity condition. We have not performed this new coverage census in this review.

Use the existing 952-state catalogue and separately recorded unpromoted certificates without conflating their namespaces. A rejected witness is not a whole-state rejection; a finite catalogue is not a classification for all n. Preserve one smallest non-rejection per structural type. Reuse exact min-cut certificates for fixed cross patterns, and derive any required projection back to all permitted patterns before promoting a state.

For source-level audit, test primitive graph-to-model implications on directly checked diameter-two edge-critical graphs, applying each statement only where its hypotheses hold. This is a different check from enumerating arrays that already assume those implications. Such testing remains finite evidence, and external review of the bridge is still required. Do not turn tests into a claim of independent mathematical acceptance merely because another language is used.

## 7. A genuinely different reserve direction: choose representatives strategically

The full representative system is chosen, not unique. With the graph and pivot fixed, the total residual count r=e(F)-tau is fixed while its distribution can vary. A possible reserve direction is to choose representatives minimizing a convex residual-load potential and investigate the resulting exchange restrictions.

Only changes between actual valid quasi-edge representatives are allowed; arbitrary orientation changes do not preserve the construction. The purpose would be to force a more useful normal form or expose irreversible pairs, not to assume every graph can be made to have an exact tight block. This direction has not been developed or computationally tested in this review. Prioritize it if a well-posed shared-budget/defect formulation retains a structurally diffuse family that the current machinery does not explain.

## 8. Success criteria and stopping rule

Primary success: a conditional theorem accounting jointly for demand and residual/destination cost over a parameterized family, with explicit assumptions and multiplicity accounting. Stronger success: a theorem forcing its applicability, or a controlled-defect extension and a genuinely exhaustive remaining branch.

Useful negative success: a fully specified relaxed family that satisfies the proposed joint inequalities but cannot be ruled out by them, identifying the missing original-graph constraint. Do not call it a counterexample to Murty-Simon unless it is independently checked as an original diameter-two edge-critical graph exceeding the actual bound.

If the next attempt only rules out one exact minimizer without a quantitative extension, preserve it, but do not automatically spend the following unit on the next integer. Reassess against the shared-budget objective. Do not restart a larger unstructured MILP merely because a compact theorem is not immediate.

## 9. Sources and trust boundaries

Repository sources read at da6d0dd04224cfaf4bf6212c02c5d9dc34851e23:

- CURRENT_STATE.md; predecessor blob 50f580999215236f825b893dd6bacd14f7cd0050.
- project/research/general_n/2026-09-16-residual-endpoint-cap-v1/PROOF.md.
- project/research/general_n/2026-09-12-arc-realisation-pilot-v1/FIXED_NEIGHBOURHOOD_FLOW.md.
- project/research/general_n/2026-09-15-forced-core-capacity-v1/README.md.
- README.md, live overview and current-research-chain sections (historical update lines are not fresh workflow checks).
- releases/general-7-12-reviewer-v1/README.md: existing candidate high-degree theorem; independent review/novelty open.

External primary-source orientation was checked against Dailly-Foucaud-Hansberg, 'Strengthening the Murty-Simon conjecture on diameter 2 critical graphs', arXiv:1812.08420, and Wang-Zhang-Zhu, 'Improved bound on the number of edges of diameter-k-critical graphs', arXiv:2409.17491. Both report the already-known sufficiently-large-order result. This limited literature check is not a novelty audit of our framework. Another asymptotic assertion alone would not settle the missing exact cases.

Canonical status remains 4,626 exclusions / 952 survivors / 3,632 whole-state closures. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. This strategic note does not rerun their evidence or change their scope. The mathematical endpoint-cap result remains internal and conditional. No new generalized bound, statistical success probability or schedule is asserted.
