# A bounded-hole deletion lemma closes the next defect boundary

17 September 2026. Paul Lenz / ChatGPT-Geeps.

**WIP_UNVERIFIED.** Complete new hand derivation preserved before fresh bounded-hole tests. The predecessor proves D>=2floor(d/2)+1 for actual exact blocks d>=5. This note strengthens that conclusion by one more unit; no catalogue promotion or external acceptance.

## Local lemma

Let T induce Q in a graph G. Suppose a vertex c outside T is adjacent to every T-vertex. Every other vertex outside T either has no T-neighbour, misses at most h vertices of T, or has exactly one T-neighbour and is adjacent to c. If ts is an edge of Q and both endpoints have Q-degree at least h+1, deleting ts preserves every pair previously at distance at most two.

Proof. The endpoints retain t-c-s. An affected pair with different endpoints has the form t,x for an exclusive neighbour x of s, or the reverse. If x is tight, use t-c-x. If x is a protected singleton neighbour, use t-c-x. Otherwise x misses t and at most h-1 other tight vertices. The set N_Q(t) minus {s} has at least h vertices, so one of them, r, neighbours x. Use t-r-x. Reverse t,s for the other direction. These cases cover every path of length at most two using the deleted edge. Edges among the external vertices are unrestricted.

The star-forest lemma is the h=1 case. This note uses h=2 and endpoint degree at least three.

## Exact-block boundary

Use the definitions and pinned graph-to-interface and universal-core sources in STAR_FOREST_CLOSURE.md. Put r=2floor(d/2), d>=5. The predecessor rules out D=r. Suppose D=r+1.

First, 2mu=r and L+beta=1. Indeed 2mu is even and at most r. For 2mu<=r-2 the universal-core envelope is at least 2d-4 for even d>=6, and at least 3d-7 for odd d>=5. These are strictly larger than r+1. The exact defect identity then gives L+beta=1.

Let g be the number of universal vertices of Q and let M be its missing-edge graph. The universal-core inequality implies (d-2)max(0,g-1)<=1, hence g<=1. The d-g nonisolated vertices of M have total degree 2mu=r. Each of them therefore has degree at most r-(d-g-1). For odd d, r=d-1 and g<=1, so its maximum degree is at most one. For even d, r=d and g<=1, so its maximum degree is at most two. Universal vertices of Q have no missing neighbours. Consequently every Q-vertex has degree at least d-2 in the odd case, or d-3 in the even case: in either case at least three.

Next there is a common interface label. Let kappa=|K| and a0 be the number of zero-demand K-labels, hence the number with weight d. The others have weight d-1. The exact weight identity reads

    (d-1)kappa+a0=d+(d-1)m+r+1.

Thus a0 is 2 modulo d-1 for odd d, and 3 modulo d-1 for even d. Since L<=1, at most one zero-demand label can fail to have all d tight neighbours. Therefore the actual common-label count z satisfies z>=a0-1>=1. (For even d it is at least two.) Choose such a common label c. As in the predecessor, domination and the low residual-degree ceiling forbid any selection of c; thus c is adjacent in G to every full pool vertex.

Finally check every external vertex against the h=2 lemma. For k in K, its loss w_k-ell_k is at most L<=1 and w_k>=d-1, so ell_k>=d-2. Every high vertex, the pivot and every A-label outside T union K has no tight G-neighbour. Every full pool vertex has exactly one tight G-neighbour and is adjacent to c. For a remaining B-vertex, no tight incidence is selected; all its missing tight G-neighbours are residual tight incidences counted in beta. Since beta<=1, it misses at most one tight vertex. This classification exhausts the original graph.

Every tight edge now satisfies the h=2 lemma, because all Q-degrees are at least three. There is at least one such edge. Its deletion preserves diameter two, contradicting edge-criticality. Hence D=r+1 is impossible, and

    D >= 2floor(d/2)+2                         (d>=5).

Consequently

    W >= d+(d-1)m+2floor(d/2)+2,
    W >= d^2+2floor(d/2)+2,
    extras => W >= d(2d-1)+2floor(d/2)+2.

At d=5 this is D>=6 and W>=31, or W>=51 with extras. Neither D=6 nor attainability is decided by this note. Exact-block coverage for arbitrary graphs remains open.

## Verification target and provenance

The hand proof is the general argument. The next finite check exhausts distinguished-edge Q for d=4,...,6 with endpoint degrees at least three, and every external probe having at most two holes, no tight neighbours, or one protected tight neighbour. A separate C++ path checker must agree per record. Include negative controls for degree two, three holes, absent common label and unprotected singleton neighbours.

The strict predecessor, its 324554-record tests and their hashes remain unchanged at commit 072b24bfbd256b0d941725460e944da7cb402eae. No fresh 11357-record universal-core replay is claimed. This extension is a new derivation in this continuation, not a byte-restored old attachment.
