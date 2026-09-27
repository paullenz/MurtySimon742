# Canonical stratified Hall closure under weaker crossing hypotheses

27 September 2026. **New internal candidate results, with hand proofs and executed finite checks. Not external review, a novelty claim, or a full Murty–Simon proof.**

This continuation starts from `ABSTRACT_CROSSING_DOMINANCE.md` (Git blob `03c3fd9fda0d507440b1fcfa8510a322291a201d`) and `MANUSCRIPT.md` (blob `d745e07ee8ee47b66d16d6aa538673b11ed1f1a4`). It reconstructs the original argument, weakens its assumptions, and answers the manuscript's canonical-witness question.

## 1. Model and exact statements

Let V be finite, with a partition into blocks B_i. Each vertex u is both a source with demand d_u and a receiver with capacity P_u. All demands and capacities are nonnegative integers. R is a loopless directed relation; every compatible source–receiver arc has unit capacity.

For S subseteq V set

    y_w(S) = |{u in S : u R w}|,
    H(S) = sum_w min(P_w, y_w(S)),
    D(S) = sum_{u in S} d_u,       F(S) = H(S) - D(S).

Write alpha_(i,k)=|{w in B_i:P_w>=k}| and beta_(i,k)(S)=|{w in B_i:y_w(S)>=k}|, and put

    U(S) = sum_i sum_{k>=1} min(alpha_(i,k), beta_(i,k)(S)),
    G(S) = U(S) - D(S).

Equivalently, within each block sort P and y in the same order and sum the coordinatewise minima. Layer-cake expansion proves this equivalence and H<=U.

For every same-block pair x,y with P_x<P_y assume:

1. **Incoming nesting:** z R x implies z R y for every third vertex z.
2. **Outgoing nesting:** x R z implies y R z for every third vertex z.
3. **Pair implication:** y R x implies x R y. Both arcs are NOT required to exist in advance.
4. **Antitone demand:** d_x>=d_y.

Call conditions 1–3 weak crossing dominance (WCD), as local terminology for this note only. Equal-capacity pairs have no imposed demand order or neighbourhood order.

**Theorem A — weakened minimum exactness.** Under these assumptions,

    min_S G(S) = min_S F(S) = gamma.

The original TCD theorem is a special case: mutual compatibility implies condition 3, and equal block demands imply condition 4.

**Theorem B — canonical optimum.** Let M+ be the greatest minimizer of F. Start at M+ and repeatedly delete the selected high-capacity endpoint of any positive rearrangement crossing. Every choice sequence terminates at the SAME set C. This C is the greatest member, under inclusion, of

    T = {S : F(S)=gamma and U(S)=H(S)} = argmin G.

The family T is closed under unions, but need not be closed under intersections. G need not be submodular.

These are existence/structure and witness-extraction statements. They do not assert gamma>=0 in every D2C application.

## 2. Crossing orientation under the weaker pair assumption

If U(S)>H(S), a threshold in some block supplies x,y,m with

    P_x < m <= P_y,       y_x(S) >= m > y_y(S).

Let a_x,a_y count incoming arcs from S excluding x and y. Incoming nesting gives a_x<=a_y. Because R is loopless,

    y_x(S) = a_x + 1_(y in S) 1_(y R x),
    y_y(S) = a_y + 1_(x in S) 1_(x R y).

A positive difference forces y in S, y R x, a_x=a_y and the second indicator product to vanish. The pair implication gives x R y, hence x notin S. Consequently

    y_x(S)=m,       y_y(S)=m-1<P_y.

Thus an actual crossing forces mutual compatibility even though WCD did not require it for every capacity-ordered pair.

## 3. Submodularity and the neutral-deletion chain

Each min(P_w,y_w(S)) is a concave, nondecreasing function of a modular count, hence is submodular. D is modular, so F is submodular. Its minimizers are closed under union and intersection, and M+ is their union.

If S is a minimizer and x notin M+, then S+x is not a minimizer. Integrality gives F(S+x)>=gamma+1.

Suppose a crossing (x,y,m) at a minimizer S has x notin M+. Define

    A = |N+(x) intersect {w:y_w(S)<P_w}|,
    B = |N+(y) intersect {w:y_w(S)<=P_w}|.

These are the exact capped-capacity gain from adding x and loss from deleting y. Therefore

    A >= d_x+1,       B <= d_y.

The crossing receiver y belongs to the first set. Every other target in that set belongs to the second by outgoing nesting. Hence A-1<=B. Antitone demands now give the complete squeeze

    d_x+1 <= A <= B+1 <= d_y+1 <= d_x+1.

Every inequality is equality. In particular d_x=d_y and B=d_y, so F(S-y)=gamma. A strict demand drop d_x>d_y rules out this kind of crossing altogether.

