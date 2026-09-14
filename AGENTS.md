# Research-agent standing orders

Canonical repository: `paullenz/MurtySimon742` (ID 1359206057).

Read `CANONICAL_REPOSITORY.md`, the opening status summaries in `README.md`, `CURRENT_STATE.md`, `RESEARCH_EVIDENCE_INDEX.md`, and commits newer than the recorded checkpoint before resuming. Existing package-specific instructions and audit gates remain in force.

**Every commit must update the CURRENT-STATUS blocks in BOTH README.md and CURRENT_STATE.md in the same atomic commit.** This includes documentation, code, evidence-publication and automation commits. Record the completed step, verification and limitations, and next step. When results have not changed, write **mathematical status unchanged** and describe the actual non-mathematical change. Never leave status for a later commit or fabricate progress to satisfy the check.

Keep the fixed-order and general-research summaries near the top of README.md. Preserve its protected reviewer navigation, exact evidence, failures, counterexamples, audit challenges and archived states. Do not promote samples, numerical infeasibility, queued CI or timed-out computation to proof. External review stays separate from internal checks.

**README additive-preservation rule.** The root README is a cumulative reviewer/handoff surface, not disposable status prose. Routine status refreshes, reorganisations and full-file rewrites must not delete, silently condense or replace substantive historical material. In particular, the protected `REDTEAM-HISTORY` and `REVIEW-MATERIALS` blocks, failures/corrections, hostile-audit findings, and proof-hardening consequences must remain in the root README with their meaningful detail and links. New information should be added or reconciled with existing text rather than replacing it wholesale. If material is moved to an archive for length, the root README must retain a substantive summary and direct link. Removal or material compression of such content requires explicit user instruction. Before publishing a README rewrite, diff it against current `main` specifically for dropped sections, links and audit findings. The CI guard is a backstop, not permission to remove unguarded content.

The user authorizes sensible research commits and README/handoff updates without asking again. Re-read the branch before writing, preserve concurrent work, use non-forced fast-forward publication, and verify the resulting commit/file remotely. Run `python scripts/check_status_sync.py --base HEAD --head <prepared-commit>` locally when available, or check the equivalent staged status-block changes before publication. The CI check detects omissions; it is not a mathematical validator or a guarantee of branch protection.

Keep audit 34854911792 and its promotion gate unchanged unless separately authorized. Full details: `CANONICAL_REPOSITORY.md`.
