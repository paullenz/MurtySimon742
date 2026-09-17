# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has D>=12. Scope work now includes a global selected-witness Hall theorem: the excess-aware one-source envelope cannot reuse the same selected label independently across arbitrarily many active B-sources.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_SELECTED_WITNESS_HALL_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Stepped back before following the proposed coordinate-by-coordinate census. The higher-value missing structure was global selected-label reuse: the current excess-aware source envelope optimises each B-source independently even though label `i` has only `x_i` selected incidences in total.

**INSPECTED PREDECESSOR:** `6119f94ac96ca7e35fa7d772d95686bbeaea58fc`, tree `a970e38a6e37fbcf8bf9142312f1bb20aa4673d1`, confirmed current main before this transaction. Its certified empty uniform h=5 demand-four band, excess-aware source envelope, common-margin cut, scalar obstruction, staircase/heavy-load theory, five-label D>=12 theorem and canonical counts remain unchanged.

**LAST RESULT:** for fixed source loads `(p_u,q_u,rho_u)`, call `u` active when `q_u>0` and define admissible witness labels

`N(u)={i:s_i<=rho_u, e_i>=max(0,p_u-rho_u+1), C_i>=p_u+q_u}`.

Every active source has an actual selected incidence, every such incidence obeys those conditions, and label `i` has exactly `x_i` selected incidences. Choosing one selected witness per active source therefore gives a capacitated matching into the labels. Hence for every active-source subset `S`,

`|S| <= sum_{i in union_{u in S}N(u)} x_i`.

A cheap nested corollary is

`#{u:q_u>0, rho_u<=d} <= sum_{i:s_i<=d} x_i`,

with stronger endpoint/excess threshold versions and a layer-cake bound on low-residual outgoing load. This is a genuine global strengthening of the one-source envelope because it restores finite reuse multiplicity of compatible selected labels.

**STRICTNESS TEST:** an explicit bridge-level profile with `a=10,b=20,t=0,Q=29`, labels `(s,x,R,C)=(2,2,4,6)` and nine labels with `s=x=3` (two `R=2,C=5`, seven `R=3,C=6`), sources `rho=(3^5,2^7,0^8)`, and displayed `p,q` vectors satisfies the scalar ledger, exact selected/residual margins on disjoint pairs, all displayed selected-edge demand/excess/endpoint inequalities, incoming caps, and the excess-aware local source envelope. Nevertheless all seven `rho=2` sources have `q>0`, while only the demand-two label can witness them and it has selected capacity `x=2`. The Hall cut is `7<=2`, deficiency 5. Thus the new theorem separates the shared-incidence bridge from the local-envelope relaxation exactly.

**AUDIT:** `project/research/general_n/2026-09-17-selected-witness-hall-v1/` contains the proof and an exact Python replay with explicit selected and residual incidence matrices. The checker verifies all stated margins/local inequalities and the Hall deficiency. This is internal derivation/replay, not external review.

**STEP-BACK CONSEQUENCE:** the preceding uniform demand-four band did not need this theorem because low-demand selected capacity there is abundant. Its natural target is the next frontier: mixed demand 4/5 and positive selected excess, where low-demand witness incidences can become scarce. Therefore a blind histogram expansion is no longer the preferred next move; the mixed-demand frontier should be searched only after adding the nested Hall cuts, and the full capacitated witness matching should be invoked on the small residual candidate set.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` still satisfies `D>=12`, hence `W>=37` or `W>=57` with extras.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No canonical catalogue scan, q-enumeration or theorem promotion.

**PRESERVATION:** selected-witness Hall theorem and checker are in `project/research/general_n/2026-09-17-selected-witness-hall-v1/`; the uniform-band package remains in `project/research/general_n/2026-09-17-h5-uniform-band-v1/`; the excess-aware envelope remains in `project/research/general_n/2026-09-17-excess-aware-endpoint-v1/`. Earlier proofs, obstructions and failed routes remain preserved.

**UNPRESERVED WORK:** None for this bounded theorem/strictness package after remote confirmation.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: integrate the selected-witness Hall cuts into the near-Turan mixed demand 4/5 frontier at `(a,b,t)=(20,23,2)` before expanding the census. First exploit the cheap nested demand/endpoint/excess thresholds to derive a projected DP or finite screen; apply full capacitated matching only to survivors. Preserve either the smallest profile surviving both the excess-aware envelope and witness Hall, or a certified empty mixed-demand sub-band. Reassess before broadening parameters.
<!-- CURRENT-STATUS:END -->
