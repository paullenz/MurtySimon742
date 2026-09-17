# Murty–Simon / Erdős #742 — live current state

> **Programme pivot — 17 September 2026.** The active target is the stronger dense non-bipartite D2C problem around `floor((n-1)^2/4)+1`. Existing #742 work is preserved. A pre-existing August 2026 public Lean proof/equality formalisation removes sensible first-proof priority for the original conjecture unless later audit overturns it.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `POST_MS_RESIDUAL_DEFECT_TRIANGLE_ROOT_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Second bounded unit after the programme switch. The first signed-surplus checkpoint identified zero-residual sources. This unit corrects/refines the strategic emphasis: zero sources are only one boundary phenomenon. The more natural global coordinate is the residual defect `delta=-t=r-e(F)`, and the old selected count has a direct triangle interpretation.

**INSPECTED PREDECESSOR:** `ea7ddcdfed9eb5cc6194287be059e2485748f532` on `main`, containing `SIGNED_SURPLUS_PIVOT.md`. The preceding all-E mixed `{4,5}` Hall-ramp closure at `7e1c9409...` remains preserved and not promoted.

**LAST VERIFIED RESULT:** `project/research/post_ms/2026-09-17-stronger-pivot-v1/DEFECT_TRIANGLE_ROOT.md` records the exact reformulation.

Write

`delta=-t=b(n-b)-m=r-e(F)`.

Let

`M(n)=floor((n-1)^2/4)+1`.

Then the stronger bound `m<=M(n)` is **equivalent** to

`delta >= b(n-b)-M(n)`.

If `n=2s`, `b=s+d`, the target is

`delta >= s-1-d^2`.

If `n=2s+1`, `b=s+d`, the target is

`delta >= s-1-d(d-1)`.

This is the correct signed objective: prove enough residual A–B mass in excess of `F`-edges.

**TRIANGLE INTERPRETATION OF THE SELECTED SYSTEM:** because the canonical root `v` is a maximum-degree vertex of `G`,

`B=N_G(v)`.

The missing pairs of `H[B]` are exactly the edges of `G[B]`. Hence the total selected count

`Q=e(G[B])`

is exactly the number of triangles of `G` containing `v`. The Hall/selected-representative machinery is therefore a triangle-routing system rooted at a maximum-degree vertex, not merely an abstract near-Turán device.

**BASIC DEFECT BOUNDS:** summing the label minimum-degree inequality gives

`delta >= e(F)-Q`.

Summing the source minimum-degree inequality gives, with `gamma=2b-n`,

`delta >= Q-e(F)-b*gamma`.

These are exact but by themselves not sufficient for the stronger conjecture.

**DEGREE-BALANCE RESIDUAL BASELINE:** for every B-source,

`rho_u >= p_u + n-2b`.

Consequences:

- if `b<n/2`, every B-source is automatically residual-active even when `t<=0`; the h-index and charging arguments whose only use of `t>0` was activity remain available in this branch;
- if `b=n/2` (necessarily even), a zero source has `p_u=0`, and any two zero sources are adjacent in `H[B]` (equivalently, zero sources form a clique in H[B]);
- if `b>n/2`, putting `lambda=2b-n`, every zero source has `p_u<=lambda`, and the number of missing H-pairs internal to the zero-source set Z is at most `lambda|Z|`.

For a zero source `u`, `q_u=|N_A(u)|` and its H[B]-missing degree is `|N_A(u)|+p_u`; combine this with the signed zero-source component-union lemma from the predecessor.

**IMPORTANT STRATEGIC CORRECTION:** the conjectured expanded-`C5` extremals are triangle-free, so for them `Q=0`. In particular, the selected/Hall system is not supposed to reconstruct those already-understood equality examples. The published triangle-free case of the stronger conjecture already handles that branch. The natural use of our machinery is the **triangle-containing branch**, where the conjecture predicts no large-order equality examples outside the finite exceptional list.

**NEW SCOPE GAP:** if a triangle-containing D2C graph has a maximum-degree vertex lying in a triangle, choose such a canonical root and obtain `Q>0`, putting the selected/Hall machinery directly in play. It is not yet proved that such a root always exists. A finite diagnostic over every unlabeled graph of order at most 7 (`check_max_triangle_root_atlas.py`) found no counterexample: among triangle-bearing D2C isomorphism classes, every case had at least one maximum-degree vertex in a triangle. This is diagnostic evidence only.

**LITERATURE ANCHOR:** Dailly–Foucaud–Hansberg (2019) state the stronger conjecture and note the triangle-free case is already established; Lin–Wang (2025) further show sufficiently large `C5`-free D2C graphs at the stronger threshold are complete bipartite. Loh–Ma's diameter-critical work supplies independent structural information on triangles (every triangle has at least two external critical-path “feet”), potentially relevant to the next lemma.

**OLD LINE PRESERVED:** all fixed-order candidates, audits, exact-block work, h-index/receiver theory, selected-incidence Hall and the complete mixed `{4,5}` all-E closure remain available as tools. Canonical counts remain **4626 exclusions / 952 survivors / 3632 whole-state closures**; no promotion changes.

**AUTOMATION STATUS:** the hourly task is now titled `Stronger D2C Research` and is explicitly instructed to pursue this stronger target rather than the old #742 excess ladder.

**UNPRESERVED WORK:** None after this checkpoint.

**DEFERRED ADMIN:** independent fresh Lean recompilation of `Erdos742/Erdos742`; reviewer-facing README synchronization; older archive transfers; PR #2; unrelated CI/root narrative maintenance; external novelty review.

**NEXT ACTION:** MATH: attack the **maximum-triangle-root lemma**: determine whether every triangle-containing D2C graph has at least one maximum-degree vertex contained in a triangle. Use edge-critical witnesses / triangle feet, not the small-order diagnostic as proof. If false, preserve the smallest structural counterexample and replace the canonical root by a near-maximum triangle root with an explicit degree-slack term. If true, the entire remaining triangle-bearing stronger-conjecture branch can be rooted with `Q>0` and fed into the selected/Hall machinery.
<!-- CURRENT-STATUS:END -->
