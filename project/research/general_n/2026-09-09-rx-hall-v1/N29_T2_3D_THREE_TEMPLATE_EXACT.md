# n=29, t=2: exact minimal three-template 3-D certificate

## Status

**Exact finite RX-Hall result, conditional on the 3-D potential-certificate lemma and the graph-to-profile bridge.**

For the fixed 11-term primitive 3-D potential below, exactly **three** scalar bookkeeping templates are necessary and sufficient to cover all 902 regenerated `n=29, Delta=16, t=2` frontier profiles.

This is a finite certificate-compression theorem inside the RX-Hall model. It is not an unrestricted Murty-Simon theorem and does not by itself replace the current fixed-order reviewer proof chain.

## Fixed primitive potential

Let

- `B(D,V)=1[d>=D and v>=V]`,
- `J_2=1[d+v>=14]`,
- `J_0=1[d+v>=16]`,
- `SH3=1[s>=3]`.

Use

\[
\begin{aligned}
F={}&3B(3,6)+3B(3,7)+3B(3,8)+3B(3,9)\\
&+4B(3,10)+4B(3,11)+4B(3,12)+4B(3,13)\\
&+8J_2+7J_0+29SH3.
\end{aligned}
\]

There are 11 nonzero generators and the primitive weight sum is 72.

Equivalently, the `D3` staircase contribution is

\[
1_{d\ge3}\bigl(3\min(4,(v-5)_+)+4\min(4,(v-9)_+)\bigr),
\]

so the entire potential is one `D3` staircase, two diagonal thresholds, and one first-coordinate threshold.

## Three exact rational templates

All omitted scalar coefficients are zero.

### T0

\[
\lambda=12,\quad c=3,\quad
\tau_1=48/5,\quad \tau_3=4,\quad \tau_4=6,\quad
\tau_5=22/5,\quad \tau_7=1/4.
\]

Exact coverage: **734/902** profiles.

Minimum positive gap: **9/20**.

### T1

\[
\lambda=12,\quad c=13/2,\quad \mu_+=1,
\]

\[
\tau_2=13/5,\quad \tau_3=43/4,\quad \tau_4=13/2,\quad
\tau_5=7/2,\quad \tau_7=2/3.
\]

Exact coverage: **882/902** profiles.

Minimum positive gap: **227/60**.

### T2

\[
\lambda=12,\quad c=10,
\]

\[
\tau_2=46/3,\quad \tau_4=19/4,\quad \tau_5=14/3,\quad
\tau_6=5/4,\quad \tau_7=1/5.
\]

Exact coverage: **841/902** profiles.

Minimum positive gap: **7/3**.

The union covers all 902 profiles. Coverage multiplicity is:

- exactly one template: 40 profiles;
- exactly two templates: 169 profiles;
- all three templates: 693 profiles.

The exact cover checker uses only `fractions.Fraction`; no LP/MIP solver and no floating point participates in acceptance.

## Exact sufficiency replay

Workflow run: **34511664516**

Head commit: `2253aefe69a996a8ee2a09fa0ca83b7f9a518fd7`

Artifact id: **10166032194**

Artifact SHA-256:

`5af367b1693a62bc54ebd4ab3e877f678adb23911caf427daae98a275488a261`

Checker:

`n29_t2_sh3_c11_three_scalar_exact.py`

Result: **PASS**, 902/902 covered exactly.

## Exact necessity: incompatibility triangle

Profiles **0, 3, 77** are pairwise incompatible under one scalar template with this fixed potential.

The common-template system was deliberately weakened to require certificate gap merely **>=0**, rather than a positive normalized margin. For each pair

\[
(0,3),\qquad(0,77),\qquad(3,77),
\]

a sparse fixed rational Farkas multiplier vector is checked exactly.

For a pair system `A x <= b`, where the 16 scalar variables are nonnegative and envelope variables are free, each certificate satisfies:

- `y >= 0`;
- `y^T A_j >= 0` on every nonnegative scalar column;
- `y^T A_j = 0` on every free envelope column;
- `y^T b = -1`.

Thus each pair system is impossible even at common gap zero. Consequently no two scalar templates can cover the three profiles, so at least three templates are necessary.

Certificate supports are respectively 19, 19 and 20 rows.

### Exact necessity replay

Workflow run: **34512031841**

Head commit: `289db99db2eca2de1bc3ccd4097ae34b81db44e6`

Artifact id: **10166169205**

Artifact SHA-256:

`a483596bf81416bf703914afb027679f1154c30765bb5c8464f39f4796dcfadc`

Checker:

`n29_t2_sh3_c11_three_template_lower_bound_exact.py`

Result: **PASS** for all three pairwise Farkas certificates.

## Conclusion inside the fixed-potential model

\[
\boxed{\text{minimum scalar-template count}=3.}
\]

This is exact, not numerical: three explicit rational templates suffice, and a rational Farkas incompatibility triangle proves that two cannot suffice for this fixed potential.

## Structural interpretation

The earlier two-coordinate `t=2` certificate used a considerably richer potential. Restoring the first Hall coordinate has separated the geometry into a compact form:

1. the joint `D3` staircase carries the irreducible `(d,v)` information;
2. `SH3` restores first-coordinate information lost by the two-dimensional projection;
3. `J0,J2` provide the remaining diagonal slack corrections;
4. the 902 finite profiles reduce to exactly three scalar regimes under this potential.

The next high-value task is therefore not further finite certificate multiplication. It is to characterize those three regimes by simple statistics of `(s,rho)` and then ask whether the resulting regime inequalities extend symbolically in `n,t`.

## Trust boundary

Everything in the finite cover and template-count lower bound is exact arithmetic. The universal mathematical trust boundary remains the derivation of the RX-Hall/profile constraints from an actual diameter-2-critical graph and the 3-D monotone transport/potential lemma. Independent human audit remains open.
