# N34: candidate bound 289; equality classification open

12 September 2026. Research direction: Paul Lenz. Development, computation
and internal checking: ChatGPT/Geeps.

**Candidate theorem: every simple diameter-two edge-critical graph G on
34 vertices satisfies e(G)<=289=floor(34^2/4).**

The bound is attained by K(17,17). Uniqueness at equality remains OPEN:
the Delta=18, m=289 branch retains its previously enumerated 13,546
conservative states. External mathematical review, novelty assessment and
external reproduction also remain OPEN. This package establishes the
candidate upper bound, not the equality classification or an all-order proof.

## Proof assembly

The [previous N34 reduction](../2026-09-12-frontier-v1/README.md) treats
bipartite graphs, the dense non-bipartite dominating-edge case, and all
target-range maximum degrees except Delta=18. It uses the audited canonical
bridge and the twelve-, thirteen-, fourteen- and fifteen-label bounds.
At Delta=18, `(a,b)=(15,18)` and `t=m-288`. The scalar bound Q<=26 gives
m<=292. The previous exact package excludes all 291- and 292-edge states.
It therefore suffices to exclude m=290, where t=2 and dmax=13.

The preserved frontier has 337 demand profiles and 1,614 conservative
`(s,rho)` states: 1,585 positive-demand and 29 with exactly one zero demand.
It comes from the complete 77,558,760-profile enumeration and conservative
residual expansion already preserved in the preceding package. We reuse
those exact inputs without altering their historical bytes.

The disjoint exclusion ledger is:

| Stage | States excluded | States remaining |
|---|---:|---:|
| Exact positive-demand degree mass | 463 | 1,151 |
| Tight total-demand hand lemma | 148 | 1,003 |
| Original fixed nine-rectangle integer envelopes | 761 | 242 |
| Tight heavy-label subset hand lemma | 51 | 191 |
| Fixed 13-term exact-budget integer envelopes | 49 | 142 |
| Adaptive monotone exact-budget integer envelopes | 142 | 0 |

Thus every m=290 state is impossible. Combined with the previous reductions,
this proves the stated candidate bound. No numerical infeasibility result
is used as an exclusion.

## New graph arguments and exact domains

The [bridge refinements](../../general_n/2026-09-12-exact-budget-threshold-v1/BRIDGE_REFINEMENTS.md)
prove the demand-deficit identity, the tight heavy-label subset lemma and
the exact-budget envelope implication in full.

Writing S=sum s and r=sum rho, positive demands require `r=S-4` exactly.
For a state with one zero demand, put `E=S-r-4`: its zero-demand label has
`d=R-E`, while every other label has `d=R+s`. The 29 zero-demand states are
covered by 11 subset hand contradictions, four fixed exact-budget
certificates and 14 adaptive certificates. The invalid substitution d=R
for an arbitrary zero-demand label is never made.

The subset lemma retains the heavy-incidence counts from the canonical
capacity proof. If `W_h=C_h(z_h)`, it forces

`W_h-h(h+1) <= sum_{rho_u>=h}(rho_u-1)`.

It does not assume that all selected incidences at a heavy source are heavy.
This is the reusable hand obstruction extracted from the present branch.

The new envelopes use the exact balance `sum R=r`, so lambda, c and mu are
free real multipliers; transport multipliers remain nonnegative. Label and
source options, and their compatibility inequalities, are given explicitly
in the bridge refinements and regenerated directly by `verify.py`.

The fixed potential is a sum of 13 nonnegative terms, preserved in
`extended_fixed.json` as `(kind,threshold,load_cutoff,weight)`. BC means
`[d>=threshold,h<=load_cutoff]`, SH means `[s>=threshold,h<=load_cutoff]`, and
DIAG means `[d-h>=threshold]`. The adaptive stage allows these same monotone
families over the finite domains `D=1..13`, `K=1..14`, `H=0..18`,
`L=-18..14`. Its 142 certificates have 19–63 nonzero potential weights each.
They are profile-specific finite certificates; no common scalar formula
for all orders is claimed.

## Evidence and internal audit

`verify.py` uses the Python standard library and the separately structured
frontier expansion. It does not import SciPy, NumPy or either discovery
program. It regenerates every local inequality, checks multiplier signs
and strict integer gaps, checks every hand contradiction, and verifies
disjoint, complete coverage through all three saved stages.

The replay passed **431,338 local integer inequalities**, 952 exact
certificates and all 662 hand/accounting exclusions. Worst integer gap
numerators are -9,858 (original potential), -9,866 (fixed exact-budget) and
-9,535 (adaptive). The full report is [verification.json](verification.json).

The baseline failures remain in `baseline.json`; fixed-envelope failures
remain in `extended_fixed.json`. Their numerical status is diagnostic only.
The initial fixed-stage run stopped before its final checkpoint; its saved
230 rows were resumed to all 242, and the adaptive run was extended from
137 to all 142 inputs. The exact coverage verifier detects missing rows
independently of process exit status. Logs preserve those checkpoints.
`after_subset_exploration.json` preserves the intermediate list of 191 states.

The [internal audit](AUDIT.md) records the reasoning checks and limitations.
The [reviewer package](../../../../releases/n34-bound-reviewer-v1/README.md)
contains dependency hashes, replay commands and publication provenance.

## Replay

From the repository root:

```sh
python project/research/n34/2026-09-12-m290-v1/verify.py
```

To replay the prior upper layers as well:

```sh
python project/research/n34/2026-09-12-frontier-v1/verify_upper_layers.py
```

Optional coefficient rediscovery requires NumPy and SciPy:

```sh
OPENBLAS_NUM_THREADS=1 python project/research/n34/2026-09-12-m290-v1/discover.py
OPENBLAS_NUM_THREADS=1 python project/research/n34/2026-09-12-m290-v1/extended.py
OPENBLAS_NUM_THREADS=1 python project/research/n34/2026-09-12-m290-v1/extended.py --adaptive
```

Different solver versions may propose different coefficients. Mathematical
acceptance requires the solver-free verifier; a stopped or incomplete
discovery run is not a proof event. `--resume` resumes saved extended stages.

## Next obligation

To establish equality only for K(17,17), exclude the Delta=18, m=289
branch. Its conservative input has 12,926 positive-demand states and 620
zero-demand states. The new exact identity and subset lemma are natural
first filters, but that branch has not been processed by this package.
