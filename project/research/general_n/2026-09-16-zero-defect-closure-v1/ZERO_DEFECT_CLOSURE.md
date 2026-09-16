# Zero-defect tight blocks force a noncritical edge

**16 September 2026 — internal hand proof; not promoted; external review open.**

Research directed by Paul Lenz; mathematical derivation and implementations by ChatGPT/Geeps. Canonical repository: `paullenz/MurtySimon742`. This unit follows the interface-capacity theorem recovered at commit `4cb18222e4c0f56c2a5278f424c8414a09c469f7`.

## Result and scope

The zero-defect boundary of the preceding interface theorem is impossible in a diameter-two edge-critical graph. This holds for **every receiver-pool size**, not only the first boundary `W=d^2`.

In the full canonical representative system, assume the whole levels

    T={i:s_i=d}, H={u:rho_u>=d}, |T|=|H|=d>=2.

Use the full receiver pools `V_t={v outside H:R_v=T\{t}}`, their union V, and `m=|V|`. Retain the weighted capacity W from the preceding theorem. Then

    W >= d+(d-1)m+1.                                      (1)

Consequently

    W >= d^2+1,
    E>0 implies W >= d(2d-1)+1.                           (2)

For d=5 these lower bounds are 26 and 46. Their significance is **closure of an entire structural branch**, not an additional catalogue count. No positive pivot-surplus hypothesis, graph enumeration, or upper bound on d or m is used.

The proof invokes original edge-criticality inside the tight-label clique, beyond the conditions on representatives of edges inside B. This distinction matters: the older local selected-system relaxation really can attain zero defect, as explicit noncritical graph controls below demonstrate. The strengthened conclusion must not be applied to that relaxation as though criticality of all original edges had already been checked.

## 1. Established notation and the exact identity

Let G be diameter-two edge-critical, J its complement, p a minimum-degree vertex of J, A=N_J(p), B=V(J)\N_J[p], and F=G[A]. Choose one actual quasi-edge representative `(u,i)->v` for each unordered edge uv of G[B]. At a B-vertex u, partition its A-neighbours in J as `S_u` selected and `R_u` residual; let `rho_u=|R_u|`. At i in A, let R_i count its residual incidences and put `s_i=max(0,deg_F(i)-R_i)`.

The preceding theorem derives directly from this graph construction: label demand and source eligibility; distinct destinations and no opposite selected orientations; forward and reverse selected containment; and

    N_F(i) subset R_u union R_v for every (u,i)->v.        (3)

It proves that every high vertex selects T, no low vertex selects T, and `K=N_F(T)\T` is residual at every high vertex. In particular `|K|<=c=min_H rho` and `R_k>=d`. A positive-demand k in K has both ends of a selected obligation low, so (3) gives `s_k<=d-2`.

Define lambda_j to be the j-th largest low residual degree. For i outside T the earlier weight is d if s_i=0; it is lambda_(s_i) when `1<=s_i<=d-2`, that index exists and lambda_(s_i)>=s_i; otherwise it is zero. W is the sum of the largest `min(c,|A\T|)` weights.

**Useful simplification on any actual exact-block realization.** There are at least d full receiver vertices of residual degree d-1. Therefore `lambda_j=d-1` for `1<=j<=d`. In particular every k in K has weight d at zero demand and d-1 at positive demand. This simplification is not asserted for arbitrary infeasible scalar inputs before the receiver-count condition has been established.

Write

    ell_k=|N_F(k) intersect T|,
    L=sum_(k in K)(w_k-ell_k),
    beta=sum_(t in T)[R_t-(m-|V_t|)],
    mu=binom(d,2)-e(F[T]),
    P=W-sum_(k in K)w_k.

All four numbers P,L,beta,mu are nonnegative integers. The exact identity already proved is

    W-d-(d-1)m = P+L+beta+2mu.                            (4)

We prove the stronger intrinsic assertion

    L+beta+2mu >= 1.                                     (5)

Thus the contradiction does not depend on any unused top-c capacity P.

## 2. Zero defect gives an explicit neighbourhood partition

Suppose, for contradiction, that `L=beta=mu=0`.

Since mu=0, T induces a clique in G. Since beta=0, all residual occurrences of tight labels are in V. All their selected occurrences are at H. Let `O=B\(H union V)`.

Since L=0, every k in K attains its weight. A zero-demand k is adjacent in F to all d tight labels. A positive-demand k is adjacent to exactly d-1 tight labels. Partition K into

    C = labels adjacent to every t in T,
    Q_t = labels whose only missing tight neighbour is t.

For d=2 there are no positive-demand labels in K (their demand is at most d-2=0), so every Q_t is empty. For d>=3 the Q_t contain the positive-demand labels. Set `z=|C|` and `q=sum_t|Q_t|`.

The exact interface count gives

    d*z+(d-1)*q = d+(d-1)*m.                             (6)

If d>=3, reducing modulo d-1 gives `z=1 mod (d-1)`, so z cannot be zero. If d=2, q=0 and (6), with m>=2, gives z>=2. Thus in every case there exists a common label c0 in C.

A common label cannot be selected at a low vertex: its d tight neighbours must all be present by quasi-edge domination, none can be selected there, and fewer than d residual slots are available. It is residual, not selected, at H. Hence it is never selected anywhere. At every v in V, its residual set lies in T and does not contain c0; nor can it select c0. Therefore c0v is an edge of G. Also c0 is adjacent in G to every tight label by definition.

For each t in T the entire original G-neighbourhood is now

    N_G(t) = (T\{t}) union (K\Q_t) union O union V_t.     (7)

