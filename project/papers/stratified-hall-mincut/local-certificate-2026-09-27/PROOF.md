# Local certificates for the greatest rearrangement-tight Hall minimum

27 September 2026. Internal research result with a hand proof and executed exact tests. Not externally reviewed, formally verified, or novelty-cleared. No new Murty–Simon edge bound or general conjecture proof is asserted.

## 1. Model and claim

Let V be a finite nonempty set, partitioned into blocks. Let R be a loopless directed relation. Every supported source–receiver arc has capacity one. A vertex w has receiver capacity P_w and source demand d_w, each a finite nonnegative real number. For S contained in V write

    y_w(S) = |{u in S : u R w}|,
    H(S) = sum_w min(P_w,y_w(S)),
    D(S) = sum_(u in S) d_u,
    F(S) = H(S)-D(S).

Within each block, sort its capacities and its receiver counts separately in the same direction and sum the coordinatewise minima. Summing over blocks defines U(S). Put G=U-D. The elementary same-order rearrangement inequality gives H<=U. One way to prove it is to integrate the intersection bound

    |{w:P_w>=t and y_w(S)>=t}|
      <= min(|{w:P_w>=t}|, |{w:y_w(S)>=t}|)

within each block. The right side is attained by same-order pairing. This continuous layer-cake argument covers real capacities; a discrete threshold sum would not.

Let gamma=min F, and let M+ be the greatest exact minimizer. Such a greatest minimizer exists: each receiver term is a concave nondecreasing function of a modular count, so F is submodular, and its minimizers are closed under union and intersection.

A tight exact minimizer is a set T with F(T)=gamma and H(T)=U(T). These sets need not form an intersection lattice. The theorem below supplies a certificate for their greatest member when a specified deletion sequence exists. It does NOT assert that every input has a tight minimizer, a greatest tight minimizer, or a successful sequence.

**Theorem L (local canonical certificate).** Supply a feasible supported flow and verify that its residual network has no source-to-sink path. Derive M+ as in Section 2. Starting at M+, supply a sequence of deletions obeying the local rule in Section 3. Every maximal local deletion sequence has the same terminal C, whether tight or not. If H(C)=U(C), then:

1. F(C)=gamma and min G=min F=gamma.
2. Every tight exact minimizer is contained in C. Thus C is their unique greatest member.

A successful certificate exists exactly when this unique terminal is tight.

No global nesting, pair-compatibility condition, demand ordering, or demand integrality is assumed in this statement. The mathematics allows real quotas; the accompanying executable verifies exact rational inputs. The unique terminal may fail to be tight outside the inherited structural class. Order-independence is not completeness.

## 2. Certifying optimality and the greatest starting set

Use distinct source and receiver copies, with arcs

    s -> u_L: capacity d_u,
    u_L -> w_R: capacity 1 if u R w,
    w_R -> t: capacity P_w.

For a prescribed set S of left vertices on the source side, choosing the receiver sides optimally gives cut capacity

    D(V\S) + H(S) = D(V)+F(S).

Hence minimum network cut value is D(V)+gamma. Feasibility of a supplied middle-arc flow is checked directly, including unit capacities and source/receiver bounds; the outer flows are its row/column sums. A feasible flow with no residual s-to-t path is maximum: its residual source-reachable set gives a cut of equal value.

For the GREATEST rather than least minimum cut, let Q be the set of all network vertices from which t is reachable by positive residual arcs. Its complement A is forward-closed in the residual network, includes s, and excludes t. It is a minimum-cut source side. Every minimum-cut source side is forward-closed and cannot intersect Q, so is contained in A. Thus A is the greatest one. Projecting A to the left vertices gives M+.

For completeness of the projection argument: every exact F-minimizer has a receiver-side completion giving a minimum cut by the displayed identity. Conversely the left projection S of any minimum cut has D(V)+F(S) no larger than that cut and no smaller than the minimum value, so F(S)=gamma. Therefore the left projection of the greatest cut is precisely the union of all exact minimizers.

The verifier computes Q by reverse reachability FROM t. It does not substitute forward reachability from s. It additionally checks flow value = D(V)+F(M+). These are checks on the supplied instance, not trust in a producing solver.

## 3. Local deletion rule

At an exact minimum S, choose a source a in S and receiver indices x,y. Require:

- x and y lie in the same block, and P_x<P_y.
- a R x and NOT a R y.
- On the remaining currently selected rows, z R y implies z R x for every z in S\{a}.
- There is a positive crossing:

      max(P_x,y_y(S)) < min(P_y,y_x(S)).                 (L1)

