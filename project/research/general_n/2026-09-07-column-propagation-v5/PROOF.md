# General-order column propagation and supplement activation — v5

7 September 2026. Directed by Paul Lenz; mathematical development, implementations and internal checks by ChatGPT/Geeps.

**Candidate mathematical derivations; exact finite arithmetic reproduced; independent mathematical review OPEN.** No complete order 28, full general conjecture, improved uniform degree coefficient, novelty, priority, formal verification or theorem-ledger promotion is claimed.

## 1. Scope and inherited dependencies

The repository baseline read in this session was `a2d973920979ad480c66d617304bf038b791b98a` of `paullenz/MurtySimon25`. The v4 checkpoint is preserved by its parent commit `a96711534b47e12c597d826dcf23896cf396f9e6`. The actual uploaded original v4 ZIP has SHA-256 `3944e786fb0ea5322ae3e18dd177ef8b01046d903076a4ca61caf89fdc5ae184`; its bytes were checked and extracted here.

The finite input is exactly the v4 list of 13,196 `(s,rho)` rows in 1,119 demand patterns for `(n,b,m)=(28,15,196)`. This turn does not independently re-enumerate the upstream 17,669,896 v4 rows or the full earlier n=25/n=27 proofs. The copied input files are hash-pinned. The v3 overlapping degree-case exclusions are not new results of v5.

The new work retains individual possible degree/residual-column pairs, couples them to one source row at a time, and prices the extra outgoing selections forced at supplements. These are necessary-condition projections, not a simultaneous full-graph realization.

The graph framework uses the published complement correspondence [1] and the project's residual/quasi-edge injections [2–4]. Those universal mathematical premises remain review obligations; numerical replay does not prove them.

## 2. Notation and inherited facts

For a non-bipartite diameter-two edge-critical graph G, excluding stars, let H be its complement. Choose a minimum-degree vertex v in H and set

    A=N_H(v), B=V(H)\N_H[v], a=|A|, b=|B|=Delta(G), n=a+b+1.

Let F be the complement of H[A], and d_i the degree of label i in F. For each missing unordered B-pair choose exactly one cross quasi-edge `ui -> w`: ui is an H-edge, and its endpoints totally dominate every vertex except the unique supplement w. Orient the missing pair from u to w. Different missing pairs use different selected cross-edges, and at one source their labels and supplements are distinct. Every other existing A–B edge is residual.

Write rho_u and R_i for residual row and column degrees, r=sum rho=sum R, q_u and p_u for outgoing and incoming selected-pair degrees, and x_i for selected incidences at label i. Put

    Q=sum q=sum p=sum x,
    t=m-b(n-b), ell=b-a-1=2b-n,
    s_i=max(0,d_i-R_i), S=sum s_i.

The inherited identities and inequalities are

    sum d_i=2(r+t), x_i>=s_i,
    selected ui->w implies
        d_i<=rho_u+R_i,
        d_i<=rho_u+rho_w,
        d_i<=rho_u+q_u-1,
        rho_w+q_w>=q_u-1,
    q_u+rho_u<=a,
    p_u<=rho_u+ell.                                      (2.1)

For the last inequality, the H-degree of u is `b-1+rho_u-p_u`, at least a. Therefore

    Q<=r+ell*b.                                           (2.2)

A chosen set of exactly s_i actual selected incidences at every label has S arcs. Such a subset exists because x_i>=s_i; it is not an assertion that x_i=s_i. Zero-demand labels can still have actual selected edges. They remain available to all source-capacity and row-status tests.

## 3. Forced labels and column domains

The first selected-edge inequality implies that a label of positive demand s_i can only be selected at sources with rho_u>=s_i. More restrictive source sets can be inferred from the other necessary bounds.

For any safely computed superset E_i of all possible selected sources of i, `|E_i|<s_i` is impossible. If `|E_i|=s_i>0`, every vertex of E_i must select i. In particular, none of those vertices can be i's supplement, because a supplement must miss i in H. This is a shared-adjacency restriction, not merely a degree-sum comparison.

The finite projection begins with all `(d_i,R_i)` satisfying the specified demand, degree bound, residual sum and degree sum. For s_i>0, R_i=d_i-s_i. For s_i=0, R_i>=d_i. Introduce

    z_i=R_i+s_i-d_i>=0,
    Z=sum z_i=S-r-2t.                                    (3.1)

Positive-demand labels have z_i=0. A compatible collection of columns must satisfy the two exact sums `sum R_i=r` and `sum z_i=Z`. Multichoice generating products eliminate an individual option only when it appears in no collection satisfying both sums. Thus an R-column is not sorted independently from its demand label.

