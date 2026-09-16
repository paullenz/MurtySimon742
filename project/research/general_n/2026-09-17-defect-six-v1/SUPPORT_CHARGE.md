# Pair-covered interfaces and a critical-edge charge inequality

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**WIP_UNVERIFIED: complete hand derivation preserved before new finite checks.** All claims concern the actual whole-level exact block in the source treatment pinned at 314f953a5ba15ca62148d52062bd0ee8568dcccb. External mathematical review, novelty, sharpness and catalogue promotion remain open. The preceding special-case D=6 proof remains unchanged at f047855b3d4f51f273fe1ba270284f6025134243.

## 1. Statements

Use the source definitions: |T|=|H|=d, Q=G[T], K=N_G(T) intersect (A minus T), full receiver pools V_t with p_t>=1 and m=sum p_t, defect D=L+beta+2mu, mu=binom(d,2)-e(Q), and weights w_k in {d-1,d}. Define

    E_h(Q)=#{ts in E(Q): deg_Q(t)>=h+1 and deg_Q(s)>=h+1}, h>=1.

Call the interface pair-covered when every two distinct tight vertices have a common neighbour in K. The following are necessary conditions for an actual diameter-two edge-critical realization.

(A) If D<d(d-2), then the interface is pair-covered. More precisely every distinct t,s have at least

    d-floor((d+D)/(d-1))

common K-neighbours.

(B) Whenever the interface is pair-covered, for every integer h>=1,

    E_h(Q) <= L+floor(L/h)+beta.                         (SC)

Consequently

    D >= 2mu + ceil(h E_h(Q)/(h+1))                     (1)

for each h. Neither statement needs one interface label adjacent to all T.

(C) At d=5 these conditions close both D=6 and D=7, strengthening the source conclusion to

    D>=8, W>=5+4m+8, W>=33,
    extra high-source selections imply W>=53.           (2)

No claim at D=8, graph attainability or unrestricted exact-block coverage is made.

## 2. Pair coverage from exact rows

Write K_t=N_G(t) intersect K and kappa=|K|. Every K-label has weight at least d-1, and the exact identity is

    sum_K w_k=d+(d-1)m+D.

Therefore kappa<=m+floor((d+D)/(d-1)). The source rows give

    |K_t|=1+m-p_t+beta_t+nu_t,
    nu_t=d-1-deg_Q(t), beta_t>=0.

Since the other d-2 pools are nonempty, p_t+p_s<=m-(d-2), so |K_t|+|K_s|>=m+d. Subtracting kappa proves (A). The strict bound on D makes its displayed integer lower bound at least one. This uses full pools, not merely the selected destinations, and is an actual interface assertion.

## 3. Exactly which external vertices can threaten a tight edge

For a tight support S subset T define its threat set

    B_Q(S)={ts in E(Q): s in S, t outside S,
                         N_Q(t) intersect S={s}}.

Edges are unordered; the displayed orientation is the one whose first endpoint is outside S. At most one edge is contributed by each t outside S, so |B_Q(S)|<=d-|S|. Membership means a particular tight-intermediate replacement is unavailable, NOT that the edge really is critical; other external replacement paths can still exist.

Suppose the interface is pair-covered and delete a tight edge ts. Its endpoints still have a path through a common K-neighbour. Every affected pair wholly inside T also retains such a path. The only other potentially destroyed short paths have endpoints t,x with x an exclusive neighbour of s, or the reverse.

Every full-pool vertex v in V_s is adjacent in G to every K-label k that neighbours s. To check this, kv cannot be residual in J because R_v=T minus {s}; it cannot be selected in J because k and v both miss s in J, contradicting domination of all A-labels. Hence kv is absent in J. A common K-neighbour of t,s thus supplies t-k-v. This does not require k to neighbour every tight vertex.

