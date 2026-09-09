---
title: "A layer-sum residual bound for diameter-2 edge-critical graphs"
subtitle: "Reviewer edition 1 - retained candidate general structural theorem"
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
We present the retained candidate layer-sum argument yielding a cubic residual inequality, its resulting surplus bound, and the rational maximum-degree threshold 13/22. The result remains useful structural history even though later profile-integral arguments improve the threshold. Independent mathematical review remains open.
\end{abstract}

**Reviewer status.** retained candidate hand proof; independent mathematical review OPEN. This reviewer edition is an editorial rendering of the canonical source proof listed below. It does not convert same-assistant checking into external independence, does not make a novelty or priority claim, and does not claim the unrestricted Murty-Simon conjecture unless the source proof itself proves such a statement.

**Canonical claim.** `n >= 6 and Delta(G) >= (13/22)n imply e(G) < floor(n^2/4)`.

**Canonical proof source.** `project/research/general_n/2026-09-08-layer-sum-v1/PROOF.md`. The source is reproduced in full below; substantive mathematical changes must be made in the canonical proof first and then rebuilt into this edition.

---

# A layer-sum residual bound for diameter-two edge-critical graphs

8 September 2026. Paul Lenz: research direction. ChatGPT/Geeps: mathematical development, code, drafting and internal checks.

**Status: candidate hand proof; finite internal checks REPRODUCED; independent mathematical review OPEN.** This is not a certified replacement for a frozen finite-order proof, a novelty determination, or a solution of the whole Murty-Simon conjecture. A local quasi-edge/edge-insertion slice is checked in Lean 4.19.0; the threshold-capacity counting lemma, layer sum and 13/22 consequence are not formally verified.

## Main statements

Let G be a finite simple diameter-two edge-critical graph. Write n=|V(G)|, m=e(G), b=Delta(G), a=n-1-b, and t=m-b(n-b). In the minimum-complement-degree selected/residual construction below, write r for the number of residual cross-edges and S for the sum of minimum label demands.

For a>=1, the candidate inequalities are

    3 S^3 <= a^2 r(2r+1),                         (1)
    t < (4/81)a^2 + 1/8.                         (2)

They imply the following exact rational degree threshold:

    n>=6 and Delta(G)>=13n/22  ==>  m<floor(n^2/4).  (3)

Here 13/22=0.59090909... . Lowering the threshold enlarges the maximum-degree range covered, but the middle-degree range remains open. The qualification n>=6 is essential for a strict conclusion at this coefficient: K(2,3) has n=5, Delta=3>=65/22 and m=6=floor(25/4).

The new step is to sum the already derived threshold capacity over *all* demand levels using their common residual budget. The exact integer correction in that capacity yields (1). The older charging-deficit theorem, its numerical constants and its large-a cutoff are not dependencies of this proof.

## 1. Graph-to-selected-system construction

Put H=complement(G). An adjacent total dominating pair in H is equivalent to a pair at distance greater than two in G: its two endpoints are nonadjacent in G and have no common G-neighbour. Thus H has no such pair. For every missing edge uw of H, criticality of G gives such a pair in H+uw.

Choose v of minimum H-degree. Set A=N_H(v), B=V(H) minus N_H[v]. Then |A|=a and |B|=b. For any missing pair uw in H[B], both u and w miss v, so {u,w} cannot be the new total dominating pair. A pair avoiding both u and w has unchanged domination. Hence there is an existing edge ui, or its reverse orientation wi, whose open H-neighbourhoods cover every vertex except w (respectively u). Its auxiliary i lies in A to dominate v. Write ui->w and call w the supplement.

Choose exactly one such cross-edge for every missing unordered B-pair. Distinct pairs give distinct selected cross-edges because the B-endpoint and unique exception recover the pair. At each source, labels and supplements are each distinct. Every unordered B-pair carries at most one selected arc. All other existing H[A,B] edges are residual.

Let rho_u be residual degree at u in B, R_i residual degree at i in A, and let r be their common sum. Put F=complement(H[A]), d_i=deg_F(i). Let x_i count actual selected edges at label i, and set

    s_i=max(0,d_i-R_i),    S=sum_i s_i.

The selected cross-edges and the existing edges of H[B] together number binom(b,2). Counting the remaining edges of H gives

    e(F)=r+t,    sum_i d_i=2(r+t),    sum_i R_i=r.       (4)

Also deg_H(i)=a-d_i+R_i+x_i>=a by the choice of v. Consequently

    x_i>=s_i,    0<=s_i<=a-1,    S>=r+2t.             (5)

An actual selected degree x_i need not equal its minimum demand s_i.

## 2. Two local facts

**Source demand.** If ui->w is selected, then d_i<=rho_u+R_i and hence s_i<=rho_u.

