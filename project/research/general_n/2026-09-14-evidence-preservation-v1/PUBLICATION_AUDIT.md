# Verified evidence publication — completed 14 September 2026

**The raw evidence is now committed, not merely queued or held in a temporary download.** Publication commit `b6a15db114d7b4f3b71d73da816daec563f11824` added all 16 verified files in `durable/`. The manifest was fetched back from main and its blob matched the executed local record. Its SHA256 is `3bfacfe22427bced71574a9879102594ed9e21103c799739558e254e46526fa7`.

## Keep mathematical verification separate from the publication failure

Run `34894544147`, job `104145146205`, passed all artifact downloads, exact source/frozen-result blob checks, complete conditioned-excess replay, historical-output reconstruction and source/artifact hash checks. It then committed the generated data locally, but `git rebase origin/main` refused because the runner checkout had unstaged changes. Checkout logs separately record seven legacy ZIP/LFS pointer warnings. The exact proven failure is an unclean checkout blocking rebase; no mathematical discrepancy or hash mismatch occurred.

The job uploaded all evidence despite that publication failure: artifact `10368074968`, `conditioned-excess-sealed-evidence`, archive SHA256 `12af6eba08bf0c5b1f211afe64be881af3a138e9d9bde03eac9e9185cb4086aa`. This archive was downloaded locally, all 15 payload files checked against the manifest, and the manifest found byte-identical to the earlier local PASS record.

The old run as a whole remains FAILED and its history is preserved. Do not relabel it green merely because its mathematical step passed. Do not rerun it blindly: its computation already succeeded and the failure is reproducible publication logic, not a transient solver failure.

## Publication-only repair

Commit `ba8ad063b5dd570b7551c585bf6d88dabf5a5008` added `.github/workflows/publish-verified-conditioned-evidence.yml`. Run `34895776658`, job `104149243135`, completed SUCCESS. It reuses the already verified archive instead of rerunning mathematics. It checks the pinned manifest SHA256, every file size and SHA256, and the complete conditioned canonical JSON hash. It then creates a Git tree on the latest main, preserves existing files and concurrent history, and updates main without force. Any differing existing durable file is a blocker. All 16 resulting Git blobs are fetched and checked after publication.

The publication commit is `b6a15db114d7b4f3b71d73da816daec563f11824`, timestamp 2026-09-14 20:56:33 UTC. No audit budgets or concurrency limits were changed. No queued/running/successful audit job was retried. No candidate was promoted.

## What is durable

The committed directory includes the complete new conditioned replay and nine remaining arrays; original 713-row synthetic corpus and frozen scanner; original pilot and all 812 difficult profiles; both complete capped/block actual-expected pairs; generator totals; full before-and-after 257-job audit snapshots; and both historical capped-spill output files, reproduced byte-for-byte. The manifest records each byte count and SHA256. Earlier exploratory source and all five block-output objects were already committed in readable form.

The complete conditioned output hash remains `7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e`. Empty/full block boundaries, unsuccessful branches and non-rejections are included. The recent research checkpoint now replays offline from committed inputs without reliance on expiring Actions artifacts.

This is completion of the recent research-evidence preservation scope, not a claim of independent mathematical review of every historical manuscript. Internal verification, successful publication, external acceptance and third-party reproduction remain separate. The 2655 relational candidates remain UNPROMOTED pending their full coverage/dual agreement/zero-unresolved/aggregate/reviewed-ledger chain.
