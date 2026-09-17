# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has D>=12. Scope work now includes a strict excess-aware endpoint-orientation envelope: incoming load changes which selected labels are actually available at a source, and this yields genuinely stronger common-margin cuts than the preceding `2Q` ceiling.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_EXCESS_AWARE_ENDPOINT_ENVELOPE_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Completed one bounded common-margin refinement and a strict abstract test; no survivor scan or workflow launch.

**INSPECTED PREDECESSOR:** `b6fe88b7c84c111786a2cfc111ccf97178353a79`, tree `ff2514e0fcc4fab4a40fb91741c5727d76af9a1c`, confirmed current main immediately before this transaction. Its global endpoint-orientation cut, scalar obstruction, staircase/receiver/h-index results, five-label D>=12 theorem and canonical counts remain unchanged.

**LAST RESULT:** define selected excess `e_i=x_i-s_i`. For each source u and incoming load p, retain only labels with `0<s_i<=rho_u` and `e_i>=max(0,p-rho_u+1)`, then let `A_u(p)` be the largest outgoing q allowed by endpoint mass `p+q<=C_i` and pair cap `p+q<=b-1`; include q=0. Every legal source has `q_u<=A_u(p_u)`. Therefore

`Q <= max{sum A_u(p_u): 0<=p_u<=P_u^0, sum p_u=Q}`,

where `P_u^0=min(b-1,rho_u+b-a-1)`. More generally, for nonnegative integer weights alpha,beta,

`(alpha+beta)Q <= sum_u max_p[alpha A_u(p)+beta p]`.

This is an exact one-dimensional source-envelope projection of the stated common-margin bridge facts; it is stronger than maximizing endpoint mass independently of incoming load.

**STRICTNESS TEST:** a new abstract non-square profile has `a=20,b=23,t=2,Q=80`, `rho=(5^7,4^8,2,1^7)`, twenty labels with `s=x=4`, `R=(5,4^14,3^5)` and `C=(9,8^14,7^5)`. The preceding global endpoint cut passes **at equality**: `sum B=160=2Q`. Because every label has zero selected excess, the `(alpha,beta)=(2,3)` excess-aware support cut has source maxima 22 on rho-5, 21 on rho-4, 12 on rho-2 and 9 on rho-1, so

`sum H=7*22+8*21+12+7*9=397 < 400=5Q`.

Thus the excess-aware refinement is strictly stronger than the preceding common-margin cut. The exact incoming-total DP allows at most 78 outgoing units at incoming total 80. The profile also passes basic Erdős-Gallai and residual Gale-Ryser checks; it is still only an abstract bridge profile, not a graph realization.

**AUDIT:** `project/research/general_n/2026-09-17-excess-aware-endpoint-v1/` contains the general proof, Python exact envelope/degree checker, separately structured C++ arithmetic/DP checker and pinned summary. Both checkers reproduce `basic=160`, `weighted=397`, exact outgoing maximum 78.

**STEP-BACK CONSEQUENCE:** selected excess is now confirmed to add real non-decoupled information. The next question is not whether to keep this refinement, but what survives it. Search the abstract non-square frontier after the full envelope before paying the cost of pair-choice/target-capacity/selected-incidence Hall. If a survivor exists, preserve it as the next obstruction; if a justified band is empty, extract a short weighted cut from the active support-function certificates.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` still satisfies `D>=12`, hence `W>=37` or `W>=57` with extras. Nothing here weakens that theorem.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No canonical catalogue scan, q-enumeration or promotion in this unit.

**PRESERVATION:** new theorem/checkers are in `project/research/general_n/2026-09-17-excess-aware-endpoint-v1/`. The predecessor common-margin cut remains at `project/research/general_n/2026-09-17-global-endpoint-orientation-v1/`; all earlier structural and negative results remain preserved.

**UNPRESERVED WORK:** None for this bounded theorem/audit after remote confirmation.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: search the abstract non-square frontier that satisfies the staircase/heavy-load constraints, the basic common-margin cut and the full excess-aware envelope. Start with the near-Turan h=5 bands and preserve the smallest exact survivor or a certified empty band. Do not begin with the canonical 952-row catalogue; the purpose is to understand the general structural obstruction first.
<!-- CURRENT-STATUS:END -->
