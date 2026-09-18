# Follow-up process audit and repair - 19 September 2026

## Why this follow-up exists

The first daily red-team checkpoint, commit `03356bf3203fdc9bbd35fad97c6574eb16f3dcaa`, correctly identified a deterministic status-policy failure at its predecessor but then stated that the audit checkpoint repaired the live status schema. A hostile check of the checkpoint's own workflows showed that this statement was premature: the new checkpoint itself failed Status synchronization and also broke the N30 reviewer-package navigation validator.

This note preserves those second-order audit findings rather than silently correcting them.

## Finding 1 - status parser rejected human-readable `AUDIT`

Status synchronization run `35405621026`, job `105794668021`, failed at `Check every new commit` with:

`03356bf3203f: CURRENT_STATE.md WORK MODE must be one of MATH, ADMIN, AUDIT, STATUS, RECOVERY`

The human-readable status line was:

`**WORK MODE:** `AUDIT``

The failure was a parser/format mismatch, not an invalid mode. `scripts/check_status_sync.py` first collapses the status block to one line, then used:

`re.search(r'WORK MODE:\s*`?([A-Z]+)`?', new_current)`

The closing Markdown bold marker `**` occurs immediately after the colon, so the regex could not reach `AUDIT`.

### Repair

The parser now accepts either plain or Markdown-bold field syntax:

`WORK MODE:(?:\*\*)?\s*`?([A-Z]+)`?`

The allowed semantic values remain unchanged. This repairs presentation compatibility without weakening the mode policy.

## Finding 2 - valid README directory links tripped the frozen N30 navigation check

N30 reviewer-v3 package run `35405621004`, job `105794668117`, failed in `project/reviews/n30/2026-09-11-reviewer-v3/check_package.py` with:

`AssertionError: ('README.md', 'project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/')`

The root README link is valid GitHub navigation to an existing directory. The checker, however, required every relative Markdown link target to satisfy `Path.is_file()`.

### Repair

The navigation assertion now uses `Path.exists()`. This continues to reject broken relative targets while allowing legitimate repository-directory links. The proof table checks, pinned input hashes, release-manifest hashes, frozen N29 bridge hash, PDF existence checks, and portable ZIP checks are unchanged.

## Mathematical effect

None. These are repository/process defects. They do not strengthen or weaken any mathematical theorem.

The mathematical audit conclusion remains deliberately bounded:

- no fatal contradiction was found in the current load-bearing rooted-witness/Hall/rigid-U-witness spine;
- the newest Hall and rigid-witness calculations are internally supported but remain conditional on shared graph-theoretic premises;
- the finite source-tuple theorem remains a priority independent re-proof dependency;
- an independent graph-level regression on realizable D2C graphs remains missing;
- no global eventual second-extremal theorem is claimed.

## Additional independent hostile-control replay

The explicit `X_3` adjacency reconstructed in `PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md` was independently replayed again during this audit follow-up. It has 12 vertices, 32 edges, diameter 2, degree multiset

`[4,4,4,4,5,5,5,6,6,6,7,8]`,

and deleting each of its 32 edges destroys diameter 2. This verifies the graph property independently of the theorem packages. The documentary caveat remains: direct isomorphism to the paper is still based on the published figure rather than an author-supplied machine-readable adjacency list.

## Repository hygiene conclusion

The README's live mathematical target, current structural chain, hostile-control caveat, daily-audit reference, and programme horizon are current. The issue exposed here was not stale mathematical prose but incompatibility between valid current README navigation and an older file-only package-link assertion.

Historical Git-LFS checkout warnings for seven legacy ZIP paths were observed in workflow logs. They are recorded rather than repaired in this checkpoint because they concern preserved historical evidence and are not blocking the active mathematics.

## Next audit priorities

1. Re-prove the finite source-tuple hierarchy and integrated subset deficit statement independently from definitions.
2. Build a graph-level regression for rooted slots/Hall quantities/rigid-witness quantities on actual D2C graphs including `X_3`.
3. Keep testing the audit checkpoint itself: a repository audit is not complete until the repair commit's own status and package workflows are checked.
4. Preserve any failure as evidence; do not relabel deterministic policy or navigation failures as transient infrastructure.
