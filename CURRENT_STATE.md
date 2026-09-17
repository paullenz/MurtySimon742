# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has `D>=12`. Exact selected-incidence Hall majorization now completely closes the mixed demand-4/5 near-Turán frontier at `(a,b,t)=(20,23,2)` across **all** total selected excess values `E`; no `E>=10` survivor remains.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_MIXED_45_FRONTIER_CLOSED_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Critically reassessed the E=10 continuation before running another level-by-level search. The Hall threshold family compresses through capped ramps, and three range-uniform certificates close every arithmetically possible remaining excess level at once.

**INSPECTED PREDECESSOR:** `8661c9e9baf6d60297ff4e9294ad5dc23a5eb3a1` plus the preserved E=9 Hall-majorization package. All E<=9 packages, full selected-incidence Hall, quadratic endpoint work, common-margin/staircase/heavy-load results and the five-label `D>=12` theorem remain preserved.

**EXACT INCIDENCE FACTS:** for every selected incidence `ui`,

`s_i<=rho_u`, `e_i>=g_u=max(0,p_u-rho_u+1)`, `C_i=R_i+x_i>=w_u=p_u+q_u`.

Selected-label distinctness gives `q_u g_u<=E`. Full capacitated Hall remains valid on the eligibility graph. At `(a,b,t)=(20,23,2)` with `k` demand-five labels,

`r=76+k`, `Q=80+E+k`, and `sum p=sum q=Q`.

**HALL COUNT MAJORIZATION:** for every threshold `T`,

`sum_{w_u>=T} q_u <= sum_{C_i>=T} x_i`,

and

`sum_{rho_u=4}q_u <= sum_{s_i=4}x_i`.

Define the capped ramp

`H_L(z)=max(0,min(z,L)-4)=sum_{T=5}^L [z>=T]`.

Any nonnegative combination of these ramps is therefore a valid Hall potential.

**NEW RANGE-UNIFORM CLOSURE:**

- `10<=E<=15`: use `Phi=4H_9+12H_12+4H_19`, demand-four weight `mu=33`. Exact local support inequalities sum to contradiction gap `60E-580>=20`.
- `16<=E<=21`: use `Phi=5H_9+19H_14`, `mu=40`. The summed gap is `47E-750>=2`.
- `22<=E<=42`: use `Phi=6H_8+24H_15`, `mu=46`. The summed gap is `47E-k-1006>=8`.

The incoming cap `p_u<=rho_u+2` gives globally

`Q<=r+46`,

hence `80+E+k<=122+k` and therefore

`E<=42`.

So the three ramp bands cover **every** possible `E>=10`.

**CURRENT RESULT:** combining the new theorem with the preserved `E=0,...,9` closures gives

> **No canonical bridge in the established mixed demand-4/5 near-Turán scope `(a,b,t)=(20,23,2)` survives at any total selected excess `E`.**

The new E>=10 argument itself does not require the older `h>=5` hypothesis. The combined all-E statement retains whatever scope assumptions are required by the E<=2 predecessor.

**AUDIT / PRESERVATION:** `project/research/general_n/2026-09-17-hall-ramp-all-excess-v1/HALL_RAMP_ALL_EXCESS.md` contains the structural proof. `check_hall_ramp_all_excess.py` independently enumerates every local integer source/label state for the three range certificates, checks every global `(E,k)` gap exactly, and verifies the global `E<=42` cap. External mathematical review remains open.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` still satisfies `D>=12`, hence `W>=37` or `W>=57` with extras.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No catalogue scan, q-enumeration or conjecture-level promotion was used for the new closure.

**STRATEGIC CONSEQUENCE:** do **not** continue to `E=43`; there is no such case. The selected-excess dimension of this mixed `{4,5}` frontier is exhausted. The next structural target is to determine whether remaining near-Turán bridge scope can be forced into the now-closed `{4,5}` demand support, or whether the Hall-ramp theorem generalizes cleanly to the next demand-support patterns. Prefer a compact support-reduction/generalization theorem over survivor-by-survivor exclusions.

**AUTOMATION STATUS:** scheduled research continuation is active; cadence is managed outside the repository.

**UNPRESERVED WORK:** none required for the all-E mixed `{4,5}` closure. Exploratory optimization used to discover the three ramps is not proof-relevant; the committed replay checker uses exact integer arithmetic only.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: step back from selected-excess enumeration and inventory the exact remaining scope between the general h-index/receiver bridge and the closed mixed `{4,5}` frontier. Seek either (i) a structural reduction forcing the next near-Turán obstruction into demand support `{4,5}`, or (ii) a demand-support-general Hall-ramp theorem. Do not return to catalogue scans unless needed as a diagnostic for the structural statement.
<!-- CURRENT-STATUS:END -->
