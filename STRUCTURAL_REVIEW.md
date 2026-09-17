# Current structural review — 17 September 2026

The project now has four positive structural layers plus one important negative scope result. The negative result matters because it prevents the programme from spending further time on a scalar recursion that the present relaxation cannot support.

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

This is not a graph realization and not a counterexample to Murty–Simon. It is a clean obstruction to the **aggregated proof strategy**: the currently available scalar inequalities do not force entry into the exact block.

## Strategic consequence

The positive structural programme remains valuable, but the next move should preserve information that the scalar relaxations discarded.

The leading target is the joint endpoint/orientation system. Before local source capacities are maximized independently, every selected incidence satisfies

    R_i+x_i >= q_u+p_u,

while globally

    sum_u q_u = sum_u p_u,

and selected representatives use distinct unordered B-pairs. These constraints couple label load, source outdegree and supplement indegree. The current heavy-load theorem relaxes that joint system into independent source maxima; the scalar obstruction survives after that decoupling.

The next high-value theorem should therefore derive a global inequality from endpoint loads, orientation conservation, pair uniqueness and residual-light incoming capacity, or else formalize a genuine reduced-system peeling operation whose h-index can actually fall.

**Status:** internal candidate mathematics plus an internally audited negative relaxation result. Exact-block coverage is narrowed but not solved. Canonical counts remain 4626 exclusions / 952 survivors / 3632 whole-state closures; no unrestricted Murty-Simon proof or catalogue promotion is claimed.

Use [CURRENT_STATE.md](CURRENT_STATE.md) for the live operational handoff. All earlier proofs, verifiers, failed routes and review material remain preserved.
