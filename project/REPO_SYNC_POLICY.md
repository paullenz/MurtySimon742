# Repository synchronization standing order

This repository is the durable project record for the Murty–Simon / Erdős #742 work, including the frozen n=25/n=27 candidates and the general-order programme.

## Standing rule

Whenever substantive project work is carried out in ChatGPT and repository access is available, preserve the recoverable work in this repository in the same working session where practical.

Preserve, as applicable:

- new hand arguments and proof drafts;
- corrections and retractions;
- current OPEN / REPRODUCED / PROJECT_CERTIFIED status;
- scripts, parameters, solver inputs, outputs and survivor lists;
- proof certificates and replay logs;
- audit capsules and manifests;
- cryptographic hashes and environment/provenance notes;
- paper-ready theorem dependencies only after promotion under the audit policy.

A chat transcript is never sufficient preservation by itself.

## Mandatory commit-completion rule — 7 September 2026

Paul requested that future commits be completed, following the unfinished v5 publication. Treat each publication as one end-to-end task, not as a collection of successful uploads. Do not resume discretionary research while a requested publication remains unfinished.

Before writing, read the current target branch, the relevant files and the exact intended change set. Verify the local checkpoint's manifest and, for encoded storage, test recovery against every original file hash. Preserve the original evidence, historical timings and scope labels; do not turn regenerated outputs into purported historical evidence.

Complete every required step: upload content, create the complete tree, create a commit with the current parent, and update the intended branch. A contents-API write may combine these steps, but still requires the checks below. A blob SHA, tree SHA, unreferenced commit, local patch or successful upload is NOT completed publication.

Before reporting success:

1. Read back the target branch and verify that it points to the intended commit, or to a verified descendant containing the unchanged publication.
2. Inspect the committed change set. Verify all intended paths and their content hashes, including every storage part, recovery program and manifest; check key files by reading them at the committed SHA.
3. Verify the README points to the committed checkpoint and reports its exact scope, survivor counts and review status. Verify the standing-order changes when included.
4. Confirm that no unintended existing file, frozen proof or governed theorem-ledger entry was modified or deleted.
5. Save a publication receipt identifying the repository, branch, parent, commit, expected changed paths, hashes and checks actually completed. Report the verified commit identifier to Paul.

Use non-forced branch updates. If the branch advances concurrently, reread it and rebuild on the new parent without overwriting other work. Keep a recoverable local checkpoint of the publication state, including uploaded blob hashes, after each successful stage so an interruption can be resumed without guesswork.

If any step fails, retain the exact tool response and identify the last verified stage. Retry a recoverable failure using the available tools and persisted state. Never infer a loss of GitHub permission merely from incomplete tool discovery or an unfinished operation. Do not claim success until branch attachment and read-back checks pass. External outages cannot be guaranteed away; an unresolved failure must be reported explicitly as INCOMPLETE, with the actual error and recoverable files, not as a completed commit or a promise of background work.

## No silent promotion

The status hierarchy is:

`PUBLISHED / PROJECT_CERTIFIED / REPRODUCED / REPORTED_ONLY / OPEN / INADMISSIBLE`.

A lower-status result must never be imported into the theorem chain as though it were PROJECT_CERTIFIED.

Solver UNSAT without replayable proof evidence remains computational evidence only unless an independently audited hand argument replaces it.

## Open-work rule

Open material is preserved too. Failed approaches, partial enumerations, surviving cases, timeouts, unresolved proof obligations and known trust gaps belong in the repository. They should be labelled accurately rather than omitted.

## Practical limitation

Repository synchronization occurs when a ChatGPT work session is active and GitHub access is available; this file is a standing project instruction, not a background process. Commit completion and mathematical certification remain separate questions.

## Standing authorization for GitHub commits and pushes — 12 September 2026

Paul explicitly instructed: “Great - you don't need to ask my permission to commit to GitHub in future”.

This is continuing user authorization to commit and push routine Murty–Simon research, code, proofs, audit evidence, documentation and corrections to the public repository `paullenz/MurtySimon742`, including its `main` branch. Complete these updates without requesting fresh user permission for each checkpoint. Continue the existing preservation, README/link consistency, non-forced update and publication verification requirements.

If a platform approval or access-control block occurs, report the actual block and preserve the prepared work. Do not misdescribe it as missing user authorization, and do not bypass the control.
