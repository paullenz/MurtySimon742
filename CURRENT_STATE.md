# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-20  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_R1_K2_HALF_RAY_PRIVATE_FOOT_HU_FORCING_2026_09_20`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `7e6c442a09eb6b5969571398c603cae8d2dfeb4f`; before forward mathematics this invocation reread CURRENT_STATE.md, README.md, latest commits, the 20 September daily red-team audit, residual-one/low-k profiles, general Y--U capacity, rooted/score ledgers, H/Y polarization and H--H certificate split. The audit gate remained binding.

LAST VERIFIED RESULT: `The off-ray chain was hostile-replayed and inserted into a normalized variable ledger. For bounded ratios theta=y/p, kappa=c/p, eta=b/p and q=C/p^2, Y0=eta theta+max{0,theta(kappa-2eta),(q/eta)^2} and Z0=max{kappa theta+eta,eta+Y0}; every asymptotic survivor must satisfy F=Z0+Y0+kappa(kappa-theta)-2q <= S0=((1+kappa)^2-theta^2)/2, while rooted-Q feedback forces kappa>=sqrt(2(theta^2+theta+1))-(1+theta). At theta=1 the score gap is strictly positive for every kappa>0 by a complete three-case proof, so the bounded-ratio high-Y endpoint is closed. The first simple intermediate direction theta=kappa=1/2 has an exact family p=2t,c=y=t,lambda=2t-1,u=t+1,x=2t+1,k=2,m=2t-1. A same-session hostile replay caught and corrected the impossible literal assignment b=0: selected witnesses W_s lie in B0, so b>=2; the corrected minimal assignment is b=2, B0=W_s, with C=e(B0,D)<=2(t-1). This corrected ray still survives score, rooted-Q, exact Ccap_P, ONE-P and CROWD with quadratic margin; e(Y)=0, e(Y,U)=O(p), e(U)=O(p). H-side localization gives at most u triangle-free H--U edges. For triangular t h_i, no t-sourced U witness is possible; if d_H(t)>=2 no t-sourced Y witness is possible; if also d_Y(t)>0 no A_X witness is possible. NEW: in that H-multi/Y-active t-sourced case the matched witness is forced to the private foot q_i. Therefore N(t) cap N(q_i)={h_i}; writing U_i^-={w in U:c(w)_i=bar(d)_i}, this forces N_U(t) cap U_i^-=empty. Conversely any reverse U-witness for h_i->t has endpoint-indexed code bar(d) xor e_i and d_Y=0, so reverse-U H--U capacity is at most sum r_i<=u. The live obstruction is now overlap/control of these private-coordinate U-hole slices, not aggregate pair capacity.`

UNPRESERVED WORK: `None after preservation. New/updated notes: ONE_CODE_R1_K2_OFFRAY_NORMALIZED_SCORE_AND_HIGH_Y_GAP.md; corrected ONE_CODE_R1_K2_INTERMEDIATE_HALF_RAY.md; corrected ONE_CODE_R1_K2_HALF_RAY_HU_TRIANGLE_SCOPE.md; expanded ONE_CODE_R1_K2_HALF_RAY_HU_ORIENTATION_FILTER.md with private-foot forcing; diagnostic check_offray_normalized_score.py. One heavier SciPy diagnostic timed out and was replaced; no proof depends on computation.`

DEFERRED ADMIN: `README remains deliberately at the independently audited public checkpoint. Do not promote same-session off-ray/high-Y/half-ray results before the next daily hostile audit. The initial same-session b=0 interpretation is explicitly superseded by the mandatory b>=2 correction. Historical notes remain preserved. The prior golden dual-witness model remains superseded.`

NEXT ACTION: `Hostile-replay HU-PRIVATE/HU-IHOLE first. Then aggregate the coordinate-slice exclusions N_U(t) cap U_i^-=empty for H-multi/Y-active vertices while retaining endpoint populations r_i and the two B0 witnesses. The central question is whether many t-sourced H edges force enough distinct U-nonedges through source-coordinate uniqueness / code incidence, while the alternative reverse-U and triangle-free arms have only O(u) endpoint-indexed capacity. Keep non-U reverse orientations explicit rather than silently discarding them. In parallel quantify the high-Y exclusion wedge and isolate unbounded c/p. Keep y=o(p) on the separate large-gap/rooted-residual route.`

AUDIT GATE: `The 20 September daily red-team audit remains binding. P1/P2 semantics are repaired; raw same-code criticality and ordered (source,witness) injection independently passed in later repair work; X_3 remains mandatory; exact pair-local Ccap_P/(ONE-P)/(CROWD) remain load-bearing whenever invoked; finite scans are diagnostics only; superseded evidence stays superseded; bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with x>=3.`

