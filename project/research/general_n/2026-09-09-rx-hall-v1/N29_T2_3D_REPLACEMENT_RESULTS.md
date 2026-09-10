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

The returned SH3 weights in the four feasible deletion cases were all positive (approximately 0.552, 0.579, 1.928 and 0.892 respectively), so SH3 was genuinely used rather than merely available.

## Stronger all-SH challenge to D3

To test whether the failure to replace D3 was merely caused by choosing S=3, workflow run **34501406140** deleted D3 while retaining D2,D4,J0,J2 and allowed **all first-coordinate thresholds S=2,...,12** with free nonnegative common weights.

Artifact id: **10162006593**

Artifact SHA-256: `6c1ec47288f565ce067e475e967cbe20a7fe546bdaa885022a902bebf6e0e08c`

Result: **infeasible** on the same 107 profiles (41,316 inequalities; HiGHS status 2).

A nonnegative combination of the threshold basis S=2,...,12 represents an arbitrary nondecreasing separable step potential of the first coordinate on the relevant integer domain, up to an irrelevant constant. Therefore, within the tested basis:

> D3 cannot be replaced even by an arbitrary separable monotone s/rho potential while D2,D4,J0,J2 remain available.

This is substantially stronger than the single-SH3 failure. It says D3 is carrying genuinely joint (d,v) information that the full separable first-coordinate marginal does not recover on these obstruction profiles.

## Partial subset-lattice observation

A subsequent D3+SH3 subset-lattice run **34501297499** suffered a JSON serialization failure when it reached its first feasible case. Before the tooling failure it had already established that the following were infeasible:

- D3 + SH3 alone;
- D3 + SH3 + D2;
- D3 + SH3 + D4;
- D3 + SH3 + J0;
- D3 + SH3 + J2;
- D3 + SH3 + D2 + D4.

The next tested set, `D3 + SH3 + D2 + J0`, solved feasibly and then triggered the NumPy-integer JSON serialization bug. Hence that four-family set is already known floating-feasible on bad107. Since all one-optional-family sets above are infeasible, `{D3,SH3,D2,J0}` is inclusion-minimal in this lattice regardless of the outcomes of later subsets.

The serialization bug was fixed in commit **65a33d7a7208b96313151bce416c612dbfc8f847** and the complete 16-case lattice was re-run as workflow **34501499674**.

## Current interpretation

The best emerging structural picture is no longer that t=2 intrinsically needs all five projected families. Instead:

1. D3 appears genuinely fundamental in this RX-Hall basis;
2. one retained first-coordinate threshold SH3 can substitute for much of the projected D2/D4/diagonal information;
3. at least two additional ingredients beyond D3+SH3 are needed on the bad107 set, because every single optional-family extension is infeasible;
4. one explicit minimal feasible combination is `D3 + SH3 + D2 + J0`.

Before promoting any simplification, the inclusion-minimal lattice survivors must be tested on the full 902-profile t=2 frontier and then exactified with corrected scaling or direct rational/Fraction checking.
