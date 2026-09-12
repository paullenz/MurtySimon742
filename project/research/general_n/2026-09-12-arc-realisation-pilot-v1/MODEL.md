# Exact model specification and omission boundary

12 September 2026. Necessary relaxations of the canonical graph bridge.

For each source u and label i, binary x_ui and r_ui indicate selected and
residual cross incidences. For every eligible source/label and v!=u, binary
z_uiv assigns its exception. Binary y_uv records an oriented missing B-pair.
Integer q_u,p_u are its outdegree and indegree. For each h=1..max(s), binary
e_uh means more than h selected labels at u have demand at least h.

Both modes impose:

- sum_i r_ui=rho_u; x_ui+r_ui<=1; x_ui=0 if s_i>rho_u;
- sum_v z_uiv=x_ui; sum_i z_uiv=y_uv; y_uv+y_vu<=1;
- q_u=sum_i x_ui; p_u=sum_v y_vu;
- q_u+rho_u<=a; p_u<=rho_u+b-a-1;
- sum_u x_ui>=s_i;
- x_ui=1 implies sum_v(x_vi+r_vi)>=q_u+p_u;
- y_uv=1 implies rho_v+q_v>=q_u-1;
- if H_uh=sum_(s_i>=h)x_ui, then e_uh=1 exactly when H_uh>h;
- for s_i>=h and rho_v<h, z_uiv+e_uh<=1.

The orientation and incidence equations imply q_u+p_u<=b-1 and equality
of the total incoming and outgoing degrees. Endpoint implication uses the
valid bound b-1 when x_ui=0; destination implication uses a. All coefficients,
variable bounds and row bounds are saved as exact integers. Zero objective
asks only for a feasible assignment; optimality is irrelevant here.

`label_compatible` adds

    z_uiv+x_vi+r_vi<=1,
    x_vi+r_vi-x_ui-y_uv-y_vu+z_uiv>=-1.

The second row also applies when z_uiv does not exist (interpreted as zero).
It says that if i is selected at u and {u,v} is a chosen missing pair, v must
contain i unless that very incidence has v as its exception. The first row
requires the exception to miss i. Together these are precisely the B-side
domination conditions in the [fixed-neighbourhood proof](FIXED_NEIGHBOURHOOD_FLOW.md).

The model fixes labelled residual and demand sequences but not H[A], the
degree sequence d_i, the exact d/R/s relation, its graph realization, A-side
quasi-edge domination, or criticality for other graph edges. Residual column
degrees are sums of the actual residual incidence matrix. A model witness
would be an abstract routing witness, not a Murty-Simon counterexample.

The two modes both search simultaneous arcs. Their difference is B-side
label compatibility, not the difference between fractional and integral
counts. This frozen experiment cannot measure either model's strength when
neither returns a verified incumbent or exclusion certificate.

Solver interface reference: [SciPy milp documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.milp.html).
The installed SciPy version is pinned in the environment record, rather than
inferred from the current online manual. All twelve original statuses are 1,
with the message reporting a time limit and no primal incumbent. The nominal
20-second internal limit is not a strict wall-time guarantee; the independent
45-second process guard never fired. The longest observed solver time was
23.42042074899655 seconds. None of these statuses is an infeasibility proof.
