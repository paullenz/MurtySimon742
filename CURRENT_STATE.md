# Dense diameter-2-critical research — live current state

> **Active target — 17 September 2026.** The live graph-theory problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The 2019 Dailly–Foucaud–Hansberg all-order strengthening is false: the published 2024 order-12, size-32 D2C graph remains a mandatory hostile control. Existing Murty–Simon / Erdős #742 work and the standalone-paper programme remain preserved, but they are not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `ANTIPODE_TIGHT_MATCHING_BOOLEAN_PAIR_STABILITY_NOT_PROMOTED`.

**WORK MODE:** `EVENTUAL_D2C_MATH`. This unit reassessed the now-singular antipode branch after the `Q=0` closure. Rather than immediately trying another coarse defect inequality, it isolated the exact error term of a disjoint-support antipode and proved that the zero-error antipodes cannot branch. If they cover the rooted B-layer, the whole layer becomes a 2-lift of a complete graph and the A-layer becomes a Boolean transversal system. This is exactly the kind of stability normal form sought in the previous handoff: the error vanishes on the cube/Boolean mechanism and the order-12 hostile control lands precisely on that boundary.

**INSPECTED PREDECESSOR:** `1a58c7a61a5828b03eaaf81ce1af67dd35faa37e` (`Redirect live state after closing Q0 branch`). The Q0 theorem remains live and preserved; it is not revisited here.

## Preserved entry point

For a non-bipartite D2C graph above `M(n)`, Q0-IN forces every maximum-degree root `v` to have

`Q=e(G[N(v)])>0`.

For `n>=14`, the preserved all-private edge-witness theorem then forces an antipode pair

`u,w in B=N(v)`, `uw notin E(G)`, `N(u) intersect N(w)={v}`.

The live problem is to convert that structure into the required residual defect while retaining the finite `12/32` exception.

## New exact antipode ledger

Write

`A=V(G)\N[v]`, `a=|A|`, `b=|B|=Delta(G)`, `lambda=2b-n=b-a-1`,

and vertex degree slack

`epsilon_x=b-d_G(x)>=0`.

For an antipode pair define

- `U=N_A(u)`, `W=N_A(w)`, `C=A\(U union W)`;
- `X=N_B(u)`, `Y=N_B(w)`, `Z=(B\{u,w})\(X union Y)`;
- `eta(uw)=|C|+|Z|`.

The antipode condition makes both unions disjoint. Direct degree counting gives the exact identity

> **ANTIPODE SLACK IDENTITY**
>
> `epsilon_u+epsilon_w = lambda+1+eta(uw)`.             (AS)

Thus `eta` is literally the excess endpoint slack beyond the unavoidable `lambda+1` baseline.

Call an antipode **tight** when `eta=0`; equivalently

`d(u)+d(w)=n-1`,

and every vertex outside `{u,w,v}` is adjacent to exactly one endpoint.

In the complement `H`, every antipode edge satisfies

`uw -> v`.

So one H-edge is simultaneously a quasi-edge for both missing root edges `uv` and `wv`; this is the exact quasi-edge double-use mechanism of the antipode branch.

