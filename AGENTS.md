# Research-agent standing orders

Canonical repository: `paullenz/MurtySimon742` (ID 1359206057).

Read `CANONICAL_REPOSITORY.md`, the opening status summaries in `README.md`, `CURRENT_STATE.md`, `RESEARCH_EVIDENCE_INDEX.md`, and commits newer than the recorded checkpoint before resuming. Existing package-specific instructions and audit gates remain in force.

**Every commit must update the CURRENT-STATUS blocks in BOTH README.md and CURRENT_STATE.md in the same atomic commit.** This includes documentation, code, evidence-publication and automation commits. Record the completed step, verification and limitations, and next step. When results have not changed, write **mathematical status unchanged** and describe the actual non-mathematical change. Never leave status for a later commit or fabricate progress to satisfy the check.

Keep the fixed-order and general-research summaries near the top of README.md. Preserve its protected reviewer navigation, exact evidence, failures, counterexamples, audit challenges and archived states. Do not promote samples, numerical infeasibility, queued CI or timed-out computation to proof. External review stays separate from internal checks.

The user authorizes sensible research commits and README/handoff updates without asking again. Re-read the branch before writing, preserve concurrent work, use non-forced fast-forward publication, and verify the resulting commit/file remotely. Run `python scripts/check_status_sync.py --base HEAD --head <prepared-commit>` locally when available, or check the equivalent staged status-block changes before publication. The CI check detects omissions; it is not a mathematical validator or a guarantee of branch protection.

Keep audit 34854911792 and its promotion gate unchanged unless separately authorized. Full details: `CANONICAL_REPOSITORY.md`.