The pivot, high vertices and A-labels outside T union K have no tight G-neighbours. All other vertices are K-labels or O=B minus (H union V). For x in either class, put S_x=N_G(x) intersect T. If x is an exclusive neighbour of s and ts is not in B_Q(S_x), some r in N_Q(t) intersect S_x differs from s, supplying t-r-x. Reverse t,s.

It follows that every critical tight edge must lie in the union of the sets B_Q(S_x) for x in K union O. This is a necessary cover; it is not a converse. In particular full-pool singleton supports have been protected rather than incorrectly charged as exceptions.

## 4. Charge threats to loss and residual incidences

Fix h>=1 and count only edges in E_h(Q). For k in K put l_k=w_k-|S_k|>=0. If k threatens an edge ts in this set, the outside endpoint t has at least h+1 neighbours in Q, exactly one of which lies in S_k. All its other neighbours, and t itself, lie outside S_k. Thus

    d-|S_k|>=h+1.

But d-|S_k|=d-w_k+l_k<=l_k+1, so l_k>=h. This k threatens at most d-|S_k|<=l_k+1 counted edges. Summing over contributing K-labels costs at most L plus their number. Their number is at most floor(L/h), because each consumes at least h distinct units of the nonnegative total L.

For x in O, let q_x=d-|S_x|. No tight label is selected at a low source, so q_x counts its residual tight incidences. All tight residual incidences in full pools were subtracted in beta, and high vertices select rather than retain T. Hence sum_(x in O)q_x=beta. The threat bound for these vertices sums to at most beta.

The necessary cover in Section 3 gives (SC), even with overlapping threats: a union has size at most the sum of its sizes. Put q=L+beta. Then E_h<=q+floor(q/h)=floor((h+1)q/h), which implies q>=ceil(h E_h/(h+1)), proving (1). No computational enumeration or fixed-order bound is used.

For h=1, E_1<=2L+beta. For h=2, E_2<=L+floor(L/2)+beta. This refines the worst-case bounded-hole lemma by accounting for the total support loss and the number of exceptional labels.

## 5. Hand corollary for d=5

The source treatment gives D>=6. Suppose D is 6 or 7. Since D<15, Section 2 supplies pair coverage. The source universal-core envelope excludes mu=0 and mu=1 (their lower bounds are 12 and 8), while 2mu<=D excludes mu>=4. Thus mu=2 or 3.

If mu=2, no Q-vertex has degree one: that would require three missing incident edges. All eight Q-edges therefore lie in E_1. Equation (SC) gives

    8<=2L+beta<=2(L+beta)=2(D-4)<=6,

a contradiction. This includes both adjacent and disjoint missing edges; no common-label congruence or special exceptional-support case is needed.

If mu=3, Q has seven edges and total missing degree six. Each Q-degree-one vertex consumes three units of missing degree, so there are at most two such vertices. At most two edges have a degree-one endpoint; degree-zero vertices have no incident edge. Consequently E_1>=5. But

    E_1<=2(L+beta)=2(D-6)<=2,

again a contradiction. Therefore D>=8. The capacity conclusions (2) follow from the exact W identity, m>=5 and m>=10 when extras exist.

## 6. Diagnostic observation and next checks

An executed elementary local enumeration, used only to inspect the new bound, evaluated all 1024 labelled Q at d=5 and all 32768 at d=6. It minimized 2mu+max((d-2)max(0,g-1), max_h ceil(h E_h/(h+1))) over Q, finding minima 8 and 13 respectively. Forty d=5 and sixty d=6 graphs attain those necessary-condition minima. These are NOT original graph realizations, and no d=6 theorem is promoted from this diagnostic. Its reproducible code and per-graph ledger are to be preserved with the fresh tests.

Next verify the pair-covered local deletion criterion on graphs with two external probes, including an example with no single all-tight common label. Check the exact threat cover and charge separately using another path implementation. Include deliberate failures of pair coverage and pool protection, and controls demonstrating that threat coverage is not sufficient for criticality. Preserve the input/decision streams, negative cases and boundary table. Review D=8 only after this bounded theorem and its evidence are durably checked.