SECOND STRICT: `Provisional exact unloaded second-strict chain remains finite-order: mixed y=1 x=3 gives n<=16; x=4 n<=19; x>=5 n<=33; two-X-hole arm n<=816; (0,2) empty; mixed y>=2 internally closed. Conditional on the rigid one-code interface and predecessor closures, no exact unloaded second-strict survivor remains for n>=817. Pending hostile replay.`

R1 K2 LIVE CHAIN: `Residual-one common hub/beta fan -> k=2,J2=empty -> global H/Y polarization -> B0 source collapse -> e(Y)=0 -> all Y--U edges triangular -> reverse B0 capacity/isolation -> exact high-Y ray closed -> off-ray normalized score/rooted obstruction -> theta=1 endpoint closed -> corrected minimal-B0 half-ray survives aggregate gates -> H--U triangle exceptions <=u -> H--U orientation filter -> H-multi/Y-active t-sourced edges forced through private foot q_i -> coordinate-slice U-hole condition -> next: overlap/injection of those slices.`

R1 K2 SUPERSESSION: `Do not return to the exact kappa=theta=1 ray, the golden dual-witness model, or the literal b=0 half-ray. The latter was caught and corrected before handoff. The live bounded-ratio problem is the b=2 minimal-B0 half-ray and its private-coordinate H--U criticality; unbounded c/p remains separate.`
<!-- CURRENT-STATUS:END -->

---

## Binding audit gate

Latest daily audit: `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Binding constraints:
- repaired P1/P2 semantics;
- raw same-code criticality / ordered `(source,witness)` injection independently passed in later repair;
- `X_3` mandatory negative control;
- zero positive actual D2C rigid complete Hall cuts with `x>=3` in bounded regression;
- exact pair-local `Ccap_P`, `(ONE-P)`, `(CROWD)` whenever invoked;
- finite scans are diagnostics only;
- superseded evidence stays superseded;
- same-session closures stay provisional until hostile replay.

## Session ledger — current invocation

**Invocation start:** 21:28:21 BST.  
**Planned preservation cutoff:** 21:55:38 BST.

Substantive units completed:
1. reconciled CURRENT_STATE.md, README.md, live commits and the daily red-team audit before forward mathematics;
2. hostile-replayed `e(Y)=0`;
3. replayed all-Y--U triangularity;
4. replayed high-Y D reverse B0 witness location;
5. replayed B0--D isolation and multiplicity divisor b;
6. derived normalized Y-hole coefficient Y0;
7. derived simultaneous total-hole coefficient Z0;
8. localized e(U) and inserted it into the rooted identity;
9. derived normalized score F<=S0;
10. normalized rooted-Q feedback and obtained the kappa ratio floor;
11. proved theta=1 score gap strictly positive by three cases;
12. added a diagnostic grid after pivoting from a timed-out heavier diagnostic;
13. isolated the intermediate theta=kappa=1/2 density direction;
14. evaluated exact score/rooted margins;
15. tested exact Ccap_P, ONE-P and CROWD, all open;
16. localized H--U triangle exceptions to endpoint-indexed code classes;
17. bounded total triangle-free H--U edges by u;
18. caught the impossible b=0 assignment because W_s subseteq B0;
19. corrected the exact ray to b=2 and re-derived its physical/score bounds;
20. corrected the Y--U interpretation to global O(p) sparsity rather than pointwise degree<=1;
21. proved no t-sourced U witness exists for an H--U edge and no Y witness when d_H(t)>=2;
22. proved that if d_H(t)>=2 and d_Y(t)>0 then any t-sourced triangular H--U certificate is matched-layer;
23. proved any reverse U-witness for h_i->t is Y-anticomplete with endpoint-indexed code bar(d) xor e_i, hence total reverse-U H--U capacity is at most u;
24. refined the matched-layer arm: a Y-active t rules out every d-selected matched endpoint, while h_i selects the bar-d endpoint only at private coordinate i, forcing the witness exactly to q_i;
25. extracted the coordinate-slice consequence N_U(t) cap U_i^-=empty for every such private-foot t-sourced certificate.

**Live unfinished line:** aggregate private-coordinate slice exclusions with source-coordinate uniqueness / code incidence while retaining r_i and the two B0 witnesses; separately high-Y wedge and unbounded c/p.

**Stop reason:** preservation checkpoint after twenty-five tightly connected mathematical/audit units. The remaining half-ray problem is now a concrete private-coordinate U-hole overlap problem.