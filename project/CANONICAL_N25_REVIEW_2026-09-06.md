> **Later update — 6 September 2026:** A [complete N=25 candidate proof and full-chain audit](reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md) now covers both the 156-edge upper bound and equality exactly for K_{12,13}. The new [reconciliation](reviews/n25/2026-09-06-full-chain-candidate-v1/RECONCILIATION.md) explains the published reduction, replacement Delta=15/16 arguments and complete equality checks. This is an internally reviewed candidate with reproduced arithmetic; external mathematical review remains outstanding and the governed theorem ledger is not promoted. The earlier review below is retained verbatim as historical evidence.

# N=25 canonical review and external-audit backlog

**Date:** 6 September 2026  
**Repository:** `paullenz/MurtySimon25`  
**Reviewed baseline:** `0269ebd5d80beb4be8a9d395352371cc51e1a64d`  
**Overall result:** N=25 is not yet proved by this project. The existing project ledger reduces the remaining mathematical frontier to Delta=14, but the repository is not yet a self-contained external-audit package.

## 1. Canonical coordination and scope

The user has designated the chat opened with “make this now the canonical chat for N=25” on 6 September 2026 as the canonical coordination chat. GitHub remains the durable record. This review is the consolidation baseline; later results must be merged with dates, evidence, corrections and explicit status changes rather than replacing history silently.

All 19 tracked files at the baseline commit were read, together with the branch and release listings. Available cross-chat summaries were reconciled with them. The original missing PDF/DOCX/ZIP files and complete historical transcripts were not available for fresh inspection here. This is therefore a repository/content/dependency review, **not a fresh replay of all historical computations or independent peer review**. No new branch elimination is claimed.

The existing `repro-v1/ledger/theorem_ledger.json` remains the mathematical-status record. This review and `CANONICAL_TASKS.json` record the consolidated backlog and missing evidence. A project-certified mathematical claim, a fully replayed certificate corpus, repository availability and external acceptance are separate facts.

## 2. Executive findings

The main preservation gap is real: the repository records completed work more extensively than it contains the evidence for that work. At the baseline it contains 19 text/code files, four standalone hand-proof notes, no proof archives or paper binaries, no test directory and no generators or solver/checker sources. There is only `main`, and there are no GitHub Releases. The configured Git LFS patterns do not themselves supply any evidence bytes.

The existing current-artifact manifest lists 15 missing binary files; the historical-audit manifest lists another eight. All 23 must be recovered or explicitly accounted for. Their retained hashes are useful provenance, but do not make their contents available.

The Delta=15 row cites only `evidence/reports/erdos_742_n25_audited_reductions_v5_2026-09-06.pdf`, which is absent. There is no standalone Delta=15 proof, branch-by-branch closure record, certification source or certificate corpus in the inspected tree. The upload manifest names no Delta=15-specific package. Earlier chat summaries report a final Audit v4, deterministic verifier and verifier output, but the current historical manifest does not list v4. Recovering that chain is a **P0 preservation task**, not an instruction to assume Delta=15 is mathematically open again.

The fast reproduction entry point is currently broken: it calls missing modules. A local copy of `reproduce_all.sh` was checked against its exact Git blob SHA and run; it exits with code 2 because `scripts/verify_artifacts.py` is absent. This was a local reconstruction check, not a clean clone or mathematical replay. `verify_ledger.py` also imports an absent `ledger/paper_import_manifest.json`.

## 3. Consolidated mathematical status

### Global branches

| Branch | Existing project position | External-audit work still needed |
|---|---|---|
| Exact 157-edge reduction and admissible maximum degrees | Imported into current project baseline | Recover complete proof and exact published inputs. Do not assume deleting edges preserves diameter-criticality. |
| Delta=13 | Earlier summaries report eliminated | Add the actual proof and a ledger entry; neither is in the baseline tree. |
| Delta=17 | PROJECT_CERTIFIED; hand proof present | Preserve all complement-reduction dependencies. The cited primary Theorem 3.6(a) and its integer application were checked in this review. |
| Delta=16 | PROJECT_CERTIFIED; hand proof present | Supply standalone shared lemmas and explicit elementary exclusions of all other k. |
| Delta=15 | PROJECT_CERTIFIED for all k in the existing ledger; prior summaries describe k=0 through 6 closed | Recover, map and replay/review the entire Delta=15 proof and certification chain. The repository does not yet independently substantiate it. |
| Delta=14 | Sole remaining branch under the project baseline | Resolve the genuine mathematical gaps and complete certification/preservation for the other subcases. |

