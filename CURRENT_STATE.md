# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The 2019 all-order second-extremal strengthening is false because of a published 12-vertex, 32-edge D2C graph. The live problem is the sufficiently-large / eventual second-extremal classification around `M(n)=floor((n-1)^2/4)+1`. Existing Murty–Simon / Erdős #742 work remains preserved.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INDEPENDENT_HYPERCUBE_FACE_EXCEPTION_MECHANISM_NOT_NOVELTY_CLEARED`.

**WORK MODE:** `MATH`. Reconstructed a deterministic 12-vertex/32-edge D2C benchmark matching all published coarse invariants and then generalized its visible structure. This is an independent reconstruction: direct isomorphism to the published Figure 1 has not yet been certified from authoritative adjacency data, so the repository does not call it the published graph. Radosavljević's claimed exhaustive small-order enumeration reports a single Conjecture-3 counterexample through order 13, which strongly suggests isomorphism, but that is supporting evidence rather than the identity certificate.

**INSPECTED PREDECESSOR:** `e736305b286fd45d2d496eb6ec5850d40417e4a6` on `main`, which corrected the target after the 2024 literature collision.

**LAST VERIFIED RESULT:** `project/research/post_ms/2026-09-17-stronger-pivot-v1/HYPERCUBE_FACE_EXCEPTION.md` and `check_hypercube_face_family.py` preserve the construction, hand proof and deterministic checks.

For every `k>=3`, define `X_k` on

`{r} union {a_1,...,a_k} union {0,1}^k`

by:

1. the cube vertices induce the hypercube `Q_k`;
2. `r` is adjacent to every cube vertex;
3. `a_i` is adjacent exactly to the cube vertices whose i-th coordinate is `0`;
4. there are no other edges.

Then `X_k` is D2C. The proof is elementary and edge-type exact:

- for a cube edge `xy` differing in coordinate `i` with `x_i=0,y_i=1`, the pair `(a_i,y)` has unique common neighbour `x`;
- the same pair certifies criticality of the face edge `a_i x`;
- for a root edge `rx`, the antipodal cube vertex `bar(x)` and `x` have unique common neighbour `r` when `k>=3`.

Diameter 2 follows directly from the root, coordinate flips and common zero-coordinate cube vertices.

The parameters are

`n=2^k+k+1`,
`m=(k+1)2^k`.

For `k=3`, this gives `n=12,m=32`, degree sequence

`8,7,6,6,6,5,5,5,4,4,4,4`,

a unique dominating edge `r 000`, and a primitive/twin-free graph. A randomized reconstruction search found multiple labelled hits but only one isomorphism class in the bounded sample; this is diagnostic, not exhaustive uniqueness.

**CANONICAL PROFILE OF k=3:** root at the unique degree-8 vertex:

- `b=8`, `a=3`;
- `delta=b(n-b)-m=0`, equivalently `t=0`;
- `F=G[A]` is empty;
- total residual count `r=0`, so **every B-source has rho=0**;
- `B` induces `Q_3`, so `Q=e(G[B])=12` rooted triangles;
- the 12 H-cross edges are all selected representatives, with no residual cross edge;
- each A-label is selected four times, but every label demand is `s_i=0` because `F` is empty.

More generally, for `X_k` the canonical root is `r`, `A={a_i}`, `B=Q_k`, `F=empty`, `t=delta=r=0`, and

`Q=k*2^(k-1)`.

Each cube edge in coordinate `i` has a unique canonical quasi-edge: orient it from the endpoint with bit `1` to the endpoint with bit `0` and use label `a_i`. Thus for cube vertex `x`,

`q_x=weight(x)`, `p_x=k-weight(x)`, `rho_x=0`.

This is a crucial hostile control: a large selected system can coexist with **zero demand and zero residual mass**. Any eventual proof depending only on positive demand or residual h-index must explicitly exclude or price this boundary mechanism.

**WHY THE FINITE EXCEPTION DOES NOT SCALE AT THE SAME DENSITY:** `X_3` has `m=32>M(12)=31`. But for every `k>=4`,

`(k+1)2^k < M(2^k+k+1)`.

Indeed with `N=2^k`,

`(N+k)^2-4(k+1)N = N(N-2k-4)+k^2 >0`

for `k>=4`. So the natural hypercube-face continuation remains D2C but immediately drops below the second-extremal threshold. This explains one concrete way a genuine finite obstruction can self-dilute rather than threaten the eventual conjecture.

**IDENTITY / NOVELTY BOUNDARY:** an independently found labelled representative has graph6 `KnbI^UpaKgi\``; the deterministic construction uses another isomorphic labelling. The project has not obtained authoritative adjacency data for Figure 1 and does not claim direct identification. A quick literature search did not locate this `Q_k` face construction in named form, but no comprehensive novelty search has been done; **do not claim the infinite family as new**.

**LITERATURE STATUS:** the peer-reviewed 2024 paper establishes existence of the 12/32 counterexample and says it has a dominating edge. The 2023 small-order enumeration reports a single counterexample through order 13. The 2025 Lin–Wang paper asks the sufficiently-large version and proves a substantial `C5`-free case. These remain external inputs, not project theorems.

**OLD LINE PRESERVED:** all fixed-order candidates, audits, exact-block work, residual h-index/receiver theory, selected-incidence Hall and the complete mixed `{4,5}` all-E closure remain available. Canonical ledger remains **4626 exclusions / 952 survivors / 3632 whole-state closures**; no promotion changes.

**AUTOMATION STATUS:** hourly task is `Eventual D2C Research`; it must keep the 12-vertex exception as a negative control and not revert to the false all-order strengthening or the closed old excess ladder.

**UNPRESERVED WORK:** None after this checkpoint.

**DEFERRED ADMIN:** authoritative Figure-1 adjacency/isomorphism certification; fresh Lean recompilation of `Erdos742/Erdos742`; reviewer-facing README synchronization; older archive transfers; PR #2; unrelated CI/root narrative maintenance; full novelty search for the hypercube-face construction.

**NEXT ACTION:** MATH: classify the **zero-residual boundary** `t=0, r=0, F=empty` in canonical coordinates. Translate the selected representatives into an orientation/edge-labelling of `G[B]`: every B-edge must be represented by a unique A-nonedge at one endpoint, and in the hypercube family these labels are coordinate directions. Derive a general constraint on `G[B]` (degree, label classes, 4-cycle/cube structure, or expansion) strong enough to show that high-density members of this boundary are finite/small, or preserve a different scalable family if one exists. Keep `X_3` as the mandatory equality/exception control and `X_k,k>=4` as scalable negative controls.
<!-- CURRENT-STATUS:END -->
