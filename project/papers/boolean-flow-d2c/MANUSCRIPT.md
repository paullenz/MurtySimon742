# Boolean coordinate flow and root-edge stability in near-extremal diameter-2-critical graphs

**Status:** working paper skeleton. This is a graph-theoretic candidate paper built around the exact zero-residual boundary and its first perturbative extension. The core results are internal candidate theorems; external mathematical review and novelty review remain open.

## Abstract — provisional

Let `G` be a diameter-2-critical graph and root it at a maximum-degree vertex `v`. The canonical root decomposition splits the remaining vertices into `B=N(v)` and `A=V(G)\N[v]`, with residual mass measuring cross-incidences not accounted for by the selected criticality representatives. We study the exact zero-residual boundary and its first perturbations near the second-extremal density scale.

When `A` is independent and the residual mass vanishes, the `A`-neighbourhood of each vertex of `B` is a Boolean word. Every edge of `G[B]` changes exactly one coordinate, and criticality canonically orients it in the increasing coordinate direction. Every zero coordinate has a unique outgoing flip. This produces a directed Boolean-coordinate flow. A factorial path count, combined with criticality of root edges, gives an order cutoff: any non-bipartite graph in this exact boundary satisfying `m >= floor((n-1)^2/4)+1` has `n<=294`.

We then show that root-edge criticality has a stable perturbative form. Every triangle-active neighbour of the root either possesses a private `A`-neighbour or has an antipodal `B`-vertex with disjoint `A`-support. The private alternative is controlled by the edges inside `A`; the antipode alternative forces an explicit residual/defect payment. This identifies the first obstruction to extending Boolean flow away from the exact boundary and supplies a structural dichotomy for subsequent near-extremal analysis.

## 1. Introduction

### 1.1 Context

Diameter-2-critical (D2C) graphs have diameter two and lose that property after deletion of any edge. The classical Murty–Simon problem concerns their maximum number of edges; a separate second-extremal line studies graphs near `floor((n-1)^2/4)+1` edges. The present paper does **not** claim an eventual second-extremal classification. Its purpose is to isolate a structural boundary mechanism and quantify its first perturbation.

### 1.2 Why Boolean structure appears

At the exact zero-residual boundary, the criticality representative attached to an internal `B`-edge determines a unique missing/incident `A`-coordinate. The criticality axioms then force all other coordinates to agree. This turns `G[B]` into a directed subgraph of a Boolean cube, possibly with repeated code fibres subject to the canonical constraints.

### 1.3 Contributions

Provisional contributions, subject to novelty clearance:

1. Boolean coding of the exact zero-residual non-bipartite boundary;
2. unique outgoing coordinate flips and directed coordinate-flow structure;
3. factorial path-growth inequality `z! <= b lambda^z`;
4. root-criticality forcing a code with at least `ceil(a/2)` zero coordinates;
5. the consequent second-extremal boundary cutoff `n<=294`;
6. an explicit hypercube-face family as a hostile/model example, without a novelty claim at present;
7. the root-edge antipode-or-private-foot dichotomy;
8. private-foot injection into the nonisolated part of `G[A]` and the resulting perturbative inequalities.

## 2. Canonical maximum-degree-root notation

Let `v` be a maximum-degree root,

`B=N_G(v)`, `A=V(G)\N_G[v]`, `b=|B|`, `a=|A|`.

Let `F=G[A]` and `f=e(F)`. Retain the canonical selected/residual construction from the research programme, but restate every piece needed by this paper so the manuscript is self-contained.

Use:

- `Q=e(G[B])`;
- residual source values `rho_u` and `r=sum rho_u`;
- defect `delta=r-f=b(n-b)-m` in the current canonical ledger;
- `lambda=2b-n`;
- appropriate incoming/outgoing selected counts `p_u,q_u`.

Every identity inherited from the canonical bridge must be reproved or cited to a theorem proved in this paper; no hidden repository notation is acceptable in the finished manuscript.

## 3. Exact zero-residual Boolean coding

Assume

`t=0`, `F=empty`, and hence `r=0`,

and assume `G` is non-bipartite, so `Q>0` in this boundary.

For `u in B`, define

`c(u) in {0,1}^a`, with `c_i(u)=1` iff `u a_i in E(G)`.

### Theorem 3.1 — one-coordinate edges

Every edge `uw` of `G[B]` joins two codes at Hamming distance exactly one. The selected criticality representative determines the changed coordinate.

### Theorem 3.2 — canonical orientation

Orient `uw` from the endpoint whose changed coordinate is `0` to the endpoint whose changed coordinate is `1`. For every `u` and every zero coordinate of `c(u)`, there is exactly one outgoing edge flipping that coordinate, and there are no other outgoing `B`-edges.

Explain carefully what multiplicities of equal codes are or are not permitted by the canonical construction.

## 4. Factorial path growth

Let `z(u)` be the number of zero coordinates of `c(u)`. From a vertex with `z` zeros, every ordering of its zero coordinates generates a monotone directed path of length `z` to an all-one fibre. This gives `z!` paths.

The maximum-degree bound gives directed indegree at most

`lambda=2b-n`.

Therefore each endpoint receives at most `lambda^z` such paths per starting-fibre accounting, yielding the central inequality

`z! <= b lambda^z`.

This section needs a completely explicit treatment of repeated code fibres and path collisions.

## 5. Root criticality forces a large-zero code

