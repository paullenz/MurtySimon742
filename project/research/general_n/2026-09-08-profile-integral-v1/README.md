# Profile-integral continuation: 293/500

8 September 2026. **Complete candidate argument; internal exact computations REPRODUCED; independent mathematical review OPEN. Not PROJECT-CERTIFIED or fully formalised.**

[PROOF.md](PROOF.md) completes the previously unfinished candidate

    n>=6 and Delta(G)>=293n/500  ==>  e(G)<floor(n^2/4).

Here 293/500=0.586 exactly. For a=n-1-Delta and t=e(G)-Delta(n-Delta), the new profile bound is

    t < a^2/24+a/8.

It retains individual demands in each threshold, controls the discrete-to-integral error by a shifted midpoint argument, and uses an exact polynomial minorant. Jensen is valid but not needed. The old cubic bound and 4/81 coefficient are not dependencies. The small a=6 and a=11 cases have a 640-case integer certificate. In particular this excludes n=29, Delta=17 from the 210-edge target, but does not resolve all of n=29. K(2,3) prevents an unqualified strict n>=4 statement.

## Reproduce

Python 3.10+; standard library only, no network, optimiser or solver:

```sh
python3 -I -B src/check_profile_integral.py --output /absolute/path/to/new-results.json
```

The output path must not exist. With default limits the parsed output must equal [evidence/RESULTS.json](evidence/RESULTS.json). It checks 478,192 sorted demand profiles, 4,215,632 threshold levels, 833,250 rational midpoint cases, 640 small-certificate cases and 5,173,536 eligible degree pairs through n=5,000. The latter is an arithmetic regression, NOT a proof of all graph orders through 5,000. `EXECUTION.json` records the actual local command and environment.

[AUDIT.md](AUDIT.md) states the attacks, negative controls, simplifications and remaining trust boundaries. [MANIFEST.json](MANIFEST.json) hashes this checkpoint's payloads; publication and any clean-runner results have separate receipts. The new workflow is `.github/workflows/profile-integral.yml`.

No actual positive-surplus graph was produced. Abstract profiles need not be graph-realisable. No new Lean verification or independent researcher endorsement is claimed. The prior layer-sum manuscripts, frozen n=25/27/28 proofs, original archives and governed theorem ledger are unchanged. Paul retains specialist outreach.
