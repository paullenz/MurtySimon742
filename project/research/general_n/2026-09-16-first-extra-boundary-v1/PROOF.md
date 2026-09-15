# Closing the first extra-selection boundary

16 September 2026. Research directed by Paul Lenz; internal mathematical development by ChatGPT/Geeps.

**Status: WIP_INTERNAL_PROOF_NOT_PROMOTED.** One bounded symbolic continuation from `6c0f63f520ff9882046543a61311699156ef5c4b`. The conclusions are conditional on the full canonical graph-to-selected/residual bridge. Independent expert review remains OPEN. No catalogue replay, original-graph enumeration, new catalogue exclusion, or unrestricted Murty-Simon proof is claimed.

## 1. Main conclusion and scope

In the full canonical system, suppose the tight labels and eligible high sources satisfy `|T|=|H|=d`. Write `a=|A|` and `E=sum_H(|S_u|-d)`. Let

    tau = e(G)-b(a+1) = e(F)-r

be the canonical surplus. Then the new conclusion is

    tau>=0 and a<=3d  ==>  E=0.                         (B0)

The predecessor proved rigidity for `a<3d` without a surplus restriction, but allowed `E<=d-1` at `a=3d`. This note closes that boundary in the nonnegative-surplus regime, which includes the positive-surplus counterexample search. In an actual graph, the full representative property gives `E=e(G[H])`, so the high-source induced graph is edgeless in this regime.

This does NOT exclude every tight-block state with `a=3d`: it forces its high-source selections to be rigid. It does NOT assert rigidity at this boundary when tau is negative. A graph exceeding the Murty-Simon benchmark would have tau>0 because `b(a+1)<=floor((a+b+1)^2/4)`.

The more general saturated-core obstruction proved below is, for `d>=2`,

    E>0 and |K|=2d-1
    ==> tau <= e(F[P])-e(F[K])-R_P-3*binom(d,2),        (B1)

where `K=N_F(T) minus T`, `P=A minus (T union K)`, and `R_P=sum_{i in P}R_i`. This is a bound on the actual canonical surplus, not a statement that the upper bound is realizable.

## 2. Definitions and exact dependencies

Write J for the complement of the original graph G, to avoid confusing J with the high-source set H. The canonical minimum-degree pivot in J gives A, B, `a=|A|`, `b=|B|`, and `F=complement(J[A])`.

For a label i in A, let `delta_i=deg_F(i)`, let R_i be its total residual degree into B, and let x_i be its number of selected sources. At a B-vertex u, write `N_u=S_u disjoint-union R_u`, where R_u is a set and `rho_u=|R_u|`. In particular R_i is a number attached to a label; R_u is a set attached to a source. The bridge supplies

    s_i=max(0,delta_i-R_i),  x_i>=s_i,
    i in S_u ==> s_i<=rho_u,
    r=sum_i R_i=sum_u rho_u,  e(F)=r+tau.                 (C)

The selected system is the FULL system, with one representative for every missing unordered J[B]-pair, not a demand-thinned choice. Each selected label has a destination, distinct selected labels at one source have distinct destinations, and opposite orientations of a missing pair cannot both be selected. For an obligation `(u,i)->w`,

    i not in N_w,
    S_u minus {i} subset N_w,
    S_w subset N_u,
    N_F(i) subset N_u.                                   (P)

The last condition is A-side quasi-edge domination. The reverse containment is the previously reviewed consequence of quasi-edge domination and unique representative orientation.

Fix `d>=1`, and put

    T={i:s_i=d}, H={u:rho_u>=d}, M={v:rho_v=d-1}.

Assume `|T|=|H|=d`. Every tight label must be selected at every high source, and nowhere else. Let `D_u` be the d tight destinations of high u. A receiver of tight label t lies in M, omits t, and has residual set exactly `T minus {t}`.

The predecessor establishes, for `K=N_F(T) minus T` and `kappa=|K|`,

    K subset R_u for every high u;
    an extra high selection goes to a high source w
      with D_u intersect D_w empty;
    R_t=delta_t-d<=kappa-1 for every tight t.             (D)

For reference, an extra label cannot end outside H because it would force all d tight labels into fewer than d residual slots. A label in K is present at every high source by A-side domination; an extra selection of that label could therefore have no high destination omitting it. This proves the first statement of (D).