- Deletion is explicitly neutral:

      F(S\{a}) = F(S) = gamma.                        (L2)

Then delete a. The distinguished source a need not equal the high-capacity receiver y. The low receiver x may itself be selected. These relaxations distinguish this certificate from the earlier high-endpoint-only crossing procedure. The selected-row implication is local to the actual witness, not a new global nesting requirement.

The two row conditions say that the selected incoming rows of the high receiver are contained in those of the low receiver, with a supplying at least one strict difference. If a=y, looplessness makes the missing a R y automatic; the general rule does not rely on that special case.

## 4. Persistence proof

**Lemma.** Under the local rule, every exact minimum T contained in S that contains a still has a positive crossing between x and y. Consequently it is not tight.

**Proof.** Since T and S\{a} are exact minima and exact minima are intersection-closed,

    T\{a} = T intersect (S\{a})

is an exact minimum. Thus deleting a from either S or T loses exactly d_a units of capped receiver capacity.

For each receiver w reached by a, define

    ell_w(W) = min(P_w,y_w(W)) - min(P_w,y_w(W)-1)

for W containing a. Its incoming count is at least one. As W shrinks, ell_w(W) can only increase, because the capped count has nonincreasing marginal increments. Hence ell_w(T)>=ell_w(S) term by term. The sums are both d_a, so equality holds at every reached receiver.

In particular, a R x and (L1) give y_x(S)>P_x, so ell_x(S)<1. Termwise equality gives ell_x(T)<1, which forces y_x(T)>P_x. Also y_y(T)<=y_y(S)<P_y.

The selected-row containment continues to hold on T, and a remains in T. Therefore

    y_x(T) >= y_y(T)+1.

Together with P_x<P_y, the four strict inequalities imply

    max(P_x,y_y(T)) < min(P_y,y_x(T)).

This is a positive crossing. Swapping the two capacities in their block strictly increases the capped sum: throughout the nonempty displayed threshold interval, the original capacity and count superlevel sets cross. Thus U(T)>H(T). QED.

This proof uses equality of nonnegative termwise differences, not cancellation of signed quantities. No integer demand or positive integral objective gap is needed. Unit supported arcs are used in the marginal-loss formula and the distinguished-row difference; no arbitrary weighted-arc extension is asserted.

## 5. Proof of Theorem L

Initially every exact minimizer, hence every tight one, is contained in M+. Inductively suppose the current S contains every tight exact minimizer. Neutrality preserves F(S)=gamma. If a tight exact minimum T contained the next deleted a, the persistence lemma would contradict its tightness. Therefore no tight exact minimum loses a vertex in this step, and the containment invariant survives.

Each step strictly reduces S; at most |V| steps are possible. At a tight terminal C, neutrality gives F(C)=gamma and H(C)=U(C), so G(C)=gamma. Since G>=F>=gamma everywhere, min G=gamma. The maintained containment invariant says that C contains every tight exact minimizer, proving greatestness and uniqueness. Any other successful certificate has a tight terminal with the same greatestness property, hence the same terminal. QED.

The argument does not prove union closure of the whole tight family on arbitrary certified instances. A greatest member is not by itself union closure. Nor does it produce certificates for every instance whose minimum margins happen to agree.

## 6. Commutation and unique termination, even on failed instances

The persistence lemma gives more than exclusion of tight witnesses. If deletion of a using receivers x,y is valid at S, then the SAME deletion with the SAME receivers is valid at every exact minimum T contained in S that still contains a. The lemma supplies the positive crossing. Intersection closure supplies neutrality. The row-containment condition is inherited on subsets, and the distinguished arcs are unchanged.

Consequently, if two different sources a,b can be deleted at S, deletion of a remains valid at S without b, and deletion of b remains valid at S without a. Both two-step paths end at S without {a,b}. Different witnesses deleting the same source already have the same immediate result.

Every path is finite, since one source is removed per step. A direct induction on |S| now proves uniqueness of its terminal: for two possible first deletions of different sources, the common two-step descendant has a unique terminal by induction. Each first descendant has that same terminal by induction. If the first deleted sources agree there is nothing to prove. The zero-move case is immediate. This proves confluence without assuming that any tight terminal exists.

