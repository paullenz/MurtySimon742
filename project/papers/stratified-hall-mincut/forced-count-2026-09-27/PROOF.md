# Residual forced-count Hall certificates, version 3

27 September 2026. Internal mathematics only, not external/formal verification,
novelty clearance or a general Murty–Simon proof. Inspected main:
fc5d692113f62a55c91dacbca3a5b1a499f65cb1. The predecessor version-2 package
remains unchanged at ../residual-certificate-2026-09-27/.

## 1. Exact rule and inherited framework

Use the predecessor's finite loopless unit source-receiver relation R, source
demands d, receiver capacities P, and receiver-block partition. Quotas are
nonnegative finite reals in the theorem, exact rationals in the verifier.
H(S)=sum_w min(P_w,y_w(S)), D(S)=sum_(u in S)d_u, F=H-D, gamma=min F.
U pairs the capacities and counts in sorted order within each block. F is
submodular; its minima are closed under unions and intersections. H<=U.

One feasible supplied flow is checked maximum in the FULL ORIGINAL network
s->u_L->w_R->t with capacities d_u,1,P_w. All positive residual arcs and
reachability below refer to that unchanged full network. Exact F-minima are
precisely the left projections of complete minimum cuts. Every such complete
cut is residual-forward-closed. M+, the greatest F-minimum, is the left
projection of the complement of the vertices reaching t. Right vertices,
s and t are not source demands and never count as incoming source rows.

At an exact minimum S, choose a nonempty removal K and an anchor a in K.
In path mode K={a}; in block mode K is the FULL left projection of a residual
SCC. Require K subset S, F(S-K)=gamma, and choose x,y,b with:

- x,y in one receiver block and P_x<P_y;
- a checked residual path a_L -> b_L (zero length permitted);
- bRx and not bRy;
- every z in S with zRy also satisfies zRx;
- max(P_x,y_y(S)) < min(P_y,y_x(S)).

Let C_a be the set of LEFT/source vertices reachable from a_L, including a,
and q_x(a)=|{u in C_a:uRx}|. Require one of two low-receiver safeguards:

(I) k_x=|{u in K:uRx}|>0; or
(FC) q_x(a)>P_x.

Version 3 explicitly records which guard is used. For FC it supplies the
claimed contributing source set; the verifier recomputes the exact set from
the checked flow, requires equality of sets and checks the strict inequality.
It never trusts a supplied count or uses reachability in the source-induced
subgraph. Selecting only one of two applicable guards does not change the
possible removed sets. Within an SCC all anchors have the same reachability.

## 2. Persistence, soundness and confluence

Let T subset S be an exact minimum meeting K. In block mode all of K belongs
to T by strong connectivity and complete-cut closure; in path mode this is
immediate. In particular a in T, so C_a subset T and b in T. Also
T-K=T intersect (S-K) is an exact minimum, giving neutral removal at T.

Under guard FC, y_x(T)>=q_x(a)>P_x directly. This bound uses only the fixed
residual implication, not neutral-loss cancellation. Under guard I, put
k_w=|{u in K:uRw}| and
L_w(W)=min(P_w,y_w(W))-min(P_w,y_w(W)-k_w), for W containing K.
As W shrinks these losses cannot decrease. Their sums at S and T both equal
D(K), so equality holds term by term. At x the original crossing and k_x>0
give L_x(S)<k_x; hence L_x(T)<k_x, forcing y_x(T)>P_x.

In either case selected incoming containment and b's strict difference yield
y_x(T)>=y_y(T)+1. Also y_y(T)<=y_y(S)<P_y and P_x<P_y. These four strict
inequalities yield the same positive crossing at T. Thus U(T)>H(T), and all
rule conditions including the SAME chosen safeguard persist.

Consequently no tight exact minimum meets K. Starting from M+ and repeatedly
applying the rule preserves containment of all tight exact minima. If the
terminal C is tight, it is their unique greatest member and min(U-D)=gamma.

Two available different SCC blocks are disjoint, and each move persists after
the other. Path moves also commute. A neutrally deletable singleton cannot
share an SCC with another source, since S-a is an exact minimum. Thus path
moves form a subclass of block moves. The finite diamond argument proves
one terminal for every maximal sequence of either mode, tight or not.
None of this asserts certificate completeness or nonnegative margin.

## 3. Frozen improvement and strictness boundary

For P=(1,0,1), d=(1,0,0), one block, R={0->1,0->2,1->2}, use unit flow
0->2. M+=V and gamma=0. Version 2 is stuck at V. Version 3 first deletes
1 with x=1,y=0,b=0 and residual path 1_L->2_R->0_L. Although 1 misses
receiver 1, its forced contributor set there is {0}, so q_1(1)=1>P_1=0.
Deleting 1 is neutral. Then delete 0 by incidence to reach the greatest tight
minimum {2}. All eight source subsets are included in the focused evidence.

Strictness is essential. The predecessor's unsafe example has blocks
{0,1},{2}, P=(1,2,1), d=(0,2,0), R={0->2,1->0,1->2,2->0}. The attempted
deletion of a=0 using x=0,y=1 would lose the tight minimum {0,1}. Its forced
contributor set is {1}, giving q_0(0)=1=P_0, not a strict excess. Version 3
must reject this step, including when a false contributor set is supplied.

## 4. First implementation checkpoint

Focused tests are recorded separately. Exhaustive comparisons and remaining
obstructions are not assumed from the proof; they are the next test unit.
The current rule is an instance certificate class, not a completeness theorem.
