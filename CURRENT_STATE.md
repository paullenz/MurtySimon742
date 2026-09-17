# Dense diameter-2-critical research — live current state

> **Literature correction — 17 September 2026.** The 2019 Dailly–Foucaud–Hansberg all-order strengthening is false: a published 2024 paper gives a 12-vertex, 32-edge D2C graph, while `floor((n-1)^2/4)+1=31`. The active programme is therefore the **eventual / corrected second-extremal problem**, not the false universal statement. Existing Murty–Simon / Erdős #742 work remains preserved.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `LITERATURE_CORRECTION_EVENTUAL_SECOND_EXTREMAL_TARGET`.

**WORK MODE:** `MATH`. A potentially fatal literature collision was checked before further theorem-building and found genuine. The research target has been repaired immediately rather than allowing the hourly work to optimize against a false conjecture.

**INSPECTED PREDECESSOR:** `82de82825036321ecb78817550753aa05f18d768` on `main`. Its residual-defect and rooted-triangle reformulations remain valid mathematics; only the scope/target statement needed correction.

**LAST VERIFIED RESULT:** `project/research/post_ms/2026-09-17-stronger-pivot-v1/LITERATURE_CORRECTION_2024_EXCEPTION.md` records the correction and its strategic consequences.

**2019 CONJECTURE 3 IS FALSE AS STATED:** Radosavljević, Stanić and Živković, *Primitive diameter 2-critical graphs*, Publications de l'Institut Mathématique 115(129) (2024), 21–32, DOI `10.2298/PIM2429021R`, explicitly exhibit a D2C graph with

`n=12, m=32`,

while

`floor((n-1)^2/4)+1=31`.

They state that the graph has a dominating edge. This is a counterexample to Dailly–Foucaud–Hansberg Conjecture 3, but not to the Murty–Simon bound (`32<36`). The graph had already been found in Radosavljević's small-order work.

**CORRECT ACTIVE TARGET:** the live problem is the **sufficiently-large second-extremal classification**, matching the 2025 Lin–Wang Question 1:

> for sufficiently large `n`, if a D2C graph has at least `M(n)=floor((n-1)^2/4)+1` edges, must it be complete bipartite or an expanded `C5` from `C5+`?

Equivalently, for sufficiently large non-bipartite D2C graphs, seek `m<=M(n)` with equality only in `C5+`. This formulation permits finite exceptions such as the 12-vertex graph.

**AUTHORITATIVE `C5+` DEFINITION:** use the original 2019 Dailly–Foucaud–Hansberg paper: three consecutive vertices of `C5` are expanded to independent twin sets and

`|X2| in {floor((n-3)/2), ceil((n-3)/2)}`.

The 2024 paper prints a different `(n-2)/3` parameter while referring back to this family; do not use that secondary formula for extremal calculations. The original source is the project authority.

**WHY THE PIVOT STILL MAKES SENSE:** the triangle-free version of the non-bipartite second-extremal bound is already established in the literature, with the expanded-`C5` family providing the large equality examples. Therefore our structural machinery is most naturally aimed at the **triangle-containing branch**, where eventual strictness below `M(n)` would complete the second-extremal picture (modulo the already-known triangle-free branch).

**RESIDUAL-DEFECT REFORMULATION REMAINS VALID:** with maximum-degree root, `b=Delta`,

`delta=b(n-b)-m=r-e(F)`.

The target threshold translates to

`delta >= b(n-b)-M(n)`

for the eventual problem. Also `Q=e(G[N(v)])` is the number of triangles through the root. These identities are independent of the false all-order conjecture.

**MANDATORY NEGATIVE CONTROL:** every new structural lemma intended for the eventual theorem must either hold on the published 12-vertex exception or explicitly use a hypothesis that excludes its finite mechanism. In particular, do not infer a universal `n>=12` theorem from small-order diagnostics or from the old 2019 statement.

**EXTERNAL #742 COLLISION:** unchanged. The pre-existing `Erdos742/Erdos742` Lean proof/equality formalisation remains the reason first-proof priority for #742 is not the active goal, pending independent recompilation and external acceptance.

**OLD LINE PRESERVED:** all fixed-order candidates, audits, exact-block work, h-index/receiver theory, selected-incidence Hall, and the complete mixed `{4,5}` all-E closure remain available. Canonical ledger remains **4626 exclusions / 952 survivors / 3632 whole-state closures**; no promotion changes.

**AUTOMATION STATUS:** the hourly research task is being retargeted again to the **eventual second-extremal** problem and must explicitly remember that the 2019 all-order strengthening has a 12-vertex counterexample.

**UNPRESERVED WORK:** None after this checkpoint.

**DEFERRED ADMIN:** independent fresh Lean recompilation of `Erdos742/Erdos742`; reviewer-facing README synchronization; older archive transfers; PR #2; unrelated CI/root narrative maintenance; comprehensive novelty review.

**NEXT ACTION:** MATH: obtain or reconstruct the exact 12-vertex/32-edge exception (preferably graph6 or adjacency data) and compute its canonical residual profile `(b,a,delta,Q,F,rho,p,q)`. Use it as a hostile negative control against the residual-defect, zero-source and maximum-triangle-root ideas. Identify exactly which finite mechanism lets it beat `M(12)`. Only then resume the maximum-triangle-root / Hall attack for the sufficiently-large triangle-bearing branch.
<!-- CURRENT-STATUS:END -->
