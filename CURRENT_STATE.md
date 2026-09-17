# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has `D>=12`. Scope work now retains exact selected-incidence multiplicities, full capacitated Hall, restricted quadratic endpoint layers, and Hall-count majorization. In the mixed demand-4/5 near-Turán frontier at `(a,b,t)=(20,23,2)`, total selected excess `E=0,...,9` is internally excluded; any survivor in the established scope must have `E>=10`.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_HALL_MAJORIZATION_BARRIER_E10_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Continued the exact-incidence scope attack without returning to the canonical survivor catalogue. E=9 initially defeated the endpoint-load affine potential hierarchy, but the exact selected-incidence **count** Hall thresholds supplied the missing information and compressed to a one-line uniform contradiction.

**INSPECTED PREDECESSOR:** `89386b81b31265e818fc0edf98e1f0420a92f25f` plus the preserved E=9 Hall-majorization package. All E<=8 packages, full selected-incidence Hall, quadratic endpoint work, common-margin/staircase/heavy-load results and the five-label `D>=12` theorem remain preserved.

**EXACT INCIDENCE FACTS:** for every selected incidence `ui`,

`s_i<=rho_u`, `e_i>=g_u=max(0,p_u-rho_u+1)`, `C_i=R_i+x_i>=w_u=p_u+q_u`.

Selected-label distinctness gives `q_ug_u<=E`. Full capacitated Hall remains valid on the eligibility graph.

**E=5 THROUGH E=8:** preserved unchanged. E=5 has gap `63+2k`; E=6 has constant gap `12`; E=7 has `190-9k>=10`; E=8 has constant gap `4`. See the corresponding dated packages and replay checkers.

**E=9 NEW STRUCTURAL LAYER — HALL COUNT MAJORIZATION:** endpoint eligibility alone gives, for every threshold T,

`sum_{w_u>=T}q_u <= sum_{C_i>=T}x_i`.

Demand compatibility also gives

`sum_{rho_u=4}q_u <= sum_{s_i=4}x_i`.

Define

`phi_9(z)=2[z>=6]+[z>=7]+2[z>=8]+[z>=9]+[z>=10]+[z>=11]+[z>=12]+[z>=13]+[z>=14]+[z>=16]+[z>=18]`.

Take two copies of the demand-four count inequality plus the endpoint-threshold Hall combination encoded by `phi_9`. With

`omega_B=2[rho=4]+phi_9(w)`,
`omega_A=2[s=4]+phi_9(C)`,

every actual bridge satisfies

`sum omega_B q <= sum omega_A x`.

Exact local support inequalities are

`omega_B q >= 9p+16q-17rho-10`,

`omega_A x <= 8+5R+3[s=5]+18e`.

Summing at E=9 (`Q=89+k`, `r=76+k`) gives a **constant contradiction gap 1** for every `k=0,...,20`. Thus E=9 is impossible.

**CURRENT BARRIER:** combining all preserved results gives

> **Any surviving mixed demand-4/5 near-Turán bridge in the established scope must have total selected excess `E>=10`.**

The E=3,...,9 closures themselves do not require the original `h>=5` hypothesis; the combined statement retains whatever scope assumptions are still needed by the E<=2 predecessor.

**DISCOVERY / FAILURE RECORD:** before Hall-count majorization was introduced, the complete affine endpoint-load potential cone failed for E=9 on `k=5,...,18`, even with all endpoint/excess/demand intersections. A threshold-Hall histogram relaxation was then found infeasible for all 21 k values; its LP relaxation was also infeasible. Dual compression yielded the short `phi_9` certificate above. This preserved failure is important: count majorization contains information that weighted endpoint-load sums alone discard.

**AUDIT / PRESERVATION:** `project/research/general_n/2026-09-17-e9-hall-majorization-v1/E9_HALL_MAJORIZATION.md` contains the structural proof; `check_e9_hall_majorization.py` checks every local source/label state and the constant global gap 1. E5/E6/E7/E8 packages and all earlier work remain preserved. External mathematical review remains open.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` still satisfies `D>=12`, hence `W>=37` or `W>=57` with extras.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No catalogue scan, q-enumeration or conjecture-level promotion.

**AUTOMATION STATUS:** the hourly Murty-Simon research automation remains deliberately paused per the user's noon instruction. Other alerts were not altered; research continues manually in the active chat.

**UNPRESERVED WORK:** exploratory E=10 coefficient searches are not yet frozen; no `E>=11` claim.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: test E=10 first against the same Hall-count architecture (endpoint thresholds plus demand-four capacity) with exact local condition `q_ug_u<=10`. Search for a short integer Hall staircase and affine local support inequalities. If no such uniform certificate exists, escalate to excess-threshold/full subset Hall only after preserving the first exact obstruction. Do not broaden demand support until this mechanism is understood.
<!-- CURRENT-STATUS:END -->