The Delta=17 source is Haynes, Henning, van der Merwe and Yeo, *A maximum degree theorem for diameter-2-critical graphs*, Theorem 3.6(a), p. 1885, DOI `10.2478/s11533-014-0449-3`. Its minimum-degree formulation applies at order 25 with complement minimum degree seven. This check does not reprove every imported complement reduction.

### Delta=14 branch ledger

Here `k` means the minimum degree of `C=H[A]`, not a degree parameter of the original graph. The recorded setup has `|A|=10`, `|B|=14`, `e(C)+r=42` and `e(F)=r+3`.

| k / subcase | Governing baseline status | Remaining task |
|---|---|---|
| k=8, r=1..2 | PROJECT_CERTIFIED | Recover standalone proof or exact source section; audit shared dependencies. |
| k=7, r=2..7 | PROJECT_CERTIFIED | Recover hand base case and all certificate packages; external maintained-checker replay. |
| k=6, r=3..12 | REPRODUCED | Complete proof evidence for every terminal screening exclusion; independent coverage/replay. This is computational closure, not current certificate closure. |
| k=5, r=4..8 | REPORTED_ONLY | Recover and audit the claimed eliminations, or reconstruct them. |
| k=5, r=9 and r=12..17 | REPRODUCED | Complete certification, including screening exclusions and independent catalogue verification. |
| k=5, r=10..11 | OPEN | Mathematical elimination first. |
| k=4, r=20..22 | PROJECT_CERTIFIED | Recover dense-band proof and capsule; do not generalize to all k=4. |
| k=4, r=5..19 | OPEN | Mathematical elimination. |
| k=3, r=6..27 | OPEN | Mathematical elimination. |
| k=2, profiles 8+2 and 8+1+1 | PROJECT_CERTIFIED | Recover and verify capsule and complete profile coverage. |
| k=2, connected, r=7..16 and r=27..32 | PROJECT_CERTIFIED | Recover hand/arithmetic evidence and complete coverage. |
| k=2, connected, r=17..26 | REPRODUCED in GitHub | Reconcile later reported certificate completion as described below; do not silently promote. |
| k=2, profile 9+1, r=7 | PROJECT_CERTIFIED | Recover proof. |
| k=2, profile 9+1, r=8..28 | OPEN | Genuine remaining mathematical family. |
| k=2, profile 9+1, r=29..32 | INADMISSIBLE | Preserve the parameter-bound proof. |
| k=1, r=8..37 | PROJECT_CERTIFIED; hand proof present | Audit residual-component/residual-label dependencies and recover optional arithmetic companion. |
| k=0, r=9..42 | PROJECT_CERTIFIED; hand proof present | Audit quasi-edge and residual-component dependencies. |

### Later work not yet integrated

Recovered chat summaries report k=7 completion at 80/80 certificates, 9,437,852 checked RUP additions and byte-for-byte regeneration of all 80 CNFs, with maintained third-party DRAT/LRAT replay still requested. These are historical reported audit results, not computations repeated in this review.

For connected k=2, r=17..26, one recovered checkpoint reports 339/578 internally LRAT-certified leaves and a later summary reports 578/578 completion. Preserve the later claim as pending reconciliation, not as an instruction to restart 239 old leaves. Obtain the final per-leaf/cube manifest, exact CNFs, proof traces and replay logs. Verify original-formula linkage, assumption discharge and exhaustive cube coverage, then perform maintained external replay and encoding review. The old k=2 capsule must not be assumed to contain certificates produced later.

## 4. Delta=15 recovery and acceptance checklist

Build a dedicated Delta=15 dossier with a separate entry for each k=0..6 and every admissible residual range. Each entry must state the theorem, exact case coverage, method, dependencies and the actual evidence that closes it.

