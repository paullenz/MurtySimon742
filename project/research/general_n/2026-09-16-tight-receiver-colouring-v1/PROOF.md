# Tight-receiver colouring and residual-capacity amplification

16 September 2026. Research directed by Paul Lenz; internal mathematical development by ChatGPT/Geeps.

**Status: WIP_INTERNAL_PROOF_NOT_PROMOTED.** A bounded symbolic continuation from `8d9d932620ea02ea69193202924f45ed35d77eb6`. This is a conditional derivation using the full canonical graph-to-selected/residual bridge, not merely its numerical relaxation. Independent expert review is OPEN. No catalogue execution, new state exclusion, or unrestricted Murty-Simon proof is claimed.

## 1. Exact assumptions and notation

Use the canonical bridge at the inspected commit, with original graph G, its complement J, the A-side graph F=complement(J[A]), and a=|A|. Write delta_i=deg_F(i), R_i for the total residual B-degree of label i, and

    s_i=max(0,delta_i-R_i).

At each B-vertex u, N_u=S_u disjoint-union R_u, with |R_u|=rho_u. Here R_i is a number attached to an A-label; R_u is a set at a B-vertex. Every label i is selected at at least s_i distinct sources; selecting i at u requires s_i<=rho_u. The full selected system represents every missing unordered J[B]-pair exactly once. Each selected label has a destination; different selected labels at a source have different destinations; opposite orientations cannot both be selected.

For an actual obligation (u,i)->w, we use:

    i not in N_w;
    S_u minus {i} subset N_w;
    S_w subset N_u;
    every F-neighbour of i belongs to N_u.                 (P)

The last assertion is A-side quasi-edge domination (canonical Section 6.1). The reverse containment is the previously reviewed consequence of quasi-edge domination and unique selected orientation. Neither is an assumption about an arbitrary independently chosen scalar routing.

Fix d>=1 and define

    T={i:s_i=d}, H={u:rho_u>=d}, M={v:rho_v=d-1}, m=|M|.

Assume |T|=|H|=d. Set

    h=min_{u in H}rho_u,
    E=sum_{u in H}(|S_u|-d),
    K=(union_{t in T}N_F(t)) minus T, kappa=|K|.

The exact identity delta_t=d+R_t for t in T is ESSENTIAL below. It must not be silently supplied to a relaxation that has only s_t<=delta_t-R_t or arbitrary demand numbers.

## 2. Universal high residual set

Every tight label needs d selected sources and has exactly d eligible sources, H. Thus T subset S_u for every high u.

An extra high label j in S_u minus T must have a high destination: otherwise (P) would place all d labels of T in the destination's neighbourhood, all residual by eligibility, despite fewer than d residual slots.

Now let j in K. Some tight t is an F-neighbour of j. Since every high source selects t, A-side domination puts j in N_u at every high u. If any high source selected j, its destination would have to be high, where j is already present. This contradicts destination absence. Therefore

    K subset R_u for every u in H,                         (1)
    kappa <= h,
    delta_t <= (d-1)+kappa for every t in T,
    R_t <= kappa-1 for every t in T.                       (2)

This argument has NO receiver-count upper bound.

## 3. Used receivers carry a globally consistent tight label

For each u in H, let f_t(u) be the destination of its tight label t, and D_u={f_t(u):t in T}. These are d distinct vertices of M. Indeed a tight destination cannot be high, and it contains the other d-1 tight labels residually; consequently its residual set is exactly T minus {t}, and t itself is absent.

A used receiver cannot receive different tight labels from different high sources. Receiving t forces residual set T minus {t} and absence of t; receiving another tight label would contradict this. Thus the sets

    U_t={f_t(u):u in H}

are pairwise disjoint as t varies. Put c_t=|U_t|, U=union_t U_t, and ell=|U|=sum_t c_t. Each c_t is between 1 and d; U is the USED subset of M, not necessarily all of M.

For each t, every used receiver outside U_t carries t residually, so

    ell-c_t <= R_t <= kappa-1.                             (3)

Summing gives the new residual-capacity inequality

    (d-1)ell <= d(kappa-1) <= d(h-1).                      (4)

For d>=2 this bounds the used receiver pool:

    ell <= floor(d(kappa-1)/(d-1))
        <= floor(d(h-1)/(d-1)).                           (5)

A sharper version retaining F[T] is

    ell-c_t <= deg_{F[T]}(t)+|N_F(t) minus T|-d,
    (d-1)ell <= d*kappa+2e(F[T])-d^2.                     (6)

The coarser (4) follows using 2e(F[T])<=d(d-1). Since ell>=d, (4) also gives kappa>=d when d>=2.

## 4. Proper colouring: stronger than the anonymous disjoint-set reduction

Let Gamma have vertex set H, with uw an edge precisely when D_u and D_w are disjoint. The saved disjoint-destination lemma gives E<=e(Gamma), and for an actual graph G, E=e(G[H]) and G[H] is a subgraph of Gamma.

For completeness, the disjointness step is short. If extra j at u has high destination w and v belongs to both D_u and D_w, forward containment puts j in N_v. Since R_v is a subset of T, j is selected at v. Reverse containment at the tight obligation from w to v then puts j in N_w, contradicting destination absence. Distinct destinations and unique orientations inject extra obligations into unordered Gamma edges.

Fix ONE tight label t. Colour each high source u by its receiver f_t(u). Sources of the same colour share a receiver, hence cannot be adjacent in Gamma. This is a proper colouring with c_t colours. Therefore

    chi(Gamma) <= c := min_t c_t <= floor(ell/d).          (7)

