# The low-demand exception: explicit heavy-degree transport

12 September 2026. Candidate graph-to-model argument and exact certificate.
Development and internal checking: ChatGPT/Geeps; external review OPEN.

The exceptional state is

`s=(1^2,2^13)`, `rho=(1^10,2^8)`, `(a,b,t,dmax)=(15,18,1,13)`.

The saved `low_state_rx.json` records a numerical feasible point of the older
RX/Hall relaxation. It is not a graph. That relaxation omits a useful
consequence of the canonical heavy-label supplement argument.

## 1. Additional graph constraint

Fix h=2, call a label heavy when s_i>=h, and let H_u be the actual number of
heavy selected incidences from source u. The
[source-capped threshold proof](../../general_n/2026-09-12-source-capped-threshold-v1/SOURCE_CAPPED_THRESHOLD.md)
shows that every heavy selected arc from a source with H_u>h ends in
`Z_h={u:rho_u>=h}`. Distinct arcs are counted by supplement indegree p, so

`sum_{u:H_u>h} H_u <= sum_{u:rho_u>=h} p_u`.                (1)

Unlike total outdegree q_u, H_u distinguishes which selected labels force
this routing. The new model retains H_u as part of each source's state.
Equation (1) is universal; the certificate below is for this one fixed state.

## 2. Exact grouped graph image

Let source residual group k have size n_k, and label demand group g have
size m_g. All quantities below are normalized counts of actual vertices,
pairs or selected incidences. They therefore lie in [0,1].

- W(k,q,p,H) is the fraction of sources in group k with that exact state.
- L(g,R,x) is the fraction of labels in group g with that exact state.
- P(k,l,q,q') is the number of oriented selected B-pairs with these source
  and supplement groups/outdegrees, divided by `n_k(n_l-[k=l])`.
  When k=l and n_k=1, no such variable is needed because self-pairs do not exist.
- Z(k,g,q,p,H,R,x) is the number of selected source-label pairs with the
  specified states, divided by n_k*m_g.

W and L have unit normalization within each group. Source states obey the
canonical bounds `q+rho<=a`, `q+p<=b-1`, and `p<=rho+b-a-1`.
If a source has at most c_light compatible light labels and c_heavy compatible
heavy labels, distinct selected labels also give

`q<=c_light+c_heavy`,

`max(0,q-c_light)<=H<=min(q,c_heavy)`.

All demands in this exceptional state are positive. Thus d=R+s for labels,
and we require `d<=13`, `x>=s`, `R+x<=18`, and `x<=#{u:rho_u>=s}`.
The grouped residual identity is `sum_g m_g E_g[R]=r` exactly.

P is allowed only if `rho_l+q'>=q-1`. Its outgoing balance is

`sum_l (n_l-[k=l]) P(k,l,q,q')`, summed over q',
`= q sum_{p,H}W(k,q,p,H)`.

Its incoming balance, for fixed l,q', is

`sum_k (n_k-[k=l]) P(k,l,q,q')`, summed over q,
`= sum_{p,H}p W(l,q',p,H)`.

The group normalization factors agree because
`n_k(n_l-[k=l])=n_l(n_k-[k=l])`. These equations count the same selected
arcs from their two ends.

Z is allowed only if the canonical incidence conditions hold:

`s_g<=rho_k`, `R+s_g<=rho_k+q-1`, `R+x>=q+p`.

It is also absent when its label is heavy but H=0, or light but H=q.
For a fixed source state and label group,

`sum_{R,x} Z(k,g,q,p,H,R,x) <= W(k,q,p,H)`.

This counts at most one selected edge per actual source-label pair.
Summing these incidences over all label groups, with factors m_g, gives
`q W(k,q,p,H)`. Summing only over heavy groups gives `H W(k,q,p,H)`.
For a fixed label state, summing Z over source groups/states with factors n_k
gives `x L(g,R,x)`. These are exact incidence balances.

Finally (1) becomes the single linear inequality

`sum_{k,q,p,H} n_k (H [H>2]-p [rho_k>=2]) W(k,q,p,H)<=0`.

Every graph realizing the state supplies this normalized nonnegative model
point. Additional pair-capacity constraints are omitted, which only enlarges
the domain. Infeasibility of this domain is therefore a valid exclusion.

## 3. Exact certificate and replay

The pure-integer specification `heavy_model.py` constructs 12,570 variables,
12,985 inequalities (including unit upper bounds) and 690 equalities.
`certify_heavy.py` uses the previously preserved Farkas proposal/repair code.
It stores every nonzero integer multiplier in `heavy_certificate.json`.

For inequalities `A x<=b`, equalities `E x=f`, and nonnegative variables x,
the saved multipliers satisfy

`lambda>=0`, `lambda A+mu E>=0`,

`lambda b+mu f=-998530<0`.

Thus an actual model point would satisfy

`0 <= (lambda A+mu E)x <= -998530`,

a contradiction. The sign check covers all 12,570 columns. The proof does
not depend on the solver's infeasibility report or the numerical feasible
point of the earlier relaxation.

The main standard-library verifier reconstructs the integer model, checks
every multiplier and column, and places this exclusion in the exact coverage
ledger. Numerical discovery uses SciPy; certificate verification does not.
The model specification is shared between discovery and reconstruction;
the envelope verifier elsewhere is separately implemented. Neither is
external independent mathematical review.