To check that this is exhaustive: p has no G-edge to A; labels outside T union K have no F-edge to T by definition; all high vertices contain every tight label in J; the full pools give exactly the stated residual tight occurrences; and beta=0 forbids any additional ones in O. Equation (7) retains the whole graph, not merely the induced T-K subgraph.

## 3. Every tight edge is redundant

Fix distinct t,s in T and delete the edge ts of G. We show that every pair previously at distance at most two still has distance at most two.

Any path of length at most two that is destroyed uses ts. Its endpoints are either t,s themselves, or t,x with x adjacent to s, or s,x with x adjacent to t. If x is already adjacent to the other endpoint, that direct edge remains. It is therefore enough to check the endpoints and the exclusive neighbours.

The pair t,s retains the path `t-c0-s`. By (7),

    N_G(s)\(N_G(t) union {t}) = Q_t union V_s.

If x is in V_s, the path `t-c0-x` remains because c0 is adjacent to every pool vertex. If x is in Q_t, then d>=3 and x is adjacent to every tight label except t. Choose `r in T\{t,s}`. The path `t-r-x` remains and does not use ts. For d=2 this case is absent because Q_t is empty.

The reverse direction is identical with s and t interchanged. All affected vertex pairs are covered; pairs with neither endpoint t nor s cannot have a destroyed path of length at most two using ts. Thus `diam(G-ts)<=2`, contradicting edge-criticality.

This proves (5), then (1) by (4). Since m>=d, the first bound in (2) follows. When E>0 the preceding destination-colouring theorem forces every pool to have at least two vertices, so m>=2d and the second bound follows. **Both previously described scalar boundary equalities are therefore impossible in the original graph class.**

## 4. Finite checks and why they are not vacuous

`check_redundancy.py` computes reachable-within-two sets before and after each tight-edge deletion. A separately written C++ program instead tests paths of length zero, one or two by explicit intermediate-vertex search. Their full per-graph outputs agree on **8,601 records**, with input and decision hashes in the recorded check summary.

The positive local-lemma tests comprise **8,342 exhaustive completions** of seven specified small neighbourhood partitions and **240 seeded varied completions**. They cover **34,539 tight-edge deletions**, with no lost distance-at-most-two pair. Among these graphs, 7,200 have diameter two before deletion. These tests exercise nonempty one-hole classes and differing pool sizes, but are not a census of canonical graphs or of any survivor catalogue.

There are also **14 explicit noncritical graph controls**, for d=2,...,15. Take disjoint sets T,C,H,V of size d, two vertices O, and pivot p. Add: all edges in T; all T-C, H-V and C-V edges; the matching t-v_t; all p-(H union V union O) edges; and all O-(T union C) edges. Add no other edges.

Each constructed graph has diameter two and maximum degree at p. Its full G[B] edges have the exact representatives `(h,t)->v_t`. These yield the exact tight block, `rho_H=d`, `rho_V=d-1`, `rho_O=0`, and `W=d^2`. The test checks these facts directly, including the quasi-edge identities, all represented B-pairs, demand, containment and residual injections. But deleting any T-edge leaves diameter two, as predicted: **560 tested deletions**. Its pivot surplus is `-d(d-1)/2`, not a positive-surplus or Murty–Simon counterexample. These controls demonstrate that the new global-criticality input is substantive rather than an algebraic contradiction already present in the earlier relaxation.

Five negative controls remove, respectively, the common label, a required common-to-pool edge, the d=2 prohibition on one-hole labels, the restriction against a two-hole/off-pool defect, or completeness of T. All five have diameter two and exhibit at least one destructive tight-edge deletion. They prevent dropping the proof's essential conditions. The arithmetic forcing C to be nonempty was additionally checked on 9,442 bounded integer solutions.

The tests support the named finite steps; the hand proof establishes the parameter-free conclusion. Both implementations and the proof are by the same assistant. No external acceptance, original-graph enumeration of the conjecture, new catalogue exclusion, promotion, or novelty claim is made.

## 5. Next structural question

The zero-defect branch is closed. The next target is the **smallest positive intrinsic defect** in (5). At intrinsic defect one, the tight graph is still complete, and exactly one unit must come from either beta (an extra tight residual occurrence) or L (one missing unit of tight-neighbour capacity). Determine whether that single defect can supply indispensable witnesses for every tight edge, or whether further defect is forced. Keep d=2 and d=3 separate where their short alternative paths differ.

This is a stated next proof obligation, not a claim that intrinsic defect one has already been excluded. Configurations without the exact tight-block hypothesis and larger-defect configurations remain outside this closure. The complete unrestricted conjecture is not claimed proved.

## Sources and preservation

The complete preceding graph-to-interface theorem is recovered in `CURRENT_STATE.md` at commit `4cb18222e4c0f56c2a5278f424c8414a09c469f7`. The earlier 17-file bundle is preserved unchanged with SHA256 `d948e286846e53c569a748cf7bce0f8c3bc4bd5547c6333e46e9ceec0feb6b8e`.

For background only, the classical complement/total-domination and quasi-edge framework is described in Tao Wang, Ping Wang and Qinglin Yu, *On Murty-Simon Conjecture II*, arXiv:1301.0460v1 (2013), Sections 1–2, https://arxiv.org/html/1301.0460v1. That source is not asserted to contain the new zero-defect argument; a full literature novelty assessment remains open.

The complete raw evidence is in the SHA256-identified attachment recorded in CURRENT_STATE.md. Run the two accompanying sources to regenerate CHECK_RESULTS.json and both gzip tables. Their separate raw GitHub paths are not claimed installed by this source-first publication.
