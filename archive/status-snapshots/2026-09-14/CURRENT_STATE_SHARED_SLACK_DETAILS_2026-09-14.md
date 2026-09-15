# Murty–Simon / Erdős #742 — current state handoff

**14 September 2026. Latest checkpoint: shared block-slack pressure. Plan `e8a64d4af782a17ceae368e6218a7aa37ce1db05` preceded the experiments. Proof `a1e93b3fd1415bcaba64b71d75436d31a18a4b82`, hardened hand explanation `4ad8657beff74c3bc075f9d0fb1b71a7bb1ffd06`, verifier `bed3e780d48327e8d09897c222707e28912141a8`, complete original-sample output `7e92fc952a141a807b80c33f9a22b61f3663de7c`, fresh output `8622562f8c2d0fbb3e1d363273d8b366ee882db5`. Inspect newer commits and current CI before resuming.**

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Read [RESEARCH_EVIDENCE_INDEX.md](RESEARCH_EVIDENCE_INDEX.md), [the shared-slack proof](project/research/general_n/2026-09-14-joint-blocks-v1/README.md), and [offline reproduction](project/research/general_n/2026-09-14-joint-blocks-v1/REPRODUCE.md). Prior detailed handoffs and proofs remain in named archives and Git history; the immediately preceding conditioned/sealed handoff remains accessible at the parent history of this commit. Nothing is silently removed or upgraded to external acceptance.

## Canonical frontier — unchanged

```text
whole-state closures:            977
canonical exclusions:          1,971
canonical survivors:           3,607
  N34-derived:                 3,529
  N35-derived:                    78
recovered relational candidates:2,655 — UNPROMOTED
```

The fixed-order candidates n25 and n27 through n35, plus the general7/12 candidate, are unchanged and externally unreviewed. The sampled profiles below are not canonical scalar states or actual graphs. Do not promote the2,655 candidates: require full exact coverage, both implementations agreeing state by state, zero unresolved, a successful aggregate and a separate reviewed ledger step. Preserve N34/N35 provenance and reviewer navigation.

## Documentation first; publication repaired and inspected

The starting plan recorded the verified conditioned checkpoint and proposed joint-block work BEFORE experiments. The preceding durable evidence is fully committed in `b6a15db114d7b4f3b71d73da816daec563f11824`; publication-only run34895776658 was directly checked SUCCESS. It reused the verified bytes and did not rerun the large audit. All16 durable files and manifest hashes are recorded in [PUBLICATION_AUDIT.md](project/research/general_n/2026-09-14-evidence-preservation-v1/PUBLICATION_AUDIT.md).

Run34894544147 passed mathematical and hash verification, but its overall status remains FAILED because an unclean checkout blocked rebase. Do not relabel it green or call it a mathematical discrepancy. The independent publication-only repair succeeded. Dedicated capped-spill34885163695 and combined capped/block34887492789 also passed. These scopes and external acceptance remain separate.

## Shared-slack theorem

Keep Q=r+2t+D0+Esel, e_i=x_i-s_i>=0, rho_u>=1, q_u+rho_u<=a. Structural surplus is t; q threshold tau; demand-block threshold eta. Every selected positive-demand label satisfies d_u=(p_u-rho_u+1)_+<=e_i. Retain all legitimate earlier target caps, particularly exact potential-pair degrees. Negative caps reject a branch; z is never silently bounded by Esel.

For any label block L containing EVERY zero-demand label, let A_u be eligible labels and define

```text
f_u=(q_u-|A_u outside L|)_+,
m_u=|A_u intersect L|,
S_L=sum_L s_i, M=sum f_u.
```

Fix its ACTUAL excess e_L, and let H=Esel-e_L and J=S_L+e_L-M. Actual low-block selected counts satisfy k_u>=f_u and sum_u(k_u-f_u)=J. For d>0, distinct positive labels outside L force k_u>=q_u-floor(H/d). Define

```text
gamma_u(0;H)=0,
gamma_u(d;H)=(q_u-f_u-floor(H/d))_+ for d>=1.
```

Admissibility also requires max(f_u,q_u-floor(H/d))<=m_u. The central new necessary inequality is

```text
sum_u gamma_u(d_u;H)<=J,
H+sum_u gamma_u(d_u;H)<=Esel+S_L-M.
```

The shared J cannot be independently spent by every source. At J=0 this recovers the tight-block mechanism behind row295. A group with d>=h and q-f>=v must have cardinality at most floor(J/(v-floor(H/h))) whenever the denominator is positive. The proof uses one actual incidence matrix; it does not sum overlapping high-label excess as if disjoint.

The exact integer DP maximizes total pressure with these per-source options and ONE total slack budget. It is exact only for this explicit relaxation. For a tail interval receiver box A, free=min(A,rho-1) and pressure limit A-free, every actual tail must satisfy Q_tau<=sum free+DP maximum. Tail pressure is at most full pressure and the slack cost is nondecreasing. No universal q-tail sufficiency, equality of Hall minima or fixed-q monotonicity is assumed.

## Three new ORIGINAL sample exclusions

The new calculation directly tests the NINE conditioned non-rejections and retains parent rejected branches through the pinned full parent certificate. All branch ranges are explicitly accounted for:

```text
row240 eta2: parent e_L39,40; new41..45
row258 eta2: parent38..41; new42..48
row342 eta3: parent33,34; new35..41
```

Original713-profile sample: **707 rejected, six not rejected**:

