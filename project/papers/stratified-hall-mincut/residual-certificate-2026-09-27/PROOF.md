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
