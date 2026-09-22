# Residual-support hostile replay

22 September 2026. PASS. Internal bounded computation, not external proof verification or exhaustive graph enumeration.

The deterministic equality fixture suite was replayed on 1,396 graph fixtures, 2,783 maximum-root cases and 68,741 legal selected assignments. At 2,727 roots all assignments within the configured limit were exhausted; 56 roots were sampled. The population includes balanced complete bipartite graphs of both parities, prior small-graph fixtures and deterministic greedy D2C samples. These are not 1,396 isomorphism classes.

New checks: 68,741 exact core-ledger identities, 88 boundary exclusions, 980 independent-support cases (seven with nonempty F), 700 one/two-support cases (503 with nonempty F), 518 cases with 1<=r<=4 (456 with nonempty F), and 68,737 cases with S<=4. The inherited checker also verified 39,846 edge deletions by BFS.

Non-vacuity caveat: no nonempty-F independent-support fixture with three or more residual labels occurred. The general multi-center saturation theorem therefore retains a genuine unexercised branch; seven nonempty small-support instances are not evidence of exhaustive coverage. No target-density nonbipartite counterexample was found or assumed.

Exact output and physical witnesses: SUPPORT_RESULTS.json. Reproduction: python check_support.py --output SUPPORT_RESULTS.json, alongside the three inherited wrappers and raw-profile dependencies. Source SHA256: be79c5b87a94dfa385ea57864421595d2686af6a85550af14d75179a2599ce53. Fixture ledger SHA256: 74b2166c218867b5ccb6090846e813ac7cb4900f6c402817fd744bf9150e2b5b.

Highest-value next action: use the exact residual-core ledger to bound positive core demand and test the three-column extension; do not promote abstract surviving cores into actual D2C examples.
