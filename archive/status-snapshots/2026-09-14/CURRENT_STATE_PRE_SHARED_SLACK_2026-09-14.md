# Murty–Simon / Erdős #742 — current state handoff

**14 September 2026. Latest mathematical checkpoint: conditioned spill slack and the row-295 equality obstruction. The full research evidence is now sealed in the repository at `b6a15db114d7b4f3b71d73da816daec563f11824`. Inspect newer commits and current CI before resuming.**

Canonical repository: `paullenz/MurtySimon742`, ID1359206057. Read [RESEARCH_EVIDENCE_INDEX.md](RESEARCH_EVIDENCE_INDEX.md), [the full conditioned proof](project/research/general_n/2026-09-14-conditioned-excess-v1/README.md), and [the publication audit](project/research/general_n/2026-09-14-evidence-preservation-v1/PUBLICATION_AUDIT.md). The entire immediately preceding detailed handoff is preserved verbatim in [CURRENT_STATE_PRE_SEALED_2026-09-14.md](CURRENT_STATE_PRE_SEALED_2026-09-14.md). Its queued publication observations are superseded below; its mathematical details remain valid. Earlier root overviews and handoffs are retained unchanged in their named archives and Git history.

## Canonical frontier and review boundary — unchanged

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered relational candidates: 2,655 — UNPROMOTED
```

No synthetic-profile rejection changes this ledger. Promotion requires exact coverage of all2655 inputs, both relational implementations agreeing state by state, zero unresolved states, successful aggregate and then a separate reviewed ledger step. Preserve N34/N35 provenance and the existing closure-ledger validator. The fixed-order candidates n25,n27 through n35 and general7/12 theorem are unchanged; external review, novelty assessment and third-party reproduction remain OPEN.

## Completed verification and publication

- Capped-spill `34885163695`: directly rechecked SUCCESS, including exact corpus regeneration and complete frozen checks.
- Combined capped/block `34887492789`: SUCCESS; both complete actual/expected pairs downloaded and locally compared. Artifact10364839603, archive SHA256 `08b3df5892c99c5fb8acc728052e1355ffe51a3af2d6d965c248d2003fe0e5a1`.
- Conditioned/seal `34894544147`: the MATHEMATICAL AND HASH VERIFICATION STEPS PASSED, but the overall run FAILED when rebase refused unstaged runner-checkout changes. Evidence upload succeeded. Do not misclassify this as a mathematical or hash failure, or falsely call the whole run green.
- Publication-only repair `34895776658`: SUCCESS. It preserved the successful computation, rechecked the pinned artifact bytes, and used non-forced Git tree publication rather than a dirty checkout. All16 verified files are committed at `b6a15db114d7b4f3b71d73da816daec563f11824`. The committed manifest was fetched back and checked.

[PUBLICATION_AUDIT.md](project/research/general_n/2026-09-14-evidence-preservation-v1/PUBLICATION_AUDIT.md) records the failure, repair, hashes, exact scope and successful publication. The old seal workflow is retained historically; do not blindly retry its known unclean-checkout publication path. No mathematical verification was weakened and no audit was duplicated.

## Large relational audit: snapshot, not promotion

The most recent COMPLETE diagnostic inspected in this research session is the combined artifact's full257-job snapshot at **2026-09-14 19:43:10.495414 UTC**: successful plan,128 successful audit shards,128 queued shards, no accepted aggregate. It is now committed in the durable inputs directory. This is a timestamped historical snapshot, not a claim of current audit completion.

For current status, fetch every jobs page or a newer complete diagnostic. Never infer stalling from a run-level queued label or the first page. Preserve completed work. Retry one individual failed/cancelled job only after logs establish transient infrastructure failure, at most once per distinct failure. Do not restart computational timeouts, queued/running/successful jobs, duplicate the256-shard audit, or change budgets/concurrency. The existing hourly monitor retains these conditions. The2655 candidates remain unpromoted.

## New mathematical result and exact scope

Keep Q=r+2t+D0+Esel, D0=S-r-2t>=0, Esel=Q-S>=0 and x_i=s_i+e_i. Structural surplus is t; q threshold tau; label threshold eta. All zero-demand labels must be treated explicitly and z is never silently bounded by Esel. The canonical bridge gives rho>=1, q+rho<=a, selected-label eligibility s_i<=rho_u and positive-label endpoint pressure (p_u-rho_u+1)_+<=e_i. All earlier legitimate caps remain in use.

For any label block L containing all zero-demand labels, let A_u be eligible labels, f_u=(q_u-|A_u outside L|)_+, M=sum f_u, S_L=sum_L s_i and m_u=|A_u intersect L|. Fix the ACTUAL excess e_L in L; J=S_L+e_L-M>=0. Actual low-block selection counts satisfy

```text
k_u<=kmax_u=min(q_u,m_u,f_u+J).
```

When q_u>kmax_u, distinct selected positive-demand labels outside L imply

```text
p_u<=rho_u-1+floor((Esel-e_L)/(q_u-kmax_u)).
```

Use the SAME e_L in this cap and the integer top-source upper envelope, and exhaust every admissible integer value. Earlier relaxations separately spent the excess differently; this coupling removes that freedom. No universal q-tail theorem, joint graph realization or complete weight-family claim is assumed.

Row295 now has a short hand proof. Twelve (q,rho)=(2,1) sources must fill both demand-one labels, forcing e_L>=22 out of Esel28. Actual charge C=sum q_u(p_u-rho_u+1)_+ has lower126 and upper148-e_L<=126. Equality forces e_L22, fully occupied low columns, zero pressure on q>3 sources, and total pressure10 on four q3 sources. Each q3 source must select three other distinct labels, but total remaining excess is6, so each pressure is at most2 and their total at most8. Contradiction:10<=8. The source-cap table and each equality implication are explicit in the proof and verifier.

Complete conditional branches exclude sampled rows295,365,570: eta1/e_L22..28, eta1/e_L22..38 and eta2/e_L43..49 respectively. Frozen examples include129>126,206>205 and242>241. The cumulative sampled position is **704/713 rejected, nine not rejected**:

```text
108,160,240,258,338,342,347,471,586.
```

This new replay directly checks the earlier12 remainder profiles and retains the preceding701 exclusions. It is NOT a fresh independent full713 generation or any canonical whole-state enumeration. All original arrays remain preserved.

## Reproduction and durable source of truth

[REPRODUCE.md](project/research/general_n/2026-09-14-conditioned-excess-v1/REPRODUCE.md) is an offline standard-library replay. Completed checks:9293 actual selected-incidence configurations,42649 conditioned inequalities,2000 independent brute comparisons including empty projections, all3 standing hostile examples and all12 inputs. The verifier reuses prior cap/receiver modules but separately implements the conditioned cap and DP.

Full canonical output SHA256:

```text
7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e
```

This binds unsuccessful branches and non-rejections too. The [full output](project/research/general_n/2026-09-14-evidence-preservation-v1/durable/CONDITIONED_EXCESS_FULL.json), [nine profiles](project/research/general_n/2026-09-14-evidence-preservation-v1/durable/REMAINDER_9.json) and [manifest](project/research/general_n/2026-09-14-evidence-preservation-v1/durable/MATERIALIZATION_STATUS.json) are now actual committed files, not future promises.

The durable archive also contains the original713 corpus, frozen scanner, pilot and812 inputs, completed combined-CI outputs and full audit snapshots, and both historical capped outputs regenerated byte-for-byte. Eleven exploratory source files, prior-module copy and five full block-output objects were recovered in readable form; source hashes match original bundles. Numerical exploration and unsuccessful singleton bounds remain recorded as non-proofs. Bad encoded-transfer attempts were rejected and documented in TRANSFER_ERRATUM.md, not accepted as evidence.

Latest proof/verifier/frozen commits: `ab132ffd4c82f50d4ffe2120e8167c861e7ba6a6`, `0baedfab7df5870fdd8b475d7eed8163f075844f`, `73d06b1990b0995df7b78b2cf9226c730d6a9dcb`. Documentation and readable recovery: `63fc1e5e6f5e6ead63f5ca3753618d870b917a22`, `caaae9a6b6e5fc6d0bfacfd9185947037c95859f`. Final data publication: `b6a15db114d7b4f3b71d73da816daec563f11824`.

## Next priority and trust boundary

Attack common excess totals across several blocks, or the joint incidence constraints lost by choosing each label's best sources independently. The nine explicit non-rejections are boundary evidence, not graph constructions. The universal goal is a contradiction forced by the FULL bridge, not extrapolation of sample success.

Retain exact q-layer/mincut, crossing-wall/saturation and independent maximum-cut/stability routes. Check fixed-q monotonicity before transferring witness theorems to new caps. Internal proof, same-assistant separately structured verification, remote CI, preserved data, external acceptance and independent reproduction remain distinct. No timeout, missing output, unsuccessful numerical search or repository publication is a proof. The canonical selected/residual bridge remains the principal correlated external-review dependency.
