# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-20  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

`X_3` (12 vertices, 32 edges, versus `M(12)=31`) remains the mandatory negative control. The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is not the target. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not the optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_R1_K2_OFFRAY_HALF_RAY_MIN_B0_HU_TRIANGLE_LOCALIZED_2026_09_20`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `7e6c442a09eb6b5969571398c603cae8d2dfeb4f`; before forward mathematics this invocation reread CURRENT_STATE.md, README.md, the latest commits, the 20 September daily red-team audit, the residual-one profile, low-k escape normal form, general Y--U triangle/capacity theorem, weighted rooted ledger, rooted-Q feedback, A-side compensator identity, global H/Y polarization, and H--H certificate split. The audit gate remained binding throughout.

LAST VERIFIED RESULT: `The load-bearing off-ray chain was independently replayed with no new defect found at its stated conditional scope. For bounded ratios theta=y/p, kappa=c/p, eta=b/p and q=C/p^2, define Y0=eta theta+max{0,theta(kappa-2eta),(q/eta)^2} (eta=0 is a limiting density, not literal B0 emptiness) and Z0=max{kappa theta+eta,eta+Y0}. Every asymptotic survivor must satisfy F=Z0+Y0+kappa(kappa-theta)-2q <= S0=((1+kappa)^2-theta^2)/2, while rooted-Q feedback forces kappa>=sqrt(2(theta^2+theta+1))-(1+theta). At theta=1 the score gap is strictly positive for every kappa>0 by a complete three-case proof, so the bounded-ratio high-Y endpoint y/p->1 is impossible. The first simple exact intermediate direction is p=2t,c=y=t,g0=t,lambda=2t-1,u=t+1,x=2t+1,k=2,m=2t-1. SAME-SESSION CORRECTION: the initial draft incorrectly set b=|B0|=0. This is impossible because the two selected U witnesses W_s have code bar d and no H-neighbour, so W_s subseteq B0 and b>=2. The corrected minimal assignment is b=2, B0=W_s; C=e(B0,D) is left variable but C<=2(t-1), so eta=b/p->0 and q=C/p^2->0. The corrected ray still survives score, rooted-Q, exact Ccap_P, purified ONE-P and scalar CROWD with quadratic margin. It has e(Y)=0, e(Y,U)=O(p), e(U)=O(p), with all high-Y reverse-certificate capacity concentrated through the two B0 witnesses. H-side localization remains valid: an H--U edge h_i t can be triangle-free only when c(t)=bar(d) xor e_i and d_Y(t)=0; endpoint-indexed classes are disjoint, so at most u H--U edges can be triangle-free. The same endpoint classes supply U-certified H--H edges.`

UNPRESERVED WORK: `None after preservation. New theorem note: ONE_CODE_R1_K2_OFFRAY_NORMALIZED_SCORE_AND_HIGH_Y_GAP.md. Corrected exact intermediate note: ONE_CODE_R1_K2_INTERMEDIATE_HALF_RAY.md. Corrected H-side lemma: ONE_CODE_R1_K2_HALF_RAY_HU_TRIANGLE_SCOPE.md. New diagnostic: check_offray_normalized_score.py. A heavier SciPy diagnostic timed out and was replaced by a lightweight grid; no proof depends on computation.`

DEFERRED ADMIN: `README remains deliberately at the independently audited public checkpoint. Do not promote same-session off-ray/high-Y/half-ray results before the next daily hostile audit. The initial same-session b=0 interpretation is explicitly superseded by the mandatory b>=2 correction. Historical notes remain preserved. The prior q=1 golden forward/reverse/dual witness split and W_min curve remain superseded.`

NEXT ACTION: `First hostile-replay the mandatory B0 floor W_s subseteq B0 and the corrected exact half-ray arithmetic. Then orient the triangular H--U bulk on the corrected minimal-B0 half-ray while retaining both selected B0 witnesses and endpoint-indexed populations r_i=|U_{bar(d) xor e_i}|. The same r_i reservoir controls U-certified H--H edges and the only possible triangle-free H--U edges; do not aggregate it away. A U vertex with at least two H-neighbours cannot use a Y witness in a U-sourced singleton certificate for one H-edge. Combine this with private-foot alternatives and source-coordinate uniqueness. In parallel quantify the high-Y exclusion wedge and isolate unbounded c/p. Keep y=o(p) on the separate large-gap/rooted-residual route.`

AUDIT GATE: `The 20 September daily red-team audit remains binding. P1/P2 semantics are repaired; raw same-code criticality and ordered (source,witness) injection independently passed in later repair work; X_3 remains mandatory; exact pair-local Ccap_P/(ONE-P)/(CROWD) remain load-bearing whenever invoked; finite scans are diagnostics only; superseded evidence stays superseded; bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with x>=3.`

SECOND STRICT: `Provisional exact unloaded second-strict chain remains finite-order: mixed y=1 x=3 gives n<=16; x=4 n<=19; x>=5 n<=33; two-X-hole arm n<=816; (0,2) empty; mixed y>=2 internally closed. Conditional on the rigid one-code interface and predecessor closures, no exact unloaded second-strict survivor remains for n>=817. Pending hostile replay.`

R1 K2 LIVE CHAIN: `Residual-one common hub/beta fan -> k=2,J2=empty -> global H/Y polarization -> B0 source collapse -> e(Y)=0 -> all Y--U edges triangular -> reverse B0 capacity/isolation -> exact high-Y ray closed -> off-ray normalized score/rooted obstruction -> theta=1 endpoint closed -> corrected intermediate minimal-B0 half-ray (b=2, eta->0) survives aggregate gates -> endpoint-indexed H--U triangle exceptions total at most u -> next: orient almost-all triangular H--U edges with r_i and the two selected B0 witnesses explicit.`

R1 K2 SUPERSESSION: `Do not return to the exact kappa=theta=1 ray or the superseded golden dual-witness model. Do not use the same-session literal b=0 half-ray statement; it was caught and corrected before final handoff. The live bounded-ratio problem is the b=2 minimal-B0 half-ray and its H-side criticality; unbounded c/p remains separate.`
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

## Live structural chain

`audited rooted/Hall setup`
`-> rigid singleton-head implication`
`-> one-code residual-one common hub / beta fan`
`-> k=2,J2=empty`
`-> global H/Y polarization`
`-> B0 source collapse`
`-> e(Y)=0`
`-> all Y--U edges triangular`
`-> reverse B0 capacity / isolation`
`-> exact high-Y ray closure`
`-> off-ray score/rooted normalization`
`-> theta=1 endpoint closure`
`-> corrected intermediate b=2 minimal-B0 half-ray`
`-> H--U triangle exceptions localized to endpoint-indexed code classes`
`-> next: raw orientation of the quadratic triangular H--U bulk`.

## Session ledger — current invocation

**Invocation start:** 21:28:21 BST.  
**Planned preservation cutoff:** 21:55:38 BST.

Substantive units completed:
1. reconciled CURRENT_STATE.md, README.md, live commits through `7e6c442...`, and the 20 September daily red-team audit before forward mathematics;
2. independently hostile-replayed `e(Y)=0`;
3. replayed the all-Y--U-triangular theorem;
4. replayed the high-Y D reverse B0 witness location;
5. replayed the B0--D isolation charge and multiplicity divisor b;
6. derived the off-ray normalized Y-hole coefficient Y0;
7. derived the simultaneous total-hole coefficient Z0;
8. localized U edges as e(U)=C+O(|D|) and inserted this into the rooted identity;
9. derived the normalized score condition F<=S0;
10. normalized rooted-Q feedback and obtained the kappa ratio floor;
11. proved the theta=1 score gap strictly positive for every kappa>0 by three cases;
12. added a diagnostic grid checker after pivoting from a timed-out heavier SciPy diagnostic;
13. isolated the intermediate normalized half-ray theta=kappa=1/2, eta=q=0 as a density direction;
14. evaluated exact score and rooted-Q margins on its integer realization;
15. tested exact pair-local Ccap_P, ONE-P and CROWD; all remain open;
16. localized H--U triangle exceptions to the endpoint-indexed classes U_{bar(d) xor e_i};
17. summed those classes to show at most u H--U edges can be triangle-free;
18. hostile-replayed the literal b=0 assignment and found it impossible because W_s subseteq B0;
19. corrected the exact ray to the minimal physical floor b=2, retained variable C<=2(t-1), and re-derived exact score sparsity bounds; the ray still survives with quadratic margin;
20. corrected the H-side interpretation: not every U vertex has d_Y<=1; instead e(Y,U)=O(p) with high-Y capacity concentrated through the two selected B0 witnesses.

**Live unfinished line:** orient the triangular H--U bulk with the two selected B0 witnesses and endpoint populations r_i explicit; separately quantify the high-Y wedge and audit unbounded c/p.

**Stop reason:** preservation checkpoint after twenty tightly connected mathematical/audit units. A same-session physical-assignment error was caught, corrected in both affected notes, and explicitly superseded before final handoff.