---
title: "A profile-integral maximum-degree bound for diameter-2 edge-critical graphs"
subtitle: "Reviewer edition 1 - candidate general structural theorem"
author: "Paul Lenz research project; mathematical development and drafting with ChatGPT/Geeps"
date: "9 September 2026"
documentclass: article
fontsize: 11pt
geometry: [a4paper, margin=25mm]
colorlinks: true
linkcolor: "black"
urlcolor: "blue"
---

\begin{abstract}
We present the current candidate profile-integral argument proving the profile-integral surplus bound in the selected/residual framework and deriving an exact rational maximum-degree threshold which, for orders at least six, forces a strict improvement over the balanced complete-bipartite edge bound. The argument is a general structural candidate rather than a proof of the unrestricted Murty-Simon conjecture. Its finite integer checks are retained and replayed internally; independent mathematical review and novelty assessment remain open.
\end{abstract}

**Reviewer status.** complete candidate hand argument; independent review and novelty assessment OPEN. This reviewer edition is an editorial rendering of the canonical source proof listed below. It does not convert same-assistant checking into external independence, does not make a novelty or priority claim, and does not claim the unrestricted Murty-Simon conjecture unless the source proof itself proves such a statement.

**Canonical claim.** `n >= 6 and Delta(G) >= (293/500)n imply e(G) < floor(n^2/4)`.

**Canonical proof source.** `project/research/general_n/2026-09-08-profile-integral-v1/PROOF.md`. The source is reproduced in full below; substantive mathematical changes must be made in the canonical proof first and then rebuilt into this edition.

---

# A profile-integral bound and the 293/500 maximum-degree candidate

8 September 2026. Paul Lenz: research direction. ChatGPT/Geeps: derivation, software, drafting and internal audit.

**Status: complete candidate hand argument with explicit finite integer certificates. Internal computations REPRODUCED; independent mathematical review and novelty assessment OPEN. Not PROJECT-CERTIFIED, not a full Lean proof, and not a solution of the unrestricted Murty-Simon conjecture.**

## Statement and scope

Let G be a finite simple diameter-two edge-critical graph, with n vertices, m edges and maximum degree b. Put a=n-1-b and t=m-b(n-b). The argument below gives, for a>=1,

    t < a^2/24 + a/8.                                      (P)

Together with explicitly bounded small cases, it gives the candidate implication

    n>=6 and b >= (293/500)n  ==>  m < floor(n^2/4).         (T)

Here 293/500=0.586 exactly. The strict statement cannot be extended to all n>=4: K(2,3) has n=5, b=3 and m=6=floor(25/4), while 3>=293*5/500.

This completes the previously unfinished 0.586 route. The original Jensen step is valid, but unnecessary: a pointwise scalar bound can be summed directly. The proof also avoids dependence on the older cubic residual inequality or its 4/81 coefficient. It does depend on the graph-to-demand construction and exact threshold count, which are rederived below. No positive-surplus graph is assumed to exist or found by this work.

## 1. Graph-to-demand construction

Write H for the complement of G. An adjacent total-dominating pair in H is a pair nonadjacent in G with no common G-neighbour. Thus H has none; inserting any missing H-edge creates one, by edge-criticality of G.

Choose v of minimum H-degree a and put A=N_H(v), B=V(H) minus N_H[v], so |A|=a and |B|=b. Insert a missing pair uw inside H[B]. A newly created adjacent total-dominating pair must use u or w: otherwise neither its adjacency nor its neighbourhood union changed. The pair {u,w} itself misses v. Consequently a new pair uses exactly one endpoint, say u, and another vertex i. Its edge ui already existed. To dominate v it must have i in A. Before insertion its open H-neighbourhood union was exactly V(H) minus {w}; otherwise it would already have totally dominated H. In particular, both u and i miss w. Denote this quasi-edge by ui->w.

Choose one such cross-edge for each missing unordered B-pair. Two distinct missing pairs cannot yield the same selected cross-edge: its B-endpoint and its unique undominated vertex recover the pair. At a fixed source, selected labels and supplements are separately distinct. Every unordered B-pair carries at most one selected orientation. All remaining H[A,B] edges are called residual.

Let rho_u and R_i be residual degrees at u in B and i in A, respectively, with common total r. Put F=complement(H[A]), d_i=deg_F(i), and let x_i be the number of actual selections at label i. Define

    s_i=max(0,d_i-R_i),    S=sum_i s_i.

The selected cross-edges together with H[B] account for binom(b,2) edges. Counting H gives

    e(F)=r+t,    sum_i d_i=2(r+t),    sum_i R_i=r.

Minimum H-degree gives a-d_i+R_i+x_i>=a. Hence

    0<=s_i<=a-1,    x_i>=s_i,    S>=r+2t.                (1)

