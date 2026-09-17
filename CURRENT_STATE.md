# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has `D>=12`. Scope work now retains exact selected-incidence multiplicities, a full capacitated Hall theorem, and a restricted quadratic endpoint method that rules out total selected excess `E=0,1,2,3` in the mixed demand-4/5 near-Turán frontier at `(a,b,t)=(20,23,2)`.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_E3_RESTRICTED_QUADRATIC_CLOSURE_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Reconciled the concurrent `E=3` partition-reduction work with a stronger restricted-incidence potential. The split-partition proof remains useful and its corrected failed coefficient attempt is preserved, but the new argument closes **all three** excess partitions uniformly, including the formerly unresolved unique `(3)` case.

**INSPECTED PREDECESSOR:** `a70339b81f3cb25afd93353d6eba0818b1e3f07f`, which hand-closes `(2,1)` and `(1,1,1)` and reduces `E=3` to a unique excess-three label. Its corrected proof/checker and the explicitly preserved failed `10p+15q` attempt remain unchanged. The full selected-incidence Hall theorem, `E<=2` barrier, quadratic endpoint work, earlier Hall/common-margin/staircase/heavy-load packages and five-label `D>=12` theorem remain preserved.

**GENERAL RESTRICTED QUADRATIC LEMMA:** the global endpoint ledger is

`sum_u q_u(p_u+q_u) <= sum_i x_i C_i`.

Restricting to selected incidences sourced at `rho_u=4`, demand compatibility forces their labels to have `s_i=4`, hence

`sum_{rho_u=4} q_u(p_u+q_u) <= sum_{s_i=4} x_i C_i`.

Multiply the global inequality by six and add the restricted one. Define

`K_B=sum_u (6+[rho_u=4])q_u(p_u+q_u)`

and

`K_A=sum_i (6+[s_i=4])x_i C_i`.

Every actual bridge satisfies

`K_B<=K_A`.

This is a demand-restricted projection of the exact selected-incidence matrix: stronger than the undifferentiated quadratic ledger but much cheaper than full Hall.

**E=3 UNIFORM HAND CLOSURE:** total excess `E=3` and distinct selected labels at each source imply

`q_u g_u<=3`, where `g_u=max(0,p_u-rho_u+1)`.

Using only the canonical local caps, every source satisfies

`(6+[rho=4])q(p+q) >= 60p+102q-79rho-104`.            (S)

The complete active local ranges have positive minimum slack: for `rho=4`, the minima at `g=0,1,2,3` are `6,21,60,7`; for `rho>=5` they are `7,37,79,25`. Thus (S) covers the unique `g=3,q=1` states that escaped the preceding split-partition argument.

Every label, using `d_i=R_i+s_i<=19` and `e_i<=3`, satisfies

`(6+[s_i=4])x_i C_i <= 112+30R_i+38[s_i=5]+172e_i`.  (L)

For `s=4`, right minus left is `(2-7e)R+116e-7e^2>=0`; for `s=5`, it is `e(112-6R-6e)>=0`.

Summing (S) over the 23 sources and (L) over the 20 labels gives

`K_B >= 162Q-79r-2392`,

`K_A <= 2756+30r+38k`.

At `E=3`,

`Q=83+k`, `r=76+k`.

Therefore the necessary inequality `K_B<=K_A` would require

`14+15k<=0`,

which is impossible for every `k=0,...,20`.

Hence **all three `E=3` excess partitions are impossible**, including the unique `(3)` case left open by the concurrent partition-reduction checkpoint.

**CURRENT BARRIER:** combining the earlier `E<=2` hand theorem with this result gives

> **Any surviving mixed demand-4/5 near-Turán bridge in the established scope must have total selected excess `E>=4`.**

The `E=3` argument itself does not require the earlier `h>=5` assumption; the combined statement retains whatever scope hypotheses are needed by the `E<=2` predecessor.

**FULL SELECTED-INCIDENCE HALL:** remains available and unchanged. For eligibility `s_i<=rho_u`, `e_i>=g_u`, `C_i>=p_u+q_u`, the actual simple selected-incidence matrix has exact row degrees `q_u` and column degrees `x_i`, hence for every source subset `S`,

`sum_{u in S}q_u <= sum_i min(x_i, |{u in S:i eligible at u}|)`.

Its row corollary requires each source to have `q_u` distinct compatible labels. The restricted quadratic lemma above is a weighted projection of this exact incidence structure.

**AUDIT:** `project/research/general_n/2026-09-17-e3-restricted-quadratic-v1/E3_RESTRICTED_QUADRATIC.md` contains the uniform hand proof. `check_e3_restricted_quadratic.py` exhaustively checks the complete local source and label integer domains and all 21 final gaps. Independent replay returned `PASS_E3_RESTRICTED_QUADRATIC`. The corrected split-partition proof/checker remain preserved in `2026-09-17-e3-partition-reduction-v1/`; their failed first coefficient choice is deliberately retained. Full selected-incidence Hall remains in `2026-09-17-full-selected-incidence-hall-v1/`; `E<=2` proof/checker remain in `2026-09-17-small-excess-quadratic-v1/`. External mathematical review remains open.

**STEP-BACK CONSEQUENCE:** the significant pattern is the restricted-incidence weighting, not the numerical value three. The combination `6*(global quadratic)+(rho=4 restricted quadratic)` admits simple local potentials and yields a contradiction uniform in all 21 demand mixtures. The next high-value question is whether the coefficients can be parameterized in total excess `E`, rather than advancing one excess value at a time.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` still satisfies `D>=12`, hence `W>=37` or `W>=57` with extras.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No canonical catalogue scan, q-enumeration or conjecture-level promotion.

**PRESERVATION:** uniform E3 closure/checker are in `project/research/general_n/2026-09-17-e3-restricted-quadratic-v1/`; corrected split-partition work in `2026-09-17-e3-partition-reduction-v1/`; full selected-incidence Hall in `2026-09-17-full-selected-incidence-hall-v1/`; small-excess barrier in `2026-09-17-small-excess-quadratic-v1/`; all earlier structural/audit packages remain preserved.

**UNPRESERVED WORK:** exploratory `E=4+` coefficient searches are diagnostic only until frozen; no `E>=5` claim yet.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: seek a parameterized restricted-quadratic potential for `E>=4`. Start with `E=4`, where `q_ug_u<=4`; search for small integer source/label potentials using the same global plus demand-restricted ledgers, then derive them by hand. If `E=4` closes, test whether the coefficients interpolate in `E`; if the method fails, preserve the smallest exact incidence-level obstruction. Do not broaden demand support until this excess mechanism is understood.
<!-- CURRENT-STATUS:END -->