For every F-neighbour j of i, domination by ui forces uj to be an H-edge. At most rho_u of these edges are residual. Every other uj is selected and has a distinct supplement w_j different from w. Since ui dominates w_j and u misses w_j, iw_j exists. It is residual: both i and w_j miss j in A, whereas a selected edge has its unique exception in B. The distinct supplements therefore inject the remaining F-neighbours into residual edges at i.

**Supplement adjacency.** If ui->w is selected, w neighbours every other selected label at u. Indeed a different selected uj has a different exception, so it must dominate w; u misses w, forcing jw.

These arguments use neither positive surplus nor residual activity. The counting below uses all actual selected heavy incidences, not a replacement x_i=s_i.

## 3. Exact threshold capacity

For an integer h>=1 define

    I_h={i:s_i>=h},    Z_h={u:rho_u>=h},
    W_h=sum_{i in I_h} s_i,    z_h=|Z_h|.

Every selection of a label in I_h has its source in Z_h. A vertex outside Z_h selects no heavy label, so all its neighbours in I_h are residual, and there are at most h-1 of them.

Let ell_u count actual heavy selections at source u. If ell_u>h, every heavy selection there has its supplement inside Z_h: that supplement must neighbour the other ell_u-1>=h heavy labels. Let j sources have ell_u>h. The other z_h-j sources contribute at most (z_h-j)h heavy selections. Heavy arcs from the j sources occupy distinct unordered pairs in Z_h incident with those sources, of which there are at most

    j(z_h-j)+binom(j,2)=j z_h-j(j+1)/2.

Therefore

    W_h <= (z_h-j)h + j z_h-j(j+1)/2.                (6a)

If W_h>0, a heavy label has s_i>=h and x_i>=s_i, so it is incident with at least h distinct selected cross-edges and hence at least h distinct sources. Source demand puts those sources in Z_h, giving z_h>=h.

Now put q=z_h-h>=0. There is no approximation or continuous optimisation in the remaining step. Subtracting the right side of (6a) from the proposed bound gives the exact integer identity

    h z_h + binom(q,2)
      - [(z_h-j)h + j z_h-j(j+1)/2]
      = (q-j)(q-j-1)/2 >= 0.                         (6b)

The last inequality holds for every integer q-j because the product of two consecutive integers is nonnegative. Equality is possible only when j=q or j=q-1. Thus

    W_h <= h z_h + binom(z_h-h,2),
    2W_h <= z_h^2-z_h+h(h+1).                       (6)

If z_h<h, then W_h=0 by the preceding distinct-source argument. In particular W_h<=z_h^2 in all cases.

This proof exposes exactly where both structural premises enter: (i) a source with more than h heavy selections may use only supplements in Z_h, and (ii) each unordered B-pair supports at most one selected orientation. Dropping either premise admits explicit abstract counterexamples. A separate adversarial checker enumerates marked partial orientations and includes both failures as negative controls.

## 4. Summing the demand levels

If S=0, (1) is immediate and (5) gives t<=0, so (2) holds. Assume S>0, and let H0=max_i s_i>=1. This H0 is the maximum *demand*, not the maximum residual degree.

A label of demand H0 has at least H0 selected sources, each of residual degree at least H0. Thus

    z_h>=H0 for 1<=h<=H0,    H0^2<=r.

Write r0=sum_{h=1}^{H0} z_h<=r and L=sum_{h=1}^{H0} sqrt(W_h). Counting each demand once per level gives

    sum_h W_h=sum_i s_i^2.

Because W_h<=S, and by Cauchy-Schwarz on the a demands,

    S^2 <= a sum_i s_i^2 = a sum_h W_h <= a sqrt(S) L.

Therefore

    S^3 <= a^2 L^2.                                 (7)

A second, weighted Cauchy-Schwarz inequality gives

    L^2 <= r0 sum_h W_h/z_h.

All denominators here are positive. Divide (6) by z_h, sum, and use z_h>=H0:

    2 sum_h W_h/z_h
      <= r0-H0 + sum_{h=1}^{H0} h(h+1)/z_h
      <= r0-H0 + (H0+1)(H0+2)/3
       = r0+(H0^2+2)/3.

Here sum_{h=1}^{H0} h(h+1)=H0(H0+1)(H0+2)/3. Hence

    2 L^2 <= r0 [r0+(H0^2+2)/3]
           <= r [r+(r+2)/3].

Equivalently, 3L^2<=r(2r+1). Combining with (7) proves (1).

For comparison, discarding the integer correction in (6) and using only W_h<=z_h^2 gives the weaker S^3<=a^2 r^2. That was the first intermediate result of this session; it is not the final bound.

## 5. A quadratic bound on surplus

Equation (1) implies

    (r+1/4)^2 >= (3/2) S^3/a^2 + 1/16,
    r > sqrt(3/2) S^(3/2)/a - 1/4.