The use of actual selections is essential: x_i is not replaced by s_i.

### Source demand and supplement forcing

If ui->w is selected, every F-neighbour j of i forces an H-edge uj. At most rho_u such edges are residual. Each other uj is selected, with a distinct supplement w_j different from w. Since ui dominates w_j and u misses w_j, iw_j is an H-edge. It must be residual: i and w_j both miss j in A, whereas a selected cross-edge has its unique exception in B. Distinct supplements give an injection of these remaining F-neighbours into residual edges at i. Thus

    d_i<=rho_u+R_i,    and so    s_i<=rho_u.             (2)

Also, the supplement w of ui->w neighbours every other selected label j at source u. The quasi-edge uj has a different exception and must dominate w, while u misses w.

## 2. Exact threshold capacity

For h>=1 set

    I_h={i:s_i>=h},  W_h=sum_{i in I_h}s_i,
    Z_h={u:rho_u>=h},  z_h=|Z_h|.

Every actual heavy selection has its source in Z_h by (2). A source outside Z_h selects no heavy label; hence all its heavy-label neighbours are residual, and it has at most h-1 of them.

If a source has ell_u>h actual heavy selections, the supplement of each such selection neighbours its other ell_u-1>=h distinct heavy labels. Such a supplement must lie in Z_h. Let J be these high-load sources and j=|J|. Their heavy arcs use distinct unordered pairs inside Z_h incident with J; there are

    j(z_h-j)+binom(j,2)=j*z_h-j(j+1)/2

such pairs. The other z_h-j sources have at most h heavy selections each. Therefore

    W_h <= sum_{u in Z_h}ell_u
        <= (z_h-j)h+j*z_h-j(j+1)/2.

When W_h>0, a heavy label needs at least h distinct selected sources, so z_h>=h. With q=z_h-h, the gap from the last bound to h*z_h+binom(q,2) is exactly (q-j)(q-j-1)/2, nonnegative for every integer q-j. Thus

    2W_h <= z_h^2-z_h+h(h+1).                           (3)

If W_h=0 the pointwise argument below is empty. If H0=max_i s_i>0, a label of demand H0 needs H0 distinct sources of residual degree at least H0. Consequently

    z_h>=H0>=h  (1<=h<=H0),    sum_{h=1}^{H0}z_h<=r.    (4)

No graph-wide residual-activity assumption or weak-core reduction is used.

## 3. Retaining the individual demand profile

For h<=H0 let ell=|I_h| and p=ell/a. Every radicand below is positive, since h<=s_i<=a-1. Cauchy-Schwarz gives

    [(1/a) sum_{i in I_h} sqrt(2a*s_i-h^2)]^2
      <= (ell/a^2)(2a*W_h-ell*h^2)
       = 2p*W_h-p^2*h^2.

By (3) and z_h>=h, 2W_h<=z_h^2+h^2. Since 0<=p<=1 and z_h>=h,

    2p*W_h-p^2*h^2
      <= p*z_h^2+p(1-p)h^2
      <= z_h^2.

The last gap is (1-p)(z_h^2-p*h^2)>=0. Taking nonnegative square roots proves

    z_h >= (1/a) sum_{i:s_i>=h} sqrt(2a*s_i-h^2).       (5)

Summing (5) and interchanging finite sums, using the shared budget (4), yields

    r >= (1/a) sum_i D_a(s_i),
    D_a(s)=sum_{h=1}^s sqrt(2a*s-h^2).                 (6)

The source lower bound z_h>=h is indispensable. Inequality (3) by itself would not justify (5).

## 4. A rigorously directed sum-to-integral estimate

Define

    Phi(x)=integral from 0 to x of sqrt(2x-y^2) dy,  0<=x<=1.

We claim, for integer 0<=s<=a-1,

    D_a(s) >= a^2*Phi(s/a)-a/4.                        (7)

The case s=0 is immediate. Otherwise a>=2, s>=1. Let f(x)=sqrt(2a*s-x^2) on [0,s+1/2]. This interval is inside the radicand's nonnegative domain, since

    2a*s-(s+1/2)^2-s^2
      =2s(a-s)-s-1/4 >= s-1/4 > 0.

The function is decreasing and concave. For every integer h=1,...,s, midpoint concavity gives

    f(h) >= integral from h-1/2 to h+1/2 of f(x) dx.

For completeness, integrate f(h-u)+f(h+u)<=2f(h) for 0<=u<=1/2. Thus D_a(s)>=integral from 1/2 to s+1/2 of f. The difference between the desired integral over [0,s] and this shifted integral is at most

    [f(0)-f(s+1/2)]/2
       <= [sqrt(2a*s)-s]/2
       <= a/4.

The middle inequality uses f(s+1/2)>=s, already proved. The final inequality follows from

    (s+a/2)^2-2a*s=(s-a/2)^2>=0.

