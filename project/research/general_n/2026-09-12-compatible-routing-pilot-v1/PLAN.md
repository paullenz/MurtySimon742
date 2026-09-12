# Bounded compatibility pilot: frozen design

12 September 2026. Candidate research; external review remains OPEN.
Baseline main: `580c6692749d274725439ddb0bb4957e192792e7`.

Before any pilot LP, select first/middle/last state IDs in every
layer / historical proof method / zero-demand-presence stratum from the exact
5,578 joint-routing survivors. This gives 29 cases, including the sole N35
307-edge survivor and representatives of zero-demand states. These are already
excluded by canonical fixed-order certificates, not unresolved graph cases.

Four modes are compared at h=2..max(s), T=4h and all possible high-sender
counts j. Old source-capacity exclusions bypass the solver. One uncertified j
blocks the threshold, and a complete threshold witness ends that mode.
Every attempted LP has a ten-second limit. Numerical status alone never
excludes a case. Save vectors, statuses, objectives and every rounding repair.

1. `catalogue_free`: optimize the prior heavy-only local bound without its
   frozen multiplier catalogue. Any improvement here is catalogue optimization.
2. `selected_balance`: retain q, the total selected degree, source-label
   eligibility counts and conservation sum q=sum p. Use the sharper endpoint
   load q+p. This separates selected-degree effects from destination eligibility.
3. `separate_transport`: impose both the existing all-arc q-eligibility tails
   and the heavy-forced q-eligibility tails with per-destination receiving caps.
4. `joint_transport`: additionally impose two-threshold cuts in which those
   two kinds of traffic compete for the same receiving capacity.

For a fixed h and j, let F_u=H_u 1[H_u>h], O_u=q_u-F_u,
E_k={u:rho_u+q_u>=k}, Z={u:rho_u>=h}, and
m_u=min(p_u,j-1[H_u>h]). Ordinary arcs from q>k end in E_k;
forced heavy arcs from q>ell end in Z intersect E_ell. Hence

    sum O_u 1[q_u>k] + sum F_u 1[q_u>ell]
      <= sum_{E_k} p_u + sum_{(Z intersect E_ell) minus E_k} m_u.

This is a necessary cut: the two classes are disjoint arcs and the right side
counts shared capacity only once. For ell>=k the cut is dominated by the
all-arc k-tail; use ell<k for the new mixed family. Cutoffs 0..a+1 cover the
empty and full eligibility sets because rho+q<=a. A hand derivation and an
independent audit are required before accepting the graph-level application.

Selected-label degree d and label residual R are not retained in this pilot.
Thus no claim of actual label/supplement allocation or full graph feasibility
will be made. A negative result motivates reassessment before a full sweep.
