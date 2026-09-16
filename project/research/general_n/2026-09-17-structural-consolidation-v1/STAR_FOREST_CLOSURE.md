# Zero-loss star forests and strict universal defect

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**WIP_UNVERIFIED: complete hand derivation preserved before fresh finite checks. Not promoted; external review and novelty open.** This is a fresh reconstruction from the published source proofs, not a claim to have recovered the byte-identical attachment described in another chat.

## Scope and statement

Retain the full canonical representative system of a diameter-two edge-critical graph G and its whole exact levels T={i:s_i=d}, H={u:rho_u>=d}, |T|=|H|=d. Let Q=G[T], K=N_G(T) intersect (A minus T), mu=binom(d,2)-e(Q), and let the full low pools be V_t={v outside H:R_v=T minus {t}}, p_t=|V_t|, m=sum p_t. Use the established nonnegative integers L,beta and intrinsic defect D=L+beta+2mu. Define W as in the pinned interface theorem.

**Claim.** For every d>=5,

    D >= 2 floor(d/2)+1,
    W >= d+(d-1)m+2 floor(d/2)+1.

Thus W>=d^2+2 floor(d/2)+1, and extra high-source selections require W>=d(2d-1)+2 floor(d/2)+1. At d=5 this is D>=5 and W>=30, or W>=50 when extras exist. These are necessary exact-block conditions, not a global conjecture proof, sharpness claim or catalogue promotion.

## 1. Published prerequisites

The graph-to-interface theorem is preserved in CURRENT_STATE.md at commit 4cb18222e4c0f56c2a5278f424c8414a09c469f7. It derives from actual quasi-edge representatives, rather than numerical routings: tight labels selected at all H and nowhere else; K residual at H; source eligibility; residual-union containment; nonempty full pools; and extra selections implying m>=2d.

The universal-core theorem is project/research/general_n/2026-09-16-universal-core-defect-v1/UNIVERSAL_CORE_DEFECT.md at commit 3353576e458b1ccfd025a38bfb06eb3b5c6e5dc5. It gives

    D >= 2mu+(d-2)max(0,d-2mu-1) >= 2 floor(d/2).

Write ell_k=|N_G(k) intersect T|, with w_k=d when s_k=0 and w_k=d-1 otherwise. These are the actual interface weights because all full pools exist. Let kappa=|K|. The exact identities are

    L=sum_K(w_k-ell_k),
    beta=sum_t[R_t-(m-p_t)],
    sum_K w_k=d+(d-1)m+L+beta+2mu,
    W-d-(d-1)m=P+D, P>=0.

No prior finite check is represented as freshly replayed by this note.

## 2. Zero loss with a common label forces a star forest

Suppose L=beta=0. Every K-label has tight support either all of T (weight d), or all of T except one label (weight d-1). Write C for the common-label class and X_t for the class missing only t. Suppose C is nonempty and choose c in C.

The condition beta=0 exhausts every residual tight incidence in the full pools. With O=B minus (H union V), the entire tight neighbourhood is

    N_G(t)=N_Q(t) union (K minus X_t) union O union V_t.

This is an equality in the original graph: p has no G-edge to A, A-labels outside T union K have no tight neighbours, high vertices select T, low vertices select no T, and beta=0 prohibits additional residual tight incidences outside V.

The common label c is adjacent in G to every pool vertex. To prove this, first observe that c cannot be selected at a high vertex because all K is residual there. It cannot be selected at a low vertex either: its d tight neighbours must all be present in that source's J-neighbourhood by domination, none can be selected there, and its residual degree is less than d. Hence c is never selected. It is not residual at a pool vertex, whose residual set is T minus one label. Therefore it is absent in J, and present in G, at every pool vertex.

Consider an edge ts of Q with deg_Q(t)>=2 and deg_Q(s)>=2. Delete it. Its endpoints still have t-c-s. Every other potentially destroyed path of length at most two has endpoints t,x where x is an exclusive neighbour of s, or the reverse. The displayed neighbourhood partition accounts for all such x:

* For x in T, use t-c-x.
* For x in X_t, choose r in N_Q(t) minus {s}. The degree premise guarantees r; x misses only t in T, so t-r-x remains.
* For x in V_s, use t-c-x.

No O-vertex is exclusive; high vertices, p and labels outside T union K contribute none. Reverse t and s for the other direction. Thus every previously short pair stays short, contrary to edge-criticality.

Consequently every Q-edge has an endpoint of degree one. Every nontrivial connected component is a star: if a component had two vertices of degree at least two, a shortest path between them would contain an edge whose endpoints both had degree at least two. Isolated vertices are allowed. In particular e(Q)<=d-1 and

    2mu >= (d-1)(d-2).

The common-label assumption is essential to this lemma as stated; it is forced at the particular numerical boundary below, not asserted at every zero-loss configuration.

## 3. Equality in the universal bound is impossible

Put r=2 floor(d/2), and suppose D=r. Since L,beta>=0, 2mu<=r. If 2mu<r, its even value is at most r-2. The function

    f(x)=x+(d-2)(d-x-1)

is decreasing for d>=5. For even d this gives D>=f(d-2)=2d-4>d=r. For odd d it gives D>=f(d-3)=3d-7>d-1=r. In both cases the positive part in the universal-core bound is active throughout the interval used. These contradictions force

    2mu=r, L=beta=0.

Let z=|C|. Every K-label then contributes either d or d-1 incidences, giving

    (d-1)kappa+z=d+(d-1)m+r.

For odd d, z is 1 modulo d-1. For even d, z is 2 modulo d-1. Since d>=5, neither residue is zero, so z>0. The star-forest lemma now gives r>= (d-1)(d-2), impossible: r<=d and (d-1)(d-2)>d for d>=5.

Therefore D>r, and integrality proves the claim. The W consequences follow from P>=0, m>=d and, when extras exist, m>=2d.

## 4. Boundary and continuation

For d=5 the old D=4 boundary has Q=K5 minus two disjoint edges. The argument closes it as part of the parameter-wide theorem, not by an individual state scan. It does not exclude D=5, does not establish that every graph has an exact block, and does not settle configurations without one.

The next bounded mathematical question is to classify how a single unit of L or beta could protect all tight edges when d=5 and D=5; do not assume the zero-loss partition remains exact in that case. First run fresh local-lemma checks with an independently structured path checker, include controls violating the degree, support and pool-protection premises, and preserve exact inputs and decisions. Then assemble one short treatment with the pinned prerequisites and precise proof obligations.