Finally, the substitution x=a*y gives integral_0^s f(x) dx=a^2*Phi(s/a), proving (7). In particular, we do NOT incorrectly assert that a decreasing right-endpoint sum is above its unshifted integral; the shift and endpoint correction are essential.

Summing (7) in (6) gives

    r >= a sum_i Phi(s_i/a)-a/4.                       (8)

## 5. An elementary scalar certificate; Jensen is not needed

We prove the uniform strict bound

    x-Phi(x) < 1/12,    0<=x<=1.                       (9)

For 0<=u<=1,

    sqrt(1-u) >= 1-u/2-u^2/2.

Indeed B=1-u/2-u^2/2=(1-u)(1+u/2)>=0, and

    (1-u)-B^2=u^2(1-u)(u+3)/4>=0.

For x>0, apply this with u=y^2/(2x) and integrate from 0 to x:

    Phi(x)>=sqrt(2x)*(x-x^2/12-x^3/40).

Put q=sqrt(x/2), so 0<=q<=1/sqrt(2). It suffices to bound

    P(q)=2q^2-4q^3+(2/3)q^5+(2/5)q^7.

If 0<=q<=1/2, then

    P(q)<=2q^2-(457/120)q^3.

For c=457/120, the exact factorisation

    32/(27c^2)-(2q^2-cq^3)
      = c*(q-4/(3c))^2*(q+2/(3c)) >= 0

gives

    P(q)<=51200/626547<1/12,
    1/12-51200/626547=4049/2506188>0.

If 1/2<=q<=1/sqrt(2), use q^2<=1/2 and q^4<=1/4 to obtain

    P(q)<=2q^2-(107/30)q^3.

The last cubic is decreasing for q>=1/2, since its derivative is q*(4-107q/10)<0. Its value at 1/2 is 13/240<1/12. This proves (9), including x=0 directly. Both rational margins are positive; no numerical optimiser or approximate integral is used.

Using (8) and summing (9) gives

    r > S-a^2/12-a/4.

Combining with 2t<=S-r from (1) proves (P).

### Check of the originally proposed Jensen step

For 0<x<=1,

    Phi(x)=(x/2)*sqrt(2x-x^2)+x*arcsin(sqrt(x/2)),
    Phi'(x)=sqrt(x(2-x))+arcsin(sqrt(x/2)),
    Phi''(x)=(3/2-x)/sqrt(x(2-x))>0.

Continuity at zero makes Phi convex on [0,1], so finite Jensen with weights 1/a is valid. It would give r>=a^2*Phi(S/a^2)-a/4. However, (9) can be summed directly, making Jensen and these derivative formulae optional rather than dependencies of (T). This removes a potential proof obligation without changing the requested coefficient.

## 6. Exact degree assembly for a>=31

Suppose n>=6, b>=293n/500 and m>=floor(n^2/4). Since n=a+b+1,

    b-n/2 >= (43/207)(a+1),
    t >= (b-n/2)^2-1/4.

Therefore the difference between this lower bound on t and (P)'s upper bound is at least

    D(a)=(43/207)^2*(a+1)^2-1/4-a^2/24-a/8.

Its quadratic coefficient is 509/342792>0. Direct rational arithmetic gives

    D(31)=1757/85698>0,
    D(32)-D(31)=9401/171396>0.

All subsequent forward differences increase by twice the positive quadratic coefficient. Thus D(a)>0 for every integer a>=31, contradicting (P).

## 7. Small a, without the older cubic inequality

For a=0, G has a universal vertex and edge-criticality forces a star: any edge between other vertices could be deleted without losing diameter two. Thus m=n-1<floor(n^2/4) for n>=6. For a=1, F is edgeless and t=-r<=0; the degree premise with n>=6 gives a strictly positive required t.

For 2<=a<=30 define

    b0=ceil(293(a+1)/207),
    T0=floor((b0-a-1)^2/4).

The exact identity floor(n^2/4)-b(n-b)=floor((b-a-1)^2/4) incorporates parity. Since b>=b0>a+1, the required t is nondecreasing in b. The table in Appendix A shows 24*T0>=a^2+3a for every such a except 6 and 11. Those ordinary cases contradict the strict inequality (P).

For the two exceptions we give a small finite integer certificate derived only from (3)-(4). Write H0=max s_i>0 and fix S. For each 1<=h<=H0, let k_h be the number of demands at least h. Since

    S <= k_h*H0+(a-k_h)(h-1),

we have

    K_h=max(1,ceil((S-a(h-1))/(H0-h+1))) <= k_h.

Consequently

    W_h >= w_h=max(H0,h*K_h,S-(a-K_h)(h-1)).