Recover the hand proofs, finite arithmetic verifiers, all graph/core catalogues and their generators, model/CNF generators, semantic checkers, solver inputs and outputs, any proof traces, replay tools/logs, environment and build information, exact commands and hashes. Preserve proof-producing-verifier development as well as the final code so changes in the model can be audited.

Classify evidence by what it actually is. A hand argument does not need an invented SAT certificate. A solver-only rejection needs a valid proof or a replacement argument before it is a certified terminal exclusion. A small arithmetic script does not verify all of the mathematical reduction. Do not presume that DRAT or LRAT certificates were generated merely because earlier work was called certified.

Recover the v4 final paper, deterministic verifier and its recorded output, then connect these to v5 and the corrected theorem chain. Preserve earlier comprehensive/fresh audits and correction notes. In particular, the rejected inactive-supplement shortcut must not re-enter the accepted verifier; recover its counterexample/regression test and map any affected historical computations.

Exact original Delta=15 package names and hashes were not recovered in this review. They are explicit discovery tasks, not blanks to fill by guessing. Missing original work can be reconstructed, but a reconstruction needs a new date and provenance rather than being passed off as the original evidence.

## 5. Repository repairs and artifact placement

The following modules named by the current runner are missing:

```text
repro-v1/scripts/verify_artifacts.py
repro-v1/scripts/verify_zip_integrity.py
repro-v1/scripts/run_k2_fast.py
repro-v1/scripts/run_k4_fast.py
repro-v1/scripts/verify_k2_job_manifest.py
repro-v1/scripts/verify_external.py
repro-v1/scripts/check_full_dependencies.py
```

Also missing are `repro-v1/tests/test_ledger_negative.py`, `repro-v1/ledger/paper_import_manifest.json`, `repro-v1/ledger/artifacts.lock.json`, `repro-v1/proof_migration/`, the paper source/rendered files and the referenced dense-k4 hand proof. The current obligations JSON has only six entries and omits multiple recovery, base-proof and open-k5 obligations.

The detailed recovery manifest lists all 23 known missing binaries with their existing SHA-256 values and proposed destinations. Keep the original release ZIP immutable, but also restore its browsable sources. Reconcile the checkpoint path: the runner requires `repro-v1/external/delta14_full_checkpoint_2026-09-06.zip`, whereas generic upload instructions suggest putting ZIPs in `evidence/archives/`. Every path must resolve deliberately, not by relying on an auditor to guess.

Standalone hand proofs and shared lemmas should be browsable text. Keep original audit PDFs/DOCX alongside their source/provenance, and store large certificates as actual available LFS objects or durable hash-pinned external artifacts. A hash, an LFS configuration or a dead chat download is not an available proof package.

## 6. Complete canonical task register

`CANONICAL_TASKS.json` contains 40 stable task IDs, priorities, acceptance conditions and dependencies. P0 denotes preservation/foundational/readiness blockers; P1 denotes mathematics, certification and integration; P2 denotes external review and release. Some work can proceed in parallel after its dependencies are met.