A used receiver has a unique omitted tight label. Thus, if U_t is the set of receivers used for tight label t, then the U_t are pairwise disjoint. Write `c_t=|U_t|` and `ell=sum_t c_t`. The exact residual degrees satisfy

    ell-c_t <= R_t <= kappa-1.                           (R)

An extra selection implies a disjoint high pair, hence `c_t>=2` for EVERY tight t and `kappa>=2d-1`. Extras use labels outside T union K, so `E>0` also implies `a-d-kappa>=1`. These are the predecessor's bounds, not new assumptions about arbitrary scalar routings.

## 3. Common tight neighbours cannot be selected anywhere

This observation does not require saturation of kappa. Let a label k outside T be F-adjacent to every member of T. Such k belongs to K and is residual, not selected, at every high source by (D).

Suppose k were selected at a non-high source v. A-side domination in (P) would force `T subset N_v`. None of those tight labels can be selected at v, by eligibility. All d would therefore be residual at v, contradicting `rho_v<d`.

Consequently

    N_F(k) contains T ==> x_k=0 ==> R_k>=delta_k.         (Z)

The last implication uses the minimum-degree demand inequality in (C). It is important to prove x_k=0 first: ZERO DEMAND ALONE DOES NOT MEAN A LABEL IS UNSELECTED. The full selected system may include labels with s_i=0.

## 4. Equality structure when kappa=2d-1 and E>0

Assume now `d>=2`, `E>0`, and `kappa=2d-1`. For every tight t, (R) and `c_s>=2` give

    2(d-1) <= sum_{s!=t}c_s = ell-c_t
            <= R_t <= 2d-2.

Every inequality is an equality. Since for each s there exists a different tight t, all `c_s=2`; thus

    ell=2d,  R_t=2d-2,  delta_t=3d-2 for every t.         (S1)

All residual occurrences of tight t are precisely the used receivers in `U minus U_t`: they already account for its entire residual degree.

By definition of K, a tight label has no F-neighbour outside T union K. Its largest possible degree there is

    (d-1)+(2d-1)=3d-2.

The degree in (S1) attains that maximum. Hence

    F[T] is complete and every T-K pair is an F-edge.     (S2)

Every label of K is now a common F-neighbour of all T. Applying (Z),

    x_k=0, s_k=0, R_k>=delta_k for EVERY k in K.           (S3)

This global absence of selected K-labels is the decisive extra constraint. Counting only residuals at the high sources and tight receivers is insufficient.

## 5. Exact edge/residual accounting

Partition A into T, K, and P. There are no F-edges between T and P. Put `e_K=e(F[K])`, `e_P=e(F[P])`, and let e_KP count F-edges between K and P. By (S2),

    e(F)=binom(d,2)+d*kappa+e_K+e_KP+e_P.                (L1)

The total degree of the K-labels is

    sum_{k in K}delta_k=d*kappa+2e_K+e_KP.

By (S1), (S3), and the definition of R_P,

    r >= 2d(d-1)+d*kappa+2e_K+e_KP+R_P.                 (L2)

Subtracting (L2) from (L1), and using the exact identity `tau=e(F)-r`, gives

    tau <= e_P-e_K-R_P-3*binom(d,2),                     (L3)

which is (B1). All K-P terms cancel; they must not be silently omitted from either side before subtraction.

In particular, if tau>0 and p=|P|, then

    binom(p,2) >= e_K+R_P+3*binom(d,2)+1
               >= 3*binom(d,2)+1.                       (L4)

This necessary inequality applies ONLY to the `kappa=2d-1`, E>0 branch. It is not an a-only bound for branches with larger kappa and is not sufficient for realization.

## 6. Closure at a=3d

If `a=3d` and E>0, the predecessor's `kappa>=2d-1` and existence of an extra label outside T union K force

    kappa=2d-1, P={j}.

Thus e_P=0. Equation (L3) yields

    tau <= -3*binom(d,2)-e_K-R_j
         <= -3*binom(d,2)<0                              (B2)

for d>=2. This contradicts tau>=0. Together with the predecessor's rigidity for a<3d, it proves (B0). For d=1 there is only one high source and an extra selection would require another high destination, so E=0 directly; no division by d-1 is used.

For example, d=5 and a=15 would force `tau<=-30` if extras existed, rather than merely allowing up to four extras. In the positive-surplus search this proves E=0. This is an illustrative consequence, not a newly rejected catalogue state.

## 7. Additional boundary structure and a second algebraic check

These observations are conditional on the hypothetical E>0 boundary configuration and are not needed for (L3).

