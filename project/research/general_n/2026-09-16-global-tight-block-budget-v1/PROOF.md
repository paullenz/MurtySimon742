# Global demand–residual budget for a tight block

16 September 2026. Research directed by Paul Lenz; internal mathematical development by ChatGPT/Geeps.

**Status: WIP_INTERNAL_PROOF_NOT_PROMOTED.** One bounded continuation from `a5bc61ec94cbdb461e7d6515bc23062f80733508` in `paullenz/MurtySimon742`. This is a conditional derivation from the FULL canonical graph-to-selected/residual bridge, including its positive-surplus residual-activity lemma. Independent expert review remains OPEN. No catalogue replay, original-graph enumeration, new state exclusion, or unrestricted Murty–Simon proof is claimed.

## 1. Main result

Use the canonical setup below and assume `tau>0`, `d>=2`, and `|T|=|H|=d`. Let Gamma be the disjoint-tight-receiver graph on H and let `z=chi(Gamma)`. Then

    a(d-1)+d >= b+2*tau+z*d*(2d-3).                       (G1)

Consequently, if the number E of extra high-source selections is positive,

    (d-1)(a-4d) >= b-3d+2*tau.                           (G2)

An extra selection forces at least 2d used receivers outside the d high sources, so b>=3d. Therefore

    tau>0 and a<=4d ==> E=0.                             (G3)

In particular the live handoff's next boundary `a=3d+1` is closed without classifying its weak K-labels one by one. This extends the previous a<=3d rigidity result in the POSITIVE-surplus regime. The earlier nonnegative-surplus result remains a separate preserved statement; residual activity is not being assumed automatically at tau=0.

For an actual canonical graph, b is its maximum degree. The elementary maximum-degree count gives b>=a+2 when tau>0. Thus for d>=3 an extra selection must satisfy the stronger integer bound

    a >= 4d+1+ceil((4+2*tau)/(d-2)).                      (G4)

For example, d=5 and integer tau>=1 require a>=23 for extras; hence E=0 through a=22 in that case. These are necessary conditions, not assertions that extras can actually occur at the displayed lower limits.

The full tight-block hypotheses with tau>0 are impossible for d=1 or d=2 (Section 6). For d>=3, a forced conclusion E=0 means high-source rigidity, NOT exclusion of the whole state. In an actual graph the full representative property identifies E with e(G[H]); the latter is then zero.

## 2. Setup and inherited facts

Let G be a finite simple diameter-two edge-critical graph. Write J=complement(G). Choose a minimum-degree pivot v in J, set A=N_J(v), B=V(J) minus N_J[v], and put

    a=|A|, b=|B|=Delta(G), n=a+b+1,
    F=complement(J[A]), tau=e(G)-b(a+1)=e(F)-r.

For each A-label i, write delta_i=deg_F(i), R_i for its total residual B-degree, x_i for its number of selected sources, and

    s_i=max(0,delta_i-R_i), x_i>=s_i.

At a B-vertex u, the A-neighbourhood N_u is the disjoint union of the selected-label set S_u and residual-label set R_u, with rho_u=|R_u|. R_i is a number on an A-label; R_u is a set on a B-source. The bridge supplies

    i in S_u ==> s_i<=rho_u,
    r=sum_i R_i=sum_u rho_u,
    S:=sum_i s_i >= r+2*tau.                             (C1)

The selected system is the full representative system, not a demand-thinned routing: each missing unordered J[B]-pair has one selected representative, with distinct destinations for different selected labels at a source and no double orientation. For an actual obligation (u,i)->w it supplies

    i not in N_w, S_u minus {i} subset N_w,
    S_w subset N_u, N_F(i) subset N_u.                   (C2)

The final condition is A-side quasi-edge domination. The reverse containment is the already reviewed consequence of quasi-edge domination and unique selected orientation.

Set

    T={i:s_i=d}, H={u:rho_u>=d}, M={u:rho_u=d-1},
    K=(union_{t in T}N_F(t)) minus T, kappa=|K|.

T is the ENTIRE demand-d level, not a chosen d-element subset. Every tight label needs d distinct selected sources and exactly d sources are eligible, namely H. Hence all high sources select all of T.

A tight obligation of label t ends outside H, at a receiver with residual set exactly T minus {t}. In particular the receiver lies in M and omits t from its entire A-neighbourhood. Let f_t(u) be that receiver for high u, and D_u={f_t(u):t in T}. D_u has d distinct elements.

An extra high label must end at another high source: a destination outside H would otherwise need all d tight labels residually in fewer than d slots. A label k in K is present at every high source by A-side domination at a neighbouring tight label. It cannot be selected there, because every possible high destination would contain it. Thus

    K subset R_u for every u in H.                      (C3)

