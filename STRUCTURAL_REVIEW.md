# Current structural review — 17 September 2026

The project now has three complementary structural layers. The third was chosen after a deliberate step-back review rather than by mechanically following the previous handoff.

## 1. Five-label exact block

[Five-label defect eleven is impossible](project/research/general_n/2026-09-17-d5-defect11-closure-v1/THEOREM.md) proves, under the whole-level exact-block hypothesis |T|=|H|=5,

    D >= 12,
    W >= 37,
    extras => W >= 57.

The preceding exact support-cover and pair-coverage packages supply the critical-edge machinery and independent finite checks. D=12 attainability, sharpness and external acceptance remain open.

The parameter-wide exact-block predecessor also supplies pair coverage, critical-edge support charging and the hand lower bound `D>=ceil(d(d-1)/4)` for general block size d.

## 2. Scope bridge via h-index saturation

[Residual h-index saturation and the exact-block equality face](project/research/general_n/2026-09-17-hindex-saturation-v1/HINDEX_SATURATION.md) revisits the general residual h-index argument. If h is the residual h-index, |{rho>=h}|=h+u, and k labels have demand h, then

    b+2t <= (a-h-u)(h-1)+k.

Equivalently, the older h-index upper bound loses the explicit stability term `a-k+u(h-1)`. When u=0, receiver containment forces k<=h; k=h is precisely the square exact block. This identifies the exact-block theory as a saturation face rather than an isolated hypothesis.

## 3. Destination bridge via receiver inflation

[Receiver inflation beyond h-index saturation](project/research/general_n/2026-09-17-receiver-inflation-v1/RECEIVER_INFLATION.md) adds a penalty that the scalar h-index theorem does not see. For a threshold q<h, omission counting bounds how many high sources can select at most q maximum-demand labels. The remaining selected mass cannot all use destinations inside the h+u high sources because selected representatives consume distinct B-pairs. Overflow to low destinations forces those receivers to carry at least q maximum-demand labels residually.

With `N=h+u`,

    ell_q=min(N,floor(ku/(k-q))),
    Y_q=max(0,kh-q ell_q-C(N,2)),
    z_q=ceil(Y_q/N),

one obtains

    r >= b+h(h-1)+u(h-1)+(q-1)z_q,

and hence

    b+2t <= (a-h-u)(h-1)+k-(q-1)z_q.

The accompanying exact dynamic programme checks the row-load relaxation for 6,090 parameter/threshold combinations. The graph implication remains a hand theorem by the same assistant, so external mathematical review is still required.

This receiver mechanism is complementary to the preserved 12 September heavy-load/routing family: that theorem charges supplement indegree and residual tails, whereas receiver inflation charges destination pair capacity and forced low residual load.

## Strategic consequence

The broader review changes the next priority. The excess-high-source branch u>0 is now explicitly penalized, but it is not the only way to avoid the square exact block. When k<h, mass can migrate to demand h-1 and the top-level receiver penalty can weaken while the aggregate demand bound remains large. The next target is therefore a **multi-level staircase/peeling theorem** coupling the h and h-1 levels, ideally with the existing heavy-load tail inequalities.

**Status:** internal candidate mathematics. Exact-block coverage is narrowed but not solved. Canonical counts remain 4626 exclusions / 952 survivors / 3632 whole-state closures; no unrestricted Murty-Simon proof or catalogue promotion is claimed.

Use [CURRENT_STATE.md](CURRENT_STATE.md) for the live operational handoff. All earlier proofs, verifiers, failed routes and review material remain preserved.