Every used receiver has residual set `T minus {t}`. By (S3), it has no selected K-labels. At a=3d its only possible selected label is therefore j.

Choose a high source u selecting extra j. Forward containment along every tight obligation from u forces j to be selected at each receiver in D_u. Such a receiver has no K-neighbours in its A-neighbourhood. A-side domination for selected j excludes every F-edge from j to K. There is no F-edge from j to T by definition of P, and there is no other P-label. Hence

    delta_j=0, s_j=0.                                    (A1)

The only positive-demand labels are then T, with total demand d^2. The high sources contribute at least `d(2d-1)` residual incidences and the 2d used receivers contribute `2d(d-1)`, on disjoint B-vertex sets. Thus `r>=4d^2-3d`. The canonical inequality `sum_i s_i>=r+2*tau` independently gives

    tau <= (d^2-r)/2 <= -3*d*(d-1)/2.

This checks the boundary contradiction by a different algebraic route within the SAME internally reviewed bridge; it is not independent expert verification.

The actual high-source graph G[H] would also be a disjoint union of stars and isolated vertices. Every high edge has extra label j, oriented from a source selecting j to a destination omitting j. A source selecting j has exactly one outward high edge and cannot receive a high edge, so it is a leaf. Sources omitting j are centres; those with residual j are isolated. This assertion is about G[H], NOT the whole disjointness graph Gamma.

## 8. Checks, rejected weakenings, and precise limits

`python check_boundary.py` was run locally with no downloaded inputs or third-party packages. Exact output is preserved in `CHECK_RESULTS.json`. Source SHA256:

    09b17e030557265453eba7d4ef1d95363992b31341b5e4ea347f8b58b5a3760e

The checks cover 296,675 receiver-count vectors (d=2 through 7), 2,035 proper tight-presence profiles (d=2 through 10), and 67,656 small A-side graphs with the saturated T/K structure and arbitrary remaining F-edges. The latter directly compute degrees and compare the residual lower bound with the asserted surplus expression, including nonzero R_P controls. These tests validate the NEW equality, eligibility and counting reductions only. They neither enumerate original G nor independently validate the canonical bridge.

Three controls are preserved:

1. Dropping (S3) and counting only high/receiver residuals gives a spurious relaxed surplus +1 at d=3, whereas the necessary zero-selection/minimum-degree bound gives an upper bound -19. The weakened model is deliberately not a valid canonical realization.
2. At kappa=2d, a K-label can miss one tight F-neighbour and pass local A-side domination at a receiver missing that same tight label. An explicit d=3 local configuration is in the checker. Thus the claim that ALL K-labels are unselected must not simply be exported beyond the saturated branch. This is a local control, not an original-graph counterexample.
3. The relaxed inequality admits surplus zero for d=2, kappa=3, p=3. No realization, sufficiency, or positive-surplus counterexample is inferred.

The symbolic proof of the star-forest and isolated-j observations is recorded above; those are not asserted to have been separately established by the finite checker. External review of all shared bridge dependencies remains OPEN.

## 9. Preservation and next bounded question

Canonical status is unchanged: 4,626 exclusions, 952 survivors, and 3,632 whole-state closures. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. Original equality replay remains NOT_RUN in this continuation. State 3349 enumeration remains unresolved.

At the next scalar boundary a=3d+1, an extra selection would allow kappa=2d-1 or 2d. The former leaves p=2, and (L3) bounds tau by at most `1-3*binom(d,2)<0` for d>=2. Thus only kappa=2d remains for a positive-surplus attempt. The next unit should examine this one-unit-larger common residual set without assuming (S2) or (S3) still holds. No such extension is proved here.

Exact sources, all inspected at immutable commit `6c0f63f520ff9882046543a61311699156ef5c4b` in `paullenz/MurtySimon742`:

- `project/research/general_n/2026-09-16-tight-receiver-colouring-v1/PROOF.md` (blob `4cbabdd552c448b769b682e654675d6693654b4f`).
- `project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`, particularly Sections 2-6 (blob `4b6aa9e69166393d9a75c514f6f384a85c12363f`).
- The live predecessor `CURRENT_STATE.md` (blob `28890c8251697378ed1f01907599db16ffbd0c0f`), archived unchanged in the publication checkpoint.

All previous proofs, failed routes, controls, reviewer material, and README history remain preserved. This note does not promote a computational or mathematical claim into the canonical ledger.
