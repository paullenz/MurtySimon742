# n=30 Delta=17 CI provenance note

9 September 2026.

**Status:** audit/provenance note. No mathematical claim is promoted by this file.

The first public clean-runner attempts for the n=30, Delta=17 early kernel exposed several verification/provenance issues. They are preserved here because the project policy is to record failures rather than silently erase them.

## 1. Raw-file hash was too strict

The first verifier required the committed exact-dual JSON file to have the same raw-byte SHA-256 as a freshly generated certificate file. Harmless JSON formatting differences made the byte hashes differ.

This was a provenance-check design error, not a mathematical contradiction. In the same failed workflow, the freshly regenerated 18 duals had already passed the standard-library exact checker.

## 2. Semantic certificate identity was also the wrong invariant

The next revision canonicalized JSON before hashing. This removed whitespace sensitivity but exposed a deeper point: HiGHS can propose different valid dual rays for the same infeasible source-capacity system. A fresh run therefore need not reproduce the same exact integer multiplier vector that was committed earlier.

Again, the freshly regenerated certificate set passed exact verification before the identity check failed.

Requiring ray identity would confuse **one representation of a proof certificate** with the mathematical proof event itself.

## 3. One committed certificate had stale derived metadata

After ray identity was removed, the exact checker reached the committed certificate arithmetic. It verified the multiplier sign/capacity conditions and the strict contradiction, then found that one certificate's stored `lhs`/`rhs` labels were stale from an earlier version of the same profile.

For the profile

```text
[3,3,4,4,4,4,5,5,5,5,5,5]
```

with `rmax=44`, `scale=2`, `mu=0`, and weights

```text
[1,0,0,0,0,0,0,0,0,0,0,1],
```

the exact derived values are

```text
lhs=57,
rhs=54,
margin=3,
```

not the stale displayed values `59,56,3`. The underlying weights still gave a valid exact contradiction; the failure was correctly triggered because the committed metadata did not match the recomputed arithmetic.

The complete 18-certificate file was then regenerated directly from the exact kernel rather than editing the one row by hand.

## 4. Correct proof invariant

The verifier now checks the invariants that matter mathematically:

1. regenerate the complete `t=4` charging-feasible demand domain;
2. independently apply the exact threshold/source-count cuts;
3. confirm that exactly 18 demand profiles remain;
4. confirm that the committed certificate file contains exactly one certificate for each of those 18 profiles and no others;
5. verify every committed integer dual directly against the reconstructed Hall/source-capacity inequalities;
6. recompute and check every stored `lhs`, `rhs`, and strict margin from the certificate weights.

A separately regenerated set of solver-proposed dual rays is also exact-verified, but it is **not required to be identical** to the committed set.

This replay contract is robust to solver degeneracy while remaining strict about the exact mathematical content of committed evidence.

The failed CI runs remain visible in GitHub Actions history. They should not be cited as mathematical failures; they are verifier/provenance failures that produced a stronger evidence contract.