Choose t with c_t=c. Then ell-c >= (d-1)c, while (3) bounds ell-c by kappa-1. For d>=2,

    chi(Gamma) <= c <= floor((kappa-1)/(d-1))
                         <= floor((h-1)/(d-1)).            (8)

In particular:

* If m<3d, then ell<3d, so Gamma and G[H] are BIPARTITE, not merely triangle-free.
* If h<3d-2 (equivalently h<=3d-3), the same bipartiteness follows WITHOUT any upper bound on m.
* If h<2d-1, Gamma is edgeless and E=0, again WITHOUT a receiver-count upper bound.

These are internal conditional strengthenings. The prior anonymous five-set C5 at d=5, m=13 remains a valid abstract set-family example, but it CANNOT be the tight-receiver system above: C5 needs at least three colours, so each of the five tight labels would need at least three distinct receivers, requiring ell>=15. Its former use as a limit on what the full labelled system might imply was too weak. No historical evidence is deleted, and no original-graph counterexample is claimed.

## 5. General edge and extra-label budgets

For d>=2 define the scalar bound

    q=min(d, floor(m/d), floor((h-1)/(d-1))).

Under the hypotheses q>=1. A proper colouring of Gamma uses at most q colours. If the colour-class sizes are n_1,...,n_q (allowing empty classes), then

    E <= e(Gamma) <= (d^2-sum_j n_j^2)/2.

The sum of squares is smallest for balanced sizes: moving one vertex from a class at least two larger than another reduces that sum. Write d=q*b+r with 0<=r<q. Thus

    E <= [d^2-r(b+1)^2-(q-r)b^2]/2.                       (9)

This is elementary complete-multipartite counting, not a newly claimed extremal theorem. In particular q=1 gives E=0 and q=2 gives E<=floor(d^2/4). Replacing h with kappa gives a potentially sharper bound when F is known.

There is also a receiver-independent budget using a. If E>0 then some disjoint pair D_u,D_w exists; each tight-label receiver class has at least two distinct members. Hence for every t, ell-c_t>=2(d-1), so (2)-(3) give

    E>0 implies kappa>=2d-1, hence rho_u>=2d-1 for ALL u in H.  (10)

Extra high selected labels must lie outside T union K, which has at most p=a-d-kappa remaining labels. Each such label is selected at at most d-1 high sources, since its high destination omits it. Therefore

    E <= (d-1)(a-d-kappa).                                (11)

If E>0 there must be at least one such label. Combining with (10) yields

    E>0 implies a>=3d,
    E <= (d-1)max(0,a-3d+1).                              (12)

Consequently a<3d forces E=0 for arbitrary m. At a=3d, E<=d-1. These are necessary bounds, not claims that the bounds are attained by original graphs. They may be combined with (9).

For d=1 there is only one high source; an extra label would need another high destination, impossible. Thus E=0 directly. No division by d-1 is used in that case.

## 6. Route rejected and audit boundaries

The predecessor's occurrence argument cannot simply be extrapolated with a slack allowance E. Let k=m-d. A demand outside T cannot exceed d-1: demand>d would require more than d eligible high sources, and demand=d is already in T. Thus when k>=d, the old condition s_i>e_L(i)+k is vacuous even before accounting for extra selections. The new argument instead uses actual F-neighbourhoods, the exact demand identity, and consistent receiver labels.

Critical dependencies for hostile review are (i) eligibility and all tight labels selected at all high sources, (ii) A-side quasi-edge domination, (iii) the high-destination and disjoint-destination arguments, (iv) the exact identity delta_t=d+R_t, and (v) the unique omitted tight label at every used receiver. The elementary colouring and counting do not replace review of those dependencies. Results for anonymous d-set families must not be substituted for results about consistently labelled receivers.

The new checks enumerate 50,755 necessary coloured receiver patterns for d=1,...,4, up to independent receiver renaming within each tight label, and test 19 boundary/negative controls. They validate the new incidence, colouring, and threshold steps only. They do not enumerate original diameter-two edge-critical graphs or run a catalogue verifier. The per-label extra-selection bound is proved symbolically above, not claimed established by these receiver-pattern checks.

## 7. Reproducible checks and exact sources

Run `python check_residual_capacity.py`; the full recorded output is `CHECK_RESULTS.json`. Source SHA256: `be8e2c5f2831c6afd9da9464c8df38fb673f8458965aa5e1f5032c28c8799af4`.

All dependencies below are read at immutable commit `8d9d932620ea02ea69193202924f45ed35d77eb6` in `paullenz/MurtySimon742`:

- `project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`, Sections 2, 3, 5, 6.1, 6.4, and 7.
- `project/research/general_n/2026-09-15-spare-receiver-rigidity-v1/PRESERVED_HANDOFF.md`.
- `project/research/general_n/2026-09-15-disjoint-receiver-boundary-v1/PRESERVED_HANDOFF.md`.
- `project/research/general_n/2026-09-15-triangle-free-receiver-budget-v1/PRESERVED_HANDOFF.md` (the complete predecessor proof was already available in the conversation; its stable location is confirmed by the live handoff).

The predecessor live handoff is archived in the same checkpoint. Canonical totals remain 4,626 exclusions, 952 survivors, and 3,632 whole-state closures; the 41 strict/equality certificates remain NOT_PROMOTED and the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. Original equality replay remains NOT_RUN in this continuation; state 3349 enumeration remains unresolved.

## 8. Next bounded mathematical question

Analyse the first non-rigid scalar boundary a=3d. If extras occur, (10)-(11) leave only one label outside T union K. Determine the resulting high-source graph and residual structure before attempting a catalogue scan. Treat any further rigidity or impossibility as a new proof obligation, not a consequence already established here.
