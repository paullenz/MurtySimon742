# Closing the d=2 singleton-defect exception

16 September 2026. Internal hand proof and executed finite verification; not promoted. External mathematical review and literature novelty remain open. Research directed by Paul Lenz; derivation and verification development by ChatGPT/Geeps.

This proof continues `cf718afcba303618f2231b95d452b9af5671c8d8` and the private-witness reduction preserved at `81067c78adc18c1bb4c3792c289d168af20f0540` in `paullenz/MurtySimon742`. It uses original all-edge criticality, not merely feasibility of the selected/residual relaxation.

## Theorem and scope

In the full canonical representative system of an actual diameter-two edge-critical graph, an exact d=2 tight block cannot have intrinsic defect one. Together with the preceding zero-defect closure and the d>=3 critical-edge covering theorem, this gives

    L+beta+2mu >= 2 for every exact block |T|=|H|=d>=2.   (1)

Accordingly the weighted interface capacity satisfies

    W >= d+(d-1)m+2,
    W >= d^2+2,
    E>0 implies W >= d(2d-1)+2.                         (2)

No positive pivot-surplus hypothesis, fixed graph order or receiver-pool upper bound is required. The larger quadratic increment (d-1)(d-2) still requires a complete tight graph and d>=3. Graphs without an exact tight block, and larger intrinsic defects, are not excluded by this theorem.

For d=2 the generic scalar thresholds 6 and 8 already follow by rounding the preceding bounds 5 and 7 because W is even. The advance is the exclusion of the entire one-defect structure and the stronger joint W,m inequality, not a misleading extra improvement to those rounded scalar thresholds.

## 1. Canonical facts used

Let J be the complement of G. A minimum-degree vertex p of J gives A=N_J(p), B=V(G) minus N_J[p], and F=G[A]. Thus p is adjacent in G to every vertex of B and no vertex of A. For each edge uv of G[B], choose exactly one actual quasi-edge (u,i)->v, i in A, meaning

    N_J(u) union N_J(i)=V(G) minus {v}.                 (3)

Selected A-B edges are these chosen representatives; all other existing A-B edges of J are residual. At u in B write its A-neighbourhood as the disjoint union S_u union R_u, with rho_u=|R_u|. At a label i let R_i,x_i be its residual and selected incidence counts, delta_i=deg_F(i), and s_i=max(0,delta_i-R_i).

The canonical bridge gives x_i>=s_i, source eligibility s_i<=rho_u at any selected i, forward and reverse selected containment, and

    N_F(i) subset R_u union R_v for (u,i)->v.           (4)

For an exact block T={i:s_i=d}, H={u:rho_u>=d}, |T|=|H|=d, every high vertex selects all T and no low vertex selects T. Put K=N_F(T) minus T. Each k in K is residual at every high vertex; if it is selected, both endpoints are low, so s_k<=d-2. Define full pools V_t={v outside H:R_v=T minus {t}}, p_t=|V_t|, V=union V_t, m=|V|, and O=B minus (H union V). Every p_t>=1. On an actual block the weights are w_k=d for s_k=0 and d-1 otherwise. The nonnegative defects are

    L=sum_K(w_k-|N_F(k) intersect T|),
    beta=sum_T[R_t-(m-p_t)], mu=binom(d,2)-e(F[T]).

The preceding exact capacity identity is W-d-(d-1)m=P+L+beta+2mu, P>=0. All these facts are proved in the preserved base and covering treatments; no sufficiency for graph realization is inferred.

## 2. The one-defect structure

Assume d=2 and L+beta+2mu=1. Every K-label has s_k=0 and weight two. Also beta=0 automatically: any low residual occurrence of a tight label fills that vertex's sole available residual slot and places it in a full pool. Therefore mu=0, L=1.

Write T={t,s}. Then ts is an edge of G. Exactly one label k in K has a single tight neighbour, say s; all other labels form a common class C, |C|=c, adjacent to both t and s in F. Put

    X=V_t, Y=V_s, Z=A minus (T union C union {k}).

The exact tight rows give |X|=c, |Y|=c-1, c>=2. Full-pool saturation gives all C-X and C-Y edges in G: a common label cannot be selected at a low vertex, and its residual label there is tight. The entire tight neighbourhoods are

    N_G(t)={s} union C union X union O,
    N_G(s)={t,k} union C union Y union O.                (5)