Start with S=M+. A low crossing endpoint is outside S. After a high endpoint y is deleted, its receiver count is below P_y; later deletions can only reduce that count. It can never become a low endpoint, which would require a count strictly above its own capacity. Thus every later low endpoint remains outside the ORIGINAL M+. The squeeze applies at every step. Each step removes a vertex, so after at most |V| steps the process reaches a minimum with U=H. This proves Theorem A.

**Important audit point:** the reference set is the fixed original M+, not a newly recomputed maximal minimizer. Strict slack after deletion is what licenses subsequent steps.

## 4. Persistence lemma — the new load-bearing step

**Lemma.** Suppose (x,y) is a crossing at a minimum S for which deletion of y is neutral. Let T subseteq S be any exact minimum containing y. Then (x,y) remains a positive crossing at T, possibly at a smaller threshold.

**Proof.** Both S-y and T minimize F. Their intersection T-y also minimizes F. Thus deleting y has the same capped-capacity loss d_y at both S and T:

    sum_(w in N+(y)) 1_(y_w(S)<=P_w)
      = d_y
      = sum_(w in N+(y)) 1_(y_w(T)<=P_w).

For each target in this sum its indicator can only increase when S shrinks to T. Equality of the sums therefore forces equality term by term. The target x is in N+(y), and at S it has y_x(S)>P_x. Its indicator is zero and remains zero at T. Hence y_x(T)>P_x.

At the original crossing the third-source incoming counts a_x,a_y were equal. Incoming nesting holds for each third source individually. Equality of their sums over S means each selected third source contributes either to both x,y or to neither. This remains true on the subset T. As y remains selected and x remains absent,

    y_x(T)=y_y(T)+1.

Also y_y(T)<=y_y(S)<P_y. Setting m'=y_x(T) gives P_x<m'<=P_y and y_y(T)=m'-1. This is the required positive crossing. QED.

This proof uses nonnegative indicator differences, not an unjustified cancellation of arbitrary signed quantities.

## 5. Canonical terminal and union closure

Every exact minimum is contained in M+. Maintain the invariant that the current set S contains every tight exact minimum T in the family T of Section 1. Initially this is true.

If the next crossing deletion removes y, and some such T contained y, the persistence lemma would make T have a positive crossing. This contradicts its tightness. Thus no tight exact minimum contains the deleted y, and the invariant is preserved.

At termination the current set C is itself a tight exact minimum and contains all of them. It is consequently their unique greatest member. Every deletion order therefore has the same endpoint. Moreover, because H<=U and the two minimum values agree, a minimizer of G must have F=G=gamma; conversely every tight exact minimum minimizes G. This proves the canonical assertion without assuming G submodular.

**Union closure, with a separate argument.** Let A,B be tight exact minima, W=A union B and I=A intersect B. Both W,I minimize F, so equality holds in the submodular inequality for H. Since every receiver contributes a nonnegative submodularity gap, equality holds separately at every receiver.

Suppose W has a crossing (x,y). Write a=y_x(A), b=y_x(B), c=y_x(I), e=y_x(W), p=P_x; then a+b=c+e and e>p. Assume y in A. The incoming-count equality at the crossing propagates from W to A as above. Because y_y(A)<P_y and A is tight, a<=p.

If y also belongs to B, tightness similarly gives b<=p. The receiver-x submodularity gap is then e-p>0, a contradiction. If y notin B, the arc y R x gives a-c>=1. With a<=p<e, that receiver's gap is min(a-c,e-p)>0, again a contradiction. Thus W is tight. Finite unions give the greatest member directly as well.

## 6. Constructive extraction using one ordinary maximum flow

Build a network with separate left/source and right/receiver copies:

    s -> u_L       capacity d_u;
    u_L -> w_R     capacity 1 whenever u R w;
    w_R -> t       capacity P_w.

Fixing the left vertices on the source side to be S and choosing each receiver side optimally gives cut capacity

    D(V\S) + sum_w min(P_w,y_w(S)) = D(V)+F(S).

After computing any maximum flow, let Q be the vertices from which t is reachable along positive residual-capacity arcs. The complement of Q is the greatest source side of a minimum cut: any minimum-cut source side is residual-forward-closed and cannot contain a vertex reaching t; conversely this complement is forward-closed and excludes t. Its left projection is therefore M+.

Apply crossing deletion to that projection, WITHOUT further maximum-flow calls. This yields C after at most n deletions. A straightforward implementation can recompute counts and inspect same-block pairs at each step in polynomial time. No improvement over the asymptotic complexity of ordinary minimum cut is claimed.

The verifier separately checks flow feasibility, flow/cut equality, residual construction of M+, equality with the union of ALL brute-force minima, every reachable deletion choice, the unique terminal, and containment of every tight minimum.

