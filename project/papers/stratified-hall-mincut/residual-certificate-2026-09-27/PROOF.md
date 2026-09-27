# Residual implication certificates for tight Hall minima

27 September 2026. Internal hand proofs; not external review, formal verification,
novelty clearance, or a general Murty–Simon proof. X3, audit34854911792,
equality and certification controls are unchanged. Predecessor:
b61a0b59d3960b6a48c2c0e869667a843ef6b18c.

## 1. Model and reconstructed predecessor

Use the loopless unit relation, nonnegative finite real P,d, partition, y,H,D,F,
and same-order sorted-capacity bound U of ../local-certificate-2026-09-27/PROOF.md.
Let gamma=min F. F is submodular, so its minima form a union/intersection lattice.
H<=U by the continuous layer-cake intersection inequality, including real P.

The OLD local rule at a minimum S deletes a source a provided x,y are in one
block, P_x<P_y, aRx, not aRy, all selected high-incoming rows also enter x,
max(P_x,y_y(S))<min(P_y,y_x(S)), and F(S-a)=gamma. In particular it requires
that the removed row itself supply a strict incoming difference.

## 2. Complete cuts and source projections

Fix ONE checked maximum flow in the ORIGINAL full network:
s->u_L of capacity d_u, u_L->w_R of capacity 1 for uRw, w_R->t of capacity P_w.
Its positive residual network is fixed throughout all deletions. The capacity
of the cheapest cut with left projection S is D(V)+F(S). Thus every F-minimum
has at least one complete minimum-cut completion, and every minimum cut
projects to an F-minimum. A minimum cut has no residual edge leaving its
source side: capacity minus flow value is the sum of forward residual
capacities across the cut. Conversely a residual-forward-closed side containing
s and excluding t is a minimum cut.

Consequently a residual path a_L -> b_L implies: EVERY F-minimum containing a
contains b. This statement transfers through a complete cut; it does not
pretend that the left projection alone is a complete cut. Intermediate right
vertices, s, and sources later removed from the current set are not dropped
from the fixed residual graph. If a completion contains a path's start it
contains the entire path. A path to t is impossible for a in any minimum.

The complement of the vertices reaching t is the greatest complete minimum
cut. Its left projection M+ is the greatest F-minimum. Different receiver
completions can have the same left projection; this causes no ambiguity for
M+ or the implication argument. No converse equating all logical implications
with paths from a is asserted (mandatory b can be reachable from s instead).

## 3. Path rule P

At an exact minimum S choose sources a,b and receivers x,y. Require:

1. a in S; x,y in the same block; P_x<P_y.
2. aRx (aRy is now allowed).
3. bRx and not bRy, and a checked positive-residual path a_L -> b_L.
   The length-zero path [a_L] is allowed when a=b.
4. For every z in S, zRy implies zRx.
5. max(P_x,y_y(S)) < min(P_y,y_x(S)).
6. F(S-a)=gamma (explicit exact neutrality).

Then delete a. The implication guarantees b in S. This contains the old rule
by taking b=a and the length-zero path.

**Persistence theorem P.** If this rule is valid at S, it is valid with the
SAME witnesses and the SAME fixed residual path at every F-minimum T subset S
containing a. No such T is tight.

Proof. T-a=T intersect (S-a) is a minimum. For each w reached by a put
ell_w(W)=min(P_w,y_w(W))-min(P_w,y_w(W)-1), for W containing a.
These losses are nondecreasing as W shrinks. Their sums at S and T both equal
d_a. Thus every loss agrees termwise. At x, y_x(S)>P_x implies ell_x(S)<1,
so ell_x(T)<1 and hence y_x(T)>P_x. Also y_y(T)<=y_y(S)<P_y.
The residual implication forces b in T. Selected-row containment and b's
strict difference give y_x(T)>=y_y(T)+1. Together with P_x<P_y these four
strict inequalities prove the same positive crossing at T. Interchanging
capacities P_x,P_y strictly increases H on its crossing interval, so U(T)>H(T).
Neutrality, row containment and all the other rule conditions persist. QED.

**Confluence theorem P.** All maximal P-deletion sequences from M+ have one
terminal, even if that terminal is not tight.

