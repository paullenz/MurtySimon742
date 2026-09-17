# Current structural review — 17 September 2026

The project now has a five-label exact-block theorem, several general scope bridges, an important scalar-recursion obstruction, and a new exact-incidence result that completely closes one concrete near-Turán scope frontier.

## 1. Five-label exact block

[Five-label defect eleven is impossible](project/research/general_n/2026-09-17-d5-defect11-closure-v1/THEOREM.md) proves, under the whole-level exact-block hypothesis `|T|=|H|=5`,

    D >= 12,
    W >= 37,
    extras => W >= 57.

The preceding exact support-cover and pair-coverage packages supply the critical-edge machinery and independent finite checks. D=12 attainability, sharpness and external acceptance remain open.

The parameter-wide exact-block predecessor also supplies pair coverage, critical-edge support charging and the hand lower bound `D>=ceil(d(d-1)/4)` for general block size d.

## 2. Scope bridge via h-index saturation

[Residual h-index saturation and the exact-block equality face](project/research/general_n/2026-09-17-hindex-saturation-v1/HINDEX_SATURATION.md) revisits the general residual h-index argument. If h is the residual h-index, `|{rho>=h}|=h+u`, and k labels have demand h, then

    b+2t <= (a-h-u)(h-1)+k.

Equivalently, the older h-index upper bound loses the explicit stability term `a-k+u(h-1)`. When `u=0`, receiver containment forces `k<=h`; `k=h` is precisely the square exact block. This identifies the exact-block theory as a saturation face rather than an isolated hypothesis.

## 3. Destination bridge via receiver inflation

[Receiver inflation beyond h-index saturation](project/research/general_n/2026-09-17-receiver-inflation-v1/RECEIVER_INFLATION.md) adds a penalty that the scalar h-index theorem does not see. For a threshold `q<h`, omission counting bounds how many high sources can select at most q maximum-demand labels. The remaining selected mass cannot all use destinations inside the h+u high sources because selected representatives consume distinct B-pairs. Overflow to low destinations forces those receivers to carry at least q maximum-demand labels residually.

With `N=h+u`,

    ell_q=min(N,floor(ku/(k-q))),
    Y_q=max(0,kh-q ell_q-C(N,2)),
    z_q=ceil(Y_q/N),

one obtains

    r >= b+h(h-1)+u(h-1)+(q-1)z_q,

and hence

    b+2t <= (a-h-u)(h-1)+k-(q-1)z_q.

The accompanying exact dynamic programme checks the row-load relaxation for 6,090 parameter/threshold combinations. The graph implication remains a hand theorem by the same assistant, so external mathematical review is still required.

## 4. Coupled staircase / first peeling theorem

[Coupled demand/residual staircases and the first peeling inequality](project/research/general_n/2026-09-17-staircase-peeling-v1/STAIRCASE.md) rewrites the canonical threshold-capacity theorem in terms of demand-tail counts

    K_d=#{i:s_i>=d}

and residual-tail counts

    N_d=#{u:rho_u>=d}.

Positive surplus gives exact layer-cake identities

    S=sum_d K_d,
    r=sum_d N_d,

so the ledger becomes

    2t <= sum_d (K_d-N_d).

At every threshold d the existing pair-capacity theorem becomes

    d K_d + sum_{j>d} K_j
      <= d N_d + C(N_d-d,2).

For the top two levels, if `N_h=N_{h-1}=h` and the top demand level is non-square, then

    b+2t <= (h-2)(a-h+1).

At h=5,

    N_5=5 and b+2t>3a-12
      => K_5=5 or N_4>=6.

This is a genuine top-level narrowing of the exact-block coverage problem.

## 5. Scalar recursion obstruction

[Scalar staircase obstruction](project/research/general_n/2026-09-17-staircase-scalar-obstruction-v1/SCALAR_OBSTRUCTION.md) tests the proposed next step rather than assuming that the staircase can simply be iterated.

Two facts emerge.

First, if h is the residual h-index and `N_h=h`, then for every `d<h`,

    N_d>=h>d.