```text
108,160,338,347,471,586.
```

This is not a three-state reduction of the3,607 frontier. The previous701 block-pressure and three conditioned exclusions retain their own verification scopes. The unified new harness reruns the parent conditioned proof before accepting its branch coverage.

A hand-readable row240 branch has eta2,e_L41,H4,J2. Tail demand104, free capacity28, zero-slack pressure74. With ONLY two slack, at most one further pressure unit is affordable:28+74+1=103<104. Some larger gains cost three or more slack and are unavailable; the initial broad wording about every marginal unit costing two was corrected explicitly. Exact capacities for e_L41..45 are103,101,102,102,102. The earlier draft's103 for e_L44 was a conservative bound; exactDP gives102. Verifier, frozen result and theorem were unchanged.

## Tests and hostile boundary

Completed local shared-slack checks:

```text
exhaustive actual incidence systems: 9,293
arbitrary low-label blocks:         25,391
  positive-slack blocks:            12,305
fresh random incidence attempts:    10,000
  legal source/label projection:     7,839
independent brute comparisons:       3,000
  pressure vectors checked:        237,067
standing hostile q-tail examples:        3
```

The random-incidence domain need not satisfy the positive-surplus scalar ledger; it tests the lemma on actual selected matrices. The separate synthetic corpus below does satisfy its stated scalar ledger but is not graph-realized.

Preserved false shortcut: sum_u(q_u-k_u)d_u<=H fails for X=[[1,0],[1,0]], s=[1,0], rho=[1,1], d=[1,1], low block={zero label}. Both sources share one positive label, whose total excess is1 but summed incidence charge2. The valid theorem charges spare low-block selections instead.

## Simultaneous blocks: negative full-profile result retained

The partition cap uses ONE vector of equal-demand-block excess totals. A source of positive pressure d can use at most min(block size,floor(block excess/d)) labels in each eligible positive block; zero labels are handled separately. Coupling these caps with exact block totals in the previous charge envelope tests597 surviving tuples:25 total-capacity rejections,118 priced rejections,454 retained tuples across all six original remaining profiles.

**No additional profile closure.** This experiment does not exhaust all multiresource shared-slack inequalities or jointly realize source/label incidences. `explore_multiblock.py` and the exact full-output digest are committed; the full larger output is deterministically reconstructible and retained in the portable bundle/CI outputs, not claimed as a raw committed JSON file.

## Fresh synthetic sample: separate namespace

Seed74220260919 was fixed before inspecting its results. The original hash-pinned generator was changed only in its two seed literals.100,000 trials reproduce44451 scalar-domain cases,5539 cap passes,1496 incidence passes and715 pair-flow passes,53 with zero demands. Raw TSV SHA256:

```text
f0e32e99a66d51027d1ad89d9f3874a8d50b3d4d215e8e1dd0d816786504dc2e
```

Fresh715-profile results:701 capped-spill exclusions,3 additional block-pressure,1 additional conditioned,3 additional shared-slack; **seven not rejected**. The new shared rows are163,362,687. Fresh non-rejections:20,91,391,490,528,562,677. Their complete arrays and all three new branch certificates are in `FRESH_RECHECK_FULL.json`. These row IDs are NOT original713 row IDs. New seed means out-of-sample reconnaissance, not independently designed generation or actual canonical graphs.

## Reproduction, transfer checks and new CI

`run_replay.py --outdir /tmp/shared-slack-replay` provides an offline repository-root-aware chain: source hashes, parent proof, new shared checks, fresh raw corpus, complete fresh result and full negative multiblock replay. Python standard library and g++17 only; no artifact download or optimizer needed. The committed source/result blobs were checked against locally executed outputs. The generator helper itself reproduced the exact fresh bytes.

Canonical full-output hashes:

```text
parent: 7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e
shared: 35d4c3c05595102b2a568d986d8bab753059da4a2c59b31689a550aaddb23ce6
fresh: 754774a0d4fdb23c8403efe4c5e41f2df950ebf933f903ca7e3d335d6ce370f9
multi: d979d53bad1239b65442265b477594cffa05ec67750d8be6b3123add2b2b5127
```

The new whole-harness CI is34898768799, triggered by `de4cdce81db75301b622874fdfe6f5c792e89b7a`; it was QUEUED at first inspection. Completed component tests do not imply this separate end-to-end remote gate passed. Preserve any failure and do not weaken hashes or frozen values. The workflow is read-only, uploads all outputs even on failure, and does not alter relational-audit budgets or concurrency.

For the large relational audit34854911792, use complete current job pages or a complete newer diagnostic. No new live count is asserted here. Historical snapshots remain durable. Do not retry queued/running/successful jobs, duplicate the256-shard audit or restart timeouts without review. The hourly automation continues under its conservative rules; it is not autonomous mathematical work between turns.

## Next target and trust boundary

Attack common selected-source usage across several blocks, or the full multiresource version of shared slack. Independent per-label best-source choices can still be incompatible, so surviving current upper bounds is not realization. Use the six original and seven fresh examples as separate hostile laboratories; do not infer a universal theorem from their counts.

Retain exact q-layer/mincut, crossing-wall/saturation and maximum-cut/stability routes. The canonical graph-to-selected/residual bridge remains the principal correlated external-review dependency. Hand derivation, local tests, separately structured same-assistant arithmetic, remote CI, durable publication and external acceptance are distinct. No timeout, missing output, failed numerical search or repository commit certifies a graph-theoretic exclusion by itself.
