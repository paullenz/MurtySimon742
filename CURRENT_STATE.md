# Murty–Simon / Erdős #742 — live current state

> Read this first. The d=2 exception has been reduced to a private-witness normal form; the complete symbolic derivation is preserved below before further attack. No exclusion of this family is claimed yet.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `WIP_INTERNAL_D2_PRIVATE_WITNESS_NORMAL_FORM_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Theorem-first priority. One bounded normal-form derivation, not a survivor scan.

**INSPECTED PREDECESSOR:** `cf718afcba303618f2231b95d452b9af5671c8d8`, tree `988f21417e5d63396ef22154786542d92fe9c929`, CURRENT_STATE blob `0b257681052ea383e008bb51cc3fa82ea55c214d`. Main was re-read before this contents update; the preceding full handoff, proof and evidence remain at that immutable commit.

**LAST VERIFIED RESULT:** new internal symbolic reduction, finite verification pending. For the remaining d=2 intrinsic-defect-one family, write C for c>=2 common labels, k for the unique singleton adjacent to s, X=V_t and Y=V_s. Original criticality of ts forces N_G(t) intersect N_G(k)={s}. The full quasi-edge identities then force N_G(k)={s} union Y, N_F(k)={s}, every O-vertex residual set {k}, and a function f:X->Y with |X|=c, |Y|=c-1 and N_G(x) intersect Y={f(x)}. Every function edge satisfies S_x={k} disjoint-union S_f(x). Some receiver therefore has two sources with identical selected sets and A-neighbourhoods. This is not yet a redundant-edge proof: full B-neighbourhoods need not coincide.

**SCOPE:** actual full canonical system and all-edge criticality, exact d=2 block and intrinsic defect one. No positive-surplus assumption. Both tight vertices are maximum-degree vertices, as is the pivot. The previous d>=3 one-defect closure and conditional quadratic clique-defect theorem are unchanged.

**CHECKS:** new finite tests NOT_RUN. No rerun of earlier 506403 records, graph realization, catalogue application or external acceptance is claimed. All derivations are by the same assistant. Literature novelty and external review OPEN.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Prior 203-key candidate union, 41 strict/equality certificates, 170-candidate audit and state3349 retain their previous boundaries. No workflow launch, q-enumeration or promotion.

**UNPRESERVED WORK:** no completed symbolic finding remains only in session memory after remote confirmation; full derivation below. Earlier raw-stream and attachment transfers remain pending.

**DEFERRED ADMIN:** older evidence transfers; root README/reviewer integration; unrelated CI/status work; independent review, novelty assessment and promotion.

**NEXT ACTION:** continue this same d=2 normal-form attack: determine whether a fibre of f with at least two sources forces a redundant original edge using the full representative system, or characterize the remaining freedom. Do not equate shared A-neighbourhoods with full twins. Verify the resulting graph/representative implications and preserve exact controls before asserting closure.

**PROCESS RULE:** one bounded unit then immediate preservation and one remote confirmation; no background-work claim or automatic promotion.
<!-- CURRENT-STATUS:END -->

## Preserved derivation: defect-one d=2 private-witness normal form

Use the full canonical representative system of an actual diameter-two edge-critical graph G, J its complement, and the minimum-J-degree pivot p. Assume an exact d=2 block T={t,s}, H={h:rho_h>=2}, |H|=2, and intrinsic defect L+beta+2mu=1. All K-labels have demand zero; beta=0, mu=0. Let C consist of the common K-labels, |C|=c, and let k be the unique singleton K-label, adjacent in F=G[A] only to s among T. Let

    X=V_t (residual set {s}), Y=V_s (residual set {t}),
    O=B minus (H union X union Y), Z=A minus (T union C union {k}).

The exact tight rows give |X|=c, |Y|=c-1, c>=2. The inherited full-pool saturation gives all C-X and C-Y edges in G. Exact tight neighbourhoods are

    N_G(t)={s} union C union X union O,
    N_G(s)={t,k} union C union Y union O.                 (N1)

### 1. Criticality forces the only remaining private witness

Deleting ts preserves the endpoint distance via any member of C. Every affected pair involving an exclusive neighbour in X or Y retains a path through C. The only remaining potentially damaged pair is {t,k}. Therefore original edge-criticality forces

    N_G(t) intersect N_G(k)={s}.                         (N2)

In particular k has no G-neighbour in C, X or O. Its J-edges to X are selected: the unique residual label there is s. Its J-edges to O cannot be selected, because selection of k requires its F-neighbour s to be present in J at the source; s has no J-occurrence in O by beta=0. Therefore

    R_o={k} for every o in O.                            (N3)

O is allowed to be empty; no positive pivot surplus is assumed.

### 2. All singleton obligations end in Y

The label k is residual at both high vertices and is present in J at every X or O vertex by (N2). At any y in Y it is absent in J: it is not the residual label t, and selection would require s present in J at y, which is impossible. Thus an actual selected obligation (x,k), x in X, has its destination f(x) in Y.

The canonical residual-union inclusion applied to this obligation yields

    N_F(k) subset R_x union R_f(x)={s,t}.

But k is not adjacent to t in F and is adjacent to s. Hence N_F(k)={s}. Combining all A- and B-parts gives the exact full neighbourhood

    N_G(k)={s} union Y.                                 (N4)

For each x in X, the quasi-edge identity says the unique common G-neighbour of x and k is f(x). Since xs is absent in G, (N4) gives

    N_G(x) intersect Y={f(x)}.                          (N5)

Thus the entire X-Y subgraph is a function graph X->Y, with |X|=|Y|+1; at least one receiver has two distinct preimages. No injectivity is assumed or inferred.

### 3. Selected sets agree across every function edge

For x in X, y=f(x), forward selected containment gives S_x minus {k} subset N_J(y) intersect A={t} union S_y. No low source selects t, hence S_x minus {k} subset S_y. Reverse selected containment gives S_y subset {s} union S_x. No low source selects s, and k is absent at y, so the converse holds. Consequently

    S_x={k} disjoint-union S_f(x),
    N_J(x) intersect A={s,k} disjoint-union S_f(x),
    N_J(y) intersect A={t} disjoint-union S_y.            (N6)

Two distinct preimages of one y have exactly the same selected sets and A-neighbourhoods. This does not establish equality of their entire B-neighbourhoods or prove that either is removable.

### 4. Exact auxiliary consequences

The singleton is residual at exactly H union O and selected at exactly X, hence

    delta_k=1, R_k=2+|O|, x_k=c, s_k=0.                 (N7)

By (N1), both tight vertices have degree 2c+1+|O|=|B|. They, as well as p, are maximum-degree vertices in G, independently of the number of labels in Z.

### Limits and next step

The family is reduced, not excluded. Next test whether a fibre of size at least two forces a redundant original edge under the complete representative identities, or characterize the remaining freedom without asserting that shared A-neighbourhoods are full twins. Preserve failures and graph controls; do not report a survivor reduction.

The prior critical-edge covering proof and exact verification sources remain in `project/research/general_n/2026-09-16-critical-edge-covering-v1/` at the inspected predecessor. The main milestone remains a comparatively short structural treatment, not incremental survivor counts.
