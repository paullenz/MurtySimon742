# Murty–Simon / Erdős #742 — current state handoff

**14 September 2026. Latest mathematical checkpoint: conditioned spill slack and the row-295 equality obstruction. Proof `ab132ffd4c82f50d4ffe2120e8167c861e7ba6a6`, executed verifier `0baedfab7df5870fdd8b475d7eed8163f075844f`, frozen result `73d06b1990b0995df7b78b2cf9226c730d6a9dcb`. Historical-source recovery `caaae9a6b6e5fc6d0bfacfd9185947037c95859f`; hash-strict materialization/CI `e50f4a95b2420835bc2aa8a50e3334e75a0da996`. Inspect newer commits and current run information before resuming.**

Canonical repository: `paullenz/MurtySimon742`, ID `1359206057`. The entire preceding block-pressure handoff is preserved verbatim in [CURRENT_STATE_PRE_CONDITIONED_2026-09-14.md](CURRENT_STATE_PRE_CONDITIONED_2026-09-14.md); the previous root overview is [README_PRE_CONDITIONED_2026-09-14.md](README_PRE_CONDITIONED_2026-09-14.md). Their earlier queue statuses and research priorities are historical. Begin with [RESEARCH_EVIDENCE_INDEX.md](RESEARCH_EVIDENCE_INDEX.md) for dependency and verification scope.

## Canonical frontier and promotion boundary — unchanged

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered relational candidates: 2,655 — UNPROMOTED
```

The fixed-order candidates n25 and n27 through n35 and the general 7/12 candidate theorem are unchanged; external mathematical review, novelty assessment and third-party reproduction remain OPEN. The synthetic profiles below are not graphs, whole canonical scalar states or unresolved obligations in those reviewer packages. Preserve both reviewer-navigation surfaces.

Do not promote the recovered candidates. The required chain is exact coverage of all 2655 inputs, both relational implementations agreeing state by state, zero unresolved states, successful aggregate, then a separate reviewed ledger step. Preserve N34/N35 provenance and the existing closure-ledger validator. The discovery SHA256 remains `2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970`.

## CI and actual evidence inspected

Capped-spill run `34885163695` was directly rechecked and has completed SUCCESS, including exact synthetic regeneration and its full frozen comparisons. Combined capped/block-pressure run `34887492789` has also completed SUCCESS. The downloaded combined artifact is `10364839603`, archive SHA256 `08b3df5892c99c5fb8acc728052e1355ffe51a3af2d6d965c248d2003fe0e5a1`. Both complete actual/expected JSON pairs were compared locally and agree.

Its complete, 257-job audit snapshot is timestamped **2026-09-14 19:43:10.495414 UTC**:

```text
audit 34854911792:
  successful plan:          1
  successful audit shards:128
  queued audit shards:    128
  successful aggregate inspected: NONE
```

This is NOT a current run-level inference or a claim of full audit completion. Earlier snapshots at 19:17 and 18:55 are preserved, not silently rewritten. Recheck every job page or a newer complete diagnostic before reporting current progress. Do not cancel/duplicate the full audit, restart successful or queued work, alter budgets/concurrency, or retry computational timeouts without review. Individual failed/cancelled jobs may be retried once only after their logs establish transient infrastructure failure. Hash or frozen-value disagreements are blockers.

The new conditioned-verification/evidence-publication run is **34894544147**, job104145146205. It remained QUEUED at direct inspection. It is a new proof/preservation scope, not a retry of the large audit. It runs the full new verifier, checks every source/artifact hash, regenerates historical output bytes and publishes only verified data in the evidence directory. Do not claim remote PASS or completed durable publication before checking the run and committed materialization record. Its writes do not touch the promoted ledger.

The existing hourly GitHub automation remains separate from ongoing mathematical work; preserve its conservative retry and notification rules. Internal CI success is not external mathematical acceptance.

## Notation and retained canonical requirements

```text
Q=r+2t+D0+Esel,
D0=S-r-2t>=0,
Esel=Q-S>=0,
x_i=s_i+e_i, e_i>=0,
c_u=q_u+rho_u<=a, rho_u>=1,
d_u=(p_u-rho_u+1)_+.
```

`t` is structural surplus, `tau` a q threshold, `eta` a demand-block threshold. Never silently assume z<=Esel. Selected ui implies s_i<=rho_u; at a selected POSITIVE-demand label, d_u<=e_i. Retain all legitimate caps: incoming/residual, simple degree, exact potential-pair, selected excess, localized and all-source spill. Negative caps mean infeasibility, never clipping.

The preceding source-specific charge envelope independently maximized the best sources for each label and the excess distribution. Its optimum was a safe UPPER bound, not a jointly realizable selected matrix. The new step couples the cap and this envelope to the SAME exact block-excess total.

## New universal conditional lemma

Read [the conditioned proof](project/research/general_n/2026-09-14-conditioned-excess-v1/README.md). For any label set L containing all zero-demand labels, with eligible source labels A_u={i:s_i<=rho_u}, put

```text
S_L=sum_{i in L}s_i,
f_u=(q_u-|A_u outside L|)_+,
M=sum_u f_u,
m_u=|A_u intersect L|.
```

Fix the ACTUAL excess e_L on L and define J=S_L+e_L-M, E_H=Esel-e_L. Necessarily J>=0. If k_u counts actual low-block selections, then sum k=M+J and k_u>=f_u. Hence

```text
k_u<=kmax_u=min(q_u,m_u,f_u+J).
```

Whenever q_u>kmax_u,

```text
p_u<=rho_u-1+floor(E_H/(q_u-kmax_u)).
```

The distinct selected labels outside L are positive-demand and each needs at least d_u excess. This proves the inequality. It neither assumes a q-tail theorem nor double-counts the source's forced spill.

For L={s<=eta}, split exhaustively over integer e_L from max(0,M-S_L) to Esel. Use the resulting cap AND an exact e_L constraint in the top-source upper-envelope DP. Every actual incidence system lies in one such branch. Empty/full conditioning blocks have their explicit exact totals. Rejecting every branch excludes the profile; finding one non-rejected branch is not graph realization.

## Hand resolution of row 295: equality would require 10<=8

Row295 has a24,b28,Q109,r79,t1,D0=0,Esel28; demands are 1 twice, 2 three times, 3 three times and 4 sixteen times. Twelve sources with (q,rho)=(2,1) must select BOTH low labels. This forces low-label excess e_L>=22, leaving at most six above that block.

The proof note and verifier give the exact source-ceiling score table: every label of demand2,3,4 with excess e<=6 contributes at most5e. The two demand-one labels contribute at most4(2+e_L). Thus actual selected charge C=sum q_u d_u satisfies

```text
C<=4(2+e_L)+5(28-e_L)<=126.
```

The orientation balance gives sum d>=109-sum(rho-1)=58. All q>=2, exactly twelve q2 sources have d<=4, so C>=3*58-12*4=126. Feasibility forces equality everywhere. In particular e_L=22 and both low-label selected columns are completely filled by the twelve forced sources; every q>3 source has zero pressure.

The four q3 sources would need total pressure10. None can use the already-filled low labels, so each selects three other distinct positive labels. Total excess there is only six; each q3 pressure is at most2, giving total at most8. Contradiction:10<=8.

This is a short hand certificate, not a numerical optimizer claim. Additional singleton column bounds alone did not lower the old optimum126; that unsuccessful attempt is preserved in the exploration directory.

## Exact finite branch coverage and tests

The final verifier directly replays ALL twelve preceding non-rejections. It is standard-library code with source blob `412356d3585e2fda845434868e52653a58852aee`, matched against the locally executed file. It implements the new conditional cap/DP separately and uses prior modules only for earlier caps and receiver arithmetic.

```text
selected-incidence configurations: 9,293
conditioned inequalities:          42,649
independent brute comparisons:      2,000
  nonempty projections:              143