The n=28 computation has a=12, b=15, t=1. The inherited low-k argument rules out a vertex of H[A]-degree zero: its bound would require `15<=65-choose(11,2)=10`. Therefore every F-degree is at most 10. This dimension-specific bound is an inherited candidate input, not a new v5 theorem.

Source capacities are refined using matching of distinct labels to distinct supplements. Every already forced label must be covered by that matching. Each step uses previously proved upper caps, and it retains a source's actual selected degree whenever an actual graph exists. Subset source and unordered-pair budgets are also checked. The source matching calculation allows extra selections, including selections on zero-demand labels.

## 4. A missing-neighbour restriction

**Lemma.** If source u has q_u selected labels and j in A is not adjacent to u in H, then

    d_j<=a-q_u-1.                                        (4.1)

**Proof.** Each of the q_u selected quasi-edges at u has its exception in B. Hence it must dominate j. Since uj is absent, j is adjacent in H[A] to every selected label at u. These are q_u distinct vertices, none equal to j. Thus j has at least q_u H[A]-neighbours and at most a-1-q_u F-neighbours. This also covers q_u=0.

This lemma allows one B-row to be coupled to all individual column choices and their global sums. Fix a trial q for source u. Each A-label must have exactly one of three statuses:

* selected at u;
* residual at u;
* not adjacent to u in H.

There are exactly q selected labels, rho_u residual labels, and a-q-rho_u missing labels. A selected label must satisfy all safe source eligibility and supplement restrictions, including `d_i<=rho_u+q-1`; it consumes no residual ui edge. A residual label requires R_i>=1 and cannot already be forced selected at u. A missing label satisfies (4.1), cannot be forced selected at u, and has `R_i+s_i<=b-1` because its total B-neighbourhood is at most b-1. Selected status requires `R_i+max(1,s_i)<=b`.

A dynamic program asks whether all these statuses and column choices can meet, simultaneously, the exact selected count q, residual count rho_u, column-residual sum r and slack sum Z. If not, q is excluded. An individual column option is removed only if, for at least one B-row, it appears in no such solution at any remaining q.

Each graph gives a feasible witness to every row projection. Pruning and repeating is therefore safe by induction. Different rows may still be witnessed by different full column assignments. Consequently a surviving fixed point is **not** a proof of jointly consistent columns, let alone a graph.

The discovery dynamic program stores residual sums as bits in separate slack layers. The separately written checker packs both sums into a generating polynomial. Both implement the recurrence just proved. Their agreement is implementation cross-checking by the same assistant, not independent mathematical authorship. The compiled implementations explicitly restrict their input dimensions and r<63; an unsupported input raises an error, not an infeasibility conclusion. The mathematical lemma has no such finite-order restriction.

## 5. General supplement-activation charging

Let l_u be any proved lower bound on q_u, and P_w any nonnegative upper bound on p_w. For example, forced incidences imply l_u>=f_u; source-capacity totals give `l_u>=S-sum_{v!=u}c_v`; a forced selected label gives `l_u>=d_i-rho_u+1`. Upper incoming caps follow from (2.1) and safe possible-source support.

For every selected arc u->w, the supplement inequality gives

    q_w-l_w >= (l_u-1-rho_w-l_w)_+.

Take any subset T of actual selected arcs. There are at most P_w arcs of T entering w. If any enter w then P_w>0. Each of their nonnegative costs is at most q_w-l_w, so averaging over the incoming capacity gives

    sum_{(u,w) in T} (l_u-1-rho_w-l_w)_+ / P_w
        <=sum_w(q_w-l_w)=Q-sum_w l_w.                    (5.1)

Terms with P_w=0 cannot occur. More explicitly, at a fixed w, at most P_w summands each bounded by q_w-l_w are divided by P_w. This avoids counting the same required increase in q_w as a separate new increase for every incoming arc.

If Q<=U is a proved upper bound, every chosen required-incidence subset T must therefore fit the budget `U-sum l`. This accounts for the fact that supplying a supplement may itself force additional outgoing selected edges. The operation is not an assumption that a supplement is free once its incoming capacity is available.

## 6. Exact network certificates

Choose exactly s_i actual selected incidences per label. A relaxation of their possible placement is represented by a directed capacitated network:

    source -> label i -> source-label (i,u)
           -> ordered-pair (u,w) -> supplement w -> sink.

The first capacity is s_i, source-label capacity is one, ordered-pair capacity is one, and incoming capacity is P_w. The domain includes only triples allowed by the safe column and source bounds; in particular a forced source for label i cannot be its supplement. The cost on a triple is the summand of (5.1), scaled by the common denominator of all positive P_w.

