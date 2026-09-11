# Provenance and next steps

Paul requested continuation after the four-envelope checkpoint was published. The starting branch was verified as `d063c25445671c2588f5a619ecbc468e9698806d` in `paullenz/MurtySimon742`; the local checkout was clean. The visible conversation and the preserved predecessor handover supplied the working context. No other-chat retrieval or sub-agent was used.

## Mathematical work completed

The target was the remaining completeness premise for the 100 `Q>=18` demand profiles at `n=30,Delta=16,m=225`.

1. Re-read the earlier m226 clipping proof. Its clipping maps extend to demands zero and one; the only potentially sensitive payment case is twelve fives plus a low entry. At level three that entry contributes zero unless it is three. This is now stated explicitly and audited over all four low values.
2. Prove that at cap four, `N2<=10` gives deficit at most four and `N2<=11` gives deficit at most five. This leaves only `(p,N2)=(12,12),(13,11),(13,12),(13,13)`.
3. Derive the complete cap-four classification by two threshold counts: `4+2+18+46=70` profiles.
4. Lift fours to fives in every eligible cap-four profile. Among the 366 possible positive lifts, 30 survive, in six explicitly stated families. The interval proof uses capacity breakpoints; every accepted and rejected affine interval is printed.
5. Lift fives to sixes in each of those 30 profiles. All 225 possible lifts have score at most sixteen, while the endpoint requires at least eighteen. The maximum over each of the six families is `14,15,15,15,16,16`. Forward clipping then rules out every original demand at least six.
6. The resulting 100 profiles exactly match the old file, including scores. The old file is read only for this final optional comparison and does not participate in derivation.
7. Feed the new list into the unchanged four-envelope checker. It reproduces 211/211 tight-row contradictions with the same four formulas and minimum gap one.

The early interactive probes calculated cap-four deficit maxima, counts by `(p,N2,max demand)`, and lift maxima. All proof-relevant values from those probes are reproduced by the preserved checker and written tables. Some exploratory larger bounding boxes were also inspected (for example, allowing all `y in {12,13}`, `10<=z<=y`, `3<=k<=z` before a six-lift); they were not needed and are not proof premises. There were no solver calls, timeouts, UNSAT claims or unrecorded new theorem promotions in this continuation.

## Verification and limitations

The self-contained checker uses standard-library integer arithmetic. Direct first-fit thresholds are checked against independently implemented capacity-interval inversion and against demand-vector tail sums. The cap-four tables, cap-five table, clipping payments and six-lift maxima are explicit constants from the written argument, not loaded survivor lists. The appendix records 230 cap-five affine intervals and 131 cap-six intervals.

This is a candidate hand proof with finite arithmetic tables, not a claim that those tables need no audit. Same-assistant independent implementations remain internal corroboration. The combined endpoint replay correctly retains the downstream flag `profile_completeness_is_input=true`: completeness is supplied upstream by the new written argument, not certified by the envelope checker itself.

The earlier historical 100-profile file, four-envelope formulas, frozen reviewer packages, proof sources, previous audits, and theorem ledger are preserved. Only current navigation/status text and three predecessor checkpoint READMEs receive additive updates.

## Remaining work

- Perform an adversarial review of the assembled Delta=16 route: universal graph bridge, new classification and its printed arithmetic, tail-slack reconstruction, ledger exclusions, and all four envelopes across 211 rows.
- Look for further structural compression of the envelope arithmetic if it materially improves human auditability; do not mistake fewer computer checks for a new theorem.
- Review and simplify the separate Delta=17 finite pieces at 225 and 226 edges. The current analytic cap already excludes `m>=228`, but the full N30 assembly must account for every intermediate scope explicitly.
- Only after that assembly and its review should a new N30 reviewer edition be considered. Preserve N29 reviewer-v4 and the other current versions in every reviewer entry point.

No unrestricted general-N result or claim of novelty beyond the project's internal development follows from this finite-order classification. Independent specialist review is OPEN.