The inherited disjoint-destination argument puts every extra obligation on an edge of Gamma, where uw is an edge exactly when D_u and D_w are disjoint. To recall its key step: a shared tight receiver v would have to select the extra label j, and reverse containment from the destination high source w would put j in N_w, contradicting destination absence. Therefore E>0 implies Gamma has an edge and z>=2. Every nonempty vertex set H gives z>=1 even when Gamma is edgeless.

## 3. Colouring forces two distinct residual costs

A used receiver cannot receive two different tight labels: its uniquely omitted tight label and residual set would contradict each other. Consequently the receiver pools

    U_t={f_t(u):u in H}, c_t=|U_t|,
    U=union_{t in T}U_t, ell=|U|=sum_t c_t

are pairwise disjoint across t. Also U and H are disjoint since their residual sizes are respectively d-1 and at least d.

For any fixed t, colouring high u by f_t(u) is a proper colouring of Gamma: sources with the same receiver cannot have disjoint D-sets. Thus each c_t>=z, and

    ell>=d*z.                                           (C4)

Every receiver in U minus U_t carries t residually. Since s_t=d>0, the exact demand identity gives delta_t=d+R_t. On the other hand all F-neighbours of t lie among the other d-1 tight labels and K. Therefore

    z(d-1) <= sum_{s!=t}c_s = ell-c_t
            <= R_t = delta_t-d <= kappa-1.

Hence

    kappa>=1+z(d-1).                                    (C5)

These are separate costs: K is residual at the high sources, while U consists of different B-vertices carrying d-1 tight residual labels each. Counting their residual incidences does NOT count the same B-source twice.

## 4. Global demand cap and residual lower bound

### 4.1 No label has demand greater than d

If a label had demand s_i>d, its s_i distinct selected sources would all have rho>=s_i>d and hence lie in H, which has only d vertices. This is impossible. A label outside the exact level T cannot have demand d either. Thus

    s_i<=d-1 for i outside T,
    S<=d^2+(a-d)(d-1)=a(d-1)+d.                         (C6)

This uses distinct selected SOURCES, not a relaxed routing that permits repetitions.

### 4.2 Use residual activity only in its proved regime

For tau>0, canonical Section 9 proves rho_u>=1 for every B-vertex. Count disjoint source classes H, U, and O=B minus (H union U). Equations (C3)-(C5) give

    r >= d*kappa + ell*(d-1) + (b-d-ell)
      = b+d*(kappa-1)+ell*(d-2)
      >= b+z*d*(d-1)+z*d*(d-2)
      = b+z*d*(2d-3).                                  (C7)

The coefficient d-2 is nonnegative for d>=2, which is why substituting the lower bound on ell is legitimate. The proof treats d=1 separately.

Combining (C1), (C6), and (C7) proves (G1).

### 4.3 Exact nonnegative slack identity

The counting proof can be audited without hidden inequalities. Define

    eta=sum_{i outside T}(d-1-s_i),
    alpha=sum_i max(0,R_i-delta_i),
    sigma_H=sum_{u in H}(rho_u-kappa),
    sigma_O=sum_{u in O}(rho_u-1).

All four are nonnegative in the stated regime. The exact max/positive-part identity is

    S=r+2*tau+alpha,

not necessarily S=r+2*tau. Direct substitution gives

    a(d-1)+d-b-2*tau
      = z*d*(2d-3)
        +d*(kappa-1-z(d-1))
        +(d-2)*(ell-z*d)
        +eta+alpha+sigma_H+sigma_O.                     (G5)

Every term after the first is nonnegative. This identifies the exact sources of looseness in (G1) and provides a concrete next target, rather than claiming the scalar bound is attainable.

## 5. Rigidity and the maximum-degree sharpening

If E>0 then z>=2. Rearranging (G1) gives (G2). Also ell>=2d and H is disjoint from U, so b>=3d. Because tau>0, the right-hand side of (G2) is strictly positive. This proves (G3).

For comparison, without invoking residual activity at O, the simpler disjoint-source count still gives

    r>=d(2d-1)+2d(d-1)=4d^2-3d

whenever E>0. With (C1) and (C6) this yields

    2*tau <= (d-1)(a-4d).                               (G6)

Thus the a<=4d conclusion in the positive-surplus regime does not itself depend on the stronger unused-vertex activity count. Equation (G2), however, DOES depend on that activity through its b-term.

Since b=Delta(G), the degree sum is at most b*n. Substituting e(G)=b(a+1)+tau and n=a+b+1 gives

    2*tau <= b*(b-a-1).

For tau>0 this forces the integer bound b>=a+2. Substituting into (G2) gives

    (d-2)*a >= 4d^2-7d+2+2*tau.

For d>=3, polynomial division and integer rounding give exactly (G4).

For integer tau>=1, (G4) requires a at least 19, 20, 23, 27, 31, 34 for d=3,4,5,6,7,8 respectively. These are lower bounds for possible extra selections under the listed hypotheses, not realizability assertions or catalogue exclusions. Retaining the actual b and tau in (G2) is generally stronger than substituting b>=a+2.