| Task IDs | Required work |
|---|---|
| REC-01..04 | Recover Delta=15/v4, all 23 known binaries, the latest k=2 certificates and all other material chat-only work. |
| BASE-01..04 | Fix theorem scope; substantiate the exact-edge and degree reductions; publish shared lemmas; prove exhaustive k/r/profile coverage. |
| M14-K2 | Solve 9+1, r=8..28. |
| M14-K3 | Solve r=6..27. |
| M14-K4 | Solve r=5..19. |
| M14-K5-LOW | Recover/audit or reconstruct r=4..8. |
| M14-K5-MID | Solve r=10..11. |
| C15 | Audit all Delta=15 branch closures against the recovered evidence. |
| C14-K2 | Reconcile and independently replay the complete 578-leaf certificate corpus and cube coverage. |
| C14-K6 | Close every screening-stage proof gap. |
| C14-K5 | Certify r=9 and r=12..17 and verify independent catalogues. |
| C14-K7 | Recover/review all 80 certificates and run maintained external replay. |
| C14-HAND, C16-17 | Audit present and missing hand-proof dependencies, bounds and arithmetic. |
| ENC-01..02 | Prove graph-to-model soundness; test all constraints and quarantine invalid shortcuts. |
| CAT-01, LEAF-01 | Prove enumeration/symmetry completeness and account for every terminal exclusion. |
| RUN-01..06 | Restore dependencies/manifests; pin environment; provide explicit fast/full/replay commands; negative tests; clean-clone checks and CI. |
| LEDGER-01..02 | Separate mathematical status, available bytes, internal replay and external review; expand obligations and synchronize status documents. |
| PAPER-01..03 | Restore canonical editable manuscript; map theorem dependencies; verify equality-classification scope. |
| LIT-01 | Verify current literature, novelty claims, precise attribution and theorem hypotheses before submission. |
| EXT-01..02 | Independent mathematical review and independent clean-environment computational reproduction. |
| REL-01..02 | Freeze a complete durable release; verify auditor access, licensing, authorship and tool notices. |

### Acceptance conditions that must not be skipped

**Encoding.** Every genuine counterexample must produce a permitted encoded instance. Audit exact selected/residual separation, injective missing-B assignments, full quasi-edge domination, minimum degree, diameter two, exact k/r constraints, cardinality encodings and symmetry restrictions. UNSAT in a sound necessary-condition model can eliminate a branch; SAT in that relaxation is not automatically a counterexample.

**Coverage.** Independently rebuild or check the core catalogue, case partition, label canonicalization and terminal leaf manifest. Preserve all timeouts, interruptions, empty cases, duplicates and survivors. Every terminal screen needs a valid mathematical justification or replayable certificate. Exact LP/MILP certification is required only for such methods actually used terminally; alternatively remove or replace that terminal rule.

**Replay.** Verify the original CNF identity as well as the proof. Cube-and-conquer requires proof that the cubes cover the parent problem and proper treatment of assumptions. A maintained independent checker is distinct from an internally written second checker. Formally checked LRAT is a strong target, not a substitute for the graph-to-encoding proof or a universal requirement for every hand argument.

**Runner.** The current `--full` command explicitly omits full proof replay. Supply and test the separate replay command before describing a full proof audit. Missing files, corrupt/truncated certificates, absent contradiction, wrong formula, skipped leaves, bad cubes and unknown statuses must fail safely. Lightweight CI success must not be advertised as a completed theorem proof.

**Theorem scope.** Excluding 157-edge counterexamples alone does not automatically classify all 156-edge equality cases. Determine whether earlier arguments already establish uniqueness of `K12,13`; otherwise prove it separately or accurately restrict the paper's claim.

## 7. Order of work

First recover Delta=15/v4 and the full current reproducibility/certificate bundles, while freezing the present conservative ledger and source inventory. Next repair the checkout, establish the common reduction and restore case-level manifests. Then complete k=6, the reproduced k=5 bands and the later k=2 certification, while attacking genuinely open Delta=14 families. Finally integrate the manuscript against the proven dependency graph, obtain independent mathematical and computational review, and freeze an accessible release.

The repo may remain private while authorized auditors review it. This consolidation does not change visibility, invite reviewers or run a background process. External audit of a partial result can begin before all open mathematics is finished, provided the scope is labelled accurately.

## 8. Sources and provenance

Repository facts use the pinned baseline commit above, especially `README.md`, `repro-v1/ledger/theorem_ledger.json`, `proof_obligations.json`, the two entry scripts, four hand proofs, both hash manifests and the audit/readme/preservation documents. Source inventory records all 19 path/blob-SHA pairs. GitHub branch/release listings were checked in the same review session.

Historical counts and later completion reports are explicitly attributed to recovered cross-chat summaries; their original artifacts remain recovery obligations. Primary-source check for Delta=17: https://d-nb.info/1372516379/34 (Theorem 3.6(a), p.1885). Proof-checking reference: Cruz-Filipe et al., *Efficient Certified RAT Verification*, https://arxiv.org/abs/1612.02353. Neither reference certifies the project's missing computation.