This network intentionally relaxes some constraints. It does not enforce one global capacity on opposite orientations of an unordered pair, and it does not enforce every actual outgoing-source total within the network. Separate safe total upper bounds remain in U. Relaxing these constraints cannot create a false rejection: every actual required subset still maps to a flow of value S with cost at most the scaled budget.

A cut of capacity below S is a rejection certificate. For a cost certificate, let C_e be each edge capacity, c_e its integer cost, and pi an arbitrary integer potential on network vertices. Every S-flow has cost at least

    S(pi_sink-pi_source)
      -sum_{e=(u,v)} C_e max(0,pi_v-pi_u-c_e).            (6.1)

To prove this, apply `c_e x_e >= (pi_v-pi_u)x_e - C_e(pi_v-pi_u-c_e)_+` to every edge and sum. Flow conservation cancels the interior potentials. A strict excess of (6.1) over the scaled budget is an exact contradiction.

Discovery uses an integer minimum-cost flow implementation. Acceptance uses (6.1), not a solver status. The separate checker rebuilds the graph by named resources, recomputes the lower and upper degree bounds, and evaluates the integer formula. It imports neither the discovery network builder nor its flow solver.

## 7. A solver-free forced-block corollary

Suppose p labels are each forced to be selected at all z vertices of a source set Z. None of those z vertices can supplement any of those p labels. The pz mandatory arcs must therefore go to B\Z.

Suppose every vertex outside Z has residual degree at most c. By (2.1), each can receive at most c+ell arcs. If c+ell<=0, no mandatory arc is possible. Otherwise at least

    ceil(pz/(c+ell))

outside vertices must be used as supplements. Each such vertex has q_w>=p-1-c, since every source in Z has at least p selected labels. Hence

    Q >= pz + ceil(pz/(c+ell)) (p-1-c)_+.                (7.1)

Together with (2.2), this is a scalar obstruction. It is also impossible when the required number of outside vertices exceeds |B\Z|.

A directly identifiable block has demand h on p labels and exactly h residual rows of degree at least h. Those labels are forced at those h sources, so z=h. The general minimum-cost bound deals with overlapping or nonuniform forced structures; the block argument often supplies a shorter explanation.

### The first retained order-28 row

Its demands are `(0,0,0,0,1,4,4,4,4,4,4,4)`, and its residual rows are eleven 1s followed by four 4s. Thus r=27 and ell=2. Seven demand-four labels must all be selected at the four rho=4 sources. Their 28 mandatory arcs must end among the eleven rho=1 vertices.

Each of those vertices can receive at most three arcs, so at least ten are used. Each used vertex must make at least `7-1-1=5` outgoing selections. Therefore

    Q>=28+10*5=78,
    Q<=27+2*15=57.

This is a contradiction. It excludes **every individual-column refinement of the row**. The 47 saved direct block certificates overlap the main network/joint exclusions and are not added to their totals.

## 8. An infinite family of whole demand-row exclusions

For every integer p>=10, consider

    a=2p, b=2p+3, n=4p+4,
    m=(2p+2)^2+1, t=2, ell=2,
    rho=(1 repeated 2p+1 times, 2,2),
    s=(0, 1 repeated p-1 times, 2 repeated p times).

Here r=2p+5, S=3p-1, and the zero-demand slack is `S-r-2t=p-10>=0`. The p demand-two labels are all forced at the two rho=2 sources. Their 2p mandatory arcs use rho=1 supplements. Applying (7.1) and then weakening the ceiling downward gives

    Q>=2p+(p-2)ceil(2p/3)>=2p(p+1)/3.

But (2.2) gives Q<=6p+11. The difference is positive because

    2p(p+1)/3-(6p+11)=(2p^2-16p-33)/3>0.

The numerator equals 7 at p=10 and increases by 4p-14 when p is increased by one. Thus **every compatible (d,R) refinement of every row in this infinite family is excluded**. This is not a completed theorem for all graphs at the displayed orders. Its first orders are 44,48,52,...; the proposed dense edge count is one above the balanced complete-bipartite target. No such graph is constructed.

These rows are not ruled out merely by an inconsistent scalar ledger. One explicit column choice has k=min(15,p-1),

    d=(max(0,16-p), 2 repeated k, 1 repeated p-1-k, 3 repeated p),
    R=(max(6,p-10), 1 repeated k, 0 repeated p-1-k, 1 repeated p).

It has the stated demands, sum R=2p+5 and sum d=4p+14. The F-degree sequence and residual bipartite sequence are separately graphical. For p>=16, construct F by a cycle on the p high labels and the fifteen degree-two low labels, add a matching on sixteen high labels, attach the remaining degree-one low labels to the remaining high labels, and leave the zero label isolated. The six p=10,...,15 bases have explicit checked edge lists. The residual construction is also supplied in the test program.

