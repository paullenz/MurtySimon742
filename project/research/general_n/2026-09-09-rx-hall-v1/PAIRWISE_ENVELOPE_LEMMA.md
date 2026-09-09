# Direct pairwise-staircase envelope lemma

9 September 2026. Candidate structural reduction inside the selected/residual necessary-condition framework. This is **not** an unrestricted Murty--Simon theorem.

## 1. Purpose

The minimized n=30 pairwise-staircase contradiction was first found as an exact Farkas certificate. After removing redundant unit upper bounds, its remaining group-normalisation multipliers have a direct interpretation: they simply lower-bound each normalized source or label distribution by the minimum value of a local score.

This yields a reusable inequality with no Farkas dual variables and no explicit LP-density upper bounds.

## 2. Generic W/L setting

Let source residual-degree groups have values `rho` and multiplicities `N_rho`, with normalized distributions

\[
\sum_{q,p} W_{\rho,q,p}=1,
\qquad W_{\rho,q,p}\ge0.
\]

Let positive-demand label groups have values `s` and multiplicities `M_s`, with normalized distributions

\[
\sum_{R,x} L_{s,R,x}=1,
\qquad L_{s,R,x}\ge0.
\]

Retain the exact identities

\[
\sum_{\rho,q,p}N_\rho(q-p)W_{\rho,q,p}=0,
\tag{E1}
\]

\[
\sum_{s,R,x}M_s R L_{s,R,x}=r,
\tag{E2}
\]

and

\[
\sum_{\rho,q,p}N_\rho qW_{\rho,q,p}
=
\sum_{s,R,x}M_s xL_{s,R,x}.
\tag{E3}
\]

For every threshold `j>=1`, source/supplement transport gives

\[
T_j:=
\sum_{\rho,q,p}N_\rho
\left(
q\mathbf1_{q\ge j+1}
-p\mathbf1_{\rho+q\ge j}
\right)W_{\rho,q,p}
\le0.
\tag{E4}
\]

Put

\[
d=R+s,\qquad h=R+x,
\]

\[
\alpha=\rho+q-1,\qquad \beta=q+p.
\]

Let `Psi_L(s,R,x)` and `Psi_S(rho,q,p)` arise from any nonnegative weighted sum of valid BC and SH staircase upper-set inequalities. Equivalently, as in `PAIRWISE_STAIRCASE_POTENTIAL.md`, write

\[
\Psi_L=F(d,h)+G(s,h),
\]

\[
\Psi_S=F(\alpha,\beta)+G(\rho,\beta).
\]

Then pairwise monotone transport gives

\[
\sum_{s,R,x}M_s x\Psi_L(s,R,x)L_{s,R,x}
\le
\sum_{\rho,q,p}N_\rho q\Psi_S(\rho,q,p)W_{\rho,q,p}.
\tag{E5}
\]

## 3. Envelope inequality

Choose real `mu`, nonnegative `lambda,c`, and nonnegative threshold multipliers `tau_j`. Define the label score

\[
\mathcal L_s(R,x)
=
\lambda R+c x+x\Psi_L(s,R,x),
\tag{E6}
\]

and the source score

\[
\mathcal S_\rho(q,p)
=
\mu(q-p)
+
\sum_j\tau_j
\left(
q\mathbf1_{q\ge j+1}
-p\mathbf1_{\rho+q\ge j}
\right)
-cq-q\Psi_S(\rho,q,p).
\tag{E7}
\]

Multiplying (E1)--(E5) by the stated coefficients and adding gives the necessary inequality

\[
\sum_{s,R,x}M_s\mathcal L_s(R,x)L_{s,R,x}
+
\sum_{\rho,q,p}N_\rho\mathcal S_\rho(q,p)W_{\rho,q,p}
\le \lambda r.
\tag{E8}
\]

Now define local envelopes over the allowed model domains:

\[
\ell(s)=\min_{R,x}\mathcal L_s(R,x),
\tag{E9}
\]

\[
\sigma(\rho)=\min_{q,p}\mathcal S_\rho(q,p).
\tag{E10}
\]

Because every W and L group is a normalized nonnegative distribution,