There are no other A-neighbours by the definition of K, no high neighbours because high vertices select T, and no further tight residual occurrences by beta=0.

## 3. Protecting ts determines the singleton completely

Deleting ts preserves its endpoint distance via C. A pair involving an exclusive pool neighbour in X or Y also retains a path through C. The only potentially damaged pair is {t,k}. Edge-criticality therefore forces

    N_G(t) intersect N_G(k)={s}.                        (6)

In particular k has no G-neighbour in C, X or O. Thus k is selected at each x in X, whose residual set is {s}. At every o in O it is residual: selection of k would require its F-neighbour s to be present in J at o, impossible outside the full pools. Hence R_o={k}.

At Y the label k is absent in J. It is not residual there (the residual label is t), and selection again would require s present. It is present in J throughout H, X and O. Therefore each selected (x,k) has destination f(x) in Y. Equation (4) implies N_F(k) subset {s,t}; as kt is not an F-edge, N_F(k)={s}. In particular

    N_G(k)={s} union Y,
    N_G(x) intersect Y={f(x)}.                         (7)

The second equality is also immediate from (3): x and k have exactly one common G-neighbour, namely f(x). The map f:X->Y need not be injective.

For y=f(x), forward containment gives S_x minus {k} subset {t} union S_y. No low vertex selects t, so this is contained in S_y. Reverse containment gives S_y subset {s} union S_x; no low vertex selects s and k is absent at y. Consequently

    S_x={k} disjoint-union S_y.                        (8)

Both selected sets, apart from k at x, lie in Z. Thus for every z in Z,

    xz in E(G) if and only if yz in E(G).              (9)

## 4. The common class also becomes saturated

A common label q in C is never selected. At a low source, selection would require both tight labels residually, impossible with rho<=1; at H it is residual. Its only residual occurrences are the two high vertices: X and Y have tight residual labels, and every O-vertex has residual label k. Thus R_q=2 and x_q=0. From x_q>=s_q follows delta_q<=R_q=2. Its two tight neighbours already meet this bound. Therefore

    N_F(q)={t,s},
    N_G(q)={t,s} union X union Y union O.              (10)

In particular no common label has an additional F-neighbour in C or Z. This step uses the minimum-pivot degree/demand inequality and the full residual partition; it cannot be obtained from the earlier local private-witness control alone.

## 5. An elementary twin-containment obstruction