Let L_h be the least integer z>=H0 satisfying z^2-z+h(h+1)>=2w_h. The function z(z-1) is increasing on integers z>=1, so (3)-(4) imply z_h>=L_h and r>=sum_h L_h. It follows that

    S-r <= S-sum_h L_h.                                (10)

For fixed a, there are only 1<=H0<=a-1 and H0<=S<=a*H0 to check. Direct integer evaluation of (10) gives the following row maxima:

| H0 | a=6: maximum upper bound on S-r | a=11: maximum upper bound on S-r |
|---:|---:|---:|
| 1 | 2 | 6 |
| 2 | 1 | 8 |
| 3 | 0 | 7 |
| 4 | -2 | 7 |
| 5 | -7 | 4 |
| 6 | not applicable | 1 |
| 7 | not applicable | -4 |
| 8 | not applicable | -10 |
| 9 | not applicable | -18 |
| 10 | not applicable | -27 |

This is 80 (H0,S) cases for a=6 and 560 for a=11, with 290+3,905=4,195 threshold evaluations. The function `small_certificate` in the supplied standard-library checker reproduces the table using direct integer iteration; it does not call the square-root inversion used by the larger profile audit. The case S=0 gives t<=0 separately.

Thus a=6 gives t<=1, whereas b0=10 requires t>=2. And a=11 gives t<=4, whereas b0=17 requires t>=6. These close the two exceptions and finish (T).

In particular, n=29 and Delta=17 is excluded from attaining 210 edges by this candidate argument. This does NOT resolve n=29 at all maximum degrees or establish a whole-order n=29 theorem.

## Appendix A. Finite degree comparison

The final column is 24*T0-a^2-3a. Nonnegative values suffice because (P) is strict. The two negative rows use (10) instead.

| a | b0 | T0 | 24*T0-a^2-3a |
|---:|---:|---:|---:|
| 2 | 5 | 1 | 14 |
| 3 | 6 | 1 | 6 |
| 4 | 8 | 2 | 20 |
| 5 | 9 | 2 | 8 |
| 6 | 10 | 2 | -6 |
| 7 | 12 | 4 | 26 |
| 8 | 13 | 4 | 8 |
| 9 | 15 | 6 | 36 |
| 10 | 16 | 6 | 14 |
| 11 | 17 | 6 | -10 |
| 12 | 19 | 9 | 36 |
| 13 | 20 | 9 | 8 |
| 14 | 22 | 12 | 50 |
| 15 | 23 | 12 | 18 |
| 16 | 25 | 16 | 80 |
| 17 | 26 | 16 | 44 |
| 18 | 27 | 16 | 6 |
| 19 | 29 | 20 | 62 |
| 20 | 30 | 20 | 20 |
| 21 | 32 | 25 | 96 |
| 22 | 33 | 25 | 50 |
| 23 | 34 | 25 | 2 |
| 24 | 36 | 30 | 72 |
| 25 | 37 | 30 | 20 |
| 26 | 39 | 36 | 110 |
| 27 | 40 | 36 | 54 |
| 28 | 42 | 42 | 140 |
| 29 | 43 | 42 | 80 |
| 30 | 44 | 42 | 18 |

## Audit, dependencies and provenance

The starting repository checkpoint was `8e676ae8fac0a7894c649e797a58124ad5a1062d`. The graph-to-threshold antecedent is `../2026-09-08-layer-sum-v1/PROOF.md`, blob `019bf9377d548aaf2990289752c307790149eadb`, with its separate construction, residual-injection and threshold audits. Those arguments are rederived here, not assumed true merely because earlier tests passed. The earlier 13/22 proof, numerical constants and finite-order papers are not changed.

The fresh exact audit examines 478,192 sorted demand profiles through a=11 and 4,215,632 associated threshold levels; 833,250 rational midpoint identities; the 640-case small certificate above; and 5,173,536 degree pairs satisfying the proposed ratio with 6<=n<=5,000. The full output, parameters and execution environment are saved with the source. These are abstract systems, not actual critical graphs. Some abstract profiles allow positive S-r; none is claimed graph-realisable. The finite degree sweep is not a proof of all graphs through 5,000; the universal degree argument is Sections 6-7.

The checker verifies exact identities and integer consequences, not the full calculus or all graph-theoretic steps in a proof assistant. The new result is NOT formally verified. Earlier local Lean lemmas cover only explicitly scoped quasi-edge logic. Independent specialist review, external researcher reproduction and literature priority remain OPEN. No solver UNSAT claim or external endorsement is made.

An official primary documentation cross-check of the optional Jensen statement is Mathlib's `Analysis.Convex.Jensen`, in particular `ConvexOn.map_sum_le`. The required equal weights are nonnegative and sum to one, and all s_i/a lie in the proved convexity interval. That documentation is not a formal check of this manuscript. No new best-known literature claim is made.
