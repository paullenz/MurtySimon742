# Publication recovery procedure

Canonical repository: `paullenz/MurtySimon742` (ID 1359206057).

This procedure supplements AGENTS.md; it does not override preservation, per-commit handoff updates, audit gates, protected branches, or the two-failure circuit breaker. It concerns repository publication, not mathematical acceptance.

## Establish the current state before diagnosing a failure

Read CURRENT_STATE.md on main first, then read the main ref. Compare any pending attachment's base commit with that live head. When the result is already present, inspect the actual package and handoff and reconcile the status instead of applying an older patch over newer work. Record separately: remote publication, local attachment preservation, mathematical verification, CI status and promotion status.

Do not infer that GitHub cannot be written merely because the local environment has no GitHub CLI, a raw-file download fails, a tool is absent from an initial discovery subset, or a previous turn exposed fewer actions. These are different observations. Re-discover the connector's exact write actions once for the current session, using targeted searches for create_tree and update_ref (and create_file/update_file for the bounded fallback). Tool discovery is not a successful write or proof of permission; only an actual action establishes that route's result. Do not claim a permanent platform repair from one successful transaction.

## Preferred atomic publication

1. Read the current main ref and its commit's tree. Build on that exact base tree; never omit base_tree while replacing the repository state.
2. Include the research or administrative artifacts and the CURRENT_STATE status update in the same new tree. Preserve an old handoff by reusing its verified blob SHA when required. Keep unrelated existing paths untouched.
3. Create a commit whose parent is the inspected head. Re-read main before moving the ref. If another writer advanced it, reconcile their changes and rebuild on the new head; never force-push or overwrite concurrent work.
4. Move main with force=false. A created blob, tree or unattached commit does not mean main has been updated.
5. Confirm the remote ref and the resulting handoff once. Report the exact commit and which files were published. A comparison of changed paths can additionally confirm the intended scope. Do not claim fresh CI success or a fresh proof replay unless they were actually observed/performed.

The connector performs this route without requiring a local clone, local CLI, or direct raw-file network access. The route is usable only while its actions are exposed and authorized.

## Bounded fallback, not a retry spiral

If atomic write actions are not exposed but update_file is available, an existing CURRENT_STATE-only checkpoint can still be published using its freshly read blob SHA. For an unpublished small research unit, that one-file checkpoint may include the complete literal result in a clearly delimited preserved-work appendix and a precise statement of which separate artifacts remain pending. This is a fallback preservation format, not permission to claim a multi-file package was published. Avoid leaking secrets or personal data into a public repository.

Do not publish a sequence of incomplete active-line commits merely because create_file is available: AGENTS.md still requires the live handoff to change with every active-line commit. Use an existing safe branch/atomic route only as supported by the actual tools and repository rules. Never bypass a permission denial or branch protection.

After one recoverable preservation failure, make at most one sensible fallback attempt. After two consecutive preservation failures, stop retries and provide a verified local bundle plus a precise blocked handoff where possible. Distinguish ACTION_NOT_EXPOSED, PERMISSION_DENIED, NON_FAST_FORWARD, NETWORK_FAILURE and REMOTE_CONFIRMATION_FAILED; do not guess a deeper cause or request broad permissions without evidence.

## Durable receipt

Record the inspected head, published commit once known, predecessor handoff blob, affected paths, verification actually performed, remaining blockers and unchanged mathematical trust boundary. When a preceding published result resolves an earlier unpublished report, explicitly say it was found already published rather than claiming to have uploaded it anew. Keep historical attachments identifiable by checksums; a checksum record alone is not an upload of those attachment bytes.

Official API references: https://docs.github.com/en/rest/git/trees ; https://docs.github.com/en/rest/git/commits ; https://docs.github.com/en/rest/git/refs ; https://docs.github.com/en/rest/repos/contents . The create-tree API's base_tree preserves unchanged entries; a non-forced ref update requires fast-forward ancestry. Existing branch protections and permissions still apply.
