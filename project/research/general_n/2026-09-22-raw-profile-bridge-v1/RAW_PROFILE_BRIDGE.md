# Raw criticality to the selected profile: independent reconstruction

22 September 2026. Status: **INTERNAL_REDERIVATION_NOT_EXTERNALLY_VERIFIED**.

This note reconstructs the entire graph-to-profile interface directly from edge deletion in a finite simple diameter-two-critical graph. It assumes neither the previous source-tuple premises nor the external e+disj+X proof. It is a same-project independent derivation, not external peer review or a formal proof.

## Quantified statement and domain

Let G have n>=3 vertices and diameter exactly two, with deleting any edge destroying the property that all distinct vertices are at distance at most two. Let v be ANY maximum-degree vertex, b=deg_G(v), a=n-1-b, and H the complement.

For a>=1, put A=N_H(v), B=V(G)\(A union {v}), F=G[A], and t=e(G)-b(n-b). For EVERY choice of one legal quasi-edge for each edge of G[B], define the selected and residual cross-edges as below. The ledger, source-demand injection, threshold-capacity inequality and profile projection below all hold. No optimizing choice, canonical tie-breaking, or positive surplus assumption is required.

The a=0 case must be separated before dividing by a. A D2C graph with a universal vertex is a star: an edge joining two other vertices could be deleted while the universal vertex still supplies every distance-two path. Consequently t=0 in that case.

**Scope defect found:** the 9 September strengthened proof displays t<5a^2/128+a/8 as a universal surplus bound without restricting a>=1. At a=0 a star gives 0<0, which is false. The same domain restriction is required for the 21 September displayed S39 surplus bound. This does not invalidate either maximum-degree implication, because both degree assemblies already handle a=0 separately. The profile calculations themselves always require a>=1.

## 1. Exact translation of edge-criticality

An adjacent pair x,y in H totally dominates H exactly when xy is a nonedge of G and x,y have no common G-neighbour. Thus H has no adjacent total-dominating pair.

For any edge uw of G, removing uw from G creates a pair of vertices that are neither adjacent nor have a common neighbour. In H+uw this is an adjacent total-dominating pair. This remains true if removing uw disconnects G: distance infinity also exceeds two.

Now restrict to u,w in B. A newly dominating pair in H+uw must contain u or w, since only the neighbourhoods of those two vertices changed. It cannot be the new pair {u,w}, because both vertices miss v in H+uw. Therefore the pair is an existing H-edge {u,i}, after possibly interchanging u,w. To dominate v, its other endpoint i must lie in A. Its original open-neighbourhood union is exactly V(H)\{w}: adding uw can newly cover only w for this pair, and there was no dominating pair beforehand.

Call this ui -> w a legal quasi-edge. Equivalently, in G, ui is a nonedge and N_G(u) intersection N_G(i) is exactly {w}. This equivalence provides a separate checker representation.

## 2. Choice-independent injection and exact ledger

Choose one legal triple (u,i,w) for each unordered edge {u,w} of G[B]. A chosen cross-edge ui determines its B endpoint u and its unique uncovered vertex w. It therefore cannot be selected for two different B-pairs.

At a fixed source u:
- chosen labels i are distinct;
- supplements w are distinct;
- no unordered B-pair is selected in both orientations.

Let Q be the selected cross-edge set. All remaining H[A,B] edges form R. Let rho_u and R_i be residual degrees at source u and label i; let x_i be the selected degree at i. Set r=|R|, d_i=deg_F(i), s_i=max(0,d_i-R_i), and S=sum_i s_i.

Since |Q|=e(G[B])=binom(b,2)-e(H[B]),

e(H) = a + binom(a,2)-e(F) + binom(b,2) + r.

Taking complements gives the exact identity

e(G)=b(a+1)+e(F)-r, hence e(F)=r+t.

Also sum_i d_i=2(r+t) and sum_i R_i=r. The minimum H-degree is a, so

deg_H(i)=1+(a-1-d_i)+R_i+x_i >= a,

which gives x_i>=s_i, 0<=s_i<=a-1, and

S >= sum_i(d_i-R_i) = r+2t.

These conclusions quantify over every legal selection. Selection can change the residual graph and demands; it cannot invalidate the identities.

## 3. Source-demand injection with explicit residual witnesses

