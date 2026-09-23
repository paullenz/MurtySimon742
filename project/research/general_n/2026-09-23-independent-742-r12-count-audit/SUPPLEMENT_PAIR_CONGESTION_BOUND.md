# Supplement-pair congestion bound

23 September 2026. Status: **PROVED INTERNAL STRUCTURAL LEMMA; DEGREE-ONLY RELAXATION INSUFFICIENT**.

Let v be a maximum-degree root, B=N(v), |B|=b=Delta, and A=V(G)\(B union {v}), |A|=a. Fix one legal endpoint-label selection on the G[B]-edges. For a physical source u in B, let S_u be the labels selected at u, and for i in S_u let sigma_u(i) in B be its supplement. At a fixed source the supplement map is injective.

For every co-selected F-edge {i,k} subset S_u (with F=G[A]), define its unordered supplement-pair image

Phi(u,{i,k})={sigma_u(i),sigma_u(k)}.

## Lemma 1: exact congestion charge

For p,q in B, let M_{pq} be the number of co-selected F-edge occurrences whose supplement-pair image is {p,q}. Then

M_{pq} <= |N_{G[B]}(p) intersect N_{G[B]}(q)|.

Proof. If Phi(u,{i,k})={p,q}, then the two selected certificates use the distinct G[B]-edges up and uq, so u is adjacent in G[B] to both p and q. For a fixed source u and a fixed unordered pair {p,q}, injectivity of sigma_u determines at most one unordered label pair {i,k}. Hence distinct occurrences counted by M_{pq} give distinct common B-neighbours u of p and q. QED.

Consequently, with

C = sum_{u in B} e(F[S_u]),

we have the exact global bound

C = sum_{p<q} M_{pq}
  <= sum_{p<q} |N_B(p) intersect N_B(q)|
  = sum_{u in B} binom(d_{G[B]}(u),2).

This is a genuine cross-source reuse bound: collisions are charged to B-two-paths rather than treated sourcewise.

## Lemma 2: maximum-degree/profile form

Write q_u=|N_H(u) intersect A| for the number of A-labels nonadjacent to u (selected plus residual). Since v is adjacent to u and v has maximum degree b,

1 + d_{G[B]}(u) + d_G(u,A) <= b,

while d_G(u,A)=a-q_u. Therefore

d_{G[B]}(u) <= b-a-1+q_u = 2b-n+q_u.

Thus

C <= sum_{u in B} binom(b-a-1+q_u,2).

Inside the unresolved strip b/n<250/429, using n=a+b+1 gives

b-a-1 < (71/179)(a+1),

so

C < sum_{u in B} binom(q_u + (71/179)(a+1),2).

The bound keeps the source H-loads q_u and therefore is stronger than a bare multiplicity constant.

## Weighted consequence and limit

For the occurrence-weighted F-codegree sum T used by the robust plateau argument, trivially c_F(i,k)<=a-2, hence

T <= (a-2) C
  <= (a-2) sum_{u in B} binom(d_{G[B]}(u),2).

However, the existing endpoint cap q_u<=c a with c=6771/16000 and the worst live-strip ratio b/a -> 250/179 yield the leading degree-only coefficient

(1/2)(250/179)(250/179 - 1 + 6771/16000)^2
 = 5513146264081/11745974272000
 = 0.4693647488... .

The current robust lower coefficient for T is 31640625/5664582488 = 0.0055856941..., so this degree-only relaxation is still larger by a factor 84.03. Therefore the new congestion lemma is structurally valid but cannot close the plateau after replacing the actual B-two-path distribution by only the maximum-degree and q_u endpoint caps.

A fresh replay on 62 independently generated/certified live-strip maximum-degree roots (n=17..28, 40 seeds/order) checked the deterministic-selection instance C<=sum binom(d_B,2)<=sum binom(b-a-1+q_u,2) with zero violations. This is regression evidence, not part of the proof.

## Route consequence

Do not return to unrestricted injectivity: the companion live-strip search already finds 13 collisions. The useful theorem-level target is now to combine positive-demand inequalities with the **distribution** of B-two-path capacity, rather than its crude maximum-degree envelope. Any successful improvement must show that high-demand co-selected F-edge occurrences are forced onto a substantially smaller subset of the available B-two-path capacity, or that their supplement-pair congestion itself forces extra residual charge.