So the same unreduced graph cannot literally reach a lower square face `N_d=d`. Any genuine lower-level recursion would need a reduced graph/representative system whose residual h-index changes.

Second, there is an explicit abstract feasible point of the current scalar relaxation at one edge above Turan:

    a=20, b=23, n=44, t=2, m=485,
    s=(4^20),
    rho=(5^5,4^11,1^7).

It has

    S=80,
    r=76,
    r+2t=S,

and tails

    K=(20,20,20,20,0,...),
    N=(23,16,16,16,5,0,...).

Thus the residual h-index is 5 but `K_5=0`. All staircase-capacity inequalities, both canonical charging inequalities, h-index saturation, and the exact restricted heavy-load cutoff family survive. The latter is checked for every integer cutoff: finite ranges are enumerated exactly and an analytic linear lower bound closes the infinite tail. Basic label and residual degree sequences are also graphical.

This is not a graph realization and not a counterexample to Murty-Simon. It is a clean obstruction to the **aggregated proof strategy**: the scalar inequalities alone do not force entry into the exact block.

## 6. Exact selected-incidence Hall majorization closes the mixed 4/5 frontier

The scalar obstruction led to retaining the actual selected-incidence multiplicities. For every selected incidence `ui` the canonical bridge has

    s_i<=rho_u,
    e_i>=max(0,p_u-rho_u+1),
    R_i+x_i>=p_u+q_u.

Full capacitated Hall then yields threshold-count majorization

    sum_{p_u+q_u>=T} q_u
      <= sum_{R_i+x_i>=T} x_i,

together with the demand-four restriction

    sum_{rho_u=4} q_u
      <= sum_{s_i=4} x_i.

Earlier exact-incidence packages successively exclude total selected excess `E=0,...,9` in the mixed demand-4/5 near-Turán frontier `(a,b,t)=(20,23,2)`.

[Hall-ramp majorization closes the remaining mixed demand-4/5 selected-excess range](project/research/general_n/2026-09-17-hall-ramp-all-excess-v1/HALL_RAMP_ALL_EXCESS.md) compresses the rest. Define

    H_L(z)=max(0,min(z,L)-4)
          =sum_{T=5}^L [z>=T].

Three range-uniform Hall potentials suffice:

    10<=E<=15 : Phi=4H_9+12H_12+4H_19,
    16<=E<=21 : Phi=5H_9+19H_14,
    22<=E<=42 : Phi=6H_8+24H_15.

After exact local support inequalities are summed, the contradiction gaps are respectively

    60E-580,
    47E-750,
    47E-k-1006.

Their minima on the stated ranges are `20`, `2`, and `8`. Finally,

    sum p_u <= sum(rho_u+2)

forces `E<=42`.

Therefore, combining with the earlier `E<=9` work:

> **No canonical bridge in the established mixed demand-4/5 near-Turán scope `(20,23,2)` survives at any selected-excess level.**

This is a concrete closure of the selected-excess scope gap in that demand support. It is not yet a reduction of the full conjecture to the five-label exact block, because other demand-support patterns remain to be controlled. The new theorem has an exact integer replay checker and uses no catalogue scan.

## Strategic consequence

The endpoint/orientation programme has now paid off in a substantial way: it does more than kill the earlier scalar witness. In the mixed `{4,5}` near-Turán frontier it removes the entire selected-excess dimension.

The next move should therefore **not** be another E-level exclusion. The useful structural question is now one level higher:

1. Can the general h-index/receiver machinery force any remaining near-Turán obstruction into demand support `{4,5}`?
2. Failing that, can Hall-ramp majorization be stated and proved in a demand-support-general form?

Either route would connect the new incidence theorem to the five-label exact-block theory and is more valuable than expanding the canonical survivor catalogue.

**Status:** internal candidate mathematics with exact finite replay, plus preserved negative relaxation results. External mathematical review, novelty assessment and conjecture-level promotion remain open. Canonical counts remain 4626 exclusions / 952 survivors / 3632 whole-state closures.

Use [CURRENT_STATE.md](CURRENT_STATE.md) for the live operational handoff. All earlier proofs, verifiers, failed routes and review material remain preserved.