It follows that a greedy search choosing ANY admissible triple (a,x,y) decides whether this local certificate class succeeds; no branching search is required. A straightforward search over triples and exact quantity recomputation is polynomial in the finite input size (including rational bit lengths), with at most |V| successful deletions. No improvement over ordinary flow asymptotics or novelty of a general rewriting principle is claimed.

The exact tests explore every reachable local choice, not merely one greedy path, and assert that there is exactly one terminal per instance. Stuck instances therefore cannot be rescued simply by choosing a different order under the SAME rule. Section 10 proposes changing the information allowed in the rule instead.

## 7. Relation to the inherited structural theorem

In the existing WCD/RD theorem, same-block capacity-ordered pairs have incoming/outgoing nesting, a reverse-arc implication, and d_y<=floor(d_x). That earlier theorem supplies neutral deletions of selected high endpoints from M+ until tightness.

At its actual crossings, selected third-row incoming nesting is an equality term by term: the low receiver has exactly one more incoming arc, supplied by the high source, and the low source is absent. Accordingly its deletions obey Section 3 with a=y. The local verifier can certify those sequences without evaluating the global assumptions.

Thus the inherited theorem supplies certificate existence on its own stated class; Theorem L supplies a separate soundness proof that also accepts some inputs outside that class. The existence implication is conditional on the inherited theorem, not a new external audit of all its premises. The exhaustive checks here verify that implication on their stated finite domains only.

## 8. Strictly broader examples

All vertex labels are zero-based. HOSTILE_RESULTS.json stores the instances, flows, checks and traces.

**A third source performs the deletion.** One block, P=(0,0,1), d=(0,0,0), and only arc 0->1. M+=V, gamma=0. Choose x=1,y=2,a=0. Deleting 0 is neutral and yields the greatest tight minimum {1,2}. An endpoint-only rule cannot take this step: the high receiver 2 has no outgoing arc to the low receiver 1.

**Selected low receiver and fractional demand.** One block, P=(0,1), d=(1/2,0), only arc 1->0. M+=V and gamma=-1/2. With x=0,y=1,a=1, delete 1 and obtain C={0}. The low receiver was selected throughout. The global pair implication fails, yet the local certificate is valid.

**Strict reverse selected-row nesting.** Blocks {0,1},{2}, P=(1,3,0), d=(0,0,1), arcs 1->0 and 2->0. The original incoming nesting fails at third vertex 2. Nevertheless delete a=1 using x=0,y=1; C={0,2}, gamma=0. The local implication is strict, not selected-row equality.

**Fractional capacity.** One block, P=(0,3/4), d=(1/2,0), both arcs. The supplied flow sends 1/2 from 0 to 1. M+={1}, gamma=0; deleting 1 gives C empty. This verifies exact rational flow, residual extraction and neutral deletion together.

## 9. A proved incompleteness boundary

One block, P=(0,2,1), d=(1,1,0), and arcs

    0->1, 0->2, 1->2.

The flow 0->1 and 1->2 has value two. The exact minima are

    empty, {2}, {1}, {1,2}, {0,1}, {0,1,2},

all of value zero. The tight minima are exactly empty, {2}, {1}, {1,2}. Therefore M+=V and the greatest tight minimum is {1,2}.

At M+, the only crossing is low receiver 2 versus high receiver 1. Deleting source 0 would be neutral, but it hits BOTH receivers, so is not a distinguished incoming row. Source 1 supplies the strict incoming difference but deleting it is not neutral. There is no admissible local step. This is a genuine boundary of certificate completeness, not a refutation of soundness or of closure. All eight subset values are saved in INCOMPLETENESS.json.

The residual path

    0_L -> 2_R -> 1_L

explains the missing information. The first arc has unused capacity; the second reverses the supplied unit flow from 1 to 2. Every minimum-cut source side containing 0_L must therefore contain 1_L. In this example the source providing the strict count difference is forced by the source being deleted, instead of being that source itself.

## 10. Exact next mathematical task

Extend the certificate by a checked residual implication a_L -> b_L, where the neutral deletion removes a, a reaches the low receiver, and b supplies the strict incoming-row difference. Test soundness by redoing the persistence proof, then implement and exhaustively check the rule; begin with Section 9's frozen instance. All-or-none residual components may be needed beyond single-source deletions.

This enhanced rule is NOT implemented or counted as tested in this checkpoint. Do not silently treat the present certificate as complete. The original Chen-main-condition comparison also remains source-blocked; see COMPARISON.md rather than repeating an abstract-only inference.
