# n=29, t=2: restoring the first Hall coordinate

Date: 2026-09-10

Status: **structural floating-point reconnaissance inside the RX-Hall relaxation.** These tests do not alter the fixed-order n=29 theorem package and remain conditional on the graph-to-RX-Hall bridge. The trusted exact t=2 certificate remains the preserved 16-generator potential until any 3-D simplification is exactified.

## Setup

The two-coordinate BC/DST screen on the 107 profiles obstructing the naive three-term potential found that every family in

\[
D2+D3+D4+J_0+J_2
\]

was individually indispensable within that 2-D family basis.

The exact incidence coupling, however, is three-dimensional:

\[
(s,d,v)\le (\rho,\alpha,w).
\]

Therefore for every threshold \(S\),

\[
\sum_i x_i\,\mathbf 1[s_i\ge S]
\le
\sum_u q_u\,\mathbf 1[\rho_u\ge S].
\]

The natural t=2 threshold is \(S=t+1=3\).

## Single SH3 replacement screen

Workflow run **34500939994**, artifact **10161837947**, artifact SHA-256

`b15d748c00902b543fc84a82f4a60875fc22a56907246367e25df8b105e64c28`.

On the 107 obstruction profiles, add one free common SH3 term and delete one 2-D family at a time:

| deletion | result with SH3 |
|---|---|
| D2 | feasible |
| D3 | **infeasible** |
| D4 | feasible |
| J0 | feasible |
| J2 | feasible |
| none | feasible |

Thus the earlier five-family irreducibility is largely a projection effect: the first coordinate can replace D2, D4, J0 or J2 individually. D3 is the unique family in this screen that survives the 3-D challenge.

The returned SH3 weights in the four feasible deletion cases were all positive, so SH3 was genuinely used rather than merely available.

## Stronger all-SH challenge to D3

Workflow run **34501406140** deleted D3 while retaining D2,D4,J0,J2 and allowed **all first-coordinate thresholds S=2,...,12** with free nonnegative common weights.

Artifact id: **10162006593**

Artifact SHA-256: `6c1ec47288f565ce067e475e967cbe20a7fe546bdaa885022a902bebf6e0e08c`

Result: **infeasible** on the same 107 profiles (41,316 inequalities; HiGHS status 2).

A nonnegative combination of S=2,...,12 represents an arbitrary nondecreasing separable step potential of the first coordinate on the relevant integer domain, up to an irrelevant constant. Therefore, within the tested basis:

> D3 cannot be replaced even by an arbitrary separable monotone s/rho potential while D2,D4,J0,J2 remain available.

This is substantially stronger than the single-SH3 failure. D3 carries genuinely joint (d,v) information that the full separable first-coordinate marginal does not recover on these obstruction profiles.

## Complete D3+SH3 subset lattice

The first lattice run **34501297499** found its first feasible case and then suffered a NumPy-integer JSON serialization failure. That tooling bug was fixed in commit **65a33d7a7208b96313151bce416c612dbfc8f847**; the unchanged 16-case lattice then completed successfully in workflow run **34501499674**.

Artifact id: **10162097192**

Artifact SHA-256: `00c23be6b98bff3fc383c9bda777614d627ed2ae0f4a9d87992ce11dc860a6d9`

D3 and SH3 were held present; every subset of optional families `{D2,D4,J0,J2}` was tested on bad107.

All zero- or one-optional-family cases were infeasible. Among two-optional-family cases:

| optional families beside D3+SH3 | result |
|---|---|
| D2 + D4 | infeasible |
| **D2 + J0** | **feasible** |
| **D2 + J2** | **feasible** |
| D4 + J0 | infeasible |
| D4 + J2 | infeasible |
| **J0 + J2** | **feasible** |

Consequently the exact inclusion-minimal family sets in this lattice are

\[
\{D3,SH3,D2,J_0\},
\qquad
\{D3,SH3,D2,J_2\},
\qquad
\{D3,SH3,J_0,J_2\}.
\]

Every three-optional-family superset containing one of these was feasible, as was the full family. In particular, **D4 is absent from every inclusion-minimal 3-D survivor**.

The three minimal floating optima used respectively 17, 14 and 11 active individual generators; their SH3 weights were approximately 0.9003, 2.4042 and 0.6391.

## Current interpretation

The best structural picture is therefore:

1. D3 is the robust joint-geometry component: it survives both the single-SH3 and arbitrary-all-SH replacement attacks.
2. SH3 captures enough of the discarded first Hall coordinate to eliminate D4 entirely from every minimal family survivor on bad107.
3. D3+SH3 alone, or with any one of D2/D4/J0/J2, is insufficient.
4. Exactly three two-optional-family combinations survive on bad107: `D2+J0`, `D2+J2`, and `J0+J2`.
5. This is a family-level result, not individual-generator minimality and not yet proof-grade.

All three minimal survivors are now being promoted to the full 902-profile t=2 frontier in `n29_t2_sh3_minimal_families_full902.py`. Only full-frontier survivors should be support-pruned and exactified; the trusted 16-generator t=2 certificate remains the proof-grade finite result in the meantime.