Full hand note:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/ANTIPODE_TIGHT_MATCHING_STABILITY.md`

## New theorem — tight antipodes cannot branch

> **TIGHT-ANTIPODE MATCHING THEOREM.** For a fixed root `v`, the tight antipode pairs form a matching on `B`.

If a vertex `w` had two tight partners `u1,u2`, put

`R=V(G)\(N(w) union {w})`.

Tightness forces

`N[ui]={v} union R`

for both partners. Hence `u1,u2` are adjacent true twins. Deleting their edge leaves them at distance two through `v` and does not destroy any other length-at-most-two connection, contradicting D2C criticality.

Therefore any antipode hub of multiplicity at least two must pay positive `eta` on all but at most one incident antipode relation.

## Antipode matching cut

For any matching `M` in the antipode graph, summing (AS) gives

`sum_{x in V(M)} epsilon_x = |M|(lambda+1)+sum_{e in M} eta(e)`.

The canonical B-side slack ledger is

`sum_{x in B} epsilon_x = b lambda + r - Q`.

Hence

> `b lambda+r-Q >= |M|(lambda+1)+sum_{e in M} eta(e)`.  (AMC)

At exact balance this is

`r-Q >= |M|+sum eta(e)`.

This is not yet the eventual second-extremal contradiction, but it prices disjoint antipodes and their non-Boolean error exactly rather than with a coarse support count.

## Full tight cover — Boolean-pair normal form

If tight antipodes cover all of `B`, Theorem above makes them a perfect matching. Write

`b=2k`, `P_i={u_i,w_i}` for `1<=i<=k`.

Then:

1. Between every two fibres `P_i,P_j`, the `2x2` B-adjacency is a perfect matching. Thus `G[B]` is a **2-lift of K_k**.
2. Every `A`-vertex is adjacent to exactly one endpoint of every pair, hence receives a binary code in `{0,1}^k`.
3. The rooted triangle count is exact:

   `Q=k(k-1)`.
4. Exactly half of the A-B pairs are G-edges, so the H-cross total is `ak`; hence

   `r=k(a-k+1)`.
5. Therefore

   `delta=k(a-k+1)-e(F)`.
6. Every `A`-vertex has `d_F(x)<=k` by maximum degree.

This is much more rigid than the previous generic antipode partition.

## Forced selected-witness codes

In the full tight-cover normal form, let a B-edge `pq` between fibres `P_i,P_j` be canonically represented at source `q` by

`qx -> p`

with `x in A`.

Then the binary code of `x` is forced by the ordered edge `q -> p`:

- at `P_j`, choose the mate of `q`;
- at `P_i`, choose `p`;
- at every other fibre, choose the endpoint not adjacent to `q`.

Moreover, if `S_q=N_A(q)`, then

`N_F(x) intersect S_q = empty`.

Thus selected incidences in the zero-error antipode branch are not generic Hall capacity: each one demands a prescribed Boolean code plus an F-separation condition. This is the new bridge to the selected/Hall machinery.

## Mandatory 12/32 hostile control

The reconstructed `X_3` lies **exactly** in the full tight-cover normal form:

`a=3`, `b=8`, `k=4`, `lambda=4`, `Q=12`, `r=0`, `F=empty`, `delta=0`.

Its four cube-antipodal pairs are the tight matching. The B-layer is

`Q_3 ~= K_{4,4}-M`,

a 3-regular 2-lift of `K_4`. The three A-vertices are Boolean transversals of the four fibres. Every one of the 12 rooted B-edges has exactly one canonical A-witness in the deterministic reconstruction.

Thus the new theorem does not suppress the published finite exception; it identifies its structural mechanism precisely.

## Verification

Companion regression:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/check_antipode_tight_matching_stability.py`

Recorded summary:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/ANTIPODE_TIGHT_MATCHING_CHECK_SUMMARY.json`

Finite evidence:

- 21 D2C atlas classes through order 7;
- 50 maximum-degree root instances;
- 87 antipode edges;
- 11 tight antipode edges across 9 roots;
- zero failure of the exact slack identity or tight-matching theorem;
- 8 full-tight-cover roots, all satisfying the 2-lift/transversal and exact `Q,r` formulas;
- forced selected-witness code/F-separation checks on every B-edge of those nontrivial atlas full-cover instances;
- explicit `X_3` replay: four tight antipode pairs, `Q=12`, `r=0`, and 12 uniquely represented B-edges.

Finite checks are regression evidence only. The hand proofs are the mathematical basis.

## Trust boundary

The tight-antipode matching theorem, `(AMC)`, and the full tight-cover Boolean-pair normal form are internal hand mathematics with finite regression. External mathematical review and novelty assessment remain open. **No eventual second-extremal theorem is claimed.**

The live branch is now split more sharply:

1. **errorful antipodes:** `eta>0` is charged directly by `(AS)/(AMC)`;
2. **tight antipodes:** they form disjoint pairs;
3. **full/near-full tight cover:** the root layer becomes a 2-lift/Boolean code system, with selected witnesses having forced code types and F-separation.

**UNPRESERVED WORK:** None after this current-state commit.

**NEXT ACTION:** Attack the **full or near-full tight-antipode matching branch** before returning to generic scalar inequalities. In the full-cover case, exploit the forced-code orientation system for the `k(k-1)` B-edges: at source `q`, every selected incidence must use a prescribed A-code and that label has no F-neighbour in `S_q=N_A(q)`. Seek a global code/Hall inequality that upper-bounds `e(F)` or forces residual mass, then combine it with

`delta=k(a-k+1)-e(F)`.

Use `(AMC)` to pay for the unmatched/errorful part in a near-full cover. Preserve `X_3` as the exact zero-error finite model. Do not return to the Q0 branch, the closed mixed `{4,5}` selected-excess ladder, or first-proof optimization for Erdős #742.
<!-- CURRENT-STATUS:END -->