standing hostile examples:              3
prior remainder inputs replayed:        12
newly excluded sampled rows: 295,365,570
```

Complete exclusion branches:

```text
row295: eta1, e_L22..28
row365: eta1, e_L22..38
row570: eta2, e_L43..49
```

Every value in each stated range is rejected by total capacity, empty necessary projection or a strict integer price/envelope inequality. Examples include129>126,206>205 and242>241. All branch values, including non-excluding attempts for other profiles, are emitted by the full verifier.

Cumulative sampled-corpus position: **704/713 rejected, nine not rejected**. Prior701 exclusions are retained; this new session does NOT claim a fresh independent generation of all713 profiles or a whole-state scan. Remaining rows:

```text
108,160,240,258,338,342,347,471,586.
```

The preceding twelve full arrays remain committed in `2026-09-14-block-pressure-v1/REMAINDER_12.json`. No input was deleted to hide a failure.

## Documentation, exact output and preservation gates

Use [REPRODUCE.md](project/research/general_n/2026-09-14-conditioned-excess-v1/REPRODUCE.md). The complete canonical JSON replay SHA256 is

```text
7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e
```

This binds unsuccessful branches too. `FROZEN_RESULT.json` includes all new exclusion certificates and explicitly marks omitted unsuccessful detail in its compact display; the full deterministic replay reconstructs all of it with committed inputs alone.

The [evidence-preservation package](project/research/general_n/2026-09-14-evidence-preservation-v1/README.md) recovers eleven original exploratory source files, a convenience prior copy and five full block-output objects from the portable bundles. Source blobs were checked byte-for-byte. Historical numerical multiplier failures remain non-proofs. Two large capped historical outputs were regenerated locally with exact original byte hashes. The new materializer also passed locally, checking17 source/output files, raw artifacts and the entire conditioned result.

Raw corpus, original scanner, pilot/812 inputs, combined-CI outputs, full queue snapshots, the two large historical outputs and the complete conditioned replay are to be committed by the hash-strict seal workflow into `durable/`. Only an inspected successful committed `MATERIALIZATION_STATUS.json` establishes that publication. If the run remains queued, the dependency is explicit; do not call the repository archival work fully sealed. The portable session bundle retains all original inputs and outputs meanwhile.

Bad long encoded archive transfers were detected and removed from the working tree, with errors retained in Git history and `TRANSFER_ERRATUM.md`. They were never accepted as evidence. The mathematical verifier and frozen result remained intact. Readable replacements have matching original hashes; never weaken a hash gate to accept a transfer.

## Next mathematical target and trust boundary

Enforce common excess totals across multiple demand blocks, or the joint incidence constraints lost by independently choosing each label's best sources. The nine remaining profiles are concrete boundary tests. A universal theorem must force a contradiction from full canonical structure, not from extrapolation of the sample.

Retain exact q-layer/mincut, crossing-wall/saturation and independent maximum-cut/stability routes and all hostile cases. Check monotonicity before transferring old witness theorems to new caps. Actual graph orientations satisfy Hall; other bridge constraints must force the contradiction. No queue label, timeout, missing output, failed numerical search or internal green run is an external proof. The canonical graph-to-selected/residual bridge remains the principal correlated review dependency.