Proof. Two admissible distinct deletions a,c commute: S-c is an exact minimum
containing a, so persistence allows a there, and conversely for c after a.
Both paths reach S-{a,c}. Different witnesses for the same deletion have the
same successor. Induction on |S| proves unique termination because every step
reduces cardinality. This proof also covers intermediate exact minima. QED.

**Certificate theorem P.** Every state of such a sequence contains every
tight exact minimum. If its terminal C is tight, C is their unique greatest
member and min(U-D)=min F=gamma.

Proof. Start at M+. If a tight minimum contained a deleted source, persistence
would give a crossing in that minimum, contradiction. Thus containment is
preserved. At a tight terminal, U(C)-D(C)=F(C)=gamma, while U-D>=F>=gamma
pointwise. This proves the result. No completeness or general margin sign is
claimed. No union closure of the tight family follows merely from greatestness.

## 4. Frozen example

One block, P=(0,2,1), d=(1,1,0), R={0->1,0->2,1->2}. Use flow 0->1 and
1->2, each one. M+={0,1,2}, gamma=0. With a=0,b=1,x=2,y=1, the checked
path is 0_L -> 2_R -> 1_L. At S the counts at x,y are 2,1, and
max(1,1)=1<2=min(2,2). All high-incoming rows also enter x. Deleting 0 is
neutral. The remaining {1,2} has H=U=1 and demand 1. Hence it is the greatest
tight minimum. Source 1 itself cannot be neutrally deleted at S. This is a
strict extension of the old rule, not an inherited result.

## 5. Status at first checkpoint

The preceding proofs have been checked internally by direct derivation.
Implementation and exhaustive replay are the next unit; no new executed test
coverage is claimed at this first checkpoint. All-or-none residual blocks are
an unimplemented prospective strengthening here.

## 6. All-or-none residual source blocks (subsequent extension)

Fix the same full residual network. Its strongly connected components (SCCs)
partition network vertices. The nonempty LEFT projections K of SCCs partition
sources. Every exact minimum contains all or none of each K, because any
complete cut containing one SCC vertex contains the entire SCC. We do NOT
identify K with the full SCC: it may also contain right vertices, s or t.
Those vertices are not source demands and are not removed from the network.

**Block rule B.** Replace singleton removal in rule P by removal of one such K.
Require K subset S, F(S-K)=gamma, k_x=|{u in K:uRx}|>0, an anchor a in K,
and a residual path a_L -> b_L, with b the strict row from rule P. Keep the
same receiver crossing and selected-row containment. K must be the full left
projection of an SCC, not an arbitrary strongly connected selection.

**Persistence theorem B.** For an exact minimum T subset S that meets K,
all of K lies in T. Then T-K=T intersect (S-K) is a minimum. Set
k_w=|{u in K:uRw}| and
L_w(W)=min(P_w,y_w(W))-min(P_w,y_w(W)-k_w), for W containing K.
For fixed k_w>=0 this is nonincreasing in y_w(W); thus L_w(T)>=L_w(S).
Both sums equal D(K), so equality holds receiver by receiver. Since k_x>0
and y_x(S)>P_x, L_x(S)<k_x. Thus L_x(T)<k_x, forcing y_x(T)>P_x.
The anchor is in T, hence b is in T. Containment and b give y_x(T)>y_y(T),
while y_y(T)<P_y. The crossing, neutrality and every rule condition persist.
In particular no tight exact minimum meets K. QED.

**Confluence and certificate theorems B.** Distinct fixed source blocks are
disjoint. If two deletions are available, each remains available after the
other by persistence. The same finite diamond induction proves a unique
terminal for every maximal block sequence. Tight termination certifies the
greatest tight minimum and minimum-margin exactness as before.

Rule B subsumes rule P: a neutrally deletable singleton a cannot share a
residual SCC with another source in S, since S-a is a minimum. All sources
in a's SCC were already in S. Thus its source block must be {a}. This avoids
an unsound mixture of overlapping singleton and block moves.

The proofs do not assert completeness. A fixed SCC need not be neutrally
removable: selected sources in predecessor SCCs can force it. Nor does a
crossing guarantee the selected incoming containment assumed by both rules.