These separate realizations do **not** assert that the selected, residual and F-adjacencies can coexist in a graph G. Their purpose is to expose that the new contradiction addresses shared selection requirements, not just an impossible degree sum.

## 9. Complete executed finite scope

All 13,196 input rows are processed, with exactly the following disposition:

| Stage | Rows rejected at that stage | Rows left |
|---|---:|---:|
| v4 retained input | — | 13,196 |
| Joint column-domain, matching and one-row adjacency projection | 5,471 | 7,725 |
| Exact activation-cost certificates | 663 | — |
| Exact activation-network cut certificates | 144 | 6,918 |

The final 6,918 rows belong to 830 demand patterns. Their retained individual option domains, safe caps and forced labels are saved explicitly in `evidence/FINAL_SURVIVORS.json`. These are OPEN numerical relaxations, not actual graphs.

The separately written checker replays every input disposition and reconstructs every surviving domain, cap and forced set. The activation checker recomputes all 807 integer certificates and verifies that rejected rows and final survivors partition the 7,725 intermediate rows. The direct block checker verifies 47 overlapping explanations. See the exact JSON reports for the executed checks.

A preliminary propagation-only pass and a preliminary activation pass are preserved as exploratory predecessors. Their totals are not additional exclusions. A diagnostic count of symmetric formal column combinations is also preserved; it is not an enumeration of actual graphs or a completed rejection search over those combinations.

**Edge-count boundary:** this computation is at m=196 only. With s and rho fixed, changing t changes the exact slack (3.1); a row omitted at m=196 could matter at another edge count. No monotonicity for these new tests is assumed. The m>=197 coverage obligation therefore remains OPEN.

## 10. Verification limits and next work

The general arguments in Sections 4–8 are candidate mathematical proofs. Tests cannot establish their universal validity. The 400 tiny joint-projection tests compare masks and option support with brute-force enumeration. Two thousand abstract activation systems include 1,553 positive-cost tests. They satisfy the tested activation premises but are not critical graphs or full density-ledger realizations.

The actual-graph replay rechecks 916 saved selections on 639 distinct labelled critical graphs, including 3,666 missing-neighbour inequalities and 584 with a nonzero selected source degree. All 884 instances within the compiled projection domain preserve their actual singleton columns and source degrees. The other 32 are outside that implementation's declared range; the direct lemma tests still include them. There are no positive-surplus actual examples and no positive activation-cost examples in this particular actual-graph sample. The latter limitation is explicitly distinct from the nonvacuous abstract tests.

A negative control shows why incoming-capacity normalization cannot be omitted: the unnormalized proposed charge is 12 while only 3 units of extra outgoing degree exist. Zeroed cost potentials and malformed flow cuts are rejected. The saved actual examples include selected zero-demand labels, reinforcing why the model must allow their extra incidences.

The next refinement is to require **one common full column assignment across multiple source rows**, then use the v4 individual-label tail bounds and shared F-neighbourhood constraints on the remaining joint possibilities. This v5 pass does not claim to have run the v4 tail separator over every fully specified remaining column. A full order-28 conclusion additionally needs above-target edge-count coverage and all earlier degree/equality dependencies assembled and reviewed.

## References and attribution

[1] T. W. Haynes, M. A. Henning, L. C. van der Merwe and A. Yeo, *A maximum degree theorem for diameter-2-critical graphs*, Central European Journal of Mathematics 12 (2014), 1882–1889, DOI 10.2478/s11533-014-0449-3. Published complement correspondence is an input. Author repository: https://dc.etsu.edu/etsu-works/15862/ . Its full original proof was not re-audited in this turn.

[2] Project n=27 candidate, `project/reviews/n27/2026-09-07-candidate-v1/PROOF.md`, particularly the residual and quasi-edge framework. Earlier versions remain unchanged.

[3] Project general-order pair-budgets-v2 and coupled-resource-v2, source of the incoming capacity, supplement degree and residual inequalities.

[4] Project demand-support-v3 and label-tail-v4, source of the demand/slack identities, finite input rows and inherited low-k bound. The copied dependencies are explicitly hash-pinned in PROVENANCE.json.

[5] A. Dailly, F. Foucaud and A. Hansberg, *Strengthening the Murty–Simon conjecture on diameter 2 critical graphs*, Discrete Mathematics 342 (2019), 3142–3159, https://arxiv.org/abs/1812.08420 . Dependency of the earlier low-degree frontier, not needed for the new fixed-row activation contradiction.

“New” means newly developed in this project continuation, not a verified literature-priority claim. Paul Lenz directed the work. ChatGPT/Geeps developed the mathematics, programs and internal checks. The frozen n=25/n=27 candidates, their external-review status, and the governed theorem ledger are not changed.
