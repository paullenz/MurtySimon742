# Local subscription-only Hall/min-cut pilot

**27 September 2026: source prepared; 30 offline tests pass; NOT deployed or running.** No paid model requests, hosting, top-ups, API integrations or schedules have been started. Financial and health alerts are untouched. The old hourly research and audit tasks remain paused.

This is a bounded operational prototype, not a promise of uninterrupted research. It runs three queued reasoning jobs: audit the Hall/min-cut proof, adversarially review it, then consolidate a reviewer package. Shell tools, browsing and multi-agent execution are disabled in this first pilot. It can propose checker code as text but cannot claim to have executed that code or assessed novelty. It does not update mathematical claims or publish to Git automatically.

## Reliability and evidence

`worker.py` provides a SQLite queue, immutable per-attempt folders, an inherited OS lock, a child process wrapper, stop/time limits, and content-hash/event validation. A supervisor crash does not cause a duplicate launch while its child holds the lock. If the child completes, the next invocation imports the receipt without repeating generation. Ambiguous interrupted work becomes `needs_attention`, not an automatic retry. Every restart rechecks saved outputs.

Empty or truncated streams, mismatched job IDs, changed artifacts, nonzero exits and missing terminal events are rejected. `saved_unreviewed` is an operational label, NOT a proof certificate. Elapsed process time is not recorded as uninterrupted reasoning time or human-equivalent hours.

`ACCEPTANCE.json` records all 30 executed offline tests in three disjoint batches, including actual process-kill, stop, timeout and lock tests. A fake Codex executable was used: no authenticated live-client compatibility, account entitlement, long-run uptime or mathematics has been certified. The worker/test Git blobs exactly match the tested SHA-256 hashes in that report. Full test logs and expanded instructions are also included in the downloadable source bundle delivered in the coordinating chat.

## No-extra-charge gate

The program has no API client, API-key fallback, credit-purchase, auto-reload, paid-hosting or GitHub workflow path. It forces ChatGPT authentication with the OpenAI provider in a dedicated Codex home; rejects API/custom-endpoint environment variables; and reads the account and rate-limit metadata before each job. It refuses API auth, paid/unknown workspaces, spendable credits, unknown credit information, reached limits or inadequate allowance headroom. It never evades usage limits with another account or service.

**ChatGPT login alone is not a billing guarantee.** Purchased credits may be used after included usage. The documented account interface does not establish the auto-reload setting. Before activation the owner must personally confirm no automatic reload, no spendable purchased credits and a personal included plan. That confirmation expires after 24 hours. Missing account/credit fields are a blocker, not zero. Do not weaken the check to make the program run. If the account cannot supply a no-charge route, leave this pilot disabled.

No computer has been provisioned, no service installed, and no model requests sent. This needs an existing computer kept running and your included Codex allowance; it cannot supply unlimited 24/7 inference. Ordinary electricity/internet and the existing subscription still apply. The Codex model need not be the model serving the ChatGPT conversation.

## Local setup (macOS/Linux, Python 3.10+, Git, current official Codex CLI)

Run from this directory. Tests need no login, network or paid service:

```sh
python3 -m unittest -v test_worker
python3 worker.py init --repo /absolute/path/to/MurtySimon742
```

Initialization reads `CURRENT_STATE.md` first and pins only the named paper sources from a Git commit. It creates private state OUTSIDE the repository, at `$HOME/.local/state/murty-hall-pilot` by default, and starts with `enabled=false`. It refuses to overwrite existing state. Sign in locally using the dedicated Codex home:

```sh
CODEX_HOME="$HOME/.local/state/murty-hall-pilot/codex-home" codex login
```

Use ChatGPT browser sign-in, never an API key. Do not paste tokens into chat or commit authentication files. Inspect the account's Usage/Billing page. Only AFTER personally confirming auto-reload is off, no purchased credits are available and the plan has included usage:

```sh
python3 worker.py acknowledge-billing --no-paid-credits-and-auto-reload-off
```

This records YOUR confirmation, not independent billing verification. Then edit the private `settings.json` and set `enabled` to `true`. Keep the safety ceilings. `model:null` uses the Codex default; a model already available within the plan may be specified. Unsupported settings must fail, not cause a paid fallback. The default requested reasoning effort is `high`.

```sh
python3 worker.py preflight
python3 worker.py run
```

Preflight reads account metadata without starting a model turn. Unknown credit/plan information means STOP. The queue is a foreground local process, not an installed daemon. On a Mac, `caffeinate -i python3 worker.py run` can keep the computer awake while the command is active. Never copy this ChatGPT login into public GitHub Actions or a cloud runner.

## Stop, inspect, recover

```sh
python3 worker.py status
python3 worker.py stop
```

A durable `STOP` flag prevents new jobs and asks the child wrapper to terminate the running process group. Partial artifacts stay preserved. To lift an intentional stop, inspect the state, remove only the `STOP` flag, and invoke `run` again. The program does not clear stops or enable itself.

For an incomplete attempt, inspect its artifacts and confirm the previous turn has ended before authorising an explicit retry:

```sh
python3 worker.py retry 01-proof-audit --previous-turn-ended
```

Old attempts remain intact. The attempt ceiling and quota guards still apply. There is no exactly-once remote-execution guarantee after every possible failure, automatic reboot handling or indefinite recovery loop.

## Local evidence is not remote backup

Attempt folders contain prompts, launch records, events, stderr, result files where available and final receipts. No automatic Git push is implemented. Never upload the entire state directory: it contains Codex authentication/session data. Review and publish only the needed reports and redacted reproducibility artifacts. Canonical mathematical claims and historical session credits remain unchanged by this pilot.

## Primary documentation checked

- https://developers.openai.com/codex/auth/
- https://developers.openai.com/codex/noninteractive/
- https://developers.openai.com/codex/app-server/
- https://developers.openai.com/codex/config-reference/
- https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
- https://help.openai.com/en/articles/12642688
- https://github.com/openai/codex/blob/67a709665ac7b50311b93e32612c9a8281684787/codex-rs/app-server-protocol/schema/typescript/v2/CreditsSnapshot.ts

The documented credit schema has `hasCredits`, `unlimited`, and nullable `balance`. Omitted credit information is not evidence of zero credits. Live protocol compatibility remains to be checked on the owner's machine without weakening the no-cost controls.