Reference for standard residual-network conventions: NetworkX's official maximum-flow documentation, https://networkx.org/documentation/stable/_modules/networkx/algorithms/flow/maxflow.html . The canonical deletion proof above is supplied here rather than delegated to that documentation.

## 7. Hostile examples and precise limits

All examples are executed with exact arithmetic in `ADVERSARIAL_CHECKS.json`; vertex lists below are zero-indexed.

**Smallest pointwise failure.** Two vertices, one block, capacities (0,1), arcs 0->1 and 1->0, equal integer demand 1. S={1} has H=0 and U=1. Nevertheless both minima are -1, attained tightly by the full set. Thus arbitrary minimum F-witnesses need not be tight.

**Real demands fail already on two vertices.** Use the same relation and capacities, but both demands 1/2. The exact minimum is -1/2 and the rearranged minimum is 0. Integer-demand strictness cannot silently be replaced by strict positivity.

**Unordered integer demands fail on two vertices.** The same system with demands (0,1) has exact minimum -1 and rearranged minimum 0. The antitone condition is a genuine sufficient replacement for equal demand, not permission to drop demand restrictions altogether.

**Omitting the pair implication fails.** Capacities (0,1), demands (1,1), and only the arc 1->0 give exact minimum -2 but rearranged minimum -1. Incoming/outgoing nesting away from the diagonal is vacuous here.

**Incoming/outgoing hypotheses have explicit deletion counterexamples.** The evidence includes counterexamples both to omission from WCD and to omission from the original strict TCD, with all remaining listed conditions checked.

**G need not be submodular.** One block, capacities (0,0,2), demands (1,1,1), arcs 0->2, 1->2, 2->0, 2->1. For A={0,2}, B={1,2}, U(A)+U(B)=2 whereas U(A union B)+U(A intersect B)=3. Subtracting modular D preserves this violation.

**The tight-minimum family need not be an intersection lattice.** Blocks {0,1},{2}, capacities (0,2,0), all demands 1, arcs 0->1, 1->0, 2->1 satisfy TCD. Sets {0,1} and {1,2} are tight minima of value -1. Their intersection {1} remains an exact F-minimum but has H=0<U=1. Do not replace the proven union closure by full lattice closure.

**A nontrivial all-orders test.** Six independent bidirected pairs, capacities (0,1) and zero demands in each pair, plus an isolated vertex of demand 1 and capacity 0. M+ consists of the six high-capacity vertices and the isolated vertex. Its exact margin is -1 and its rearrangement gap is 6. All 64 reachable states and 192 deletion transitions were checked; the 6!=720 deletion orders all end at the isolated vertex. This is a test, not a proof by example.

Section 9 proves a natural real-capacity extension and a restricted real-demand extension. No weighted-arc or unrestricted-demand extension is asserted.

## 8. Verification and trust boundary

The checked-in original verifier had a one-shot iterator defect: demand generators were exhausted after the first capacity/digraph profile. Its actual output was 3 and 9 demand instances, not the frozen record's 39,636 and 172,080. The source blob was reproduced exactly before testing. Materialising demands repairs it; a coverage invariant now detects this class of omission.

The repaired original checker reproduced every historical numeric counter. The separately written bitset/sorted-pair/flow checker also reproduced the two original regimes and tested the canonical assertions. Additional exhaustive WCD/antitone regimes contain 9,252 three-vertex and 1,793,664 four-vertex demand instances. There are also 1,500 seeded structured directed examples of orders 5–9 and the 13-vertex all-orders example. Read `VERIFICATION.json` for final executed records and source hashes; finite checks are not the mathematical proof.

This is an additional same-programme audit, not a blinded or external independent derivation. Novelty remains unassessed. A preliminary official-journal check confirms the relevant threshold/Ferrers comparison paper exists (Marmulla and Brandes, 24 June 2026, DOI 10.7155/jgaa.v30i1.3099), but its full results have NOT been compared here. No equivalence with a named digraph class is claimed.

The Murty–Simon/D2C bridge obligations and the full general conjecture remain unchanged. The result gives an exact and now canonical Hall witness; it does not prove that all model instances have nonnegative Hall margin.


## 9. Real receiver capacities and a sharp rounded-demand condition

Here is a further generalization, with a complete adaptation rather than an appeal to continuity.

**Theorem C.** Receiver capacities P_u and source demands d_u may be arbitrary finite nonnegative real numbers. Keep WCD and replace the antitone-demand hypothesis by

    P_x < P_y in one block  implies  d_y <= floor(d_x).       (RD)

Define U by same-order sorted pairing, or equivalently by the CONTINUOUS layer-cake integral

    U(S) = sum_i integral_(t>0) min(|{w in B_i:P_w>=t}|,
                                   |{w in B_i:y_w(S)>=t}|) dt.