Let K=sqrt(3/2) and u=K sqrt(S)/a. From (5),

    2t <= S-r < (a^2/K^2) u^2(1-u) + 1/4.

For every u>=0,

    4/27-u^2(1-u) = (u-2/3)^2(u+1/3) >= 0.

Since K^2=3/2, this gives t<4a^2/81+1/8. Together with the S=0 case, (2) holds for every a>=1. There is no large-a hypothesis.

## 6. The degree consequence and small cases

A universal vertex forces an edge-critical graph to be a star: any edge between other vertices would be redundant. This gives m=n-1<floor(n^2/4) for n>=4. Hence assume a>=1.

Suppose b>=13n/22 and m>=floor(n^2/4). Then b-n/2>=2(n-b)/9=2(a+1)/9. Accounting for parity,

    t >= (b-n/2)^2-1/4 >= (4/81)(a+1)^2-1/4.        (8)

For a>=4 the last expression exceeds 4a^2/81+1/8, because

    (4/81)(2a+1) >= 4/9 > 3/8.

This contradicts (2). For a=2, the degree premise forces b>=5; for a=3 it forces b>=6. The exact integer identity

    floor(n^2/4)-b(n-b)=floor((b-a-1)^2/4)

then gives t>=1 in both cases, whereas (2) gives respectively t<16/81+1/8<1 and t<36/81+1/8<1.

For a=1 and n>=6, b=n-2>=4, so the same identity gives t>=1. But F has one vertex, and (4) gives t=-r<=0. This proves (3) for all n>=6.

At n=4 the degree premise forces a star, so strictness also holds. At n=5 it permits K(2,3), and a strict all-n>=4 statement would be false. No such statement is claimed.

## 7. Audit scope, evidence and dependencies

The default replay rebuilds all 33,864 labelled simple graphs with 3<=n<=6. Two separately implemented criticality tests agree on every one. The 608 critical graphs yield 920 selected systems when all maximum-degree roots and all quasi-edge selections are included. Ten saved atlas-derived seven-vertex graphs supply another 32 systems, and 40 deterministic greedy graph samples on 8, 10, 12, 16 and 20 vertices supply 107 systems. Larger graph samples use the first and last available selections, not all choices.

All 1,059 checked systems pass the graph construction, residual injections, exact threshold count, layer identities, (1) and (2). The run makes 2,119 threshold tests, but only 13 have nonempty demand tails, from 12 systems. No positive-surplus graph occurs. This is an important limitation: the samples do not test the dense contradiction nonvacuously. The 2,353 abstract demand multisets and 10,200 scalar-identity cases test algebra, not graph realisability. Missing, duplicate and self-supplement selections are rejected. K(2,3) is an explicit negative control for overbroad small-order strictness.

The inherited continuation's separate regression also passes: 99 rounding cases, 2,550 integer maximisations and 1,728,186 admitted checks on 59,809 labelled oriented graphs. These are fresh executions in this response, not a recovery of earlier claimed execution results. A new independent adversarial threshold checker separately verifies the exact identity (6b), enumerates marked partial orientations with outside-Z endpoints, and confirms that removing either unordered-pair uniqueness or high-source confinement breaks the bound.

No complete new graph order, proof through n=1,000, full formal verification, independent researcher reproduction, literature priority or external endorsement is asserted. The source, output and authorship are internal to this project. Frozen n25/n27/n28 papers, original archives and the governed theorem ledger are unchanged.

**Independent-review priorities:** verify the heavy-supplement confinement and unordered-pair injection used in (6a); then verify the layer sum. The graph-to-quasi-edge bridge now has a checked local Lean slice, and the residual injection has separate computational assurance, but neither fact makes the global 13/22 statement externally verified.

**Research next step:** audit/formalise the graph-to-threshold reduction before optimising further. A later sharpening could retain the full residual-tail distribution instead of replacing r0 and H0^2 by r. There is no claim yet that this closes the middle-degree gap.

## Provenance and literature limits

The immediate project antecedent is `../2026-09-07-stability-spare-sources-v9/THRESHOLD_CAPACITY_CONTINUATION.md`, commit `f332e47ae4c32dd28ff0c7765130fff2770b20e0`, blob `c2a478de88c7bd68dc02fdface2f3458e40a189e`. Its two local facts and threshold lemma are reproved above. This proof does not depend on its 0.6129 arithmetic, Fan's estimate, a weak-core reduction, total-domination complement classification, or residual activity.

The fresh literature search located the author-institution record of Haynes et al., *A maximum degree theorem for diameter-2-critical graphs*, DOI 10.2478/s11533-014-0449-3, and the arXiv records 1812.08420 and 2409.17491. This was not an exhaustive novelty audit and establishes no best-known claim. The earlier v9 literature comparison, including its 2016-preprint caveat, is preserved rather than overwritten. No external theorem is used in the displayed derivation.
