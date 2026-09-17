# Murty–Simon / Erdős #742 — live current state

> **Programme pivot — 17 September 2026.** A pre-existing public August 2026 proof/formalisation of the Murty–Simon inequality and equality clauses has been located and source-audited sufficiently to change research priority, although independent local Lean recompilation remains open. The project is therefore no longer optimizing for a first proof of Erdős #742. Existing work is preserved and repurposed toward the stronger dense non-bipartite D2C problem of Dailly–Foucaud–Hansberg.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `POST_MS_STRONGER_CONJECTURE_PIVOT_SIGNED_SURPLUS_NOT_PROMOTED`.

**WORK MODE:** `MATH`. The user explicitly authorized the programme switch. The active target is now structural theory for dense non-bipartite diameter-2-critical graphs near the stronger bound `floor((n-1)^2/4)+1`, not further level-by-level work on the already closed mixed `{4,5}` selected-excess frontier.

**INSPECTED PREDECESSOR:** `7e1c9409e0022d58461c5155929d95b451686547` on `main`. That concurrent checkpoint materially improved the old line before the pivot: exact Hall ramps close the entire mixed demand-4/5 near-Turán frontier `(a,b,t)=(20,23,2)` for every arithmetically possible selected excess `E`. That result remains preserved and not promoted.

**LAST VERIFIED RESULT:** the first post-pivot bounded mathematical unit is preserved at `project/research/post_ms/2026-09-17-stronger-pivot-v1/SIGNED_SURPLUS_PIVOT.md`. It extracts a signed-surplus extension of the residual h-index framework.

Let `z=#{u in B: rho_u=0}`. For residual h-index `h>=1`, write `|{u:rho_u>=h}|=h+eta` and let `k=#{i:s_i=h}`. Then every canonical bridge satisfies

`b+2t <= (a-h-eta)(h-1)+k+z`.

The coarse form is

`b+2t <= (a+1)h-h^2+z`.

Thus the old positive-surplus theorem is exactly the `z=0` case; zero-residual sources quantify the loss when `t<=0`.

For each zero-residual source `u`, with `S=N_A(u)` and `T=A\S`, the old activity proof yields more than the positive-surplus contradiction:

- there are no `F`-edges between `S` and `T`, so `S` is a union of connected components of `F`;
- `e(F[S]) <= -t`;
- hence any zero-residual source forces `t<=0`.

This is now the leading structural object: zero sources define binary component signatures on `F`.

**STRONGER TARGET / LITERATURE STATUS:** Dailly–Foucaud–Hansberg, Discrete Mathematics 342 (2019), Conjecture 3: for non-bipartite D2C `G != H5`,

`e(G) <= floor((n-1)^2/4)+1`,

with equality conjectured exactly for their expanded-`C5` family `C5+` and thirteen listed small graphs. Lin–Wang, Discrete Applied Mathematics 375 (2025), prove that sufficiently large `C5`-free D2C graphs at or above this threshold are complete bipartite. Therefore the unresolved non-bipartite high-density problem is intrinsically `C5`-bearing.

**TARGET COORDINATES:** put `M(n)=floor((n-1)^2/4)+1`, `e=m-M(n)`, and `d=Delta-floor(n/2)`. In the canonical residual setup `t=m-Delta(n-Delta)`:

- if `n=2s`, `t=e+d^2-(s-1)`;
- if `n=2s+1`, `t=e+d(d-1)-(s-1)`.

A violating graph has `e>=1`. The old positive-surplus machinery applies only when the right side is positive. At the conjectured expanded-`C5` equality examples, `Delta=floor(n/2)`, `e=0`, and `t=1-s<0`. So simply extending the old `E=10,11,...` programme would structurally miss the predicted extremals.

**OLD LINE PRESERVED:** the predecessor's all-E `{4,5}` Hall-ramp closure, E<=9 packages, full selected-incidence Hall, exact-block `D>=12`, receiver/h-index/staircase work, fixed-order candidates and audit artifacts all remain in history and retain their existing trust boundaries. They are now supporting tools for the positive-surplus/high-degree branch, not the primary project objective.

**EXTERNAL #742 COLLISION:** the public `Erdos742/Erdos742` repository predates this repository and contains a Lean source claiming an axiom-clean proof of the inequality plus a separate equality formalisation. Source-level dependency inspection found the only `sorry` in the inequality file to be an unused negative statement, not on the target chain. Independent recompilation in a fresh Lean/mathlib environment is still open, so the project does not promote the external claim to peer-reviewed acceptance; strategically, however, first-proof priority is treated as unavailable unless that audit fails.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No new catalogue promotion, no stronger-conjecture theorem, and no claim of novelty beyond the internal signed-surplus derivation.

**AUTOMATION STATUS:** scheduled research continuation must follow this new target. Do not spend autonomous cycles extending the old mixed `{4,5}` excess ladder or attempting `E=43` (the predecessor already proved no such case exists).

**UNPRESERVED WORK:** None after this checkpoint.

**DEFERRED ADMIN:** independent fresh Lean recompilation of `Erdos742/Erdos742`; reviewer-facing README synchronization; older archive transfers; PR #2; unrelated CI/root historical narrative maintenance; external novelty review.

**NEXT ACTION:** MATH: attack the multiple-zero-source regime. For two zero-residual B-sources `u,v`, exploit that `S_u=N_A(u)` and `S_v=N_A(v)` are unions of connected components of `F`, every cross-edge at a zero source is selected, supplements are sourcewise distinct, and `e(F[S_u]),e(F[S_v])<=-t`. Derive an exact restriction on the possible component-signature pairs. The objective is to force a small cyclic/twin block pattern compatible with expanded `C5`, or obtain a quantitative penalty ruling out stronger-bound violations. Preserve the first theorem or obstruction before broadening scope.
<!-- CURRENT-STATUS:END -->
