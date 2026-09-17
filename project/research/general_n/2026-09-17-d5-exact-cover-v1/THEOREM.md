# Five-label exact support cover forces defect at least eleven

**17 September 2026. Internal candidate theorem; external review and novelty open.**
Research directed by Paul Lenz. Derivation and implementations by ChatGPT/Geeps.

## Statement and scope

Retain the actual selected-representative system and whole exact block from the preceding structural theorem:

    |T|=|H|=d=5,
    Q=G[T],
    K=N_{G[A]}(T)\T,
    D=L+beta+2mu,

where mu is the number of missing edges of Q, L is the total K-support loss and beta counts residual tight incidences outside the full receiver pools. The preceding pair-coverage theorem proves that whenever D<15, every tight pair has a common K-neighbour and every critical tight edge lies in the union of the support-threat sets B_Q(S_x) for x in K union O.

Then every actual five-label exact block satisfies

    D >= 11.

Consequently the inherited scalar capacity obeys

    W >= 5+4m+11 >= 36,

and if there is an extra high-source selection, m>=10 and hence

    W >= 56.

This remains an exact-block theorem. It does not prove that every extremal graph has such a block, does not promote any catalogue exclusion, and does not establish attainability or sharpness of D=11.

## 1. Replace each exceptional vertex by a weighted support

For S subseteq T, the already-proved threat set is

    B_Q(S)={ts in E(Q): s in S, t notin S,
                         N_Q(t) intersect S={s}}.

Criticality plus pair coverage implies

    E(Q) subseteq union_{x in K union O} B_Q(S_x).       (1)

Full receiver-pool vertices are protected by common pair-neighbours and therefore are not charged as arbitrary exceptions.

For a K-label k, write S_k=N_G(k) intersect T and l_k=w_k-|S_k|. At d=5, w_k is 5 at zero demand and 4 at positive demand. Hence every K-label pays at least

    c(S_k)=max(0,4-|S_k|)                               (2)

units of L. Indeed at positive demand equality holds; at zero demand the actual loss is one larger unless |S_k|=5.

For x in O, its defect contribution is q_x=5-|S_x|, because its missing tight G-neighbours are precisely residual tight incidences counted in beta. Thus

    q_x >= c(S_x).                                      (3)

Let tau(Q) be the minimum total c-cost of any multiset of nonempty supports S whose B_Q(S) cover all edges of Q. Equations (1)--(3) give

    L+beta >= tau(Q),
    D >= 2mu+tau(Q).                                    (4)

This is a genuine lower bound: tau deliberately gives every exception the cheaper K-price, so O-vertices cannot invalidate it.

## 2. The ten-edge auxiliary problem is finite and exact

There are only ten possible tight edges on five labelled vertices and therefore 2^10=1024 labelled graphs Q. For each Q, there are only 31 nonempty supports S subseteq T.

The published verifier forms the exact bit mask B_Q(S) for every support and solves the weighted union-cover problem by dynamic programming over subsets of E(Q). No graph realization, floating-point optimization, random search or heuristic pruning is involved.

The complete result is:

| missing tight edges mu | minimum tau(Q) among such Q |
|---:|---:|
| 0 | 12 |
| 1 | 9 |
| 2 | 7 |
| 3 | 6 |
| 4 | 4 |
| 5 | 2 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |

Therefore

    min_Q [2mu+tau(Q)] = 11.                            (5)

The minimum is attained only by two labelled degree types in this auxiliary problem:

- mu=1, tau=9, degree sequence (3,3,4,4,4): 10 labelled Q;
- mu=2, tau=7, degree sequence (3,3,3,3,4): 15 labelled Q.

These are auxiliary tight graphs, not claimed realizations of the original exact block.

## 3. Deduction for the original graph

Suppose for contradiction that an actual d=5 exact block had D<=10. Since D<15, the preceding pair-coverage theorem applies, and hence so does the critical support cover (1). Equation (4) and the exact auxiliary minimum (5) then give

    D >= 11,

contradiction. Thus every actual five-label exact block has D>=11.

The capacity conclusions follow from the inherited identity W>=5+4m+D, with m>=5, and m>=10 if extras occur.

## 4. Reproducibility and trust boundary

`check_d5_cover.py` and `check_d5_cover.cpp` independently enumerate all 1024 labelled Q, all 31 nonempty supports, and the exact weighted set-cover dynamic programme. Their complete 1024-row outputs agree byte-for-byte. The row stream SHA256 is

    80aa3a20b985dab08080c5d645bdf44cadb9498ec3be636219a670e35e4943c9.

The exact histogram and the two minimum degree types are pinned in `CHECK_SUMMARY.json`.

Both programs and the proof were written by the same assistant, so this is strong internal reproducibility evidence rather than independent external review. The finite computation concerns only the five-vertex auxiliary support-cover lemma; the graph-to-interface bridge, pair coverage and necessity of the threat cover remain hand arguments and should be reviewed directly.

## 5. Next structural target

The immediate equality frontier is now D=11. The auxiliary minimizers show exactly where to look: Q=K5 minus one edge, or Q with two missing edges forming a matching (degree sequence 3,3,3,3,4). The next proof unit should impose the **actual exact-row identities, support multiplicities, demand types and receiver-pool incidences** on those two auxiliary families. A cheap set cover is only necessary, not sufficient for original-graph realization.

Separately, exact-block coverage remains the principal gap between this scoped theory and an unrestricted Murty-Simon result.
