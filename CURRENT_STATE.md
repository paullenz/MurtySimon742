# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** A public August 2026 repository predating this project appears to contain Lean formalizations of both the Murty–Simon inequality and equality clauses; source-level inspection has found no target-chain dependency gap, although an independent fresh rebuild remains open. Separately, the 2019 all-order second-extremal strengthening is false because of a published 12-vertex, 32-edge D2C graph. The live problem is therefore the sufficiently-large / eventual second-extremal classification around `M(n)=floor((n-1)^2/4)+1`. Existing Murty–Simon / Erdős #742 work remains preserved.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FALSE_2019_DEPENDENCY_AUDIT_AND_README_SYNC_NO_PROOF_DEMOTION`.

**WORK MODE:** `AUDIT`. User requested that the README reflect the full change of situation and asked whether the false 2019 conjecture undermines the proofs. A targeted dependency audit was therefore performed before further mathematics.

**INSPECTED PREDECESSOR:** `32a5d27be924e6d2e6741aec7e91fc21fee35bb0` on `main`, containing the zero-residual Boolean-coding theorem and the `n<=294` cutoff.

**LAST VERIFIED MATHEMATICAL RESULT:** unchanged from the predecessor. In the exact canonical boundary

`t=0`, `F=empty`, hence `r=0`,

any non-bipartite D2C graph with

`m>=M(n)=floor((n-1)^2/4)+1`

must satisfy `n<=294`. The proof converts `G[B]` into a directed Boolean-coordinate flow, obtains the factorial path inequality `z!<=b lambda^z`, forces `z>=ceil(a/2)` from root criticality, and finishes with an exact finite arithmetic check below the hand cutoff. This remains an internal candidate theorem; external mathematical and novelty review remain open.

**2019 FALSE-CONJECTURE DEPENDENCY AUDIT:** preserved at

`project/research/post_ms/2026-09-17-stronger-pivot-v1/DEPENDENCY_AUDIT_2019_FALSE_CONJECTURE.md`.

The audit found **no load-bearing use of Dailly–Foucaud–Hansberg Conjecture 3 as a premise** in the inspected fixed-order proofs, canonical selected/residual bridge, residual h-index derivations, Hall machinery, signed-surplus identities or zero-residual cutoff.

The important distinction is now explicit:

- the 2019 **Conjecture 3** all-order bound is false;
- the same 2019 paper contains separate **proved dominating-edge theorems**, which remain valid inputs where used;
- the D2C / total-domination-edge-critical complement correspondence used in the canonical construction is the earlier **Hanson–Wang (2003)** result, not Conjecture 3.

Accordingly, no existing project theorem is demoted merely because Conjecture 3 is false. What changes is the strategic quantifier: `M(n)` is a comparison threshold for an eventual/sufficiently-large problem, not a universal theorem.

**CORRECTIONS IN THIS CHECKPOINT:**

1. `project/research/general_n/2026-09-07-residual-hindex-v1/README.md` now attributes the complement/total-domination correspondence to Hanson–Wang (2003), explicitly separates the proved 2019 dominating-edge theorem from false Conjecture 3, and states that Conjecture 3 is not a proof input.
2. `SIGNED_SURPLUS_PIVOT.md` is marked as a historically corrected pivot; its algebra is retained while the all-order target is replaced by the eventual problem.
3. `DEFECT_TRIANGLE_ROOT.md` now treats `M(n)` as a comparison threshold and no longer describes the false all-order statement as an established/viable universal bound.
4. The root `README.md` is synchronized with the August 2026 external proof collision, the 2024 counterexample, this dependency audit, the new eventual target, the zero-residual `n<=294` result, and the bounded automation window.

**EXTERNAL #742 COLLISION:** `Erdos742/Erdos742` predates this repository. Its inequality Lean source states the Formal Conjectures target and its visible `sorry` is an unused negative statement outside the target dependency chain; a separate equality formalization is also present. This is not treated as peer-reviewed acceptance until independently rebuilt/reviewed, but first-solution priority is treated as unavailable unless that external development fails audit.

**FALSE 2019 ALL-ORDER TARGET:** Radosavljević, Stanić and Živković (2024) report a 12-vertex, 32-edge D2C graph, while `M(12)=31`. The graph is a mandatory negative control for every proposed general theorem. `LITERATURE_CORRECTION_2024_EXCEPTION.md` records the primary-source correction and the move to the sufficiently-large formulation studied in recent work.

**CURRENT POST-PIVOT STRUCTURE:** the reconstructed hypercube-face graph `X_3` has `n=12,m=32` and the canonical profile `a=3,b=8,t=0,F=empty,r=0`. The family `X_k` remains D2C for `k>=3` but lies below `M(n)` for `k>=4`. In the exact zero-residual boundary, B-edges change one A-code coordinate, orient from `0` to `1`, and every zero coordinate has exactly one outgoing flip. This yields the Boolean-flow / factorial-growth cutoff above.

**OLD LINE PRESERVED:** fixed-order candidates, audits, exact-block work, residual h-index/receiver theory, selected-incidence Hall and the complete mixed `{4,5}` all-E closure remain available. Canonical ledger remains **4626 exclusions / 952 survivors / 3632 whole-state closures**; no promotion changes.

**AUTOMATION STATUS:** hourly task is `Eventual D2C Research`. Per the user's instruction, this automated research window is bounded to three more days and a separate stop task is scheduled for **20 September 2026 at about 13:53 UK time**. The research automation must retain the published 12-vertex exception as a hostile control, must not revert to the false all-order 2019 conjecture, and must not optimize for first-proof priority on Erdős #742.

**UNPRESERVED WORK:** None after this audit/checkpoint once the commit is published.

**DEFERRED ADMIN:** authoritative Figure-1 adjacency/isomorphism certification; fresh independent Lean recompilation of `Erdos742/Erdos742`; older archive transfers; PR #2; unrelated CI/root historical narrative maintenance; full novelty search for the hypercube-face construction and Boolean-flow formulation.

**NEXT ACTION:** MATH: return to the perturbative Boolean-flow problem after this documentation/dependency transaction. Move one layer outward from `r=e(F)=0`: quantify how small residual mass / `F`-edge mass corrupts the coordinate-flow system, seek an inequality of the form `n<=N(delta,e(F),...)`, and use the 12-vertex graph as a regression control. Preserve the first theorem, counterexample or obstruction before broadening scope.
<!-- CURRENT-STATUS:END -->
