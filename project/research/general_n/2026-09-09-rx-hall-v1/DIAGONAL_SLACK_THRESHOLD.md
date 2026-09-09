# Diagonal BC thresholds as cumulative slack transport

10 September 2026. Research note inside the RX-Hall programme.

**Status: exact consequence of the candidate graph-to-incidence / BC compatibility framework. This note does not by itself prove the Murty–Simon conjecture.**

## 1. BC coordinates

For a selected label incidence write

\[
d_i=R_i+s_i,\qquad v_i=b-(R_i+x_i),
\]

and for a source state write

\[
\alpha_u=\rho_u+q_u-1,\qquad w_u=b-(q_u+p_u).
\]

The BC projection of source-label compatibility is

\[
(d_i,v_i)\le (\alpha_u,w_u)
\]

coordinatewise on every selected incidence.

The sums of the two BC coordinates simplify to

\[
d_i+v_i=b+s_i-x_i=b-(x_i-s_i),
\]

and

\[
\alpha_u+w_u=b+\rho_u-p_u-1=b-(p_u-\rho_u+1).
\]

Thus the residual transport variable `R` and the selected source degree `q`
disappear completely from the *threshold condition* on the coordinate sum.

## 2. Cumulative slack inequality

Fix an integer `c` and define the increasing diagonal upper-set indicator

\[
J_c(d,v)=\mathbf 1[d+v\ge b-c].
\]

Because `J_c` is coordinatewise nondecreasing, every selected incidence obeys

\[
J_c(d_i,v_i)\le J_c(\alpha_u,w_u).
\]

Using the identities above,

\[
J_c(d_i,v_i)=\mathbf 1[x_i-s_i\le c]
\]

and

\[
J_c(\alpha_u,w_u)=\mathbf 1[p_u-\rho_u+1\le c].
\]

Summing over the selected incidence graph counts label `i` exactly `x_i` times
and source `u` exactly `q_u` times. Hence

\[
\boxed{
\sum_i x_i\,\mathbf 1[x_i-s_i\le c]
\le
\sum_u q_u\,\mathbf 1[p_u-\rho_u+1\le c].
}
\tag{DST-c}
\]

This is an exact one-dimensional projection of BC transport.

For `c=0` it reads

\[
\sum_{i:x_i=s_i}s_i
\le
\sum_{u:p_u\le \rho_u-1}q_u.
\]

It compares the selected mass of labels that are saturated at their minimum
allowed selected degree with source mass having at least one unit of supplement
slack relative to `rho`.

## 3. Stochastic-dominance interpretation

Let the label slack be

\[
a_i=x_i-s_i\ge0
\]

and the source slack be

\[
e_u=p_u-\rho_u+1.
\]

Then `(DST-c)` is the family of weighted cumulative inequalities

\[
\sum_i x_i\mathbf1[a_i\le c]
\le
\sum_u q_u\mathbf1[e_u\le c].
\]

Since total selected incidence agrees on both sides,

\[
\sum_i x_i=\sum_u q_u,
\]

this is a weighted first-order stochastic-dominance statement between the two
slack distributions. Equivalently, every nonincreasing scalar test function of
the slack variable gives the corresponding weighted transport inequality.

In the original BC coordinates this is exactly the family of potentials that
depend only on `d+v`.

## 4. Relation to the t=2 inverse search

The first unrestricted monotone BC-only numerical optimum for the n=29 `t=2`
hard-38 common-potential problem has exactly seven negative discrete mixed
differences, all on

\[
d+v=b-1=15.
\]

The same seven locations occur in the demand-45 monotone BC-only optimum. This
motivates testing diagonal threshold steps directly rather than extrapolating the
successful `t=3` slope-one min-hinge dictionary.

A different candidate, the concave capped-sum family

\[
\min(d+v,K),
\]

was tested first. Even allowing every cap `K`, supermodular BC plus nonnegative
capped-sum corrections remains infeasible on the common hard-38 system. That
negative result is preserved in

`checkpoints/N29_T2_BC_CAP_CORRECTION_RUN_34418165165.json`.

The capped-sum failure does **not** falsify `(DST-c)`: capped sums impose a
particular cumulative relation among successive diagonal thresholds, while the
step family permits their weights independently.

## 5. Current falsification target

The active test is whether a compact combination of:

1. ordinary BC rectangle / supermodular transport; and
2. independent diagonal slack thresholds `(DST-c)`

can reproduce the common n=29 `t=2` obstruction, first on the 38-profile hard
core and then on all 902 regenerated `t=2` profiles.

A stronger target, if the diagonal family is successful, is to ask whether the
rectangle part can be removed entirely, leaving a purely one-dimensional slack
majorization argument.

All positive numerical results remain proposal-only until exactified. The
fixed-order n=29 candidate proof does not depend on this post-hoc compression.