**Lemma.** Let G have diameter two. Suppose distinct vertices q and q' have identical open neighbourhoods, and a vertex k has

    N_G(k) proper-subset N_G(q)=N_G(q').                 (11)

Then, for any x in N_G(q) minus N_G(k), the edge qx is redundant: deleting it preserves diameter two.

**Proof.** The inclusion implies k is not adjacent to q or q': otherwise q would belong to its own open neighbourhood. Identical open neighbourhoods likewise imply q and q' are nonadjacent. Consider paths that might be lost when qx is deleted.

Any two-step path x-q-w is replaced by x-q'-w. For the other endpoint, any direct q-w edge except qx survives. If w is nonadjacent to q, then w is also nonadjacent to k by inclusion. When w is different from k, diameter two supplies a common neighbour z of k and w. This z lies in N_G(q) and is not x, so q-z-w survives. When w=k, choose any z in the nonempty N_G(k); again q-z-k survives. Finally, k and x are nonadjacent, so the same diameter-two argument gives z in N_G(k) intersect N_G(x), and q-z-x preserves the deleted edge's endpoint distance.

No pair with neither endpoint q nor x can have a destroyed path of length at most two using qx. The cases are exhaustive. This is an elementary path argument; no claim of literature novelty is made for the lemma.

**Application.** Since c>=2, choose distinct common labels q,q' in C. Equation (10) makes them full false twins, not merely vertices with matching A-neighbourhoods. Equations (7) and (10) give

    N_G(k)={s} union Y
      proper-subset {t,s} union X union Y union O=N_G(q).

Every x in X belongs to the difference. The lemma therefore makes every C-X edge separately redundant, contradicting original edge-criticality. No simultaneous deletion assertion is made.

Thus intrinsic defect one is impossible for d=2. Together with the preserved zero-defect and d>=3 theorems this proves (1)-(2).

### The initially preserved direct proof is consistent but longer

The symbolic checkpoint also gives a complete direct affected-pair partition: the endpoints use t; exclusive neighbours of q use f(x) or the pivot; exclusive neighbours of x use t, f(x), or a high vertex's actual s-destination. That proof uses (8)-(9). The twin-containment lemma removes these extra dependencies from the deletion step. In particular, matching Z-neighbourhoods and a duplicate fibre of f are not needed once (7), (10) and diameter two are established. Those true normal-form consequences remain preserved rather than being silently discarded.

## 6. Audit boundaries and abandoned shortcut

The initial normal-form attack considered two distinct sources in a fibre of f, whose existence follows from |X|=|Y|+1. Identical selected sets give identical A-neighbourhoods but do not establish equality of entire B-neighbourhoods. No full-twin or injectivity assertion is used. The successful proof instead saturates the common labels and deletes C-X, leaving ts itself protected by the singleton.

The theorem is conditional on the stated actual canonical graph construction and its reviewed bridge. Local completions used in checks are not certified diameter-two edge-critical graphs. No new graph order, canonical catalogue exclusion, independent acceptance or novelty claim follows from these tests.

## 7. Executed verification and precise coverage

Python bitset reachability and independently structured C++ explicit-path enumeration agree on **6,204 complete per-graph records**, checking **18,485 predicted redundant deletions** on graphs of diameter two. Both implementations are by the same assistant, not independent external reviewers.

The generic-lemma search examined every labelled simple graph through six vertices: 33,867 graphs, of which 11,324 have diameter at most two. It retained 1,710 graphs satisfying the twin-containment premises, representing 5,160 ordered witnesses and 4,080 distinct tested edges. This is an exhaustive small-graph check of the elementary lemma, not a census of canonical tight-block systems.

There are 4,400 local completions (4,160 exhaustive small completions and 240 seeded larger ones). Of these, 2,132 have diameter two and exercise 11,021 predicted redundant edges. The remaining non-diameter-two records are compared between implementations but are not counted as successful applications of the lemma. Selected-set equality is not imposed in these relaxed local graphs. There are 436 source instances violating the stronger Z-neighbourhood equality while the diameter-two deletion conclusion still holds, consistent with its removal as a dependency of the final lemma.

The strongest application controls are **90 complete, explicitly represented, noncritical diameter-two graphs**, for c=2 through 9. Both implementations verify the maximum-degree pivot, every G[B] edge's single quasi-edge representative, all residual sets and exact demand levels, and intrinsic defect one. Python checks unique common G-neighbours; C++ checks complement open-neighbour unions directly. All 1,053 representatives validate. Forty-two controls have a genuinely selected extra label at a Y-vertex, so the representative tests are not limited to empty selected receiver sets.

Each control's tight edge ts really is critical: deletion loses exactly the pair {t,k}. Nevertheless every C-X edge is redundant, totaling 3,384 such tested edges. These graphs are **not** edge-critical graphs or conjecture counterexamples. They demonstrate that the previous local private witness can persist even when full B-representation and minimum-pivot conditions hold; using all-edge criticality, not merely the old representative relaxation, is essential.

Four negative controls produce a destructive designated deletion when the false-twin requirement, diameter-two premise, strict containment, or common-label saturation is omitted. The diameter-three control is explicitly not presented as a diameter-two example.

The sources, complete graph records, exact input and decision streams, deterministic generator and replay command are included. Run `python3 check_d2.py --replay-only` to verify stored graph records, or omit the flag to regenerate them. The SHA256 input/decision digests in CHECK_SUMMARY.json agree between both implementations. No old-pipeline replay, catalogue count, promotion, independent acceptance or graph-realization claim is inferred.

## Sources and continuation

The predecessor treatments are the recovered interface proof at 4cb18222e4c0f56c2a5278f424c8414a09c469f7:CURRENT_STATE.md, the zero-defect package at 54f974fcff8acd85870deacc931da15ec4b11069, and the critical-edge covering package at cf718afcba303618f2231b95d452b9af5671c8d8. The full private-witness reduction is preserved at 81067c78adc18c1bb4c3792c289d168af20f0540:CURRENT_STATE.md. Classical complement/quasi-edge background: Tao Wang, Ping Wang and Qinglin Yu, On Murty-Simon Conjecture II, arXiv:1301.0460 (2013), https://arxiv.org/abs/1301.0460. That paper is not asserted to contain this argument.

The next mathematical target is incomplete F[T], starting with one missing tight edge. Quantify the new short-path witnesses rather than transplanting the clique-defect bound. Configurations without an exact block remain a separate coverage obligation.