Fix a selected ui -> w and j in N_F(i). Since i misses j in H and j is not the exceptional vertex w in B, u must meet j in H.

Partition these j according to whether uj is residual or selected. There are at most rho_u in the first class. In the second class write uj -> w_j. The supplements w_j are distinct and differ from w. The original ui dominates w_j, while u misses w_j; hence iw_j is an H-edge.

That H-edge iw_j is residual. Indeed i misses j because ij is an F-edge, and w_j misses j because uj -> w_j. So {i,w_j} fails to dominate the A-vertex j. Every selected cross-edge has its sole undominated vertex in B, ruling out selection of iw_j.

The map j -> iw_j is injective into the residual edges at i. Therefore

d_i <= rho_u + R_i, and s_i <= rho_u.

This proves the injection without counting witness incidences as if they were distinct physical sources.

## 4. Supplement forcing and the exact threshold count

Fix 1<=h<=H0=max_i s_i, and define

I_h={i:s_i>=h}, W_h=sum_{i in I_h}s_i,
Z_h={u:rho_u>=h}, z_h=|Z_h|.

Let ell_u be the ACTUAL number of selected labels of u in I_h. The inequality W_h<=sum_u ell_u uses x_i>=s_i; demand is never substituted for actual selected degree in the combinatorial count.

Source-demand injection shows that ell_u>0 implies u in Z_h. Let J={u:ell_u>h}, with j=|J|. For a selection ui -> w at u in J, each other selected heavy label k is an H-neighbour of w: the pair uk has a different exception and must dominate w, while u misses w. Thus w has at least ell_u-1>=h distinct neighbours in I_h.

These neighbours are not asserted to be all residual. If any wk is selected, source-demand injection gives rho_w>=s_k>=h. Otherwise all those at-least-h edges are residual, again giving rho_w>=h. Thus every supplement of a heavy selection from J lies in Z_h.

The heavy selections from J correspond to distinct unordered pairs inside Z_h meeting J. There are at most

j(z_h-j)+binom(j,2)=j*z_h-j(j+1)/2

such pairs. Other sources in Z_h have at most h heavy selections. Consequently

W_h <= (z_h-j)h+j*z_h-j(j+1)/2.

A label with maximum demand H0 has at least H0 distinct selected sources, each with residual degree at least H0. Thus z_h>=H0>=h. Put q=z_h-h. The difference between h*z_h+binom(q,2) and the preceding upper bound is

(q-j)(q-j-1)/2 >= 0,

because q-j is an integer (including when negative). Hence

2W_h <= z_h^2-z_h+h(h+1).

Finally,

sum_{h=1}^{H0} z_h = sum_u min(rho_u,H0) <= r.

The maximum-demand source bound and the nested residual budget are separate requirements; neither is inferred from the quadratic capacity inequality alone.

## 5. Individual profile projection

For h<=H0 put ell=|I_h| and p=ell/a. For i in I_h the radicand 2a*s_i-h^2 is positive: 1<=h<=s_i<=a-1. Cauchy gives

[(1/a) sum_{i in I_h} sqrt(2a*s_i-h^2)]^2
 <= 2pW_h-p^2 h^2
 <= p*z_h^2+p(1-p)h^2
 <= z_h^2.

The middle inequality uses z_h>=h to drop -z_h+h from the exact capacity bound. The final gap is (1-p)(z_h^2-p*h^2)>=0. Taking nonnegative roots and summing yields

r >= (1/a) sum_i sum_{h=1}^{s_i} sqrt(2a*s_i-h^2).

If H0=0 all sums are empty and the assertion is simply r>=0.

The subsequent shifted-midpoint integral estimate and rational scalar certificates are analytic dependencies, distinct from this reconstructed graph bridge. They retain their separately audited scope and need a>=1.

## 6. Audit disposition

No blocking flaw was found in the raw graph bridge. Every argument works for every maximum-degree root and every legal choice of selected quasi-edges. The residual-or-selected supplement dichotomy is essential.

The newly identified a=0 statement defect is repaired by a domain restriction; it does not change the separately assembled 7/12 or 250/429 candidate threshold claims. Those claims remain internally reviewed, not externally established.

Actual-graph regression must now check the constructed objects and injections under multiple legal selections. It must separately report zero-demand and positive-demand cases, because all-zero controls do not exercise the source-demand or heavy-threshold arguments.
