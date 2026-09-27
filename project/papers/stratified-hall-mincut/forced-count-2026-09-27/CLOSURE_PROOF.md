# Signed residual-closure certificates (schema 4)

Internal structural extension, 27 September 2026. Not external verification,
novelty clearance, or a general Murty–Simon proof. Schema 3 remains frozen.

## 1. Mandatory sources and exact anchored minima

Use PROOF.md's model and a fixed checked maximum flow with residual digraph Q
on the FULL network vertices. Write r(v) for its forward reachable set,
s,t for its original terminals. Every exact F-minimum is the source projection
of a complete minimum cut, which is residual-forward-closed, contains s and
excludes t. Let M- be the source projection of r(s).

For any a belonging to an exact minimum S, r(s) union r(a_L) is a complete
minimum cut: it is forward-closed, contains s and does not reach t. Its source
projection L_a is consequently the LEAST exact minimum containing a, and is
contained in S. In particular all mandatory sources are included, even if
there is no path from a_L to them. Thus the exact lower bound of y_x(T), over
exact minima T subset S containing a, is y_x(L_a).

A source a is mandatory iff a_L is reachable from s. If a is not mandatory,
let Pred(a) be all full network vertices that can reach a_L. From any complete
cut with source projection S, delete Pred(a). The result is still forward-
closed: an edge from a retained vertex to a predecessor would make that
vertex a predecessor too. It still contains s and excludes t. Therefore

    S' = S minus {u in S: u_L reaches a_L}

is an exact F-minimum. It is the greatest exact minimum contained in S that
omits a. This removes a reverse-reachable set, possibly spanning several
SCCs; it does not falsely declare those sources an all-or-none block.

## 2. A signed closure optimization

Fix same-block receivers x,y with P_x<P_y. Put
c_u=1_(uRx)-1_(uRy), and let m be the number of negative c_u. Define

    delta(a,x,y;S) = min {sum_(u in T)c_u : F(T)=gamma, a in T subset S}.

This is an integer. The following auxiliary network computes it exactly.
Keep every original residual-network vertex, add terminals sigma,tau, and
put B=n+1. Add capacity-B arcs:

- u->v for every positive original residual arc;
- sigma->s and sigma->a_L;
- t->tau and u_L->tau for every source u outside S.

For c_u=+1 add u_L->tau of capacity one. For c_u=-1 add sigma->u_L of
capacity one. Parallel capacities are added. Source/receiver copies remain
distinct. Receiver vertices have zero objective weight.

Every complete original minimum cut with a in its source projection T subset
S gives an auxiliary cut crossing no B-arc, of capacity m+sum_(u in T)c_u.
Conversely, any auxiliary cut crossing no B-arc is such a complete original
minimum cut. A feasible anchored original cut exists, with auxiliary cost at
most n, so B>n forces every minimum auxiliary cut to cross no B-arc. Hence

    auxiliary maximum-flow value = m + delta(a,x,y;S).

The distinction between complete cuts and source projections is essential:
receiver completions may differ but their objective weights are zero.

**Verification needs less than optimality.** ANY feasible auxiliary flow of
value f gives delta>=f-m by weak duality. Therefore a certificate only needs
a checked integral auxiliary flow with f-m>=1. No optimizer, claimed lower
bound, or asserted auxiliary maximum is trusted. The producer computes a
maximum flow to find certificates and compare the exact delta with an oracle.

## 3. Uniform crossing certificate

At an exact minimum S, choose a NONMANDATORY source a in S and same-block
x,y with P_x<P_y. Require:

    y_x(L_a)>P_x,       y_y(S)<P_y,
    a feasible auxiliary flow with value at least m+1.

Every exact minimum T subset S containing a then has y_x(T)>P_x,
y_y(T)<P_y, and y_x(T)-y_y(T)>=1. Thus (x,y) is a positive rearrangement
crossing in every such T. No tight exact minimum contained in S can contain a,
or any source that forces a. Delete the full predecessor source set in
Section 1; the new state is still an exact minimum and preserves every tight
one. If the final state is tight it is their greatest member and min(U-D)=gamma.

With an optimized auxiliary flow these conditions are NECESSARY AND
SUFFICIENT for this SAME ordered pair to cross in EVERY exact minimum
T subset S containing a. Necessity of the low and high bounds uses the actual
extreme minima L_a and S; necessity of the signed bound uses the displayed
minimum. This is completeness for a specified uniform pair, not completeness
of the overall tight-minimum certificate procedure.

## 4. Persistence and confluence with overlapping removals

Restrict S to an exact minimum T containing a. L_a is unchanged and contained
in T; high counts can only decrease. The auxiliary network merely gains
capacity-B exclusion arcs for newly absent source vertices. The SAME supplied
auxiliary flow remains feasible. Thus the same anchored pair certificate
persists, without recomputing its flow.

Two roots a,b can have overlapping predecessor sets. Removing their union
always gives the common state S minus (Pred_L(a) union Pred_L(b)). If b
survives removal of Pred_L(a), its certificate persists and its second removal
reaches that common state. If b does not survive, b reaches a; then every
predecessor of b is a predecessor of a, so the common state was already reached
by removing a's predecessors. The symmetric argument handles the other order.
All paths strictly reduce the source set. This local joining property and
induction on cardinality give a unique terminal, tight or not.

Schema 4 subsumes every schema-3 block move: if K is neutrally removable, no
source in S outside K can force its anchor a, so Pred_L(a) intersect S=K.
The schema-3 persistence theorem proves the pair is uniform. The exact tests
above therefore hold and a suitable integral auxiliary flow exists. The
incidence safeguard is subsumed as well: apply its loss argument at L_a.

## 5. Frozen schema-3 obstruction

One block, P=(0,2,0), d=(1,0,1), R={0->1,1->0,2->0}; flow 0->1 of value
one. gamma=-1. All minima contain source 2; they are {2},{0,2},{1,2},V.
The only tight minimum is {0,2}. At V, x=0,y=1 crosses, but source 0 enters
high receiver 1 without entering low receiver 0. All schema-3 moves fail its
row-containment condition.

For a=1, the least anchored minimum is {1,2}: the mandatory row 2 contributes
one incoming arc to receiver 0, as does row 1. Hence the low lower bound is
2>P_0=0, while the high upper bound at V is 1<P_1=2. The signed difference is
2 on {1,2}, and 1 on V. Its minimum is one. Removing the predecessors of 1
removes just {1}, yielding the greatest tight minimum {0,2}.

This is compensation by a mandatory incoming row, not pairwise row nesting.
No general certificate-completeness claim is made. Executed coverage and any
remaining obstruction are reported separately.