Use criticality of a root edge `vu`. When `u` is triangle-active, deletion of `vu` cannot be witnessed by `(v,u)` itself through that triangle. In the exact independent-A boundary, the surviving critical pair forces another `B`-vertex with disjoint `A`-support.

Thus, if `u` has `z` zero coordinates, its antipodal partner has at least `a-z` zero coordinates, so some code has

`z >= ceil(a/2)`.

State separately the degree/no-leaf facts used to exclude the private-A alternative in the exact boundary.

## 6. Boundary order cutoff

Combine `z>=ceil(a/2)` with `z!<=b lambda^z` and the density condition

`m>=floor((n-1)^2/4)+1`.

The current audited derivation first gives a hand cutoff for large `a`, then checks the remaining finite integer range exactly. The strongest surviving necessary arithmetic point is

`a=134`, `lambda=24`, `z=67`, `b=159`, `n=294`.

> **Theorem 6.1 (internal candidate).** Any non-bipartite D2C graph in the exact canonical boundary `t=0`, `F=empty`, `r=0` with `m>=floor((n-1)^2/4)+1` has `n<=294`.

The theorem does not claim existence at `n=294`; that point is only an arithmetic survivor of necessary conditions.

Before submission, decide whether the finite check can be shortened analytically or presented as a tiny certified appendix.

## 7. Hypercube-face model family

For `k>=3`, define `X_k` on

`{r} union {a_1,...,a_k} union {0,1}^k`

by taking the cube vertices to induce `Q_k`, joining `r` to every cube vertex, and joining `a_i` exactly to cube vertices with i-th coordinate zero.

Give the elementary edge-type proof that `X_k` is D2C.

Parameters:

`n=2^k+k+1`, `m=(k+1)2^k`.

For `k=3`, this produces a 12-vertex, 32-edge graph matching the coarse invariants of the known published obstruction; authoritative isomorphism certification remains a separate task and should not be assumed in the theorem statement.

For `k>=4`, prove that this natural continuation falls below the second-extremal comparison threshold. This makes the family a useful model of a finite obstruction that self-dilutes.

**Novelty warning:** do not call the `X_k` family new until a dedicated construction search is complete.

## 8. Root-edge antipode-or-private-foot dichotomy

Move away from the exact boundary. Call `u in B` triangle-active if it has a neighbour in `B`.

> **Theorem 8.1 (internal candidate).** For every triangle-active `u`, criticality of the root edge `vu` forces one of:
>
> 1. a **private foot** `x in A` with `N_G(x) cap B={u}`;
> 2. an **antipode** `w in B\{u}` with `uw` a nonedge and `N_G(u) cap N_G(w)={v}`.

The proof should be written directly from the effect of deleting `vu`: `(v,u)` remains at distance two via a rooted triangle, so any newly distant pair whose old shortest path used `vu` is of one of the two stated forms.

## 9. Quantitative stability consequences

Let `P` be the set of triangle-active `B`-vertices with a private `A`-neighbour. In a non-star D2C graph, a private `A`-vertex cannot be a leaf, so it is incident with an `F`-edge. Consequently

`|P| <= nu(F) <= 2e(F)`,

where `nu(F)` here denotes the number of nonisolated vertices of `F` (rename in final manuscript to avoid collision with matching-number notation).

If a triangle-active source has no private foot, the antipode has disjoint `A`-support. Writing the canonical cross-deficit at a source as `h_u=q_u+rho_u`, obtain

`h_u+h_w>=a`,

and hence globally

`Q+r>=a`.

Combining with the canonical source inequality `Q<=r+b lambda` gives

`2r+b lambda>=a`,

or equivalently in the current defect variables

`2 delta + 2e(F) + b(2b-n) >= a`.  (RSD)

If every triangle-active source is private-supported, then all rooted-triangle edges lie among at most `2e(F)` active vertices, yielding

`Q <= binom(min(b,2e(F)),2)`.  (PRIVATE)

Thus the perturbative problem splits into an explicit antipode-payment branch and an all-private branch controlled by internal `A`-structure.

## 10. Current frontier

The next mathematical objective for this paper is not a broad scan. It is to understand the **all-private branch**:

- classify how private `A`-feet can sit inside `F`;
- use criticality of incident `F`-edges;
- look for forced small cyclic/twin quotients or further residual charge;
- then return to factorial/Boolean expansion on the antipode branch.

A successful bound that forces `e(F)` or residual mass to grow with `a` would turn the present stability dichotomy into a substantially stronger near-extremal theorem.

## 11. Literature obligations

The paper must be positioned against:

- classical D2C/Murty–Simon literature;
- Füredi’s sufficiently-large theorem;
- the strengthened/second-extremal conjectures and dominating-edge results;
- the 2023 small-order enumeration and 2024 primitive-D2C constructions/counterexample literature;
- the 2025 `C5`-free second-extremal classification;
- any known hypercube, product, or Boolean-code constructions of D2C graphs.

No novelty claim for the Boolean-flow formulation, the `X_k` family, or the stability lemma is authorised until this comparison is complete.

## 12. Current trust boundary

The cutoff and stability dichotomy are internal hand results with finite regression/checking where stated. They are not externally reviewed. This paper does not claim an eventual second-extremal classification, does not claim the 12-vertex reconstruction is authoritatively the published graph, and does not claim first-solution priority for Murty–Simon/Erdős #742.