## 6. Small d and the distinction between rigidity and exclusion

For d=2, already z>=1 in (G1) gives

    a+2 >= b+2*tau+2,

contradicting b>=a+2 when tau>0. Thus the full tight-block assumptions with d=2 are impossible in this regime, whether E is zero or positive.

For d=1, a tight obligation would require a receiver of residual size zero. This contradicts residual activity for tau>0. Hence that tight block is impossible as well.

For larger d, (G1) with z>=1 gives a necessary condition for the tight block to exist at all. Using z>=2 is justified ONLY in the extra-selection branch; failure of that stronger condition forces E=0 and is NOT a proof that the entire state is impossible. No canonical ledger has been changed here.

## 7. Preserved by-product from the initial a=3d+1 attempt

The first local route examined how weak K-labels could remain selectable. The following useful restriction emerged before the global count made the boundary classification unnecessary:

    If j is selected at any high source and j is outside T,
    then N_F(j) intersect K is empty.                    (L)

Proof. Suppose k in K were an F-neighbour of extra label j selected at u. For every tight t, the receiver v=f_t(u) must contain j by forward containment. Its residual set is T minus {t}, so j is selected at v. A-side domination for j forces k into N_v; since k is outside T, k too is selected at v. A-side domination for k now implies t is NOT an F-neighbour of k, because t is absent from N_v. This holds for every t in T, contradicting k in K. Therefore (L) holds.

An extra label already has no F-neighbour in T by its being outside T union K. If A minus (T union K) is a singleton {j}, (L) therefore makes j isolated in F. Zero demand alone does not imply a label is unselected, and no such inference is made.

The predecessor's local control showing that K-labels may remain selectable at kappa=2d is still valid. This unit does NOT extend the saturated claim that every K-label is unselected. It instead bypasses that unproved extension with (G1).

## 8. Checks and their limits

Run `python check_budget.py`. The recorded output is `CHECK_RESULTS.json`. Checker SHA256:

    6b9417177d3e0e81092577400f86e1b555893dc9e1ad8eec841ded35b68dcf50

The checker actually ran locally, without downloaded inputs or third-party packages. It checks:

- 229,508 small F-degree/residual assignments for the exact positive-part identity, including nonzero alpha.
- 50,748 formal source/label-array cases for (G5) and its consequences; 5,216 have positive induced tau. These are necessary-condition arrays, NOT graph realizations.
- 360 demand/eligibility cases, integer lower-limit calculations, and the d=2 numerical obstruction.
- Four controls: dropping unused-vertex residual activity breaks the b-dependent strengthening; choosing only a subset of the demand-d labels breaks the demand cap; dropping alpha incorrectly turns an inequality into equality; taking the largest receiver pool as a chromatic lower bound is invalid.

These checks test the new arithmetic and necessary-assumption steps. They do not enumerate original graphs, replay the catalogue, establish the canonical bridge, establish graph realizability, or replace independent expert review. The proof of (L) is symbolic, not separately certified by these finite checks. No sharpness or novelty relative to the literature is claimed.

## 9. Exact dependencies, preservation, and next task

Dependencies were read from the canonical repository at immutable commit `a5bc61ec94cbdb461e7d6515bc23062f80733508`:

- `CURRENT_STATE.md`, blob `b48da28bba6097db0789ff4c05131a590a035707`.
- `project/research/general_n/2026-09-16-first-extra-boundary-v1/PROOF.md`, blob `b724f1d57300b8dce0e788cc145826fc3cd1da15`, especially Sections 2-4 and the warning about kappa=2d.
- `project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`, blob `4b6aa9e69166393d9a75c514f6f384a85c12363f`, Sections 2-6 and 9.

The receiver-colouring mechanism inherited from `project/research/general_n/2026-09-16-tight-receiver-colouring-v1/PROOF.md` is rederived in Section 3 rather than treated as an unexamined scalar assertion. The bridge and disjoint-destination reduction still require independent review.

Canonical totals remain 4,626 exclusions, 952 survivors, and 3,632 whole-state closures. The 41 strict/equality certificates remain NOT_PROMOTED; the 170-candidate audit remains AUDIT_COMPLETE_NOT_PROMOTED. Original equality replay remains NOT_RUN in this continuation; state 3349 enumeration remains unresolved. Earlier proofs, controls, audit material, and README history are retained.

**Next bounded task:** quantify unavoidable slack in (G5), especially eta plus d*(kappa-1-z(d-1)), starting at the minimum kappa permitted by the receiver colouring. Investigate whether a saturated T-K interface forces a demand deficit large enough to sharpen (G1). Prove that implication before applying it outside the predecessor's saturated branch. No improved additive term beyond (G1) is asserted in this checkpoint. The already closed a=3d+1 boundary does not need another local classification or a catalogue download first.