Do not retain the old discrete threshold sum for fractional capacities. Then minimum exactness, the greatest tight minimum, order-independent deletion, union closure and one-flow extraction all remain valid.

For integer demands, (RD) is exactly the earlier antitone condition. In particular, **receiver-capacity integrality is unnecessary** for the original equal-integer-demand theorem. Fractional demands are also allowed in some unequal-demand systems; the theorem does not wrongly reject all real demands.

**Proof adaptation.** A positive continuous rearrangement gap supplies a pair with

    max(P_x,y_y(S)) < min(P_y,y_x(S)).

Incoming nesting and the pair implication still force x absent, y selected and y_x=y_y+1. Thus the high receiver has strict slack and the low receiver is above its capacity.

Let S be a minimum and x lie outside M+. Adding x has actual gain a>d_x. Although a is no longer an integer, each affected receiver gains at most one, so a<=A, where A is the INTEGER number of unsaturated targets of x. Consequently A>=floor(d_x)+1.

Let ell be the actual loss from deleting y. Minimality gives ell<=d_y. Let B be the number of its targets whose current count is at most capacity. Each of those targets loses exactly one, since it already has an incoming arc from y. Other targets can lose a fraction, so B<=ell. The same outgoing-nesting injection gives A-1<=B. Therefore

    floor(d_x)+1 <= A <= B+1 <= ell+1 <= d_y+1 <= floor(d_x)+1.

All inequalities are equalities. In particular ell=d_y=floor(d_x), so deletion is neutral. Notice that d_x itself need not equal d_y. This proves the modified neutral-deletion step and the unchanged finite termination argument.

For persistence replace indicator losses by

    ell_w(S) = min(P_w,y_w(S)) - min(P_w,y_w(S)-1),

for targets w of the selected y. These losses are nondecreasing when the source set shrinks but still contains y. Neutrality at S and T, obtained by intersecting minima, again forces equality term by term. At the low receiver x its loss is less than one because y_x(S)>P_x. Equality forces y_x(T)>P_x as well. Third-source incoming equality propagates to T, and y_y(T)<P_y still holds. Together with P_x<P_y, these inequalities give a positive continuous crossing at T. The canonical argument follows unchanged. The union-closure calculation in Section 5 already works for real capacities. The flow cut identity also works over the reals. QED.

**Sharpness as a uniform local demand condition.** This does NOT mean every individual system violating (RD) fails. It means no unconditional theorem over all WCD systems can permit an arbitrary violating capacity-ordered demand pair.

Take any a,b>=0 with b>floor(a)=k. Make one block {x,y}, capacities (0,1), demands (a,b), with both arcs between x,y. Add k singleton-block auxiliary vertices, each of capacity 2 and demand 0. Both x and y point to every auxiliary; auxiliaries have no outgoing arcs. This satisfies even the original strict TCD. Auxiliary source selection has no effect, leaving only four relevant source choices:

| Selected from {x,y} | F | G |
|---|---:|---:|
| neither | 0 | 0 |
| x | k+1-a | k+1-a |
| y | k-b | k+1-b |
| both | 2k+1-a-b | 2k+1-a-b |

Since k<=a<k+1 and b>k, the unique relevant exact minimum is k-b<0. Every entry in the G column is strictly larger. This constructs a counterexample for EVERY violating pair. In particular every nonintegral common demand a=b fails in some system, not merely demand 1/2 on two vertices.

**Executed checks.** Exact Fraction arithmetic verifies 25,800 three-vertex half-integer-capacity instances and 229,104 four-vertex instances. Their minimum/canonical discrepancies are zero; 4,588 and 75,456 respectively have fractional minimum values. A further 36,690 instances test (RD) with fractional demands, and 24 rational members of the sharpness family are checked. A positive example with capacities (0,3/4), demands (1/2,0) and mutual arcs confirms that permitted fractional demands can require a genuine neutral deletion. An additional demand-1 example has an addition margin of 1/2, explicitly demonstrating why the old integral-margin step cannot simply be reused.

These checks support the real-variable proof; they do not establish it by extrapolation from half-integers.

## 10. Exact continuation target

The next step is a focused novelty/dependency comparison of Theorems B and C with the cited Ferrers/threshold neighbourhood theory and the classical representation of all minimum cuts. The specific questions are whether those results already imply (i) the greatest rearrangement-tight minimizer and order-independent deletion and (ii) the sharp rounded-demand boundary. Produce an implication proof or a precise separation example, not merely a list of related citations.

Start by reading the FULL Marmulla–Brandes paper (DOI 10.7155/jgaa.v30i1.3099), not its abstract, and the original minimum-cut representation results it or the literature identifies. That comparison has NOT been done in this session. Do not promote novelty, a new D2C bound or a full Murty–Simon theorem while it remains open.
