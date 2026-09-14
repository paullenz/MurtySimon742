# Canonical repository

Current project repository: `paullenz/MurtySimon742`

GitHub repository ID: `1359206057`

This supersedes older project repository names, including `paullenz/MurtySimon25`. Legacy `N25_*` filenames are historical paths, not repository identifiers.

## Mandatory restart order

For every project restart or context recovery:

1. confirm this repository identity;
2. read [`CURRENT_STATE.md`](CURRENT_STATE.md);
3. inspect commits newer than the synchronization point recorded there;
4. reconcile any material newer result back into `CURRENT_STATE.md` before treating the handoff as current.

## Standing synchronization order

`CURRENT_STATE.md` is the mandatory live handoff surface and must be updated after any material research-state change, including:

- a canonical frontier or ledger count change;
- completion/failure of a discovery, recovery or audit gate;
- promotion, falsification or material weakening of a theorem/corollary;
- a change in the principal research attack;
- a material negative result that changes priorities;
- pausing work after a substantive research block.

A state sync must preserve the distinction between discovery, internal verification, independent implementation, external mathematical review and external reproduction. Preliminary scan output must never be promoted merely by rewriting the state file.