\[
\boxed{
\sum_s M_s\ell(s)
+
\sum_\rho N_\rho\sigma(\rho)
\le \lambda r.
}
\tag{ENV}
\]

This is the direct pairwise-staircase envelope lemma.

### Proof

Equation (E8) follows by adding one valid pairwise-potential inequality, the nonnegative combination `sum tau_j T_j<=0`, and the exact equalities (E1)--(E3) with multipliers `mu`, `lambda`, and `-c` respectively. Each normalized L group has expectation of `mathcal L_s` at least `ell(s)`; each normalized W group has expectation of `mathcal S_rho` at least `sigma(rho)`. Substituting these lower bounds in (E8) proves (ENV). No density upper bound and no Farkas theorem is needed. QED.

## 4. Exact n=30 exceptional-state certificate

For the preserved exceptional state

```text
s   = [1,1,2,2,3,3,3,3,3,3,3,3,3]
rho = [1,1,1,1,1,1,1,1,2,3,3,3,3,3,3,3]
r = 31,
a = 13, b = 16, dmax = 11,
```

take

```text
lambda = 4698
c      = 5258
mu     = 6640
tau_2  = 461
tau_3  = 461
all other tau_j = 0.
```

Take the six BC staircases from the greedy-minimized exact certificate:

```text
weight 2322: (1,-2),(3,-4),(4,-6),(6,-8),(9,-9)
weight  955: (1,-1),(2,-4),(3,-9),(4,-13)
weight 1566: (1,-2),(2,-3),(3,-4),(4,-5)
weight 2215: (1,-1),(2,-4)
weight 1190: (1,-1),(2,-2),(3,-5),(6,-6),(7,-7),(8,-10),(11,-12)
weight 2826: (1,-3)
```

and the three indispensable SH staircases:

```text
weight 1459: (1,-1),(2,-5),(3,-6)
weight 1674: (1,-1),(2,-7)
weight 1998: (1,-1),(2,-2),(3,-11).
```

Here a BC generator `(D,-H)` represents the upper-set condition `d>=D` and `h<=H`; an SH generator `(S,-H)` represents `s>=S` and `h<=H`.

Exact local minimization gives:

| group | multiplicity | local minimum | first minimizing state |
|---|---:|---:|---|
| label `s=1` | 2 | 21030 | `(R,x)=(1,1)` |
| label `s=2` | 2 | 41590 | `(R,x)=(4,2)` |
| label `s=3` | 9 | 58659 | `(R,x)=(5,3)` |
| source `rho=1` | 8 | -19922 | `(q,p)=(2,1)` |
| source `rho=2` | 1 | -37093 | `(q,p)=(3,2)` |
| source `rho=3` | 7 | -44300 | `(q,p)=(2,4)` |

Therefore the left side of (ENV) is at least

```text
2*21030 + 2*41590 + 9*58659
+ 8*(-19922) + 1*(-37093) + 7*(-44300)
= 146602.
```

But

```text
lambda*r = 4698*31 = 145638.
```

Thus (ENV) would require

\[
146602\le145638,
\]

an exact contradiction with margin

\[
\boxed{964}.
\]

This is stronger and conceptually cleaner than the transformed Farkas certificate's `-881` margin because the normalization constants are reset to the exact local envelopes rather than inherited from a rounded dual proposal.

## 5. Why this matters for general n

The finite LP contradiction has now become a purely local optimization problem:

1. choose a small pairwise staircase potential `F+G` and a few threshold weights;
2. minimize the label score separately for each demand value `s`;
3. minimize the source score separately for each residual degree `rho`;
4. compare the resulting profile sum with `lambda*r`.

This is a far more plausible route to a parameterised all-n inequality than carrying W/L/Z distributions or Farkas multipliers. The next research target is to replace the finite six-plus-three staircase potential by a parameterised family whose envelopes can be bounded symbolically in terms of aggregate profile statistics.

## 6. Status boundary

The envelope lemma itself is an algebraic consequence of the candidate pairwise monotone-transport model and its graph-derived identities. The displayed n=30 contradiction is exact finite arithmetic. Neither establishes that the same staircase weights work for arbitrary profiles or arbitrary n. The universal graph-to-model validity remains the principal mathematical trust boundary.
